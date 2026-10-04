# AI Toolkit wiki

AI Toolkit makes a reviewed catalog of 60 open-source tools searchable without loading every tool's instructions into agent context. Begin with repository comparisons, then retrieve a skill or documentation section inside the selected system.

| Start here | What you will find |
| --- | --- |
| [Getting started](Getting-Started.md) | Small lexical install, full semantic install, and first searches |
| [All 60 tools](Tool-Catalog.md) | Categories and a detailed page for every catalog entry |
| [RAG recommendations](../rag.md) | Project evidence bundles, MCP access, reproducible evaluation and a sourced demo |
| [Retrieval system](Retrieval-System.md) | Corpus, local embeddings, lexical search, scoring, and limits |
| [Codex and OpenCode](Codex-and-OpenCode.md) | Explicit client registration and on-demand skills |
| [Runtime setup](Runtime-Setup.md) | Separate source retrieval from application and MCP setup |
| [Maintenance](Maintenance.md) | Pins, updates, regeneration, indexing, and checks |
| [Troubleshooting](Troubleshooting.md) | Missing source, lexical fallback, registration conflicts, and runtime gaps |
| [Security and privacy](Security-and-Privacy.md) | Network boundaries, credentials, browser isolation, and provenance |

**Cataloged, source downloaded, and runtime configured are separate states.** A fresh clone has catalog metadata and manager code. Bootstrap downloads only requested source repositories and, if explicitly requested, the local semantic runtime. Each upstream application has its own setup requirements.

This wiki is versioned under `docs/wiki/` so documentation changes can be reviewed alongside code and source pins. [Return to the README](../../README.md).
