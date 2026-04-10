# Challenge — Iteration 3: "What do we NOT expect?"
> Parent: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> Predecessors: [Gather](gather.md), [Extract](extract.md)
> Goal: Stress-test финалистов нейминга, визуализации, multi-iteration дизайна.

## C1: Empirical LLM naming test (Qwen3.5-27B, zero-context)

**Method:** Одна и та же беседа (клиент: 18% clients = 80% revenue, subscription model failed, PM frustrated, prefers markdown). Разные section names. Модель: Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled (local vLLM). Zero context — модель не знает TFW. Минимальный instruction: только название секции + 1 sentence.

### Сравнительная таблица результатов

| Section Name | Что модель записала | Thinking mode | Ловит preference (markdown)? | Ловит emotion (PM frustrated)? | Analysis depth |
|---|---|---|---|---|---|
| **Strategic Insights** | Pareto analysis + business model implications + process gap + preference. **ADDED: "revenue concentration risk", "non-negotiable customization", "decision continuity gaps"** | Analytical — разбирал каждый пункт на implications | ✅ Да, но как «lightweight documentation preference» | ✅ Да, «decision continuity gaps» | **Deepest** — добавил стратегические выводы которых не было в input |
| **Fact Candidates** | 4 пункта, дословно: Pareto, subscription failed, PM reports decisions lost, prefers markdown. **Без analysis. Lists directly.** | Reporting — «These are all factual statements. I should record them concise and factual without adding interpretation» | ✅ Как голый факт | ✅ Как голый факт (no interpretation) | **Shallowest** — чистый reporting без analysis |
| **Strategic Signals** | Revenue concentration risk + failed transition + decision tracking gap + documentation preference | Analytical but signal-detection framing — «This indicates a process/communication breakdown» | ✅ Как «tool/process misalignment» | ✅ Как «operational inefficiency and PM frustration» | **Medium-high** — close to Strategic Insights |
| **Key Learnings** | Revenue concentration risk + subscription model failure + process gap + tool preference | Reflective — «I need to convert these observations into concise bullet points that capture the essence of what was learned» | ✅ Как «documentation platform decisions» | ✅ Как «knowledge retention problem causing PM frustration» | **Medium** — factual with mild interpretation |
| **Domain Signals** | Revenue concentration + failed subscription model + agile methodology gaps + documentation stack | Mixed — analytical + reporting | ✅ Как «current documentation stack» | ✅ Как «knowledge management or documentation process issue» | **Medium** — more factual than Strategic Insights |

### Key empirical findings

1. **«Strategic Insights» triggered the deepest analytical mode.** Модель не просто записала факты — она ДОБАВИЛА выводы: «revenue concentration risk», «non-negotiable customization», «decision continuity gaps». Ни одно другое название не дало такой глубины.

2. **«Fact Candidates» triggered pure reporting mode.** Модель БУКВАЛЬНО сказала в thinking: «I should record them concise and factual **without adding interpretation**.» Это EXACTLY the behavior we want for §6. Название работает как промпт.

3. **«Strategic Signals» ≈ «Strategic Insights» minus depth.** Близко по фреймингу, но «Signals» дал чуть менее глубокий анализ.

4. **«Key Learnings» = retrospective mode.** Средняя глубина, хорошее подведение итогов, но weak on forward-looking.

5. **«Domain Signals» split attention** — модель пыталась и анализировать и репортить, получилось среднее.

### D28 empirical verdict

| Name | Target behavior | Actual behavior | Match? |
|------|----------------|-----------------|--------|
| Strategic Insights | Synthesis + implications | ✅ Deep synthesis | **PERFECT** |
| Fact Candidates | Raw reporting | ✅ Pure facts, no interpretation | **PERFECT** |
| Strategic Signals | Strategic detection | ⚠️ Close to Insights but shallower | Good |
| Key Learnings | Lessons extracted | ✅ Retrospective capture | Good |
| Domain Signals | Domain-specific patterns | ⚠️ Split between analysis and reporting | Fair |

**VERDICT:** Названия «Strategic Insights» и «Fact Candidates» = уже правильные. Они запускают EXACTLY нужный cognitive mode. Менять их = regression.

