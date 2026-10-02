# crucix

Local OSINT dashboard and data-collection application aggregating geopolitical, economic, environmental, transport, and market sources, with optional LLM analysis and messaging bots.

[Upstream repository](https://github.com/calesthio/Crucix) · [Pinned source](https://github.com/calesthio/Crucix/tree/3db7068817e0c815df353fa0f19657c85142789d) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Browsers, research, and web data |
| Operating model | application |
| Recommended scope | on-demand |
| Registered production skill paths | 0 |
| Reviewed source commit | `3db7068817e0c815df353fa0f19657c85142789d` |

## Purpose and use cases

Useful for situational research, but starting the dashboard triggers network data collection and scheduled refreshes; messaging integrations remain optional.

**Discovery tags:** `research`, `osint`, `dashboard`, `geopolitics`, `economic-data`, `satellite`, `weather`, `markets`, `data-sources`, `intelligence`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Node.js >=22 and npm >=10; Express runtime dependency, optional discord.js.
- Some public sources need no credentials; FRED_API_KEY, FIRMS_MAP_KEY, and EIA_API_KEY enable additional sources.
- Optional ACLED credentials, AISSTREAM_API_KEY, and ADSB_API_KEY unlock other feeds.
- Optional LLM_API_KEY or existing Codex authentication; Telegram/Discord alerts and bots need separately configured tokens/channels.

## Setup guidance

**Setup scope:** shared application deployment; chosen feeds and integrations

**Next action:** setup-required

**Working directory:** Isolated deployment/build working copy under runtime/crucix; preserve the pinned source checkout.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Create an isolated application working copy, install its Node dependencies, and configure only the selected public/API feeds and optional model/notification integrations.

**Verification to perform:** Start using the README instructions and confirm the dashboard receives a selected public feed.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read crucix README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npm install
```

Example 2:

```bash
npm install discord.js
```

## Source entry points

- [README.md](https://github.com/calesthio/Crucix/blob/3db7068817e0c815df353fa0f19657c85142789d/README.md)
- [package.json](https://github.com/calesthio/Crucix/blob/3db7068817e0c815df353fa0f19657c85142789d/package.json)
- [.env.example](https://github.com/calesthio/Crucix/blob/3db7068817e0c815df353fa0f19657c85142789d/.env.example)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show crucix
bin/toolkit search "research osint" --repo crucix
bin/toolkit docs crucix "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [calesthio/Crucix at `3db7068817e0`](https://github.com/calesthio/Crucix/tree/3db7068817e0c815df353fa0f19657c85142789d). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo crucix --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
