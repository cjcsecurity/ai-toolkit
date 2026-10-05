#!/usr/bin/env python3
"""Short-lived Serena or Chrome MCP sessions; discover schemas only when requested.

Use bin/toolkit-mcp (or toolkit-serena) to use the installed MCP SDK.
Each invocation starts a fresh server; isolated Chrome pages do not persist
between invocations; use batch for a multi-step session.
The timeout bounds session work; SDK cleanup adds a bounded shutdown grace period.
Serena may create project-local .serena metadata. Global runtime state is kept
in this toolkit's state/serena directory, separate from the user's ~/.serena.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import shutil
from pathlib import Path
import sys
import tempfile

ROOT = Path(os.environ.get('AI_TOOLKIT_HOME', Path(__file__).resolve().parent)).expanduser().resolve()
SERENA = os.environ.get('TOOLKIT_SERENA_COMMAND', 'serena')
CHROME = os.environ.get('TOOLKIT_CHROME_COMMAND', str(Path(__file__).resolve().parent / 'bin/toolkit-chrome-mcp'))
TRUNCATION = '\n[truncated: increase --budget to see more]\n'


class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)


def budget_value(value):
    number = int(value)
    if number < 128:
        raise argparse.ArgumentTypeError('--budget must be at least 128 characters')
    return number


def timeout_value(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError('--timeout must be a finite positive number')
    return number


def parser():
    cli = ArgumentParser(description=__doc__)
    cli.add_argument('--server', choices=('serena', 'chrome'), default='serena')
    commands = cli.add_subparsers(dest='command', required=True)
    discover = commands.add_parser('tools', help='list names, or one exact tool schema')
    discover.add_argument('--tool', help='return the named tool definition as JSON')
    call = commands.add_parser('call', help='call one tool on the selected server')
    call.add_argument('tool')
    call.add_argument('--args', required=True, help='JSON object matching the tool schema')
    batch = commands.add_parser('batch', help='run up to 20 sequential calls in one session; stop on tool error')
    batch.add_argument('--steps', required=True, help='JSON array of {tool: NAME, args: OBJECT}')
    for command in (discover, call, batch):
        command.add_argument('--server', choices=('serena', 'chrome'), default=argparse.SUPPRESS)
        command.add_argument('--project', help='Serena: required project directory; Chrome: optional working directory (default cwd)')
        command.add_argument('--budget', type=budget_value, default=8000, help='maximum output characters, including truncation notice (minimum 128)')
        command.add_argument('--timeout', type=timeout_value, default=90, help='session timeout in seconds, plus bounded SDK shutdown grace')
    return cli


def emit(text, budget, stream, *, json_output=False):
    text = text.rstrip('\n') + '\n'
    if len(text) > budget:
        if json_output:
            text = json.dumps({'truncated': True, 'required_budget': len(text),
                               'message': 'Response omitted; increase --budget.'}) + '\n'
        else:
            text = text[:budget-len(TRUNCATION)] + TRUNCATION
    stream.write(text)


def exception_message(error):
    children = getattr(error, 'exceptions', None)
    if children:
        return '; '.join(exception_message(child) for child in children)
    return str(error) or type(error).__name__


async def execute(options, project, arguments):
    import anyio
    from mcp import ClientSession, types
    from mcp.client.stdio import StdioServerParameters, stdio_client

    if options.server == 'serena':
        server = StdioServerParameters(
            command=SERENA,
            args=['start-mcp-server', '--project', str(project), '--context', 'codex',
                  '--agent-interface', 'tools', '--transport', 'stdio',
                  '--enable-web-dashboard', 'false', '--open-web-dashboard', 'false',
                  '--enable-gui-log-window', 'false', '--log-level', 'ERROR',
                  '--tool-timeout', str(options.timeout)],
            cwd=str(project),
            env={"SERENA_HOME": str(ROOT / "state" / "serena")},
        )
    else:
        server = StdioServerParameters(command=CHROME, args=[], cwd=str(project),
            env={key: value for key, value in os.environ.items() if key.startswith('TOOLKIT_') or key == 'AI_TOOLKIT_HOME'})
    # Keep verbose server startup logs out of the model's output/context budget.
    with tempfile.TemporaryFile(mode='w+', encoding='utf-8') as server_log:
        with anyio.fail_after(options.timeout):
            async with stdio_client(server, errlog=server_log) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    if options.command in ('call', 'batch'):
                        steps = [{'tool': options.tool, 'args': arguments}] if options.command == 'call' else arguments
                        results = []
                        failed = False
                        for index, step in enumerate(steps):
                            result = await session.call_tool(step['tool'], arguments=step['args'])
                            payload = result.model_dump(mode='json', by_alias=True, exclude_none=True)
                            failed = bool(getattr(result, 'is_error', False))
                            if options.command == 'call':
                                return json.dumps(payload, ensure_ascii=False, indent=2), int(failed)
                            results.append({'index': index, 'tool': step['tool'], 'isError': failed, 'result': payload})
                            if failed:
                                break
                        return json.dumps({'results': results, 'stopped_on_error': failed}, ensure_ascii=False, indent=2), int(failed)
                    tools = []
                    cursor = None
                    while True:
                        page = await session.list_tools(params=types.PaginatedRequestParams(cursor=cursor))
                        tools.extend(page.tools)
                        cursor = page.next_cursor
                        if not cursor:
                            break
                    if options.tool:
                        for tool in tools:
                            if tool.name == options.tool:
                                return json.dumps(tool.model_dump(mode='json', by_alias=True, exclude_none=True), ensure_ascii=False, indent=2), 0
                        raise ValueError(f'Unknown {options.server} tool: {options.tool}')
                    return '\n'.join(f'{tool.name}: {" ".join((tool.description or "").split())[:180]}' for tool in tools), 0


def main(argv=None):
    options = None
    try:
        options = parser().parse_args(argv)
        if options.server == 'serena' and not options.project:
            raise ValueError('--project is required for Serena')
        project = Path(options.project or Path.cwd()).expanduser().resolve(strict=True)
        if not project.is_dir():
            raise ValueError('--project must name an existing directory')
        if options.server == 'serena' and (project == Path.home().resolve() or project == Path(project.anchor)):
            raise ValueError('--project must be a specific project directory, not home or filesystem root')
        arguments = json.loads(options.args) if options.command == 'call' else None
        if options.command == 'call' and not isinstance(arguments, dict):
            raise ValueError('--args must be a JSON object')
        if options.command == 'batch':
            arguments = json.loads(options.steps)
            if not isinstance(arguments, list) or not 1 <= len(arguments) <= 20:
                raise ValueError('--steps must be a JSON array with 1 to 20 calls')
            for index, step in enumerate(arguments):
                if not isinstance(step, dict) or not isinstance(step.get('tool'), str) or not step['tool'].strip() or not isinstance(step.get('args'), dict):
                    raise ValueError(f'Batch step {index} must contain a nonempty tool string and args object')
        try:
            import anyio
            import mcp
        except ImportError as exc:
            raise RuntimeError('Optional MCP dependencies are missing. Create runtime/mcp with Python 3.11+ and install requirements-mcp.txt there, then use bin/toolkit-mcp.') from exc
        command = SERENA if options.server == 'serena' else CHROME
        if not shutil.which(command):
            variable = 'TOOLKIT_SERENA_COMMAND' if options.server == 'serena' else 'TOOLKIT_CHROME_COMMAND'
            raise ValueError(f'{options.server} executable unavailable: {command}. Install it explicitly and set {variable} to its executable path.')
        output, code = anyio.run(execute, options, project, arguments)
        emit(output, options.budget, sys.stdout,
             json_output=options.command != 'tools' or bool(options.tool))
        return code
    except SystemExit as error:
        return int(error.code or 0)
    except TimeoutError:
        emit(f'{options.server} session timed out after {options.timeout:g} seconds; subprocess cleanup completed.', options.budget, sys.stderr)
        return 124
    except KeyboardInterrupt:
        emit('MCP session interrupted.', options.budget if options else 8000, sys.stderr)
        return 130
    except Exception as error:
        emit(f'MCP error: {exception_message(error)}', options.budget if options else 8000, sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
