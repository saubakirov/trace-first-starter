# REVIEW — TFW_20260904-113200_VBSA / Phase A: Value-bearing budget contract and adoption

> **Date**: 2026-09-04
> **Author**: Codex (Reviewer), on behalf of `saubakirov`
> **Verdict**: 🔄 **REVISE** — pass 2: **one** proposed rung-1 item; the three pass-1 items are closed
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

## 8. Coordinator Ruling

> **Ruling date:** 2026-09-04
> **Coordinator:** Codex, on behalf of `saubakirov`
> **Round:** rung 1 only
> **Governing execution artifact:** approved `TS__phase-a__value_bearing_budget_contract_and_adoption.md` at `36e50e4a362d474550f26e58defe56132b5417be`, bounded by this ruled live REVIEW
> **Lifecycle:** remains `RF` until the same Executor accepts the return and records `RF → ONB`

The Coordinator accepts all three proposals once. They are necessary to satisfy the already-approved AC and do not revise Goal, Value, accepted outputs, AC, DoF, phase ownership, architecture, public interfaces, persisted data, or trust/authority boundaries. The repair surface is confined to the existing approved 31 implementation paths: the canonical `plan`/`init` workflows and their already-declared tracked copies, the EV template, and the two ASSURANCE files. No new VALUE path, normative carrier, manifest entry, ledger, script, or authority is permitted. The immutable owner-approved denominator remains 29 logical VALUE files and 1,100 touched LOC; because the repairs change VALUE files, the same Executor must create a new tested Candidate and recompute the complete Baseline-to-Candidate result before EV/RF.

| # | Proposal ruling | Closed implementation bound | Owner | Observable completion |
|---|---|---|---|---|
| 1 | **ACCEPTED — rung 1** | Make `/tfw-plan` load the uniquely addressed canonical classification, `Value-bearing accounting contract`, and `Decomposition, constraints, and change authority` sections while retaining one canonical authority. Add mutation-sensitive structural assurance; keep both adapter copies exact. | Same Executor | A meaning-reversing or missing-route mutant fails; repaired canonical and adapter files pass D75 context ceilings and exact-copy checks. |
| 2 | **ACCEPTED — rung 1** | Replace the self-fulfilling receiver assertion with behavior-derived or executable init/update preservation assurance inside the existing workflow and test carriers. Do not touch a foreign project. | Same Executor | A preserve-to-overwrite mutant fails, while a controlled clean receiver proves root and `.tfw/README.md` North-Star bytes unchanged. |
| 3 | **ACCEPTED — rung 1** | Keep `VERIFIED`, `DEFERRED`, `BLOCKED`, and `N/A` as the only EV Result statuses. Keep phase-attribution `INVALID` only inside accounting detail, never as a competing Result status. | Same Executor | Template and structural test admit exactly four Result statuses and still preserve the `INVALID` attribution outcome. |

**RF §6 debt disposition:** **not material — owed and forbidden to pay in this phase.** The current 120-code-point ceiling means remediation is owed, but HC-1 M2 and immutable-journal Trace Discipline forbid changing `workspace/2026/TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md`. The unchanged, exactly reproduced 123-code-point baseline observation does not block this rung-1 return and must not be hidden or repaired by the Executor.

**Dispatch:** return the existing approved TS plus this ruled live REVIEW to the same Executor. Start `/tfw-handoff`. After the new RF, return to the same Reviewer with `/tfw-review`.

---

## 9. Reviewer Pass 2 — Map

The same Executor returned the ruled rung-1 round through lineage `5ab04d0e666ad38960229013a7ac649e693f3ca8` → `15ac484` → `a1afe36` → Candidate `edb0017bd0c1d33eafbf99ee2b9c841e2fd91b2f` → RF/EV HEAD `b600c6f466001a9a95170011cf942e38d1c03e7a`. Candidate changes exactly the ruled 13-path subset (11 approved VALUE plus two approved ASSURANCE paths) and retains the approved TS at `36e50e4a362d474550f26e58defe56132b5417be`, Baseline `f5a96af07dcdc4230ecf31100bd155a3dca09604`, literal 29-path VALUE selector, and immutable 29/1,100 denominator.

All three pass-1 findings are behaviorally closed: `/tfw-plan` loads the three unique canonical ranges and rejects route/value mutants; controlled init/update receiver operations preserve North-Star/history bytes and reject an overwrite mutant; EV admits exactly four Result statuses while keeping attribution `INVALID` in detail. Independent return verification nevertheless found one new rung-1 discrepancy: the return met the planner context ceiling by removing approved semantics from the canonical ranges, and the source-derived guard does not detect inversion of the surviving selector rule.

## 10. Reviewer Pass 2 — Verify

