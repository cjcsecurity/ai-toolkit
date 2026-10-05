# Catalog maintenance loops

Adapted from [Loop Engineering's thin-loop pattern](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/patterns/thin-loop.md). The issue tracker, pull requests, Actions summaries and local service journal carry state. No background model or agent is invoked.

| Loop | Cadence | Output | Validation | Stop switch |
| --- | --- | --- | --- | --- |
| Reviewed local additions | Daily, 09:17 America/Denver plus up to five minutes | One PR per new tool, with deterministic branch identity | Portable metadata, upstream pin, manager tests, generated docs/links, diff and secret checks | Disable `toolkit-catalog-pr.timer` and stop its service |
| Tool discovery | Weekly, Monday 15:23 UTC | At most one issue per ISO week, with up to five candidates | Bounded public GitHub search, license/activity filters, exclusions and prior-report deduplication | Disable the Tool discovery workflow |

The local publisher copies only a new manifest entry and literal category data into an isolated published-base worktree. It leaves source checkout edits intact. Existing or closed PRs are respected. The discovery loop never changes the manifest, installs tools, or claims candidates have been reviewed. Neither loop merges PRs.

Each run has a timeout; failed commands stop publication. Authentication and API errors stay visible rather than being interpreted as empty results. Review the resulting PRs and discovery issues before choosing tools. See [setup and operations](docs/catalog-automation.md) and [discovery configuration](docs/tool-discovery.md).
