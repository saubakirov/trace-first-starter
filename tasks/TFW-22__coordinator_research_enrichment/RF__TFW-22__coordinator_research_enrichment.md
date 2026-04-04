# RF — TFW-22: Coordinator & Research Enrichment

> **Дата**: 2026-04-04
> **Автор**: Executor (AI)
> **Статус**: 🟢 RF — Выполнено
> **Parent HL**: [HL-TFW-22](HL-TFW-22__coordinator_research_enrichment.md)
> **TS**: [TS-TFW-22](TS__TFW-22__coordinator_research_enrichment.md)

---

## 1. Что сделано

### Новые файлы
| Файл | Описание |
|------|----------|
| `.tfw/workflows/research/base.md` | Core research algorithm: OODA Stage Loop, Sufficiency Verdict, Trust Protocol, modular mode loading (504 words) |
| `.tfw/workflows/research/focused.md` | Focused mode: single-pass, generic criteria only (106 words) |
| `.tfw/workflows/research/deep.md` | Deep mode: multi-loop, hypothesis-driven, metacognitive check (171 words) |

### Изменённые файлы
| Файл | Изменения |
|------|----------|
| `.tfw/templates/HL.md` | +§3.1 «Визуализация результата» (ascii mandatory, mermaid optional), +§10 «Обоснование RESEARCH» (гипотезы, слепые зоны, риски, фокус) |
| `.tfw/templates/RES.md` | +Hypotheses table в Briefing (linked to HL §10), +Sufficiency Verdict в каждом stage checkpoint (generic + mode-specific) |
| `.tfw/workflows/plan.md` | Full algorithm refactor: 1213→781 words (-36%). Inline bloat → ref-inside-step. +Step 4c (§3.1, §10), +Step 5 (Hypothesis Iteration), +strengthened RESEARCH Gate (Step 6). DNA layer inline |
| `.tfw/PROJECT_CONFIG.yaml` | +`tfw.research.default_mode: focused`, +`modes.focused` (loops_per_stage: 1), +`modes.deep` (loops_per_stage: 3, require_counter_evidence: true). workflow path → `research/base.md` |
| `.tfw/workflows/config.md` | Sync registry: `research.md` → `research/base.md` (4 entries), +3 new entries (default_mode, focused.loops, deep.loops). Adapter sync command updated |
| `CLAUDE.md` | research workflow path → `research/base.md` |
| `KNOWLEDGE.md` | P8 path reference → `research/base.md` |
| `.agent/workflows/tfw-plan.md` | Synced (exact copy of plan.md) |
| `.agent/workflows/tfw-research.md` | Synced (exact copy of base.md) |
| `.claude/commands/tfw-plan.md` | Synced (exact copy of plan.md) |
| `.claude/commands/tfw-research.md` | Synced (exact copy of base.md) |

### Удалённые файлы
| Файл | Причина |
|------|---------|
| `.tfw/workflows/research.md` | Replaced by `research/` directory (base + focused + deep) |

## 2. Ключевые решения

1. **base.md compressed to 504 words** (target was ≤600). Removed Stage Descriptions section — agent gets stage identities from `templates/RES.md` (each stage has its title + blockquote prompt). This follows the template-owns-format pattern (D23/TFW-21).
2. **plan.md at 781 words** (target ≤950, original 1213). Removed: Prerequisites list (→ Step 1), Scope Budget table (→ Step 7b), Status Transitions diagram (→ ref conventions.md §5), Anti-patterns block (→ Footer self-check), Approval Gates section (→ implicit in GATE/WAIT points).
3. **CLAUDE.md and KNOWLEDGE.md path updates** — outside TS file scope but necessary to prevent broken references. These are live reference documents, not historical task artifacts.
4. **Config Sync Registry** — added 3 new entries for default_mode and modes.* as per user answer to blocking Q2. Registry now serves as "what YAML keys are consumed where" — not limited to inline display.

