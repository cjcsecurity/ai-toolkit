#!/usr/bin/env python3
"""Print local RAG MCP configuration for a coding agent without changing its settings."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLIENTS = ('claude', 'cursor', 'gemini', 'vscode', 'copilot-cli', 'windsurf',
           'cline', 'roo', 'continue', 'codex', 'opencode', 'generic')


def render_config(root: Path, client: str, *, python: Path | None = None,
                  data_root: Path | None = None) -> str:
    if client not in CLIENTS:
        raise ValueError(f'Unknown client: {client}')
    root = root.expanduser().resolve()
    data_root = (data_root or root).expanduser().resolve()
    server = root / 'rag_server.py'
    if not server.is_file():
        raise ValueError(f'Checkout does not contain {server}')
    # Do not resolve a venv's interpreter symlink: its location selects the venv.
    python = (python or data_root / 'runtime/search/bin/python').expanduser().absolute()
    if not python.is_file() or not os.access(python, os.X_OK):
        raise ValueError(f'Python runtime unavailable at {python}. Install requirements-rag.txt '
                         'in runtime/search, or pass --python /absolute/path/to/venv/bin/python.')
    if not data_root.is_dir():
        raise ValueError(f'Toolkit data directory does not exist: {data_root}')
    command = str(python)
    args = [str(server), '--root', str(data_root)]
    entry = {'command': command, 'args': args}
    if client == 'codex':
        # JSON basic strings/arrays are valid TOML for these string-only values.
        return ('[mcp_servers.ai-toolkit]\n'
                f'command = {json.dumps(command, ensure_ascii=False)}\n'
                f'args = {json.dumps(args, ensure_ascii=False)}\n')
    if client == 'opencode':
        config = {'mcp': {'ai-toolkit': {'type': 'local', 'command': [command, *args]}}}
    elif client == 'vscode':
        config = {'servers': {'ai-toolkit': {'type': 'stdio', **entry}}}
    else:
        if client == 'claude':
            entry['type'] = 'stdio'
        elif client == 'copilot-cli':
            entry['type'] = 'local'
            entry['tools'] = ['search_tools', 'recommend_tools', 'get_tool', 'read_tool_source', 'search_status']
        config = {'mcpServers': {'ai-toolkit': entry}}
    return json.dumps(config, indent=2, ensure_ascii=False) + '\n'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, epilog=(
        'Prints JSON (TOML for Codex) to stdout. Merge the ai-toolkit entry into the host config; '
        'do not overwrite existing settings. See docs/wiki/Agent-Integration.md.'))
    parser.add_argument('--client', choices=CLIENTS, required=True)
    parser.add_argument('--python', type=Path, help='Path to a Python with requirements-rag.txt installed')
    parser.add_argument('--data-root', type=Path,
                        default=Path(os.environ.get('AI_TOOLKIT_HOME', ROOT)),
                        help='Catalog/index directory (default: AI_TOOLKIT_HOME or this checkout)')
    args = parser.parse_args()
    try:
        print(render_config(ROOT, args.client, python=args.python, data_root=args.data_root), end='')
    except (ValueError, OSError) as error:
        parser.exit(1, f'Error: {error}\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
