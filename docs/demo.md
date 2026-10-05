# A demo made with tools from the library

[Watch the 22-second demo](assets/ai-toolkit-demo.mp4) · [Static preview](assets/poster.jpg)

The video follows a real discovery task: find a workflow for creating a project demo. Its terminal scenes are styled, abridged replays of actual CLI output. Animation timing does not represent search performance.

## Try the search

From the repository root:

```bash
python3 scripts/bootstrap.py
bin/toolkit search "launch video" --kind repo --limit 3 --lexical
bin/toolkit show brag
python3 scripts/bootstrap.py --repo brag --lexical
bin/toolkit skills brag "launch video" --limit 2 --lexical
bin/toolkit --budget 12000 read brag skills/brag/SKILL.md
```

The repository search returns Brag. After its pinned source is downloaded, skill search identifies `skills/brag/SKILL.md`. Read the selected instructions and setup requirements before configuring a tool. Discovery, source download, and runtime setup are separate steps.

## Tools used

| Tool | Role |
| --- | --- |
| [Brag](wiki/tools/brag.md) | Project-to-video workflow and storyboard. |
| [Hyperframes](wiki/tools/hyperframes.md) | HTML animation, seekable timeline, frame checks, and local rendering with CLI 0.8.106. |
| [Humanizer](wiki/tools/humanizer.md) | Editing guidance for the project copy. |
| [Semgrep](wiki/tools/semgrep.md) | Static analysis of the Python manager. |

The Open Atlas design uses mint, evergreen, and route blue, with dark terminal panels. Typography combines Archivo, Source Sans 3, and JetBrains Mono. The video has no music or narration. The MP4 is 1080 × 1080 at 30 fps; the README uses a smaller GIF and offers a static preview.

AI Toolkit finds relevant tools and instructions. The agent then applies those instructions to produce the result; the manager itself is not a video renderer.

[Back to the README](../README.md)
