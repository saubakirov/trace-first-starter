# TS — TFW_20260921-220500_AGSK / Phase B: Migration Guide and Documentation Sync

> **Current filename**: `TS__phase-b__migration_guide_and_documentation_sync.md`
> **Date**: 2026-09-22
> **Author**: Antigravity Coordinator
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW_20260921-220500_AGSK](../HL-TFW_20260921-220500_AGSK.md)

---

## 1. Objective

Разработать и опубликовать исчерпывающее нормативное руководство по миграции `.tfw/migrations/3.5.0.md`, подробно описывающее алгоритм безопасной утилизации устаревшего каталога `.agent/` и перехода адаптера Antigravity на архитектуру навыков для сторонних проектов-потребителей TFW. Синхронизировать реестр знаний `KNOWLEDGE.md`, понятийный словарь `.tfw/glossary.md`, сводные таблицы адаптеров в `README` на трёх языках (en, ru, kk) и зафиксировать выпуск в `.tfw/CHANGELOG.md`.

---

## 2. Scope

### In Scope

- Создание нормативного руководства `.tfw/migrations/3.5.0.md` с точными правилами классификации, сохранения пользовательских файлов и ликвидации `.agent/`.
- Модификация `KNOWLEDGE.md`: актуализация строки "Adapters" (10 канонических маршрутов, удаление устаревших отсылок к `.agent/workflows/`).
- Модификация `.tfw/glossary.md`: актуализация статьи "Tool Adapter" (указание на `.agents/skills/` вместо `workflows`).
- Модификация `README.md`, `README.ru.md`, `README.kk.md`: приведение сводной таблицы адаптеров к актуальным путям Antigravity (`.agents/rules/tfw.md` и `.agents/skills/`).
- Модификация `.tfw/CHANGELOG.md`: внесение записи о миграции адаптера Antigravity и выводе `.agent/` под заголовком `[3.5.0]`.
- Модификация `.agents/rules/tfw.md` и `.tfw/adapters/antigravity/tfw-rules.md.template`: добавление чёткой инструкции по отправке вертикальных сообщений через `send_message` (извлечение UUID из `coordinator_route: "antigravity:thread:local:<uuid>"`).
- Модификация `.tfw/adapters/antigravity/README.md`: документирование механики адресных сообщений между сессиями Antigravity под `tfw-gates-only`.
- Верификация прохождения тестов репозитория (`pytest tools/tests/ docs/scripts/ -q`).

### Out of Scope

- Изменение манифеста `.tfw/adapters/manifest.yaml` (выполнено в Фазе A).
- Изменение канонических процессов `.tfw/workflows/` и шаблонов `.tfw/templates/`.
- Физический бамп версии в `.tfw/VERSION` (выполняется специальной процедурой `/tfw-release` при релизе фреймворка).

---

## 3. Principles Check

| # | HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Single Source of Truth (Манифест и правила согласованы) | AC-2, AC-3, AC-4 | Сверка описания путей во всех документах с `manifest.yaml`. |
| P2 | Нулевой технический долг | AC-2, AC-3 | Устранение замечаний Проверяющего из Фазы A (строка Adapters и статья Tool Adapter). |
| P3 | Безопасность внешних потребителей | AC-1 | Детальный регламент миграции в `3.5.0.md` защищает пользовательские наработки от случайного удаления. |
| P4 | Отсутствие сикофанства и плейсхолдеров | AC-1, AC-5, AC-7 | Руководство, правила и записи в журнале содержат законченный производственный текст. |

---

## 4. Affected Files and Value-Bearing Accounting

Все 10 файлов классифицированы как `VALUE` (нормативные документы миграции, системный реестр знаний, публичная документация и правила Antigravity).

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `.tfw/migrations/3.5.0.md` | CREATE | `VALUE` | Руководство по обновлению до версии 3.5.0 и утилизации `.agent/`. |
| `KNOWLEDGE.md` | MODIFY | `VALUE` | Актуализация записи Adapters: 10 маршрутов, `.agents/skills/`, удаление `.agent/workflows/`. |
| `.tfw/glossary.md` | MODIFY | `VALUE` | Актуализация статьи Tool Adapter под навыки Antigravity. |
| `README.md` | MODIFY | `VALUE` | Сводная таблица адаптеров: обновление точки входа Antigravity. |
| `README.ru.md` | MODIFY | `VALUE` | Русская локализация таблицы адаптеров. |
| `README.kk.md` | MODIFY | `VALUE` | Казахская локализация таблицы адаптеров. |
| `.tfw/CHANGELOG.md` | MODIFY | `VALUE` | Фиксация изменений релиза 3.5.0 (AGSK). |
| `.agents/rules/tfw.md` | MODIFY | `VALUE` | Инструкция по пересылке сообщений через `send_message` по UUID координатора. |
| `.tfw/adapters/antigravity/tfw-rules.md.template` | MODIFY | `VALUE` | Синхронизация шаблона правила (побайтовый паритет с `tfw.md`). |
| `.tfw/adapters/antigravity/README.md` | MODIFY | `VALUE` | Документирование адресных сообщений в описании адаптера. |

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | 10 literal paths listed above |
| Baseline / selector source | `a26322ea1551a376510d5403e0e7a2dfec5d4dcb` (commit завершения Фазы A) |
| Candidate rule | Первый коммит Исполнителя, содержащий все 10 путей VALUE при зелёных тестах ASSURANCE |
| Logical VALUE files | 10 (1 создание, 9 модификаций) |
| Touched text LOC | Ожидается добавление ~300–400 строк |
| Multiplier / authority | Неизменяемый утвержденный знаменатель из 10 файлов; отклонение = BLOCKED |
| Approval epoch / failure | Согласование TS владельцем; изменение перечня файлов без поправки запрещено |

