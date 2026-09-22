# RES — TFW_20260922-123250_CMTR: Per-Launch Model and Reasoning Selection

> **Current filename**: `research/iter3/RES.md`
> **Date**: 2026-09-22
> **Author**: Codex Researcher
> **Status**: RES — Iteration 3 complete; MORE NEEDED
> **Parent HL**: [CMTR](../../HL-TFW_20260922-123250_CMTR.md)
> **Mode**: Pipeline; focused, one OODA pass per stage
> **Producer unit**: `codex:thread:local:01a0c89b-3d1e-7bd1-b8ab-a6376a7607d1`
> **Parent Coordinator**: `codex:thread:local:01a0c400-3e48-7422-bb86-3b34fe177aa5`
> **Activation / dispatch source**: delegated `/tfw-research TFW_20260922-123250_CMTR Phase B`, iteration 3; [dispatch](../../phase-b/journal/20260922-151933__dispatch__4b9e.md) at `f1ab1a03a2038d5b2887e4158c6c78fef58949e0`
> **Coordination authority**: `HL-TFW_20260922-123250_CMTR.md @ addb2e707dd9f271b7bf1287617a8b93b8d72cb0`; owner-approved A2 at `2c72ec8c6b0b21269caf95b707d26c631be5df52`
> **Originating proposer**: `none`
> **Synthesis authority**: [Challenge answer](../../journal/20260922-154336__gate_answer__a19d.md) at `12388d000eeebc475099f9f7d681ffcf52c59ff1`; permits this RES only
> **Repository base**: `839dfb07b90673c630b947de46a1598d21e63a36`

## Research Context

Iteration 3 derives a selection rule after A2 rejected the role-tier strategy. Native observations establish usable parts of the Codex, Antigravity CLI/IDE and Claude Code contracts, while counterexamples separate capability, effort and verification failures. The result is a defensible decision procedure and bounded provider bindings. It is not a validated cost optimizer: this Researcher launch predates the derived rule, foreign-provider role chains were not piloted, and no cheaper alternative was compared on equivalent work.

## Briefing

[Briefing](1_briefing.md) defines the scope; [Gather](2_gather.md) records commands, exact dated rosters and primary sources; [Extract](3_extract.md) derives candidate combinations; [Challenge](4_challenge.md) narrows them and corrects a cross-surface Ultra implication. All four stages were accepted separately by the Coordinator. Producer commits are `d4d52c793df05295706161eb89765df69d8d8d18`, `80648efdd81e170c1098c4966b8024158a386d19`, `9a60b90ec2836147e65f34a9c950d71d57840d81`, and `4308d120a222163b8fe50a14438d2cbb36715213`; exact gate/landing provenance remains in their headers and the synthesis answer.

## Decisions

| # | Research decision | Rationale |
|---|---|---|
| D9 | Assess the next concrete result through uncertainty, dependency breadth, verification strength and error consequence | Small edits can change authority; broad mechanical work can have a strong oracle. Role names and file counts cannot determine sufficient capability |
| D10 | Select capable models first, then sufficient supported effort; compare feasible pairs | Context/tools are hard constraints. Higher effort cannot supply missing capability; a stronger model with lower effort may be a valid candidate |
| D11 | Reuse comparable accepted evidence; otherwise make first-use sufficiency explicitly provisional and verifiable | Neither fluent rationale nor default maximum proves quality. If no defensible choice or assurance exists, return the missing prerequisite |
| D12 | Prefer lower resource only within the justified sufficient set and known cost ordering | Per-token price and model size are not completed-task cost. Unknown economy remains unknown; no savings percentage is claimed |
| D13 | Bind at actual launch using the target surface's current inventory and exact controls | A help flag, general docs page or another surface's roster cannot substitute for target availability. Keep requested parameters, resolved settings and outcome distinct |
| D14 | Record result and material rework in the existing return; adjust the next choice by failure type | Missing facts, capability, follow-through and verification need different remedies. No new standing profile, calculator or artifact is required |

### Compact decision contract

