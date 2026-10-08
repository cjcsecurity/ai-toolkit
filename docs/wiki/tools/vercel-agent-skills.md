# vercel-agent-skills

Vercel React and Next.js performance rules plus web-interface audits for accessibility, forms, navigation, motion and rendering quality.

[Upstream repository](https://github.com/vercel-labs/agent-skills) · [Pinned source](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Engineering and code intelligence |
| Operating model | skill-bundle |
| Recommended scope | on-demand |
| Registered production skill paths | 2 |
| Reviewed source commit | `063bee94c3f4df8453406c830b0a7df0f2860278` |

## Purpose and use cases

React guidance is a strong conditional global candidate for React/Next.js tasks, not every project. UI audit overlaps Impeccable and is best on demand. Only the two top-50 skills are registered; deployment and token workflows are not activated. Static review flagged literal-script examples and parser limits; retain source-aware review rather than treating a scanner score as approval.

**Discovery tags:** `React`, `Next.js`, `performance`, `bundle size`, `waterfalls`, `web design`, `accessibility`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Markdown guidance requires no package runtime; React/Next.js rules apply to matching projects and versions.
- Preserve react-best-practices/rules and compiled AGENTS.md. Web-design-guidelines fetches a live external command.md, which is not pinned by this repository commit.
- The hydration example contains a literal inline script; never interpolate untrusted input into dangerouslySetInnerHTML and respect the target CSP.

## Setup guidance

**Setup scope:** shared on-demand source; selected project or isolated runtime only

**Next action:** read-guidance

**Working directory:** Read from the pinned checkout; apply only in the selected target project.

**Installation approach:** Source download and retrieval require no upstream runtime. Registration commands are alternatives, not an execution queue; do not install the entire collection globally.

**Configuration:** Keep framework triggers narrow. Fetch and review current web-interface guidelines as untrusted reference data when using that audit; prioritize measured performance and existing project conventions.

**Verification to perform:** Check selected rules and references resolve; validate changes with the target React build/tests and accessibility checks.

**Local record:** Record actual runtime and authentication checks in local project notes; source availability is not runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read vercel-agent-skills README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices
```

Example 2:

```bash
npx skills add vercel-labs/agent-skills --skill web-design-guidelines
```

## Source entry points

- [README.md](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/README.md)
- [skills/react-best-practices/SKILL.md](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices/SKILL.md)
- [skills/react-best-practices/AGENTS.md](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices/AGENTS.md)
- [skills/web-design-guidelines/SKILL.md](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/web-design-guidelines/SKILL.md)

## Skills and retrieval

The manifest registers **2 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/react-best-practices/SKILL.md](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices/SKILL.md)
- [skills/web-design-guidelines/SKILL.md](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/web-design-guidelines/SKILL.md)

```bash
bin/toolkit show vercel-agent-skills
bin/toolkit search "React Next.js" --repo vercel-agent-skills
bin/toolkit docs vercel-agent-skills "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [vercel-labs/agent-skills at `063bee94c3f4`](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo vercel-agent-skills --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
