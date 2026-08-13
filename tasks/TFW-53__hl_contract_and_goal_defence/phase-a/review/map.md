# Map — "What was done?"

> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF__phase-a__contract_in_artifacts.md](../RF__phase-a__contract_in_artifacts.md)
> TS: [TS__phase-a__contract_in_artifacts.md](../TS__phase-a__contract_in_artifacts.md)
> Mode: spec

## Understanding

Phase A turns the HL contract from an idea in `HL-TFW-53` into artifact state, across exactly three
framework files and no new ones. `.tfw/templates/HL.md` gains a five-field contract header block, a
three-state marker on every section heading (`🔒 FROZEN` / `🟢 FREE` / `🟢 APPEND-ONLY`) with a
subsection-inheritance rule, a `§12 Amendment Log` carrying a 10-column grammar with `Type` and
`Verdict` vocabularies, and a four-property gate clause appended to §3.1. `.tfw/templates/RES.md`
splits `HL Update Recommendations` into `Refinements` (free sections) and `Amendment Proposals`
(frozen sections) and loses line 32's `Coordinator applies these`. `.tfw/conventions.md` gains the
governing definition: a `#### HL Contract` subsection with 21 numbered rules in four groups, a §5
REJECT-branch-(a) redefinition, and seven §14 anti-patterns.

Two decisions go beyond the TS letter, both recorded in RF §2: adding `🚫 WITHDRAWN` to the §12
verdict vocabulary (found by diffing the shipped grammar against HL-TFW-53's own 12 live rows, where
A11 is a withdrawal the four-value draft could not name), and time-scoping the rule-6 tripwire to
"§5 and §6 *as they stand at the moment of classification*" (surfaced by the AC-8 exercise, where row
A1 classifies one way against the 2026-08-08 contract and the other way against today's).

Nothing in this phase executes. `plan.md`, `review.md` and `research/base.md` still carry the old
instructions — Phase B is what makes them obey. TS §2 declares that intermediate state as expected.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — HL declares its own contract state (header field, three states, §12 pointer, inline markers) | RF §3 AC-1 ✅, 5/5 bullets, section lists cross-checked against HL §3 | ✅ |
| AC-2 — §12 with enforceable column grammar (10 cols, Type enum, RESTRICT rule, `PROPOSED`, explicit-N/A, instruction text) | RF §3 AC-2 ✅, 7/7 bullets; grammar diffed against 12 live rows → EV §E2 | ✅ |
| AC-3 — RES classifies instead of instructing (two tables, § column, evidence/cost/alternatives, line 32 deleted) | RF §3 AC-3 ✅, 5/5; gate `grep "Coordinator applies these"` → 0 | ✅ |
| AC-4 — `conventions.md` defines the HL Contract; split matches template and HL §3 | RF §3 AC-4 ✅, 3/3 | ✅ |
| AC-5 — an amendment verdict is a distinct recorded act | RF §3 AC-5 ✅ — rules 8, 9 | ✅ |
| AC-6 — the baseline is diffable (commit-first, `freeze` scope word, slash-free recovery, no self-naming) | RF §3 AC-6 ✅ — rules 13–16; gate run under both shells → `baseline_recovery.txt` | ✅ |
| AC-7 — delegated authority is a ceiling | RF §3 AC-7 ✅ — rules 17–19 | ✅ |
| AC-8 — granularity rule + carve-out + word-count delta + 5 discriminating rows | RF §3 AC-8 ✅ — rules 5–7; delta reported §4; 5/5 with circularity limit stated first | ✅ |
| AC-9 — Phase HL may no longer author a contract | RF §3 AC-9 ✅ — rules 20–21 + §14 entry; gate `git show 721ca15:…` → EV §E9 | ✅ |
| AC-10 — `❌ REJECT` branch (a) no longer thaws the contract | RF §3 AC-10 ✅; verdict vocabulary and §5 status table untouched | ✅ |
| AC-11 — Working Backwards and visualization mandatory in §3.1 | RF §3 AC-11 ✅, 8/8; no budget/slot/cut-order language; applied to HL's own §3.1 → EV §E11 4/4 | ✅ |
| AC-12 — anti-pattern set complete | RF §3 AC-12 ✅ — 7 present; reproducible count 28 → 35 | ✅ |
| Evidence Artifacts (EV file, `baseline_recovery.txt`, `classification_exercise.md`) | All three present in `phase-a/evidence/` | ✅ |
| Budget: 0 new files, 3 modifications, ~180 added lines | 165 insertions / 16 deletions, 3 files, 0 new framework files | ✅ |

## Deviations from TS

Two, both declared in RF §2 and neither expanding the phase's file set:

1. **`🚫 WITHDRAWN` added to the §12 `Verdict` vocabulary.** AC-2's Evidence clause asked only to
   *record* any field the template could not hold. The executor recorded it and also closed it.
   Justified in RF §2 Decision 1 and EV §E2: HL-TFW-53 §12 row A11 is a live withdrawal, and shipping
   a template that cannot carry the artifact AC-2 names as its own test corpus was judged worse than
   the addition. Under the shipped granularity rule this is a refinement — DoD-2 enumerates `Type`
   values and the column set, not `Verdict` values, so no frozen claim moves.
2. **Rule 6's tripwire time-scoped** — "under §5 and §6 *as they stand at the moment of
   classification*", six words added during the AC-8 exercise. Specification of *how* Phase A
   deliverable 3 meets its outcome; recorded in RF §2 Decision 2 and in
   `classification_exercise.md` §Finding as a change the exercise caused.

**TS items not addressed:** none. All 12 ACs and all three Evidence Artifacts are delivered.

**Undeclared change:** the same commit (`e37a8dc`) also de-links three rows of the executor's own
ONB §2 table and updates the README Task Board row. Both are executor-writable artifacts, but
neither appears in RF §1 or RF §4 — carried to verify.md.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3? — 12 ACs, table above
- [x] Read HL §7 Principles — can I state the design philosophy? — 17 principles; the load-bearing
      set for Phase A is P3 (structural enforcement over guidelines), P5 (evidence, cost,
      alternative), P9 (naming creates behavior), P10 (authority cannot self-extend), P11 (a remark
      is not a verdict), P12 (a frozen baseline must be diffable). The philosophy: the contract must
      exist as *artifact state* — a header field, a marked heading, a column — because a rule with
      no enforcement site is decoration, and the framework has already lost this bet twice (D46's
      "not rubber stamp" half, `templates/RES.md:32`).
- [x] Read ONB — were blocking questions resolved? — both, on 2026-08-10. Q1 (`Proposer` column)
      answered (b), ruled a refinement, retro-fitted to HL §12's live rows by the coordinator.
      Q2 (`APPLIED — restrictive`) answered (a): D8 semantics ship immediately, token name escalated
      as amendment A10 and approved. All 7 recommendations accepted, 5 risks ruled, 9
      inconsistencies dispositioned.

Stage complete: YES
