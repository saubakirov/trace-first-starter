# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. The evidence from Verify is now the basis for the quality ruling.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | Verify V3/V6/V7 and discrepancies D1–D3 show that TS AC-4, AC-5, and AC-7 are not met: the planner does not load canonical VBSA authority, clean-receiver preservation is not behavior-derived or mutation-sensitive, and the EV form contradicts its fixed status vocabulary. |
| 2 | (a) Purpose Check; (b) Design soundness | ❌ | **(a) ✅ Aligned:** the master-HL baseline requires that “Planning, execution, and review use one reproducible accounting contract,” serving the North-Star requirement that an authorized successor can inspect and continue the work; the concrete harm at stake is repeated RF/REVIEW correction caused by self-invalidating or role-dependent totals. The result adds no adjacent deliverable, confesses no different home, and addresses that material harm. **(b) ❌:** the design does not structurally preserve the single contract at the planner entry point and allows assurance to remain green under meaning-reversing mutants (Verify D1/D2); the contradictory EV Result placeholder also violates the one-vocabulary evidence design (D3). |
| 3 | Debt disposed | ❌ | RF §6 contains one real pre-existing RDP observation. REVIEW §5 will carry `pending — coordinator` with the proposed `not material — owed and forbidden to pay` disposition, naming HC-1 M2 and immutable-journal trace integrity as the barring clauses. That pending state is legal but is not yet a Coordinator ruling and therefore keeps the phase open. |
| 4 | Style & standards | ❌ | Naming, adapter synchronization, and formatting otherwise hold, but `.tfw/templates/evidence/EV.md` states a four-status standard and then exposes `INVALID` as a fifth Result value (Verify D3); the planner checkpoint also uses positional prose instead of uniquely addressed canonical reads required by D75 (D1). |
| 5 | Observations collected | ✅ | RF §6 records one specific, reproduced baseline defect: the RDP journal summary is 123 code points against the 120 limit. It is neither filler nor attributed to this phase, and Verify V9 confirms it was not modified. |
| 6 | RF completeness (§7–9) | ✅ | RF §7 explicitly reports no Fact Candidates, §8 reports no Strategic Insights, and §9 supplies a relevant accounting/authority diagram. The empty candidate/insight sets are credible because the implementation applies already-approved D15–D21 and D73–D75 rather than discovering new durable facts. |
| 7 | Evidence completeness — does the evidence exist? | ✅ | EV contains E1–E7 plus exactly one E-accounting row; all eight items have actual commands/results and use a currently valid evidence status. No TS Evidence field is missing. |
| 8 | Evidence sufficiency — does the evidence establish the claim? | ❌ | The green suite and evidence establish accounting, Git timing, adapter parity, config migration, HC-1, and current text presence, but E4/E7 do not establish receiver preservation or D75 routing under adverse source changes, and E5 does not expose the EV status contradiction (Verify Evidence Verification and D1–D3). |
| 9 | Backward compatibility | ❌ | `/tfw-plan` is an existing selective-read consumer. Its discovered graph now receives only `Planner scope checkpoint`, while that resolved body does not contain or uniquely address the canonical classification/accounting/authority rules it tells the planner to apply; a new planner can therefore author a TS from a shorthand copy instead of the canonical contract (Verify D1). |
| 10 | Safety | ✅ | Baseline→Candidate changes contain no secrets, credentials, destructive operations, or protected historical rewrites. HC-1 checks are clean, the twelve adapters are byte-identical to their canonical sources, the manifest and VERSION are unchanged, and the foreign-receiver preservation defect is an assurance gap rather than an executed overwrite in this repository. |

Rows 7 and 8 intentionally differ: the evidence artifacts are present and populated, but three offered green signals do not prove the corresponding structural claims.

## Purpose Check — row 2 clause (a)

