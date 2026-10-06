# filmcraft

Rust non-linear video editor with timeline editing, color grading, audio mixing, captions and export, exposed through desktop, CLI and MCP interfaces.

[Upstream repository](https://github.com/storytold/filmcraft) · [Pinned source](https://github.com/storytold/filmcraft/tree/ada55eb62568ba75be25cd12bd07b5fbdc37f88d) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Writing, video, and audio |
| Operating model | desktop application + cli + mcp |
| Recommended scope | on-demand |
| Registered production skill paths | 0 |
| Reviewed source commit | `ada55eb62568ba75be25cd12bd07b5fbdc37f88d` |

## Purpose and use cases

Edit media with an agent-accessible command engine and interchange formats. Upstream reports substantial remaining production gaps, including platform testing and large-footage performance.

**Discovery tags:** `video-editing`, `timeline`, `color-grading`, `audio`, `captions`, `mcp`, `rust`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Rust 1.95+ and Cargo for source builds; macOS requires Xcode command-line tools, Windows MSVC build tools, and Linux a C toolchain plus ALSA, GTK 3 and X11/Wayland development packages.
- Desktop graphics/audio support is needed for the UI. Headless CLI and stdio MCP are separate modes. FFmpeg/ffprobe are optional test oracles, not the internal codec runtime.
- Hardware decoding is currently macOS-only; no VST3/Audio Units/OpenFX hosting and no HEVC/AV1 export at this pin. Windows and Linux receive less upstream testing.
- MIT OR Apache-2.0 code; third-party component and asset notices remain separate.

## Setup guidance

**Setup scope:** project-local or isolated tool runtime; explicit agent registration

**Next action:** setup-required

**Working directory:** An isolated tool checkout or the selected target project, according to the pinned setup guide.

**Installation approach:** Reuse a compatible runtime first. Select one documented installation route, review dependencies and pin the version; commands are examples, not a script to execute in order.

**Configuration:** Build the selected desktop or CLI target. Register stdio MCP only in the intended agent, and keep source media separate from test output.

**Verification to perform:** List CLI commands, render a short disposable sample and inspect the exported frames/audio before using a real editing project.

**Local record:** Record the actual runtime version, checks and remaining requirements locally. Catalog/source presence does not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read filmcraft README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
cargo run --release -p filmcraft
```

Example 2:

```bash
cargo run --release -p filmcraft-cli -- mcp
```

## Source entry points

- [README.md](https://github.com/storytold/filmcraft/blob/ada55eb62568ba75be25cd12bd07b5fbdc37f88d/README.md)
- [Cargo.toml](https://github.com/storytold/filmcraft/blob/ada55eb62568ba75be25cd12bd07b5fbdc37f88d/Cargo.toml)
- [docs/contributing.md](https://github.com/storytold/filmcraft/blob/ada55eb62568ba75be25cd12bd07b5fbdc37f88d/docs/contributing.md)
- [docs/agents.md](https://github.com/storytold/filmcraft/blob/ada55eb62568ba75be25cd12bd07b5fbdc37f88d/docs/agents.md)
- [docs/control-protocol.md](https://github.com/storytold/filmcraft/blob/ada55eb62568ba75be25cd12bd07b5fbdc37f88d/docs/control-protocol.md)
- [ROADMAP.md](https://github.com/storytold/filmcraft/blob/ada55eb62568ba75be25cd12bd07b5fbdc37f88d/ROADMAP.md)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show filmcraft
bin/toolkit search "video-editing timeline" --repo filmcraft
bin/toolkit docs filmcraft "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [storytold/filmcraft at `ada55eb62568`](https://github.com/storytold/filmcraft/tree/ada55eb62568ba75be25cd12bd07b5fbdc37f88d). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo filmcraft --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
