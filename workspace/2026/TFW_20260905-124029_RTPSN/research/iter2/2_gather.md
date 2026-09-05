# Gather — «Чего мы ещё не знаем?»
> **Mindset:** Explorer. Карта пространства решений без преждевременного выбора.
> **Test:** все независимые измерения и альтернативы перечислены до этапа Challenge.
> Parent: [HL-TFW_20260905-124029_RTPSN](../../HL-TFW_20260905-124029_RTPSN.md)
> Goal: выбрать короткую, однозначную и переносимую грамматику названий TFW-сессий, которая помогает различать работу, задачу и фазу и не создаёт полномочий.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1. Первый cue | формальная роль (`Coordinator`) | точный skill (`tfw-plan`) | функция workflow (`PLAN`) | иерархия (`LEAD`) |
| D2. Task cue | полный canonical ID | утверждённая аббревиатура | legacy ID `TFW-##` | короткий ID с collision fallback |
| D3. Порядок | work → task → phase | task → work → phase | hierarchy → task → phase | phase → task → work |
| D4. Разделитель | ASCII pipe ` | ` | ASCII hyphen ` - ` | Unicode middle dot ` · ` | emoji/пиктограмма |
| D5. Phase cue | `Phase A` | `Ph.A` | позиционный bare token `A` | сегмент отсутствует |
| D6. Иерархия | не кодировать | `Main Coordinator` | `LEAD` | host/session discriminator |
| D7. Момент разрешения | до чтения состояния, из запроса | после чтения task state | после создания canonical ID | после workflow-local selection |
| D8. Collision fallback | полный task ID | существующий semantic discriminator | host stable key | одно сообщение о коллизии без догадки |
| D9. Возможности host | rename + readback | rename без readback | только auto-title | rename недоступен |
| D10. Область workflow | всегда task-bound | task-bound только в одном режиме | project-wide | task создаётся внутри workflow |

## Findings

### G1. Фактический корпус идентификаторов задач

В `workspace/2026/` обнаружены 10 современных task ID: `ASSISTED15`, `TLD`,
`FA15ES`, `CRATM`, `RDP`, `RTMW`, `RCFR`, `RTBO`, `VBSA`, `RTPSN`.
Коллизий аббревиатур в этом корпусе нет: 10 уникальных значений из 10.
Длина аббревиатур: от 3 до 10 символов; распределение — 3: 2, 4: 4,
5: 2, 6: 1, 10: 1. Полный современный ID занимает 23–30 символов,
среднее — 24,8. Кроме того, в репозитории есть 53 legacy-каталога с
canonical cue вида `TFW-##`; для них отдельная аббревиатура не нужна.

Эти числа относятся только к доступному checkout. Они не доказывают глобальную
уникальность аббревиатуры на других хостах или в ещё не подключённых task roots.

### G2. Наблюдаемые названия сессий в текущем приложении

Снимок sidebar API содержит 30 Codex-задач. Длина title: 13–59 символов,
среднее 29,6. Из них 18 начинаются с формальной роли и pipe, 9 содержат
буквальный сегмент `| Phase `, 2 используют em dash, 0 используют middle dot.
Видны одновременно сокращённые и полные формы, role-first и task-first:
`Reviewer | INNO-8 | Phase A`, `INNO-8 Phase A — coordinator`,
`Main Coordinator | 20260828-201343__catalog_intake_commands`.

Есть минимум четыре одинаковых title `Coordinator | INF-12`. Это наблюдаемая
коллизия sidebar-метаданных: task cue и формальная роль сами по себе не всегда
различают параллельные сессии. API не показывает фактическую ширину sidebar,
точку визуального обрезания или поведение поиска, поэтому по снимку нельзя
делать вывод о pixel-level truncation и discoverability.

### G3. Количественное сравнение длины

Для одного реального task cue и фазы получены следующие длины по Unicode code
points:

| Candidate | Length |
|-----------|-------:|
| `Coordinator | TFW_20260902-111644_CRATM | Phase A` | 49 |
| `Coordinator | CRATM | Phase A` | 29 |
| `tfw-plan · CRATM · A` | 20 |
| `COORD · CRATM · Ph.A` | 20 |
| `PLAN · CRATM · A` | 16 |
| `CRATM · PLAN · A` | 16 |
| `PLAN \| CRATM \| A` | 16 |
| `PLAN - CRATM - A` | 16 |
| `📝 PLAN · CRATM · A` | 18 |