The contract baseline is `174e660bd75d3ad978584a8e1f59d6b22fd4f44f`. Later master-HL differences are confined to free §8 and append-only §12 operating-topology records; frozen §§1/3–7 are unchanged. The Project North Star requires purposeful, human-governed, inspectable continuation and rejects output that obscures authority or continuation. Phase A is therefore fit for the intended purpose, but its current implementation quality is insufficient for acceptance because D1–D3 weaken the structural enforcement that purpose requires.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D73 — workflow-owned, uniquely addressed reads | RF §2 decision 2 and §4 claim `Planner scope checkpoint` preserves the single authoritative route | **Yes:** the selective graph contains only the checkpoint; its positional body neither includes nor uniquely addresses the two canonical rule sections (Verify D1). |
| 2 | D74/D75 — minimal role paths with source-derived proof; selective workflow reads must retain behavior and reject semantic mutants | RF §4 and EV E4/E7 claim source-derived D75 and clean-receiver proof | **Yes:** both the planner meaning-reversal mutant and the init overwrite mutant remain green (Verify D1/D2). |
| 3 | D52 — Evidence uses the fixed `VERIFIED / DEFERRED / BLOCKED / N/A` vocabulary | RF §3 AC-5 and EV E5 claim a compliant, uniquely bound accounting row | **Yes:** the EV row placeholder admits `INVALID` as a Result status instead of keeping attribution invalidity inside the accounting details (Verify D3). |

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence, and every failure names a specific finding.
- [x] No row uses a bare `⚪ N/A` or silently skips a universal check.
- [x] Row 2(a) was answered against master HL at contract baseline plus the Project North Star, with a quoted clause and a concrete harm; neither TS nor Phase HL was used as the reference.
- [x] Rows 7 and 8 were answered separately: evidence exists, but three claims are not established.
- [x] DoD assessment cites Verify D1–D3 and the affected ACs.
- [x] REVIEW §5 debt is identified as legal `pending — coordinator`, with an admissible proposed ruling and an existing task-local target; it remains open until the Coordinator rules.
- [x] RF §§7–9 were checked for presence and quality.
- [x] KNOWLEDGE.md was cross-referenced and three material contradictions were documented.
- [x] RF Fact Candidates were reviewed; none require challenge because none were proposed.

Stage complete: YES

# Pass 2 — Return Judge

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | Return Verify R2-V5/R2-D1 shows that AC-1, AC-2, and AC-7 are not met. The candidate shortened the sole canonical semantic authority until approved cross-domain examples and the fixed-diff/deterministic-selector/freehand-subtraction rules disappeared, while the claimed source-derived guard remains green when the surviving selector sentence is inverted. |
| 2 | (a) Purpose Check; (b) Design soundness | ❌ | **(a) ✅ Aligned:** the frozen master-HL baseline says, “Planning, execution, and review use one reproducible accounting contract,” so the concrete harm remains role-dependent or self-invalidating totals that create false RF/REVIEW correction loops. The returned implementation remains directed at that purpose and adds no adjacent deliverable. **(b) ❌:** the design makes `.tfw/conventions.md` the semantic authority but removes approved semantics from its loaded ranges, then verifies hard-coded expectations rather than deriving the relevant ambiguity/selector behavior from that authority (R2-D1). |
| 3 | Debt disposed | ✅ | REVIEW §8 contains the Coordinator's terminal ruling for the existing RDP journal observation: `not material — owed and forbidden to pay in this phase`, with HC-1 M2 and immutable-journal trace integrity as the barring clauses. No pass-2 debt is introduced and none remains pending. |
| 4 | Style & standards | ❌ | Naming, formatting, four-status EV vocabulary, receiver policy, and adapter synchronization now hold. However, the canonical authority is too compressed to satisfy the approved semantic-content standard in AC-1/AC-2, and the guard still violates D75's source-derived, mutation-sensitive proof requirement (R2-D1). |
| 5 | Observations collected | ✅ | RF §6 still records the reproduced, pre-existing RDP journal summary of 123 code points against 120. The terminal ruling is in REVIEW §8, the protected journal remains unchanged, and return verification found no new observation requiring debt treatment. |
| 6 | RF completeness (§§7–9) | ✅ | The cumulative RF retains credible §§7–9, and its return-round additions state the closed findings, result, evidence, and value-flow consequence without displacing the cumulative record. |
| 7 | Evidence completeness — does the evidence exist? | ✅ | The cumulative and return EV material exists, is command-backed, and uses the fixed four-status vocabulary. The original three return targets have direct evidence and all now reproduce successfully. |
| 8 | Evidence sufficiency — does the evidence establish the claim? | ❌ | Evidence establishes exact accounting, fixed refs, timing, parity, receiver preservation, four-status EV behavior, config migration, and HC-1. It does not establish preservation of the approved canonical semantics: a freehand-permission mutant leaves both the planner projection and VBSA record unchanged and is not rejected (R2-D1; E1/E7). |
| 9 | Backward compatibility | ❌ | `/tfw-plan` now reaches the three intended canonical ranges, but an existing planner consumer can no longer recover the approved cross-domain classifications or the whole-fixed-diff and deterministic-selector constraints from the designated semantic authority. It can therefore produce a non-replayable selector while the conformance guard stays green (R2-D1). |
| 10 | Safety | ✅ | Baseline→Candidate contains no secrets, destructive behavior, binary ambiguity, unapproved implementation path, protected historical rewrite, or HC-1 violation. The defect is a material semantic/assurance regression, not evidence of an executed unsafe mutation. |

