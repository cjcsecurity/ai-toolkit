# cyberstrike

AI security-assessment harness with terminal/web interfaces, specialized agents, a large on-demand skill collection including CIS/NIST/MITRE controls, integrated browser testing, and optional remote/MCP tools.

[Upstream repository](https://github.com/CyberStrikeus/CyberStrike) · [Pinned source](https://github.com/CyberStrikeus/CyberStrike/tree/04f4575961083759411a5c0466dd18902a7259dd) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Security and assessment |
| Operating model | application |
| Recommended scope | on-demand |
| Registered production skill paths | 7,689 |
| Reviewed source commit | `04f4575961083759411a5c0466dd18902a7259dd` |

## Purpose and use cases

Explicit user selection; complementary assessment harness and searchable control-level methods. Keep its extensive skills and provider/MCP integrations on demand. The earlier 5k-star filter applied to discovery suggestions; this explicitly requested repository had 2919 stars at review.

**Discovery tags:** `security assessment`, `pentest`, `CIS benchmarks`, `NIST controls`, `MITRE ATT&CK`, `OWASP`, `compliance auditing`, `security skills`, `MCP`, `browser testing`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Published CLI: compatible npm/Node installation or another documented platform package; source development uses the repository-pinned Bun 1.3.9 monorepo toolchain. The source package reports 1.1.16; published runtime versions must be checked separately.
- A configured LLM provider/API key or upstream-supported authenticated provider connection; account access and usage limits depend on the provider.
- HackBrowser requires its browser/runtime dependencies and selected test sessions. Optional Bolt remote execution requires separately deployed servers and pairing; external MCP services have independent prerequisites.
- The bundled Markdown methods can be read without installing the harness. Running an assessment requires the user-authorized target and configuration.

## Setup guidance

**Setup scope:** shared assessment CLI or isolated application runtime; per-task provider, target and optional integrations

**Next action:** setup-required

**Working directory:** Use an isolated shared runtime or a working copy under runtime/cyberstrike; preserve the pinned source checkout. Target configuration belongs to the selected project.

**Installation approach:** Choose one documented install route from install_commands and pin its version. These are setup references, not a script to run in full. Reuse any subsequently installed runtime first.

**Configuration:** Choose the packaged CLI route and pin the selected release. Configure the model provider first; add browser, Bolt or MCP integrations only when the selected task requires them. Reading an individual skill does not require installing the harness.

**Verification to perform:** Check the installed CLI help/version and provider configuration. Verify optional browser/remote connectivity separately; do not treat a launched UI as proof of a completed assessment.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read cyberstrike README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npm install -g @cyberstrike-io/cyberstrike@latest
```

Example 2:

```bash
bun add -g @cyberstrike-io/cyberstrike@latest
```

## Source entry points

- [README.md](https://github.com/CyberStrikeus/CyberStrike/blob/04f4575961083759411a5c0466dd18902a7259dd/README.md)
- [package.json](https://github.com/CyberStrikeus/CyberStrike/blob/04f4575961083759411a5c0466dd18902a7259dd/package.json)
- [packages/cyberstrike/package.json](https://github.com/CyberStrikeus/CyberStrike/blob/04f4575961083759411a5c0466dd18902a7259dd/packages/cyberstrike/package.json)
- [.cyberstrike/skill/CIS_benchmarks/README.md](https://github.com/CyberStrikeus/CyberStrike/blob/04f4575961083759411a5c0466dd18902a7259dd/.cyberstrike/skill/CIS_benchmarks/README.md)
- [docs/skill-signing.md](https://github.com/CyberStrikeus/CyberStrike/blob/04f4575961083759411a5c0466dd18902a7259dd/docs/skill-signing.md)

## Skills and retrieval

The manifest registers **7,689 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.1.1/SKILL.md](https://github.com/CyberStrikeus/CyberStrike/blob/04f4575961083759411a5c0466dd18902a7259dd/.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.1.1/SKILL.md)
- [.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.1.2/SKILL.md](https://github.com/CyberStrikeus/CyberStrike/blob/04f4575961083759411a5c0466dd18902a7259dd/.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.1.2/SKILL.md)
- [.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.1.3/SKILL.md](https://github.com/CyberStrikeus/CyberStrike/blob/04f4575961083759411a5c0466dd18902a7259dd/.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.1.3/SKILL.md)
- [.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.1.4/SKILL.md](https://github.com/CyberStrikeus/CyberStrike/blob/04f4575961083759411a5c0466dd18902a7259dd/.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.1.4/SKILL.md)
- [.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.1.5/SKILL.md](https://github.com/CyberStrikeus/CyberStrike/blob/04f4575961083759411a5c0466dd18902a7259dd/.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.1.5/SKILL.md)
- [.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.1.6/SKILL.md](https://github.com/CyberStrikeus/CyberStrike/blob/04f4575961083759411a5c0466dd18902a7259dd/.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.1.6/SKILL.md)
- [.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.10/SKILL.md](https://github.com/CyberStrikeus/CyberStrike/blob/04f4575961083759411a5c0466dd18902a7259dd/.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.10/SKILL.md)
- [.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.11/SKILL.md](https://github.com/CyberStrikeus/CyberStrike/blob/04f4575961083759411a5c0466dd18902a7259dd/.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.11/SKILL.md)
- [.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.12/SKILL.md](https://github.com/CyberStrikeus/CyberStrike/blob/04f4575961083759411a5c0466dd18902a7259dd/.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.12/SKILL.md)
- [.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.13/SKILL.md](https://github.com/CyberStrikeus/CyberStrike/blob/04f4575961083759411a5c0466dd18902a7259dd/.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.13/SKILL.md)
- [.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.14/SKILL.md](https://github.com/CyberStrikeus/CyberStrike/blob/04f4575961083759411a5c0466dd18902a7259dd/.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.14/SKILL.md)
- [.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.15/SKILL.md](https://github.com/CyberStrikeus/CyberStrike/blob/04f4575961083759411a5c0466dd18902a7259dd/.cyberstrike/skill/CIS_benchmarks/Cloud_Providers/AWS/cis-amazon-web-services-foundations/cis-aws-foundations-2.15/SKILL.md)

Showing 12 of 7,689 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show cyberstrike
bin/toolkit search "security assessment pentest" --repo cyberstrike
bin/toolkit docs cyberstrike "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [CyberStrikeus/CyberStrike at `04f457596108`](https://github.com/CyberStrikeus/CyberStrike/tree/04f4575961083759411a5c0466dd18902a7259dd). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo cyberstrike --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
