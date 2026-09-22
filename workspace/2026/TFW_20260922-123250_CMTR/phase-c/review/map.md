# Map — "What must be true?"
> **Mindset:** Experienced newcomer. Understand the accepted result before judging it.
> **Test:** "Can I name the material claims, harms, boundaries, evidence identities and limits?"
> RF: [RF Phase C](../RF__phase-c__minimal_core_integration_and_live_pilot.md)
> TS: [TS Phase C](../TS__phase-c__minimal_core_integration_and_live_pilot.md)

## Understanding

Phase C must forward-correct the rejected tier/profile/self-calibration design in exactly four
provider-neutral core files, place a concise five-step launch-selection rule at the real Coordinator
dispatch point, and remove two decorative template fields. Acceptance depends on semantic fidelity,
purpose and evidence honesty—not the file/LOC counts themselves—and remains bounded to Candidate
`e29ae633814c47cc41c82afab6d5359cd66f78ca` against baseline `e819908`.

## Accepted Claims and Boundaries

| ID | Layer | Accepted claim / authority boundary | Risk or concrete harm | Affected behavior / dependencies | Relevant environment | Oracle / authority | Evidence identity (`subject@revision`, source) | Required? |
|---|---|---|---|---|---|---|---|---|
| C1 | VALUE | `Launch selection` preserves the accepted five-step meaning: prerequisites; quality floor; separate model/effort and lower option; native-or-two-line application; five distinct evidence layers and next-launch correction. | Compression can silently remove authority, return, assurance timing, comparison or failure-cause semantics and permit an unsafe or decorative launch choice. | Coordinator launch decision; provider-neutral policy; Plan dispatch. Depends on the binding TS rendering and iteration-4 D15–D21. | Active repository core at Candidate. | TS AC-1/AC-2/§6; owner acceptance; semantic inspection against iter4 RES. | `.tfw/conventions.md@e29ae633`; `.tfw/workflows/plan.md@e29ae633`; TS/RES sources. | yes |
| C2 | VALUE | Plan applies launch selection to every actual role launch while retaining the coordination selection, human gate, dispatch, authority, addressability, return, title/readback and Role Lock controls needed by Plan Step 5. | A shortened workflow can preserve the headline rule yet break reliable provisioning, activation or vertical return. | `/tfw-plan` coordination and all downstream role launches. | Codex and provider-neutral Plan workflow. | TS AC-2/DoF; baseline-to-Candidate semantic diff; workflow invariants. | `.tfw/workflows/plan.md@e29ae633`; `.tfw/workflows/plan.md@e819908`; TS. | yes |
| C3 | VALUE | No active tier/profile/self-calibration/static-model residue remains; HL/TS decorative profile fields are deleted without replacement. | Stale or duplicate mechanisms would make the new rule ambiguous and reintroduce non-behavioral control. | Core convention, Plan, HL and TS authoring. | Four approved VALUE files. | TS AC-3/AC-4; focused active-text search and template inspection. | Four VALUE paths `@e29ae633`; baseline diff. | yes |
| C4 | VALUE | The compact naming and prose remain usable: heading `Launch selection`, Plan ≤1,400 words, owner-facing fallback exactly two lines, no research label in core. | A technically complete but verbose/unclear policy would fail the owner-approved product shape and make launch choices harder to apply. | Human-readable launch guidance and Plan operation. | Rendered Markdown/current repository. | Owner acceptance; TS AC-4/§6/DoF; independent reading and word count. | `.tfw/conventions.md@e29ae633`; `.tfw/workflows/plan.md@e29ae633`. | yes |
| C5 | ASSURANCE | Evidence claims distinguish requested settings, effective settings when observable, delivery, outcome and material rework; successful delivery is not presented as effective settings, sufficiency or minimum. | Proxy evidence can falsely attribute outcome quality or economy to an unobserved model/effort pair. | Phase C Executor and Reviewer pilot claims; future launch evidence. | Codex task route and durable journals/RF/EV. | TS AC-5; HL DoD/DoF; iter4 D18–D21; journal evidence. | Executor dispatch/outcome journals `@f4a970a`; Reviewer dispatch `@f4a970a`; EV/RF `@f4a970a`. | yes |
| C6 | ASSURANCE | Existing documentation/integration and blob-boundary tests pass for the accepted Candidate; no new permanent test was added and test/count evidence is not treated as product quality. | Broken generators/integration can invalidate the framework, while proxy tests can create false assurance and maintenance burden. | Repository documentation generation, integration checks and blob boundary. | Windows/Python repository environment. | TS AC-5; rerun exact configured suite; changed-file history. | `e29ae633` implementation plus independently rerun test output; EV E5. | yes |
| C7 | TRACE | Candidate changes exactly the four approved VALUE paths, all MODIFY, with 39 additions + 50 deletions = 89 touched text LOC; no later VALUE commit changes the accepted subject. | Scope creep, wrong baseline or moving Candidate makes the reviewed result unauthorised or irreproducible. | Accepted-result identity and accounting. | Git object database/current worktree. | Approved TS accounting contract and NUL-safe Git reproduction. | `e819908..e29ae633`; TS approval `d5a953f`; RF/EV. | yes |
| C8 | TRACE | Owner-approved A2, Phase C TS, distinct Executor/Reviewer units, exact dispatch and `coordinator_route` authorize this review; Reviewer remains independent and returns only to the Coordinator. | Missing or crossed authority would invalidate the verdict even if implementation is sound. | Human acceptance authority, role independence, continuation. | Codex task topology and durable task state. | Frozen HL §4.1/§12 A2; phase status/journals; activation envelope. | A2 `@2c72ec8`; coordination `@addb2e7`; review dispatch `@f4a970a`; current Reviewer unit. | yes |
| C9 | VALUE / TRACE | No release, push, adapter/provider claim, external effect, history rewrite or permanent-test addition occurred; ordinary security surface is unchanged. | Unauthorized external or cross-platform claims would exceed the human mandate; hidden executable/security change would escape this documentation review. | Repository history, changed paths and outward effects. | Local Git/worktree only. | TS out-of-scope/DoF; exact changed-file history; dispatch reservation. | `e819908..f4a970a`; task journals. | yes |