Форма из 16 символов короче полного текущего шаблона на 33 символа (67,3%)
и формы с уже сокращённым task ID на 13 символов (44,8%). Emoji занимает один
grapheme, но два UTF-16 code units; это важно для host-лимитов, считающих не
пользовательские символы, а code units.

### G4. Авторитетные источники каждого cue

Название не является источником полномочий. Work cue можно разрешить только из
выбранного canonical `/tfw-*` workflow; Role Lock workflow остаётся отдельным
источником роли. Task cue разрешается из canonical `id` выбранного `status.md`
и утверждённой HL abbreviation, а не из слов пользователя или имени окна.
Phase cue разрешается из phase `status.md`/journal либо из явно связанного
governing artifact. При отсутствии однозначной фазы её нельзя угадывать.
Hierarchy cue допустим только когда CRATM или governing delegation/state уже
явно закрепляет lead/main-координацию; title не может создать такую связь.

### G5. Классификация всех workflow surface

| Class | Workflows | Точка, где появляется авторитетный task/phase context |
|-------|-----------|-------------------------------------------------------|
| Task-bound | `/tfw-plan`, `/tfw-research`, `/tfw-handoff`, `/tfw-review`, `/tfw-resume` | после task selection/read; для новой задачи `/tfw-plan` — после создания ID |
| Conditionally task-bound | `/tfw-docs`, `/tfw-init` | docs: после single-task Select/Triage; init: только после создания init-task в full-init mode |
| Non-task-bound | `/tfw-knowledge`, `/tfw-release`, `/tfw-update`, `/tfw-config` | project-wide context, единой task binding нет |

У текущих `/tfw-plan`, `/tfw-handoff` и `/tfw-review` уже есть неодинаковые
rename-инструкции. В handoff/review rename расположен до Read Contract и потому
может опереться лишь на текст запроса, а не на проверенное task state.
`/tfw-research` и `/tfw-resume` rename-инструкции не имеют.

### G6. Внешние рекомендации по видимым labels

W3C рекомендует видимые, читаемые, общеупотребительные labels: неясная подпись
заставляет пользователя угадывать, а пригодность формулировки следует проверять
с пользователями. Отдельная рекомендация Label in Name советует сохранять слова
видимой подписи в accessible name и помещать их в начало; символ сам по себе не
является human-language label. Это подтверждает значимость стабильного первого
текстового cue, но не определяет конкретное слово для TFW.

Sources: [W3C Clear Visible Labels](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p06-clear-labels/),
[W3C Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html).

Unicode прямо отмечает, что emoji/text presentation зависит от окружения и не
гарантируется одинаковой. Это создаёт переносимый риск для emoji как обязательной
части grammar, но не относится к обычному текстовому U+00B7 MIDDLE DOT.

Source: [Unicode Technical Standard #51](https://www.unicode.org/reports/tr51/tr51-7.html).

### G7. Доступность rename в Codex и границы переноса

Официальный Codex changelog для CLI 0.150.0 фиксирует auto-titles для unnamed
terminal tasks и команду `/rename`, предлагающую редактируемый title на основе
conversation. В текущем desktop host также доступны операция переименования и
readback title через app API. Это доказывает возможность для двух наблюдаемых
поверхностей, но не для каждого provider/host adapter.

Source: [ChatGPT & Codex changelog](https://learn.chatgpt.com/docs/changelog).

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Реальный корпус task ID и отсутствие текущих abbreviation collisions | Проверка коллизий должна выполняться на каждом доступном task root, а не считаться вечным свойством |
| Наблюдаемая неоднородность title и четыре одинаковых `Coordinator | INF-12` | Нет controlled human timing/error study для H1 |
| Сравнение длины 8 форматов и экономия до 67,3% | Нет pixel-level truncation/search measurements текущего UI |
| Классифицированы все 11 workflow | Нужно вывести единое placement rule и исключения |
| Rename подтверждён для current desktop и современного Codex CLI | Остальные host adapters не проверены |
| Emoji несёт presentation/length risk | Нужно сопоставить middle dot с ASCII fallback |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?

Stage complete: YES
→ User decision: продолжить к Extract в рамках явно заданного мандата завершить Iteration 2 без дополнительного approval gate.
