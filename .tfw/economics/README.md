# Task economics: portable Full contribution contract

This directory is a Full payload copied by init/update. The task's status, journal,
HL, TS, RF and REVIEW remain authority for lifecycle, work and acceptance. This
contract gives those roles a small, task-owned account of measured AI resource
consumption. It does not create a command, service, live portfolio cache, account
charge, human time sheet or quality score.

## Choose a source recipe

A participating unit selects its exact platform surface and native source when it
starts or resumes. Record the task/phase, declared owner from status/team, role,
actual working-unit address, exact source ID, numeric source path, range start
and timezone. Never select a source by latest title, account username,
project-wide history scan or a shared account's most recent session. A reused
source splits at proven bound ranges. The source ID names the stream the unit
writes itself — its own file, rollout or database — not an ID it merely inherits
from a parent or a shared session, so each child agent is its own source whose
totals add to its parent's. If a parent total is known to include a child,
declare each exact namespace:source-id with --includes-source; the receiver
excludes that inclusive parent while a named child is present.

The three recipes below are selected independently. All produce the same version 1
JSONL, pass the same validation and return through the existing role artifact
route. The producer keeps its source locally; the receiver needs the returned
JSONL bytes and SHA-256, not access to the producer's computer.
Routine files contain daily × bound source × model/effort token aggregates and
separate duration aggregates. Native event IDs are checked during extraction;
only their count and digest travel in the compact file. Keep detailed numeric
diagnostics only for a concrete reconciliation question.

### Codex rollout recipe

Source: one exact Codex rollout JSONL bound by session_meta.id to the unit.
Current observed surface is the Codex local task rollout. A child agent writes its
own rollout: its session_meta.id is its source ID, while its session_meta.session_id
and usage records name the root session. Usage must name the rollout's own ID or
the session its own metadata declares; any other session refuses the source. One
observed child (2026-09-29) shared no response ID with its parent's rollout.
The collector reads only
session metadata, turn_context model/effort, event_msg token_count,
token_usage_record numeric usage/thread counters and
task_started/task_complete/turn_aborted timing fields. It does not export
message text. Native response records are deduplicated by response_id and
their sum must equal the final thread_token_usage. When that verified stream
exists it supplies consumption; the cumulative token_count stream is checked
separately and any disagreement is recorded with both totals in source
diagnostics and the readable task report. The streams are never added.
Without response records, positive token_count cumulative differences supply
consumption: repeated snapshots are no-ops and each positive delta must match
last_token_usage. A reset, inconsistent native thread total, changed
response usage, missing session ID or malformed counter refuses measured
output. Cached input and cache writes are subsets of
input; reasoning is a subset of output. Model comes from the preceding turn
context, not the last model in the session. A matched native task_complete
duration is completed-turn time. Open or aborted turns have unknown duration
and their observed tokens still count. Source event timestamps support local
consumption dates with an explicit offset. A bounded source prefix is hashed and
the finite cutoff is recorded.

### Claude Code JSONL recipe

Source: the exact session's Claude Code JSONL (including the Code tab/CLI source
actually observed). A subagent in the same chat writes its own
`<sessionId>/subagents/agent-<agentId>.jsonl` and repeats the parent sessionId on
every line, so its source ID is `<sessionId>/<agentId>`; the session's own stays
`<sessionId>`. Only lines of the selected unit count, and a file whose lines belong
to another unit is refused with that unit's ID. In one observed Claude Code
2.1.281–2.1.284 session, the session file held no subagent lines and shared no
message ID with its subagents. Each assistant message ID is one response. Repeated blocks
for that ID retain the largest reported output after input/cache consistency
checks. Fresh input, cache read, five-minute and one-hour cache writes, and
output are preserved separately. Thinking is a diagnostic subset only when the
source exposes it; it is never added to output twice. Native agent execution
duration is unavailable in this JSONL; a five-minute-gap heuristic is neither
native duration nor a substitute. A Code-tab/CLI observation does not establish
the ordinary Claude Desktop chat surface. If a repeated response changes
input categories, refuse the measured result.

### Antigravity IDE numeric database recipe

