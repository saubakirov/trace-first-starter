# Gather — "What do we NOT know?"
> **Mindset:** Explorer. Map the uncertainty before choosing a route.
> **Test:** Can we name each decision factor and its alternatives from the inspected sources?
> Parent: [HL-ECON](../../HL-TFW_20261001-001035_ECON.md)
> Goal: Connect measured AI resources to useful product results while preserving Daily authority and Full accounting.
> Producer: `codex:thread:local:01a0f3df-52c7-7890-abdb-c4e6240540b3`; parent `codex:thread:local:01a0ec08-7c1d-7570-9ec2-e3e00275687e`.
> Activation: original native command-first dispatch at `9453421f99006dcb66757615d6305c25cd9f04db`; approved Briefing `ff33d17fdb7c4d45245077f9be0730922578398f`; continuation answer `journal/20261001-010830__gate_answer__eaef.md @ 6817be617c7b4ba3e47c19fb23968ba9f126fc97`, transferred as identical journal bytes in `17029758`.
> Authority: `HL-TFW_20261001-001035_ECON.md @ de943efbc77914243112a89ab6e97b14ea52bfc1` §4.1; status lifecycle RES, selection baseline, native-gates, tfw-gates-only, no phase. Originating proposer: `{principal: owner:saubakirov, unit: owner-direct native discussion}`; no agent principal selected.

## Dimensions

Alternatives describe the space to compare in Extract, not approved implementations. An incompatible alternative remains a falsifying control; none is recommended at Gather.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1 — Work-record identity and authority | Explicit Daily record resolver preserving its actual form | Explicit checked binding of a selected record and returned files, bypassing Full-root entry paths | Convert/synthesize Full status to satisfy current helper, as a falsifying control | Wider unified work-state model, considered only if narrow routes fail |
| D2 — Declared attribution and unavailable identity | Validate actual known human/unit/source before numeric capture | Keep unresolved attribution and a nonmeasured failure/gap in the existing Daily record, resolve before numeric capture | Extend a separately versioned receipt/manifest to encode unavailable identity | Invent an owner/unit sentinel as a falsifying control |
| D3 — Numeric schema versus contextual metadata | Preserve version 1 numbers; read purpose/classification from the selected record/report | Use permitted namespaced extensions for additional provenance without changing core fields | Introduce a separately versioned format and documented migration | Add undeclared core fields or reinterpret existing fields, as a falsifying control |
| D4 — Time selection | Dated consumption within the requested period | Explicit task-event cohort with all received lifetime usage, including undated rows | Explicit lifetime selection without a date predicate | Treat cutoff/update as consumption or completion, as a falsifying control |
| D5 — Product-interest selection and additive accounting | Existing primary area and flat local keywords | Source-grounded derived domain/area/feature/scenario/context labels in report context, selecting a unique task set | Analyst selects associated tasks from inspected result sources with disclosed classification gaps | Allocate feature costs or add overlapping tag totals without attributed numbers, as a falsifying control |

## Findings

### G1 — Daily already has its own valid identity and authority; numeric collection and Full entry paths are separate

At unchanged product-source epoch `89292e7ac6c366278f6f3107ccc5946f1e73d30e`, `.tfw/extensions/daily-task/SKILL.md` §§1–4 requires actual request/worker attribution, an immutable whole Daily folder ID, existing receiving forms, purpose/boundary checks and truthful result/acceptance. It explicitly creates no Full status, HL, TS, RF or REVIEW. The canonical `templates/task.md` preserves five selected-Trace sections and can link evidence without a formal lifecycle.

The economics helper's `collect` (lines 760–809) accepts explicit identity/source arguments and does not read `status.md`. `validate_manifest` (161–208) accepts regex-conforming `task` and `role` strings; there is no Full-task grammar or Full-role enum there. A conventional Daily folder ID fits that grammar, and a explicitly declared Daily worker role is structurally representable. **This is source-level representability, not semantic authorization or an executed Daily capture.**

