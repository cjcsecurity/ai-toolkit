# Catalog maintenance automation

Two small workflows keep the personal collection current:

- A local daily check opens a PR for each reviewed tool added to the local manifest.
- [Weekly discovery](tool-discovery.md) finds candidates to consider. Candidates remain outside the reviewed catalog until someone chooses and reviews them.

Both use the existing GitHub CLI. They do not need a model API key or run an AI agent in the background. The scheduled discovery workflow adapts the reviewed [Loop Engineering thin-loop pattern](https://github.com/cobusgreyling/loop-engineering/blob/62801dea82905bc6afb5448d24e5386e9792ad06/patterns/thin-loop.md): bounded runs, deduplication, visible output, and an explicit stop switch.

## Local additions

Complete the normal [catalog review](../CONTRIBUTING.md#catalog-changes): add the entry to `manifest.json`, assign its ID to a category in `scripts/generate_catalog_docs.py`, and regenerate the docs. Downloading sources and rebuilding the local index are separate actions. Run the publication check manually when ready, or let the daily timer pick it up.

```bash
python3 scripts/catalog_pr.py --source /path/to/ai-toolkit \
  --repository OWNER/REPO --gitleaks /path/to/gitleaks
```

The default is a dry run. Add `--publish` to open PRs. Requirements: Python 3.11+, Git, an authenticated `gh` account with repository push/PR permissions, Gitleaks 8.30.1 or compatible, and a Linux/macOS host with `fcntl` support. The source checkout's `origin` and push destination must match the explicit repository. The default base is `main`.

The check reads new entries only. It fetches the published base into a temporary isolated worktree, copies one entry and its literal category assignment, and regenerates docs using the published generator. It never copies local executable code, unrelated edits, downloaded sources, runtime state, or generated local files. Entries need exact upstream commit pins and portable metadata; the pin is verified against GitHub.

Before pushing, it runs manager tests, generated documentation/link checks, a diff check, and a redacted staged Gitleaks scan. A failed check stops publication. Optional tests may skip when optional runtimes are absent; normal PR CI still runs. The source working tree and index are preserved. Source changes detected during validation stop the run, and edits from the last two minutes wait until the next check. This quiet period is not a substitute for finishing the metadata review.

The branch `catalog/add-TOOL-ID` provides a stable identity. An existing open PR is reported without creating another or overwriting reviewer changes. A closed PR is respected; the check does not reopen it. Subsequent edits to an entry already in a PR require an explicit follow-up on that branch. A push that succeeded before PR creation failed can be recovered if its tree still matches; otherwise the check stops for manual reconciliation. No PR is automatically merged.

## Install a daily local check

Copy the reviewed publisher to a stable location such as `~/.local/lib/ai-toolkit-automation/catalog_pr.py`. This keeps later unfinished edits to the script out of the scheduled job. Upgrade that copy deliberately after its changes merge. Keep a verified Gitleaks binary available at the path in the service.

Adapt the [service](../config/systemd/toolkit-catalog-pr.service.example) and [timer](../config/systemd/toolkit-catalog-pr.timer) into `~/.config/systemd/user/`. Replace `SOURCE`, `OWNER/REPO`, and `GITLEAKS` with your own values. Personal paths and credentials belong in local service configuration, not Git. Use an absolute Python/script path and quote paths with spaces according to systemd syntax.

```bash
systemctl --user daemon-reload
systemctl --user enable --now toolkit-catalog-pr.timer
systemctl --user start toolkit-catalog-pr.service
systemctl --user status toolkit-catalog-pr.service
journalctl --user -u toolkit-catalog-pr.service --since today
systemctl --user list-timers toolkit-catalog-pr.timer
```

The example runs daily at 09:17 America/Denver, with up to five minutes of jitter. `Persistent=true` catches up a missed run when the user service manager next starts. The machine and user service manager must be running; GitHub cannot read unpublished files on a powered-off workstation. The service has a 15-minute limit, and overlapping runs are prevented with a file lock. Network/authentication/test failures appear as a failed service in the journal and are retried on the next scheduled run. There is no separate email or chat notification.

Run `systemctl --user disable --now toolkit-catalog-pr.timer` to stop future local checks, and `systemctl --user stop toolkit-catalog-pr.service` to cancel an active one. Disable the Tool discovery workflow in GitHub Actions to stop weekly discovery.

Existing entries, source-pin updates, dependency changes, and deletions stay deliberate maintenance PRs. This workflow only turns completed new-tool metadata into a reviewable addition.