| # | What was checked | Result | Evidence |
|---|---|---|---|
| V-accounting | Independent value-bearing replay | VERIFIED | Approval `36e50e4a362d474550f26e58defe56132b5417be`; Baseline `f5a96af07dcdc4230ecf31100bd155a3dca09604`; Candidate `edb0017bd0c1d33eafbf99ee2b9c841e2fd91b2f`; literal membership is 29 `M`; 657 additions + 318 deletions = 975 touched text LOC; binary N/A 0; VALID Phase A; below 50/5,000 triggers and 58/2,200 owner ceiling; later writes are TRACE-only. |
| R2-V1 | Return lineage, exact scope, TS immutability, attribution, and HC-1 | ✅ | Candidate parent→Candidate is exactly 13 ruled paths; Candidate→HEAD has zero selector paths; approved TS is unchanged; no unapproved or protected implementation path changed. |
| R2-V2 | Pass-1 planner-route finding | ✅ closed | Three named ranges resolve once and are loaded in order; context is 24,729 ≤ 24,730; VALUE inversion and missing-route mutants fail; plan adapters are exact. |
| R2-V3 | Pass-1 clean-receiver finding | ✅ closed | Parsed init/update policies drive controlled operations; receiver bytes are preserved; preserve→overwrite changes both North-Star outputs and fails validation. |
| R2-V4 | Pass-1 EV-status finding | ✅ closed | E1 and E-accounting expose exactly `VERIFIED / DEFERRED / BLOCKED / N/A`; a fifth-status mutant fails; attribution `INVALID` remains detail only. |
| R2-V5 | Approved semantics in the loaded canonical ranges | ❌ R2-D1 | Compared with the pre-return canonical carrier, current conventions omit the approved cross-domain examples, whole-fixed-diff ambiguity rule, deterministic/replayable pre-work selector requirement, explicit freehand-subtraction prohibition, and part of the Saint-Exupéry non-damage boundary. A freehand-permission mutant leaves both planner/VBSA projections unchanged and is accepted by the guard. **Basis:** TS AC-1, AC-2, AC-7; frozen master-HL §§3/5/7; D73/D75. |
| R2-V6 | Targeted/full suites, adapters, manifest, syntax, and indices | ✅ with R2-D1 limit | Targets: 26 passed and 10 passed; runtime: 154 passed; full: 559 passed/1 skipped. Twelve adapter copies are exact; manifest is unchanged; diff/YAML/Python/project checks pass. The task check reports only the immutable ruled RDP 123>120 observation. These signals do not establish the removed semantics. |

Raw verification, commands, evidence-by-evidence results, and citation census: [review/verify.md](review/verify.md). All 13 return paths were inspected. The unchanged citation set resolves 45/45; R2-D1 is a contradiction between the implementation and existing approved authority, not a broken citation.

## 11. Reviewer Pass 2 — Judge

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD / all TS AC | ❌ | AC-1, AC-2, and AC-7 fail on R2-D1; the three pass-1 failures are closed. |
| 2 | Purpose and design | ❌ | **Purpose aligned:** the frozen baseline requires that “Planning, execution, and review use one reproducible accounting contract,” preventing role-dependent and self-invalidating totals. **Design unsound:** the designated semantic authority no longer contains the complete approved contract, and the guard verifies hard-coded expectations rather than the live selector rule. |
| 3 | Debt disposed by consequence | ✅ | Coordinator ruling §8 terminally disposes the RDP observation as `not material — owed and forbidden to pay in this phase`, citing HC-1 M2 and immutable-journal Trace Discipline. Nothing remains pending. |
| 4 | Style and standards | ❌ | Four-status EV, receiver policy, naming, and parity now hold; canonical semantic completeness and D75 source-derived mutation sensitivity do not. |
| 5 | Observations collected | ✅ | The one pre-existing RDP observation remains exact, protected, and terminally ruled; no new debt observation arose. |
| 6 | RF §§7–9 complete | ✅ | Cumulative and return content is present and credible; no unsupported Fact Candidate or Strategic Insight is asserted. |
| 7 | Evidence exists | ✅ | Cumulative plus return evidence is present, populated, and uses the fixed status vocabulary. |
| 8 | Evidence is sufficient | ❌ | Accounting and the three pass-1 repairs are established; E1/E7 do not establish canonical semantic preservation because the selector mutant is invisible. |
| 9 | Backward compatibility | ❌ | A fresh existing `/tfw-plan` consumer reaches the ranges but cannot recover all approved classification/ambiguity rules from them and may emit a non-replayable selector while conformance stays green. |
| 10 | Safety | ✅ | No secrets, destructive operations, binary ambiguity, protected-history rewrite, or HC-1 violation was found. |

Detailed purpose and KNOWLEDGE contradiction judgment: [review/judge.md](review/judge.md).

## 12. Reviewer Pass 2 — Verdict

**🔄 REVISE**

