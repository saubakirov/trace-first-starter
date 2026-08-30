<!-- HELPDESK, THIRD UPDATE: 2.0.0-dirty.4 -> 2.0.0-dirty.5. Receiving project: helpdesk (Innoforce/Avtobys),
     D:/projects/research/helpdesk. Authored 2026-08-30 by the Claude Code session that performed the update,
     acting on behalf of `saubakirov`, and filed directly into TFW-60 at the owner's request.

     THIS IS THE CONSUMER RUN THE .5 TAG WAS CUT FOR. CHANGELOG .5, "Known open at this tag": "a consumer
     already on the line updating to this tag from Step -1, with the derived pin, the three questions and
     the briefing on record." All three are on record below, with what each one cost and what it returned.

     The operator has now run this project through 0.8.7 -> .3 -> .4 -> .5 in two days and reads the
     procedure with that bias: fluent, and no longer fresh. Stated up front.

     NO JOURNAL EVENT accompanies this file. conventions.md §4: an inbound advisory record escalates
     nothing and requests no verdict, and the closed `kind` vocabulary stays closed. -->

> **Status:** advisory. It states what happened and recommends; it decides nothing, amends no
> frozen section and changes no task state.
> **Relates to:** TFW-60 Phase AC — the consumer run its last acceptance criterion names.
> **Payload taken at:** tag `v2.0.0-dirty.5` = `cab7243` on `D:/projects/research/steps-framework`,
> derived **from the tag the operator named**, `VERSION` at that commit = `2.0.0-dirty.5`; source
> `.tfw/` clean at pin and at the Step 5 recheck. Baseline `v2.0.0-dirty.4` from `installed_from`.
> **Result in the receiving project:** 34 changed paths, uncommitted at the time of writing (the
> project's rule: no commit without the owner's word); 0 tasks renamed; 1 phase state file authored
> by hand on the owner's decision.

---

# Разбор полётов: обновление TFW 2.0.0-dirty.4 → 2.0.0-dirty.5

> Проект: `helpdesk`. Дата: 2026-08-30. Исполнитель: сессия Claude Code от имени `saubakirov`,
> режим CL — владелец присутствовал и ответил на один пакет вопросов. Стены — около 25 минут,
> из них один round-trip к владельцу. Предыдущие отчёты по этому проекту: `…third_external_update`
> (0.8.7 → .3) и `…helpdesk_dirty3_to_dirty4`.

## Одной строкой

**Пять из восьми болей вчерашнего отчёта закрыты и проверены на том же проекте за сутки — и
ровно в этот день ряд field report'ов TFW-60 столкнулся на общем порядковом счётчике: мой
«четвёртый» отчёт был перезаписан чужим «четвёртым» через минуту после записи.** Задача про
conflict-resistant shared workspace получила натурное доказательство собственной темы в
своём же каталоге. Ниже — что процедура `.5` сделала правильно, где она стала церемонией, и
два дефекта payload, которые получатель увидит первым делом.

## Что произошло, в числах

| Измерение | .4 (вчера) | .5 (сегодня) |
|---|---|---|
| Файлов изменено в payload | 16 | 24 (новый 1: `templates/briefing.md`) |
| Файлов, отличных от baseline `installed_from` | 2 | **2** — `knowledge_state.yaml` ⚫, `project_config.yaml` 🟡 |
| Ложных срабатываний | 0 | **0** |
| Пин | тег = HEAD (совпадение) | **тег → коммит → VERSION**; HEAD не читался |
| Вопросов владельцу до первой записи | 0 | **3 + 1** одним сообщением, один round-trip |
| Из них ответов, изменивших конфиг | — | **0** — все три подтвердили объявленное |
| `skipped:` строк на шаге копирования | — | 2 (ровно два project-owned файла) |
| Ручных слияний | 1 | 1 (конфиг: `version`, `installed_from` — 2 ключа) |
| Адаптеров | 6 копий | 6 копий + `.agent/rules/tfw.md` + **блок `TFW:CLAUDE` вставлен один раз**; Codex/Cursor не установлены — пропущены |
| Хитов ретированной лексики вне allowlist | 6 по букве / 0 по духу | **2 живых** — `adapters/README.md:31,38` (`{version}`); остальные 7 — инструкции ретирования, по новой формулировке в allowlist |
| Тесты payload | 177 p + 2 p 1 s | 204 p (framework) + **1 FAILED** 2 p 1 s (repository) |
| `--check tasks` | 30 задач | 30 задач + 1 информационная строка (HD-30, 2 фазы) |
| `--check project` | зелёный | зелёный, `2.0.0-dirty.5` |
| `build.*` | lint, verify; test **пропущен** | lint, verify, **test — 358 passed** |
| Фазовых `status.md` написано руками | 0 | 1 (HD-31/phase-a, решение владельца) |
| Переименовано задач | 0 | 0 |

