"""Agent registration must only modify the selected temporary home."""
from pathlib import Path
import tempfile
import unittest
import sys
import subprocess

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

    def test_native_clients_discover_the_same_selector_without_replacing_settings(self):
        from scripts.install_agent import install
        cases = [
            ('claude', '.claude/skills', '.claude/CLAUDE.md'),
            ('gemini', '.gemini/skills', '.gemini/GEMINI.md'),
            ('cursor', '.cursor/skills', None),
            ('copilot', '.copilot/skills', None),
            ('windsurf', '.codeium/windsurf/skills', None),
            ('generic', '.agents/skills', None),
        ]
        for client, skills, instructions in cases:
            with self.subTest(client=client):
                home = self.home / client
                settings = home / '.settings.json'
                home.mkdir(parents=True)
                settings.write_bytes(b'{"personal": true}\r\n')
                if instructions:
                    path = home / instructions
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(b'# My instructions\r\nKeep these bytes: \xff\n')
                install(self.root, home, client)
                self.assertEqual((home / skills / 'toolkit-selector/SKILL.md').read_text(), 'Portable selector\n')
                self.assertEqual((home / skills / 'toolkit-selector').resolve(), self.root / 'skills/toolkit-selector')
                if instructions:
                    self.assertTrue(path.read_bytes().startswith(path.with_name(path.name + '.bak').read_bytes()))
                snapshot = sorted(str(p.relative_to(home)) for p in home.rglob('*'))
                install(self.root, home, client)
                self.assertEqual(sorted(str(p.relative_to(home)) for p in home.rglob('*')), snapshot)
                self.assertEqual(settings.read_bytes(), b'{"personal": true}\r\n')
                self.assertFalse((home / '.codex').exists())
                self.assertFalse((home / '.config/opencode').exists())

    def test_native_skill_collision_prevents_launcher_and_instruction_writes(self):
        from scripts.install_agent import install
        conflict = self.home / '.claude/skills/toolkit-selector'
        conflict.mkdir(parents=True)
        (conflict / 'SKILL.md').write_text('My unrelated skill')
        with self.assertRaisesRegex(ValueError, 'Refusing'):
            install(self.root, self.home, 'claude')
        self.assertEqual((conflict / 'SKILL.md').read_text(), 'My unrelated skill')
        self.assertFalse((self.home / '.local').exists())
        self.assertFalse((self.home / '.claude/CLAUDE.md').exists())

    def test_claude_rejects_symlinked_or_malformed_instructions_before_writes(self):
        from scripts.install_agent import install
        path = self.home / '.claude/CLAUDE.md'
        path.parent.mkdir(parents=True)
        for content in [b'<!-- BEGIN AI-TOOLKIT MANAGED -->', b'<!-- END AI-TOOLKIT MANAGED -->\n<!-- BEGIN AI-TOOLKIT MANAGED -->']:
            path.write_bytes(content)
            with self.assertRaisesRegex(ValueError, 'Refusing'):
                install(self.root, self.home, 'claude')
            self.assertEqual(path.read_bytes(), content)
            self.assertFalse((self.home / '.local').exists())
        path.unlink()
        path.symlink_to(self.root / 'personal.md')
        with self.assertRaisesRegex(ValueError, 'symlinked'):
            install(self.root, self.home, 'claude')
        self.assertFalse((self.root / 'personal.md').exists())
        self.assertFalse((self.home / '.local').exists())

    def test_dry_run_prints_destinations_without_creating_home(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / 'scripts/install_agent.py'), '--client', 'claude',
             '--home', str(self.home), '--dry-run'], capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('.claude/CLAUDE.md', result.stdout)
        self.assertIn('.claude/skills/toolkit-selector', result.stdout)
        self.assertFalse(self.home.exists())

    def test_invalid_parent_prevents_partial_install_including_dry_run(self):
        from scripts.install_agent import install
        for client, relative in [('cursor', '.cursor/skills'), ('claude', '.claude')]:
            for broken_link in [False, True]:
                with self.subTest(client=client, broken_link=broken_link):
                    home = self.home / f'{client}-{broken_link}'
                    parent = home / relative
                    parent.parent.mkdir(parents=True)
                    if broken_link:
                        parent.symlink_to(home / 'missing')
                    else:
                        parent.write_text('Unrelated file')
                    before = sorted(str(p.relative_to(home)) for p in home.rglob('*'))
                    for dry_run in [True, False]:
                        with self.assertRaisesRegex(ValueError, 'Refusing'):
                            install(self.root, home, client, dry_run=dry_run)
                        self.assertEqual(sorted(str(p.relative_to(home)) for p in home.rglob('*')), before)
                        self.assertFalse((home / '.local').exists())


if __name__ == '__main__':
    unittest.main()
