# HL — TFW-4: Framework Cleanup

> **Дата**: 2026-03-03
> **Автор**: Coordinator (AI) + User
> **Статус**: 🔵 HL — Ожидает ревью

---

## 1. Видение

TFW v3 вырос органически через 3 версии и 13+ итераций. Фреймворк работает в продакшене (Atamat, SQLR, RYC), но накопил «жир»: один устаревший артефакт (`STEPS.md`), copy-paste блоков внутри `.tfw/`, отсутствие onboarding-материалов для новых пользователей. Цель — привести стартер в состояние, достойное публичного репозитория: чистый, понятный, без лишнего.

> «Фреймворк, который учит дисциплине, должен сам быть дисциплинированным.»

## 2. Текущее состояние (As-Is)

### 2.1 Устаревшие элементы

| Элемент | Проблема |
|---------|----------|
| `STEPS.md` | Функция «память между сессиями» ушла в KI, conversation logs, task_boundary, RF-файлы. Summary discipline как ритуал не используется ни одним современным тулом |
| Summary Specification в `AGENTS.md` | Привязано к STEPS.md — становится бессмысленным без него |

### 2.2 Copy-paste внутри `.tfw/`

**Важный контекст**: этот репо — мета-проект. `.tfw/` описывает фреймворк, корневые файлы — проект, использующий фреймворк. Поэтому пересечения между `.tfw/README.md` и корневым `README.md` — **не дупликация** (разные слои). Пересечения между glossary, conventions и README — тоже **не дупликация** (словарь / правила / философия).

**Реальная проблема** — literal copy-paste идентичных блоков внутри `.tfw/`:

| Блок | Где скопирован | Canonical source |
|------|---------------|-----------------|
| ASCII status flow diagram | `README.md`, `conventions.md`, `glossary.md`, `workflows/plan.md` | → `conventions.md §5` |
| Scope budgets table | `README.md`, `conventions.md`, `glossary.md`, `workflows/plan.md` | → `conventions.md §6` |
| Anti-patterns list | `README.md`, `conventions.md`, `workflows/plan.md`, `workflows/handoff.md` | → `conventions.md §14` |
| Context loading order | 10 вариаций (включая adapters и `.agent/`) | → `AGENTS.md` |

### 2.3 Что отсутствует

| Элемент | Влияние |
|---------|---------|
| Сквозной пример (end-to-end tutorial) | Новый пользователь не видит how it looks in practice |
| Init-скрипт | Setup >5 минут вручную, обещано <5 |
| CHANGELOG.md | Нет формальной истории версий для open-source |
| ONB flexibility | ONB обязателен даже для 1-file задачи — overhead |

### 2.4 Количественная оценка

| Метрика | Значение |
|---------|----------|
| Всего файлов в фреймворке | 28 |
| Общий объём `.tfw/` | ~52 KB |
| Файлы с copy-paste status flow | 4 |
| Файлы с copy-paste scope budgets | 4 |
| Файлы с copy-paste anti-patterns | 4 |
| Вариации context loading | 10 |

## 3. Целевое состояние (To-Be)

### 3.1 Убрать устаревшее
- `STEPS.md` удалён из обязательных артефактов
- Summary Specification удалена из `AGENTS.md`, adapters, conventions
- Все ссылки на STEPS.md обновлены или удалены

### 3.2 De-duplicate copy-paste
- Каждый canonical блок существует в одном месте
- Остальные файлы содержат краткую ссылку: «See `conventions.md §5` for status flow»
- `.tfw/README.md` остаётся philosophy-first (без механических таблиц)
- `glossary.md` остаётся словарём (определения, без копий диаграмм)
- `workflows/*.md` содержат пошаговые инструкции, ссылаются на conventions для справочных таблиц

### 3.3 ONB flexibility
- ONB отмечен как опциональный для single-phase задач
- Обязательным остаётся только для multi-phase / team handoff

### 3.4 Добавить onboarding
- `examples/` — один демо-проект (minimal, ~5 файлов)
- `init.sh` — скрипт автоматизации setup
- `CHANGELOG.md` — история v1→v2→v3 + текущие изменения

