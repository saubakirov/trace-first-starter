# TS — TFW_20260922-123250_CMTR / Phase A: Core Framework Integration & Coordination Guidance

> **Current filename**: `TS__phase-a__core_framework_integration.md`
> **Date**: 2026-09-22
> **Author**: Antigravity Coordinator
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW_20260922-123250_CMTR](../HL-TFW_20260922-123250_CMTR.md)
> **Recommended execution profile**: Standard (Balanced tier, thinking: Medium) — Интеграция готовых выверенных диффов из ресерча в ядро TFW, верификация тестами.

---

## 1. Objective

Интегрировать в ядро фреймворка Trace-First Workflow (`.tfw/workflows/plan.md`, `.tfw/conventions.md §7`, `.tfw/templates/HL.md`, `.tfw/templates/TS.md`) правило 3 уровней когнитивной сложности (Procedural, Standard, Critical), протокол обязательной граундед-инспекции платформенных инструментов (`agy models`, `codex --help`, `claude --help`) перед выдачей рекомендаций, правила дуального запуска (UI-подсказка для нового окна vs автономный API-запуск) и механизм самокалибровки координатора без создания избыточных файлов конфигурации.

---

## 2. Scope

### In Scope

- Модификация `.tfw/workflows/plan.md`: расширение Шага 5 («Coordination Selection Gate») компактным блоком оценки когнитивного профиля фаз, обязательной граундед-инспекцией доступных моделей и правилом самокалибровки координатора.
- Модификация `.tfw/conventions.md §7`: добавление подраздела `### Cognitive Budgeting and Platform-Adaptive Launching` с правилом 3 уровней, дуальным запуском, протоколом граундед-инспекции и самокалибровкой.
- Модификация `.tfw/templates/HL.md`: добавление столбца профиля исполнения в таблицу §4.1 («Coordination Selection»).
- Модификация `.tfw/templates/TS.md`: добавление канонической строки `Recommended execution profile` в шапку метаданных спецификации.
- Полная верификация автоматических тестов репозитория (`pytest tools/tests/ docs/scripts/ -q`).

### Out of Scope

- Обновление адаптеров платформ (`.tfw/adapters/antigravity/`, `.tfw/adapters/codex/`, `.tfw/adapters/claude-code/`) и правила `.agents/rules/tfw.md` (вынесено в Фазу B).
- Актуализация базы знаний `KNOWLEDGE.md`, `README.md` и `CHANGELOG.md` (вынесено в Фазу B).
- Создание отдельных файлов конфигурации моделей (`models.yaml`) или программных калькуляторов токенов (запрещено принципами F43, F45).

---

## 3. Principles Check

| # | HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Полноценные чат-агенты, а не субагенты | AC-1, AC-2 | Тексты конвенций и воркфлоу явно оперируют созданием новых сессий/окон, запрещая подмену субагентами. |
| P2 | Естественное расширение, а не раздувание сущностей (F43, F45) | AC-1, AC-2, AC-3, AC-4 | Все изменения вносятся точечными вставками в существующие файлы; 0 новых файлов создано. |
| P3 | Фреймворк предлагает — человек выбирает (F25) | AC-1, AC-2 | В ручном режиме координатор выдает 2-строчную подсказку в UI, оставляя финальный выбор за человеком. |
| P4 | Платформенная честность (D59) | AC-1, AC-2 | Разделение между GUI-сессиями (подсказка человеку) и средами с task API (Codex native tasks). |
| P5 | Бескомпромиссность на защите ценностей (F3, D64) | AC-1, AC-2 | Запрет занижения thinking на критических этапах (Inception, Review, Deep Research). |
| P6 | Прозрачность любого выбора | AC-1, AC-2, AC-4 | Каждая рекомендация модели и thinking обязательно сопровождается 1-строчным обоснованием. |
| P7 | Граундед-инспекция вместо статической памяти (A1) | AC-1, AC-2 | Прямой запрет называть модели по памяти; обязательное требование инспекции нативными инструментами среды. |

---

## 4. Affected Files and Value-Bearing Accounting

Все 4 файла классифицированы как `VALUE` (каноническое ядро фреймворка, конвенции и шаблоны):

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `.tfw/workflows/plan.md` | MODIFY | `VALUE` | Расширение Шага 5 правилом 3 уровней, граундед-инспекцией и самокалибровкой. |
| `.tfw/conventions.md` | MODIFY | `VALUE` | Добавление подраздела Cognitive Budgeting & Platform-Adaptive Launching в §7. |
| `.tfw/templates/HL.md` | MODIFY | `VALUE` | Добавление столбца Execution profile в таблицу §4.1 Coordination Selection. |
| `.tfw/templates/TS.md` | MODIFY | `VALUE` | Добавление строки Recommended execution profile в шапку метаданных. |

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | `.tfw/workflows/plan.md`, `.tfw/conventions.md`, `.tfw/templates/HL.md`, `.tfw/templates/TS.md` |
| Baseline / selector source | `9cb04a4cc3c1fc2d3f3fef9e395798d60667ef47`; this TS at approval commit |
| Candidate rule | First tested Executor commit with required VALUE+ASSURANCE, before EV/RF/REVIEW/final transition |
| Logical VALUE files | 4 files |
| Touched text LOC | ~50–80 LOC |
| Triggers / disposition | Ни один порог декомпозиции (50 файлов / 5000 LOC) не превышен. |
| Multiplier / authority | owner-direct: saubakirov |
| Approval epoch / failure | commit approval; tests pass 100% |

