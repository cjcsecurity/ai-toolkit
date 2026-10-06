# moli

Rust headless browser for JavaScript-rendered page extraction, web search and automation through CLI, CDP and WebDriver, with optional layout and screenshots.

[Upstream repository](https://github.com/lexmount/moli) · [Pinned source](https://github.com/lexmount/moli/tree/b9fc881f87bf02ba4669860aaee6506684b2e7de) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Browsers, research, and web data |
| Operating model | cli + skills |
| Recommended scope | on-demand |
| Registered production skill paths | 3 |
| Reviewed source commit | `b9fc881f87bf02ba4669860aaee6506684b2e7de` |

## Purpose and use cases

Use a standalone browser kernel for DOM-first retrieval and agent browser tasks. Enable rendering only when needed; compatibility and visual fidelity differ from Chromium.

**Discovery tags:** `browser`, `web-extraction`, `scraping`, `web-search`, `cdp`, `webdriver`, `screenshots`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- A compatible Moli release binary for Linux, macOS or Windows; no separate Chrome or driver installation is required.
- Playwright, Puppeteer or Selenium are separate optional client dependencies for protocol automation; the open-source runtime does not require the managed Lexmount service.
- Real layout, geometry and screenshots require --layout; optional media and fonts require the corresponding resource options.
- MIT OR Apache-2.0 for the default code; vendored components and fixtures retain separate licenses and notices.

## Setup guidance

**Setup scope:** project-local or isolated tool runtime; explicit agent registration

**Next action:** setup-required

**Working directory:** An isolated tool checkout or the selected target project, according to the pinned setup guide.

**Installation approach:** Reuse a compatible runtime first. Select one documented installation route, review dependencies and pin the version; commands are examples, not a script to execute in order.

**Configuration:** Download and verify a platform release using the pinned installation guide. Keep the automation endpoint local and enable only required layout, resource and persistence options.

**Verification to perform:** Run moli --version and fetch a controlled sample page as Markdown; test protocol and screenshot behavior separately if needed.

**Local record:** Record the actual runtime version, checks and remaining requirements locally. Catalog/source presence does not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read moli README.md
```

### Documented commands and alternatives

No package installation command is recorded. Follow the setup guidance and pinned upstream instructions; source-only guidance may need no runtime.

## Source entry points

- [README.md](https://github.com/lexmount/moli/blob/b9fc881f87bf02ba4669860aaee6506684b2e7de/README.md)
- [license-metadata.json](https://github.com/lexmount/moli/blob/b9fc881f87bf02ba4669860aaee6506684b2e7de/license-metadata.json)
- [skills/moli-webfetch/SKILL.md](https://github.com/lexmount/moli/blob/b9fc881f87bf02ba4669860aaee6506684b2e7de/skills/moli-webfetch/SKILL.md)
- [skills/moli-websearch/SKILL.md](https://github.com/lexmount/moli/blob/b9fc881f87bf02ba4669860aaee6506684b2e7de/skills/moli-websearch/SKILL.md)
- [skills/moli-cdp-server/SKILL.md](https://github.com/lexmount/moli/blob/b9fc881f87bf02ba4669860aaee6506684b2e7de/skills/moli-cdp-server/SKILL.md)

## Skills and retrieval

The manifest registers **3 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/moli-cdp-server/SKILL.md](https://github.com/lexmount/moli/blob/b9fc881f87bf02ba4669860aaee6506684b2e7de/skills/moli-cdp-server/SKILL.md)
- [skills/moli-webfetch/SKILL.md](https://github.com/lexmount/moli/blob/b9fc881f87bf02ba4669860aaee6506684b2e7de/skills/moli-webfetch/SKILL.md)
- [skills/moli-websearch/SKILL.md](https://github.com/lexmount/moli/blob/b9fc881f87bf02ba4669860aaee6506684b2e7de/skills/moli-websearch/SKILL.md)

```bash
bin/toolkit show moli
bin/toolkit search "browser web-extraction" --repo moli
bin/toolkit docs moli "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [lexmount/moli at `b9fc881f87bf`](https://github.com/lexmount/moli/tree/b9fc881f87bf02ba4669860aaee6506684b2e7de). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo moli --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
