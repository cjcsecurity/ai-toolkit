# anthropic-cybersecurity-skills

Independent community collection of 818 structured skills spanning defensive security, incident response, forensics, cloud security, and authorized offensive testing.

[Upstream repository](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) · [Pinned source](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/tree/54a798831d2266a3ca61ce68a7acb80b81160d57) · [All tools](../Tool-Catalog.md)

| Catalog detail | Value |
| --- | --- |
| Category | Security and assessment |
| Operating model | skill-bundle |
| Recommended scope | on-demand |
| Registered production skill paths | 818 |
| Reviewed source commit | `54a798831d2266a3ca61ce68a7acb80b81160d57` |

## Purpose and use cases

Index the full collection but load individual relevant skills as needed; broad offensive/defensive material should not all activate globally.

**Discovery tags:** `security`, `skills`, `incident-response`, `forensics`, `threat-intelligence`, `malware-analysis`, `cloud-security`, `pentest`, `mitre`, `nist`, `compliance`, `detection`.

Scope recommendations describe how to adopt this tool if selected. They do not mean it is installed globally or ready on your machine. Bootstrap downloads source; runtime and client registration are separate.

## Requirements and dependencies

- No runtime required to read the skill library; compatible agent needed to use skill instructions.
- Per-skill tools, credentials, and access differ; inspect each Prerequisites section before use.
- Some workflows use Python and security tools such as tshark, Zeek, Suricata, or cloud/security-platform APIs.
- Offensive workflows require explicitly authorized targets and scope. The project is not affiliated with Anthropic.

## Setup guidance

**Setup scope:** read selected skill; task-specific tool environment

**Next action:** read-selected-reference

**Working directory:** Read from the stored checkout; install only selected task dependencies in an isolated environment or the target project.

**Installation approach:** Check for an existing compatible runtime first; install_commands are upstream alternatives and may include launch/configuration examples. Select one documented route, satisfy requirements, and pin its version; do not execute the list as a script.

**Configuration:** Read only the chosen SKILL.md and its Prerequisites section. Provision that workflow's tools and accounts; the collection itself needs no package installation.

**Verification to perform:** Confirm the selected skill references resolve and its required tools are available for the authorized scope.

**Local record:** After actual setup, record the runtime path/version, configuration checks and remaining requirements in local project notes. Catalog and source presence alone do not establish runtime readiness.

### Read first

After downloading this source, read the selected instructions in full:

```bash
toolkit read anthropic-cybersecurity-skills README.md
```

### Documented commands and alternatives

These are upstream installation alternatives, registration routes, or launch/configuration examples. They are **not a script to execute in order**. Follow the pinned setup guide, select the appropriate route, and review dependencies and version pins before running a command. Commands using `latest`, a branch, or an unversioned package can resolve differently from the catalog source pin.

Example 1:

```bash
npx skills add mukul975/Anthropic-Cybersecurity-Skills
```

## Source entry points

- [README.md](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/README.md)
- [SECURITY.md](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/SECURITY.md)
- [skills/analyzing-network-traffic-of-malware/SKILL.md](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/analyzing-network-traffic-of-malware/SKILL.md)

## Skills and retrieval

The manifest registers **818 production skill paths** at this revision. This is a catalog count, not the number of skills installed into your agent.

- [skills/abusing-dpapi-for-credential-access/SKILL.md](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/abusing-dpapi-for-credential-access/SKILL.md)
- [skills/abusing-shadow-credentials-for-privesc/SKILL.md](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/abusing-shadow-credentials-for-privesc/SKILL.md)
- [skills/achieving-cmmc-level-2-compliance/SKILL.md](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/achieving-cmmc-level-2-compliance/SKILL.md)
- [skills/acquiring-disk-image-with-dd-and-dcfldd/SKILL.md](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/acquiring-disk-image-with-dd-and-dcfldd/SKILL.md)
- [skills/analyzing-active-directory-acl-abuse/SKILL.md](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/analyzing-active-directory-acl-abuse/SKILL.md)
- [skills/analyzing-android-malware-with-apktool/SKILL.md](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/analyzing-android-malware-with-apktool/SKILL.md)
- [skills/analyzing-api-gateway-access-logs/SKILL.md](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/analyzing-api-gateway-access-logs/SKILL.md)
- [skills/analyzing-apt-group-with-mitre-navigator/SKILL.md](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/analyzing-apt-group-with-mitre-navigator/SKILL.md)
- [skills/analyzing-azure-activity-logs-for-threats/SKILL.md](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/analyzing-azure-activity-logs-for-threats/SKILL.md)
- [skills/analyzing-bootkit-and-rootkit-samples/SKILL.md](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/analyzing-bootkit-and-rootkit-samples/SKILL.md)
- [skills/analyzing-browser-forensics-with-hindsight/SKILL.md](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/analyzing-browser-forensics-with-hindsight/SKILL.md)
- [skills/analyzing-campaign-attribution-evidence/SKILL.md](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/analyzing-campaign-attribution-evidence/SKILL.md)

Showing 12 of 818 registered paths. Retrieve the relevant skill by topic; the complete inventory is in the [manifest](../../../manifest.json).

```bash
bin/toolkit show anthropic-cybersecurity-skills
bin/toolkit search "security skills" --repo anthropic-cybersecurity-skills
bin/toolkit docs anthropic-cybersecurity-skills "installation"
```

## Provenance and availability

This page is generated from the reviewed [manifest](../../../manifest.json). Requirements and setup guidance refer to [mukul975/Anthropic-Cybersecurity-Skills at `54a798831d22`](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/tree/54a798831d2266a3ca61ce68a7acb80b81160d57). The source pin identifies the reviewed checkout; it does not automatically pin every transitive dependency or external installer.

The entry is cataloged independently of local source presence. Download its source explicitly with the command below, then verify runtime requirements separately. No machine-specific installation, authentication, or successful runtime check is asserted here.

```bash
python3 scripts/bootstrap.py --repo anthropic-cybersecurity-skills --lexical
```

Upstream license and notice files remain in the downloaded repository. Review those terms and any dependency licenses before use.

[Runtime setup](../Runtime-Setup.md) · [Retrieval system](../Retrieval-System.md) · [Wiki home](../Home.md)
