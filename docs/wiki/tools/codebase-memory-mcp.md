# codebase-memory-mcp

Native local code knowledge-graph indexer with structural/semantic search, call tracing, architecture and change-impact queries through MCP or one-shot CLI.

[Upstream repository](https://github.com/DeusData/codebase-memory-mcp) · [Pinned source](https://github.com/DeusData/codebase-memory-mcp/tree/c61b3806bfe4c25f7003728b21d5b96a0db20e8f) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Engineering and code intelligence |
| Operating model | mcp |
| Recommended scope | global |
| Registered production skill paths | 0 |
| Reviewed source commit | `c61b3806bfe4c25f7003728b21d5b96a0db20e8f` |

## Purpose and use cases

Best as globally callable CLI with on-demand MCP: useful structural intelligence without permanent tool schemas or background processes. Overlaps Serena retrieval but adds persistent graph/architecture/cross-repo analysis; Serena adds LSP editing/refactoring. MCP always starts/joins a coordination daemon; --ui=false does not disable it. Current source scout profile exposes 8 tools and analysis 13, differing from stale README counts. Restricted profiles omit index_repository, so pre-index via CLI.

**Discovery tags:** `code graph`, `index`, `architecture`, `call graph`, `search`, `impact`, `mcp`, `cli`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Native release assets for Linux/macOS amd64/arm64 and Windows amd64; no runtime/API key needed for native binary
- Prefer Linux -portable archive; standard binary requires glibc 2.38+
- Verify release checksums.txt and keep selected release version fixed
- MCP starts shared account daemon; CLI mode neither starts nor connects it
- MCP --ui=false persists UI disablement; all active processes must share exact executable build and canonical cache root
- Automatic installer mutates detected agent MCP settings, hooks and skills unless --skip-config used
- Audited release API: v0.11.0 Linux amd64 portable tar.gz SHA256 1f9e8293eb2bc5c05cfa27a7e8fc033da6d729ffad525ccfcdaa3fd606306683; release flags must be checked against installed binary because checkout is newer

## Setup guidance

**Setup scope:** optional shared CLI; per-project code index

**Next action:** setup-required

**Working directory:** Read pinned sources in place. Use a separate runtime working copy or the selected target project for installations and generated files.

**Installation approach:** Use the pinned upstream documentation and choose one suitable route from install_commands. Lists can include alternatives, registration and launch commands; do not execute the entire list. Check for an existing compatible runtime before installing.

**Configuration:** Install the native CLI for the current platform. Index only the selected project; source installers and server profiles are alternatives. MCP configuration is separate from one-shot CLI use.

**Verification to perform:** codebase-memory-mcp --help; index a small selected project and confirm symbol results.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read codebase-memory-mcp README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
bash install.sh --skip-config --dir=/absolute/install/path
```

Example 2:

```bash
codebase-memory-mcp --ui=false --tool-profile=scout
```

Example 3:

```bash
codebase-memory-mcp --ui=false --tool-profile=analysis
```

Example 4:

```bash
codebase-memory-mcp cli index_repository --repo-path /path/to/repo
```

Example 5:

```bash
codebase-memory-mcp cli list_projects
```

Example 6:

```bash
codebase-memory-mcp cli search_graph --project my-project --name-pattern '.*Handler.*' --label Function
```

Example 7:

```bash
codebase-memory-mcp config set watcher_enabled false
```

## Source entry points

- [README.md](https://github.com/DeusData/codebase-memory-mcp/blob/c61b3806bfe4c25f7003728b21d5b96a0db20e8f/README.md)
- [docs/CONFIGURATION.md](https://github.com/DeusData/codebase-memory-mcp/blob/c61b3806bfe4c25f7003728b21d5b96a0db20e8f/docs/CONFIGURATION.md)
- [install.sh](https://github.com/DeusData/codebase-memory-mcp/blob/c61b3806bfe4c25f7003728b21d5b96a0db20e8f/install.sh)
- [src/main.c](https://github.com/DeusData/codebase-memory-mcp/blob/c61b3806bfe4c25f7003728b21d5b96a0db20e8f/src/main.c)
- [src/mcp/mcp.c](https://github.com/DeusData/codebase-memory-mcp/blob/c61b3806bfe4c25f7003728b21d5b96a0db20e8f/src/mcp/mcp.c)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show codebase-memory-mcp
bin/toolkit search "code graph index" --repo codebase-memory-mcp
bin/toolkit docs codebase-memory-mcp "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [DeusData/codebase-memory-mcp at `c61b3806bfe4`](https://github.com/DeusData/codebase-memory-mcp/tree/c61b3806bfe4c25f7003728b21d5b96a0db20e8f). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo codebase-memory-mcp --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
