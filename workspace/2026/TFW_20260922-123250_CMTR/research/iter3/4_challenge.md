# Challenge — Can the selection rule fail usefully?

> **Mindset:** Critic; focused mode, one OODA pass. These are analytical counterexamples and bounded observations, not model benchmarks.
> Parent: [CMTR HL](../../HL-TFW_20260922-123250_CMTR.md)
> Goal: Choose a sufficient model and reasoning effort for each actual launch, then economize within that quality floor.
> Producer: `codex:thread:local:01a0c89b-3d1e-7bd1-b8ab-a6376a7607d1`
> Parent / sole material return route: `codex:thread:local:01a0c400-3e48-7422-bb86-3b34fe177aa5`
> Authority: HL `addb2e707dd9f271b7bf1287617a8b93b8d72cb0`; A2 `2c72ec8c6b0b21269caf95b707d26c631be5df52`; dispatch `f1ab1a03a2038d5b2887e4158c6c78fef58949e0`; origin `none`.
> Continuation: [Extract answer](../../journal/20260922-153809__gate_answer__8c21.md) at `f14f8b10c052808a5133c99569b1e7fcb6a44b20`, inspected with the unchanged Phase B routing and iteration-3 assignment.
> Inputs: [Gather](2_gather.md) `80648efdd81e170c1098c4966b8024158a386d19`; [Extract](3_extract.md) `9a60b90ec2836147e65f34a9c950d71d57840d81`; historical Phase A candidate `92c5ee4bb83271adbc8770af93c3c6f3e3be986b`; external sources inspected 2026-09-22.

## Consistency Check

The four workload factors can coexist in any combination; breadth or novelty alone does not make a workload impossible. Incompatibilities arise between a required capability, the offered setting, the evidence supporting it and the authorized route.

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|---|---|---|---|---|
| Model capability constraint | Required tool/context missing | Effort choice on a feasible model | Highest effort as compensation | Extra reasoning cannot expose an absent source/tool or fit unavailable context |
| Effort choice on a feasible model | Arbitrary named level | Availability evidence | Model listing without that variant/capability | Global help choices do not prove the pair exists |
| Availability evidence | Documentation/help only | Enforcement and return | Claimed verified autonomous chain | Declaration does not prove account access, visibility, addressed return or activation |
| Verification strength | No effective oracle | Error cost / reversibility | Irreversible effect treated as assured by model strength | The required assurance is still missing |
| Availability evidence | CLI inventory | Enforcement and return | Exact IDE selection asserted without inspecting IDE | Different surface and possibly account/settings; no native equivalence proof |
| Effort choice on a feasible model | Setting also enables orchestration | Enforcement and return | Hidden helper substituted for a TFW role | A model option grants no role authority; topology must stay within the mandate |
| Verification strength | Passing mechanical checks only | Model capability constraint | Semantic/authority correctness inferred | The check may not test the protected consequence |

Other pairs remain possible but conditional. High consequence can coexist with narrow scope and strong checks; broad scope can coexist with straightforward reasoning. Cost evidence is incomplete rather than a reason to pretend these inputs form a total ranking.

**Surviving configurations:**

| Config from Extract | Model capability constraint | Effort choice on a feasible model | Enforcement and return | Disposition |
|---|---|---|---|---|
| C1 | Bounded transformation | Lowest justified supported level | Native task and check | Survives when the check covers the material failure |
| C2 | Necessary long-context/tools | Lower sufficient effort | Native task and check | Survives; breadth alone does not force highest effort |
| C3 | Adversarial judgment | Sufficient supported depth | Owner-visible session plus independent assurance | Conditional: higher effort alone does not make an irreversible action acceptable |
| C4 | Retrieval and synthesis | Sufficient supported depth | Candidate CLI route | Research/read-only candidate survives; autonomous TFW readiness remains unverified |
| C5 | Sustained synthesis | Appropriate supported depth | Native task and independent return | Conditional: Extract's “highest” is narrowed to justified depth, not maximum by default |
| C6 | Bounded transformation | Fixed/unexposed | Owner-visible session and check | Survives; independent conceptual decisions do not require two UI controls |
| C7 | Sustained judgment | Exact setting unobserved | Capability-only fallback | Survives as a missing-selection return, not a completed launch |
| C8 | No justified sufficient model/assurance | Undetermined | Return unresolved dependency | Survives as a stop/re-scope branch; no fabricated safe pair |

**Unexpected survivors:** C2 and C6 remain valid, and C8 is a necessary result of the rule. A useful launch policy sometimes produces a specific missing prerequisite rather than a model name.

## Findings

### C1 — Counterexamples to role tiers and automatic escalation

