# ecc

Cross-agent engineering collection with 293 canonical skills for language and framework patterns, reviews, LLM pipelines, evaluation and agent memory; optional ECC CLI, hooks, rules and client adapters have a separate integration footprint.

[Upstream repository](https://github.com/affaan-m/ECC) · [Pinned source](https://github.com/affaan-m/ECC/tree/ef648e01899ba3e8dc6371642deaaf64b4477775) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Engineering and code intelligence |
| Operating model | skill-bundle |
| Recommended scope | on-demand |
| Registered production skill paths | 293 |
| Reviewed source commit | `ef648e01899ba3e8dc6371642deaaf64b4477775` |

## Purpose and use cases

Adds a broad supplemental skill library on demand alongside the host's chosen engineering workflow. Register the 293 canonical skills/ sources; 1,027 tracked SKILL.md files also include translations and client/Pi adaptations, which corpus discovery may retain as searchable variants. Do not bulk-install ECC hooks, rules, memory observers, MCP config or global client configuration merely to make the library searchable.

**Discovery tags:** `engineering skills`, `language patterns`, `LLM cost optimization`, `evaluation harness`, `agent memory`, `continuous learning`, `Codex`, `Claude Code`, `Cursor`, `OpenCode`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Reading selected Markdown skills requires no account or runtime; runtime and external-service requirements depend on the chosen skill.
- ecc-universal 2.2.3 requires Node.js >=18. Claude plugin setup also requires Git and Claude Code >=2.1 on PATH; Windows has PowerShell setup support.
- Native Codex plugin, Claude Code, and other client adapters have different supported capabilities. Codex native hooks need client-owned trust; adapters do not guarantee Claude hook/delegation parity.
- Full setup can write client skills, commands, hooks, rules, memory and MCP configuration. The deprecated Codex sync merges ~/.codex configuration. Keep this collection on demand and preserve existing Superpowers/global instructions.
- Service-backed skills, model providers, search services and managed ECC integrations may require separate credentials/accounts; local documentation availability does not establish those integrations.

## Setup guidance

**Setup scope:** on-demand supplemental skills; optional isolated ECC package and explicitly selected client integration

**Next action:** setup-required

**Working directory:** Use an isolated runtime or a working copy under runtime/ecc; preserve the pinned source checkout. Run project operations in the selected target project.

**Installation approach:** No install is needed for toolkit read. The reviewed README commands are optional setup references, not an execution queue: the first previews guided Codex installation, while setup configures the Claude plugin. If package tools are needed, use the exact reviewed release or a working copy of this pinned revision under runtime/ecc. Do not execute a global wizard as part of catalog setup.

**Configuration:** Select individual capabilities with toolkit skills/read. Preserve the host's chosen engineering workflow. For an explicitly requested ECC client integration, inspect destination and hook/MCP/rule changes and choose one documented install path per harness; do not stack native plugin with legacy sync or full manual copies.

**Verification to perform:** For source access confirm toolkit can read the selected canonical skill. Only after optional runtime setup run its documented doctor/help checks for the chosen target and inspect resulting client configuration for collisions; do not claim hooks or external services are ready from source availability.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read ecc README.md
toolkit read ecc docs/SKILL-PLACEMENT-POLICY.md
toolkit read ecc docs/CODEX-NAVIGATION-GUIDE.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx ecc-universal@2.2.3 install --guided --harness codex --dry-run
```

Example 2:

```bash
npx ecc-universal@2.2.3 setup
```

## Source entry points

- [README.md](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/README.md)
- [docs/SKILL-PLACEMENT-POLICY.md](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/docs/SKILL-PLACEMENT-POLICY.md)
- [docs/CODEX-NAVIGATION-GUIDE.md](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/docs/CODEX-NAVIGATION-GUIDE.md)
- [package.json](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/package.json)
- [.codex-plugin/README.md](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/.codex-plugin/README.md)
- [docs/SELECTIVE-INSTALL-ARCHITECTURE.md](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/docs/SELECTIVE-INSTALL-ARCHITECTURE.md)

## Skills and retrieval

The manifest registers **293 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/accessibility/SKILL.md](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/skills/accessibility/SKILL.md)
- [skills/agent-architecture-audit/SKILL.md](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/skills/agent-architecture-audit/SKILL.md)
- [skills/agent-eval/SKILL.md](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/skills/agent-eval/SKILL.md)
- [skills/agent-harness-construction/SKILL.md](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/skills/agent-harness-construction/SKILL.md)
- [skills/agent-introspection-debugging/SKILL.md](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/skills/agent-introspection-debugging/SKILL.md)
- [skills/agent-payment-x402/SKILL.md](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/skills/agent-payment-x402/SKILL.md)
- [skills/agent-self-evaluation/SKILL.md](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/skills/agent-self-evaluation/SKILL.md)
- [skills/agent-sort/SKILL.md](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/skills/agent-sort/SKILL.md)
- [skills/agentic-engineering/SKILL.md](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/skills/agentic-engineering/SKILL.md)
- [skills/agentic-os/SKILL.md](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/skills/agentic-os/SKILL.md)
- [skills/ai-first-engineering/SKILL.md](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/skills/ai-first-engineering/SKILL.md)
- [skills/ai-regression-testing/SKILL.md](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/skills/ai-regression-testing/SKILL.md)

Showing 12 of 293 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show ecc
bin/toolkit search "engineering skills language patterns" --repo ecc
bin/toolkit docs ecc "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [affaan-m/ECC at `ef648e01899b`](https://github.com/affaan-m/ECC/tree/ef648e01899ba3e8dc6371642deaaf64b4477775). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo ecc --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
