# serena

MCP coding toolkit with language-server-backed symbol lookup, reference navigation, semantic editing, refactoring and project memories.

[Upstream repository](https://github.com/oraios/serena) · [Pinned source](https://github.com/oraios/serena/tree/d0f7f92631c23dc4c5ed0b5ccd35bc623b19a809) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Engineering and code intelligence |
| Operating model | mcp |
| Recommended scope | global |
| Registered production skill paths | 0 |
| Reviewed source commit | `d0f7f92631c23dc4c5ed0b5ccd35bc623b19a809` |

## Purpose and use cases

Strong broadly useful complement to Superpowers: adds semantic operations rather than another development process. Make the CLI globally callable and start MCP only when needed to avoid permanent schemas. --context=codex excludes six redundant file/shell tools; UI can be disabled. New v2 REPL interface compresses tool surface but changes interaction style.

**Discovery tags:** `semantic code`, `LSP`, `symbols`, `references`, `refactoring`, `mcp`, `codex`, `opencode`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- uv; README recommends Python 3.13, manifest accepts >=3.11,<3.15
- Language-specific runtimes/LSP dependencies may be downloaded or required manually
- Linux/macOS/Windows supported; optional paid JetBrains backend needs compatible IDE/plugin
- Use an installed executable to preserve current project cwd; uv run --directory changes cwd to Serena checkout, requiring explicit --project for the original project
- Latest checkout reports 2.0.0.dev0; release packages may expose different flags, so verify installed --help

## Setup guidance

**Setup scope:** optional shared on-demand MCP; project language-server dependencies

**Next action:** setup-required

**Working directory:** Read pinned sources in place. Use a separate runtime working copy or the selected target project for installations and generated files.

**Installation approach:** Use the pinned upstream documentation and choose one suitable route from install_commands. Lists can include alternatives, registration and launch commands; do not execute the entire list. Check for an existing compatible runtime before installing.

**Configuration:** Install Serena and required language runtimes or language servers. Configure the optional toolkit-serena wrapper, choose an explicit project path, and verify tools before indexing or editing.

**Verification to perform:** List tools for the project, then request symbols from a small source file.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read serena docs/02-usage/010_installation.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
uv tool install -p 3.13 serena-agent
```

Example 2:

```bash
serena init
```

Example 3:

```bash
serena start-mcp-server --project-from-cwd --context=codex --enable-web-dashboard false --enable-gui-log-window false --open-web-dashboard false
```

Example 4:

```bash
serena start-mcp-server --project /absolute/project --context=codex --agent-interface REPL --enable-web-dashboard false --enable-gui-log-window false --open-web-dashboard false
```

Example 5:

```bash
uv run --directory /abs/path/to/serena serena start-mcp-server --project /absolute/project --context=codex
```

## Source entry points

- [README.md](https://github.com/oraios/serena/blob/d0f7f92631c23dc4c5ed0b5ccd35bc623b19a809/README.md)
- [pyproject.toml](https://github.com/oraios/serena/blob/d0f7f92631c23dc4c5ed0b5ccd35bc623b19a809/pyproject.toml)
- [docs/02-usage/010_installation.md](https://github.com/oraios/serena/blob/d0f7f92631c23dc4c5ed0b5ccd35bc623b19a809/docs/02-usage/010_installation.md)
- [docs/02-usage/020_running.md](https://github.com/oraios/serena/blob/d0f7f92631c23dc4c5ed0b5ccd35bc623b19a809/docs/02-usage/020_running.md)
- [docs/02-usage/030_clients.md](https://github.com/oraios/serena/blob/d0f7f92631c23dc4c5ed0b5ccd35bc623b19a809/docs/02-usage/030_clients.md)
- [docs/02-usage/050_configuration.md](https://github.com/oraios/serena/blob/d0f7f92631c23dc4c5ed0b5ccd35bc623b19a809/docs/02-usage/050_configuration.md)
- [src/serena/cli.py](https://github.com/oraios/serena/blob/d0f7f92631c23dc4c5ed0b5ccd35bc623b19a809/src/serena/cli.py)
- [src/serena/resources/config/contexts/codex.yml](https://github.com/oraios/serena/blob/d0f7f92631c23dc4c5ed0b5ccd35bc623b19a809/src/serena/resources/config/contexts/codex.yml)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show serena
bin/toolkit search "semantic code LSP" --repo serena
bin/toolkit docs serena "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [oraios/serena at `d0f7f92631c2`](https://github.com/oraios/serena/tree/d0f7f92631c23dc4c5ed0b5ccd35bc623b19a809). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo serena --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
