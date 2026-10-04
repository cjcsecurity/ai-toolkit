"""Source-backed evidence and conservative revision attribution for retrieved passages."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import quote


def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


class Sources:
    """A request-scoped source snapshot; never trust cached checkout provenance."""

    def __init__(self, library, entries):
        self.library = library
        self.entries = entries
        self.heads = {}
        self.files = {}

    def _git(self, entry, *args, strip=True):
        result = subprocess.run(['git', '-C', entry['path'], *args],
                                capture_output=True, text=True, timeout=10)
        return (result.stdout.strip() if strip else result.stdout) if result.returncode == 0 else None

    def catalog(self, entry):
        # Availability is resolved for this host, not evidence from the manifest.
        fields = ('id', 'repo', 'description', 'requirements')
        text = json.dumps({k: entry[k] for k in fields if k in entry}, ensure_ascii=False)
        return dict(source_id='catalog-' + digest(entry['id'] + text)[:16], repo_id=entry['id'],
                    kind='repo', name=entry['repo'], path='manifest.json', lines=None,
                    json_pointer=f"/tools/{next(i for i, e in enumerate(self.entries) if e['id'] == entry['id'])}",
                    text=text, text_truncated=False, sha256=digest(text), url=None,
                    provenance={'status': 'catalog', 'recorded_revision': entry.get('commit')})

    def passage(self, row, entry):
        key = (entry['id'], row['path'])
        status = 'unversioned'
        if entry['id'] not in self.heads:
            self.heads[entry['id']] = self._git(entry, 'rev-parse', 'HEAD')
        head = self.heads[entry['id']]
        recorded = entry.get('commit')
        try:
            if key not in self.files:
                self.files[key] = self.library.read(entry['id'], row['path'])
            lines = self.files[key].splitlines()
            span = '\n'.join(lines[row['start_line']-1:row['end_line']])
            if row['text'].replace('\r\n', '\n') not in span:
                status = 'index-mismatch'
            elif head and recorded and head != recorded:
                status = 'revision-mismatch'
            elif head and recorded:
                # Git status can hide edits behind assume-unchanged/skip-worktree.
                # Verify the actual bytes represented by the immutable link instead.
                committed = self._git(entry, 'show', f"{recorded}:{row['path']}", strip=False)
                status = 'verified' if committed == self.files[key] else 'modified'
        except (OSError, ValueError):
            status = 'source-unavailable'
        url = None
        # Only GitHub URLs with an immutable revision have a known source-link format.
        base = entry.get('url', '')
        if status == 'verified' and re.fullmatch(r'https://github\.com/[\w.-]+/[\w.-]+', base) and re.fullmatch(r'[0-9a-f]{40}', recorded or ''):
            url = f"{base.removesuffix('.git')}/blob/{recorded}/{quote(row['path'], safe='/')}#L{row['start_line']}-L{row['end_line']}"
        return dict(source_id='passage-' + digest(row['uid'] + row['text'])[:16],
                    repo_id=entry['id'], kind=row['kind'], name=row['name'], path=row['path'],
                    lines=[row['start_line'], row['end_line']], text=row['text'][:1200],
                    text_truncated=len(row['text']) > 1200, sha256=digest(row['text']), url=url,
                    provenance={'status': status, 'recorded_revision': recorded,
                                'checkout_revision': head})
