# HL — TFW-19: Config Propagation

> **Дата**: 2026-04-03
> **Автор**: Coordinator (AI)
> **Статус**: 📝 HL_DRAFT — Ожидает ревью
> **Предыдущая задача**: TFW-12 (Config Centralization)

---

## 1. Проблема

TFW-12 централизовал configurable values в `PROJECT_CONFIG.yaml`. Но выбранный Pattern B (pure reference — «see config») **сломал agent enforcement**: агенты перестали видеть scope budgets inline и перестали их соблюдать.

**Root cause analysis:**

| Factor | Impact |
|--------|--------|
| Pattern B удалил числа из plan.md, conventions.md | Агенты видят «see config» вместо `≤ 7 files` — нет визуального якоря |
| «See config» = indirection | Лишний read в середине workflow. Агент может не перейти |
| Числа не закрепляются | Даже если агент прочитал config, числа стираются из memory через 2-3 шага |
| RESEARCH-12 предупреждал | R3/C1/C7: «Pattern A (values + pointer) > Pattern B для readability». User оверрайднул |

**Deeper issue**: даже если вернуть Pattern A — при смене конфига нужно руками менять N файлов. Без механизма синхронизации дрифт неизбежен.

## 2. Constraints

1. **No scripts** — TFW = чистый AI prompt framework. Нет bash, python, build tools. Только markdown workflows, которые AI agent исполняет.
2. **Universal** — работает на любом компе, у всех, в любом AI tool (Claude Code, Cursor, Antigravity).
3. **Plain text** — файлы всегда читаемы без tools. Нет compiled output, нет magic markers.
4. **All limits inline** — scope budgets, research limits, knowledge limits. Всё что агент должен соблюдать.

## 3. Варианты решения

### ~~Variant A: Render Pipeline~~ ❌

Build step = scripts. Нарушает constraint #1.

### ~~Variant C: Context Loading Mandate~~ ❌

Уже доказано что не работает. TFW-12 ссылается на config, агенты игнорируют.

### Variant B: Pattern A + AI-driven sync

Inline values (Pattern A) + AI workflow `/tfw-config` для синхронизации.

`tfw-config` = AI agent reads YAML → reads target files → compares inline values с config → proposes changes → user approves.

### Variant D: B + enforcement hooks

Всё из B + mandatory budget check в plan.md Phase 5 и research.md entry.

## 4. Решение: Variant D

### Механизм: Config Sync Registry

`tfw-config` workflow содержит **Config Sync Registry** — таблицу, mapping config keys → file locations:

```markdown
## Config Sync Registry

| Config Key | Target File | Section Header | Row Label | Current |
|------------|------------|----------------|-----------|---------|
| scope_budgets.max_files_per_phase | .tfw/workflows/plan.md | Scope Budget per Phase | Files per phase | 14 |
| scope_budgets.max_files_per_phase | .tfw/conventions.md | 6) Scope Budgets | Files per phase | 14 |
| scope_budgets.max_loc | .tfw/workflows/plan.md | Scope Budget per Phase | LOC per phase | 1200 |
| research.max_questions_per_turn | .tfw/workflows/research.md | Limits | Questions per turn | 3 |
| knowledge.max_facts_per_topic | .tfw/workflows/knowledge.md | Prerequisites | max_facts_per_topic | 50 |
| ... | ... | ... | ... | ... |
```

**Как AI agent находит значения:**
1. Opens target file
2. Finds section by header text
3. Finds table row by label text
4. Compares value in table with value in YAML
5. If different → proposes edit

**Почему это работает:**
- Нет scripts — AI agent читает markdown, находит таблицу, меняет число
- Нет magic markers — стандартные markdown таблицы
- Section headers + row labels = stable anchors (агент ищет текст, не line numbers)
- Registry в workflow = single source of mapping

### Enforcement hooks

**В plan.md Phase 5** (before Write TS):
```
> **Budget Check**: Read `tfw.scope_budgets` from PROJECT_CONFIG.yaml.
> Verify this phase fits within: ≤{max_files} files, ≤{max_new} new, ≤{max_loc} LOC.
> If exceeds — split the phase. If user approves override — document in TS.
```

**В research.md** (Limits table — already has values, just ensure sync):
```
| Questions per turn | ≤ 3 | Quality over quantity |
```

**В knowledge.md** (Phase 3 — limits reference already exists, add inline):
```
Check `max_facts_per_topic` (50), `max_topic_files` (8)
```

### Trigger modes для `/tfw-config`

| Mode | When |
|------|------|
| `tfw-config verify` | Check — report mismatches, don't change files |
| `tfw-config apply` | Read YAML → update all inline values → user approves batch |
| `tfw-config --key scope_budgets` | Apply only one config section |

### Lifecycle

```
User edits PROJECT_CONFIG.yaml (changes max_files to 10)
  → runs /tfw-config apply
  → AI reads YAML, finds max_files=10
  → AI reads plan.md, finds "Files per phase | ≤ 14"
  → AI proposes: "Files per phase | ≤ 14" → "Files per phase | ≤ 10"
  → repeat for all registry entries
  → user reviews, approves
  → AI updates files + syncs adapters
  → done
```

## 5. Scope

### What inline values to restore/add

| Category | Config Section | Target Files | Count |
|----------|---------------|--------------|-------|
| Scope budgets | `tfw.scope_budgets` | plan.md, conventions.md, TS.md template | 3 files × 4 values |
| Research limits | `tfw.research` | research.md | 1 file × 4 values |
| Knowledge limits | `tfw.knowledge` | knowledge.md | 1 file × 4 values |

**Total**: ~5 target files, ~12 config→inline mappings.

### Deliverables

1. **Restore** Pattern A tables in plan.md, conventions.md, TS.md template
2. **Add** inline limits в research.md (verify what's already there), knowledge.md
3. **Create** `.tfw/workflows/config.md` with Config Sync Registry + verify/apply modes
4. **Add** enforcement hook в plan.md Phase 5
5. **Create** adapter for Antigravity
6. **Sync** all adapters
7. **Update** conventions.md — add `config.md` to §8 Workflows, §15 Role Lock
8. **Update** glossary.md — add Config Sync Registry term

## 6. Open Questions

1. TS.md template — бюджет строка уже есть (`{N} файлов, {M} модификаций. Лимиты — см. config`). Заменить на inline defaults? Или это заполняется координатором при написании TS?
2. Нужно ли integration с tfw-update (auto-apply after framework upgrade)?

## 7. Принципы (из этой задачи)

| # | Principle |
|---|-----------|
| P1 | Enforcement values MUST be inline — indirection kills agent compliance |
| P2 | Single source of truth ≠ single place of display. Config is authoritative, inline is rendered |
| P3 | No scripts — AI agent is the execution engine. Workflows ARE the automation |
| P4 | RESEARCH recommendations exist for a reason. Override with caution (TFW-12 lesson) |

---

*HL — TFW-19: Config Propagation | 2026-04-03*
