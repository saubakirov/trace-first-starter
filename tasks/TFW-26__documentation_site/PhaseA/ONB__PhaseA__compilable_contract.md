# ONB — TFW-26 / Phase A: Compilable Contract + Infrastructure

> **Date**: 2026-04-05
> **Author**: Executor
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-26](../HL-TFW-26__documentation_site.md)
> **TS**: [TS Phase A](TS__PhaseA__compilable_contract.md)

---

## 1. Understanding

Phase A formalizes the **compilable contract** — a specification in conventions.md §16 that defines what structure TFW artifacts must have for deterministic compilation. The scope includes: the contract itself (source manifest, reference format, resolution rules, frontmatter, output nav), template amendments to standardize Source columns, 3 new glossary terms, and infrastructure scaffolding (docs/mkdocs.yml, docs/scripts/gen_docs.py skeleton, docs/requirements.txt, .github/workflows/docs.yml, .gitignore update). No implementation logic in gen_docs.py — that's Phase B.

## 2. Entry Points

| File | Role |
|------|------|
| `.tfw/conventions.md` L283-311 | End of file — §16 appended after §15 |
| `.tfw/templates/KNOWLEDGE.md` | §0, §1, §2, §3 Source columns — backtick paths → reference format |
| `.tfw/templates/TOPIC_FILE.md` | L4 stale §5 ref, add reference format note |
| `.tfw/templates/RF.md` | L62-64 FC table — add reference format note |
| `.tfw/templates/REVIEW.md` | L37-41 Tech Debt table, L63-66 FC table |
| `.tfw/templates/RES.md` | L47-49 FC table |
| `.tfw/glossary.md` | L175-182 — before `## Project-Specific Terms` |
| `.gitignore` | L1-5 — append `site/` |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | TS §16.1 row 7 changed KNOWLEDGE.md from "split by sections" (HL §3) to "Copy + frontmatter (whole file, no split)". The HL §3.1 visualization still shows separate pages for §0, §1, §3. Confirm: whole file as single page is the correct decision? | **Yes, whole file.** Decision made during planning: tasks/ included → all KNOWLEDGE.md links work without rewriting. Split added complexity for navigation that MkDocs TOC with anchors handles. Phase A HL §3.1 updated accordingly. |
| 2 | TS Step 4 mkdocs.yml has `docs_dir` implicitly defaulting to `docs/`. But gen_docs.py writes virtual pages via mkdocs-gen-files. Should `docs_dir` be set explicitly (e.g., `docs_dir: docs`) or left as default? Default is `docs/` relative to mkdocs.yml location. Since mkdocs.yml is inside `docs/`, the docs_dir would be `docs/docs/` — which is wrong. The TS should have `docs_dir: .` or the mkdocs.yml should be at project root. This affects CI workflow too (`--config-file docs/mkdocs.yml`). | **Use `docs_dir: ..`** in mkdocs.yml (points to project root). Config stays in `docs/` per HL §7 P10. Sources (README.md, .tfw/, knowledge/, tasks/) are at project root — `docs_dir` must reach them. CI: `mkdocs build --config-file docs/mkdocs.yml` works unchanged. |

## 4. Recommendations (suggestions, not blocking)

1. **mkdocs.yml location**: TS places it at `docs/mkdocs.yml`, but MkDocs default `docs_dir` is relative to the config file. If config is in `docs/`, then `docs_dir` defaults to `docs/docs/` which doesn't exist. Two fixes: (a) move mkdocs.yml to project root, or (b) set `docs_dir: .` in the config. Recommend (b) to keep all docs infrastructure in `docs/` per HL §7 P10. The gen-files plugin generates virtual pages independently of `docs_dir`, so this is about where MkDocs looks for manual/curated pages.

2. **HL template (HL.md) in template amendments**: TS Step 2 amends RF, REVIEW, RES, KNOWLEDGE, TOPIC_FILE templates — but not HL.md. The HL template has no Source columns currently. This is correct (HL usually has inline prose links, not table references). Just flagging for completeness.

3. **Reference pattern `P{N}` false positive risk**: The regex `\bP(\d+)\b` will match common prose like "P3 protocol", "P2P", etc. TS §6 acknowledges this with "Phase B will tune". I'll include the pattern exactly as specified — tuning is Phase B scope.

4. **`nav` section in mkdocs.yml**: The TS skeleton has `- Tasks: tasks/` and `- Knowledge: knowledge/` which rely on directory auto-discovery. MkDocs Material supports this. However, `tasks/` will only exist if gen_docs.py generates pages there (Phase B). The nav skeleton is correct for Phase A — it's forward-looking.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Windows line endings**: The KNOWLEDGE.md template has CRLF line endings (observed in the file). Other templates have LF. gen_docs.py (Phase B) should normalize line endings.

2. **TS has no mention of `docs/scripts/__init__.py`**: Python can't import `gen_docs` as a module without `__init__.py`. For mkdocs-gen-files, this isn't needed (it runs scripts directly), but it's worth noting.

## 6. Inconsistencies with Code (spec vs reality)

1. **TOPIC_FILE.md L4** says `§5` but KNOWLEDGE.md §4 is the Project Facts section (confirmed in both template and actual KNOWLEDGE.md). TS correctly identifies this fix — consistent.

2. **KNOWLEDGE.md template §1 header** says `Source RF` but TS changes it to `Source`. The actual KNOWLEDGE.md in the project already uses just `Source` (not `Source RF`). Template is stale — TS fix is correct.

3. **KNOWLEDGE.md template §2 Key Artifact column** says `` `tasks/PROJ-1.../RF-...md` `` but the RF naming convention is `RF__*.md` (double underscore), not `RF-*.md`. The TS standardizes to reference format (`RF {PREFIX}-1`), which fixes this.

---

*ONB — TFW-26 / Phase A: Compilable Contract + Infrastructure | 2026-04-05*
