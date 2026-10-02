# hyperframes

HTML/CSS/media video framework with seekable animations, deterministic MP4 rendering, a preview CLI, reusable blocks, and task-specific agent skills.

[Upstream repository](https://github.com/heygen-com/hyperframes) · [Pinned source](https://github.com/heygen-com/hyperframes/tree/78e849235aa96af479004ee14c2e0f8ec10ccb9d) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Writing, video, and audio |
| Operating model | cli |
| Recommended scope | on-demand |
| Registered production skill paths | 40 |
| Reviewed source commit | `78e849235aa96af479004ee14c2e0f8ec10ccb9d` |

## Purpose and use cases

Read skills/hyperframes/SKILL.md as a router, then load a specific workflow and its referenced domain guidance from this checkout. Supports Codex/OpenCode. Avoid blanket skill installs: upstream core router can install workflows on demand, and catalog includes internal duplicates and block-specific skills.

**Discovery tags:** `video`, `animation`, `motion graphics`, `html`, `mp4`, `ffmpeg`, `codex`, `opencode`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Node.js 22+ and FFmpeg for local rendering.
- Renderer browser/runtime dependencies must be installed before rendering.
- External media generation, avatar, speech, or stock services may require credentials; plain local HTML rendering does not inherently need a paid model API.

## Setup guidance

**Setup scope:** project video composition; reusable CLI and renderer dependencies

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Initialize only the target video project; configure Node, FFmpeg and browser rendering. External generation providers are optional and distinct from local rendering.

**Verification to perform:** Preview and render a short local composition; verify the output video.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read hyperframes README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx hyperframes skills update
```

Example 2:

```bash
npx hyperframes init my-video
```

Example 3:

```bash
npx hyperframes preview
```

Example 4:

```bash
npx hyperframes render
```

## Source entry points

- [README.md](https://github.com/heygen-com/hyperframes/blob/78e849235aa96af479004ee14c2e0f8ec10ccb9d/README.md)
- [skills/hyperframes/SKILL.md](https://github.com/heygen-com/hyperframes/blob/78e849235aa96af479004ee14c2e0f8ec10ccb9d/skills/hyperframes/SKILL.md)
- [skills/hyperframes-cli/SKILL.md](https://github.com/heygen-com/hyperframes/blob/78e849235aa96af479004ee14c2e0f8ec10ccb9d/skills/hyperframes-cli/SKILL.md)
- [docs/guides/plugins.mdx](https://github.com/heygen-com/hyperframes/blob/78e849235aa96af479004ee14c2e0f8ec10ccb9d/docs/guides/plugins.mdx)

## Skills and retrieval

The manifest registers **40 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [.agents/skills/captions-overlay/SKILL.md](https://github.com/heygen-com/hyperframes/blob/78e849235aa96af479004ee14c2e0f8ec10ccb9d/.agents/skills/captions-overlay/SKILL.md)
- [.agents/skills/changelog-video/SKILL.md](https://github.com/heygen-com/hyperframes/blob/78e849235aa96af479004ee14c2e0f8ec10ccb9d/.agents/skills/changelog-video/SKILL.md)
- [.agents/skills/cut-the-curve/SKILL.md](https://github.com/heygen-com/hyperframes/blob/78e849235aa96af479004ee14c2e0f8ec10ccb9d/.agents/skills/cut-the-curve/SKILL.md)
- [.agents/skills/motion-doctrine/SKILL.md](https://github.com/heygen-com/hyperframes/blob/78e849235aa96af479004ee14c2e0f8ec10ccb9d/.agents/skills/motion-doctrine/SKILL.md)
- [.agents/skills/oversized-cursor/SKILL.md](https://github.com/heygen-com/hyperframes/blob/78e849235aa96af479004ee14c2e0f8ec10ccb9d/.agents/skills/oversized-cursor/SKILL.md)
- [.agents/skills/seam-craft/SKILL.md](https://github.com/heygen-com/hyperframes/blob/78e849235aa96af479004ee14c2e0f8ec10ccb9d/.agents/skills/seam-craft/SKILL.md)
- [.claude/skills/captions-overlay/SKILL.md](https://github.com/heygen-com/hyperframes/blob/78e849235aa96af479004ee14c2e0f8ec10ccb9d/.claude/skills/captions-overlay/SKILL.md)
- [.claude/skills/changelog-video/SKILL.md](https://github.com/heygen-com/hyperframes/blob/78e849235aa96af479004ee14c2e0f8ec10ccb9d/.claude/skills/changelog-video/SKILL.md)
- [.claude/skills/cut-the-curve/SKILL.md](https://github.com/heygen-com/hyperframes/blob/78e849235aa96af479004ee14c2e0f8ec10ccb9d/.claude/skills/cut-the-curve/SKILL.md)
- [.claude/skills/motion-doctrine/SKILL.md](https://github.com/heygen-com/hyperframes/blob/78e849235aa96af479004ee14c2e0f8ec10ccb9d/.claude/skills/motion-doctrine/SKILL.md)
- [.claude/skills/oversized-cursor/SKILL.md](https://github.com/heygen-com/hyperframes/blob/78e849235aa96af479004ee14c2e0f8ec10ccb9d/.claude/skills/oversized-cursor/SKILL.md)
- [.claude/skills/seam-craft/SKILL.md](https://github.com/heygen-com/hyperframes/blob/78e849235aa96af479004ee14c2e0f8ec10ccb9d/.claude/skills/seam-craft/SKILL.md)

Showing 12 of 40 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show hyperframes
bin/toolkit search "video animation" --repo hyperframes
bin/toolkit docs hyperframes "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [heygen-com/hyperframes at `78e849235aa9`](https://github.com/heygen-com/hyperframes/tree/78e849235aa96af479004ee14c2e0f8ec10ccb9d). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo hyperframes --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
