#!/usr/bin/env python3
"""Bounded, report-only repository discovery; GitHub issues hold the loop state."""
import argparse
from datetime import date, timedelta, timezone, datetime
import html
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
WEEK_MARKER = re.compile(r"\A<!-- ai-toolkit-discovery:week (\d{4}-W\d{2}) -->\n")
CANDIDATE_MARKER = re.compile(r"^<!-- ai-toolkit-discovery:candidate ([^\n]+) -->$", re.M)


def repo_name(value):
    if (not isinstance(value, str) or not re.fullmatch(
            r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?/[A-Za-z0-9_.-]{1,100}", value)
            or value.split("/")[1] in {".", ".."} or "--" in value.split("/")[0]):
        raise ValueError("Invalid GitHub repository identifier")
    return value.lower()


def validate_config(raw):
    bounds = dict(created_days=(1, 365), pushed_days=(1, 180), min_stars=(20, 1000000),
                  per_query_limit=(1, 50), max_candidates=(1, 5))
    if not isinstance(raw, dict) or set(raw) - (set(bounds) | {"queries", "ignore"}):
        raise ValueError("Unknown discovery configuration keys")
    for key, (low, high) in bounds.items():
        if type(raw.get(key)) is not int or not low <= raw[key] <= high:
            raise ValueError(f"{key} must be an integer in {low}..{high}")
    queries = raw.get("queries")
    if not isinstance(queries, list) or not 5 <= len(queries) <= 8:
        raise ValueError("Configure 5..8 discovery queries")
    for query in queries:
        if (not isinstance(query, dict) or set(query) != {"topic", "query"}
                or any(not isinstance(v, str) or not v.strip() or len(v) > 180
                       or not v.isprintable() for v in query.values())):
            raise ValueError("Each query needs a short printable topic and query")
    if len({q["topic"].lower() for q in queries}) != len(queries):
        raise ValueError("Query topics must be distinct")
    if not isinstance(raw.get("ignore", []), list):
        raise ValueError("ignore must be a list of repository identifiers")
    for name in raw.get("ignore", []):
        repo_name(name)
    return dict(raw, ignore=raw.get("ignore", []))


def select_candidates(batches, config, excluded, today):
    excluded = {repo_name(x) for x in excluded | set(config["ignore"])}
    groups = []
    for query, batch in zip(config["queries"], batches):
        group = []
        for item in batch:
            try:
                name = repo_name(item["full_name"])
                if item["html_url"].lower() != f"https://github.com/{name}":
                    continue
                if name in excluded or any(item.get(k) is not False for k in ("private", "fork", "archived")):
                    continue
                license_id = (item.get("license") or {}).get("spdx_id")
                if not isinstance(license_id, str) or license_id in {"", "NOASSERTION", "NONE"}:
                    continue
                stars = item["stargazers_count"]
                if type(stars) is not int or stars < config["min_stars"]:
                    continue
                if any(not today - timedelta(days=config[days]) <= date.fromisoformat(item[field][:10]) <= today
                       for field, days in (("created_at", "created_days"), ("pushed_at", "pushed_days"))):
                    continue
                group.append(dict(item, topic=query["topic"]))
            except (KeyError, TypeError, ValueError, AttributeError):
                continue
        groups.append(sorted(group, key=lambda x: (-x["stargazers_count"], x["full_name"].lower())))
    start = (today.toordinal() - today.weekday()) // 7 % len(groups)
    groups = groups[start:] + groups[:start]
    selected = []
    while any(groups) and len(selected) < config["max_candidates"]:
        for group in groups:
            while group and repo_name(group[0]["full_name"]) in excluded:
                group.pop(0)
            if group and len(selected) < config["max_candidates"]:
                item = group.pop(0)
                selected.append(item)
                excluded.add(repo_name(item["full_name"]))
    return selected


def safe_text(value):
    value = " ".join("".join(c for c in str(value or "") if c.isprintable() or c.isspace()).split())[:300]
    value = html.escape(value).replace("@", "＠")
    return re.sub(r"([\\`*_{}\[\]()#+.!|~])", r"\\\1", value)


def render_report(candidates, week, config):
    lines = [f"<!-- ai-toolkit-discovery:week {week} -->", f"# Tool discovery — {week}", "",
             "Unreviewed candidates, not recommendations. Installation and compatibility are unverified.", "",
             f"Searched {len(config['queries'])} topics: created within {config['created_days']} days, "
             f"pushed within {config['pushed_days']} days, at least {config['min_stars']} stars.", ""]
    if not candidates:
        lines.append("No new qualifying candidates. No issue created.")
    for item in candidates:
        name = repo_name(item["full_name"])
        lines += [f"<!-- ai-toolkit-discovery:candidate {name} -->",
                  f"- [{safe_text(item['full_name'])}](https://github.com/{item['full_name']}) — "
                  f"{item['stargazers_count']} stars; license: {safe_text(item['license']['spdx_id'])}.",
                  f"  {safe_text(item.get('description')) or 'No description provided.'}",
                  f"  Discovery reason: matches **{safe_text(item['topic'])}** and the activity thresholds.", ""]
    return "\n".join(lines) + "\n"


def gh_api(*args, payload=None):
    try:
        result = subprocess.run(["gh", "api", "--hostname", "github.com", *args],
                                input=json.dumps(payload) if payload is not None else None,
                                text=True, capture_output=True, check=True, timeout=90)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as error:
        raise RuntimeError("GitHub API command failed; check authentication or rate limits and retry") from error
    return json.loads(result.stdout)


def discover(config, manifest, repo, publish, today):
    repo = repo_name(repo)
    excluded = {repo_name(item["repo"]) for item in manifest["tools"]}
    year, week, _ = today.isocalendar()
    week = f"{year}-W{week:02}"
    pages = gh_api(f"repos/{repo}/issues", "--method", "GET", "-f", "state=all",
                   "-F", "per_page=100", "--paginate", "--slurp")
    existing = None
    if not isinstance(pages, list) or any(not isinstance(page, list) for page in pages):
        raise ValueError("Invalid GitHub issue history response")
    for page in pages:
        for issue in page:
            if not isinstance(issue, dict):
                raise ValueError("Invalid GitHub issue history response")
            user = issue.get("user") or {}
            if not isinstance(user, dict):
                continue
            login = str(user.get("login", "")).lower()
            if not (login == repo.split("/")[0]
                    or (login == "github-actions[bot]" and user.get("type") == "Bot")):
                continue
            body = issue.get("body") or ""
            marker = WEEK_MARKER.match(body)
            if not marker or "pull_request" in issue:
                continue
            excluded.update(repo_name(name) for name in CANDIDATE_MARKER.findall(body))
            if marker[1] == week:
                existing = int(issue["number"])
    if existing is not None:
        return f"Discovery report for {week} already exists: https://github.com/{repo}/issues/{existing}\nExisting issue and human notes preserved.\n"
    batches = []
    for query in config["queries"]:
        terms = (f"{query['query']} created:>={today - timedelta(days=config['created_days'])} "
                 f"pushed:>={today - timedelta(days=config['pushed_days'])} stars:>={config['min_stars']} "
                 "archived:false fork:false is:public")
        result = gh_api("search/repositories", "--method", "GET", "-f", f"q={terms}",
                        "-f", "sort=stars", "-f", "order=desc", "-F", f"per_page={config['per_query_limit']}")
        if (not isinstance(result, dict) or result.get("incomplete_results") is not False
                or not isinstance(result.get("items"), list)):
            raise ValueError("Incomplete or invalid GitHub search response; no report published")
        batches.append(result["items"])
    candidates = select_candidates(batches, config, excluded, today)
    report = render_report(candidates, week, config)
    if publish and candidates:
        result = gh_api(f"repos/{repo}/issues", "--method", "POST", "--input", "-",
                        payload={"title": f"Tool discovery: {week}", "body": report})
        report += f"\nPublished: https://github.com/{repo}/issues/{int(result['number'])}\n"
    elif candidates:
        report += "\nDry run: use --publish to create the weekly issue.\n"
    return report


def main(argv=None, *, today=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY"), help="GitHub owner/repository")
    parser.add_argument("--config", type=Path, default=ROOT / "config/tool-discovery.json")
    parser.add_argument("--manifest", type=Path, default=ROOT / "manifest.json")
    parser.add_argument("--publish", action="store_true", help="Create one issue if this week has no report")
    args = parser.parse_args(argv)
    try:
        config = validate_config(json.loads(args.config.read_text()))
        report = discover(config, json.loads(args.manifest.read_text()), args.repo, args.publish,
                          today or datetime.now(timezone.utc).date())
        print(report, end="")
        if os.environ.get("GITHUB_STEP_SUMMARY"):
            with Path(os.environ["GITHUB_STEP_SUMMARY"]).open("a") as summary:
                summary.write(report)
        return 0
    except (OSError, ValueError, TypeError, KeyError, RuntimeError) as error:
        print(f"Discovery failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
