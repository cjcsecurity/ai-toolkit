# agent-browser

Native browser automation CLI with accessibility snapshots, compact element references, named sessions, screenshots and version-matched agent instructions.

[Upstream repository](https://github.com/vercel-labs/agent-browser) · [Pinned source](https://github.com/vercel-labs/agent-browser/tree/0207911f1bd4d0393eddaa90f2e50f96e0fb8974) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Browsers, research, and web data |
| Operating model | cli |
| Recommended scope | on-demand |
| Registered production skill paths | 2 |
| Reviewed source commit | `0207911f1bd4d0393eddaa90f2e50f96e0fb8974` |

## Purpose and use cases

On-demand alternative to existing Chrome DevTools and Playwright integrations. The public agent-browser skill is a discovery stub; read skill-data/core or installed CLI skills get core before use. Its preference for itself does not override the host tool policy. Register only the requested stub and supporting core; specialized workflows remain source references.

**Discovery tags:** `browser automation`, `accessibility snapshots`, `web testing`, `screenshots`, `agent-browser`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Chrome/Chromium and Linux browser libraries; existing Chrome, Brave, Playwright or Puppeteer browsers can be reused.
- Published native binary supports package-manager installation; source build requires Node.js 24+, pnpm 11+ and Rust.
- Cloud browsers, Slack/Electron sessions and protected deployments have separate account/access prerequisites; not needed for a local public-page check.

## Setup guidance

**Setup scope:** shared on-demand source; selected project or isolated runtime only

**Next action:** setup-required

**Working directory:** Read from the pinned checkout; apply only in the selected target project.

**Installation approach:** Source download and retrieval require no upstream runtime. For execution, reuse a compatible runtime or provision one isolated version following the pinned guide. Registration commands are alternatives, not an execution queue; do not install the entire collection globally.

**Configuration:** Use an isolated named session and a reviewed runtime version. Reuse existing browser binaries where compatible; do not attach to personal authenticated sessions implicitly.

**Verification to perform:** Verify version, load version-matched core instructions, open a public test page, inspect a snapshot and close the named session.

**Local record:** Record actual runtime and authentication checks in local project notes; source availability is not runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read agent-browser README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npm install agent-browser
```

Example 2:

```bash
agent-browser skills get core
```

Example 3:

```bash
agent-browser install
```

## Source entry points

- [README.md](https://github.com/vercel-labs/agent-browser/blob/0207911f1bd4d0393eddaa90f2e50f96e0fb8974/README.md)
- [package.json](https://github.com/vercel-labs/agent-browser/blob/0207911f1bd4d0393eddaa90f2e50f96e0fb8974/package.json)
- [skills/agent-browser/SKILL.md](https://github.com/vercel-labs/agent-browser/blob/0207911f1bd4d0393eddaa90f2e50f96e0fb8974/skills/agent-browser/SKILL.md)
- [skill-data/core/SKILL.md](https://github.com/vercel-labs/agent-browser/blob/0207911f1bd4d0393eddaa90f2e50f96e0fb8974/skill-data/core/SKILL.md)

## Skills and retrieval

The manifest registers **2 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/agent-browser/SKILL.md](https://github.com/vercel-labs/agent-browser/blob/0207911f1bd4d0393eddaa90f2e50f96e0fb8974/skills/agent-browser/SKILL.md)
- [skill-data/core/SKILL.md](https://github.com/vercel-labs/agent-browser/blob/0207911f1bd4d0393eddaa90f2e50f96e0fb8974/skill-data/core/SKILL.md)

```bash
bin/toolkit show agent-browser
bin/toolkit search "browser automation accessibility snapshots" --repo agent-browser
bin/toolkit docs agent-browser "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [vercel-labs/agent-browser at `0207911f1bd4`](https://github.com/vercel-labs/agent-browser/tree/0207911f1bd4d0393eddaa90f2e50f96e0fb8974). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo agent-browser --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
