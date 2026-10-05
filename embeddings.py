"""Pinned, CPU-only local embeddings. Network access is exclusive to ``setup``.

Install: uv venv --python 3.12 runtime/search
         uv pip sync --python runtime/search/bin/python requirements-search.txt
Download: runtime/search/bin/python embeddings.py setup
"""
from __future__ import annotations

import argparse
import hashlib
from importlib.metadata import version
import json
import os
from pathlib import Path

ROOT = Path(os.environ.get('AI_TOOLKIT_HOME', Path(__file__).resolve().parent)).expanduser().resolve()
MODEL_ID = 'sentence-transformers/all-MiniLM-L6-v2'
MODEL_REPO = 'Qdrant/all-MiniLM-L6-v2-onnx'
MODEL_REVISION = 'd13954661f83248295ba75c1ed411eef3b7b936e'
MODEL_RELATIVE_PATH = Path('runtime/search/models/all-MiniLM-L6-v2')
FASTEMBED_VERSION = '0.8.0'
QUERY_PREFIX = ''
WINDOW_TOKENS = 220
WINDOW_OVERLAP = 32
MODEL_HASHES = {
    'config.json': '1b4d8e2a3988377ed8b519a31d8d31025a25f1c5f8606998e8014111438efcd7',
    'model.onnx': 'bbd7b466f6d58e646fdc2bd5fd67b2f5e93c0b687011bd4548c420f7bd46f0c5',
    'special_tokens_map.json': '5d5b662e421ea9fac075174bb0688ee0d9431699900b90662acd44b2a350503a',
    'tokenizer.json': '851ca67100d372ca3ae031a6abd168f53489eebfd7d89523f35c5c9b4d372c3c',
    'tokenizer_config.json': 'abda01c8c14c5151ae498aceb30db406d6b91242c394fd88d3b6fd5a63a101e6',
    'vocab.txt': '07eced375cec144d27c900241f3e339478dec958f92fddbc551f295c992038a3',
}


class EmbeddingUnavailable(RuntimeError):
    """Local search dependencies or the reviewed model are unavailable."""


def verify_model(path: Path) -> None:
    """Fail before inference if a local checkpoint is absent or has changed."""
    for name, expected in MODEL_HASHES.items():
        file = path / name
        if not file.is_file():
            raise EmbeddingUnavailable(
                f'Local embedding model missing: {file}. Run '
                'runtime/search/bin/python embeddings.py setup explicitly to download it.'
            )
        with file.open('rb') as stream:
            actual = hashlib.file_digest(stream, 'sha256').hexdigest()
        if actual != expected:
            raise EmbeddingUnavailable(f'Local embedding model checksum mismatch: {file}; rerun setup.')


class LocalEmbedder:
    """Normalized 384D float32 vectors, with no inference service or query networking."""

    model_id = MODEL_ID
    dimension = 384

    def __init__(self, root: Path = ROOT, *, threads: int = 12, batch_size: int = 8):
        self.model_path = Path(root) / MODEL_RELATIVE_PATH
        verify_model(self.model_path)
        try:
            import numpy as np
            from fastembed import TextEmbedding
            from tokenizers import Tokenizer
        except ImportError as exc:
            raise EmbeddingUnavailable(
                'Local embedding runtime missing; install requirements-search.txt in runtime/search.'
            ) from exc
        if version('fastembed') != FASTEMBED_VERSION:
            raise EmbeddingUnavailable('Embedding runtime version differs from requirements-search.txt.')
        if threads < 1 or batch_size < 1:
            raise ValueError('threads and batch_size must be positive')
        self._np = np
        self.batch_size = batch_size
        self._tokenizer = Tokenizer.from_file(str(self.model_path / 'tokenizer.json'))
        self._tokenizer.no_truncation()
        self._tokenizer.no_padding()
        self.fingerprint = json.dumps({
            'model': MODEL_ID, 'repository': MODEL_REPO, 'revision': MODEL_REVISION,
            'files': MODEL_HASHES, 'fastembed': version('fastembed'),
            'onnxruntime': version('onnxruntime'), 'tokenizers': version('tokenizers'),
            'numpy': version('numpy'), 'query_prefix': QUERY_PREFIX,
            'normalization': 'l2-float32-v1',
            'passage_encoding': 'overlapping-offset-windows-normalized-mean-v1',
            'window_tokens': WINDOW_TOKENS, 'window_overlap': WINDOW_OVERLAP,
        }, sort_keys=True, separators=(',', ':'))
        self._model = TextEmbedding(
            model_name=MODEL_ID, specific_model_path=str(self.model_path),
            cache_dir=str(self.model_path.parent), local_files_only=True,
            providers=['CPUExecutionProvider'], threads=threads,
        )

    def _windows(self, text: str) -> list[str]:
        """Preserve every token using overlapping original-text slices within model capacity."""
        encoding = self._tokenizer.encode(text, add_special_tokens=False)
        count = len(encoding.ids)
        if count <= WINDOW_TOKENS:
            return [text]
        starts = list(range(0, count - WINDOW_TOKENS + 1, WINDOW_TOKENS - WINDOW_OVERLAP))
        if starts[-1] != count - WINDOW_TOKENS:
            starts.append(count - WINDOW_TOKENS)
        windows = []
        for start in starts:
            left = encoding.offsets[start][0]
            right = encoding.offsets[start + WINDOW_TOKENS - 1][1]
            segment = text[left:right]
            # A cut through a word can change its tokenization. Check the actual
            # re-encoded text, reserving two slots for CLS/SEP special tokens.
            if len(self._tokenizer.encode(segment, add_special_tokens=False).ids) > 254:
                windows.extend(self._windows(segment))
            else:
                windows.append(segment)
        return windows

    def embed_documents(self, texts: list[str]):
        """Pool all overlapping token windows, retaining passage order and complete coverage."""
        np = self._np
        if not texts:
            return np.empty((0, self.dimension), dtype=np.float32)
        windows = []
        ranges = []
        for text in texts:
            start = len(windows)
            windows.extend(self._windows(text))
            ranges.append((start, len(windows)))
        vectors = np.asarray(list(self._model.embed(windows, batch_size=self.batch_size)), dtype=np.float32)
        norms = np.linalg.norm(vectors, axis=1, keepdims=True)
        if not np.isfinite(vectors).all() or np.any(norms == 0):
            raise RuntimeError('Embedding model returned invalid vectors')
        vectors /= norms
        pooled = np.asarray([vectors[start:end].mean(axis=0) for start, end in ranges], dtype=np.float32)
        norms = np.linalg.norm(pooled, axis=1, keepdims=True)
        if np.any(norms == 0):
            raise RuntimeError('Embedding windows cancelled to a zero vector')
        return pooled / norms

    def embed_query(self, text: str):
        """MiniLM uses the same encoding for queries and documents, without instructions."""
        return self.embed_documents([QUERY_PREFIX + text])[0]


def setup(root: Path = ROOT) -> Path:
    """Explicit opt-in network operation downloading only one immutable checkpoint."""
    from huggingface_hub import snapshot_download
    destination = Path(root) / MODEL_RELATIVE_PATH
    snapshot_download(
        MODEL_REPO, revision=MODEL_REVISION, local_dir=destination,
        allow_patterns=list(MODEL_HASHES),
    )
    verify_model(destination)
    return destination


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['setup', 'verify'])
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    if args.command == 'setup':
        print(setup(args.root))
    else:
        verify_model(args.root / MODEL_RELATIVE_PATH)
        print('Pinned local model checksums verified.')
