import copy
import json
from pathlib import Path
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from scripts import catalog_pr


def entry(ident='new-tool'):
    return {
        'id': ident, 'repo': 'example/' + ident,
        'url': 'https://github.com/example/' + ident, 'commit': 'a' * 40,
        'description': 'A reviewed tool.', 'kind': 'cli',
        'path': 'repos/example--' + ident, 'tags': ['development'],
        'requirements': ['Python'], 'entrypoints': ['README.md'],
        'skill_paths': [], 'recommended_scope': 'project-local',
        'rationale': 'Useful for project work.', 'install_commands': [],
        'setup_scope': 'project-local',
        'agent_setup': {'source_revision': 'a' * 40, 'read_first': ['Read README.md'],
                        'install': 'Use an isolated runtime.', 'verify': 'Run help.'},
    }


class CatalogPRTests(unittest.TestCase):
    def test_only_new_entries_are_selected_without_copying_other_edits(self):
        base = {'tools': [entry('existing')]}
        local = copy.deepcopy(base)
        local['tools'][0]['description'] = 'Unfinished unrelated edit'
        local['tools'].append(entry())
        self.assertEqual(catalog_pr.new_entries(base, local), [entry()])
        self.assertEqual(base['tools'][0]['description'], 'A reviewed tool.')

    def test_invalid_or_private_metadata_is_rejected(self):
        for key, value in [('commit', 'main'), ('path', '/home/person/private'),
                           ('url', 'https://github.com@example.net/new-tool'),
                           ('repo', '../owner/tool'), ('notes', 'private notes'),
                           ('requirements', ['Use /Users/person/secrets']),
                           ('entrypoints', ['../../private']),
                           ('skill_paths', ['/etc/passwd'])]:
            with self.subTest(key=key):
                bad = entry()
                bad[key] = value
                with self.assertRaises(ValueError):
                    catalog_pr.new_entries({'tools': []}, {'tools': [bad]})

    def test_duplicate_ids_repositories_and_source_pin_drift_are_rejected(self):
        for tools in ([entry(), entry()], [entry(), dict(entry('other'), repo='EXAMPLE/NEW-TOOL')],
                      [dict(entry(), agent_setup={'source_revision': 'b' * 40})]):
            with self.subTest(tools=tools):
                with self.assertRaises(ValueError):
                    catalog_pr.new_entries({'tools': []}, {'tools': tools})

    def test_category_read_never_executes_source_and_requires_unique_membership(self):
        with tempfile.TemporaryDirectory() as tmp:
            marker = Path(tmp) / 'executed'
            source = f"CATEGORIES = {{'Tools': ['new-tool']}}\nopen({str(marker)!r}, 'w').write('bad')\n"
            self.assertEqual(catalog_pr.category_for(source, 'new-tool'), 'Tools')
            self.assertFalse(marker.exists())
        for source in ("CATEGORIES = {'A': [], 'B': []}",
                       "CATEGORIES = {'A': ['new-tool'], 'B': ['new-tool']}",
                       "CATEGORIES = dict(A=['new-tool'])"):
            with self.assertRaises(ValueError):
                catalog_pr.category_for(source, 'new-tool')

    def test_category_edit_preserves_other_code_and_is_literal_data(self):
        source = "# trusted generator\nCATEGORIES = {\n    'Tools': ['old'],\n}\nprint('trusted')\n"
        for category in ('Tools', 'Games and modding', "Quote's category"):
            changed = catalog_pr.add_category(source, category, 'new-tool')
            self.assertEqual(catalog_pr.category_for(changed, 'new-tool'), category)
            self.assertEqual(catalog_pr.category_for(changed, 'old'), 'Tools')
            self.assertTrue(changed.startswith('# trusted generator\n'))
            self.assertTrue(changed.endswith("print('trusted')\n"))

    def test_candidate_copies_only_one_entry_and_regenerates_from_trusted_base(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'scripts').mkdir()
            original = {'version': 1, 'catalog_revision_date': '2026-01-01', 'tools': [entry('old')]}
            (root / 'manifest.json').write_text(json.dumps(original))
            generator = root / 'scripts/generate_catalog_docs.py'
            generator.write_text("CATEGORIES = {'Tools': ['old']}\n# keep trusted code\n")
            catalog_pr.write_candidate(root, entry(), 'Games')
            result = json.loads((root / 'manifest.json').read_text())
            self.assertEqual([x['id'] for x in result['tools']], ['new-tool', 'old'])
            self.assertEqual(result['tools'][1], entry('old'))
            self.assertIn('# keep trusted code', generator.read_text())
            self.assertEqual(catalog_pr.category_for(generator.read_text(), 'new-tool'), 'Games')

    def test_closed_pr_is_respected_and_existing_open_pr_is_reused(self):
        for state in ('OPEN', 'CLOSED', 'MERGED'):
            existing = {'state': state, 'url': 'https://github.com/example/catalog/pull/1'}
            self.assertEqual(catalog_pr.existing_pr([existing]), existing)
        self.assertIsNone(catalog_pr.existing_pr([]))

    def test_repo_identity_rejects_different_remotes_and_embedded_credentials(self):
        for remote in ('https://github.com/example/catalog.git', 'git@github.com:example/catalog.git'):
            catalog_pr.check_remote(remote, 'example/catalog')
        for remote in ('https://token@github.com/example/catalog.git',
                       'https://github.com/other/catalog.git', '/tmp/catalog'):
            with self.assertRaises(ValueError):
                catalog_pr.check_remote(remote, 'example/catalog')

    def test_failed_validation_or_changed_input_never_pushes_and_preserves_source(self):
        for scenario in ('failed-tests', 'changed-input', 'failed-secret-scan', 'dry-run'):
            with self.subTest(scenario=scenario), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp) / 'source'
                root.mkdir()
                (root / 'scripts').mkdir()
                (root / 'tests').mkdir()
                (root / 'manifest.json').write_text(json.dumps({'tools': [entry('old')]}))
                (root / 'scripts/generate_catalog_docs.py').write_text(
                    "from pathlib import Path\nCATEGORIES = {'Tools': ['old']}\n"
                    "for name in ['catalog.md','docs/wiki/Tool-Catalog.md','docs/wiki/tools/new-tool.md']:\n"
                    " p=Path(name); p.parent.mkdir(parents=True,exist_ok=True); p.write_text('generated')\n")
                (root / 'tests/test_fixture.py').write_text(
                    "import unittest\nclass Check(unittest.TestCase):\n def test_gate(self):\n  self.assertTrue("
                    + ('False' if scenario == 'failed-tests' else 'True') + ")\n")
                execute = catalog_pr.run
                execute('git', 'init', '-q', root)
                execute('git', 'add', '.', cwd=root)
                execute('git', '-c', 'user.name=Test', '-c', 'user.email=test@example.invalid',
                        'commit', '-qm', 'Fixture', cwd=root)
                baseline = execute('git', 'rev-parse', 'HEAD', cwd=root)
                manifest = root / 'manifest.json'
                snapshot = {manifest: b'different' if scenario == 'changed-input' else manifest.read_bytes()}
                remote_writes = []
                def boundary(*args, **kwargs):
                    if args[:2] == ('gh', 'api'):
                        return 'a' * 40
                    if args[0] == 'fake-gitleaks':
                        if scenario == 'failed-secret-scan':
                            raise RuntimeError('Secret scan failed')
                        return ''
                    if args[:2] in [('git', 'push'), ('gh', 'pr')]:
                        remote_writes.append(args)
                        raise AssertionError('Unexpected remote write')
                    return execute(*args, **kwargs)
                args = SimpleNamespace(source=root, repository='example/catalog',
                                       base='main', gitleaks='fake-gitleaks', publish=False)
                with patch.object(catalog_pr, 'gh_json', return_value=[]), patch.object(catalog_pr, 'run', side_effect=boundary):
                    if scenario == 'dry-run':
                        catalog_pr.publish_addition(args, entry(), 'Tools', baseline, snapshot)
                    else:
                        args.publish = True
                        with self.assertRaises(RuntimeError):
                            catalog_pr.publish_addition(args, entry(), 'Tools', baseline, snapshot)
                self.assertEqual(remote_writes, [])
                self.assertEqual(execute('git', 'rev-parse', 'HEAD', cwd=root), baseline)
                self.assertEqual(execute('git', 'status', '--porcelain', cwd=root), '')
                self.assertEqual(execute('git', 'worktree', 'list', '--porcelain', cwd=root).count('worktree '), 1)


if __name__ == '__main__':
    unittest.main()