Rows 7 and 8 remain intentionally separate: the evidence exists and the three accepted return repairs are now proven, but the new semantic-preservation claim is not proven.

## Purpose Check — row 2 clause (a)

The contract baseline remains `174e660bd75d3ad978584a8e1f59d6b22fd4f44f`. Its frozen §1 requires one reproducible accounting contract and names the harm as correction rounds caused by figures invalidated by recording or checking them. Frozen §§3–7 require semantic precedence, domain-agnostic examples, whole-path fixed-diff treatment, a deterministic pre-work selector, and prohibition of freehand line subtraction. The Project North Star separately requires bounded, inspectable, continuable work and rejects technically polished output that obscures purpose or authority. Phase A remains aligned to that purpose; R2-D1 makes the present design insufficient for acceptance because the canonical carrier no longer preserves all approved decisions needed by a fresh authorized planner.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D73/D75 — selective consumers need uniquely addressed canonical authority and source-derived, mutation-sensitive proof | RF return §§2–4 and EV E1/E7 claim the planner contract is loaded and guarded from canonical sources | **Yes:** the three ranges are loaded, but approved semantics were removed from those ranges, and a meaning-reversing freehand-selector mutant leaves both derived records unchanged and is not rejected (R2-D1). |
| 2 | D74 — install/update receiver behavior must be proven from receiver policy | RF return §§2–4 and EV E4 claim clean-receiver preservation | **No:** return verification observes the exact init/update policies, unchanged receiver bytes, and a preservation-to-overwrite mutant that changes the derived result and fails validation. |
| 3 | D52 — Evidence uses `VERIFIED / DEFERRED / BLOCKED / N/A` | RF return §§2–4 and EV E5 claim the fixed vocabulary | **No:** every E1 and E-accounting Result row exposes exactly those four statuses; `INVALID` remains confined to accounting detail, and a fifth-status mutant is rejected. |

## Checkpoint

**Self-check:**
- [x] Every checklist row has pass-2 evidence, and each failure points to R2-D1.
- [x] Purpose was reread separately from the frozen master-HL baseline and Project North Star; the quoted clause and concrete harm are stated above.
- [x] Design soundness was judged independently from purpose alignment.
- [x] Evidence existence and evidence sufficiency were judged separately.
- [x] The Coordinator's §8 debt ruling is terminal; no debt remains `pending — coordinator`.
- [x] RF §§7–9 and the return additions were checked for presence and quality.
- [x] KNOWLEDGE.md was cross-referenced; the two original contradictions are closed and D73/D75 remains contradicted only by the newly observed semantic guard gap.
- [x] No implementation, TS, RF, or EV artifact was edited.

Pass 2 stage complete: YES

# Pass 3 — Return Judge

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | Return Verify R3-V1–R3-V6 independently establishes AC-1 through AC-8: the fixed accounting result is 29 `VALUE` files and 984 touched text LOC (663 additions, 321 deletions), the candidate has exactly four approved `VALUE` paths plus one approved `ASSURANCE` path, all return defects are closed, and the full regression and hygiene gates pass. |
| 2 | (a) Purpose Check; (b) Design soundness | ✅ | **(a) Aligned:** frozen master-HL §1 requires that “Planning, execution, and review use one reproducible accounting contract”; the concrete harm avoided is role-dependent or self-invalidating totals that cause false RF/REVIEW correction rounds. The result remains confined to that purpose. **(b) Sound:** one canonical source supplies three uniquely addressed semantic ranges, the planner consumes them directly, the complete approved classifications/examples/precedence rules are present, and live source-derived projections plus meaning-changing mutants prove the route rather than restating it. |
| 3 | Debt disposed | ✅ | REVIEW §8 contains the Coordinator's terminal ruling for the sole pre-existing RDP journal observation: `not material — owed and forbidden to pay in this phase`, grounded in HC-1 M2 and immutable-journal trace integrity. The stale summary wording in REVIEW §5 is synchronized to that already-issued ruling during Decide; this creates no new ruling. No pass-3 debt exists. |
| 4 | Style & standards | ✅ | Canonical naming and section structure hold; all six canonical workflows equal their twelve adapter copies byte-for-byte; the EV form exposes exactly the four permitted statuses; init/update receiver behavior is explicit and preserving; D75 is met by unique routing and source-derived, mutation-sensitive checks without a second runtime authority. |
| 5 | Observations collected | ✅ | The cumulative RF §6 retains the one reproduced, pre-existing RDP journal-summary overflow (123 code points versus 120). It remains unchanged, is governed by the terminal §8 ruling, and return verification found no new observation. |
| 6 | RF completeness (§§7–9) | ✅ | RF §§7–9 and their return additions are present and credible: no Fact Candidates or Strategic Insights are claimed, the diagram remains relevant, and pass-3 evidence confirms the corrected accounting and planner authority flow. |
| 7 | Evidence completeness — does the evidence exist? | ✅ | Twelve logical evidence items exist and are populated: E1–E7, E-accounting, the three pass-1 return findings, and R2-D1. Each material TS claim and both return rounds have command-backed evidence. |
| 8 | Evidence sufficiency — does the evidence establish the claim? | ✅ | Independent replay established the raw Git arithmetic and immutable membership, exact lineage/timing, live canonical projection, adverse semantic mutants, receiver-preservation mutant, fixed EV vocabulary mutant, adapter equality, HC-1, citation resolution, and the full test suites. The judgment does not depend only on green aggregate tests. |
| 9 | Backward compatibility | ✅ | Existing `/tfw-plan` consumers receive the full canonical contract through the three exact ranges; configuration migration and init/update receiver policies preserve existing projects and histories; all active adapters are exact; no foreign corpus or historical task artifact changed. |
| 10 | Safety | ✅ | Baseline→Candidate contains no secret, destructive behavior, binary ambiguity, protected historical rewrite, unapproved implementation path, or HC-1 violation. Candidate→HEAD changes are TRACE only, and the approved TS is byte-identical to its approval commit. |

