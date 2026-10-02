# open-code-review

Go-based code review CLI combining deterministic Git diff selection, file grouping and review rules with model-backed line-level findings, full-file scans and host-agent delegation without a separate OCR LLM endpoint.

[Upstream repository](https://github.com/alibaba/open-code-review) · [Pinned source](https://github.com/alibaba/open-code-review/tree/a758d9cbfb689937c7857ad64b2dd66adb58c0c2) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Engineering and code intelligence |
| Operating model | cli |
| Recommended scope | on-demand |
| Registered production skill paths | 2 |
| Reviewed source commit | `a758d9cbfb689937c7857ad64b2dd66adb58c0c2` |

## Purpose and use cases

Adds a focused review engine and two canonical portable skills complementary to the existing engineering workflow. Plugin copies of those two skills are also tracked and may be indexed as variants. Keep runtime setup separate from source availability and load the selected review mode on demand.

**Discovery tags:** `code review`, `Git diff review`, `line-level findings`, `review rules`, `host-agent delegation`, `SARIF`, `full-file scanning`, `CI review`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Git >=2.41 is required. Release binaries support Linux, macOS and Windows on x64/amd64 and arm64.
- The npm launcher requires Node.js >=14 and uses platform binaries or a release download with checksums; its postinstall executes scripts/install.js. A source build needs the Go 1.25.5 toolchain declared by go.mod and Make.
- OCR-managed reviews need a configured supported provider/model and credentials or compatible endpoint: Anthropic, OpenAI Chat Completions, OpenAI Responses or AWS Bedrock.
- Delegation mode requires the OCR CLI and host agent but no OCR model endpoint or OCR API key. Git diffs and project rules still need access to the selected target project.
- Project rules may live in .opencodereview/rule.json; user configuration and rules may live under ~/.opencodereview. CI posting and repository integrations need separately configured credentials and task authorization.

## Setup guidance

**Setup scope:** shared isolated review CLI; per-project review rules and optional model/client/CI integration

**Next action:** setup-required

**Working directory:** Use an isolated runtime or a working copy under runtime/open-code-review; preserve the pinned source checkout. Run project operations in the selected target project.

**Installation approach:** Choose one reviewed upstream route: npm package/release binary, or make build from a working copy of the pinned revision under runtime/open-code-review. The README global npm command is a reference; pin a reviewed package release and use an isolated prefix when preparing shared toolkit runtime. make build writes dist/opencodereview; expose a deliberate ocr launcher if using the source route. Do not use package.json version 0.0.0 as a published release version.

**Configuration:** Choose OCR-managed review or host-agent delegation. Managed mode uses ocr config provider, ocr config model and provider credentials. Delegation does not require OCR credentials. Keep target rules in the project; client plugins are optional and should not be globally registered just for retrieval.

**Verification to perform:** After installation check CLI help/version and Git compatibility. Verify delegation with ocr delegate preview --format json in the selected project without an LLM request. Managed mode additionally uses ocr llm test once configured. For an actual requested review inspect exit status, warnings, coverage/skipped files and saved findings.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read open-code-review README.md
toolkit read open-code-review plugins/open-code-review/README.md
toolkit read open-code-review skills/open-code-review-delegate/SKILL.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npm install -g @alibaba-group/open-code-review
```

Example 2:

```bash
make build
```

## Source entry points

- [README.md](https://github.com/alibaba/open-code-review/blob/a758d9cbfb689937c7857ad64b2dd66adb58c0c2/README.md)
- [plugins/open-code-review/README.md](https://github.com/alibaba/open-code-review/blob/a758d9cbfb689937c7857ad64b2dd66adb58c0c2/plugins/open-code-review/README.md)
- [skills/open-code-review-delegate/SKILL.md](https://github.com/alibaba/open-code-review/blob/a758d9cbfb689937c7857ad64b2dd66adb58c0c2/skills/open-code-review-delegate/SKILL.md)
- [skills/open-code-review/SKILL.md](https://github.com/alibaba/open-code-review/blob/a758d9cbfb689937c7857ad64b2dd66adb58c0c2/skills/open-code-review/SKILL.md)
- [package.json](https://github.com/alibaba/open-code-review/blob/a758d9cbfb689937c7857ad64b2dd66adb58c0c2/package.json)
- [go.mod](https://github.com/alibaba/open-code-review/blob/a758d9cbfb689937c7857ad64b2dd66adb58c0c2/go.mod)
- [CONTRIBUTING.md](https://github.com/alibaba/open-code-review/blob/a758d9cbfb689937c7857ad64b2dd66adb58c0c2/CONTRIBUTING.md)
- [Makefile](https://github.com/alibaba/open-code-review/blob/a758d9cbfb689937c7857ad64b2dd66adb58c0c2/Makefile)

## Skills and retrieval

The manifest registers **2 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/open-code-review-delegate/SKILL.md](https://github.com/alibaba/open-code-review/blob/a758d9cbfb689937c7857ad64b2dd66adb58c0c2/skills/open-code-review-delegate/SKILL.md)
- [skills/open-code-review/SKILL.md](https://github.com/alibaba/open-code-review/blob/a758d9cbfb689937c7857ad64b2dd66adb58c0c2/skills/open-code-review/SKILL.md)

```bash
bin/toolkit show open-code-review
bin/toolkit search "code review Git diff review" --repo open-code-review
bin/toolkit docs open-code-review "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [alibaba/open-code-review at `a758d9cbfb68`](https://github.com/alibaba/open-code-review/tree/a758d9cbfb689937c7857ad64b2dd66adb58c0c2). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo open-code-review --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