## Чеклист обновления (durable-запись, потому что процедура не называет ей места)

- Источник: `D:/projects/research/steps-framework`, `target_ref=v2.0.0-dirty.5`,
  `source_head=cab7243737c68528d0a520d2d01e935ca585b022`, `VERSION`=`2.0.0-dirty.5` ✔
- Baseline: `installed_from: D:/…@v2.0.0-dirty.4` → тег достижим ✔
- Step −1: `update.md` прочитан из `.tfw/.upstream/`, не из установленного `.4` ✔
- Step 3, ответы владельца (одно сообщение, 2026-08-30):
  1. handle → `saubakirov` (существующий `team/saubakirov.md`; ничего не создано)
  2. `task_containers` → `[workspace, tasks]` (подтверждено)
  3. `build.*` → `make lint` / `make test-unit` / `gen_index --check tasks` (подтверждено, пути существуют)
  4. *(вне трёх)* HD-31 `phase-a/` без `status.md` под живой задачей → **написать** из шаблона
- Классификация: ⚫ 1, 🟡 1, дрейф/идентичных → перезапись 24 ✔
- Step 5: копия с исключениями, напечатано `skipped:` ×2; recheck тега ✔
- Step 6: 24 копии `cmp` ✔, `.agent/rules/tfw.md` = шаблон ✔, `CLAUDE.md` блок = шаблон ✔ (программно)
- Step 7: `version: 2.0.0-dirty.5`, `installed_from: steps-framework@v2.0.0-dirty.5` (символьное имя; путь — в этой строке) ✔
- Step 8: `--check index/tasks/project` ✔; тесты (см. дефект 1); allowlist (см. дефект 2); `/tfw-*` 12 строк ✔; `make lint` ✔ `make test-unit` 358 ✔
- Step 8a: брифинг доставлен владельцу последним сообщением сессии ✔
- Step 9: `.tfw/.upstream/`, `.tfw/.baseline/` удалены ✔

## Что сработало — и что из вчерашнего закрылось

**Step −1 исполнен буквально, и это было не бесплатно.** Установленный `.4` пинил от `HEAD`;
целевой `.5` — от названного тега. Здесь `HEAD == тег`, так что старая процедура тоже прошла
бы, — то есть исправление проверено на пути, где оно *не могло* сработать иначе. Честно: Step −1
подтверждён как привычка, не как спасение. Спасением он был бы у пятого потребителя, у которого
источник ушёл вперёд.

**Baseline из `installed_from` — второй день подряд 0 ложных срабатываний.** Вчерашняя боль 4
(«победа привязана к машине») закрыта формой `{upstream}@{tag}`; я записал
`steps-framework@v2.0.0-dirty.5`. Оборотная сторона — в §Что заболело, п. 4.

**Копирование с объявленными исключениями напечатало ровно то, что должно.** Две строки
`skipped:`, и правило «a copy that reports nothing skipped … is a failed step» даёт оператору
критерий, который он может проверить глазами за секунду. Вчера я писал этот цикл сам.