Rows 7 and 8 remain separate: all required evidence exists, and its sufficiency is established independently through direct source projections, raw Git measurements, and adverse mutants in addition to aggregate regression suites.

## Purpose Check — row 2 clause (a)

The contract baseline is `174e660bd75d3ad978584a8e1f59d6b22fd4f44f`. Its frozen §1 names the governing requirement and the concrete correction-loop harm; frozen §§3–7 require the four semantic classes, cross-domain examples, precedence, fixed Baseline→Candidate accounting, deterministic pre-work selectors, prohibition of freehand subtraction, two measures, and bounded authority. The Project North Star independently requires purposeful, human-governed, inspectable continuation and rejects activity that obscures purpose or authority. The delivered result supplies the smallest complete coherent mechanism for that purpose: one authority, selective exact reads, synchronized consumers, and structural proof. It adds no adjacent deliverable, does not defer a more proper home, and introduces no material purpose issue.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D73/D75 — selective consumers need uniquely addressed canonical authority and source-derived, mutation-sensitive proof | RF pass-3 return and EV assert that the planner contract is complete, routed from canonical sources, and guarded against semantic drift | **No:** all three exact canonical ranges are loaded; the live projection contains every approved class, example, ambiguity rule, accounting rule, and protected authority boundary; omission and meaning-reversal mutants change the projection and are rejected. |
| 2 | D74 — install/update receiver behavior must be proven from receiver policy | RF and EV claim exact clean-receiver preservation | **No:** parsed init/update policy, byte-preserving controlled runs, and an overwrite mutant independently reproduce the claim. |
| 3 | D52 — Evidence uses `VERIFIED / DEFERRED / BLOCKED / N/A` | RF and EV claim the fixed vocabulary | **No:** both E1 and E-accounting Result surfaces expose exactly the four statuses; `INVALID` is confined to accounting detail, and a fifth-status mutant is rejected. |
| 4 | D43/F43 and D67 — canonical ownership and compression must preserve behavior | RF claims one canonical semantic authority with exact synchronized consumers | **No:** runtime searches find no competing authority, adapter copies are exact, and compression retains the full approved behavior under source-derived tests. |

## Checkpoint

**Self-check:**
- [x] Every checklist row has pass-3 evidence; no universal check is skipped.
- [x] Purpose was reread separately from the frozen master-HL baseline and Project North Star, with the controlling clause and concrete harm stated above.
- [x] Design soundness was judged independently from purpose alignment.
- [x] Evidence existence and evidence sufficiency were judged separately.
- [x] The Coordinator's §8 debt ruling is terminal; Decide only synchronizes the stale §5 summary to that existing ruling.
- [x] RF §§7–9 and all cumulative return additions were checked for presence and quality.
- [x] KNOWLEDGE.md was cross-referenced; all previously material contradictions are closed.
- [x] No implementation, TS, RF, or EV artifact was edited.

Pass 3 stage complete: YES