The exact accounting and all three ruled return repairs pass independent replay, but acceptance still depends on a canonical carrier that no longer expresses every approved semantic requirement. Because the defect is confined to implementation of existing AC-1/AC-2/AC-7 and frozen semantics, it is one rung-1 proposal: no TS revision, HL amendment, lifecycle move, or Owner escalation is justified. The Reviewer proposes and stops; the Coordinator must rule the item once.

### Pass-2 proposal to Coordinator

1. **Restore the complete approved semantic contract inside the three loaded canonical ranges and make the ambiguity/selector guard source-derived.** Preserve explicit domain-agnostic coverage for code, shipped prompts, accepted documents/presentations/data/generated outputs, ordinary tests versus conformance-as-product, task-folder deliverables, and TFW-looking product sources; preserve accepted/necessary precedence, the whole path's fixed Baseline→Candidate diff, a deterministic replayable narrower selector declared before work, the prohibition on freehand line subtraction, and the complete Saint-Exupéry non-damage boundary including continuation. Keep `/tfw-plan` at or below 24,730 words and its adapters exact. **Rung:** 1. **Owner:** same Executor. **Basis:** TS AC-1, AC-2, AC-7; frozen master-HL §§3/5/7; D73/D75. **Observable completion:** every named rule/example is recoverable from the three loaded canonical ranges, and changing the selector rule to permit freehand subtraction changes the source-derived output and is rejected while all pass-1 repair checks remain green.

## 13. Reviewer Pass 2 — Tech Debt

No new debt captured. The RDP 123>120 observation retains the terminal Coordinator disposition in §8; it is not pending and must not be repaired in this phase.

## 14. Reviewer Pass 2 — Traces Updated

- [x] Phase lifecycle remains `RF`; a REVISE verdict creates no transition or journal event.
- [x] Master/Phase HL and the approved TS were not changed.
- [x] Reviewer writes are confined to `review/map.md`, `review/verify.md`, `review/judge.md`, and this live REVIEW.
- [x] tfw-docs: N/A — REVISE does not enter KNW.
- [x] tfw-knowledge: N/A — REVISE does not enter KNW and no Fact Candidate exists.

## 15. Reviewer Pass 2 — Fact Candidates

No fact candidates. R2-D1 is a task-local implementation/assurance defect against approved TS and existing D73/D75 knowledge, not a new durable project fact.

## 16. Coordinator Ruling — Pass 2

> **Ruling date:** 2026-09-04
> **Coordinator:** Codex, on behalf of `saubakirov`
> **Round:** rung 1 only
> **Governing execution artifact:** unchanged approved TS at `36e50e4a362d474550f26e58defe56132b5417be`, bounded by this ruled live REVIEW
> **Lifecycle:** remains `RF` until the same Executor accepts the return and records `RF → ONB`

The Coordinator **ACCEPTS** the single pass-2 proposal once. R2-D1 is an implementation and assurance defect inside approved AC-1, AC-2, and AC-7; it changes no Goal, Value, accepted output, DoF, phase ownership, architecture, interface, persisted data, or trust/authority boundary. The repair is confined to existing approved VALUE carriers for canonical conventions/planning and their already-declared tracked copies when their canonical source changes, plus the two approved ASSURANCE files. No new path, normative carrier, manifest entry, ledger, script, migration, or authority is permitted. The immutable owner-approved denominator remains 29 logical VALUE files and 1,100 touched LOC.

**Closed implementation bound:** restore in the three `/tfw-plan`-loaded canonical ranges every approved domain example and rule named in §12: the cross-domain VALUE/ASSURANCE/TRACE/DERIVED cases; accepted-output and necessary-constituent precedence; whole-path treatment of the fixed Baseline-to-Candidate diff when roles are inseparable; a narrower selector only when deterministic, replayable, and declared before work; the explicit prohibition on freehand line subtraction; and the full Saint-Exupéry non-damage boundary including purpose, value, correctness, architecture, modularity, inspectability, and continuation. The source-derived projection and adverse mutant must derive from those live ranges: permitting freehand subtraction or removing a required rule/example changes the produced record and is rejected. `/tfw-plan` must remain at or below the unchanged 24,730-word D75 ceiling, adapters must remain exact, and every pass-1 route/receiver/EV-status check must remain green. Meeting the ceiling by deleting any other required semantic rule is outside this bound.

Because the repair changes VALUE, the same Executor must create a new tested Candidate and recompute the complete approved 29-path Baseline-to-Candidate accounting before updating the single EV accounting row and append-only RF/round traces. The terminal RDP debt disposition in §8 remains unchanged and forbids repair of the historical event.

**Dispatch:** return the unchanged approved TS plus this pass-2 ruled live REVIEW to the same Executor. Start `/tfw-handoff`. After the new RF, return to the same Reviewer with `/tfw-review`.

---

*REVIEW — TFW_20260904-113200_VBSA / Phase A: Value-bearing budget contract and adoption | 2026-09-04*
