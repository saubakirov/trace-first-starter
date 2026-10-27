# Task economics: portable contribution contract

This directory is a Full payload copied by init/update. The task's status, journal,
HL, TS, RF and REVIEW remain authority for lifecycle, work and acceptance. This
contract gives those roles a small, task-owned account of measured AI resource
consumption. It does not create a service, live usage portfolio, account
charge, human time sheet or quality score.

Standard product analysis lives in [TFW Economics](../workflows/economics.md).
[Daily](../extensions/daily-task/SKILL.md) uses its own selected record and authority with the
same numeric v1 contract; no Full status/profile is fabricated. Its routine obligation is a
cumulative snapshot before every orderly turn return and a final snapshot/concise summary.

## Choose a source recipe

A participating unit selects its exact platform surface and native source when it
starts or resumes. Record the task/phase, declared owner from status/team, role,
actual working-unit address, exact source ID, numeric source path, range start
and timezone. Never select a source by latest title, account username,
project-wide history scan or a shared account's most recent session. A reused
source splits at proven bound ranges. The source ID names the stream the unit
writes itself — its own file, rollout or database — not an ID it merely inherits
from a parent or a shared session, so each child agent is its own source whose
totals add separately when observed parent counters exclude it. If a parent total is known to include a child,
declare each exact namespace:source-id with --includes-source; the receiver
excludes that inclusive parent while a named child is present.

The provider recipes are selected independently. All produce the same version 1
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

### Claude Code and Antigravity

Read only the active surface's procedure: [Claude Code](claude-code.md) or
[Antigravity CLI / IDE / Desktop](antigravity.md). These own runtime-root discovery,
exact source binding, supported formats and collection limits. The common contract
below owns identity, receipt semantics and failure/accountability for every provider.

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

### Explicit selected Daily record

Pass `--record` to receive/report, or one `--record` per selected Daily root to summary. The
record must be an existing file contained by its exact `--task-root`; never infer Daily merely
because status is missing. Preserve the chosen receiving form/split and append one single-line
HTML comment beginning `<!-- tfw-economics-record-v1 `, followed by one JSON object and ` -->`.
This is analytical binding metadata, not lifecycle, identity authentication or permission.
The selected record's request/checkpoint remains authority for its human/worker and work.

| Binding key | Actual content |
|---|---|
| schema_version | 1, independent of the unchanged numeric schema |
| id | Exact immutable Daily folder ID, matching selected root name |
| project, goal, value, created | Declared receiving project, actual intended result/value, observed creation clock |
| owner | Actual declared accountable human; null if unresolved, never a guessed account handle |
| result_state (optional) | Actual prepared/checked/accepted state in the local form; never Full lifecycle |
| binding_outcomes (optional) | Retained typed nonmeasured binding-gap objects, not numeric usage rows |

A binding-gap object has kind `binding_unavailable`, actual producer, offset-aware observed_at,
precise code/detail, known facts object, unavailable reasons object, attempted_extraction false,
and last_good (returned numeric file SHA-256 or null). Required unavailable binding is distinct
from an attempted extraction failure; a manifest with unknown core fields remains invalid.
Keep the actual producer attributable in the record even if a required numeric unit/source ID
cannot be resolved. Receive known-binding v1 JSONL into this root's economics/roles under its
exact hash. For report/summary, prior known-binding rows must match record project/owner/task;
unknown historical ownership needs an explicit independent selection, never automatic relabeling.
The report displays record-local gaps even with no numeric rows. A last_good digest requires
resolvable received bytes; a path alone proves no receipt.

Minimal valid binding-gap shape, illustrated by a hypothetical unavailable native ID
(the example is not evidence of any actual failure):

```json
{"kind":"binding_unavailable","producer":"declared-worker","observed_at":"2026-10-27T12:00:00+05:00","code":"native_id_unavailable","detail":"Current invocation exposes no verifiable source ID after the recorded bounded checks.","known":{"role":"executor"},"unavailable":{"source_id":"No own ID in the inspected runtime metadata"},"attempted_extraction":false,"last_good":null}
```

Use the exact keys `known` and `unavailable`; record actual values and checked grounds.
For Daily this object belongs in `binding_outcomes`; `report --record` validates the
selected record. Full records the same facts in its owned role artifact. A valid
shape does not prove the cause. Known identity/path plus denied access or an
unsupported decoder is an attempted extraction failure when actually attempted,
not missing binding. Use `failure` with that known bound and actual cause; never
invent an end solely to fit the format. Record a genuinely unknown bound as a gap.
If access denial prevents discovering the end, retain the known source ID/path
under `known` and explain the missing `range_end` under `unavailable`; do not label
a known source ID unavailable. If the full bound is known, return an actual
failure receipt instead of a `binding_unavailable` object.
Optional unknown duration does not erase measured tokens; a native process's SUCCESS
with a denied action does not establish successful collection.

