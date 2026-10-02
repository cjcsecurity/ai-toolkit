# litellm

Unified OpenAI-compatible Python SDK and self-hosted AI gateway for multiple LLM providers with routing, budgets, virtual keys, guardrails and spend tracking.

[Upstream repository](https://github.com/BerriAI/litellm) · [Pinned source](https://github.com/BerriAI/litellm/tree/d729f975aaf32d1af420940f92e1ccf9644db8dc) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | AI infrastructure and retrieval |
| Operating model | framework |
| Recommended scope | project-local |
| Registered production skill paths | 0 |
| Reviewed source commit | `d729f975aaf32d1af420940f92e1ccf9644db8dc` |

## Purpose and use cases

Install the SDK per application, or deploy a shared gateway once and configure per-project routes, virtual keys and provider credentials. Useful for model portability and centralized governance. Pinned checkout contains README, ARCHITECTURE, cookbook/examples and deployment metadata, but the full docs.litellm.ai site source is absent. Four LLM translation fixture skills and a Rust maintainer tracing skill are excluded.

**Discovery tags:** `llm gateway`, `multi-provider`, `openai compatibility`, `routing`, `budgets`, `guardrails`, `proxy`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Python >=3.10,<3.15 (pyproject.toml). Published wheels recommended; building the source native Rust bridge additionally requires the documented Rust/maturin toolchain.
- Per application: project-local litellm SDK, provider/local-model endpoint selection and necessary provider credentials. These are not provisioned by cloning.
- One-time gateway alternative: isolated litellm[proxy] tool or Docker deployment, gateway config and secrets. PostgreSQL supports persistent virtual keys/spend/admin features (included in Compose); advanced scale/caching may require Redis.
- Per-project gateway clients require base URL and virtual keys; provider billing and any commercial/enterprise features depend on chosen integrations.

## Setup guidance

**Setup scope:** shared gateway or project SDK

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Choose SDK installation in the application or a shared proxy deployment. Configure chosen model endpoints/providers, routes and keys; persistence features may need PostgreSQL.

**Verification to perform:** Run one small completion against the intended configured provider and verify routing; test fallback only if configured.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read litellm README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
uv add litellm
```

Example 2:

```bash
uv tool install 'litellm[proxy]'
```

Example 3:

```bash
litellm --config /absolute/project/config.yaml
```

## Source entry points

- [README.md](https://github.com/BerriAI/litellm/blob/d729f975aaf32d1af420940f92e1ccf9644db8dc/README.md)
- [ARCHITECTURE.md](https://github.com/BerriAI/litellm/blob/d729f975aaf32d1af420940f92e1ccf9644db8dc/ARCHITECTURE.md)
- [pyproject.toml](https://github.com/BerriAI/litellm/blob/d729f975aaf32d1af420940f92e1ccf9644db8dc/pyproject.toml)
- [docker-compose.yml](https://github.com/BerriAI/litellm/blob/d729f975aaf32d1af420940f92e1ccf9644db8dc/docker-compose.yml)
- [.env.example](https://github.com/BerriAI/litellm/blob/d729f975aaf32d1af420940f92e1ccf9644db8dc/.env.example)
- [proxy_server_config.yaml](https://github.com/BerriAI/litellm/blob/d729f975aaf32d1af420940f92e1ccf9644db8dc/proxy_server_config.yaml)
- [cookbook](https://github.com/BerriAI/litellm/tree/d729f975aaf32d1af420940f92e1ccf9644db8dc/cookbook)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show litellm
bin/toolkit search "llm gateway multi-provider" --repo litellm
bin/toolkit docs litellm "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [BerriAI/litellm at `d729f975aaf3`](https://github.com/BerriAI/litellm/tree/d729f975aaf32d1af420940f92e1ccf9644db8dc). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo litellm --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
