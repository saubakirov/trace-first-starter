# REVIEW — TFW-60 / Phase A: Task State & Coordination (revision 2)

> **Date**: 2026-08-27
> **Author**: saubakirov via Codex (Reviewer)
> **Verdict**: 🔄 REVISE
> **RF**: [RF Phase A](RF__phase-a__task_state_and_coordination.md)
> **TS**: [TS Phase A, revision 3](TS__phase-a__task_state_and_coordination.md)
> **Historical REVIEW**: [first pass — REJECT](REVIEW__phase-a__task_state_and_coordination.md)
> **Stage files**: `review/rev2/map.md`, `review/rev2/verify.md`, `review/rev2/judge.md`
> This is a new review revision. It does not replace or rewrite the historical REJECT.

---

## 1. Map

The corrective pass substantially repairs the rejected result: whole-name identifiers,
actor-bearing events, complete status validation, year-nested documentation resolution,
lossless 61-row migration, phase-local state, and a non-blocking derived index are all present.
The original purpose failure is closed.

The baseline-to-HEAD surface is 119 paths (76 modified, 43 added). The RF census is 47
modified plus 30 new, 77 total. During this review the owner explicitly approved the current
file-budget overrun, so the tripwire is resolved. The remaining findings are implementation,
evidence, and trace defects under the existing approved TS R3.

Detailed map: [review/rev2/map.md](review/rev2/map.md).

## 2. Verify

| # | What was checked | Result | Evidence |
|---|---|---|---|
| 1 | Full current surface and corrective delta | ❌ | All 119 baseline-to-HEAD paths covered; all 29 corrective paths directly inspected |
| 2 | Tests, validation, index behavior | ✅ command results / ❌ contract coverage | `190 passed, 1 skipped`; 53 tasks validate; targeted probes expose synthetic timestamps and provider actors |
| 3 | Adapter parity | ✅ bytes / ❌ semantics | 22 workflow copies and 11 Codex skills match their sources; broken Windows paths are faithfully copied |
| 4 | Migration and compatibility | ✅ | 61 rows, 53 directories, 8 board-only, 0 unaccounted; 11 task statuses plus one phase status |
| 5 | AC-3 journal guarantees | ❌ | Timestamp retry is composed and reverses at midnight; matching provider actor is accepted |
| 6 | AC-4 identity resolution | ❌ | Six canonical `%LOCALAPPDATA%` paths contain TAB/BS bytes; twelve adapter copies propagate them |
| 7 | Release/config consistency | ❌ | Both config files still declare the bare timestamp as `id_format` |
| 8 | Evidence sufficiency | ❌ | 46/59 verified, 5 partial, 5 contradicted, 1 deferred, 2 N/A |
| 9 | Citation cascade | ❌ partial | 34/34 resolve and exist; 31 applications relevant, 3 ONB applications irrelevant |
| 10 | Purpose and shared-write regression | ✅ | Local validation is the build gate; a stale index is visible but does not block a transition |
| 11 | File-budget authority | ✅ owner ruling | Owner explicitly approved the actual delivered overrun during this re-review |
| 12 | Unrelated working-tree state | ✅ preserved | Existing TECH_DEBT, TFW-54, and TFW-55 changes were not modified by the reviewer |

Raw verification: [review/rev2/verify.md](review/rev2/verify.md).

## 3. Judge

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD met? | ❌ | AC-3/4/10/11 remain open |
| 2 | Purpose Check + design soundness | ❌ | Purpose ✅; design soundness ❌ for actual-clock and Windows-binding behavior |
| 3 | Tech debt documented | ✅ | Existing TD-181–TD-184 cover RF observations; no duplicate added |
| 4 | Style & standards | ❌ | Control bytes, config contradiction, evidence/citation defects |
| 5 | Observations collected | ✅ | RF §6 is concrete and routed |
| 6 | RF completeness (§7–§9) | ✅ | Required sections present and substantive |
| 7 | Evidence completeness | ✅ | All 59 items and five attachments exist |
| 8 | Evidence sufficiency | ❌ | Five contradicted and five partial items |
| 9 | Backward compatibility | ✅ | Legacy corpus, paths, identifiers, and references remain readable |
| 10 | Safety | ✅ | No destructive action, secret, move, or current unrelated-file capture found |

