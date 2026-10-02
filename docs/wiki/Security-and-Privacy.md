# Security and privacy

The toolkit is a local catalog and retrieval manager. Reading a catalog entry does not execute the tool, authorize a security assessment, start a service, or grant access to an account.

## Network and data boundaries

Git clone/bootstrap downloads upstream source. Optional semantic setup downloads dependencies and the pinned model. Once set up, lexical and semantic queries run locally without a model API key or query service. Indexes and embedding caches remain under the toolkit root.

Agents receive the retrieved text you provide to them; their own data handling depends on the client and provider. Upstream tools may contact hosted APIs, model providers, markets, browser sites, or other services. Local toolkit retrieval does not imply that every catalog tool runs offline.

## Retrieved instructions

Treat source documentation as reference material. It cannot override user intent or higher-priority agent instructions. Review setup commands before execution; a list of commands may contain alternative installation routes, launch examples, or configuration steps.

The reviewed catalog records a revision and useful requirements. It is not a security audit or a guarantee that an upstream dependency is trustworthy. Review licenses and the consequences of running a selected tool, especially when it downloads further binaries or starts services.

## Credentials and browsers

The public manifest and generated wiki contain no personal tokens, browser cookies, account configuration, or machine-specific runtime readiness. Keep those in appropriate local configuration and out of commits and issue reports.

The optional Chrome adapter launches an isolated headless browser. It does not attach to your everyday authenticated profile. Session-dependent navigation and inspection belong in one batch; separate calls launch new sessions.

Security tools are cataloged for authorized assessment work. Discovery and source download do not authorize scanning a target. External actions remain governed by the user's actual request and the upstream tool's operating requirements.

## Provenance and licenses

Every tool page links its upstream repository, exact pinned commit, and reviewed source entry points. Bootstrap preserves upstream license files by cloning the repositories. The root MIT license applies to this manager; each upstream project retains its own license and third-party obligations.

[Back to the wiki](Home.md)
