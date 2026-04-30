# RES — TFW-42: Research Cycle Restructure

> **Date**: 2026-04-30
> **Author**: Researcher (Antigravity)
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW-42](../HL-TFW-42__research_cycle_restructure.md)
> **Mode**: Pipeline

---

## Research Context
HL-TFW-42 proposes restructuring the research cycle: unified `research/` container, numbered stages, kebab-case phases, enriched iterations.yaml with multi-agent fields. This research investigates H1: whether `agent` field in iterations.yaml is sufficient for multi-agent orchestration, or whether a separate mechanism is needed. The investigation also evaluates all proposed schema enrichments against empirical evidence (AFD-2) and external frameworks.

## Briefing
See [research/briefing.md](research/briefing.md). Deep mode, autonomous execution. Three dimensions investigated: agent specification mechanism, iteration dependency model, framework guidance level.

## Decisions
| # | Decision | Rationale |
|---|----------|-----------|
| D1 | `agent` field: free-text string, optional | TFW agents are external tools (not LLM instances like CrewAI/MetaGPT). Free-text avoids registry maintenance. Optional avoids single-agent noise. Purpose is traceability, not dispatch |
| D2 | Drop `depends_on` field from v1 schema | AFD-2 empirical data (8 iterations): ALL dependencies were linear-sequential. Iteration number IS the dependency. research/base.md Step 0 already enforces predecessor reading. YAGNI — no evidence for DAG research patterns |
| D3 | Drop `brief` field — `focus` already serves this purpose | AFD-2's iterations.yaml uses YAML `>` multiline in `focus` field, functioning as both summary and brief. Separate `brief` = redundancy |
| D4 | Drop `notes` field — catch-all with no clear purpose | Catch-all fields accumulate noise. Doesn't pass "Would the next agent decide differently?" test. Specific fields (`agent`, `sources`) serve clear purposes |
| D5 | Keep `sources` field: list, optional | Unique value: planning hint that signals research approach (web vs code vs infra) to the researcher. Useful for multi-agent handoff — different agents excel at different source types. Not duplicated by stage files (those record actual, not planned sources) |
| D6 | Framework guidance: Prompt-in-template (C2 configuration) | Best balance: iterations.yaml template includes `agent:` with comment guidance. plan.md Step 6b mentions multi-agent as possibility. Not prescriptive — coordinator can ignore for single-agent projects |
| D7 | Agent purpose = traceability, not dispatch | Critical framing: TFW records which tool was used (trace), it doesn't automatically route work to tools. Coordinator (human) makes the choice. This distinguishes TFW from automated multi-agent frameworks |

## Open Questions
| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Should iterations.yaml template include agent archetype examples? | Resolved | Yes — a comment with 3 archetypes (web researcher, code auditor, infra operator) provides guidance without prescription. Derived from AFD-2 empirical patterns |
| Q2 | Is `res_file` path updated for co-located RES? | Resolved | Yes — changes from `RES__TFW-42__title.md` to `RES.md` (inside `research/iterN/`). Schema change needed in conventions.md |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | Multi-agent orchestration needs `agent` field in iterations.yaml, not a separate mechanism | open | ✅ confirmed | 4 external frameworks analyzed: all use task-level agent assignment. TFW agents are external tools, not LLM instances — no definition/registry needed. AFD-2 empirical: per-iteration assignment was the only pattern observed. Challenge C3: separate `.tfw/agents.yaml` would be stale, user-specific, and unenforced |

## HL Update Recommendations
<!-- List what should change in HL based on research. Coordinator applies these. -->
| # | What to update | Source |
|---|---------------|--------|
| R1 | §3.1 iterations.yaml schema: drop `brief`, `notes`, `depends_on` fields. Keep only `agent` (optional, free-text) and `sources` (optional, list) as new fields | D1-D5, Challenge C2/C4 |
| R2 | §4 Phase A deliverable #5: update to reflect simplified schema (2 new optional fields, not 5) | D1-D5 |
| R3 | §5 DoD #4: update iterations.yaml description — "supports optional fields: `agent`, `sources`" (not `agent`, `sources`, `depends_on`, `brief`, `notes`) | D1-D5 |
| R4 | §10 H1: mark as confirmed with evidence summary | H1 confirmation |
| R5 | Consider adding a note to HL §7 about agent field purpose: "for traceability, not dispatch" | D7 |

