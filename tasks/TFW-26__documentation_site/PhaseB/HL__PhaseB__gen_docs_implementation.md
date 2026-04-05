# HL — TFW-26 / Phase B: gen_docs.py Implementation

> **Date**: 2026-04-05
> **Author**: Coordinator
> **Status**: 📝 HL_DRAFT — Awaiting review
> **Parent HL**: [HL-TFW-26](../HL-TFW-26__documentation_site.md)

---

## 1. Vision

Phase B implements the gen_docs.py logic — the Layer 2 utility that reads TFW project artifacts and generates a navigable MkDocs site. After Phase B, running `mkdocs serve --config-file docs/mkdocs.yml` produces a fully functional local docs site with:
- All 13 static/glob sources compiled into pages
- All tasks/ artifacts accessible with preserved structure
- Reference resolver converting `RF TFW-18`, `D24`, `TD-59` into clickable hyperlinks
- Frontmatter on every page
- Working search across all content

**Impact:** The knowledge graph becomes browsable. A new team member, AI agent, or MCP endpoint can traverse the full decision chain — from verified fact → source RF → architectural decision → HL vision — through hyperlinks, not file system paths.

> "We ran `mkdocs serve`, opened the browser, clicked from knowledge/convention.md F4 → RES TFW-22 → HL-TFW-22 → D28 in KNOWLEDGE.md. Every link worked. The graph compiled itself."

## 2. Current State (As-Is)

| Aspect | Status |
|--------|--------|
| gen_docs.py | Skeleton with function signatures and manifests (Phase A) |
| Reference resolver | Patterns defined, logic = `pass` |
| MkDocs build | Exits 0 but produces only docs/index.md (12 nav warnings) |
| Local preview | `mkdocs serve` works but shows only placeholder page |

## 3. Target State (To-Be)

### 3.1 Result Visualization

```
$ mkdocs serve --config-file docs/mkdocs.yml
INFO    - Building documentation...
INFO    - [gen_docs] Processing 9 static sources...
INFO    - [gen_docs] Processing 4 glob patterns...
INFO    - [gen_docs]   knowledge/: 4 files
INFO    - [gen_docs]   tasks/: ~130 files
INFO    - [gen_docs]   workflows/: 12 files
INFO    - [gen_docs]   templates/: 9 files
INFO    - [gen_docs] Resolving references... 347 resolved, 5 warnings
WARNING - [gen_docs] Unresolved: "P3 protocol" in tasks/TFW-22.../HL (false positive, skipped)
INFO    - Documentation built in 2.3 seconds
INFO    - Serving on http://127.0.0.1:8000/

Browser:
  /                       → README.md with clickable Task Board
  /tasks/TFW-18.../       → Full task folder, all artifacts
  /knowledge-index        → KNOWLEDGE.md with D1-D34 as anchor links
  /knowledge/convention   → 7 facts, Source column = hyperlinks to RFs
  /reference/conventions  → Full conventions.md including §16
```

| Aspect | As-Is | To-Be |
|--------|-------|-------|
| gen_docs.py | 146 LOC skeleton (all `pass`) | ~200-250 LOC working implementation |
| Static sources | Not processed | 9 sources → 9 pages with frontmatter |
| Glob sources | Not processed | 4 patterns → ~155 pages with frontmatter |
| Reference resolver | Patterns only | Regex + glob resolution, ~5 resolver functions |
| MkDocs build | 12 warnings, 1 page | 0 errors, ~165 pages |
| Local preview | Placeholder | Full navigable site |

## 4. Principles

1. **Contract is the spec** — gen_docs.py implements exactly what conventions.md §16 specifies. No undocumented behavior.
2. **No silent misleading** — unresolvable references get `⚠️` marker in output (reader never mistakes broken link for text). In CI `--strict` mode, unresolved refs fail the build. Missing optional sources = WARNING (page not generated, legitimate for new projects).
3. **P{N} false positive mitigation** — use context-aware patterns (only resolve in Source columns and known table contexts, or add negative lookahead for common prose patterns).
4. **Minimal transformation** — copy + frontmatter + reference resolution. No content rewriting, no reformatting.

## 5. Fact Candidates (from planning)

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | constraint | gen_docs.py runs inside mkdocs-gen-files context where `mkdocs_gen_files.open()` is the write API. Cannot use regular file I/O. Project root = `Path(__file__).parent.parent.parent` | RF TFW-26/A §2 Key Decision #1, #3 | ✅ high |

---

*HL — TFW-26 / Phase B: gen_docs.py Implementation | 2026-04-05*