## 4. Фазы

### Phase A: Remove STEPS.md & Summary discipline + frontmatter fix 🔴
- Удалить `STEPS.md` из корня
- Убрать Summary Specification из `AGENTS.md`
- Обновить все упоминания в `.tfw/` (README, conventions, glossary, workflows, init, adapters, templates)
- Обновить `.agent/rules/agents.md`, `.agent/rules/tfw.md`
- Обновить context loading order везде (убрать шаг «read STEPS.md»)
- Добавить YAML frontmatter (`description`) в `.tfw/workflows/*.md` — без него Antigravity не регистрирует workflow как slash-команду при копировании в `.agent/workflows/`

### Phase B: De-duplicate copy-paste в `.tfw/` 🔴
- Определить canonical source для каждого блока
- В `glossary.md`: заменить копии status flow / scope budgets / anti-patterns на ссылки
- В `README.md` (`.tfw/`): заменить механические таблицы на ссылки, оставить философию
- В `workflows/plan.md`, `workflows/handoff.md`: заменить справочные таблицы на ссылки
- Sync: обновить `.agent/workflows/` копии

### Phase C: ONB flexibility 🟡
- В conventions.md: пометить ONB как optional для single-phase
- Обновить lifecycle diagram (добавить bypass arrow для ONB)
- Обновить `workflows/plan.md` и `workflows/handoff.md`


## 5. Definition of Done (DoD)

- ✅ 1. `STEPS.md` удалён, все упоминания убраны или обновлены
- ✅ 2. `.tfw/workflows/*.md` содержат YAML frontmatter с `description`
- ✅ 3. Ни одна таблица/диаграмма не скопирована более чем в одном файле внутри `.tfw/`
- ✅ 4. ONB помечен как optional для single-phase задач
- ✅ 5. Все adapter templates обновлены
- ✅ 6. `.agent/rules/` и `.agent/workflows/` синхронизированы

## 6. Definition of Failure (DoF)

- ❌ 1. Правка одного правила требует изменений более чем в 2 файлах
- ❌ 2. `.tfw/README.md` потерял философскую ценность и стал сухим reference doc

**При провале:** откатить, пересмотреть scope Phase B (de-duplication может быть слишком агрессивной).

## 7. Принципы

1. **Philosophy stays rich** — `.tfw/README.md` остаётся манифестом, а не reference card. Если нужно выбирать между «не дублировать» и «сохранить нарратив» — нарратив важнее.
2. **Glossary = словарь, Conventions = правила** — это разные документы с разным назначением. Описывать один и тот же термин с разных сторон — нормально. Копировать таблицу побуквенно — нет.
3. **Meta-project awareness** — этот репо описывает TFW И использует TFW. Корневые файлы и `.tfw/` пересекаются по замыслу, не по ошибке.
4. **Don't break working projects** — форкнутые проекты (Atamat, SQLR) ссылаются на `.tfw/`. Нельзя менять структуру templates или conventions sections без backward compatibility.

## 8. Зависимости

| Зависимость | Статус |
|-------------|--------|
| TFW-3 (README public-readiness) | 🟢 RF (завершён) |
| Форкнутые проекты (Atamat, SQLR, RYC) | ⚠️ Нужно проверить, ссылаются ли на STEPS.md |

## 9. Риски

| Риск | Вероятность | Влияние | Mitigation |
|------|-------------|---------|------------|
| De-duplication слишком агрессивна → файлы теряют self-contained читаемость | Средняя | Среднее | Принцип §7.1: нарратив важнее DRY |
| Удаление STEPS.md ломает форкнутые проекты | Низкая | Низкое | STEPS.md в форках — пустой или минимальный, удаление безболезненно |
| Init-скрипт не покрывает все ОС | Средняя | Низкое | Bash-скрипт + fallback к мануальной инструкции |
| Example project в `examples/` устаревает | Средняя | Среднее | Выбрать максимально простой домен (todo-app) |

---

*HL — TFW-4: Framework Cleanup | 2026-03-03*
