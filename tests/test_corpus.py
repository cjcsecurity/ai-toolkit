import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load_module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CorpusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.corpus = load_module('corpus') if (ROOT / 'corpus.py').exists() else None
        cls.toolkit = load_module('toolkit')

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / 'repo'
        self.repo.mkdir()
        self.row = dict(id='demo', repo='owner/demo', path=str(self.repo),
                        description='General utilities', tags=['tools'], skill_paths=[])
        self.lib = self.toolkit.Library(self.root)

    def write(self, path, text, skill=False):
        target = self.repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)
        if skill:
            self.row['skill_paths'].append(path)

    def records(self):
        self.assertIsNotNone(self.corpus, 'capability corpus extractor is missing')
        (self.root / 'manifest.json').write_text(json.dumps({'tools': [self.row]}))
        return self.corpus.build_records(self.lib)

    def test_hidden_capability_gets_own_record_and_folded_description(self):
        self.write('skills/rare/SKILL.md', '---\nname: rare-audit\ndescription: >-\n  Audit zirconium\n  pressure vessels.\nmetadata:\n  name: unrelated\n---\n# Inspection\nCheck fracture propagation.\n', True)
        rows = self.records()
        skills = [r for r in rows if r['kind'] == 'skill']
        self.assertTrue(skills)
        self.assertEqual(skills[0]['name'], 'rare-audit')
        self.assertEqual(skills[0]['description'], 'Audit zirconium pressure vessels.')
        self.assertIn('zirconium', self.corpus.embedding_text(skills[0]))
        self.assertNotIn('zirconium', next(r['text'] for r in rows if r['kind'] == 'repo'))

    def test_skill_overview_preserves_frontmatter_and_body_cache_identity(self):
        header = '---\nname: intent-skill\ndescription: >-\n  Recover interrupted tasks\n  from durable checkpoints.\n---\n'
        self.write('skills/intent/SKILL.md', header + '# Procedure\nInspect the execution log.\n', True)
        rows = [r for r in self.records() if r['kind'] == 'skill']
        overview = next((r for r in rows if r.get('passage') == 'overview'), None)
        self.assertIsNotNone(overview)
        self.assertEqual(overview['text'], header.rstrip())
        self.assertEqual([overview['start_line'], overview['end_line']], [1, 6])
        self.assertEqual(overview['description'], 'Recover interrupted tasks from durable checkpoints.')
        body = next(r for r in rows if r.get('passage') != 'overview')
        self.assertEqual(body['uid'], '3bbefde893f117268672e412ee86f800f967cecd61f2b64f4028ac0dd25dd711')
        self.assertEqual(body['text'], '# Procedure\nInspect the execution log.')
        self.assertEqual(self.corpus.embedding_text(body), 'owner/demo: intent-skill\nRecover interrupted tasks from durable checkpoints.\n# Procedure\nInspect the execution log.')

    def test_overview_provider_aliases_follow_full_file_deduplication(self):
        source = '---\nname: graph\ndescription: Trace graph relationships.\n---\nRead the graph.\n'
        self.write('skills/graph/SKILL.md', source, True)
        self.write('.claude/skills/graph/SKILL.md', source, True)
        rows = [r for r in self.records() if r.get('passage') == 'overview']
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['path'], 'skills/graph/SKILL.md')
        self.assertEqual(rows[0]['aliases'], ['.claude/skills/graph/SKILL.md'])

    def test_skill_without_frontmatter_gets_source_backed_overview(self):
        self.write('skills/plain/SKILL.md', '# Plain skill\nOperate the workflow.\n', True)
        rows = [r for r in self.records() if r.get('passage') == 'overview']
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['text'], '# Plain skill\nOperate the workflow.')
        self.assertEqual([rows[0]['start_line'], rows[0]['end_line']], [1, 2])

    def test_heading_chunks_preserve_source_locations(self):
        source = '# Intro\nOverview.\n\n## Waterfall diagnostics\nInspect timing bottlenecks.\n\n## Export\nSave the trace.\n'
        self.write('docs/guide.md', source)
        rows = [r for r in self.records() if r['kind'] == 'doc']
        match = next(r for r in rows if 'Inspect timing bottlenecks.' in r['text'])
        self.assertIn('Waterfall diagnostics', match['name'])
        self.assertEqual(match['start_line'], 4)
        self.assertEqual(match['text'], '\n'.join(source.splitlines()[match['start_line']-1:match['end_line']]).strip())

    def test_reference_entries_keep_service_details_category_and_exact_source_spans(self):
        self.row['kind'] = 'reference'
        source = ('# Directory\n## Hosting\n'
                  '  * [Harbor](https://harbor.example) - Free static sites.\n'
                  '    Includes custom domains and 5 GB storage.\n'
                  '  * [Orchard](https://orchard.example) - Managed databases.\n'
                  '* [Unindented](https://unindented.example) - Another host.\n'
                  '## Weather\n'
                  'API | Description | Auth | HTTPS | CORS |\n'
                  '|---|---|---|---|---|\n'
                  '| [Climate](https://climate.example) | Historical rainfall | apiKey | Yes | No |\n'
                  '| [Forecast](https://forecast.example) | Tomorrow\'s weather | No | Yes | Yes |\n')
        self.write('README.md', source)
        rows = [r for r in self.records() if r['kind'] == 'doc']
        harbor = next(r for r in rows if '[Harbor]' in r['text'])
        self.assertIn('5 GB storage', harbor['text'])
        self.assertNotIn('Orchard', harbor['text'])
        self.assertIn('Hosting', harbor['name'])
        self.assertIn('Harbor', harbor['name'])
        self.assertTrue(any(r['name'] == 'Hosting / Unindented' for r in rows))
        climate = next(r for r in rows if '[Climate]' in r['text'])
        self.assertNotIn('Forecast', climate['text'])
        embedded = self.corpus.embedding_text(climate)
        self.assertIn('Weather', embedded)
        self.assertIn('HTTPS', embedded)
        self.assertIn('apiKey', embedded)
        for row in rows:
            self.assertIn(row['text'], '\n'.join(source.splitlines()[row['start_line']-1:row['end_line']]))

    def test_reference_chunking_keeps_nested_limits_and_long_entry_tail(self):
        self.row['kind'] = 'reference'
        source = ('## Cloud\n* [Cloud](https://cloud.example)\n'
                  '  * [Compute](https://cloud.example/compute) - 20 hours.\n'
                  '  * [Storage](https://cloud.example/storage) - 10 GB.\n'
                  '* [Long](https://long.example) - ' + 'Details. ' * 400 + 'TAIL_LIMIT\n'
                  '## Example\n```md\n* [Not a service](https://example.invalid)\n```\n')
        self.write('README.md', source)
        rows = [r for r in self.records() if r['kind'] == 'doc']
        cloud = next(r for r in rows if '[Cloud]' in r['text'])
        self.assertIn('20 hours', cloud['text'])
        self.assertIn('10 GB', cloud['text'])
        self.assertNotIn('[Long]', cloud['text'])
        tail = next(r for r in rows if 'TAIL_LIMIT' in r['text'])
        self.assertIn('Long', tail['name'])
        self.assertFalse(any('Not a service' in r['name'] for r in rows))
        self.assertTrue(all(len(self.corpus.embedding_text(r)) <= 2000 for r in rows))

    def test_fixtures_attacks_dependencies_builds_are_excluded(self):
        for folder in ('tests', '__fixtures__', 'attack_samples', 'malicious_skills', 'node_modules', 'dist', 'build', '.venv'):
            self.write(folder + '/SKILL.md', '---\nname: fake\n---\nUntrusted decoy capability.', True)
        self.write('docs/examples/guide.md', '# Safe example\nRelevant example capability.')
        rows = self.records()
        self.assertFalse(any('Untrusted decoy' in r['text'] for r in rows))
        self.assertTrue(any('Relevant example' in r['text'] for r in rows))

    def test_administrative_history_is_excluded_but_declared_skills_are_preserved(self):
        self.write('CHANGELOG.md', '# Changes\nRemoved capability should not be discoverable.')
        self.write('docs/plans/old.md', '# Plan\nAbandoned capability.')
        self.write('skills/plans/SKILL.md', '---\nname: planning\n---\nCreate implementation plans.', True)
        rows = self.records()
        self.assertFalse(any('Removed capability' in r['text'] or 'Abandoned capability' in r['text'] for r in rows))
        self.assertTrue(any(r['name'] == 'planning' for r in rows))

    def test_duplicate_provider_copies_prefer_canonical_skill(self):
        skill = '---\nname: real-capability\ndescription: Understand graph topology.\n---\n# Graph\nTrace connectivity.\n'
        self.write('.claude/skills/graph/SKILL.md', skill, True)
        self.write('skills/graph/SKILL.md', skill, True)
        rows = [r for r in self.records() if r['kind'] == 'skill']
        self.assertTrue(rows)
        self.assertTrue(all(r['path'] == 'skills/graph/SKILL.md' for r in rows))
        self.assertIn('.claude/skills/graph/SKILL.md', rows[0]['aliases'])

    def test_all_declared_skills_survive_large_file_lists(self):
        for i in range(1003):
            self.write(f'skills/s{i:04d}/SKILL.md', f'---\nname: capability-{i}\n---\nInspect unique system {i}.\n', True)
        rows = self.records()
        self.assertEqual(len({r['name'] for r in rows if r['kind'] == 'skill'}), 1003)

    def test_giant_single_line_file_retains_middle_and_tail(self):
        source = '# Large guide\n' + ('x ' * 1_050_000) + 'TAIL_SENTINEL'
        self.write('docs/huge.md', source)
        rows = [r for r in self.records() if r['kind'] == 'doc']
        self.assertTrue(any('TAIL_SENTINEL' in r['text'] for r in rows))
        self.assertTrue(all(len(self.corpus.embedding_text(r)) <= 2000 for r in rows))
        self.assertTrue(all(1 <= r['start_line'] <= r['end_line'] <= 2 for r in rows))

    def test_long_documents_pack_short_headings_without_losing_content(self):
        source = ''.join(f'## Topic {i}\n' + (f'Capability number {i}. ' * 8) + '\n\n' for i in range(40))
        self.write('docs/many.md', source)
        rows = [r for r in self.records() if r['kind'] == 'doc']
        self.assertLess(len(rows), 15)
        for i in range(40):
            self.assertTrue(any(f'Capability number {i}.' in r['text'] for r in rows))

    def test_frontmatter_folded_paragraphs_and_literal_blocks(self):
        self.assertIsNotNone(self.corpus)
        for marker, expected in [('>-', 'First line second line.\nNew paragraph.'), ('|-', 'First line\nsecond line.\n\nNew paragraph.')]:
            text = f'---\nname: "quoted: name"\ndescription: {marker}\n  First line\n  second line.\n\n  New paragraph.\n---\nBody'
            metadata, _ = self.corpus.skill_metadata(text)
            self.assertEqual(metadata['description'], expected)
            self.assertEqual(metadata['name'], 'quoted: name')

    def test_ids_are_deterministic_and_external_symlinks_are_not_read(self):
        self.write('README.md', '# Demo\nUseful documentation.\n')
        (self.root / 'private.md').write_text('SECRET_SENTINEL')
        (self.repo / 'outside.md').symlink_to(self.root / 'private.md')
        first = self.records()
        second = self.records()
        self.assertEqual(first, second)
        self.assertEqual(len({r['uid'] for r in first}), len(first))
        self.assertFalse(any('SECRET_SENTINEL' in r['text'] for r in first))


if __name__ == '__main__':
    unittest.main()
