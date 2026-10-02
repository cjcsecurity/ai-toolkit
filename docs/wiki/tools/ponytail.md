# ponytail

Coding simplification skills for reuse-first implementation, over-engineering review, repository audits and deferred-shortcut tracking, with optional multi-agent-host plugins, lifecycle hooks and an MCP instruction server.

[Upstream repository](https://github.com/DietrichGebert/ponytail) · [Pinned source](https://github.com/DietrichGebert/ponytail/tree/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Engineering and code intelligence |
| Operating model | skill-bundle |
| Recommended scope | on-demand |
| Registered production skill paths | 6 |
| Reviewed source commit | `e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156` |

## Purpose and use cases

Adds focused complexity-review and minimal-implementation guidance while leaving the established engineering workflow in control. Index the six canonical skills; generated OpenClaw copies duplicate them and benchmark arm skills are fixtures. Do not automatically install always-on hooks or replace global instructions.

**Discovery tags:** `code simplification`, `over-engineering`, `YAGNI`, `code review`, `standard library`, `native platform`, `technical debt`, `agent skills`, `agent hooks`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Instruction-only skill retrieval requires no package install or account. Host plugin/skill discovery differs; select the adapter for the actual coding agent.
- Claude Code/Codex plugins and Cursor lifecycle hooks require Node.js on the non-interactive PATH; missing Node leaves skills usable but automatic activation inactive.
- Plugins can inject persistent per-turn/subagent guidance and write host configuration/state. Configure their scope and intensity deliberately; retrieval does not install or trust lifecycle hooks.
- Optional ponytail-mcp is a separate Node.js stdio server with npm dependencies; its prompt/tool returns instructions on demand and does not provide portable automatic per-turn injection.
- No GPU, speech model or third-party account is required by Ponytail itself. Coding agent/provider credentials belong to the chosen host; Linux/WSL adapters still need host-specific verification.

## Setup guidance

**Setup scope:** on-demand canonical skills; optional explicitly selected host adapter or isolated MCP runtime

**Next action:** read-selected-reference

**Working directory:** Read canonical skills in the pinned checkout and apply them only in the selected target project. Any optional adapter/MCP working copy belongs under runtime/ponytail; preserve the pinned source.

**Installation approach:** No install is necessary for direct skill retrieval. The recorded Codex marketplace/add commands are an optional paired upstream route, not automatic registration. Review the actual host and chosen adapter before installing. Optional MCP setup is separately documented as cd ponytail-mcp followed by npm install in a runtime working copy.

**Configuration:** Choose the specific review/audit/debt or implementation skill for the task. If a persistent host plugin is explicitly selected, inspect its lifecycle hooks and mode configuration first; upstream Codex setup requires reviewing/trusting hooks through /hooks and starting a new thread. Retain the existing global engineering instructions.

**Verification to perform:** Confirm toolkit retrieval resolves a canonical skill. After any future adapter setup, verify the selected host discovers the skill and honors the selected mode, then verify deactivation. For optional MCP, test prompt/tool discovery and returned instructions; do not equate server connection with always-on mode.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read ponytail README.md
toolkit read ponytail skills/ponytail-review/SKILL.md
toolkit read ponytail docs/agent-portability.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
codex plugin marketplace add DietrichGebert/ponytail
```

Example 2:

```bash
codex plugin add ponytail@ponytail
```

## Source entry points

- [README.md](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/README.md)
- [package.json](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/package.json)
- [docs/agent-portability.md](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/docs/agent-portability.md)
- [docs/cursor-hooks.md](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/docs/cursor-hooks.md)
- [hooks/claude-codex-hooks.json](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/hooks/claude-codex-hooks.json)
- [skills/ponytail/SKILL.md](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/skills/ponytail/SKILL.md)
- [skills/ponytail-review/SKILL.md](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/skills/ponytail-review/SKILL.md)
- [ponytail-mcp/README.md](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/ponytail-mcp/README.md)

## Skills and retrieval

The manifest registers **6 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/ponytail/SKILL.md](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/skills/ponytail/SKILL.md)
- [skills/ponytail-review/SKILL.md](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/skills/ponytail-review/SKILL.md)
- [skills/ponytail-audit/SKILL.md](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/skills/ponytail-audit/SKILL.md)
- [skills/ponytail-debt/SKILL.md](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/skills/ponytail-debt/SKILL.md)
- [skills/ponytail-gain/SKILL.md](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/skills/ponytail-gain/SKILL.md)
- [skills/ponytail-help/SKILL.md](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/skills/ponytail-help/SKILL.md)

```bash
bin/toolkit show ponytail
bin/toolkit search "code simplification over-engineering" --repo ponytail
bin/toolkit docs ponytail "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [DietrichGebert/ponytail at `e3ba2aa6f1e6`](https://github.com/DietrichGebert/ponytail/tree/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo ponytail --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
