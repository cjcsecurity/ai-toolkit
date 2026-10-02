# autocli

Rust CLI offering declarative website adapters, authenticated browser-session reuse, public API retrieval and external CLI passthrough.

[Upstream repository](https://github.com/nashsu/AutoCLI) · [Pinned source](https://github.com/nashsu/AutoCLI/tree/c0969e2c83b29a7528452b1ba555085deca8e00d) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Browsers, research, and web data |
| Operating model | cli |
| Recommended scope | on-demand |
| Registered production skill paths | 0 |
| Reviewed source commit | `c0969e2c83b29a7528452b1ba555085deca8e00d` |

## Purpose and use cases

Overlaps OpenCLI closely: originally its Rust rewrite. Pick one browser-adapter stack when a specific supported website task requires it. Public commands can work without browser integration; do not globally register a large command inventory.

**Discovery tags:** `web automation`, `rust`, `browser bridge`, `website cli`, `scraping`, `adapters`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Native release available for Linux x64/arm64, macOS x64/arm64, Windows x64; Rust/Cargo for source build
- Browser-backed commands require Chrome, unpacked AutoCLI extension, local daemon and appropriate logged-in session
- Optional AI adapter generation/cloud sharing uses AutoCLI.ai authentication
- Media downloads may need yt-dlp; agent skill lives in separate nashsu/autocli-skill repository

## Setup guidance

**Setup scope:** shared native CLI and browser bridge; per-site adapters

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Choose a compatible release or build in an isolated working copy. Browser mode also needs its extension/daemon and the selected user-controlled session.

**Verification to perform:** Run the documented autocli doctor, then a read-only command for the chosen adapter.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read autocli README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
cargo build --release
```

Example 2:

```bash
npx skills add https://github.com/nashsu/autocli-skill
```

Example 3:

```bash
autocli doctor
```

## Source entry points

- [README.md](https://github.com/nashsu/AutoCLI/blob/c0969e2c83b29a7528452b1ba555085deca8e00d/README.md)
- [Cargo.toml](https://github.com/nashsu/AutoCLI/blob/c0969e2c83b29a7528452b1ba555085deca8e00d/Cargo.toml)
- [extension](https://github.com/nashsu/AutoCLI/tree/c0969e2c83b29a7528452b1ba555085deca8e00d/extension)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show autocli
bin/toolkit search "web automation rust" --repo autocli
bin/toolkit docs autocli "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [nashsu/AutoCLI at `c0969e2c83b2`](https://github.com/nashsu/AutoCLI/tree/c0969e2c83b29a7528452b1ba555085deca8e00d). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo autocli --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
