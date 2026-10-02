# agent-reach

CLI and skill that select, configure, and check upstream tools for web pages, video transcripts, RSS, GitHub, search, and social-platform research.

[Upstream repository](https://github.com/Panniantong/Agent-Reach) · [Pinned source](https://github.com/Panniantong/Agent-Reach/tree/a19a171fa980a0785849596492e0af4db800c82f) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Browsers, research, and web data |
| Operating model | cli |
| Recommended scope | on-demand |
| Registered production skill paths | 1 |
| Reviewed source commit | `a19a171fa980a0785849596492e0af4db800c82f` |

## Purpose and use cases

Useful routing reference across platforms; upstream tools and account access differ by channel, so select channels when requested.

**Discovery tags:** `research`, `search`, `scraping`, `youtube`, `transcripts`, `rss`, `github`, `twitter`, `reddit`, `social-media`, `bilibili`, `xiaohongshu`, `mcp`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Python >=3.10; dependencies include requests, feedparser, yt-dlp, rich, and PyYAML.
- Channel-dependent upstream tools include Node.js, gh, mcporter, OpenCLI, twitter-cli, bili-cli, and rdt-cli.
- Basic web/YouTube/RSS/public GitHub paths can work without account login.
- Social channels may require explicitly supplied cookies or an existing user-controlled Chrome session; private GitHub operations require GitHub authentication.
- Optional podcast transcription uses a Groq API key; server deployments may need a proxy.

## Setup guidance

**Setup scope:** shared CLI; channel-specific setup

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Install the CLI in an isolated tool environment, then configure only the requested channels and their upstream commands; credentials/cookies depend on the channel.

**Verification to perform:** Use the documented channel diagnostics, then fetch one public test item for the selected channel.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read agent-reach docs/install.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
pipx install https://github.com/Panniantong/agent-reach/archive/main.zip
```

Example 2:

```bash
pip install https://github.com/Panniantong/agent-reach/archive/main.zip
```

## Source entry points

- [README.md](https://github.com/Panniantong/Agent-Reach/blob/a19a171fa980a0785849596492e0af4db800c82f/README.md)
- [docs/install.md](https://github.com/Panniantong/Agent-Reach/blob/a19a171fa980a0785849596492e0af4db800c82f/docs/install.md)
- [pyproject.toml](https://github.com/Panniantong/Agent-Reach/blob/a19a171fa980a0785849596492e0af4db800c82f/pyproject.toml)
- [agent_reach/skill/SKILL.md](https://github.com/Panniantong/Agent-Reach/blob/a19a171fa980a0785849596492e0af4db800c82f/agent_reach/skill/SKILL.md)

## Skills and retrieval

The manifest registers **1 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [agent_reach/skill/SKILL.md](https://github.com/Panniantong/Agent-Reach/blob/a19a171fa980a0785849596492e0af4db800c82f/agent_reach/skill/SKILL.md)

```bash
bin/toolkit show agent-reach
bin/toolkit search "research search" --repo agent-reach
bin/toolkit docs agent-reach "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [Panniantong/Agent-Reach at `a19a171fa980`](https://github.com/Panniantong/Agent-Reach/tree/a19a171fa980a0785849596492e0af4db800c82f). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo agent-reach --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
