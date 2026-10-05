# Getting started

Use Linux, macOS, or WSL with Git and Python 3.11 or later. The launchers and runtime paths target POSIX hosts; native Windows is not verified. SQLite FTS5 must be available in Python's SQLite build. Lexical retrieval uses the Python standard library and does not need a model or API key.

```bash
git clone https://github.com/cjcsecurity/ai-toolkit.git
cd ai-toolkit
python3 scripts/bootstrap.py --repo humanizer --lexical
bin/toolkit search "natural prose editing" --kind repo --limit 8
bin/toolkit show humanizer
bin/toolkit skills humanizer
```

Use `bin/toolkit read humanizer PATH_FROM_RESULTS` to read a returned skill path in full. If it exceeds the output budget, continue with `--offset` as shown by the command output.

## Choose your download scope

| Command | Sources | Retrieval |
| --- | --- | --- |
| `python3 scripts/bootstrap.py` | No upstream clones | Catalog-only lexical index |
| `python3 scripts/bootstrap.py --repo humanizer --lexical` | Selected pinned source | Catalog and available source lexical index |
| `python3 scripts/bootstrap.py --all --lexical` | All cataloged pinned sources | Lexical index |
| `python3 scripts/bootstrap.py --all --semantic` | All cataloged pinned sources | Local hybrid lexical/vector index |

Bootstrap source downloads and semantic setup use the network. Semantic setup creates `runtime/search`, installs pinned dependencies, downloads the reviewed MiniLM ONNX checkpoint, and indexes locally. `uv` is recommended for provisioning Python 3.12; without it, use an existing supported Python 3.12–3.13 interpreter with venv support. A cold full-source semantic index can reach roughly 150,000 passages and take tens of minutes to hours depending on CPU. Selected-source setup is the practical starting point. Application runtimes remain a separate task.

## Search in two stages

```bash
bin/toolkit search "convert PDFs into structured documents" --kind repo --limit 8
bin/toolkit show docling
bin/toolkit search "OCR tables" --repo docling
bin/toolkit docs docling "installation"
```

Read complete setup requirements for promising candidates. Compare coverage, operating model, platform, accounts, services, and licensing before choosing. Missing information is an unresolved requirement, not evidence that a candidate has no value.

```bash
bin/toolkit select docling --project /path/to/existing/project
bin/toolkit project --project /path/to/existing/project
```

Selection writes `.ai-toolkit.json` in the target project. It does not install dependencies or enable services.

## Check the result

```bash
bin/toolkit search-status
bin/toolkit --budget 30000 doctor
```

`search-status` reports corpus/vector coverage and search mode. `doctor` checks local source presence and recorded revisions, not whether an external service or application works. Missing sources are expected after a selective install.

Continue to [agent integration](Codex-and-OpenCode.md), [runtime setup](Runtime-Setup.md), or the [tool catalog](Tool-Catalog.md).
