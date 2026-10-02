# matt-pocock-skills

Engineering and productivity skills for domain glossaries, architecture decisions, requirements interviews, specifications, ticket planning, TDD, debugging, reviews, teaching and writing agent instructions.

[Upstream repository](https://github.com/mattpocock/skills) · [Pinned source](https://github.com/mattpocock/skills/tree/d81f3a183412e71a5b1e84ca21bc1a35eea03a60) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Engineering and code intelligence |
| Operating model | skill-bundle |
| Recommended scope | on-demand |
| Registered production skill paths | 31 |
| Reviewed source commit | `d81f3a183412e71a5b1e84ca21bc1a35eea03a60` |

## Purpose and use cases

Adds focused engineering and communication references while Superpowers remains the primary global workflow. The 27 packaged engineering/productivity skills and four misc skills are listed; six explicitly in-progress beta skills are omitted from skill_paths, but corpus auto-discovery may still make their source searchable. Misc skills are not promoted in the upstream plugin; check category and invocation policy before use.

**Discovery tags:** `engineering skills`, `domain modeling`, `glossary`, `architecture decisions`, `requirements`, `ticket planning`, `test driven development`, `debugging`, `code review`, `writing for agents`, `teaching`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Reading prompt skills needs no runtime or account; retain sibling references and agents/openai.yaml invocation policies when reading selected skills.
- Engineering workflows may depend on per-project docs/agents issue-tracker, triage-label and domain configuration. Read setup-matt-pocock-skills before adopting those workflows; configuration belongs in the selected project, not this library.
- GitHub workflows reference authenticated gh; GitLab workflows reference glab; local Markdown issue tracking is supported. Other trackers, tests, browser tools and project dependencies depend on the selected skill.
- Some review, research and implementation skills use delegated agents; misc setup skills reference Husky, lint-staged, Prettier or @total-typescript/shoehorn. These are task-specific requirements, not installed by storing this repository.
- package.json is private release-maintenance tooling (Changesets/npm), not a runtime prerequisite for using skill text. skills/in-progress is explicitly beta and excluded from the upstream plugin.

## Setup guidance

**Setup scope:** shared on-demand skill source; optional per-project workflow configuration and task-specific tools

**Next action:** read-guidance

**Working directory:** Read selected guidance from the pinned checkout; apply it in the user-selected target project or document workspace.

**Installation approach:** No runtime installation is required to read the skills. install_commands are verified upstream registration alternatives, not an execution queue. Do not register this collection globally; retrieve selected skills on demand.

**Configuration:** Preserve the host's chosen engineering workflow. Select individual references; respect explicitly user-invoked skill policies. For an adopted engineering workflow read its setup dependencies and configure the chosen project issue tracker, triage labels and glossary/ADR layout. The upstream installer can register many skills; inspect its scope before using it.

**Verification to perform:** Check selected skill and sibling references exist; check target project configuration and only the external tools needed by that task. Distinguish stable engineering/productivity, unpromoted misc, and in-progress beta sources.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read matt-pocock-skills README.md
toolkit read matt-pocock-skills skills/engineering/setup-matt-pocock-skills/SKILL.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx skills@latest add mattpocock/skills
```

## Source entry points

- [README.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/README.md)
- [.claude-plugin/plugin.json](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/.claude-plugin/plugin.json)
- [package.json](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/package.json)
- [skills/engineering/README.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/README.md)
- [skills/productivity/README.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/productivity/README.md)
- [skills/misc/README.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/misc/README.md)
- [skills/in-progress/README.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/in-progress/README.md)
- [skills/engineering/setup-matt-pocock-skills/SKILL.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/setup-matt-pocock-skills/SKILL.md)
- [skills/engineering/domain-modeling/SKILL.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/domain-modeling/SKILL.md)
- [skills/productivity/writing-for-agents/SKILL.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/productivity/writing-for-agents/SKILL.md)

## Skills and retrieval

The manifest registers **31 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/engineering/ask-matt/SKILL.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/ask-matt/SKILL.md)
- [skills/engineering/code-review/SKILL.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/code-review/SKILL.md)
- [skills/engineering/codebase-design/SKILL.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/codebase-design/SKILL.md)
- [skills/engineering/diagnosing-bugs/SKILL.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/diagnosing-bugs/SKILL.md)
- [skills/engineering/domain-modeling/SKILL.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/domain-modeling/SKILL.md)
- [skills/engineering/grill-with-docs/SKILL.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/grill-with-docs/SKILL.md)
- [skills/engineering/implement-spec/SKILL.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/implement-spec/SKILL.md)
- [skills/engineering/implement/SKILL.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/implement/SKILL.md)
- [skills/engineering/improve-codebase-architecture/SKILL.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/improve-codebase-architecture/SKILL.md)
- [skills/engineering/pr/SKILL.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/pr/SKILL.md)
- [skills/engineering/prototype/SKILL.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/prototype/SKILL.md)
- [skills/engineering/research/SKILL.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/research/SKILL.md)

Showing 12 of 31 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show matt-pocock-skills
bin/toolkit search "engineering skills domain modeling" --repo matt-pocock-skills
bin/toolkit docs matt-pocock-skills "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [mattpocock/skills at `d81f3a183412`](https://github.com/mattpocock/skills/tree/d81f3a183412e71a5b1e84ca21bc1a35eea03a60). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo matt-pocock-skills --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
