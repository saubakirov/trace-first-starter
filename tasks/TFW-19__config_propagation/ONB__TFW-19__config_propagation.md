# ONB — TFW-19: Config Propagation

> **Дата**: 2026-04-03
> **Автор**: Executor (AI)
> **Статус**: 🟠 ONB — Ожидает ответов
> **Parent HL**: [HL-TFW-19](HL-TFW-19__config_propagation.md)
> **TS**: [TS-TFW-19](TS__TFW-19__config_propagation.md)

---

## 1. Understanding (как понял задачу)

TFW-12 centralized config values into PROJECT_CONFIG.yaml but used Pattern B (pure reference: "see config"). This broke agent compliance — agents stopped reading the config file and simply ignored scope budgets. TFW-19 restores Pattern A (inline defaults + config key) across all enforcement-critical docs, creates an interactive `/tfw-config` workflow for keeping inline values synchronized with YAML, and resolves TD-48.

## 2. Entry Points (откуда начинать)

| File | Current State | Action |
|------|--------------|--------|
| `.tfw/workflows/plan.md` L112-118 | "See config" reference, no inline values | Restore compact budget table, add enforcement hook |
| `.tfw/conventions.md` L150-153 | "See config" reference only | Restore full budget table with Rationale column |
| `.tfw/workflows/knowledge.md` | No §Limits section at all | Add compact limits table |
| `.tfw/templates/TS.md` L27 | "Лимиты — см. `tfw.scope_budgets`..." | Replace with inline defaults format |
| `.tfw/workflows/research.md` L142 | Missing "defaults" wording | Add standard defaults header |
| `.tfw/workflows/config.md` | Does not exist | Create with edit/verify + Config Sync Registry |
| `.agent/workflows/tfw-config.md` | Does not exist | Create adapter copy |
| `.tfw/glossary.md` | Missing Config Sync Registry term | Add after Consolidation |
| `.agent/workflows/tfw-plan.md` | Adapter copy — stale | Sync with canonical plan.md |
| `.agent/workflows/tfw-research.md` | Adapter copy — stale | Sync with canonical research.md |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | TS Step 11 says "Resolve TD-48 (Naming Rules removed from plan.md in this task)." But plan.md already has NO Naming Rules table (grep returns 0 results). Should I just mark TD-48 as ✅ Resolved in TECH_DEBT.md with a note that the content was already absent? | ✅ Yes. Naming Rules were removed by the coordinator during this session (before TS). Mark TD-48 = ✅ Resolved. |
| 2 | The adapter `.agent/workflows/tfw-plan.md` has a **duplicate YAML frontmatter** (lines 1-3 and 5-7 both have `description: TFW Plan...`). This is out of scope per TS (I won't fix it), but the adapter sync in Step 10 will overwrite this file entirely with the canonical plan.md content — that will fix the duplication as a side effect. Is this acceptable, or should I preserve the current adapter file and only patch the budget section? | ✅ Full overwrite via `cp` is the correct approach. Adapters are byte-copies of canonical (see F1 in knowledge/convention.md). Duplicate frontmatter will be fixed as side effect. |

## 4. Recommendations (suggestions, not blocking)

1. **Standard defaults header consistency**: TS Step 6 introduces a 2-line header for research.md, but knowledge.md (Step 4) already uses the same 2-line pattern in its code block. I recommend using the **exact same 2-line header** across all 4 files (plan.md, conventions.md, knowledge.md, research.md) for maximum consistency:
   ```
   > Configured in `.tfw/PROJECT_CONFIG.yaml` (`tfw.{section}`).
   > Values below are defaults. Override in PROJECT_CONFIG for your project.
   ```
2. **Config Sync Registry completeness**: TS §Step 7 says registry must cover `scope_budgets.*`, `research.*`, `knowledge.*`. The TS.md template (Step 5) also gets an inline defaults line — should TS.md template also be in the registry? It references budget values indirectly (as placeholders). I'll include it for completeness.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **conventions.md §5 AC**: AC #5 says "conventions.md §4 has multi-phase subfolder structure" — but conventions.md already has this at L98-114. This AC item appears to be a pre-existing condition, not something to implement. I'll verify it's present and mark it as satisfied.
2. **plan.md enforcement hook placement**: TS says "Before «Write TS»" — this is L94 area (Phase 5 header). The hook should go right after the "After HL is approved..." sentence but before the "Small task" subsection, since the budget check applies to both small and large tasks.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS L53 says "Replace L133-137"** for plan.md, but the actual "See config" block is at **L112-118** in the current file. Line numbers drifted. I'll target the correct content by matching text, not line numbers.
2. **TS L83 says "Replace L132-135"** for conventions.md, but the "See config" block is at **L150-153** in the current file. Same line drift. Will use content matching.
3. **TS L119 says "Replace L27"** in TS.md template — current L27 reads `**Бюджет:** {N} новых файлов, {M} модификаций. Лимиты — см. \`tfw.scope_budgets\` в \`.tfw/PROJECT_CONFIG.yaml\`.` — this is correct, will replace.
4. **TS L129 says "Replace L142"** in research.md — current L142 reads `> Research limits are configured in...` — correct target line.

---

*ONB — TFW-19: Config Propagation | 2026-04-03*
