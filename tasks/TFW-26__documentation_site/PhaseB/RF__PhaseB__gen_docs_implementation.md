# RF — TFW-26 / Phase B: gen_docs.py Implementation

> **Date**: 2026-04-05
> **Author**: Executor
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-26](../HL-TFW-26__documentation_site.md)
> **TS**: [TS Phase B](TS__PhaseB__gen_docs_implementation.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|------------|
| `docs/scripts/test_gen_docs.py` | 29 unit tests: extract_title (6), add_frontmatter (3), _glob_base (4), resolve_references (12), validate_sources (3), _read_task_prefix (2) |
| `docs/scripts/test_integration.py` | 13 integration tests: static pages, knowledge index, task pages (10+), knowledge topics (3+), workflows (5+), templates (5+), frontmatter, D{N} anchor resolution, artifact refs in knowledge topics, TD-{N} links, index override, section index pages, directory URL validation |

### Modified Files
| File | Changes |
|------|---------|
| `docs/scripts/gen_docs.py` | Full implementation: source manifest, frontmatter injection, 6 reference resolvers (artifact, phase, HL-dash, TD, D, backtick-path), structured tasks index with numeric sorting, section index generation. 146→445 LOC |
| `docs/mkdocs.yml` | Nav restructured: Architecture → Knowledge (with sub-topics), explicit knowledge topic listing |
| `docs/requirements.txt` | Added `pyyaml>=6.0` and `pytest>=7.0` (3→5 lines) |
| `.gitignore` | Added `__pycache__/`, `.pytest_cache/`, `*.pyc` |

## 2. Key Decisions

1. **Directory URLs for all resolved links**: MkDocs with `use_directory_urls=true` serves `foo/bar.md` as `foo/bar/`. Absolute links with `.md` extension → 404. All resolved links now use `/path/to/page/` format (no `.md`). Helper: `_md_to_url()`.

2. **Structured tasks index**: Flat alphabetical list replaced by grouped-by-task index with numeric sorting. Each task shows: HL link as heading, status from README.md task board, list of artifacts with readable names (`RF — PhaseB gen docs implementation`). Sorting by `int(re.search(r'\d+', folder_name))` → TFW-1, 2, 3... not TFW-1, 10, 11.

3. **Backtick-path resolver**: KNOWLEDGE.md uses abbreviated backtick paths (`` `tasks/TFW-2.../RF__TFW-2...md` ``). New resolver converts `...` to glob wildcards for abbreviated paths. Exact `.tfw/` paths mapped to output URLs via lookup table (`.tfw/conventions.md` → `/reference/conventions/`).

4. **Closure-based sub-resolvers**: `resolve_references()` uses inner functions that capture `root` from enclosing scope. No module-level state.

5. **Module-level `main()` guard**: `if hasattr(mkdocs_gen_files, "open")` prevents execution during test imports.

6. **Integration test: relative config path**: `--config-file docs/mkdocs.yml` (relative) works; absolute path causes MkDocs to misresolve `docs_dir: .` on Windows.

7. **Nav restructuring**: "Architecture" → "Knowledge" with explicit sub-items: "Architecture & Decisions" (KNOWLEDGE.md), Topics (convention, constraint, philosophy, process).

## 3. Acceptance Criteria

- [x] `mkdocs build --config-file docs/mkdocs.yml` exits 0 with no ERROR-level messages
- [x] All 9 static sources produce pages with YAML frontmatter
- [x] All 4 glob patterns produce pages (tasks/ — 24 task folders, knowledge/ — 4 topics, workflows — 5+, templates — 5+)
- [x] Reference resolver handles `RF TFW-18`, `HL-TFW-19`, `TD-{N}`, `D{N}` patterns
- [x] References already inside markdown links are NOT double-wrapped
- [x] Missing optional sources produce WARNING
- [x] Unresolvable references left as plain text with WARNING
- [x] `tfw.task_prefix` read from PROJECT_CONFIG.yaml
- [x] Unit tests pass: 29/29
- [x] Integration tests pass: 13/13
- [x] `resolve_references()` accepts `project_root` parameter for testability
- [x] Resolved links use directory URLs (no `.md` extension → no 404)
- [x] Tasks index grouped by task, sorted numerically, with HL links and statuses
- [x] Backtick-path references in KNOWLEDGE.md resolve to clickable links
- [x] Knowledge topics visible in sidebar navigation

### Deviations from TS

| # | TS Expectation | Actual | Justification |
|---|----------------|--------|---------------|
| 1 | `mkdocs build --strict` passes | Not tested | `--strict` treats MkDocs INFO "absolute link" messages as errors. Without absolute paths, cross-page links break. Tradeoff accepted |
| 2 | Unresolvable references marked with `⚠️` | Left as plain text | Adding `⚠️` alters content semantics. WARNING in build log sufficient |
| 3 | 8+ unit tests expected | 29 unit tests | More coverage |
| 4 | Scope: TS did not mention backtick-path resolver | Added backtick-path resolver | User testing revealed KNOWLEDGE.md uses backtick-path format exclusively. Without this, the most important index page had zero clickable links |
| 5 | Scope: TS did not mention section index generation | Added tasks index + section indexes | User testing: `/tasks/` 404, flat file dumps "не ощущение вики" |
| 6 | Scope: TS did not mention nav restructuring | Restructured nav | User feedback: "Knowledge и Knowledge index как-то странно" |

## 4. Verification

- **Unit tests**: `pytest docs/scripts/test_gen_docs.py -v` → 29 passed
- **Integration tests**: `pytest docs/scripts/test_integration.py -v` → 13 passed
- **Full suite**: `pytest docs/scripts/ -v` → 42 passed in 5.9s
- **MkDocs build**: `mkdocs build --config-file docs/mkdocs.yml` → exit 0, built in ~5s
- **File count**: 2 new + 4 modified = 6 total (within budget: max 14)
- **User testing**: Live `mkdocs serve` session with user navigating site, reporting bugs, verifying fixes in real-time

### User-tested pages
- `/tasks/` — grouped index, sorted numerically ✅
- `/knowledge-index/` — backtick paths clickable ✅
- `/knowledge/convention/` — artifact refs clickable, navigate to task pages ✅
- D{N} links → `/knowledge-index/#architecture-decisions` ✅ (was 404 with `.md`)
- TD-{N} links → `/reference/tech-debt/` ✅ (was 404 with `.md`)
- Sidebar: Knowledge → Architecture & Decisions + 4 topics ✅

## 5. Observations — Phase C Scope (out-of-scope, not modified)

> These observations define the scope for an additional "wiki polish" phase before GitHub release.

| # | Area | Problem | Proposed Fix |
|---|------|---------|-------------|
| 1 | **Nav terminology** | "Concepts > Philosophy" (`.tfw/README.md`) vs "Knowledge > Topics > Philosophy" (knowledge fact file) — confusing duplication | Rename or merge: Philosophy page = TFW thesis; Knowledge/Philosophy = empirical facts. Clarify in nav labels |
| 2 | **Tasks sidebar** | Tasks section is a single flat link in sidebar. Individual tasks not browsable via sidebar — must go to `/tasks/` index first | Generate literate-nav or use `mkdocs-awesome-pages-plugin` to build sidebar tree per task |
| 3 | **Knowledge topics hardcoded** | 4 topics hardcoded in `mkdocs.yml`. New topics require manual edit | Gen_docs.py should dynamically generate nav entries or use `mkdocs-literate-nav` |
| 4 | **Broken source links** | Pre-existing relative links in source artifacts: glossary → `README.md`, conventions → `init.md`, `.tfw/README.md` → `conventions.md`. These resolve to wrong location after compilation | Two options: (a) gen_docs.py rewrites relative links during compilation, (b) fix source files to use reference format |
| 5 | **Search discoverability** | Search works (Ctrl+K / search icon) but not obvious to first-time visitors | Add search hint in index.md or enable Material's integrated search bar |
| 6 | **MkDocs 2.0 risk** | mkdocs-material warns: MkDocs 2.0 will break all plugins. `mkdocs-gen-files` depends on MkDocs 1.x plugin system | Pin `mkdocs<2.0` in requirements.txt or migrate to `properdocs` (community fork) |
| 7 | **KNOWLEDGE.md backtick paths** | Many references still use abbreviated backtick format (`tasks/TFW-2.../RF__TFW-2...md`) instead of standard reference format (`RF TFW-2`) | Migrate KNOWLEDGE.md to reference format (TD-66). Reduces resolver complexity |
| 8 | **`--strict` mode** | `--strict` build fails due to absolute link INFO messages from MkDocs. These are correct links that work, but MkDocs flags them | Investigate `use_directory_urls: false` + relative links, or suppress specific MkDocs warnings |
| 9 | **Executor session fact capture** | Coordinator has §11 Strategic Session Insights in HL template + plan.md trigger. Executor has no equivalent — no explicit step to capture user quotes, corrections, emotional signals from live testing. This session produced 5 high-value insights (§7 below) that would have been lost without user's explicit request | Add §7 "Execution Session Insights" to RF template. Add trigger in handoff.md: "Before RF: scan chat for user corrections, emotional signals, architectural revelations." Mirror Coordinator's §11 pattern |

## 6. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | constraint | MkDocs 1.6 with `use_directory_urls=true`: absolute link paths must use directory format (`/path/to/page/`) not file format (`/path/to/page.md`). File-format absolute links → 404 | Executor, user testing session | ✅ high |
| 2 | constraint | MkDocs 1.6 on Windows: `--config-file` with absolute path causes `docs_dir: .` misresolution. Use relative path (`docs/mkdocs.yml`) | Executor, integration test debugging | ✅ high |
| 3 | philosophy | User expects "Wikipedia-like" feel: everything clickable, navigable, discoverable. Flat file dumps and non-linked references = process failure. «Нет ощущения вики движка вообще» | User, live testing session | ✅ high |
| 4 | risk | MkDocs 2.0 planned as backward-incompatible rewrite — no plugin support, no theme support, no migration. `mkdocs-gen-files` will break | MkDocs Material warning | ⚠️ medium |
| 5 | convention | Tasks index must be sorted numerically by task ID (TFW-1, 2, 3... not lexicographic TFW-1, 10, 11...). Extract int from folder name for sort key | User feedback: «сортированы как попало, как для роботов» | ✅ high |
| 6 | process | Executor role lacks explicit session fact capture step. Coordinator has §11 in HL + plan.md trigger. Executor should have equivalent in RF template + handoff.md trigger to prevent insight loss | User request + this session's experience | ✅ high |

## 7. Execution Session Insights

> Insights captured from the live execution and user testing session.
> Mirrors Coordinator's §11 Strategic Session Insights (HL template).
> Category reference: conventions.md §10.1.

| # | Insight | Category | Source |
|---|---------|----------|--------|
| E1 | «Нет ощущения вики движка вообще. Возможно это просто архитектурная ошибка и мы выбрали не то что нам нужно» — User's first reaction to the generated site. Technical implementation was correct (all tests pass), but UX failed. Tests verify structure, not usability. Live user testing is mandatory for output-facing features | philosophy | User, live testing session |
| E2 | «Когда кликаю... то там все классно, каждая задача как ссылка, можно перейти почитать» — knowledge/convention/ page worked well because it has resolved references. The problem was knowledge-index (KNOWLEDGE.md) using backtick-path format that the resolver didn't handle. Same technical capability, different source formatting = completely different UX | process | User, live testing session |
| E3 | «сортированы как попало, как для роботов» — Lexicographic sorting (TFW-1, TFW-10, TFW-11, TFW-2) is technically correct but human-hostile. Numeric sorting is a baseline UX requirement, never an afterthought | convention | User feedback on /tasks/ page |
| E4 | «Knowledge и Knowledge index как-то странно. Одно из них общий индекс по важнейшим артефактам. Второе это граф знаний» — Naming confusion between Architecture Index (KNOWLEDGE.md) and Knowledge Topics (knowledge/*.md). User can't distinguish them from names alone. Terminology review needed before public release | constraint | User, nav review |
| E5 | «Что реально поправить чтобы прототип работал? А что надо ставить под сомнение и вообще менять инструменты архитектуру?» — User explicitly asked for architectural honesty, not just fixes. Answer: MkDocs Material is correct tool, implementation needed directory URLs + backtick resolver + structured index. Tool change not needed — polish needed | philosophy | User, diagnostic question |

---

*RF — TFW-26 / Phase B: gen_docs.py Implementation | 2026-04-05*