Detailed judgment: [review/rev2/judge.md](review/rev2/judge.md).

## 4. Verdict

**🔄 REVISE**

The result now serves the approved purpose and does not require HL or TS rework. It is not
ready for approval because core AC-3/4 guarantees and AC-11's evidence-accuracy requirement
remain false in the shipped tree. These are bounded corrections suitable for the same task.

### Items to fix

1. Replace `event_filename()`'s arithmetic retry with a bounded sequence of fresh system-clock
   reads. Never synthesize a second and never reuse the old date across midnight. Replace the
   current tests with a controllable-clock test that proves each candidate came from a read.
2. Enforce that `actor` resolves to a declared `team/` handle and cannot be a provider-family
   name. Add the missing positive negative-case: matching filename/body `actor: claude` must
   be refused, not only a mismatched filename.
3. Make both config files declare the whole identifier grammar
   `YYYYMMDD-HHMMSS__slug`, or rename the field if it intentionally describes only the stamp;
   the shipped name, comments, resolver, templates, and RF must agree.
4. Replace the TAB/backspace-corrupted Windows binding location with the literal
   `%LOCALAPPDATA%\tfw\bindings.yaml` in all six canonical workflows, then re-copy both full
   adapter sets and add a control-character/path regression test.
5. Regenerate the RF/EV evidence from current commands: reconcile 280/63/343 and its
   percentiles, correct E35/E40, downgrade or attach proof for E38/E48, and correct E11/E13/
   E16/E19/E47. Remove the trailing whitespace.
6. Add a current actual-clock handoff/transition for the corrective RF. Preserve the old
   43/44 first-pass event as history; do not rewrite it. The current trace must identify the
   59-item RF that was actually handed to review.
7. Preserve the old ONB, but add a new revision/addendum whose citation applications for rows
   1, 2, and 12 actually follow the cited resumability, task-locality, and D37 clauses.

After these bounded corrections, run `/tfw-review TFW-60 phase-a` again. The owner has already
approved the file-count overrun; do not return for another budget ruling unless the count or
scope moves again.

## 5. Tech Debt Collected

| # | Source | Severity | Disposition |
|---|---|---|---|
| 1 | RF §6 observations 1–3 | Med | Existing TD-181; no duplicate and no knowledge update before approval |
| 2 | RF §6 observation 5 | High | Existing TD-182 |
| 3 | RF §6 observation 6 | High | Existing TD-183 |
| 4 | RF §6 observations 7–9 | Med | Existing TD-184 |
| 5 | Review F-R2-1–F-R2-7 | Task defects | Return to execution; do not convert incomplete acceptance work into backlog debt |

No new TECH_DEBT row was added. The existing dirty `TECH_DEBT.md` was preserved exactly.

## 6. Traces Updated

- [x] New review revision and `review/rev2/` stage files created; historical REJECT untouched.
- [x] Phase-local `status.md` routed `RF → REV` for the REVISE verdict.
- [x] New actor-bearing transition event written from an actual clock read.
- [x] Task root remains `PHASES`; it does not summarize Phase A.
- [x] Derived index deliberately not rewritten by a task transition; staleness is allowed and visible.
- [x] Other project files and unrelated dirty changes preserved.
- [x] tfw-docs: **N/A — REVISE; no rejected/unapproved result is consolidated.**
- [x] tfw-knowledge: **N/A — REVISE; Fact Candidates remain unpromoted.**

## 7. Fact Candidates

No new Fact Candidates. The owner's budget approval is recorded as task authority in §§1–4;
the other findings are reproducible implementation facts.

---

*REVIEW — TFW-60 / Phase A: Task State & Coordination | revision 2 | 2026-08-27*
