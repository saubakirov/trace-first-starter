# RES — Iteration 4: Adversarial test of per-launch minimum-sufficiency claims

> **Date:** 2026-09-22
> **Author:** Researcher unit `codex:thread:local:01a0c8bf-5bbb-75f1-ac97-b8e640b531ae`
> **Status:** Iteration complete — `SUFFICIENT` recommended
> **Parent HL:** [HL-TFW_20260922-123250_CMTR](../../HL-TFW_20260922-123250_CMTR.md)
> **Mode:** Pipeline; focused, one OODA pass per stage
> **Producer unit:** `codex:thread:local:01a0c8bf-5bbb-75f1-ac97-b8e640b531ae`
> **Parent Coordinator:** `codex:thread:local:01a0c400-3e48-7422-bb86-3b34fe177aa5`
> **Activation / dispatch source:** delegated `/tfw-research TFW_20260922-123250_CMTR Phase B`, iteration 4; `phase-b/journal/20260922-155350__dispatch__9e2f.md` at Coordinator commit `46aacbd96c0f360f0aa2736c12623153be57070d`
> **Coordination authority:** owner-approved A2 at `2c72ec8c6b0b21269caf95b707d26c631be5df52`; re-frozen HL at `addb2e707dd9f271b7bf1287617a8b93b8d72cb0`
> **Synthesis authority:** `journal/20260922-162808__gate_answer__5a71.md` at Coordinator commit `59f1222a27b8839056311ab46df4df62c353e5b5`
> **Originating proposer:** `none`

## Research Context

Iteration 4 independently attacked iteration 3's provider-neutral selection rule. It asked whether the rule actually distinguishes the requested `gpt-5.6-sol` + `high` launch from a cheaper plausible `gpt-5.6-sol` + `medium` candidate, whether its evidence claims survive stricter separation, and what Phase C could observe that would falsify rather than merely illustrate the policy.

The iteration did not run provider pilots, launch helpers, compare task transcripts, or mutate the HL, TS, status, workflow, adapter, core, or Phase A history. The iteration-3 Astra/high task and iteration-4 Sol/high task performed different work and are not equivalent-work evidence.

Accepted stage chain:

| Stage | Source commit | Coordinator gate |
|---|---|---|
| Briefing | `b6bdd7422bd3fc94f7d9073fc52de6a1daf440cc`, corrected at `cd7f4b817b26f7890cc17b997deccb30b7a96354` | accepted at `2e43e5045704c2af945c95540604d55136f78391` |
| Gather | `bf7377610715a8659e1f270e120376ab5a3e31cd` | accepted at `caf096a415193492a627a5a136d5745e58aa17d3` |
| Extract | `5af3d3535769237801f6959435fcf8af9277d475` | accepted at `02f6a02bd19048787e8764c24fcbe5c1d10da23d` |
| Challenge | `f24ac9a52cd70da9388ea29205fed26af2372339` | synthesis authorized at `59f1222a27b8839056311ab46df4df62c353e5b5` |

## Briefing

The research tested four related claims:

1. Whether uncertainty, dependency breadth, oracle strength, and consequence/reversibility form a usable decision rule or only a vocabulary for post hoc justification.
2. Whether the current evidence distinguishes requested settings, effective settings, addressed delivery, outcome, and material rework.
3. Whether Codex, Antigravity CLI/IDE, Claude Code, and Claude Desktop claims stay within the evidence available on each exact surface.
4. Which prospective Phase C outcomes would support, weaken, falsify, or leave undecidable a per-launch selection claim.

The investigation used durable dispatch/gate records, the current Codex task contract, read-only installed Antigravity and Claude surfaces, provider-native documentation, and applicable project knowledge. It kept Sol/medium counterfactual: no result, quality, or economy was attributed to an unexecuted launch.

## Decisions

### D15 — Feasibility is a hard gate, not a quality factor

Before model or effort selection, the launch must have the required context, tools, current native availability, authority, addressable unit, and exact return route. More model capability or reasoning effort cannot compensate for a missing prerequisite. An honest no-launch return that names the missing prerequisite is a valid policy result.

### D16 — Consequence and oracle timing determine the safe selection posture

When a material failure is hard to reverse and the oracle is weak or late, selection should be conservative. When work is reversible and a strong, timely oracle exists, an adjacent lower candidate with a predeclared escalation trigger remains feasible. This fork prevents both default-max selection and unsafe lower-first experimentation.

### D17 — The adjacent-lower candidate must be confronted explicitly

For the exact next launch, the rationale must name the adjacent lower feasible pair and either:

