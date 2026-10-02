# brag

Agent skills that turn a project or website into a short launch video with motion, music and share copy; classic Brag uses Hyperframes and the slim variant uses available local rendering tools.

[Upstream repository](https://github.com/latent-spaces/brag) · [Pinned source](https://github.com/latent-spaces/brag/tree/cb89b9f44309b0bf4e3cb89e685fadf80c7999ed) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Writing, video, and audio |
| Operating model | skill-bundle |
| Recommended scope | on-demand |
| Registered production skill paths | 2 |
| Reviewed source commit | `cb89b9f44309b0bf4e3cb89e685fadf80c7999ed` |

## Purpose and use cases

Adds a focused project-to-launch-video workflow and an asset-free slim alternative. Retrieve only the selected skill and its references; preserve the bundled classic audio assets without global registration.

**Discovery tags:** `launch video`, `product demo`, `video generation`, `Hyperframes`, `music`, `share copy`, `agent skills`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Classic workflow requires an Agent Skills-capable coding agent, Node.js 22+, FFmpeg on PATH and Hyperframes CLI; companion Hyperframes composition skills are a separate dependency.
- Classic voiceover is opt-in and uses Kokoro through Hyperframes; its voice/runtime downloads and readiness must be checked separately.
- Slim is documented as designed for Claude Opus 5.5 and uses available local tools instead of Hyperframes or bundled assets; do not assume equivalent tested behavior on other models.
- Access to the target project or website and a writable output directory are needed. Agent-provider accounts depend on the chosen host; no letsbrag.app account is required for the local skill route.
- Linux/WSL source inspection works; rendering, browser and audio dependencies have not been installed or tested. Windows discovery symlinks need Developer Mode/admin support or manual copying.

## Setup guidance

**Setup scope:** on-demand skill retrieval or explicit project-scoped installation; isolated render dependencies and project output

**Next action:** setup-required

**Working directory:** Use runtime/brag for an isolated working copy/runtime if needed; read the pinned source in place and write video artifacts under the selected target project.

**Installation approach:** Prefer loading the selected skill directly with toolkit read. If project installation is requested, choose one documented npx skills route without -g and review/pin the resulting dependency versions. Classic requires a separately prepared Hyperframes runtime and its companion skills; no installer was executed during catalog review.

**Configuration:** Choose classic or slim and keep the full selected skill folder with its references/assets intact. Configure target input, output format and desired tone in the target project; enable voiceover only when requested. Read current Hyperframes setup documentation before installing its dependencies.

**Verification to perform:** After setup, check node --version, ffmpeg -version and npx hyperframes doctor for classic. A requested video run must pass the documented Hyperframes check, render successfully and yield a playable video with the expected duration/audio; slim needs visual and playback inspection using its chosen renderer.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read brag README.md
toolkit read brag skills/brag/SKILL.md
toolkit read brag docs/other-agents.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx skills add https://github.com/latent-spaces/brag --skill brag
```

Example 2:

```bash
npx skills add https://github.com/latent-spaces/brag --skill brag-slim
```

## Source entry points

- [README.md](https://github.com/latent-spaces/brag/blob/cb89b9f44309b0bf4e3cb89e685fadf80c7999ed/README.md)
- [plugin.json](https://github.com/latent-spaces/brag/blob/cb89b9f44309b0bf4e3cb89e685fadf80c7999ed/plugin.json)
- [docs/other-agents.md](https://github.com/latent-spaces/brag/blob/cb89b9f44309b0bf4e3cb89e685fadf80c7999ed/docs/other-agents.md)
- [skills/brag/SKILL.md](https://github.com/latent-spaces/brag/blob/cb89b9f44309b0bf4e3cb89e685fadf80c7999ed/skills/brag/SKILL.md)
- [skills/brag/references/step-3-compose.md](https://github.com/latent-spaces/brag/blob/cb89b9f44309b0bf4e3cb89e685fadf80c7999ed/skills/brag/references/step-3-compose.md)
- [skills/brag-slim/SKILL.md](https://github.com/latent-spaces/brag/blob/cb89b9f44309b0bf4e3cb89e685fadf80c7999ed/skills/brag-slim/SKILL.md)

## Skills and retrieval

The manifest registers **2 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/brag/SKILL.md](https://github.com/latent-spaces/brag/blob/cb89b9f44309b0bf4e3cb89e685fadf80c7999ed/skills/brag/SKILL.md)
- [skills/brag-slim/SKILL.md](https://github.com/latent-spaces/brag/blob/cb89b9f44309b0bf4e3cb89e685fadf80c7999ed/skills/brag-slim/SKILL.md)

```bash
bin/toolkit show brag
bin/toolkit search "launch video product demo" --repo brag
bin/toolkit docs brag "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [latent-spaces/brag at `cb89b9f44309`](https://github.com/latent-spaces/brag/tree/cb89b9f44309b0bf4e3cb89e685fadf80c7999ed). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo brag --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
