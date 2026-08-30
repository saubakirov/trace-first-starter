<!-- HELPDESK, SECOND UPDATE: 2.0.0-dirty.3 -> 2.0.0-dirty.4. Receiving project: helpdesk (Innoforce/Avtobys),
     D:/projects/research/helpdesk. Authored 2026-08-30 by the Claude Code session that performed the update,
     acting on behalf of `saubakirov`, and filed directly into TFW-60 at the owner's request.

     FILING NOTE. This report was first written to FIELD-REPORT__TFW-60__fourth_external_update.md at 11:27.
     At 11:28 another session (project innoforce-ai-first) wrote ITS fourth report to the same path and
     committed it (6f0a600); this text was overwritten on disk and restored from the authoring session's
     context under a project-qualified name. Ordinal report names are a shared counter — the thing TFW-60
     exists to remove — and two operators reached "fourth" within one minute. The name below carries the
     project and the two tags instead.

     NO JOURNAL EVENT accompanies this file. conventions.md §4: an inbound advisory record escalates
     nothing and requests no verdict, and the closed `kind` vocabulary stays closed. -->

> **Status:** advisory. It states what happened and recommends; it decides nothing, amends no
> frozen section and changes no task state.
> **Relates to:** TFW-60 Phase AB — the release cut *because of* the third report, tested on the
> same project that produced it.
> **Payload taken at:** `51677ff` on `D:/projects/research/steps-framework`, tag `v2.0.0-dirty.4`
> **verified to point at that commit** before `VERSION` was read, and re-verified before adapter
> sync. `.tfw/` of the source was clean; `tasks/` was dirty and, by the rule, ignored.
> **Result in the receiving project:** commit `6e9973a`, 23 files, 0 tasks renamed.

---

# Разбор полётов: обновление TFW 2.0.0-dirty.3 → 2.0.0-dirty.4

> Проект: `helpdesk`. Дата: 2026-08-30. Исполнитель: сессия Claude Code от имени `saubakirov`.
> Владелец был на связи, но ни один шаг вопроса не потребовал. Стены — около десяти минут,
> шесть содержательных вызовов инструментов. Предыдущий отчёт по тому же проекту —
> `FIELD-REPORT__TFW-60__third_external_update.md`; здесь я сравниваю с ним.

## Одной строкой

**Первое обновление из четырёх, в котором процедура ни разу не заставила меня додумывать, —
и первое, в котором я мог доказать, а не предположить, что ничего не потерял.** Ноль ложных
срабатываний против десяти вчера; ноль ошибок оператора против двух. Болит теперь не
процедура, а её края: где положить артефакты, которые она велит создать, и одно правило,
которое сам payload не проходит.

## Что произошло, в числах

| Измерение | .3 (вчера) | .4 (сегодня) |
|---|---|---|
| Файлов изменено в payload | 69 (мажор через четыре релиза) | 16 |
| Файлов, отмеченных как отличающиеся от baseline | 12 | 2 |
| Из них реальных (⚫ state / 🟡 customized) | 2 | **2** — `knowledge_state.yaml`, `project_config.yaml` |
| Ложных срабатываний | **10** | **0** |
| Ручных слияний | 1 | 1 (конфиг: 6 строк, все с маркером) |
| Адаптерных копий ре-синхронизировано | 24 + rules | 6 (`init`, `plan`, `update` × 2 слоя); `adapters/` не менялся |
| Ошибок оператора, пойманных гейтом | 2 | 0 |
| Тесты payload | 158 p / 2 f → 159 p | 177 p (framework) + 2 p 1 s (repository) |
| `--check index / tasks / project` | зелёные | зелёные, индекс байт-в-байт прежний |
| Переименовано задач | 0 | 0 |
| `build.*` выполнено | lint, verify | lint, verify; **`test` — не запускался** (см. §Что я пропустил) |
| Коммитов | 0, затем 1 по просьбе | 0, затем 1 по просьбе |

## Что стало хорошо — и почему это видно именно сегодня

**1. Пин источника — две строки bash, которые закрыли вчерашнюю ложь.** Вчера CHANGELOG .3
писал «tagged locally», а `git tag` тега не показывал; `installed_from` записал коммит. Сегодня
процедура начинается с `test "$tag_commit" = "$source_head"` — и тег есть, и указывает куда
надо. Тот же тест повторяется перед синком адаптеров. Как пользователю мне важно другое:
**это проверка, которую я не мог бы придумать сам без вчерашнего ожога**, а теперь она стоит
в тексте первой.

**2. Baseline = `installed_from`, а не `v{current}`.** Главная победа релиза, и она
измерима: `git archive edab067` рядом с `git archive 51677ff`, `diff -rq` между тремя
деревьями — и различия от baseline ровно два файла, оба ожидаемые. Все 16 изменённых файлов
я скопировал **не открывая**, потому что процедура доказала, что смотреть нечего. Вчера
на 10 ложных `CUSTOMIZED` ушло по пять минут `diff --strip-trailing-cr` на каждый.

