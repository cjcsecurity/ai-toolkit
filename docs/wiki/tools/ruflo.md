# ruflo

Agent orchestration meta-harness with CLI/MCP, agent teams, workflow plugins, memory, hooks and background coordination.

[Upstream repository](https://github.com/ruvnet/ruflo) · [Pinned source](https://github.com/ruvnet/ruflo/tree/6cfd88654f2c571940f32704d79a2a1892de4392) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | AI infrastructure and retrieval |
| Operating model | application |
| Recommended scope | on-demand |
| Registered production skill paths | 373 |
| Reviewed source commit | `6cfd88654f2c571940f32704d79a2a1892de4392` |

## Purpose and use cases

Large alternative execution framework, not a lightweight global capability. Init installs numerous agents, commands, hooks and a daemon; broad tool surface and strong overlap with Superpowers orchestration/planning. Evaluate per-project only. SKILL.md inventory includes repeated generated/plugin copies, not unique skills to register wholesale.

**Discovery tags:** `multi-agent`, `swarm`, `orchestration`, `memory`, `hooks`, `claude`, `codex`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Node.js >=20 and npm/npx
- Claude Code or Codex and applicable model credentials for orchestration
- Cross-platform npx wizard; POSIX install script requires bash/WSL/Git-Bash on Windows
- Optional Rust/native and database components depend on selected plugins

## Setup guidance

**Setup scope:** shared orchestration CLI; per-project initialization

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Choose only the required orchestration/plugin components. Run the init wizard in the intended project and review generated hooks/services before enabling them.

**Verification to perform:** Use documented diagnostics and a small local workflow with the configured model; test MCP only if selected.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read ruflo README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx ruflo@latest init wizard
```

Example 2:

```bash
npx ruflo@latest mcp start
```

## Source entry points

- [README.md](https://github.com/ruvnet/ruflo/blob/6cfd88654f2c571940f32704d79a2a1892de4392/README.md)
- [package.json](https://github.com/ruvnet/ruflo/blob/6cfd88654f2c571940f32704d79a2a1892de4392/package.json)
- [SKILL.md](https://github.com/ruvnet/ruflo/blob/6cfd88654f2c571940f32704d79a2a1892de4392/SKILL.md)
- [docs/ruflo-explained.md](https://github.com/ruvnet/ruflo/blob/6cfd88654f2c571940f32704d79a2a1892de4392/docs/ruflo-explained.md)
- [plugins/ruflo-core/README.md](https://github.com/ruvnet/ruflo/blob/6cfd88654f2c571940f32704d79a2a1892de4392/plugins/ruflo-core/README.md)

## Skills and retrieval

The manifest registers **373 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [.agents/skills/agent-adaptive-coordinator/SKILL.md](https://github.com/ruvnet/ruflo/blob/6cfd88654f2c571940f32704d79a2a1892de4392/.agents/skills/agent-adaptive-coordinator/SKILL.md)
- [.agents/skills/agent-agent/SKILL.md](https://github.com/ruvnet/ruflo/blob/6cfd88654f2c571940f32704d79a2a1892de4392/.agents/skills/agent-agent/SKILL.md)
- [.agents/skills/agent-agentic-payments/SKILL.md](https://github.com/ruvnet/ruflo/blob/6cfd88654f2c571940f32704d79a2a1892de4392/.agents/skills/agent-agentic-payments/SKILL.md)
- [.agents/skills/agent-analyze-code-quality/SKILL.md](https://github.com/ruvnet/ruflo/blob/6cfd88654f2c571940f32704d79a2a1892de4392/.agents/skills/agent-analyze-code-quality/SKILL.md)
- [.agents/skills/agent-app-store/SKILL.md](https://github.com/ruvnet/ruflo/blob/6cfd88654f2c571940f32704d79a2a1892de4392/.agents/skills/agent-app-store/SKILL.md)
- [.agents/skills/agent-arch-system-design/SKILL.md](https://github.com/ruvnet/ruflo/blob/6cfd88654f2c571940f32704d79a2a1892de4392/.agents/skills/agent-arch-system-design/SKILL.md)
- [.agents/skills/agent-architecture/SKILL.md](https://github.com/ruvnet/ruflo/blob/6cfd88654f2c571940f32704d79a2a1892de4392/.agents/skills/agent-architecture/SKILL.md)
- [.agents/skills/agent-authentication/SKILL.md](https://github.com/ruvnet/ruflo/blob/6cfd88654f2c571940f32704d79a2a1892de4392/.agents/skills/agent-authentication/SKILL.md)
- [.agents/skills/agent-automation-smart-agent/SKILL.md](https://github.com/ruvnet/ruflo/blob/6cfd88654f2c571940f32704d79a2a1892de4392/.agents/skills/agent-automation-smart-agent/SKILL.md)
- [.agents/skills/agent-base-template-generator/SKILL.md](https://github.com/ruvnet/ruflo/blob/6cfd88654f2c571940f32704d79a2a1892de4392/.agents/skills/agent-base-template-generator/SKILL.md)
- [.agents/skills/agent-benchmark-suite/SKILL.md](https://github.com/ruvnet/ruflo/blob/6cfd88654f2c571940f32704d79a2a1892de4392/.agents/skills/agent-benchmark-suite/SKILL.md)
- [.agents/skills/agent-byzantine-coordinator/SKILL.md](https://github.com/ruvnet/ruflo/blob/6cfd88654f2c571940f32704d79a2a1892de4392/.agents/skills/agent-byzantine-coordinator/SKILL.md)

Showing 12 of 373 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show ruflo
bin/toolkit search "multi-agent swarm" --repo ruflo
bin/toolkit docs ruflo "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [ruvnet/ruflo at `6cfd88654f2c`](https://github.com/ruvnet/ruflo/tree/6cfd88654f2c571940f32704d79a2a1892de4392). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo ruflo --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
