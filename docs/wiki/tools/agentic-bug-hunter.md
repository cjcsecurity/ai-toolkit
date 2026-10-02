# agentic-bug-hunter

Bug-bounty CLI, skill collection, and agent integrations for reconnaissance, vulnerability investigation, finding validation, and report generation.

[Upstream repository](https://github.com/awarexone/Agentic-Bug-Hunter) · [Pinned source](https://github.com/awarexone/Agentic-Bug-Hunter/tree/2e86602f61057d48e4542a51c97dd5675612358f) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Security and assessment |
| Operating model | cli |
| Recommended scope | on-demand |
| Registered production skill paths | 16 |
| Reviewed source commit | `2e86602f61057d48e4542a51c97dd5675612358f` |

## Purpose and use cases

Keep the command and skills available for explicitly scoped security tasks; its hunt/recon commands perform active target testing.

**Discovery tags:** `security`, `bug-bounty`, `pentest`, `recon`, `vulnerability`, `report-writing`, `web-security`, `api-security`, `mcp`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Python >=3.10 with requests and mcp.
- Hosted AI-provider key or a running local Ollama model for standalone AI mode; agent/plugin mode uses the selected host.
- Full reconnaissance additionally needs external tools such as subfinder, httpx, nuclei, katana, ffuf, and nmap; installer may need Go/system packages.
- Optional target credentials and explicitly authorized target scope.

## Setup guidance

**Setup scope:** isolated shared CLI; target/project configuration

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Choose standalone or host-agent mode; configure the chosen model and only the recon binaries required by the authorized task.

**Verification to perform:** Check CLI help and required binary availability before running a scoped test.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read agentic-bug-hunter README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
uv tool install agentic-bug-hunter
```

Example 2:

```bash
pipx install agentic-bug-hunter
```

Example 3:

```bash
./install.sh --agent standalone
```

## Source entry points

- [README.md](https://github.com/awarexone/Agentic-Bug-Hunter/blob/2e86602f61057d48e4542a51c97dd5675612358f/README.md)
- [FAQ.md](https://github.com/awarexone/Agentic-Bug-Hunter/blob/2e86602f61057d48e4542a51c97dd5675612358f/FAQ.md)
- [SKILL.md](https://github.com/awarexone/Agentic-Bug-Hunter/blob/2e86602f61057d48e4542a51c97dd5675612358f/SKILL.md)
- [pyproject.toml](https://github.com/awarexone/Agentic-Bug-Hunter/blob/2e86602f61057d48e4542a51c97dd5675612358f/pyproject.toml)
- [TERMS.md](https://github.com/awarexone/Agentic-Bug-Hunter/blob/2e86602f61057d48e4542a51c97dd5675612358f/TERMS.md)

## Skills and retrieval

The manifest registers **16 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [SKILL.md](https://github.com/awarexone/Agentic-Bug-Hunter/blob/2e86602f61057d48e4542a51c97dd5675612358f/SKILL.md)
- [skills/argus/SKILL.md](https://github.com/awarexone/Agentic-Bug-Hunter/blob/2e86602f61057d48e4542a51c97dd5675612358f/skills/argus/SKILL.md)
- [skills/bb-methodology/SKILL.md](https://github.com/awarexone/Agentic-Bug-Hunter/blob/2e86602f61057d48e4542a51c97dd5675612358f/skills/bb-methodology/SKILL.md)
- [skills/bug-bounty/SKILL.md](https://github.com/awarexone/Agentic-Bug-Hunter/blob/2e86602f61057d48e4542a51c97dd5675612358f/skills/bug-bounty/SKILL.md)
- [skills/cicd-security/SKILL.md](https://github.com/awarexone/Agentic-Bug-Hunter/blob/2e86602f61057d48e4542a51c97dd5675612358f/skills/cicd-security/SKILL.md)
- [skills/client-reverse/SKILL.md](https://github.com/awarexone/Agentic-Bug-Hunter/blob/2e86602f61057d48e4542a51c97dd5675612358f/skills/client-reverse/SKILL.md)
- [skills/credential-attack/SKILL.md](https://github.com/awarexone/Agentic-Bug-Hunter/blob/2e86602f61057d48e4542a51c97dd5675612358f/skills/credential-attack/SKILL.md)
- [skills/graphql-audit/SKILL.md](https://github.com/awarexone/Agentic-Bug-Hunter/blob/2e86602f61057d48e4542a51c97dd5675612358f/skills/graphql-audit/SKILL.md)
- [skills/meme-coin-audit/SKILL.md](https://github.com/awarexone/Agentic-Bug-Hunter/blob/2e86602f61057d48e4542a51c97dd5675612358f/skills/meme-coin-audit/SKILL.md)
- [skills/mobile-pentest/SKILL.md](https://github.com/awarexone/Agentic-Bug-Hunter/blob/2e86602f61057d48e4542a51c97dd5675612358f/skills/mobile-pentest/SKILL.md)
- [skills/report-writing/SKILL.md](https://github.com/awarexone/Agentic-Bug-Hunter/blob/2e86602f61057d48e4542a51c97dd5675612358f/skills/report-writing/SKILL.md)
- [skills/security-arsenal/SKILL.md](https://github.com/awarexone/Agentic-Bug-Hunter/blob/2e86602f61057d48e4542a51c97dd5675612358f/skills/security-arsenal/SKILL.md)

Showing 12 of 16 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show agentic-bug-hunter
bin/toolkit search "security bug-bounty" --repo agentic-bug-hunter
bin/toolkit docs agentic-bug-hunter "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [awarexone/Agentic-Bug-Hunter at `2e86602f6105`](https://github.com/awarexone/Agentic-Bug-Hunter/tree/2e86602f61057d48e4542a51c97dd5675612358f). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo agentic-bug-hunter --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