- predict the material quality-floor failure that excludes it; or
- state that the selected pair is provisional because the boundary is not evidenced.

Iteration 4's facts justify the downgrade from iteration-3 Astra/high to iteration-4 Sol/high as a bounded rationale, but they do not distinguish Sol/high from Sol/medium. Both can be rationalized from the same four factors. Sol/medium therefore remains an untested adjacent candidate, not a sufficient or insufficient pair.

### D18 — Evidence layers set claim ceilings

Record these fields separately:

| Layer | Meaning | Iteration-4 Codex status |
|---|---|---|
| Requested | exact creation arguments and rationale | observed: Sol + high |
| Effective | resolved model and effort after fallback, substitution, or policy | unavailable on the current task surface |
| Delivered | distinct address, exact activation, bounded wait/return | observed |
| Outcome | result judged against the exact work oracle | stage artifacts accepted through Challenge |
| Material rework | correction that changes a material claim or acceptance state | observed; causes include context selection and reasoning/follow-through |

Missing effective-setting readback need not prevent an authorized launch, but it caps attribution. The defensible wording is “the delivered unit produced an accepted result under this oracle,” not “the requested pair proved sufficient.” Completion, acceptance, or rework cannot be substituted for effective-setting evidence or minimum-cost evidence.

### D19 — “Lowest-resource currently justified candidate” is an operational evidence label inside A2

Use **lowest-resource currently justified candidate** to label a per-launch choice whose adjacent lower boundary is not yet empirically resolved. This is an operational qualifier for dispatch rationale and evidence state. It does not replace, weaken, or redefine the frozen A2 objective of choosing the **minimum sufficient / least-cost sufficient** pair.

Replacing the frozen target with “currently justified” as a weaker terminal requirement would be a frozen `SUPERSEDE` amendment. Iteration 4 does not propose that change. The label instead prevents an unevidenced provisional choice from being misreported as the proven minimum.

### D20 — Comparative evidence is bounded, not universal

The smallest useful prospective diagnostic holds model, work packet, authority, sources, tools, and oracle constant while comparing Sol/high with Sol/medium in separate visible tasks. Pair labels should be hidden from the independent output judge, output order randomized, and acceptance criteria declared before results.

Such a diagnostic can show that high was not necessary for that packet when medium passes the same oracle with no greater material rework, or support a packet-specific boundary when medium fails on the exact predicted failure and high passes. It cannot prove a global minimum because generation is variable, tasks differ in timing and hidden state, effective Codex settings and quota economy remain unavailable, and one packet cannot represent future work.

### D21 — Provider-neutral policy stops at provider-specific evidence ceilings

| Surface | Supported now | Not supported now |
|---|---|---|
| Codex desktop tasks | requested parameters, distinct task address, activation, bounded wait/return, outcome and rework | effective pair, actual task economy, minimum sufficiency |
| Antigravity CLI 1.2.8 | dated live roster; model/effort controls; candidate conversation/status/result/usage mechanics | completed TFW role chain or effective-setting pilot |
| Antigravity IDE | no current launch-readiness claim | selector/account roster, separate address, exact return, effective readback |
| Claude Code 2.1.278 | installed controls and documented candidate session/readback mechanics | live account availability, substitution/clamp result, completed TFW role chain |
| Claude Desktop | no current launch-readiness claim | selector/account roster, separate address, exact return, effective readback |

Provider, CLI, IDE, Code, and Desktop names are not interchangeable contracts. A working binding requires current evidence from the exact claimed surface.

### D22 — Phase B research is sufficient for planning, not for an optimum claim

Iteration 4 recommends `SUFFICIENT` for Phase B research. Two independent iterations now provide a falsifiable policy shape, provider-specific claim ceilings, real Codex dispatch/outcome/rework evidence, and concrete Phase C observations. This recommendation means the Coordinator can route the result to `/tfw-plan`; it does not accept Phase B, establish an empirically minimum pair, prove effective Codex settings, or declare Antigravity/Claude modes working.

D15–D20 narrow iteration-3 D9–D12 by adding hard prerequisites, a consequence/oracle fork, an adjacent-lower discriminator, and evidence-qualified wording. D21 preserves and tightens iteration-3 D13–D14. No frozen A2 decision is superseded.

## Open Questions

