"""Agent registration must only modify the selected temporary home."""
from pathlib import Path
import tempfile
import unittest
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


class AgentInstallTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'checkout with spaces'
        self.home = Path(self.tmp.name) / 'home'
        (self.root / 'bin').mkdir(parents=True)
        (self.root / 'bin/toolkit').write_text('#!/bin/sh\n')
        (self.root / 'skills/toolkit-selector').mkdir(parents=True)
        (self.root / 'skills/toolkit-selector/SKILL.md').write_text('Portable selector\n')

    def test_script_exists(self):
        self.assertTrue((ROOT / 'scripts/install_agent.py').is_file())

    def test_both_clients_preserve_bytes_backup_and_are_idempotent(self):
        from scripts.install_agent import install
        originals = {}
        for relative in ['.codex/AGENTS.md', '.config/opencode/AGENTS.md']:
            path = self.home / relative
            path.parent.mkdir(parents=True)
            original = b'# Personal instructions\r\nKeep this: \xff'
            path.write_bytes(original)
            originals[path] = original
        install(self.root, self.home, 'both')
        self.assertEqual((self.home / '.local/bin/toolkit').resolve(), self.root / 'bin/toolkit')
        self.assertEqual((self.home / '.agents/skills/toolkit-selector').resolve(), self.root / 'skills/toolkit-selector')
        first = {p: p.read_bytes() for p in originals}
        for path, original in originals.items():
            self.assertTrue(first[path].startswith(original))
            self.assertIn(str(self.root).encode(), first[path])
            self.assertTrue(any(p.read_bytes() == original for p in path.parent.glob('AGENTS.md.bak*')))
        before_paths = sorted(str(p.relative_to(self.home)) for p in self.home.rglob('*'))
        install(self.root, self.home, 'both')
        self.assertEqual({p: p.read_bytes() for p in originals}, first)
        self.assertEqual(sorted(str(p.relative_to(self.home)) for p in self.home.rglob('*')), before_paths)

    def test_available_helper_launchers_are_registered_idempotently(self):
        from scripts.install_agent import install
        names = ['toolkit-mcp', 'toolkit-serena', 'toolkit-chrome-mcp', 'toolkit-rag-mcp']
        for name in names:
            (self.root / 'bin' / name).write_text('#!/bin/sh\n')
        install(self.root, self.home, 'both')
        before = (self.home / '.codex/AGENTS.md').read_bytes()
        install(self.root, self.home, 'both')
        self.assertEqual((self.home / '.codex/AGENTS.md').read_bytes(), before)
        for name in names:
            self.assertEqual((self.home / '.local/bin' / name).resolve(), self.root / 'bin' / name)

    def test_helper_conflict_prevents_all_registration_writes(self):
        from scripts.install_agent import install
        for name in ['toolkit-mcp', 'toolkit-serena', 'toolkit-chrome-mcp', 'toolkit-rag-mcp']:
            with self.subTest(name=name):
                (self.root / 'bin' / name).write_text('#!/bin/sh\n')
                home = self.home / name
                conflict = home / '.local/bin' / name
                conflict.parent.mkdir(parents=True)
                conflict.write_text('unrelated helper')
                with self.assertRaisesRegex(ValueError, 'Refusing'):
                    install(self.root, home, 'both')
                self.assertEqual(conflict.read_text(), 'unrelated helper')
                self.assertFalse((home / '.local/bin/toolkit').exists())
                self.assertFalse((home / '.agents').exists())
                self.assertFalse((home / '.codex').exists())

    def test_unselected_client_is_untouched(self):
        from scripts.install_agent import install
        install(self.root, self.home, 'codex')
        self.assertTrue((self.home / '.codex/AGENTS.md').exists())
        self.assertFalse((self.home / '.config/opencode').exists())

    def test_conflicts_refused_before_any_config_is_written(self):
        from scripts.install_agent import install
        for relative in ['.local/bin/toolkit', '.agents/skills/toolkit-selector']:
            with self.subTest(relative=relative):
                home = self.home / relative.split('/')[0]
                conflict = home / relative
                conflict.parent.mkdir(parents=True)
                conflict.write_text('unrelated')
                with self.assertRaisesRegex(ValueError, 'refus|Refus'):
                    install(self.root, home, 'both')
                self.assertEqual(conflict.read_text(), 'unrelated')
                self.assertFalse((home / '.codex/AGENTS.md').exists())
                self.assertFalse((home / '.config/opencode/AGENTS.md').exists())


if __name__ == '__main__':
    unittest.main()
