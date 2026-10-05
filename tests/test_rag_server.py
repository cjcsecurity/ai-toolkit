import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from rag_fixture import make_library

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(importlib.util.find_spec('mcp'), 'Install requirements-rag.txt for MCP integration tests')
class RagServerTests(unittest.IsolatedAsyncioTestCase):
    async def test_real_stdio_session_recommendation_cli_parity_and_errors(self):
        from contextlib import AsyncExitStack
        from mcp import ClientSession
        from mcp.client.stdio import StdioServerParameters, stdio_client
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            library = make_library(root)
            params = StdioServerParameters(command=sys.executable,
                args=[str(ROOT / 'rag_server.py'), '--root', str(root)])
            async with AsyncExitStack() as stack:
                stderr = stack.enter_context(tempfile.TemporaryFile(mode='w+'))
                streams = await stack.enter_async_context(stdio_client(params, errlog=stderr))
                client = await stack.enter_async_context(ClientSession(*streams))
                await client.initialize()
                catalog = await client.list_tools()
                self.assertEqual({tool.name for tool in catalog.tools},
                    {'search_tools', 'recommend_tools', 'get_tool', 'read_tool_source', 'search_status'})
                result = await client.call_tool('recommend_tools', {'query': 'checkpoints', 'lexical_only': True})
                self.assertFalse(result.is_error)
                payload = result.structured_content
                cli = subprocess.run([sys.executable, str(ROOT/'toolkit.py'), '--root', str(root),
                    'recommend', 'checkpoints', '--lexical'], capture_output=True, text=True, check=True)
                self.assertEqual(payload, json.loads(cli.stdout))
                for arguments in ({'query': ''}, {'query': 'checkpoints', 'limit': 0},
                                  {'query': 'checkpoints', 'budget': 3}):
                    error = await client.call_tool('search_tools', arguments)
                    self.assertTrue(error.is_error)
                error = await client.call_tool('read_tool_source', {'tool_id': 'platform', 'path': '../../manifest.json'})
                self.assertTrue(error.is_error)
                page = await client.call_tool('read_tool_source', {'tool_id': 'platform', 'path': 'skills/main/SKILL.md'})
                self.assertIn('Persist checkpoints', page.structured_content['text'])
                self.assertIsNone(page.structured_content['next_offset'])
                metadata = await client.call_tool('get_tool', {'tool_id': 'platform'})
                self.assertEqual(json.loads(metadata.structured_content['text'])['requirements'], ['Python 3.12'])
                status = await client.call_tool('search_status', {})
                self.assertEqual(status.structured_content['status'], 'lexical-fallback')
                # The same process must observe an atomically replaced index.
                path = root/'repos/platform/skills/main/SKILL.md'
                path.write_text('# Fruit\nFind watermelons in this capability.\n')
                library.index(lexical=True)
                result = await client.call_tool('search_tools', {'query': 'watermelons', 'lexical_only': True})
                self.assertTrue(result.structured_content['results'])
                self.assertEqual(result.structured_content['sources'][0]['provenance']['status'], 'modified')


if __name__ == '__main__':
    unittest.main()
