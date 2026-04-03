# RF — TFW-19: Config Propagation

> **Дата**: 2026-04-03
> **Автор**: Executor (AI)
> **Статус**: 🟢 RF — Выполнено
> **Parent HL**: [HL-TFW-19](HL-TFW-19__config_propagation.md)
> **TS**: [TS-TFW-19](TS__TFW-19__config_propagation.md)

---

## 1. Что сделано

### Новые файлы
| Файл | Описание |
|------|----------|
| `.tfw/workflows/config.md` | Interactive config sync workflow with edit/verify modes and Config Sync Registry (3 categories, 16 mapped keys) |
| `.agent/workflows/tfw-config.md` | Antigravity adapter copy of config.md |

### Изменённые файлы
| Файл | Изменения |
|------|----------|
| `.tfw/workflows/plan.md` | Restored 4-row inline budget table (Pattern A compact), added Budget Check enforcement hook before Phase 5 TS writing |
| `.tfw/conventions.md` | Restored 4-row inline budget table with Rationale column in §6; added config.md to §8 Workflows table and §15 Role Lock table |
| `.tfw/workflows/knowledge.md` | Added §Limits section with 4-row compact table (interval, gate_mode, max_facts_per_topic, max_topic_files) |
| `.tfw/templates/TS.md` | Replaced L27 budget line with inline defaults format: `Defaults: max {max_files} files, max {max_new} new, max {max_loc} LOC.` |
| `.tfw/workflows/research.md` | Replaced L142 with standard 2-line defaults header (`Configured in...` + `Values below are defaults...`) |
| `.tfw/glossary.md` | Added Config Sync Registry term after Consolidation |
| `.agent/workflows/tfw-plan.md` | Full adapter sync (also fixed pre-existing duplicate YAML frontmatter as side effect) |
| `.agent/workflows/tfw-research.md` | Full adapter sync |
| `.agent/workflows/tfw-knowledge.md` | Full adapter sync (new §Limits propagated) |
| `TECH_DEBT.md` | Marked TD-48 as ✅ Resolved (Naming Rules already absent from plan.md) |
| `README.md` | Task board: TFW-19 status 🟡 TS_DRAFT → 🟢 RF, added ONB and RF links |

## 2. Ключевые решения

1. **Standard 2-line defaults header** applied consistently across all 4 target files: `> Configured in... > Values below are defaults...` — established as the canonical format for all inline config tables.
2. **Enforcement hook placement** — added before both "Small task" and "Large task" subsections in Phase 5, so the budget check applies universally regardless of task size.
3. **TD-48 resolution** — confirmed Naming Rules table was already absent from plan.md (removed by coordinator during TFW-19 planning session). Marked as resolved with note.
4. **Adapter sync strategy** — full `cp` overwrite for all modified workflows, per F1 convention (adapters = byte-copies). Fixed duplicate frontmatter in tfw-plan.md as a side effect.

## 3. Acceptance Criteria

- [x] plan.md has inline budget table with 4 rows matching PROJECT_CONFIG values
- [x] plan.md has enforcement hook in Phase 5
- [x] plan.md does NOT contain Naming Rules table (TD-48)
- [x] conventions.md §6 has inline budget table with 4 rows + Rationale column
- [x] conventions.md §4 has multi-phase subfolder structure (pre-existing, verified at L98-114)
- [x] knowledge.md has §Limits table with 4 rows
- [x] TS.md template L27 has inline defaults format
- [x] research.md Limits header says «defaults»
- [x] config.md workflow exists with edit + verify modes + Config Sync Registry
- [x] Config Sync Registry covers all 3 config categories (scope_budgets: 8 entries, research: 4 entries, knowledge: 4 entries)
- [x] conventions.md §8 lists config.md, §15 has config.md Role Lock
- [x] glossary.md has Config Sync Registry term
- [x] Antigravity adapter `tfw-config.md` exists
- [x] All adapters synced (plan, research, config, knowledge)
- [x] All inline values match current PROJECT_CONFIG.yaml values (14, 8, 1200, 12, 5, 3, 50, 8, hard, 3, 5, 15)

## 4. Верификация

- Lint (`echo "configure your lint command"`): PASS (meta-project placeholder)
- Tests (`echo "configure your test command"`): PASS (meta-project placeholder)
- Verify (`echo "configure your verify command"`): PASS (meta-project placeholder)

Grep verification:
```
grep "14" plan.md → L123: Files per phase | 14 ✅
grep "1200" plan.md → L125: LOC per phase | 1200 ✅
grep "Budget Check" plan.md → L92 ✅
grep -c "Naming Rules" plan.md → 0 ✅
grep "Rationale" conventions.md → L155 ✅
grep "50" knowledge.md → L116: Max facts per topic | 50 ✅
grep "defaults" research.md → L143 ✅
ls config.md → exists (4704 bytes) ✅
ls tfw-config.md → exists (4704 bytes) ✅
grep "config.md" conventions.md → 2 hits (§8 + §15) ✅
grep "Config Sync Registry" glossary.md → 1 hit ✅
```

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/conventions.md` | L38 | style | §2 Required Artifacts doesn't list `config.md` workflow — consistent with how only the "original 10" are listed, but diverges from §8 which now lists 11 workflows |
| 2 | `.tfw/PROJECT_CONFIG.yaml` | L29-39 | style | `tfw.workflows` section doesn't include `config: .tfw/workflows/config.md` — needs adding for consistency |
| 3 | `.tfw/conventions.md` | L201-208 | naming | §10.1 numbering (10.1, 10.2, 10) breaks flat scheme — pre-existing TD-45, confirmed still present |

## 6. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | convention | Adapter files are byte-copies of canonical `.tfw/workflows/` files — full `cp` overwrite is the correct sync method, not patching. Verified by F1 in `knowledge/convention.md` and user confirmation in ONB Q2 | ONB Q2 answer, knowledge/convention.md F1 | High |
| 2 | convention | Pattern A (inline defaults + config key) is the standard for enforcement-critical values. Pattern B (pure reference) proven to break agent compliance in TFW-12→TFW-19 cycle. Standard 2-line header: `> Configured in... > Values below are defaults...` | HL-TFW-19 §3, RES-TFW-19 | High |
| 3 | process | TS line numbers drift between writing and execution — content matching is more reliable than line-number targeting. All 4 TS line references in this task were stale (plan.md: L133→L112, conventions.md: L132→L150, TS.md: L27 correct, research.md: L142 correct) | ONB §6 Inconsistencies | Medium |

---

*RF — TFW-19: Config Propagation | 2026-04-03*
