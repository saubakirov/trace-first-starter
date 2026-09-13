"""One authorized SLC self-hosting application; preserved trace, not shipped migration runtime."""
from pathlib import Path
from datetime import datetime
import base64
import hashlib
import json
import subprocess
import sys
import yaml

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'tools'))
import tfw_state as state

BASELINE = 'affd9033abf94e9b9a9e27114f3bfbb16066438a'
APPROVAL = '40b2dd5666cf608a9f1282567550de6a6b62fadd'
EVIDENCE = Path(__file__).resolve().parent
CONFIG = ROOT / '.tfw/project_config.yaml'
STATE = ROOT / '.tfw/knowledge_state.yaml'
GUIDE = ROOT / '.tfw/migrations/3.3.0.md'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    original = {path.relative_to(ROOT).as_posix(): path.read_bytes() for path in (CONFIG, STATE)}
    config = yaml.safe_load(original['.tfw/project_config.yaml'])
    knowledge = yaml.safe_load(original['.tfw/knowledge_state.yaml'])
    assert config['tfw']['task_containers'] == ['workspace', 'tasks']
    assert 'historical_containers' not in config['tfw']
    for path, raw in original.items():
        assert raw == git('show', f'{BASELINE}:{path}'), path
    historical = state.iter_task_dirs(ROOT, ['tasks'])
    assert not state.iter_unmatched_task_dirs(ROOT, ['tasks'])
    state.iter_task_dirs(ROOT, ['workspace', 'tasks'])  # cross-scope collisions refuse
    membership = {p.relative_to(ROOT).as_posix(): state.parse_identifier(p.name)[1] for p in historical}
    remembered = knowledge['knowledge']['processed_task_digests']
    pairs = {key: remembered[key] for key in sorted(set(membership.values()) & remembered.keys())}
    unaffected = {k: v for k, v in remembered.items() if k not in pairs}
    before_gate = state.knowledge_pending(ROOT)
    task_blobs = git('ls-tree', '-r', BASELINE, '--', 'tasks').decode().splitlines()
    task_blobs = [line for line in task_blobs if not line.endswith('\ttasks/README.md')]
    assert not git('diff', '--name-only', BASELINE, '--', *membership), 'historical task byte drift'
    record = {
        'kind': 'SLC self-hosting preservation; before Candidate, not a native update receipt',
        'recorded_at': datetime.now().astimezone().isoformat(),
        'source_sha': BASELINE, 'approval_sha': APPROVAL,
        'approved_ts_blob': '6535418fb65ad1b6f7f7a7b40a01506c1df27943',
        'prospective_ruling': 'cc94d1241c3b31c33adbe6920121e537e4c25718',
        'guide_sha256': sha(GUIDE.read_bytes()),
        'previous_provenance': config['tfw']['installed_from'],
        'disposition': 'historical-only; owner direction in frozen HL section 3',
        'authority_path': 'workspace/2026/TFW_20260907-020729_SLC/HL-TFW_20260907-020729_SLC.md',
        'old_fields': {'task_containers': ['workspace', 'tasks'], 'historical_containers': None},
        'intended_fields': {'task_containers': ['workspace'], 'historical_containers': ['tasks']},
        'digest_map_present': True, 'membership': membership, 'removed_pairs': pairs,
        'unaffected_pairs': unaffected, 'historical_task_git_blobs': task_blobs,
        'knowledge_tree': git('rev-parse', f'{BASELINE}:knowledge').decode().strip(),
        'knowledge_index_blob': git('rev-parse', f'{BASELINE}:KNOWLEDGE.md').decode().strip(),
        'before_images_base64': {path: base64.b64encode(raw).decode() for path, raw in original.items()},
        'before_sha256': {path: sha(raw) for path, raw in original.items()},
    }
    raw = (json.dumps(record, ensure_ascii=False, indent=2) + '\n').encode()
    attachment = ROOT / '.tfw/update_receipts/slc-preservation' / sha(raw) / 'before.json'
    attachment.parent.mkdir(parents=True, exist_ok=True)
    if attachment.exists():
        assert attachment.read_bytes() == raw, 'preservation collision'
    else:
        with attachment.open('xb') as output:
            output.write(raw)
    for path, content in original.items():
        assert (ROOT / path).read_bytes() == content, 'affected input changed before live writes'
    assert membership == {p.relative_to(ROOT).as_posix(): state.parse_identifier(p.name)[1]
                          for p in state.iter_task_dirs(ROOT, ['tasks'])}
    for command in ('init', 'resume', 'knowledge', 'update'):
        canonical = (ROOT / f'.tfw/workflows/{command}.md').read_bytes()
        for directory in ('.claude/commands', '.agents/workflows'):
            assert (ROOT / f'{directory}/tfw-{command}.md').read_bytes() == canonical
    # Only exact parsed YAML keys select removals; all other source lines remain untouched.
    lines = original['.tfw/knowledge_state.yaml'].decode().splitlines(keepends=True)
    kept, removed = [], set()
    for line in lines:
        key = line.strip().split(':', 1)[0]
        if line.startswith('    ') and key in pairs:
            assert yaml.safe_load(line)[key] == pairs[key]
            removed.add(key)
        else:
            kept.append(line)
    assert removed == set(pairs)
    final_state = ''.join(kept).encode()
    expected = yaml.safe_load(original['.tfw/knowledge_state.yaml'])
    expected['knowledge']['processed_task_digests'] = unaffected
    assert yaml.safe_load(final_state) == expected
    STATE.write_bytes(final_state)  # state reconciliation precedes narrowing config
    config_text = original['.tfw/project_config.yaml'].decode()
    old = '''  # Ordered task containers. A task is CREATED in the first entry; a task is RESOLVED by
  # searching every entry in order. One concept, not two supported layouts.
  # This project lists two because the pre-2.0.0 corpus keeps its paths: renaming it would
  # have orphaned thousands of references and hundreds of commit subjects.
  task_containers: [workspace, tasks]'''
    new = '''  # Current work uses workspace. The owner-retained pre-2.0.0 corpus stays readable
  # at its original paths through the reference union, outside ordinary discovery/gates.
  # Historical disposition changes no task state; exact digest reconciliation follows
  # migrations/3.3.0.md with preserved affected pairs under update_receipts/.
  task_containers: [workspace]
  historical_containers: [tasks]'''
    assert old in config_text
    final_config = config_text.replace(old, new).replace('version: "3.2.0"', 'version: "3.3.0"')
    expected_config = yaml.safe_load(original['.tfw/project_config.yaml'])
    expected_config['tfw'].update(version='3.3.0', task_containers=['workspace'], historical_containers=['tasks'])
    assert yaml.safe_load(final_config) == expected_config
    CONFIG.write_bytes(final_config.encode())
    after_gate = state.knowledge_pending(ROOT)
    assert after_gate['removed_task_ids'] == before_gate['removed_task_ids'] == []
    assert set(after_gate['current_task_digests']).isdisjoint(pairs)
    assert not git('diff', '--name-only', BASELINE, '--', *membership)
    result = {'preservation': attachment.relative_to(ROOT).as_posix(),
              'historical_ids': len(membership), 'stateless_history': sum(not (p/'status.md').exists() for p in historical),
              'removed_pairs': len(pairs), 'unaffected_pairs': len(unaffected),
              'before_gate': before_gate, 'after_gate': after_gate,
              'historical_task_bytes_unchanged': True, 'unaffected_yaml_values_unchanged': True,
              'knowledge_bytes_unchanged': not bool(git('diff','--name-only',BASELINE,'--','knowledge','KNOWLEDGE.md')),
              'after_sha256': {p.relative_to(ROOT).as_posix(): sha(p.read_bytes()) for p in (CONFIG, STATE)}}
    (EVIDENCE/'repository-adoption.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('before_gate','after_gate')},indent=2))


if __name__ == '__main__':
    main()
