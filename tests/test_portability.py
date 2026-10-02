"""Portable catalog paths and executable entry points, without downloaded sources."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from toolkit import Library

CODE = Path(__file__).resolve().parents[1]


class PortabilityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'toolkit with spaces'
        self.root.mkdir()
        self.row = dict(id='demo', repo='owner/demo', path='repos/owner--demo',
                        description='Zirconium inspection', skill_paths=[],
                        availability='runtime-ready', commit='0' * 40)
        self.save()
        self.lib = Library(self.root)

    def save(self):
        (self.root / 'manifest.json').write_text(json.dumps({'tools': [self.row]}))

    def test_relative_catalog_reads_and_indexes_after_relocation(self):
        repo = self.root / self.row['path']
        repo.mkdir(parents=True)
        (repo / 'README.md').write_text('# Nacre\nInspect nacre fractures.\n')
        moved = self.root.with_name('relocated toolkit')
        self.root.rename(moved)
        lib = Library(moved)
        self.assertEqual(Path(lib.entry('demo')['path']), moved / self.row['path'])
        self.assertIn('nacre', lib.read('demo', 'README.md'))
        self.assertEqual(lib.docs('demo', 'nacre', lexical_only=True)[0]['id'], 'demo')

    def test_missing_source_keeps_catalog_search_and_reports_local_state(self):
        rows = self.lib.search('zirconium', kinds=['repo'], lexical_only=True)
        self.assertEqual(rows[0]['id'], 'demo')
        self.assertFalse(rows[0]['source_present'])
        self.assertEqual(rows[0]['availability'], 'source-missing')
        self.assertFalse(self.lib.doctor()[0]['source_present'])
        with self.assertRaisesRegex(FileNotFoundError, 'bootstrap'):
            self.lib.read('demo', 'README.md')

    def test_present_source_does_not_claim_runtime_ready(self):
        (self.root / self.row['path']).mkdir(parents=True)
        self.assertEqual(self.lib.entry('demo')['availability'], 'source-only')
        self.assertTrue(self.lib.doctor()[0]['source_present'])
        self.assertFalse(self.lib.doctor()[0]['revision_matches'])

    def test_catalog_rejects_traversal_absolute_outside_and_external_symlink(self):
        outside = Path(self.tmp.name) / 'outside'
        outside.mkdir()
        (self.root / 'link').symlink_to(outside, target_is_directory=True)
        for path in ('../outside', str(outside), 'link'):
            with self.subTest(path=path):
                self.row['path'] = path
                self.save()
                with self.assertRaisesRegex(ValueError, 'inside.*toolkit'):
                    self.lib.entries()

    def test_launcher_uses_own_symlink_target_from_unrelated_cwd(self):
        for name in ('toolkit.py', 'corpus.py', 'hybrid.py', 'embeddings.py'):
            shutil.copy2(CODE / name, self.root / name)
        shutil.copytree(CODE / 'bin', self.root / 'bin')
        launcher = self.root / 'bin/toolkit'
        self.assertTrue(launcher.exists(), 'portable CLI launcher must be distributed')
        link = Path(self.tmp.name) / 'toolkit alias'
        link.symlink_to(launcher)
        env = {k: v for k, v in os.environ.items() if k != 'AI_TOOLKIT_HOME'}
        result = subprocess.run([str(link), 'search', 'zirconium', '--kind', 'repo', '--lexical'],
                                cwd=self.tmp.name, env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['results'][0]['id'], 'demo')
        override = Path(self.tmp.name) / 'separate data'
        override.mkdir()
        (override / 'manifest.json').write_text(json.dumps({'tools': []}))
        env['AI_TOOLKIT_HOME'] = str(override)
        result = subprocess.run([str(link), 'list'], cwd=self.tmp.name, env=env,
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['results'], [])


    def test_chrome_default_wrapper_uses_code_checkout_with_separate_data_root(self):
        env = {key: value for key, value in os.environ.items()
               if key != 'TOOLKIT_CHROME_COMMAND'}
        env['AI_TOOLKIT_HOME'] = str(self.root)
        result = subprocess.run(
            [sys.executable, '-S', '-c',
             'import json, mcp_client; print(json.dumps({"chrome": mcp_client.CHROME, "root": str(mcp_client.ROOT)}))'],
            cwd=CODE, env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        config = json.loads(result.stdout)
        self.assertEqual(config['root'], str(self.root))
        self.assertEqual(Path(config['chrome']), CODE / 'bin/toolkit-chrome-mcp')

    def test_mcp_dependency_error_explains_optional_install(self):
        result = subprocess.run([sys.executable, '-S', str(CODE / 'mcp_client.py'),
                                 'tools', '--project', str(self.root)],
                                capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('requirements-mcp.txt', result.stderr)

    def test_chrome_wrapper_requires_explicit_local_configuration(self):
        wrapper = CODE / 'bin/toolkit-chrome-mcp'
        self.assertTrue(wrapper.is_file(), 'local-only Chrome launcher must be distributed')
        env = {k: v for k, v in os.environ.items() if not k.startswith('TOOLKIT_')}
        result = subprocess.run([str(wrapper)], env=env, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('TOOLKIT_CHROME_MCP_ENTRY', result.stderr)
        entry = self.root / 'fake server.py'
        entry.write_text('import json, os, sys; print(json.dumps({"args": sys.argv[1:], "telemetry": os.environ.get("CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS"), "updates": os.environ.get("CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS")}))')
        env.update(TOOLKIT_NODE=sys.executable, TOOLKIT_CHROME_MCP_ENTRY=str(entry),
                   TOOLKIT_CHROME_EXECUTABLE=sys.executable)
        result = subprocess.run([str(wrapper)], env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(result.stdout)
        for flag in ('--headless', '--isolated', '--no-usage-statistics', '--no-performance-crux'):
            self.assertIn(flag, data['args'])
        self.assertEqual(data['telemetry'], '1')
        self.assertEqual(data['updates'], '1')
        for flag in ('--no-usage-statistics=false', '--userDataDir=/tmp/profile', '--no-performance-crux=false'):
            result = subprocess.run([str(wrapper), flag], env=env, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0, flag)
            self.assertIn('isolated launcher', result.stderr)


if __name__ == '__main__':
    unittest.main()
