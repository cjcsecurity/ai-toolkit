# taste-skill

Portable frontend design and redesign guidance, including experimental v2 taste, minimalist, brutalist, image-to-code, and image-generation reference workflows.

[Upstream repository](https://github.com/Leonxlnx/taste-skill) · [Pinned source](https://github.com/Leonxlnx/taste-skill/tree/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Design and interfaces |
| Operating model | skill-bundle |
| Recommended scope | on-demand |
| Registered production skill paths | 13 |
| Reviewed source commit | `ce26fc25c0e5e8cab638f883de62d9a86ee5e45b` |

## Purpose and use cases

Select one appropriate skill by its frontmatter name; registering all overlapping visual styles makes routing noisy. Markdown guidance is portable to Codex/OpenCode. Default v2 name is design-taste-frontend, not taste-skill.

**Discovery tags:** `frontend`, `ui`, `design`, `typography`, `layout`, `redesign`, `image references`, `codex`, `opencode`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- No runtime needed to read implementation guidance; target project dependencies apply when building.
- Image-generation variants require an available image generator; stitch variant requires its own service/tool setup.

## Setup guidance

**Setup scope:** read selected skill; project-specific implementation tools

**Next action:** read-selected-reference

**Working directory:** Read from the stored checkout; install only selected task dependencies in an isolated environment or the target project.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Read only the selected skill and relative references. No collection-wide install is needed; image-generation/Stitch variants require their separately available tools.

**Verification to perform:** Confirm the selected skill references and chosen implementation/image tool are available.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read taste-skill README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
```

## Source entry points

- [README.md](https://github.com/Leonxlnx/taste-skill/blob/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/README.md)
- [skills/taste-skill/SKILL.md](https://github.com/Leonxlnx/taste-skill/blob/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/skills/taste-skill/SKILL.md)
- [skills/gpt-tasteskill/SKILL.md](https://github.com/Leonxlnx/taste-skill/blob/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/skills/gpt-tasteskill/SKILL.md)
- [skills/redesign-skill/SKILL.md](https://github.com/Leonxlnx/taste-skill/blob/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/skills/redesign-skill/SKILL.md)

## Skills and retrieval

The manifest registers **13 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/brandkit/SKILL.md](https://github.com/Leonxlnx/taste-skill/blob/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/skills/brandkit/SKILL.md)
- [skills/brutalist-skill/SKILL.md](https://github.com/Leonxlnx/taste-skill/blob/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/skills/brutalist-skill/SKILL.md)
- [skills/gpt-tasteskill/SKILL.md](https://github.com/Leonxlnx/taste-skill/blob/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/skills/gpt-tasteskill/SKILL.md)
- [skills/image-to-code-skill/SKILL.md](https://github.com/Leonxlnx/taste-skill/blob/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/skills/image-to-code-skill/SKILL.md)
- [skills/imagegen-frontend-mobile/SKILL.md](https://github.com/Leonxlnx/taste-skill/blob/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/skills/imagegen-frontend-mobile/SKILL.md)
- [skills/imagegen-frontend-web/SKILL.md](https://github.com/Leonxlnx/taste-skill/blob/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/skills/imagegen-frontend-web/SKILL.md)
- [skills/minimalist-skill/SKILL.md](https://github.com/Leonxlnx/taste-skill/blob/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/skills/minimalist-skill/SKILL.md)
- [skills/output-skill/SKILL.md](https://github.com/Leonxlnx/taste-skill/blob/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/skills/output-skill/SKILL.md)
- [skills/redesign-skill/SKILL.md](https://github.com/Leonxlnx/taste-skill/blob/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/skills/redesign-skill/SKILL.md)
- [skills/soft-skill/SKILL.md](https://github.com/Leonxlnx/taste-skill/blob/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/skills/soft-skill/SKILL.md)
- [skills/stitch-skill/SKILL.md](https://github.com/Leonxlnx/taste-skill/blob/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/skills/stitch-skill/SKILL.md)
- [skills/taste-skill-v1/SKILL.md](https://github.com/Leonxlnx/taste-skill/blob/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b/skills/taste-skill-v1/SKILL.md)

Showing 12 of 13 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show taste-skill
bin/toolkit search "frontend ui" --repo taste-skill
bin/toolkit docs taste-skill "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [Leonxlnx/taste-skill at `ce26fc25c0e5`](https://github.com/Leonxlnx/taste-skill/tree/ce26fc25c0e5e8cab638f883de62d9a86ee5e45b). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo taste-skill --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
