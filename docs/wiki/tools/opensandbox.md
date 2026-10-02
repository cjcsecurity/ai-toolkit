# opensandbox

Self-hosted isolated execution environments for AI agents, code, files, browsers and desktops with Docker/Kubernetes runtimes, SDKs, CLI and MCP.

[Upstream repository](https://github.com/opensandbox-group/OpenSandbox) · [Pinned source](https://github.com/opensandbox-group/OpenSandbox/tree/c7dc78a4090e5de2b9119e9bd93952cae24f87bd) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | AI infrastructure and retrieval |
| Operating model | framework |
| Recommended scope | project-local |
| Registered production skill paths | 1 |
| Reviewed source commit | `c7dc78a4090e5de2b9119e9bd93952cae24f87bd` |

## Purpose and use cases

Provision a shared sandbox server once and use per-project SDKs, images, resource policies and server credentials. Adds execution infrastructure rather than an engineering workflow. Local docs/ is available for corpus retrieval. Only skills/troubleshoot-sandbox is downstream product guidance; internal release-note skill excluded. That skill uses older opensandbox CLI examples while current README documents osb, so verify CLI help or use its documented HTTP diagnostics endpoints.

**Discovery tags:** `sandbox`, `code execution`, `agent isolation`, `docker`, `kubernetes`, `browser automation`, `sdk`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- One-time server setup: Python >=3.10, uv/pip and Docker for local sandbox execution, or a configured Kubernetes runtime/cluster. Pullable sandbox/execd runtime images and server configuration required.
- Per project: SDK (Python, TypeScript, Java/Kotlin, C# or Go), reachable server endpoint, API key if configured, sandbox images and lifecycle/resource/network policy.
- CLI installation is separate (opensandbox-cli); MCP also needs separately configured service/client transport. Firecracker/fast runtime has additional host and Kubernetes requirements documented in docs/architecture/fast-sandbox/.

## Setup guidance

**Setup scope:** shared sandbox server; per-project SDK/images/policies

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Choose Docker or Kubernetes, configure server endpoint/access and runtime images, then install only the CLI/MCP/SDK needed by the client or application.

**Verification to perform:** Create a disposable sandbox, execute a harmless command, read the result and destroy it.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read opensandbox README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
uv tool install opensandbox-server
```

Example 2:

```bash
uvx opensandbox-server init-config ~/.sandbox.toml --example docker
```

Example 3:

```bash
uvx opensandbox-server
```

Example 4:

```bash
uv tool install opensandbox-cli
```

Example 5:

```bash
uv add opensandbox
```

Example 6:

```bash
npm install @alibaba-group/opensandbox
```

## Source entry points

- [README.md](https://github.com/opensandbox-group/OpenSandbox/blob/c7dc78a4090e5de2b9119e9bd93952cae24f87bd/README.md)
- [server/README.md](https://github.com/opensandbox-group/OpenSandbox/blob/c7dc78a4090e5de2b9119e9bd93952cae24f87bd/server/README.md)
- [server/pyproject.toml](https://github.com/opensandbox-group/OpenSandbox/blob/c7dc78a4090e5de2b9119e9bd93952cae24f87bd/server/pyproject.toml)
- [cli/README.md](https://github.com/opensandbox-group/OpenSandbox/blob/c7dc78a4090e5de2b9119e9bd93952cae24f87bd/cli/README.md)
- [docs/guides/secure-access.md](https://github.com/opensandbox-group/OpenSandbox/blob/c7dc78a4090e5de2b9119e9bd93952cae24f87bd/docs/guides/secure-access.md)
- [docs/architecture/fast-sandbox/index.md](https://github.com/opensandbox-group/OpenSandbox/blob/c7dc78a4090e5de2b9119e9bd93952cae24f87bd/docs/architecture/fast-sandbox/index.md)
- [skills/troubleshoot-sandbox/SKILL.md](https://github.com/opensandbox-group/OpenSandbox/blob/c7dc78a4090e5de2b9119e9bd93952cae24f87bd/skills/troubleshoot-sandbox/SKILL.md)

## Skills and retrieval

The manifest registers **1 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/troubleshoot-sandbox/SKILL.md](https://github.com/opensandbox-group/OpenSandbox/blob/c7dc78a4090e5de2b9119e9bd93952cae24f87bd/skills/troubleshoot-sandbox/SKILL.md)

```bash
bin/toolkit show opensandbox
bin/toolkit search "sandbox code execution" --repo opensandbox
bin/toolkit docs opensandbox "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [opensandbox-group/OpenSandbox at `c7dc78a4090e`](https://github.com/opensandbox-group/OpenSandbox/tree/c7dc78a4090e5de2b9119e9bd93952cae24f87bd). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo opensandbox --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