```powershell
git diff --name-status -z 9cb04a4cc3c1fc2d3f3fef9e395798d60667ef47 HEAD -- .tfw/workflows/plan.md .tfw/conventions.md .tfw/templates/HL.md .tfw/templates/TS.md
git diff --numstat -z 9cb04a4cc3c1fc2d3f3fef9e395798d60667ef47 HEAD -- .tfw/workflows/plan.md .tfw/conventions.md .tfw/templates/HL.md .tfw/templates/TS.md
```

---

## 5. Acceptance Criteria

### AC-1: Расширение `.tfw/workflows/plan.md` (Шаг 5: Coordination Selection Gate)
Шаг 5 процесса `plan.md` дополнен абзацем, предписывающим:
1. Классификацию фаз по правилу 3 уровней сложности: Procedural (Fast tier, thinking Low/Off), Standard (Balanced tier, thinking Medium), Critical (Heavy Reasoning tier, thinking High/Max).
2. Обязательную нативную граундед-инспекцию доступных моделей платформы (`agy models`, `codex --help`, `claude --help`) перед выдачей рекомендации человеку; запрет называть модели по статической памяти.
3. Формирование 2-строчной подсказки для селектора UI нового окна с 1-строчным обоснованием (в GUI-средах) либо прямой передачей параметров `model` и `reasoning_effort` (в средах с task API).
4. Правило самокалибровки координатора (Up-Shift при нехватке когнитивной мощности на архитектуре; Down-Shift на тривиальной рутине).

- [ ] Абзац органично интегрирован в Шаг 5 `.tfw/workflows/plan.md` без дублирования существующих правил.

Gate: `Select-String -Path .tfw/workflows/plan.md -Pattern "3-tier rule|grounded"`
Evidence: Текстовый дифф и соответствие формулировке E1/A1.

### AC-2: Расширение `.tfw/conventions.md §7` (Coordination) [depends: AC-1]
В раздел `## 7) Coordination` добавлен компактный подраздел `### Cognitive Budgeting and Platform-Adaptive Launching`, содержащий:
1. Описание 3 уровней когнитивной нагрузки и их характеристик (включая защиту от overthinking на рутине и защиту состязательности на ревью).
2. Протокол дуального запуска сессий (GUI UI-подсказка человеку vs автономный запуск через task API).
3. Принцип граундед-инспекции (запрет галлюцинирования моделями по памяти).
4. Правила самокалибровки координатора (Up-Shift / Down-Shift).

- [ ] Подраздел добавлен в `.tfw/conventions.md §7` перед подразделом `### Provider-native evidence`.

Gate: `Select-String -Path .tfw/conventions.md -Pattern "Cognitive Budgeting and Platform-Adaptive Launching"`
Evidence: Текстовый дифф и валидация структуры Markdown.

### AC-3: Расширение шаблона `.tfw/templates/HL.md` [depends: AC-2]
В шаблон `HL.md` в таблицу подраздела `### 4.1 Coordination Selection 🔒 FROZEN` добавлен столбец `Execution profile` для фиксации класса сложности и профиля модели по фазам.

- [ ] Таблица §4.1 в `.tfw/templates/HL.md` содержит столбец `Execution profile` с примером заполнения.

Gate: `Select-String -Path .tfw/templates/HL.md -Pattern "Execution profile"`
Evidence: Проверка целостности таблицы шаблона.

### AC-4: Расширение шаблона `.tfw/templates/TS.md` [depends: AC-3]
В шапку метаданных шаблона `TS.md` добавлена каноническая строка:
`> **Recommended execution profile**: {Procedural | Standard | Critical} ({Model tier}, thinking: {level}) — {1-sentence rationale}`.

- [ ] Строка метаданных присутствует в шаблоне `TS.md`.

Gate: `Select-String -Path .tfw/templates/TS.md -Pattern "Recommended execution profile"`
Evidence: Проверка целостности метаданных шаблона.

### AC-5: Автоматическая верификация тестов [depends: AC-1, AC-2, AC-3, AC-4]
Все тесты репозитория (`pytest`) выполняются успешно, подтверждая обратную совместимость парсеров документации и отсутствие регрессий.

- [ ] Команда `python -m pytest tools/tests/ docs/scripts/ -q` возвращает `14 passed`.

Gate: `python -m pytest tools/tests/ docs/scripts/ -q`
Evidence: Вывод команды pytest (14 passed).

---

## 6. Technical Guidance

При реализации изменений исполнитель должен использовать проверенные тексты расширений из `research/iter2/3_extract.md` с интеграцией поправки A1:

