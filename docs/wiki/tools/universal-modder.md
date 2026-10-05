# universal-modder

Game-modding skills and Python CLI for engine recon, reverse engineering, sprite and 3D-to-sprite pipelines, Windows capture, video editing, packaging checks and shared field notes.

[Upstream repository](https://github.com/rehan-remade/universal-modder) · [Pinned source](https://github.com/rehan-remade/universal-modder/tree/0f5dcdfdcd8ed420f8413815bd6647586ab894a2) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Games and modding |
| Operating model | cli-and-skill-bundle |
| Recommended scope | project-local |
| Registered production skill paths | 10 |
| Reviewed source commit | `0f5dcdfdcd8ed420f8413815bd6647586ab894a2` |

## Purpose and use cases

Primary workflow for broad PC game modding, or focused supporting capabilities for an established game-specific loader. Preserve existing loader versions and validated save procedures; generic examples do not establish compatibility with a particular Unity/IL2CPP build. Keep all ten skills available on demand rather than registering the specialized collection globally.

**Discovery tags:** `game modding`, `Unity`, `IL2CPP`, `BepInEx`, `reverse engineering`, `sprites`, `pixel art`, `asset pipeline`, `Windows`, `WSL`, `game automation`, `save backups`, `video`, `fal`, `ComfyUI`, `MCP`, `field notes`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Python >=3.10 with Pillow >=10, NumPy >=1.24 and PyYAML >=6; uv or pipx can isolate the CLI.
- Agent Skills client for the optional skills; retain each skill directory and its references.
- ffmpeg for video editing; ffprobe is optional because the CLI has a fallback.
- Windows or WSL plus PowerShell for um win; window capture requires a Windows ffmpeg build with gfxcapture. Its setup copies tools into Windows LocalAppData rather than UM_HOME.
- Blender for um render3d; set BLENDER or provide blender on PATH.
- FAL_KEY for fal generation and its optional hosted MCP server; local ComfyUI is an alternative image workflow.
- Local game ownership, compatible loader/interop and isolated test saves must be established for each game. Skills and CLI installation do not install a mod loader.
- UM_HOME redirects backups and other per-user state; UM_KB can select a local field-note checkout. Publishing field notes requires explicit authorization and GitHub access.

## Setup guidance

**Setup scope:** project-local CLI and selected skills; optional media runtimes and fal MCP

**Next action:** setup-required

**Working directory:** Selected game-mod project; keep source, virtual environments and derived game data in ignored project directories.

**Installation approach:** Reuse a compatible Python runtime. Install the pinned CLI in an isolated environment and project-local skills with their reference directories. The plugin route is an alternative, not an additional required installation.

**Configuration:** Choose required capabilities. Provide ffmpeg for video and Blender for 3D rendering; configure fal only with a user-provided FAL_KEY, or choose local ComfyUI. Preserve existing loader and save safeguards. Review um win setup before running because it writes to Windows LocalAppData.

**Verification to perform:** Check um --version and group help, run the upstream offline tests, then exercise a small sprite pipeline and synthetic video. Verify game-specific recon read-only; game launch and capture require isolated runtime validation.

**Local record:** Record exact revision, runtime, selected skills, dependency availability and actual verification in project notes. Distinguish CLI readiness from game integration and optional services.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read universal-modder README.md
toolkit read universal-modder skills/mod-any-game/SKILL.md
toolkit read universal-modder skills/mod-any-game/references/safety.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
uv tool install git+https://github.com/rehan-remade/universal-modder@0f5dcdfdcd8ed420f8413815bd6647586ab894a2
```

Example 2:

```bash
npx skills add https://github.com/rehan-remade/universal-modder
```

Example 3:

```bash
codex plugin marketplace add rehan-remade/universal-modder
codex plugin add universal-modder@universal-modder
```

## Source entry points

- [README.md](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/README.md)
- [CONTRIBUTING.md](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/CONTRIBUTING.md)
- [pyproject.toml](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/pyproject.toml)
- [bin/um](https://github.com/rehan-remade/universal-modder/tree/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/bin/um)
- [.codex-plugin/plugin.json](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/.codex-plugin/plugin.json)
- [.codex/config.toml](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/.codex/config.toml)
- [skills/mod-any-game/SKILL.md](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/skills/mod-any-game/SKILL.md)
- [skills/mod-any-game/references/engines/unity.md](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/skills/mod-any-game/references/engines/unity.md)
- [skills/mod-any-game/references/safety.md](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/skills/mod-any-game/references/safety.md)
- [um/common.py](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/um/common.py)
- [um/win.py](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/um/win.py)
- [um/backup.py](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/um/backup.py)
- [tests/test_um.py](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/tests/test_um.py)

## Skills and retrieval

The manifest registers **10 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/mod-any-game/SKILL.md](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/skills/mod-any-game/SKILL.md)
- [skills/game-recon/SKILL.md](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/skills/game-recon/SKILL.md)
- [skills/reverse-engineering/SKILL.md](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/skills/reverse-engineering/SKILL.md)
- [skills/fal-assets/SKILL.md](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/skills/fal-assets/SKILL.md)
- [skills/asset-pipeline/SKILL.md](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/skills/asset-pipeline/SKILL.md)
- [skills/game-automation/SKILL.md](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/skills/game-automation/SKILL.md)
- [skills/showcase-video/SKILL.md](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/skills/showcase-video/SKILL.md)
- [skills/mashup-mods/SKILL.md](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/skills/mashup-mods/SKILL.md)
- [skills/publish-mod/SKILL.md](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/skills/publish-mod/SKILL.md)
- [skills/share-field-notes/SKILL.md](https://github.com/rehan-remade/universal-modder/blob/0f5dcdfdcd8ed420f8413815bd6647586ab894a2/skills/share-field-notes/SKILL.md)

```bash
bin/toolkit show universal-modder
bin/toolkit search "game modding Unity" --repo universal-modder
bin/toolkit docs universal-modder "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [rehan-remade/universal-modder at `0f5dcdfdcd8e`](https://github.com/rehan-remade/universal-modder/tree/0f5dcdfdcd8ed420f8413815bd6647586ab894a2). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo universal-modder --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
