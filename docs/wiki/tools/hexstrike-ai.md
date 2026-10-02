# hexstrike-ai

Python API service and MCP bridge that expose external reconnaissance, web-security, binary-analysis, forensics, and cloud-security tools to AI clients.

[Upstream repository](https://github.com/0x4m4/hexstrike-ai) · [Pinned source](https://github.com/0x4m4/hexstrike-ai/tree/d689933ff579d839c676c82b231f8e98326c5f04) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Security and assessment |
| Operating model | mcp |
| Recommended scope | on-demand |
| Registered production skill paths | 0 |
| Reviewed source commit | `d689933ff579d839c676c82b231f8e98326c5f04` |

## Purpose and use cases

Broad security-tool execution interface; run only for selected authorized work after installing the necessary external tools.

**Discovery tags:** `security`, `mcp`, `pentest`, `recon`, `forensics`, `binary-analysis`, `cloud-security`, `nmap`, `nuclei`, `osint`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- README advertises Python 3.8+; resolve actual compatibility of requirements.txt dependencies in an isolated environment before installation.
- Flask, requests, psutil, FastMCP, Selenium, aiohttp, mitmproxy, pwntools, and angr dependencies.
- External security binaries are separate installs; examples include nmap, nuclei, ffuf, sqlmap, GDB, and cloud scanners.
- Browser actions require Chrome/Chromium and ChromeDriver; selected cloud/OSINT tools require their own credentials.
- MCP client and running local hexstrike_server.py service; explicitly authorized targets/scope for testing.

## Setup guidance

**Setup scope:** isolated Python server/MCP runtime; external tool dependencies

**Next action:** setup-required

**Working directory:** Isolated deployment/build working copy under runtime/hexstrike-ai; preserve the pinned source checkout.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Install requirements in an isolated environment/working copy; configure server/MCP endpoints and only the external security binaries needed by the authorized task.

**Verification to perform:** Check server health and MCP tool listing without launching a target assessment.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read hexstrike-ai README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
python3 -m venv hexstrike-env
```

Example 2:

```bash
pip3 install -r requirements.txt
```

## Source entry points

- [README.md](https://github.com/0x4m4/hexstrike-ai/blob/d689933ff579d839c676c82b231f8e98326c5f04/README.md)
- [requirements.txt](https://github.com/0x4m4/hexstrike-ai/blob/d689933ff579d839c676c82b231f8e98326c5f04/requirements.txt)
- [hexstrike_mcp.py](https://github.com/0x4m4/hexstrike-ai/blob/d689933ff579d839c676c82b231f8e98326c5f04/hexstrike_mcp.py)
- [hexstrike_server.py](https://github.com/0x4m4/hexstrike-ai/blob/d689933ff579d839c676c82b231f8e98326c5f04/hexstrike_server.py)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show hexstrike-ai
bin/toolkit search "security mcp" --repo hexstrike-ai
bin/toolkit docs hexstrike-ai "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [0x4m4/hexstrike-ai at `d689933ff579`](https://github.com/0x4m4/hexstrike-ai/tree/d689933ff579d839c676c82b231f8e98326c5f04). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo hexstrike-ai --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
