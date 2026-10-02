# browser-harness

CLI, agent skill, and optional stdio MCP server for controlling a real Chrome browser over CDP, with reusable local helper functions.

[Upstream repository](https://github.com/browser-use/browser-harness) · [Pinned source](https://github.com/browser-use/browser-harness/tree/afbcc381b963040c19627d788e40c7e7663171ee) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Browsers, research, and web data |
| Operating model | cli |
| Recommended scope | on-demand |
| Registered production skill paths | 1 |
| Reviewed source commit | `afbcc381b963040c19627d788e40c7e7663171ee` |

## Purpose and use cases

Useful for interactive browser tasks; connect only when the task needs access to the user browser and its sessions.

**Discovery tags:** `browser`, `research`, `automation`, `chrome`, `cdp`, `mcp`, `logged-in-browser`, `screenshots`, `scraping`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Package requires Python >=3.11; documented installation recommends uv with Python 3.12.
- Local Chrome with remote-debugging permission and a reachable CDP endpoint, or optional Browser Use Cloud credentials.
- Local Chrome mode does not need a Browser Use API key; web accounts are accessed through existing browser sessions.
- MCP server needs the mcp extra. Local recordings are optional and the documented setup asks for a preference with default off.

## Setup guidance

**Setup scope:** shared Python CLI; explicitly selected browser session

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Install the documented Python tool environment; configure local Chrome/CDP or the cloud option. Browser account access and recording settings are chosen separately.

**Verification to perform:** Use documented connection diagnostics and read a public test page title from the selected browser.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read browser-harness install.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
uv tool install --python 3.12 --upgrade --force browser-harness
```

## Source entry points

- [README.md](https://github.com/browser-use/browser-harness/blob/afbcc381b963040c19627d788e40c7e7663171ee/README.md)
- [install.md](https://github.com/browser-use/browser-harness/blob/afbcc381b963040c19627d788e40c7e7663171ee/install.md)
- [SKILL.md](https://github.com/browser-use/browser-harness/blob/afbcc381b963040c19627d788e40c7e7663171ee/SKILL.md)
- [docs/MCP.md](https://github.com/browser-use/browser-harness/blob/afbcc381b963040c19627d788e40c7e7663171ee/docs/MCP.md)
- [pyproject.toml](https://github.com/browser-use/browser-harness/blob/afbcc381b963040c19627d788e40c7e7663171ee/pyproject.toml)

## Skills and retrieval

The manifest registers **1 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [SKILL.md](https://github.com/browser-use/browser-harness/blob/afbcc381b963040c19627d788e40c7e7663171ee/SKILL.md)

```bash
bin/toolkit show browser-harness
bin/toolkit search "browser research" --repo browser-harness
bin/toolkit docs browser-harness "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [browser-use/browser-harness at `afbcc381b963`](https://github.com/browser-use/browser-harness/tree/afbcc381b963040c19627d788e40c7e7663171ee). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo browser-harness --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
