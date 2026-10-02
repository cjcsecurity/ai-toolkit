"""Read-only capability corpus with source locations and deterministic identities.

No toolkit import or model dependency: the caller supplies the Library interface.
Files are never truncated, including documents larger than Library.read's UI limit.
"""
from bisect import bisect_right
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

CHUNK_SIZE = 1800
OVERLAP = 150
EXCLUDED_DIRS = frozenset({
    '.git', 'node_modules', 'vendor', 'vendors', 'third_party', 'third-party',
    '.venv', 'venv', '__pycache__', '.next', '.nuxt', '.cache', 'coverage',
    'dist', 'build', 'out', 'target', 'generated', '_build',
    'test', 'tests', '__tests__', 'fixture', 'fixtures', '__fixtures__',
    'testdata', 'test_data', 'test-fixtures', 'test_fixtures',
    'attack_samples', 'attack-samples', 'malicious_skills', 'malicious-skills',
})
DOC_SUFFIXES = {'.md', '.mdx', '.rst'}
ADMIN_DIRS = frozenset({'archive', 'archives', 'changelog', 'changelogs',
                        'plans', 'planning', 'reports', 'swarm-plans', 'session-logs'})


def administrative_path(relative):
    path = Path(relative)
    return (any(p.lower() in ADMIN_DIRS for p in path.parts[:-1]) or
            path.stem.lower() in {'changelog', 'changes', 'history', 'weekly-updates',
                                  'contributing', 'code_of_conduct', 'contributors', 'license'})


def excluded_path(relative):
    return any(p.lower() in EXCLUDED_DIRS for p in Path(relative).parts[:-1])


def _scalar(value):
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        try:
            return json.loads(value)
        except ValueError:
            return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    return re.split(r'\s+#', value, maxsplit=1)[0].strip()


def skill_metadata(text):
    """Parse name/description YAML scalars without interpreting instructions.

    Supports quoted/plain multiline scalars and literal/folded block scalars,
    including chomping and indentation indicators. Nested metadata is ignored.
    """
    match = re.match(r'\A\ufeff?---\s*\n(.*?)\n(?:---|\.\.\.)\s*(?:\n|$)', text, re.S)
    if not match:
        return {}, 0
    lines = match.group(1).splitlines()
    values = {}
    i = 0
    while i < len(lines):
        field = re.match(r'^(name|description):[ \t]*(.*)$', lines[i])
        i += 1
        if not field:
            continue
        key, raw = field.groups()
        tail = []
        while i < len(lines) and (not lines[i].strip() or lines[i][:1].isspace()):
            tail.append(lines[i])
            i += 1
        indicator = re.fullmatch(r'([>|])([1-9+-]{0,2})(?:\s+#.*)?', raw.strip())
        if indicator:
            nonempty = [len(line) - len(line.lstrip()) for line in tail if line.strip()]
            indent = min(nonempty, default=0)
            block = [line[indent:] if line.strip() else '' for line in tail]
            if indicator.group(1) == '>':
                pieces = []
                for n, line in enumerate(block):
                    pieces.append(line)
                    if n + 1 < len(block):
                        following = block[n + 1]
                        if line and following and not line.startswith(' ') and not following.startswith(' '):
                            pieces.append(' ')
                        elif line or not following:
                            pieces.append('\n')
                value = ''.join(pieces)
            else:
                value = '\n'.join(block)
            values[key] = value.strip()
        else:
            values[key] = _scalar(' '.join([raw] + [line.strip() for line in tail if line.strip()]))
    return values, match.end()


def _files(root):
    result = subprocess.run(['git', '-C', str(root), 'ls-files', '-z'], capture_output=True)
    # An untracked fixture directory inside another git checkout must not inherit
    # that checkout's file list. Git emits paths relative to the supplied cwd.
    if result.returncode == 0:
        return [p for p in result.stdout.decode(errors='replace').split('\0') if p]
    paths = []
    for folder, dirs, names in os.walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d.lower() not in EXCLUDED_DIRS)
        paths.extend(str((Path(folder) / name).relative_to(root)) for name in names)
    return paths


def _priority(path, declared):
    parts = Path(path).parts
    # Native sources win over per-provider generated installations.
    provider = any(p.startswith('.') for p in parts[:-1])
    templates = any(p in ('templates', 'template') for p in parts[:-1])
    return (path not in declared, provider, templates,
            not path.startswith('skills/'), len(parts), len(path), path)


def _sections(text, start=0):
    """Heading boundaries outside code fences, with exact character offsets."""
    boundaries = [(start, '')]
    position = 0
    fence = None
    for line in text.splitlines(keepends=True):
        if position < start:
            position += len(line)
            continue
        stripped = line.lstrip()
        mark = re.match(r'(`{3,}|~{3,})', stripped)
        if mark:
            marker = mark.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
        if fence is None:
            heading = re.match(r'^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$', line.rstrip('\n'))
            if heading:
                if position == boundaries[-1][0]:
                    boundaries[-1] = (position, heading.group(1))
                else:
                    boundaries.append((position, heading.group(1)))
        position += len(line)
    pending = None
    for n, (offset, heading) in enumerate(boundaries):
        end = boundaries[n + 1][0] if n + 1 < len(boundaries) else len(text)
        if (pending is not None and len(text) > CHUNK_SIZE
                and end - pending[0] <= CHUNK_SIZE):
            pending = (pending[0], end, ' / '.join(filter(None, [pending[2], heading])))
        else:
            if pending is not None:
                yield pending
            pending = (offset, end, heading)
    if pending is not None:
        yield pending


