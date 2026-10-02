# open-design

Local design studio and daemon for prototypes, decks, images, videos, design systems, plugin catalogs, and integration with coding-agent CLIs; includes a stdio MCP interface.

[Upstream repository](https://github.com/nexu-io/open-design) · [Pinned source](https://github.com/nexu-io/open-design/tree/53231d40b778d88eba23f35547bf99485d3ae9fc) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Design and interfaces |
| Operating model | application |
| Recommended scope | on-demand |
| Registered production skill paths | 338 |
| Reviewed source commit | `53231d40b778d88eba23f35547bf99485d3ae9fc` |

## Purpose and use cases

Use the app or selected portable resources for a specific design task. Its copied skills, official plugins, examples, templates, and test fixtures must not all become global skills. Codex and OpenCode MCP adapters are documented.

**Discovery tags:** `design studio`, `prototype`, `slides`, `video`, `mcp`, `design systems`, `codex`, `opencode`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Source runtime: Node ~24 and pnpm >=10.33.2 <11; package manager pin pnpm 10.33.2.
- Official desktop builds: macOS and Windows; Linux currently runs from source or Docker.
- Installed/authenticated agent CLI or a configured model endpoint; paid providers and hosted image/video features need credentials.
- Starting the app or MCP integration requires a separate installation; source postinstall script exists and was not run.

## Setup guidance

**Setup scope:** isolated application deployment; per-client integration

**Next action:** setup-required

**Working directory:** Isolated deployment/build working copy under runtime/open-design; preserve the pinned source checkout.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** On Linux use the documented source/Docker route. Install dependencies in a working copy, configure the chosen agent/model, then add only the intended client integration.

**Verification to perform:** Start the local app and verify a sample design; test MCP discovery separately if selected.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read open-design QUICKSTART.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
corepack enable && pnpm install
```

Example 2:

```bash
pnpm tools-dev run web
```

Example 3:

```bash
od mcp install codex
```

Example 4:

```bash
od mcp install opencode
```

## Source entry points

- [README.md](https://github.com/nexu-io/open-design/blob/53231d40b778d88eba23f35547bf99485d3ae9fc/README.md)
- [QUICKSTART.md](https://github.com/nexu-io/open-design/blob/53231d40b778d88eba23f35547bf99485d3ae9fc/QUICKSTART.md)
- [docs/agent-adapters.md](https://github.com/nexu-io/open-design/blob/53231d40b778d88eba23f35547bf99485d3ae9fc/docs/agent-adapters.md)
- [package.json](https://github.com/nexu-io/open-design/blob/53231d40b778d88eba23f35547bf99485d3ae9fc/package.json)

## Skills and retrieval

The manifest registers **338 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [.claude/skills/od-contribute/SKILL.md](https://github.com/nexu-io/open-design/blob/53231d40b778d88eba23f35547bf99485d3ae9fc/.claude/skills/od-contribute/SKILL.md)
- [design-templates/audio-jingle/SKILL.md](https://github.com/nexu-io/open-design/blob/53231d40b778d88eba23f35547bf99485d3ae9fc/design-templates/audio-jingle/SKILL.md)
- [design-templates/blog-post/SKILL.md](https://github.com/nexu-io/open-design/blob/53231d40b778d88eba23f35547bf99485d3ae9fc/design-templates/blog-post/SKILL.md)
- [design-templates/clinical-case-report/SKILL.md](https://github.com/nexu-io/open-design/blob/53231d40b778d88eba23f35547bf99485d3ae9fc/design-templates/clinical-case-report/SKILL.md)
- [design-templates/contact-widget/SKILL.md](https://github.com/nexu-io/open-design/blob/53231d40b778d88eba23f35547bf99485d3ae9fc/design-templates/contact-widget/SKILL.md)
- [design-templates/critique/SKILL.md](https://github.com/nexu-io/open-design/blob/53231d40b778d88eba23f35547bf99485d3ae9fc/design-templates/critique/SKILL.md)
- [design-templates/dashboard/SKILL.md](https://github.com/nexu-io/open-design/blob/53231d40b778d88eba23f35547bf99485d3ae9fc/design-templates/dashboard/SKILL.md)
- [design-templates/dating-web/SKILL.md](https://github.com/nexu-io/open-design/blob/53231d40b778d88eba23f35547bf99485d3ae9fc/design-templates/dating-web/SKILL.md)
- [design-templates/dcf-valuation/SKILL.md](https://github.com/nexu-io/open-design/blob/53231d40b778d88eba23f35547bf99485d3ae9fc/design-templates/dcf-valuation/SKILL.md)
- [design-templates/digital-eguide/SKILL.md](https://github.com/nexu-io/open-design/blob/53231d40b778d88eba23f35547bf99485d3ae9fc/design-templates/digital-eguide/SKILL.md)
- [design-templates/docs-page/SKILL.md](https://github.com/nexu-io/open-design/blob/53231d40b778d88eba23f35547bf99485d3ae9fc/design-templates/docs-page/SKILL.md)
- [design-templates/email-marketing/SKILL.md](https://github.com/nexu-io/open-design/blob/53231d40b778d88eba23f35547bf99485d3ae9fc/design-templates/email-marketing/SKILL.md)

Showing 12 of 338 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show open-design
bin/toolkit search "design studio prototype" --repo open-design
bin/toolkit docs open-design "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [nexu-io/open-design at `53231d40b778`](https://github.com/nexu-io/open-design/tree/53231d40b778d88eba23f35547bf99485d3ae9fc). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo open-design --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
