#!/usr/bin/env python3
"""Open one PR per reviewed local catalog addition; never edit the source checkout.

Dry run by default. Git, authenticated gh and Gitleaks are required. Only literal
catalog data is copied; generator code and checks come from the published base.
"""
from __future__ import annotations

import argparse
import ast
from contextlib import contextmanager
from datetime import date
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile
import time

REPOSITORY = re.compile(r'[A-Za-z0-9][A-Za-z0-9_.-]*/[A-Za-z0-9][A-Za-z0-9_.-]*')
PUBLIC_FIELDS = {
    'id', 'repo', 'url', 'commit', 'description', 'kind', 'path', 'tags',
    'requirements', 'entrypoints', 'skill_paths', 'recommended_scope',
    'rationale', 'install_commands', 'setup_scope', 'agent_setup',
}
SETUP_FIELDS = {'action', 'working_directory', 'read_first', 'install',
                'configure', 'verify', 'record_result', 'source_revision'}
GENERATOR = Path('scripts/generate_catalog_docs.py')


def run(*args, cwd=None, timeout=180):
    result = subprocess.run([str(arg) for arg in args], cwd=cwd, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            timeout=timeout,
                            env={**os.environ, 'GH_HOST': 'github.com',
                                 'GH_PROMPT_DISABLED': '1', 'GIT_TERMINAL_PROMPT': '0'})
    if result.returncode:
        # Do not reproduce potentially private metadata in scheduler logs.
        raise RuntimeError(f'{Path(str(args[0])).name} {args[1]} failed (exit {result.returncode})')
    return result.stdout.strip()


def gh_json(*args):
    return json.loads(run('gh', *args))


def check_remote(remote, repository):
    if not REPOSITORY.fullmatch(repository):
        raise ValueError('Expected a GitHub owner/repository')
    expected = {f'https://github.com/{repository}', f'https://github.com/{repository}.git',
                f'git@github.com:{repository}', f'git@github.com:{repository}.git'}
    if remote not in expected:
        raise ValueError('Source origin does not match the explicit GitHub repository')


def check_push_destinations(remotes, repository):
    if not remotes.splitlines():
        raise ValueError('Missing push destination')
    for remote in remotes.splitlines():
        check_remote(remote, repository)


def validate_entry(tool):
    ident = tool.get('id', '')
    if not isinstance(ident, str) or not re.fullmatch(r'[a-z0-9-]+', ident):
        raise ValueError('Unsafe catalog ID')
    if set(tool) - PUBLIC_FIELDS:
        raise ValueError(f'{ident}: unknown metadata fields require manual review')
    repo = tool.get('repo', '')
    if not isinstance(repo, str) or not REPOSITORY.fullmatch(repo):
        raise ValueError(f'{ident}: invalid upstream repository')
    if tool.get('url') != f'https://github.com/{repo}':
        raise ValueError(f'{ident}: upstream URL must match repository without credentials')
    pin = tool.get('commit', '')
    if not isinstance(pin, str) or not re.fullmatch(r'[0-9a-f]{40}', pin):
        raise ValueError(f'{ident}: an exact source commit is required')
    if tool.get('path') != 'repos/' + repo.replace('/', '--'):
        raise ValueError(f'{ident}: source path must be repository-relative')
    for key in ('description', 'kind', 'recommended_scope', 'rationale', 'setup_scope'):
        if not isinstance(tool.get(key), str) or not tool[key].strip():
            raise ValueError(f'{ident}: missing {key}')
    for key in ('tags', 'requirements', 'entrypoints', 'skill_paths', 'install_commands'):
        if not isinstance(tool.get(key), list) or not all(isinstance(x, str) for x in tool[key]):
            raise ValueError(f'{ident}: invalid {key}')
    for value in tool['entrypoints'] + tool['skill_paths']:
        path = PurePosixPath(value)
        if not value or path.is_absolute() or '..' in path.parts or '\\' in value:
            raise ValueError(f'{ident}: source entry points must be relative')
    setup = tool.get('agent_setup')
    if not isinstance(setup, dict) or set(setup) - SETUP_FIELDS or setup.get('source_revision') != pin:
        raise ValueError(f'{ident}: setup must match the reviewed source revision')
    for key in ('install', 'verify'):
        if not isinstance(setup.get(key), str) or not setup[key].strip():
            raise ValueError(f'{ident}: missing setup {key}')
    if not isinstance(setup.get('read_first'), list) or not setup['read_first']:
        raise ValueError(f'{ident}: missing setup reading')
    text = json.dumps(tool)
    if re.search(r'/home/|/Users/|/mnt/[a-z]/Users/|[A-Za-z]:\\\\Users\\\\', text):
        raise ValueError(f'{ident}: private workstation paths require manual review')
    if len(text) > 100_000:
        raise ValueError(f'{ident}: metadata exceeds the automatic publication limit')