Before each launch, identify the required result and material failure from uncertainty, dependencies, verification and consequence. Choose a capable model, then sufficient supported effort; prefer lower resource among justified sufficient choices. Refresh the target's native options and apply the choice at launch. Record the choice and reason, then the result and material rework. Name unresolved availability, capability or assurance; claim no optimum when cost is unknown. Correct the next choice according to the observed failure.

This is a research proposal within A2, not a new frozen ruling. A stronger first-use reference is justified only by a concrete requirement and useful verification; it is not the default for every uncertainty. A supported provider default or fixed effort can be an explicit per-launch choice. [OpenAI's quality-first selection guidance](https://developers.openai.com/api/docs/guides/model-selection) supports the ordering; [Anthropic's workload-dependent cost evidence](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence) cautions against inferring cost from model price alone. Neither source empirically validates CMTR's rule.

### Provider bindings and evidence boundary

Here **verified** qualifies a specific observation, **unverified** means declared behavior not exercised on this target, and **unavailable** means an observation/control not obtained from this unit's authorized surface. These are not provider-wide labels.

| Surface | Verified here / attributable native evidence | Launch binding | Remaining unverified or unavailable |
|---|---|---|---|
| Codex desktop task tools | Current `create_thread` roster/effort declaration; explicit creation arguments in Coordinator record; ready task, local host, addressed activation/returns and own-title readback | `create_thread` with separate `model` and `thinking`; use the ready `threadId`, exact activation and cursor-based wait. Omission inherits defaults | Effective backend model/effort were not returned; final comparative quality and minimum cost unproved |
| Antigravity CLI 1.2.7 | `agy models` returned a live roster; installed help exposes `--model`, `--effort`, exact conversation continuation and stream formats | Use current listed model/effort variants; flags and `conversation_id` form a candidate native contract | No inference or complete owner-visible TFW chain was run; effective resolution, quota and chain behavior unverified |
| Antigravity IDE 1.107.0 | Installed `chat --help` exposes execution mode but no model/effort flag | Documented owner-operated selector under the conversation prompt | Its live selector, account roster, settings and addressed chain are unavailable here; CLI roster does not prove IDE options |
| Claude Code 2.1.278 | Installed help exposes `--model`, `--effort`, exact session IDs and visible/background session controls | Current `/model` picker and per-model effort options; launch flags or session-only choices; header/`/status` readback | Account roster and resolved settings unavailable here; native TFW chain unpiloted |
| Claude Desktop | No direct inspection | Requires its own selector/session evidence | Code CLI evidence supplies no Desktop contract |