Conversely, `receive` (828–850) requires a status file with the matching ID; `status_fields` (1079–1089), `render_report` (1100–1112), `check_task_sources` (882–892) and `render_summary` (1253 onward) depend on Full status. A synthetic `status.md` would evade those mechanics while contradicting Daily's authority and the approved HL. The exact adaptation boundary appears at selected-record binding/receipt/reporting, not automatically in native token readers.

### G2 — Unknown optional metrics are representable; unknown required identity is a distinct unresolved case

`record.schema.json` manifest and helper validation require non-null project/task/owner/role/unit/source namespace/source ID/source version. `collect` and `failure_receipt` (812–825) both enforce those identities; a failure row still travels after that same required manifest. Neither `unavailableManifest` nor helper `manifest.unavailable` permits an owner/unit/source-ID reason. Namespaced extensions cannot override these core constraints.

Usage supports null model, effort, observed time, consumption date and selected token/duration fields with precise reasons; input/output/total remain required for measured usage. Thus a known Daily producer with missing optional usage dimensions and a Daily whose actual owner/unit/source cannot be established are different cases. Missing attribution must not be encoded as an invented handle or silently inferred from the OS. A nonmeasured gap in the existing Daily record is one candidate route; whether it meets the complete ECON failure-return promise is a decision-changing question for Extract/Challenge. No unavailable-identity JSONL is claimed valid.

