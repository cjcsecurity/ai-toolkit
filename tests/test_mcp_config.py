"""Host configurations must preserve executable boundaries and never edit settings."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


class McpConfigTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'checkout "with" spaces'
        self.root.mkdir()
        (self.root / 'rag_server.py').write_text('# server fixture\n')
        self.python = self.root / 'runtime/search/bin/python'
        self.python.parent.mkdir(parents=True)
        self.python.symlink_to(sys.executable)

    def test_profiles_preserve_command_arguments_and_host_schema(self):
        from scripts.mcp_config import render_config
        for client in ['claude', 'cursor', 'gemini', 'windsurf', 'cline', 'roo',
                       'continue', 'generic', 'vscode', 'copilot-cli', 'opencode', 'codex']:
            with self.subTest(client=client):
                output = render_config(self.root, client)
                if client == 'codex':
                    entry = tomllib.loads(output)['mcp_servers']['ai-toolkit']
                else:
                    config = json.loads(output)
                    key = 'servers' if client == 'vscode' else 'mcp' if client == 'opencode' else 'mcpServers'
                    self.assertEqual(set(config), {key})
                    entry = config[key]['ai-toolkit']
                args = [str(self.root / 'rag_server.py'), '--root', str(self.root)]
                if client == 'opencode':
                    self.assertEqual(entry['command'], [str(self.python), *args])
                    self.assertEqual(entry['type'], 'local')
                else:
                    self.assertEqual(entry['command'], str(self.python))
                    self.assertEqual(entry['args'], args)
                if client in ['claude', 'vscode']:
                    self.assertEqual(entry['type'], 'stdio')
                if client == 'copilot-cli':
                    self.assertEqual(entry['type'], 'local')
                    self.assertEqual(set(entry['tools']), {'search_tools', 'recommend_tools',
                        'get_tool', 'read_tool_source', 'search_status'})
                self.assertNotIn('env', entry)
                self.assertNotIn('autoApprove', entry)
                self.assertNotIn('alwaysAllow', entry)

    def test_separate_data_root_selects_its_runtime_without_changing_server_source(self):
        from scripts.mcp_config import render_config
        data = self.root / 'catalog and runtime'
        python = data / 'runtime/search/bin/python'
        python.parent.mkdir(parents=True)
        python.symlink_to(sys.executable)
        entry = json.loads(render_config(self.root, 'claude', data_root=data))['mcpServers']['ai-toolkit']
        self.assertEqual(entry['command'], str(python))
        self.assertEqual(entry['args'], [str(self.root / 'rag_server.py'), '--root', str(data)])

    def test_missing_runtime_is_actionable_and_creates_nothing(self):
        from scripts.mcp_config import render_config
        self.python.unlink()
        before = sorted(self.root.rglob('*'))
        with self.assertRaisesRegex(ValueError, 'requirements-rag.txt'):
            render_config(self.root, 'claude')
        self.assertEqual(sorted(self.root.rglob('*')), before)

    def test_rejects_unknown_client_and_missing_server(self):
        from scripts.mcp_config import render_config
        with self.assertRaisesRegex(ValueError, 'Unknown client'):
            render_config(self.root, 'not-a-client')
        (self.root / 'rag_server.py').unlink()
        with self.assertRaisesRegex(ValueError, 'rag_server.py'):
            render_config(self.root, 'claude')

    def test_cli_emits_only_configuration_from_any_working_directory(self):
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/mcp_config.py'),
            '--client', 'claude', '--python', sys.executable, '--data-root', str(self.root)],
            cwd=self.tmp.name, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        entry = json.loads(result.stdout)['mcpServers']['ai-toolkit']
        self.assertEqual(entry['command'], str(Path(sys.executable).absolute()))
        self.assertEqual(entry['args'], [str(ROOT / 'rag_server.py'), '--root', str(self.root)])
        self.assertFalse((Path(self.tmp.name) / '.mcp.json').exists())


@unittest.skipUnless(importlib.util.find_spec('mcp'), 'Install requirements-rag.txt for MCP integration tests')
class GeneratedMcpSessionTests(unittest.IsolatedAsyncioTestCase):
    async def test_generated_command_discovers_tools_and_retrieves_cited_evidence(self):
        from mcp import ClientSession
        from mcp.client.stdio import StdioServerParameters, stdio_client
        from rag_fixture import make_library
        from scripts.mcp_config import render_config
        with tempfile.TemporaryDirectory(prefix='toolkit config ') as folder:
            data = Path(folder)
            make_library(data)
            config = json.loads(render_config(ROOT, 'claude', python=Path(sys.executable), data_root=data))
            entry = config['mcpServers']['ai-toolkit']
            with tempfile.TemporaryFile(mode='w+') as stderr:
                params = StdioServerParameters(command=entry['command'], args=entry['args'], cwd=folder)
                async with stdio_client(params, errlog=stderr) as streams:
                    async with ClientSession(*streams) as client:
                        await client.initialize()
                        catalog = await client.list_tools()
                        self.assertEqual({tool.name for tool in catalog.tools}, {'search_tools',
                            'recommend_tools', 'get_tool', 'read_tool_source', 'search_status'})
                        status = await client.call_tool('search_status', {})
                        self.assertFalse(status.is_error)
                        self.assertEqual(status.structured_content['status'], 'lexical-fallback')
                        result = await client.call_tool('recommend_tools', {'query': 'checkpoints', 'lexical_only': True})
                        self.assertFalse(result.is_error)
                        self.assertTrue(result.structured_content['sources'])
                        self.assertTrue(result.structured_content['candidates'])


if __name__ == '__main__':
    unittest.main()
