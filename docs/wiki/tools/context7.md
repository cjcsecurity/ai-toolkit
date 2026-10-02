# context7

Context7 CLI, MCP server, SDKs and agent skills retrieve version-specific library documentation and code snippets from the hosted Context7 index.

[Upstream repository](https://github.com/upstash/context7) · [Pinned source](https://github.com/upstash/context7/tree/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Engineering and code intelligence |
| Operating model | cli |
| Recommended scope | global-cli |
| Registered production skill paths | 9 |
| Reviewed source commit | `635cfc8a1ea86c8a3505128b9d7e46e1f39357e1` |

## Purpose and use cases

Resolve a library ID and retrieve focused current docs through the one-shot CLI; configure MCP only for projects that need it. Source checkout includes public clients, not the private API backend, parsing or crawling engines. Provider-specific skill copies are available but canonical skills avoid duplicate discovery.

**Discovery tags:** `library documentation`, `api reference`, `version migration`, `context7`, `ctx7`, `mcp`, `skills`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- ctx7 0.5.12 declares Node.js >=18; @upstash/context7-mcp 4.1.1 requires Node.js >=20.18.1.
- Network access to the hosted Context7 service; local MCP is a client to that service rather than a self-hosted docs backend.
- CLI library/docs and MCP usage are documented as usable without authentication at lower quotas; CONTEXT7_API_KEY or browser OAuth provides higher limits. Direct REST API documentation requires Authorization: Bearer API-key for all requests.
- ctx7 setup authenticates and installs agent configuration/skills; ctx7 skills generate requires login. Avoid setup for a read-only docs query.
- Documentation queries are sent to Context7; use focused public technology questions rather than credentials or proprietary source.

## Setup guidance

**Setup scope:** optional shared CLI; hosted documentation service

**Next action:** setup-required

**Working directory:** Read pinned sources in place. Use a separate runtime working copy or the selected target project for installations and generated files.

**Installation approach:** Use the pinned upstream documentation and choose one suitable route from install_commands. Lists can include alternatives, registration and launch commands; do not execute the entire list. Check for an existing compatible runtime before installing.

**Configuration:** Install the ctx7 CLI. Public library/docs queries can work without login at lower quotas. Authenticated setup or native MCP registration is a separate optional integration.

**Verification to perform:** ctx7 --version; resolve one library and query a focused documentation topic.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read context7 skills/context7-cli/references/setup.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npm install -g ctx7@0.5.12
```

Example 2:

```bash
npx ctx7@0.5.12 --help
```

Example 3:

```bash
npx -y @upstash/context7-mcp@4.1.1 --help
```

## Source entry points

- [README.md](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/README.md)
- [packages/cli/package.json](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/packages/cli/package.json)
- [packages/mcp/package.json](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/packages/mcp/package.json)
- [packages/mcp/README.md](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/packages/mcp/README.md)
- [docs/clients/cli.mdx](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/docs/clients/cli.mdx)
- [docs/clients/codex.mdx](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/docs/clients/codex.mdx)
- [docs/api-guide.mdx](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/docs/api-guide.mdx)
- [skills/context7-cli/references/docs.md](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/skills/context7-cli/references/docs.md)
- [skills/context7-cli/references/setup.md](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/skills/context7-cli/references/setup.md)
- [skills/context7-cli/references/skills.md](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/skills/context7-cli/references/skills.md)

## Skills and retrieval

The manifest registers **9 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/context7-cli/SKILL.md](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/skills/context7-cli/SKILL.md)
- [skills/find-docs/SKILL.md](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/skills/find-docs/SKILL.md)
- [skills/context7-mcp/SKILL.md](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/skills/context7-mcp/SKILL.md)
- [packages/pi/skills/context7-docs/SKILL.md](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/packages/pi/skills/context7-docs/SKILL.md)
- [packages/opencode/skills/context7-mcp/SKILL.md](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/packages/opencode/skills/context7-mcp/SKILL.md)
- [plugins/codex/context7/skills/context7-mcp/SKILL.md](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/plugins/codex/context7/skills/context7-mcp/SKILL.md)
- [plugins/agent-plugins/context7/skills/context7-mcp/SKILL.md](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/plugins/agent-plugins/context7/skills/context7-mcp/SKILL.md)
- [plugins/copilot/context7/skills/context7-mcp/SKILL.md](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/plugins/copilot/context7/skills/context7-mcp/SKILL.md)
- [plugins/cursor/context7/skills/context7-mcp/SKILL.md](https://github.com/upstash/context7/blob/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1/plugins/cursor/context7/skills/context7-mcp/SKILL.md)

```bash
bin/toolkit show context7
bin/toolkit search "library documentation api reference" --repo context7
bin/toolkit docs context7 "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [upstash/context7 at `635cfc8a1ea8`](https://github.com/upstash/context7/tree/635cfc8a1ea86c8a3505128b9d7e46e1f39357e1). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo context7 --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