## C2: Visualization section naming — empirical test

**Method:** Одна и та же беседа (school management system). Два section names: «Diagrams» vs «Visual Map».

### Результаты

| Section Name | Что модель нарисовала | Подход |
|---|---|---|
| **Diagrams** | 3 отдельных технических диаграммы: enrollment timeline, grade export pipeline, server room architecture. **Чёткие, структурированные, engineering-grade** | Модель разделила контекст на компоненты и дала each one свою диаграмму. Technical, systemic |
| **Visual Map** | 3 диаграммы: enrollment seasonal cycle (с peak triggers), grade export pipeline (с проблемным местом), relationship diagram. **Более narrative, с пояснениями внутри** | Модель добавила аннотации («Peak Triggers», «Issue»). Более explanatory, менее technical |

### Analysis

- **«Diagrams»** = инженерный подход. Чистые диаграммы, минимум текста внутри
- **«Visual Map»** = навигационный подход. Карта с пояснениями, контекстом, аннотациями

Для HL (vision level): «Visual Map» лучше — vision нужна карта с пояснениями.
Для RF (result level): «Diagrams» лучше — result нужны чёткие технические схемы.

Но мы ищем ОДНО название...

**Counter-argument к «одному названию»:** Может HL §3.1 уже имеет «Result Visualization» — и это ДОСТАТОЧНО? А для RF/RES нужно другое?

Нет — user explicitly: «одна общая глава с одним четким названием». Значит umbrella.

**Compromise position:** «Diagrams» (umbrella) + per-template instructions (control framing). Reasons:
1. Zero learning curve
2. Empirically produces good results even for non-code projects
3. Cross-domain understood
4. Instructions carry the real behavioral load, not the name
5. «Visual Map» adds learning curve without proportional gain

## C3: «Strategic Insights» edge cases stress-test

Из Extract E2, «Strategic Insights» не ideal для preferences и emotions. Empirical test says it DOES capture them, but framed through strategic lens.

| Edge case | «Strategic Insights» behaviour |
|-----------|-------------------------------|
| User: «Мне не нравится JSON, хочу YAML» | Records as tool preference insight ✅ |
| User: 😤 «Это меня бесит» | Records as stakeholder frustration signal ✅ — but framed as «operational issue», not emotion per se |
| User: «Мой инвестор сказал что XYZ» | Records perfectly ✅ — stakeholder intelligence |
| User: «В Казахстане малому бизнесу сложно с бухгалтерией» | Records as domain context ✅ |
| User: «Я хочу чтобы продукт был для предпринимателей, не программистов» | Records as strategic vision ✅ |

All 5 edge cases captured. The word «Strategic» doesn't BLOCK non-strategic items — it ELEVATES everything to strategic framing. Preferences become «tool strategy». Emotions become «stakeholder signals». This is a FEATURE, not a bug.

**Instructions needed (addition to template):**
```markdown
> **What counts as strategic:** Business facts, domain knowledge, stakeholder priorities,
> emotional reactions, process preferences, forward-looking signals, corrections to direction.
> If in doubt: "Would the next agent decide differently knowing this?" → record it.
```

## C4: Multi-iteration design — failure scenarios

| # | Failure scenario | Design handles it? |
|---|-----------------|-------------------|
| F1 | Researcher writes «SUFFICIENT» after iteration 1. Coordinator is a fresh agent, doesn't know about min_iterations | ✅ — iterations.yaml has min_iterations. Coordinator reads YAML before deciding |
| F2 | Coordinator forgets to update iterations.yaml | ⚠️ — risk of stale file. Mitigation: researcher exit protocol reminds. But not enforced programmatically |
| F3 | Researcher in iteration 2 doesn't read previous RES | ✅ — briefing template for iter 2+ has «Predecessor» field. Workflow Step 1: researcher MUST read all previous RES |
| F4 | 5 iterations, scope creep, never reaches TS | ✅ — max_iterations (soft cap) + coordinator judgment. Design says «beyond max = scope creep signal» |
| F5 | Stage files overwritten (single `research/` folder) — lose iteration 1 detail | ⚠️ — this is the open design question. Two options remain |