Before each Daily return, bind the current physical source end, validate a cumulative capture
and return its actual numbers plus hash/range/revision/cutoff. `--complete` asserts completeness
of the selected bound only, with grounds; open turns and later consumption remain unknown tails.
A verified covering successor checks predecessor identity, revision and unchanged source prefix.
Alternatively retain exact disjoint facts and a checked cumulative view/membership before return.
Never sum cumulative revisions. Capture the final snapshot and concise summary on completion;
retain prior revisions and precise failures. Interruptions are gaps; later reconstruction cannot
prove a snapshot existed at its original return. Final-answer/cleanup tail is disclosed once.

### Full cycle and finite outcomes

Each Full role captures its own bound source at its final durable RF, REVIEW, RES or
Coordinator return. The Coordinator's final integration/close capture follows required role
results and relevant checks, immediately before final owner delivery under the existing close
order. This is a common semantic checkpoint, not a simultaneous timestamp or another acceptance
gate. Planning and unfinished-cycle estimates are labeled interim and compared only as such.
An ordinary intermediate chat reply needs no capture. Daily retains its separate cadence above.

| Observed condition | Owned return and continuation |
|---|---|
| Required binding known; extraction succeeds | Validate numeric v1 JSONL; return resolvable bytes, revision, SHA-256, range and cutoff in the existing role artifact. |
| Required binding unavailable before extraction | In that artifact record the actual producer and observed epoch, known binding facts, exact missing facts/reasons, extraction not attempted, and any last-good returned bytes/hash (or none). Emit no invalid JSONL, invented source/range, failed attempt or measured zero. |
| Known binding; attempted extraction fails | Return the unchanged v1 failure receipt with the actual attempted source/range and precise cause; preserve any last-good measurement. |
| Optional metric unavailable | Use null with its specific reason only where numeric v1 permits it. Valid measured categories remain usable. |
| Expected return missing or unreadable | Reconciliation remains incomplete; name the missing producer/return and route the unresolved obligation. |

A readable, attributable pre-extraction binding-gap disposition or valid failure receipt
discharges ordinary collection accountability, while its coverage remains unmeasured. Full
binding gaps are human-readable role evidence: the unchanged helper does not parse them or count
them as numeric receipts. The authorized Coordinator/analyst reads them alongside numeric output.
An explicit measurement deliverable or required product proof still follows its actual blocking
route; accountable nonmeasurement cannot satisfy it. Available own-source capture remains owed.

`complete: true` attests the entire selected source bound, with grounds; it does not assert a
finished turn, role or task. For example, fully reading a source prefix while a role is active
can establish selected-bound completeness; future activity remains outside it. On resume return
a new disjoint contribution or verified covering successor, preserving earlier bytes. Never
promote an actually incomplete successor to make a total look current.

A missing interpreter permits a checked equivalent extractor or an actual failure receipt.
The Python helper is the approved
narrow D82 economics exception; ordinary status, coordination and Knowledge
Gate operation require no Python, pip install or this helper.

The Coordinator compares expected invocations from actual task-local dispatch,
helper/child launch and return lineage with returned bytes and checked gaps. Include
failed/retried and auxiliary work even when it has no formal role label; accounting
membership grants no role authority. Check the returned bounded search, surface,
identity and cause against the selected provider procedure; return unsupported
claims for correction without reading another unit's private transcript. Distinguish
unperformed search, missing binding, denied access and unsupported extraction.
receive checks task,
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

Show expected/received units separately from each selected source/revision/range and its
excluded or missing coverage, next to the estimate. Receipt of every file does not establish a
current whole-cycle total. Last-good measurement and a later nonmeasured outcome coexist.

The finite cutoff excludes final delivery, short subsequent exchanges and safe cleanup.
Disclose this tail once; it does not recursively trigger recapture. Substantive reopened work
is a separately bounded continuation, never hidden in that tail. Optional unavailable metrics
and a small finite tail do not block an otherwise accepted result; material missing evidence
retains its existing gate.

Nonmeasured failed attempts never arbitrate or supersede measured ranges. Retain their hashes,
attempted bounds, precise code/detail and chronological latest outcome alongside usable prior
measurement, whether linked, overlapping or disjoint. Excluded means not selected for totals;
it never suppresses failure readback. A failure receipt leaves operation_seconds null with a
reason when the failed invocation was not timed; it does not assert zero handling cost.
Collector operation, whole invocation/integration wall time and native duration are distinct.

## Commands, reports and prices

Use cycle economics to answer a management, product or retrospective question about actual
results and comparable work. The owner's practical 5–7% tolerance guides decisions, not billing
or a guaranteed accuracy interval. Preserve exact observed facts; round only presentation.
If error magnitude is unknown, say so. A material missing role, stale selected revision,
incompatible metric or duplicate cannot be excused by this tolerance. A small difference that
could be explained by uncertainty does not justify a confident ranking. Further collection
needs a concrete decision it could change; routine reporting can be a concise estimate with
coverage. The [analysis workflow](../workflows/economics.md) and [report model](../templates/economics.md)
guide interpretation; the standalone helper produces its fixed numeric report, not that template.

Run the helper with an available Python 3 standard-library interpreter:

