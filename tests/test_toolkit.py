import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / 'toolkit.py'


class ToolkitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location('toolkit', MODULE)
        cls.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.module)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        repo = self.root / 'repos' / 'demo--browser'
        (repo / 'skills' / 'browser-debug').mkdir(parents=True)
        (repo / 'README.md').write_text('# Browser\nInspect browser performance and network requests.\n')
        (repo / 'skills/browser-debug/SKILL.md').write_text('---\nname: browser-debug\ndescription: Inspect browser network requests.\n---\nRun diagnostics and inspect timings.\n')
        other = self.root / 'repos/demo--finance'
        other.mkdir()
        (other / 'README.md').write_text('# Finance\nAnalyze balance sheets.\n')
        self.rows = [
            dict(id='browser', repo='demo/browser', path=str(repo), description='Browser performance diagnostics', tags=['network', 'debugging'], kind='mcp', clone_status='cloned', skill_paths=['skills/browser-debug/SKILL.md']),
            dict(id='finance', repo='demo/finance', path=str(other), description='Financial statement analysis', tags=['accounting'], kind='skill-bundle', clone_status='cloned', skill_paths=[]),
        ]
        (self.root / 'manifest.json').write_text(json.dumps({'version': 1, 'tools': self.rows}))
        self.lib = self.module.Library(self.root)
        self.lib.index()

    def test_search_ranks_relevant_tool_and_unknown_query_is_empty(self):
        self.assertEqual(self.lib.search('debug browser network')[0]['id'], 'browser')
        self.assertEqual(self.lib.search('zyxnonexistent'), [])
        self.assertEqual(self.lib.search('" OR * --')[0:1], [])

    def test_docs_stay_within_selected_repo_and_include_source(self):
        rows = self.lib.docs('browser', 'network')
        self.assertTrue(rows)
        self.assertTrue(all(x['id'] == 'browser' for x in rows))
        self.assertIn('path', rows[0])
        self.assertEqual(self.lib.docs('finance', 'network'), [])

    def test_index_rebuild_removes_deleted_document(self):
        p = Path(self.rows[0]['path']) / 'README.md'
        p.unlink()
        self.lib.index()
        self.assertFalse(any(x['path'] == 'README.md' for x in self.lib.docs('browser', 'network')))

    def test_read_rejects_traversal_and_external_symlink(self):
        with self.assertRaises(ValueError):
            self.lib.read('browser', '../../manifest.json')
        link = Path(self.rows[0]['path']) / 'outside.md'
        link.symlink_to(self.root / 'manifest.json')
        with self.assertRaises(ValueError):
            self.lib.read('browser', 'outside.md')

    def test_skill_search_and_full_read(self):
        rows = self.lib.skills('browser', 'network')
        self.assertEqual(rows[0]['name'], 'browser-debug')
        self.assertIn('Run diagnostics', self.lib.read('browser', rows[0]['path']))

    def test_folded_skill_description_is_searchable(self):
        p = Path(self.rows[0]['path']) / 'skills/browser-debug/SKILL.md'
        p.write_text('---\nname: browser-debug\ndescription: >-\n  Inspect waterfall timings\n  and network latency.\nmetadata:\n  version: 1\n---\nBody')
        self.lib.index()
        rows = self.lib.skills('browser', 'waterfall')
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['description'], 'Inspect waterfall timings and network latency.')

    def test_status_distinguishes_missing_runtime_from_ready_index(self):
        result = self.lib.search_status()
        self.assertEqual(result['status'], 'lexical-fallback')
        self.assertEqual(result['vectors'], 0)
        self.assertIn('setup', result['note'])
        self.assertGreater(result['passages']['skill'], 0)

    def test_failed_embedding_rebuild_preserves_published_index(self):
        from unittest.mock import patch
        original = self.lib.db.read_bytes()
        with patch('hybrid.index_vectors', side_effect=RuntimeError('inference failed')):
            with self.assertRaises(RuntimeError):
                self.lib.index(semantic=True)
        self.assertEqual(self.lib.db.read_bytes(), original)
        self.assertFalse(list(self.root.glob('.index-*.sqlite3')))
        self.assertEqual(self.lib.search('browser')[0]['id'], 'browser')

    def test_global_search_retrieves_nested_capability_with_source_lines(self):
        p = Path(self.rows[0]['path']) / 'skills/browser-debug/SKILL.md'
        p.write_text('---\nname: restore-session\ndescription: Recover interrupted execution.\n---\n# Checkpoints\nPersist task state and resume after crashes.\n')
        self.lib.index()
        rows = self.lib.search('restore-session', kinds=['skill'])
        self.assertEqual(rows[0]['name'], 'restore-session')
        self.assertEqual(rows[0]['path'], 'skills/browser-debug/SKILL.md')
        self.assertGreaterEqual(rows[0]['lines'][0], 1)
        self.assertGreaterEqual(rows[0]['lines'][1], rows[0]['lines'][0])
        self.assertEqual(rows[0]['match_kind'], 'skill')

    def test_manifest_changes_refresh_search_and_remove_deleted_entries(self):
        self.rows[0]['description'] = 'Unique watermelons'
        self.rows[0]['tags'] = []
        self.rows.pop()
        (self.root / 'manifest.json').write_text(json.dumps({'tools': self.rows}))
        self.assertEqual(self.lib.search('watermelons')[0]['id'], 'browser')
        self.assertEqual(self.lib.search('accounting'), [])

    def test_selection_preserves_preferences_and_invalid_selection_does_not_write(self):
        project = self.root / 'project'
        project.mkdir()
        p = project / '.ai-toolkit.json'
        p.write_text(json.dumps({'notes': 'prefer local tools', 'tools': ['finance']}))
        self.lib.select(['browser'], project)
        self.assertEqual(json.loads(p.read_text())['notes'], 'prefer local tools')
        self.assertEqual(json.loads(p.read_text())['tools'], ['finance', 'browser'])
        before = p.read_text()
        with self.assertRaises(ValueError):
            self.lib.select(['nonexistent'], project)
        self.assertEqual(p.read_text(), before)

    def test_output_is_valid_json_within_budget(self):
        out = self.module.bounded_json([{'text': 'x' * 9000}] * 8, 1200)
        self.assertLessEqual(len(out), 1200)
        self.assertTrue(json.loads(out)['truncated'])

    def test_paged_read_returns_exact_continuation_without_losing_characters(self):
        text = 'abcdef' * 500
        first = self.module.read_excerpt(text, 'browser', 'README.md', 0, 700)
        self.assertLessEqual(len(first), 700)
        import re
        offset = int(re.search(r'Next offset: (\d+)', first).group(1))
        second = self.module.read_excerpt(text, 'browser', 'README.md', offset, 700)
        self.assertIn(text[offset:offset + 100], second)
        self.assertIn(text[:offset], first)


if __name__ == '__main__':
    unittest.main()
