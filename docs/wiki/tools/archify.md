# archify

Diagram-authoring skill and Node.js renderer producing validated standalone interactive HTML/SVG for architecture, workflows, sequences, data flow and lifecycles from typed JSON, with repository evidence and image/video exports.

[Upstream repository](https://github.com/tt-a1i/archify) · [Pinned source](https://github.com/tt-a1i/archify/tree/d5a1333d7447c866a765adac7d4d062f2f02e4d2) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Design and interfaces |
| Operating model | skill-bundle |
| Recommended scope | on-demand |
| Registered production skill paths | 1 |
| Reviewed source commit | `d5a1333d7447c866a765adac7d4d062f2f02e4d2` |

## Purpose and use cases

Adds a specialized diagram workflow and its complete bundled renderer/templates/schemas. The delivered production skill is archify/SKILL.md; .agents/skills/archify-review is an internal project-maintenance skill and is excluded from the declared production count, though corpus discovery may still index it. Keep the full package layout available on demand without a global skill installation.

**Discovery tags:** `architecture diagrams`, `workflow diagrams`, `sequence diagrams`, `data flow`, `state machines`, `interactive HTML`, `SVG`, `diagram validation`, `source evidence`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Node.js >=18 is required by archify/package.json (version 3.0.1). Packaged rendering/validation uses bundled validators and does not require npm install inside the skill package.
- The required finalize browser-evidence gate needs accessible Chrome or Chromium; ARCHIFY_CHROME can select its executable. Browser readiness has not been tested by source review.
- No Archify account or hosted service is required for local authoring/viewing. A capable host agent and shell access are needed for the full renderer workflow; Claude.ai sandbox capability depends on Node access.
- Keep archify/ assets, bin, renderers, schemas, examples and references together. Repository-backed evidence needs the selected repository and exact source revision.
- Optional update awareness makes a bounded GET of the stable manifest and writes reminder state; ARCHIFY_UPDATE_CHECK_DISABLED=1 disables that networking and state. External links and certain exported/viewer features depend on normal browser capabilities.

## Setup guidance

**Setup scope:** on-demand skill and isolated Node renderer; target-project diagram artifacts and browser checks

**Next action:** setup-required

**Working directory:** Use an isolated runtime or a working copy under runtime/archify; preserve the pinned source checkout. Run project operations in the selected target project.

**Installation approach:** No package installation is required by the upstream Skill. Preserve the complete pinned source and prepare a working copy under runtime/archify when execution is requested; use node with the absolute archify/bin/archify.mjs path. Upstream README npx skills add/use routes are optional client registration mechanisms, not needed for toolkit retrieval and not executed here.

**Configuration:** Keep generated candidate JSON, HTML and receipts in the target project. Read the selected type schema/example and authoring references. Configure an isolated Chrome/Chromium executable for finalization when needed; disable optional update checks via ARCHIFY_UPDATE_CHECK_DISABLED=1 when offline operation is desired.

**Verification to perform:** During runtime setup use node archify/bin/archify.mjs doctor and its documented demo command from the working-copy root. For requested artifacts use the Skill finalize command and verify validate, deliver, strict provenance check and browser-check receipts. Distinguish automated browser evidence from visual inspection; missing browser support is not a passing full finalization.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read archify archify/SKILL.md
toolkit read archify README.md
toolkit read archify archify/references/delivery-contract.md
```

### Documented commands and alternatives

No package installation command is recorded. Follow the setup guidance and pinned upstream instructions; source-only guidance may need no runtime.

## Source entry points

- [archify/SKILL.md](https://github.com/tt-a1i/archify/blob/d5a1333d7447c866a765adac7d4d062f2f02e4d2/archify/SKILL.md)
- [README.md](https://github.com/tt-a1i/archify/blob/d5a1333d7447c866a765adac7d4d062f2f02e4d2/README.md)
- [archify/references/delivery-contract.md](https://github.com/tt-a1i/archify/blob/d5a1333d7447c866a765adac7d4d062f2f02e4d2/archify/references/delivery-contract.md)
- [archify/package.json](https://github.com/tt-a1i/archify/blob/d5a1333d7447c866a765adac7d4d062f2f02e4d2/archify/package.json)
- [archify/schemas/README.md](https://github.com/tt-a1i/archify/blob/d5a1333d7447c866a765adac7d4d062f2f02e4d2/archify/schemas/README.md)
- [archify/references/repository-authoring.md](https://github.com/tt-a1i/archify/blob/d5a1333d7447c866a765adac7d4d062f2f02e4d2/archify/references/repository-authoring.md)
- [archify/references/update-awareness.md](https://github.com/tt-a1i/archify/blob/d5a1333d7447c866a765adac7d4d062f2f02e4d2/archify/references/update-awareness.md)

## Skills and retrieval

The manifest registers **1 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [archify/SKILL.md](https://github.com/tt-a1i/archify/blob/d5a1333d7447c866a765adac7d4d062f2f02e4d2/archify/SKILL.md)

```bash
bin/toolkit show archify
bin/toolkit search "architecture diagrams workflow diagrams" --repo archify
bin/toolkit docs archify "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [tt-a1i/archify at `d5a1333d7447`](https://github.com/tt-a1i/archify/tree/d5a1333d7447c866a765adac7d4d062f2f02e4d2). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo archify --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
