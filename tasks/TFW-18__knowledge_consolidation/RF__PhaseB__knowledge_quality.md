# RF — TFW-18 / Phase B: Knowledge Quality

> **Дата**: 2026-04-03
> **Автор**: Executor (AI)
> **Статус**: 🟢 RF — Выполнено
> **Parent HL**: [HL Phase B](HL__PhaseB__knowledge_quality.md)
> **TS**: [TS Phase B](TS__PhaseB__knowledge_quality.md)

---

## 1. Что сделано

### Новые файлы
| Файл | Описание |
|------|----------|
| `ONB__PhaseB__knowledge_quality.md` | Executor onboarding report (0 blocking questions) |

### Изменённые файлы
| Файл | Изменения |
|------|----------|
| `.tfw/templates/RF.md` | §6 FC: reframed «project knowledge → strategic knowledge», swapped anti-patterns for good/bad examples |
| `.tfw/templates/REVIEW.md` | §5 FC: same reframe as RF.md |
| `.tfw/templates/RES.md` | §FC: same reframe + kept «THIS project» filter, added tfw-docs redirect for impl details |
| `.tfw/workflows/research.md` | §Closure L110: one-line reframe to strategic knowledge |
| `.tfw/workflows/handoff.md` | L81-87: leads with «stakeholder priorities, domain patterns» instead of «environment, constraints» |
| `.tfw/conventions.md` | §10.1: expanded category examples (domain→revenue patterns/client segments, stakeholder→priorities/pain points, constraint→contractual obligations, etc.) |
| `.tfw/workflows/knowledge.md` | Phase 2: «strategic knowledge», mentions «decisions, emotions, data», redirects tech details to tfw-docs |
| `.tfw/README.md` | §v3: added Knowledge consolidation bullet; workflows table: added knowledge + config rows |
| `.agent/workflows/tfw-research.md` | Synced from canonical (cp) |
| `.agent/workflows/tfw-handoff.md` | Synced from canonical (cp) |
| `.agent/workflows/tfw-knowledge.md` | Synced from canonical (cp) |

## 2. Ключевые решения

1. **Exact TS text used**: All replacement text taken verbatim from TS Steps 1-8. No deviations.
2. **Adapter sync via cp**: Same method as Phase A (byte-identical copies). 3 adapters synced.

## 3. Acceptance Criteria

- [x] RF.md FC prompt says «strategic knowledge» not «next agent's behavior»
- [x] REVIEW.md FC prompt matches RF.md
- [x] RES.md FC prompt same reframe + keeps «THIS project» filter
- [x] research.md §Closure FC bullet reframed
- [x] handoff.md FC guidance leads with «stakeholder priorities, domain patterns»
- [x] conventions.md §10.1 `domain` examples include: revenue patterns, client segments, market metrics
- [x] conventions.md §10.1 `stakeholder` examples include: priorities, pain points, quotes
- [x] knowledge.md Phase 2 says «strategic knowledge» and mentions «decisions, emotions, data»
- [x] .tfw/README.md §v3 lists Knowledge consolidation
- [x] .tfw/README.md workflows table includes knowledge and config
- [x] All 3 adapters synced (diff = 0)
- [x] No file exceeds P10 word limit after changes (research.md: 1165w, knowledge.md: 718w)
- [x] Anti-pattern examples include «implementation details» as NOT-FC

## 4. Верификация

- Lint (`echo "configure your lint command"`): N/A (markdown files only)
- Tests (`echo "configure your test command"`): N/A (markdown files only)
- Verify: All grep/diff checks passed:
  - `strategic knowledge` found in RF.md, REVIEW.md, RES.md, research.md, knowledge.md
  - `next agent's behavior` count = 0 in RF.md, REVIEW.md
  - `revenue patterns` and `priorities, pain points` found in conventions.md
  - `Knowledge consolidation` found in README.md
  - All 3 adapters: diff = 0
  - Word counts: research.md 1165w (≤1200), knowledge.md 718w (≤1200)

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/README.md` | 77 | todo | Workflows table in §Project Structure tree still lists old set `(plan, research, handoff, review, resume, docs, release, update)` — doesn't include knowledge/config. Only the table in §Canonical Workflows was updated per TS scope |
| 2 | `.tfw/workflows/review.md` | — | style | review.md also has a FC mindset reminder (added in Phase A) but was not in scope for Phase B reframe — still uses old «project knowledge» framing |

> **Types:** `dead-code`, `naming`, `todo`, `duplication`, `perf`, `security`, `style`, `missing-test`, `ux`

## 6. Fact Candidates

> **Before writing Fact Candidates, review the conversation history.** The human's
> messages are the primary source of strategic knowledge — domain insights, stakeholder
> priorities, business context, and constraints that shape decisions.
>
> Good: "18% clients = 80% revenue (Pareto)", "stakeholder: find problem clients first"
> NOT fact candidates: "project uses git", "code is in Python", implementation details (→ §5 Observations → tfw-docs)
> These are NOT verified facts. They become facts after `/tfw-knowledge` consolidation.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | process | Phase B "knowledge quality" reframe was a pure text-edit task (0 new files, 8 modifications, ~120 words) — this size is optimal for single-session executor completion | Execution timing | Medium |
| 2 | convention | The `.tfw/README.md` has two places listing workflows: a tree in §Project Structure (L77) and a table in §Canonical Workflows (L161-172). Both need updating when workflows change — easy to miss the tree | Observation #1 during execution | High |

> **Categories** (open list): `environment`, `process`, `stakeholder`, `constraint`, `convention`, `domain`, `context`, `risk`

---

*RF — TFW-18 / Phase B: Knowledge Quality | 2026-04-03*
