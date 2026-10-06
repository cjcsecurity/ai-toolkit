#!/usr/bin/env python3
"""Register this toolkit checkout with selected agents without replacing personal settings."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]
START = b'<!-- BEGIN AI-TOOLKIT MANAGED -->'
END = b'<!-- END AI-TOOLKIT MANAGED -->'
CLIENTS = {
    'codex': '.codex/AGENTS.md',
    'opencode': '.config/opencode/AGENTS.md',
    'claude': '.claude/CLAUDE.md',
    'gemini': '.gemini/GEMINI.md',
    'cursor': None,
    'copilot': None,
    'windsurf': None,
    'generic': None,
}
# Each link points to the same canonical skill; client settings stay untouched.
SKILL_DIRS = {
    'claude': '.claude/skills',
    'gemini': '.gemini/skills',
    'cursor': '.cursor/skills',
    'copilot': '.copilot/skills',
    'windsurf': '.codeium/windsurf/skills',
}


def managed_block(root: Path) -> bytes:
    skill = root / 'skills/toolkit-selector/SKILL.md'
    # Use this checkout's portable skill as the canonical instructions.
    text = (f'\n# Shared AI toolkit\n\n'
            f'The toolkit checkout is at `{root}`. Before substantial project work or choosing tools, '
            f'read the toolkit-selector skill at `{skill}` and run `toolkit project`. '
            'When choosing or preparing a toolset, first run `toolkit search "project outcome" --kind repo --limit 8`, '
            'compare matching systems with `toolkit show ID`, and read their complete setup guides. '
            'Identify the primary workflow, supporting tools, and reasons for passing relevant alternatives before installing; '
            'base exclusions on documented requirements or known project constraints, and report unknown scale or runtime setup '
            'as gaps rather than treating them as evidence against a system. '
            'Then search individual capabilities with `toolkit search "what the task needs" --repo ID`; '
            'for an already-selected workflow, go directly to capability search. '
            'The `toolkit` launcher is installed in `~/.local/bin`; ensure that directory is on PATH.\n')
    return START + text.encode('utf-8') + END


def updated_content(old: bytes, block: bytes) -> bytes:
    if START not in old and END not in old:
        separator = b'\n\n' if old and not old.endswith(b'\n') else b'\n' if old else b''
        return old + separator + block + b'\n'
    if old.count(START) != 1 or old.count(END) != 1:
        raise ValueError('Refusing malformed or duplicate AI-TOOLKIT managed markers; repair them and retry')
    start = old.index(START)
    end = old.index(END)
    if end < start:
        raise ValueError('Refusing reversed AI-TOOLKIT managed markers')
    return old[:start] + block + old[end + len(END):]


def check_parents(path: Path) -> None:
    for parent in path.parents:
        if (parent.exists() or parent.is_symlink()) and not parent.is_dir():
            raise ValueError(f'Refusing non-directory or broken parent at {parent}; move it aside explicitly')


def check_link(path: Path, target: Path) -> None:
    check_parents(path)
    if path.is_symlink() and path.resolve() == target.resolve():
        return
    if path.exists() or path.is_symlink():
        raise ValueError(f'Refusing to replace unrelated command or skill at {path}; move it aside explicitly')


def write_config(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        backup = path.with_name(path.name + '.bak')
        suffix = 1
        while backup.exists() or backup.is_symlink():
            backup = path.with_name(f'{path.name}.bak.{suffix}')
            suffix += 1
        shutil.copy2(path, backup)
    descriptor, name = tempfile.mkstemp(prefix=f'.{path.name}-', dir=path.parent)
    try:
        with os.fdopen(descriptor, 'wb') as stream:
            stream.write(content)
        if path.exists():
            shutil.copymode(path, name)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def install(root: Path, home: Path, client: str, *, dry_run: bool = False) -> None:
    root, home = root.resolve(), home.expanduser().resolve()
    if client not in {*CLIENTS, 'both'}:
        raise ValueError(f'Unknown client: {client}')
    # Keep the original meaning of --client both, even as clients are added.
    selected = ['codex', 'opencode'] if client == 'both' else [client]
    launcher = root / 'bin/toolkit'
    skill = root / 'skills/toolkit-selector'
    if not launcher.is_file() or not (skill / 'SKILL.md').is_file():
        raise ValueError('Checkout must contain bin/toolkit and skills/toolkit-selector/SKILL.md')
    links = {home / '.local/bin/toolkit': launcher, home / '.agents/skills/toolkit-selector': skill}
    for name in selected:
        if name in SKILL_DIRS:
            links[home / SKILL_DIRS[name] / 'toolkit-selector'] = skill
    for name in ['toolkit-mcp', 'toolkit-serena', 'toolkit-chrome-mcp', 'toolkit-rag-mcp']:
        helper = root / 'bin' / name
        if helper.is_file():
            links[home / '.local/bin' / name] = helper
    # Validate every intended write before mutating the selected home.
    for path, target in links.items():
        check_link(path, target)
    block = managed_block(root)
    configs = []
    for name in selected:
        if CLIENTS[name] is None:
            continue
        path = home / CLIENTS[name]
        check_parents(path)
        if path.is_symlink():
            raise ValueError(f'Refusing symlinked agent instructions at {path}; manage that file explicitly')
        old = path.read_bytes() if path.exists() else b''
        new = updated_content(old, block)
        if new != old:
            configs.append((path, new))
    if dry_run:
        for path, target in links.items():
            print(f'Link: {path} -> {target}')
        for path, _ in configs:
            print(f'Update managed instructions: {path}')
        print('Dry run: no files changed. MCP registration is a separate step.')
        return
    for path, target in links.items():
        if not path.is_symlink():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.symlink_to(target, target_is_directory=target.is_dir())
    for path, content in configs:
        write_config(path, content)
    print(f'Registered toolkit for {client} in {home}. Add {home / ".local/bin"} to PATH if needed.')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--client', choices=[*CLIENTS, 'both'], required=True,
                        help='Agent to configure; both means Codex and OpenCode only')
    parser.add_argument('--home', type=Path, default=Path.home(), help='Home directory to configure (default: current user)')
    parser.add_argument('--dry-run', action='store_true', help='Validate and preview destinations without writing files')
    args = parser.parse_args()
    try:
        install(ROOT, args.home, args.client, dry_run=args.dry_run)
    except (ValueError, OSError) as error:
        parser.exit(1, f'Error: {error}\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
