# loop-engineering

Patterns, templates, skills and a Node CLI for recurring repository triage, PR maintenance and verification loops.

[Upstream repository](https://github.com/cobusgreyling/loop-engineering) · [Pinned source](https://github.com/cobusgreyling/loop-engineering/tree/62801dea82905bc6afb5448d24e5386e9792ad06) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Engineering and code intelligence |
| Operating model | reference |
| Recommended scope | reference |
| Registered production skill paths | 40 |
| Reviewed source commit | `62801dea82905bc6afb5448d24e5386e9792ad06` |

## Purpose and use cases

Useful pattern library for explicitly requested recurring work; lifecycle, verification, worktree and planning material overlaps Superpowers. Per-project init writes operating state and instructions; avoid global loop activation.

**Discovery tags:** `agent loops`, `triage`, `pull requests`, `automation`, `cost`, `codex`, `opencode`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Markdown needs no runtime
- Unified loop CLI requires Node.js >=18 and npm/npx
- GitHub-oriented patterns require repository permissions and appropriate scheduler/agent credentials
- Codex and OpenCode examples included; Node CLI is cross-platform, shell examples may need POSIX tools

## Setup guidance

**Setup scope:** read patterns; optional target-repository CLI setup

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Read the chosen loop pattern. Run init only inside the intended project; use the tool flag matching the client and inspect generated workflow/config files.

**Verification to perform:** Run the documented loop doctor on the target project before scheduling a loop.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read loop-engineering docs/QUICKSTART.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx @cobusgreyling/loop init . --pattern daily-triage --tool codex
```

Example 2:

```bash
npx @cobusgreyling/loop doctor .
```

Example 3:

```bash
npx @cobusgreyling/loop cost --pattern daily-triage --level L1
```

## Source entry points

- [README.md](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/README.md)
- [docs/QUICKSTART.md](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/docs/QUICKSTART.md)
- [docs/operating-loops.md](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/docs/operating-loops.md)
- [examples/codex](https://github.com/cobusgreyling/loop-engineering/tree/62801dea82905bc6afb5448d24e5386e9792ad06/examples/codex)
- [examples/opencode](https://github.com/cobusgreyling/loop-engineering/tree/62801dea82905bc6afb5448d24e5386e9792ad06/examples/opencode)
- [tools/loop/package.json](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/tools/loop/package.json)

## Skills and retrieval

The manifest registers **40 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/budget-negotiator/SKILL.md](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/skills/budget-negotiator/SKILL.md)
- [skills/install-loop/SKILL.md](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/skills/install-loop/SKILL.md)
- [skills/loop-budget/SKILL.md](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/skills/loop-budget/SKILL.md)
- [skills/loop-constraints/SKILL.md](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/skills/loop-constraints/SKILL.md)
- [skills/loop-triage/SKILL.md](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/skills/loop-triage/SKILL.md)
- [skills/loop-verifier/SKILL.md](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/skills/loop-verifier/SKILL.md)
- [skills/minimal-fix/SKILL.md](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/skills/minimal-fix/SKILL.md)
- [starters/changelog-drafter-opencode/skills/changelog-scan/SKILL.md](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/starters/changelog-drafter-opencode/skills/changelog-scan/SKILL.md)
- [starters/changelog-drafter/.claude/skills/changelog-scan/SKILL.md](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/starters/changelog-drafter/.claude/skills/changelog-scan/SKILL.md)
- [starters/changelog-drafter/.claude/skills/draft-release-notes/SKILL.md](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/starters/changelog-drafter/.claude/skills/draft-release-notes/SKILL.md)
- [starters/changelog-drafter/.codex/skills/changelog-scan/SKILL.md](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/starters/changelog-drafter/.codex/skills/changelog-scan/SKILL.md)
- [starters/changelog-drafter/.codex/skills/draft-release-notes/SKILL.md](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/starters/changelog-drafter/.codex/skills/draft-release-notes/SKILL.md)

Showing 12 of 40 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show loop-engineering
bin/toolkit search "agent loops triage" --repo loop-engineering
bin/toolkit docs loop-engineering "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [cobusgreyling/loop-engineering at `62801dea8290`](https://github.com/cobusgreyling/loop-engineering/tree/62801dea82905bc6afb5448d24e5386e9792ad06). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo loop-engineering --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
