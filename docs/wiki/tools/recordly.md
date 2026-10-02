# recordly

Electron desktop screen recorder and editor with automatic zooms, cursor effects, webcam overlays, timeline editing, and video/GIF export.

[Upstream repository](https://github.com/webadderallorg/Recordly) · [Pinned source](https://github.com/webadderallorg/Recordly/tree/18884285b11b3603fc4ccede89add40e0e4a9bd6) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Writing, video, and audio |
| Operating model | application |
| Recommended scope | on-demand |
| Registered production skill paths | 0 |
| Reviewed source commit | `18884285b11b3603fc4ccede89add40e0e4a9bd6` |

## Purpose and use cases

Standalone desktop application rather than an Agent Skill or documented Codex/OpenCode MCP integration. Keep source and build instructions available for recording/editing needs.

**Discovery tags:** `screen recorder`, `demo video`, `desktop`, `electron`, `cursor`, `zoom`, `video editor`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Desktop session required; macOS 14+, Windows 10 build 19041+, or modern Linux.
- Linux uses Electron capture and generally PipeWire for system audio; cursor hiding is unsupported on Linux.
- Source build needs Node/npm plus native build tools: Linux build-essential/cmake/libx11-dev/libxtst-dev/libxrandr-dev/libxt-dev, macOS Xcode CLI tools, or Windows Visual Studio C++ tools/CMake.

## Setup guidance

**Setup scope:** desktop application; GUI/audio/capture prerequisites

**Next action:** setup-required

**Working directory:** Isolated deployment/build working copy under runtime/recordly; preserve the pinned source checkout.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Choose a supported release or source build in a working copy. A desktop session and OS-specific capture/audio dependencies are required; headless CLI availability is insufficient.

**Verification to perform:** Launch the UI and make a short disposable recording/export with the selected capture method.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read recordly README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npm install
```

Example 2:

```bash
npm run dev
```

Example 3:

```bash
npm run build
```

## Source entry points

- [README.md](https://github.com/webadderallorg/Recordly/blob/18884285b11b3603fc4ccede89add40e0e4a9bd6/README.md)
- [package.json](https://github.com/webadderallorg/Recordly/blob/18884285b11b3603fc4ccede89add40e0e4a9bd6/package.json)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show recordly
bin/toolkit search "screen recorder demo video" --repo recordly
bin/toolkit docs recordly "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [webadderallorg/Recordly at `18884285b11b`](https://github.com/webadderallorg/Recordly/tree/18884285b11b3603fc4ccede89add40e0e4a9bd6). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo recordly --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
