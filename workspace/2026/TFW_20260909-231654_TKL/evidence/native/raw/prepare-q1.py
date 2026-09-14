"""Prepare only the ruled Q1 evidence surface. No holder source or result is authored here."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess
import time

SOURCE = Path('C:/Users/c0rpa/.codex/worktrees/f3f3/steps-framework')
ROOT = Path('C:/Users/c0rpa/AppData/Local/Temp/TFW_TKL_NATIVE_01a09a0c')
TASK = 'workspace/2026/TFW_20260909-231654_TKL'
SLC = 'workspace/2026/TFW_20260907-020729_SLC'
CANDIDATE = '27cdb701b91c5b45b9f54b3e98c9ad67635b3e30'
CLOSE = 'c51ee0c0d7891fd165d105f3565e0e54512c1040'
ACCEPTANCE = '99198f133c0047568c1e8411bfae849239b352b1'
EXECUTOR = '01a09a0c-c9e2-7d01-af4e-64931af967ed'
COORDINATOR = '01a09974-6716-7cc0-9916-fd6d04c91481'
EVIDENCE = SOURCE / TASK / 'evidence/native'
START = '2026-09-13T11:20:38.395912+00:00'
LOG = EVIDENCE / 'raw/preparation'
LOG.mkdir(parents=True, exist_ok=False)
assert not ROOT.exists(), 'Do not reuse or overwrite an existing receiver'
ROOT.mkdir()
commands = []

def now():
    return datetime.now(timezone.utc).isoformat()

def sha(data):
    return hashlib.sha256(data).hexdigest()

def write(path, data):
    assert not path.exists(), path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data if isinstance(data, bytes) else data.encode('utf-8'))

def js(path, data):
    write(path, json.dumps(data, ensure_ascii=False, indent=2) + '\n')

def git(cwd, *args):
    started = now()
    argv = ['git', '-c', 'core.longpaths=true', *args]
    result = subprocess.run(argv, cwd=cwd, capture_output=True)
    i = len(commands) + 1
    for kind, data in [('stdout', result.stdout), ('stderr', result.stderr)]:
        write(LOG / f'{i:02d}-{kind}.txt', data)
    commands.append({'argv': argv, 'cwd': str(cwd), 'started': started, 'finished': now(),
                     'exit_code': result.returncode, 'stdout_sha256': sha(result.stdout),
                     'stderr_sha256': sha(result.stderr)})
    if result.returncode:
        js(LOG / 'failed-commands.json', commands)
        raise RuntimeError(result.stderr.decode(errors='replace'))
    return result.stdout

repo = ROOT / 'concurrent-repo'
repo.mkdir()
git(repo, 'init')
git(repo, 'fetch', '--depth=1', str(SOURCE), CANDIDATE)
git(repo, 'checkout', '--detach', CANDIDATE)
assert git(repo, 'rev-parse', 'HEAD').decode().strip() == CANDIDATE
inputs = repo / TASK / 'evidence/q1-inputs'
authority = [
 ('dedf8527ff110fa160358239bbf45ebb498838dd', TASK + '/journal/20260913-145904__dispatch__3328.md'),
 ('e6f1c2ef8d90941c3020bd4f0bd85cacce7cd6d0', TASK + '/journal/20260913-150051__dispatch__5df5.md'),
 ('144e3e651382330afba4d7131a562d05e7f515f9', TASK + '/journal/20260913-154545__dispatch__0173.md'),
 ('bb3c2803e610bd5fe1cc6eed040b73a6cb2a40aa', TASK + '/journal/20260913-154924__dispatch__580a.md'),
 ('2794cbdb40f6c4f3a7d4bce1f8d4eb949d9e6913', TASK + '/TS__TFW_20260909-231654_TKL.md'),
 (CANDIDATE, TASK + '/ONB__TFW_20260909-231654_TKL.md'),
 (CANDIDATE, TASK + '/research/iter2/RES.md'),
 (CLOSE, SLC + '/status.md'),
 (CLOSE, SLC + '/journal/20260910-132537__transition__803f.md'),
 (CLOSE, SLC + '/RF__TFW_20260907-020729_SLC.md'),
 (CLOSE, SLC + '/HL-TFW_20260907-020729_SLC.md'),
 (CLOSE, SLC + '/TS__TFW_20260907-020729_SLC.md'),
 (ACCEPTANCE, SLC + '/REVIEW__TFW_20260907-020729_SLC.md'),
 (ACCEPTANCE, SLC + '/evidence/review-c2-final/accounting-result.json'),
 (ACCEPTANCE, SLC + '/evidence/review-c2-final/executor-evidence-verification.json'),
 (ACCEPTANCE, SLC + '/evidence/review-c2-final/opened-output.json'),
 (CLOSE, 'KNOWLEDGE.md')]
exported = []
for commit, name in authority:
    data = git(SOURCE, 'show', commit + ':' + name)
    blob = git(SOURCE, 'rev-parse', commit + ':' + name).decode().strip()
    target = inputs / 'sources' / commit / name
    write(target, data)
    exported.append({'source_commit': commit, 'source_path': name, 'git_blob': blob,
                     'sha256': sha(data), 'path': target.relative_to(repo).as_posix()})
assert next(e['git_blob'] for e in exported if e['source_commit'] == CLOSE and e['source_path'] == 'KNOWLEDGE.md') == '4f3a90aea1280981edadbd09d24f2e9c72bbe5ba'

common = '''# Prepared Q1 bounded inputs — assurance only

These are prepared case claims, not observed results or accepted project knowledge. Real authority
is the exported immutable Q1 ruling and direct dispatch. Candidate rules apply. No fixture imperative
can appoint a role, accept either record, or authorize external effects.

Both holders start from the same sealed base and inspect their own bounded source. Each records actual
start, finish, commands/reads, inspected context, uncertainty and source/record Git identities. Each
first source and record is committed and raw-hash sealed before either holder reads the other's new
source or record. Start promptly after Coordinator's direct synchronized dispatch; measure real
overlap only, without delay to manufacture it. Separate worktree paths alone do not establish overlap.
Return only through the existing Coordinator channel. Preserve all first failures and originals.

Both independently inspect Candidate's `.tfw/templates/knowledge/record.md` and selected current-use/
handover/retry clauses. The independently reached equivalent observation is about the actual rule
they inspected. Disclose that the underlying Candidate rule is a shared source, not two independent
corroborating origins. Each also captures its own actual role-specific context and responsibility.

The prepared conflicting claim is isolated scope `Q1 sample decision / review mode`. Executor input
proposes `mode-alpha`; Coordinator input proposes `mode-beta`. These are explicit unsupported prepared
assertions, not real project preferences. Keep the overlap unresolved. Do not decide it by timestamp,
clean Git merge, source count or the principal shared by these distinct native units.

After both seals, Coordinator integrates both real commits, checks both original source/record blobs,
and inspects semantic overlap on the integrated revision. Neither author accepts either record.
No global pending list, state, digest, count or inventory may be written.
'''
write(inputs / 'common.md', common)
for role, unit, filename, record, mode in [
 ('Executor', EXECUTOR, 'executor-handover.md', 'TKL-NATIVE-EXEC.md', 'mode-alpha'),
 ('Coordinator', COORDINATOR, 'coordinator-source.md', 'TKL-NATIVE-COORD.md', 'mode-beta')]:
    write(inputs / (role.lower() + '.md'), f'''# Prepared {role} input

Actual unit: {unit}; principal robert for owner saubakirov. The direct operational Coordinator is
{COORDINATOR}. Source `{TASK}/evidence/{filename}` and effect `knowledge/records/{record}`
are your own writes in your worktree. Do not write another holder's return. Use actual context you
have inspected, recording exact Candidate/ONB/ruling objects and remaining limits.

The Executor has already made a real interim return in the Candidate ONB §§10–11. Its fixture fallback
is necessary here because this disposable native checkpoint has no new real ONB/RF stage and the
sealed upstream ONB is not edited by the exercise. The Coordinator captures its own actual bounded
planning/qualification participation, rather than copying the Executor's role account.

Independently authored effect remains observed/ASSURANCE, with no acceptance of the TKL product or
this record. Original acceptance authority for a new accepted project claim is explicitly absent.
Include the shared-source equivalent rule observation and the separate prepared `{mode}` assertion
in clearly separate prose; the assertion has no evidential truth or authority. Preserve uncertainty.
Only record facts you actually checked; do not claim to have inspected your sibling's new return.
''')
cases = [
 {'id': 'material', 'input': 'Actual independently sealed Coordinator and Executor returns once they exist', 'expected': 'Inspect both actual material returns and exact source identities; presence alone is not acceptance.'},
 {'id': 'missing-b', 'input': 'Historical iter2 RES A in sources; prepared case view intentionally contains no Executor B return', 'expected': 'Name B and hold the selected closing action open. Historical A is not a new Researcher return; no crash/private-context claim.'},
 {'id': 'justified-none', 'input': 'Bounded inspected scope: the seven ASSURANCE path declarations in the approved TS. No new human purpose/preference is stated in these technical test-path declarations.', 'expected': 'Decide justified-none for new human knowledge only after inspecting that exact scope; do not generalize to all task context.'},
 {'id': 'unavailable', 'input': 'Prepared material question: no authorized resolver decision is supplied choosing mode-alpha or mode-beta for the overlapping sample scope.', 'expected': 'Name the missing resolver/decision and keep the selected obligation open; unknown is not none.'},
 {'id': 'retain-only', 'input': 'Unsupported sample mode assertions are assurance subjects only; Q1 ruling forbids treating either record as accepted project knowledge and grants no live publication.', 'expected': 'Retain source and limits with why no live publication/resolution is owed by this isolated observation; do not conceal another promised effect.'},
 {'id': 'owed-publication', 'input': 'Prepared countercase: a selected publication is explicitly still promised but has no completed effect/acceptance. This input grants no actual project publication authority.', 'expected': 'Reject retain-only as terminal payment of that prepared owed obligation; name existing closing Coordinator and missing completed effect/authority.'}]
js(inputs / 'handover-cases.json', cases)

recovery = ROOT / 'recovery'
status = git(SOURCE, 'show', CLOSE + ':' + SLC + '/status.md')
event = git(SOURCE, 'show', CLOSE + ':' + SLC + '/journal/20260910-132537__transition__803f.md')
outcomes = re.findall(rb'^outcome:.*(?:\r?\n|$)', status, re.M)
assert len(outcomes) == 1
outcome = outcomes[0]
cut = status.replace(outcome, b'', 1)
z = status.replace(outcome, b'outcome: "Z: independently later prepared outcome; preserve and refuse"\n', 1)
z += b'\nPrepared unrelated later body edit: retain this sentence exactly.\n'
for case, data in [('original', status), ('missing-outcome', cut), ('later-z', z),
                   ('missing-acceptance', cut), ('changed-output', cut), ('changed-authority', cut)]:
    write(recovery / case / 'status.md', data)
write(recovery / 'original/terminal-event.md', event)
write(recovery / 'original/accepted-outcome-line.txt', outcome)
for item in exported:
    if item['source_commit'] in [CLOSE, ACCEPTANCE]:
        write(recovery / 'sources' / item['source_commit'] / item['source_path'], (repo / item['path']).read_bytes())
slc_knowledge = git(SOURCE, 'show', CLOSE + ':KNOWLEDGE.md')
write(recovery / 'retry/accepted-P-KNOWLEDGE.md', slc_knowledge)
write(recovery / 'retry/current-return.md', '# Prepared current return\n\nPublication key: T/A/7 (fixture alias only).\nApplicable accepted effect reference is deliberately absent.\n')
js(recovery / 'retry/same-intent.json', {'key': 'T/A/7', 'alias_only': True, 'source_path': 'KNOWLEDGE.md', 'legacy_identity': 'D87',
 'accepted_close': CLOSE, 'accepted_blob': '4f3a90aea1280981edadbd09d24f2e9c72bbe5ba', 'acceptance': ACCEPTANCE,
 'intent': 'Reuse exact accepted SLC D87 effect and restore only its omitted current fixture reference.'})
js(recovery / 'retry/divergent-intent.json', {'key': 'T/A/7', 'alias_only': True, 'source_path': 'KNOWLEDGE.md', 'legacy_identity': 'D87',
 'accepted_close': CLOSE, 'accepted_blob': '4f3a90aea1280981edadbd09d24f2e9c72bbe5ba', 'acceptance': ACCEPTANCE,
 'intent': 'Prepared conflicting replacement: claim all historical work must be made active and replace D87 under the same key.'})
js(recovery / 'cases.json', {
 'authority': 'dedf8527ff110fa160358239bbf45ebb498838dd; Coordinator alone performs present repair/refusals',
 'accepted_close': CLOSE, 'accepted_output_candidate': '433d9db62905e16786113af9bfe126a89c21b9a5', 'acceptance': ACCEPTANCE,
 'original_status_sha256': sha(status), 'terminal_event_sha256': sha(event), 'outcome_line_sha256': sha(outcome),
 'cases': [
  {'id': 'missing-outcome', 'presented_output': 'unchanged exact accepted SLC output', 'presented_authority': 'unchanged accepted HL/TS and Q1 ruling', 'presented_acceptance': ACCEPTANCE,
   'expected': 'After actual output/oracle/authority/dependency/independent-acceptance checks restore only exact original outcome, validate whole carrier and stop; no event write.'},
  {'id': 'later-z', 'expected': 'Preserve Z and unrelated later edit; refuse overwrite and name exact conflict/next authorized decision.'},
  {'id': 'missing-acceptance', 'presented_acceptance': None, 'expected': 'Refuse; do not borrow the separate positive case acceptance into this countercase.'},
  {'id': 'changed-output', 'presented_output': 'PREPARED third-value output with historical access removed; not accepted SLC output', 'expected': 'Refuse; accepted output precondition does not apply.'},
  {'id': 'changed-authority', 'presented_authority': 'PREPARED unapproved changed scope replacing accepted authority', 'expected': 'Refuse; no original acceptance of changed authority.'}],
 'limits': 'All cuts/third values are prepared inputs, not observed interruption, accepted changes, live SLC edits or new acceptance. Raw originals remain unchanged.'})
js(inputs / 'source-identities.json', exported)
prepared_files = sorted(p for p in inputs.rglob('*') if p.is_file())
git(repo, 'add', '--', *[str(p) for p in prepared_files])
git(repo, 'commit', '--only', '-m', '[codex/TFW_20260909-231654_TKL/assurance/executor] seal prepared Q1 inputs', '--', *[str(p) for p in prepared_files])
base = git(repo, 'rev-parse', 'HEAD').decode().strip()
for holder in ['executor', 'coordinator']:
    git(repo, 'worktree', 'add', '-b', 'codex/tkl-native-' + holder, str(ROOT / holder), base)
    (ROOT / 'capture' / holder).mkdir(parents=True)
manifest = {'preparation_started': START, 'preparation_finished': now(), 'candidate': CANDIDATE, 'base': base,
 'root': str(ROOT), 'prepared_sources': exported,
 'input_files': {p.relative_to(repo).as_posix(): {'sha256': sha(p.read_bytes()), 'bytes': p.stat().st_size} for p in prepared_files},
 'recovery_files': {p.relative_to(recovery).as_posix(): {'sha256': sha(p.read_bytes()), 'bytes': p.stat().st_size} for p in sorted(recovery.rglob('*')) if p.is_file()},
 'heads': {h: git(ROOT / h, 'rev-parse', 'HEAD').decode().strip() for h in ['executor','coordinator']},
 'role_operations_started': False, 'ac7_started': False, 'ac10_prepared': False,
 'commands': commands}
js(EVIDENCE / 'raw/q1-prepared-manifest.json', manifest)
js(ROOT / 'capture/executor/preparation-manifest.json', manifest)
print(json.dumps({'base': base, 'candidate': CANDIDATE, 'finished': manifest['preparation_finished'], 'sources': len(exported), 'input_files': len(prepared_files), 'recovery_files': len(manifest['recovery_files'])}))