Source: one exact Antigravity IDE 2.17.0 conversation database. The collector
opens SQLite read-only and takes a consistent in-memory backup; it reads only
gen_metadata.idx and gen_metadata.data. The bounded, observed protobuf mapping
is outer field 1 / nested field 4: fresh input field 2, cached input field 5,
candidate output field 3, thinking field 9, content field 10 and generation
duration field 11 (seconds/nanoseconds). Model is outer field 19. An absent
counter beside reported ones is zero, because proto3 omits zero-valued scalars.
A usage message that reports no counter at all, as observed for failed API calls,
measures nothing: the row is not counted and the source diagnostics give how many
were left out. A missing usage message is refused. A subagent writes its own
conversation database under its own UUID. The observed
invariant candidate = thinking + content is checked per row. Candidate already
includes thinking. Generation duration is model time, not full agent time.
gen_metadata alone does not prove a calendar date; rows remain undated until a
separately verified index/time join exists. A changed table, model encoding or
numeric relation yields an unsupported-source result, not a guessed report.
The private mapping is version-specific, not a provider guarantee.

## JSONL format and field map

One file contains a manifest first, then measured usage rows or one typed failure
row. Every line is UTF-8 JSON and the file ends with a newline. The public
machine-readable row type contract is record.schema.json. The standard-library
helper additionally checks arithmetic, date/offset agreement, ranges,
cross-row uniqueness and null reasons. Schema version 1 is the only writer.
Unknown versions and unknown core keys are errors. One optional extensions
object admits namespaced keys such as tfw.diagnostics; extensions never change
core totals or required gates.

| Field | Source or calculation | Required use |
|---|---|---|
| project, task, phase, owner, role, unit | task/phase status, dispatch and explicit bound working unit | expected/received comparison and group filters; no OS/account identity inference |
| source_namespace, source_id, source_version, source_sha256, source_size, source_label | exact source selection and captured bytes/numeric DB rows | prove source and decoder scope; never use role-bearing source keys for spend identity |
| revision, predecessor_sha256, range_start/end, complete | producer's bound range and prior returned file hash | successor/disjoint/overlap reconciliation |
| captured_at, cutoff, timezone, observed_at, consumption_date | collection clock and supported native event time or date-only source | finite tail and selected-period analysis; a known date needs no invented minute, while an unproved date is null |
| model, effort | observed turn/message/generation context | model grouping and exact rate selection; unobserved setting is null |
| fresh, cached, cache_write, cache_write_5m/1h, input, output, reasoning, total | native categories and mutually exclusive bucket sum | token comparison and dated API reference estimate; reasoning/cache are subsets |
| duration_seconds, duration_kind | native completed turn or generation timer | compare only the same time kind; no elapsed-minus-role waiting inference |
| tfw_version, coordination_mode | actually bound project/source state | optional comparison; missing historical binding is null |
| operation_seconds | producer's collector wall time | visible collection overhead, separate from provider agent time |
| unavailable | a specific reason for each absent optional value | distinguish unavailable from measured zero |
| failure code/detail | actual failed collection attempt | return accountability only, never measured coverage |

Validation requires finite nonnegative counters, input = fresh + cached +
cache_write, total = input + output, reasoning <= output and (when both known)
cache_write = five-minute + one-hour writes. A zero is an observed zero only.
The manifest's project/task/source/range applies to every row; row IDs are
unique in that file. Nulls have reasons. A failure-only file contains no usage.
The helper writes no version 2 migration. A future format change must preserve
the original file, emit a separately validated new file and document semantic
changes, source/revision mapping and the accepting authority. Rewriting old
task files during normal update is forbidden.

## Producer, transfer and reconciliation

At the normal return gate, a role captures its own source, validates its file,
records its SHA-256 and returns resolvable bytes/revision with RF, REVIEW, RES
or Coordinator return. On resume it produces a new file for the new bound range
or a verified successor; it does not overwrite the earlier return. An
unsuccessful collection returns a failure receipt with the attempted source
and precise cause. A missing interpreter permits a checked equivalent
extractor or an explicit failure receipt. The Python helper is the approved
narrow D82 economics exception; ordinary status, coordination and Knowledge
Gate operation require no Python, pip install or this helper.

