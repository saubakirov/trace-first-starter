"""Disposable PTTC B command capture; executes one explicit argv, without selecting tests."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from datetime import datetime, timezone

root = Path(r'C:/Users/c0rpa/.codex/worktrees/04a4/steps-framework')
out = root / 'workspace/2026/TFW_20260907-133942_PTTC/phase-b/evidence'
out.mkdir(exist_ok=True)
label, *command = sys.argv[1:]
assert command and not (out / (label + '.receipt.json')).exists()
def git(*args):
    return subprocess.check_output(['git', *args], cwd=root)
paths = git('ls-files', '-z').decode('utf-8').split('\0')
manifest = {p: hashlib.sha256((root/p).read_bytes()).hexdigest()
            for p in paths if p and (root/p).is_file()}
(out / (label+'.sources.json')).write_text(json.dumps(manifest, indent=2), encoding='utf-8')
env = os.environ.copy()
env.update(PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1',
           PYTEST_PLUGINS='pttc_b_observer', PYTHONPATH=r'E:/TEMP/pttc-phase-b-01a08565',
           PTTC_OBSERVATION=str(out / label))
receipt = dict(argv=command, cwd=str(root), head=git('rev-parse','HEAD').decode().strip(),
               start=datetime.now(timezone.utc).isoformat(), source_manifest=label+'.sources.json',
               environment='Python 3.13.5; pytest 8.4.2; PyYAML 6.0.3; MkDocs 1.6.1; Material 9.7.6')
start=time.perf_counter()
with (out/(label+'.stdout.txt')).open('wb') as stdout, (out/(label+'.stderr.txt')).open('wb') as stderr:
    try:
        limit=float(env['PTTC_COMMAND_LIMIT_SECONDS']) if env.get('PTTC_COMMAND_LIMIT_SECONDS') else None
        process=subprocess.run(command,cwd=root,env=env,stdout=stdout,stderr=stderr,timeout=limit)
        code=process.returncode
    except subprocess.TimeoutExpired:
        code=124
        receipt['stopped_at_allocated_timeout']=limit
receipt.update(exit=code,wall_seconds=time.perf_counter()-start,
               end=datetime.now(timezone.utc).isoformat())
(out/(label+'.receipt.json')).write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt))
print((out/(label+'.stdout.txt')).read_text(encoding='utf-8',errors='replace')[-12000:].encode('ascii','backslashreplace').decode('ascii'))
print((out/(label+'.stderr.txt')).read_text(encoding='utf-8',errors='replace')[-2000:].encode('ascii','backslashreplace').decode('ascii'))
sys.exit(code)
