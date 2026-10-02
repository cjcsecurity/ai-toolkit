"""Optional MCP SDK tests with a real local server fixture."""
import contextlib
import importlib.util
import io
import json
import os
import sys
from pathlib import Path
import tempfile
import time
import unittest
from unittest.mock import patch
from contextlib import chdir

ROOT = Path(__file__).resolve().parents[1]
HAS_MCP = importlib.util.find_spec('mcp') is not None
FIXTURE = '#!' + sys.executable + '\n' + '''import anyio, json, os
from pathlib import Path
from mcp import types
from mcp.server import Server
from mcp.server.stdio import stdio_server
Path("fixture.pid").write_text(str(os.getpid()))
Path("fixture-home").write_text(os.environ.get("SERENA_HOME", ""))
Path("fixture-cwd").write_text(os.getcwd())
async def list_tools(ctx, params):
    return types.ListToolsResult(tools=[types.Tool(name="echo", description="Echo arguments. " + "detail " * 200, inputSchema={"type":"object","properties":{"text":{"type":"string"}},"required":["text"]}), types.Tool(name="fail", description="Return an error", inputSchema={"type":"object"}), types.Tool(name="slow", description="Wait", inputSchema={"type":"object"})])
state={}
async def call_tool(ctx, params):
    if params.name == "store":
        state.update(params.arguments)
    if params.name == "recall":
        return types.CallToolResult(content=[types.TextContent(type="text",text=json.dumps(state))])
    if params.name == "slow":
        await anyio.sleep(60)
    return types.CallToolResult(content=[types.TextContent(type="text", text=json.dumps(params.arguments))], isError=params.name=="fail")
server=Server("fixture", on_list_tools=list_tools, on_call_tool=call_tool)
async def run():
    async with stdio_server() as (read,write):
        await server.run(read,write,server.create_initialization_options())
anyio.run(run)
'''

