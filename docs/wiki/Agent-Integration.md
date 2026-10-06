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

For agents with local stdio MCP support, use the [RAG host setup](../rag.md#connect-an-mcp-host). This provides `search_tools`, `recommend_tools`, `get_tool`, `read_tool_source`, and `search_status` without requiring a shell tool in the agent.

## Compatibility and verification

The installer targets Linux, macOS, and WSL. Installer tests run on Linux with isolated temporary homes, including paths with spaces, repeat runs, backups, and conflicts. Platform locations were checked against the official references below on **2026-10-05**. Configuration compatibility does not establish an end-to-end test inside every proprietary client.

Run the agent in the same environment as the toolkit. For WSL or remote development, its shell/MCP process must be able to access that Linux checkout and runtime. Native Windows launchers are not verified. Cloud agents cannot access your local index automatically; provision the checkout and runtime in their execution environment. Hosts that accept only remote HTTP MCP need a separate deployment; this toolkit exposes local stdio.

To verify your client, confirm that it discovers `toolkit-selector`, then ask it to search the library and cite the returned source. MCP verification should list the five tools and call `search_status` before a recommendation. Follow the host's normal trust and tool-approval controls.

Official setup references: [Claude Code skills](https://code.claude.com/docs/en/skills) and [memory](https://code.claude.com/docs/en/memory), [Gemini skills](https://geminicli.com/docs/cli/skills/) and [context](https://geminicli.com/docs/cli/gemini-md/), [Cursor skills](https://cursor.com/docs/skills), [VS Code skills](https://code.visualstudio.com/docs/agent-customization/agent-skills), and [Cascade skills](https://docs.devin.ai/desktop/cascade/skills) (Windsurf's documentation now redirects to Devin Desktop; the legacy global skill path remains documented).

[Superpowers](https://github.com/obra/superpowers) is an optional complementary workflow installed separately. See [security and privacy](Security-and-Privacy.md) for the boundary between retrieved text and agent authority.
