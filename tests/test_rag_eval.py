import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from rag_fixture import make_library
from evals.run import metrics

ROOT = Path(__file__).resolve().parents[1]


class EvaluationTests(unittest.TestCase):
    def test_evaluation_writer_preserves_large_reports(self):
        from evals import run
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / 'report.json'
            report = {'runs': [{'requested_mode': 'lexical', 'summary': {}}],
                      'evidence': 'large report\n' * 8000}
            with patch.object(run, 'evaluate', return_value=report), \
                    patch.object(sys, 'argv', ['run.py', '--output', str(output)]):
                run.main()
            self.assertEqual(json.loads(output.read_text()), report)
            self.assertEqual(sorted(p.name for p in Path(folder).iterdir()), ['report.json'])

    def test_metrics_count_misses_in_denominator(self):
        result = metrics([1, None, 3])
        self.assertAlmostEqual(result['hit_at_k'], 2/3)
        self.assertAlmostEqual(result['mrr_at_k'], 4/9)
        self.assertEqual(result['cases'], 3)
        self.assertEqual(metrics([])['hit_at_k'], None)

    def test_cli_evaluation_records_actual_fallback_and_separates_negative_cases(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); make_library(root)
            cases = root/'cases.json'
            cases.write_text(json.dumps({'version': 1, 'cases': [
                {'id': 'nested', 'split': 'development', 'task': 'search', 'query': 'checkpoints',
                 'expected': [{'repo_id': 'platform', 'names': ['durable-execution'], 'path_prefixes': []}]},
                {'id': 'negative', 'split': 'holdout', 'task': 'search', 'query': 'zzunfindable', 'expected': []},
                {'id': 'repository', 'split': 'development', 'task': 'discover', 'query': 'persist',
                 'expected': [{'repo_id': 'platform'}]},
            ]}))
            output = root/'report.json'
            proc = subprocess.run([sys.executable, str(ROOT/'evals/run.py'), '--root', str(root),
                '--cases', str(cases), '--output', str(output)], text=True, capture_output=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            report = json.loads(output.read_text())
            hybrid = next(r for r in report['runs'] if r['requested_mode'] == 'hybrid')
            self.assertEqual(hybrid['cases'][0]['actual_mode'], 'lexical-fallback')
            # The repository overview occupies rank 1 in unfiltered search.
            self.assertEqual(hybrid['cases'][0]['rank'], 2)
            self.assertIsNone(hybrid['cases'][1]['rank'])
            self.assertEqual(hybrid['cases'][2]['rank'], 1)
            self.assertTrue(hybrid['cases'][2]['references_valid'])
            self.assertIn('verified', hybrid['cases'][2]['provenance_statuses'])
            self.assertEqual(hybrid['summary']['development/search']['cases'], 1)
            self.assertNotIn('holdout/search', hybrid['summary'])
            self.assertEqual(len(report['dataset_sha256']), 64)
            self.assertEqual(len(report['index_sha256']), 64)


if __name__ == '__main__':
    unittest.main()
