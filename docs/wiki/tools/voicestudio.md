# voicestudio

Local speech studio with Electron desktop, voice cloning and design, transcription, dubbing, audiobooks, a REST API and an optional MCP connection to its running backend.

[Upstream repository](https://github.com/debpalash/VoiceStudio) · [Pinned source](https://github.com/debpalash/VoiceStudio/tree/befc0a6f5b552b0b99e6eea574bc3c55e3d0519a) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Writing, video, and audio |
| Operating model | application |
| Recommended scope | on-demand |
| Registered production skill paths | 2 |
| Reviewed source commit | `befc0a6f5b552b0b99e6eea574bc3c55e3d0519a` |

## Purpose and use cases

Adds local speech production and automation workflows plus dedicated audio and maintainer skills. Keep models, desktop/backend runtime and integration setup distinct from the searchable source; use current Electron guidance rather than retired Tauri setup sections.

**Discovery tags:** `voice cloning`, `speech synthesis`, `text to speech`, `transcription`, `video dubbing`, `audiobooks`, `local audio`, `Electron`, `MCP`, `CUDA`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Current desktop is Electron; Tauri was retired after 0.5.3. Source package version is 0.5.6. Source setup needs Git, Node.js 22+, Bun, uv/Python (pyproject requires >=3.11), and native build tooling including Rust/Cargo for builds.
- Linux release artifacts target x86_64. On WSL2, verify Electron display/audio, microphone/global shortcuts and GPU passthrough separately. A headless backend is an alternative deployment, not proof of desktop support.
- CPU processing is supported but slower; NVIDIA CUDA and Apple Silicon MPS acceleration require compatible hardware/runtime. Linux ROCm is opt-in; Windows ARM is experimental and Intel Mac uses a remote backend. Select an engine that fits actual RAM/VRAM and disk.
- Model weights are separate downloads with engine-specific licenses and sizes. Packaged CPU setup uses roughly 5 GiB runtime disk while source setup follows the CUDA lockfile; the base OmniVoice model adds roughly 2.3 GB. Reuse existing model/data paths.
- Basic local workflows do not require a cloud-service account. Hugging Face tokens are optional for public models but required with accepted access conditions for gated engines/diarization; optional cloud translation, remote workers and protected APIs require their own credentials.
- REST and MCP need a running backend (default localhost:3900); MCP HTTP endpoint is /mcp/. File-based MCP workflows require a configured shared base path; compressed audio requires FFmpeg. Do not infer downloaded models from catalog listings.
- The omnivoice-gallery git submodule is not initialized by the toolkit source downloader. Review its documented need before a chosen build or gallery workflow.

## Setup guidance

**Setup scope:** isolated desktop/backend runtime and model storage; per-project API/MCP integration

**Next action:** setup-required

**Working directory:** Use a separate working copy under runtime/voicestudio for any source setup. Preserve the pinned checkout and reuse the user's existing application data/models when present.

**Installation approach:** Choose an architecture-compatible VoiceStudio-Electron release or the documented source route in a runtime working copy: bun install, then bun run setup:api. These are source setup steps, not interchangeable alternatives; the npx skills command is a separate optional skill installation. Prefer packaged CPU setup on a CPU-only host. Inspect installer/build prerequisites first. Dependencies and models require separate installation.

**Configuration:** Determine desktop versus headless deployment and verify WSL GUI/audio requirements before promising desktop readiness. Select actual compute device and engine, preserve existing data paths, and establish model download scope/license requirements. Keep cloud services and analytics opt-in. Add optional credentials only for selected gated models or remote services; connect MCP per project only after backend health succeeds.

**Verification to perform:** For source desktop, launch with the documented bun run dev and let Electron supervise its backend. Check GET /health and /openapi.json, actual compute device and GET /models installed state. Complete an authorized short audio generation and decode/play the output. Test requested MCP operations against the live endpoint; application launch alone is not model readiness.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read voicestudio README.md
toolkit read voicestudio electron/README.md
toolkit read voicestudio docs/install/agent.md
toolkit read voicestudio docs/performance.md
toolkit read voicestudio skills/voicestudio/SKILL.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
bun install
```

Example 2:

```bash
bun run setup:api
```

Example 3:

```bash
npx skills add debpalash/VoiceStudio
```

## Source entry points

- [README.md](https://github.com/debpalash/VoiceStudio/blob/befc0a6f5b552b0b99e6eea574bc3c55e3d0519a/README.md)
- [package.json](https://github.com/debpalash/VoiceStudio/blob/befc0a6f5b552b0b99e6eea574bc3c55e3d0519a/package.json)
- [pyproject.toml](https://github.com/debpalash/VoiceStudio/blob/befc0a6f5b552b0b99e6eea574bc3c55e3d0519a/pyproject.toml)
- [electron/README.md](https://github.com/debpalash/VoiceStudio/blob/befc0a6f5b552b0b99e6eea574bc3c55e3d0519a/electron/README.md)
- [docs/install/agent.md](https://github.com/debpalash/VoiceStudio/blob/befc0a6f5b552b0b99e6eea574bc3c55e3d0519a/docs/install/agent.md)
- [docs/install/script.md](https://github.com/debpalash/VoiceStudio/blob/befc0a6f5b552b0b99e6eea574bc3c55e3d0519a/docs/install/script.md)
- [docs/performance.md](https://github.com/debpalash/VoiceStudio/blob/befc0a6f5b552b0b99e6eea574bc3c55e3d0519a/docs/performance.md)
- [docs/setup/huggingface-token.md](https://github.com/debpalash/VoiceStudio/blob/befc0a6f5b552b0b99e6eea574bc3c55e3d0519a/docs/setup/huggingface-token.md)
- [docs/mcp.md](https://github.com/debpalash/VoiceStudio/blob/befc0a6f5b552b0b99e6eea574bc3c55e3d0519a/docs/mcp.md)
- [docs/speech-platform.md](https://github.com/debpalash/VoiceStudio/blob/befc0a6f5b552b0b99e6eea574bc3c55e3d0519a/docs/speech-platform.md)
- [skills/voicestudio/SKILL.md](https://github.com/debpalash/VoiceStudio/blob/befc0a6f5b552b0b99e6eea574bc3c55e3d0519a/skills/voicestudio/SKILL.md)

## Skills and retrieval

The manifest registers **2 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/voicestudio/SKILL.md](https://github.com/debpalash/VoiceStudio/blob/befc0a6f5b552b0b99e6eea574bc3c55e3d0519a/skills/voicestudio/SKILL.md)
- [skills/voicestudio-maintainer/SKILL.md](https://github.com/debpalash/VoiceStudio/blob/befc0a6f5b552b0b99e6eea574bc3c55e3d0519a/skills/voicestudio-maintainer/SKILL.md)

```bash
bin/toolkit show voicestudio
bin/toolkit search "voice cloning speech synthesis" --repo voicestudio
bin/toolkit docs voicestudio "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [debpalash/VoiceStudio at `befc0a6f5b55`](https://github.com/debpalash/VoiceStudio/tree/befc0a6f5b552b0b99e6eea574bc3c55e3d0519a). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo voicestudio --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
