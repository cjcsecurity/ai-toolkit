# docling

Local document conversion and extraction for PDF, Office files, HTML, images and audio into Markdown or structured DoclingDocument JSON, with OCR, tables and RAG chunking.

[Upstream repository](https://github.com/docling-project/docling) · [Pinned source](https://github.com/docling-project/docling/tree/bba2ec58fe58af1be630fea5cc0d35b0ad2a472e) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | AI infrastructure and retrieval |
| Operating model | framework |
| Recommended scope | on-demand |
| Registered production skill paths | 1 |
| Reviewed source commit | `bba2ec58fe58af1be630fea5cc0d35b0ad2a472e` |

## Purpose and use cases

Use an isolated shared CLI for one-off document conversion, or install the SDK in each application that embeds processing. Model artifacts can be cached once per selected environment; pipeline and output configuration remain task/project-specific. Full docs/ Markdown and product skill references are present. Docling MCP and docling-serve are separate packages/repos, not already configured here. Excludes imported maintainer Python/agent-building skills.

**Discovery tags:** `document parsing`, `pdf`, `ocr`, `markdown`, `rag`, `tables`, `document extraction`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Python >=3.10,<4.0 (root docling-slim and packages/docling metadata); uv or pip. Linux/macOS/Windows, x86_64 or arm64 with compatible dependency wheels.
- Local PDF/ML pipelines use PyTorch and download model artifacts on first use; offline operation requires prefetched model weights and artifacts-path configuration. CPU operation is supported; accelerator support depends on installed PyTorch and pipeline.
- OCR/VLM/ASR/extraction extras and model licenses apply to the chosen pipeline. Tesseract OCR needs separate system installation; Nemotron OCR requires Linux x86_64, Python 3.12 and CUDA 13.x.
- Per-project Python SDK installs/configuration differ from a reusable CLI tool installation. Remote conversion requires a separate docling-serve endpoint and API key if configured; remote MCP requires docling-mcp and client configuration.

## Setup guidance

**Setup scope:** shared conversion CLI/model cache or project SDK

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Choose a CLI tool environment for one-off conversion or a project dependency for embedded processing. Select OCR/VLM extras and download only required model artifacts.

**Verification to perform:** Convert a small sample document to Markdown/JSON and verify extracted text; test OCR separately if selected.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read docling docs/getting_started/installation.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
uv tool install docling
```

Example 2:

```bash
uvx --from docling docling report.pdf --to md --output /tmp/
```

Example 3:

```bash
uv add docling
```

Example 4:

```bash
docling-tools models download
```

## Source entry points

- [README.md](https://github.com/docling-project/docling/blob/bba2ec58fe58af1be630fea5cc0d35b0ad2a472e/README.md)
- [pyproject.toml](https://github.com/docling-project/docling/blob/bba2ec58fe58af1be630fea5cc0d35b0ad2a472e/pyproject.toml)
- [packages/docling/pyproject.toml](https://github.com/docling-project/docling/blob/bba2ec58fe58af1be630fea5cc0d35b0ad2a472e/packages/docling/pyproject.toml)
- [docs/getting_started/installation.md](https://github.com/docling-project/docling/blob/bba2ec58fe58af1be630fea5cc0d35b0ad2a472e/docs/getting_started/installation.md)
- [docs/usage/advanced_options.md](https://github.com/docling-project/docling/blob/bba2ec58fe58af1be630fea5cc0d35b0ad2a472e/docs/usage/advanced_options.md)
- [docs/usage/api_server/index.md](https://github.com/docling-project/docling/blob/bba2ec58fe58af1be630fea5cc0d35b0ad2a472e/docs/usage/api_server/index.md)
- [docs/usage/mcp.md](https://github.com/docling-project/docling/blob/bba2ec58fe58af1be630fea5cc0d35b0ad2a472e/docs/usage/mcp.md)
- [docling/.agents/skills/docling/SKILL.md](https://github.com/docling-project/docling/blob/bba2ec58fe58af1be630fea5cc0d35b0ad2a472e/docling/.agents/skills/docling/SKILL.md)

## Skills and retrieval

The manifest registers **1 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [docling/.agents/skills/docling/SKILL.md](https://github.com/docling-project/docling/blob/bba2ec58fe58af1be630fea5cc0d35b0ad2a472e/docling/.agents/skills/docling/SKILL.md)

```bash
bin/toolkit show docling
bin/toolkit search "document parsing pdf" --repo docling
bin/toolkit docs docling "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [docling-project/docling at `bba2ec58fe58`](https://github.com/docling-project/docling/tree/bba2ec58fe58af1be630fea5cc0d35b0ad2a472e). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo docling --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
