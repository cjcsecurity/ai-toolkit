# promptfoo

CLI/library for LLM prompt and agent evaluations, model comparisons, assertions, CI gates, authorized red teaming and optional MCP evaluation tools; includes four production setup/run skills.

[Upstream repository](https://github.com/promptfoo/promptfoo) · [Pinned source](https://github.com/promptfoo/promptfoo/tree/94119b67648756bf475a950885b2799c1694f1c2) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | AI infrastructure and retrieval |
| Operating model | cli |
| Recommended scope | on-demand |
| Registered production skill paths | 4 |
| Reviewed source commit | `94119b67648756bf475a950885b2799c1694f1c2` |

## Purpose and use cases

Build reusable evaluations and inspect failures before tuning prompts or selecting models. Keep red-team actions scoped to the authorized app. Index the four shipped plugin skills; exclude internal repository development skills and example/fixture skills. Preserve the plugin skills tree because provider and redteam setup share a bundled YAML parser.

**Discovery tags:** `llm evaluation`, `evals`, `model comparison`, `assertions`, `red teaming`, `prompt injection`, `ci`, `mcp`, `skills`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Reviewed version 0.123.1 requires Node.js >=22.22.0; upstream recommends Node.js 24 LTS.
- Most hosted target/grader providers require their API credentials; local Ollama, custom JavaScript/Python providers and deterministic assertions are alternatives. Python provider scripts need a suitable Python environment.
- Hosted model/HTTP target calls send configured prompt/test data to those providers. Redteam generation/grading may call remote helpers; --no-share disables result sharing but not those calls.
- Optional MCP needs @modelcontextprotocol/sdk, which slim installs omitting optional dependencies may lack. No globally running MCP is required for CLI evals.
- Native dependencies can require compatible packaged binaries or build tooling when a binary is unavailable; use the package manager's supported install path.

## Setup guidance

**Setup scope:** optional shared core CLI; project eval config/provider extras

**Next action:** setup-required

**Working directory:** Read pinned sources in place. Use a separate runtime working copy or the selected target project for installations and generated files.

**Installation approach:** Use the pinned upstream documentation and choose one suitable route from install_commands. Lists can include alternatives, registration and launch commands; do not execute the entire list. Check for an existing compatible runtime before installing.

**Configuration:** Install a reviewed Promptfoo release, create project eval YAML, and configure only selected local or hosted model providers. Optional integrations may require additional dependencies.

**Verification to perform:** Run a small eval with deterministic assertions; inspect successes, failures and errors, not just process exit status.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read promptfoo site/docs/installation.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npm install -g promptfoo@0.123.1
```

Example 2:

```bash
npx promptfoo@0.123.1 --help
```

## Source entry points

- [README.md](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/README.md)
- [package.json](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/package.json)
- [site/docs/installation.md](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/site/docs/installation.md)
- [site/docs/getting-started.md](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/site/docs/getting-started.md)
- [site/docs/configuration/reference.md](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/site/docs/configuration/reference.md)
- [site/docs/configuration/expected-outputs/index.md](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/site/docs/configuration/expected-outputs/index.md)
- [site/docs/providers/ollama.md](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/site/docs/providers/ollama.md)
- [site/docs/red-team/index.md](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/site/docs/red-team/index.md)
- [site/docs/integrations/mcp-server.md](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/site/docs/integrations/mcp-server.md)
- [site/docs/configuration/telemetry.md](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/site/docs/configuration/telemetry.md)
- [plugins/promptfoo/skills/promptfoo-evals/references/eval-patterns.md](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/plugins/promptfoo/skills/promptfoo-evals/references/eval-patterns.md)
- [plugins/promptfoo/skills/promptfoo-provider-setup/references/provider-patterns.md](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/plugins/promptfoo/skills/promptfoo-provider-setup/references/provider-patterns.md)
- [plugins/promptfoo/skills/promptfoo-redteam-setup/references/redteam-setup-patterns.md](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/plugins/promptfoo/skills/promptfoo-redteam-setup/references/redteam-setup-patterns.md)
- [plugins/promptfoo/skills/promptfoo-redteam-run/references/redteam-run-patterns.md](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/plugins/promptfoo/skills/promptfoo-redteam-run/references/redteam-run-patterns.md)

## Skills and retrieval

The manifest registers **4 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [plugins/promptfoo/skills/promptfoo-provider-setup/SKILL.md](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/plugins/promptfoo/skills/promptfoo-provider-setup/SKILL.md)
- [plugins/promptfoo/skills/promptfoo-evals/SKILL.md](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/plugins/promptfoo/skills/promptfoo-evals/SKILL.md)
- [plugins/promptfoo/skills/promptfoo-redteam-setup/SKILL.md](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/plugins/promptfoo/skills/promptfoo-redteam-setup/SKILL.md)
- [plugins/promptfoo/skills/promptfoo-redteam-run/SKILL.md](https://github.com/promptfoo/promptfoo/blob/94119b67648756bf475a950885b2799c1694f1c2/plugins/promptfoo/skills/promptfoo-redteam-run/SKILL.md)

```bash
bin/toolkit show promptfoo
bin/toolkit search "llm evaluation evals" --repo promptfoo
bin/toolkit docs promptfoo "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [promptfoo/promptfoo at `94119b676487`](https://github.com/promptfoo/promptfoo/tree/94119b67648756bf475a950885b2799c1694f1c2). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo promptfoo --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
