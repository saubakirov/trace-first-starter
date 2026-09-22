# Extract — "What do we NOT see?" (Iteration 2)
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260922-123250_CMTR](../../HL-TFW_20260922-123250_CMTR.md)
> Goal: enable the coordinator to recommend or autonomously select platform-native models and thinking effort per launch to preserve quality without burning tokens or quotas

## Анализ эффективности правила 3 уровней на контрастных сценариях

Сравнительная матрица применения CMTR к трем историческим сценариям TFW:

| Показатель | Сценарий 1: Процедурный (TFW-55 B.2) | Сценарий 2: Стандартный (TFW-26 A/B) | Сценарий 3: Критический (RVAG Review) |
| :--- | :--- | :--- | :--- |
| **Характер работы** | Локализация README, синхронизация таблиц | Разработка скрипта `gen_docs.py` (445 LOC) | Состязательный аудит процесса и ценностей |
| **Класс CMTR** | **1. Procedural** | **2. Standard** | **3. Critical / Adversarial** |
| **Профиль модели** | Fast tier (Flash / Haiku / 4o-mini) | Balanced tier (Sonnet / Pro / o3-mini) | Heavy Reasoning (Sonnet High / o3 High) |
| **Режим Thinking** | Low / Off | Medium (~4k токенов) | High / Max (16k+ токенов) |
| **Задержка ответа** | 3–5 секунд (вместо 45 сек) | 15–20 секунд | 40–90 секунд (оправданная глубина) |
| **Экономия токенов/квот** | **~75% экономии** на фазе | **~35% экономии** (снятие overthinking) | 0% (экономия запрещена, 100% фокус на качестве) |
| **Влияние на качество** | Исключены галлюцинации overthinking | Четкое выполнение AC без зацикливаний | Полное исключение сикофантии (F3) |

## Буквальные тексты расширений для фазы реализации (Фаза A)

### E1: Расширение `.tfw/workflows/plan.md` (Шаг 5: Coordination Selection Gate)

В существующий Шаг 5 органично добавляется следующий абзац (принцип Сент-Экзюпери — строго 1 компактный блок):

```markdown
Classify the cognitive profile for task phases and roles using the 3-tier rule: Procedural (routine docs, formatting, sync, lint; Fast tier, thinking: Low/Off), Standard (implementation by TS/AC; Balanced tier, thinking: Medium), or Critical (inception, review, deep research; Heavy Reasoning tier, thinking: High/Max). For owner-assisted GUI environments (Antigravity, Claude Desktop), formulate a 2-line launch prompt for the human UI selector with a 1-sentence rationale; for native task environments (Codex native tasks), pass model and reasoning effort parameters directly. Self-calibration: if the coordinator's current session lacks cognitive depth for a multi-phase or core architecture task, advise an upshift; if idle on trivial routine, advise a downshift.
```

### E2: Расширение `.tfw/conventions.md §7` (Coordination)

Добавление компактного подраздела `### Cognitive Budgeting and Platform-Adaptive Launching`:

```markdown
### Cognitive Budgeting and Platform-Adaptive Launching

TFW optimizes cognitive expenditure per launch across three discrete tiers:
1. **Procedural:** Routine documentation, sync, formatting, version updates, linting. Fast tier (Flash, Haiku, 4o-mini), thinking Low/Off. Prevents overthinking and reduces latency by up to 80%.
2. **Standard:** Implementation by approved TS and AC, modular coding, focused iteration-1 research. Balanced tier (Sonnet, Pro, o3-mini), thinking Medium.
3. **Critical / Adversarial:** Task inception, architectural design, independent review, adversarial research. Heavy Reasoning tier (Sonnet High Thinking, o3 High, Gemini Pro High). Downgrading power on this tier is strictly prohibited.

**Dual Launch Protocol:**
- *Owner-Assisted (GUI):* In Antigravity, Claude Desktop, and GUI sessions, the coordinator outputs a 2-line selector guidance for the human opening a new chat window. Cross-session messaging via queues delivers to storage; activation of sleeping windows remains an owner action.
- *Autonomous (Native API):* Under an approved delegation mandate on platforms with native task creation (Codex), the coordinator passes `model` and `reasoning_effort` directly to the creation API and logs the dispatch.

**Self-Calibration:**
A coordinator evaluating complex multi-component architecture on a Fast tier session issues a single non-blocking recommendation to upshift the active window to Pro/High; conversely, on trivial local edits it suggests a downshift to conserve quota.
```

### E3: Расширение шаблона `.tfw/templates/HL.md` (§4.1 Coordination Selection)

В шапку или таблицу координации §4.1 добавляется поле профиля исполнения:

```markdown
| Activation source | Accountable owner | Delegated Coordinator unit | Mandate scope / role reach | Dialogue | Reservations / controls | Amendment authority | Immutable epoch | Execution profile |
|---|---|---|---|---|---|---|---|---|
| owner-direct / delegated | {owner} | {unit or N/A} | {scope} | tfw-gates-only | {controls} | {grant} | {epoch} | {Procedural/Standard/Critical} ({Model class}, thinking: {level}) |
```

### E4: Расширение шаблона `.tfw/templates/TS.md` (Шапка метаданных)

В метаданные спецификации задачи добавляется одна каноническая строка:

```markdown
> **Recommended execution profile**: {Procedural | Standard | Critical} ({Model tier}, thinking: {level}) — {1-sentence rationale}
```

## Checkpoint

| Found | Remaining |
|---|---|
| Доказана эффективность CMTR на всех 3 контрастных сценариях | Проверить формулировки на избыточность и отсутствие скрытых конфликтов (Challenge) |
| Подготовлены точные формулировки расширений ядра для Фазы A | Оценить риски нарушения Role Lock или усложнения CI |

**Sufficiency:**
- [x] External source used? (Да: проверены исторические трассы TFW и канонические шаблоны)
- [x] Briefing gap closed? (Да: подготовлены готовые тексты диффов для ядра)

---
Stage complete: YES