## 3. Acceptance Criteria

### Phase A: Templates
- [x] HL template содержит §3.1 с инструкцией по визуализации (ascii mandatory)
- [x] HL template содержит §10 с таблицей гипотез, слепыми зонами, рисками незнания, фокусом
- [x] RES template содержит Hypotheses table в Briefing
- [x] RES template содержит Sufficiency Verdict формат в checkpoint

### Phase B: plan.md Refactor
- [x] plan.md contains Role Lock + Mindset as inline header (DNA layer)
- [x] No inline Anti-patterns block (replaced with ref-inside-step in footer)
- [x] No inline Status Transitions (replaced with ref)
- [x] No inline Prerequisites list (replaced with Step 1)
- [x] No inline Scope Budget table (replaced with Step 7b)
- [x] Step 4c requires §3.1 and §10
- [x] Step 5: Hypothesis Iteration exists with FOR EACH loop
- [x] Step 6: RESEARCH Gate references §10
- [x] Word count ≤ 950 (actual: 781)
- [x] Both adapters synced

### Phase C: research/ Directory
- [x] `research/base.md` exists, ≤600 words (actual: 504), contains OODA Stage Loop
- [x] `research/focused.md` exists, ≤200 words (actual: 106), contains focused mode settings
- [x] `research/deep.md` exists, ≤250 words (actual: 171), contains deep mode + metacognitive check
- [x] Old `research.md` deleted
- [x] `PROJECT_CONFIG.yaml` has `default_mode` and `modes.{focused,deep}` with numeric/boolean settings
- [x] Sufficiency Verdict format in base.md (2-level: generic + mode-specific)
- [x] Checkpoint criteria = SOFT (report, not block). loops_per_stage = HARD LIMIT
- [x] Trust Protocol table in base.md
- [x] Config sync registry updated (paths + 3 new entries)
- [x] Both adapters synced with base.md content

## 4. Верификация

- Lint: N/A (markdown documentation, no code)
- Tests: N/A (no executable code)
- Verify:
  - All files exist: ✅
  - Old research.md deleted: ✅
  - Adapter sync (diff): ✅ plan.md = tfw-plan.md = claude tfw-plan.md, base.md = tfw-research.md = claude tfw-research.md
  - Word counts: plan.md=781 (≤950 ✅), base.md=504 (≤600 ✅), focused.md=106 (≤200 ✅), deep.md=171 (≤250 ✅)
  - base+focused=624 < 1165 (old) ✅, base+deep=689 < 1165 (old) ✅
  - Broken refs: CLAUDE.md and KNOWLEDGE.md updated. Historical task artifacts (HL/TS/RF of past tasks) intentionally not modified — they are traces.

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `conventions.md` | 181 | style | Workflows table row still says `research.md` in the Purpose column: `Structured investigation → RES artifact`. Path is not a direct reference (it's the table row for research.md workflow) but may cause confusion. The `tfw.workflows.research` in PROJECT_CONFIG.yaml was updated to `research/base.md`. |
| 2 | `conventions.md` | 277 | style | Role Lock table row for `handoff.md` lists `code` in Forbidden Artifacts. Handoff workflow itself says "For code changes: write production-ready code" (line 64). The "code" entry in forbidden column may be a legacy from before executor was allowed to write code via handoff. Contradicts the handoff workflow intent. |

## 6. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | convention | Config Sync Registry semantics expanded: entries cover all YAML keys consumed in workflows, not just inline display values. "What YAML keys are consumed where" is the registry purpose. | User answer to ONB Q2 | High |
| 2 | convention | `.tfw/workflows/plan.md` is always source of truth for adapters. Adapter drift in `.claude/commands/` is a known issue, resolved by copy-on-modify at end of each phase. | User answer to ONB Q1 | High |

---

> fact-candidates: processed 2026-04-04

*RF — TFW-22: Coordinator & Research Enrichment | 2026-04-04*