| Case / attempted shortcut | Protected failure | Result of applying the candidate rule |
|---|---|---|
| A one-line documentation edit changes the root delegation mandate; call it “routine docs” | Grants unintended authority despite small text diff | Semantic consequence and weak mechanical oracle dominate; require judgment and the proper decision route, not a routine-role preset |
| A broad mechanical update is fully checked by an appropriate deterministic oracle; call it “large therefore critical” | Unnecessary model/effort spend | Retain enough context/tools, but permit lower effort when reasoning is bounded and the oracle actually protects the result |
| A cheaper model cannot inspect required visual evidence; set maximum effort | Unsupported conclusion from unseen evidence | Reject the capability mismatch before comparing effort |
| A capable model has all facts but repeatedly misses a cross-system contradiction | Purpose/architecture defect | Greater capability is a candidate for the next launch; more effort is not automatically the cure |
| A suitable model skips an available required check | Undetected material defect | Inspect instructions, access, stopping behavior and effort. Higher next-launch effort is a hypothesis, not proof of the cause |
| Quota leaves only an unjustified weaker choice | Quality floor silently reduced | Surface the unavailable sufficient option; do not launch a lower-quality substitute merely to keep activity going |
| The fastest per-token model requires extensive retries while a stronger model can finish | Misstated economy | Compare sufficient pairs on relevant outcome/resource evidence; retain “cost ordering unknown” where none exists |
| A missing legal/business requirement or source is guessed by a larger model | Confident unsupported output | Obtain the missing fact or route the dependency; compute cannot replace authority or evidence |

These thought experiments falsify simple mappings and identify failure conditions. They do not prove a win rate, savings percentage, model quality ranking or the reliability of the proposed rule.

### C2 — Provider counterexamples refine the binding

