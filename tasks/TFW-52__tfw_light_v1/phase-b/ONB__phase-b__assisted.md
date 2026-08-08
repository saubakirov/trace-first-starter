# ONB — TFW-52 / Phase B: Assisted

> **Date**: 2026-08-09
> **Author**: Codex (Executor)
> **Status**: 🟠 ONB — Approved 2026-08-09
> **Parent HL**: [HL-TFW-52](../HL-TFW-52__tfw_light_v1.md) — ✅ HL_APPROVED rev. 2
> **TS**: [TS Phase B](TS__phase-b__assisted.md) — ✅ TS_APPROVED 2026-08-09

---

## 1. Understanding

Phase B должна создать самостоятельный русскоязычный Codex-first starter-root `editions/02-assisted/`, который сохраняет понятное ядро Light, но снимает наблюдённую ручную рутину через статусные папки, task-local traces, локальную заявленную атрибуцию, основу памяти и установленные/trusted hooks `SessionStart`, `PreCompact`, `Stop`. Фаза не имеет права закрыться на чтении файлов или синтетических вызовах обработчика: после реализации Coordinator должен запустить отдельные внешние Codex-сессии на новых корнях вне `steps-framework`, включая одинаковый многозадачный контроль Light/Assisted. Периодическая консолидация, Team/ролевые режимы, аутентификация и Full остаются вне scope. Если AC-8 покажет слабую или нулевую разницу, Executor фиксирует первый результат и немедленно возвращает его Coordinator без повторного «улучшенного» прогона.

## 2. Entry Points

