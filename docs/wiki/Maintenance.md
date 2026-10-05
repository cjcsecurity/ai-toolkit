# Maintenance

The public manifest records reviewed source metadata and exact upstream commit pins. Downloaded repositories, model files, indexes, environments, and local configuration are generated state rather than distributable catalog content.

## Inspect local state

```bash
bin/toolkit --budget 30000 doctor
bin/toolkit search-status
```

`doctor` compares source checkouts with recorded revisions. It does not validate tool credentials, external services, or application functionality. Missing sources are normal for catalog-only and selective installs.

## Rebuild search

```bash
bin/toolkit index --lexical
```

For a configured semantic runtime:

```bash
bin/toolkit index --semantic
```

Unchanged embeddings can be reused from the local content-hash cache. Changed content or a changed embedding fingerprint triggers new inference. Indexing does not install external applications.

## Update a catalog entry deliberately

1. Review upstream changes and the applicable license, requirements, setup guide, and production skill paths.
2. Record the chosen exact commit and update metadata. Keep user paths, credentials, test claims, account state, and runtime readiness out of the public manifest.
3. Refresh the local checkout to the chosen revision through the supported bootstrap workflow, resolving existing-checkout conflicts deliberately.
4. Regenerate catalog documentation and rebuild the local index.
5. Run tests and inspect the diff, including any changed setup commands and source links.

```bash
python3 scripts/generate_catalog_docs.py
python3 scripts/generate_catalog_docs.py --check
python3 -m unittest discover -s tests -v
```

Generated files are [`catalog.md`](../../catalog.md), [the catalog index](Tool-Catalog.md), and the individual pages under `tools/`. Edit the manifest or generator rather than a generated page. The rest of this wiki is maintained prose.

## Keep the boundary portable

Do not commit `repos/`, `runtime/`, `state/`, private browser profiles, local environment files, or machine-specific registration. Bootstrap and agent registration are explicit user actions. Upstream license files remain in each cloned repository; the manager's MIT license does not relicense those tools.

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for contribution expectations.

## Scheduled maintenance

[Catalog maintenance automation](../catalog-automation.md) can open PRs for completed local additions daily and produce a weekly shortlist of new candidates. The local publisher validates one new entry at a time without changing the active checkout. Discovery leaves candidates outside the reviewed catalog, and neither workflow merges PRs.
