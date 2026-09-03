# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. The evidence from Verify controls the ruling.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | Verify D1 breaches TS AC-1 and AC-6; D2 breaches AC-5 and leaves AC-2's G4 gate unestablished; D3 breaches the one-authority/exact-path requirements of AC-2 and AC-4. |
| 2 | Purpose Check + design soundness | ❌ | **(a) Aligned:** master HL §1 at baseline `2728dae` requires “the smallest sufficient, role-specific context” and NS1 protects purposeful, inspectable continuation; no excess or phase deferral was shipped, and the concrete harm at stake is mandatory irrelevant context crowding out task reasoning. **(b) Unsound as delivered:** static declared edges and fixed expected outcomes cannot detect a live bootstrap or semantic regression, which is exactly the harm D1/D2 reproduce. This is a repairable implementation/evidence defect, not `not fit for purpose` and not a contract defect. |
| 3 | Debt disposed | ✅ | REVIEW §5 contains the one RF observation as `pending — coordinator`, the legal waiting state. It proposes `not material — owed and forbidden to pay`, names the persistent red task gate as the consequence, and cites TS AC-6/§2 as the bar. It keeps the phase open until the Coordinator rules. |
| 4 | Style & standards | ✅ | All 49 candidate paths match authorized scope/trace categories; naming and reference grammar hold; `git diff --check` is clean; no candidate or prior trace was edited by the Reviewer. |
| 5 | Observations collected | ✅ | The RF observation is real: `--check tasks` reproduces 123 code points against 120. D1-D3 are material acceptance findings and appear in §4 rather than being diluted into debt. |
| 6 | RF completeness (§7-9) | ✅ | RF contains §7 Fact Candidates (“No fact candidates”), §8 Strategic Insights (“No strategic insights”), and a useful §9 topology diagram. |
| 7 | Evidence completeness — does it exist? | ✅ | EV has six valid rows and all four raw evidence companions exist; no evidence reference is missing. |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | Green pytest output proves the code under test passed, but E1/E2/E5/E6 test declared topology/outcomes rather than the active root and candidate behavior. Corrected counts and the nonexistent-root probe directly refute sufficiency. |
| 9 | Backward compatibility | ❌ | The active runtime convention still sends Antigravity consumers to singular `.agent/rules`, while the new manifest and adapter contract install plural `.agents/*`; a consumer following the runtime authority can miss the installed command surface (Verify D3). |
| 10 | Safety | ✅ | No secrets, credentials, deployment, network mutation, destructive command, merge, rebase, cherry-pick, or push is involved. Repository writes are confined to review traces and the required phase transition. |

## Purpose Check — row 2 clause (a)

**Aligned.** The result is aimed at the frozen master-HL clause “Every TFW role enters each lifecycle checkpoint with the smallest sufficient, role-specific context” and NS1's requirement that an authorized successor can inspect authority and continue. The material harm is attention lost to mandatory irrelevant inputs and false confidence from an audit that omits them. No adjacent product, deferred phase deliverable, or internally inconsistent reference clause was introduced. D1-D3 are repairable failures to deliver the approved purpose, so the route is 🔄 REVISE rather than ❌ REJECT.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | Architecture Map `Adapters` row says `config.md` carries the full copy map/drift check and names singular `.agent/workflows` | RF says the new manifest is the one map and Antigravity uses plural `.agents/*` | Yes — stale project documentation. It is not an extra repair proposal in this verdict because §§1-3 are owned by the post-approval `/tfw-docs` step; REVIEW is not approved and the Reviewer cannot write them. |
| 2 | D23/D25/D61, D63/D68/D72, D54, D69 | HL/ONB claim progressive disclosure, protected lifecycle semantics, exact commands, and full identifier behavior | No — every cited decision exists and matches its asserted use. |

RF Fact Candidates need no challenge: the section explicitly reports none, and every review finding here is mechanically discoverable rather than Human-Only knowledge.

## Checkpoint

**Self-check:**
- [x] Every checklist item has specific evidence?
- [x] No N/A row or silent skip?
- [x] Row 2(a) answered against the contract baseline and Project North Star, with clause and harm?
- [x] Rows 7 and 8 answered separately?
- [x] Verify findings cited in the DoD assessment?
- [x] Row 3 checks the pending disposition, existing phase, consequence, and barring clauses?
- [x] RF §7-9 checked for presence and quality?
- [x] KNOWLEDGE.md cross-referenced and the stale row documented?
- [x] Fact Candidates reviewed?

Stage complete: YES