The Coordinator compares the expected units from actual task-local
dispatch/return lineage with the actual returned bytes. receive checks task,
project and unit against the selected task root and copies the exact file into
economics/roles/ under its content hash. Repeating the same bytes is a no-op;
a remote pathname without readable bytes is not receipt. All revisions stay
available. A complete successor naming a verified predecessor and covering
its range replaces it for totals only when the earlier captured native source
prefix still hashes identically; disjoint ranges add. Missing predecessor,
unproved overlap, attribution conflict or one native source claimed by
multiple units is excluded and diagnosed. A unit whose measured files are all
excluded is reported as omitted, not as a failure, and the summary names it
beside the totals. A file captured under a source ID later shown wrong is not a
revision and cannot be superseded: keep it outside economics/roles/ with the
reason in the task record, then collect and return the corrected file.
A root task selection reads its
direct economics/roles files and each immediate phase-*/economics/roles leaf
whose phase status matches the task ID. Missing phase return bytes are shown
as coverage gaps; identical returned bytes are counted once. A phase report
selects only its own leaf. No parent report is added to child facts. Failed
and retried measured work remains. Old tasks need no
retroactive role file; an old partial export is labeled partial.

The finite cutoff can omit the producer's final message and later cleanup.
That tail is disclosed once and does not recursively trigger recapture.
Missing/unreadable expected unit bytes keep reconciliation incomplete. A
readable failure receipt satisfies the return obligation but proves no
measurement. Optional unavailable metrics and a small finite tail do not
block an otherwise accepted task.

## Commands, reports and prices

Run the helper with an available Python 3 standard-library interpreter:

- collect: exact --provider, --source, --source-id, --source-version,
  --project, --task, --owner, --role, --unit, --timezone, --start,
  --revision and --out. Use --phase and --end for a bounded phase/range.
  Use --predecessor for a successor, --includes-source for a known inclusive
  parent and --complete only when coverage is actually complete.
- failure: the same identity/source/range flags plus --code and --detail.
- validate followed by one or more returned files.
- receive: --source, --task-root, --project, --task and --expected-unit.
- report: one --task-root, --project, optional --expected-unit repeats,
  --primary-area and 3–5 --keyword values, and --out. The report keeps one
  structured metadata block in economics.md alongside readable purpose,
  accepted-result reference, totals, role/model detail, missing coverage,
  source hashes and cutoff. Supply --status-timezone for the explicit offset
  of the task status clock to calculate calendar elapsed; without it, elapsed
  remains unavailable.
- summary: repeat --task-root for selected roots; combine --date-from,
  --date-to, --project, --task, --tag, --role and --model; use --csv and
  --out for rebuildable exports. --show-helpdesk-afd renders the requested
  two-project view with an explicit no-captured-data row.

The task report lives beside status.md; a phase may have its own economics.md.
Numeric JSONL has no result narrative or quality score. Purpose and value
come from status/HL; accepted changes link RF/REVIEW after independent
acceptance. One primary product area and 3–5 local product keywords are
assigned at close. The area is additive, while overlapping keywords are
filters and never multiply totals. Changing classification edits only the
report metadata, not consumption rows.

Observed zero cache writes cost zero even if the optional five-minute and
one-hour split fields are null; positive unsplit writes remain explicitly
unpriced. Period spending uses dated events in the selected period, including ongoing
and unsuccessful work. Undated rows remain in lifetime totals and are
explicitly excluded from date filters. Completed-task mean/median use
selected completed task lifetime totals, count and range; partial coverage is
disclosed. Time rankings separate completed-turn, generation and provider
run seconds. Task calendar elapsed is a status/journal interval, not a sum of
parallel roles. Report prices are conditional Standard API equivalents from
rates.json at its dated epoch, never observed subscription charges. Unknown
model, token split or tariff condition stays unpriced while tokens remain.
Provider tools, Google cache storage, regional/long-context premiums and
subscription allocation are excluded unless separately evidenced and ruled.
No live network is needed to re-open a captured task.

## Receiver installation and update

Full init copies this directory and the economics report template as one
connected payload from its pinned source; update uses its pinned source and
ordinary conflict-preserving receiver rules. Inspect destination ownership
and existing bytes before replacement. A customized or ambiguous receiver
file is preserved for an explicit owner decision; no updater silently
overwrites or migrates task JSONL, status, role returns or a customized
price card. A repeat with identical source bytes is stable. The ten canonical
Full workflows and their ten Claude installed copies are the selected
entrypoints; Codex/Antigravity thin routers keep selecting canonical
workflows. Daily, Light, Assisted and Cursor targets are unchanged.

The package requires no pip module, daemon, shared database or account
change. If no Python interpreter is available, ordinary TFW continues and
the producer uses an equivalent checked extractor or a specific failure
receipt. Real distribution into another production project follows that
project's existing init/update authority.