- collect: exact --provider, --source, --source-id, --source-version,
  --project, --task, --owner, --role, --unit, --timezone, --start,
  --revision and --out. Use --phase and --end for a bounded phase/range.
  For supported AG continuation, repeat --prior for the selected immutable facts;
  the provider guide explains its checked cumulative view and refusal boundaries.
  Use --predecessor for a raw-prefix successor, --includes-source for a known inclusive
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
  --out for rebuildable exports. Project comparisons use the selected sources.

Summary also supports `--owner` and `--unit` predicates. `--record` explicitly binds Daily roots;
without it Full status/root/phase behavior remains required. Compose cohort/event and richer
product-interest membership from cited current records before accounting when no direct selector
exists. Deduplicate the selected union. Contextual metadata is associated with the exact selected
root and returned file identity, never a cross-project bare task ID.

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
price card. A repeat with identical source bytes is stable. All current manifest
commands, including standard Economics, are selected entrypoints for the chosen
adapter; Codex/Antigravity thin routers select canonical workflows, while
Claude/Cursor commands copy them. The core transition guide classifies old
optional entries before connected writes. Daily discovery alone needs explicit
selection and its installation contract. No unrelated receiver mode is migrated.

The package requires no pip module, daemon, shared database or account
change. If no Python interpreter is available, ordinary TFW continues and
the producer uses an equivalent checked extractor or a specific failure
receipt. Real distribution into another production project follows that
project's existing init/update authority.

## Official public quote history and task-owned used basis

Standard Economics installs by default; Daily remains opt-in. Participating task-bound Full units
use this same price/source contract on their existing own-return route. Numerical v1 facts and the
legacy dated `rates.json` remain unchanged. The helper performs local validation/storage only;
agents fetch actual first-party sources with working documentation/web tools, no network service.

Actual home `~/.tfw/rates/<provider>/YYYY-MM.json` contains public quotes only. Use exact model and
conditions, never guessed aliases. Freshness is checked timestamp for that model/profile, strictly
less than 30 days; inspect prior month files too. Missing model/conditions, expiry or an explicit
today-check triggers official lookup. File mtime, another model's freshness and each token-counter
change do not. Record observed/publication/effective dates separately; unknown effective date is null.
Source failure leaves exact cause and last-known quote/date; current valuation stays qualified.

Create an observation JSON with schema_version 1; provider, model, currency, unit; a nonempty
conditions object; checked_at with UTC offset; nullable effective_from/published_on; rates keys
fresh/cached/cache_write_5m/cache_write_1h/output as nonnegative Decimal strings or null; source_urls,
source_evidence mapping fetched public URLs to SHA-256, and notes. Unit supported for USD numerical
valuation is `per_1M_text_tokens`. Provider/model/profile must be verified by the agent. An absent
positive category stays unpriced; a null unused category does not invent consumption.

Run `python .tfw/economics/tfw_economics.py quote-store --observation <actual-public-quote-file>`.
The default root is actual `Path.home()/.tfw/rates`; --cache-root is only an explicitly selected
receiving root or bounded fixture. Provider OS locks serialize read/merge/write and release on
process death. Atomic same-directory replacement leaves the last good month on failure; repeat
quote IDs are no-ops. Keep every prior observation/month, including changed same-model prices;
no global task/usage/owner data or full-provider catalogue belongs here. Ambiguous equal-time
quotes refuse selection; do not overwrite custom/malformed cache data.

Run `quote-select --provider <observed-provider> --model <exact-model> --conditions <JSON-object>
--task-root <actual-selected-task-root>`. It checks current UTC by default; --at is an explicit
observed epoch/fixture, --verify-today requires lookup even with a fresh quote. Missing/expired
returns exit 2 plus typed lookup_required reason/last_known, never silent zero. Fresh selection
creates immutable `economics/quotes/<sha256>.json` and returns its hash/quote IDs. This file is
task-owned public price evidence; native source locators/tokens remain in separate original JSONL.
For distinct models, `quote-bundle --basis <captured-file> ... --task-root <root>` freezes a bundle;
different conditions for the same model require separate named valuations, not overwrite.

Use `report` or `summary --rates <captured-basis>` to reproduce offline/on another computer.
Reports expose used basis hash, profiles, checked/source/effective dates and valuation kind.
Original cards still load without migration. Recorded basis, historical_reconstruction,
current_revaluation and last_known_source_failure are distinct. Historical reconstruction needs
evidenced effective date/consumption interval; the helper refuses unknown effective dates and
leaves rows outside the evidenced interval unpriced. Freshness itself proves no historical price.
Unknown actual request band/tier/region means conditional scenario(s), never subscription charges.

Preserve earlier report and basis bytes before creating a changed quote/report epoch. A mutable
economics.md is only a current projection backed by retained dated report/quote data. Framework
install/update does not overwrite public home cache, task bases, original usage or historical cards.
Internal collector, integration/native duration, subscription/credit invoices and product value
remain distinct. Prices are sourced API equivalents, not ROI or agent quality rankings.
