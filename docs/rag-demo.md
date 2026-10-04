# Agent recommendation demonstration

This example was run on 2026-10-04 UTC using the real local stdio MCP server and its official Python SDK client. Evidence came from the published 60-repository index and local MiniLM model. The calling Codex assistant generated the recommendation below after inspecting that evidence. The session did not expose an exact deployment/model identifier; no separate generation API was called.

## Request and retrieval

> Python HTML extraction that finds the same product elements after a website changes its layout.

Constraint: prefer local Python parsing and inspect setup requirements.

```bash
runtime/search/bin/python examples/rag_mcp.py --output /tmp/rag-demo-evidence.json
```

The recorded [MCP evidence bundle](../reviews/rag-demo-evidence.json) contains three candidates: Scrapling, Firecrawl and Browser Harness. It records the query, constraint, model/corpus identity, repository prerequisites, exact evidence, and source provenance. Retrieval used hybrid mode. This script performs retrieval only; the prose below is the separately generated answer.

## Generated recommendation

**Start with Scrapling's parser and adaptive selectors.** Its adaptive-scraping documentation describes tracking and relocating elements when a site's structure changes, which directly matches the requirement. The retrieved skill also describes using its parser without fetching a website. [Adaptive selector evidence](https://github.com/D4Vinci/Scrapling/blob/971d5edb9c01f000dd4befcd21742e9b22260dc7/docs/parsing/adaptive.md#L1-L42), [parser evidence](https://github.com/D4Vinci/Scrapling/blob/971d5edb9c01f000dd4befcd21742e9b22260dc7/agent-skill/Scrapling-Skill/SKILL.md#L333-L368).

The reviewed catalog requires Python 3.10 or newer. Core parsing and browser fetching have different dependencies; browser fetchers need additional browser/system setup. The evidence bundle reports Scrapling as source-only on the retrieval host; this does not establish that its runtime is installed. Read its complete setup guide and selected skill, then verify against a saved HTML fixture. Evidence: `catalog-f30f0ef50add3d73` in the [recorded bundle](../reviews/rag-demo-evidence.json).

Firecrawl is an alternative for a broader scraping service. Its reviewed hosted setup requires an account/API key, while self-hosting introduces a Docker stack. Those prerequisites add work for this local parsing request. Browser Harness centers on controlling a Chrome session over CDP; its retrieved examples do not establish an adaptive-selector capability. Based on the supplied evidence, neither is my first choice for this requirement. Evidence: `catalog-025818587bbabf1b` and `catalog-21d41d6202b73a49` in the [recorded bundle](../reviews/rag-demo-evidence.json).

## Evidence review

| Claim | Supporting source ID | Check |
| --- | --- | --- |
| Adaptive selectors address changing layouts | `passage-fb93baf252c18876` | Retrieved documentation explicitly describes element relocation. |
| Parser can be used separately from website fetching | `passage-1aea88cca7d5df0b` | Retrieved skill introduces direct parser use. |
| Python/setup requirements | `catalog-f30f0ef50add3d73` | Checked against the catalog projection; host availability is reported separately on the candidate. |
| Firecrawl requires hosted credentials or a local service stack | `catalog-025818587bbabf1b` | Checked against reviewed requirements. |
| Browser Harness requires Chrome/CDP or its cloud option | `catalog-21d41d6202b73a49` | Checked against reviewed requirements. |

The two cited Scrapling files were verified against the recorded Git commit blobs. The recommendation's preference is the agent's judgment from the supplied requirements and evidence, not a retrieval score interpreted as confidence.

No website was fetched, runtime installed, account accessed, or repository instructions executed during this example. This is one inspected answer, not an automated faithfulness benchmark or a claim of installation success.
