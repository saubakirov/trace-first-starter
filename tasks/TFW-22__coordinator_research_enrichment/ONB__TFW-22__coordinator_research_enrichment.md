# ONB — TFW-22: Coordinator & Research Enrichment

> **Дата**: 2026-04-04
> **Автор**: Executor (AI)
> **Статус**: 🟠 ONB — Ожидает ответов
> **Parent HL**: [HL-TFW-22](HL-TFW-22__coordinator_research_enrichment.md)
> **TS**: [TS-TFW-22](TS__TFW-22__coordinator_research_enrichment.md)

---

## 1. Understanding (как понял задачу)

3-phase task to enrich coordinator/research workflows:
- **Phase A** — Add §3.1 (visualization) and §10 (RESEARCH justification) to HL template; add Hypotheses table and Sufficiency Verdict to RES template. 2 files modified, ≤50 LOC.
- **Phase B** — Refactor plan.md from info-dump to algorithm-first format: remove inline bloat (anti-patterns, scope budget table, status transitions, prerequisites), replace with ref-inside-step pattern. Add Step 5 (Hypothesis Iteration), strengthen RESEARCH Gate. Target ≤950 words. 3 files (plan.md + 2 adapters).
- **Phase C** — Replace monolithic research.md with modular `research/{base,focused,deep}.md`. OODA Stage Loop, Sufficiency Verdict, Trust Protocol, YAML-configurable modes. Delete old research.md. Update config sync registry. 3 new + 4 modified + 1 deleted = 8 files.

## 2. Entry Points (откуда начинать)

- `.tfw/templates/HL.md` (71 lines) — add §3.1 and §10
- `.tfw/templates/RES.md` (136 lines) — add Hypotheses + Sufficiency Verdict
- `.tfw/workflows/plan.md` (175 lines, ~1213 words) — full algorithm refactor
- `.tfw/workflows/research.md` (162 lines, ~1165 words) — to be replaced by directory
- `.tfw/PROJECT_CONFIG.yaml` (94 lines) — add research modes
- `.tfw/workflows/config.md` (104 lines) — update sync registry
- `.agent/workflows/tfw-plan.md`, `.agent/workflows/tfw-research.md` — adapter sync
- `.claude/commands/tfw-plan.md`, `.claude/commands/tfw-research.md` — adapter sync

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | Claude Code adapter `tfw-plan.md` (`.claude/commands/tfw-plan.md`, 165 lines) differs from `.tfw/workflows/plan.md` (175 lines) — lines 112-128 (Scope Budget section) have 3 lines of rationale text instead of the table. Which version is canonical? I'll sync both to the new refactored version, but want to confirm: `.tfw/workflows/plan.md` is the source of truth and adapters are copies? | Да. `.tfw/workflows/plan.md` = source of truth. Adapters = copies. Drift в claude adapter = known issue, Phase B resolves it. Sync both adapters to новый refactored plan.md. |
| 2 | TS Step C6 says "Update config.md sync registry: change `research.md` → `research/base.md`". The current registry has 4 entries pointing to `research.md`. After refactoring, the Limits table moves into base.md. Should I also add new registry entries for `tfw.research.default_mode` and `tfw.research.modes.*` settings, even though those values appear only in YAML (no inline display)? Or only update paths for existing entries? | Да, добавь новые entries для `default_mode` и `modes.*`. Если значение из YAML читается в workflow шаге (Step 2: read default_mode) — оно должно быть в registry. Даже если no inline display. Registry = "what YAML keys are consumed where". |

## 4. Recommendations (suggestions, not blocking)

1. **Word count verification method**: TS says "count words" but doesn't specify how. I'll use `wc -w` on the markdown file content (excluding YAML frontmatter). This is consistent with how P10 was established in TFW-21.
2. **Phase ordering is optimal**: A→B→C is correct — templates first (B/C reference them), plan.md before research.md (plan.md references research workflow path).

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Adapter inconsistency**: `.claude/commands/tfw-plan.md` already differs from `.tfw/workflows/plan.md` in the Scope Budget section. After Phase B, both adapters will be synced to the new refactored plan.md — this resolves it, but worth noting the pre-existing drift.
2. **Config Sync Registry path change**: After Phase C, `research.md` path in the sync registry becomes `research/base.md`. If any other files (conventions.md §8, README.md) reference `research.md` by path, those refs will break. I'll check and report in Observations.
3. **`tfw.workflows.research` in PROJECT_CONFIG.yaml**: TS Step C7 changes this to `research/base.md`. The `config.md` Adapter Sync section line 91 also has `cp .tfw/workflows/research.md .agent/workflows/tfw-research.md`. After refactoring, the copy command path must also update.

## 6. Inconsistencies with Code (spec vs reality)

1. TS Step B5 says copy plan.md to `.agent/workflows/tfw-plan.md` and `.claude/commands/tfw-plan.md`. But the `.claude/commands/tfw-plan.md` already differs from source — it was manually edited with different Scope Budget text (lines 112-116 have prose instead of table). This is an existing inconsistency that the TS correctly resolves by syncing.
2. TS §3C lists `config.md` as MODIFY but the Adapter Sync section of `config.md` (line 91) still has `cp .tfw/workflows/research.md` — this also needs updating to `research/base.md`. Not explicitly called out in TS steps but logically implied.

---

*ONB — TFW-22: Coordinator & Research Enrichment | 2026-04-04*
