# chrome-devtools-mcp

Chrome automation and debugging MCP server plus CLI for DOM/browser interaction, screenshots, network/console inspection and performance traces.

[Upstream repository](https://github.com/ChromeDevTools/chrome-devtools-mcp) · [Pinned source](https://github.com/ChromeDevTools/chrome-devtools-mcp/tree/648a6676e7ed64394ae2bdc5ac1deb7802d0d037) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Browsers, research, and web data |
| Operating model | mcp |
| Recommended scope | on-demand |
| Registered production skill paths | 7 |
| Reviewed source commit | `648a6676e7ed64394ae2bdc5ac1deb7802d0d037` |

## Purpose and use cases

Strong engineering addition, best globally discoverable through a selector and activated on demand. --slim exposes only navigation, script execution and screenshots, reducing schema cost but omitting full diagnostic tools. Domain skills complement Superpowers; browser-testing instructions need the full server.

**Discovery tags:** `browser`, `chrome`, `devtools`, `debugging`, `performance`, `accessibility`, `mcp`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Node.js ^20.19.0 || ^22.12.0 || >=23 and npm
- Installed Google Chrome current stable or Chrome for Testing; other Chromium browsers are not officially supported
- Linux headless use should pass --headless; custom executable can be set using --executable-path
- Chrome launches lazily on first browser tool call; existing browser connection uses --browser-url or --ws-endpoint
- Usage statistics default enabled; --no-usage-statistics disables them; --no-performance-crux avoids CrUX requests

## Setup guidance

**Setup scope:** optional shared on-demand MCP and isolated browser

**Next action:** setup-required

**Working directory:** Read pinned sources in place. Use a separate runtime working copy or the selected target project for installations and generated files.

**Installation approach:** Use the pinned upstream documentation and choose one suitable route from install_commands. Lists can include alternatives, registration and launch commands; do not execute the entire list. Check for an existing compatible runtime before installing.

**Configuration:** Install compatible Node.js, the Chrome DevTools MCP package and a supported Chrome/Chrome-for-Testing binary. Configure the optional toolkit MCP launcher as described in docs/wiki/Runtime-Setup.md. Keep browser sessions isolated.

**Verification to perform:** toolkit-mcp --server chrome tools; verify one isolated browser interaction when needed.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read chrome-devtools-mcp README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx -y chrome-devtools-mcp@latest
```

Example 2:

```bash
npx -y chrome-devtools-mcp@latest --slim --headless
```

Example 3:

```bash
npx -y chrome-devtools-mcp@latest --headless --no-usage-statistics --no-performance-crux
```

## Source entry points

- [README.md](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/648a6676e7ed64394ae2bdc5ac1deb7802d0d037/README.md)
- [package.json](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/648a6676e7ed64394ae2bdc5ac1deb7802d0d037/package.json)
- [docs/configuration.md](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/648a6676e7ed64394ae2bdc5ac1deb7802d0d037/docs/configuration.md)
- [docs/client-configurations.md](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/648a6676e7ed64394ae2bdc5ac1deb7802d0d037/docs/client-configurations.md)
- [docs/advanced-usage.md](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/648a6676e7ed64394ae2bdc5ac1deb7802d0d037/docs/advanced-usage.md)
- [docs/cli.md](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/648a6676e7ed64394ae2bdc5ac1deb7802d0d037/docs/cli.md)
- [docs/slim-tool-reference.md](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/648a6676e7ed64394ae2bdc5ac1deb7802d0d037/docs/slim-tool-reference.md)

## Skills and retrieval

The manifest registers **7 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/a11y-debugging/SKILL.md](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/648a6676e7ed64394ae2bdc5ac1deb7802d0d037/skills/a11y-debugging/SKILL.md)
- [skills/chrome-devtools-cli/SKILL.md](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/648a6676e7ed64394ae2bdc5ac1deb7802d0d037/skills/chrome-devtools-cli/SKILL.md)
- [skills/chrome-devtools/SKILL.md](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/648a6676e7ed64394ae2bdc5ac1deb7802d0d037/skills/chrome-devtools/SKILL.md)
- [skills/cookie-debugging/SKILL.md](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/648a6676e7ed64394ae2bdc5ac1deb7802d0d037/skills/cookie-debugging/SKILL.md)
- [skills/debug-optimize-lcp/SKILL.md](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/648a6676e7ed64394ae2bdc5ac1deb7802d0d037/skills/debug-optimize-lcp/SKILL.md)
- [skills/memory-leak-debugging/SKILL.md](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/648a6676e7ed64394ae2bdc5ac1deb7802d0d037/skills/memory-leak-debugging/SKILL.md)
- [skills/troubleshooting/SKILL.md](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/648a6676e7ed64394ae2bdc5ac1deb7802d0d037/skills/troubleshooting/SKILL.md)

```bash
bin/toolkit show chrome-devtools-mcp
bin/toolkit search "browser chrome" --repo chrome-devtools-mcp
bin/toolkit docs chrome-devtools-mcp "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [ChromeDevTools/chrome-devtools-mcp at `648a6676e7ed`](https://github.com/ChromeDevTools/chrome-devtools-mcp/tree/648a6676e7ed64394ae2bdc5ac1deb7802d0d037). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo chrome-devtools-mcp --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
