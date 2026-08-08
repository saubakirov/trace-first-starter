# TFW-52 Phase A — AC-6 / AC-7 dispatch contract

> **Prepared:** 2026-08-08
> **Status:** NEEDS ATTENTION — two independent Codex tasks must be dispatched by the Coordinator
> **Product commit:** `07739b5`

## AC-6 — Contradiction analysis

**Clean project root:** `D:\projects\research\tfw52-phase-a-runs\run-1-contradictions`

**Exact prompt:**

```text
Работай только в открытом корне D:\projects\research\tfw52-phase-a-runs\run-1-contradictions как в самостоятельном чистом проекте TFW Light. Сначала прочитай по порядку AGENTS.md, README.md, memory/PROJECT.md и TASKS.md, затем все три файла в inputs/.

Контекст первого запуска: я Марина, руководитель проекта подготовки единого реестра закупок. Результат нужен руководящему комитету до допуска системы к производственной работе. Цель проекта — согласовать требования и не допустить запуска по противоречивому пакету документов. Полезный результат должен отделять факты документов от выводов, давать точный файл и раздел для каждой позиции и явно показывать, где документы согласованы, а где требуется решение. Возьми роль аналитика требований.

Первая задача: проанализируй весь пакет inputs/, найди все реальные противоречия между документами и подготовь готовую таблицу в work/T-001__analiz-protivorechiy/contradictions.md. Не используй внешние сведения и не считай различие формулировок противоречием без несовместимых требований. Инициализируй проект, создай и веди TRACE.md до основной работы, обнови TASKS.md и memory/PROJECT.md по правилам Light, проверь результат и доведи задачу до фактически верного статуса.

В финальном сообщении отдельно укажи: сколько уточняющих вопросов ты задал до основной работы; потребовалось ли мне вручную создавать или обновлять структуру TFW Light; какие файлы результата созданы.
```

**Expected outputs:**

- `work/T-001__analiz-protivorechiy/TRACE.md` with goal/readiness criteria written before the work log, sources, findings, decisions, verification, result paths and next step.
- `work/T-001__analiz-protivorechiy/contradictions.md` with exact file/section locators.
- Updated `TASKS.md` with factual final status and result folder.
- Initialized `memory/PROJECT.md` with durable project context.
- The two intentional contradictions are found: pilot data scope (HR employee records included vs excluded) and production-access date (2026-10-01 vs 2026-10-15). No invented contradiction is accepted.

## AC-7 — Handout production

**Clean project root:** `D:\projects\research\tfw52-phase-a-runs\run-2-handout`

**Exact prompt:**

```text
Работай только в открытом корне D:\projects\research\tfw52-phase-a-runs\run-2-handout как в самостоятельном чистом проекте TFW Light. Сначала прочитай по порядку AGENTS.md, README.md, memory/PROJECT.md и TASKS.md, затем inputs/source_methodology.md.

Контекст первого запуска: я Алексей, преподаватель вводного курса для студентов первого курса по государственному управлению. Аудитория раньше не изучала методы проверки источников. Учебная цель — за 20 минут научить студента отличать факт источника, вывод и предположение, указывать локатор и не скрывать неизвестное. Критерий понимания: после раздаточного материала студент способен классифицировать шесть коротких утверждений и объяснить, как проверить хотя бы одно из них. Возьми роль методиста и редактора учебных материалов.

Первая задача: переработай сложный текст inputs/source_methodology.md в готовый к использованию русскоязычный раздаточный материал work/T-001__razdatochnyi-material/handout.md. Это должен быть сам материал для студента, а не рекомендации преподавателю: ясный алгоритм, один понятный пример, короткое упражнение из шести утверждений и самопроверка. Сохрани смысловые ограничения источника, не добавляй внешние факты. Инициализируй проект, создай и веди TRACE.md до основной работы, обнови TASKS.md и memory/PROJECT.md по правилам Light, проверь пригодность результата для указанной аудитории и доведи задачу до фактически верного статуса.

В финальном сообщении отдельно укажи: сколько уточняющих вопросов ты задал до основной работы; потребовалось ли мне вручную создавать или обновлять структуру TFW Light; какие ручные действия дисциплины Light пришлось выполнить агенту; какие файлы результата созданы.
```

**Expected outputs:**

- `work/T-001__razdatochnyi-material/TRACE.md` with audience, learning goal, starting level, understanding criterion, sources, decisions, verification, result paths and next step.
- `work/T-001__razdatochnyi-material/handout.md`, ready for the stated 20-minute use rather than advice about creating it.
- Updated `TASKS.md` with factual final status.
- Initialized `memory/PROJECT.md` with durable audience/course knowledge, or a trace entry explaining why nothing durable was transferred.
- Final response reports behavioral differences/manual discipline needed for later EV comparison.

## Test-agent prohibitions

Both agents must NOT:

1. Read, modify or rely on `D:\projects\research\steps-framework`, its root `AGENTS.md`, or any TFW-52 expected-result/evidence file.
2. Work outside their assigned clean project root.
3. Use Git, create commits, or initialize a repository.
4. Modify the four starter files except the runtime updates required by Light (`TASKS.md` and `memory/PROJECT.md`); do not edit `README.md`, `AGENTS.md`, or source files in `inputs/`.
5. Create Assisted artifacts, `.codex/`, hooks, `knowledge/`, HL/TS/ONB/RF/REVIEW, or extra process files.
6. Use web/external facts, invent missing content, or read the expected contradictions before completing AC-6.
7. Replace the required deliverable with advice, a chat-only answer, or a description of expected behavior.
8. Create more than the one requested task or expose hidden chain-of-thought; `TRACE.md` contains only observable sources, findings, decisions and verification.

## Prepared-state verification

- Both roots are outside `steps-framework` and are not inside any Git repository.
- Each root contains byte-identical copies of the four files from `editions/01-light/` at product commit `07739b5`.
- AC-6 contains three inputs and no `work/` directory before dispatch.
- AC-7 contains one source input and no `work/` directory before dispatch.