**3. `git archive` вместо копии рабочего дерева.** `__pycache__` источника в payload не
попал; вчера я вычищал его руками.

**4. Ретированные ключи названы трижды и одинаково.** CHANGELOG, `update.md` Step 3 и
`--check project`: `initial_seq`, `id_max_retries`, `review.default_mode`. У меня был второй;
третьего не было. Я не проверял это по памяти — знал, что `--check project` назовёт промах.
**Гейт, который скажет, чего именно я не сделал, — это и есть прозрачность.**

**5. Тесты разделены на framework и repository.** `-k "not repository"` → 177 passed;
`-k repository` → 2 passed, 1 skipped на проекте-получателе. Вчера два repository-теста
падали до миграции, и я полчаса разбирался, мой ли это дефект.

**6. `update.md` ужался до 840 слов.** Каждая команда — одна строка на копирование.

**7. `not checked:` в каждом выводе.** Как пользователю мне это дороже зелёного статуса.
Именно из этого списка я взял «adapter copies» и написал `cmp`-цикл.

## Что заболело

### 1. Правило allowlist в Step 6 не проходит сам payload

Grep по `id_max_retries|review\.default_mode|initial_seq` без CHANGELOG и `migrations/` даёт
шесть хитов: `workflows/update.md:69`, `workflows/init.md:123` и их четыре адаптерные копии.
Оба места — инструкции ретирования. По духу — allowlist; по букве («canonical migration or
changelog text») — нет. Правило написано как бинарное и бинарно не исполнимо: **у каждого
получателя оно формально красное на свежем payload**. *(Закрыто в `.5`: «text whose purpose
is to retire the term».)*

### 2. Step 3 велит сравнить с baseline — и не говорит, как

Для target процедура задаёт `.tfw/.upstream/` и `git archive`; для baseline — ни каталога, ни
команды. Я изобрёл `.tfw/.baseline/` по аналогии; Step 9 о нём не знает.

### 3. Step 4 велит написать чеклист — и не говорит, куда

Вчера чеклист жил в `MIGRATION.md`, потому что мажор дал ему дом. Сегодня — только в
терминале. Единственная durable-запись о классификации — сообщение коммита, которое я написал
сам.

### 4. `installed_from` — локальный путь, который не переживёт вторую машину

`D:/projects/research/steps-framework@v2.0.0-dirty.4`: на другой машине — путь в пустоту, а
`tfw.upstream` смотрит на GitHub, где dirty-тегов нет. Сегодняшняя победа (0 ложных
срабатываний) — **свойство машины, а не проекта**. *(Закрыто в `.5`: `{upstream}@{tag}`,
`--check project` ловит путь.)*

### 5. `scope_budgets` тихо сменил маркер `← FRAMEWORK` → `← PROJECT`

Правильно, но **CHANGELOG молчит**, а это смена контракта: вчера `tfw-update` имел право
перезаписать четыре числа, сегодня — нет.

### 6. Комментарии рядом с `← PROJECT`-ключами наследуют словарь версии

Вчерашний комментарий владельца говорил «new clock-id tasks»; сегодня грамматика другая, и
никакой diff против baseline этого не поймает — он и есть кастомизация. Поправил руками.

### 7. Новая грамматика — цена для пользователя, о которой релиз не говорит

- **Тема коммита.** `[claude-code/HD_20260830-143000_PWA/phase-a/executor]` — 50 символов
  из 72. Конвенция про длину subject этого не обсуждает.
- **`ABBR` = латиница без объявления.** `[A-Z0-9]+` для проекта с `content_language: ru`;
  ни конвенция, ни шаблон HL не говорят «Latin uppercase». *(В `.5` — инициалы одобренного
  названия; латиница по-прежнему не названа словом.)*

### 8. «Claude rules → managed `CLAUDE.md` content» — без маркеров

Codex получил marker-bounded block, Claude — «managed content» без границ. *(Закрыто в `.5`:
`TFW:CLAUDE:START/END`.)*

## Что я пропустил — и говорю об этом

- **`build.test` не запускался.** `make test-unit` — полный юнит-набор API; я ограничился
  `lint` и `verify`. Утверждение «build still passes» в моём коммите относится к lint и
  task-state, не к тестам приложения.
- **Существующие HL не получили строку `Abbreviation:`.** Осознанно; ни один гейт её не читает.

## Итог с точки зрения пользователя TFW

Удобно: да — впервые обновление не потребовало ни одного суждения о содержимом файлов.
Понятно: да, кроме двух мест, где процедура велит создать артефакт и не говорит где.
Прозрачно: да — каждый гейт печатает, чего он не проверял; это лучшее свойство релиза.
Критика: одно правило (allowlist) написано как бинарное и бинарно не исполнимо; одно
изменение контракта (`scope_budgets`) не объявлено; одна главная победа (`installed_from`)
привязана к машине, а не к проекту. Три из четырёх закрыты в `.5` — см. отчёт
`FIELD-REPORT__TFW-60__helpdesk_dirty4_to_dirty5.md`.
