# hackingtool

Python security-tool catalog, installer and launcher with category/tag search, optional AI recommendations and guided workflows; includes a documented catalog of 215 active tools across 21 categories.

[Upstream repository](https://github.com/Z4nzu/hackingtool) · [Pinned source](https://github.com/Z4nzu/hackingtool/tree/ef5334f8d37e5be2eecbf56e334f5e3f0f6817ec) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Security and assessment |
| Operating model | cli |
| Recommended scope | on-demand |
| Registered production skill paths | 0 |
| Reviewed source commit | `ef5334f8d37e5be2eecbf56e334f5e3f0f6817ec` |

## Purpose and use cases

Complements the library with a searchable inventory of individual security utilities. Installing this launcher does not install its downstream catalog. Keep optional AI and task-specific utilities on demand.

**Discovery tags:** `security tool catalog`, `tool discovery`, `OSINT`, `forensics`, `network security`, `cloud security`, `static analysis`, `tool launcher`, `AI recommendations`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Python >=3.10 on Linux or macOS; README explicitly rejects native Windows despite a Windows package classifier. WSL Linux can use the Linux setup route.
- Source installation using pipx, uv tool or an isolated venv; README hides PyPI installation examples pending distribution availability, so use the reviewed source route rather than assuming pip install hackingtool is the intended package.
- Core dependencies include rich, PyYAML, platformdirs, prompt_toolkit and python-dotenv. Individual downstream tools may require Go >=1.21, Ruby, Docker, tmux or system packages.
- AI is optional: configure an OpenAI-compatible provider/key or local Ollama. Catalog browsing and ordinary launcher functions work without AI.
- Downstream tools and external actions require their own installation, accounts and authorized task scope. Reference/link entries do not represent local executable packages.

## Setup guidance

**Setup scope:** shared isolated catalog/launcher; individually selected downstream tool installations

**Next action:** setup-required

**Working directory:** Use an isolated shared runtime or a working copy under runtime/hackingtool; preserve the pinned source checkout. Target configuration belongs to the selected project.

**Installation approach:** Choose one documented install route from install_commands and pin its version. These are setup references, not a script to run in full. Reuse any subsequently installed runtime first.

**Configuration:** Create a working copy of the recorded revision under the toolkit runtime area and choose pipx or uv tool installation from that directory. Configure optional AI only if needed. Select and install downstream utilities individually; the catalog itself does not provision all tools.

**Verification to perform:** Check CLI help and list/search the local catalog without running a tool. Confirm prerequisites for each selected downstream utility separately.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read hackingtool README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
pipx install .
```

Example 2:

```bash
uv tool install .
```

Example 3:

```bash
uv sync
```

## Source entry points

- [README.md](https://github.com/Z4nzu/hackingtool/blob/ef5334f8d37e5be2eecbf56e334f5e3f0f6817ec/README.md)
- [pyproject.toml](https://github.com/Z4nzu/hackingtool/blob/ef5334f8d37e5be2eecbf56e334f5e3f0f6817ec/pyproject.toml)
- [docs/HOW-TO-USE.md](https://github.com/Z4nzu/hackingtool/blob/ef5334f8d37e5be2eecbf56e334f5e3f0f6817ec/docs/HOW-TO-USE.md)
- [docs/TOOLS.md](https://github.com/Z4nzu/hackingtool/blob/ef5334f8d37e5be2eecbf56e334f5e3f0f6817ec/docs/TOOLS.md)
- [Dockerfile](https://github.com/Z4nzu/hackingtool/blob/ef5334f8d37e5be2eecbf56e334f5e3f0f6817ec/Dockerfile)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show hackingtool
bin/toolkit search "security tool catalog tool discovery" --repo hackingtool
bin/toolkit docs hackingtool "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [Z4nzu/hackingtool at `ef5334f8d37e`](https://github.com/Z4nzu/hackingtool/tree/ef5334f8d37e5be2eecbf56e334f5e3f0f6817ec). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo hackingtool --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
