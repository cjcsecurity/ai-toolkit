# agent-skills

Twenty-five engineering skills and lifecycle commands covering requirements, implementation, testing, review, UI, APIs, performance and shipping.

[Upstream repository](https://github.com/addyosmani/agent-skills) · [Pinned source](https://github.com/addyosmani/agent-skills/tree/2686b620fc1fed2e8f60c704839c766b8594c6b6) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Engineering and code intelligence |
| Operating model | skill-bundle |
| Recommended scope | on-demand |
| Registered production skill paths | 25 |
| Reviewed source commit | `2686b620fc1fed2e8f60c704839c766b8594c6b6` |

## Purpose and use cases

Register only api-and-interface-design and observability-and-instrumentation globally if desired; they add domain guidance. Planning/TDD/debugging/review/worktree-like process guidance overlaps existing Superpowers. Keep the full bundle available through a selector. Relative ../../references links require preserving the repository layout; standalone per-skill copying can break them.

**Discovery tags:** `engineering skills`, `api design`, `observability`, `performance`, `frontend`, `review`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Skill-capable client; Markdown itself needs no runtime
- Codex and OpenCode integrations documented
- Browser-testing skill requires Chrome DevTools MCP
- Preserve references/ for skills that link shared checklists; do not globally register using-agent-skills bootstrap alongside Superpowers

## Setup guidance

**Setup scope:** read selected skill; project-specific prerequisites

**Next action:** read-selected-reference

**Working directory:** Read from the stored checkout; install only selected task dependencies in an isolated environment or the target project.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Read selected skills and their relative references directly from this checkout; installing the whole collection is unnecessary. Register individual domain skills only when appropriate for the chosen host.

**Verification to perform:** Confirm the selected SKILL.md and its relative references resolve; check its task-specific prerequisites.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read agent-skills docs/codex-setup.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx skills add addyosmani/agent-skills --list
```

Example 2:

```bash
npx skills add addyosmani/agent-skills --skill api-and-interface-design
```

Example 3:

```bash
npx skills add addyosmani/agent-skills --skill observability-and-instrumentation
```

## Source entry points

- [README.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/README.md)
- [docs/codex-setup.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/docs/codex-setup.md)
- [docs/opencode-setup.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/docs/opencode-setup.md)
- [skills/api-and-interface-design/SKILL.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/skills/api-and-interface-design/SKILL.md)
- [skills/observability-and-instrumentation/SKILL.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/skills/observability-and-instrumentation/SKILL.md)
- [references/observability-checklist.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/references/observability-checklist.md)

## Skills and retrieval

The manifest registers **25 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/api-and-interface-design/SKILL.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/skills/api-and-interface-design/SKILL.md)
- [skills/browser-testing-with-devtools/SKILL.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/skills/browser-testing-with-devtools/SKILL.md)
- [skills/ci-cd-and-automation/SKILL.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/skills/ci-cd-and-automation/SKILL.md)
- [skills/code-review-and-quality/SKILL.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/skills/code-review-and-quality/SKILL.md)
- [skills/code-simplification/SKILL.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/skills/code-simplification/SKILL.md)
- [skills/constraint-driven-development/SKILL.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/skills/constraint-driven-development/SKILL.md)
- [skills/context-engineering/SKILL.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/skills/context-engineering/SKILL.md)
- [skills/debugging-and-error-recovery/SKILL.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/skills/debugging-and-error-recovery/SKILL.md)
- [skills/deprecation-and-migration/SKILL.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/skills/deprecation-and-migration/SKILL.md)
- [skills/documentation-and-adrs/SKILL.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/skills/documentation-and-adrs/SKILL.md)
- [skills/doubt-driven-development/SKILL.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/skills/doubt-driven-development/SKILL.md)
- [skills/frontend-ui-engineering/SKILL.md](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/skills/frontend-ui-engineering/SKILL.md)

Showing 12 of 25 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show agent-skills
bin/toolkit search "engineering skills api design" --repo agent-skills
bin/toolkit docs agent-skills "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [addyosmani/agent-skills at `2686b620fc1f`](https://github.com/addyosmani/agent-skills/tree/2686b620fc1fed2e8f60c704839c766b8594c6b6). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo agent-skills --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
