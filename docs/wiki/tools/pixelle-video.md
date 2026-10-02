# pixelle-video

Python/Streamlit short-video creation platform combining LLM scripts, image/video workflows, speech, templates, background music, and FFmpeg composition.

[Upstream repository](https://github.com/ATH-MaaS/Pixelle-Video) · [Pinned source](https://github.com/ATH-MaaS/Pixelle-Video/tree/848b054e4fae40dabc62ec58e960b573e83793ac) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Writing, video, and audio |
| Operating model | application |
| Recommended scope | on-demand |
| Registered production skill paths | 0 |
| Reviewed source commit | `848b054e4fae40dabc62ec58e960b573e83793ac` |

## Purpose and use cases

Run as a dedicated application when generating videos. No SKILL.md files; fastmcp dependency alone is not evidence of a ready Codex/OpenCode connector. Preserve documented source setup and inspect API/MCP entrypoints before future integration.

**Discovery tags:** `video generation`, `short video`, `streamlit`, `comfyui`, `tts`, `ffmpeg`, `python`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Python >=3.11, uv, FFmpeg, and project dependencies.
- macOS/Linux source installation supported; Windows all-in-one package is documented.
- LLM endpoint/model/API key for script generation; local ComfyUI or RunningHub credentials for workflow-based media.
- Direct media providers such as OpenAI, DashScope, Volcengine, or Kling need provider credentials when selected.

## Setup guidance

**Setup scope:** isolated media application runtime; provider configuration

**Next action:** setup-required

**Working directory:** Isolated deployment/build working copy under runtime/pixelle-video; preserve the pinned source checkout.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Prepare Python/uv and FFmpeg in a working copy. Configure the selected script-generation model and local ComfyUI or hosted media provider.

**Verification to perform:** Start the documented Streamlit UI and render a short sample with the selected backend.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read pixelle-video README_EN.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
uv run streamlit run web/app.py
```

## Source entry points

- [README_EN.md](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/README_EN.md)
- [pyproject.toml](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/pyproject.toml)
- [web/app.py](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/web/app.py)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show pixelle-video
bin/toolkit search "video generation short video" --repo pixelle-video
bin/toolkit docs pixelle-video "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [ATH-MaaS/Pixelle-Video at `848b054e4fae`](https://github.com/ATH-MaaS/Pixelle-Video/tree/848b054e4fae40dabc62ec58e960b573e83793ac). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo pixelle-video --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
