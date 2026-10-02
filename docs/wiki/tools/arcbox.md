# arcbox

Rust container and virtual-machine runtime for macOS with Docker compatibility, Kubernetes, Linux/macOS guests and disposable agent sandboxes.

[Upstream repository](https://github.com/arcboxlabs/arcbox) · [Pinned source](https://github.com/arcboxlabs/arcbox/tree/a5b82f0e2ab9de287fd62d06d18c973891c11c78) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | AI infrastructure and retrieval |
| Operating model | application |
| Recommended scope | reference |
| Registered production skill paths | 0 |
| Reviewed source commit | `a5b82f0e2ab9de287fd62d06d18c973891c11c78` |

## Purpose and use cases

The documented desktop runtime targets Apple hardware/macOS. Keep as reference on Linux; check platform support before selecting the runtime. Fleet Linux support is a separate developing component.

**Discovery tags:** `macos`, `containers`, `docker`, `virtual machines`, `sandbox`, `rust`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- macOS host for documented runtime; Rust 1.96+ when building source
- Apple Silicon M3 or newer and macOS 15+ required for nested Firecracker agent sandboxes
- macOS guests require Apple Silicon, VZ backend and APFS
- Daemon and VM images; Docker/kubectl context changes happen via explicit enable commands

## Setup guidance

**Setup scope:** supported macOS host only; unavailable on this Linux/WSL host

**Next action:** check-platform

**Working directory:** Use a supported macOS host for the documented runtime; Linux and WSL hosts can retrieve documentation without installing the macOS runtime.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Check the current host against upstream platform requirements. Use the documented macOS setup on supported Apple hardware; other hosts can read the reference without provisioning the desktop runtime.

**Verification to perform:** On the supported host, verify daemon/VM health and one disposable container. Use OpenSandbox for a Linux-oriented alternative.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read arcbox README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
brew install --cask arcboxlabs/tap/arcbox
```

Example 2:

```bash
abctl daemon start
```

Example 3:

```bash
abctl docker enable
```

## Source entry points

- [README.md](https://github.com/arcboxlabs/arcbox/blob/a5b82f0e2ab9de287fd62d06d18c973891c11c78/README.md)
- [Cargo.toml](https://github.com/arcboxlabs/arcbox/blob/a5b82f0e2ab9de287fd62d06d18c973891c11c78/Cargo.toml)
- [docs/agent-sandbox.md](https://github.com/arcboxlabs/arcbox/blob/a5b82f0e2ab9de287fd62d06d18c973891c11c78/docs/agent-sandbox.md)
- [docs/sandbox-api.md](https://github.com/arcboxlabs/arcbox/blob/a5b82f0e2ab9de287fd62d06d18c973891c11c78/docs/sandbox-api.md)
- [docs/macos-guest.md](https://github.com/arcboxlabs/arcbox/blob/a5b82f0e2ab9de287fd62d06d18c973891c11c78/docs/macos-guest.md)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show arcbox
bin/toolkit search "macos containers" --repo arcbox
bin/toolkit docs arcbox "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [arcboxlabs/arcbox at `a5b82f0e2ab9`](https://github.com/arcboxlabs/arcbox/tree/a5b82f0e2ab9de287fd62d06d18c973891c11c78). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo arcbox --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
