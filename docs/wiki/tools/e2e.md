# e2e

TypeScript end-to-end test runner combining natural-language agent actions with deterministic assertions for web and mobile applications.

[Upstream repository](https://github.com/tester-army/e2e) · [Pinned source](https://github.com/tester-army/e2e/tree/fd3a0c766b4d40c74fabdbc578e3832d80553bf9) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Engineering and code intelligence |
| Operating model | framework + cli + skill |
| Recommended scope | on-demand |
| Registered production skill paths | 1 |
| Reviewed source commit | `fd3a0c766b4d40c74fabdbc578e3832d80553bf9` |

## Purpose and use cases

Test user journeys using Playwright or mobile simulators; verified agent actions can replay without model calls until the application changes.

**Discovery tags:** `testing`, `e2e`, `web`, `mobile`, `playwright`, `agent-testing`, `mcp`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Node.js ^22.22.3 or >=24.8.0; Windows uses WSL. Install the e2e SDK and the selected web or mobile engine in the target project.
- Web testing uses Playwright and its browser dependencies. Mobile testing needs Xcode and an iOS simulator, or the Android SDK and an emulator.
- Agent steps require a supported subscription login, API provider credentials or local model; deterministic tests need no model. Hosted browsers/simulators are optional services.
- CLI telemetry is enabled by default; E2E_TELEMETRY_DISABLED=1 or npx e2e telemetry disable opts out.
- Apache-2.0; pre-1.0 APIs and configuration can change between minor releases.

## Setup guidance

**Setup scope:** project-local or isolated tool runtime; explicit agent registration

**Next action:** setup-required

**Working directory:** An isolated tool checkout or the selected target project, according to the pinned setup guide.

**Installation approach:** Reuse a compatible runtime first. Select one documented installation route, review dependencies and pin the version; commands are examples, not a script to execute in order.

**Configuration:** Choose web or mobile, set the application target and configure a model only for agent steps; review generated configuration and telemetry preferences.

**Verification to perform:** Run the generated example against the selected local application, then verify one meaningful user flow and its assertions.

**Local record:** Record the actual runtime version, checks and remaining requirements locally. Catalog/source presence does not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read e2e README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx e2e init
```

## Source entry points

- [README.md](https://github.com/tester-army/e2e/blob/fd3a0c766b4d40c74fabdbc578e3832d80553bf9/README.md)
- [docs/quickstart.mdx](https://github.com/tester-army/e2e/blob/fd3a0c766b4d40c74fabdbc578e3832d80553bf9/docs/quickstart.mdx)
- [docs/telemetry.mdx](https://github.com/tester-army/e2e/blob/fd3a0c766b4d40c74fabdbc578e3832d80553bf9/docs/telemetry.mdx)
- [packages/e2e/package.json](https://github.com/tester-army/e2e/blob/fd3a0c766b4d40c74fabdbc578e3832d80553bf9/packages/e2e/package.json)
- [skills/e2e/SKILL.md](https://github.com/tester-army/e2e/blob/fd3a0c766b4d40c74fabdbc578e3832d80553bf9/skills/e2e/SKILL.md)

## Skills and retrieval

The manifest registers **1 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/e2e/SKILL.md](https://github.com/tester-army/e2e/blob/fd3a0c766b4d40c74fabdbc578e3832d80553bf9/skills/e2e/SKILL.md)

```bash
bin/toolkit show e2e
bin/toolkit search "testing e2e" --repo e2e
bin/toolkit docs e2e "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [tester-army/e2e at `fd3a0c766b4d`](https://github.com/tester-army/e2e/tree/fd3a0c766b4d40c74fabdbc578e3832d80553bf9). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo e2e --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
