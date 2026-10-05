"""Small real catalog/index shared by transport and evidence tests."""
import json
from pathlib import Path
import subprocess

from toolkit import Library


def git(root, *args):
    return subprocess.run(['git', '-C', str(root), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def make_library(root):
    root = Path(root)
    rows = []
    for name, description, body in [
        ('platform', 'General development collection',
         '---\nname: durable-execution\ndescription: Resume checkpoints after interrupted jobs.\n---\n# Recovery\nPersist checkpoints and resume interrupted jobs safely.\n'),
        ('recovery', 'Checkpoints and recovery for interrupted jobs',
         '---\nname: restore\ndescription: Restore interrupted jobs from checkpoints.\n---\n# Restore\nRecover durable checkpoints without losing work.\n'),
        ('colors', 'Accessible visual design', '# Colors\nChoose accessible color palettes.\n'),
    ]:
        repo = root / 'repos' / name
        (repo / 'skills' / 'main').mkdir(parents=True)
        (repo / 'README.md').write_text('# Overview\n' + description + '\n')
        (repo / 'skills/main/SKILL.md').write_text(body)
        if name == 'platform':
            for i in range(5):
                copy = repo / f'provider-{i}/SKILL.md'
                copy.parent.mkdir()
                copy.write_text(body + f'\nProvider instructions {i}.\n')
        git(repo, 'init', '-q')
        git(repo, 'add', '.')
        git(repo, '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid',
            'commit', '-qm', 'Fixture sources')
        rows.append(dict(id=name, repo=f'demo/{name}', path=str(repo),
                         url=f'https://github.com/demo/{name}', commit=git(repo, 'rev-parse', 'HEAD'),
                         description=description, tags=[], skill_paths=['skills/main/SKILL.md'],
                         availability='source-ready', requirements=['Python 3.12'],
                         agent_setup={'action': 'setup-required', 'verify': 'Read the documented example.'}))
    (root / 'manifest.json').write_text(json.dumps({'version': 1, 'tools': rows}, indent=2))
    library = Library(root)
    library.index(lexical=True)
    return library
