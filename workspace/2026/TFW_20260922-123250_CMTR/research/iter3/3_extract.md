# Extract — Separate feasibility, sufficiency and economy

> **Mindset:** Analyst; focused mode, one OODA pass. Candidate structures below await Challenge.
> Parent: [CMTR HL](../../HL-TFW_20260922-123250_CMTR.md)
> Goal: Choose a sufficient model and reasoning effort for each actual launch, then economize within that quality floor.
> Producer: `codex:thread:local:01a0c89b-3d1e-7bd1-b8ab-a6376a7607d1`
> Parent / sole material return route: `codex:thread:local:01a0c400-3e48-7422-bb86-3b34fe177aa5`
> Authority: HL `addb2e707dd9f271b7bf1287617a8b93b8d72cb0`; A2 `2c72ec8c6b0b21269caf95b707d26c631be5df52`; dispatch `f1ab1a03a2038d5b2887e4158c6c78fef58949e0`; origin `none`.
> Continuation: corrected [Gather answer](../../journal/20260922-153340__gate_answer__b7e4.md) at `5326d70b3c56cbd82fde69f9afc309918b6851a1`, inspected with phase status and iteration assignment. The superseded answer is not used.
> Inputs: [Gather](2_gather.md) at `80648efdd81e170c1098c4966b8024158a386d19`; selected knowledge and frozen HL at base `839dfb07b90673c630b947de46a1598d21e63a36`; external sources opened 2026-09-22.

## Configuration Space

The complete space is factorized: any combination of Gather's four workload dimensions may be paired with a model meeting its context/tool constraints, an effort actually supported by that model, an observed availability source and an authorized enforcement/return route. The model/effort and provider/route pairs are constrained relations, not arbitrary Cartesian products. The tables show contrasting configurations rather than claim exhaustive empirical coverage; labels identify examples only, not permanent work classes.

| Config | Uncertainty / novelty | Dependency breadth | Verification strength | Error cost / reversibility |
|---|---|---|---|---|
| C1 | Known transformation | Local invariant | Deterministic consequence check | Cheap isolated correction |
| C2 | Known transformation | Long context with distant constraints | Deterministic consequence check | Expensive rework |
| C3 | Conflicting interpretations | Local invariant | Independent judgment | Irreversible or authority error |
| C4 | Retrievable missing facts | Multiple providers | Partial checks | Downstream reliance |
| C5 | Novel behavior | Multiple systems | Weak oracle | Downstream reliance |
| C6 | Known transformation | Local invariant | Deterministic check | Cheap correction |
| C7 | Conflicting interpretations | Coupled artifacts | Independent judgment | Expensive rework |
| C8 | Novel behavior | Multiple systems | No effective oracle | Irreversible effect |

| Config | Model capability constraint | Effort choice on a feasible model | Availability evidence | Enforcement and return |
|---|---|---|---|---|
| C1 | Bounded transformation | Lowest exposed setting | Host-native inventory | Native task and exact return |
| C2 | Long-context/tool capability even when reasoning is straightforward | Lowest supported depth adequate to preserve constraints | Host-native inventory | Native task and exact return |
| C3 | Adversarial judgment | Greater supported single-unit depth | Current target selector | Owner-operated visible session |
| C4 | Source retrieval plus synthesis | Greater supported depth | Help/docs only | Candidate CLI contract needing pilot |
| C5 | Sustained cross-system synthesis | Highest supported single-unit depth | Host-native inventory | Native task and independent return |
| C6 | Bounded transformation | Fixed/unexposed | Current target selector | Owner-operated visible session |
| C7 | Sustained judgment | No exact setting observable | No observable source | Capability-only instruction; launch choice unresolved |
| C8 | No demonstrated sufficient model under the present verification plan | Undetermined | Inventory may still be available | No justified material launch until the missing assurance is resolved |

C2 (stronger context/tool capability with lower effort), C6 (fixed effort) and C8 (availability without sufficient assurance) make combinations visible that a single model/thinking tier cannot express. This is structural analysis, not a result of model trials.

## Findings

### E1 — A quality floor must name a protected result and a check

For the exact next work, describe what must be correct and what could reveal a material failure. Use the four factors to identify the capability that the work requires: unfamiliar/conflicting information needs synthesis and judgment; coupled dependencies need context retention and tools; a partial oracle leaves more inference unchecked; expensive or irreversible errors need stronger assurance before action. Factors do not add into a numeric score, and easy factors cannot cancel a missing critical capability.

