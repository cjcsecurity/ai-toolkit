# text-to-cad

Agent skills and local cadgen runtime for parametric CAD, STEP/STL/GLB/3MF exports, engineering drawings, manufacturing checks and robot descriptions.

[Upstream repository](https://github.com/earthtojake/text-to-cad) · [Pinned source](https://github.com/earthtojake/text-to-cad/tree/8ef3a97f594f9145d28692900dfe1c547852041c) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Design and interfaces |
| Operating model | skills + plugin + cli + mcp |
| Recommended scope | on-demand |
| Registered production skill paths | 12 |
| Reviewed source commit | `8ef3a97f594f9145d28692900dfe1c547852041c` |

## Purpose and use cases

Generate and inspect geometry locally through build123d/OpenCascade, with optional fabrication and printer integrations. Install one plugin or skills route per agent to avoid duplicate skills.

**Discovery tags:** `cad`, `3d-modeling`, `step`, `stl`, `engineering-drawings`, `manufacturing`, `robotics`, `mcp`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- uv and Python >=3.11; the documented plugin command uses managed Python 3.13 and cadgen==0.7.14. First use needs network access for runtime downloads.
- cadgen depends on build123d >=0.11.1,<0.12, cadquery-ocp-novtk >=7.9,<8, drawing libraries and Playwright; browser snapshots fetch their browser on first use. Node.js 20+ is documented for the JavaScript tooling.
- Fabrication, part search and printer integrations have separate network/account/device requirements. Core geometry runs locally.
- On Windows with Smart App Control, unsigned OCP modules may be blocked; WSL is an alternative without disabling that protection.
- MIT core/plugin; individual skills and bundled components retain their license files. Usage analytics are opt-in; DO_NOT_TRACK=1 disables them, and CADGEN_UPDATE_CHECK=0 disables the version check.

## Setup guidance

**Setup scope:** project-local or isolated tool runtime; explicit agent registration

**Next action:** setup-required

**Working directory:** An isolated tool checkout or the selected target project, according to the pinned setup guide.

**Installation approach:** Reuse a compatible runtime first. Select one documented installation route, review dependencies and pin the version; commands are examples, not a script to execute in order.

**Configuration:** Choose the documented plugin for the intended client or standalone skills, not both. Keep the viewer local; configure fabrication services and printer access only for a selected task.

**Verification to perform:** Run cadgen doctor, build a small local part, inspect its exported geometry and open it in the viewer before fabrication.

**Local record:** Record the actual runtime version, checks and remaining requirements locally. Catalog/source presence does not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read text-to-cad README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx skills add earthtojake/text-to-cad
```

Example 2:

```bash
uvx --no-config --managed-python --python 3.13 --from cadgen==0.7.14 cadgen mcp
```

## Source entry points

- [README.md](https://github.com/earthtojake/text-to-cad/blob/8ef3a97f594f9145d28692900dfe1c547852041c/README.md)
- [packages/cadgen/pyproject.toml](https://github.com/earthtojake/text-to-cad/blob/8ef3a97f594f9145d28692900dfe1c547852041c/packages/cadgen/pyproject.toml)
- [skills/cad/SKILL.md](https://github.com/earthtojake/text-to-cad/blob/8ef3a97f594f9145d28692900dfe1c547852041c/skills/cad/SKILL.md)
- [skills/engineering-drawing/SKILL.md](https://github.com/earthtojake/text-to-cad/blob/8ef3a97f594f9145d28692900dfe1c547852041c/skills/engineering-drawing/SKILL.md)
- [skills/dfm/SKILL.md](https://github.com/earthtojake/text-to-cad/blob/8ef3a97f594f9145d28692900dfe1c547852041c/skills/dfm/SKILL.md)

## Skills and retrieval

The manifest registers **12 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/bambu-labs/SKILL.md](https://github.com/earthtojake/text-to-cad/blob/8ef3a97f594f9145d28692900dfe1c547852041c/skills/bambu-labs/SKILL.md)
- [skills/cad/SKILL.md](https://github.com/earthtojake/text-to-cad/blob/8ef3a97f594f9145d28692900dfe1c547852041c/skills/cad/SKILL.md)
- [skills/dfam-check/SKILL.md](https://github.com/earthtojake/text-to-cad/blob/8ef3a97f594f9145d28692900dfe1c547852041c/skills/dfam-check/SKILL.md)
- [skills/dfm/SKILL.md](https://github.com/earthtojake/text-to-cad/blob/8ef3a97f594f9145d28692900dfe1c547852041c/skills/dfm/SKILL.md)
- [skills/dxf/SKILL.md](https://github.com/earthtojake/text-to-cad/blob/8ef3a97f594f9145d28692900dfe1c547852041c/skills/dxf/SKILL.md)
- [skills/engineering-drawing/SKILL.md](https://github.com/earthtojake/text-to-cad/blob/8ef3a97f594f9145d28692900dfe1c547852041c/skills/engineering-drawing/SKILL.md)
- [skills/gcode/SKILL.md](https://github.com/earthtojake/text-to-cad/blob/8ef3a97f594f9145d28692900dfe1c547852041c/skills/gcode/SKILL.md)
- [skills/sdf/SKILL.md](https://github.com/earthtojake/text-to-cad/blob/8ef3a97f594f9145d28692900dfe1c547852041c/skills/sdf/SKILL.md)
- [skills/sendcutsend/SKILL.md](https://github.com/earthtojake/text-to-cad/blob/8ef3a97f594f9145d28692900dfe1c547852041c/skills/sendcutsend/SKILL.md)
- [skills/srdf/SKILL.md](https://github.com/earthtojake/text-to-cad/blob/8ef3a97f594f9145d28692900dfe1c547852041c/skills/srdf/SKILL.md)
- [skills/step-parts/SKILL.md](https://github.com/earthtojake/text-to-cad/blob/8ef3a97f594f9145d28692900dfe1c547852041c/skills/step-parts/SKILL.md)
- [skills/urdf/SKILL.md](https://github.com/earthtojake/text-to-cad/blob/8ef3a97f594f9145d28692900dfe1c547852041c/skills/urdf/SKILL.md)

```bash
bin/toolkit show text-to-cad
bin/toolkit search "cad 3d-modeling" --repo text-to-cad
bin/toolkit docs text-to-cad "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [earthtojake/text-to-cad at `8ef3a97f594f`](https://github.com/earthtojake/text-to-cad/tree/8ef3a97f594f9145d28692900dfe1c547852041c). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo text-to-cad --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