- `tasks/TFW-52__tfw_light_v1/HL-TFW-52__tfw_light_v1.md` — master contract rev. 2; отдельного Phase HL нет по явному контракту TS.
- `tasks/TFW-52__tfw_light_v1/phase-b/TS__phase-b__assisted.md` — точные AC, DoF, affected files и evidence plan.
- `tasks/TFW-52__tfw_light_v1/phase-a/RF__phase-a__product_line_and_light.md` и `REVIEW__phase-a__product_line_and_light.md` — фактический predecessor и verdict `APPROVE`.
- `editions/README.md`, `editions/01-light/` и корневой `README.md` — текущая продуктовая линия, frozen Light input и две разрешённые точки модификации.
- `tasks/TFW-52__tfw_light_v1/research/iter2/RES.md` и `2_gather.md` — доказательные границы hooks, root, identity и risk gate; iter1/iter3 прочитаны для migration/Team boundaries.
- [Official Codex Hooks manual](https://learn.chatgpt.com/docs/hooks) — текущий публичный контракт events, trust, config и wire fields.
- Локально установленный `OpenAI.Codex` `26.727.6591.0`; bundled `codex-cli 0.146.0-alpha.9.2`; `hooks` помечены `stable`. Бинарный SHA-256: `ECD7A3EAFF5E42723DBBA03B5C91514B3986B5DB5CBCA8F34619620B5356F31F`.
- `.tfw/project_config.yaml` — authoritative budgets `30 files / 15 new / 3000 LOC / 30 modified`; TD-125 закрыт commit `49f5e27`.
- `tasks/TFW-52__tfw_light_v1/phase-b/evidence/` — будущий EV и индекс артефактов; live roots должны создаваться только под новым уникальным путём `D:\projects\research\tfw52-phase-b-runs\`.

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions.

Executor всё равно не переходит к реализации до явного решения Coordinator по этому ONB-gate.

## 4. Recommendations (suggestions, not blocking)

1. Реализовать один файловый контракт состояния на двух платформах: одинаковые event arguments и observable outcomes в `tfw-hook.ps1`/`tfw-hook.sh`; никаких отдельных scripts по событиям. `SessionStart` должен безопасно обрабатывать не только обязательные `startup`/`resume`, но и документированный `compact`, не создавая задачу при `active_task = none`.
2. До handler dispatch разрешать Assisted-root прямо в `command`/`commandWindows` ancestor-walk по точным полям `Активная редакция` и `Версия редакции`. Относительный `.codex/hooks/...` путь и `git rev-parse` не использовать: официальный manual подтверждает, что commands получают session `cwd`.
3. Локальную привязку хранить вне синхронизируемого проекта под стабильным `project_id`; shared `CURRENT_USER` не создавать. В проекте остаются только профили и заявленная provenance; automation использует отдельного актора.
4. Считать forecast TS `9 new / 2 modified / ≈700 LOC` продуктовым implementation budget. ONB/RF/EV и требуемые evidence attachments являются обязательными trace outputs, как в Phase A, но должны быть минимальны и агрегированы; live roots не копировать в репозиторий целиком, если достаточно hash/tree/log/точечных файлов по TS.
5. После готовности mechanisms и локальной verification остановиться и отправить Coordinator отдельный pre-evidence отчёт. Ни один внешний Codex run из этой Executor-сессии не запускать.
6. Предварительный dispatch plan после реализации:
   - `hooks-lifecycle-01`: clean Assisted root; install/trust, startup/resume, реальный compact, aligned/misaligned one-shot Stop, root fixtures и visible manual fallback; ожидаются tree, install/trust log, event effects и handler hashes.
   - `control-light-01` и продолжение во второй сессии: один frozen сценарий из ≥3 последовательных не-кодовых задач; ожидаются все traces/results и четыре метрики AC-8.
   - `control-assisted-01` и продолжение во второй сессии: те же prompts/inputs в том же порядке; ожидаются traces/results/candidates и те же метрики. При слабой разнице — немедленный stop/report Coordinator.
   - `risk-gate-01`: искусственный секрет и искусственные медицинские ПДн; ожидаются отсутствие shared записи, состояние inbox и точный один вопрос.
   - `migration-01`: заполненный Light → Assisted плюс duplicate-contract refusal; ожидаются before/after tree, content hashes и заполненный migration record.
   - `participants-a` / `participants-b`: две Coordinator-created sessions на одном общем non-Git root, разные задачи и profiles; ожидаются writer map, отдельные traces/candidates и отсутствие общего mutable hotspot.
7. Перед каждым из этих runs Executor отправит Coordinator отдельный exact bounded prompt, абсолютный новый root и исчерпывающий список ожидаемых артефактов. Повторно использовать или перезаписывать существующий run запрещено.

## 5. Risks Found (edge cases, potential issues not in TS)

1. Trust относится к точному hash hook-definition. Любая правка `hooks.json` или command после trust делает definition skipped до re-review; evidence должен фиксировать hash и не менять implementation между trust и run.
2. Official contract запускает все matching command hooks и может делать это конкурентно. Локально global/project hooks сейчас отсутствуют, но Assisted не должен заявлять эксклюзивность или полагаться на порядок относительно чужих hooks.
3. Документированного события «содержательная задача началась» нет. `AGENTS.md` обеспечивает семантическую активацию до durable action; hooks проверяют observable state. `Stop` слишком поздний, чтобы сам доказать trace-first ordering, поэтому live evidence нужны transcript order и file timestamps/content.
4. `PreCompact` обязан пройти реальную manual/auto compaction: прямой вызов handler является fixture, но не lifecycle evidence. Coordinator-created session должна сохранить наблюдаемый callback effect.
5. `Stop` создаёт continuation prompt, а не отклоняет ход. Первый mismatch может продолжить ровно один раз; при `stop_hook_active = true` повторное расхождение должно быть сохранено/сообщено без второго continuation и без тихого исправления.
6. Handler может проверить deterministic secret patterns, но не является смысловым классификатором медицинских/юридических/персональных категорий. Последние удерживает модель по `AGENTS.md`; тексты продукта не должны приписывать эту способность hook.
7. Две локальные Codex-сессии на общей папке доказывают разделение путей и writer ownership, но не дают provider-specific гарантии атомарности или конфликтов синхронизации. EV должен формулировать ровно наблюдённое.
8. AC-8 дорог и чувствителен к prompt drift. Все входы и формулировки надо заморозить до первого Light run; после наблюдения результата нельзя менять сценарий для Assisted или переигрывать слабый outcome.
9. Миграция обязана сохранить исходные `README.md`, `AGENTS.md`, `TASKS.md`, `memory/PROJECT.md`, traces и results рядом как provenance; «аккуратное» удаление или переписывание будет DoF.
10. В checkout присутствуют чужие незакоммиченные изменения только в TFW-53. Любой stage/commit должен использовать точные pathspecs Phase B и разрешённые README, без reset/checkout/revert и без захвата TFW-53.

## 6. Inconsistencies with Code (spec vs reality)

1. Task Board показывает `✅ DONE (A) · 🟡 TS_DRAFT (B)`, хотя Phase B TS уже имеет `✅ TS_APPROVED`. Создание этого ONB требует точного перехода строки в `🟠 ONB (B)` и добавления ссылки; остальной Task Board не меняется.
2. TS forecast перечисляет 9 product files и 2 modifications, но обязательные ONB/RF/EV/evidence traces добавляют отдельные файлы. Это не продуктовый scope drift, однако итоговый RF должен раздельно показать product files и workflow/evidence artifacts и проверить budget accounting прозрачно.
3. `.tfw/project_config.yaml` содержит `content_language: en`, тогда как approved TS и делегация явно требуют русскоязычный Assisted. Для этой фазы explicit TS/user contract применяется к наполнению; canonical template headings ONB/EV/RF остаются English.
4. До реализации отсутствуют `editions/02-assisted/`, repository `.codex/hooks.json` и global `~/.codex/hooks.json`; это ожидаемое pre-implementation состояние. Текущий repository root trusted, но каждый внешний clean root и каждая новая hook definition ещё потребуют отдельного trust-review.
5. Official manual и установленный build согласуются с TS guidance: `SessionStart` sources `startup/resume/clear/compact`, `PreCompact` triggers `manual/auto` и игнорирует plain stdout, `Stop` имеет `stop_hook_active`/`last_assistant_message`, `commandWindows` поддерживается, async hooks не поддерживаются. Доказанных schema/API расхождений на ONB нет.
6. Bundled executable из WindowsApps нельзя запустить непосредственно из shell (`Access is denied`), но его точная diagnostic copy запускается и сообщает `codex-cli 0.146.0-alpha.9.2`; `doctor` дал `17 ok / 0 warn / 0 fail`, а `features list` подтвердил `hooks stable true`. Live evidence всё равно должно выполняться через реальные Coordinator-created Codex sessions, а не через эту diagnostic copy.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | K1 — `.tfw/README.md`, The Problem / The Thesis | ✅ | Applied | Task-local traces и одна короткая карта памяти остаются переносимым контекстом между сессиями. |
| 2 | K2 — `.tfw/README.md`, Structural Enforcement / Naming Creates Behavior | ✅ | Applied | Статус определяется папкой; exact marker names и paths становятся проверяемым контрактом. |
| 3 | K3 — `.tfw/README.md`, Candor Over Flattery / Honesty Over Convincingness | ✅ | Applied | Manual fallback, trust gap и слабый AC-8 outcome называются прямо; availability не выдаётся за evidence. |
| 4 | K4 — `KNOWLEDGE.md` D22 | ✅ | Applied | Consolidation lifecycle не реализуется; создаётся только пригодная файловая основа. |
| 5 | K5 — `KNOWLEDGE.md` D28, D33 | ✅ | Applied | Working Backwards фиксируется до работы; точные имена используются как поведенческие cues без длинной церемонии. |
| 6 | K6 — `KNOWLEDGE.md` D40, D47 | ✅ | Applied | Пользовательский слой объясняет business value; новый starter не получает чужое project state. |
| 7 | K7 — `KNOWLEDGE.md` D56 | ✅ | Applied | Frozen TFW-51 и содержательная часть Light остаются read-only; migration сохраняет provenance. |
| 8 | K8 — `knowledge/philosophy.md` F3, F4, F7, F13 | ✅ | Applied | Критическая проверка, filesystem gates, MVP-boundary и domain-agnostic русский язык ограничивают решение. |
| 9 | K9 — `knowledge/process.md` F4, F5, F6 | ✅ | Applied | ONB записывается до сообщения, работа идёт по AC dependencies, а scope explosion запрещён. |
| 10 | K10 — `knowledge/constraint.md` F1, F2, F7 | ✅ | Applied | Local identity не попадает в shared state, пользовательские файлы имеют word limits, evidence остаётся non-code. |
| 11 | K11 — `knowledge/stakeholder.md` F1, F3 | ✅ | Applied | Assisted оценивается по полезному живому результату и сравнению с Light, не по synthetic checks. |
| 12 | K12 — HL TFW-51 | ✅ | Applied | Сохраняются цель, trace, пять статусов, memory semantics и понятный не-кодовый рабочий цикл Light. |
| 13 | K13 — RES TFW-52 iter1 | ✅ | Applied | Visible edition root и bounded preservation check используются без migration platform или глобальных гарантий. |
| 14 | K14 — RES TFW-52 iter2 | ✅ | Applied | Hook trust, next-start boundary, attribution≠authentication и capture-time risk gate формируют implementation/evidence boundaries. |
| 15 | K15 — RES TFW-52 iter3 | ✅ | Applied | Team/roles не поставляются; разные sessions нужны только как evidence carriers по прямому контракту делегации. |
| 16 | NEW — `KNOWLEDGE.md` D57 | ✅ | Applied | Фактический Phase A result закрепляет `editions/` topology, available Light, Full=`.tfw/` и Phase B ownership of Assisted. |
| 17 | NEW — `KNOWLEDGE.md` D53 | ✅ | Applied | Mandatory `evidence/` + EV и resolved artifact references применяются до RF; assertion без файла не получает VERIFIED. |
| 18 | NEW — `KNOWLEDGE.md` D54 | ✅ | Applied | Codex surface проверяется по реальному adapter/manual contract; `/tfw-*` Full adapter не копируется в короткий Assisted starter. |

---

*ONB — TFW-52 / Phase B: Assisted | 2026-08-09*