## Fact Candidates

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | domain | TFW agents are external tools (IDE-level systems like Antigravity, Claude Code, Codex CLI), not LLM instances. This fundamentally simplifies agent specification vs frameworks like CrewAI/MetaGPT that must define agent capabilities | Gather G1 analysis, Challenge C3 | ★★★ |
| FC2 | process | In AFD-2 (8 iterations, 3 agents), all iteration dependencies were linear-sequential. No DAG patterns observed. Each iteration consumed predecessor RES only | Gather G2, Challenge C2 | ★★★ |
| FC3 | process | Three agent archetypes emerged from AFD-2: Web Researcher (Antigravity — web search, synthesis, large context), Code Auditor (Codex — file traversal, commands), Infra Operator (Claude Code — MCP access, SSH) | Gather G2 table | ★★☆ |
| FC4 | convention | YAML multiline `>` in `focus` field makes a separate `brief` field redundant. AFD-2's iterations.yaml already uses this pattern | Extract E4 | ★★★ |

> fact-candidates: processed 2026-04-30

> **Source format**: Uses reference patterns per compilable_contract.md §2.

## Strategic Insights (Research)

> No human interaction occurred during this autonomous research session. Strategic insights from HL (S1-S3) were used as input but no new human-sourced insights emerged.

No strategic insights.

## Findings Map

```
H1: Agent field in iterations.yaml?
├── CONFIRMED ✅
├── Evidence FOR (4 branches):
│   ├── CrewAI parallel: task-level `agent:` field = industry standard
│   ├── AFD-2 empirical: per-iteration assignment worked for 8 iterations
│   ├── Locality: agent near focus/hypotheses = co-located data
│   └── Optional: single-agent projects ignore it
├── Evidence AGAINST (3 branches, all refuted):
│   ├── Separate .tfw/agents.yaml → REFUTED: would be stale, user-specific
│   ├── Structured profiles → REFUTED: TFW doesn't own agent capabilities  
│   └── Enum registry → REFUTED: brittle, fails on new agents
└── Schema simplification:
    ├── KEEP: agent (free-text, optional)
    ├── KEEP: sources (list, optional)  
    ├── DROP: brief (redundant with focus)
    ├── DROP: notes (catch-all noise)
    └── DROP: depends_on (iteration number = dependency)
```

## Iteration Status

- **Iteration:** 1 of 1 (min) / 3 (max)
- **Hypotheses tested:** H1 (confirmed ✅)
- **Hypotheses deferred:** None
- **Gaps discovered:** None
- **Superseded decisions:** None

### Open Threads (for next iteration)

No open threads.

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to update HL and write TS
- [ ] **MORE NEEDED** — {specify what and why}
- [ ] **BLOCKED** — {specify blocker}

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

Justification for SUFFICIENT with 1 iteration (below `min_iterations: 2` default):
1. `iterations.yaml` for this task has `min_iterations: 1` — coordinator override with rationale: "single focused hypothesis (H1), empirically bounded scope"
2. H1 is fully confirmed with external evidence (5 web searches, 4 framework comparisons) and internal evidence (AFD-2 8-iteration dataset)
3. Schema was simplified (5→2 new fields) based on evidence, not expanded
4. No gaps or open threads discovered
5. Deep mode requirements met: 2+ decisions per stage, hypothesis tested per stage, counter-evidence sought at every stage

## Conclusion
Research investigated how TFW should present multi-agent research orchestration via iterations.yaml, testing H1 against 4 external multi-agent frameworks (CrewAI, AutoGen, LangGraph, MetaGPT) and AFD-2 empirical data (8 iterations, 3 agents). H1 confirmed: a free-text `agent` field in iterations.yaml is sufficient — no separate mechanism needed. The critical insight is that TFW agents are external tools (not LLM instances), making the agent field about traceability rather than dispatch. Research also simplified the proposed schema by dropping 3 of 5 proposed fields (`brief`, `notes`, `depends_on`) based on redundancy analysis and YAGNI evidence. The surviving schema adds only `agent` (optional, free-text) and `sources` (optional, list) to existing iterations.yaml fields. Self-critique: the AFD-2 dataset (1 project, 8 iterations) is limited. The 3-archetype pattern (Web Researcher / Code Auditor / Infra Operator) may not generalize to all project types. However, the design is intentionally minimal — it records choices without constraining them.

---

*RES — TFW-42: Research Cycle Restructure | 2026-04-30*
