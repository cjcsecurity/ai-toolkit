# public-apis

Curated catalog of public APIs organized by topic, with descriptions and authentication, HTTPS, and CORS information.

[Upstream repository](https://github.com/public-apis/public-apis) · [Pinned source](https://github.com/public-apis/public-apis/tree/8939d468fa4580039c4e22cc4998eb3fef8130d1) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Browsers, research, and web data |
| Operating model | reference |
| Recommended scope | reference |
| Registered production skill paths | 0 |
| Reviewed source commit | `8939d468fa4580039c4e22cc4998eb3fef8130d1` |

## Purpose and use cases

Searchable reference needs no runtime installation; evaluate each selected API separately.

**Discovery tags:** `reference`, `research`, `api-discovery`, `public-data`, `open-data`, `integration`, `datasets`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- No dependencies or login needed to read the local catalog.
- Individual API providers may require registration, API keys, payment, or separate usage terms.

## Setup guidance

**Setup scope:** reference only; no installation

**Next action:** read-selected-reference

**Working directory:** Read from the stored checkout; install only selected task dependencies in an isolated environment or the target project.

**Installation approach:** None: this is a reference catalog, not an installable runtime.

**Configuration:** Read the catalog. Each selected external API has its own credentials, SDK and usage requirements.

**Verification to perform:** Check the selected provider's documentation and a read-only test request if the task needs live access.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read public-apis README.md
```

### Documented commands and alternatives

No package installation command is recorded. Follow the setup guidance and pinned upstream instructions; source-only guidance may need no runtime.

## Source entry points

- [README.md](https://github.com/public-apis/public-apis/blob/8939d468fa4580039c4e22cc4998eb3fef8130d1/README.md)
- [CONTRIBUTING.md](https://github.com/public-apis/public-apis/blob/8939d468fa4580039c4e22cc4998eb3fef8130d1/CONTRIBUTING.md)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show public-apis
bin/toolkit search "reference research" --repo public-apis
bin/toolkit docs public-apis "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [public-apis/public-apis at `8939d468fa45`](https://github.com/public-apis/public-apis/tree/8939d468fa4580039c4e22cc4998eb3fef8130d1). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo public-apis --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
