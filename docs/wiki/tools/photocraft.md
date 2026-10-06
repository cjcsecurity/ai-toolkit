# photocraft

Rust image editor with layered PSD workflows, masks, adjustments and automation through a headless CLI, MCP server and authenticated desktop control channel.

[Upstream repository](https://github.com/storytold/photocraft) · [Pinned source](https://github.com/storytold/photocraft/tree/a96a621deea97d4b1ecd173b8b921587e33f3ca5) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Design and interfaces |
| Operating model | desktop application + cli + mcp |
| Recommended scope | on-demand |
| Registered production skill paths | 0 |
| Reviewed source commit | `a96a621deea97d4b1ecd173b8b921587e33f3ca5` |

## Purpose and use cases

Create and edit layered images interactively or through the same command engine from agents. Upstream labels this early alpha; validate document round trips before relying on it.

**Discovery tags:** `image-editing`, `psd`, `layers`, `raster`, `design`, `mcp`, `rust`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Use a platform release or build with Rust 1.90+ and Cargo. Desktop source builds support macOS, Windows and Linux; releases also include FreeBSD and web variants.
- Linux source builds require libxkbcommon, Wayland, X11/Xrandr/Xi, Mesa GL and GTK 3 development packages; desktop rendering needs a supported graphics backend.
- Headless CLI/MCP and desktop control are separate launch modes. Desktop control uses a private bearer token and explicit automation read/write roots.
- MIT OR Apache-2.0 code; ArtCraft brand assets and third-party assets have separate terms.

## Setup guidance

**Setup scope:** project-local or isolated tool runtime; explicit agent registration

**Next action:** setup-required

**Working directory:** An isolated tool checkout or the selected target project, according to the pinned setup guide.

**Installation approach:** Reuse a compatible runtime first. Select one documented installation route, review dependencies and pin the version; commands are examples, not a script to execute in order.

**Configuration:** Choose a platform release or isolated source build. For automation, select headless MCP or authenticated desktop control with explicit working-directory capabilities.

**Verification to perform:** Open a disposable layered sample, export an image and reopen its PSD; check CLI/MCP command discovery before automating real assets.

**Local record:** Record the actual runtime version, checks and remaining requirements locally. Catalog/source presence does not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read photocraft README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
cargo run --release -p photocraft -- image.psd
```

## Source entry points

- [README.md](https://github.com/storytold/photocraft/blob/a96a621deea97d4b1ecd173b8b921587e33f3ca5/README.md)
- [Cargo.toml](https://github.com/storytold/photocraft/blob/a96a621deea97d4b1ecd173b8b921587e33f3ca5/Cargo.toml)
- [docs/development.md](https://github.com/storytold/photocraft/blob/a96a621deea97d4b1ecd173b8b921587e33f3ca5/docs/development.md)
- [docs/control-protocol.md](https://github.com/storytold/photocraft/blob/a96a621deea97d4b1ecd173b8b921587e33f3ca5/docs/control-protocol.md)
- [docs/contributing.md](https://github.com/storytold/photocraft/blob/a96a621deea97d4b1ecd173b8b921587e33f3ca5/docs/contributing.md)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show photocraft
bin/toolkit search "image-editing psd" --repo photocraft
bin/toolkit docs photocraft "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [storytold/photocraft at `a96a621deea9`](https://github.com/storytold/photocraft/tree/a96a621deea97d4b1ecd173b8b921587e33f3ca5). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo photocraft --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
