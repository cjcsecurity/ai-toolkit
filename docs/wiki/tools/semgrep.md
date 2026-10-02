# semgrep

Local multi-language static analysis with code-like rules, bug/security searches, custom YAML rules and CI scanning; optional bundled MCP server integrates findings with coding agents.

[Upstream repository](https://github.com/semgrep/semgrep) · [Pinned source](https://github.com/semgrep/semgrep/tree/31729a1719c6e76ac8d41ec8fb9ab191621ee10f) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Security and assessment |
| Operating model | cli |
| Recommended scope | on-demand |
| Registered production skill paths | 0 |
| Reviewed source commit | `31729a1719c6e76ac8d41ec8fb9ab191621ee10f` |

## Purpose and use cases

Use Community Edition for local pattern/rule scanning and scoped code review. This repository ships no SKILL.md files; Guardian plugin skills are a separate distribution. Advanced cross-file analysis, Supply Chain and Secrets capabilities require platform/Pro access rather than the source checkout alone.

**Discovery tags:** `security`, `sast`, `static analysis`, `code scanning`, `rules`, `taint analysis`, `ci`, `mcp`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Installed CLI 1.179.0 uses isolated Python 3.13.15 and its bundled engine; reviewed source declares 1.178.0 and Python >=3.10. Source and runtime versions are recorded separately.
- Local Community Edition scans with local rules do not require account authentication. Registry rules need network access; AppSec Platform, Pro engine/rules and semgrep ci platform workflows require login or SEMGREP_APP_TOKEN and appropriate entitlements.
- Optional semgrep mcp is bundled with the CLI and needs a compatible MCP client; it can run on demand via stdio. Guardian hooks/plugin integration must be configured separately.
- Community Edition analysis is primarily bounded to a function/file and does not provide all advanced platform analysis. Building full source is substantially heavier than installing a packaged engine.

## Setup guidance

**Setup scope:** optional shared Community Edition CLI; project rules

**Next action:** setup-required

**Working directory:** Read pinned sources in place. Use a separate runtime working copy or the selected target project for installations and generated files.

**Installation approach:** Use the pinned upstream documentation and choose one suitable route from install_commands. Lists can include alternatives, registration and launch commands; do not execute the entire list. Check for an existing compatible runtime before installing.

**Configuration:** Install a compatible reviewed Semgrep Community Edition release in an isolated environment. Use local rules for a small offline smoke check before adding remote rules or authenticated platform features.

**Verification to perform:** semgrep --version; run a local rule on a seeded sample and confirm the expected finding without remote rules.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read semgrep README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
uv tool install semgrep==1.178.0
```

Example 2:

```bash
pipx install semgrep==1.178.0
```

Example 3:

```bash
python3 -m pip install semgrep==1.178.0
```

## Source entry points

- [README.md](https://github.com/semgrep/semgrep/blob/31729a1719c6e76ac8d41ec8fb9ab191621ee10f/README.md)
- [cli/pyproject.toml](https://github.com/semgrep/semgrep/blob/31729a1719c6e76ac8d41ec8fb9ab191621ee10f/cli/pyproject.toml)
- [cli/src/semgrep/mcp/README.md](https://github.com/semgrep/semgrep/blob/31729a1719c6e76ac8d41ec8fb9ab191621ee10f/cli/src/semgrep/mcp/README.md)
- [CONTRIBUTING.md](https://github.com/semgrep/semgrep/blob/31729a1719c6e76ac8d41ec8fb9ab191621ee10f/CONTRIBUTING.md)
- [CHANGELOG.md](https://github.com/semgrep/semgrep/blob/31729a1719c6e76ac8d41ec8fb9ab191621ee10f/CHANGELOG.md)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show semgrep
bin/toolkit search "security sast" --repo semgrep
bin/toolkit docs semgrep "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [semgrep/semgrep at `31729a1719c6`](https://github.com/semgrep/semgrep/tree/31729a1719c6e76ac8d41ec8fb9ab191621ee10f). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo semgrep --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
