"""Portable setup regression tests; all Git sources stay in temporary directories."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


class SourceSyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'toolkit with spaces'
        self.root.mkdir()
        self.upstream = Path(self.tmp.name) / 'upstream'
        self.git('init', str(self.upstream))
        self.git('-C', str(self.upstream), 'config', 'user.email', 'test@example.invalid')
        self.git('-C', str(self.upstream), 'config', 'user.name', 'Test')
        (self.upstream / 'README.md').write_text('first\n')
        self.git('-C', str(self.upstream), 'add', '.')
        self.git('-C', str(self.upstream), 'commit', '-m', 'first')
        self.sha = self.git('-C', str(self.upstream), 'rev-parse', 'HEAD').strip()
        (self.upstream / 'README.md').write_text('second\n')
        self.git('-C', str(self.upstream), 'commit', '-am', 'second')
        self.entry = dict(id='example', repo='example/source', url='https://github.com/example/source.git',
                          path='repos/example--source', commit=self.sha)
        self.env = patch.dict(os.environ, {'GIT_CONFIG_COUNT': '1',
            'GIT_CONFIG_KEY_0': f'url.{self.upstream}.insteadOf',
            'GIT_CONFIG_VALUE_0': self.entry['url']})
        self.env.start()
        self.addCleanup(self.env.stop)

    @staticmethod
    def git(*args):
        return subprocess.run(['git', *args], check=True, text=True, capture_output=True).stdout

    def test_scripts_exist(self):
        self.assertTrue((ROOT / 'scripts/sync_sources.py').is_file())
        self.assertTrue((ROOT / 'scripts/bootstrap.py').is_file())

    def test_fetches_exact_revision_and_is_idempotent(self):
        from scripts.sync_sources import sync_repository
        destination = sync_repository(self.root, self.entry)
        self.assertEqual(self.git('-C', str(destination), 'rev-parse', 'HEAD').strip(), self.sha)
        self.assertEqual((destination / 'README.md').read_text(), 'first\n')
        self.assertEqual(sync_repository(self.root, self.entry), destination)

    def test_dirty_and_wrong_revision_are_preserved(self):
        from scripts.sync_sources import sync_repository
        destination = sync_repository(self.root, self.entry)
        (destination / 'local.txt').write_text('keep')
        with self.assertRaisesRegex(ValueError, 'dirty'):
            sync_repository(self.root, self.entry)
        self.assertEqual((destination / 'local.txt').read_text(), 'keep')
        (destination / 'local.txt').unlink()
        changed = dict(self.entry, commit='0' * 40)
        with self.assertRaisesRegex(ValueError, 'revision'):
            sync_repository(self.root, changed)
        self.assertEqual(self.git('-C', str(destination), 'rev-parse', 'HEAD').strip(), self.sha)

    def test_rejects_escape_and_remote_protocol(self):
        from scripts.sync_sources import sync_repository
        for change in [dict(path='../escape'), dict(path='/tmp/escape'), dict(commit='main'),
                       dict(url='file:///tmp/repo'), dict(path='runtime/source')]:
            with self.subTest(change=change), self.assertRaises(ValueError):
                sync_repository(self.root, dict(self.entry, **change))
        outside = Path(self.tmp.name) / 'outside'
        outside.mkdir()
        (self.root / 'repos').symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            sync_repository(self.root, self.entry)
        self.assertEqual(list(outside.iterdir()), [])

    def test_failed_fetch_leaves_no_checkout_or_temporary_clone(self):
        from scripts.sync_sources import sync_repository
        with self.assertRaises((ValueError, RuntimeError)):
            sync_repository(self.root, dict(self.entry, commit='0' * 40))
        self.assertFalse((self.root / self.entry['path']).exists())
        self.assertEqual(list((self.root / 'repos').iterdir()), [])

    def test_scoped_selection_and_unknown_id(self):
        from scripts.sync_sources import select_repositories
        entries = [self.entry, dict(self.entry, id='other')]
        self.assertEqual(select_repositories(entries, ['example'], False), [self.entry])
        self.assertEqual(select_repositories(entries, [], True), entries)
        self.assertEqual(select_repositories(entries, [], False), [])
        with self.assertRaisesRegex(ValueError, 'Unknown'):
            select_repositories(entries, ['missing'], False)

    def test_bootstrap_indexes_own_root_despite_foreign_environment_override(self):
        for name in ('toolkit.py', 'corpus.py', 'hybrid.py', 'embeddings.py'):
            shutil.copy2(ROOT / name, self.root / name)
        (self.root / 'manifest.json').write_text(json.dumps({'tools': [self.entry]}))
        foreign = Path(self.tmp.name) / 'foreign toolkit'
        foreign.mkdir()
        (foreign / 'manifest.json').write_text(json.dumps({'tools': []}))
        env = dict(os.environ, AI_TOOLKIT_HOME=str(foreign))
        result = subprocess.run([sys.executable, '-S', '-c',
            'from pathlib import Path; import sys; '
            'from scripts.bootstrap import bootstrap; bootstrap(Path(sys.argv[1]), [], False, False)',
            str(self.root)], cwd=ROOT, env=env, capture_output=True, text=True, check=True)
        self.assertTrue((self.root / 'index.sqlite3').is_file(), result.stdout)
        self.assertFalse((foreign / 'index.sqlite3').exists())
        self.assertEqual(sorted(p.name for p in foreign.iterdir()), ['manifest.json'])

    def test_catalog_only_bootstrap_works_without_third_party_dependencies(self):
        # A real child process under -S catches accidental site-package imports.
        (self.root / 'manifest.json').write_text(json.dumps({'tools': [self.entry]}))
        (self.root / 'toolkit.py').write_text(
            'import pathlib, sys\npathlib.Path(__file__).with_name("indexed.txt").write_text(" ".join(sys.argv[1:]))\n')
        result = subprocess.run([sys.executable, '-S', '-c',
            'from pathlib import Path; import sys; '
            'from scripts.bootstrap import bootstrap; bootstrap(Path(sys.argv[1]), [], False, False)',
            str(self.root)], cwd=ROOT, capture_output=True, text=True, check=True)
        self.assertIn('catalog-only', result.stdout.lower())
        self.assertEqual((self.root / 'indexed.txt').read_text(), 'index --lexical')
        self.assertFalse((self.root / 'repos').exists())
        self.assertFalse((self.root / 'runtime').exists())


class SemanticRuntimeTests(unittest.TestCase):
    def test_semantic_probe_requires_python_supported_by_pinned_dependencies(self):
        from scripts.bootstrap import compatible_python
        with tempfile.TemporaryDirectory() as directory:
            probe = Path(directory) / 'python-probe'
            for version, expected in [((3, 11), False), ((3, 12), True),
                                      ((3, 13), True), ((3, 14), False)]:
                with self.subTest(version=version):
                    # Simulate interpreter versions while running the real probe code.
                    probe.write_text(f'#!{sys.executable}\nimport sys\n'
                                     f'sys.version_info = {version!r}\nexec(sys.argv[2])\n')
                    probe.chmod(0o755)
                    self.assertEqual(compatible_python(str(probe)), expected)


if __name__ == '__main__':
    unittest.main()
