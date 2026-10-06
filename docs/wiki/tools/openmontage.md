# openmontage

Agent-directed video production workspace with staged pipelines, provider routing, production knowledge, rendering tools and a local storyboard dashboard.

[Upstream repository](https://github.com/calesthio/OpenMontage) · [Pinned source](https://github.com/calesthio/OpenMontage/tree/9327439db69021ab4b0e2776729bf3b58fdb5a87) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Writing, video, and audio |
| Operating model | agent workflow + tool library |
| Recommended scope | on-demand |
| Registered production skill paths | 90 |
| Reviewed source commit | `9327439db69021ab4b0e2776729bf3b58fdb5a87` |

## Purpose and use cases

Coordinate scripts, media generation, narration, compositing and delivery through pipeline artifacts. Select one pipeline and its providers; the skill library is retrieved on demand rather than installed globally.

**Discovery tags:** `video-production`, `animation`, `demo-video`, `storyboard`, `remotion`, `hyperframes`, `ffmpeg`, `skills`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Python 3.10+, FFmpeg, Node.js 18+ and an AI coding assistant; make setup installs Python dependencies, Remotion dependencies and attempts Piper TTS and HyperFrames setup.
- Pipeline requirements vary: cloud image/video/voice providers need their own credentials and may incur charges; offline/local alternatives require suitable models and runtime resources.
- Optional GPU workflows need compatible NVIDIA hardware and additional dependencies. Provider availability and quality checks must be confirmed per production.
- AGPL-3.0 project license; bundled skills, dependencies and generated media have their own applicable terms.

## Setup guidance

**Setup scope:** project-local or isolated tool runtime; explicit agent registration

**Next action:** setup-required

**Working directory:** An isolated tool checkout or the selected target project, according to the pinned setup guide.

**Installation approach:** Reuse a compatible runtime first. Select one documented installation route, review dependencies and pin the version; commands are examples, not a script to execute in order.

**Configuration:** Use an isolated production workspace, select its pipeline and provider budget, then configure only the necessary credentials in private environment files. Use .agents/skills as the canonical Layer 3 skill collection; mirrored .claude skills are not registered twice.

**Verification to perform:** Run the documented preflight and a small selected pipeline; inspect ffprobe, sampled frames, audio and stage artifacts before claiming production readiness.

**Local record:** Record the actual runtime version, checks and remaining requirements locally. Catalog/source presence does not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read openmontage README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
make setup
```

Example 2:

```bash
make preflight
```

## Source entry points

- [README.md](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/README.md)
- [AGENT_GUIDE.md](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/AGENT_GUIDE.md)
- [PROJECT_CONTEXT.md](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/PROJECT_CONTEXT.md)
- [Makefile](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/Makefile)
- [requirements.txt](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/requirements.txt)
- [pipeline_defs](https://github.com/calesthio/OpenMontage/tree/9327439db69021ab4b0e2776729bf3b58fdb5a87/pipeline_defs)
- [skills/pipelines](https://github.com/calesthio/OpenMontage/tree/9327439db69021ab4b0e2776729bf3b58fdb5a87/skills/pipelines)
- [backlot/README.md](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/backlot/README.md)

## Skills and retrieval

The manifest registers **90 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [.agents/skills/3d-asset-generation/SKILL.md](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/.agents/skills/3d-asset-generation/SKILL.md)
- [.agents/skills/acestep/SKILL.md](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/.agents/skills/acestep/SKILL.md)
- [.agents/skills/agents/SKILL.md](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/.agents/skills/agents/SKILL.md)
- [.agents/skills/ai-video-gen/SKILL.md](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/.agents/skills/ai-video-gen/SKILL.md)
- [.agents/skills/atlas-cloud/SKILL.md](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/.agents/skills/atlas-cloud/SKILL.md)
- [.agents/skills/avatar-video/SKILL.md](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/.agents/skills/avatar-video/SKILL.md)
- [.agents/skills/azure-speech-to-text/SKILL.md](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/.agents/skills/azure-speech-to-text/SKILL.md)
- [.agents/skills/azure-text-to-speech/SKILL.md](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/.agents/skills/azure-text-to-speech/SKILL.md)
- [.agents/skills/beautiful-mermaid/SKILL.md](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/.agents/skills/beautiful-mermaid/SKILL.md)
- [.agents/skills/bfl-api/SKILL.md](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/.agents/skills/bfl-api/SKILL.md)
- [.agents/skills/canvas-procedural-animation/SKILL.md](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/.agents/skills/canvas-procedural-animation/SKILL.md)
- [.agents/skills/character-animation-qa/SKILL.md](https://github.com/calesthio/OpenMontage/blob/9327439db69021ab4b0e2776729bf3b58fdb5a87/.agents/skills/character-animation-qa/SKILL.md)

Showing 12 of 90 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show openmontage
bin/toolkit search "video-production animation" --repo openmontage
bin/toolkit docs openmontage "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [calesthio/OpenMontage at `9327439db690`](https://github.com/calesthio/OpenMontage/tree/9327439db69021ab4b0e2776729bf3b58fdb5a87). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo openmontage --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
