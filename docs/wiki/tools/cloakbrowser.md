# cloakbrowser

Python/JavaScript wrappers and CLI around a separately downloaded patched Chromium browser, compatible with Playwright/Puppeteer workflows and persistent profiles.

[Upstream repository](https://github.com/CloakHQ/CloakBrowser) · [Pinned source](https://github.com/CloakHQ/CloakBrowser/tree/f44864b6ed3c5fe9cc48fb9954fb413b5b2a02ef) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Browsers, research, and web data |
| Operating model | cli |
| Recommended scope | on-demand |
| Registered production skill paths | 0 |
| Reviewed source commit | `f44864b6ed3c5fe9cc48fb9954fb413b5b2a02ef` |

## Purpose and use cases

Optional browser backend for difficult automation; installation downloads an external browser binary and current builds have account/license requirements.

**Discovery tags:** `browser`, `scraping`, `automation`, `chromium`, `playwright`, `puppeteer`, `fingerprint`, `persistent-profile`, `cdp`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Python >=3.9 with Playwright/httpx/cryptography, or JavaScript runtime with playwright-core/puppeteer-core.
- Downloaded platform-specific Chromium binary and Linux browser system libraries/fonts as applicable.
- README states latest binary needs a free GitHub-sign-in license key for one concurrent session or a paid key; older v146 binary works without a key.
- Proxies and authenticated browser profiles are optional and task-dependent.

## Setup guidance

**Setup scope:** project SDK or isolated reusable browser environment

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Choose the Python or JS binding and Playwright or Puppeteer integration; install the patched browser and required system libraries for that route.

**Verification to perform:** Launch an isolated browser, open a public/local test page, then close it.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read cloakbrowser README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
pip install cloakbrowser
```

Example 2:

```bash
npm install cloakbrowser playwright-core
```

Example 3:

```bash
npm install cloakbrowser puppeteer-core
```

Example 4:

```bash
playwright install-deps chromium
```

## Source entry points

- [README.md](https://github.com/CloakHQ/CloakBrowser/blob/f44864b6ed3c5fe9cc48fb9954fb413b5b2a02ef/README.md)
- [pyproject.toml](https://github.com/CloakHQ/CloakBrowser/blob/f44864b6ed3c5fe9cc48fb9954fb413b5b2a02ef/pyproject.toml)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show cloakbrowser
bin/toolkit search "browser scraping" --repo cloakbrowser
bin/toolkit docs cloakbrowser "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [CloakHQ/CloakBrowser at `f44864b6ed3c`](https://github.com/CloakHQ/CloakBrowser/tree/f44864b6ed3c5fe9cc48fb9954fb413b5b2a02ef). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo cloakbrowser --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
