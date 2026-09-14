# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [Phase A RF](../RF__phase-a__continuation_responsibilities.md)
> TS: [approved Phase A TS](../TS__phase-a__continuation_responsibilities.md)

## Understanding

The Executor rewrote canonical Plan and synchronized its two full-copy receivers so an exact existing task or phase is inspected before the Knowledge Gate or any Plan write, producing one routing, wait, or terminal result without performing another workflow's effect. Two existing assurance modules were extended to exercise the 28-case routing matrix, ten identity/readback cases, no-mutation and semantic mutants, receiver-retirement preconditions, split-history preservation, parity, scope, and Baseline-to-Candidate accounting; Resume and its live retirement surfaces were left unchanged. The immutable Candidate is `c319269d24abb89a58e2dc1a18ada1ea4ecb8120`, whose own commit contains exactly three VALUE and two ASSURANCE modifications; EV and RF were added later at TRACE base `77f39be7d8c44656aa30e1a11b041b3f44d24954`.

The governing chain is the owner-approved TS proposal `413945ca0a4f34065ff22b8b24f47bf694d72710` (blob `d15c5dc8b25c2751ed289a418f937226608333dc`), followed by approval producer `7f4e942f66a4ef19a100b10a9fd30e11ea143c25`, which records the owner act and changes the TS carrier to APPROVED. The immutable accounting authority is `3 VALUE files / 900 touched text LOC` against Baseline `f6e85aa898061779c6b37bba34dc97e28c76f01f`; C1 keeps Resume on any acceptance miss.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — only three literal VALUE paths; canonical/copy parity; Plan ≤1,200; complete `C < 2,737`; no Resume/substitute surface | RF claims exactly three VALUE modifications, two byte-identical receivers, Plan and `C` both 1,199, `3/747`, no new instruction/helper or Resume path | ✅ |
| AC-2 — total routing-only matrix, phase-local truth, exact lifecycle routes, 28 fixtures, no pre-route mutation | RF claims all 28 lifecycle/selection fixtures return the exact route and preserve complete repository bytes | ✅ |
| AC-3 — authoritative identity re-resolution/reapplication, root/child/non-AT split, exact readback, failure behavior | RF claims ten identity/readback cases cover root, child, non-AT, invalid facts, reapply/readback, and transport failure | ✅ |
| AC-4 — route outputs only; lifecycle effects remain with their owners; exact Coordinator control boundary | RF claims no delegated effect and exact Coordinator-control routing for close/recovery and carrier mismatch | ✅ |
| AC-5 — Resume unchanged; four-class receiver model including `TARGET_CURRENT`; ten-command/four-adapter convergence; 179+3 history oracle; C1 on failure | RF claims all receiver classes, four-adapter convergence, empty second run, 179-entry digest, three aggregate subsequence oracles, and unchanged Resume | ✅ |
| AC-6 — targeted and configured suites; mutants change projection; per-AC EV; exact five-path Candidate; TRACE not runtime input | RF claims 355 targeted passes, 625 collected, 624 passes plus one platform skip, passing mutants, five Candidate paths, and TRACE-only evidence | ✅ |
| Approved accounting contract — literal VALUE selector, immutable Baseline/Candidate, numeric numstat, first tested Candidate before EV/RF, prospective authority | RF claims `3` logical VALUE files, `255 + 492 = 747` touched text LOC, Baseline `f6e85aa…`, Candidate `c319269…`, and pre-work owner authority under `3/900` | ✅ |

## Deviations from TS

No RF-declared scope deviation. The Baseline-to-Candidate repository diff contains pre-existing TKL and RWNR planning/trace paths because the approved accounting Baseline predates Phase A execution; the Candidate commit itself lists exactly the five approved VALUE/ASSURANCE paths. Whether all aligned claims are true is reserved for Verify.

## Checkpoint

**Self-check:**
- [x] Read RF §1–§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES
