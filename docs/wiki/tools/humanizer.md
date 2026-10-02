# humanizer

Prose editing skill that removes common AI writing patterns, matches an author voice, and preserves facts, citations and non-prose file content.

[Upstream repository](https://github.com/blader/humanizer) · [Pinned source](https://github.com/blader/humanizer/tree/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Writing, video, and audio |
| Operating model | skill-bundle |
| Recommended scope | on-demand |
| Registered production skill paths | 1 |
| Reviewed source commit | `225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8` |

## Purpose and use cases

Adds an optional focused prose editing pass with 26 pattern checks, voice matching, and pasted-text, file and embedded output modes. Retrieve the skill when useful; no global registration or change to the Superpowers workflow is needed.

**Discovery tags:** `writing`, `editing`, `prose`, `voice matching`, `AI writing patterns`, `plain language`, `copy editing`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- A coding agent or assistant capable of reading Markdown; no runtime, package install, API key or account is required for the editing guidance.
- Provide the prose to edit and optionally a voice sample. File editing needs access to the selected document; preserve code, frontmatter, data and link targets.
- The optional Skills CLI installer uses Node/npm. The optional Claude Code plugin requires Claude Code 2.1.142 or newer; those are distribution alternatives, not prerequisites for on-demand reading.
- scripts/validate-package.py is repository packaging validation, not an editing runtime.

## Setup guidance

**Setup scope:** shared on-demand prose guidance; no runtime setup

**Next action:** read-guidance

**Working directory:** Read selected guidance from the pinned checkout; apply it in the user-selected target project or document workspace.

**Installation approach:** No runtime installation is required to read the skills. install_commands are verified upstream registration alternatives, not an execution queue. Do not register this collection globally; retrieve selected skills on demand.

**Configuration:** Read SKILL.md on demand and select pasted-text, file or embedded mode for the task. Use an author sample when supplied and preserve factual claims. The README explicitly permits omitting --global from its Codex installation command; no registration was performed.

**Verification to perform:** Verify the rewrite against the original facts, names, numbers, citations and intended voice. In file mode verify that code, metadata, data and link destinations remain intact.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read humanizer README.md
toolkit read humanizer SKILL.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx skills add blader/humanizer --agent codex
```

## Source entry points

- [README.md](https://github.com/blader/humanizer/blob/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8/README.md)
- [SKILL.md](https://github.com/blader/humanizer/blob/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8/SKILL.md)
- [agents/openai.yaml](https://github.com/blader/humanizer/blob/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8/agents/openai.yaml)
- [.claude-plugin/plugin.json](https://github.com/blader/humanizer/blob/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8/.claude-plugin/plugin.json)
- [.cursor-plugin/plugin.json](https://github.com/blader/humanizer/blob/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8/.cursor-plugin/plugin.json)

## Skills and retrieval

The manifest registers **1 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [SKILL.md](https://github.com/blader/humanizer/blob/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8/SKILL.md)

```bash
bin/toolkit show humanizer
bin/toolkit search "writing editing" --repo humanizer
bin/toolkit docs humanizer "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [blader/humanizer at `225a6f39ac85`](https://github.com/blader/humanizer/tree/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo humanizer --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