def _chunks(text, start, end):
    """Prefer paragraph/line breaks, preserving every character of long lines."""
    cursor = start
    while cursor < end:
        stop = min(cursor + CHUNK_SIZE, end)
        if stop < end:
            lower = cursor + CHUNK_SIZE * 2 // 3
            for separator in ('\n\n', '\n', ' '):
                boundary = text.rfind(separator, lower, stop)
                if boundary >= lower:
                    stop = boundary + len(separator)
                    break
        left, right = cursor, stop
        while left < right and text[left].isspace():
            left += 1
        while right > left and text[right - 1].isspace():
            right -= 1
        if left < right:
            yield left, right
        if stop == end:
            break
        # Overlap on a complete line/word where available, at most 150 chars.
        overlap = max(cursor + 1, stop - OVERLAP)
        boundary = text.find('\n', overlap, stop)
        if boundary < 0:
            boundary = text.find(' ', overlap, stop)
        cursor = boundary + 1 if boundary >= 0 else stop


def _digest(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def embedding_text(record):
    """Keep identity and complete source text; skill overviews may exceed 2000 chars."""
    prefix = f"{record.get('repo', record['repo_id'])}: {record['name']}"
    description = record.get('description', '')
    if description and description not in record['text']:
        prefix += '\n' + description
    room = max(0, 1999 - len(record['text']))
    return prefix[:room] + '\n' + record['text']


def build_records(library):
    records = []
    for row in sorted(library.entries(), key=lambda r: r['id']):
        repo_id = row['id']
        overview = '\n'.join(filter(None, [row.get('repo', repo_id), row.get('description', ''), ' '.join(row.get('tags', []))]))
        records.append(dict(uid=_digest(repo_id + ':repo'), repo_id=repo_id,
                            repo=row.get('repo', repo_id), kind='repo', name=row.get('repo', repo_id),
                            path='', start_line=1, end_line=1, text=overview[:CHUNK_SIZE],
                            content_hash=_digest(overview), aliases=[]))
        root = Path(row['path'])
        if not root.is_dir():
            continue
        declared = set(row.get('skill_paths', []))
        files = set(_files(root)) | declared
        files = [p for p in files if Path(p).suffix.lower() in DOC_SUFFIXES and not excluded_path(p)
                 and (p in declared or Path(p).name.lower() == 'skill.md' or not administrative_path(p))]
        seen_files = {}
        seen_chunks = {}
        for relative in sorted(files, key=lambda p: _priority(p, declared)):
            try:
                path = library.safe_path(row, relative)
                if not path.is_file():
                    continue
                text = path.read_text(errors='replace')
            except (ValueError, OSError):
                continue
            if not text.strip():
                continue
            is_skill = relative in declared or Path(relative).name.lower() == 'skill.md'
            kind = 'skill' if is_skill else 'doc'
            metadata, body_start = skill_metadata(text) if is_skill else ({}, 0)
            name = metadata.get('name') or Path(relative).parent.name
            file_hash = _digest(text.strip())
            if file_hash in seen_files:
                for record in seen_files[file_hash]:
                    record['aliases'].append(relative)
                continue
            file_records = []
            line_starts = [0] + [m.end() for m in re.finditer('\n', text)]
            if is_skill:
                # Frontmatter carries intent that may never appear in the body.
                # Keep its own source-backed passage without changing any body
                # chunk boundaries, identities, or cached embedding inputs.
                if body_start:
                    left, right = 0, len(text[:body_start].rstrip())
                else:
                    left, right = next(_chunks(text, 0, len(text)))
                overview_text = text[left:right]
                skill_overview = dict(
                    uid=_digest(f'{repo_id}:skill:{relative}:overview'),
                    repo_id=repo_id, repo=row.get('repo', repo_id), kind='skill',
                    name=name, path=relative, passage='overview',
                    start_line=bisect_right(line_starts, left),
                    end_line=bisect_right(line_starts, right - 1),
                    text=overview_text, description=metadata.get('description', ''),
                    content_hash=_digest(overview_text), aliases=[])
                records.append(skill_overview)
                file_records.append(skill_overview)
            if not text[body_start:].strip():
                body_start = 0
            for section_start, section_end, heading in _sections(text, body_start):
                for left, right in _chunks(text, section_start, section_end):
                    chunk = text[left:right]
                    # Skill identity stays attached even when two skills share
                    # boilerplate. Doc duplicates don't need separate vectors.
                    content_hash = _digest(chunk)
                    dedup_key = (kind, name if is_skill else '', content_hash)
                    if dedup_key in seen_chunks:
                        existing = seen_chunks[dedup_key]
                        if relative != existing['path'] and relative not in existing['aliases']:
                            existing['aliases'].append(relative)
                        file_records.append(existing)
                        continue
                    record = dict(uid=_digest(f'{repo_id}:{kind}:{relative}:{left}:{right}'),
                                  repo_id=repo_id, repo=row.get('repo', repo_id), kind=kind,
                                  name=name if is_skill else (heading or Path(relative).stem),
                                  path=relative, start_line=bisect_right(line_starts, left),
                                  end_line=bisect_right(line_starts, right - 1), text=chunk,
                                  content_hash=content_hash, aliases=[])
                    if is_skill:
                        record['description'] = metadata.get('description', '')
                    records.append(record)
                    file_records.append(record)
                    seen_chunks[dedup_key] = record
            seen_files[file_hash] = file_records
    return records
