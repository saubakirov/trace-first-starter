# HL — TFW-15: Pipeline Formalization

> **Дата**: 2026-04-01
> **Автор**: Coordinator (AI)
> **Статус**: 📝 HL_DRAFT — Ожидает ревью (updated after RES)

---

## 1. Проблема

Текущий pipeline TFW имеет три связанные проблемы:

### 1.1 Статусы = документы

Pipeline смешивает **процессные статусы** с **типами документов**:

| Статус | Документ | Проблема |
|--------|----------|----------|
| 🔵 HL | HL.md | Статус = документ. «🔵 HL» = мы пишем HL или HL уже готов? ❌ |
| 🟡 TS | TS.md | Статус = документ ❌ |

Конкретные проблемы:
1. **HL используется дважды:** draft при написании, финальный после RESEARCH. Нет отдельного статуса.
2. **Phase 3.5** — костыль из TFW-11, потому что не было места в нумерации.

### 1.2 Статусы нигде не определены формально

- Нет единого реестра статусов (список, emoji, описания)
- Нет определения, кто какой статус может ставить (role → status)
- Переходы описаны текстом в разных файлах, нет state machine

### 1.3 Концепции смешаны

- **Document Type** vs **Template** — не разделены (HL = и тип артефакта, и файл шаблона)
- **Workflow** vs **Adapter Command** (skill, slash-command) — синонимы без определений
- **Status** — определён как emoji-label, но не как формальный объект

## 2. Целевое состояние

### 2.1 Новый pipeline (Variant D — 8 statuses)

```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE
                          (skip: 📝 HL_DRAFT ··· 🟡 TS_DRAFT)
```

**Логика Variant D:**
- Статусов остаётся 8 (проверенное количество), не считая BLOCKED
- `HL_DRAFT` и `TS_DRAFT` — самодокументирующиеся имена. Агент видит `_DRAFT` и понимает: документ пишется/обсуждается
- `🔵 HL` и `📋 PLAN` убраны — нет двойного использования HL, нет мёртвого статуса «HL approved»
- Approval implicit: переход `HL_DRAFT → RES` или `HL_DRAFT → TS_DRAFT` = HL утверждён

**Ключевые переходы:**
```
📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT     # research done, HL finalized
📝 HL_DRAFT ··· 🟡 TS_DRAFT              # research skipped, HL confirmed
```

### 2.2 Status Registry (PROJECT_CONFIG.yaml)

Единый реестр статусов с `role` field:

```yaml
tfw:
  statuses:
    - id: TODO
      emoji: "⬜"
      description: "Task registered, work not started"
    - id: HL_DRAFT
      emoji: "📝"
      description: "HL being drafted or discussed"
      role: coordinator
    - id: RES
      emoji: "🔬"
      description: "Research in progress (optional)"
      role: coordinator
    - id: TS_DRAFT
      emoji: "🟡"
      description: "TS written, awaiting approval"
      role: coordinator
    - id: ONB
      emoji: "🟠"
      description: "Executor onboarding"
      role: executor
    - id: RF
      emoji: "🟢"
      description: "Execution complete, RF written"
      role: executor
    - id: REV
      emoji: "🔍"
      description: "Review in progress"
      role: reviewer
    - id: DONE
      emoji: "✅"
      description: "Task closed"
    - id: BLOCKED
      emoji: "❌"
      description: "Blocked by dependency"
```

**Дизайн-решения (RES D4, E6):**
- `id` IS the label. Нет отдельного поля `label` (KISS)
- `role` связывает статус с ролью — кто отвечает за этот этап
- `transitions` не включены — deferred. Переходы описаны в conventions.md prose
- TODO / DONE / BLOCKED — boundary states, без `role`

### 2.3 Transition Matrix

| From | To | Role | Trigger |
|------|----|------|---------|
| ⬜ TODO | 📝 HL_DRAFT | Coordinator | `/tfw-plan` creates HL draft |
| 📝 HL_DRAFT | 🔬 RES | Coordinator | User approves HL draft, research recommended |
| 📝 HL_DRAFT | 🟡 TS_DRAFT | Coordinator | User approves HL draft, research skipped |
| 🔬 RES | 🟡 TS_DRAFT | Coordinator | Research done, HL finalized, TS written |
| 🟡 TS_DRAFT | 🟠 ONB | Executor | `/tfw-handoff` starts, ONB written |
| 🟠 ONB | 🟢 RF | Executor | Implementation done, RF written |
| 🟢 RF | 🔍 REV | Reviewer | `/tfw-review` starts |
| 🔍 REV | ✅ DONE | Reviewer | APPROVE verdict |
| 🔍 REV | 🟢 RF | Reviewer | REVISE verdict (back to executor) |
| 🔍 REV | 🛑 User decision | Reviewer | REJECT verdict |
| * | ❌ BLOCKED | Any | External dependency blocks progress |

**REJECT = branching point (RES C6, D5):**
```
🔍 REV → ❌ REJECT → 🛑 User decides:
                        (a) → 📝 HL_DRAFT (rework HL)
                        (b) → 🔬 RES (new research)
                        (c) → 🟡 TS_DRAFT (HL fine, rewrite TS)
```

### 2.4 Concept Taxonomy (TODO — full formalization deferred)

