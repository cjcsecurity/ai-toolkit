# strix

AI application-security assessment CLI and agent skills for source, web and API testing, remediation and CI workflows, with Docker sandboxes, model-provider configuration and separate managed-cloud integrations.

[Upstream repository](https://github.com/usestrix/strix) · [Pinned source](https://github.com/usestrix/strix/tree/007ed1a94e7dbf7b096c81e5b0354533ce94e0db) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Security and assessment |
| Operating model | application |
| Recommended scope | on-demand |
| Registered production skill paths | 9 |
| Reviewed source commit | `007ed1a94e7dbf7b096c81e5b0354533ce94e0db` |

## Purpose and use cases

Adds local and managed assessment workflows plus nine downstream agent skills. Select the relevant workflow without registering the full collection globally. CLI installation, model connectivity, Docker sandbox setup and managed-cloud accounts are distinct readiness requirements.

**Discovery tags:** `application security`, `API security`, `web security`, `code review`, `penetration testing`, `remediation`, `CI security scanning`, `Docker sandbox`, `security skills`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Local CLI needs running Docker with permission to create containers; first assessment downloads the sandbox image. Source/Python package strix-agent 1.6.2 requires Python >=3.12.
- Use a compatible packaged release/wheel where available. Source packaging includes a compiled Go TUI sidecar build hook and can require additional build tooling; consult scripts/tui_sidecar_hook.py before source installation.
- Set STRIX_LLM and provider credentials such as LLM_API_KEY, or configure a compatible local endpoint via LLM_API_BASE. Local providers must emit structured tool_calls, not text-form tool invocations.
- Target source/application access and user-authorized scope are required for assessment. Results are written under strix_runs; CI needs project secrets and Docker-enabled runners when using the local mode.
- Managed cloud skills need a separate Strix account/API or repository integration; reading skills locally needs no runtime, account or assessment launch.

## Setup guidance

**Setup scope:** shared isolated assessment CLI and Docker runtime; per-project model, target or managed-cloud integration

**Next action:** setup-required

**Working directory:** Use an isolated shared runtime or a working copy under runtime/strix; preserve the pinned source checkout. Target configuration belongs to the selected project.

**Installation approach:** Choose one documented install route from install_commands and pin its version. These are setup references, not a script to run in full. Reuse any subsequently installed runtime first.

**Configuration:** Choose local CLI or managed-cloud workflow. For local use, install a reviewed packaged release in an isolated environment, configure Docker and the selected provider/endpoint, and read the selected skill. Keep CI/workflow configuration in its target project.

**Verification to perform:** Check CLI help/version, Docker connectivity and structured model tool-call support. For an explicitly requested test assessment, verify final run status and findings rather than relying only on exit code.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read strix docs/quickstart.mdx
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
pipx install strix-agent
```

## Source entry points

- [README.md](https://github.com/usestrix/strix/blob/007ed1a94e7dbf7b096c81e5b0354533ce94e0db/README.md)
- [pyproject.toml](https://github.com/usestrix/strix/blob/007ed1a94e7dbf7b096c81e5b0354533ce94e0db/pyproject.toml)
- [docs/quickstart.mdx](https://github.com/usestrix/strix/blob/007ed1a94e7dbf7b096c81e5b0354533ce94e0db/docs/quickstart.mdx)
- [docs/usage/cli.mdx](https://github.com/usestrix/strix/blob/007ed1a94e7dbf7b096c81e5b0354533ce94e0db/docs/usage/cli.mdx)
- [docs/advanced/configuration.mdx](https://github.com/usestrix/strix/blob/007ed1a94e7dbf7b096c81e5b0354533ce94e0db/docs/advanced/configuration.mdx)
- [docs/llm-providers/local.mdx](https://github.com/usestrix/strix/blob/007ed1a94e7dbf7b096c81e5b0354533ce94e0db/docs/llm-providers/local.mdx)
- [docs/integrations/coding-agents.mdx](https://github.com/usestrix/strix/blob/007ed1a94e7dbf7b096c81e5b0354533ce94e0db/docs/integrations/coding-agents.mdx)
- [scripts/tui_sidecar_hook.py](https://github.com/usestrix/strix/blob/007ed1a94e7dbf7b096c81e5b0354533ce94e0db/scripts/tui_sidecar_hook.py)

## Skills and retrieval

The manifest registers **9 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/api-security-testing/SKILL.md](https://github.com/usestrix/strix/blob/007ed1a94e7dbf7b096c81e5b0354533ce94e0db/skills/api-security-testing/SKILL.md)
- [skills/application-security-testing/SKILL.md](https://github.com/usestrix/strix/blob/007ed1a94e7dbf7b096c81e5b0354533ce94e0db/skills/application-security-testing/SKILL.md)
- [skills/ci-security-scanning-with-strix/SKILL.md](https://github.com/usestrix/strix/blob/007ed1a94e7dbf7b096c81e5b0354533ce94e0db/skills/ci-security-scanning-with-strix/SKILL.md)
- [skills/find-security-vulnerabilities-in-code/SKILL.md](https://github.com/usestrix/strix/blob/007ed1a94e7dbf7b096c81e5b0354533ce94e0db/skills/find-security-vulnerabilities-in-code/SKILL.md)
- [skills/fix-security-vulnerabilities-with-strix/SKILL.md](https://github.com/usestrix/strix/blob/007ed1a94e7dbf7b096c81e5b0354533ce94e0db/skills/fix-security-vulnerabilities-with-strix/SKILL.md)
- [skills/managed-pentesting-with-strix/SKILL.md](https://github.com/usestrix/strix/blob/007ed1a94e7dbf7b096c81e5b0354533ce94e0db/skills/managed-pentesting-with-strix/SKILL.md)
- [skills/owasp-top-10-testing/SKILL.md](https://github.com/usestrix/strix/blob/007ed1a94e7dbf7b096c81e5b0354533ce94e0db/skills/owasp-top-10-testing/SKILL.md)
- [skills/penetration-testing-with-strix/SKILL.md](https://github.com/usestrix/strix/blob/007ed1a94e7dbf7b096c81e5b0354533ce94e0db/skills/penetration-testing-with-strix/SKILL.md)
- [skills/web-app-penetration-testing/SKILL.md](https://github.com/usestrix/strix/blob/007ed1a94e7dbf7b096c81e5b0354533ce94e0db/skills/web-app-penetration-testing/SKILL.md)

```bash
bin/toolkit show strix
bin/toolkit search "application security API security" --repo strix
bin/toolkit docs strix "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [usestrix/strix at `007ed1a94e7d`](https://github.com/usestrix/strix/tree/007ed1a94e7dbf7b096c81e5b0354533ce94e0db). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo strix --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
