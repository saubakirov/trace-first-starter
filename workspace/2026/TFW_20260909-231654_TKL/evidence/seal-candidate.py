"""One-time immutable Candidate accounting and current Q3 observation; no product writes."""
from pathlib import Path
import collections
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[4]
TASK = 'workspace/2026/TFW_20260909-231654_TKL'
EVIDENCE = ROOT / TASK / 'evidence'
BASE = 'ec91c56007c20cda79f740fec15c85e4af74d17c'
CANDIDATE = '27cdb701b91c5b45b9f54b3e98c9ad67635b3e30'
APPROVAL = '2794cbdb40f6c4f3a7d4bce1f8d4eb949d9e6913'
TS_BLOB = 'f69fd4099a21a07ae2d17e6b5108b04ac94f107e'

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def write(path, data):
    assert not path.exists(), path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)

def output(path, data):
    write(path, (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode())

ts_path = TASK + '/TS__TFW_20260909-231654_TKL.md'
assert git('rev-parse', APPROVAL + ':' + ts_path).decode().strip() == TS_BLOB
assert git('rev-parse', CANDIDATE + ':' + ts_path).decode().strip() == TS_BLOB
ts = git('show', TS_BLOB).decode()
values = re.findall(r'^\| `([^`]+)` \| (?:MODIFY|CREATE|DELETE) \| VALUE \|', ts, re.M)
assurance = re.findall(r'^\| `([^`]+)` \| MODIFY \| ASSURANCE \|', ts, re.M)
assert len(values) == len(set(values)) == 58
assert len(assurance) == len(set(assurance)) == 7
tested = json.loads((EVIDENCE / 'checks/13-full/source-before.json').read_bytes())
tested_binding = {}
for name in values + assurance:
    entry = tested[name]
    path = ROOT / name
    if entry.get('absent'):
        assert not path.exists()
        assert subprocess.run(['git', 'cat-file', '-e', CANDIDATE + ':' + name], cwd=ROOT, capture_output=True).returncode != 0
        tested_binding[name] = {'tested_absent': True, 'candidate_absent': True}
    else:
        assert sha(path.read_bytes()) == entry['sha256'], name
        filtered = git('hash-object', '--path=' + name, str(path)).decode().strip()
        obj = git('rev-parse', CANDIDATE + ':' + name).decode().strip()
        assert obj == filtered, name
        tested_binding[name] = {'tested_raw_sha256': entry['sha256'], 'candidate_git_blob': obj,
                                'candidate_git_bytes_sha256': sha(git('show', obj)),
                                'normal_filter_identity_verified': True}

def parse_status(raw):
    fields = raw.rstrip(b'\0').split(b'\0') if raw else []
    rows = []
    while fields:
        status = fields.pop(0).decode()
        paths = [fields.pop(0).decode()]
        if status.startswith(('R', 'C')):
            paths.append(fields.pop(0).decode())
        rows.append({'status': status, 'paths': paths})
    return rows

def parse_numstat(raw):
    fields = raw.rstrip(b'\0').split(b'\0') if raw else []
    rows = []
    while fields:
        add, delete, path = fields.pop(0).split(b'\t', 2)
        paths = [path.decode()] if path else [fields.pop(0).decode(), fields.pop(0).decode()]
        rows.append({'paths': paths, 'additions': int(add) if add != b'-' else None,
                     'deletions': int(delete) if delete != b'-' else None})
    return rows

target = EVIDENCE / 'accounting/candidate-27cdb70'
commands = {}
for name, flag, selected in [('value-name-status', '--name-status', values),
                             ('value-numstat', '--numstat', values),
                             ('all-name-status', '--name-status', [])]:
    args = ['diff', flag, '--find-renames=50%', '-z', BASE, CANDIDATE, '--', *selected]
    raw = git(*args)
    write(target / (name + '.z'), raw)
    commands[name] = {'argv': ['git', *args], 'sha256': sha(raw), 'bytes': len(raw)}
status = parse_status((target / 'value-name-status.z').read_bytes())
numstat = parse_numstat((target / 'value-numstat.z').read_bytes())
inventory = parse_status((target / 'all-name-status.z').read_bytes())
assert {p for row in status for p in row['paths']} == set(values)
assert {tuple(row['paths']) for row in status} == {tuple(row['paths']) for row in numstat}
for row in inventory:
    classes = set()
    for p in row['paths']:
        if p in values:
            classes.add('VALUE')
        elif p in assurance:
            classes.add('ASSURANCE')
        elif p.startswith(TASK + '/') or p.startswith('.tfw/update_receipts/knowledge-lifecycle/'):
            classes.add('TRACE')
        else:
            raise AssertionError('Unclassified changed path: ' + p)
    assert len(classes) == 1, row
    row['class'] = classes.pop()
adds = sum(r['additions'] or 0 for r in numstat)
deletes = sum(r['deletions'] or 0 for r in numstat)
state = next(r for r in numstat if r['paths'] == ['tools/tfw_state.py'])
assert state['additions'] == 0
assert len(status) < 116 and adds + deletes < 5148
accounting = {'observed_at': datetime.now(timezone.utc).isoformat(), 'baseline': BASE,
 'candidate': CANDIDATE, 'approval': APPROVAL, 'ts_blob': TS_BLOB,
 'planned': {'logical_value_files': 58, 'additions': 1375, 'deletions': 1199, 'touched_text_loc': 2574},
 'actual': {'logical_value_files': len(status), 'additions': adds, 'deletions': deletes,
            'touched_text_loc': adds + deletes, 'binary_metric_na': [r for r in numstat if r['additions'] is None]},
 'planned_zero_additions_tools_state_preserved': True,
 'triggers': '58-file planning prompt already owner-approved; no added VALUE path, planned-zero growth or 2x trigger.',
 'commands': commands, 'value_name_status': status, 'value_numstat': numstat,
 'complete_baseline_candidate_inventory': inventory,
 'inventory_counts': dict(collections.Counter(r['class'] for r in inventory)),
 'tested_binding': tested_binding,
 'limits': ['Working raw CRLF bytes and normal-filter Git blobs are separate identities; matching filter identity binds tested files to Candidate.',
            'This accounting is not independent acceptance. Later excluded-only evidence does not replace Candidate.']}
output(target / 'accounting.json', accounting)

# One explicitly current observation; the omitted original map cannot be reconstructed as a past seal.
receipt = '.tfw/update_receipts/knowledge-lifecycle/0a435729c93141639ada55fb77a7508d47d0d1b9c159d50b6e05bdfb364ebacf/preservation.json'
original = json.loads((ROOT / receipt).read_bytes())
assert sha((ROOT / receipt).read_bytes()) == Path(receipt).parent.name
snapshots = [EVIDENCE / 'checks/01-02-source-before-corrections.json'] + sorted((EVIDENCE / 'checks').glob('*/source-before.json'))
snapshot_data = {str(p.relative_to(ROOT)).replace('\\', '/'): json.loads(p.read_bytes()) for p in snapshots}
identities = {}
for name in values:
    generations = {}
    for epoch in [BASE, CANDIDATE]:
        result = subprocess.run(['git', 'rev-parse', epoch + ':' + name], cwd=ROOT, capture_output=True)
        if result.returncode:
            generations[epoch] = {'absent': True}
        else:
            blob = result.stdout.decode().strip()
            generations[epoch] = {'git_blob': blob, 'git_bytes_sha256': sha(git('show', blob))}
    generations['observed_working_snapshots'] = {p: d[name] for p, d in snapshot_data.items() if name in d}
    identities[name] = generations
supplement = {'kind': 'CURRENT supplemental observation, Q3; procedural deviation remains for independent Reviewer',
 'observed_at': datetime.now(timezone.utc).isoformat(), 'author_unit': '01a09a0c-c9e2-7d01-af4e-64931af967ed',
 'principal': 'robert', 'baseline': BASE, 'candidate': CANDIDATE, 'approval': APPROVAL, 'ts_blob': TS_BLOB,
 'ruling': '144e3e651382330afba4d7131a562d05e7f515f9', 'direct_dispatch': 'bb3c2803e610bd5fe1cc6eed040b73a6cb2a40aa',
 'original_attachment': {'path': receipt, 'sha256': sha((ROOT / receipt).read_bytes()),
  'preserved_raw_commit': '9c05a0d44d53cf99d07f2ab4eecd8c45369713de', 'unchanged_now': True},
 'deviation': 'The original preservation attachment omitted the separate old/intended reader/adapter identity map. This omission is not repaired or retrospectively sealed by this current observation.',
 'unknown': ['Pre-application working-tree reader/adapter bytes and their line endings',
             'Contemporaneous reader-map sealing, which the original attachment did not record',
             'Per-reader installation times'],
 'observation_limits': ['Baseline Git objects establish reconstructable old source identities, not the unknown checkout/timing facts.',
  'Initial source snapshot was taken during the first affected test run at 2026-09-13T10:20:40.956326+00:00, not before adoption or that run.',
  'Each later source-before snapshot describes its own actual test-input generation.',
  'Neither Executor nor Coordinator accepts the reconstruction or adoption/provenance completeness; independent Reviewer judges the remaining defect.',
  'Prospective established adoption will establish only its own procedure and cannot rewrite this self-adoption history.'],
 'original_intended': original['intended'],
 'final_entry_generation': json.loads((EVIDENCE / 'checks/current-map-correction.json').read_bytes()),
 'final_config_raw_sha256': sha((ROOT / '.tfw/project_config.yaml').read_bytes()),
 'final_entry_raw_sha256': sha((ROOT / 'KNOWLEDGE.md').read_bytes()),
 'map_scope': 'All 58 approved VALUE paths, including canonical readers, installed copies, routers, role forms and associated implementation; explicit absence for create/delete generations.',
 'identities': identities,
 'snapshot_manifest_hashes': {p: sha((ROOT / p).read_bytes()) for p in snapshot_data}}
assert supplement['final_config_raw_sha256'] == original['intended']['.tfw/project_config.yaml']
assert supplement['final_entry_raw_sha256'] != original['intended']['KNOWLEDGE.md']
output(EVIDENCE / 'adoption/q3-current-observation.json', supplement)
print(json.dumps({'candidate': CANDIDATE, 'actual': accounting['actual'], 'inventory': accounting['inventory_counts'],
                  'q3_sha256': sha((EVIDENCE / 'adoption/q3-current-observation.json').read_bytes())}))
