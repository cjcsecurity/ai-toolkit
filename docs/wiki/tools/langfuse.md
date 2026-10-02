# langfuse

Self-hosted LLM observability, tracing, prompt management, evaluation datasets and experiments platform.

[Upstream repository](https://github.com/langfuse/langfuse) · [Pinned source](https://github.com/langfuse/langfuse/tree/9a29212e855c60ffb86d1989b62918b3781d9652) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | AI infrastructure and retrieval |
| Operating model | application |
| Recommended scope | project-local |
| Registered production skill paths | 0 |
| Reviewed source commit | `9a29212e855c60ffb86d1989b62918b3781d9652` |

## Purpose and use cases

Deploy once as a shared service or use Langfuse Cloud, then instrument each selected application with project-local SDKs and project credentials. Complements general observability with LLM traces and evaluation. This source repository contains deployment and API specifications; full user docs and SDK implementation live elsewhere. Maintainer engineering, operations and release skills are excluded.

**Discovery tags:** `llm observability`, `tracing`, `prompt management`, `evaluation`, `datasets`, `self-hosted`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- One-time self-hosted service: Docker/Compose or Kubernetes/Helm; PostgreSQL, ClickHouse, Redis, S3-compatible object storage (MinIO in bundled Compose), persistent storage and reviewed deployment secrets. No services started by library addition.
- Per application: Langfuse endpoint and project public/secret keys; Python or JS/TS SDK or direct API instrumentation. Cloud requires a Langfuse account.
- Source development only: Node.js 24 and pnpm 12.6.0 (package.json); not prerequisites for container deployment or SDK consumers.
- Model/provider access is needed when using LLM judges or playground features; tracing itself does not install a model.

## Setup guidance

**Setup scope:** shared service or cloud account; per-application instrumentation

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Prepare deployment configuration/secrets and backing services, or select Cloud. Add SDK instrumentation and project keys to each application that sends traces.

**Verification to perform:** Check service health and ingest/read a disposable trace before enabling application instrumentation.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read langfuse README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
docker compose -f repos/langfuse--langfuse/docker-compose.yml up
```

## Source entry points

- [README.md](https://github.com/langfuse/langfuse/blob/9a29212e855c60ffb86d1989b62918b3781d9652/README.md)
- [docker-compose.yml](https://github.com/langfuse/langfuse/blob/9a29212e855c60ffb86d1989b62918b3781d9652/docker-compose.yml)
- [.env.prod.example](https://github.com/langfuse/langfuse/blob/9a29212e855c60ffb86d1989b62918b3781d9652/.env.prod.example)
- [package.json](https://github.com/langfuse/langfuse/blob/9a29212e855c60ffb86d1989b62918b3781d9652/package.json)
- [fern/apis](https://github.com/langfuse/langfuse/tree/9a29212e855c60ffb86d1989b62918b3781d9652/fern/apis)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show langfuse
bin/toolkit search "llm observability tracing" --repo langfuse
bin/toolkit docs langfuse "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [langfuse/langfuse at `9a29212e855c`](https://github.com/langfuse/langfuse/tree/9a29212e855c60ffb86d1989b62918b3781d9652). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo langfuse --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