def new_entries(base, local):
    existing_ids = {x['id'] for x in base['tools']}
    existing_repos = {x['repo'].casefold() for x in base['tools']}
    ids, repos, additions = set(), set(), []
    for tool in local['tools']:
        ident, repo = tool['id'], tool['repo'].casefold()
        if ident in ids or repo in repos:
            raise ValueError('Duplicate catalog IDs or upstream repositories')
        ids.add(ident)
        repos.add(repo)
        if ident not in existing_ids:
            validate_entry(tool)
            if repo in existing_repos:
                raise ValueError(f'{ident}: upstream is already cataloged under another ID')
            additions.append(tool)
    return sorted(additions, key=lambda x: x['id'])


def categories_node(source):
    nodes = [node.value for node in ast.parse(source).body
             if isinstance(node, ast.Assign)
             and any(isinstance(t, ast.Name) and t.id == 'CATEGORIES' for t in node.targets)]
    if len(nodes) != 1 or not isinstance(nodes[0], ast.Dict):
        raise ValueError('Expected one literal CATEGORIES dictionary')
    categories = ast.literal_eval(nodes[0])
    if not all(isinstance(k, str) and isinstance(v, list)
               and all(isinstance(ident, str) for ident in v) for k, v in categories.items()):
        raise ValueError('Invalid catalog categories')
    return nodes[0], categories


def category_for(source, ident):
    _, categories = categories_node(source)
    matches = [name for name, ids in categories.items() for item in ids if item == ident]
    if len(matches) != 1:
        raise ValueError(f'{ident}: assign exactly one category before publication')
    return matches[0]


def add_category(source, category, ident):
    node, categories = categories_node(source)
    if any(ident in ids for ids in categories.values()):
        raise ValueError(f'{ident}: already categorized in the published generator')
    # AST columns count UTF-8 bytes. Splice literal data without running or
    # copying any executable code from the potentially unfinished local script.
    encoded = source.encode()
    lines = encoded.splitlines(keepends=True)
    def end_offset(item):
        return sum(map(len, lines[:item.end_lineno - 1])) + item.end_col_offset - 1
    if category in categories:
        value = next(value for key, value in zip(node.keys, node.values)
                     if ast.literal_eval(key) == category)
        pos = end_offset(value)
        prefix = '' if not categories[category] else ('' if encoded[:pos].rstrip().endswith(b',') else ',')
        addition = f'{prefix} {ident!r}'
    else:
        pos = end_offset(node)
        prefix = '' if not categories or encoded[:pos].rstrip().endswith(b',') else ','
        addition = f'{prefix}\n    {category!r}: [{ident!r}],\n'
    return (encoded[:pos] + addition.encode() + encoded[pos:]).decode()


def write_candidate(root, tool, category, *, revision_date=None):
    manifest = root / 'manifest.json'
    data = json.loads(manifest.read_text())
    data['tools'].append(tool)
    data['tools'].sort(key=lambda x: x['id'])
    data['catalog_revision_date'] = revision_date or date.today().isoformat()
    manifest.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    script = root / GENERATOR
    script.write_text(add_category(script.read_text(), category, tool['id']))


