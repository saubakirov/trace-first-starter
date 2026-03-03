# TS — TFW-4 / Phase A: Remove STEPS.md + frontmatter fix

> **Дата**: 2026-03-03
> **Автор**: Coordinator (AI)
> **Статус**: 🟡 TS — Ожидает апрува
> **Parent HL**: [HL-TFW-4](HL-TFW-4__framework_cleanup.md)

---

## 1. Цель

Удалить устаревший артефакт `STEPS.md` и связанный с ним ритуал Summary Specification из всех файлов фреймворка. Добавить YAML frontmatter в workflow-файлы чтобы Antigravity корректно регистрировал их как slash-команды.

## 2. Scope

### In Scope
- Удаление `STEPS.md` из корня проекта
- Удаление Summary Specification секции из `AGENTS.md`
- Обновление всех ссылок на STEPS.md в `.tfw/` и `.agent/`
- Обновление context loading order (убрать шаг 2: `STEPS.md`)
- Добавление YAML frontmatter с `description` в `.tfw/workflows/*.md`
- Синхронизация `.agent/workflows/` с обновлёнными `.tfw/workflows/`
- Обновление root `README.md` (таблица "What's Inside")

### Out of Scope
- Файлы в `tasks/` (исторические артефакты, не трогаем)
- De-duplication (Phase B)
- ONB changes (Phase C)
- Содержательные изменения философии в `.tfw/README.md` (только удаление ссылок на STEPS)

## 3. Затрагиваемые файлы

| Файл | Действие | Описание |
|------|----------|----------|
| `STEPS.md` | DELETE | Удалить файл |
| `AGENTS.md` | MODIFY | Убрать step 2 из context loading, убрать Summary Specification секцию + conduct rule про Summary |
| `README.md` | MODIFY | Убрать строку `STEPS.md` из таблицы "What's Inside", убрать "summary discipline" из Key Concepts |
| `.tfw/README.md` | MODIFY | Убрать STEPS.md из project structure, context loading, "The One Rule" секцию, Getting Started шаги 4-5 |
| `.tfw/conventions.md` | MODIFY | Убрать STEPS.md из §2 Required Artifacts, §10 Context Loading, §13 Summary Line |
| `.tfw/glossary.md` | MODIFY | Убрать Summary-related entries если есть |
| `.tfw/init.md` | MODIFY | Убрать STEPS.md из Step 4, verification checklist, adapter template |
| `.tfw/workflows/plan.md` | MODIFY | Убрать step 2 из prerequisites, step 8 "Update STEPS.md". Добавить YAML frontmatter |
| `.tfw/workflows/handoff.md` | MODIFY | Убрать steps 11, 17 "Update STEPS.md". Добавить YAML frontmatter |
| `.tfw/workflows/resume.md` | MODIFY | Добавить YAML frontmatter |
| `.tfw/templates/REVIEW.md` | MODIFY | Убрать `STEPS.md — closure entry added` из §4 Traces Updated |
| `.tfw/adapters/antigravity/tfw-rules.md.template` | MODIFY | Убрать STEPS.md из context loading |
| `.tfw/adapters/claude-code/CLAUDE.md.template` | MODIFY | Убрать STEPS.md из context loading |
| `.tfw/adapters/cursor/tfw.mdc.template` | MODIFY | Убрать STEPS.md из context loading |
| `.agent/rules/agents.md` | MODIFY | Убрать step 2, Summary Specification, conduct rule |
| `.agent/rules/tfw.md` | MODIFY | Убрать STEPS.md из context loading, summary discipline rule |
| `.agent/workflows/tfw-plan.md` | MODIFY | Sync с `.tfw/workflows/plan.md` |
| `.agent/workflows/tfw-handoff.md` | MODIFY | Sync с `.tfw/workflows/handoff.md` |
| `.agent/workflows/tfw-resume.md` | MODIFY | Sync с `.tfw/workflows/resume.md` |
| `.agent/workflows/tfw-task.md` | MODIFY | Убрать упоминания STEPS если есть |

**Бюджет:** 1 удаление, 19 модификаций. Превышает лимит ≤7 файлов, но изменения механические (find+remove references). Не содержит новой логики.

## 4. Детальные шаги

### Step 1: Delete STEPS.md
Удалить файл `STEPS.md` из корня.

### Step 2: Update AGENTS.md
- Убрать строку `2. STEPS.md (progress log)` из Context Loading
- Перенумеровать оставшиеся шаги (3→2, 4→3, ...)
- Убрать строку `End every significant reply with a **Summary line**` из Conduct
- Удалить секцию `## Summary Specification` целиком (строки 35-41)

