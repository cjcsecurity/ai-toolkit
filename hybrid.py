"""Capability-level lexical/vector retrieval with persistent local embedding cache."""
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import sys

SCHEMA_VERSION = '2'
# Sharper decay preserves strong single-channel matches among weak shared hits.
RRF_K = 20
STOP = set('a an the i we you our your to for with and or of in on from use using need want tools tool project that can is are how do me my find something help please would like have has it its this which'.split())


def query_text(query):
    words = [t for t in re.findall(r'\w+', query.lower()) if t not in STOP and len(t) > 1][:32]
    return ' OR '.join('"' + t + '"' for t in words)


def populate(conn, records):
    from corpus import embedding_text
    conn.executescript('''
        CREATE TABLE IF NOT EXISTS metadata(key TEXT PRIMARY KEY, value TEXT);
        DROP TABLE IF EXISTS units;
        DROP TABLE IF EXISTS unit_search;
        DROP TABLE IF EXISTS unit_vectors;
        CREATE TABLE units(uid TEXT PRIMARY KEY, repo_id TEXT, kind TEXT, name TEXT, path TEXT,
          start_line INTEGER, end_line INTEGER, description TEXT, text TEXT, embed_text TEXT, content_hash TEXT);
        CREATE INDEX units_repo_kind ON units(repo_id,kind);
        CREATE VIRTUAL TABLE unit_search USING fts5(uid UNINDEXED,name,body,tokenize='porter unicode61');
        CREATE TABLE unit_vectors(uid TEXT PRIMARY KEY, vector BLOB NOT NULL);
    ''')
    for r in records:
        text = embedding_text(r)
        conn.execute('INSERT INTO units VALUES (?,?,?,?,?,?,?,?,?,?,?)', (r['uid'], r['repo_id'], r['kind'], r['name'], r['path'], r['start_line'], r['end_line'], r.get('description', ''), r['text'], text, hashlib.sha256(text.encode()).hexdigest()))
        conn.execute('INSERT INTO unit_search VALUES (?,?,?)', (r['uid'], r['name'], r.get('description', '') + '\n' + r['text']))
    conn.execute('INSERT OR REPLACE INTO metadata VALUES (?,?)', ('hybrid_schema', SCHEMA_VERSION))


def local_embedder(root):
    from embeddings import LocalEmbedder
    return LocalEmbedder(Path(root))


