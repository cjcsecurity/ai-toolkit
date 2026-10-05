# Contributing

Contributions should improve tool selection, the accuracy of reviewed metadata, or the reliability of local retrieval. Keep the public repository portable: source and runtime downloads are explicit setup steps, and machine-specific readiness belongs outside the public catalog.

## Catalog changes

For a new or updated entry, review upstream documentation and record an exact commit pin. Explain the tool's purpose, operating model, requirements, recommended scope, setup alternatives, production skill paths, and useful source entry points. Distinguish known requirements from unknown setup details. Do not infer runtime readiness from source availability.

Exclude private paths, credentials, browser state, personal configuration, local logs, and unverified success claims. Retain upstream licensing and avoid registering whole specialized collections globally by default.

The collection is expected to grow. Keep the README headline and promotional graphics independent of a fixed tool count; generated catalog counts describe the current manifest. Personal announcement drafts and design explorations belong outside the checkout.

Regenerate the checked-in catalog pages after editing metadata:

```bash
python3 scripts/generate_catalog_docs.py
python3 scripts/generate_catalog_docs.py --check
```

## Manager changes

Keep the lexical path usable with Python 3.11+ and the standard library. Optional search and MCP dependencies should stay isolated and explicit. Query operations must not silently download models or contact an embedding API. Preserve source locations, bounded output, and useful error messages.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/generate_catalog_docs.py --check
```

Tests that require optional dependencies or the real checkpoint may be skipped in a standard-library environment; report which suite you ran. Use the optional runtime when changing embedding behavior. Do not claim all application runtimes were validated by manager tests.

A pull request should state the problem, the resulting behavior, relevant validation, and any platform or setup limits. Include changes to generated documentation when source pins or catalog metadata change.

## Before publishing

Review the staged diff and filenames. With [Gitleaks](https://github.com/gitleaks/gitleaks) installed, scan reachable history and the staged changes:

```bash
gitleaks git --redact --log-opts=--all
gitleaks git --redact --staged
```

The configuration excludes only three exact public model-checksum values; normal secret rules remain enabled. Keep scanner reports outside the repository. For vulnerability reports, follow the [security policy](SECURITY.md).
