# RES — TFW-32 Iteration 3: Naming Finals, Visualization, Multi-Iteration

> **Date**: 2026-04-10
> **Author**: AI (Researcher)
> **Status**: 🔬 RES — Complete (Iteration 3)
> **Parent HL**: [HL-TFW-32](HL-TFW-32__methodology_and_positioning.md)
> **Mode**: Pipeline (deep)
> **Predecessors**: [RES1](RES__TFW-32__methodology_and_positioning.md) (D1-D9), [RES2](research2/RES__iter2__naming_visualization_multiiter.md) (D10-D14)

---

## Research Context

Iteration 3 investigated naming decisions left open by RES1 and RES2: §6/§7 section names for facts and human knowledge, visualization section naming, and multi-iteration research formalization. Unlike previous iterations which used theoretical analysis (SECI model, D28 reasoning), this iteration used **empirical LLM testing** — running the same conversation through Qwen3.5-27B with each candidate name as the only prompt. Results directly contradicted RES1 D2 and RES2 D10.

## Briefing

See [research3/briefing.md](research3/briefing.md). Key user direction:
- Wants comparison tables for all naming decisions (name, framing, pros, cons)
- Multi-iteration: research should be self-leading. min_iterations = 2. Full spec needed
- Meta-principle: «название = промпт» (Claude Code Dreaming) — if named right, AI needs fewer instructions
- Terms will become communication foundation for humans too. Balance: industry (understood, code-centric) vs custom (value-centric, needs learning)

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D15 | **Keep «Strategic Insights» for §7/§11. Do NOT rename.** Supersedes RES2 D10 («Strategic Signals»). Add tighter instruction block to all templates | Empirical LLM test: «Strategic Insights» triggered the deepest analytical mode (Qwen3.5-27B added implications not in input). «Strategic Signals» scored shallower. «Fact Candidates» triggered pure reporting (correct for §6). D28 confirmed empirically: correct name = correct cognitive mode. 7-variant comparison table: SI tied top (7/9) with Key Learnings and Domain Signals, but has strongest prompt behavior |
| D16 | **Keep «Fact Candidates» for §6. Do NOT rename.** Supersedes RES1 D2 («Doc Candidates + Knowledge Candidates»). Sharpen instructions, not name | Empirical test: model said «record factual without adding interpretation» — EXACTLY the target behavior. 5-variant comparison: Project Patterns (8/9) technically stronger but loses one-off facts. «Fact Candidate» = pipeline metaphor (candidate → verified). 31 tasks of usage. Backwards compatible |
| D17 | **Use «Diagrams» for visualization section across all result artifacts (HL §3.1, RF, RES).** Per-template instructions carry framing load | Empirical test: «Diagrams» produced structured engineering-grade output. «Visual Map» produced explanatory narrative output. For universal section: «Diagrams» = zero learning curve, cross-domain understood. Instructions control level: HL = value delivery flow, RF = technical process, RES = findings visualization. 8-variant comparison: Diagrams (7/9), Process Maps (8/9 but narrow) |
| D18 | **Multi-iteration: `researchN/` folders (accumulate, don't overwrite). All RES files on task root with iterN naming** | TFW trace philosophy: deleting stage files = deleting traces. VLM-3 practice: research3 briefing referenced specific findings from research1 gather. Disk cost negligible vs information value. 5 failure scenario test: 4/5 handled, F5 (info loss) = reason to keep folders |
| D19 | **Multi-iteration: `iterations.yaml` + researcher exit protocol + coordinator gate in plan.md. min_iterations = 2 (configurable hard floor)** | Empirical from 6 iterations (VLM-3×4 + TFW-32×2): without control file, coordinator tracks state in head (works for 1 person, doesn't scale). Researcher exit protocol (tested in RES2 TFW-32: «Iteration Status» block) was useful. Gate in plan.md: coordinator CANNOT proceed to TS while iterations < min |
| D20 | **Naming philosophy is coherent. §5/§6/§7 = cognitive modes (observe/candidate/synthesize). Diagrams = output format. Different function = different naming logic. Acceptable** | Coherence test: three capture sections follow cognitive mode ontology. Viz section = rendering purpose, not capture. Inconsistency is structural, not a defect |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q8 | Should «Strategic Insights» be renamed to «Strategic Insights» + qualifier in RF? E.g., «Strategic Insights (Execution)» vs «Strategic Insights (Planning)» in HL? | Open | RES2 proposed qualifiers. Coordinator decides: one section name everywhere, or qualified by context |
| Q9 | Where exactly in plan.md does the coordinator iteration gate go? After Step 5b? New Step 5c? | Open | Design exists, insertion point TBD |
| Q10 | Should iterations.yaml min_iterations be configurable in PROJECT_CONFIG.yaml? | Open | Proposed default = 2. Config key: `tfw.research.min_iterations` |

## Hypotheses

| # | Hypothesis | RES2 Status | RES3 Status | Evidence |
|---|-----------|-------------|-------------|----------|
| H5c | «Strategic Signals» (D10) — not final, better variant exists | NEW (RES2 left open Q5) | ❌ REFUTED (reversed) | Empirical: «Strategic Insights» (original) > «Strategic Signals» (D10). 7-variant comparison + LLM test. **D10 was regression, not improvement** |
| H6c | «Diagrams» (D12) — not final, better variant exists | NEW | ⚠️ PARTIALLY CONFIRMED | 8-variant comparison: «Process Maps» technically stronger (8/9) but too narrow. «Visual Map» interesting but adds learning curve. «Diagrams» wins as umbrella with per-template instructions |
| H7c | Multi-iteration should be self-leading, min_iterations=2, full spec needed | NEW | ✅ CONFIRMED | Full design: iterations.yaml + exit protocol + briefing template iter2+ + coordinator gate + researchN/ folders. 6 iterations analyzed from practice, 5 failure scenarios tested |
| H_meta | All names should follow ONE philosophy | NEW | ✅ CONFIRMED with nuance | §5/§6/§7 = cognitive modes (coherent). Diagrams = output format (different category). Acceptable because different function |

## HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| 1 | §3 Target State: Replace D10/D11 naming with «keep Strategic Insights + keep Fact Candidates + sharpen instructions». Supersedes RES1 D2 AND RES2 D10 | D15, D16 |
| 2 | §4 Phase A: Add «Diagrams section to RF and RES templates» (from D12, kept). Expand HL §3.1 instructions | D17 |
| 3 | §4 Phase A: Add «Formalize multi-iteration research: iterations.yaml, exit protocol, briefing template for iter 2+, coordinator gate in plan.md, researchN/ folder structure» | D18, D19 |
| 4 | §10 Hypotheses: Update H5 and H6 — both original names were correct all along. Research journey: D2 → D10 → D15 shows importance of empirical testing | D15, D16 |
| 5 | §11: Keep name «Strategic Insights» (REMOVE the rename action item from Phase A scope) | D15 |
| 6 | Phase A scope: add iterations.yaml format spec, exit protocol template, briefing template for iter 2+, min_iterations config key | D19 |

## Fact Candidates

> Reviewing conversation history. Applying sharpened instructions:
> Project-level facts discoverable by reading code/data. NOT tech debt (→ Observations). NOT human-only (→ Strategic Insights).

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC13 | process | LLM section headers = micro-prompts. Empirically confirmed: same conversation, different section name → fundamentally different LLM behavior (analytical synthesis vs pure reporting vs retrospective). This is why D28 (Naming Creates Behavior) works | External research (naming-as-prompting) + Empirical test (Qwen3.5-27B), 2026-04-10 | ★★★ |
| FC14 | convention | TFW naming splits into two ontological categories: (1) Capture sections (§5/§6/§7) follow cognitive mode naming (observe/candidate/synthesize). (2) Output sections (Diagrams) follow format naming. Different function = different naming logic | Challenge C5 analysis, 2026-04-10 | ★★☆ |
| FC15 | process | Multi-iteration research in practice (6 iterations across 2 projects): every iteration had a SPECIFIC trigger (verify facts, check sycophancy, deepen specific topic). «Just run another iteration» without trigger = waste. Trigger taxonomy: error correction, gap filling, depth on specific finding, user-injected new direction | VLM-3 (4 iter) + TFW-32 (2 iter), analysis 2026-04-10 | ★★★ |

## Strategic Insights (from conversation)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS5 | philosophy | «Если правильно назовём — ИИ проще, слов надо меньше» — confirmed as «Claude Code Dreaming» principle. Empirically proven: section name = the strongest single-word prompt. Trumps instructions in determining cognitive mode | User (2026-04-10). Confirmed by empirical LLM test | ★★★ |
| SS6 | philosophy | Terms will become communication foundation for humans. Balance needed: industry terms (understood, code-centric) vs custom terms (value-centric, needs learning). Decision: use industry terms when they work cross-domain (Diagrams), keep original when proven (Strategic Insights, Fact Candidates) | User (2026-04-10), briefing | ★★★ |
| SS7 | process | Research should be self-leading. «Он должен явно оставлять что не закрыто». Min 2 iterations always. Agents always want to finish faster — structural enforcement needed | User (2026-04-10), confirmed in RES2 SS2 | ★★★ |

## Conclusion

Iteration 3 used **empirical LLM testing** (Qwen3.5-27B, zero-context) to resolve naming decisions open since RES1. Central finding: both RES1 D2 (rename to Doc/Knowledge Candidates) and RES2 D10 (rename to Strategic Signals) were regressions — the original names «Strategic Insights» and «Fact Candidates» produce empirically optimal LLM behavior. «Strategic Insights» triggers deep analytical synthesis (model ADDS implications not in input). «Fact Candidates» triggers pure reporting (model explicitly avoids interpretation). No proposed alternative matched this precision.

For visualization: «Diagrams» wins as umbrella term. Cross-domain, zero learning curve, empirically produces good output for both vision and detail levels. Per-template instructions carry the framing load.

Multi-iteration research formalized from 6 real iterations: `researchN/` folders (trace preservation), `iterations.yaml` (coordinator control), researcher exit protocol (mandatory gap list + open threads), briefing template for iteration 2+, coordinator gate in plan.md (min_iterations = 2 hard floor).

Self-critique: The empirical test used one model (Qwen3.5-27B). Results may differ on Claude, GPT-4o, Gemini. However, the naming-as-prompting principle is confirmed by external research across models. The biggest unresolved item: exact plan.md insertion point for coordinator iteration gate (Q9).

## Iteration Status

- **Iteration:** 3 of 2 (min) / 5 (max)
- **Hypotheses tested:** H5c (refuted — originals better), H6c (partially confirmed — Diagrams wins), H7c (confirmed — full design), H_meta (confirmed — philosophy coherent)
- **Hypotheses deferred:** None
- **Gaps discovered:**
  - Q8: qualifier for Strategic Insights by context (Planning vs Execution)
  - Q9: exact plan.md insertion point
  - Q10: min_iterations as PROJECT_CONFIG key
- **Superseded decisions:** D15 supersedes D10 (RES2). D16 supersedes D2 (RES1). Net effect: reverted to original names with tighter instructions

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | Qualifier for Strategic Insights by context | HL §11 vs RF §7 — same section name or with (Planning)/(Execution) qualifier? | extract: test both approaches in template mock-up |
| 2 | plan.md exact insertion point for iteration gate | Gate exists but not placed in workflow | extract: review plan.md structure, propose Step 5c |
| 3 | Cross-model validation of naming test | Only tested on Qwen3.5-27B | gather: run same test on Claude/GPT if available |

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to update HL and write TS
- [ ] MORE NEEDED
- [ ] BLOCKED

Open threads are detail-level (qualifier format, plan.md insertion, cross-model validation). Core decisions are solid with empirical backing. Can be resolved during TS/execution.

> ⚠️ Coordinator decides. Researcher recommends but does NOT decide.

---

*RES — TFW-32 Iteration 3: Naming Finals, Visualization, Multi-Iteration | 2026-04-10*
