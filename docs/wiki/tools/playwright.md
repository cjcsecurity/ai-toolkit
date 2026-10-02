# playwright

Browser automation and end-to-end tests across Chromium, Firefox and WebKit, with locators, web-first assertions, screenshots, network mocking, tracing and production CLI/trace/component-testing skills.

[Upstream repository](https://github.com/microsoft/playwright) · [Pinned source](https://github.com/microsoft/playwright/tree/b630e71fcda7885885c459bcbb88e5bfa7c0a1ac) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Browsers, research, and web data |
| Operating model | framework |
| Recommended scope | on-demand |
| Registered production skill paths | 3 |
| Reviewed source commit | `b630e71fcda7885885c459bcbb88e5bfa7c0a1ac` |

## Purpose and use cases

Use the target project's Playwright version for durable tests and isolated browser workflows. The reviewed checkout is development version 1.64.0-next, so newly documented CLI/trace/mount behavior must be checked against any installed stable version. Exclude upstream .claude maintenance/triage skills; preserve production skills and their references/templates.

**Discovery tags:** `browser testing`, `e2e`, `automation`, `screenshots`, `visual regression`, `trace`, `component testing`, `playwright-cli`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Reviewed package manifests require Node.js >=20; current setup guide recommends latest 22.x, 24.x or 26.x.
- Compatible browser downloads and Linux system libraries are required; npx playwright install installs browsers, --with-deps additionally installs OS packages.
- Reviewed guide supports Windows 11+/Server 2019+/WSL, macOS 14+, Debian 12/13 and Ubuntu 22.04/24.04/26.04 on x86-64 or arm64.
- Authenticated app testing requires explicitly configured storage state/test credentials; isolated sessions do not inherit the user's regular browser login.
- CLI skill requires @playwright/cli or a sufficiently new local playwright cli. Trace/component-testing skills describe development features and may need a matching release. Framework-specific gallery/component tests require the app's dev server and React/Vue build setup.

## Setup guidance

**Setup scope:** existing shared browser runtime; project-local test dependency

**Next action:** setup-required

**Working directory:** Read pinned sources in place. Use a separate runtime working copy or the selected target project for installations and generated files.

**Installation approach:** Use the pinned upstream documentation and choose one suitable route from install_commands. Lists can include alternatives, registration and launch commands; do not execute the entire list. Check for an existing compatible runtime before installing.

**Configuration:** Install a compatible pinned @playwright/test dependency and browser in the target project or prepare a separate shared CLI environment. Reuse an existing runtime only after checking it. Browser and native system dependencies are separate.

**Verification to perform:** Use the installed project's Playwright CLI --version and run one local browser interaction or the project's smallest browser test.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read playwright README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npm install --save-dev @playwright/test
```

Example 2:

```bash
npx playwright install chromium
```

Example 3:

```bash
npm install -g @playwright/cli@latest
```

## Source entry points

- [README.md](https://github.com/microsoft/playwright/blob/b630e71fcda7885885c459bcbb88e5bfa7c0a1ac/README.md)
- [package.json](https://github.com/microsoft/playwright/blob/b630e71fcda7885885c459bcbb88e5bfa7c0a1ac/package.json)
- [packages/playwright/package.json](https://github.com/microsoft/playwright/blob/b630e71fcda7885885c459bcbb88e5bfa7c0a1ac/packages/playwright/package.json)
- [docs/src/intro-js.md](https://github.com/microsoft/playwright/blob/b630e71fcda7885885c459bcbb88e5bfa7c0a1ac/docs/src/intro-js.md)
- [docs/src/browsers.md](https://github.com/microsoft/playwright/blob/b630e71fcda7885885c459bcbb88e5bfa7c0a1ac/docs/src/browsers.md)
- [docs/src/test-assertions-js.md](https://github.com/microsoft/playwright/blob/b630e71fcda7885885c459bcbb88e5bfa7c0a1ac/docs/src/test-assertions-js.md)
- [docs/src/trace-viewer.md](https://github.com/microsoft/playwright/blob/b630e71fcda7885885c459bcbb88e5bfa7c0a1ac/docs/src/trace-viewer.md)
- [docs/src/auth.md](https://github.com/microsoft/playwright/blob/b630e71fcda7885885c459bcbb88e5bfa7c0a1ac/docs/src/auth.md)
- [docs/src/network.md](https://github.com/microsoft/playwright/blob/b630e71fcda7885885c459bcbb88e5bfa7c0a1ac/docs/src/network.md)
- [packages/playwright-core/src/tools/skills/playwright-cli/references/session-management.md](https://github.com/microsoft/playwright/blob/b630e71fcda7885885c459bcbb88e5bfa7c0a1ac/packages/playwright-core/src/tools/skills/playwright-cli/references/session-management.md)
- [packages/playwright-core/src/tools/skills/playwright-cli/references/test-generation.md](https://github.com/microsoft/playwright/blob/b630e71fcda7885885c459bcbb88e5bfa7c0a1ac/packages/playwright-core/src/tools/skills/playwright-cli/references/test-generation.md)
- [packages/playwright-core/src/tools/skills/playwright-component-testing/references/gallery-spec.md](https://github.com/microsoft/playwright/blob/b630e71fcda7885885c459bcbb88e5bfa7c0a1ac/packages/playwright-core/src/tools/skills/playwright-component-testing/references/gallery-spec.md)

## Skills and retrieval

The manifest registers **3 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [packages/playwright-core/src/tools/skills/playwright-cli/SKILL.md](https://github.com/microsoft/playwright/blob/b630e71fcda7885885c459bcbb88e5bfa7c0a1ac/packages/playwright-core/src/tools/skills/playwright-cli/SKILL.md)
- [packages/playwright-core/src/tools/skills/playwright-trace/SKILL.md](https://github.com/microsoft/playwright/blob/b630e71fcda7885885c459bcbb88e5bfa7c0a1ac/packages/playwright-core/src/tools/skills/playwright-trace/SKILL.md)
- [packages/playwright-core/src/tools/skills/playwright-component-testing/SKILL.md](https://github.com/microsoft/playwright/blob/b630e71fcda7885885c459bcbb88e5bfa7c0a1ac/packages/playwright-core/src/tools/skills/playwright-component-testing/SKILL.md)

```bash
bin/toolkit show playwright
bin/toolkit search "browser testing e2e" --repo playwright
bin/toolkit docs playwright "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [microsoft/playwright at `b630e71fcda7`](https://github.com/microsoft/playwright/tree/b630e71fcda7885885c459bcbb88e5bfa7c0a1ac). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo playwright --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