| # | Question | Resolution / remaining boundary |
|---|---|---|
| Q1 | What exact threshold distinguishes an adjacent lower pair? | No empirical threshold exists yet. Record a predicted material failure or call the choice provisional; Phase C may run a bounded comparison if it needs a stronger claim. |
| Q2 | How can requested settings be separated from effective settings? | Codex currently exposes the request and delivery but not the effective pair. Claude Code documents prospective readback; Antigravity CLI exposes candidate initialization/result fields. Each surface must be tested natively before an applied-pair claim. |
| Q3 | What can Phase C falsify? | It can falsify a rationale, a packet-specific necessity claim, an adapter/readback claim, a working binding claim, or fitness for purpose. It cannot establish a global minimum from one successful launch. |

## Hypotheses

| # | Hypothesis | Iteration-4 status |
|---|---|---|
| H1 | Quality floor → least-resource-sufficient is more robust than role-based tiers. | **partial** — tier shortcuts and default-max rationales are analytically rejected; no equivalent-work outcome comparison establishes the lower boundary. |
| H2 | Selecting model capability and reasoning effort separately prevents errors hidden by one profile. | **partial** — native contracts and the Sol/high versus Sol/medium counterfactual show distinct controls; no causal field comparison was run. |
| H3 | Applying the choice at dispatch is more reliable than a frozen HL/TS profile and needs no permanent artifact. | **partial** — real Codex parameter passing, addressability, delivery, outcome, and rework are durable; the narrowed prospective rule is unpiloted and effective settings remain unobserved. |
| H4 | Each claimed platform has an authoritative availability source and an exact autonomous or owner-assisted route. | **partial** — Codex's route is proven; Antigravity CLI and Claude Code have bounded candidate mechanics; Antigravity IDE, Claude Desktop, account selectors, and foreign-provider chains remain unpiloted. |

## HL Update Recommendations

### Refinements

These are free-section refinements for Coordinator consideration; they do not edit the HL in this unit.

| HL section | Recommended refinement | Evidence |
|---|---|---|
| §2 Current state | Record that Codex requested-parameter dispatch and return work, while effective settings and minimum sufficiency remain unobserved; record iteration-4's context-selection and reasoning/follow-through corrections. | D18; iteration-4 Briefing return and accepted stages |
| §7.2 Evidence | Add iteration-4 stage/gate commits, the 2026-09-22 current tool observations, and provider-native documentation with exact surface/date boundaries. | Accepted stage chain; D21 |
| §8 Dependencies | Make current native inventory, a valid separate-unit/return route, a predeclared oracle, and provider-specific readback where claimed explicit Phase C dependencies. | D15, D18, D21 |
| §9 Risks | Add post hoc default-max rationale, stale source/version selection, requested≠effective settings, single-run overclaim, judge bias, and cross-surface evidence transfer. | D16–D21 |
| §10 Research Case | Update H1–H4 to the statuses above; record the narrowed contract, claim ceilings, and Phase C falsifiers. | D15–D22 |

### Amendment Proposals

No amendment proposals.

“Lowest-resource currently justified candidate” is classified as an operational evidence label within approved A2, not as a replacement for the frozen minimum-sufficient target. Any future attempt to make that phrase the weaker terminal goal would require an explicit `SUPERSEDE` proposal and owner verdict.

## Fact Candidates

No fact candidates. The iteration introduced no new human-only fact or preference; Coordinator dispatches and gates supplied authority and artifact state rather than new owner knowledge.

## Strategic Insights

No strategic insights. All material conclusions are researcher-derived findings or refinements, not new human input.

## Findings Map

```text
exact next launch
        |
        v
hard feasibility gate
context · tools · native availability · authority · address · return
        |
        +-- missing --> honest no-launch + exact prerequisite
        |
        v
quality floor
uncertainty · dependencies · oracle timing/strength · consequence/reversibility
        |
        v
lowest-resource currently justified candidate
        |
        +-- adjacent lower excluded by predicted material failure
        |                         or
        +-- choice explicitly provisional
        |
        v
dispatch evidence, kept separate
requested -> effective (if observable) -> delivery -> outcome -> material rework
        |
        v
classify failure cause
context/tool/source · binding/readback · capability/effort · oracle
        |
        v
correct the next launch by failure type

claim ceiling:
requested/delivered != applied != sufficient != minimum sufficient
```

## Iteration Status

**Iteration:** 4 of 4 minimum / 5 maximum  
**Recommendation:** [x] `SUFFICIENT`  [ ] `MORE NEEDED`  [ ] `BLOCKED`

The research question is sufficiently bounded for planning. A fifth research iteration is not required before Phase C unless the Coordinator identifies a new unresolved research question. Empirical questions now belong to authorized Phase C work, not another paper-only loop.

