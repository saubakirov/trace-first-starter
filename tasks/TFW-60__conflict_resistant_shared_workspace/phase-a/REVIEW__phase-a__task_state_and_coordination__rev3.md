# REVIEW — TFW-60 / Phase A: Task State & Coordination (revision 3)

> **Date**: 2026-08-27
> **Author**: saubakirov via Codex (Reviewer)
> **Verdict**: 🔄 REVISE
> **RF**: [RF Phase A, revision 2](RF__phase-a__task_state_and_coordination.md)
> **TS**: [TS Phase A, revision 4](TS__phase-a__task_state_and_coordination.md)
> **Historical reviews**: [revision 2 — REVISE](REVIEW__phase-a__task_state_and_coordination__rev2.md) · [first pass — REJECT](REVIEW__phase-a__task_state_and_coordination.md)
> **Stage files**: `review/rev3/map.md`, `review/rev3/verify.md`, `review/rev3/judge.md`
> This is a new review revision. It does not replace or rewrite either historical verdict.

---

## 1. Map

The second corrective pass materially fixes review revision 2's clock arithmetic, provider
actor, config grammar, Windows-path, and missing-handoff findings. The core Phase A result —
task-local authority and journals, a non-blocking derived index, lossless migration, phase
state, and TFW 2.0.0 release surface — remains purpose-aligned.

All 30 paths in the new executor iteration were inspected. Together with revision 2's complete
119-path audit, this covers the current implementation; the intervening TFW-58 proposal is a
separately attributed coordinator change. The owner formally approved the unchanged delivered
budget of 47 modified plus 30 new product files, 77 total.

Detailed map: [review/rev3/map.md](review/rev3/map.md).

## 2. Verify

| # | What was checked | Result | Evidence |
|---|---|---|---|
| 1 | Second corrective delta | ✅ coverage / ❌ result | 30/30 paths inspected; three material discrepancy classes remain |
| 2 | Full tests and state gates | ✅ | `206 passed, 1 skipped`; 53 tasks validate; index current before transition |
| 3 | Adapter parity | ✅ | 22 workflow copies and 11 Codex skills match their sources byte-for-byte |
| 4 | Clock, provider, config, Windows path, handoff | ✅ core fixes | Every requested edit exists and its direct regression test passes |
| 5 | Declared actor and human accountability | ❌ | Empty `team/` disables production membership validation; profile type is discarded, so agent accountability passes |
| 6 | Full identifier and event grammar across release surface | ❌ | Config/tests use the whole ID; canonical init/artifact/event examples still teach superseded semantics |
| 7 | Migration and task-locality | ✅ | 61 IDs accounted, zero unaccounted; stale index does not block local state |
| 8 | Evidence completeness | ✅ | All 59 numbered rows and seven attachments exist |
| 9 | Evidence sufficiency | ❌ | 50 verified, 4 partial, 2 contradicted, 1 deferred, 2 N/A; final artifacts mix incompatible snapshots |
| 10 | Citation cascade | ⚠️ disclosed history | 34/34 references resolve and exist; 31 applications relevant, 3 old ONB applications irrelevant and explicitly recorded under R4 |
| 11 | File-budget authority | ✅ owner ruling | The owner formally approved the delivered 77-file product count; no further scope/count movement found |
| 12 | Git safety and unrelated work | ✅ | Corrective commits are scoped; current TECH_DEBT and TFW-54/55 work remains untouched |

Raw verification: [review/rev3/verify.md](review/rev3/verify.md).

## 3. Judge

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD met? | ❌ | AC-2/3/4/10/13 remain open through verify F-R3-1–F-R3-3 |
| 2 | Purpose Check + design soundness | ❌ | Purpose ✅; design soundness ❌ for fail-open identity and contradictory canonical naming |
| 3 | Tech debt documented | ✅ | Existing TD-181–TD-184 cover surviving RF observations; current findings are task defects |
| 4 | Style & standards | ❌ | `{ID}` has two meanings, old event grammar remains, and final evidence contradicts itself |
| 5 | Observations collected | ✅ | RF §6 is concrete and routed |
| 6 | RF completeness (§7–9) | ✅ | Required sections are present and substantive |
| 7 | Evidence completeness | ✅ | All rows and attachments exist with explicit statuses |
| 8 | Evidence sufficiency | ❌ | Two evidence rows are contradicted and four are partial; RF-level counts also disagree |
| 9 | Backward compatibility | ❌ | Legacy corpus passes, but shipped init/templates can generate names the current contract rejects |
| 10 | Safety | ✅ | No destructive action, secret, task move, or unrelated capture found |

