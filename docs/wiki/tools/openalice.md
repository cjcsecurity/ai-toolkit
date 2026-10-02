# openalice

Local trading-research orchestrator with agent workspaces, market tools, recurring research, inbox, quantitative projects, and optional broker integration.

[Upstream repository](https://github.com/TraderAlice/OpenAlice) · [Pinned source](https://github.com/TraderAlice/OpenAlice/tree/0d4faa90c67d6c24685c7b40679bea5a5742a215) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Finance and markets |
| Operating model | application |
| Recommended scope | on-demand |
| Registered production skill paths | 15 |
| Reviewed source commit | `0d4faa90c67d6c24685c7b40679bea5a5742a215` |

## Purpose and use cases

Supports native Codex/OpenCode agents but is a separate stateful application, not a global skill collection. Its default skills depend on Alice services; load them only within the app or adapt an individual workflow. Broker connections are optional and require separate explicit configuration.

**Discovery tags:** `finance`, `trading`, `research`, `orchestrator`, `codex`, `opencode`, `broker`, `market data`, `workspaces`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Desktop downloads documented for macOS/Windows; CLI/server path also supports Linux.
- Source build: Node >=22.19.0, pnpm 11.7.0, dependencies, and an installed host agent CLI with model login/credentials.
- Published native CLI does not require host Node/Bun; Linux installer expects Bash, tar/gzip, diff, checksum utility, curl, and flock.
- Market-data provider access depends on selected provider; broker credentials are only needed for broker features.

## Setup guidance

**Setup scope:** shared desktop/CLI application; selected data integrations

**Next action:** setup-required

**Working directory:** Isolated deployment/build working copy under runtime/openalice; preserve the pinned source checkout.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Choose a supported packaged CLI or source deployment. Configure the host agent/model and requested market-data providers; broker features are separate configuration.

**Verification to perform:** Verify local app/CLI startup and a read-only market-data example.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read openalice docs/cli-installer.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
pnpm install
```

Example 2:

```bash
pnpm dev
```

Example 3:

```bash
curl -fsSL https://openalice.ai/install | bash
```

## Source entry points

- [README.md](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/README.md)
- [package.json](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/package.json)
- [docs/cli-installer.md](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/docs/cli-installer.md)
- [docs/remote-quickstart.md](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/docs/remote-quickstart.md)

## Skills and retrieval

The manifest registers **15 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [.claude/skills/tool-audit/SKILL.md](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/.claude/skills/tool-audit/SKILL.md)
- [default/skills/alice-analysis/SKILL.md](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/default/skills/alice-analysis/SKILL.md)
- [default/skills/alice-uta/SKILL.md](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/default/skills/alice-uta/SKILL.md)
- [default/skills/alice/SKILL.md](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/default/skills/alice/SKILL.md)
- [default/skills/build-thesis/SKILL.md](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/default/skills/build-thesis/SKILL.md)
- [default/skills/delegate-autoquant/SKILL.md](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/default/skills/delegate-autoquant/SKILL.md)
- [default/skills/file-delivery/SKILL.md](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/default/skills/file-delivery/SKILL.md)
- [default/skills/market-data/SKILL.md](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/default/skills/market-data/SKILL.md)
- [default/skills/opencli-reader/SKILL.md](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/default/skills/opencli-reader/SKILL.md)
- [default/skills/retrospective/SKILL.md](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/default/skills/retrospective/SKILL.md)
- [default/skills/scan-value-chain/SKILL.md](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/default/skills/scan-value-chain/SKILL.md)
- [default/skills/sector-rotation/SKILL.md](https://github.com/TraderAlice/OpenAlice/blob/0d4faa90c67d6c24685c7b40679bea5a5742a215/default/skills/sector-rotation/SKILL.md)

Showing 12 of 15 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show openalice
bin/toolkit search "finance trading" --repo openalice
bin/toolkit docs openalice "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [TraderAlice/OpenAlice at `0d4faa90c67d`](https://github.com/TraderAlice/OpenAlice/tree/0d4faa90c67d6c24685c7b40679bea5a5742a215). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo openalice --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