## TS ↔ RF Alignment

| TS requirement | RF claim | Claim IDs | Aligned? |
|---|---|---|---|
| AC-1 concise provider-neutral launch rule | RF §§1–3 marks AC-1 complete and names the five-part evidence boundary. | C1, C4, C5 | ⚠️ verify semantics |
| AC-2 enforcement at actual dispatch | RF §3 defers Reviewer launch/outcome; Plan and Executor dispatch are claimed. Reviewer dispatch now exists. | C1, C2, C5, C8 | ⚠️ partial until Verify |
| AC-3 decorative profile removal | RF §§1–4 claims both template fields and legacy active text removed. | C3 | ⚠️ verify search/diff |
| AC-4 naming, length and exact boundary | RF §§1–4 claims 1,390 words, four files and 89 touched LOC. | C4, C7 | ⚠️ verify reproduction |
| AC-5 purpose assurance without proxy tests | RF §§3–5 reports 14 passing existing tests and defers independent REVIEW. | C5, C6, C9 | ⚠️ partial until this REVIEW |
| TS DoF and frozen HL DoD/DoF | RF says no deviations or observations and bounds effective/minimum claims. | C1–C9 | ⚠️ independently judge |

## Verification Selection

| Claim IDs | Planned check or reusable evidence | Why this depth | Known gap or limit |
|---|---|---|---|
| C1, C2, C4 | Inspect complete Candidate versions and full baseline diff of conventions/Plan; compare each shortened Plan passage to baseline and the binding TS/iter4 semantics; count Plan words. | Aggressive compression can cause a material semantic loss not caught by textual search or tests. | Reviewer can judge wording and preserved controls, not prove future operator behavior. |
| C3 | Inspect both templates and run focused searches over the four active files, distinguishing historical/task text from active core. | Removal is exact and mechanically checkable, but false positives need semantic review. | Repository-wide historical mentions are expected and not active residue. |
| C5 | Audit dispatch, gate, RF/EV and current Reviewer launch claims against the five evidence layers; search active text and Phase C records for effective/minimum/savings/provider overclaims. | Evidence-layer conflation directly violates purpose and could turn a pilot into false model-quality guidance. | Effective backend settings and an equivalent-work lower-resource comparison remain unavailable by design. |
| C6 | Rerun `python -m pytest tools/tests/ docs/scripts/ -q`, inspect whether Candidate adds tests, and classify what the tests actually protect. | Existing generator/integration/blob checks are required compatibility evidence, not semantic proof. | A green suite cannot establish launch-selection purpose or semantic fidelity. |
| C7, C9 | Reproduce exact NUL-safe name-status/numstat with the literal selector; inspect commits from Candidate through delivered source and exact full worktree status. | Accepted-result identity and authorized boundary are mandatory floors. | Local Git proves repository state, not absence of unrecorded external effects; dispatch reserves those effects. |
| C8 | Validate current phase state, A2/TS approval, dispatch destination/title, current source commit, role independence and exact Coordinator return path. | A valid implementation cannot cure invalid authority or crossed role topology. | Effective backend model/effort and exactly-once transport are unobservable; no claim will rely on them. |
| C1–C9 | Read relevant PV P0–P4 and P5–P7 citations at Verify, then judge frozen Goal/Value and North Star separately. | Purpose assurance must not collapse into TS conformance. | Human acceptance remains with the owner; Reviewer can only issue the workflow verdict. |

## Deviations from TS

No established deviation at Map. RF correctly leaves AC-2 and AC-5 pending for the independent
Reviewer; those are open assurance steps, not implementation deviations. Verify must determine
whether the final Reviewer dispatch closes the live-pilot boundary and whether any compressed Plan
passage lost material meaning.

## Checkpoint

**Self-check:**
- [x] Read RF §§1–5, governing TS AC/DoF, HL purpose/principles, ONB and referenced predecessors?
- [x] Mapped every material accepted claim and the mandatory safety/security, authority and result-identity boundaries?
- [x] Bound each claim to affected behavior/dependencies, environment, oracle/authority and exact evidence identity?
- [x] Recorded a replayable verification selection and every known gap or limit?
- [x] Avoided classifying by filename, discrepancy count or artifact volume?

Stage complete: YES
