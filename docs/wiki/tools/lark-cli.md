# lark-cli

Official Lark/Feishu CLI skills for docs, spreadsheets, Base, drive, messages, calendar, mail, approvals, tasks, meetings, OKRs and workplace workflows.

[Upstream repository](https://github.com/larksuite/cli) · [Pinned source](https://github.com/larksuite/cli/tree/7beffb086d7fa3c5b843d8affa7c089f49cfc65e) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Workplace and marketing |
| Operating model | cli |
| Recommended scope | on-demand |
| Registered production skill paths | 28 |
| Reviewed source commit | `7beffb086d7fa3c5b843d8affa7c089f49cfc65e` |

## Purpose and use cases

The 24 open.feishu.cn top-50 SKILL.md bodies exactly matched this pinned official repository during review. Register all 28 production skills because several top-50 workflows depend on non-top-50 meeting/note skills. Keep the collection on demand; it is workplace-specific and can access or modify private workspace data. Test and template skills are excluded.

**Discovery tags:** `Lark`, `Feishu`, `workplace automation`, `documents`, `spreadsheets`, `calendar`, `meetings`, `approvals`, `open.feishu.cn`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- Skill text needs no runtime. Published @larksuite/cli package requires Node.js >=16 and a supported native platform.
- Source build requires Go >=1.23 and Python 3 according to README; inspect go.mod for the exact toolchain before building.
- Actual workspace operations require a Lark/Feishu app, user or bot authentication, tenant access and operation-specific scopes.
- Preserve sibling lark-shared, lark-meeting and references; upstream instructions are primarily Chinese.
- Credentials use platform storage; never print tokens. High-risk writes have an explicit confirmation gate and supported commands offer dry-run.
- SkillSpector static analysis is partial for several references and flags documented credential, deletion and validation-bypass surfaces. Review the chosen workflow and scripts before execution; cataloging is not blanket runtime approval.

## Setup guidance

**Setup scope:** shared on-demand source; selected project or isolated runtime only

**Next action:** setup-required

**Working directory:** Read from the pinned checkout; apply only in the selected target project.

**Installation approach:** Source download and retrieval require no upstream runtime. For execution, reuse a compatible runtime or provision one isolated version following the pinned guide. Registration commands are alternatives, not an execution queue; do not install the entire collection globally.

**Configuration:** Install only for an actual Lark task; inspect installer skill-registration scope. Configure the chosen app and minimal domains, distinguish user/bot identity and retain high-risk confirmations. No account authorization is implied by cataloging.

**Verification to perform:** Verify selected skill and sibling references; for runtime setup check version, auth status and a minimal authorized read before any write.

**Local record:** Record actual runtime and authentication checks in local project notes; source availability is not runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read lark-cli README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx @larksuite/cli@1.0.97 install
```

Example 2:

```bash
lark-cli auth status
```

## Source entry points

- [README.md](https://github.com/larksuite/cli/blob/7beffb086d7fa3c5b843d8affa7c089f49cfc65e/README.md)
- [package.json](https://github.com/larksuite/cli/blob/7beffb086d7fa3c5b843d8affa7c089f49cfc65e/package.json)
- [skills/lark-shared/SKILL.md](https://github.com/larksuite/cli/blob/7beffb086d7fa3c5b843d8affa7c089f49cfc65e/skills/lark-shared/SKILL.md)
- [skills/lark-shared/references/lark-shared-high-risk-approval.md](https://github.com/larksuite/cli/blob/7beffb086d7fa3c5b843d8affa7c089f49cfc65e/skills/lark-shared/references/lark-shared-high-risk-approval.md)
- [skills/lark-meeting/SKILL.md](https://github.com/larksuite/cli/blob/7beffb086d7fa3c5b843d8affa7c089f49cfc65e/skills/lark-meeting/SKILL.md)

## Skills and retrieval

The manifest registers **28 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/lark-approval/SKILL.md](https://github.com/larksuite/cli/blob/7beffb086d7fa3c5b843d8affa7c089f49cfc65e/skills/lark-approval/SKILL.md)
- [skills/lark-apps/SKILL.md](https://github.com/larksuite/cli/blob/7beffb086d7fa3c5b843d8affa7c089f49cfc65e/skills/lark-apps/SKILL.md)
- [skills/lark-attendance/SKILL.md](https://github.com/larksuite/cli/blob/7beffb086d7fa3c5b843d8affa7c089f49cfc65e/skills/lark-attendance/SKILL.md)
- [skills/lark-base/SKILL.md](https://github.com/larksuite/cli/blob/7beffb086d7fa3c5b843d8affa7c089f49cfc65e/skills/lark-base/SKILL.md)
- [skills/lark-calendar/SKILL.md](https://github.com/larksuite/cli/blob/7beffb086d7fa3c5b843d8affa7c089f49cfc65e/skills/lark-calendar/SKILL.md)
- [skills/lark-contact/SKILL.md](https://github.com/larksuite/cli/blob/7beffb086d7fa3c5b843d8affa7c089f49cfc65e/skills/lark-contact/SKILL.md)
- [skills/lark-doc/SKILL.md](https://github.com/larksuite/cli/blob/7beffb086d7fa3c5b843d8affa7c089f49cfc65e/skills/lark-doc/SKILL.md)
- [skills/lark-drive/SKILL.md](https://github.com/larksuite/cli/blob/7beffb086d7fa3c5b843d8affa7c089f49cfc65e/skills/lark-drive/SKILL.md)
- [skills/lark-event/SKILL.md](https://github.com/larksuite/cli/blob/7beffb086d7fa3c5b843d8affa7c089f49cfc65e/skills/lark-event/SKILL.md)
- [skills/lark-im/SKILL.md](https://github.com/larksuite/cli/blob/7beffb086d7fa3c5b843d8affa7c089f49cfc65e/skills/lark-im/SKILL.md)
- [skills/lark-mail/SKILL.md](https://github.com/larksuite/cli/blob/7beffb086d7fa3c5b843d8affa7c089f49cfc65e/skills/lark-mail/SKILL.md)
- [skills/lark-markdown/SKILL.md](https://github.com/larksuite/cli/blob/7beffb086d7fa3c5b843d8affa7c089f49cfc65e/skills/lark-markdown/SKILL.md)

Showing 12 of 28 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show lark-cli
bin/toolkit search "Lark Feishu" --repo lark-cli
bin/toolkit docs lark-cli "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [larksuite/cli at `7beffb086d7f`](https://github.com/larksuite/cli/tree/7beffb086d7fa3c5b843d8affa7c089f49cfc65e). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo lark-cli --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