def index_vectors(conn, root, required=False, embedder=None):
    """Reuse unchanged vectors; failed rebuilds leave the published index untouched."""
    try:
        embedder = embedder or local_embedder(root)
    except (ImportError, RuntimeError, FileNotFoundError) as exc:
        if required:
            raise RuntimeError(f'Local semantic runtime is unavailable: {exc}') from exc
        conn.execute('INSERT OR REPLACE INTO metadata VALUES (?,?)', ('embedding_status', 'unavailable'))
        return {'embedded': 0, 'cached': 0, 'mode': 'lexical'}
    cache_path = Path(root) / 'state' / 'embedding-cache.sqlite3'
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache = sqlite3.connect(cache_path)
    cache.execute('CREATE TABLE IF NOT EXISTS vectors(model TEXT, hash TEXT, vector BLOB, PRIMARY KEY(model,hash))')
    import numpy as np
    pending = {}
    cached = 0
    rows = conn.execute('SELECT uid,content_hash,embed_text FROM units').fetchall()
    try:
        for uid, content_hash, text in rows:
            old = cache.execute('SELECT vector FROM vectors WHERE model=? AND hash=?', (embedder.fingerprint, content_hash)).fetchone()
            valid = old and len(old[0]) == embedder.dimension * 4
            if valid:
                vector = np.frombuffer(old[0], dtype='<f4')
                valid = np.isfinite(vector).all() and abs(float(np.linalg.norm(vector)) - 1) < 0.01
            if valid:
                conn.execute('INSERT INTO unit_vectors VALUES (?,?)', (uid, old[0]))
                cached += 1
            else:
                pending.setdefault(content_hash, {'text': text, 'uids': []})['uids'].append(uid)
        todo = list(pending.items())
        print(f'Embedding {len(todo)} new passages locally; reusing {cached} vectors.', file=sys.stderr, flush=True)
        for start in range(0, len(todo), 128):
            batch = todo[start:start + 128]
            vectors = embedder.embed_documents([v['text'] for _, v in batch])
            if vectors.shape != (len(batch), embedder.dimension) or not np.isfinite(vectors).all():
                raise ValueError('Embedding dimensions do not match the corpus')
            for (key, item), vector in zip(batch, vectors):
                blob = vector.astype('<f4').tobytes()
                cache.execute('INSERT OR REPLACE INTO vectors VALUES (?,?,?)', (embedder.fingerprint, key, blob))
                conn.executemany('INSERT INTO unit_vectors VALUES (?,?)', [(uid, blob) for uid in item['uids']])
            cache.commit()
            if start == 0 or (start // 128) % 10 == 0 or start + 128 >= len(todo):
                print(f'Embedded {min(start + 128, len(todo))}/{len(todo)} passages.', file=sys.stderr, flush=True)
        conn.execute('INSERT OR REPLACE INTO metadata VALUES (?,?)', ('embedding_fingerprint', embedder.fingerprint))
        conn.execute('INSERT OR REPLACE INTO metadata VALUES (?,?)', ('embedding_model', embedder.model_id))
        conn.execute('INSERT OR REPLACE INTO metadata VALUES (?,?)', ('embedding_status', 'ready'))
        return {'embedded': len(todo), 'cached': cached, 'mode': 'hybrid', 'model': embedder.model_id}
    finally:
        cache.close()


def retrieve(conn, query, root, limit=5, repo_id=None, kinds=None, lexical_only=False, embedder=None):
    """RRF merges exact-term and meaning matches, then deduplicates capabilities."""
    q = query_text(query)
    if not q:
        return [], 'lexical' if lexical_only else 'hybrid'
    where = []
    params = []
    if repo_id:
        where.append('u.repo_id=?'); params.append(repo_id)
    if kinds:
        where.append('u.kind IN (' + ','.join('?' for _ in kinds) + ')'); params.extend(kinds)
    filters = (' AND ' + ' AND '.join(where)) if where else ''
    top = max(80, limit * 16)
    identities = {r['uid']: (r['repo_id'], r['path'], r['name']) for r in
                  conn.execute('SELECT uid,repo_id,path,name FROM units u WHERE 1=1' + filters, params)}
    # Rank capabilities, not chunks: a long manual must not consume the candidate pool.
    lex_ranks, snippets, representatives = {}, {}, {}
    cursor = conn.execute("SELECT u.uid,snippet(unit_search,2,'','', ' … ',90) AS excerpt FROM unit_search JOIN units u ON u.uid=unit_search.uid WHERE unit_search MATCH ?" + filters + ' ORDER BY bm25(unit_search,0,4,1)', [q, *params])
    for row in cursor:
        key = identities[row[0]]
        if key in lex_ranks:
            continue
        lex_ranks[key] = len(lex_ranks) + 1
        snippets[key] = row[1]
        representatives[key] = row[0]
        if len(lex_ranks) >= top:
            break
    cursor.close()
    dense_ranks, similarities = {}, {}
    mode = 'lexical' if lexical_only else 'lexical-fallback'
    if not lexical_only:
        recorded = conn.execute("SELECT value FROM metadata WHERE key='embedding_fingerprint'").fetchone()
        if recorded:
            try:
                embedder = embedder or local_embedder(root)
                if recorded[0] != embedder.fingerprint:
                    raise RuntimeError('Embedding model changed; run toolkit index --semantic')
                import numpy as np
                rows = conn.execute('SELECT u.uid,v.vector FROM units u JOIN unit_vectors v ON u.uid=v.uid WHERE 1=1' + filters, params).fetchall()
                if rows:
                    matrix = np.stack([np.frombuffer(r[1], dtype='<f4') for r in rows])
                    scores = matrix @ embedder.embed_query(query)
                    if not np.isfinite(scores).all():
                        raise ValueError('Stored vectors contain invalid values; rebuild the index')
                    order = np.argsort(-scores, kind='stable')
                    for rank, position in enumerate(order, 1):
                        # Drop very weak similarities; this is not an answer-confidence test.
                        if float(scores[position]) < 0.25:
                            continue
                        uid = rows[position][0]
                        key = identities[uid]
                        if key in dense_ranks:
                            continue
                        dense_ranks[key] = len(dense_ranks) + 1
                        similarities[key] = float(scores[position])
                        representatives.setdefault(key, uid)
                        if len(dense_ranks) >= top:
                            break
                mode = 'hybrid'
            except (ImportError, RuntimeError, FileNotFoundError, ValueError) as exc:
                dense_ranks, similarities = {}, {}
                print(f'Semantic search unavailable; using lexical search: {exc}', file=sys.stderr)
    ids = set(lex_ranks) | set(dense_ranks)
    if not ids:
        return [], mode
    matches = []
    exact = query.strip().lower()
    for key in ids:
        uid = representatives[key]
        row = conn.execute('SELECT * FROM units WHERE uid=?', (uid,)).fetchone()
        record = dict(row)
        lr, sr = lex_ranks.get(key), dense_ranks.get(key)
        score = (1 / (RRF_K + lr) if lr else 0) + (1 / (RRF_K + sr) if sr else 0)
        if record['kind'] == 'skill':
            score *= 1.1
        if exact in (record['name'].lower(), record['repo_id'].lower()) and (record['kind'] != 'doc'):
            score += 1
        excerpt = snippets.get(key, record['text'][:650])
        description = record.get('description', '')
        if description and excerpt.startswith(description):
            excerpt = excerpt[len(description):].lstrip() or record['text'][:650]
        record.update(score=score, lexical_rank=lr, semantic_rank=sr, semantic_similarity=similarities.get(key), excerpt=excerpt)
        matches.append(record)
    matches.sort(key=lambda r: (-r['score'], r['repo_id'], r['path'], r['start_line']))
    selected, seen = [], set()
    for row in matches:
        identity = (row['repo_id'], row['path'], row['name'])
        if identity in seen:
            continue
        seen.add(identity)
        selected.append(row)
        if len(selected) >= limit:
            break
    return selected, mode
