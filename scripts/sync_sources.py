#!/usr/bin/env python3
"""Fetch explicitly selected catalog sources at their recorded immutable revisions."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def load_entries(root: Path) -> list[dict]:
    data = json.loads((root / 'manifest.json').read_text(encoding='utf-8'))
    entries = data['tools']
    if not isinstance(entries, list):
        raise ValueError('manifest.json tools must be a list')
    ids = [entry['id'] for entry in entries]
    if len(ids) != len(set(ids)):
        raise ValueError('manifest.json contains duplicate repository IDs')
    return entries


def select_repositories(entries: list[dict], ids: list[str], all_sources: bool) -> list[dict]:
    if all_sources and ids:
        raise ValueError('Choose --all or --repo, not both')
    known = {entry['id'] for entry in entries}
    unknown = set(ids) - known
    if unknown:
        raise ValueError(f'Unknown repository ID(s): {", ".join(sorted(unknown))}; run toolkit list')
    return list(entries) if all_sources else [entry for entry in entries if entry['id'] in ids]


def _git(*args: str, cwd: Path | None = None) -> str:
    result = subprocess.run(['git', *args], cwd=cwd, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(f'git {args[0]} failed: {result.stderr.strip()}')
    return result.stdout.strip()


def _destination(root: Path, entry: dict) -> Path:
    repo = entry.get('repo', '')
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo):
        raise ValueError('Repository must be a GitHub owner/name')
    expected_urls = {f'https://github.com/{repo}', f'https://github.com/{repo}.git'}
    if entry.get('url') not in expected_urls:
        raise ValueError(f'{entry.get("id")}: source URL must be its HTTPS GitHub repository')
    if not re.fullmatch(r'[0-9a-fA-F]{40}', entry.get('commit', '')):
        raise ValueError(f'{entry.get("id")}: commit must be a full 40-character SHA')
    expected_path = f'repos/{repo.replace("/", "--")}'
    if entry.get('path') != expected_path:
        raise ValueError(f'{entry.get("id")}: path must be {expected_path}')
    root = root.resolve()
    destination = root / expected_path
    if not destination.resolve().is_relative_to(root):
        raise ValueError(f'{entry.get("id")}: source path escapes the toolkit root')
    if destination.is_symlink():
        raise ValueError(f'Refusing symlink checkout {destination}; move it aside explicitly')
    return destination


def sync_repository(root: Path, entry: dict) -> Path:
    """Clone one pinned source atomically; preserve all pre-existing user work."""
    destination = _destination(Path(root), entry)
    commit = entry['commit'].lower()
    if destination.exists():
        if not (destination / '.git').exists():
            raise ValueError(f'Refusing existing non-Git directory {destination}; move it aside explicitly')
        if _git('status', '--porcelain', '--untracked-files=all', cwd=destination):
            raise ValueError(f'Refusing dirty checkout {destination}; commit or move your changes first')
        current = _git('rev-parse', 'HEAD', cwd=destination)
        if current != commit:
            raise ValueError(f'Refusing revision change in {destination}: found {current}, expected {commit}; move the checkout aside and retry')
        return destination
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=f'.{destination.name}-', dir=destination.parent))
    try:
        _git('init', str(temporary))
        _git('remote', 'add', 'origin', entry['url'], cwd=temporary)
        _git('fetch', '--depth=1', 'origin', commit, cwd=temporary)
        _git('-c', 'core.hooksPath=/dev/null', 'checkout', '--detach', 'FETCH_HEAD', cwd=temporary)
        actual = _git('rev-parse', 'HEAD', cwd=temporary)
        if actual != commit:
            raise RuntimeError(f'Fetched revision mismatch: expected {commit}, got {actual}')
        if destination.exists() or destination.is_symlink():
            raise ValueError(f'Checkout appeared during fetch: {destination}; refusing to replace it')
        temporary.rename(destination)
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)
    return destination


def add_selection_arguments(parser: argparse.ArgumentParser, *, required: bool = False) -> None:
    selection = parser.add_mutually_exclusive_group(required=required)
    selection.add_argument('--all', dest='all_sources', action='store_true', help='Fetch every catalog source (no upstream runtimes)')
    selection.add_argument('--repo', action='append', default=[], metavar='ID', help='Fetch a repository ID; repeat to select several')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_selection_arguments(parser, required=True)
    args = parser.parse_args()
    try:
        entries = select_repositories(load_entries(ROOT), args.repo, args.all_sources)
        for entry in entries:
            print(f'{entry["id"]}: {sync_repository(ROOT, entry)}')
    except (ValueError, RuntimeError, OSError, KeyError) as error:
        parser.exit(1, f'Error: {error}\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
