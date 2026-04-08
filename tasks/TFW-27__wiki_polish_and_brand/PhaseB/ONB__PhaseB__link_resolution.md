# ONB — TFW-27 / Phase B: Link Resolution & Dynamic Navigation

> **Date**: 2026-04-08
> **Author**: Executor
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL__PhaseB__link_resolution.md](HL__PhaseB__link_resolution.md)
> **TS**: [TS__PhaseB__link_resolution.md](TS__PhaseB__link_resolution.md)

---

## 1. Understanding

Phase B adds 4 features to gen_docs.py (~120 LOC): (1) bare task ID resolver, (2) markdown link rewriter for broken cross-references, (3) HTML anchors on entity table rows, (4) literate-nav SUMMARY.md generation. Then config changes: remove hardcoded `nav:` from mkdocs.yml, add `literate-nav` + `section-index` plugins to requirements.txt. End state: `mkdocs build --strict` passes clean, all 31 broken internal links are auto-fixed, navigation is auto-generated from filesystem.

## 2. Entry Points

| File | Purpose | Lines of Interest |
|------|---------|-------------------|
| `docs/scripts/gen_docs.py` | Main build script (445 LOC). All 4 features go here | `resolve_references()` L243-387, `copy_with_frontmatter()` L88-98, `main()` L392-444, `STATIC_SOURCES` L18-28, `GLOB_SOURCES` L31-36 |
| `docs/mkdocs.yml` | Site config. Hardcoded `nav:` block L43-63 to remove, `plugins:` L37-41 to extend | L37-63 |
| `docs/requirements.txt` | Python deps. Add 2 new packages | L1-5 |
| `docs/scripts/test_gen_docs.py` | Unit tests (241 lines, 19 tests). Add tests for 3 new features | Entire file |
| `docs/scripts/test_integration.py` | Integration tests (187 lines). Add build verification | Entire file |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | TS Step 4 (literate-nav SUMMARY.md) uses `mkdocs_gen_files.Nav()` which requires the `mkdocs-gen-files` API. Current gen_docs.py does not import `Nav` from `mkdocs_gen_files`. The `mkdocs_gen_files.Nav()` API was added in `mkdocs-gen-files>=0.5` — should I verify the minimum version in requirements.txt is sufficient, or pin to a higher minimum? | Current `requirements.txt` already has `mkdocs-gen-files>=0.5`. This is sufficient — `Nav()` is available since 0.5. No version bump needed. |

## 4. Recommendations (suggestions, not blocking)

1. **Resolver ordering clarity.** The TS specifies link rewriter runs BEFORE `resolve_references()` (Step 2), but bare task ID runs INSIDE `resolve_references()` as the last sub-resolver (Step 1). This is correct and avoids conflicts — link rewriter handles pre-existing markdown links, then reference resolvers handle text patterns. I propose adding a comment block documenting the full pipeline order for maintainability.
   > ✅ Accepted. Add a pipeline order comment block.

2. **`os.path.relpath` on Windows.** TS §6 calls out the risk of `os.path.relpath` platform differences. I propose using `PurePosixPath` for all URL-relative computations instead, keeping `os.path` out of URL logic entirely. This is consistent with the existing pattern in gen_docs.py which uses `.replace("\\", "/")` everywhere.
   > ✅ Accepted. Use `PurePosixPath`. No `import os`.

3. **Test coverage.** TS does not specify test count, but the existing test suite has 19 unit tests + 14 integration tests. I plan to add ~8-10 unit tests (covering bare task ID, link rewriter, table anchors) and ~3-4 integration tests (strict mode, deep links, auto-nav). This keeps the test file manageable.
   > ✅ Accepted. Good coverage plan.

4. **`import os` scope.** TS Step 2 notes `import os` is needed. I recommend using `from pathlib import PurePosixPath` instead to avoid introducing `os` module dependency and keep path handling consistent with the existing codebase.
   > ✅ Accepted. Addressed by Rec 2.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Existing `D{N}` resolver produces absolute links.** — Safe, rewriter skips `/`-prefixed.

2. **`<span id="...">` inside table cells.** — Acceptable risk. `tables` extension present. Proceed.

3. **literate-nav Tasks section.** — Correct: flat Tasks entry is sufficient for Phase B. Per-task sidebar is Phase C if needed.

4. **RELEASE.md optional.** — Good catch. Conditionally add nav item: `if (root / "RELEASE.md").exists():`. Apply same logic to other optional sources (KNOWLEDGE.md, TECH_DEBT.md).
   > ✅ Must fix in implementation.

5. **Bare task ID regex and section headers.** — Acceptable trade-off. Links in headings are valid.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS Step 2 signature uses `source_path: str`** in `rewrite_markdown_links()`, but the function `copy_with_frontmatter()` at L88 receives `source_path: str` as the first argument. The TS correctly shows it being called as `rewrite_markdown_links(result, source_path, path_map)` — this is consistent with current code.

2. **TS Step 5 says "Remove the entire `nav:` block (lines 43-63)"** — actual mkdocs.yml `nav:` is at lines 43-63 (22 lines). This is accurate.

3. **TS Step 4 implies `_generate_nav()` is called in `main()`** but doesn't specify exact placement. It should run AFTER all pages are generated (after both static and glob processing), since it needs to reference pages that have been written. I'll add it at the end of `main()`.

---

*ONB — TFW-27 / Phase B: Link Resolution & Dynamic Navigation | 2026-04-08*
