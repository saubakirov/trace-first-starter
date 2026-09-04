# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase B](../../RF__phase-b__primary_role_paths.md)
> TS: [TS Phase B revision 2](../../TS__phase-b__primary_role_paths__rev2.md)

## Understanding

The executor repaired the three findings from the first Phase B review without reopening the
accepted role-path compression. It added all four Researcher stage-template edges to both focused
and deep candidate graphs, replaced anchor-removal checks with source-derived output-changing
semantic mutants, and made `conventions.md` the sole three-rung REVISE routing authority consumed by
Plan, Handoff, and Review.

The revision implementation changes exactly 12 existing implementation/test files: the shared
conventions, three canonical workflows and their six generated workflow copies, plus the two existing
test modules. The RF, EV, four raw evidence transcripts, phase status, and journal transition are
result traces written after that implementation. Candidate ancestor `8b16c0b` and the RF-named
`8066284` have the identical tree `82ea539466cffb52ad0dce64903a80020bea626f`.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-R1 — enumerate the exact four Researcher stage-template edges in both modes; retain exact graph totals `6,103` focused and `6,168` deep; fail an omitted edge | RF rev2 §3 claims all eight ordered stage edges, exact totals, and a source-derived omission mutant; RF §5 points to R2-E1 and `runtime-context-primary-roles.txt` | ✅ |
| AC-R2 — source-derived output-changing P/R/E/V/C/A mutants must complete record construction, change a named semantic field, and fail only at independent comparison while ordinary and isolated cases pass | RF rev2 §§2–3 claim six output-changing semantic mutants, ordinary cases, isolated family mismatch, and no probe-anchor deletion; RF §5 points to R2-E2 and `semantic-primary-roles.txt` | ✅ |
| AC-R3 — one authoritative rung 1/2/3/mixed route with exact recipient, ruling site, governing artifact, lifecycle effect, hard stop, and contradiction mutants | RF rev2 §§1–3 claim the conventions table is authoritative, Plan/Handoff/Review delegate to it, all four isolated cases pass, and four source-derived contradiction mutants fail; RF §5 points to R2-E3 and `semantic-primary-roles.txt` | ✅ |
| AC-R4 — exact copies, four clean receivers with 11 commands, retained reductions and graph totals, all gates, exact 12-file/551-LOC round, cumulative 24-file/1,556-LOC budget, frozen exclusions, and append-only use of exactly five evidence files | RF rev2 §§3–5 claims exact copy parity, clean receivers, all five reductions and graph totals, 156 targeted tests, 450 collected tests, 449 passed plus one skip, project verification, only the accepted RDP diagnostic, exact round/cumulative budgets, unchanged exclusions, and five evidence artifacts | ✅ |

## Deviations from TS

No deviation is declared. The implementation commit `8b16c0b` changes exactly the 12 paths listed in
TS revision 2 §3 and records 442 insertions plus 109 deletions, exactly 551 changed lines. Its parent
contains the approved return traces; candidate `ba7827e` adds only the cumulative RF/EV/raw evidence,
phase status, and one journal event. The first REVIEW, its first-round stage files, original TS,
master/phase HL, tasks, skills, manifest, templates, config, and knowledge files are outside the
revision implementation commit.

## Referenced Predecessors

- `80382fbffd52b1f13cb3b38e8e450ecc0fef2fd5` — Phase B immutable comparison baseline.
- `272a7cf` — first-round reviewed candidate and revision-2 comparison point.
- `REVIEW__phase-b__primary_role_paths.md` — first review, including the three returned findings and
  their Coordinator-ruled disposition block.
- `TS__phase-b__primary_role_paths.md` — original governing TS retained as history.
- `ONB__phase-b__primary_role_paths.md` — cumulative onboarding record with the revision-2 return.

## Checkpoint

**Self-check:**
- [x] Read RF §1–§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES
