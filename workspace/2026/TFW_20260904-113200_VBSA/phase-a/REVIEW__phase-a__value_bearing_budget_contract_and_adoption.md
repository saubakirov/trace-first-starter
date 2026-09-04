# REVIEW — TFW_20260904-113200_VBSA / Phase A: Value-bearing budget contract and adoption

> **Date**: 2026-09-04
> **Author**: Codex (Reviewer), on behalf of `saubakirov`
> **Verdict**: 🔄 **REVISE** — **three** proposed rung-1 items
> **RF**: [RF Phase A](RF__phase-a__value_bearing_budget_contract_and_adoption.md)
> **TS**: [TS Phase A](TS__phase-a__value_bearing_budget_contract_and_adoption.md), approved at `36e50e4a362d474550f26e58defe56132b5417be`
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`

---

## 1. Map

Phase A replaces whole-diff scope counting with one prospective, semantic `VALUE` surface and carries that contract through planning, execution, evidence, review, configuration, migration, and adapters. The RF binds Baseline `f5a96af07dcdc4230ecf31100bd155a3dca09604` to Candidate `6dce719338fece2601c1e1ce770273a1bb87c441`, declares the approved 29-path VALUE membership, and reports 634 additions plus 318 deletions (952 touched text LOC); the implementation also modifies two approved ASSURANCE test files. The accounting, Candidate timing, HC-1 boundary, configuration, migration, Saint-Exupéry placement, and adapter parity are correct, but three structural contract/assurance defects prevent acceptance.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|---|---|---|
| V-accounting | Independent value-bearing replay | VERIFIED | Approval `36e50e4a362d474550f26e58defe56132b5417be`; Baseline `f5a96af07dcdc4230ecf31100bd155a3dca09604`; Candidate `6dce719338fece2601c1e1ce770273a1bb87c441`; literal 29-path membership, all `M`; 634 additions, 318 deletions, 952 touched text LOC; no binary N/A; below 50/5000 decomposition triggers and 58/2200 owner ceiling; Candidate is the first implementation commit and later writes are TRACE-only. |
| V1 | Git lineage, Candidate timing, post-Candidate invariance, and HC-1 | ✅ | All refs resolve in order; approved TS is unchanged; Candidate→HEAD changes no VALUE path; Baseline→Candidate protected-path diffs are zero. |
| V2 | Canonical four-class model, config, migration, release/update/init text | ✅ | Live and starter config are exactly 50/5000/2; VERSION and historical migrations remain unchanged; Unreleased/release guidance and forward compatibility are present. |
| V3 | Planner route to canonical VBSA authority | ❌ | The selective `/tfw-plan` graph loads only `Planner scope checkpoint`; the body refers positionally to rules outside its resolved range, and a meaning-reversing checkpoint mutant does not fail the graph or semantic record. **Basis:** TS AC-7; D73/D75. |
| V4 | Clean-receiver preservation proof | ❌ | The test creates receiver bytes and asserts them without exercising or deriving init/update preservation; changing the init rule from preserve to overwrite remains green. **Basis:** TS AC-4 and AC-7; D74/D75. |
| V5 | EV status contract | ❌ | `.tfw/templates/evidence/EV.md` declares four Evidence statuses but permits `INVALID` as a fifth Result value in E-accounting. **Basis:** TS AC-5; D52. |
| V6 | Adapter, manifest, Saint-Exupéry, and full-suite checks | ✅ with stated limits | Twelve adapter copies are byte-identical, manifest blob is unchanged, local quote placement is exact, project check passes, and the full suite reports 553 passed / 1 skipped. Those green signals do not establish V3–V5 because the relevant mutants remain invisible. |

Raw verification and command log: [review/verify.md](review/verify.md). Verification inspected all 31 implementation files after discrepancies exceeded the 14-file configured sample. External citations resolved and supported their attached claims. The known `gen_index.py --check tasks` exit 1 is limited to the immutable RDP journal summary at 123 code points against the current 120 ceiling; it predates this phase and HC-1 forbids its repair here.

## 3. Judge

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD / all TS AC | ❌ | AC-4, AC-5, and AC-7 fail under V3–V5; see Verify D1–D3. |
| 2 | Purpose and design | ❌ | **Purpose aligned:** master-HL baseline clause “Planning, execution, and review use one reproducible accounting contract” addresses the material harm of role-dependent, self-invalidating totals and accords with the North Star's inspectable continuation. **Design unsound:** canonical planner routing and adverse-mutation enforcement do not hold, and EV exposes a contradictory status contract. |
| 3 | Debt disposed by consequence | ❌ | The RDP observation is legally `pending — coordinator` with a proposed consequence-based `not material — owed and forbidden to pay` ruling; no Coordinator disposition exists yet, so the phase stays open. |
| 4 | Style and standards | ❌ | EV's Result placeholder violates its own four-status vocabulary; the planner checkpoint violates D75's uniquely addressed selective-read standard. |
| 5 | Observations collected | ✅ | RF §6 contains one concrete, reproducible, correctly scoped baseline observation and no filler. |
| 6 | RF §7–§9 complete | ✅ | Fact Candidates, Strategic Insights, and diagram sections are present and credible; no new candidate is claimed. |
| 7 | Evidence exists | ✅ | E1–E7 and exactly one E-accounting row exist with populated commands and actual outputs. |
| 8 | Evidence is sufficient | ❌ | E4/E7 do not prove D75 routing or receiver preservation against adverse changes; E5 misses the EV status contradiction. |
| 9 | Backward compatibility | ❌ | Existing `/tfw-plan` selective-read consumers do not receive the canonical sections that the loaded checkpoint tells them to apply. |
| 10 | Safety | ✅ | No secrets, destructive operations, historical rewrites, or HC-1 violations; the receiver issue is a proof gap, not an executed overwrite here. |

Detailed judgment and KNOWLEDGE contradictions: [review/judge.md](review/judge.md).

## 4. Verdict

**🔄 REVISE**

The delivery is fit for the approved purpose and its VALUE accounting is exact, but production acceptance would rely on three green signals that do not enforce their stated contracts. All three repairs fit inside the existing approved TS, so this is a rung-1-only round: no TS revision, HL amendment, lifecycle move, or owner escalation is justified. The items below are proposals; the Coordinator holds acceptance authority and must rule them once before returning the existing approved TS plus the ruled live REVIEW to the same Executor.

### If REVISE — proposals to coordinator

1. **Make the planner checkpoint a real uniquely addressed route to canonical VBSA authority and make route semantics mutation-sensitive.** The `/tfw-plan` selective-read graph must load the exact canonical classification, `Value-bearing accounting contract`, and `Decomposition, constraints, and change authority` content through uniquely named targets; a semantic inversion or removal of that route must fail structural assurance, and synchronized adapters must remain exact. **Rung:** 1. **Owner:** same Executor. **Basis:** TS AC-7; D73/D75. **Observable completion:** graph/output assertions fail on a meaning-reversing checkpoint mutant and pass on the repaired canonical/adapted files.
2. **Replace the self-fulfilling clean-receiver check with behavior-derived or executable preservation assurance.** The check must obtain receiver North-Star preservation from the actual init/update contract or exercise it on a controlled receiver, and an explicit preserve→overwrite mutant must fail while root and `.tfw/README.md` bytes remain unchanged. **Rung:** 1. **Owner:** same Executor. **Basis:** TS AC-4 and AC-7; D74/D75. **Observable completion:** the overwrite mutant is rejected and the clean-receiver fixture proves byte identity without modifying any foreign project.
3. **Restore one four-value Evidence Result vocabulary.** Keep `VERIFIED / DEFERRED / BLOCKED / N/A` as the only EV Result statuses and represent unresolved phase attribution as `INVALID` inside the accounting account/detail, with a structural assertion that no fifth Evidence status is admitted. **Rung:** 1. **Owner:** same Executor. **Basis:** TS AC-5; D52. **Observable completion:** template and parser/test agree on four Evidence statuses and still preserve the required phase-attribution outcome.

## 5. Tech Debt Collected and Disposed

| # | Source | Severity | File | Description | Disposition |
|---|---|---|---|---|---|
| 1 | RF §6 / `gen_index.py --check tasks` | Low | `workspace/2026/TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md` | Immutable baseline summary is 123 code points against the current 120 ceiling. | **pending — coordinator**; proposed **not material — owed and forbidden to pay**: it answers “is remediation owed?” with yes under the current ceiling, but HC-1 M2 and immutable-journal Trace Discipline bar payment in this phase because editing the event would corrupt history. |

## 6. Traces Updated

- [x] Phase lifecycle remains `RF`; REVISE alone creates no transition and no journal event.
- [x] Master/Phase HL status was not changed because the phase did not complete and §5 remains pending.
- [x] Stale project files and protected paths were checked; no Reviewer write occurred outside review-stage files and this REVIEW.
- [x] tfw-docs: N/A — verdict is REVISE; KNW is not entered.
- [x] tfw-knowledge: N/A — verdict is REVISE and RF contains no Fact Candidates.

## 7. Fact Candidates

No fact candidates. The returned items are implementation/assurance defects against already-approved TS and KNOWLEDGE contracts, not new durable project facts.

---

*REVIEW — TFW_20260904-113200_VBSA / Phase A: Value-bearing budget contract and adoption | 2026-09-04*
