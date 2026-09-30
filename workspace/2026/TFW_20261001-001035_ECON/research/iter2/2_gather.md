# Gather — H2 bounds, revision arbitration and measured cost

> **Mindset:** Explorer. Map unknowns before narrowing; every assumption is a question.
> Parent: [HL-TFW_20261001-001035_ECON](../../HL-TFW_20261001-001035_ECON.md)
> Goal: Ground product economics in observed evidence and routine cumulative Daily capture before every orderly turn return.

Producer: `codex:thread:local:01a0f3df-52c7-7890-abdb-c4e6240540b3`; parent/return route: `codex:thread:local:01a0ec08-7c1d-7570-9ec2-e3e00275687e`. Same delegated activation and coordination authority: `HL-TFW_20261001-001035_ECON.md @ de943efbc77914243112a89ab6e97b14ea52bfc1`, section 4.1; originating proposer owner saubakirov. Effective status remains RES, `baseline`, `native-gates`, `tfw-gates-only`; `WORK=RESEARCH`, no phase. Iteration 2 remains the first pending entry; H2 is open. Focused mode, one OODA loop, gpt-6.1-sol/high are retained.

Gather activation: approved [Briefing](1_briefing.md) at `187cbe47016a77bc253863d5bfd10b601381ea9e` and exact `journal/20261001-022828__gate_answer__0e75.md @ 69718ca193f355d002e051470a643ec365b9088f`. The latter was transferred unchanged at `fa5ca7cef082ed0b3a1f5f660fac76a980041b99`; exact-path comparison returned no differences. This answer authorizes Gather, not Extract or an H2 verdict.

Own-source resume binding: same exact locator in [initial entry](../entry.md), `codex.rollout`, source/session metadata ID `01a0f3df-52c7-7890-abdb-c4e6240540b3`, native version `0.159.2`, timezone `+05:00`, matching the native environment ID. Retain cumulative H2 start 411. This Gather continuation is evidenced by zero-based `task_started` line 559 at `2026-09-30T21:28:55.145Z`, turn `01a0f438-722a-7020-9543-a27652c5d832`. H1 `[0,377)` remains accepted; `[377,411)` remains explicitly unknown coverage. Only own metadata, numeric counters and event boundary/time fields were inspected; no foreign source or message content was output.

## Dimensions

Alternatives are mapped, not recommended. Existing authority/source constraints still apply; an alternative's current limitation is reported in Findings.

| Dimension | Alt A | Alt B | Alt C |
|---|---|---|---|
| D1: Coverage claim | Finite observed prefix with an open turn | Fully inspected closed selected range | Whole task/work lifetime completeness |
| D2: Revision sequence | Covering cumulative successor marked complete | Covering live cumulative successor marked incomplete | Proven disjoint increment with a separate bound |
| D3: Continuity proof | Exact predecessor bytes and matching recomputed native prefix | Predecessor bytes present but native prefix changed | Missing predecessor or prefix proof |
| D4: Failure accounting | Linked v1 capture-failure receipt from a known binding | Unlinked v1 failure receipt over the attempted range | Existing-record typed unavailable-binding outcome with last-good reference |
| D5: Cost surface | Collector's internal timed operation | Host invocation, output validation/write and receiver/reconciliation path | Observed native token/time interval for collection-related work |

D1 describes completeness evidence, D2 how revisions combine, D3 what proves continuity, D4 how nonmeasurement enters the receiving route, and D5 which cost is actually observed. Full task completeness cannot be inferred from a finite range, and a record-local unknown-binding outcome cannot be treated as a v1 numeric file.

## Findings

### G1 — Completeness is a producer declaration; range and lifetime differ

Source inspection at the unchanged helper SHA-256 `6421da79a5cb7e7aca5f2061ca648e04a1147aeec00120c4a9870baacad53328`, product source commit `0cd723a203611871e3c49a174aeb3e7220fda40c`:

- `parser` line 1383 accepts `--complete`; `manifest` lines 737–757 copies it to `complete`; `validate_manifest` line 189 checks only that it is a boolean. There is no independent complete-turn, complete-task or all-source-lifetime gate attached to that flag.
- `source_lines` lines 317–323 reads the selected file and drops a final unterminated JSONL suffix. For line readers, `collect` lines 784–803 validates the requested end against available complete lines and hashes a normalized byte prefix from line 0 through the exclusive end. The hash is not restricted to `range_start`; earlier lines establish identity/context/counters.
- `codex_rows` lines 325–485 checks observed numeric stream consistency, range membership, source metadata and matched duration events. Open/aborted turns retain observed tokens and unavailable completed-turn duration. Its unmatched-turn diagnostic is not a rejection of `complete=true`.
- `manifest.cutoff` is the collection clock, not the last consumption event time or a task completion event. The consumption date comes from supported native row timestamps with an explicit timezone. The finite-tail contract in economics README lines 169–175 remains applicable.

These observations expose a decision-changing semantic gap: a range can have all its selected bytes inspected while the producer's later work is still absent. A validated complete declaration is not proof of whole-task coverage. Extract/Challenge must establish which bounded claim is honest and compatible with replacing a live cumulative contribution. No false or true H2 verdict follows yet.

Permitted own-source boundary evidence is already available for later probes: `task_complete` at line 489, `2026-09-30T21:06:43.648Z`, turn `01a0f41e-b590-7703-9ddf-68740df552a5`, duration 355202 ms; and at line 557, `2026-09-30T21:22:43.734Z`, turn `01a0f42f-0339-7402-81af-703479e4d514`, duration 246834 ms. Thus exclusive ends **490** and **558**, both beginning at 411, are two concrete closed-turn candidates for the approved twenty timing captures. These are observed boundary fields, not a collector result, final Daily proof or whole-task duration.

### G2 — One-time replacement has explicit structural conditions

`collect` lines 769–803 validates predecessor bytes, checks source namespace/ID/unit, recomputes the predecessor prefix when the new start covers it, and refuses changed bytes before writing the new contribution. `reconcile` lines 895–987 separately operates on returned bytes; it has no access to the producer's native file.

| Situation | Current source branch | Unresolved evidence for Challenge |
|---|---|---|
| Identical returned bytes at multiple paths | Content hash deduplicates the file before grouping. | Repeat native receipt and verify no duplicate contribution. |
| Complete covering successor | Predecessor must exist; namespace/ID/unit/project/task/phase must match; revision must increase; range must cover; returned prefix proof must equal predecessor source hash. Prior file is excluded from consumption. | Verify actual native prefix plus exactly one accepted cumulative total, including a revision chain. |
| Incomplete overlapping successor | New file is excluded as `unproved successor overlap`; prior bytes are not deliberately replaced. | Verify that newer observations do not silently disappear behind a stale total and that the exclusion is visible. |
| Disjoint bounds | Nonoverlapping contributions remain eligible; source/event uniqueness supplies the accounting denominator. | Verify additive increments and reconcile them with an explicitly cumulative view without weakening the required snapshots. |
| Unlinked overlap | Remaining overlapping eligible files are both excluded, with a conflicting-range diagnostic. | Verify omission versus failure/zero and any impact of an overlapping failure receipt. |
| Missing predecessor, mismatched identity/revision or absent/wrong prefix proof | Successor is excluded with a specific diagnostic. | Verify last-good retention and whether a later revision can conceal an unresolved chain problem. |

Grouping is by native namespace/ID; successor identity additionally includes the work/project/phase and unit. Spend identity must remain native. Product classification metadata is a separate H1 delivery obligation. A receiver's valid content hash proves receipt of those bytes, not the truth of a declared completeness flag or prefix assertion supplied by an unchecked writer.

### G3 — Failure files participate in range arbitration before row kind

`write_jsonl` lines 119–127 refuses overwrite, and `receive` lines 828–850 copies exact bytes under their hash, preserving all received revisions. `failure_receipt` lines 812–825 requires a known v1 binding and attempted nonempty range; it produces a manifest plus one failure row, no measured usage. This is not the H1 record-local unavailable-binding format.

However, `reconcile` arbitrates all manifests before it examines whether their rows are failures. Failure-row handling appears only at lines 970–973 for files still active. Source-backed risks to challenge are:

- An unlinked overlapping failure file may participate in the conflict that excludes the last successful contribution. Preservation of its bytes alone would not prove that usable last-good consumption remains in the report.
- A linked incomplete overlapping failure file may be excluded before its row's exact code is converted into a capture-failure diagnostic. The report lists file hashes and generic source diagnostics, but its source-diagnostic block and provenance loop do not explicitly extract failure-row `detail` from every excluded file (report lines 1135–1170, 1230–1244).
- `failure_only` is a unit-level received-minus-reported set. A unit with a previous usage file and a later failure can therefore be neither missing nor failure-only while still having a failed latest attempt. Last-good, latest attempt, measurement and omission need distinct readback.

These are static branch observations and candidate failure modes, not reproduced outcomes. Extract should prepare exact oracles; Challenge should exercise both linked and unlinked failed attempts and verify resolvable last-good bytes plus visible cause. The final receiving route must retain H1's unknown-binding truthfulness instead of fabricating the core v1 identity.

### G4 — Collector timing stops before file output and final validation

The helper starts `time.monotonic()` at line 765, after initial binding argument checks; elapsed time is passed into `manifest` at line 804. `write_jsonl` and `validate_file` happen later at lines 806–807. Thus `operation_seconds` covers source read/decode, predecessor validation/prefix hashing and compaction; it omits output serialization/write, final validation, interpreter startup, CLI parsing, receiver/report invocation and agent work.

`source_lines` reads the whole physical file before the requested end is applied. A fixed logical bound may still incur reads of later physically present bytes. Each future sample must record both the selected prefix size/end and actual source-file size. Prefix size, native row count and compact output size answer different questions; compaction does not eliminate decode work. `compact_rows` lines 687–734 groups verified events into date/model/effort token and separate duration buckets.

`render_report` line 1135 sums operation values across the distinct returned files, including superseded/excluded attempts. This is separate from reconciled consumption. The failure writer supplies a literal operation value 0 at line 820 without timing its actual invocation; that value must not be reported as evidence that failure handling cost no time. Raw benchmark outputs belong to explicit research probe evidence, not twenty unlinked authoritative contributions that introduce overlapping ranges.

The approved plan fixes ten captures for each of the two available bound candidates, all raw samples and median/range, with initial/subsequent invocation distinguished. Observable host wall time will separately include invocation, validation and the selected reconciliation path. No timing has been measured in Gather. No causal whole-agent overhead, arbitrary “modest” threshold, disk-cache condition or unobserved cross-host claim is justified.

### G5 — Daily workflow acceptance remains a delivery effect

The current Daily canonical skill and record template, source skill commit `d20c79451526b3ef03256b94fb1285f01ecafb76`, preserve actual request/authority, pre-action context, bounded result/check and next authority; they contain no per-turn/final economics obligation. Daily grants no formal Full role authority and directs formal work to the existing Coordinator route.

This Researcher's genuine native source can test collector mechanisms and boundary evidence. It cannot establish that a delivered Daily entry binds a real Daily request, updates before every orderly return and leaves its final selected-record summary. Existing-form binding, typed-gap reporter visibility and cross-project enrichment remain the accepted H1 delivery requirements. No new Daily record, Full status, product change, second role or acceptance is created here.

### External method check

Primary sources accessed 2026-10-01:

- [Python 3.13 time documentation](https://docs.python.org/3.13/library/time.html#time.perf_counter): monotonic/performance-counter differences measure elapsed intervals; process CPU time is a different quantity. This supports separating internal and host wall timing, not a native agent-time inference.
- [Python 3.13 hashlib documentation](https://docs.python.org/3.13/library/hashlib.html#hash-objects): SHA-256 digests are determined by supplied bytes, and incremental updates are equivalent to concatenation. A prefix match must compare the same byte sequence; it does not establish source ownership or completeness.

The helper's normalized complete-line byte sequence is the exact current comparison object. Native source stability, correct bound ownership and honest complete declarations remain separate grounds to test.

## OODA — one focused loop

**Observe:** read the approved gate/Briefing, current routing/control, selected collector/validation/receipt/reconciliation/report branches, economics contract, Daily skill/form, knowledge scope and primary time/hash documentation; inspect own numeric boundary metadata only.

**Orient:** map five independent dimensions against H2 and the accepted H1 boundaries. Separate declared range completeness from whole task completion, numeric receipt from failed-attempt readback, collector operation from end-to-end integration.

**Decide:** the Gather mapping is sufficient to compare configurations in Extract. Completeness declaration and failure-range arbitration are material falsification targets; neither is resolved by existing v1 validity. Stay focused; no broader role, product mutation, permanent tests or weaker every-turn obligation.

**Act:** preserve G1–G5 and the concrete bound candidates in this stage file, then return its gate. Extract is not activated by this return.

## Checkpoint

| Found | Remaining |
|---|---|
| Five independent dimensions and current replacement/arbitration rules | Select configurations and falsifiable expected totals in Extract. |
| Complete is an unchecked producer declaration at validation; closed own-turn ends 490/558 are available | Prove honest bounded completeness and native cumulative replacement in Challenge; preserve whole-task tail. |
| Failure manifests enter overlap arbitration before row handling | Reproduce or falsify last-good exclusion and failure-cause visibility risks. |
| Internal timing boundary excludes output/validation/startup; whole-file reads can exceed selected prefix | Measure the fixed twenty captures and separately observed integration path. |
| Current Daily surfaces do not implement the obligation | Keep genuine every-turn Daily/final-summary delivery acceptance explicitly owed. |

**Sufficiency:**
- [x] External source used: primary Python time/hashlib documentation, bounded methodological claims only.
- [x] Briefing gap closed for Gather: unknowns, current branches, evidence surfaces and candidate bounds are mapped; the hypothesis is still open.
- [x] Dimensions identified: five factors, at least three alternatives each, no strategy recommended before Challenge.

Material handover: same Researcher, scoped current source at the named epochs/hash; static observations and own event boundaries are distinguished from probe results. Knowledge-use/handover rules were reapplied; `TKL-20260929-TEQM` applicability/grounds/disposition/source/producer and incoming exact-identity references were inspected, with no incoming successor/conflict found. Its scoped Full/observed-recipe claims and surviving D82/D86 boundaries remain applicable. No new human Fact Candidate or publication is owed by this stage. H2, final Daily proof, TS/denominator and owner result reservations remain open.

Stage complete: **YES**.
Recommendation: accept this bounded Gather map and continue focused Extract through the same Coordinator's immutable gate answer.
Status: **WAIT — Gather gate**.
