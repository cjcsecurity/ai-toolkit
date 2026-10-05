# Weekly tool discovery

The weekly job creates an issue with up to five **unreviewed candidates, not
recommendations**. A human still reviews source, licensing, overlap, prerequisites,
and compatibility before adding anything to the catalog. GitHub license metadata
is a filter, not a legal or installation review.

The schedule is Monday at 15:23 UTC (09:23 MDT / 08:23 MST). GitHub may delay
scheduled jobs. `workflow_dispatch` runs the same workflow manually. Disable
`tool-discovery.yml` in Actions to stop discovery.

## Run and configure

Python 3.11+ and an authenticated GitHub CLI are sufficient. Candidate code is never
downloaded or executed, and no model, AI key, package installation, or local index
is needed. GitHub Actions supplies its job token only to the discovery step, with
`contents: read` and `issues: write` permissions.

```bash
# Read-only preview (the default); choose the catalog's issue repository.
python scripts/discover_tools.py --repo OWNER/REPOSITORY

# Publish only if this ISO week has no existing discovery issue.
python scripts/discover_tools.py --repo OWNER/REPOSITORY --publish

# Run the focused regression suite without GitHub access.
python -m unittest discover -s tests -p test_discover_tools.py -v
```

`--repo` defaults to `GITHUB_REPOSITORY` in Actions. `--config` and `--manifest`
accept alternate local files. The default configuration is
[`config/tool-discovery.json`](../config/tool-discovery.json), with seven topic
queries covering agent skills, MCP, developer tools, retrieval, browser automation,
game modding, and creative AI.

Configuration permits 5–8 distinct topic queries, 1–50 results per query, and
1–5 candidates per report. Defaults require creation within 180 days, a push within
90 days, and at least 20 stars. The supported ranges are 1–365 creation days,
1–180 push days, and 20–1,000,000 stars. Add `owner/repository` strings to the
optional `ignore` array to suppress particular projects; comparisons ignore case.
Unknown configuration keys and invalid repository identifiers fail before API calls.

Each query fetches one page sorted by stars. Selection rotates its starting topic
weekly, takes one candidate per topic, and fills remaining slots from available
topics. Star ties within a topic use repository name order. Results are stable for
the same ISO week and API snapshot; search results and star counts can change.
Bounded searches can miss repositories outside the fetched pages or without the
configured topic tags.

## Issue state and failure behavior

The script reads every page of open **and closed** repository issues using
[`gh api --paginate --slurp`](https://cli.github.com/manual/gh_api). Only issue
bodies beginning with the exact `<!-- ai-toolkit-discovery:week YYYY-Www -->`
marker belong to this job. Pull requests and other issues are ignored. Candidate
markers record previously reported repositories; closing a report therefore does
not cause dismissed candidates to recur. Preserve those markers when editing.

Existing catalog entries, ignored or previously reported repositories, duplicates,
private repositories, forks, archived projects, and repositories without a known
SPDX license identifier are excluded. Invalid URLs are discarded. Descriptions
and labels have mentions, HTML, control characters, and Markdown neutralized.
Repository URLs are constructed from validated GitHub identifiers.

An existing report for the UTC ISO week makes the whole run skip publication,
including when the issue is closed. Human edits and notes remain intact. Workflow
concurrency serializes scheduled and manual Actions runs; avoid simultaneous local
`--publish` runs because GitHub issue creation has no atomic uniqueness constraint.

All history and search requests must succeed before publication. An API error,
incomplete search, malformed configuration, or invalid issue state fails the job
without publishing a partial report. A failed create request can have an ambiguous
outcome; rerun to consult issue state. No candidates means a successful job summary
and no issue. Successful and skipped runs write to stdout and
`GITHUB_STEP_SUMMARY` when available.

## Reused workflow

This adapts the reviewed [Loop Engineering thin-loop starter](https://github.com/cobusgreyling/loop-engineering/tree/62801dea82905bc6afb5448d24e5386e9792ad06/starters/thin-loop)
at revision `62801dea82905bc6afb5448d24e5386e9792ad06`, MIT licensed, copyright
2026 Cobus Greyling and contributors. Its operating pattern is retained: one scheduled Action, GitHub
issues as persistent state, the job summary as the report, and a unique marker
that prevents duplicate writes. This adaptation adds deterministic repository
queries and replaces the starter's per-thread comment with one weekly issue.
There are no labels, closes, repository edits, candidate installs, or agent/model
invocations. See the upstream [MIT license](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/LICENSE).
