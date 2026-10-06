# Coding-agent integration

Use one local library from several coding agents. The selector teaches a shell-capable agent how to discover tools and read their setup instructions; the optional [RAG MCP server](../rag.md) exposes the same evidence through native tool calls.

## Install the selector

From your bootstrapped toolkit checkout, choose the agent you use:

```bash
python3 scripts/install_agent.py --client claude --dry-run
python3 scripts/install_agent.py --client claude
export PATH="$HOME/.local/bin:$PATH"
```

Restart the client after registration. In Claude Code, invoke `/toolkit-selector` or ask it to find a tool for your task. The agent needs shell access to run `toolkit` and filesystem access to the checkout. No model API key is needed for toolkit retrieval; the coding agent's own authentication still applies.

| Client option | Selector location under your home | Managed instruction file |
| --- | --- | --- |
| `claude` | `.claude/skills/toolkit-selector` | `.claude/CLAUDE.md` |
| `gemini` | `.gemini/skills/toolkit-selector` | `.gemini/GEMINI.md` |
| `cursor` | `.cursor/skills/toolkit-selector` | Uses native skill discovery |
| `copilot` | `.copilot/skills/toolkit-selector` | Uses native skill discovery in VS Code / Copilot CLI |
| `windsurf` | `.codeium/windsurf/skills/toolkit-selector` | Uses native skill discovery in Cascade |
| `codex` | `.agents/skills/toolkit-selector` | `.codex/AGENTS.md` |
| `opencode` | `.agents/skills/toolkit-selector` | `.config/opencode/AGENTS.md` |
| `generic` | `.agents/skills/toolkit-selector` | Load the skill explicitly if your agent does not discover this directory |

All clients also receive the shared `.agents/skills/toolkit-selector` link. Each link points to the same source directory. `--client both` retains its original meaning: **Codex and OpenCode only**. Run the installer separately for each additional client you want to configure.

Registration validates all destinations before writing. It preserves bytes outside its managed instruction block, backs up changed instruction files, and refuses unrelated command/skill destinations, symlinked instruction files, and malformed managed blocks. Repeating an unchanged installation creates no extra backups. It does not modify JSON settings, trust configuration, or MCP server registrations.

The linked commands are `toolkit`, `toolkit-mcp`, `toolkit-serena`, `toolkit-chrome-mcp`, and `toolkit-rag-mcp`. Optional adapters require [runtime setup](Runtime-Setup.md). Registration does not install the cataloged applications or copy their entire skill collections into your agent.

Preview with `--dry-run`, or use `--home /tmp/toolkit-demo-home` to test installation in another home directory. The checkout must remain at its installed path: moving it breaks its symlinks. `AI_TOOLKIT_HOME` selects another data/runtime root for CLI operations; it cannot repair a broken link. Bootstrap and source sync use their own checkout root.

## Other coding platforms

A coding agent with local command execution and file access can use the CLI directly, even without native skill discovery:

```bash
/absolute/path/to/ai-toolkit/bin/toolkit project
/absolute/path/to/ai-toolkit/bin/toolkit search "API code review" --kind repo --limit 8 --lexical
/absolute/path/to/ai-toolkit/bin/toolkit show semgrep
```

Point the agent at `skills/toolkit-selector/SKILL.md` in the checkout, or add this to its supported project-instruction file:

> Use the toolkit selector when choosing tools. Run `toolkit project` first, compare repositories with `toolkit search "project outcome" --kind repo`, and inspect requirements with `toolkit show ID`. Then retrieve capabilities from the selected repository and read the complete relevant instructions. Keep source availability and runtime readiness separate.

For agents with local stdio MCP support, configure the RAG server below. This provides `search_tools`, `recommend_tools`, `get_tool`, `read_tool_source`, and `search_status` without requiring a shell tool in the agent.

## Connect the RAG server

