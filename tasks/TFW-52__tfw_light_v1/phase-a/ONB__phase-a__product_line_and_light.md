# ONB — TFW-52 / Phase A: линейка редакций и стабильный Light

> **Date**: 2026-08-08
> **Author**: Codex (Executor)
> **Status**: 🟠 ONB — Approved 2026-08-08
> **Parent HL**: [HL-TFW-52](../HL-TFW-52__tfw_light_v1.md)
> **TS**: [TS Phase A](TS__phase-a__product_line_and_light.md)

---

## 1. Understanding

Phase A должна превратить замороженный четырёхфайловый baseline TFW-51 в самостоятельную редакцию Light внутри новой продуктовой линейки. Исполнение ограничено созданием `editions/README.md`, копированием четырёх baseline-файлов в `editions/01-light/` с тремя строго перечисленными видами правок и точечной вставкой в корневой `README.md`. Assisted, hooks, `.codex/`, Team, автоматическая консолидация, `.tfw/` и исторический TFW-51 не входят в scope. После реализации Light должен пройти два реальных не-кодовых прогона в отдельных Codex-сессиях на двух чистых проектах вне `steps-framework`; только после полного evidence допускается RF.

## 2. Entry Points

- `tasks/TFW-52__tfw_light_v1/HL-TFW-52__tfw_light_v1.md` — утверждённый стратегический контракт rev. 2.
- `tasks/TFW-52__tfw_light_v1/phase-a/TS__phase-a__product_line_and_light.md` — утверждённый контракт Phase A; отдельного Phase HL нет по явному решению TS.
- `tasks/TFW-51__tfw_light_ru/tfw-light-ru/README.md` — baseline и единственная обязательная содержательная правка инструкции установки.
- `tasks/TFW-51__tfw_light_ru/tfw-light-ru/AGENTS.md` — baseline без содержательных изменений.
- `tasks/TFW-51__tfw_light_ru/tfw-light-ru/TASKS.md` — baseline без изменений.
- `tasks/TFW-51__tfw_light_ru/tfw-light-ru/memory/PROJECT.md` — baseline с добавлением полей активной редакции и версии.
- `README.md` — точечный вход в линейку и Task Board; файл уже содержит чужие незакоммиченные изменения.
- `tasks/TFW-52__tfw_light_v1/phase-a/evidence/` — будущие EV и артефакты двух внешних прогонов.

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions.

## 4. Recommendations (suggestions, not blocking)

1. Считать лимиты из TS (14 файлов, 8 новых, 12 изменённых, 1200 LOC) действующим более строгим потолком Phase A, хотя незакоммиченный `.tfw/project_config.yaml` сейчас показывает 30/15/30/3000. Фаза укладывается в оба набора, поэтому scope менять не требуется.
2. Сохранить до реализации SHA-256 всех четырёх файлов TFW-51 и повторить проверку перед RF; это даст прямой артефакт для AC-8 без изменения исторической папки.
3. После готовности продуктовых файлов подготовить два конкретных чистых пути и нейтральные входы вне `steps-framework`, затем запросить у координатора запуск двух отдельных Codex-сессий. Не выполнять AC-6/7 в этой сессии и не подменять их локальной симуляцией.

## 5. Risks Found (edge cases, potential issues not in TS)

1. В checkout уже есть чужие незакоммиченные изменения: `.tfw/project_config.yaml`, `README.md`, весь каталог TFW-52 и `tasks/TFW-53__hl_contract_and_goal_defence/research/iter2/`. Коммиты этой стадии должны добавлять только явно выбранные собственные файлы и не захватывать соседние traces.
2. Строка TFW-52 в Task Board сама является частью чужого незакоммиченного diff. Её ONB-обновление можно сохранить в working tree, но нельзя включать в ONB-коммит вместе с исходным чужим добавлением строки.
3. AC-6 и AC-7 зависят от диспетчеризации координатором отдельных пользовательских Codex-сессий. Это не блокирует реализацию, но блокирует VERIFIED evidence и RF, пока оба прогона фактически не завершены и их файлы не скопированы в `phase-a/evidence/`.
4. Прогоны могут случайно унаследовать инструкции `steps-framework`, если чистый проект окажется внутри репозитория или сессия будет открыта не в его корне. EV должен фиксировать абсолютный внешний путь и отдельную сессию для каждого прогона.
5. AC-2 допускает только три вида отличий от baseline. Форматирование, стилистические улучшения, изменение переводов или структуры `TRACE.md` создадут автоматический Definition of Failure даже при хорошем пользовательском результате.

