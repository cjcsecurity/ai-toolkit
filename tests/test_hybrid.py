import importlib.util
import sqlite3
import tempfile
import unittest
from pathlib import Path

import hybrid

HAS_NUMPY = importlib.util.find_spec('numpy') is not None


class HybridTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.db = sqlite3.connect(':memory:')
        self.db.row_factory = sqlite3.Row
        self.addCleanup(self.db.close)
        self.records = [
            dict(uid='checkpoint', repo_id='platform', repo='demo/platform', kind='skill', name='durable-execution', path='skills/durable/SKILL.md', start_line=1, end_line=8, text='Persist checkpoints and recover interrupted execution.', content_hash='a'),
            dict(uid='colors', repo_id='platform', repo='demo/platform', kind='skill', name='palette-design', path='skills/palette/SKILL.md', start_line=1, end_line=8, text='Choose accessible colors and typography.', content_hash='b'),
            dict(uid='other', repo_id='other', repo='demo/other', kind='doc', name='Checkpoint reference', path='docs/checkpoint.md', start_line=12, end_line=20, text='Persist checkpoints in durable storage.', content_hash='c'),
        ]
        hybrid.populate(self.db, self.records)

    def test_lexical_search_finds_internal_skill_without_repo_summary(self):
        rows, mode = hybrid.retrieve(self.db, 'accessible colors', self.root, lexical_only=True)
        self.assertEqual(rows[0]['uid'], 'colors')
        self.assertEqual(rows[0]['path'], 'skills/palette/SKILL.md')
        self.assertEqual(mode, 'lexical')

    def test_repository_and_kind_filters_apply_to_all_candidates(self):
        rows, _ = hybrid.retrieve(self.db, 'checkpoints', self.root, repo_id='other', kinds=['doc'], lexical_only=True)
        self.assertEqual([r['uid'] for r in rows], ['other'])
        self.assertEqual(hybrid.retrieve(self.db, 'checkpoints', self.root, repo_id='other', kinds=['skill'], lexical_only=True)[0], [])

    def test_duplicate_chunks_do_not_fill_result_slots(self):
        duplicate = dict(self.records[0], uid='checkpoint-later', start_line=9, end_line=15)
        hybrid.populate(self.db, [*self.records, duplicate])
        rows, _ = hybrid.retrieve(self.db, 'checkpoints', self.root, lexical_only=True)
        identities = [(r['repo_id'], r['path'], r['name']) for r in rows]
        self.assertEqual(len(identities), len(set(identities)))

    def test_long_skill_cannot_exhaust_candidate_pool(self):
        records = [dict(self.records[0], uid=f'chunk-{i}', start_line=i + 1) for i in range(110)]
        records.append(dict(self.records[0], uid='second', name='other-capability', path='skills/other/SKILL.md'))
        hybrid.populate(self.db, records)
        rows, _ = hybrid.retrieve(self.db, 'checkpoints', self.root, lexical_only=True)
        self.assertEqual(len(rows), 2)

    def test_repository_discovery_uses_chunks_without_counting_duplicate_votes(self):
        summaries = [dict(self.records[0], uid=rid + '-summary', repo_id=rid, kind='repo',
                          name='demo/' + rid, path='', text='General utilities')
                     for rid in ('platform', 'other')]
        hybrid.populate(self.db, [*summaries, *self.records])
        before, _ = hybrid.retrieve(self.db, 'checkpoints', self.root, kinds=['repo'], lexical_only=True)
        self.assertEqual({r['repo_id'] for r in before}, {'platform', 'other'})
        self.assertTrue(all(r['kind'] == 'repo' and r['matches'] for r in before))
        copies = [dict(self.records[0], uid=f'copy-{i}', path=f'copies/{i}.md') for i in range(120)]
        hybrid.populate(self.db, [*summaries, *self.records, *copies])
        after, _ = hybrid.retrieve(self.db, 'checkpoints', self.root, kinds=['repo'], lexical_only=True)
        self.assertEqual([(r['repo_id'], r['score']) for r in before],
                         [(r['repo_id'], r['score']) for r in after])
        filtered, _ = hybrid.retrieve(self.db, 'checkpoints', self.root, kinds=['repo'],
                                      repo_id='other', lexical_only=True)
        self.assertEqual([r['repo_id'] for r in filtered], ['other'])
        self.assertEqual(filtered[0]['matches'][0]['path'], 'docs/checkpoint.md')

    @unittest.skipUnless(HAS_NUMPY, 'optional NumPy dependency missing')
    def test_repository_vector_discovery_finds_capability_without_keyword_overlap(self):
        import numpy as np
        summary = dict(self.records[0], uid='summary', kind='repo', name='demo/platform',
                       path='', text='General utilities')
        hybrid.populate(self.db, [summary, *self.records])
        class Embedder:
            fingerprint = 'discovery-v1'
            def embed_query(self, text):
                return np.array([1, 0], dtype=np.float32)
        self.db.execute('INSERT INTO metadata VALUES (?,?)', ('embedding_fingerprint', 'discovery-v1'))
        self.db.executemany('INSERT INTO unit_vectors VALUES (?,?)', [
            (uid, np.array(vector, dtype=np.float32).tobytes())
            for uid, vector in [('summary', [0, 1]), ('checkpoint', [1, 0]), ('colors', [0, 1])]])
        rows, mode = hybrid.retrieve(self.db, 'resume where it stopped', self.root,
                                    kinds=['repo'], embedder=Embedder())
        self.assertEqual(mode, 'hybrid')
        self.assertEqual([r['repo_id'] for r in rows], ['platform'])
        self.assertIsNone(rows[0]['lexical_rank'])
        self.assertEqual(rows[0]['matches'][0]['uid'], 'checkpoint')

    @unittest.skipUnless(HAS_NUMPY, 'optional NumPy dependency missing')
    def test_repository_channels_retain_their_own_winning_passage(self):
        import numpy as np
        summary = dict(self.records[0], uid='summary', kind='repo', name='demo/platform',
                       path='', text='General utilities')
        hybrid.populate(self.db, [summary, *self.records])
        class Embedder:
            fingerprint = 'two-passages'
            def embed_query(self, text):
                return np.array([1, 0], dtype=np.float32)
        self.db.execute('INSERT INTO metadata VALUES (?,?)', ('embedding_fingerprint', 'two-passages'))
        self.db.executemany('INSERT INTO unit_vectors VALUES (?,?)', [
            (uid, np.array(vector, dtype=np.float32).tobytes())
            for uid, vector in [('summary', [0, 1]), ('checkpoint', [1, 0]), ('colors', [0, 1])]])
        rows, _ = hybrid.retrieve(self.db, 'colors', self.root, kinds=['repo'], embedder=Embedder())
        self.assertEqual(len(rows), 1)
        self.assertEqual({r['uid'] for r in rows[0]['matches']}, {'colors', 'checkpoint'})
        self.assertEqual((rows[0]['lexical_rank'], rows[0]['semantic_rank']), (1, 1))


    @unittest.skipUnless(HAS_NUMPY, 'optional NumPy dependency missing; install requirements-search.txt')
    def test_cached_vectors_are_reused_and_changed_content_is_reembedded(self):
        import numpy as np
        class Embedder:
            fingerprint = 'cache-v1'
            model_id = 'fake'
            dimension = 2
            calls = 0
            def embed_documents(self, texts):
                self.calls += len(texts)
                return np.array([[1, 0] for _ in texts], dtype=np.float32)
        model = Embedder()
        hybrid.index_vectors(self.db, self.root, embedder=model)
        self.assertEqual(model.calls, 3)
        hybrid.populate(self.db, self.records)
        result = hybrid.index_vectors(self.db, self.root, embedder=model)
        self.assertEqual(result['cached'], 3)
        self.assertEqual(model.calls, 3)
        changed = [dict(self.records[0], text='Recover crashed workflows'), *self.records[1:]]
        hybrid.populate(self.db, changed)
        hybrid.index_vectors(self.db, self.root, embedder=model)
        self.assertEqual(model.calls, 4)

    def test_unavailable_model_is_reported_as_lexical_fallback(self):
        rows, mode = hybrid.retrieve(self.db, 'colors', self.root)
        self.assertEqual(rows[0]['uid'], 'colors')
        self.assertEqual(mode, 'lexical-fallback')

    @unittest.skipUnless(HAS_NUMPY, 'optional NumPy dependency missing; install requirements-search.txt')
    def test_model_change_never_reuses_incompatible_vectors(self):
        import numpy as np
        class Embedder:
            fingerprint = 'new-model'
            dimension = 2
            def embed_query(self, text):
                raise AssertionError('Mismatched model must not perform inference')
        self.db.execute('INSERT INTO metadata VALUES (?,?)', ('embedding_fingerprint', 'old-model'))
        self.db.execute('INSERT INTO unit_vectors VALUES (?,?)', ('colors', np.array([1, 0], dtype=np.float32).tobytes()))
        rows, mode = hybrid.retrieve(self.db, 'colors', self.root, embedder=Embedder())
        self.assertEqual(mode, 'lexical-fallback')
        self.assertEqual(rows[0]['uid'], 'colors')

    @unittest.skipUnless(HAS_NUMPY, 'optional NumPy dependency missing; install requirements-search.txt')
    def test_wrong_vector_dimensions_keep_lexical_results(self):
        import numpy as np
        class Embedder:
            fingerprint = 'invalid-v1'
            dimension = 2
            def embed_query(self, text):
                return np.array([1, 0], dtype=np.float32)
        self.db.execute('INSERT INTO unit_vectors VALUES (?,?)', ('colors', np.array([1, 0, 0], dtype=np.float32).tobytes()))
        self.db.execute('INSERT INTO metadata VALUES (?,?)', ('embedding_fingerprint', 'invalid-v1'))
        rows, mode = hybrid.retrieve(self.db, 'colors', self.root, embedder=Embedder())
        self.assertEqual(rows[0]['uid'], 'colors')
        self.assertEqual(mode, 'lexical-fallback')

    @unittest.skipUnless(HAS_NUMPY, 'optional NumPy dependency missing; install requirements-search.txt')
    def test_invalid_cached_vector_is_recomputed(self):
        import numpy as np
        class Embedder:
            fingerprint = 'nan-v1'
            model_id = 'fake'
            dimension = 2
            def embed_documents(self, texts):
                return np.array([[1, 0] for _ in texts], dtype=np.float32)
        hybrid.index_vectors(self.db, self.root, embedder=Embedder())
        with sqlite3.connect(self.root / 'state/embedding-cache.sqlite3') as cache:
            cache.execute('UPDATE vectors SET vector=?', (np.array([np.nan, 0], dtype=np.float32).tobytes(),))
        hybrid.populate(self.db, self.records)
        result = hybrid.index_vectors(self.db, self.root, embedder=Embedder())
        self.assertEqual(result['cached'], 0)
        self.assertEqual(result['embedded'], 3)

    @unittest.skipUnless(HAS_NUMPY, 'optional NumPy dependency missing; install requirements-search.txt')
    def test_vector_candidate_with_no_keyword_overlap_is_retrieved(self):
        import numpy as np
        class Embedder:
            fingerprint = 'test-v1'
            dimension = 2
            def embed_query(self, text):
                return np.array([1, 0], dtype=np.float32)
        self.db.executemany('INSERT INTO unit_vectors VALUES (?,?)', [('checkpoint', np.array([1, 0], dtype=np.float32).tobytes()), ('colors', np.array([0, 1], dtype=np.float32).tobytes()), ('other', np.array([0.8, 0.6], dtype=np.float32).tobytes())])
        self.db.execute('INSERT OR REPLACE INTO metadata VALUES (?,?)', ('embedding_fingerprint', 'test-v1'))
        rows, mode = hybrid.retrieve(self.db, 'resume where it stopped', self.root, embedder=Embedder())
        self.assertEqual(rows[0]['uid'], 'checkpoint')
        self.assertEqual(mode, 'hybrid')
        self.assertIsNone(rows[0]['lexical_rank'])
        self.assertGreater(rows[0]['semantic_similarity'], 0.99)


if __name__ == '__main__':
    unittest.main()
