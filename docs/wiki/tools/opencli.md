# opencli

TypeScript CLI with website/Electron adapters and browser primitives using a Chrome extension and local bridge daemon.

[Upstream repository](https://github.com/jackwener/OpenCLI) · [Pinned source](https://github.com/jackwener/OpenCLI/tree/24136945847afbfad266c6c46a8cd335377f9112) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Browsers, research, and web data |
| Operating model | cli |
| Recommended scope | on-demand |
| Registered production skill paths | 6 |
| Reviewed source commit | `24136945847afbfad266c6c46a8cd335377f9112` |

## Purpose and use cases

Useful specialized logged-in browser automation but overlaps AutoCLI and some Chrome DevTools features. Requires browser bridge and sessions, with broad site actions; activate for explicit website work instead of a universal engineering install. Several skills can be selected by task.

**Discovery tags:** `browser automation`, `website cli`, `electron`, `adapters`, `chrome extension`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Node.js >=20.18.1 for npm CLI installation; CLI supports Linux/macOS/Windows
- Chrome/Chromium Browser Bridge extension and local auto-start daemon for browser-backed commands
- Authenticated site sessions as needed; choose explicit profile when several are connected
- npm package contains postinstall adapter-fetch/setup scripts; inspect before installing
- Optional yt-dlp for some media downloads; desktop Electron targets need CDP access

## Setup guidance

**Setup scope:** shared CLI and browser bridge; per-site adapters

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Install the CLI once; set up the documented Chrome extension/bridge for browser-backed adapters and select an appropriate existing user-controlled session.

**Verification to perform:** Run opencli doctor, then a read-only adapter command.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read opencli README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npm install -g @jackwener/opencli
```

Example 2:

```bash
opencli doctor
```

Example 3:

```bash
npx skills add jackwener/opencli --skill opencli-browser
```

Example 4:

```bash
npx skills add jackwener/opencli --skill opencli-adapter-author
```

## Source entry points

- [README.md](https://github.com/jackwener/OpenCLI/blob/24136945847afbfad266c6c46a8cd335377f9112/README.md)
- [package.json](https://github.com/jackwener/OpenCLI/blob/24136945847afbfad266c6c46a8cd335377f9112/package.json)
- [docs/guide/extending-opencli.md](https://github.com/jackwener/OpenCLI/blob/24136945847afbfad266c6c46a8cd335377f9112/docs/guide/extending-opencli.md)
- [skills/opencli-browser/SKILL.md](https://github.com/jackwener/OpenCLI/blob/24136945847afbfad266c6c46a8cd335377f9112/skills/opencli-browser/SKILL.md)
- [skills/opencli-adapter-author/SKILL.md](https://github.com/jackwener/OpenCLI/blob/24136945847afbfad266c6c46a8cd335377f9112/skills/opencli-adapter-author/SKILL.md)
- [PRIVACY.md](https://github.com/jackwener/OpenCLI/blob/24136945847afbfad266c6c46a8cd335377f9112/PRIVACY.md)

## Skills and retrieval

The manifest registers **6 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [clis/antigravity/SKILL.md](https://github.com/jackwener/OpenCLI/blob/24136945847afbfad266c6c46a8cd335377f9112/clis/antigravity/SKILL.md)
- [skills/opencli-adapter-author/SKILL.md](https://github.com/jackwener/OpenCLI/blob/24136945847afbfad266c6c46a8cd335377f9112/skills/opencli-adapter-author/SKILL.md)
- [skills/opencli-autofix/SKILL.md](https://github.com/jackwener/OpenCLI/blob/24136945847afbfad266c6c46a8cd335377f9112/skills/opencli-autofix/SKILL.md)
- [skills/opencli-browser/SKILL.md](https://github.com/jackwener/OpenCLI/blob/24136945847afbfad266c6c46a8cd335377f9112/skills/opencli-browser/SKILL.md)
- [skills/opencli-usage/SKILL.md](https://github.com/jackwener/OpenCLI/blob/24136945847afbfad266c6c46a8cd335377f9112/skills/opencli-usage/SKILL.md)
- [skills/smart-search/SKILL.md](https://github.com/jackwener/OpenCLI/blob/24136945847afbfad266c6c46a8cd335377f9112/skills/smart-search/SKILL.md)

```bash
bin/toolkit show opencli
bin/toolkit search "browser automation website cli" --repo opencli
bin/toolkit docs opencli "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [jackwener/OpenCLI at `24136945847a`](https://github.com/jackwener/OpenCLI/tree/24136945847afbfad266c6c46a8cd335377f9112). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo opencli --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