def existing_pr(prs):
    # A closed PR is a deliberate review decision, not a request to recreate it.
    # A matching branch name in an unrelated fork must not suppress this queue.
    prs = [pr for pr in prs if pr.get('isCrossRepository') is False]
    return next((pr for pr in prs if pr['state'] == 'OPEN'), prs[0] if prs else None)


def recovery_context(source, base, pushed):
    # Rebuild from the original published ancestor and date, not today's main.
    # The complete reconstructed tree must match before this branch is reused.
    ancestor = run('git', 'merge-base', base, pushed, cwd=source)
    data = json.loads(run('git', 'show', f'{pushed}:manifest.json', cwd=source))
    revision = date.fromisoformat(data['catalog_revision_date']).isoformat()
    return ancestor, revision


def push_candidate(root, branch):
    # An inherited push.followTags setting must not publish unreviewed refs.
    run('git', 'push', '--no-follow-tags', 'origin', f'HEAD:refs/heads/{branch}', cwd=root)


@contextmanager
def isolated_tree(source, base):
    with tempfile.TemporaryDirectory(prefix='toolkit-catalog-') as temporary:
        root = Path(temporary) / 'worktree'
        run('git', 'worktree', 'add', '--detach', root, base, cwd=source)
        try:
            yield root
        finally:
            run('git', 'worktree', 'remove', '--force', root, cwd=source)


