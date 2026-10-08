# anthropic-skills

Anthropic frontend-design guidance for distinctive, accessible interfaces, visual hierarchy, restrained motion and clear product copy.

[Upstream repository](https://github.com/anthropics/skills) · [Pinned source](https://github.com/anthropics/skills/tree/683bc88e56f3e09ba94f7055977f3d3aa499f202) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Design and interfaces |
| Operating model | skill-bundle |
| Recommended scope | on-demand |
| Registered production skill paths | 1 |
| Reviewed source commit | `683bc88e56f3e09ba94f7055977f3d3aa499f202` |

## Purpose and use cases

Register only the requested frontend-design skill. Existing Impeccable already covers global frontend design and accessibility; use this as an optional reference rather than a second automatic design workflow. Other repository skills are not promoted by this entry, though source auto-discovery may retrieve them.

**Discovery tags:** `frontend design`, `interface design`, `accessibility`, `typography`, `UX writing`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Frontend-design is Markdown guidance with no required runtime; testing/rendering depends on the selected frontend project.
- Repository mixes licenses: frontend-design has an Apache-2.0 LICENSE.txt in its own directory; document skills have separate source-available terms. Review individual licenses before adopting other skills.

## Setup guidance

**Setup scope:** shared on-demand source; selected project or isolated runtime only

**Next action:** read-guidance

**Working directory:** Read from the pinned checkout; apply only in the selected target project.

**Installation approach:** Source download and retrieval require no upstream runtime. Registration commands are alternatives, not an execution queue; do not install the entire collection globally.

**Configuration:** Preserve the project design system and user brief; read only the selected skill. Do not activate unrelated document-generation or provider-specific workflows.

**Verification to perform:** Confirm frontend-design and license exist; validate resulting UI with the target project tools when actually used.

**Local record:** Record actual runtime and authentication checks in local project notes; source availability is not runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read anthropic-skills README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx skills add anthropics/skills --skill frontend-design
```

## Source entry points

- [README.md](https://github.com/anthropics/skills/blob/683bc88e56f3e09ba94f7055977f3d3aa499f202/README.md)
- [skills/frontend-design/LICENSE.txt](https://github.com/anthropics/skills/blob/683bc88e56f3e09ba94f7055977f3d3aa499f202/skills/frontend-design/LICENSE.txt)
- [skills/frontend-design/SKILL.md](https://github.com/anthropics/skills/blob/683bc88e56f3e09ba94f7055977f3d3aa499f202/skills/frontend-design/SKILL.md)

## Skills and retrieval

The manifest registers **1 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/frontend-design/SKILL.md](https://github.com/anthropics/skills/blob/683bc88e56f3e09ba94f7055977f3d3aa499f202/skills/frontend-design/SKILL.md)

```bash
bin/toolkit show anthropic-skills
bin/toolkit search "frontend design interface design" --repo anthropic-skills
bin/toolkit docs anthropic-skills "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [anthropics/skills at `683bc88e56f3`](https://github.com/anthropics/skills/tree/683bc88e56f3e09ba94f7055977f3d3aa499f202). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo anthropic-skills --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
