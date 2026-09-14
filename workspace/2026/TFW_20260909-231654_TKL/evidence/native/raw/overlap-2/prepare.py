from pathlib import Path
from datetime import datetime, timezone
import subprocess
import json
import hashlib

SOURCE = Path('C:/Users/c0rpa/.codex/worktrees/f3f3/steps-framework')
NATIVE = Path('C:/Users/c0rpa/AppData/Local/Temp/TFW_TKL_NATIVE_01a09a0c')
ROOT = NATIVE / 'overlap-2'
BASE = 'e00ca51d05f4e451441cb9fc267579a7f9e4d4ce'
TASK = 'workspace/2026/TFW_20260909-231654_TKL'
EVIDENCE = SOURCE / TASK / 'evidence/native/raw/overlap-2'
assert not ROOT.exists()
ROOT.mkdir()
repo = ROOT / 'concurrent-repo'
repo.mkdir()
commands = []

def git(cwd, *args):
    start = datetime.now(timezone.utc).isoformat()
    argv = ['git', '-c', 'core.longpaths=true', *args]
    result = subprocess.run(argv, cwd=cwd, capture_output=True)
    n = len(commands) + 1
    (EVIDENCE / f'{n:02d}-stdout.txt').write_bytes(result.stdout)
    (EVIDENCE / f'{n:02d}-stderr.txt').write_bytes(result.stderr)
    commands.append({'argv': argv, 'cwd': str(cwd), 'started': start,
                     'finished': datetime.now(timezone.utc).isoformat(), 'exit_code': result.returncode})
    assert result.returncode == 0, result.stderr
    return result.stdout

git(repo, 'init')
git(repo, 'fetch', '--depth=2', str(NATIVE / 'concurrent-repo'), BASE)
git(repo, 'checkout', '--detach', BASE)
assigned = {
    'executor': [TASK + '/evidence/executor-handover-2.md', 'knowledge/records/TKL-NATIVE-EXEC-2.md'],
    'coordinator': [TASK + '/evidence/coordinator-source-2.md', 'knowledge/records/TKL-NATIVE-COORD-2.md'],
}
prepared = json.loads((SOURCE / TASK / 'evidence/native/raw/q1-prepared-manifest.json').read_bytes())
holders = {}
for holder in ['executor', 'coordinator']:
    tree = ROOT / holder
    branch = 'codex/tkl-native-' + holder + '-2'
    git(repo, 'worktree', 'add', '-b', branch, str(tree), BASE)
    assert git(tree, 'rev-parse', 'HEAD').decode().strip() == BASE
    assert not git(tree, 'status', '--porcelain')
    for name, expected in prepared['input_files'].items():
        assert hashlib.sha256((tree / name).read_bytes()).hexdigest() == expected['sha256']
    assert all(not (tree / name).exists() for paths in assigned.values() for name in paths)
    (ROOT / 'capture' / holder).mkdir(parents=True)
    holders[holder] = {'worktree': tree.as_posix(), 'branch': branch, 'head': BASE,
                       'permitted_two_paths': assigned[holder], 'clean': True,
                       'all_four_outputs_absent': True, 'original_22_input_hashes_equal': True}
metadata = {
    'preparation_started': json.loads((EVIDENCE / '00-preparation-start.json').read_bytes())['started'],
    'prepared_at': datetime.now(timezone.utc).isoformat(),
    'candidate': '27cdb701b91c5b45b9f54b3e98c9ad67635b3e30', 'base': BASE,
    'ruling': 'f70037d94c975fe889eaab9bf17ee18e26608137',
    'first_epoch': 'Preserved unchanged in sibling concurrent-repo/executor/coordinator/capture/recovery; no first originals copied into fresh source/record outputs.',
    'holders': holders, 'commands': commands,
    'original_prepared_manifest_sha256': hashlib.sha256((SOURCE / TASK / 'evidence/native/raw/q1-prepared-manifest.json').read_bytes()).hexdigest(),
    'input_interpretation': 'Same immutable 22-file e00 input package. Direct 6f91 Coordinator dispatch changes only fresh physical root, branch and assigned output names to the exact -2 paths here; the prior input documents remain byte-exact, not silently rewritten. All source, observed-only, independence and no-acceptance semantics remain.',
    'barrier_received': False, 'source_or_record_written': False,
    'limits': 'Preparation <=15 active minutes, post-barrier <=15 active minutes excluding scheduler wait. Exactly one second attempt; no third attempt if no overlap. Actual intervals only, no artificial delay. Same existing native holders and source package. Each own original sealed before sibling visibility.',
}
p = EVIDENCE / 'prepared-packet.json'
assert not p.exists()
p.write_text(json.dumps(metadata, indent=2) + '\n', encoding='utf-8', newline='\n')
(ROOT / 'prepared-packet.json').write_bytes(p.read_bytes())
print(json.dumps({'prepared_at': metadata['prepared_at'], 'packet': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'holders': holders}))
