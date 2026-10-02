# ast-grep

Tree-sitter based structural code search, YAML lint rules and AST-aware rewrites, with Rust CLI and Node.js/Python programmatic bindings.

[Upstream repository](https://github.com/ast-grep/ast-grep) · [Pinned source](https://github.com/ast-grep/ast-grep/tree/25334496c105c9c728f0a6024f3d164aed40cacc) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Engineering and code intelligence |
| Operating model | cli |
| Recommended scope | global-cli |
| Registered production skill paths | 0 |
| Reviewed source commit | `25334496c105c9c728f0a6024f3d164aed40cacc` |

## Purpose and use cases

Use precise syntax patterns for refactors, migrations and custom linting beyond text search. Read matches before applying rewrites; prefer the ast-grep executable because sg can conflict with the system group command. This source repo has no production Agent Skills; detailed guides live on the linked official site.

**Discovery tags:** `ast`, `structural search`, `codemod`, `rewrite`, `lint`, `tree-sitter`, `static analysis`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Reviewed version 0.45.3. npm CLI package declares Node.js >=12 and supplies platform-specific native binaries; Python wheel or standalone binaries are alternatives.
- Building the Rust source requires Rust >=1.88.0 and Cargo (edition 2024); installation from supported binary packages avoids a source build.
- No account/API key required for local structural search, linting or rewriting; project YAML config/rules are optional.

## Setup guidance

**Setup scope:** shared installed CLI; optional project rules

**Next action:** setup-required

**Working directory:** Read pinned sources in place. Use a separate runtime working copy or the selected target project for installations and generated files.

**Installation approach:** Use the pinned upstream documentation and choose one suitable route from install_commands. Lists can include alternatives, registration and launch commands; do not execute the entire list. Check for an existing compatible runtime before installing.

**Configuration:** Install a compatible ast-grep CLI using one documented route, then use it in the target project. Project YAML rules are optional; the CLI does not require a package in each project.

**Verification to perform:** ast-grep --version; test a structural match on a small fixture before a rewrite.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read ast-grep README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npm install --global @ast-grep/cli@0.45.3
```

Example 2:

```bash
pip install ast-grep-cli==0.45.3
```

Example 3:

```bash
cargo install ast-grep --version 0.45.3 --locked
```

## Source entry points

- [README.md](https://github.com/ast-grep/ast-grep/blob/25334496c105c9c728f0a6024f3d164aed40cacc/README.md)
- [npm/README.md](https://github.com/ast-grep/ast-grep/blob/25334496c105c9c728f0a6024f3d164aed40cacc/npm/README.md)
- [npm/package.json](https://github.com/ast-grep/ast-grep/blob/25334496c105c9c728f0a6024f3d164aed40cacc/npm/package.json)
- [Cargo.toml](https://github.com/ast-grep/ast-grep/blob/25334496c105c9c728f0a6024f3d164aed40cacc/Cargo.toml)
- [pyproject.toml](https://github.com/ast-grep/ast-grep/blob/25334496c105c9c728f0a6024f3d164aed40cacc/pyproject.toml)
- [crates/napi/README.md](https://github.com/ast-grep/ast-grep/blob/25334496c105c9c728f0a6024f3d164aed40cacc/crates/napi/README.md)
- [crates/pyo3/README.md](https://github.com/ast-grep/ast-grep/blob/25334496c105c9c728f0a6024f3d164aed40cacc/crates/pyo3/README.md)
- [schemas/rule.json](https://github.com/ast-grep/ast-grep/blob/25334496c105c9c728f0a6024f3d164aed40cacc/schemas/rule.json)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show ast-grep
bin/toolkit search "ast structural search" --repo ast-grep
bin/toolkit docs ast-grep "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [ast-grep/ast-grep at `25334496c105`](https://github.com/ast-grep/ast-grep/tree/25334496c105c9c728f0a6024f3d164aed40cacc). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo ast-grep --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