**Unsupported effort:** the native Antigravity roster in Gather includes only two Pro variants, whereas CLI help exposes three effort labels globally. It cannot justify constructing the absent third variant. [Claude's model configuration](https://code.claude.com/docs/en/model-config) documents model-specific effort support and downward resolution of unsupported choices. A launch can accept a request yet apply a different setting. Record available resolution/readback separately; a material mismatch requires reconsideration before dependent work continues, not a silent label update.

**Surface mismatch:** an Antigravity IDE `--mode agent` parameter is not “high thinking.” A CLI model listing does not prove the IDE selector. [Antigravity's headless contract](https://antigravity.google/docs/cli/headless/) also rejects CLI-handled `/model` commands inside stream-JSON input. Thus “send the same selector command everywhere” is not a portable binding. No runtime failure was induced here.

**Topology correction to Gather G2:** the general [OpenAI model page](https://learn.chatgpt.com/docs/models) associates Ultra with subagents, but the more specific [subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents) distinguishes ChatGPT Work's proactive Ultra delegation from current local Codex's direct-request/project-instruction activation. This unit's active instructions independently prohibit unrequested delegation. Therefore **this research does not prove that selecting `ultra` in this local Codex tool automatically spawns helpers**. The supported finding is narrower: inspect the target surface's semantics and maintain the role boundary; neither accepting nor excluding an enum value by cross-surface analogy is justified. No Ultra run was performed.

**Requested versus effective settings:** the Codex native tool calls the field `thinking`, while Phase A core prose used `reasoning_effort`. That is a concrete reason to keep exact field names in the relevant adapter, not copy an API-shaped universal spelling into core. Likewise changing settings for a future turn is distinct from switching the currently executing response. The present rule makes no active-window self-calibration promise.

### C3 — Candidate policies survive only as bounded branches

| Candidate | Attack | Disposition |
|---|---|---|
| P1 validated reuse | Same role and file count, but different error consequence or oracle | Survives only when comparable outcome evidence covers the material requirements; role-name similarity is insufficient |
| P2 capability-led first use | Fluent reasoning describes a model as sufficient without evidence | Survives as explicit provisional judgment tied to capability evidence and verification; cannot be relabeled empirically proved |
| P3 conservative reference | “Uncertain” always selects maximum model and effort | Reject as a universal default; retain only when a concrete unresolved capability/assurance requirement justifies the extra resource and a useful outcome check exists |

The surviving proposal combines P1 and P2, with P3 as a justified exceptional first-use branch and C8 as the honest no-selection outcome. The selection can explicitly retain a provider default. Neither the largest model nor lowest effort is a universal optimum.

**Refined compact rule:** Before each launch, identify the required result and material failure from uncertainty, dependencies, verification and consequence. Choose a capable model, then sufficient supported effort; prefer lower resource only among choices with a defensible sufficiency basis. Refresh the native options and apply the choice in the actual launch. Record the choice and reason, then the result and material rework. If availability, capability or assurance is unresolved, name that gap; if cost is unknown, claim no optimum. Correct the next choice according to the observed failure.

This retains the approved quality-before-economy objective. It does not amend A2 into a guarantee that an untested cheaper pair cannot work.

### C4 — Real CMTR evidence and its limit

| Evidence | What it establishes | What it does not establish |
|---|---|---|
| Dispatch `f1ab1a0`, supplemental native-call record `dcc38f9`, received activation and this unit's address | Coordinator-recorded creation arguments `model: gpt-6-astra`, `thinking: high`, concrete rationale, distinct unit, host and actual delivery | Backend-effective settings or lowest sufficient cost |
| Coordinator Briefing/Gather/Extract answers and unchanged landings | Same-unit continuation; independently inspected stage returns within bounds | Independent acceptance of the final rule or complete Phase B |
| Local version/help commands and `agy models` | Installed contracts and a live CLI roster | Inference success, remaining quota or complete foreign-provider chain |
| Historical candidate `92c5ee4` diff | Phase A encoded role tiers, static names, profile fields, self-calibration and an unsupported latency claim in core | Any causal effect of model/effort on the quality of that implementation |
| Corrected Gather gate answer `5326d70` | Coordinator disclosed and corrected a journal-validator prefix mismatch | A Researcher model-capability failure requiring higher effort |

The Coordinator answered the bounded native-call request in [supplemental dispatch](../../phase-b/journal/20260922-153956__dispatch__4e6a.md) at `dcc38f964e419eab1b389f31ae3d06dde6973fbd`, inspected by `git show`. Its first-person record names the exact creation arguments above, the project worktree from `master`, and the provisioning-only prompt. Initial native return contained only `clientThreadId: client-new-thread:86f768ac-cffe-40d4-a086-903cc3f5d8b0` and `hostId: local`; registration later resolved this Researcher's ready `threadId`. Title-write and bounded-wait results established the ready address before exact activation. This is attributable native-call evidence from the producer, not a transcript inspection by this Researcher. It corroborates parameter passing; effective backend settings remain unobserved. A final research outcome still needs synthesis and independent iteration 4.

**Substantive correction in this iteration:** the specific local-Codex topology documentation narrows the earlier broad Ultra implication. This is an observed source-scope correction, not a demonstrated need for more compute. Token economy and relative sufficiency remain unmeasured.

### C5 — Integration and independent challenge must protect the actual dispatch

Inspection of Phase A's exact diff identifies its four correction sites: `.tfw/conventions.md` subsection `Cognitive Budgeting and Platform-Adaptive Launching`, `.tfw/workflows/plan.md` Step 5, `.tfw/templates/HL.md` `Execution profile` column and `.tfw/templates/TS.md` `Recommended execution profile` line. The new rule cannot merely replace their tier names with a better paragraph: the next real dispatch must consume the selection.

The current Plan workflow's post-approval dispatch paragraph and conventions' coordination contract are relevant enforcement sites; the root native bindings own exact call fields and readback. A search also found there is no `.tfw/workflows/resume.md` in this base, despite a legacy knowledge-index reference, so no implementation plan should invent that target. This is a scoped integration input, not authority to edit core or every historical mention. The Coordinator must select the final Phase C surface after iteration 4.

Independent iteration 4 should challenge: whether the concrete next launch rationale distinguishes a cheaper feasible alternative; whether a real native call applies the requested pair or reports a mismatch; whether owner-assisted output is usable from the current target selector; and whether accepted result/rework supports the decision. It must preserve the unavailable-provider boundary. No permanent tests or unrelated benchmarks were added.

## Checkpoint

| Found | Remaining |
|---|---|
| Conditional P1/P2 policy with justified P3 and explicit no-selection outcome | Independent attack and real comparative outcomes |
| Provider flags, effort variants and topology cannot be copied across surfaces | Effective-setting readback and Antigravity/Claude native chain pilots |
| Broad Ultra implication narrowed by surface-specific evidence | Actual local Ultra behavior remains untested |
| Actual dispatch/returns support delivery and bounded continuation | Final RES, independent iteration 4 and Phase B acceptance |

**OODA:** observed exact Phase A changes, live task-local answers and primary provider counter-evidence; oriented them against the candidate branches; rejected automatic maximum/default tiers and narrowed the cross-surface Ultra claim; recorded the surviving rule and open empirical limits.

**Sufficiency:**
- [x] External source used: official OpenAI, Claude and Antigravity pages opened and relevant passages checked on 2026-09-22; two search queries.
- [x] Briefing gap closed: counterexamples applied, real-dispatch claims bounded, escalation causes separated, independent continuation named.
- [x] Pairwise incompatibilities checked and surviving Extract configurations listed; no completeness or success-rate claim.

## Material handover at this checkpoint

- **Producer / source epoch:** this Researcher; exact commits and dated native/external sources above.
- **Inspected scope:** current routing and exact answer, Challenge template, Extract candidates, selected knowledge current-use/handover rules, Phase A candidate diff, bounded dispatch integration search and provider-specific counter-evidence.
- **Materiality:** capability, effort and verification failures need different responses. The policy survives as a provisional decision discipline with an explicit uncertainty branch, not as a proven optimizer. Local-Codex Ultra claims are corrected in scope here.
- **Uncertainty:** model sufficiency, resource optimum, effective settings and foreign-provider complete launch chains remain unproved; no new role or session was created.
- **Continuation:** recommend close Challenge and authorize only synthesis in this unit. Final iteration 3 should recommend MORE NEEDED for independent iteration 4; no Phase B closure is claimed.

---
Stage complete: YES
→ Coordinator decision: pending; stop before RES synthesis.
