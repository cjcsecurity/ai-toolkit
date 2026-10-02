# agentmemory

Persistent agent memory service using the iii engine, BM25/optional embeddings, knowledge graphs, MCP/REST APIs, native skills and agent lifecycle integrations.

[Upstream repository](https://github.com/rohitg00/agentmemory) · [Pinned source](https://github.com/rohitg00/agentmemory/tree/b3d6cf50026655233f11c2273b898af0ca82cf03) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | AI infrastructure and retrieval |
| Operating model | application |
| Recommended scope | on-demand |
| Registered production skill paths | 17 |
| Reviewed source commit | `b3d6cf50026655233f11c2273b898af0ca82cf03` |

## Purpose and use cases

Substantial service stack and 54 advertised MCP tools with automatic lifecycle integrations; duplicates other memory approaches and adds standing ports/processes. Use only when cross-session memory is a concrete need; evaluate data retention and scope per project before broad installation.

**Discovery tags:** `memory`, `persistence`, `iii`, `bm25`, `embeddings`, `mcp`, `hooks`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Node.js >=20, npm/npx
- Pinned iii-engine v0.22.1; automatically installed on macOS/Linux with curl, POSIX sh, tar
- Native Windows requires manual iii.exe setup; WSL2 and Docker alternatives documented
- Runtime ports 3111, 3112, 3113, 49134
- Keyless BM25 works without provider; optional local embedding model downloads or hosted provider credentials
- First launch interactively configures selected agents and starts services

## Setup guidance

**Setup scope:** shared memory service; per-client integration

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Provision the iii engine and service environment once, check port availability, then configure only the intended client hooks and selected embedding provider.

**Verification to perform:** Use the documented service checks and store/retrieve a disposable memory before enabling client integration.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read agentmemory INSTALL_FOR_AGENTS.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx -y @agentmemory/agentmemory@latest
```

Example 2:

```bash
npm install -g @agentmemory/agentmemory@latest
```

Example 3:

```bash
npx skills add rohitg00/agentmemory -y
```

## Source entry points

- [README.md](https://github.com/rohitg00/agentmemory/blob/b3d6cf50026655233f11c2273b898af0ca82cf03/README.md)
- [package.json](https://github.com/rohitg00/agentmemory/blob/b3d6cf50026655233f11c2273b898af0ca82cf03/package.json)
- [INSTALL_FOR_AGENTS.md](https://github.com/rohitg00/agentmemory/blob/b3d6cf50026655233f11c2273b898af0ca82cf03/INSTALL_FOR_AGENTS.md)
- [DESIGN.md](https://github.com/rohitg00/agentmemory/blob/b3d6cf50026655233f11c2273b898af0ca82cf03/DESIGN.md)
- [.env.example](https://github.com/rohitg00/agentmemory/blob/b3d6cf50026655233f11c2273b898af0ca82cf03/.env.example)

## Skills and retrieval

The manifest registers **17 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [plugin/skills/agentmemory-agents/SKILL.md](https://github.com/rohitg00/agentmemory/blob/b3d6cf50026655233f11c2273b898af0ca82cf03/plugin/skills/agentmemory-agents/SKILL.md)
- [plugin/skills/agentmemory-architecture/SKILL.md](https://github.com/rohitg00/agentmemory/blob/b3d6cf50026655233f11c2273b898af0ca82cf03/plugin/skills/agentmemory-architecture/SKILL.md)
- [plugin/skills/agentmemory-config/SKILL.md](https://github.com/rohitg00/agentmemory/blob/b3d6cf50026655233f11c2273b898af0ca82cf03/plugin/skills/agentmemory-config/SKILL.md)
- [plugin/skills/agentmemory-hooks/SKILL.md](https://github.com/rohitg00/agentmemory/blob/b3d6cf50026655233f11c2273b898af0ca82cf03/plugin/skills/agentmemory-hooks/SKILL.md)
- [plugin/skills/agentmemory-mcp-tools/SKILL.md](https://github.com/rohitg00/agentmemory/blob/b3d6cf50026655233f11c2273b898af0ca82cf03/plugin/skills/agentmemory-mcp-tools/SKILL.md)
- [plugin/skills/agentmemory-rest-api/SKILL.md](https://github.com/rohitg00/agentmemory/blob/b3d6cf50026655233f11c2273b898af0ca82cf03/plugin/skills/agentmemory-rest-api/SKILL.md)
- [plugin/skills/commit-context/SKILL.md](https://github.com/rohitg00/agentmemory/blob/b3d6cf50026655233f11c2273b898af0ca82cf03/plugin/skills/commit-context/SKILL.md)
- [plugin/skills/commit-history/SKILL.md](https://github.com/rohitg00/agentmemory/blob/b3d6cf50026655233f11c2273b898af0ca82cf03/plugin/skills/commit-history/SKILL.md)
- [plugin/skills/forget/SKILL.md](https://github.com/rohitg00/agentmemory/blob/b3d6cf50026655233f11c2273b898af0ca82cf03/plugin/skills/forget/SKILL.md)
- [plugin/skills/handoff/SKILL.md](https://github.com/rohitg00/agentmemory/blob/b3d6cf50026655233f11c2273b898af0ca82cf03/plugin/skills/handoff/SKILL.md)
- [plugin/skills/lesson/SKILL.md](https://github.com/rohitg00/agentmemory/blob/b3d6cf50026655233f11c2273b898af0ca82cf03/plugin/skills/lesson/SKILL.md)
- [plugin/skills/memory-discipline/SKILL.md](https://github.com/rohitg00/agentmemory/blob/b3d6cf50026655233f11c2273b898af0ca82cf03/plugin/skills/memory-discipline/SKILL.md)

Showing 12 of 17 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show agentmemory
bin/toolkit search "memory persistence" --repo agentmemory
bin/toolkit docs agentmemory "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [rohitg00/agentmemory at `b3d6cf500266`](https://github.com/rohitg00/agentmemory/tree/b3d6cf50026655233f11c2273b898af0ca82cf03). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo agentmemory --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