External cross-check: [JSON Schema null reference](https://json-schema.org/understanding-json-schema/reference/null) distinguishes null from absence. [Object reference, Additional Properties / Extending Closed Schemas](https://json-schema.org/understanding-json-schema/reference/object) explains why undeclared properties cannot simply be inserted into a closed object. These are schema semantics, not proof of application behavior. They support checking both the published schema and the helper's stricter arithmetic/cross-row rules.

### G3 — Consumption periods are implemented; task-event cohorts are not the same operation

Helper `summarize` (1018–1077) uses `consumption_date` for inclusive date bounds; null dates are excluded from a period and retained in unfiltered lifetime totals as `undated_tokens`. `date_at` (99–103) converts an actual offset-bearing source timestamp into the bound explicit timezone; `validate_row` (235–240) checks date/offset agreement. `captured_at` and cutoff are collection boundaries, not replacement consumption timestamps.

The CLI (1368–1426) exposes date/project/task/role/model/tag filters but no cohort-event, owner or unit selector. Owner/unit exist in records, so their absent CLI filters do not alone imply a numeric schema redesign. Cohort selection would first need a cited created/completed/other chosen task event from Full or Daily sources, then lifetime accounting without a consumption-date predicate. The helper's completed-task comparison (1335–1355) admits only Full lifecycle DONE roots already represented in selected spending; a DONE task with entirely undated usage can disappear under consumption date filtering. This is not a demonstrated created/completed-date cohort implementation.

[Python datetime, Aware and naive objects](https://docs.python.org/3/library/datetime.html#aware-and-naive-objects) confirms that timezone information is needed to locate a timestamp unambiguously. A Daily folder's local stamp supplies identity; without an evidenced clock offset/event meaning it cannot independently prove consumption or acceptance time. Unknown dates and ambiguous query meaning must remain visible.

### G4 — Product labels are currently report context; numeric spend identity is independent

Helper report metadata (1146–1167) stores one primary area and 3–5 distinct local keywords, subject to report argument checks (1113–1121). `render_summary` (1277–1288) accepts one tag matching that area or keyword list. It has no built-in typed domain/feature/scenario/context classification, source references for derived classifications, multiple-tag Boolean predicate or feature allocation.

The numeric manifest has no product field; existing report metadata can describe classification without rewriting resource rows. For overlapping interests, the relevant spending subject is the unique set of associated tasks/returned contributions, not the sum of separate tag totals. A feature name in a task's context establishes association, not the feature's standalone cost. Missing report metadata means the current tag filter excludes the root; that omission must be disclosed in an analytical report rather than interpreted as no associated work.

### G5 — Existing deduplication is reusable but must be applied at the correct selection boundary

`reconcile` (895–987) deduplicates identical bytes, uses native namespace/source identity for range conflicts, requires verified predecessor/prefix rules for covered replacement, excludes an inclusive parent while its named child is present, and deduplicates native event IDs. `task_sources` selects root role bytes and immediate matching phase leaves; `render_summary` eliminates repeated root paths and a phase explicitly selected with its parent. No parent report total is added to leaf numbers.

The union of selected product interests should enter this accounting once. Separate summaries subsequently added by an analyst do not inherit automatic cross-summary deduplication. Multiple selected roots are reconciled separately in `render_summary`, so Extract/Challenge must examine the correct union boundary rather than assume all arbitrary repeated sources are globally reconciled. Range/completeness successor conditions are observed dependencies only here; their live behavior belongs to H2.

## OODA — one focused pass

- **Observe:** inspected five current product sources: Daily skill, Daily form, economics README, helper, published schema; unchanged against the named control epoch. Used three primary external reference pages on schema/null/date semantics. No foreign runtime source or historical task corpus was read.
- **Orient:** ordinary Daily numeric identity may fit version 1, while selected-root/report authority remains Full-specific. Unknown required identity and task-cohort selection are independent from missing optional usage fields and ordinary period filters.
- **Decide:** close Gather as a boundary/dimension map. Compare narrow routes with these actual failure cases in Extract; do not declare H1 true from structural representability or choose an implementation here.
- **Act:** preserve this stage and return its normal gate. No code/schema/permanent test was written; no Daily capture or modified helper was run.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Explicit numeric collector is not intrinsically Full-status-dependent; receive/report/summary are. | Smallest valid Daily binding/receipt/report route and observed counterexamples. |
| Required identity cannot be null even for the current failure receipt. | Whether record-local nonmeasurement preserves the frozen failure-return contract, or an explicitly versioned extension is necessary. |
| Dated consumption and lifetime accounting already differ correctly. | Actual cohort-event evidence/selection and absent owner/unit filtering. |
| Report labels and spending identity are separate; tag metadata gaps and overlapping selections matter. | Minimal provenance-bearing product selection and union/reconciliation behavior. |
| Existing Full root/phase and source deduplication boundaries are identifiable. | Bounded ordinary Full/phase, unknown attribution and date/tag counterexamples in Challenge; H2 later. |

**Sufficiency:**
- [x] External source used: the three primary pages above, accessed 2026-10-01.
- [x] Briefing gap closed for Gather: actual boundaries and discriminating unknowns mapped; compatibility verdict remains later work.
- [x] Five dimensions identified, each with at least three alternatives; no alternative selected as recommended.

## Material handover and currentness

Producer/parent/authority are recorded above. Product source epoch is `89292e7ac6c366278f6f3107ccc5946f1e73d30e`; `git diff` against those five paths found no intervening change. TEQM qualified source `knowledge/records/TKL-20260929-TEQM.md` retains its accepted specification/independent-Candidate scope and portability limits; the incoming relation lookup found no TEQM successor/conflict. Its surviving D82/D86 constraints remain applicable. Knowledge handover/current-use conventions were applied at this return. No publication or revised authority is inferred.

Material result: G1–G5 are source-backed engineering observations; the required-identity failure case and absence of cohort selection are the principal new uncertainties. H1 is still open. No broader redesign has been proven necessary. The existing Briefing and qualified economics record remain reusable sources. Own economics binding is unchanged in `research/entry.md`; final RES will include the validated finite contribution or typed failure.

Stage complete: YES
→ User decision: **WAIT — Gather gate.** Recommend close Gather and authorize Extract over these five dimensions; name any material missing boundary before advancement. No owner-reserved decision is requested at this stage.