@unittest.skipUnless(HAS_MCP, "optional MCP SDK missing; install requirements-mcp.txt")
class MCPClientTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue((ROOT/'mcp_client.py').exists(), 'MCP client implementation is missing')
        spec=importlib.util.spec_from_file_location('toolkit_mcp_client', ROOT/'mcp_client.py')
        self.client=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.client)
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.project=Path(self.tmp.name)
        fixture=self.project/'fixture-server'
        fixture.write_text(FIXTURE)
        fixture.chmod(0o755)
        self.mock=patch.object(self.client,'SERENA',str(fixture))
        self.mock.start()
        self.addCleanup(self.mock.stop)

    def run_cli(self,*args):
        out,err=io.StringIO(),io.StringIO()
        with contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
            code=self.client.main(list(args))
        return code,out.getvalue(),err.getvalue()

    def assert_stopped(self):
        pid=int((self.project/'fixture.pid').read_text())
        with self.assertRaises(ProcessLookupError):
            os.kill(pid,0)

    def test_discovery_is_concise_without_schemas_and_reaps_server(self):
        code,out,err=self.run_cli('tools','--project',str(self.project))
        self.assertEqual(code,0,err)
        self.assertIn('echo',out)
        self.assertIn('slow',out)
        self.assertNotIn('inputSchema',out)
        self.assertLess(len(out),700)
        self.assert_stopped()

    def test_runtime_state_is_isolated_from_global_serena_config(self):
        code,out,err=self.run_cli('tools','--project',str(self.project))
        self.assertEqual(code,0,err)
        home=(self.project/'fixture-home').read_text()
        self.assertTrue(home, 'SERENA_HOME must be explicitly isolated')
        self.assertNotEqual(Path(home).resolve(), Path.home()/'.serena')
        self.assertTrue(Path(home).is_absolute())

    def test_chrome_uses_caller_cwd_without_project_and_shares_tool_calls(self):
        with patch.object(self.client,'CHROME',str(self.project/'fixture-server'),create=True), chdir(self.project):
            code,out,err=self.run_cli('--server','chrome','tools')
            self.assertEqual(code,0,err)
            self.assertIn('echo',out)
            self.assertEqual((self.project/'fixture-cwd').read_text(),str(self.project))
            self.assertEqual((self.project/'fixture-home').read_text(),'')
            code,out,err=self.run_cli('call','echo','--server','chrome','--args','{"text":"chrome"}')
            self.assertEqual(code,0,err)
            self.assertEqual(json.loads(json.loads(out)['content'][0]['text']),{'text':'chrome'})
        self.assert_stopped()

    def test_batch_preserves_session_state(self):
        steps=json.dumps([{'tool':'store','args':{'text':'remember'}},{'tool':'recall','args':{}}])
        with patch.object(self.client,'CHROME',str(self.project/'fixture-server'),create=True), chdir(self.project):
            code,out,err=self.run_cli('--server','chrome','batch','--steps',steps)
        self.assertEqual(code,0,err)
        rows=json.loads(out)['results']
        self.assertEqual([row['index'] for row in rows],[0,1])
        self.assertEqual(json.loads(rows[1]['result']['content'][0]['text']),{'text':'remember'})
        self.assert_stopped()

    def test_batch_stops_on_error(self):
        steps=json.dumps([{'tool':'echo','args':{'text':'ok'}},{'tool':'fail','args':{}},{'tool':'slow','args':{}}])
        code,out,err=self.run_cli('batch','--project',str(self.project),'--steps',steps)
        self.assertNotEqual(code,0)
        body=json.loads(out)
        self.assertTrue(body['stopped_on_error'])
        self.assertEqual(len(body['results']),2)
        self.assertTrue(body['results'][1]['isError'])
        self.assertEqual(body['results'][1]['index'],1)
        self.assert_stopped()

    def test_batch_validates_all_steps_before_start(self):
        for steps in [[],[{'tool':'echo','args':[]}],[{'tool':'echo','args':{}}]*21,[{'args':{}}]]:
            with self.subTest(steps=steps):
                code,out,err=self.run_cli('batch','--project',str(self.project),'--steps',json.dumps(steps))
                self.assertNotEqual(code,0)
                self.assertFalse((self.project/'fixture.pid').exists())

    def test_selected_schema_is_exact(self):
        code,out,err=self.run_cli('tools','--project',str(self.project),'--tool','echo')
        self.assertEqual(code,0,err)
        self.assertEqual(json.loads(out)['inputSchema'],{'type':'object','properties':{'text':{'type':'string'}},'required':['text']})

    def test_call_preserves_arguments_and_propagates_tool_error(self):
        args='{"text":"hello \\u2603"}'
        code,out,err=self.run_cli('call','echo','--project',str(self.project),'--args',args)
        self.assertEqual(code,0,err)
        self.assertEqual(json.loads(json.loads(out)['content'][0]['text']),{'text':'hello ☃'})
        code,out,err=self.run_cli('call','fail','--project',str(self.project),'--args','{}')
        self.assertNotEqual(code,0)
        self.assertTrue(json.loads(out)['isError'])
        self.assert_stopped()

    def test_output_has_hard_budget_and_truncation_notice(self):
        code,out,err=self.run_cli('call','echo','--project',str(self.project),'--args',json.dumps({'text':'x'*10000}),'--budget','200')
        self.assertEqual(code,0,err)
        self.assertLessEqual(len(out),200)
        self.assertIn('truncated',out.lower())

    def test_timeout_is_bounded_and_reaps_server(self):
        start=time.monotonic()
        code,out,err=self.run_cli('call','slow','--project',str(self.project),'--args','{}','--timeout','0.8')
        self.assertNotEqual(code,0)
        self.assertIn('timed out',err.lower())
        self.assertLess(time.monotonic()-start,12)
        self.assert_stopped()

    def test_invalid_arguments_never_start_server(self):
        cases=[('tools',),('tools','--project',str(Path.home())),('tools','--project',str(self.project/'missing')),('call','echo','--project',str(self.project),'--args','[]'),('call','echo','--project',str(self.project),'--args','{'),('tools','--project',str(self.project),'--budget','0'),('call','echo','--project',str(self.project),'--args','{}','--timeout','nan')]
        for args in cases:
            with self.subTest(args=args):
                code,out,err=self.run_cli(*args)
                self.assertNotEqual(code,0)
                self.assertFalse((self.project/'fixture.pid').exists())

    def test_unknown_schema_is_an_error(self):
        code,out,err=self.run_cli('tools','--project',str(self.project),'--tool','missing')
        self.assertNotEqual(code,0)
        self.assertIn('missing',err)
        self.assert_stopped()

if __name__=='__main__':
    unittest.main()
