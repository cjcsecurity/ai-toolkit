"""Weekly discovery behavior; GitHub is the only mocked dependency."""
import contextlib
from datetime import date
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts import discover_tools as discovery

TODAY = date(2026, 10, 5)
BOT = {"login": "github-actions[bot]", "type": "Bot"}


def config():
    return dict(queries=[dict(topic=f"topic-{n}", query=f"topic:topic-{n}") for n in range(7)],
                created_days=180, pushed_days=90, min_stars=20, per_query_limit=20,
                max_candidates=5, ignore=[])


def repository(name="example/tool", **changes):
    result = dict(full_name=name, html_url=f"https://github.com/{name}", description="Useful tool",
                  private=False, fork=False, archived=False, license={"spdx_id": "MIT"},
                  stargazers_count=25, created_at="2026-09-01T12:00:00Z",
                  pushed_at="2026-10-01T12:00:00Z")
    result.update(changes)
    return result


class DiscoverySelectionTests(unittest.TestCase):
    def test_filters_catalog_ignore_seen_and_duplicate_case_insensitively(self):
        batches = [[repository("CATALOG/tool"), repository("ignore/tool"), repository("seen/tool"),
                    repository("new/tool"), repository("NEW/tool")], [], [], [], [], [], []]
        settings = config()
        settings["ignore"] = ["IGNORE/tool"]
        chosen = discovery.select_candidates(batches, settings, {"catalog/tool", "seen/tool"}, TODAY)
        self.assertEqual([item["full_name"] for item in chosen], ["new/tool"])

    def test_rejects_unqualified_repositories(self):
        changes = [dict(private=True), dict(fork=True), dict(archived=True), dict(license=None),
                   dict(license={"spdx_id": "NOASSERTION"}), dict(stargazers_count=19),
                   dict(created_at="2025-01-01T00:00:00Z"), dict(pushed_at="2026-01-01T00:00:00Z"),
                   dict(html_url="https://evil.invalid/tool"), dict(full_name="../tool"),
                   dict(private=None), dict(created_at="not a date")]
        for change in changes:
            with self.subTest(change=change):
                self.assertEqual(discovery.select_candidates([[repository(**change)]] + [[]] * 6,
                                                           config(), set(), TODAY), [])

    def test_rotation_diversifies_limits_and_ranking_are_stable(self):
        batches = [[repository(f"topic{n}/low", stargazers_count=21),
                    repository(f"topic{n}/high", stargazers_count=90)] for n in range(7)]
        first = discovery.select_candidates(batches, config(), set(), TODAY)
        self.assertEqual(len(first), 5)
        self.assertEqual(len({item["topic"] for item in first}), 5)
        self.assertTrue(all(item["full_name"].endswith("/high") for item in first))
        self.assertEqual(first, discovery.select_candidates(batches, config(), set(), date(2026, 10, 11)))
        next_week = discovery.select_candidates(batches, config(), set(), date(2026, 10, 12))
        self.assertNotEqual({x["topic"] for x in first}, {x["topic"] for x in next_week})

    def test_backfills_from_available_topics_without_duplicates(self):
        batches = [[repository(f"example/tool{n}") for n in range(8)]] + [[]] * 6
        chosen = discovery.select_candidates(batches, config(), set(), TODAY)
        self.assertEqual(len(chosen), 5)
        self.assertEqual(len({item["full_name"] for item in chosen}), 5)

    def test_validates_configuration_bounds_and_repository_identifiers(self):
        self.assertEqual(discovery.validate_config(config()), config())
        invalid = [dict(max_candidates=6), dict(per_query_limit=101), dict(min_stars=-1),
                   dict(created_days=True), dict(pushed_days=0), dict(queries=[]),
                   dict(queries=[dict(topic="x", query="x")] * 7),
                   dict(ignore=["https://github.com/owner/repo"]), dict(unknown=True)]
        for changes in invalid:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                discovery.validate_config(dict(config(), **changes))
        for name in ["../repo", "owner/..", "owner/repo/extra", "owner/repo?x", "-owner/repo", "x@y/repo"]:
            with self.subTest(name=name), self.assertRaises(ValueError):
                discovery.repo_name(name)

    def test_report_neutralizes_untrusted_markup_and_mentions(self):
        item = repository(description="@everyone <img src=x> [click](javascript:evil) `code`\nnext\x1b[31m")
        item["topic"] = "MCP"
        report = discovery.render_report([item], "2026-W41", config())
        self.assertIn("https://github.com/example/tool", report)
        self.assertIn("MIT", report)
        self.assertIn("25 stars", report)
        self.assertIn("Unreviewed candidates", report)
        self.assertNotIn("@everyone", report)
        self.assertNotIn("<img", report)
        self.assertNotIn("[click](", report)
        self.assertNotIn("`code`", report)
        self.assertNotIn("\x1b", report)
        self.assertIn("<!-- ai-toolkit-discovery:candidate example/tool -->", report)


class DiscoveryCommandTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.config = self.root / "config.json"
        self.config.write_text(json.dumps(config()))
        self.manifest = self.root / "manifest.json"
        self.manifest.write_text(json.dumps({"tools": [{"repo": "catalog/existing"}]}))
        self.args = ["--repo", "catalog/toolkit", "--config", str(self.config),
                     "--manifest", str(self.manifest)]
        self.pages = [[]]
        self.results = [repository(), repository("catalog/existing")]
        self.reads = []
        self.writes = []
        self.failure = None
        self.search_response = None

    def gh(self, command, **kwargs):
        self.assertEqual(command[:2], ["gh", "api"])
        if "POST" in command:
            self.writes.append(json.loads(kwargs["input"]))
            response = dict(html_url="https://github.com/catalog/toolkit/issues/10", number=10)
        else:
            self.reads.append(command)
            if self.failure == len(self.reads):
                raise subprocess.CalledProcessError(1, command, stderr="API unavailable")
            if "search/repositories" in command:
                response = (self.search_response if self.search_response is not None else
                            dict(total_count=len(self.results), incomplete_results=False, items=self.results))
            else:
                self.assertIn("repos/catalog/toolkit/issues", command)
                self.assertIn("state=all", command)
                self.assertIn("--paginate", command)
                self.assertIn("--slurp", command)
                response = self.pages
        return subprocess.CompletedProcess(command, 0, stdout=json.dumps(response), stderr="")

    def invoke(self, publish=False):
        out, err = io.StringIO(), io.StringIO()
        with patch.object(subprocess, "run", side_effect=self.gh), contextlib.redirect_stdout(out), \
                contextlib.redirect_stderr(err), patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": str(self.root / "summary")}):
            code = discovery.main(self.args + (["--publish"] if publish else []), today=TODAY)
        return code, out.getvalue(), err.getvalue()

    def test_dry_run_reports_and_summarizes_without_writes(self):
        code, report, error = self.invoke()
        self.assertEqual((code, error), (0, ""))
        self.assertIn("example/tool", report)
        self.assertNotIn("catalog/existing", report)
        self.assertEqual(self.writes, [])
        self.assertEqual(len(self.reads), 8)
        self.assertIn("example/tool", (self.root / "summary").read_text())
        for command in self.reads[1:]:
            query = next(x for x in command if x.startswith("q="))
            self.assertIn("created:>=2026-04-08", query)
            self.assertIn("pushed:>=2026-07-07", query)
            self.assertIn("stars:>=20", query)
            self.assertIn("per_page=20", command)

    def test_publish_creates_one_issue_after_all_reads(self):
        code, report, error = self.invoke(publish=True)
        self.assertEqual((code, error), (0, ""))
        self.assertEqual(len(self.writes), 1)
        self.assertEqual(len(self.reads), 8)
        self.assertIn("2026-W41", self.writes[0]["title"])
        self.assertTrue(self.writes[0]["body"].startswith("<!-- ai-toolkit-discovery:week 2026-W41 -->\n"))
        self.assertIn("example/tool", self.writes[0]["body"])
        self.assertIn("issues/10", report)

    def test_existing_week_skips_closed_issue_and_preserves_human_notes(self):
        body = "<!-- ai-toolkit-discovery:week 2026-W41 -->\nHuman notes: keep this."
        self.pages = [[], [dict(number=8, state="closed", body=body, user=BOT)]]
        code, report, error = self.invoke(publish=True)
        self.assertEqual((code, error), (0, ""))
        self.assertIn("already exists", report)
        self.assertIn("issues/8", report)
        self.assertEqual(self.pages[1][0]["body"], body)
        self.assertEqual(self.writes, [])
        self.assertEqual(len(self.reads), 1)

    def test_previous_closed_reports_suppress_seen_repositories(self):
        body = "<!-- ai-toolkit-discovery:week 2026-W40 -->\n<!-- ai-toolkit-discovery:candidate EXAMPLE/tool -->"
        self.pages = [[], [dict(number=5, state="closed", body=body, user=BOT)]]
        code, report, error = self.invoke(publish=True)
        self.assertEqual((code, error), (0, ""))
        self.assertIn("No new qualifying candidates", report)
        self.assertEqual(self.writes, [])

    def test_other_issues_and_pull_requests_do_not_suppress_candidates(self):
        marker = "<!-- ai-toolkit-discovery:week 2026-W41 -->\n<!-- ai-toolkit-discovery:candidate example/tool -->"
        self.pages = [[dict(number=2, body="Human discussion quoting:\n" + marker, user=BOT),
                       dict(number=3, body=marker, pull_request={"url": "ignored"}, user=BOT),
                       dict(number=4, body="<!-- thin-loop -->\n" + marker, user=BOT)]]
        code, report, error = self.invoke()
        self.assertEqual((code, error), (0, ""))
        self.assertIn("example/tool", report)
        self.assertEqual(len(self.reads), 8)

    def test_untrusted_authors_cannot_suppress_week_or_candidates(self):
        users = [None, {"login": "public-user", "type": "User"},
                 {"login": "github-actions[bot]", "type": "User"},
                 {"login": "other-app[bot]", "type": "Bot"}]
        for user in users:
            for week in ("2026-W40", "2026-W41"):
                with self.subTest(user=user, week=week):
                    self.reads.clear()
                    body = f"<!-- ai-toolkit-discovery:week {week} -->\n<!-- ai-toolkit-discovery:candidate example/tool -->"
                    self.pages = [[dict(number=9, body=body, user=user, author_association="MEMBER")]]
                    code, report, error = self.invoke()
                    self.assertEqual((code, error), (0, ""))
                    self.assertIn("https://github.com/example/tool", report)
                    self.assertEqual(len(self.reads), 8)

    def test_repository_owner_reports_are_trusted_case_insensitively(self):
        self.args[1] = "CATALOG/toolkit"
        for week, expected in [("2026-W40", "No new qualifying candidates"),
                               ("2026-W41", "already exists")]:
            with self.subTest(week=week):
                body = f"<!-- ai-toolkit-discovery:week {week} -->\n<!-- ai-toolkit-discovery:candidate example/tool -->"
                self.pages = [[dict(number=9, body=body, user={"login": "Catalog", "type": "User"})]]
                code, report, error = self.invoke(publish=True)
                self.assertEqual((code, error), (0, ""))
                self.assertIn(expected, report)
                self.assertEqual(self.writes, [])

    def test_api_failures_on_history_or_last_search_never_publish(self):
        for failure in (1, 8):
            with self.subTest(failure=failure):
                self.reads.clear()
                self.failure = failure
                code, report, error = self.invoke(publish=True)
                self.assertNotEqual(code, 0)
                self.assertIn("failed", error.lower())
                self.assertEqual(self.writes, [])

    def test_invalid_config_fails_before_api_calls(self):
        self.config.write_text(json.dumps(dict(config(), max_candidates=10)))
        code, _, error = self.invoke(publish=True)
        self.assertNotEqual(code, 0)
        self.assertIn("max_candidates", error)
        self.assertEqual(self.reads, [])
        self.assertEqual(self.writes, [])

    def test_malformed_or_incomplete_api_data_fails_without_publishing(self):
        for response in [[], {"incomplete_results": True, "items": [repository()]}]:
            with self.subTest(response=response):
                self.search_response = response
                code, _, error = self.invoke(publish=True)
                self.assertNotEqual(code, 0)
                self.assertIn("response", error)
                self.assertEqual(self.writes, [])
        self.search_response = None
        self.pages = [[None]]
        code, _, error = self.invoke(publish=True)
        self.assertNotEqual(code, 0)
        self.assertIn("response", error)
        self.assertEqual(self.writes, [])


if __name__ == "__main__":
    unittest.main()