| Open thread carried forward | Phase C obligation |
|---|---|
| Rule integration | Integrate the narrowed gate at the actual dispatch point; remove Phase A tier/static-profile/self-calibration effects without creating a permanent model roster. |
| Codex outcome evidence | Run at least one bounded prospective launch under the rule. If a minimum/necessity claim is required, use a C5-class adjacent-lower same-packet diagnostic with a predeclared, independent/blinded oracle; otherwise keep the choice provisional. |
| Provider bindings | For each mode claimed working, use the current exact surface to prove roster/selector, explicit selection, separate visible unit, exact return, and effective readback where the surface supports it. Keep unpiloted modes bounded or unavailable. |
| Correction loop | Record requested, effective when observable, delivery, outcome, and material rework; classify the failure before changing model or effort. |
| Purpose assurance | Independently review implementation and results against the frozen HL/North Star. Do not add a permanent eval suite or tests solely to satisfy evidence counts. |

Phase C should interpret prospective outcomes as follows:

| Observation | Supported conclusion | Forbidden overclaim |
|---|---|---|
| Selected task passes first try | delivered unit met the packet oracle | minimum or future robustness |
| Result passes after material source/context correction | strong oracle caught a recoverable context defect | stronger model would have prevented it |
| Sol/medium passes the same blinded oracle with no more material rework | high was not demonstrably necessary for that packet | universal sufficiency or exact savings |
| Medium fails and high passes on the predeclared predicted failure | bounded packet-specific high/medium boundary | provider-wide invariant |
| Both fail for the same missing source/tool/context | prerequisite dominates model choice | escalate model by default |
| Requested/readback mismatch | binding or readback defect | requested pair's quality caused the outcome |
| Surface lacks roster, separate unit, exact return, or required readback | working binding claim fails for that tested surface | provider-wide impossibility |
| Polished output violates frozen HL/North Star | not fit for TFW purpose | formal completion equals sufficiency |

## Conclusion

Iteration 4 falsified the idea that four named factors alone constitute a discriminating selection rule. The rule survives only after adding a hard feasibility gate, a consequence/oracle fork, explicit treatment of the adjacent lower feasible pair, non-substitutable evidence fields, and an honest epistemic label.

The strongest defensible compact contract is:

> For the exact next launch, first require the needed context, tools, native route, authority, and return. Then set the quality floor from uncertainty, dependencies, oracle timing/strength, and consequence/reversibility. Choose the lowest-resource pair currently justified on that surface; for the adjacent lower feasible pair, record either the predicted material failure that excludes it or that the choice is provisional. Record requested, effective when observable, delivery, outcome, and material rework separately. Correct the next launch by failure type. Claim minimum only from bounded comparative outcome and actual-surface economy; otherwise say unknown.

This preserves A2's minimum-sufficiency goal while refusing to call an untested provisional selection the minimum. The principal limitations are explicit: no equivalent-work pilot ran, effective Codex settings and completed-task economy are unavailable, one bounded comparison could not prove a global optimum, and foreign-provider working modes remain untested. Those are now exact Phase C obligations rather than unresolved policy ambiguity.

## Material handover

- **Producer unit:** Researcher `codex:thread:local:01a0c8bf-5bbb-75f1-ac97-b8e640b531ae`.
- **Authority epoch:** owner-approved A2 at `2c72ec8c6b0b21269caf95b707d26c631be5df52`; iteration-4 dispatch at Coordinator commit `46aacbd96c0f360f0aa2736c12623153be57070d`; synthesis gate at `59f1222a27b8839056311ab46df4df62c353e5b5`.
- **Inspected scope:** four accepted iteration-4 stages; iteration-3 RES and durable dispatch/gate records; current HL free-section state; current Codex task contract; read-only installed Antigravity/Claude controls; provider-native model-selection, evaluation, headless, and readback documentation; applicable project knowledge.
- **Materiality:** adds the hard feasibility gate, consequence/oracle fork, adjacent-lower discriminator, five-field evidence record, claim ceilings, provider surface boundaries, Phase C falsifiers, and an explicit operational-versus-frozen classification for “currently justified.”
- **Uncertainty:** no provider pilot or equivalent-work comparison occurred; Codex effective settings and task economy remain unavailable; Antigravity IDE, Claude Desktop, account selectors, and foreign-provider role chains are not launch-ready claims.
- **Decision owner:** the parent Coordinator decides Phase B acceptance and `/tfw-plan` routing; the owner retains A2-reserved decisions. This Researcher neither accepts Phase B nor begins Phase C.
- **Continuation:** use this RES as the Phase B research input to `/tfw-plan`; carry the listed Phase C obligations and claim ceilings into the TS.

---

Research iteration 4 complete. Continue with `/tfw-plan` to classify and plan the accepted research recommendations.