### On F5: folder structure decision

| Approach | Pro | Con |
|----------|-----|-----|
| **Single `research/`**, overwrite stage files | Clean. RES = trace. Stage files = scratch | Info loss. Can't re-read gather from iteration 1 |
| **`researchN/`** folders, accumulate | Zero info loss. Full trace | Disk grows. Multiple folders. Which stage files matter? |
| **Hybrid: `research/` + archive** | Active in research/, archive old to researchN/ before overwrite | Complexity. Extra step |

**I now think `researchN/` is correct.** Reasons from practice:
1. VLM-3 research3 briefing REFERENCED specific findings from research1 gather. Without the file, researcher would need to re-discover
2. TFW philosophy = «trace is the product». Deleting stage files = deleting traces
3. Disk cost is negligible vs information value
4. Each researcher reads ONLY their own folder + all RES files on task root. Previous research folders are reference, not mandatory

## C5: Naming philosophy coherence test

**Question from H_meta:** Do all names follow ONE philosophy?

| Section | Current name | Philosophy |
|---------|-------------|------------|
| §5 (RF) | Observations | «What the agent SEES technically» — observer mode |
| §6 (RF, RES, REVIEW) | Fact Candidates | «What we THINK might be true» — candidate pipeline |
| §7/§11 (HL, RF, RES) | Strategic Insights | «What the human KNOWS strategically» — synthesis mode |
| Viz section | Diagrams (proposed) | «SHOW the structure visually» — rendering mode |

**Does this cohere?** Let me check:
- **Observations** → passive, technical, internal → ✅ right level
- **Fact Candidates** → pipeline metaphor (candidate → verified) → ✅ right process
- **Strategic Insights** → active synthesis from human input → ✅ right cognitive mode
- **Diagrams** → concrete output type → ⚠️ different ontological category (it's a FORMAT, not a COGNITION)

**I notice:** First three names describe COGNITIVE MODES (observe, candidating, synthesize). Fourth describes OUTPUT FORMAT (diagram). This is an inconsistency.

Alternative: «Visual Thinking» — same cognitive ontology as others. But empirically worse at prompting (not tested).

**Assessment:** The inconsistency is acceptable. «Diagrams» lives in a different section purpose — it's about OUTPUT, not CAPTURE. §5/§6/§7 capture information. Diagrams section RENDERS information. Different function = different naming logic is OK.

## Checkpoint

| # | Finding | Status |
|---|---------|--------|
| C1 | **Empirically proven:** «Strategic Insights» = deepest analytical mode. «Fact Candidates» = cleanest reporting mode. Both ALREADY optimal | **CONFIRMED: no rename needed** |
| C2 | **«Diagrams»** > «Visual Map» for universal use. Per-template instructions carry framing load | Recommend «Diagrams» |
| C3 | «Strategic Insights» handles ALL edge cases including preferences and emotions (elevates them to strategic framing). Add instruction block for clarity | Keep + extend instructions |
| C4 | Multi-iteration design handles 4/5 failure scenarios. F5 (folder structure) → `researchN/` is correct per TFW trace philosophy | Design solid |
| C5 | Naming philosophy is coherent for capture sections (cognitive modes). Viz section (output format) = different category, acceptable | Philosophy holds |

**Sufficiency:**
- [x] External source used? (Empirical LLM testing on local model)
- [x] Briefing gap closed? (All 3 topics challenged + edge-case tested)

**Deep mode criteria:**
- [x] Hypothesis tested? H5c (REFUTED — original names are optimal), H6c (Diagrams wins), H7c (design validated through failure scenarios), H_meta (philosophy coherent)
- [x] Counter-evidence sought? Tested 5 alternative names empirically. Tested 5 edge cases for SI. Tested 5 failure scenarios for multi-iteration
- [x] Metacognitive check: SURPRISED. Пришёл менять названия — уходу с вердиктом «не менять». Оригинальные названия эмпирически лучше всех предложенных. RES1 D2 и RES2 D10 оба были regression.

Stage complete: YES
→ Proceed to Synthesis (RES)
