#!/usr/bin/env python3
"""Shared, bounded retrieval for a local agent toolkit. No network on reads."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import stat
import subprocess
import sys
import tempfile

ROOT = Path(os.environ.get('AI_TOOLKIT_HOME', Path(__file__).resolve().parent)).expanduser().resolve()
STOP = set('a an the i we you our your to for with and or of in on from use using need want tools tool project that can is are how do me my'.split())
PROFILE_LIMIT = 64 * 1024


def read_project_profile(path):
    """Read a small regular profile without following a project-supplied link."""
    try:
        before = path.lstat()
    except FileNotFoundError:
        return None
    if not stat.S_ISREG(before.st_mode):
        raise ValueError('Project profile must be a regular file; symlinks are not allowed')
    flags = os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0) | getattr(os, 'O_NONBLOCK', 0)
    with os.fdopen(os.open(path, flags), 'rb') as stream:
        opened = os.fstat(stream.fileno())
        if (not stat.S_ISREG(opened.st_mode)
                or (before.st_dev, before.st_ino) != (opened.st_dev, opened.st_ino)):
            raise ValueError('Project profile changed while opening it')
        raw = stream.read(PROFILE_LIMIT + 1)
    if len(raw) > PROFILE_LIMIT:
        raise ValueError('Project profile exceeds the 64 KiB limit')
    data = json.loads(raw)
    if (not isinstance(data, dict) or not isinstance(data.get('tools', []), list)
            or any(not isinstance(item, str) for item in data.get('tools', []))):
        raise ValueError('Project profile must be an object with a list of tool names')
    return data


def terms(query):
    return [t for t in re.findall(r'[\w]+', query.lower()) if t not in STOP and len(t) > 1][:24]


def match_query(query):
    return ' OR '.join('"' + t.replace('"', '""') + '"' for t in terms(query))


def atomic_json(path, data):
    payload = (json.dumps(data, indent=2, ensure_ascii=False) + '\n').encode('utf-8')
    if len(payload) > PROFILE_LIMIT:
        raise ValueError('Project profile exceeds the 64 KiB limit')
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, prefix='.' + path.name)
    try:
        with os.fdopen(fd, 'wb') as f:
            f.write(payload)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def bounded_json(data, budget=8000):
    """Keep output valid JSON and enforce a character ceiling, including framing."""
    budget = max(256, budget)
    envelope = {'results': data, 'truncated': False} if isinstance(data, list) else data
    out = json.dumps(envelope, ensure_ascii=False, indent=2)
    if len(out) <= budget:
        return out
    if isinstance(data, list):
        envelope = {'results': list(data), 'truncated': True}
        while envelope['results']:
            envelope['results'].pop()
            out = json.dumps(envelope, ensure_ascii=False, indent=2)
            if len(out) <= budget:
                return out
    return json.dumps({'truncated': True, 'message': 'Result exceeds the character budget; narrow the query or increase --budget.'})


def read_excerpt(text, name, path, offset=0, budget=8000):
    budget = max(256, budget)
    offset = max(0, offset)
    prefix = f'Source: {name}/{path}'[:budget // 3] + f'\nOffset: {offset}; total characters: {len(text)}\n'
    room = max(1, budget - len(prefix) - 100)
    fragment = text[offset:offset + room]
    end = offset + len(fragment)
    suffix = f'\n[Next offset: {end}; continue with --offset {end}.]' if end < len(text) else '\n[End of file.]'
    return prefix + fragment + suffix


def skill_metadata(text):
    """Read the simple name/description scalars, including YAML block strings."""
    match = re.match(r'^---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
    if not match:
        return {}
    values = {}
    active = None
    for line in match.group(1).splitlines():
        field = re.match(r'^([\w-]+):\s*(.*)$', line)
        if field:
            key, value = field.groups()
            active = key if key in ('name', 'description') else None
            if active:
                values[active] = '' if re.fullmatch(r'[>|][+-]?', value) else value
        elif active and line[:1].isspace() and line.strip():
            values[active] = (values[active] + ' ' + line.strip()).strip()
    for key, value in values.items():
        if len(value) > 1 and value[0] == value[-1] and value[0] in ('"', "'"):
            if value[0] == '"':
                try:
                    value = json.loads(value)
                except ValueError:
                    value = value[1:-1]
            else:
                value = value[1:-1].replace("''", "'")
            values[key] = value
    return values


class Library:
    def __init__(self, root=ROOT):
        self.root = Path(root).expanduser().resolve()
        self.manifest = self.root / 'manifest.json'
        self.db = self.root / 'index.sqlite3'

    def entries(self, *, manifest_bytes=None):
        """Resolve catalog entries, optionally from an already-read snapshot."""
        raw = self.manifest.read_bytes() if manifest_bytes is None else manifest_bytes
        rows = json.loads(raw)['tools']
        for row in rows:
            source = Path(row['path'])
            path = (self.root / source).resolve()
            if '..' in source.parts or path == self.root or not path.is_relative_to(self.root):
                raise ValueError('Source paths must remain inside the toolkit root')
            row['path'] = str(path)
            row['source_present'] = path.is_dir()
            # Catalog metadata describes requirements, never another host's readiness.
            row['availability'] = 'source-only' if row['source_present'] else 'source-missing'
        return rows

    def entry(self, name):
        matches = [r for r in self.entries() if name.lower() in (r['id'].lower(), r['repo'].lower())]
        if len(matches) != 1:
            raise ValueError(f'Unknown or ambiguous toolkit entry: {name}')
        return matches[0]

    def summary(self, row):
        keys = ['id', 'repo', 'description', 'kind', 'recommended_scope', 'availability', 'requirements', 'path']
        return {k: row[k] for k in keys if k in row}

    def safe_path(self, row, relative):
        root = Path(row['path']).resolve()
        p = (root / relative).resolve()
        if not p.is_relative_to(root):
            raise ValueError('Path must remain inside the selected repository')
        return p

    def read(self, name, relative):
        row = self.entry(name)
        p = self.safe_path(row, relative)
        if not row['source_present']:
            raise FileNotFoundError(f'Source for {row["id"]} is missing; run python3 scripts/bootstrap.py --repo {row["id"]}')
        if p.stat().st_size > 2_000_000:
            raise ValueError('File exceeds 2 MB; inspect a relevant section directly')
        return p.read_text(errors='replace')

    def index(self, semantic=False, lexical=False):
        """Build a complete replacement; failed builds leave the published index intact."""
        import corpus
        import hybrid
        manifest_bytes = self.manifest.read_bytes()
        fd, temp = tempfile.mkstemp(dir=self.root, prefix='.index-', suffix='.sqlite3')
        os.close(fd)
        conn = None
        try:
            records = corpus.build_records(self)
            conn = sqlite3.connect(temp)
            hybrid.populate(conn, records)
            status = {'mode': 'lexical', 'embedded': 0, 'cached': 0} if lexical else hybrid.index_vectors(conn, self.root, required=semantic)
            conn.execute('INSERT OR REPLACE INTO metadata VALUES (?,?)', ('manifest_hash', hashlib.sha256(manifest_bytes).hexdigest()))
            conn.commit()
            conn.close()
            conn = None
            os.replace(temp, self.db)
        finally:
            if conn is not None:
                conn.close()
            if os.path.exists(temp):
                os.unlink(temp)
        return {'tools': len(self.entries()), 'passages': len(records), 'index': str(self.db), **status}

    def connect(self, lexical_only=False):
        import hybrid
        if not self.db.exists():
            self.index(lexical=lexical_only)
        conn = sqlite3.connect(self.db)
        expected = hashlib.sha256(self.manifest.read_bytes()).hexdigest()
        metadata = dict(conn.execute('SELECT key,value FROM metadata'))
        if metadata.get('manifest_hash') != expected or metadata.get('hybrid_schema') != hybrid.SCHEMA_VERSION:
            conn.close()
            self.index(lexical=lexical_only)
            conn = sqlite3.connect(self.db)
        conn.row_factory = sqlite3.Row
        return conn

    def search(self, query, limit=5, repo_id=None, kinds=None, lexical_only=False):
        import hybrid
        if repo_id:
            repo_id = self.entry(repo_id)['id']
        with self.connect(lexical_only=lexical_only) as conn:
            rows, mode = hybrid.retrieve(conn, query, self.root, limit, repo_id, kinds, lexical_only)
        entries = {r['id']: r for r in self.entries()}
        results = []
        for r in rows:
            entry = entries[r['repo_id']]
            results.append(dict(id=r['repo_id'], repo=entry['repo'], match_kind=r['kind'],
                name=r['name'], description=r.get('description', '')[:500], path=r['path'],
                lines=[r['start_line'], r['end_line']], excerpt=r['excerpt'][:650],
                availability=entry['availability'], source_present=entry['source_present'], retrieval=mode,
                lexical_rank=r['lexical_rank'], semantic_rank=r['semantic_rank']))
        return results

    def docs(self, name, query, limit=3, lexical_only=False):
        return self.search(query, limit, name, ['doc', 'skill'], lexical_only)

    def search_status(self):
        with self.connect() as conn:
            metadata = dict(conn.execute('SELECT key,value FROM metadata'))
            counts = dict(conn.execute('SELECT kind,count(*) FROM units GROUP BY kind'))
            vectors = conn.execute('SELECT count(*) FROM unit_vectors').fetchone()[0]
        import hybrid
        reason = None
        ready = False
        try:
            model = hybrid.local_embedder(self.root)
            ready = (metadata.get('embedding_fingerprint') == model.fingerprint
                     and vectors == sum(counts.values()) and vectors > 0)
            if not ready:
                reason = 'Index is incomplete or uses another model; run toolkit index --semantic'
        except (ImportError, RuntimeError, FileNotFoundError) as exc:
            reason = str(exc)
        return {'model': metadata.get('embedding_model'), 'status': 'hybrid-ready' if ready else 'lexical-fallback',
                'passages': counts, 'vectors': vectors, 'local': True, 'output_budget': 8000,
                'note': reason}

    def skills(self, name, query='', limit=10, lexical_only=False):
        if query.strip():
            return self.search(query, limit, name, ['skill'], lexical_only)
        row = self.entry(name)
        words = terms(query)
        matches = []
        for relative in row.get('skill_paths', []):
            try:
                text = self.read(name, relative)
            except (OSError, ValueError):
                continue
            fields = skill_metadata(text)
            fields.setdefault('name', Path(relative).parent.name)
            fields.setdefault('description', '')
            fields['path'] = relative
            searchable = (fields['name'] + ' ' + fields['description'] + ' ' + relative).lower()
            score = sum(w in searchable for w in words)
            if not words or score:
                matches.append((score, fields))
        return [r for _, r in sorted(matches, key=lambda x: (-x[0], x[1]['path']))[:limit]]

    def select(self, names, project):
        ids = [self.entry(n)['id'] for n in names]  # Validate before any write.
        project = Path(project).resolve()
        if not project.is_dir():
            raise ValueError('Project directory must already exist')
        path = project / '.ai-toolkit.json'
        data = read_project_profile(path)
        if data is None:
            data = {'version': 1, 'tools': []}
        data['tools'] = list(dict.fromkeys([*data.get('tools', []), *ids]))
        atomic_json(path, data)
        return {'profile': str(path), 'tools': data['tools'], 'note': 'Records preferences; does not enable services or install dependencies.'}

    def doctor(self):
        results = []
        for row in self.entries():
            p = Path(row['path'])
            actual = None
            if p.is_dir():
                result = subprocess.run(['git', '-C', str(p), 'rev-parse', '--show-toplevel'], capture_output=True, text=True)
                if result.returncode == 0 and Path(result.stdout.strip()).resolve() == p:
                    result = subprocess.run(['git', '-C', str(p), 'rev-parse', 'HEAD'], capture_output=True, text=True)
                    actual = result.stdout.strip() if result.returncode == 0 else None
            results.append({'id': row['id'], 'source_present': row['source_present'],
                            'revision_matches': actual is not None and actual == row.get('commit'),
                            'availability': row['availability']})
        return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT, help='Toolkit catalog/index directory')
    parser.add_argument('--budget', type=int, default=8000, help='Maximum output characters (default 8000)')
    sub = parser.add_subparsers(dest='cmd', required=True)
    sub.add_parser('list')
    p = sub.add_parser('index')
    group = p.add_mutually_exclusive_group()
    group.add_argument('--semantic', action='store_true', help='Require a complete local embedding build')
    group.add_argument('--lexical', action='store_true', help='Build only the lexical index')
    sub.add_parser('search-status')
    sub.add_parser('doctor')
    p = sub.add_parser('recommend', help='Retrieve cited tool evidence for a project; your agent generates the recommendation')
    p.add_argument('query'); p.add_argument('--project'); p.add_argument('--constraints', default='')
    p.add_argument('--limit', type=int, default=5); p.add_argument('--lexical', action='store_true')
    p = sub.add_parser('search'); p.add_argument('query'); p.add_argument('--limit', type=int, default=5); p.add_argument('--repo'); p.add_argument('--kind', choices=['repo', 'skill', 'doc']); p.add_argument('--lexical', action='store_true')
    p = sub.add_parser('show'); p.add_argument('id')
    p = sub.add_parser('docs'); p.add_argument('id'); p.add_argument('query'); p.add_argument('--limit', type=int, default=3); p.add_argument('--lexical', action='store_true')
    p = sub.add_parser('skills'); p.add_argument('id'); p.add_argument('query', nargs='?', default=''); p.add_argument('--limit', type=int, default=10); p.add_argument('--lexical', action='store_true')
    p = sub.add_parser('read'); p.add_argument('id'); p.add_argument('path'); p.add_argument('--offset', type=int, default=0)
    p = sub.add_parser('select'); p.add_argument('ids', nargs='+'); p.add_argument('--project', default=os.getcwd())
    p = sub.add_parser('project'); p.add_argument('--project', default=os.getcwd())
    args = parser.parse_args()
    lib = Library(args.root)
    try:
        if args.cmd == 'recommend':
            from rag import RagService, encode
            print(encode(RagService(args.root).recommend(args.query, project=args.project,
                  constraints=args.constraints, limit=args.limit, lexical_only=args.lexical, budget=args.budget)))
            return
        if args.cmd == 'list':
            data = [{'id': r['id'], 'kind': r.get('kind'), 'availability': r['availability'], 'source_present': r['source_present']} for r in lib.entries()]
        elif args.cmd == 'index': data = lib.index(semantic=args.semantic, lexical=args.lexical)
        elif args.cmd == 'search-status': data = lib.search_status()
        elif args.cmd == 'doctor': data = lib.doctor()
        elif args.cmd == 'search': data = lib.search(args.query, min(max(args.limit, 1), 20), args.repo, [args.kind] if args.kind else None, args.lexical)
        elif args.cmd == 'docs': data = lib.docs(args.id, args.query, min(max(args.limit, 1), 10), args.lexical)
        elif args.cmd == 'skills': data = lib.skills(args.id, args.query, min(max(args.limit, 1), 50), args.lexical)
        elif args.cmd == 'show':
            data = dict(lib.entry(args.id))
            data['skill_count'] = len(data.pop('skill_paths', []))
        elif args.cmd == 'read':
            text = lib.read(args.id, args.path)
            print(read_excerpt(text, args.id, args.path, args.offset, args.budget))
            return
        elif args.cmd == 'select': data = lib.select(args.ids, args.project)
        elif args.cmd == 'project':
            path = Path(args.project).resolve() / '.ai-toolkit.json'
            data = read_project_profile(path)
            if data is None:
                data = {'tools': [], 'note': 'No project selection saved'}
        print(bounded_json(data, args.budget))
    except (OSError, ValueError, RuntimeError, KeyError, sqlite3.Error) as exc:
        print(json.dumps({'error': str(exc)}), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