```powershell
$valuePaths = @(
  '.tfw/migrations/3.5.0.md'
  'KNOWLEDGE.md'
  '.tfw/glossary.md'
  'README.md'
  'README.ru.md'
  'README.kk.md'
  '.tfw/CHANGELOG.md'
  '.agents/rules/tfw.md'
  '.tfw/adapters/antigravity/tfw-rules.md.template'
  '.tfw/adapters/antigravity/README.md'
)
```

---

## 5. Acceptance Criteria

### AC-1: Создание нормативного руководства `.tfw/migrations/3.5.0.md`
- [ ] Файл `.tfw/migrations/3.5.0.md` создан и оформлен в соответствии с прецедентами TFW (`3.4.0.md`, `3.4.1.md`).
- [ ] Описан контекст: переход Antigravity на навыки (`.agents/skills/`), отказ от `.agents/workflows/` и полная ликвидация устаревшего каталога `.agent/`.
- [ ] Приведена таблица маршрутов обновления с предыдущих версий (3.4.1, 3.4.0 и др.).
- [ ] Сформулирован четкий алгоритм классификации содержимого `.agent/` для внешних проектов:
  - Системные файлы TFW (`rules/agents.md`, `rules/tfw.md`, `workflows/*.md`) подлежат удалению после проверки наличия аналогов в `.agents/`.
  - Пользовательские правила (custom rules) переносятся в `.agents/rules/<имя>.md`.
  - Пользовательские рабочие процессы (custom workflows) конвертируются в навыки `.agents/skills/<имя>/SKILL.md` (с YAML frontmatter `name` и `description`).
  - Личные заметки и локальные конвенции переносятся в `README.md` проекта или соответствующую документацию.
- [ ] Приведена пошаговая процедура безопасного удаления пустого каталога `.agent/`.

Gate: Наличие файла `.tfw/migrations/3.5.0.md` с полным набором обязательных секций.
Evidence: Анализ содержимого файла в EV.

### AC-2: Актуализация реестра знаний `KNOWLEDGE.md`
- [ ] В строке таблицы `Adapters` обновлено количество канонических маршрутов (с 11 на 10).
- [ ] Удалены устаревшие пути `.agent/workflows/` и оговорка о совместимости с singular `.agent`.
- [ ] Зафиксировано, что Antigravity использует единый с Codex каталог навыков `.agents/skills/`.

Gate: Сверка строки "Adapters" в `KNOWLEDGE.md` на отсутствие подстроки `.agent/workflows/`.
Evidence: Ripgrep-проверка строки.

### AC-3: Актуализация статьи в `.tfw/glossary.md`
- [ ] В определении термина `Tool Adapter` строка Antigravity обновлена: заменено `.agents/workflows/tfw-{command}.md` на `.agents/skills/tfw-{command}/SKILL.md`.

Gate: Отсутствие упоминания `.agents/workflows` в `.tfw/glossary.md`.
Evidence: Текстовая проверка словарной статьи.

### AC-4: Синхронизация таблиц адаптеров в `README.md`, `README.ru.md`, `README.kk.md`
- [ ] В файлах `README.md`, `README.ru.md`, `README.kk.md` в таблице адаптеров строка Antigravity обновлена: путь `.agent/rules/tfw.md` заменен на `.agents/rules/tfw.md` с указанием навыков в `.agents/skills/`.

Gate: Ripgrep по `README*.md` не находит вхождений `.agent/rules/tfw.md`.
Evidence: Вывод команды ripgrep в EV.

### AC-5: Внесение записи о выпуске в `.tfw/CHANGELOG.md`
- [ ] В `.tfw/CHANGELOG.md` добавлена секция `## [3.5.0] — YYYY-MM-DD` с кодовым названием `AGSK — Antigravity Skill Migration & Legacy .agent Retirement`.
- [ ] Подробно описаны категории `Changed`, `Removed` и `Compatibility and updating` со ссылкой на `migrations/3.5.0.md`.

Gate: Наличие корректно структурированной записи `[3.5.0]` в `CHANGELOG.md`.
Evidence: Сверка формата с Keep a Changelog.

### AC-6: Сохранность тестов репозитория (ASSURANCE)
- [ ] Все 14 существующих тестов (`test_git_blob_sizes.py`, `test_gen_docs.py`, `test_integration.py`) проходят успешно без ошибок.

