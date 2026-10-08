# vercel-skills

Vercel Skills CLI and find-skills guidance for discovering, inspecting and selectively installing skills from GitHub and well-known website indexes.

[Upstream repository](https://github.com/vercel-labs/skills) · [Pinned source](https://github.com/vercel-labs/skills/tree/87a266971d9460a3d2606075b8e91edc83325472) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Engineering and code intelligence |
| Operating model | cli |
| Recommended scope | on-demand |
| Registered production skill paths | 1 |
| Reviewed source commit | `87a266971d9460a3d2606075b8e91edc83325472` |

## Purpose and use cases

External discovery fallback after the reviewed toolkit. find-skills overlaps toolkit-selector and suggests global unpinned installation, so do not make it an always-on router. Only the public find-skills path is registered; internal factory workflows are excluded.

**Discovery tags:** `skill discovery`, `skills.sh`, `skill installation`, `agent skills`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Prompt guidance needs no runtime; CLI package requires Node.js >=22.20.0 and npm/npx.
- Network access is required for registry search and source downloads; upstream CLI supports telemetry opt-out via DISABLE_TELEMETRY or DO_NOT_TRACK.
- Inspect selected skill provenance and references before registration; popularity is not a security guarantee.

## Setup guidance

**Setup scope:** shared on-demand source; selected project or isolated runtime only

**Next action:** setup-required

**Working directory:** Read from the pinned checkout; apply only in the selected target project.

**Installation approach:** Source download and retrieval require no upstream runtime. For execution, reuse a compatible runtime or provision one isolated version following the pinned guide. Registration commands are alternatives, not an execution queue; do not install the entire collection globally.

**Configuration:** Search external skills only when reviewed local coverage is insufficient; preserve the selected project and agent scope. Pin downloaded source before adoption.

**Verification to perform:** Confirm selected skill and references exist; if using CLI, list candidates before selecting a skill.

**Local record:** Record actual runtime and authentication checks in local project notes; source availability is not runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read vercel-skills README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx skills@1.7.1 find react
```

Example 2:

```bash
npx skills@1.7.1 add vercel-labs/agent-skills --list
```

## Source entry points

- [README.md](https://github.com/vercel-labs/skills/blob/87a266971d9460a3d2606075b8e91edc83325472/README.md)
- [package.json](https://github.com/vercel-labs/skills/blob/87a266971d9460a3d2606075b8e91edc83325472/package.json)
- [skills/find-skills/SKILL.md](https://github.com/vercel-labs/skills/blob/87a266971d9460a3d2606075b8e91edc83325472/skills/find-skills/SKILL.md)

## Skills and retrieval

The manifest registers **1 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/find-skills/SKILL.md](https://github.com/vercel-labs/skills/blob/87a266971d9460a3d2606075b8e91edc83325472/skills/find-skills/SKILL.md)

```bash
bin/toolkit show vercel-skills
bin/toolkit search "skill discovery skills.sh" --repo vercel-skills
bin/toolkit docs vercel-skills "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [vercel-labs/skills at `87a266971d94`](https://github.com/vercel-labs/skills/tree/87a266971d9460a3d2606075b8e91edc83325472). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo vercel-skills --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