### 1. Текст для `.tfw/workflows/plan.md` (Шаг 5):
```markdown
Classify the cognitive profile for task phases and roles using the 3-tier rule: Procedural (routine docs, formatting, sync, lint; Fast tier, thinking: Low/Off), Standard (implementation by TS/AC; Balanced tier, thinking: Medium), or Critical (inception, review, deep research; Heavy Reasoning tier, thinking: High/Max). Grounded inspection is mandatory: inspect the platform's exposed models (e.g. agy models, codex --help, claude --help) before recommending; never guess model names from memory. For owner-assisted GUI environments (Antigravity, Claude Desktop), formulate a 2-line launch prompt for the human UI selector with a 1-sentence rationale; for native task environments (Codex native tasks), pass model and reasoning effort parameters directly. Self-calibration: if the coordinator's current session lacks cognitive depth for a multi-phase or core architecture task, advise an upshift; if idle on trivial routine, advise a downshift.
```

### 2. Текст для `.tfw/conventions.md §7`:
```markdown
### Cognitive Budgeting and Platform-Adaptive Launching

TFW optimizes cognitive expenditure per launch across three discrete tiers:
1. **Procedural:** Routine documentation, sync, formatting, version updates, linting. Fast tier (Flash, Haiku, 4o-mini), thinking Low/Off. Prevents overthinking and reduces latency by up to 80%.
2. **Standard:** Implementation by approved TS and AC, modular coding, focused iteration-1 research. Balanced tier (Sonnet, Pro, o3-mini), thinking Medium.
3. **Critical / Adversarial:** Task inception, architectural design, independent review, adversarial research. Heavy Reasoning tier (Sonnet High Thinking, o3 High, Gemini Pro High). Downgrading power on this tier is strictly prohibited.

**Grounded Inspection:**
The coordinator never recommends models from pre-trained memory. It inspects exposed platform tools (e.g. `agy models`, `codex --help`, `claude --help`) before advising, or operates purely by abstract tiers (Fast / Balanced / Heavy) when the platform exposes no inspection mechanism.

**Dual Launch Protocol:**
- *Owner-Assisted (GUI):* In Antigravity, Claude Desktop, and GUI sessions, the coordinator outputs a 2-line selector guidance for the human opening a new chat window. Cross-session messaging via queues delivers to storage; activation of sleeping windows remains an owner action.
- *Autonomous (Native API):* Under an approved delegation mandate on platforms with native task creation (Codex), the coordinator passes `model` and `reasoning_effort` directly to the creation API and logs the dispatch.

**Self-Calibration:**
A coordinator evaluating complex multi-component architecture on a Fast tier session issues a single non-blocking recommendation to upshift the active window to Pro/High; conversely, on trivial local edits it suggests a downshift to conserve quota.
```

### 3. Текст для `.tfw/templates/HL.md` (§4.1):
```markdown
| Activation source | Accountable owner | Delegated Coordinator unit | Mandate scope / role reach | Dialogue | Reservations / controls | Amendment authority | Immutable epoch | Execution profile |
|---|---|---|---|---|---|---|---|---|
| owner-direct / delegated | {human owner handle} | {native address or `N/A — owner-direct`} | {bounded task/phases and roles} | tfw-gates-only / iterative | {owner-reserved decisions and controls} | {exact bounded grant or `none`} | {full commit/object ref} | {Procedural/Standard/Critical} ({Model class}, thinking: {level}) |
```

### 4. Текст для `.tfw/templates/TS.md` (Шапка):
```markdown
> **Recommended execution profile**: {Procedural | Standard | Critical} ({Model tier}, thinking: {level}) — {1-sentence rationale}
```

---

## 7. Definition of Failure

- ❌ 1. Нарушение обратной совместимости или падение тестов `pytest tools/tests/ docs/scripts/ -q`.
- ❌ 2. Создание отдельных конфигурационных файлов моделей (`models.yaml`), нарушающих принцип Сент-Экзюпери.
- ❌ 3. Упоминание внутрисессионных субагентов вместо полноценных независимых сессий/чат-агентов TFW.
- ❌ 4. Разрешение координатору рекомендовать коммерческие названия моделей по статической памяти без граундед-инспекции окружения.

---

## 8. Evidence Plan

- Обязательный артефакт свидетельств: `workspace/2026/TFW_20260922-123250_CMTR/phase-a/evidence/EV__phase-a__core_framework_integration.md`.
- Содержимое: Environment Header, таблица статусов AC-1..AC-5 (VERIFIED / DEFERRED / BLOCKED / N/A), вывод `pytest`, дифф проверенных файлов.

---

## 9. Cross-Phase Modifications

- Фаза A обновляет каноническое ядро фреймворка, конвенции и шаблоны.
- Фаза B использует заложенные контракты Фазы A для адаптации специфичных файлов вендоров (`.tfw/adapters/`, `.agents/rules/tfw.md`, документация).

---

*TS — TFW_20260922-123250_CMTR / Phase A: Core Framework Integration & Coordination Guidance | 2026-09-22*