**Маркерный блок `TFW:CLAUDE` — вчерашняя боль 8 закрыта.** Наш `CLAUDE.md` маркеров не имел;
по правилу §9 я вставил блок один раз, вынес проектные секции (Project Context, Conduct, Code
Quality Mandate, Execution Modes) наружу и **программно** сравнил регион между маркерами с
шаблоном — `True`. Следующий синк — механический. Одна деталь: блок шаблона не содержит строки
про производный индекс `workspace/00-INDEX.md`, которую наш `.4`-рендер нёс в порядке загрузки;
я перенёс её в Project Context. Это правильно (маршрут — проектный), но оператор должен это
*заметить*, шаблон не подскажет.

**Антигравити-правило без `{version}`.** Копия = шаблон, `cmp` вместо подстановки. Вчерашний
`.agent/rules/tfw.md` был рендером с вписанным «TFW 0.8.5» два релиза назад — теперь такого
класса дрейфа нет.

**Фазовое состояние — гейт сказал ровно то, что нужно, и ровно столько.** HD-30 (закрытая, без
собственного `status.md`) — одна информационная строка, exit 0. HD-31 (`ONB`, живая) — была бы
failure; владелец решил писать. Шаблон с фазовым абзацем сделал это работой на две минуты, и
фраза «The task-level `status.md` never summarizes it» отличает файл от задачного без открытия
каталога. Хорошо.

**Allowlist по новой формулировке — вчерашняя боль 1 закрыта.** `update.md:82`, `init.md:125`
и цитата в `adapters/claude-code/README.md:71` — текст, назначение которого ретировать термин.
Правило теперь бинарно исполнимо на этих семи хитах. Но не на двух других — дефект 2.

**`build.test` запущен.** Вчера я его пропустил и записал это; сегодня `make test-unit` —
358 passed за 15 секунд. Пропуск был экономией, которая ничего не экономила.

## Дефекты payload — по тяжести

### 1. `-k repository` содержит тест, зашитый на корпус задач самого фреймворка

```
test_the_repository_stateless_phases_are_all_informational
E  AssertionError: {'HD-30__tickets_filters_creator_route_bus'}
   assert named == {"TFW-42__…", "TFW-46__…", "TFW-47__…", "TFW-52__…", "TFW-53__…", "TFW-55__…"}
```

Тест утверждает, что информационные строки `--check tasks` называют ровно шесть задач
**репозитория фреймворка**. На любом получателе он красный по построению. Это противоречит
двум обещаниям подряд: `.4` — «Framework tests and repository-state tests are separable.
Receiving projects can run the payload suite without inheriting checks against this
repository's own task corpus» — и `migrations/2.0.0.md` `.5`, который велит получателю после
миграции запустить именно `-k repository`. Два других repository-теста проходят/скипаются на
получателе корректно — значит, разделение задумано, а этот тест в него не вписан.

Цена для пользователя не в одном красном тесте, а в том, чему он учит: **документированный
гейт красный на корректном проекте → оператор учится читать «1 failed» как норму.** Это
худшее, что может сделать гейт. Исправление — либо третий маркер (`-k "repository and not
framework_corpus"`), либо тест читает ожидаемый набор из состояния репозитория, а не из
литерала, либо скип по `PROJECT_ROOT != framework root`.

### 2. `adapters/README.md` — живое употребление ретированной инструкции `{version}`

CHANGELOG `.5`: «The Antigravity and Cursor rule templates no longer require a `{version}`
substitution … A test refuses `{version}` in any adapter template». Шаблоны чисты. Но
`.tfw/adapters/README.md:31` показывает `# TFW {version}` как пример, а `:38` велит: «When
creating an adapter from a template, replace `{version}` with the value from `tfw.version`».
Это не ретирование — это инструкция сделать то, что релиз отменил. Тест её не видит, потому
что README не шаблон. Оператор, который читает README (а он для этого написан), получит
противоречие с `tfw-rules.md.template`, где подставлять уже нечего.

### 3. Порядковые имена field report'ов — общий счётчик в задаче про его отсутствие

Хронология по mtime и git:

- 11:27 — эта сессия записала `FIELD-REPORT__TFW-60__fourth_external_update.md` (helpdesk .3→.4)
  и правку-указатель в `…third_external_update.md`.
