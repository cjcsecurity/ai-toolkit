# Codex and OpenCode

The toolkit's selector is a small discovery skill. It tells the agent to compare repository candidates, read requirements, retrieve relevant capabilities, and keep specialized collections on demand.

After cloning and bootstrapping the toolkit, explicitly register either or both clients:

```bash
python3 scripts/install_agent.py --client both
export PATH="$HOME/.local/bin:$PATH"
```

Use `--client codex` or `--client opencode` for one client. Registration creates command symlinks under `~/.local/bin` and a shared selector symlink at `~/.agents/skills/toolkit-selector`. It adds a managed instruction block to `~/.codex/AGENTS.md` for Codex or `~/.config/opencode/AGENTS.md` for OpenCode. Existing text outside that block is preserved, and changed instruction files receive a backup. Unrelated command or skill destinations, symlinked instruction files, or malformed managed blocks cause an error. The linked commands are `toolkit`, `toolkit-mcp`, `toolkit-serena`, and `toolkit-chrome-mcp`; the adapter commands still need their optional runtime and server setup. It does not register all 60 tools, install their runtimes, or enable MCP servers.

The `--home PATH` option is useful for testing registration in a temporary home before applying it to a real account:

```bash
python3 scripts/install_agent.py --client both --home /tmp/toolkit-demo-home
```

The launchers resolve their code from the toolkit checkout. `AI_TOOLKIT_HOME` optionally selects another data/runtime root for CLI operations; bootstrap and source sync always use their own script checkout root. Moving the checkout can break the installed symlinks: inspect and explicitly remove outdated links before registering the new location. An environment variable cannot repair a broken symlink.

## Working instructions for agents

A concise project instruction can establish the discovery habit:

> Use the toolkit selector for substantial project work. Run `toolkit project` first. For a new toolset, search the project outcome with `toolkit search "project outcome" --kind repo --limit 8`, inspect promising setup guides with `toolkit show ID`, and compare requirements before choosing. Search capabilities inside selected repositories and read the relevant skill completely. Keep catalog availability, source availability, and runtime readiness separate.

```bash
toolkit project
toolkit search "API code review and static analysis" --kind repo --limit 8
toolkit show semgrep
toolkit search "custom rules" --repo semgrep
```

`toolkit select ID ... --project /path/to/project` records project preferences. It neither grants permission for external actions nor starts an application.

## Global versus on demand

Some catalog entries recommend a broadly useful global CLI or skill. Those recommendations are metadata for a deliberate setup decision; registration installs only the toolkit selector and launchers. Full skill directories often contain references, scripts, agents, and assets, so preserve their layout when installing a selected skill later.

[Superpowers](https://github.com/obra/superpowers) is a complementary engineering workflow that can be installed separately through its upstream instructions. It is not bundled, activated, or counted among the 60 catalog tools. The toolkit also works without it.

See [runtime setup](Runtime-Setup.md) for optional one-shot MCP adapters and [security and privacy](Security-and-Privacy.md) for the boundary between retrieved text and agent authority.