Detailed judgment: [review/rev3/judge.md](review/rev3/judge.md).

## 4. Verdict

**🔄 REVISE**

The original purpose failure remains closed, and the second pass fixed most of the previous
review. Approval is still premature because the shipped validator does not actually guarantee
declared human accountability, canonical instructions disagree with the whole-ID and
actor-bearing contracts, and the evidence package again fails its own final-measurement rule.
All three are bounded corrections under the approved TS R4; no HL amendment or new budget
ruling is needed unless the product surface moves beyond the already approved 77 files.

### Items to fix

1. Make participant validation fail closed and type-aware. Parse actual `team/` profiles,
   reject missing/empty/malformed profile sets for new events, require `actor` to name a
   declared handle, and require `on_behalf_of` to name a declared **human** handle. Exercise
   the production `collect`/`--validate` path in tests, not only direct calls with an injected
   non-empty set.
2. Complete the canonical naming sweep. Make `{ID}` mean the whole
   `YYYYMMDD-HHMMSS__slug` identifier in `init.md`, artifact formats, and every template;
   remove the second appended title where the full ID already carries it; replace actorless
   journal examples; propagate affected copies; add a regression test that rejects bare-ID,
   doubled-slug, and actorless current examples on the shipped canonical surface.
3. Rebuild RF/EV evidence once from a pinned final snapshot with reproducible commands and
   one declared population. At minimum reconcile E16 and E35, the EV's revision-3 header and
   old `190 passed` block, 116 versus the actual 921-file scan, 292 versus the recorded
   294/current 295 subject population, E48's missing final commit, and the measurement log's
   `HEAD=86bc963` claim versus its later handoff content. Avoid unpinned “baseline-to-HEAD”
   counts that invalidate themselves when the RF commit lands.

The approved TS R4 disposition of the three old ONB citation applications is accepted as an
explicit historical correction route: preserve the ONB and keep RF observation 12. No ONB
rewrite is requested by this review.

## 5. Tech Debt Collected

| # | Source | Severity | Disposition |
|---|---|---|---|
| 1 | RF §6 observations 1–3 | Med | Existing TD-181; no duplicate and no consolidation before approval |
| 2 | RF §6 observation 5 | High | Existing TD-182 |
| 3 | RF §6 observation 6 | High | Existing TD-183 |
| 4 | RF §6 observations 7–9 | Med | Existing TD-184 |
| 5 | Review F-R3-1–F-R3-3 | Task defects | Return to execution; do not convert incomplete acceptance work into backlog debt |

No TECH_DEBT row was added. The existing dirty file was preserved exactly.

## 6. Traces Updated

- [x] New `rev3` stage files and REVIEW revision created; both older verdicts remain unchanged.
- [x] Phase-local `status.md` routed `RF → REV` for the REVISE verdict.
- [x] New actor-bearing transition event written from the actual clock.
- [x] Task root remains `PHASES`; it does not summarize Phase A.
- [x] Derived index deliberately not rewritten by the transition; staleness is allowed and visible.
- [x] Other project files and unrelated dirty changes preserved.
- [x] tfw-docs: **N/A — REVISE; no unapproved result is consolidated.**
- [x] tfw-knowledge: **N/A — REVISE; Fact Candidates remain unpromoted.**

## 7. Fact Candidates

> fact-candidates: processed 2026-08-30

No new Fact Candidates. The formal budget approval is a task-specific authority decision,
and the remaining findings are reproducible implementation/evidence facts.

---

*REVIEW — TFW-60 / Phase A: Task State & Coordination | revision 3 | 2026-08-27*
