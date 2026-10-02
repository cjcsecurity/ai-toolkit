# gh-aw

GitHub CLI extension for defining AI repository automation in Markdown and compiling it to GitHub Actions with scoped permissions and validated safe outputs.

[Upstream repository](https://github.com/github/gh-aw) · [Pinned source](https://github.com/github/gh-aw/tree/35eb607ae44d32b6e6bc21350330c9a8e57e8b38) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Engineering and code intelligence |
| Operating model | cli |
| Recommended scope | project-local |
| Registered production skill paths | 5 |
| Reviewed source commit | `35eb607ae44d32b6e6bc21350330c9a8e57e8b38` |

## Purpose and use cases

Install the gh-aw extension once; author and compile workflows in selected repositories, with project-specific engine authentication, Actions permissions and deployment review. Adds reasoning-driven repository automation alongside deterministic CI. Docs source at docs/src/content/docs includes Markdown and MDX. Retain only workflow product skills; exclude squad templates, generic/internal engineering, developer release and fixture guidance. Root skill is a thin installation/router entry; choose specific workflow skills on demand.

**Discovery tags:** `github actions`, `agentic workflows`, `repository automation`, `workflow compiler`, `safe outputs`, `ci`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- One-time CLI: GitHub CLI gh >=2.0.0 and gh-aw extension; Linux, macOS or Windows with WSL. Published extension installation does not require Go. Source build only requires Go 1.26.8 per go.mod.
- Per repository: GitHub Actions enabled, appropriate repository access and authenticated gh for repository/run operations; Markdown workflows plus generated .lock.yml files.
- Selected AI engine requires its own account and repository secrets/credentials (Copilot, Claude, Codex, Gemini or Pi provider). Compile/reading source is distinct from deploying or running workflows.
- Review generated Actions configuration, scoped permissions, tools, network policy and safe outputs before committing/deploying automation. No auth or repository deployment changes performed by library addition.

## Setup guidance

**Setup scope:** shared gh extension; per-repository workflow configuration

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Install the extension once, then author/compile workflows in the target repository. Engine secrets and Actions deployment are separate from local compilation.

**Verification to perform:** Check extension help/version and compile a sample workflow; inspect generated Actions before deployment.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read gh-aw install.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
gh extension install github/gh-aw
```

Example 2:

```bash
gh aw compile
```

## Source entry points

- [README.md](https://github.com/github/gh-aw/blob/35eb607ae44d32b6e6bc21350330c9a8e57e8b38/README.md)
- [install.md](https://github.com/github/gh-aw/blob/35eb607ae44d32b6e6bc21350330c9a8e57e8b38/install.md)
- [create.md](https://github.com/github/gh-aw/blob/35eb607ae44d32b6e6bc21350330c9a8e57e8b38/create.md)
- [SKILL.md](https://github.com/github/gh-aw/blob/35eb607ae44d32b6e6bc21350330c9a8e57e8b38/SKILL.md)
- [docs/src/content/docs/setup/quick-start.mdx](https://github.com/github/gh-aw/blob/35eb607ae44d32b6e6bc21350330c9a8e57e8b38/docs/src/content/docs/setup/quick-start.mdx)
- [docs/src/content/docs/reference](https://github.com/github/gh-aw/tree/35eb607ae44d32b6e6bc21350330c9a8e57e8b38/docs/src/content/docs/reference)
- [go.mod](https://github.com/github/gh-aw/blob/35eb607ae44d32b6e6bc21350330c9a8e57e8b38/go.mod)
- [.github/aw/github-agentic-workflows.md](https://github.com/github/gh-aw/blob/35eb607ae44d32b6e6bc21350330c9a8e57e8b38/.github/aw/github-agentic-workflows.md)

## Skills and retrieval

The manifest registers **5 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [SKILL.md](https://github.com/github/gh-aw/blob/35eb607ae44d32b6e6bc21350330c9a8e57e8b38/SKILL.md)
- [.github/skills/agentic-workflows/SKILL.md](https://github.com/github/gh-aw/blob/35eb607ae44d32b6e6bc21350330c9a8e57e8b38/.github/skills/agentic-workflows/SKILL.md)
- [.github/skills/debugging-workflows/SKILL.md](https://github.com/github/gh-aw/blob/35eb607ae44d32b6e6bc21350330c9a8e57e8b38/.github/skills/debugging-workflows/SKILL.md)
- [.github/skills/optimize-agentic-workflow/SKILL.md](https://github.com/github/gh-aw/blob/35eb607ae44d32b6e6bc21350330c9a8e57e8b38/.github/skills/optimize-agentic-workflow/SKILL.md)
- [.github/skills/review-agentic-workflows/SKILL.md](https://github.com/github/gh-aw/blob/35eb607ae44d32b6e6bc21350330c9a8e57e8b38/.github/skills/review-agentic-workflows/SKILL.md)

```bash
bin/toolkit show gh-aw
bin/toolkit search "github actions agentic workflows" --repo gh-aw
bin/toolkit docs gh-aw "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [github/gh-aw at `35eb607ae44d`](https://github.com/github/gh-aw/tree/35eb607ae44d32b6e6bc21350330c9a8e57e8b38). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo gh-aw --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
