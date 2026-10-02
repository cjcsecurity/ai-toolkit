# shannon

Autonomous security-testing application that analyzes source-available web applications/APIs and attempts exploit validation in containerized worker sessions.

[Upstream repository](https://github.com/KeygraphHQ/shannon) · [Pinned source](https://github.com/KeygraphHQ/shannon/tree/a14c7944d87b30ed7bfecd4bad06562e24002b01) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Security and assessment |
| Operating model | application |
| Recommended scope | on-demand |
| Registered production skill paths | 0 |
| Reviewed source commit | `a14c7944d87b30ed7bfecd4bad06562e24002b01` |

## Purpose and use cases

Keep as an explicitly selected security workflow; starting it performs active exploitation and provisions local infrastructure.

**Discovery tags:** `security`, `pentest`, `web-security`, `api-security`, `source-analysis`, `vulnerability`, `exploit-validation`, `docker`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Docker and Node.js >=18 for the documented npx workflow.
- AI provider credentials or supported subscription authentication; provider-specific cybersecurity workload requirements may apply.
- Target source repository and reachable application endpoint.
- Explicitly authorized non-production testing environment and target scope; optional target login/TOTP/email configuration.

## Setup guidance

**Setup scope:** isolated assessment runtime; model and target configuration

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Use the documented setup to provision Docker/runtime in a working copy. Configure the selected provider and the explicitly authorized test app/source separately.

**Verification to perform:** Verify setup diagnostics and container readiness before running an authorized non-production test.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read shannon README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx @keygraph/shannon@latest setup
```

## Source entry points

- [README.md](https://github.com/KeygraphHQ/shannon/blob/a14c7944d87b30ed7bfecd4bad06562e24002b01/README.md)
- [docs/ai-providers.md](https://github.com/KeygraphHQ/shannon/blob/a14c7944d87b30ed7bfecd4bad06562e24002b01/docs/ai-providers.md)
- [docs/configuration.md](https://github.com/KeygraphHQ/shannon/blob/a14c7944d87b30ed7bfecd4bad06562e24002b01/docs/configuration.md)
- [docs/safety.md](https://github.com/KeygraphHQ/shannon/blob/a14c7944d87b30ed7bfecd4bad06562e24002b01/docs/safety.md)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show shannon
bin/toolkit search "security pentest" --repo shannon
bin/toolkit docs shannon "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [KeygraphHQ/shannon at `a14c7944d87b`](https://github.com/KeygraphHQ/shannon/tree/a14c7944d87b30ed7bfecd4bad06562e24002b01). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo shannon --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