There are two kinds of support for sufficiency: comparable accepted outcomes under materially similar conditions, and a conservative provisional judgment grounded in current provider capability information plus a concrete verification plan. The latter remains provisional. If neither supports the required result, the quality floor is unresolved; choosing the largest model cannot supply missing facts, authority, access or a trustworthy oracle.

External check: [OpenAI model selection](https://developers.openai.com/api/docs/guides/model-selection) orders accuracy before cost/latency and evaluates smaller choices against that target. Its production-dataset recipe does not establish a numeric threshold for one TFW task or authorize new permanent tests. Here the approved task criteria and actual accepted returns supply the relevant observations.

### E2 — Separate model and effort decisions, then compare feasible pairs

First determine which models can perform the work with the required context, modality, tools and judgment. For each plausible model, determine an effort sufficient for the work and supported by that exact surface. Compare the resulting sufficient pairs; do not greedily choose the cheapest model ID before considering the effort and rework it may require. Raising effort cannot repair an absent capability.

[Anthropic's cost/intelligence evidence](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence) shows that cost ordering can change by workload; stronger models at reduced effort can be competitive, while longer research loops can cost more. Its API benchmark results are not this subscription's prices or CMTR savings. They expose why a model's per-token price, name or default effort is not a reliable ordering of completed-task cost.

When comparable native usage/cost data exist, use them with the result and rework. When only a provider's relative resource guidance is known, identify the selection as a qualitative resource preference. When candidates cannot be ordered on available evidence, retain a justified sufficient choice and state that the cheapest is unknown. The rule must not invent a cost frontier or perform extra model runs solely to claim an optimum.

### E3 — Candidate policies to challenge

| Candidate | Selection mechanism | Explicit uncertainty behavior | Unsettled comparison |
|---|---|---|---|
| P1 — validated reuse | Reuse the least-resource pair already accepted on materially comparable work, after refreshing native availability | Re-evaluate when novelty, dependencies, oracle, consequence or surface changes | How similar must work be before reuse is defensible? |
| P2 — capability-led first use | Establish required capability, select a justified available model, then sufficient supported effort; prefer lower resource among justified pairs | Label first-use sufficiency provisional; name the concrete verification/return | Can the rationale discriminate candidates without becoming a tier or default-max rule? |
| P3 — conservative reference | For unresolved capability comparisons, use a stronger justified reference at its supported appropriate effort, learn from its return, then consider a lower-resource next launch | Makes no initial minimum-cost claim; returns unresolved assurance gaps | Does this create unnecessary spend where a bounded lower choice was already supported? |

P1–P3 may form branches of one rule rather than rival global policies. Retaining a model's provider default can be an explicit per-launch decision; per-launch assessment does not require changing the setting every time. [Anthropic's Claude Code guidance](https://claude.com/blog/claude-model-and-effort-level-in-claude-code) often favors default effort and distinguishes capability failures from inadequate follow-through. This qualifies an automatic “complex → maximum effort” rule; it does not override A2's requirement to assess each launch.

### E4 — Draft provider-neutral contract for Challenge

1. State the exact next result and its material failure; assess uncertainty, dependencies, verification and consequence.
2. Identify the required model capability, context and tools; retain models with a defensible sufficiency basis.
3. Choose sufficient supported effort separately; compare the feasible pairs using only known resource evidence.
4. Refresh the target surface's native availability and route. If the choice is unavailable, reconsider sufficient alternatives; if none is justified, return the missing fact or capability to the Coordinator.
5. Apply the choice in native creation or a two-line owner launch. Record the requested choice, reason, actual address and available readback in the existing dispatch/return.
6. Use accepted results, material rework and failures to adjust the next launch. Attribute the problem before changing capability or effort.

“Minimum sufficient” here is a bounded decision objective over supported candidates, not a mathematical or empirical guarantee that an untested cheaper choice would fail. Challenge must test whether this wording preserves A2's value without promising unattainable certainty.

### E5 — Exact provider bindings and missing observations

| Surface | Availability and choice binding | Enforcement / readback | Explicit unknown handling |
|---|---|---|---|
| Codex desktop task tools | Refresh `create_thread` calling-host roster; validate the selected destination. Separate `model` and `thinking` fields | Native `create_thread`; retain ready `threadId`/host and exact dispatch; use addressed send and cursor wait. Creation/payload evidence is distinct from effective backend setting evidence | If native return omits resolved settings, say requested parameters only. Avoid effort options that introduce unapproved hidden role units; `ultra` needs separate topology assessment |
| Antigravity CLI 1.2.7 | `agy models`; inspect current `--model`/`--effort` semantics. Resolve model and effort to an actually listed variant, not an invented pair | Help/doc candidate: launch flags, returned `conversation_id`, exact-ID continuation, selected-session resolution log. Requires its own authorized native TFW pilot | Do not infer IDE availability or a complete visible role chain from the CLI roster. Unlisted variants remain unverified |
| Antigravity IDE 1.107.0 | Actual new-conversation model selector; model/effort variants as it exposes them | Owner selects and confirms the visible setting before entering the exact role activation; installed `chat --mode` controls execution mode | Live selector/readback unavailable here; give required capability, not the CLI's model names as an IDE recommendation |
| Claude Code 2.1.278 | Current `/model` picker and its per-model effort options/caps; pin exact resolution when known | `--model` and `--effort` for an authorized session, or session-only picker choices; exact session ID and header/`/status` readback. CLI background controls are candidate mechanics, not a verified TFW chain | Current account roster is unobserved here. Neither a docs alias nor help example proves availability; don't pass unsupported effort and assume it survives fallback |
| Claude Desktop | Its own current selector and session controls | Owner-assisted until that surface has native proof | Uninspected; Claude Code flags provide no Desktop evidence |

This is a research evidence matrix, not a proposed generic capability table for core. Exact model names remain in dated native observations and dispatches.

Concrete output shapes, using the actual CMTR work rather than placeholders:

```text
Dispatch recorded: /tfw-research TFW_20260922-123250_CMTR Phase B, iteration 3 · gpt-6-astra · high.
Reason: disputed architecture spans three providers with weak verification; this is the recorded choice, not a proved cheapest pair.
```

```text
Claude Code selection: exact model and effort unavailable to verify from this unit.
Next step: inspect the new session's /model picker; the work needs sustained cross-provider analysis, tools and supported deeper reasoning.
```

The second block is an honest availability fallback, not a ready concrete model selection. A completed owner-assisted choice requires the selector observation; no syntax can manufacture it.

## Checkpoint

| Found | Remaining |
|---|---|
| Feasible-pair selection separates capability, effort, assurance and economy | Adversarial counterexamples and accepted real outcomes |
| Evidence reuse, first-use judgment and conservative reference are explicit candidate branches | Decide where their boundaries succeed or fail |
| Unknown inventory, costs, effective settings and assurance each have a distinct response | Native pilot gaps from Gather remain open |
| Stronger model/lower effort and fixed-effort configurations are expressible | Empirical comparison is not yet available |

**OODA:** observed provider selection guidance and Gather's native constraints; oriented their claims to the task rather than importing API benchmarks; derived candidate policies and incomplete-observation branches; recorded them for Challenge without selecting a winner.

**Sufficiency:**
- [x] External source used: linked official OpenAI and Anthropic pages opened and relevant passages inspected on 2026-09-22; two search queries. One blog re-open returned an error; its successfully opened Gather source was available and inspected by `find`.
- [x] Briefing Extract gap closed: candidate rule, separate decisions, provider bindings and unknown handling are explicit.
- [x] Configuration Space built from Gather dimensions; factorization and representative configurations are distinguished from tests.

## Material handover at this checkpoint

- **Producer / source epoch:** this Researcher; Gather and authority commits above; selected provider documents as of 2026-09-22.
- **Inspected scope:** corrected answer and routing/iteration spine, Extract template, Gather findings, selected knowledge handover/current-use ranges and external model-selection evidence.
- **Materiality:** a cheaper model ID need not produce a cheaper sufficient pair; absence of a measured optimum is not evidence for automatic maximum effort; missing assurance is not repaired by more compute.
- **Uncertainty:** sufficiency remains provisional, economy lacks a measured ordering, and foreign-provider role chains remain unpiloted.
- **Continuation:** recommend close Extract and authorize Challenge in the same unit; this is not approval of the candidate policy or Phase B closure.

---
Stage complete: YES
→ Coordinator decision: pending; stop before Challenge.
