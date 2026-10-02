"""Real CPU model checks; run with runtime/search/bin/python -m unittest discover -s tests."""
import importlib.util
from pathlib import Path
import socket
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
AVAILABLE = importlib.util.find_spec('fastembed') is not None


class LocalEmbeddingTests(unittest.TestCase):
    def test_missing_model_fails_locally_with_setup_instructions(self):
        from embeddings import LocalEmbedder
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(socket.socket, 'connect', side_effect=AssertionError('network')):
                with self.assertRaisesRegex(RuntimeError, 'setup'):
                    LocalEmbedder(Path(directory))

    def test_changed_model_file_is_rejected_before_loading(self):
        from embeddings import LocalEmbedder, MODEL_RELATIVE_PATH
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / MODEL_RELATIVE_PATH
            path.mkdir(parents=True)
            (path / 'config.json').write_text('{}')
            with self.assertRaisesRegex(RuntimeError, 'checksum mismatch'):
                LocalEmbedder(Path(directory))

    @unittest.skipUnless(AVAILABLE, 'optional search runtime is not installed')
    @unittest.skipUnless((ROOT / 'runtime/search/models/all-MiniLM-L6-v2/model.onnx').exists(),
                         'optional model is not installed')
    def test_real_model_matches_paraphrase_offline_and_normalizes_vectors(self):
        import numpy as np
        from embeddings import LocalEmbedder
        with patch.object(socket.socket, 'connect', side_effect=AssertionError('network')):
            model = LocalEmbedder()
            documents = model.embed_documents([
                'Durable execution with checkpoint recovery resumes interrupted workflows.',
                'Create beautiful animated characters and pixel art sprite sheets.',
                'Financial statements, quarterly revenue and balance sheet accounting.',
            ])
            query = model.embed_query('pick up where it left off after a crash')
            scores = documents @ query
            self.assertEqual(int(scores.argmax()), 0)
            self.assertGreater(float(scores[0] - scores[1:].max()), 0.1)
            self.assertEqual(documents.shape, (3, 384))
            self.assertEqual(documents.dtype, np.float32)
            self.assertEqual(query.shape, (384,))
            self.assertEqual(query.dtype, np.float32)
            np.testing.assert_allclose(np.linalg.norm(documents, axis=1), 1.0, atol=1e-6)
            self.assertAlmostEqual(float(np.linalg.norm(query)), 1.0, places=6)
            self.assertEqual(model.embed_documents([]).shape, (0, 384))
            batches = model.embed_documents([
                'Durable execution with checkpoint recovery resumes interrupted workflows.',
                'Create beautiful animated characters and pixel art sprite sheets.',
                'Financial statements, quarterly revenue and balance sheet accounting.',
            ] * 12)
            self.assertEqual(batches.shape, (36, 384))
            # Padding and floating point batch operations can cause tiny differences.
            np.testing.assert_allclose(batches @ query, np.tile(scores, 12), atol=0.01)

    @unittest.skipUnless(AVAILABLE, 'optional search runtime is not installed')
    @unittest.skipUnless((ROOT / 'runtime/search/models/all-MiniLM-L6-v2/model.onnx').exists(),
                         'optional model is not installed')
    def test_relevant_tail_beyond_context_limit_changes_semantic_match(self):
        from embeddings import LocalEmbedder
        model = LocalEmbedder()
        prefix = 'Gardening soil flowers sunshine watering green plants. ' * 45
        recovery = ' Durable workflows recover saved checkpoints and resume after crashes.' * 12
        accounting = ' Financial statements report quarterly revenue and balance sheet accounts.' * 12
        vectors = model.embed_documents([prefix + recovery, prefix + accounting])
        scores = vectors @ model.embed_query('pick up where it left off after a crash')
        self.assertGreater(float(scores[0] - scores[1]), 0.1)


if __name__ == '__main__':
    unittest.main()
