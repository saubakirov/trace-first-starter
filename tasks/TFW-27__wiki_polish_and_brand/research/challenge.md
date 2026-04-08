# Challenge — "What do we NOT expect?"
> Parent: [HL-TFW-27](../HL-TFW-27__wiki_polish_and_brand.md)
> Goal: Wikipedia-style link resolution in compiled docs.

## Findings

### C1: P{N} — двойная семантика, решение опасно

**Проблема:** `P{N}` используется в двух разных контекстах:

1. **KNOWLEDGE.md §0** — глобальные принципы (`P7 = Self-review is not review`). 8 штук: P1, P2, P3, P5, P7, P8, P9, P10.

2. **HL §7 каждой задачи** — локальные принципы задачи (`P1 = handoff.md combines executor and reviewer` в HL-TFW-8). Нумерация начинается с P1 заново в КАЖДОМ HL.

Если резолвер видит `P1` в тексте — он НЕ МОЖЕТ знать, это глобальный P1 ("Traces over code") или локальный P1 из конкретного HL. Примеры из реального кода:

- `HL P1, P5` (в RF TFW-9) → P1 здесь = **локальный** принцип из HL-TFW-9, НЕ глобальный
- `HL §7 P5` → тоже локальный
- `D10/P10 compression` (в RF TFW-26) → P10 = глобальный принцип

**Whitelist не спасает:** P1 есть и в KNOWLEDGE.md §0, и в HL-TFW-8, и в HL-TFW-9 — все разные.

**Решение:** P{N} как автоматический резолвер — НЕ делаем. Вместо этого:
- HTML-якоря на строках таблицы KNOWLEDGE.md §0: `<a id="p1"></a>P1` → линкуемо как `/knowledge-index/#p1`
- Source-колонки таблицы (`TFW-5 HL §7`) → покрываются существующим резолвером bare task ID
- Если автор хочет ссылку на глобальный принцип — пишет полную ссылку руками

### C2: Bare task ID `TFW-18` — порядок выполнения

**Проблема:** Если bare `TFW-18` резолвер запускается ДО `RF TFW-18`, то текст `RF TFW-18` превращается в `RF [TFW-18](url)` → ломает artifact resolver.

**Решение:** Bare task ID resolver запускается ПОСЛЕДНИМ, после всех type-prefixed resolvers. Regex: `\bTFW-\d+\b` с negative lookbehind на `(HL|TS|RF|ONB|RES|REVIEW)[\s-]` и `(?<![)`.

Проверил: после artifact resolver `RF TFW-18` уже превращён в `[RF TFW-18](url)`. Guard `(?<![)` в bare resolver пропустит `TFW-18` внутри `[...]`. Работает.

### C3: HTML-якоря в таблицах MkDocs

MkDocs Material рендерит markdown-таблицы в HTML. Встроенный HTML в ячейках (`<a id="p7"></a>P7`) рендерится корректно — это стандартное поведение.

gen_docs.py добавляет якорь при обработке:
- KNOWLEDGE.md §0 → `| <a id="p7"></a>P7 |` → якорь для `/knowledge-index/#p7`
- KNOWLEDGE.md §1 → `| <a id="d24"></a>D24 |` → якорь для `/knowledge-index/#d24`
- TECH_DEBT.md → `| <a id="td-72"></a>TD-72 |` → якорь для `/reference/tech-debt/#td-72`
- knowledge/*.md → `| <a id="f4"></a>F4 |` → якорь для `/knowledge/process/#f4`

~30 LOC. Один regex на таблицу + замена первого столбца.

### C4: File paths без бэктиков — false positive risk ВЫСОКИЙ

**Проблема:** `.tfw/conventions.md` без бэктиков в running text — regex `\.tfw/[^\s]+\.md` может сматчить:
- URL-фрагменты
- Уже ready markdown-ссылки `[text](.tfw/conventions.md)` (target часть)
- Код в fenced blocks

**Решение:** Оставить file paths ТОЛЬКО в бэктиках. Текущий backtick resolver работает. Расширять на plain text — false positives перевешивают пользу. Если путь важен — автору достаточно обернуть в бэктики.

### C5: Markdown link rewriting (404 fix)

**Проблема:** `[glossary.md](glossary.md)` внутри `.tfw/conventions.md` → после компиляции conventions → `reference/conventions/`, glossary → `reference/glossary/`. Relative link `glossary.md` → 404.

**Решение:** gen_docs.py при обработке файла знает source path. Для каждого `[text](target)`:
1. target = resolve relative to source dir → `.tfw/glossary.md`
2. lookup in Source Manifest → `reference/glossary.md`
3. rewrite: `[glossary.md](/reference/glossary/)`

**Edge cases:**
- Anchors: `[text](glossary.md#section)` → `/reference/glossary/#section` ✅ _md_to_url_with_anchor уже есть
- External URLs: `[text](https://...)` → skip ✅
- Non-mapped targets: `[text](PROJECT_CONFIG.yaml)` → no mapping, leave as-is ✅
- Relative `../` links в tasks: `[HL-TFW-26](../HL-TFW-26__*.md)` → folder structure preserved, relative link works → skip ✅

~50 LOC. Детерминистический, низкий false positive risk.

## Итог

| Фича | Verdict |
|------|---------|
| P{N} auto-resolver | ❌ **Отказ** — двойная семантика, false positives неизбежны |
| P{N} HTML-якоря | ✅ Делаем — якоря на таблицах для deep linking |
| Bare task ID `TFW-18` | ✅ Делаем — последним в цепочке |
| File paths без бэктиков | ❌ **Отказ** — false positives, бэктики достаточно |
| Markdown link rewriting | ✅ Делаем — детерминистический fix |
| HTML-якоря на D{N}, TD-{N}, F{N} | ✅ Делаем — параллельно с P{N} |

**Финальный скоуп: 3 новых фичи + 1 enhancement (якоря)**

| Фича | LOC |
|------|-----|
| Bare task ID resolver | ~15 |
| Markdown link rewriter | ~50 |
| HTML-якоря на таблицах (P, D, TD, F) | ~30 |
| literate-nav integration | ~25 |
| **Итого gen_docs.py** | **~120** |

Stage complete: YES
