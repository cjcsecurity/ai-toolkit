# finance-skills

Agent Skills for market data, company valuation, earnings, options, stock research, read-only social research, startup analysis, and optional external market-data providers.

[Upstream repository](https://github.com/himself65/finance-skills) · [Pinned source](https://github.com/himself65/finance-skills/tree/7fe91853b536304b13bce210ecf8b685cf77ec48) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Finance and markets |
| Operating model | skill-bundle |
| Recommended scope | on-demand |
| Registered production skill paths | 26 |
| Reviewed source commit | `7fe91853b536304b13bce210ecf8b685cf77ec48` |

## Purpose and use cases

Select an individual skill and preserve its references instead of installing every plugin group. Standard skill guidance is usable with Codex/OpenCode, but Claude dynamic-shell syntax and generative-ui show_widget assumptions need adaptation to available tools.

**Discovery tags:** `finance`, `stocks`, `valuation`, `earnings`, `yfinance`, `tradingview`, `market data`, `codex`, `opencode`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Python/yfinance for core market-data skills; Yahoo Finance network access and rate limits.
- External provider skills can need paid API access (for example Fintel/Adanos).
- Social and desktop readers require opencli/browser sessions, TradingView/CDP, or tdl/Telegram setup as applicable.
- UI skill targets Claude show_widget and is not directly portable without an equivalent widget surface.

## Setup guidance

**Setup scope:** read selected skill; per-skill Python tools or connectors

**Next action:** read-selected-reference

**Working directory:** Read from the stored checkout; install only selected task dependencies in an isolated environment or the target project.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Read the chosen skill and references directly. Install its data/runtime dependencies only; provider subscriptions, browser sessions and host-specific widgets vary by skill.

**Verification to perform:** Confirm the selected skill prerequisites and retrieve a small read-only sample using the chosen provider.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read finance-skills README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx plugins add himself65/finance-skills
```

Example 2:

```bash
npx skills add himself65/finance-skills --skill yfinance-data
```

## Source entry points

- [README.md](https://github.com/himself65/finance-skills/blob/7fe91853b536304b13bce210ecf8b685cf77ec48/README.md)
- [plugins/market-analysis/skills/yfinance-data/SKILL.md](https://github.com/himself65/finance-skills/blob/7fe91853b536304b13bce210ecf8b685cf77ec48/plugins/market-analysis/skills/yfinance-data/SKILL.md)
- [plugins/market-analysis/skills/company-valuation/SKILL.md](https://github.com/himself65/finance-skills/blob/7fe91853b536304b13bce210ecf8b685cf77ec48/plugins/market-analysis/skills/company-valuation/SKILL.md)
- [plugins/data-providers/skills/tradingview-mcp/SKILL.md](https://github.com/himself65/finance-skills/blob/7fe91853b536304b13bce210ecf8b685cf77ec48/plugins/data-providers/skills/tradingview-mcp/SKILL.md)

## Skills and retrieval

The manifest registers **26 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [plugins/data-providers/skills/finance-sentiment/SKILL.md](https://github.com/himself65/finance-skills/blob/7fe91853b536304b13bce210ecf8b685cf77ec48/plugins/data-providers/skills/finance-sentiment/SKILL.md)
- [plugins/data-providers/skills/fintel-data/SKILL.md](https://github.com/himself65/finance-skills/blob/7fe91853b536304b13bce210ecf8b685cf77ec48/plugins/data-providers/skills/fintel-data/SKILL.md)
- [plugins/data-providers/skills/hormuz-strait/SKILL.md](https://github.com/himself65/finance-skills/blob/7fe91853b536304b13bce210ecf8b685cf77ec48/plugins/data-providers/skills/hormuz-strait/SKILL.md)
- [plugins/data-providers/skills/hyperliquid-reader/SKILL.md](https://github.com/himself65/finance-skills/blob/7fe91853b536304b13bce210ecf8b685cf77ec48/plugins/data-providers/skills/hyperliquid-reader/SKILL.md)
- [plugins/data-providers/skills/tradingview-mcp/SKILL.md](https://github.com/himself65/finance-skills/blob/7fe91853b536304b13bce210ecf8b685cf77ec48/plugins/data-providers/skills/tradingview-mcp/SKILL.md)
- [plugins/data-providers/skills/tradingview-reader/SKILL.md](https://github.com/himself65/finance-skills/blob/7fe91853b536304b13bce210ecf8b685cf77ec48/plugins/data-providers/skills/tradingview-reader/SKILL.md)
- [plugins/market-analysis/skills/company-valuation/SKILL.md](https://github.com/himself65/finance-skills/blob/7fe91853b536304b13bce210ecf8b685cf77ec48/plugins/market-analysis/skills/company-valuation/SKILL.md)
- [plugins/market-analysis/skills/earnings-preview/SKILL.md](https://github.com/himself65/finance-skills/blob/7fe91853b536304b13bce210ecf8b685cf77ec48/plugins/market-analysis/skills/earnings-preview/SKILL.md)
- [plugins/market-analysis/skills/earnings-recap/SKILL.md](https://github.com/himself65/finance-skills/blob/7fe91853b536304b13bce210ecf8b685cf77ec48/plugins/market-analysis/skills/earnings-recap/SKILL.md)
- [plugins/market-analysis/skills/estimate-analysis/SKILL.md](https://github.com/himself65/finance-skills/blob/7fe91853b536304b13bce210ecf8b685cf77ec48/plugins/market-analysis/skills/estimate-analysis/SKILL.md)
- [plugins/market-analysis/skills/etf-premium/SKILL.md](https://github.com/himself65/finance-skills/blob/7fe91853b536304b13bce210ecf8b685cf77ec48/plugins/market-analysis/skills/etf-premium/SKILL.md)
- [plugins/market-analysis/skills/options-payoff/SKILL.md](https://github.com/himself65/finance-skills/blob/7fe91853b536304b13bce210ecf8b685cf77ec48/plugins/market-analysis/skills/options-payoff/SKILL.md)

Showing 12 of 26 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show finance-skills
bin/toolkit search "finance stocks" --repo finance-skills
bin/toolkit docs finance-skills "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [himself65/finance-skills at `7fe91853b536`](https://github.com/himself65/finance-skills/tree/7fe91853b536304b13bce210ecf8b685cf77ec48). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo finance-skills --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
