# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF TFW-56](../RF__TFW-56__review_mode_removal.md)
> TS: [TS TFW-56](../TS__TFW-56__review_mode_removal.md)

## Understanding

The executor deleted the `code / docs / spec` review-mode **selection** — the folder
`.tfw/workflows/review/` with its three mode files, the `review.md` mode step and its 🛑 WAIT gate,
the `tfw.review.default_mode` config key in two files, and the `Mode:` / `Review Mode` fields in four
templates — and promoted the checks that selection was gating into the universal Judge checklist,
which goes from 7 rows to 10. `review.md`'s steps renumber 0-7 contiguously, so Step 0 is Session
Naming for the first time and TD-106 closes by deletion rather than annotation.

Three decisions shape the result beyond the literal TS. **(1)** S1 was written *against* U7 rather
than merely differently: row 7 asks whether the evidence exists, row 8 whether it establishes the
claim, with a contrast note and a Checkpoint item forcing separate answers. **(2)** U2 was split into
two separately quotable clauses — (a) mapping integrity, (b) design soundness — so that TFW-53 Phase
C, whose frozen DoD-20 replaces the mapping-integrity check in that same row, can replace clause (a)
without silently taking the promoted S3 with it. **(3)** All three orphaned `docs`/`spec` verify
actions were migrated into a new **Claim & Source Checks** section in `verify.md` rather than
declined, which AC-4 also permitted.

Scope: 20 modified + 3 deleted framework/root files + 1 new evidence artifact. Net LOC −39. One
anomaly is self-reported: the three deletions were swept into a concurrent session's commit
(`fbdf443`, TFW-53/B), so the outcome is correct but its attribution is not.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 selection absent, steps contiguous, Step 0 = Session Naming | RF §3 AC-1; EV §E1 | ✅ |
| AC-2 corrected ten-row Judge checklist, S1 ≠ U7, rates carried | RF §3 AC-2; EV §E2, §E3 | ✅ |
| AC-3 all eight mode rows given a recorded home | RF §3 AC-3 accounting table (8 rows) | ✅ |
| AC-4 three orphaned verify actions homed; four `code` actions still mandated | RF §3 AC-4 accounting table (8 distinct actions) | ✅ |
| AC-5 `REVIEW.md` §3 matches `judge.md` row-for-row | RF §3 AC-5; EV §E4 | ✅ |
| AC-6 `default_mode` gone, `min_verify_ratio` untouched | RF §3 AC-6; EV §E5 | ✅ |
| AC-7 propagation table correct, step pointer resolves | RF §3 AC-7; EV §E6 | ✅ |
| AC-8 conventions + glossary carry no mode vocabulary | RF §3 AC-8; EV §E6 | ⚠️ substance ✅, command misquoted in RF (V-D1) |
| AC-9 six adapter copies clean and behaviourally identical | RF §3 AC-9; EV §E6 | ✅ |
| AC-10 VERSION bumped, CHANGELOG names the removed key | RF §3 AC-10 | ✅ |
| AC-11 TD-106 closed with the reason | RF §3 AC-11 | ✅ |
| AC-12 grep gate zero, history intact, 3 deletions, no framework file created | RF §3 AC-12 (qualified); EV §E7, §E8, §E9 | ✅ on substance, attribution flagged by the executor |

## Deviations from TS

1. **`tfw.version` in `.tfw/project_config.yaml` bumped `1.0.0` → `1.1.0`** alongside `.tfw/VERSION`.
   Not itemised in TS §4, but inside a file TS §4 already lists as MODIFY. Justified in RF §2
   decision 1 by `git log -p` showing the two fields moving in lockstep since 0.8.5. Recorded, not
   hidden. Accepted as refinement, not scope creep.
2. **`REVIEW.md` §3 gained a seventh row that was missing before this task.** Baseline
   (`6c3c506`) shows 6 rows against `judge.md`'s 7 — the Evidence completeness row added in 0.8.8
   never reached the synthesis template. AC-5 requires row-for-row alignment, so repairing it is a
   consequence of the AC, not a bonus fix. RF §2 decision 5 records it so the 6 → 10 move does not
   read as three extra rows of scope.
3. **`conventions.md` §11 L466 (*"Mode files loaded at Step 2, not at start"*) deliberately left
   unedited.** RF §2 decision 6 and Observation 6. The sentence's D42 lineage is about review, but it
   remains true of research (`research/base.md` Step 2 loads `focused`/`deep`). Reported rather than
   changed — correct under "do not widen scope".
4. **Nothing in TS §2 Out of Scope was touched.** The rigour axis, `update.md`'s removed-key rule,
   the TFW-45 consolidator, goal defence in review, and history rewriting are all absent from the
   diff. Verified.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
      *Delete rather than relabel; no coverage loss without a recorded home; a check that cannot fail
      is not a check; what to check is declared once, by the TS; explicit N/A over silent skip;
      history is evidence; behavioural adapter parity; structural enforcement over promise.*
- [x] Read ONB — were blocking questions resolved? *One blocking question (Q1, version bump), owner
      answered `1.1.0`. Four notes N1-N4 recorded.*

Stage complete: YES
