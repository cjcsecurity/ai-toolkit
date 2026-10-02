# financial-services

Claude financial-services plugin marketplace containing financial modeling, banking, equity research, private-equity, fund-admin, operations, and advisor workflows plus data connectors.

[Upstream repository](https://github.com/anthropics/financial-services) · [Pinned source](https://github.com/anthropics/financial-services/tree/574ed3624aebd0418c7e96cd101262f30210ab26) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Finance and markets |
| Operating model | skill-bundle |
| Recommended scope | on-demand |
| Registered production skill paths | 112 |
| Reviewed source commit | `574ed3624aebd0418c7e96cd101262f30210ab26` |

## Purpose and use cases

Read selected source skills in plugins/vertical-plugins rather than bundled agent copies. Individual Markdown methods can inform Codex/OpenCode, but Claude marketplace manifests, commands, managed-agent deployment, and tool names are not native drop-in integrations; adapt only requested workflows.

**Discovery tags:** `finance`, `dcf`, `valuation`, `equity research`, `investment banking`, `financial modeling`, `mcp`, `claude plugins`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Reading Markdown methods requires no build/runtime.
- Live financial-data connectors may require commercial provider subscriptions, API keys, or OAuth.
- Official plugin runtime is Claude Code/Cowork; Managed Agents deployment requires an Anthropic API key.
- Some workflows require spreadsheet/document capabilities and private financial documents supplied by the user.

## Setup guidance

**Setup scope:** read selected methods; task-specific connectors

**Next action:** read-selected-reference

**Working directory:** Read from the stored checkout; install only selected task dependencies in an isolated environment or the target project.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** The listed claude plugin commands are for Claude, not Codex/OpenCode. These clients can read selected skills locally; configure only needed compatible data/document connectors.

**Verification to perform:** Verify selected references and any required spreadsheet/data connector using non-production sample input.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read financial-services README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
claude plugin marketplace add anthropics/financial-services
```

Example 2:

```bash
claude plugin install financial-analysis@claude-for-financial-services
```

## Source entry points

- [README.md](https://github.com/anthropics/financial-services/blob/574ed3624aebd0418c7e96cd101262f30210ab26/README.md)
- [plugins/vertical-plugins/financial-analysis/.mcp.json](https://github.com/anthropics/financial-services/blob/574ed3624aebd0418c7e96cd101262f30210ab26/plugins/vertical-plugins/financial-analysis/.mcp.json)

## Skills and retrieval

The manifest registers **112 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [claude-for-msft-365-install/.claude/skills/verify/SKILL.md](https://github.com/anthropics/financial-services/blob/574ed3624aebd0418c7e96cd101262f30210ab26/claude-for-msft-365-install/.claude/skills/verify/SKILL.md)
- [plugins/agent-plugins/earnings-reviewer/skills/audit-xls/SKILL.md](https://github.com/anthropics/financial-services/blob/574ed3624aebd0418c7e96cd101262f30210ab26/plugins/agent-plugins/earnings-reviewer/skills/audit-xls/SKILL.md)
- [plugins/agent-plugins/earnings-reviewer/skills/earnings-analysis/SKILL.md](https://github.com/anthropics/financial-services/blob/574ed3624aebd0418c7e96cd101262f30210ab26/plugins/agent-plugins/earnings-reviewer/skills/earnings-analysis/SKILL.md)
- [plugins/agent-plugins/earnings-reviewer/skills/earnings-preview/SKILL.md](https://github.com/anthropics/financial-services/blob/574ed3624aebd0418c7e96cd101262f30210ab26/plugins/agent-plugins/earnings-reviewer/skills/earnings-preview/SKILL.md)
- [plugins/agent-plugins/earnings-reviewer/skills/model-update/SKILL.md](https://github.com/anthropics/financial-services/blob/574ed3624aebd0418c7e96cd101262f30210ab26/plugins/agent-plugins/earnings-reviewer/skills/model-update/SKILL.md)
- [plugins/agent-plugins/earnings-reviewer/skills/morning-note/SKILL.md](https://github.com/anthropics/financial-services/blob/574ed3624aebd0418c7e96cd101262f30210ab26/plugins/agent-plugins/earnings-reviewer/skills/morning-note/SKILL.md)
- [plugins/agent-plugins/earnings-reviewer/skills/xlsx-author/SKILL.md](https://github.com/anthropics/financial-services/blob/574ed3624aebd0418c7e96cd101262f30210ab26/plugins/agent-plugins/earnings-reviewer/skills/xlsx-author/SKILL.md)
- [plugins/agent-plugins/gl-reconciler/skills/audit-xls/SKILL.md](https://github.com/anthropics/financial-services/blob/574ed3624aebd0418c7e96cd101262f30210ab26/plugins/agent-plugins/gl-reconciler/skills/audit-xls/SKILL.md)
- [plugins/agent-plugins/gl-reconciler/skills/break-trace/SKILL.md](https://github.com/anthropics/financial-services/blob/574ed3624aebd0418c7e96cd101262f30210ab26/plugins/agent-plugins/gl-reconciler/skills/break-trace/SKILL.md)
- [plugins/agent-plugins/gl-reconciler/skills/gl-recon/SKILL.md](https://github.com/anthropics/financial-services/blob/574ed3624aebd0418c7e96cd101262f30210ab26/plugins/agent-plugins/gl-reconciler/skills/gl-recon/SKILL.md)
- [plugins/agent-plugins/gl-reconciler/skills/xlsx-author/SKILL.md](https://github.com/anthropics/financial-services/blob/574ed3624aebd0418c7e96cd101262f30210ab26/plugins/agent-plugins/gl-reconciler/skills/xlsx-author/SKILL.md)
- [plugins/agent-plugins/kyc-screener/skills/kyc-doc-parse/SKILL.md](https://github.com/anthropics/financial-services/blob/574ed3624aebd0418c7e96cd101262f30210ab26/plugins/agent-plugins/kyc-screener/skills/kyc-doc-parse/SKILL.md)

Showing 12 of 112 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show financial-services
bin/toolkit search "finance dcf" --repo financial-services
bin/toolkit docs financial-services "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [anthropics/financial-services at `574ed3624aeb`](https://github.com/anthropics/financial-services/tree/574ed3624aebd0418c7e96cd101262f30210ab26). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo financial-services --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