Exact dated identifiers are preserved in Gather rather than repeated as durable recommendations. [Antigravity's headless contract](https://antigravity.google/docs/cli/headless/) and [Claude's model configuration](https://code.claude.com/docs/en/model-config) supply documented mechanics, not account/pilot proof. Logical independence of model and effort is compatible with a provider encoding the pair in one slug. Global effort flags do not establish every pair; silent fallback must not be called successful application of the requested setting.

**Correction carried forward:** Gather's broad Ultra implication is narrowed by Challenge C2. [Surface-specific OpenAI documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents) distinguishes ChatGPT Work's proactive Ultra behavior from local Codex delegation triggered by direct request or applicable instructions. No local Ultra behavior was tested, and its label alone neither proves nor disproves compatibility with the TFW role boundary.

### Real launch and observed outcome

The Coordinator's [supplemental dispatch](../../phase-b/journal/20260922-153956__dispatch__4e6a.md) at `dcc38f964e419eab1b389f31ae3d06dde6973fbd` records actual `create_thread` arguments `model: gpt-6-astra`, `thinking: high`, a separate project worktree and provisioning-only prompt. The first return supplied a temporary `clientThreadId`; later registration/title/wait evidence resolved this unit's ready address before activation. This establishes requested parameter passing and delivery, not effective backend settings.

The observed result is this policy derivation, native inventory/help evidence and accepted stage returns. Material rework was a source-scope correction of the Ultra claim; it does not establish that a different model or more effort was needed. Independent acceptance of the final research and a prospective launch under the rule are still owed. No comparative token, latency or quality experiment occurred.

### Phase C inputs after independent iteration 4

Challenge C5 inspected candidate `92c5ee4bb83271adbc8770af93c3c6f3e3be986b`. Forward correction should replace its cognitive-tier/self-calibration subsection in `.tfw/conventions.md` and Step 5 text in `.tfw/workflows/plan.md`, remove its `Execution profile` column from `.tfw/templates/HL.md` and `Recommended execution profile` line from `.tfw/templates/TS.md`, and apply the new rule at the actual dispatch site. The existing Plan post-approval dispatch paragraph and conventions' coordination section are concrete integration points; exact provider fields belong in their native adapter bindings. The current Codex field is `thinking`, not Phase A's universal `reasoning_effort` spelling. Final scope remains the Coordinator's Phase C decision; neither this RES nor an absent legacy `resume.md` reference authorizes extra edits.

## Open Questions

| # | Question | Status | Answer |
|---|---|---|---|
| Q1 | Does this rule choose a lower-resource sufficient pair on actual work? | Open | No comparative or prospective validation yet; iteration 4 must attack the concrete next choice and its evidence |
| Q2 | Can native readback establish resolved settings? | Partly open | Codex creation arguments and address are evidenced; effective backend settings are not. Other providers need their own native proof |
| Q3 | Are the other provider modes ready to claim as working TFW launches? | Open | CLI controls are documented/observed, but account selectors and complete native role chains remain unpiloted |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|---|---|---|---|
| H1 | Quality-floor selection is more robust than role tiers on real launches | open | Open; analytical support only | Challenge rejects role/count shortcuts; no equivalent-work outcome comparison |
| H2 | Separate capability and effort decisions prevent combined-profile errors | open | Open; structural and native-contract support | Independent constraints, fixed effort and model-slug variants; no causal field comparison |
| H3 | Dispatch application is more reliable than HL/TS profile fields without a new artifact | open | Partial native feasibility; comparative reliability open | Actual explicit Codex arguments and existing dispatch/return; the derived rule was not prospectively piloted |
| H4 | Each claimed provider has an authoritative inventory and exact usable launch route | open | Partial, surface-specific | Codex bounded native evidence; Antigravity CLI roster; Claude help; unresolved selector/effective-setting/chain claims |

## HL Update Recommendations

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|---|---|
| R6 | §2 | Replace historical savings, latency and causal overthinking assertions with their unsupported status; distinguish each installed provider surface and its observed controls | Gather G2–G6; Challenge C2/C4 |
| R7 | §7.2 | Add dated native roster/help evidence, the Coordinator's actual creation record and provider-owned contract pages with their scopes | Gather G2–G5; supplemental dispatch `dcc38f9` |
| R8 | §9 | Record incomplete cost ordering, effort resolution/fallback, unavailable selectors and unpiloted foreign-provider role chains | Extract E2/E5; Challenge C2 |
| R9 | §10 | Preserve H1–H4 as open/partial as above; use independent iteration 4 to challenge the next real choice and evidence rather than repeat unsupported confirmation | This RES hypotheses and open threads |
| R10 | §11 | Mark historical S2 profile-field strategy and S3 active-window self-calibration as superseded by A2; retain their historical origin | A2; Challenge C3/C5 |

### Amendment Proposals — frozen sections, resolved-ruler verdict required

**No amendment proposals.** The result preserves A2's quality floor, per-launch choice, provider-native evidence and independent iteration requirements. Unavailable evidence remains open; this report does not waive an acceptance criterion or authorize a provider substitution.

## Fact Candidates

No new human-only fact candidates. Conversation review found Coordinator dispatches, gate answers and native observations; the owner's strategic correction is already captured in A2 and HL S7–S10. Technical findings remain sourced research material for the Coordinator, without duplicate knowledge publication.

## Strategic Insights (Research)

No strategic insights. This bounded iteration had no new direct human domain input.

## Findings Map

```text
Exact next result + material failure
  uncertainty / dependencies / verification / consequence
                         |
             required capability, context, tools
                         |
       feasible model + separately sufficient effort
                         |
       current native availability and authorized route
             /                               \
    justified choice                    missing prerequisite
    prefer lower resource               return exact gap
    where evidence permits              to Coordinator
             |
    actual launch -> requested / resolved / outcome evidence
             |
    accepted result + material rework -> next-launch correction
```

## Iteration Status

- **Iteration:** 3 of 4 (min) / 5 (max).
- **Hypotheses tested:** H1/H2 analytically challenged; H3 bounded native parameter-passing feasibility; H4 provider/surface contract inspection. None is declared fully confirmed.
- **Hypotheses deferred:** empirical H1/H2, comparative H3 and complete per-provider H4 to independent iteration 4 and the authorized Phase C pilot as applicable.
- **Gaps discovered:** cost ordering, effective-setting readback, foreign-provider account selectors and complete chains, prospective validation of the rule.
- **Superseded decisions:** A2 already supersedes predecessor tier/profile/self-calibration decisions; this RES does not rule another amendment. Challenge C2 supersedes only Gather's broad local-Ultra implication; accepted stage history stays unchanged.

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|---|---|---|
| 1 | Concrete next-launch choice versus a cheaper plausible pair | A rationale must change behavior and discriminate candidates | Independent Researcher attacks selection grounds; retain qualitative/unknown cost limits |
| 2 | Requested versus resolved setting | A native call can resolve differently from its arguments | Use available native readback; preserve exact unavailable fields rather than infer them |
| 3 | Antigravity and Claude surface-specific readiness | A documented CLI is not a complete TFW role contract | Bound claims to existing evidence; identify exact native inventory/visible-unit/return proof for authorized pilots |
| 4 | Prospective outcome and rework | Completing this report does not validate its own rule | Observe actual launches under the rule and independent acceptance; distinguish policy, context, tool and model failures |

### Recommendation

- [ ] **SUFFICIENT**
- [x] **MORE NEEDED** — the Coordinator should activate a different directly addressable Researcher for iteration 4. Independent attack and prospective evidence remain required before Phase B acceptance and Phase C implementation.
- [ ] **BLOCKED**

## Conclusion

Iteration 3 replaces unsupported role tiers with a compact quality-first selection proposal and identifies where each native provider contract is observed, merely declared or unavailable. Its strongest evidence is actual Codex parameter passing/addressed continuation and the live Antigravity CLI roster; its strongest limitation is the lack of comparative quality/cost evidence and complete foreign-provider pilots. The rule is ready for independent challenge, not for a claim of empirical optimality or Phase B closure.

### Material handover at this return

- **Producer / epoch:** this Researcher; four exact stage commits, frozen authority and native-call record above; external/native observations on 2026-09-22.
- **Inspected scope:** task/phase routing and gate lineage, both predecessor RES files, four accepted iteration-3 stages, selected conventions/knowledge and relation checks, exact Phase A diff, current native tools/CLI surfaces and primary provider documentation. All stage files were reread for synthesis.
- **Materiality:** compact rule, provider-specific bindings, requested/resolved/outcome distinction, Ultra scope correction, exact forward-correction inputs and classified free-section recommendations.
- **Uncertainty / existing owner:** Coordinator retains the unresolved selection/pilot decisions and the complete return path to human owner `saubakirov`; no missing context is called resolved. The independently assigned iteration 4 must be provisioned and activated by the Coordinator.
- **Continuation:** return this RES to `codex:thread:local:01a0c400-3e48-7422-bb86-3b34fe177aa5` for `/tfw-plan` to register the iteration, assess refinements and dispatch independent iteration 4. This Researcher stops; no status, iteration-control, HL, TS, core or Phase A history was edited.

---

*RES — TFW_20260922-123250_CMTR: Per-Launch Model and Reasoning Selection | 2026-09-22*
