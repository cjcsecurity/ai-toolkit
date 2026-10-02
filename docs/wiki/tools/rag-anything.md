# rag-anything

Python framework built on LightRAG for parsing and indexing documents, images, tables, equations, audio, and video for multimodal retrieval and question answering.

[Upstream repository](https://github.com/HKUDS/RAG-Anything) · [Pinned source](https://github.com/HKUDS/RAG-Anything/tree/1f73f0154c48b3d616674608af98748585b856f3) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | AI infrastructure and retrieval |
| Operating model | application |
| Recommended scope | on-demand |
| Registered production skill paths | 0 |
| Reviewed source commit | `1f73f0154c48b3d616674608af98748585b856f3` |

## Purpose and use cases

Use in a task-specific Python environment for document research; parser models and multimodal dependencies can be substantial.

**Discovery tags:** `research`, `rag`, `documents`, `pdf`, `ocr`, `multimodal`, `knowledge-graph`, `retrieval`, `tables`, `audio`, `video`, `lightrag`, `mineru`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Python >=3.10; core dependencies include LightRAG, MinerU, huggingface_hub, and tqdm.
- Parser model downloads occur on first use; GPU support is optional and backend-dependent.
- Full RAG needs configured language/vision/embedding model functions and provider credentials if using hosted providers; parser-only examples need no API key.
- Office documents need LibreOffice; video needs ffmpeg; optional image/audio/video/PaddleOCR extras add dependencies. PaddleOCR also needs a platform-specific PaddlePaddle install.

## Setup guidance

**Setup scope:** isolated application/SDK environment; parser/model configuration

**Next action:** setup-required

**Working directory:** Isolated deployment/build working copy under runtime/rag-anything; preserve the pinned source checkout.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Choose parser-only or full RAG and only needed extras. Configure parser artifacts and selected language/vision/embedding providers; optional Office/video tools are separate.

**Verification to perform:** Parse a small document; for full RAG also index it and verify an answer supported by that document.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read rag-anything README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
pip install raganything
```

Example 2:

```bash
pip install "raganything[all]"
```

Example 3:

```bash
uv sync
```

## Source entry points

- [README.md](https://github.com/HKUDS/RAG-Anything/blob/1f73f0154c48b3d616674608af98748585b856f3/README.md)
- [pyproject.toml](https://github.com/HKUDS/RAG-Anything/blob/1f73f0154c48b3d616674608af98748585b856f3/pyproject.toml)
- [examples/raganything_example.py](https://github.com/HKUDS/RAG-Anything/blob/1f73f0154c48b3d616674608af98748585b856f3/examples/raganything_example.py)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show rag-anything
bin/toolkit search "research rag" --repo rag-anything
bin/toolkit docs rag-anything "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [HKUDS/RAG-Anything at `1f73f0154c48`](https://github.com/HKUDS/RAG-Anything/tree/1f73f0154c48b3d616674608af98748585b856f3). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo rag-anything --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
