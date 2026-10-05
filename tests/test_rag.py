import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from rag_fixture import git, make_library
from rag import RagService, encode

ROOT = Path(__file__).resolve().parents[1]


class RagTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.library = make_library(self.root)
        self.service = RagService(self.root)

    def test_nested_capability_survives_weak_repository_summary(self):
        result = self.service.recommend('resume interrupted checkpoints', lexical_only=True)
        self.assertIn('platform', [c['id'] for c in result['candidates']])
        self.assertEqual(len(result['candidates']), len({c['id'] for c in result['candidates']}))
        self.assertIn('recovery', [c['id'] for c in result['candidates']])
        platform = next(c for c in result['candidates'] if c['id'] == 'platform')
        capabilities = [s for s in result['sources'] if s['source_id'] in platform['evidence'] and s['kind'] == 'skill']
        self.assertEqual(len([s for s in capabilities if s['name'] == 'durable-execution']), 1)

    def test_service_expands_tilde_root_before_resolving(self):
        root = '~/' + os.path.relpath(self.root, Path.home())
        service = RagService(root)
        self.assertEqual(service.library.root, self.root)
        result = service.search('checkpoints', repo_id='recovery', lexical_only=True)
        self.assertTrue(result['results'])

    def test_git_verification_failures_preserve_unverified_evidence(self):
        original_run = subprocess.run
        for command in ('rev-parse', 'show'):
            for error in (FileNotFoundError('git unavailable'), subprocess.TimeoutExpired('git', 10)):
                def fail_verification(args, **kwargs):
                    if command in args:
                        raise error
                    return original_run(args, **kwargs)
                with self.subTest(command=command, error=type(error).__name__), \
                        patch('rag_sources.subprocess.run', side_effect=fail_verification):
                    result = self.service.search('checkpoints', repo_id='recovery', kind='skill', lexical_only=True)
                    source = result['sources'][0]
                    self.assertIn('checkpoints', source['text'])
                    self.assertEqual(source['provenance']['status'], 'unversioned')
                    self.assertIsNone(source['url'])

    def test_evidence_is_exact_source_text_with_verified_commit_link(self):
        result = self.service.search('checkpoints', repo_id='platform', kind='skill', lexical_only=True)
        source = result['sources'][0]
        self.assertEqual(source['provenance']['status'], 'verified')
        self.assertIn('/blob/' + source['provenance']['recorded_revision'] + '/', source['url'])
        text = self.library.read('platform', source['path'])
        start, end = source['lines']
        self.assertIn(source['text'], '\n'.join(text.splitlines()[start-1:end]))
        self.assertEqual(result['retrieval']['mode'], 'lexical')

    def test_changed_source_never_gets_verified_citation(self):
        path = self.root / 'repos/platform/skills/main/SKILL.md'
        path.write_text('Completely changed since indexing.\n')
        result = self.service.search('checkpoints', repo_id='platform', kind='skill', lexical_only=True, limit=20, budget=64000)
        source = next(s for s in result['sources'] if s['path'] == 'skills/main/SKILL.md')
        self.assertEqual(source['provenance']['status'], 'index-mismatch')
        self.assertIsNone(source['url'])

    def test_checkout_revision_mismatch_is_visible(self):
        repo = self.root / 'repos/recovery'
        git(repo, '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid',
            'commit', '--allow-empty', '-qm', 'New revision')
        result = self.service.search('checkpoints', repo_id='recovery', kind='skill', lexical_only=True)
        self.assertEqual(result['sources'][0]['provenance']['status'], 'revision-mismatch')
        self.assertIsNone(result['sources'][0]['url'])

    def test_assume_unchanged_does_not_verify_text_absent_from_commit(self):
        repo = self.root/'repos/platform'
        git(repo, 'update-index', '--assume-unchanged', 'skills/main/SKILL.md')
        (repo/'skills/main/SKILL.md').write_text('# Invented\nNoveluncommitted checkpoints functionality.\n')
        self.library.index(lexical=True)
        result = self.service.search('noveluncommitted', repo_id='platform', lexical_only=True)
        self.assertEqual(result['sources'][0]['provenance']['status'], 'modified')
        self.assertIsNone(result['sources'][0]['url'])

    def test_provider_copies_cannot_hide_weak_summary_alternative(self):
        rows = json.loads(self.library.manifest.read_text())
        rows['tools'][1]['description'] = 'General development collection'
        self.library.manifest.write_text(json.dumps(rows))
        (self.root/'repos/recovery/README.md').write_text('# Overview\nGeneral development collection\n')
        repo = self.root/'repos/platform'
        body = (repo/'skills/main/SKILL.md').read_text()
        for i in range(90):
            path = repo/f'copy-{i}/SKILL.md'
            path.parent.mkdir()
            path.write_text(body + f'\nProvider {i}.\n')
        git(repo, 'add', '.')
        self.library.index(lexical=True)
        result = self.service.recommend('resume interrupted checkpoints', lexical_only=True, budget=64000)
        self.assertIn('recovery', [c['id'] for c in result['candidates']])

    def test_profile_is_context_without_hiding_alternatives_or_writing(self):
        project = self.root / 'project'; project.mkdir()
        profile = project / '.ai-toolkit.json'
        content = json.dumps({'tools': ['colors'], 'root': '/not/the/library', 'notes': 'preserve'})
        profile.write_text(content)
        result = self.service.recommend('checkpoints', project=str(project), constraints='Python; local execution', lexical_only=True)
        self.assertEqual(result['project']['selected_tools'], ['colors'])
        self.assertEqual(result['constraints'], 'Python; local execution')
        self.assertIn('recovery', [c['id'] for c in result['candidates']])
        self.assertEqual(profile.read_text(), content)

    def test_malformed_profile_fails_clearly(self):
        project = self.root / 'project'; project.mkdir()
        (project / '.ai-toolkit.json').write_text('{"tools":"platform"}')
        with self.assertRaisesRegex(ValueError, 'profile'):
            self.service.recommend('checkpoints', project=str(project))

    def test_project_context_rejects_symlinks_without_reading_external_preferences(self):
        project = self.root / 'project'
        project.mkdir()
        outside = self.root / 'outside-profile.json'
        outside.write_text('{"tools": ["private-tool"]}')
        profile = project / '.ai-toolkit.json'
        profile.symlink_to(outside)
        for target_exists in (True, False):
            with self.subTest(target_exists=target_exists), self.assertRaises(ValueError):
                self.service.recommend('checkpoints', project=str(project), lexical_only=True)
            outside.unlink(missing_ok=True)

    def test_relative_catalog_paths_have_verified_provenance_from_another_directory(self):
        manifest = json.loads(self.library.manifest.read_text())
        for entry in manifest['tools']:
            source = Path(entry['path'])
            entry['path'] = str(source.relative_to(self.root) if source.is_absolute() else source)
        self.library.manifest.write_text(json.dumps(manifest))
        self.library.index(lexical=True)
        result = self.service.search('checkpoints', repo_id='recovery', kind='skill', lexical_only=True)
        self.assertEqual(result['sources'][0]['provenance']['status'], 'verified')
        self.assertTrue(result['sources'][0]['url'])

    def test_recommendation_reports_local_source_availability(self):
        result = self.service.recommend('checkpoints', lexical_only=True)
        self.assertTrue(result['candidates'])
        self.assertTrue(all(row['availability'] == 'source-only' for row in result['candidates']))

    def test_recommendation_rejects_catalog_paths_outside_root(self):
        manifest = json.loads(self.library.manifest.read_text())
        manifest['tools'][0]['path'] = '../outside'
        self.library.manifest.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, 'inside the toolkit root'):
            self.service.recommend('checkpoints', lexical_only=True)

    def test_budget_preserves_complete_references(self):
        result = self.service.recommend('checkpoints', lexical_only=True, budget=2500)
        self.assertLessEqual(len(encode(result)), 2500)
        self.assertTrue(result['truncated'])
        source_ids = {s['source_id'] for s in result['sources']}
        referenced = {sid for c in result['candidates'] for sid in c['evidence']}
        self.assertEqual(referenced, source_ids)
        self.assertTrue(all(c['evidence'] for c in result['candidates']))

    def test_default_budget_keeps_useful_result_with_large_setup_metadata(self):
        rows = json.loads(self.library.manifest.read_text())
        for entry in rows['tools']:
            entry['agent_setup']['configure'] = 'Long installation guidance. ' * 150
            entry['requirements'] = ['A required dependency with platform details. ' * 25] * 3
        self.library.manifest.write_text(json.dumps(rows))
        self.library.index(lexical=True)
        result = self.service.recommend('checkpoints', lexical_only=True)
        self.assertTrue(result['candidates'])
        self.assertLessEqual(len(encode(result)), 8000)
        self.assertTrue(result['truncated'])

    def test_catalog_metadata_has_manifest_pointer(self):
        result = self.service.recommend('checkpoints', lexical_only=True, budget=64000)
        sources = [s for s in result['sources'] if s['kind'] == 'repo']
        self.assertTrue(sources)
        self.assertTrue(all(s['path'] == 'manifest.json' and s['json_pointer'].startswith('/tools/') for s in sources))
        self.assertTrue(all(s['lines'] is None for s in sources))

    def test_catalog_citation_contains_reviewed_fields_without_derived_availability(self):
        result = self.service.recommend('checkpoints', lexical_only=True, budget=64000)
        source = next(s for s in result['sources'] if s['kind'] == 'repo' and s['repo_id'] == 'recovery')
        self.assertEqual(json.loads(source['text']), {
            'id': 'recovery', 'repo': 'demo/recovery',
            'description': 'Checkpoints and recovery for interrupted jobs',
            'requirements': ['Python 3.12'],
        })
        candidate = next(row for row in result['candidates'] if row['id'] == 'recovery')
        self.assertEqual(candidate['availability'], 'source-only')

    def test_empty_results_still_report_fallback(self):
        result = self.service.search('unfindablezxq')
        self.assertEqual(result['results'], [])
        self.assertEqual(result['retrieval']['mode'], 'lexical-fallback')
        self.assertTrue(result['retrieval']['fallback_reason'])

    def test_filters_and_invalid_arguments(self):
        result = self.service.search('checkpoints', kind='skill', repo_id='recovery', lexical_only=True)
        self.assertTrue(result['results'])
        self.assertTrue(all(s['repo_id'] == 'recovery' and s['kind'] == 'skill' for s in result['sources']))
        for options in ({'query': ''}, {'query': ' * '}, {'query': 'checkpoints', 'limit': 0},
                        {'query': 'checkpoints', 'budget': 5}, {'query': 'checkpoints', 'kind': 'unknown'}):
            with self.subTest(options=options), self.assertRaises(ValueError):
                self.service.search(**options)

    def test_missing_or_stale_index_does_not_trigger_write(self):
        manifest = self.root / 'manifest.json'
        manifest.write_text(manifest.read_text() + '\n')
        with self.assertRaisesRegex(RuntimeError, 'index'):
            self.service.search('checkpoints')
        self.library.db.unlink()
        with self.assertRaisesRegex(RuntimeError, 'index'):
            self.service.search('checkpoints')
        self.assertFalse(self.library.db.exists())

    def test_same_service_observes_rebuilt_index(self):
        before = self.service.search('watermelons', lexical_only=True)
        self.assertEqual(before['results'], [])
        path = self.root / 'repos/recovery/skills/main/SKILL.md'
        path.write_text('# Fruit\nWatermelons uniquely describe this capability.\n')
        self.library.index(lexical=True)
        after = self.service.search('watermelons', lexical_only=True)
        self.assertTrue(after['results'])
        self.assertNotEqual(before['index'], after['index'])

    def test_partial_vector_index_reports_fallback(self):
        import sqlite3
        from array import array
        class Model:
            fingerprint = 'test'
            def embed_query(self, query):
                raise AssertionError('Incomplete indexes must fall back before query embedding')
        with sqlite3.connect(self.library.db) as db:
            db.execute("INSERT INTO metadata VALUES ('embedding_fingerprint','test')")
            uid = db.execute('SELECT uid FROM units LIMIT 1').fetchone()[0]
            db.execute('INSERT INTO unit_vectors VALUES (?,?)', (uid, array('f', [1, 0]).tobytes()))
        with patch('hybrid.local_embedder', return_value=Model()):
            result = self.service.search('checkpoints')
        self.assertEqual(result['retrieval']['mode'], 'lexical-fallback')
        self.assertIn('coverage', result['retrieval']['fallback_reason'].lower())

    def test_cached_model_is_reused_but_changed_files_force_revalidation(self):
        from embeddings import MODEL_HASHES, MODEL_RELATIVE_PATH
        folder = self.root/MODEL_RELATIVE_PATH
        folder.mkdir(parents=True)
        for name in MODEL_HASHES:
            (folder/name).write_text('fixture')
        with patch('hybrid.local_embedder', side_effect=[object(), RuntimeError('checksum mismatch')]) as factory:
            first = self.service._model()
            self.assertIs(self.service._model(), first)
            (folder/'config.json').write_text('changed model file')
            with self.assertRaisesRegex(RuntimeError, 'checksum'):
                self.service._model()
            self.assertEqual(factory.call_count, 2)

    def test_source_pages_round_trip_unicode_and_escape_heavy_text(self):
        path = self.root / 'repos/recovery/README.md'
        original = '\n"\\☃\t' * 900
        path.write_text(original)
        pieces = []; offset = 0
        while True:
            result = self.service.read_source('recovery', 'README.md', offset=offset, budget=1200)
            self.assertLessEqual(len(encode(result)), 1200)
            pieces.append(result['text'])
            if result['next_offset'] is None:
                break
            self.assertGreater(result['next_offset'], offset)
            offset = result['next_offset']
        self.assertEqual(''.join(pieces), original)
        with self.assertRaises(ValueError):
            self.service.read_source('recovery', '../../manifest.json')

    def test_get_tool_metadata_has_lossless_continuation(self):
        parts = []; offset = 0
        while True:
            page = self.service.get_tool('platform', budget=1024, offset=offset)
            parts.append(page['text'])
            self.assertLessEqual(len(encode(page)), 1024)
            if page['next_offset'] is None:
                break
            offset = page['next_offset']
        metadata = json.loads(''.join(parts))
        self.assertEqual(metadata['requirements'], ['Python 3.12'])
        self.assertEqual(metadata['agent_setup']['action'], 'setup-required')

    def test_cli_uses_same_evidence_contract(self):
        proc = subprocess.run([sys.executable, str(ROOT / 'toolkit.py'), '--root', str(self.root),
                               'recommend', 'checkpoints', '--lexical'], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(json.loads(proc.stdout), self.service.recommend('checkpoints', lexical_only=True))


class RagPortabilityTests(unittest.TestCase):
    def test_quoted_home_directory_root_matches_library_resolution(self):
        self.assertEqual(RagService('~').library.root, Path.home().resolve())

    def test_relative_sources_work_from_an_unrelated_directory(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / 'toolkit with spaces'
            root.mkdir()
            make_library(root)
            service = RagService(root)
            result = service.search('Persist checkpoints', repo_id='platform', kind='skill', lexical_only=True, budget=16000)
            self.assertTrue(result['sources'])
            self.assertTrue(all(s['provenance']['status'] == 'verified' for s in result['sources']))
            self.assertTrue(all(r['availability'] == 'source-only' for r in result['results']))
            catalog = service.search('checkpoints', kind='repo', lexical_only=True, budget=16000)
            for source in catalog['sources']:
                evidence = json.loads(source['text'])
                raw = json.loads((root/'manifest.json').read_text())['tools']
                entry = next(e for e in raw if e['id'] == source['repo_id'])
                self.assertTrue(all(entry[k] == v for k, v in evidence.items()))

    def test_missing_downloads_report_current_host_availability(self):
        import shutil
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            make_library(root)
            shutil.rmtree(root/'repos/platform')
            result = RagService(root).search('General development collection', repo_id='platform', kind='repo', lexical_only=True)
            self.assertEqual(result['results'][0]['availability'], 'source-missing')

if __name__ == '__main__':
    unittest.main()
