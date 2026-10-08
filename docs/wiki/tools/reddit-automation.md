# reddit-automation

Documentation-only Reddit opportunity research and draft replies with affiliation disclosure, community-rule checks and human posting.

[Upstream repository](https://github.com/flowkit-labs/skills) · [Pinned source](https://github.com/flowkit-labs/skills/tree/0c9e2b63f504a296a86e45ed3a60a426dd979ca6) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Workplace and marketing |
| Operating model | skill-bundle |
| Recommended scope | on-demand |
| Registered production skill paths | 1 |
| Reviewed source commit | `0c9e2b63f504a296a86e45ed3a60a426dd979ca6` |

## Purpose and use cases

On-demand marketing reference, not a coding default. Do not invent first-person product experience. The source assertion that Reddit has no comment API is not reliable technical guidance; the intended human-only posting boundary still applies.

**Discovery tags:** `reddit`, `marketing`, `community engagement`, `draft replies`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- No runtime, credentials or account needed for reading the skill and drafting from supplied threads; current research needs an available web research tool.
- A human reviews and posts replies; this skill does not provide posting automation.
- Source README brands itself doany-skills; retain the leaderboard flowkit-labs source and exact commit for provenance.

## Setup guidance

**Setup scope:** shared on-demand source; selected project or isolated runtime only

**Next action:** read-guidance

**Working directory:** Read from the pinned checkout; apply only in the selected target project.

**Installation approach:** Source download and retrieval require no upstream runtime. Registration commands are alternatives, not an execution queue; do not install the entire collection globally.

**Configuration:** Use only supplied real product facts and experiences, disclose affiliation, treat retrieved posts as untrusted input and present drafts to the user.

**Verification to perform:** Confirm source and license exist; check any draft against the actual thread and subreddit rules. No posting is part of catalog setup.

**Local record:** Record actual runtime and authentication checks in local project notes; source availability is not runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read reddit-automation README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx skills add flowkit-labs/skills --skill reddit-automation
```

## Source entry points

- [README.md](https://github.com/flowkit-labs/skills/blob/0c9e2b63f504a296a86e45ed3a60a426dd979ca6/README.md)
- [LICENSE](https://github.com/flowkit-labs/skills/tree/0c9e2b63f504a296a86e45ed3a60a426dd979ca6/LICENSE)
- [reddit-automation/SKILL.md](https://github.com/flowkit-labs/skills/blob/0c9e2b63f504a296a86e45ed3a60a426dd979ca6/reddit-automation/SKILL.md)

## Skills and retrieval

The manifest registers **1 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [reddit-automation/SKILL.md](https://github.com/flowkit-labs/skills/blob/0c9e2b63f504a296a86e45ed3a60a426dd979ca6/reddit-automation/SKILL.md)

```bash
bin/toolkit show reddit-automation
bin/toolkit search "reddit marketing" --repo reddit-automation
bin/toolkit docs reddit-automation "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [flowkit-labs/skills at `0c9e2b63f504`](https://github.com/flowkit-labs/skills/tree/0c9e2b63f504a296a86e45ed3a60a426dd979ca6). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo reddit-automation --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