First complete the [RAG runtime and index setup](../rag.md#set-up-a-checkout). The configuration helper prints the correct format for your host:

```bash
python3 scripts/mcp_config.py --client claude
python3 scripts/mcp_config.py --client vscode
```

It uses an absolute Python path, the server script, and an explicit data directory. It defaults to `runtime/search/bin/python` under your data root. Use `--python /path/to/venv/bin/python` for another environment with `requirements-rag.txt` installed, and `--data-root /path/to/library` for a separate catalog/index. `AI_TOOLKIT_HOME` supplies the default data root when set. Interpreter symlinks keep their virtual-environment location.

The helper prints configuration only. Merge its `ai-toolkit` entry into the destination below, preserving other entries and settings. **Do not redirect output over an existing configuration file.** Generated output contains your local paths; keep it out of public commits. File/executable checks do not verify installed packages or index readiness; use the connection test below.

| `--client` | Format and destination | Official reference |
| --- | --- | --- |
| `claude` | `mcpServers` in project `.mcp.json`, or use the CLI command below for user scope | [Claude Code MCP](https://code.claude.com/docs/en/mcp) |
| `cursor` | `mcpServers` in `~/.cursor/mcp.json` or project `.cursor/mcp.json` | [Cursor MCP](https://cursor.com/docs/mcp) |
| `gemini` | `mcpServers` in `~/.gemini/settings.json` or project `.gemini/settings.json` | [Gemini MCP](https://geminicli.com/docs/tools/mcp-server/) |
| `vscode` | `servers` in project `.vscode/mcp.json`, or **MCP: Open User Configuration** | [VS Code MCP](https://code.visualstudio.com/docs/agent-customization/mcp-servers) |
| `copilot-cli` | `mcpServers` with an explicit tool list in `~/.copilot/mcp-config.json` | [Copilot CLI MCP](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers) |
| `windsurf` | `mcpServers` in the file opened by Cascade's **Open MCP config file** | [Cascade MCP](https://docs.devin.ai/desktop/cascade/mcp) |
| `cline` | `mcpServers` in the extension's **Configure MCP Servers** file, or CLI `~/.cline/mcp.json` | [Cline MCP](https://docs.cline.bot/mcp/mcp-overview) |
| `roo` | `mcpServers` in project `.roo/mcp.json` or **Edit Global MCP** | [Roo Code MCP](https://roocodeinc.github.io/Roo-Code/features/mcp/using-mcp-in-roo/) |
| `continue` | JSON `mcpServers` in project `.continue/mcpServers/ai-toolkit.json`; use Agent mode | [Continue MCP](https://docs.continue.dev/customize/deep-dives/mcp) |
| `codex` | TOML `[mcp_servers.ai-toolkit]` in `~/.codex/config.toml` | [Codex MCP](https://developers.openai.com/codex/mcp) |
| `opencode` | `mcp` with a `local` command array in `opencode.json` / `opencode.jsonc` | [OpenCode MCP](https://opencode.ai/docs/mcp-servers/) |
| `generic` | Common `mcpServers` JSON; adapt the wrapper to your host | Consult your host's local stdio documentation |

Copilot CLI and VS Code use different wrapper keys; select the matching profile. The tool list in the Copilot CLI profile exposes the five retrieval tools without changing approval policies. No generated profile enables automatic tool approval or imports credentials from your environment.

### Claude Code quick connection

After preparing the RAG runtime, this alternative registers the default checkout directly at user scope. Substitute your actual absolute checkout path in all three places:

```bash
claude mcp add --scope user --transport stdio ai-toolkit -- \
  /absolute/path/to/ai-toolkit/runtime/search/bin/python \
  /absolute/path/to/ai-toolkit/rag_server.py \
  --root /absolute/path/to/ai-toolkit
```

Quote each path if it contains spaces. For a separate runtime/data root, use the generated configuration instead. In Claude Code, open `/mcp`, confirm the connection, and ask: “Use AI Toolkit to find a tool for browser testing. Compare requirements and cite the source evidence.” Install the selector too if you want Claude to follow the full discover/read/setup workflow.

### Verify the connection

In your host, confirm that `ai-toolkit` lists the five tools, call `search_status`, then call `recommend_tools` with a task description. Its evidence should include source IDs and paths. Missing or incompatible semantic embeddings report lexical fallback; explicitly build the semantic index to enable hybrid retrieval.

The automated suite parses every generated JSON/TOML profile and launches the generated command through a real MCP SDK session, checking discovery, status, and cited recommendations against an isolated fixture. That validates the server connection contract; interactive skill selection and approvals still depend on the client. The [SDK example](../../examples/rag_mcp.py) also tests an existing local index without registering a client.

## Compatibility and verification

The installer targets Linux, macOS, and WSL. Installer tests run on Linux with isolated temporary homes, including paths with spaces, repeat runs, backups, and conflicts. Platform locations were checked against the official references below on **2026-10-05**. Configuration compatibility does not establish an end-to-end test inside every proprietary client.

Run the agent in the same environment as the toolkit. For WSL or remote development, its shell/MCP process must be able to access that Linux checkout and runtime. Native Windows launchers are not verified. Cloud agents cannot access your local index automatically; provision the checkout and runtime in their execution environment. Hosts that accept only remote HTTP MCP need a separate deployment; this toolkit exposes local stdio.

To verify your client, confirm that it discovers `toolkit-selector`, then ask it to search the library and cite the returned source. MCP verification should list the five tools and call `search_status` before a recommendation. Follow the host's normal trust and tool-approval controls.

Official setup references: [Claude Code skills](https://code.claude.com/docs/en/skills) and [memory](https://code.claude.com/docs/en/memory), [Gemini skills](https://geminicli.com/docs/cli/skills/) and [context](https://geminicli.com/docs/cli/gemini-md/), [Cursor skills](https://cursor.com/docs/skills), [VS Code skills](https://code.visualstudio.com/docs/agent-customization/agent-skills), and [Cascade skills](https://docs.devin.ai/desktop/cascade/skills) (Windsurf's documentation now redirects to Devin Desktop; the legacy global skill path remains documented).

[Superpowers](https://github.com/obra/superpowers) is an optional complementary workflow installed separately. See [security and privacy](Security-and-Privacy.md) for the boundary between retrieved text and agent authority.