| Концепция | Определение | Где живёт |
|-----------|------------|-----------|
| **Document Type** | Тип артефакта: HL, RES, TS, ONB, RF, REVIEW | glossary.md |
| **Template** | Канонический формат для документа | `.tfw/templates/` |
| **Workflow** | Tool-agnostic процесс (plan, research, handoff...) | `.tfw/workflows/` |
| **Adapter Command** | Tool-specific вызов workflow (slash-command, skill) | `.claude/commands/`, `.agent/workflows/` |
| **Status** | Процессный статус задачи на борде | PROJECT_CONFIG.yaml `tfw.statuses` |

> Document Status (DRAFT/APPROVED в header файла) — **deferred** (RES D7). Не в скоупе TFW-15. Файловые headers обновляются только чтобы соответствовать новым именам статусов.

### 2.5 Phase 3.5 → Phase 4

plan.md фазы перенумеровываются:
- Phase 1: Research & Analysis
- Phase 2: Write HL (draft) → борд `📝 HL_DRAFT`
- Phase 3: Review & Refine
- **Phase 4: RESEARCH Gate** (бывший 3.5)
- **Phase 5: Decide Scope & Write TS** (бывший Phase 4) → борд `🟡 TS_DRAFT`

Step numbering fix (RES E3, D6): plan.md имеет пропуск (step 8 отсутствует). Починить in-passing.

## 3. Скоуп изменений

### Живые файлы (нужно менять)

| # | Файл | Действие | Описание |
|---|------|----------|----------|
| 1 | `.tfw/PROJECT_CONFIG.yaml` | MODIFY | Добавить `tfw.statuses` registry с `role` field |
| 2 | `.tfw/conventions.md` | MODIFY | §5: новый pipeline, status table (HL_DRAFT/TS_DRAFT), REJECT branching |
| 3 | `.tfw/glossary.md` | MODIFY | Concept Taxonomy определения, pipeline diagram |
| 4 | `.tfw/README.md` | MODIFY | Pipeline diagram + Task Lifecycle section |
| 5 | `.tfw/workflows/plan.md` | MODIFY | Phase 3.5 → Phase 4, renumber, step numbering fix, status refs |
| 6 | `.tfw/workflows/research.md` | MODIFY | Status Transitions section |
| 7 | `README.md` (root) | MODIFY | Key Concepts pipeline string + task board legend |
| 8 | `.tfw/templates/HL.md` | MODIFY | `🔵 HL — Ожидает ревью` → `📝 HL_DRAFT — Ожидает ревью` |
| 9 | `.tfw/templates/TS.md` | MODIFY | `🟡 TS — Ожидает апрува` → `🟡 TS_DRAFT — Ожидает апрува` |

### Архивные файлы (НЕ меняем)

Файлы в `tasks/TFW-{1..14}/` — исторические артефакты. Менять = фальсифицировать.

### Файлы вне скоупа

- Адаптеры (.claude/, .agent/) — ссылаются на workflow файлы, не на статусы
- Templates (ONB, RF, REVIEW, RES) — не содержат pipeline строк
- `.tfw/CHANGELOG.md` — `Phase 3.5` упоминания исторические, не трогаем

**Бюджет:** 0 новых файлов, 9 модификаций.

## 4. Definition of Done

- [ ] 1. Новый pipeline: `⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE`
- [ ] 2. PROJECT_CONFIG.yaml: `tfw.statuses` реестр с `role` field
- [ ] 3. conventions.md: status table обновлена + REJECT = branching point
- [ ] 4. glossary.md: Concept Taxonomy definitions
- [ ] 5. README.md (.tfw/): pipeline diagram обновлён
- [ ] 6. plan.md: Phase 3.5 → Phase 4, step numbering fix, status refs
- [ ] 7. research.md: Status Transitions обновлены
- [ ] 8. README.md (root): Key Concepts + task board legend
- [ ] 9. HL.md template: `📝 HL_DRAFT — Ожидает ревью`
- [ ] 10. TS.md template: `🟡 TS_DRAFT — Ожидает апрува`
- [ ] 11. Grep по `🔵 HL` в `.tfw/` (excluding CHANGELOG.md) возвращает 0 результатов
- [ ] 12. Grep по `Phase 3.5` в `.tfw/` (excluding CHANGELOG.md) возвращает 0 результатов

## 5. Definition of Failure

- ❌ Архивные файлы (tasks/) или CHANGELOG.md переписаны — фальсификация истории
- ❌ Status registry рассинхронизировалась с conventions/glossary
- ❌ Adapter commands сломались
- ❌ Статусов стало больше 10 — раздувание

## 6. Зависимости

| Зависимость | Статус |
|-------------|--------|
| TFW-14 (research interaction model) | ✅ DONE |
| TFW-12 (config centralization) | ✅ DONE |

## 7. Принципы

1. **Statuses ≠ Documents** — процессные статусы описывают фазу работы, не тип артефакта
2. **Single Source of Truth** — статусы определены в PROJECT_CONFIG.yaml, остальные файлы ссылаются
3. **Implicit Approval** — переход к следующему статусу = предыдущий этап утверждён
4. **Same count, better names** — 8 статусов (проверенное количество), только имена чётче

## 8. Риски

| Риск | Вероятность | Влияние | Mitigation |
|------|-------------|---------|------------|
| Config раздувается | Низкая | Низкое | statuses — фиксированный список |
| Agent не читает config | Средняя | Среднее | conventions.md содержит transition matrix inline |
| `_DRAFT` suffix длинный на борде | Низкая | Низкое | Emoji делает visual scan, текст вторичен (RES C5) |

---

*HL — TFW-15: Pipeline Formalization | 2026-04-01*
