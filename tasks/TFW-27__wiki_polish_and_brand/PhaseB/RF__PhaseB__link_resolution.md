# RF — TFW-27 / Phase B: Link Resolution & Dynamic Navigation

> **Date**: 2026-04-08
> **Author**: Executor
> **Status**: 🟢 RF — Execution complete
> **Parent HL**: [HL__PhaseB__link_resolution.md](HL__PhaseB__link_resolution.md)
> **TS**: [TS__PhaseB__link_resolution.md](TS__PhaseB__link_resolution.md)
> **ONB**: [ONB__PhaseB__link_resolution.md](ONB__PhaseB__link_resolution.md)

---

## 1. Summary

All 4 features from TS are implemented. `mkdocs build --strict` passes clean. 68 tests pass (55 unit + 13 integration).

## 2. What Was Done

### 2.1 Bare Task ID Resolver (TS Step 1)
- Added regex `(?<!\[)(?<!\w)\b(TFW-\d+)\b(?!\])(?!__)(?!/)` to resolve standalone `TFW-N` references to HL page links.
- Negative lookaheads prevent false positives: `(?!\])` blocks already-linked IDs, `(?!__)` blocks folder names, `(?!/)` blocks phase refs like `TFW-26/A`.
- Resolves by globbing `tasks/{PREFIX}-N__*/HL-*.md` and linking to the first match.

### 2.2 Markdown Link Rewriter (TS Step 2)
- `_build_path_map()` builds source→output mapping from STATIC_SOURCES + GLOB_SOURCES.
- `rewrite_markdown_links()` rewrites `[text](relative.md)` using the path map + PurePosixPath relpath computation.
- Template placeholder links (containing `{`) are neutralized to code spans to prevent strict-mode warnings.
- External, absolute, anchor-only, and non-`.md` links are passed through unchanged.

### 2.3 HTML Table Anchors (TS Step 3)
- `add_table_anchors()` injects `<span id="d24">D24</span>` into table rows matching entity patterns: `D{N}`, `TD-{N}`, `P{N}`, `F{N}`, `S{N}`.
- Applied to `knowledge-index.md` and `reference/tech-debt.md` output pages.

### 2.4 Literate-Nav SUMMARY.md (TS Step 4)
- `_generate_nav()` builds nav structure using `mkdocs_gen_files.Nav()` and writes `SUMMARY.md`.
- Conditional inclusion for optional sources: `KNOWLEDGE.md`, `TECH_DEBT.md`, `RELEASE.md` (Risk #4 fix).
- Workflows and templates are dynamically enumerated, including nested structures.

### 2.5 Configuration Changes (TS Steps 5–6)
- `docs/mkdocs.yml`: Removed 22-line hardcoded `nav:` block. Added `literate-nav` (nav_file: SUMMARY.md) and `section-index` plugins.
- `docs/requirements.txt`: Added `mkdocs-literate-nav>=0.6` and `mkdocs-section-index>=0.3`.

### 2.6 Strict Mode Fix (beyond TS scope)
All existing resolvers produced absolute links (`/tasks/...`, `/reference/...`) which MkDocs strict mode treats as warnings. Converted ALL resolvers to relative links by:
- Adding `output_path` parameter to `resolve_references()`.
- Creating `_make_url()` helper that computes relative paths via `_posix_relpath()`.
- Eliminating 3100+ absolute link INFO messages.

### 2.7 Task Board Regex Fix
The `_generate_tasks_index()` function's Task Board regex was capturing HL/TS/RF artifact column content (containing markdown links with `tasks/` paths) into the status field. Fixed to explicitly capture only columns 2 (Task) and 3 (Status).

## 3. Files Modified

| File | Delta | Change |
|------|-------|--------|
| `docs/scripts/gen_docs.py` | +236 LOC (445→681) | 4 new features + strict-mode refactor |
| `docs/mkdocs.yml` | -18 net | Removed nav block, added 2 plugins |
| `docs/requirements.txt` | +2 lines | `mkdocs-literate-nav`, `mkdocs-section-index` |
| `docs/scripts/test_gen_docs.py` | +147 LOC | 28 new unit tests (6 test classes) |
| `docs/scripts/test_integration.py` | 1 line fix | Updated D{N} assertion for relative URLs |

## 4. Test Results

```
55 unit tests passed     (test_gen_docs.py)
13 integration tests passed  (test_integration.py)
68 total — 0 failures
mkdocs build --strict — PASSED (0 warnings)
```

## 5. Decisions Made

| # | Decision | Rationale |
|---|----------|-----------|
| 1 | Convert ALL resolvers to relative links | Absolute links caused strict-mode failure. Not in original TS scope, but required for DoD #7 (strict pass). |
| 2 | `PurePosixPath` over `os.path.relpath` | Cross-platform safety (ONB Rec #2). No `import os`. |
| 3 | Template placeholders → code spans | MkDocs strict mode warns on `{PREFIX}` links in templates. Neutralizing them to code preserves display intent. |
| 4 | `(?!/)` in bare task ID regex | Prevents collision with phase refs (`TFW-26/A`) where `TFW-26` would be matched independently. |
| 5 | Task Board regex fix | Status field was capturing artifact link columns, causing `tasks/tasks/` double-prefix in tasks/index.md. |

## 6. LOC Budget

TS estimated ~120 LOC. Actual +236 LOC. Overage caused by:
- Strict-mode refactor (+50 LOC): `_make_url()`, `output_path` propagation, TD/D resolver functions
- Path utility functions (+25 LOC): `_normalize_posix_path`, `_posix_relpath`
- Conditional nav items (+15 LOC): optional source guards
- Task Board regex fix (+10 LOC)

gen_docs.py now at 681 LOC. Per TS §6: "if script exceeds ~600 LOC, consider extracting resolvers into a separate module."

## 7. Observations

### Fact Candidates
1. **FC-TECH**: gen_docs.py at 681 LOC — approaching the threshold for extraction. The reference resolver section alone is 200+ LOC and could become `resolvers.py`.
2. **FC-TECH**: All existing resolvers used absolute links, which was invisible in non-strict mode. Strict mode as a quality gate caught this latent issue.
3. **FC-PROCESS**: The bare task ID regex needed 3 negative lookaheads (`(?!\])(?!__)(?!/)`). Each one prevents a specific class of false positive. Complex regex deserves explicit unit tests for each case.
4. **FC-TECH**: `_generate_tasks_index()` Task Board parser had a regex that leaked artifact links into status text. Any time source markdown with links is parsed into another doc, link context shifts must be handled.

### Tech Debt Candidates
1. **TD-CANDIDATE**: Extract `resolve_references()` and helpers into `docs/scripts/resolvers.py` (gen_docs.py at 681 LOC, 14 files scope budget = OK but growing).
2. **TD-CANDIDATE**: Artifact resolver doesn't search PhaseX subfolders for `RF TFW-26` (only `RF TFW-26/A` works). Many "Unresolved reference: RF TFW-26" warnings in gen_docs output.
3. **TD-CANDIDATE**: `_generate_tasks_index()` Task Board parser is fragile — regex-based parsing of README.md tables. Consider extracting task metadata to a structured format.

---

*RF — TFW-27 / Phase B: Link Resolution & Dynamic Navigation | 2026-04-08*