### Step 3: Update root README.md
- Убрать строку `| STEPS.md | Progress journal (Summary lines) |` из таблицы
- Изменить `no sycophancy, no placeholders, summary discipline` → `no sycophancy, no placeholders`

### Step 4: Update `.tfw/README.md`
- Убрать `├── STEPS.md` из project structure tree (L68)
- Убрать `STEPS.md` из context loading sequence (L88)
- Переписать секцию "The One Rule: Summary Discipline" (L93-103) → заменить на краткое описание trace discipline через RF/Task Board
- Обновить Getting Started шаги 4-5 (L299-300) — убрать упоминание STEPS

### Step 5: Update `.tfw/conventions.md`
- Убрать `STEPS.md` из §2 Required Artifacts (L16)
- Убрать `STEPS.md` из §10 Context Loading (L151)
- Удалить §13 Summary Line (L168-172) или переписать без привязки к STEPS

### Step 6: Update `.tfw/init.md`
- Убрать `# STEPS.md` из Step 4 (L106)
- Убрать `STEPS.md` из .gitignore warning (L124)
- Убрать `STEPS.md` из verification checklist (L139)
- Убрать `STEPS.md` из adapter template context (L164)

### Step 7: Update `.tfw/workflows/*.md` (plan, handoff, resume)
- `plan.md`: убрать step 2 prereq (L16), step 8 (L58). Добавить frontmatter:
  ```yaml
  ---
  description: TFW Plan — research, write HL, review, scope decision, write TS
  ---
  ```
- `handoff.md`: убрать step 11 (L66), step 17 (L137). Добавить frontmatter:
  ```yaml
  ---
  description: TFW Handoff — executor onboarding, implementation, RF, coordinator review
  ---
  ```
- `resume.md`: добавить frontmatter:
  ```yaml
  ---
  description: TFW Resume — locate task, build status matrix, decide next phase
  ---
  ```

### Step 8: Update `.tfw/templates/REVIEW.md`
- Убрать `- [ ] STEPS.md — closure entry added` из §4 Traces Updated (L46)

### Step 9: Update adapter templates
- `.tfw/adapters/antigravity/tfw-rules.md.template`: убрать STEPS.md (L18)
- `.tfw/adapters/claude-code/CLAUDE.md.template`: убрать STEPS.md (L21)
- `.tfw/adapters/cursor/tfw.mdc.template`: убрать STEPS.md (L20)

### Step 10: Update `.agent/rules/`
- `agents.md`: убрать step 2, Summary Specification, summary conduct rule (mirror changes from Step 2)
- `tfw.md`: убрать STEPS.md из context loading (L18), summary discipline rule (L28)

### Step 11: Sync `.agent/workflows/`
- Copy updated `.tfw/workflows/plan.md` → `.agent/workflows/tfw-plan.md`
- Copy updated `.tfw/workflows/handoff.md` → `.agent/workflows/tfw-handoff.md`
- Copy updated `.tfw/workflows/resume.md` → `.agent/workflows/tfw-resume.md`
- Check `tfw-task.md` for STEPS references

## 5. Acceptance Criteria

- [ ] `STEPS.md` не существует в корне проекта
- [ ] `grep -ri "STEPS.md" --include="*.md" --include="*.template" --include="*.yaml"` находит совпадения ТОЛЬКО в `tasks/` (исторические артефакты)
- [ ] Context loading order во всех файлах начинается с `AGENTS.md` → `TASK.md` (без STEPS)
- [ ] Ни один файл не содержит Summary Specification формат (`Stage={stage} | Iteration=...`)
- [ ] `.tfw/workflows/*.md` содержат YAML frontmatter с `description`
- [ ] `.agent/workflows/tfw-*.md` синхронизированы с `.tfw/workflows/`
- [ ] Нет broken links или нумерационных ошибок после удаления шагов

## 6. Риски фазы

| Риск | Mitigation |
|------|------------|
| Забыть обновить одну из 10 вариаций context loading | Grep-проверка по acceptance criteria |
| Нумерация шагов в workflows сбивается при удалении | Проверить нумерацию вручную |
| `.tfw/README.md` теряет ключевую секцию "The One Rule" | Заменить на "Trace Discipline" с акцентом на RF + Task Board |

---

*TS — TFW-4 / Phase A: Remove STEPS.md + frontmatter fix | 2026-03-03*
