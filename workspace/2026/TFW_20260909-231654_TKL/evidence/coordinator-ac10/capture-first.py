"""Coordinator-only custody export. Never executed or installed in the consumer root."""
import datetime
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).parent
PRE = json.loads((ROOT / '01-predispatch.json').read_text(encoding='utf-8'))
TURN = '01a09b6a-6513-73f3-9ab6-f36149196b7c'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def save(name, value):
    destination = ROOT / name
    assert not destination.exists(), 'Custody files are append-only'
    destination.write_bytes((json.dumps(value, indent=2, ensure_ascii=True) + '\n').encode('utf-8'))


session = Path(PRE['session_prefix']['path'])
raw = session.read_bytes()
boundary = PRE['session_prefix']['bytes']
assert sha(raw[:boundary]) == PRE['session_prefix']['sha256'], 'Session prefix changed'
rows = [json.loads(line) for line in raw[boundary:].splitlines()]
completions = [row for row in rows if row['type'] == 'event_msg'
               and row.get('payload', {}).get('type') == 'task_complete'
               and row['payload'].get('turn_id') == TURN]
assert len(completions) == 1, 'Original first turn has not completed exactly once'
complete = completions[0]
cutoff = complete['ordinal']
rows = [row for row in rows if row['ordinal'] <= cutoff]
starts = [row for row in rows if row['type'] == 'event_msg'
          and row.get('payload', {}).get('type') == 'task_started']
assert len(starts) == 1 and starts[0]['payload']['turn_id'] == TURN
answer = complete['payload']['last_agent_message']
assert isinstance(answer, str) and answer.strip()

consumer = Path(PRE['consumer_root'])
files = {p.relative_to(consumer).as_posix(): p for p in consumer.rglob('*') if p.is_file()}
assert set(files) == set(PRE['input_files'])
current = {}
for name, path in files.items():
    data = path.read_bytes()
    current[name] = {'sha256': sha(data), 'bytes': len(data)}
assert current == PRE['input_files'], 'Consumer input changed'
envelope = consumer.parent
assert sha((envelope / 'manifest.json').read_bytes()) == PRE['manifest_sha256']
assert sha((envelope / 'oracle/expected.json').read_bytes()) == PRE['oracle_sha256']
assert sha((envelope / 'neutral-question.txt').read_bytes()) == PRE['question_sha256']

# Export only visible tool arguments/results, completed visible operations/messages,
# the dispatched user message, and actual turn clocks. Never export reasoning,
# system/developer instructions, unrelated history, compaction or world state.
trail = []
for row in rows:
    payload = row.get('payload', {})
    kind = payload.get('type')
    cleaned = None
    if row['type'] == 'response_item' and kind in {
        'function_call', 'function_call_output', 'custom_tool_call', 'custom_tool_call_output'
    }:
        cleaned = {k: v for k, v in payload.items()
                   if k != 'internal_chat_message_metadata_passthrough'}
    elif row['type'] == 'event_msg' and kind in {'task_started', 'task_complete'}:
        cleaned = {k: payload[k] for k in ['type', 'turn_id', 'started_at', 'completed_at', 'duration_ms']
                   if k in payload}
    elif row['type'] == 'event_msg' and kind == 'item_completed':
        item = payload.get('item', {})
        if item.get('type') in {'commandExecution', 'mcpToolCall'}:
            cleaned = {k: payload[k] for k in ['type', 'thread_id', 'turn_id', 'item',
                                               'started_at_ms', 'completed_at_ms'] if k in payload}
        elif item.get('type') == 'agentMessage' and item.get('phase') in {'commentary', 'final_answer'}:
            cleaned = {k: payload[k] for k in ['type', 'thread_id', 'turn_id', 'item',
                                               'started_at_ms', 'completed_at_ms'] if k in payload}
    if cleaned is not None:
        trail.append({'timestamp': row['timestamp'], 'ordinal': row['ordinal'],
                      'type': row['type'], 'payload': cleaned})

calls = [row for row in trail if row['type'] == 'response_item'
         and row['payload']['type'] in {'function_call', 'custom_tool_call'}]
finished = datetime.datetime.fromisoformat(complete['timestamp'].replace('Z', '+00:00'))
admitted = datetime.datetime.fromisoformat(PRE['admitted_at'])
observed = datetime.datetime.now(datetime.timezone.utc).isoformat()
answer_path = ROOT / '02-first-answer.txt'
assert not answer_path.exists()
answer_path.write_bytes(answer.encode('utf-8'))
save('03-visible-tool-trail.json', trail)
save('04-original-turn-clock.json', {
    'start': starts[0],
    'completion': {'timestamp': complete['timestamp'], 'ordinal': complete['ordinal'],
                   'type': complete['type'],
                   'payload': {k: v for k, v in complete['payload'].items() if k != 'last_agent_message'}},
    'conservative_dispatch_clock': PRE['admitted_at'],
    'deadline': PRE['deadline'],
    'elapsed_from_dispatch_seconds': (finished - admitted).total_seconds(),
    'within_20_minutes': finished <= datetime.datetime.fromisoformat(PRE['deadline']),
    'deductions_seconds': 0,
})
save('05-original-custody.json', {
    'observed_at': observed, 'producer': PRE['destination_unit'], 'turn_id': TURN,
    'parent_and_custodian': PRE['source_unit'], 'source_session': str(session),
    'source_prefix': PRE['session_prefix'], 'first_new_ordinal': rows[0]['ordinal'],
    'completion_ordinal': cutoff, 'first_answer_path': answer_path.name,
    'first_answer_sha256': sha(answer_path.read_bytes()), 'first_answer_bytes': answer_path.stat().st_size,
    'visible_trail_sha256': sha((ROOT / '03-visible-tool-trail.json').read_bytes()),
    'native_tool_invocations': len(calls),
    'calls_for_manual_operation_count': [{'ordinal': row['ordinal'], 'name': row['payload'].get('name'),
                                         'type': row['payload']['type']} for row in calls],
    'input_path_set_and_bytes_unchanged': True, 'input_files': current,
    'manifest_sha256': PRE['manifest_sha256'], 'oracle_sha256': PRE['oracle_sha256'],
    'question_sha256': PRE['question_sha256'], 'prior_exposure': PRE['prior_exposure'],
    'reasoning_or_unrelated_history_exported': False,
    'scope': 'Original first answer and observable tool/clock/input custody only, sealed before scoring. '
             'This export makes no per-criterion judgment or OS containment claim.',
})
print(json.dumps({'answer_bytes': answer_path.stat().st_size, 'answer_sha256': sha(answer_path.read_bytes()),
                  'calls': len(calls), 'elapsed_seconds': (finished-admitted).total_seconds(),
                  'sealed_at': observed}, indent=2))
