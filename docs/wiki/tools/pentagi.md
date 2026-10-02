# pentagi

Containerized autonomous penetration-testing application with agent workflows, security tools, browser/search integrations, persistent memory, reports, and a web UI.

[Upstream repository](https://github.com/vxcontrol/pentagi) · [Pinned source](https://github.com/vxcontrol/pentagi/tree/01acdda6d3b81a5a4164533dbd8fcf43b5ae2457) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Security and assessment |
| Operating model | application |
| Recommended scope | on-demand |
| Registered production skill paths | 0 |
| Reviewed source commit | `01acdda6d3b81a5a4164533dbd8fcf43b5ae2457` |

## Purpose and use cases

Full multi-service security application with Docker execution access; keep inactive until a scoped assessment calls for it.

**Discovery tags:** `security`, `pentest`, `autonomous-agent`, `docker`, `vulnerability`, `research`, `web-ui`, `knowledge-graph`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Docker and Docker Compose or supported Podman configuration; documented minimum 2 vCPU, 4 GB RAM, and 20 GB free disk.
- Docker API access for worker/container management and network access for images.
- At least one LLM provider configured using an API key, Bedrock credentials, or local Ollama/custom endpoint; embeddings need compatible configuration.
- Local web UI account login; optional search-service keys, OAuth, and Graphiti/Neo4j setup.
- Explicitly authorized assessment targets and scope.

## Setup guidance

**Setup scope:** isolated shared container stack; per-assessment configuration

**Next action:** setup-required

**Working directory:** Isolated deployment/build working copy under runtime/pentagi; preserve the pinned source checkout.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Prepare Compose environment, model provider, embeddings and worker-container access in a deployment working copy. Configure assessment targets separately.

**Verification to perform:** Verify container health and UI login without starting an assessment.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read pentagi examples/guides/installation_configuration.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
docker compose up -d
```

## Source entry points

- [README.md](https://github.com/vxcontrol/pentagi/blob/01acdda6d3b81a5a4164533dbd8fcf43b5ae2457/README.md)
- [examples/guides/installation_configuration.md](https://github.com/vxcontrol/pentagi/blob/01acdda6d3b81a5a4164533dbd8fcf43b5ae2457/examples/guides/installation_configuration.md)
- [EULA.md](https://github.com/vxcontrol/pentagi/blob/01acdda6d3b81a5a4164533dbd8fcf43b5ae2457/EULA.md)
- [docker-compose.yml](https://github.com/vxcontrol/pentagi/blob/01acdda6d3b81a5a4164533dbd8fcf43b5ae2457/docker-compose.yml)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show pentagi
bin/toolkit search "security pentest" --repo pentagi
bin/toolkit docs pentagi "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [vxcontrol/pentagi at `01acdda6d3b8`](https://github.com/vxcontrol/pentagi/tree/01acdda6d3b81a5a4164533dbd8fcf43b5ae2457). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo pentagi --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
