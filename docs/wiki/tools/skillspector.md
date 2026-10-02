# skillspector

Static and optional LLM-based scanner for agent skill bundles, with vulnerability-pattern analysis, dependency checks and JSON/SARIF reports.

[Upstream repository](https://github.com/NVIDIA/SkillSpector) · [Pinned source](https://github.com/NVIDIA/SkillSpector/tree/2226747e4ca97198bb82faf5085b8a75f2e1dc02) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Security and assessment |
| Operating model | cli |
| Recommended scope | on-demand |
| Registered production skill paths | 1 |
| Reviewed source commit | `2226747e4ca97198bb82faf5085b8a75f2e1dc02` |

## Purpose and use cases

Useful audit CLI for future skill changes with no need for a permanent MCP schema. Complements Superpowers rather than duplicating engineering process. Scanning finds indicators, not proof of safety. Only skills/skill-inspector is a product skill; inventory also includes deliberately unsafe test fixtures that must not be installed.

**Discovery tags:** `skill security`, `static analysis`, `supply chain`, `scanner`, `sarif`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Python >=3.12,<3.15 and uv/pip; OS-independent package classifier
- yara-python native wheel/build support may be needed
- Optional MCP requires [mcp] extra
- --no-llm avoids sending file contents to providers, but dependency names/versions are still queried at OSV.dev
- LLM analysis needs configured provider credentials or supported CLI/local endpoint

## Setup guidance

**Setup scope:** shared isolated scanner CLI; optional provider/MCP setup

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Install the CLI or selected MCP extra in an isolated tool environment. Choose local/no-LLM or configured model analysis; dependency lookup can still contact OSV.

**Verification to perform:** Scan a small benign skill and inspect JSON findings; verify provider behavior separately if LLM analysis is selected.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read skillspector README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
uv tool install git+https://github.com/NVIDIA/skillspector.git
```

Example 2:

```bash
uv tool install 'skillspector[mcp] @ git+https://github.com/NVIDIA/skillspector.git'
```

Example 3:

```bash
skillspector scan ./my-skill/ --no-llm --format json --output report.json
```

## Source entry points

- [README.md](https://github.com/NVIDIA/SkillSpector/blob/2226747e4ca97198bb82faf5085b8a75f2e1dc02/README.md)
- [pyproject.toml](https://github.com/NVIDIA/SkillSpector/blob/2226747e4ca97198bb82faf5085b8a75f2e1dc02/pyproject.toml)
- [docs/OPENCODE_EXTENSION.md](https://github.com/NVIDIA/SkillSpector/blob/2226747e4ca97198bb82faf5085b8a75f2e1dc02/docs/OPENCODE_EXTENSION.md)
- [docs/ANALYSIS_RESOURCE_BOUNDS.md](https://github.com/NVIDIA/SkillSpector/blob/2226747e4ca97198bb82faf5085b8a75f2e1dc02/docs/ANALYSIS_RESOURCE_BOUNDS.md)
- [skills/skill-inspector/SKILL.md](https://github.com/NVIDIA/SkillSpector/blob/2226747e4ca97198bb82faf5085b8a75f2e1dc02/skills/skill-inspector/SKILL.md)

## Skills and retrieval

The manifest registers **1 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/skill-inspector/SKILL.md](https://github.com/NVIDIA/SkillSpector/blob/2226747e4ca97198bb82faf5085b8a75f2e1dc02/skills/skill-inspector/SKILL.md)

```bash
bin/toolkit show skillspector
bin/toolkit search "skill security static analysis" --repo skillspector
bin/toolkit docs skillspector "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [NVIDIA/SkillSpector at `2226747e4ca9`](https://github.com/NVIDIA/SkillSpector/tree/2226747e4ca97198bb82faf5085b8a75f2e1dc02). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo skillspector --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