## 6. Inconsistencies with Code (spec vs reality)

1. TS фиксирует лимиты 14/8/12/1200, а текущий незакоммиченный `.tfw/project_config.yaml` содержит 30/15/30/3000. Это не блокирует Phase A: план 6 продуктовых файлов и около 250 LOC проходит более строгий контракт TS. Config не изменяется.
2. Task Board показывает `🟡 TS_DRAFT (A)`, хотя Phase TS имеет статус `✅ TS_APPROVED`. Переход строки в `🟠 ONB (A)` выполняется после создания этого ONB.
3. `editions/` пока отсутствует, что соответствует pre-implementation состоянию и не противоречит TS.
4. Baseline TFW-51 фактически содержит ровно четыре файла; `tfw-light-ru` не встречается в их содержимом. Третий разрешённый вид правки из TS применяется только при наличии совпадения и не требует искусственно создавать diff.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | K1 — `.tfw/README.md`, The Problem / The Thesis | ✅ | Applied | Light сохраняет task-local trace и короткую память как переносимый контекст, а не как дополнительную церемонию. |
| 2 | K2 — `.tfw/README.md`, Structural Enforcement / Naming Creates Behavior | ✅ | Applied | Ровно четыре стартовых файла и будущий `work/.../TRACE.md` проверяются структурно; названия редакций и путей не варьируются. |
| 3 | K3 — `.tfw/README.md`, Candor Over Flattery / Honesty Over Convincingness | ✅ | Applied | Ручные пределы Light и отсутствие Assisted после Phase A будут названы прямо; AC-6/7 нельзя объявить пройденными без реальных прогонов. |
| 4 | K4 — `KNOWLEDGE.md` D22 | ✅ | Applied | Автоматическая консолидация исключена; Phase A сохраняет только ручной перенос долговечного знания. |
| 5 | K5 — `KNOWLEDGE.md` D28, D33 | ✅ | Applied | Используются точные названия и Working Backwards до содержательных действий; структура baseline не переименовывается. |
| 6 | K6 — `KNOWLEDGE.md` D40, D47 | ✅ | Applied | Линейка объясняется через ценность работы; новый starter не получает чужое runtime-состояние. |
| 7 | K7 — `KNOWLEDGE.md` D56 | ✅ | Applied | TFW-51 остаётся замороженным источником; новая редакция создаётся копированием, исходник не редактируется. |
| 8 | K8 — `knowledge/philosophy.md` F3, F4, F7, F13 | ✅ | Applied | Критическая проверка, структурные gates, MVP-граница и domain-agnostic язык применяются без расширения Phase A. |
| 9 | K9 — `knowledge/process.md` F4, F5, F6 | ✅ | Applied | ONB записан до чата о готовности; реализация будет следовать AC/gates и не расширять scope по собственной инициативе. |
| 10 | K10 — `knowledge/constraint.md` F1, F2, F7 | ✅ | Applied | Light остаётся коротким, не хранит личные предпочтения как общие факты и проверяется на двух не-кодовых сценариях. |
| 11 | K11 — `knowledge/stakeholder.md` F1, F3 | ✅ | Applied | Публичный вход формулируется через полезность для работы; синтетическая проверка не заменяет AC-6/7. |
| 12 | K12 — HL TFW-51 | ✅ | Applied | Сохранены четыре файла, пять статусов, лимит трёх вопросов, структура trace и словесные лимиты baseline. |
| 13 | K13 — RES TFW-52 iter1 | ✅ | Applied | `editions/` трактуется как утверждённое решение текущего масштаба, а Working Backwards — как контракт вперёд; глобальные утверждения не добавляются. |
| 14 | K14 — RES TFW-52 iter2 | ✅ | Applied | Границы hooks, identity и shared-memory риска относятся к Phase B; Phase A не создаёт заготовки под них. |
| 15 | K15 — RES TFW-52 iter3 | ✅ | Applied | Team полностью исключён; `03-team/` и ролевые обещания не создаются. |
| 16 | NEW — `knowledge/process.md` F26 | ✅ | Applied | Executor вправе сделать локальные коммиты только для принадлежащих ему файлов текущей стадии. |
| 17 | NEW — `knowledge/constraint.md` F8 | ✅ | Applied | Commit Attribution форматирует уже разрешённый коммит, но не создаёт cadence или push-authority; push запрещён делегированием. |

---

*ONB — TFW-52 / Phase A: линейка редакций и стабильный Light | 2026-08-08*
