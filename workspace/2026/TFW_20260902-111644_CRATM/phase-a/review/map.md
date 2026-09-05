# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase A](../RF__phase-a__isolation_and_attribution.md)
> TS: [TS Phase A](../TS__phase-a__isolation_and_attribution.md) at approval commit `29a5c8a98af52493d142c9872ca97a22a5db4eda`

## Understanding

The Executor added a canonical prose protocol for isolated mutation worktrees, exact-path staging,
and producer-attributed cross-session landing, then placed short enforcement edges in the Handoff and
Review workflows. The delivery is one Candidate commit over the approved seven literal VALUE paths,
with four tracked workflow copies synchronized to their two canonical sources and later TRACE commits
recording evidence, RF, and lifecycle state. The RF treats the actual cross-session landing as a
post-review Coordinator action and records that observation as deferred.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — one portable six-part worktree protocol, with isolation explicitly neither lock nor merge strategy | RF §3 claims the canonical protocol answers all six lifecycle questions and preserves the stated boundary | ✅ |
| AC-2 — exact-path staging and independent enforcement on both role surfaces | RF §3 claims all forbidden broad forms, status/cached-set inspection, full paths, dirty-work preservation, and foreign-hunk STOP are present on both surfaces | ✅ |
| AC-3 — a crossing deliverable has its own producer-attributed landing commit, path-history recovery, and exact Candidate reachability before cleanup | RF §3 marks AC-3 complete while RF §§2, 5 and EV E3b state that the actual post-review landing has not occurred and is `DEFERRED` | ❌ |
| AC-4 — selective-read order preserved and four tracked copies byte-identical | RF §3 claims one canonical body, retained Candidate/accounting/Purpose order, and exact adapter parity | ✅ |
| AC-5 — only seven Markdown VALUE paths, no prohibited surface, exact word-count necessity | RF §3 claims the boundary held and RF §4 supplies counts, necessity, D75 results, and the full test result | ✅ |
| AC-6 — immutable approval/Baseline/Candidate facts and literal NUL-safe accounting reproduce the delivery | RF §§1, 3 and 4 claim `7` files, `97 + 17 = 114` touched LOC, fixed `7/160` denominator, correct ordering, and no authority trigger | ✅ |

## Deviations from TS

- The implementation and accounting claims address the six ACs, but the actual AC-3 landing evidence
  required by the TS Gate/Evidence text is absent: EV E3b is explicitly `DEFERRED`, and the RF still
  checks AC-3 as complete.
- Commit `87c26bbcea64f3e2dcf4b6ebd094b4dc0da769ff` is a historical pre-review landing attempt with
  parents at approval and Executor TRACE. It is not an ancestor of the review-ready `HEAD`
  `71e2589bf33fb808372f20acd365fc98a6794223`; the current lineage therefore neither relies on it nor
  supplies a qualifying post-review landing through it.
- No additional RF work appears outside the approved seven VALUE paths plus declared Phase A TRACE.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES

## Round 2 — Map Update

The same review cycle resumed from final-integration tip
`050bfb3bf69e3be4dd65fd62d6ba107a625ade3e`. No VALUE or ASSURANCE path changed after Candidate.
The returned work is TRACE only: the Coordinator ruled the first REVIEW, created qualifying
post-review landing `bb9c86f90208d9d58c62fe695e6d97d238ca28d7`, the same Executor appended
ONB/EV/RF/state evidence under the rung-1 bound, and the Coordinator landed that return in
`050bfb3bf69e3be4dd65fd62d6ba107a625ade3e`.

### TS ↔ RF Alignment Delta

| TS requirement | Round 2 RF/EV claim | Aligned? |
|---|---|---|
| AC-3 — actual reviewed crossing landing, producer-attributed path history, exact Candidate reachability before cleanup | RF Round 2 and EV E3b-R2 name `bb9c86f…`, its reviewed/ruling parent, trailers, tree equality, path history, exact Candidate, excluded failed attempt, and preserved worktree | ✅ pending independent replay in Round 2 Verify |
| AC-1, AC-2, AC-4–AC-6 | No implementation, Candidate, selector, denominator, accounting, or test claim changed | ✅ first-round verification remains applicable; late-VALUE absence must be replayed |

### Round 2 Checkpoint

- [x] Read current phase status and new journal events?
- [x] Read live REVIEW ruling and append-only ONB/RF/EV Round 2 content?
- [x] Recovered the full lineage from first REVIEW through final integration tip?
- [x] Confirmed the governing TS and Candidate identities are unchanged?

Round 2 stage complete: YES
