# Troubleshooting

| Symptom | Check and next step |
| --- | --- |
| Repository appears in search but its files cannot be read | Only its catalog summary may be present. Run `python3 scripts/bootstrap.py --repo ID --lexical` to download its pinned source. |
| Search reports lexical fallback | Run `bin/toolkit search-status`. Explicitly configure semantic retrieval with `python3 scripts/bootstrap.py --semantic`, then check coverage. |
| Semantic setup cannot find a supported Python | Use `uv` for the recommended Python 3.12 setup, or install Python 3.12–3.13 with venv support. Lexical mode still works on Python 3.11+. |
| Model checksum mismatch | Stop using the modified checkpoint. Re-run explicit model setup to download the recorded revision; do not bypass hash verification. |
| No SQLite FTS5 module | Use a Python distribution whose SQLite includes FTS5. It is required even for lexical mode. |
| Results are broad or dominated by one collection | Start with `--kind repo`; then refine the task and search within a chosen repository using `--repo ID`. |
| Output is clipped | Increase `toolkit --budget N COMMAND` or continue `read` with the reported `--offset`. The budget is characters. |
| `toolkit` is not found after registration | Add `~/.local/bin` to `PATH`, or invoke `bin/toolkit` from the checkout. |
| Registration reports a conflict | Inspect the existing destination and decide which installation to keep. The installer preserves conflicting user files instead of overwriting them. |
| Launchers refer to a moved checkout | Inspect and explicitly remove stale symlinks, then register the new checkout. `AI_TOOLKIT_HOME` selects a data/runtime root but cannot repair broken launcher links. |
| `doctor` reports missing source | Expected after selective bootstrap; download only the repositories you need. |
| `doctor` reports a revision mismatch | Inspect local checkout changes before updating. Do not discard uncommitted work just to satisfy the recorded pin. |
| MCP adapter cannot start | Install the optional MCP client dependencies and the selected server separately; check its command/path environment variables. |
| Browser authentication is missing | The Chrome adapter uses an isolated browser. Normal-profile authentication is not inherited. |
| Tool source is present but the application fails | Read its requirements and verify its own runtime. Source indexing does not install applications, credentials, containers, or services. |

For an issue report, include your OS, Python version, command, concise error, and relevant `search-status`/`doctor` output. Remove private paths, credentials, and sensitive source excerpts before sharing.

[Getting started](Getting-Started.md) · [Runtime setup](Runtime-Setup.md) · [Retrieval system](Retrieval-System.md)
