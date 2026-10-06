# rea

CLI, MCP server and investigation skill for evidence-based analysis of native binaries, Electron/JavaScript applications, .NET assemblies and websites.

[Upstream repository](https://github.com/morluto/rea) · [Pinned source](https://github.com/morluto/rea/tree/9b392bb2f83decda39b4f871a079b411082bcd2f) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Engineering and code intelligence |
| Operating model | cli + mcp + skill |
| Recommended scope | on-demand |
| Registered production skill paths | 1 |
| Reviewed source commit | `9b392bb2f83decda39b4f871a079b411082bcd2f` |

## Purpose and use cases

Inspect application behavior and recover cited implementation evidence with local analysis providers; decompilation yields pseudocode, not original source.

**Discovery tags:** `reverse-engineering`, `binary-analysis`, `ghidra`, `hopper`, `electron`, `mcp`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Node.js 22.19+ or 24.11+ and npm; supported hosts are macOS 12+, Ubuntu 24.04+, Fedora 41+ and 64-bit Arch Linux. Windows operations remain unavailable at this revision.
- Native analysis requires separately installed Hopper (separate vendor license/demo limits) or Ghidra 12.1.4 with a 64-bit JDK 21; Ghidra supports Linux x64 and macOS x64/arm64.
- Linux Hopper demo sessions require Python 3, Xvfb, X11 and XTEST; setup may request system package installation.
- REA is MIT-licensed; analysis-provider licenses and target authorization are separate.

## Setup guidance

**Setup scope:** project-local or isolated tool runtime; explicit agent registration

**Next action:** setup-required

**Working directory:** An isolated tool checkout or the selected target project, according to the pinned setup guide.

**Installation approach:** Reuse a compatible runtime first. Select one documented installation route, review dependencies and pin the version; commands are examples, not a script to execute in order.

**Configuration:** Select the agent registrations and analysis provider explicitly; review setup changes and preserve existing client configuration.

**Verification to perform:** Run rea doctor --json, then analyze an owned local sample and inspect the evidence and provider limitations.

**Local record:** Record the actual runtime version, checks and remaining requirements locally. Catalog/source presence does not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read rea README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npm install --global rea-agents
```

Example 2:

```bash
npx rea-agents setup
```

## Source entry points

- [README.md](https://github.com/morluto/rea/blob/9b392bb2f83decda39b4f871a079b411082bcd2f/README.md)
- [docs/installation.md](https://github.com/morluto/rea/blob/9b392bb2f83decda39b4f871a079b411082bcd2f/docs/installation.md)
- [package.json](https://github.com/morluto/rea/blob/9b392bb2f83decda39b4f871a079b411082bcd2f/package.json)
- [skills/reverse-engineer-anything/SKILL.md](https://github.com/morluto/rea/blob/9b392bb2f83decda39b4f871a079b411082bcd2f/skills/reverse-engineer-anything/SKILL.md)

## Skills and retrieval

The manifest registers **1 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/reverse-engineer-anything/SKILL.md](https://github.com/morluto/rea/blob/9b392bb2f83decda39b4f871a079b411082bcd2f/skills/reverse-engineer-anything/SKILL.md)

```bash
bin/toolkit show rea
bin/toolkit search "reverse-engineering binary-analysis" --repo rea
bin/toolkit docs rea "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [morluto/rea at `9b392bb2f83d`](https://github.com/morluto/rea/tree/9b392bb2f83decda39b4f871a079b411082bcd2f). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo rea --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
