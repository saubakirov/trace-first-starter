# HL — TFW-18 / Phase B: Knowledge Quality — Strategic vs Technical

> **Дата**: 2026-04-03
> **Автор**: Coordinator (AI)
> **Статус**: 📝 HL_DRAFT — Approved
> **Parent HL**: [HL-TFW-18](HL-TFW-18__knowledge_consolidation.md)

---

## 1. Проблема

TFW-18 Phase A built knowledge infrastructure. Infrastructure works. Content quality is wrong: agents collect technical gotchas instead of strategic knowledge.

**Evidence** (LEE project): 14 fact candidates — best ones (ABC Pareto, churn patterns, stakeholder priorities) came from chat history. Templates say «Extract what would change the next agent's behavior» → agents interpret as API limits, file encoding, config quirks.

**Root cause**: Two knowledge systems conflated:

| System | Purpose | What it captures |
|--------|---------|-----------------|
| **tfw-docs** | Technical reference | Architecture, decisions, conventions |
| **tfw-knowledge** | Strategic intelligence | Domain patterns, stakeholder priorities, business context |

Templates guide toward tfw-docs material. Strategic knowledge leaks through chat and gets lost.

## 2. Решение

Reframe Fact Candidates guidance across all templates and workflows. One core change applied to 8 locations:

**Current**: «Extract what would change the next agent's behavior»
**New**: «Extract strategic knowledge — domain patterns, stakeholder priorities, business context. Technical observations → §Observations → tfw-docs»

## 3. Scope

| # | File | Change | Word impact |
|---|------|--------|-------------|
| 1 | `.tfw/templates/RF.md` §6 | Reframe FC prompt + swap examples | +15 |
| 2 | `.tfw/templates/REVIEW.md` §5 | Same reframe | +15 |
| 3 | `.tfw/templates/RES.md` §FC | Same reframe + keep «THIS project» filter | +10 |
| 4 | `.tfw/workflows/research.md` §Closure L110 | One-line reframe | +5 |
| 5 | `.tfw/workflows/handoff.md` L81-87 | Reorder list + reframe | +5 |
| 6 | `.tfw/conventions.md` §10.1 | Expand category examples | +20 |
| 7 | `.tfw/workflows/knowledge.md` Phase 2 | Sharpen gather guidance | +10 |
| 8 | `.tfw/README.md` | Add knowledge to §v3 + workflows table | +40 |

**Budget**: 0 new, 8 modified. +120 words total. All files stay within P10 limits.

## 4. Philosophy

| # | Principle |
|---|-----------|
| P1 | tfw-docs = technical reference. tfw-knowledge = strategic intelligence. Don't mix. |
| P2 | Most valuable knowledge = chat history. Templates must guide agents to look there for strategic, not technical. |
| P3 | Domain-agnostic: examples must cover business, education, engineering — any domain. |

---

*HL — TFW-18 / Phase B: Knowledge Quality | 2026-04-03*
