# hypit

Agent-oriented video creation system with SVML compositions, captions, reusable assets, local rendering and optional generation/model services.

[Upstream repository](https://github.com/hypit-ai/hypit) · [Pinned source](https://github.com/hypit-ai/hypit/tree/e8f94006e1eed9b299448fe5bce6afa5646e2ba5) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Writing, video, and audio |
| Operating model | application |
| Recommended scope | on-demand |
| Registered production skill paths | 1 |
| Reviewed source commit | `e8f94006e1eed9b299448fe5bce6afa5646e2ba5` |

## Purpose and use cases

Specialized media-production capability, not general engineering infrastructure. Keep its skill discoverable for explicit video work and prepare renderer/services only then. Little direct Superpowers overlap.

**Discovery tags:** `video`, `svml`, `captions`, `render`, `media`, `creative`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Node.js >=22.15 and pnpm 10.33.x
- Live builds need ffmpeg/ffprobe, downloaded Chrome/Chromium and relevant programs
- Local WhisperX/OpenCV programs require Python 3.10–3.13 and uv
- Optional generation services require accounts/credentials; code-rendered visuals need no generation API
- Review platform-specific runtime dependencies before provisioning

## Setup guidance

**Setup scope:** isolated media application runtime; per-project composition

**Next action:** setup-required

**Working directory:** Isolated deployment/build working copy under runtime/hypit; preserve the pinned source checkout.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Provision the selected runtime profile and required programs in a working copy. Select local rendering or explicitly configured generation providers.

**Verification to perform:** Run documented hypit doctor for the selected runtime profile, then render a small local sample.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read hypit README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx skills add hypit-ai/hypit -g
```

Example 2:

```bash
pnpm install --frozen-lockfile
```

Example 3:

```bash
hypit doctor --runtime <profile>
```

Example 4:

```bash
hypit runtime up --runtime <profile>
```

## Source entry points

- [README.md](https://github.com/hypit-ai/hypit/blob/e8f94006e1eed9b299448fe5bce6afa5646e2ba5/README.md)
- [package.json](https://github.com/hypit-ai/hypit/blob/e8f94006e1eed9b299448fe5bce6afa5646e2ba5/package.json)
- [docs/guide/develop.md](https://github.com/hypit-ai/hypit/blob/e8f94006e1eed9b299448fe5bce6afa5646e2ba5/docs/guide/develop.md)
- [docs/guide/runtime.md](https://github.com/hypit-ai/hypit/blob/e8f94006e1eed9b299448fe5bce6afa5646e2ba5/docs/guide/runtime.md)
- [skills/hypit/SKILL.md](https://github.com/hypit-ai/hypit/blob/e8f94006e1eed9b299448fe5bce6afa5646e2ba5/skills/hypit/SKILL.md)

## Skills and retrieval

The manifest registers **1 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/hypit/SKILL.md](https://github.com/hypit-ai/hypit/blob/e8f94006e1eed9b299448fe5bce6afa5646e2ba5/skills/hypit/SKILL.md)

```bash
bin/toolkit show hypit
bin/toolkit search "video svml" --repo hypit
bin/toolkit docs hypit "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [hypit-ai/hypit at `e8f94006e1ee`](https://github.com/hypit-ai/hypit/tree/e8f94006e1eed9b299448fe5bce6afa5646e2ba5). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo hypit --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
