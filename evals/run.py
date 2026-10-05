#!/usr/bin/env python3
"""Reproducible RAG retrieval comparison; no model API or generated-answer grader."""
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import statistics
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from rag import RagService


def file_hash(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def write_report(path, report):
    """Replace a complete evaluation report without applying project-profile limits."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(dir=path.parent, prefix='.' + path.name)
    try:
        with os.fdopen(descriptor, 'w', encoding='utf-8') as stream:
            json.dump(report, stream, ensure_ascii=False, indent=2)
            stream.write('\n')
        os.replace(name, path)
    finally:
        Path(name).unlink(missing_ok=True)


def metrics(ranks):
    """First relevant result metrics; partial relevance labels are not recall labels."""
    count = len(ranks)
    return dict(cases=count, hits=sum(r is not None for r in ranks),
                hit_at_k=sum(r is not None for r in ranks)/count if count else None,
                mrr_at_k=sum(1/r for r in ranks if r is not None)/count if count else None)


def matches(row, expected, task):
    # Preserve the historical capability matcher's named/path-prefix semantics.
    return any(row['id'] == e['repo_id'] and (
        task == 'recommend' or (row.get('kind') != 'repo' and (
            row.get('name') in e.get('names', []) or
            any(row.get('path', '').startswith(p) for p in e.get('path_prefixes', [])))))
        for e in expected)


def evaluate(root, cases_path, *, limit=5, split='all', task='all'):
    root = Path(root)
    dataset = json.loads(Path(cases_path).read_text())
    cases = [c for c in dataset['cases'] if (split == 'all' or c['split'] == split)
             and (task == 'all' or c['task'] == task)]
    if not cases:
        raise ValueError('No evaluation cases selected')
    if not 1 <= limit <= 20:
        raise ValueError('limit must be 1..20')
    before = file_hash(root/'index.sqlite3')
    report = dict(schema_version=1, evaluated_at=datetime.now(timezone.utc).isoformat(),
                  dataset_sha256=file_hash(cases_path), index_sha256=before, limit=limit, budget=64000,
                  implementation_sha256={p: file_hash(ROOT/p) for p in
                      ['rag.py', 'rag_sources.py', 'hybrid.py', 'corpus.py', 'embeddings.py', 'evals/run.py']},
                  notes=[
                      'Labels identify designated relevant sources, not all relevant results; hit@k is not recall.',
                      'Development labels predate this extension; holdout labels were written before this evaluation.',
                      'Holdout denotes new repository-selection labels, not wholly unseen query phrasing; adaptive_parser overlaps a development case.',
                      'Fresh service per mode; first query includes lazy model initialization. Subsequent queries reuse it.',
                      'Times include retrieval, source verification and JSON budget assembly, but exclude subprocess/host startup.',
                      'Unsupported-query results are observations, not a calibrated abstention score.',
                      'Constraint satisfaction and generated-answer faithfulness require separate review.',
                  ], runs=[])
    for mode in ('lexical', 'hybrid'):
        service = RagService(root)
        run = dict(requested_mode=mode, cases=[], summary={})
        groups = defaultdict(list)
        durations = []
        for case in cases:
            started = time.perf_counter()
            if case['task'] == 'recommend':
                payload = service.recommend(case['query'], constraints=case.get('constraints', ''),
                                            limit=limit, lexical_only=mode == 'lexical', budget=64000)
                rows = payload['candidates']
            else:
                payload = service.search(case['query'], limit=limit, lexical_only=mode == 'lexical', budget=64000)
                rows = payload['results']
            elapsed = time.perf_counter() - started
            durations.append(elapsed)
            expected = case.get('expected', [])
            rank = next((i+1 for i, row in enumerate(rows) if matches(row, expected, case['task'])), None)
            if expected:
                groups[case['split'] + '/' + case['task']].append(rank)
            ids = {s['source_id'] for s in payload['sources']}
            refs = {s for row in rows for s in row['evidence']}
            result = dict(id=case['id'], split=case['split'], task=case['task'], query=case['query'],
                          expected=expected, constraints=case.get('constraints', ''), rank=rank,
                          actual_mode=payload['retrieval']['mode'], fallback_reason=payload['retrieval']['fallback_reason'],
                          seconds=round(elapsed, 4), result_count=len(rows), truncated=payload['truncated'],
                          references_valid=ids == refs and all(row['evidence'] for row in rows),
                          provenance_statuses=sorted({s['provenance']['status'] for s in payload['sources']}),
                          results=[{k: row[k] for k in ('id', 'name', 'kind', 'path') if k in row} for row in rows])
            run['cases'].append(result)
            run['index'] = payload['index']
            print(f"{mode}: {case['id']}: rank={rank} ({elapsed:.2f}s)", file=sys.stderr, flush=True)
        run['summary'] = {key: metrics(ranks) for key, ranks in groups.items()}
        run['latency'] = dict(first_query_seconds=round(durations[0], 4),
                              subsequent_query_median_seconds=round(statistics.median(durations[1:]), 4) if len(durations) > 1 else None,
                              maximum_seconds=round(max(durations), 4))
        report['runs'].append(run)
    if file_hash(root/'index.sqlite3') != before:
        raise RuntimeError('Index changed during evaluation; rerun against one published index')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--cases', type=Path, default=ROOT/'evals/cases.json')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--limit', type=int, default=5)
    parser.add_argument('--split', choices=['all', 'development', 'holdout'], default='all')
    parser.add_argument('--task', choices=['all', 'search', 'recommend'], default='all')
    args = parser.parse_args()
    report = evaluate(args.root, args.cases, limit=args.limit, split=args.split, task=args.task)
    write_report(args.output, report)
    print(json.dumps({r['requested_mode']: r['summary'] for r in report['runs']}, indent=2))


if __name__ == '__main__':
    main()
