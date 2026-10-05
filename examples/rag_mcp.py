#!/usr/bin/env python3
"""Retrieve a real evidence bundle over MCP for an agent to turn into an answer."""
import argparse
import asyncio
import json
from pathlib import Path
import sys

from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from toolkit import atomic_json

DEFAULT_CONSTRAINTS = 'Inspect source evidence and installation requirements before choosing.'


async def retrieve(query, root, constraints=DEFAULT_CONSTRAINTS):
    parameters = StdioServerParameters(command=sys.executable,
        args=[str(ROOT/'rag_server.py'), '--root', str(root)])
    async with stdio_client(parameters, errlog=sys.stderr) as streams:
        async with ClientSession(*streams) as client:
            await client.initialize()
            response = await client.call_tool('recommend_tools', {
                'query': query, 'constraints': constraints,
                'limit': 3, 'budget': 24000,
            })
            if response.is_error:
                raise RuntimeError(str(response.content))
            return response.structured_content


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', nargs='?', default='Python HTML extraction that finds the same product elements after a website changes its layout')
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--constraints', default=DEFAULT_CONSTRAINTS,
                        help='Project constraints supplied to the recommending agent')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = asyncio.run(retrieve(args.query, args.root, constraints=args.constraints))
    if args.output:
        atomic_json(args.output, result)
        print(f'Evidence saved to {args.output}; generate an answer using its sources and instructions.')
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
