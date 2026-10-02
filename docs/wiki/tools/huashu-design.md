# huashu-design

Chinese-language design skill for HTML prototypes, slide decks, animation, data visualization, critique, and local PDF/PPTX/video export, with bundled templates and scripts.

[Upstream repository](https://github.com/alchaincyf/huashu-design) · [Pinned source](https://github.com/alchaincyf/huashu-design/tree/0830494ecb1c117e25b313a8114fe55a6bf2b125) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Design and interfaces |
| Operating model | skill-bundle |
| Recommended scope | on-demand |
| Registered production skill paths | 1 |
| Reviewed source commit | `0830494ecb1c117e25b313a8114fe55a6bf2b125` |

## Purpose and use cases

Read root SKILL.md for matching prototype/deck tasks and preserve the full repository as skill base, including references/assets/scripts/demos. Codex-compatible Markdown, but workflow mandates three visual drafts before selection and is broader than a default UI skill; keep optional.

**Discovery tags:** `design`, `prototype`, `slides`, `pptx`, `pdf`, `html`, `animation`, `chinese`, `huashu`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Core design guidance is Markdown; export scripts need their documented local runtime/toolchain.
- package.json lists Playwright, pdf-lib, pptxgenjs, and sharp; browser setup and FFmpeg/Python are needed by applicable exporters.
- Optional cloud narration/review uses provider API keys; core local design/export does not require them.
- Main skill and detailed references are primarily Chinese; README.en.md provides English overview.

## Setup guidance

**Setup scope:** read selected skill; optional isolated export runtime

**Next action:** read-selected-reference

**Working directory:** Read from the stored checkout; install only selected task dependencies in an isolated environment or the target project.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Read the core skill/references directly. Install the selected PDF/PPTX/video exporter dependencies in a working copy only when exporting.

**Verification to perform:** Confirm references load; for an exporter, render a small sample and check its output file.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read huashu-design README.en.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx skills add alchaincyf/huashu-design
```

## Source entry points

- [README.en.md](https://github.com/alchaincyf/huashu-design/blob/0830494ecb1c117e25b313a8114fe55a6bf2b125/README.en.md)
- [SKILL.md](https://github.com/alchaincyf/huashu-design/blob/0830494ecb1c117e25b313a8114fe55a6bf2b125/SKILL.md)
- [SECURITY.md](https://github.com/alchaincyf/huashu-design/blob/0830494ecb1c117e25b313a8114fe55a6bf2b125/SECURITY.md)
- [package.json](https://github.com/alchaincyf/huashu-design/blob/0830494ecb1c117e25b313a8114fe55a6bf2b125/package.json)

## Skills and retrieval

The manifest registers **1 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [SKILL.md](https://github.com/alchaincyf/huashu-design/blob/0830494ecb1c117e25b313a8114fe55a6bf2b125/SKILL.md)

```bash
bin/toolkit show huashu-design
bin/toolkit search "design prototype" --repo huashu-design
bin/toolkit docs huashu-design "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [alchaincyf/huashu-design at `0830494ecb1c`](https://github.com/alchaincyf/huashu-design/tree/0830494ecb1c117e25b313a8114fe55a6bf2b125). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo huashu-design --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
