# Extract — «Чего не видно в сырых наблюдениях?»
> **Mindset:** Analyst. Из наблюдений построена конфигурационная модель.
> **Test:** пространство содержит комбинации, которых не было в Briefing.
> Parent: [HL-TFW_20260905-124029_RTPSN](../../HL-TFW_20260905-124029_RTPSN.md)
> Goal: вывести из корпуса и workflow surface проверяемую модель выбора, разрешения и применения session title.

## Configuration Space

Ниже перечислены непротиворечивые классы конфигураций. Строка `C12`, где
функциональный cue сочетается с legacy task ID и bare phase, не предлагалась в
Briefing и выявлена только после сопоставления dimensions.

| Config | D1. Первый cue | D2. Task cue | D3. Порядок | D4. Разделитель | D5. Phase cue | D6. Иерархия | D7. Момент разрешения | D8. Collision fallback | D9. Возможности host | D10. Область workflow |
|--------|----------------|--------------|---------------|-------------------|---------------|----------------|------------------------|------------------------|------------------------|------------------------|
| C1 | formal role | full ID | work→task→phase | pipe | `Phase A` | none | pre-read | full ID | rename+readback | task-bound |
| C2 | formal role | abbreviation | work→task→phase | pipe | `Phase A` | none | after state read | full ID | rename+readback | task-bound |
| C3 | exact skill | abbreviation | work→task→phase | middle dot | bare | none | after state read | full ID | rename+readback | task-bound |
| C4 | workflow function | abbreviation | work→task→phase | middle dot | bare | none | after state read | full ID | rename+readback | task-bound |
| C5 | workflow function | abbreviation | task→work→phase | middle dot | bare | none | after state read | full ID | rename+readback | task-bound |
| C6 | workflow function | abbreviation | work→task→phase | pipe | bare | none | after state read | full ID | rename+readback | task-bound |
| C7 | workflow function | abbreviation | work→task→phase | hyphen | bare | none | after state read | full ID | rename+readback | task-bound |
| C8 | emoji + function | abbreviation | work→task→phase | middle dot | bare | none | after state read | full ID | rename+readback | task-bound |
| C9 | hierarchy | abbreviation | hierarchy→task→phase | middle dot | bare | `LEAD` | after state read | host key | rename+readback | task-bound |
| C10 | workflow function | abbreviation | work→task | middle dot | omitted | none | after task selection | full ID | rename+readback | task-bound |
| C11 | workflow function | abbreviation | work→task→phase | middle dot | bare | none | after workflow-local selection | report once | rename+readback | conditionally task-bound |
| C12 | workflow function | legacy `TFW-##` | work→task→phase | middle dot | bare | none | after state read | host key | rename+readback | task-bound |
| C13 | workflow function | full ID | work→task→phase | middle dot | bare | none | after ID creation | host key | rename+readback | task created inside workflow |
| C14 | workflow function | abbreviation | work→task→phase | middle dot | bare | none | after state read | semantic discriminator | rename+readback | task-bound |
| C15 | workflow function | abbreviation | work→task→phase | middle dot | bare | none | after state read | report once | rename without readback | task-bound |
| C16 | workflow function | abbreviation | work→task→phase | pipe | bare | none | after state read | report once | rename unavailable | task-bound |
| C17 | — | — | — | — | — | — | workflow entry | — | any | project-wide |

## Findings

### E1. Двухслойная модель: semantic title и host transport

Наблюдения разделяются на два независимых слоя:

1. Semantic layer отвечает на три вопроса: какая работа выполняется, над какой
   задачей и, когда это существенно и известно, над какой фазой.
2. Host layer отвечает на операции: поддерживает ли host rename, сохраняет ли
   символы, позволяет ли прочитать результат и проверить title collisions.

Provider-neutral правило не может обещать одинаковое поведение host. Оно может
одинаково вычислять semantic string, затем выполнять доступную host operation и
однократно сообщать о недоступности или непроверяемом результате. Эта модель
сохраняет title как navigation metadata, а не переносит в него authority.

### E2. Детерминированный resolution pipeline

Из D2, D5, D7–D9 следует общий pipeline:

1. Выбранный workflow задаёт work function, но не новое полномочие.
2. Read Contract или workflow-local selection разрешает ровно одну task.
3. Для современного ID берётся утверждённая HL abbreviation, только если она
   уникальна среди доступных task roots; иначе берётся полный canonical ID.
   Для legacy task cue равен canonical `TFW-##`.
