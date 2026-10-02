# firecrawl

Web-data API and SDKs for search, URL scraping, crawling, mapping, browser interactions, and structured extraction; includes self-hosted server source and agent skills.

[Upstream repository](https://github.com/firecrawl/firecrawl) · [Pinned source](https://github.com/firecrawl/firecrawl/tree/c4873f545dfdb6a164763cbcf34bf043b06803db) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Browsers, research, and web data |
| Operating model | application |
| Recommended scope | on-demand |
| Registered production skill paths | 5 |
| Reviewed source commit | `c4873f545dfdb6a164763cbcf34bf043b06803db` |

## Purpose and use cases

Useful hosted scraping option with CLI/MCP integrations; enable a selected integration when needed rather than launching the full service globally.

**Discovery tags:** `scraping`, `research`, `web-search`, `crawl`, `markdown`, `structured-extraction`, `browser`, `mcp`, `sdk`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Hosted use: Firecrawl account and FIRECRAWL_API_KEY; service usage may consume credits.
- Python SDK or Node.js SDK/CLI runtime, depending on integration.
- Self-hosting: Docker/Compose stack includes API/workers, Playwright, Redis, RabbitMQ, and NuQ PostgreSQL; configure optional services per SELF_HOST.md.
- Some hosted features and proprietary scraping components are not included in the local stack.

## Setup guidance

**Setup scope:** hosted service plus project SDK, or shared self-hosted stack

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Choose hosted API/CLI or SELF_HOST.md deployment. Hosted use needs an API key; self-hosting has different components and feature coverage.

**Verification to perform:** Fetch one public test URL through the configured endpoint and inspect the returned content.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read firecrawl SELF_HOST.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
pip install firecrawl-py
```

Example 2:

```bash
npm install firecrawl
```

Example 3:

```bash
npx -y firecrawl-cli@latest init --all --browser
```

## Source entry points

- [README.md](https://github.com/firecrawl/firecrawl/blob/c4873f545dfdb6a164763cbcf34bf043b06803db/README.md)
- [SELF_HOST.md](https://github.com/firecrawl/firecrawl/blob/c4873f545dfdb6a164763cbcf34bf043b06803db/SELF_HOST.md)
- [skills/firecrawl-build/SKILL.md](https://github.com/firecrawl/firecrawl/blob/c4873f545dfdb6a164763cbcf34bf043b06803db/skills/firecrawl-build/SKILL.md)
- [apps/api/package.json](https://github.com/firecrawl/firecrawl/blob/c4873f545dfdb6a164763cbcf34bf043b06803db/apps/api/package.json)

## Skills and retrieval

The manifest registers **5 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/firecrawl-build-interact/SKILL.md](https://github.com/firecrawl/firecrawl/blob/c4873f545dfdb6a164763cbcf34bf043b06803db/skills/firecrawl-build-interact/SKILL.md)
- [skills/firecrawl-build-onboarding/SKILL.md](https://github.com/firecrawl/firecrawl/blob/c4873f545dfdb6a164763cbcf34bf043b06803db/skills/firecrawl-build-onboarding/SKILL.md)
- [skills/firecrawl-build-scrape/SKILL.md](https://github.com/firecrawl/firecrawl/blob/c4873f545dfdb6a164763cbcf34bf043b06803db/skills/firecrawl-build-scrape/SKILL.md)
- [skills/firecrawl-build-search/SKILL.md](https://github.com/firecrawl/firecrawl/blob/c4873f545dfdb6a164763cbcf34bf043b06803db/skills/firecrawl-build-search/SKILL.md)
- [skills/firecrawl-build/SKILL.md](https://github.com/firecrawl/firecrawl/blob/c4873f545dfdb6a164763cbcf34bf043b06803db/skills/firecrawl-build/SKILL.md)

```bash
bin/toolkit show firecrawl
bin/toolkit search "scraping research" --repo firecrawl
bin/toolkit docs firecrawl "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [firecrawl/firecrawl at `c4873f545dfd`](https://github.com/firecrawl/firecrawl/tree/c4873f545dfdb6a164763cbcf34bf043b06803db). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo firecrawl --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
