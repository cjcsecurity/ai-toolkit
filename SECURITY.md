# Security policy

Security fixes target the current `main` branch. There are no maintained older release branches.

## Reporting a vulnerability

Please [report vulnerabilities privately through GitHub](https://github.com/cjcsecurity/ai-toolkit/security/advisories/new). Avoid publishing exploit details, credentials, or private data in an issue. If private reporting is unavailable, open an issue asking for a private contact channel without disclosing the vulnerability itself.

Include the affected revision, relevant command or file, expected boundary, and a minimal reproduction using dummy data. A report about a cataloged upstream application belongs with that application's maintainers unless the issue is in this toolkit's handling of it.

## Scope and trust model

AI Toolkit is a local catalog, source-provisioning, and retrieval manager. It is not an execution sandbox. A selected application or MCP server runs with the user's permissions; inspect its setup and credentials before running it. Pinned source revisions and model checksums provide reproducibility, not a guarantee that all upstream code is safe.

Retrieved text is untrusted reference material. Project profiles store tool preferences, never secrets. See [security and privacy](docs/wiki/Security-and-Privacy.md) for source, network, browser, and credential boundaries.