4. Phase cue берётся только из проверенного phase state или governing artifact;
   при отсутствии или неоднозначности весь phase segment опускается.
5. После render host выполняет rename. Если readback доступен, сравнивается
   фактическая строка. Невозможность rename/readback сообщается один раз и не
   блокирует основной workflow.

В этом pipeline не требуется угадывать ID, фазу, роль или порядковый номер
сессии. Для `/tfw-plan` новой задачи шаг 2 завершается лишь после создания ID;
это объясняет исключение из общего «сразу после Read Contract» placement rule.

### E3. Функция workflow образует минимальный устойчивый словарь

Точные skill names различают workflow, но тратят префикс `tfw-`; формальные роли
сливают разные функции: `Coordinator` не различает plan, resume и project-wide
coordination, а `Executor` не сообщает, что session запущена через handoff.
Функциональные токены дают однозначное отображение для task-bound surface:

| Workflow | Function token | Binding |
|----------|----------------|---------|
| `/tfw-plan` | `PLAN` | task-bound; new-task title после ID creation |
| `/tfw-research` | `RESEARCH` | task-bound; iteration не заменяет phase |
| `/tfw-handoff` | `EXEC` | task + phase после Read Contract |
| `/tfw-review` | `REVIEW` | task + phase после Read Contract |
| `/tfw-resume` | `RESUME` | task после selection; phase только если однозначна |
| `/tfw-docs` | `DOCS` | только single-task auto/manual mode |
| `/tfw-init` | `INIT` | только full-init после создания init-task |

`/tfw-knowledge`, `/tfw-release`, `/tfw-update` и `/tfw-config` не получают
task-oriented title: они project-wide и не разрешают единственный task cue.

### E4. Иерархия ортогональна workflow function

`LEAD` отвечает не на вопрос «какой workflow», а на вопрос «какое уже выданное
отношение координации надо различить». Поэтому он не может автоматически
подменять `PLAN`, `RESUME` или другую функцию. Непротиворечивы две модели:

- использовать обычный work token, когда governing state не требует отличать
  lead session;
- использовать отдельный `LEAD` только при явном CRATM/delegation binding и
  никогда не выводить его из слов «main»/«coordinator» в auto-title.

Такой `LEAD` остаётся label существующей связи, а не выдачей полномочий.

### E5. Collision — два разных класса, а не одна проблема

Abbreviation collision возникает между разными canonical task ID; его полностью
устраняет переход конкретного task cue к полному ID. Exact semantic collision
возникает между двумя sessions одной функции, задачи и фазы; полный task ID её
не устраняет. Существующий authoritative discriminator (`LEAD`, другая phase)
может различить такие sessions только когда он уже есть. В противном случае
остаётся несемантический host stable key либо однократный collision report.
Выдуманный ordinal (`#2`) ненадёжен: после archive/reorder он не имеет
авторитетного источника.

### E6. Consistency важнее вариативности сокращений

W3C указывает, что повторяющиеся функции следует идентифицировать одинаково:
пользователи переносят знакомое обозначение, могут искать его и получают более
предсказуемую навигацию. W3C также отмечает, что label не обязан быть длинным —
слово или даже один символ достаточно, если он даёт подходящий cue. Следствие
для модели: один токен должен всегда означать одну функцию, а phase может быть
bare token только внутри фиксированной позиции и документированной grammar.

Sources: [W3C Consistent Identification](https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification),
[W3C Headings and Labels](https://www.w3.org/WAI/WCAG21/Understanding/headings-and-labels).

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Semantic resolution отделён от host transport | Нужно выбрать canonical separator и ASCII fallback |
| Получен единый resolution pipeline без guessing | Нужно испытать его adversarial cases |
| Work-function vocabulary различает task-bound workflows | Нужно выбрать между function-first и task-first |
| Legacy-комбинация `REVIEW · TFW-37 · A` выявлена вне Briefing | Нужен verdict по bare phase и hierarchy exception |
| Abbreviation и exact semantic collisions разделены | Нужен точный fallback для exact collision без semantic source |
| W3C подтверждает ценность consistent concise labels | Human recognition speed/error всё ещё не измерены |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?

Stage complete: YES
→ User decision: продолжить к Challenge в рамках явного мандата завершить Iteration 2.
