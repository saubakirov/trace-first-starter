# RES — TFW-45 iter2: Swarm Design Validation

> **Date**: 2026-06-15
> **Author**: Researcher (Antigravity)
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW-45](../../HL-TFW-45__multi_agent_workflows.md)
> **Mode**: Deep (1 OODA loop per stage — sufficient evidence per stage)

---

## Research Context

TFW-45 iteration 2 investigated the three foundational hypotheses for swarm mode: H1 (does a fresh agent produce qualitatively different output?), H8 (what abstraction — mode or execution model?), and H9 (does fresh context win over lost nuance?). Building on iter1's cross-platform capabilities audit (D1-D7, 4 surviving platform configurations), this iteration resolved the swarm design space and converged on a single recommended configuration.

## Briefing

Reference: [1_briefing.md](1_briefing.md). Focus: H1, H8, H9. User direction: H1 is hypothesis without proof — empirical A/B test planned on helpdesk project. Mode model is open — user willing to break backward compatibility if proven better. User signal: "не знаю, проверять надо."

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D8 | **H1 is structurally justified but empirically unvalidated** | Anchoring bias evidence: single agent carries cognitive baggage (reasoning path, dead ends, user corrections) from prior stages. Fresh agent sees only structured output (stage file). File-based anchoring is WEAKER than conversation-based: (1) structured vs raw, (2) finite vs growing, (3) no "Lost in the Middle" effect. Persona research shows system-prompt placement = more persistent behavior. But no TFW-specific empirical data. Proceed with design, plan A/B test on helpdesk |
| D9 | **Swarm is NOT a mode — it's an execution model, orthogonal to focused/deep** | Modes (focused/deep) control investigation DEPTH (OODA loops, counter-evidence required). Execution model controls WHO investigates (same agent or sub-agents). Independent axes: swarm × focused, swarm × deep. Making swarm a third mode is structurally wrong — eliminates the depth axis |
| D10 | **Recommended config: `execution_model: auto \| single \| multi`** | All 5 surviving configurations (S2, S3', S5, S6, S7) converge to S7+S3': config key with auto-detection + command-line override. `auto` = detect platform capability (sub-agent spawn available?) → use multi if yes, single if not. `/tfw-research --single` overrides per run |
| D11 | **Coordinator writes Briefing + RES. Sub-agents write Gather/Extract/Challenge** | Briefing requires user interaction (guiding questions → 🛑 WAIT → user answers). Sub-agents can't interact with user directly. RES requires synthesis across all stages. Only 3 sub-agents per iteration, not 4. Briefing has no "contamination" problem (it's the start of research) |
| D12 | **Full stage files as inter-stage transfer (not summaries)** | TFW stage files ARE already structured artifacts (Dimensions table, Configuration Space, Checkpoint). Adding a summary layer loses information unnecessarily. Stage file quality determines transfer quality — this is enforced by TFW templates |
| D13 | **Swarm × focused = valid but low-ROI** | Anchoring bias argument is weakest for short conversations (focused = 1 OODA loop, few turns). Recommend swarm with deep mode for maximum benefit. Config allows swarm × focused but documentation should note the recommendation |
| D14 | **Token budget is NOT a constraint** | Sub-agent system_prompt needs ~400-500 tokens (Mindset + TFW context loading + stage instructions). Current context windows = 200K-1M+ tokens. Sub-agent system_prompt < 1% of window |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Does swarm actually produce better research output than single-agent? | Deferred — empirical A/B test | Plan: helpdesk project review, old vs new, across Claude Code + Antigravity. Separate task |
| Q2 | Should `auto` be the default, or should `single` be default for safety? | Design recommendation | `auto` recommended. If platform supports sub-agents, there's no reason NOT to use them (cost escape hatch exists via `--single`). But user may prefer `single` default for predictability — this is a TS/implementation choice |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | Fresh sub-agent with Mindset-as-system-prompt produces qualitatively different output — "clean slate" eliminates anchoring bias | needs-research | 🔄 **Structurally justified, empirically unvalidated** | Anchoring bias literature (LLMs highly susceptible, standard mitigations insufficient). "Lost in the Middle" effect. File-based transfer weaker than conversation-based anchoring (structured vs reasoning path). Persona research: system-prompt placement = more persistent but NOT consistently better on objective tasks. Sufficient for design, needs A/B test |
| H8 | Mode file is the right abstraction for swarm | needs-research | ❌ **Refuted** | Swarm is an execution model, not a mode. Modes control depth (OODA loops), execution model controls who runs (single vs multi). Independent axes. Making swarm a mode conflates them. New abstraction: `execution_model: auto \| single \| multi` in project_config.yaml |
| H9 | Fresh context trade-off resolves in favor of fresh for investigative workflows | needs-research | ✅ **Confirmed** | Lost nuance analysis: user corrections → medium impact but captured in stage output; dead ends → positive loss; emotional context → low impact; cross-stage reasoning → depends on stage file quality (enforced by TFW templates). "Context rot" evidence (attention dilution, cascade of errors, task interference) favors fresh. Stage files = sufficient transfer medium |

## HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| 1 | §10 H1: Change status to "Structurally justified — needs empirical A/B test (helpdesk project)" | D8 |
| 2 | §10 H8: Change to "Refuted — swarm is execution model, not mode. New config key: execution_model" | D9 |
| 3 | §10 H9: Change to "Confirmed — fresh context wins, stage files = sufficient transfer" | D12 |
| 4 | §3.2: Replace "swarm.md mode file" concept with "execution_model config key + swarm protocol file" | D9, D10 |
| 5 | §3.2: Add Briefing/RES = coordinator, Gather/Extract/Challenge = sub-agents architecture | D11 |
| 6 | Add new §: execution_model config schema (`auto \| single \| multi`) with command override | D10 |

## Fact Candidates

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | architecture | Swarm (multi-agent execution) and investigation depth (focused/deep) are orthogonal axes. Combining them into one "mode" dimension is a category error. This likely applies beyond research — review workflow's Map/Verify/Judge stages have the same orthogonality | Gather G3, Extract E1 | ★★★ |
| FC2 | philosophy | Anchoring bias in LLMs is stronger via conversation history (reasoning path, implicit agreements, dead ends all contribute) than via structured file input (tables, checklists, explicit decisions). This means: structured artifact-based inter-agent transfer is inherently less biasing than shared conversation | Gather G1, Challenge C1 | ★★☆ |
| FC3 | process | Briefing stage has a unique constraint vs other research stages: it requires user interaction (guiding questions → wait → answers). This makes it unsuitable for sub-agent spawn in platforms where sub-agents can't directly interact with users (Antigravity). Other stages (Gather/Extract/Challenge) are self-contained once input is provided | Extract E6, Challenge C2 | ★★★ |
| FC4 | architecture | All investigated execution model configurations (S2, S3', S5, S6, S7) converge to the same design: config-level default + runtime override. This pattern appears to be a universal resolution for "opt-in vs default" design tensions in framework features | Challenge C5 | ★★☆ |
| FC5 | process | Swarm × focused mode combination is valid but low-ROI: anchoring bias (the primary justification for swarm) is weakest in short conversations with single OODA loops. The sweet spot is swarm × deep | Challenge C4 | ★★☆ |

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | architecture | The "execution model" concept (`auto \| single \| multi`) may become a general TFW pattern applicable beyond research. Review workflow (Map/Verify/Judge) has the same stage structure and the same anchoring problem. If empirical testing confirms H1, the execution_model config key should be elevated from `tfw.research.execution_model` to `tfw.execution_model` (global) with per-workflow override capability | D9, D10, FC1 | ★★☆ |
| SS2 | strategy | The user's willingness to break backward compatibility ("не знаю, проверять надо") combined with the `auto` detection mechanism means TFW could transparently upgrade all users on capable platforms to multi-agent execution. This is a significant deployment strategy: no opt-in friction for platforms that support it, automatic fallback for those that don't | D10, User direction | ★★★ |

## Findings Map

```
         H1 (fresh agent quality)          H8 (abstraction)           H9 (context trade-off)
         │                                 │                          │
         ▼                                 ▼                          ▼
    ┌────────────┐                   ┌────────────┐            ┌────────────┐
    │ ANCHORING  │                   │ SWARM ≠    │            │ FRESH      │
    │ BIAS       │                   │ MODE       │            │ CONTEXT    │
    │            │                   │            │            │ WINS       │
    │ conversation│                  │ orthogonal │            │            │
    │ > file     │                   │ to depth   │            │ stage files│
    │ (stronger) │                   │            │            │ = enough   │
    └─────┬──────┘                   └─────┬──────┘            └─────┬──────┘
          │                                │                         │
          └────────────────┬───────────────┘                         │
                           │                                         │
                    ┌──────▼──────────────────────────────────────────▼──┐
                    │                CONVERGED DESIGN                     │
                    │                                                    │
                    │  execution_model: auto | single | multi            │
                    │  default_mode:    focused | deep                   │
                    │  command override: --single / --multi              │
                    │                                                    │
                    │  Coordinator: Briefing + RES                       │
                    │  Sub-agents:  Gather (Explorer)                    │
                    │               Extract (Analyst)                    │
                    │               Challenge (Critic)                   │
                    │                                                    │
                    │  Transfer: full stage files (structured artifacts) │
                    └───────────────────────────────────────────────────┘
```

## Iteration Status

- **Iteration:** 2 of 2 (min) / 4 (max)
- **Hypotheses tested:** H1 (🔄 structurally justified), H8 (❌ refuted — swarm ≠ mode), H9 (✅ confirmed)
- **Hypotheses deferred:** None from iter2 scope. H1 empirical validation = separate task
- **Gaps discovered:** A/B test needed for H1 (planned: helpdesk project). Q2 (auto vs single default) is TS-level decision
- **Superseded decisions:** HL's "swarm.md mode file" concept → replaced by `execution_model` config key

### Open Threads (for future iterations, if needed)

1. **Empirical H1 test:** Separate task — run old-style single-agent review vs new multi-agent review on helpdesk project. Compare across Claude Code + Antigravity
2. **Review workflow swarm:** Phase B of TFW-45 — same execution_model pattern, different stages (Map/Verify/Judge)
3. **System prompt template wording:** Exact text for sub-agent system_prompt. Sketch in Extract E5, needs refinement in TS

### Recommendation
- [x] **SUFFICIENT** — both minimum iterations complete, all assigned hypotheses resolved
- [ ] **MORE NEEDED** — {specify}
- [ ] **BLOCKED** — {specify}

> Both iter1 (cross-platform capabilities) and iter2 (swarm design validation) are complete. 9 hypotheses total: H2 ✅, H3 ✅ (not recommended), H4 ❌, H5 ✅, H6 🔄, H7 ✅, H1 🔄 (structurally justified), H8 ❌ (refuted — swarm ≠ mode), H9 ✅. The design has converged to a single recommended configuration (S7+S3'). The only unresolved item is H1 empirical validation, which is explicitly out of scope (separate experiment task). Proceed to `/tfw-plan` to update HL and write TS.

## Conclusion

This research validated the foundational design for TFW's multi-agent investigative workflows by resolving three hypotheses. H1 (fresh agent quality) is structurally justified through anchoring bias evidence — conversation-based anchoring is stronger than file-based anchoring, meaning fresh sub-agents receiving structured stage files as input are less biased than a single agent carrying conversation history across stages. H8 (mode abstraction) was refuted: swarm is NOT a mode but an execution model orthogonal to investigation depth, requiring a new config key (`execution_model: auto | single | multi`) rather than a third mode file. H9 (context trade-off) was confirmed: fresh context wins for investigative workflows because lost nuance is either captured in structured stage output, irrelevant (dead ends), or low-impact (emotional context). All 5 surviving design configurations converged to a single recommendation (S7+S3': config default with auto-detection + command override), and the architecture settled on coordinator-writes-Briefing+RES, sub-agents-write-Gather/Extract/Challenge (3 agents per iteration). Without this research, the implementation would have incorrectly modeled swarm as a third mode file (conflating depth with execution model), potentially broken backward compatibility on unproven H1, and missed the auto-detection opportunity that makes multi-agent transparent for capable platforms.

---

*RES — TFW-45 iter2: Swarm Design Validation | 2026-06-15*