Gate: `python -m pytest tools/tests/ docs/scripts/ -q` завершается с кодом 0 (14 passed).
Evidence: Лог выполнения тестов.

### AC-7: Эксплицитная инструкция по пересылке сообщений в Antigravity (включая RESEARCH)
- [ ] В `.agents/rules/tfw.md` и `.tfw/adapters/antigravity/tfw-rules.md.template` добавлена однозначная инструкция:
  «В Antigravity вертикальные сообщения Координатору под `tfw-gates-only` отправляются инструментом `send_message`: извлечь UUID из `coordinator_route` (отбросив префикс `antigravity:thread:local:`) и вызвать `send_message(Recipient="<uuid>", Message="...")`. Адресная отправка между сессиями Antigravity поддерживается платформой; все роли (Исследователь при завершении итераций/RES, Исполнитель при ONB/RF, Проверяющий при REV/REVIEW) обязаны направлять формальные рапорты Координатору напрямую вместо перекладывания на владельца.»
- [ ] В `.tfw/adapters/antigravity/README.md` задокументирована механика пересылки сообщений через `send_message` для всех ролей (Researcher, Executor, Reviewer).
- [ ] Правило `.agents/rules/tfw.md` и шаблон `tfw-rules.md.template` побайтово идентичны.

Gate: `git diff --no-index .tfw/adapters/antigravity/tfw-rules.md.template .agents/rules/tfw.md` возвращает нулевой вывод.
Evidence: Побайтовая сверка правила и шаблона в EV.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-b__migration_guide_and_documentation_sync.md` | Сводный отчёт о проверке каждого критерия приёмки AC-1 — AC-7. |
| `evidence/doc-sweep.txt` | Подтверждение отсутствия устаревших путей `.agent/` во всей проектной документации. |

---

## 6. Technical Guidance

1. **Структура `.tfw/migrations/3.5.0.md`:**
   Ориентироваться на структуру `migrations/3.4.1.md` и `migrations/3.4.0.md`. Документ `3.5.0.md` составляется на английском языке в строгом соответствии со стилем TFW Core, с исчерпывающим освещением всех сценариев для русскоязычных и англоязычных проектов.
2. **Точная строка для `KNOWLEDGE.md`:**
   ```markdown
   | Adapters | One tooling manifest defines four vendor roots and 10 routes. Whole copies are byte-compared; root blocks are marker-bounded. Init/update/config consume it. Antigravity and Codex share the `.agents/skills/` surface; singular `.agent` is fully retired | `.tfw/adapters/manifest.yaml`, `.tfw/adapters/` (claude-code, cursor, antigravity, codex), `.claude/commands/`, `.agents/skills/`, `.agents/rules/tfw.md`, `.tfw/workflows/init.md`, `.tfw/workflows/update.md`, `.tfw/workflows/config.md` |
   ```
3. **Формулировка правила Antigravity по отправке сообщений (все роли, включая RESEARCH):**
   ```markdown
   ### Coordination Messaging
   Under `tfw-gates-only`, role units communicate vertically with their Coordinator via `send_message`:
   - Extract the target UUID from `coordinator_route` (strip `antigravity:thread:local:`).
   - Call `send_message(Recipient="<uuid>", Message="...")` to report every gate transition:
     - **Researcher:** report completion of each research iteration and RES artifact delivery.
     - **Executor:** report ONB start, blockers, and RF completion.
     - **Reviewer:** report REV start and REVIEW verdict (APPROVE / REVISE / REJECT).
   - Cross-session addressed messaging between active Antigravity threads is fully supported; role units must send formal notifications directly upon completing gate work instead of delegating status delivery to the human owner.
   ```

---

## 7. Definition of Failure

- ❌ 1. Отсутствие файла `.tfw/migrations/3.5.0.md` или пропуск инструкции по сохранению пользовательских файлов.
- ❌ 2. Сохранение устаревших ссылок на `.agent/workflows/` в `KNOWLEDGE.md` или `.tfw/glossary.md`.
- ❌ 3. Сохранение `.agent/rules/tfw.md` в любом из файлов `README*.md`.
- ❌ 4. Расхождение между `.agents/rules/tfw.md` и `.tfw/adapters/antigravity/tfw-rules.md.template`.
- ❌ 5. Падение автоматических тестов репозитория.
- ❌ 6. Модификация файлов вне согласованного знаменателя из 10 путей.

---

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Пропуск упоминания устаревших путей в локализациях `README` | Прогон ripgrep по всей кодовой базе перед формированием отчёта RF. |
| Рассинхронизация нумерации маршрутов (11 вместо 10) | Чёткая фиксация в AC-2 удаления `/tfw-resume` из исторической строки. |

---

## 9. Cross-Phase Modifications (multi-phase only)

| File | Also modified in | Coordination note |
|---|---|---|
| `KNOWLEDGE.md` | Phase A (было отложено) | Замечание §5 Проверяющего из Фазы A закрывается в рамках данной фазы. |

---

*TS — TFW_20260921-220500_AGSK / Phase B: Migration Guide and Documentation Sync | 2026-09-22*
