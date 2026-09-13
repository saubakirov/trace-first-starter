"""Capture actual pytest and nested MkDocs observations without changing their commands/results."""
from pathlib import Path
from datetime import datetime
import contextlib
import hashlib
import json
import os
import subprocess
import sys
import time
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[4]
EVIDENCE = Path(__file__).resolve().parent
label, *arguments = sys.argv[1:]
assert label and arguments
prefix = EVIDENCE / label
assert not prefix.with_suffix('.receipt.json').exists(), 'preserve previous check epochs'
os.chdir(ROOT)
sys.path.insert(0, str(ROOT))  # match python -m pytest's root import context
os.environ['PYTHONUTF8'] = '1'
original_run = subprocess.run
builds = []


def observed_run(*args, **kwargs):
    result = original_run(*args, **kwargs)
    command = args[0] if args else kwargs.get('args', [])
    if isinstance(command, (tuple, list)) and 'mkdocs' in command:
        capture = f'{label}.mkdocs-{len(builds)+1}'
        for stream in ('stdout','stderr'):
            value = getattr(result, stream) or ''
            (EVIDENCE/f'{capture}.{stream}.txt').write_text(value,encoding='utf-8')
        builds.append({'command':command,'cwd':str(kwargs.get('cwd',ROOT)),
                       'exit_code':result.returncode,'capture':capture})
    return result


sources = {}
for base in ('.tfw','.agents','.claude','tools','docs/scripts'):
    for path in (ROOT/base).rglob('*'):
        if path.is_file() and path.suffix in ('.md','.py','.yaml','.yml') and '__pycache__' not in path.parts:
            sources[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
started = datetime.now().astimezone().isoformat()
begin = time.monotonic()
import pytest
with prefix.with_suffix('.stdout.txt').open('x',encoding='utf-8') as out, prefix.with_suffix('.stderr.txt').open('x',encoding='utf-8') as err:
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err), patch('subprocess.run', observed_run):
        code = int(pytest.main(arguments))
receipt = {'started':started,'duration_seconds':time.monotonic()-begin,'cwd':str(ROOT),
           'python':sys.version,'command':['python','-m','pytest',*arguments],
           'exit_code':code,'builds':builds,'source_sha256':sources}
prefix.with_suffix('.receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({key:value for key,value in receipt.items() if key != 'source_sha256'},indent=2))
print(prefix.with_suffix('.stdout.txt').read_text(encoding='utf-8')[-7000:])
sys.exit(code)
