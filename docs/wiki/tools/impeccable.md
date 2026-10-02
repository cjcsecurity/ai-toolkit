# impeccable

One frontend design router skill with 24 commands, detailed UX and visual design references, optional live browser workflows, and a deterministic design detector engine.

[Upstream repository](https://github.com/pbakaus/impeccable) · [Pinned source](https://github.com/pbakaus/impeccable/tree/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Design and interfaces |
| Operating model | skill-bundle |
| Recommended scope | global |
| Registered production skill paths | 20 |
| Reviewed source commit | `14dafe9c8c2186a9608c7e96edfe7ee69a1923ec` |

## Purpose and use cases

Recommended single global UI skill. Preserve upstream name impeccable and expose the entire provider-native directory: .agents/skills/impeccable for Codex and .opencode/skills/impeccable for OpenCode, including reference/, scripts/, agents/, and assets. Do not flatten SKILL.md, copy every provider duplicate, or install hooks implicitly. Files can be linked from the shared checkout; its launcher downloads a pinned engine on first invocation if absent.

**Discovery tags:** `frontend`, `ui`, `ux`, `design`, `accessibility`, `audit`, `polish`, `animation`, `codex`, `opencode`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Reading skill/reference files needs no runtime.
- Engine launcher uses a self-contained platform binary; if not bundled, first execution downloads it into ~/.impeccable/bin.
- Optional npm installer requires Node >=22.18.0; upstream installer may modify provider hooks unless disabled.
- Browser inspection/live iteration needs an available supported browser and project dev server.

## Setup guidance

**Setup scope:** existing global skill and engine; project browser integration

**Next action:** read-guidance

**Working directory:** Read pinned sources in place. Use a separate runtime working copy or the selected target project for installations and generated files.

**Installation approach:** Use the pinned upstream documentation and choose one suitable route from install_commands. Lists can include alternatives, registration and launch commands; do not execute the entire list. Check for an existing compatible runtime before installing.

**Configuration:** Choose the documented Codex or OpenCode distribution when native registration is desired, preserving references, scripts, agents and assets. On-demand source guidance requires no global installation; engine execution can need downloads.

**Verification to perform:** Load the global impeccable skill and use its documented engine check; verify browser access only for live UI work.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read impeccable README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx impeccable install
```

Example 2:

```bash
npx impeccable update
```

## Source entry points

- [README.md](https://github.com/pbakaus/impeccable/blob/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec/README.md)
- [.agents/skills/impeccable/SKILL.md](https://github.com/pbakaus/impeccable/blob/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec/.agents/skills/impeccable/SKILL.md)
- [.opencode/skills/impeccable/SKILL.md](https://github.com/pbakaus/impeccable/blob/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec/.opencode/skills/impeccable/SKILL.md)
- [.agents/skills/impeccable/reference/routing.md](https://github.com/pbakaus/impeccable/blob/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec/.agents/skills/impeccable/reference/routing.md)

## Skills and retrieval

The manifest registers **20 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [.agent/skills/impeccable/SKILL.md](https://github.com/pbakaus/impeccable/blob/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec/.agent/skills/impeccable/SKILL.md)
- [.agents/skills/impeccable/SKILL.md](https://github.com/pbakaus/impeccable/blob/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec/.agents/skills/impeccable/SKILL.md)
- [.claude/skills/impeccable/SKILL.md](https://github.com/pbakaus/impeccable/blob/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec/.claude/skills/impeccable/SKILL.md)
- [.cursor/skills/impeccable/SKILL.md](https://github.com/pbakaus/impeccable/blob/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec/.cursor/skills/impeccable/SKILL.md)
- [.dsh/skills/impeccable/SKILL.md](https://github.com/pbakaus/impeccable/blob/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec/.dsh/skills/impeccable/SKILL.md)
- [.gemini/skills/impeccable/SKILL.md](https://github.com/pbakaus/impeccable/blob/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec/.gemini/skills/impeccable/SKILL.md)
- [.github/skills/impeccable/SKILL.md](https://github.com/pbakaus/impeccable/blob/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec/.github/skills/impeccable/SKILL.md)
- [.grok/skills/impeccable/SKILL.md](https://github.com/pbakaus/impeccable/blob/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec/.grok/skills/impeccable/SKILL.md)
- [.hermes/skills/impeccable/SKILL.md](https://github.com/pbakaus/impeccable/blob/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec/.hermes/skills/impeccable/SKILL.md)
- [.kiro/skills/impeccable/SKILL.md](https://github.com/pbakaus/impeccable/blob/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec/.kiro/skills/impeccable/SKILL.md)
- [.opencode/skills/impeccable/SKILL.md](https://github.com/pbakaus/impeccable/blob/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec/.opencode/skills/impeccable/SKILL.md)
- [.pi/skills/impeccable/SKILL.md](https://github.com/pbakaus/impeccable/blob/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec/.pi/skills/impeccable/SKILL.md)

Showing 12 of 20 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show impeccable
bin/toolkit search "frontend ui" --repo impeccable
bin/toolkit docs impeccable "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [pbakaus/impeccable at `14dafe9c8c21`](https://github.com/pbakaus/impeccable/tree/14dafe9c8c2186a9608c7e96edfe7ee69a1923ec). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo impeccable --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
