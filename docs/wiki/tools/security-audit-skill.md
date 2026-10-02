# security-audit-skill

Source-first security audit guidance with trust-boundary analysis, coverage-led hunting, independent finding verification, structured verdicts and machine-readable audit reports.

[Upstream repository](https://github.com/cloudflare/security-audit-skill) · [Pinned source](https://github.com/cloudflare/security-audit-skill/tree/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Security and assessment |
| Operating model | skill-bundle |
| Recommended scope | on-demand |
| Registered production skill paths | 1 |
| Reviewed source commit | `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8` |

## Purpose and use cases

Adds a focused Cloudflare audit workflow and domain-specific review references. Guidance is immediately readable; full audits require a compatible agent, Node validators and enforced local execution isolation. Store on demand without launching an assessment or changing the global Superpowers workflow.

**Discovery tags:** `security audit`, `source code security`, `trust boundaries`, `coverage ledger`, `vulnerability validation`, `independent verification`, `security report`, `Node validators`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Reading guidance needs no runtime or account. Full audit orchestration needs a tool-capable model and parallel sub-agents, an explicitly selected source target, output directory and reviewed source revision.
- Node.js is required for the bundled zero-dependency validate-findings.cjs and validate-coverage-ledger.cjs validators. No npm package installation is required for those scripts; execution has not been tested or configured during library review.
- Target-controlled builds, tests and processes require an OS-enforced sandbox with external networking disabled, an allowlisted empty environment, read-only source/toolchain, assigned scratch writes and resource limits. Sandbox readiness is not established by cloning the skill.
- Full audits use fresh independent verifiers, parent-owned shared reports and per-agent scratch/artifact directories. Companion references cover web/auth, client, AI/LLM, supply chain, cloud, protocols, availability, data isolation, native apps and memory safety.
- The skill distinguishes guidance from full audit mode. A full run requires both JSON validators and final report artifacts or an explicit incomplete status; missing execution controls are recorded as needs_validation rather than executing target code.

## Setup guidance

**Setup scope:** shared on-demand audit guidance; per-assessment agent, Node.js and sandbox capability checks

**Next action:** read-guidance

**Working directory:** Read selected guidance from the pinned checkout; apply it in the user-selected target project or document workspace.

**Installation approach:** No runtime installation is required to read the skills. install_commands are verified upstream registration alternatives, not an execution queue. Do not register this collection globally; retrieve selected skills on demand.

**Configuration:** Use guidance mode for focused questions. Before an explicitly requested full audit, resolve target, source ref, scope/profile/budget and output directory, select relevant companion files, verify delegation and OS-enforced sandbox capabilities, and keep the source checkout clean. No audit or target code has run.

**Verification to perform:** For an actual full audit verify Node availability, sandbox controls and independent-agent support, then validate produced artifacts with node <skill-dir>/validate-findings.cjs <output-dir>/findings.json and node <skill-dir>/validate-coverage-ledger.cjs <output-dir>/coverage-ledger.json as documented in VALIDATION-AND-REPORTING.md. Guidance availability alone does not verify full audit execution readiness.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read security-audit-skill README.md
toolkit read security-audit-skill skills/security-audit/SKILL.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit
```

## Source entry points

- [README.md](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/README.md)
- [skills/security-audit/SKILL.md](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/SKILL.md)
- [skills/security-audit/RECONNAISSANCE.md](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/RECONNAISSANCE.md)
- [skills/security-audit/HUNTING.md](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/HUNTING.md)
- [skills/security-audit/VALIDATION-AND-REPORTING.md](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/VALIDATION-AND-REPORTING.md)
- [skills/security-audit/report-schema.json](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/report-schema.json)
- [skills/security-audit/validate-findings.cjs](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-findings.cjs)
- [skills/security-audit/validate-coverage-ledger.cjs](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-coverage-ledger.cjs)

## Skills and retrieval

The manifest registers **1 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/security-audit/SKILL.md](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/SKILL.md)

```bash
bin/toolkit show security-audit-skill
bin/toolkit search "security audit source code security" --repo security-audit-skill
bin/toolkit docs security-audit-skill "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [cloudflare/security-audit-skill at `c1c8a8c14710`](https://github.com/cloudflare/security-audit-skill/tree/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo security-audit-skill --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
