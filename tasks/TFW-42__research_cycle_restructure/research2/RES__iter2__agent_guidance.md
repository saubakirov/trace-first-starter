# RES — iter2: Agent Guidance Formalization

> **Date**: 2026-04-30
> **Author**: Researcher (Antigravity)
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW-42](../HL-TFW-42__research_cycle_restructure.md)
> **Mode**: Pipeline

---

## Research Context
Iteration 1 confirmed H1 (agent field in iterations.yaml) and simplified the schema (5→2 new fields). But it left a gap: HOW should TFW guide coordinators in choosing agents for different iterations? This iteration investigates tool capabilities, designs the guidance framework, and produces concrete output (table text, template comments, workflow changes).

## Briefing
See [research2/briefing.md](research2/briefing.md). Builds on iter 1 decisions D1/D6/D7.

## Decisions
| # | Decision | Rationale |
|---|----------|-----------|
| D8 | Guidance uses CAPABILITY CATEGORIES, not tool names | Tool-agnosticism (TFW principle). Capabilities are stable ("web search needed"); tools are volatile ("Antigravity has web search" — may change). Specific tool mapping = project-level KNOWLEDGE.md, not framework conventions |
| D9 | Two-tier guidance: conventions.md table + iterations.yaml template comment | Pattern A validated (D24): inline hint at decision point + reference for detail. Conventions table = 5-row capability matrix. Template = commented-out `agent`/`sources` fields. Neither is mandatory |
| D10 | plan.md Step 6b gets 1-sentence reference, not active prompt | "Consider different tools. See conventions.md §4." Active prompting ("which agent will you use?") is too prescriptive for an optional feature. Reference = awareness without obligation |
| D11 | Human decides, framework provides decision table (not suggestions) | Framework cannot reliably suggest tools (E5: keyword matching is brittle, tool landscape volatile, TFW = methodology not runtime). Coordinator sees table → applies judgment → records in `agent` field |
| D12 | 5 research activity categories (collapsed from 8 subtask types) | Web research, Code audit, Infra recon, Architecture synthesis, Data analysis. Collapsed: competitive analysis → web research, document review → any tool, prototype validation → code audit. 5 rows = scannable at a glance |

## Open Questions
| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q3 | Should tfw-init prompt users to document available tools? | Deferred | Out of scope for TFW-42. Natural candidate for future task — could enrich project KNOWLEDGE.md during init |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | Multi-agent orchestration needs `agent` field in iterations.yaml, not a separate mechanism | confirmed (iter 1) | ✅ extended | Iter 2 adds: the `agent` field is ACCOMPANIED by a capability table in conventions.md and a workflow reference in plan.md. The field alone is insufficient without guidance context |

## HL Update Recommendations
| # | What to update | Source |
|---|---------------|--------|
| R6 | §4 Phase A deliverables: add "Agent selection guidance subsection in conventions.md" | D8, D9, D12 |
| R7 | §4 Phase B deliverables: add "plan.md Step 6b — 1-sentence multi-agent reference" | D10 |
| R8 | §5 DoD: add "Conventions include agent selection guidance table (tool-agnostic)" | D8, D12 |
| R9 | §7 Principles: add P7 "Tool-agnostic guidance — capabilities not brands" | D8 |

## Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC5 | domain | 5 research activity categories in TFW: web research, code audit, infra recon, architecture synthesis, data analysis. Each maps to specific tool capabilities needed | Gather G2-G3, Extract E1 | ★★★ |
| FC6 | philosophy | Tool-agnosticism in guidance = describe capabilities needed, not tool names. Specific tool mapping is project-level knowledge, not framework convention | Challenge C4, D8 | ★★★ |
| FC7 | process | The complete coordinator multi-agent flow: plan.md trigger → conventions.md reference → iterations.yaml record → KNOWLEDGE.md accumulation. Mirrors TFW's general pattern: workflow → conventions → artifact → knowledge | Challenge C6 | ★★☆ |

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | philosophy | User asks «рекомендовать что-то или человек сам выбирает» — the answer is BOTH: framework provides a decision table (recommendation infrastructure), human makes the final choice. This is the TFW pattern across all artifacts: HL recommends phases, TS recommends approach, but coordinator/executor DECIDES. **Implication:** every TFW guidance mechanism should follow this pattern — provide decision context, not decisions. | User, iter 2 trigger | ★★★ |

> fact-candidates: processed 2026-04-30

## Findings Map

```
Agent guidance formalization
├── WHERE does guidance live?
│   ├── conventions.md §4 — capability table (5 rows, tool-agnostic)
│   ├── iterations.yaml template — commented-out `agent`/`sources` fields  
│   └── plan.md Step 6b — 1-sentence reference
│
├── WHAT does the table contain?
│   ├── Research activity → Key capability → Example tools (generic)
│   ├── 5 categories: web research, code audit, infra, synthesis, data
│   └── Footer: "guidance, not prescription"
│
├── HOW specific?
│   ├── Framework level: capability categories (stable)
│   └── Project level: tool-to-capability mapping (KNOWLEDGE.md, volatile)
│
└── WHO decides?
    ├── Human coordinator — always
    ├── Framework — provides decision table
    └── Never: automated suggestion (E5 rejected)
```

## Iteration Status

- **Iteration:** 2 of 2 (min) / 3 (max)
- **Hypotheses tested:** H1 (confirmed in iter 1, extended in iter 2 with guidance context)
- **Hypotheses deferred:** None
- **Gaps discovered:** Q3 (tfw-init tool documentation) — minor, deferred
- **Superseded decisions:** None (iter 2 extends iter 1, no conflicts)

### Open Threads (for next iteration)

No open threads.

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to update HL and write TS
- [ ] **MORE NEEDED** — {specify what and why}
- [ ] **BLOCKED** — {specify blocker}

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion
This iteration answered the user's question: "for which cases which agents are better, and how to formalize this." The answer is a two-tier capability-based guidance system: conventions.md provides a 5-row tool-agnostic capability table (research activity → key capability needed), while iterations.yaml template includes commented-out `agent`/`sources` fields. plan.md Step 6b adds a 1-sentence reference. The coordinator sees the table, applies judgment, and records the choice. Specific tool mapping (e.g., "Antigravity = web search + MCP") lives in project-level KNOWLEDGE.md, not in framework conventions — preserving TFW's tool-agnosticism. The total change footprint is ~20 lines across 3 files. Self-critique: the 5 research activity categories were derived primarily from one project (AFD-2). Additional projects would validate or expand this taxonomy. However, the design is intentionally minimal and extensible — categories can be added without structural changes.

---

*RES — iter2: Agent Guidance Formalization | 2026-04-30*
