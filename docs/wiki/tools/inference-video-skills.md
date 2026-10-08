# inference-video-skills

AI video generation recipes for inference.sh belt CLI, including text-to-video, image-to-video, avatars, lip sync and editing.

[Upstream repository](https://github.com/101-skills/superpowers) · [Pinned source](https://github.com/101-skills/superpowers/tree/becc25649700d5457772a00e5143e28ccf9e5afa) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Writing, video, and audio |
| Operating model | cli |
| Recommended scope | on-demand |
| Registered production skill paths | 1 |
| Reviewed source commit | `becc25649700d5457772a00e5143e28ccf9e5afa` |

## Purpose and use cases

On-demand video source. Despite its repository name, this is an inference.sh-oriented collection, not the obra/Superpowers engineering workflow. Register only the requested video skill; related upstream skills remain optional references.

**Discovery tags:** `AI video generation`, `inference.sh`, `belt`, `text to video`, `image to video`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Reading the skill requires no runtime. Execution requires the inference.sh belt CLI and authenticated account with access to the selected hosted model.
- Model availability, account quotas and charges require current provider verification; prompts and media are sent to the hosted service.
- CLI installation is separately versioned. Prefer a reviewed package-manager release over executing the remote curl-to-shell example.

## Setup guidance

**Setup scope:** shared on-demand source; selected project or isolated runtime only

**Next action:** setup-required

**Working directory:** Read from the pinned checkout; apply only in the selected target project.

**Installation approach:** Source download and retrieval require no upstream runtime. For execution, reuse a compatible runtime or provision one isolated version following the pinned guide. Registration commands are alternatives, not an execution queue; do not install the entire collection globally.

**Configuration:** Choose and review a CLI release, authenticate only for a requested generation task, and verify model inputs and cost before submitting media. Preserve existing local-video alternatives.

**Verification to perform:** Read the skill and installation guide; separately check belt version, authentication and one authorized bounded generation when selected.

**Local record:** Record actual runtime and authentication checks in local project notes; source availability is not runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read inference-video-skills README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx skills add 101-skills/superpowers --skill ai-video-generation
```

Example 2:

```bash
npx @inferencesh/belt --help
```

## Source entry points

- [README.md](https://github.com/101-skills/superpowers/blob/becc25649700d5457772a00e5143e28ccf9e5afa/README.md)
- [cli-install.md](https://github.com/101-skills/superpowers/blob/becc25649700d5457772a00e5143e28ccf9e5afa/cli-install.md)
- [tools/video/ai-video-generation/SKILL.md](https://github.com/101-skills/superpowers/blob/becc25649700d5457772a00e5143e28ccf9e5afa/tools/video/ai-video-generation/SKILL.md)

## Skills and retrieval

The manifest registers **1 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [tools/video/ai-video-generation/SKILL.md](https://github.com/101-skills/superpowers/blob/becc25649700d5457772a00e5143e28ccf9e5afa/tools/video/ai-video-generation/SKILL.md)

```bash
bin/toolkit show inference-video-skills
bin/toolkit search "AI video generation inference.sh" --repo inference-video-skills
bin/toolkit docs inference-video-skills "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [101-skills/superpowers at `becc25649700`](https://github.com/101-skills/superpowers/tree/becc25649700d5457772a00e5143e28ccf9e5afa). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo inference-video-skills --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
