# scrapling

Python HTML parser, HTTP/browser fetchers, adaptive selectors, spider framework, scraping CLI, and optional MCP server.

[Upstream repository](https://github.com/D4Vinci/Scrapling) · [Pinned source](https://github.com/D4Vinci/Scrapling/tree/971d5edb9c01f000dd4befcd21742e9b22260dc7) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Browsers, research, and web data |
| Operating model | cli |
| Recommended scope | on-demand |
| Registered production skill paths | 1 |
| Reviewed source commit | `971d5edb9c01f000dd4befcd21742e9b22260dc7` |

## Purpose and use cases

Good local extraction option; install only the needed parser, fetcher, or MCP extras to avoid unnecessary browser downloads.

**Discovery tags:** `scraping`, `research`, `html`, `css-selectors`, `xpath`, `crawl`, `spider`, `playwright`, `mcp`, `markdown`, `rag`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Python >=3.10.
- Core parsing uses lxml, cssselect, orjson, tld, and w3lib.
- Fetchers need extra dependencies including curl_cffi, Playwright/Patchright and browser/system dependencies installed with scrapling install.
- MCP support uses the ai extra; no Scrapling account is required. Target-specific authentication or proxy configuration may be needed.

## Setup guidance

**Setup scope:** shared isolated CLI or project Python dependency; selected extras

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Choose core parsing, fetchers or ai/MCP extras. Browser fetchers additionally need documented browser/system setup; plain HTML parsing does not.

**Verification to perform:** Parse a small HTML sample first; test an isolated browser fetch only when fetchers were installed.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read scrapling README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
pip install scrapling
```

Example 2:

```bash
pip install "scrapling[fetchers]"
```

Example 3:

```bash
pip install "scrapling[ai]"
```

Example 4:

```bash
scrapling install
```

## Source entry points

- [README.md](https://github.com/D4Vinci/Scrapling/blob/971d5edb9c01f000dd4befcd21742e9b22260dc7/README.md)
- [pyproject.toml](https://github.com/D4Vinci/Scrapling/blob/971d5edb9c01f000dd4befcd21742e9b22260dc7/pyproject.toml)
- [agent-skill/Scrapling-Skill/SKILL.md](https://github.com/D4Vinci/Scrapling/blob/971d5edb9c01f000dd4befcd21742e9b22260dc7/agent-skill/Scrapling-Skill/SKILL.md)

## Skills and retrieval

The manifest registers **1 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [agent-skill/Scrapling-Skill/SKILL.md](https://github.com/D4Vinci/Scrapling/blob/971d5edb9c01f000dd4befcd21742e9b22260dc7/agent-skill/Scrapling-Skill/SKILL.md)

```bash
bin/toolkit show scrapling
bin/toolkit search "scraping research" --repo scrapling
bin/toolkit docs scrapling "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [D4Vinci/Scrapling at `971d5edb9c01`](https://github.com/D4Vinci/Scrapling/tree/971d5edb9c01f000dd4befcd21742e9b22260dc7). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo scrapling --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
