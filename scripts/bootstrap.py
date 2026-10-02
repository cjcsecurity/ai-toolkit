#!/usr/bin/env python3
"""Set up the catalog and selected source checkouts; semantic search is opt-in."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys

if __package__:
    from .sync_sources import ROOT, add_selection_arguments, load_entries, select_repositories, sync_repository
else:
    from sync_sources import ROOT, add_selection_arguments, load_entries, select_repositories, sync_repository


def run(command: list[str], root: Path) -> None:
    # Bootstrap owns this checkout; CLI data-root overrides must not redirect setup.
    env = dict(os.environ, AI_TOOLKIT_HOME=str(root.resolve()))
    subprocess.run(command, cwd=root, env=env, check=True)


def compatible_python(executable: str) -> bool:
    probe = subprocess.run([executable, '-c',
        'import sys; sys.exit(not ((3, 11) <= sys.version_info[:2] <= (3, 13)))'],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return probe.returncode == 0


def semantic_runtime(root: Path) -> Path:
    runtime = root / 'runtime/search'
    python = runtime / 'bin/python'
    uv = shutil.which('uv')
    if runtime.exists():
        if not python.exists() or not compatible_python(str(python)):
            raise ValueError(f'{runtime} is not a compatible Python 3.11–3.13 environment; move it aside and retry')
    else:
        runtime.parent.mkdir(parents=True, exist_ok=True)
        if uv:
            run([uv, 'venv', '--python', '3.12', str(runtime)], root)
        else:
            candidates = [shutil.which(name) for name in ['python3.12', 'python3.11', 'python3.13']]
            candidates.append(sys.executable)
            selected = next((candidate for candidate in candidates if candidate and compatible_python(candidate)), None)
            if not selected:
                raise ValueError('Semantic search requires Python 3.11–3.13 (3.12 recommended). Install uv or a compatible Python; lexical mode works on Python 3.11+.')
            run([selected, '-m', 'venv', str(runtime)], root)
    if uv:
        run([uv, 'pip', 'install', '--python', str(python), '-r', str(root / 'requirements-search.txt')], root)
    else:
        run([str(python), '-m', 'pip', 'install', '-r', str(root / 'requirements-search.txt')], root)
    return python


def bootstrap(root: Path, ids: list[str], all_sources: bool, semantic: bool) -> None:
    root = root.resolve()
    if sys.version_info < (3, 11):
        raise ValueError('Python 3.11 or newer is required')
    if not shutil.which('git'):
        raise ValueError('Git is required; install Git and retry')
    entries = select_repositories(load_entries(root), ids, all_sources)
    if not entries:
        print('Catalog-only setup: indexing repository metadata; no source repositories selected.', flush=True)
    for entry in entries:
        print(f'Syncing {entry["id"]} at {entry["commit"]}', flush=True)
        sync_repository(root, entry)
    python = semantic_runtime(root) if semantic else Path(sys.executable)
    if semantic:
        print('Downloading and verifying the pinned embedding model for semantic search.', flush=True)
        run([str(python), str(root / 'embeddings.py'), 'setup', '--root', str(root)], root)
    run([str(python), str(root / 'toolkit.py'), 'index', '--semantic' if semantic else '--lexical'], root)
    print(f'Setup complete ({"semantic" if semantic else "lexical"}); agent registration is separate.', flush=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_selection_arguments(parser)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--lexical', action='store_true', help='Standard-library lexical index (default)')
    mode.add_argument('--semantic', action='store_true', help='Install an isolated search runtime and download the pinned model')
    args = parser.parse_args()
    try:
        bootstrap(ROOT, args.repo, args.all_sources, args.semantic)
    except (ValueError, RuntimeError, OSError, KeyError, subprocess.CalledProcessError) as error:
        parser.exit(1, f'Error: {error}\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
