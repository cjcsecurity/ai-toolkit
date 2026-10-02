# laya

Local non-autoregressive decision model SDK and CLI for typed choices, scores, triage, routing, and moderation, with optional HTTP and stdio MCP servers.

[Upstream repository](https://github.com/NandhaKishorM/laya) · [Pinned source](https://github.com/NandhaKishorM/laya/tree/4aa6761be8173de4ce6d92c31b3e40b6eaf59a7c) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | AI infrastructure and retrieval |
| Operating model | mcp |
| Recommended scope | on-demand |
| Registered production skill paths | 0 |
| Reviewed source commit | `4aa6761be8173de4ce6d92c31b3e40b6eaf59a7c` |

## Purpose and use cases

This is a decision-engine runtime, not a visual design skill. Optional stdio MCP can be configured in Codex/OpenCode when structured decisions are needed; do not preload model weights globally for unrelated tasks.

**Discovery tags:** `decision model`, `routing`, `triage`, `classification`, `local ai`, `python`, `mcp`, `huggingface`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Python >=3.10, PyTorch, Transformers, safetensors, Hugging Face Hub, and NumPy.
- Hugging Face checkpoint download on first use and memory/storage for 322M/421M parameter models.
- CPU, CUDA, or Apple MPS; GPU is optional and benchmark speeds are hardware-specific.
- laya[mcp] extra for MCP, laya[serve] for HTTP; no commercial API key required for local inference.

## Setup guidance

**Setup scope:** isolated shared inference runtime or project SDK

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Select Python SDK, MCP extra or HTTP extra. Download the required checkpoint and select a supported CPU/GPU device; no commercial API key is needed for local inference.

**Verification to perform:** Run a documented small local classification/routing example and verify the typed result.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read laya README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
python -m pip install laya
```

Example 2:

```bash
pip install "laya[mcp]"
```

Example 3:

```bash
laya-mcp-server
```

Example 4:

```bash
pip install "laya[serve]"
```

## Source entry points

- [README.md](https://github.com/NandhaKishorM/laya/blob/4aa6761be8173de4ce6d92c31b3e40b6eaf59a7c/README.md)
- [pyproject.toml](https://github.com/NandhaKishorM/laya/blob/4aa6761be8173de4ce6d92c31b3e40b6eaf59a7c/pyproject.toml)
- [laya/mcp/server.py](https://github.com/NandhaKishorM/laya/blob/4aa6761be8173de4ce6d92c31b3e40b6eaf59a7c/laya/mcp/server.py)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show laya
bin/toolkit search "decision model routing" --repo laya
bin/toolkit docs laya "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [NandhaKishorM/laya at `4aa6761be817`](https://github.com/NandhaKishorM/laya/tree/4aa6761be8173de4ce6d92c31b3e40b6eaf59a7c). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo laya --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
