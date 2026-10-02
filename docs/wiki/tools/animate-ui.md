# animate-ui

React/TypeScript/Tailwind/Motion animated component source and shadcn-compatible registry, with documentation and optional shadcn Registry MCP setup.

[Upstream repository](https://github.com/imskyleen/animate-ui) · [Pinned source](https://github.com/imskyleen/animate-ui/tree/efeb96ffd7a3b7a4868667e4ac3c346620fb3044) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Design and interfaces |
| Operating model | reference |
| Recommended scope | on-demand |
| Registered production skill paths | 0 |
| Reviewed source commit | `efeb96ffd7a3b7a4868667e4ac3c346620fb3044` |

## Purpose and use cases

Consult component source and add only the selected registry component to a target project. No Agent Skill bundle; agents can use source/docs directly, while optional registry MCP is a separate shadcn integration.

**Discovery tags:** `react`, `components`, `animation`, `motion`, `tailwind`, `shadcn`, `ui`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Compatible React/TypeScript/Tailwind/Motion target application.
- Source monorepo declares Node >=20 and pnpm 10.4.1; shadcn CLI for documented component install.
- Optional shadcn MCP must be configured separately in the chosen client.

## Setup guidance

**Setup scope:** target application dependencies and components

**Next action:** setup-required

**Working directory:** Selected target project for SDKs/components/configuration; isolated shared tool environment for standalone CLI installs.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Run shadcn/component commands in the target React app. Select only the required components and compatible Tailwind/Motion dependencies.

**Verification to perform:** Build the app and render the selected component; check required peer dependencies.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read animate-ui apps/www/content/docs/installation.mdx
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx shadcn@latest init
```

Example 2:

```bash
npx shadcn@latest add @animate-ui/primitives-texts-sliding-number
```

Example 3:

```bash
npm install -D shadcn@latest
```

## Source entry points

- [README.md](https://github.com/imskyleen/animate-ui/blob/efeb96ffd7a3b7a4868667e4ac3c346620fb3044/README.md)
- [package.json](https://github.com/imskyleen/animate-ui/blob/efeb96ffd7a3b7a4868667e4ac3c346620fb3044/package.json)
- [apps/www/content/docs/installation.mdx](https://github.com/imskyleen/animate-ui/blob/efeb96ffd7a3b7a4868667e4ac3c346620fb3044/apps/www/content/docs/installation.mdx)
- [apps/www/content/docs/mcp.mdx](https://github.com/imskyleen/animate-ui/blob/efeb96ffd7a3b7a4868667e4ac3c346620fb3044/apps/www/content/docs/mcp.mdx)

## Skills and retrieval

The manifest registers **0 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

No production Agent Skill path is registered. Search its documentation and source entry points instead.

```bash
bin/toolkit show animate-ui
bin/toolkit search "react components" --repo animate-ui
bin/toolkit docs animate-ui "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [imskyleen/animate-ui at `efeb96ffd7a3`](https://github.com/imskyleen/animate-ui/tree/efeb96ffd7a3b7a4868667e4ac3c346620fb3044). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo animate-ui --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
