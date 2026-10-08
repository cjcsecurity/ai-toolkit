#!/usr/bin/env python3
"""Render portable catalog/wiki pages from reviewed manifest metadata.

Run from any directory; --check verifies generated output and local Markdown links.
Runtime state, local checkout presence, and private usage records are never rendered.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import quote, unquote

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    'Engineering and code intelligence': [
        'agent-skills', 'ast-grep', 'codebase-memory-mcp', 'context7', 'ecc',
        'gh-aw', 'loop-engineering', 'matt-pocock-skills', 'open-code-review',
        'ponytail', 'serena', 'rea', 'e2e',
    ],
    'Design and interfaces': [
        'animate-ui', 'archify', 'awesome-claude-design', 'huashu-design',
        'impeccable', 'open-design', 'taste-skill', 'photocraft', 'text-to-cad',
    ],
    'Browsers, research, and web data': [
        'agent-reach', 'autocli', 'browser-harness', 'chrome-devtools-mcp',
        'cloakbrowser', 'crucix', 'firecrawl', 'opencli', 'playwright',
        'public-apis', 'free-for-dev', 'scrapling', 'moli',
     'agent-browser'],
    'Security and assessment': [
        'agentic-bug-hunter', 'anthropic-cybersecurity-skills', 'cyberstrike',
        'hackingtool', 'hexstrike-ai', 'pentagi', 'security-audit-skill',
        'semgrep', 'shannon', 'skillspector', 'strix',
    ],
    'AI infrastructure and retrieval': [
        'agentmemory', 'arcbox', 'docling', 'langfuse', 'laya', 'litellm',
        'opensandbox', 'promptfoo', 'rag-anything', 'ruflo',
    ],
    'Finance and markets': ['finance-skills', 'financial-services', 'openalice'],
    'Writing, video, and audio': [
        'brag', 'humanizer', 'hyperframes', 'hypit', 'pixelle-video',
        'recordly', 'voicestudio', 'filmcraft', 'openmontage',
    ],

    'Games and modding': ['universal-modder'],
}


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def upstream_path(tool, path):
    leaf = PurePosixPath(path).name
    kind = 'blob' if PurePosixPath(path).suffix or leaf in {'Dockerfile', 'Makefile'} else 'tree'
    return f"{tool['url']}/{kind}/{tool['commit']}/{quote(path, safe='/')}"


def bullets(values):
    return '\n'.join(f'- {v}' for v in values)


def render_tool(tool, category):
    ident = tool['id']
    skills = tool.get('skill_paths', [])
    setup = tool.get('agent_setup', {})
    parts = [
        f'# {ident}',
        f"{tool['description']}",
        f"[Upstream repository]({tool['url']}) · [Pinned source]({tool['url']}/tree/{tool['commit']}) · [All tools](../Tool-Catalog.md)",
        '| Catalog detail | Value |\n| --- | --- |\n' + '\n'.join([
            f'| Category | {category} |',
            f"| Operating model | {cell(tool['kind'])} |",
            f"| Recommended scope | {cell(tool.get('recommended_scope', 'on-demand'))} |",
            f'| Registered production skill paths | {len(skills):,} |',
            f"| Reviewed source commit | `{tool['commit']}` |",
        ]),
        '## Purpose and use cases',
        tool.get('rationale', ''),
        '**Discovery tags:** ' + ', '.join(f'`{tag}`' for tag in tool.get('tags', [])) + '.',
        'Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.',
        '## Requirements and dependencies',
        bullets(tool.get('requirements', [])) or 'Read the pinned upstream guide for task-specific requirements.',
        '## Setup guidance',
        f"**Setup scope:** {tool.get('setup_scope', 'Select an isolated or project-local environment appropriate to this tool.')}",
    ]
    labels = {
        'action': 'Next action',
        'working_directory': 'Working directory',
        'install': 'Installation approach',
        'configure': 'Configuration',
        'verify': 'Verification to perform',
        'record_result': 'Local record',
    }
    for key, label in labels.items():
        if setup.get(key):
            parts.append(f'**{label}:** {setup[key]}')
    read_first = setup.get('read_first', [])
    if read_first:
        parts.extend(['### Read first', 'After downloading this source, read the selected instructions in full:',
                      '```bash\n' + '\n'.join(read_first) + '\n```'])
    commands = tool.get('install_commands', [])
    parts.append('### Documented commands and alternatives')
    if commands:
        parts.append('These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.')
        for i, command in enumerate(commands, 1):
            parts.append(f'Example {i}:\n\n```bash\n{command}\n```')
    else:
        parts.append('No package installation command is recorded. Follow the setup guidance and pinned upstream instructions; source-only guidance may need no runtime.')
    parts.extend(['## Source entry points', bullets([
        f'[{path}]({upstream_path(tool, path)})' for path in tool.get('entrypoints', [])
    ]) or 'See the pinned upstream repository.'])
    parts.extend(['## Skills and retrieval',
                  f'The manifest registers **{len(skills):,} production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.'])
    if skills:
        parts.append(bullets(f'[{path}]({upstream_path(tool, path)})' for path in skills[:12]))
        if len(skills) > 12:
            parts.append(f'Showing 12 of {len(skills):,} registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).')
    else:
        parts.append('No production Agent Skill path is registered. Search its documentation and source entry points instead.')
    query = ' '.join(tool.get('tags', [])[:2]) or 'setup'
    parts.append(f'```bash\nbin/toolkit show {ident}\nbin/toolkit search "{query}" --repo {ident}\nbin/toolkit docs {ident} "installation"\n```')
    parts.extend(['## Provenance and availability',
                  f"This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [{tool['repo']} at `{tool['commit'][:12]}`]({tool['url']}/tree/{tool['commit']}). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.",
                  'The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.',
                  f'```bash\npython3 scripts/bootstrap.py --repo {ident} --lexical\n```',
                  'Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.',
                  '[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)'])
    return '\n\n'.join(parts) + '\n'


def render_index(tools, prefix):
    by_id = {t['id']: t for t in tools}
    heading = '# Tool catalog\n\n'
    intro = (f'**{len(tools)} reviewed tools and collections**, grouped by their main use. '
             'Categories are navigation aids; many tools span several areas. Each tool page includes requirements, setup alternatives, skill counts, and links to its exact upstream source revision.\n\n'
             'Catalog membership does not imply downloaded source or a configured runtime. Global recommendations are optional adoption choices, never automatic installation.\n\n')
    sections = []
    for category, ids in CATEGORIES.items():
        rows = ['| Tool | Type | Skills | Purpose |', '| --- | --- | ---: | --- |']
        for ident in ids:
            t = by_id[ident]
            rows.append(f"| [{ident}]({prefix}{ident}.md) | {cell(t['kind'])} | {len(t.get('skill_paths', [])):,} | {cell(t['description'])} |")
        sections.append(f'## {category}\n\n' + '\n'.join(rows))
    return heading + intro + '\n\n'.join(sections) + '\n'


def output_files():
    tools = json.loads((ROOT / 'manifest.json').read_text())['tools']
    expected = [ident for ids in CATEGORIES.values() for ident in ids]
    actual = [t['id'] for t in tools]
    if len(expected) != len(set(expected)) or set(expected) != set(actual):
        raise ValueError('Every manifest entry must appear in exactly one catalog category')
    if len(actual) != len(set(actual)):
        raise ValueError('Duplicate manifest IDs')
    pages = {
        Path('catalog.md'): render_index(tools, 'docs/wiki/tools/'),
        Path('docs/wiki/Tool-Catalog.md'): render_index(tools, 'tools/'),
    }
    category_by_id = {ident: cat for cat, ids in CATEGORIES.items() for ident in ids}
    for tool in tools:
        if not re.fullmatch(r'[a-z0-9-]+', tool['id']):
            raise ValueError('Unsafe catalog ID')
        if not re.fullmatch(r'[0-9a-f]{40}', tool['commit']):
            raise ValueError(f"Missing immutable source pin: {tool['id']}")
        pages[Path(f"docs/wiki/tools/{tool['id']}.md")] = render_tool(tool, category_by_id[tool['id']])
    return pages


def check_links():
    errors = []
    paths = [ROOT / 'README.md', ROOT / 'CONTRIBUTING.md', ROOT / 'catalog.md', *(ROOT / 'docs/wiki').rglob('*.md')]
    for path in paths:
        if not path.exists():
            continue
        # The managed docs use ordinary inline Markdown links without nested URLs.
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            target_path = unquote(target.split('#', 1)[0])
            if target_path and not (path.parent / target_path).exists():
                errors.append(f'{path.relative_to(ROOT)}: missing link target {target}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if generated docs differ or local links are broken')
    args = parser.parse_args()
    pages = output_files()
    errors = []
    expected_tool_files = {ROOT / p for p in pages if str(p).startswith('docs/wiki/tools/')}
    for extra in (ROOT / 'docs/wiki/tools').glob('*.md'):
        if extra not in expected_tool_files:
            errors.append(f'Unexpected generated tool page: {extra.relative_to(ROOT)}')
    for relative, content in pages.items():
        target = ROOT / relative
        if args.check:
            if not target.exists() or target.read_text() != content:
                errors.append(f'Out of date: {relative}')
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content)
    if args.check:
        errors.extend(check_links())
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f"{'Checked' if args.check else 'Generated'} {len(expected_tool_files)} tool pages and 2 catalog indexes.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
