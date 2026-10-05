# Runtime setup

Source retrieval and runtime setup are separate operations. Bootstrap makes source documents searchable; individual tools may still require language runtimes, browser binaries, containers, services, model providers, accounts, or platform-specific hardware.

Read `toolkit show ID`, the [tool page](Tool-Catalog.md), and its pinned upstream setup guide before provisioning. Listed commands are documented alternatives or examples. Select the appropriate route; do not execute every line as an installation script.

## Local search runtime

Lexical search runs with Python 3.11+ and SQLite FTS5. Semantic setup is explicit:

```bash
python3 scripts/bootstrap.py --semantic
bin/toolkit search-status
```

This creates an isolated search environment and downloads the pinned model for currently available source and catalog content. To download all source too, add `--all`. `uv` is recommended for Python 3.12; the fallback supports an existing Python 3.12–3.13 with venv. Dependencies are recorded in [`requirements-search.txt`](../../requirements-search.txt).

## Optional RAG server

The local RAG server and CLI recommendations share the manager's search environment. Install `requirements-rag.txt` into `runtime/search` to add the official MCP SDK alongside the pinned embedding dependencies. `bin/toolkit-rag-mcp` starts the stdio server; configure a host explicitly. See [RAG setup](../rag.md).

## Optional MCP client runtime

The one-shot MCP client has its own optional dependencies. From the toolkit root:

```bash
python3 -m venv runtime/mcp
runtime/mcp/bin/python -m pip install -r requirements-mcp.txt
```

[`requirements-mcp.txt`](../../requirements-mcp.txt) pins `mcp==2.2.0` and `anyio==4.15.1`. Installing these client dependencies does not install or start an upstream MCP server.

## Serena adapter

Install Serena using the instructions at the [recorded source revision](tools/serena.md), then set `TOOLKIT_SERENA_COMMAND` to the Serena executable path (not a shell command containing arguments). The adapter supplies server arguments. Use a selected project path, not your entire home directory.

```bash
bin/toolkit-serena tools --project /path/to/project
bin/toolkit-serena tools --project /path/to/project --tool TOOL_NAME
bin/toolkit-serena call TOOL_NAME --project /path/to/project --args '{}'
```

Discover the schema before constructing actual arguments. Language-server dependencies depend on the project's languages. A one-shot call starts a temporary server while project caches may persist.

## Chrome DevTools adapter

Prepare Node.js, Chrome, and the Chrome DevTools MCP package separately using its [tool page](tools/chrome-devtools-mcp.md). Configure paths that exist on your machine:

```bash
export TOOLKIT_NODE=/path/to/node
export TOOLKIT_CHROME_MCP_ENTRY=/path/to/chrome-devtools-mcp/build/src/bin/chrome-devtools-mcp.js
export TOOLKIT_CHROME_EXECUTABLE=/path/to/chrome
bin/toolkit-mcp --server chrome tools
```

The configured JavaScript path must be the package's CLI executable, not its library module. For the pinned package this is `build/src/bin/chrome-devtools-mcp.js`; check the installed package's `bin` mapping if using another revision.

The adapter uses an isolated headless browser. It does not inherit authentication from your normal Chrome profile. Discover the installed server's tool schemas before constructing a batch. For example, inspect its page-listing tool, then use a batch that needs no page identifier:

```bash
bin/toolkit-mcp --server chrome tools --tool list_pages
bin/toolkit-mcp --server chrome batch --steps '[{"tool":"list_pages","args":{}}]'
```

Use this example only when the discovered schema exposes `list_pages` with these arguments. Page identifiers come from the running server; there is no guaranteed initial page ID. Each invocation creates a fresh session, so IDs returned by one invocation must not be reused in another.

Keep dependent browser operations in one batch when all arguments can be specified upfront. The batch runs sequentially and stops on its first tool error; it does not substitute earlier outputs into later arguments. If subsequent calls need arguments constructed from returned page IDs, use an upstream persistent MCP client that keeps the same session open.

For adapters, `--budget` and `--timeout` go after `tools`, `call`, or `batch`, unlike the main `toolkit --budget ... COMMAND` syntax.

Calls, batches, and individual schemas return JSON. If a response exceeds the budget, the wrapper returns a valid JSON envelope with `truncated: true` and `required_budget`, omitting the response body. The tool's exit status is preserved. Choose a larger budget before calls with side effects; repeating a call to recover its output can repeat the action. The concise tool list and diagnostic errors remain plain text.

## Other applications

Install only the selected system and its justified dependencies in an appropriate isolated or project environment. Source presence does not prove runtime health. Verify a concrete operation after setup and record actual versions and remaining prerequisites locally. Keep credentials and machine-specific readiness records out of the public manifest.

[Back to the wiki](Home.md)