- 11:28 — сессия проекта `innoforce-ai-first` записала **свой** `…fourth_external_update.md`
  по тому же пути. Мой текст перезаписан.
- Коммит `6f0a600` «file the fourth external update's report» — чужой сессии — **включил мою
  правку третьего отчёта**, о которой она не знала: `git status` каталога стал чистым, и
  указатель «см. fourth» теперь вёл на чужой документ.
- 11:40 — третья сессия (`kaznpu-ai-lab`) записала `…fifth_external_update.md`.

Ни одна сторона не ошиблась: имя `fourth` было корректным для каждой в момент записи. Это
ровно та модель отказа, которую `conventions.md` §4 описывает для идентификаторов задач —
«no participant reads a project-wide maximum to learn which identifier is free» — и которую
ряд отчётов TFW-60 нарушает своим соглашением об именах. Мой отчёт восстановлен из контекста
сессии как `…helpdesk_dirty3_to_dirty4.md`; указатель в третьем исправлен. Рекомендация —
имена без счётчика: `FIELD-REPORT__TFW-60__{project}_{from}_to_{to}.md` или, по грамматике
самого фреймворка, `{YYYYMMDD-HHMMSS}__{project}`. И заметка в TFW-60: три отчёта за одно
утро от трёх операторов одного владельца — это уже не гипотетический сценарий.

## Что заболело в процедуре

### 1. Три вопроса на втором обновлении за сутки — церемония, а не решение

Все три ответа подтвердили то, что проект уже объявлял: один профиль в `team/`, вчерашний
`[workspace, tasks]` с комментарием владельца в конфиге, `build.*`, проверенный вчера. Я
поставил объявленные значения первыми с пометкой «Recommended», владелец выбрал их за один
проход — процедура это допускает, и round-trip стоил минуту. Но формулировка «asked, never
inferred» **не различает** проект без объявленного значения (вопрос обязателен) и проект с
объявленным (достаточно подтверждения). Четвёртый вопрос — про HD-31 — был единственным, где
владелец принимал решение, и его процедура не предусматривает: он возник из `--check tasks`.
Предложение: Step 3 формулировать как «present the declared value and ask for confirmation;
ask open-ended only where none is declared», и явно разрешить добавлять к пакету решения,
которые гейты подняли по ходу read-only шагов.

### 2. Чеклист — теперь три вещи, которые надо в него записать, и по-прежнему нет места

`.5` добавил: «record the answers in the checklist», «the checklist records that the briefing
was delivered», «for a local checkout … the path in the checklist». Вчерашняя боль 3 не
закрыта, а усилена: артефакт стал обязательным носителем трёх фактов и не имеет пути.
Я поместил его в этот отчёт (§Чеклист) и в сообщение коммита — оба места проект-специфичны.
Одна строка «the checklist lives at `{first-container}/UPDATE-{target}.md`» или «…in the
commit that records the update» закроет это окончательно.

### 3. Брифинг: «no free text» против «one bullet per Changed item»

Шаблон `briefing.md` бинден к CHANGELOG: одна пуля на пулю, без свободного текста. `Changed`
в `.5` — восемь пунктов, из которых шесть про саму процедуру обновления (пин от тега, Step −1,
маркеры, allowlist, форма `installed_from`, длина `update.md`). Для владельца helpdesk честный
ответ на «что вы теперь делаете иначе» по этим шести — «ничего: это делает оператор
обновления». Шаблон не разрешает ни пропустить пулю, ни сказать это словами. Я выполнил
правило — каждая пуля есть — и сгруппировал их так, чтобы владелец увидел два пункта, которые
касаются его (аббревиатура = инициалы; фазовый `status.md`), первыми. Предложение: разрешить
в блоке одну фиксированную фразу «*applies to the update operator, not to daily work*» как
допустимую «пулю-обёртку» для процедурных изменений.

### 4. `scope_budgets` — второй день подряд тихое изменение