def publish_addition(args, tool, category, base, snapshot):
    ident = tool['id']
    branch = f'catalog/add-{ident}'
    prior = existing_pr(gh_json('pr', 'list', '--repo', args.repository, '--head', branch,
                                '--state', 'all', '--limit', '100', '--json', 'state,url,isCrossRepository'))
    if prior:
        print(f"{ident}: {prior['state'].lower()} PR already exists: {prior['url']}")
        return
    upstream = run('gh', 'api', f"repos/{tool['repo']}/commits/{tool['commit']}", '--jq', '.sha')
    if upstream != tool['commit']:
        raise ValueError(f'{ident}: upstream source revision could not be verified')
    check_push_destinations(run('git', 'remote', 'get-url', '--push', '--all', 'origin',
                                cwd=args.source), args.repository)
    # An earlier push may have succeeded even when PR creation timed out.
    remote = run('git', 'ls-remote', '--heads', 'origin', f'refs/heads/{branch}', cwd=args.source)
    pushed, revision_date = None, None
    if remote:
        pushed = remote.split()[0]
        if not re.fullmatch(r'[0-9a-f]{40}', pushed):
            raise ValueError('Invalid remote branch response')
        run('git', 'fetch', 'origin', f'refs/heads/{branch}', cwd=args.source)
        base, revision_date = recovery_context(args.source, base, pushed)
    with isolated_tree(args.source, base) as root:
        write_candidate(root, tool, category, revision_date=revision_date)
        run(sys.executable, GENERATOR, cwd=root)
        run(sys.executable, GENERATOR, '--check', cwd=root)
        run(sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-q', cwd=root, timeout=300)
        paths = ['manifest.json', str(GENERATOR), 'catalog.md', 'docs/wiki/Tool-Catalog.md',
                 f'docs/wiki/tools/{ident}.md']
        run('git', 'add', '--', *paths, cwd=root)
        changed = run('git', 'diff', '--cached', '--name-only', cwd=root).splitlines()
        if set(changed) - set(paths):
            raise ValueError('Candidate includes files outside the catalog allowlist')
        run('git', 'diff', '--cached', '--check', cwd=root)
        run(args.gitleaks, 'git', '--staged', '--redact', '--no-banner',
            '--ignore-gitleaks-allow', '--config', '.gitleaks.toml', cwd=root)
        if pushed and run('git', 'write-tree', cwd=root) != run('git', 'rev-parse', f'{pushed}^{{tree}}', cwd=root):
            raise ValueError('Previously pushed branch differs from the validated addition; reconcile manually')
        if any(path.read_bytes() != content for path, content in snapshot.items()):
            raise RuntimeError('Local catalog changed during validation; retry after editing finishes')
        print(f'{ident}: validated catalog, documentation, tests, upstream pin and secrets')
        if not args.publish:
            print(f'{ident}: dry run; would open {branch}')
            return
        check_push_destinations(run('git', 'remote', 'get-url', '--push', '--all', 'origin', cwd=root), args.repository)
        if not pushed:
            user = gh_json('api', 'user')
            email = f"{user['id']}+{user['login']}@users.noreply.github.com"
            run('git', '-c', f"user.name={user['login']}", '-c', f'user.email={email}',
                'commit', '-m', f'Add {ident} to the reviewed tool catalog', cwd=root)
            push_candidate(root, branch)
        body = root.parent / 'pr-body.md'
        body.write_text(
            f'Adds `{ident}` from [{tool["repo"]}]({tool["url"]}) at reviewed source '
            f'`{tool["commit"]}`, including setup requirements and generated catalog pages.\n\n'
            'Created from the new local catalog entry. Existing entry edits, private state, '
            'downloaded sources and runtimes are excluded.\n\n'
            'Validation: source commit verified upstream; manager unit tests, generated documentation '
            'and link checks, diff checks, and staged Gitleaks scan passed. Optional runtime tests '
            'may skip locally; hosted CI provides additional checks. Catalog membership does not '
            'assert that the upstream application has been installed or tested.\n\n'
            '<!-- toolkit-catalog-addition:v1 -->\n')
        print(run('gh', 'pr', 'create', '--repo', args.repository, '--base', args.base,
                  '--head', branch, '--title', f'Add {ident} to the reviewed tool catalog',
                  '--body-file', body, cwd=root))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--repository', required=True, help='Explicit GitHub owner/repository')
    parser.add_argument('--base', default='main')
    parser.add_argument('--gitleaks', default='gitleaks')
    parser.add_argument('--publish', action='store_true')
    parser.add_argument('--settle-seconds', type=int, default=120)
    args = parser.parse_args()
    args.source = args.source.resolve()
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._/-]*', args.base) or '..' in args.base:
        parser.error('Invalid base branch')
    if args.settle_seconds < 0:
        parser.error('--settle-seconds cannot be negative')
    try:
        # Only scheduling is POSIX-specific; this script fails clearly on other hosts.
        import fcntl
        state = Path(os.environ.get('XDG_STATE_HOME', str(Path.home() / '.local/state'))) / 'ai-toolkit'
        state.mkdir(parents=True, exist_ok=True, mode=0o700)
        with (state / 'catalog-pr.lock').open('w') as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                print('Another catalog check is active; skipping.')
                return 0
            check_remote(run('git', 'remote', 'get-url', 'origin', cwd=args.source), args.repository)
            paths = [args.source / 'manifest.json', args.source / GENERATOR]
            if any(time.time() - path.stat().st_mtime < args.settle_seconds for path in paths):
                print('Catalog editing is recent; waiting until the next check.')
                return 0
            snapshot = {path: path.read_bytes() for path in paths}
            tracking = f'refs/remotes/origin/{args.base}'
            run('git', 'fetch', 'origin', f'refs/heads/{args.base}:{tracking}', cwd=args.source)
            base = run('git', 'rev-parse', tracking, cwd=args.source)
            published = json.loads(run('git', 'show', f'{base}:manifest.json', cwd=args.source))
            local = json.loads(snapshot[paths[0]])
            additions = new_entries(published, local)
            if not additions:
                print('No unpublished catalog additions.')
            for tool in additions:
                category = category_for(snapshot[paths[1]].decode(), tool['id'])
                publish_addition(args, tool, category, base, snapshot)
        return 0
    except (ValueError, RuntimeError, OSError, subprocess.TimeoutExpired) as error:
        print(f'Catalog check stopped: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
