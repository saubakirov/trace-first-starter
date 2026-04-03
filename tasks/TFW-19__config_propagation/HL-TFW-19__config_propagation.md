# HL — TFW-19: Config Propagation

> **Дата**: 2026-04-03
> **Автор**: Coordinator (AI)
> **Статус**: 📝 HL_DRAFT — Обновлён после RESEARCH
> **Предыдущая задача**: TFW-12 (Config Centralization)
> **RESEARCH**: [RES-TFW-19](RES__TFW-19__config_propagation.md) — подтвердил подход

---

## 1. Проблема

TFW-12 централизовал config → Pattern B (pure reference «see config») → **агенты перестали соблюдать scope budgets**. RESEARCH-12 предупреждал: Pattern A лучше. User оверрайднул. Практика подтвердила: RESEARCH был прав.

## 2. Constraints

1. **No scripts** — TFW = чисто AI prompt framework. Workflows = automation.
2. **Universal** — работает на любом компе, в любом AI tool.
3. **Plain text** — файлы читаемы без tools.
4. **Token density** — минимум слов для максимума enforcement (P10: ≤1200 words per workflow).

## 3. Решение

### Pattern A: Inline Defaults + Config Key

Стандартный формат (эталон = research.md Limits table):

```markdown
> Configured in `.tfw/PROJECT_CONFIG.yaml` (`tfw.{section}`).
> Values below are defaults. Override in PROJECT_CONFIG for your project.

| Parameter | Default | Config key |
|-----------|---------|------------|
| ... | ... | `key_name` |
```

**Rationale column** — только в `conventions.md` (canonical description). Остальные файлы = compact.

### tfw-config: Interactive AI Workflow

Два режима:

**Edit mode** (primary):
```
User: /tfw-config
Agent: "Что хотите изменить в конфигурации?"
User: "scope budget max_files до 10"
Agent: reads YAML → finds all inline locations → proposes batch update:
  - PROJECT_CONFIG.yaml: 14→10
  - plan.md table: 14→10
  - conventions.md table: 14→10
  - TS.md defaults: 14→10
  "Применить? (4 файла)"
User: "да"
Agent: updates files + syncs adapters
```

**Verify mode**:
```
User: /tfw-config verify
Agent: reads YAML + all inline tables → reports mismatches or "all in sync"
```

### Config Sync Registry

Таблица внутри `config.md` workflow — mapping config key → file location:

| Config Key | Target File | Section Header |
|------------|------------|----------------|
| `scope_budgets.max_files_per_phase` | plan.md | Scope Budget per Phase |
| `scope_budgets.max_files_per_phase` | conventions.md | 6) Scope Budgets |
| `scope_budgets.max_loc` | plan.md | Scope Budget per Phase |
| `research.max_questions_per_turn` | research.md | Limits |
| `knowledge.max_facts_per_topic` | knowledge.md | Limits |
| ... | ... | ... |

AI agent: read registry → open file → find section → find table row → compare → update.

## 4. Scope

### Phase A: Restore Inline Values

| Target | Section | Action |
|--------|---------|--------|
| plan.md | §Scope Budget per Phase | Restore 4-row table (compact) |
| conventions.md | §6 Scope Budgets | Restore 4-row table (full, with Rationale) |
| knowledge.md | New §Limits section | Add 4-row table (compact) |
| TS.md template | L27 budget line | Replace with inline defaults |
| research.md | §Limits | Restore «defaults» wording header |
| plan.md | Phase 5 | Add enforcement hook: read config, verify phase fits budget |

### Phase B: tfw-config Workflow

| Deliverable | Description |
|-------------|-------------|
| `.tfw/workflows/config.md` | Workflow with edit/verify modes + Config Sync Registry |
| `.agent/workflows/tfw-config.md` | Antigravity adapter |
| conventions.md | Add config.md to §8 Workflows, §15 Role Lock |
| glossary.md | Add Config Sync Registry term |

## 5. Принципы (confirmed by RESEARCH)

| # | Principle |
|---|-----------|
| P1 | Enforcement values MUST be inline — indirection kills agent compliance |
| P2 | Single source of truth ≠ single place of display. Config is authoritative, inline is rendered |
| P3 | No scripts — AI agent is the execution engine |
| P4 | RESEARCH recommendations exist for a reason (TFW-12 lesson) |

---

*HL — TFW-19: Config Propagation | 2026-04-03*