Вчера маркер `FRAMEWORK → PROJECT` без строки в CHANGELOG. Сегодня **значения по умолчанию**
в шаблоне и таблица в `conventions.md` §5: 30/15/3000/30 → 50/50/5000/50 — и снова ни слова в
`.5`. Проектные 35/18/3500/26 сохранены (маркер PROJECT теперь на моей стороне), но владелец,
читающий конвенцию, увидит цифры, которых у него нет, и не узнает из CHANGELOG, что они
изменились. Ключ, помеченный «preserve on update», всё равно заслуживает строки в `### Changed`,
когда меняется его *умолчание*.

### 5. `installed_from` — символьное имя, которое ни на что не указывает

`steps-framework@v2.0.0-dirty.5` переживёт вторую машину — и на ней **не разрешится ни во
что**: `tfw.upstream` смотрит на GitHub без dirty-тегов, а символ `steps-framework` нигде не
определён. Процедура честно велит записать путь «в чеклисте» (см. боль 2). Для следующего
обновления это означает fallback baseline с объявленной неопределённостью — то, что `.4`
устранил. Не дефект `.5`; следствие неопубликованной линии тегов. Но пока dirty-теги не в
remote, `installed_from` в этой форме — обещание, которое проверить может только та машина,
что его дала.

## Что не трогалось и почему

- Codex (`.agents/`) и Cursor (`.cursor/`) не установлены — строки Step 6 пропущены, каталоги
  не созданы. `AGENTS.md` без блока `TFW:CODEX` — по правилу «report and leave»: отмечено,
  не тронуто.
- Ни одна задача, ни одно событие, ни один мигрированный `status.md` не переименованы и не
  переписаны. Индекс изменился на одну строку (HD-31 phase-a получила состояние).
- `knowledge_state.yaml`, `knowledge/`, `KNOWLEDGE.md`, `TECH_DEBT.md` — не открывались.
- HL существующих задач не получили `Title`/`Abbreviation` — поля для новых задач.
- **Не проверен негативный путь** `--check project` на `installed_from` с `D:/…`: я сменил
  форму до запуска гейта. Утверждение CHANGELOG «reports a drive letter» принято на веру.

## Рекомендации — по цене исправления

| # | Действие | Цена | Закрывает |
|---|---|---|---|
| 1 | Скипать/перемаркировать `test_the_repository_stateless_phases_are_all_informational` вне корня фреймворка | 3 строки | Дефект 1 |
| 2 | `adapters/README.md`: убрать пример `# TFW {version}` и инструкцию подстановки; расширить тест с шаблонов на README | 2 строки + 1 тест | Дефект 2 |
| 3 | Имена field report'ов без порядкового счётчика; заметка в TFW-60 о коллизии 11:27/11:28 | переименование | Дефект 3 |
| 4 | Step 3: «present declared value, confirm; ask open only where undeclared» + разрешить добавлять решения от гейтов | 3 строки | Боль 1 |
| 5 | Назвать путь чеклиста | 1 строка | Боль 2 (второй день) |
| 6 | `briefing.md`: допустимая фраза-обёртка для процедурных `Changed` | 2 строки | Боль 3 |
| 7 | CHANGELOG `.5` `### Changed`: строка о `scope_budgets` 30/15/3000/30 → 50/50/5000/50 | 1 строка | Боль 4 |
| 8 | Опубликовать dirty-линию в приватный remote, чтобы `installed_from` разрешался | инфраструктура | Боль 5 |

## Итог с точки зрения пользователя TFW

Удобно: да — вчерашние восемь болей за сутки стали тремя; всё, что процедура обещала
измерить, она измерила и напечатала. Понятно: да, кроме чеклиста, который стал обязательнее и
остался бездомным. Прозрачно: да — `skipped:`, `note:`, `not checked:` дают оператору три
разных слоя честности, и ни один не притворяется другим. Критика: два дефекта payload
получатель увидит в первые пять минут (красный repository-тест, `{version}` в README), и оба
учат тому, чему фреймворк учить не хочет — читать красное как норму и инструкцию как
устаревшую. И один урок вне payload: ряд отчётов о conflict-resistant workspace потерял отчёт
на конфликте имён.
