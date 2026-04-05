# ONB — TFW-26 / Phase B: gen_docs.py Implementation

> **Date**: 2026-04-05
> **Author**: Executor
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-26](../HL-TFW-26__documentation_site.md)
> **TS**: [TS Phase B](TS__PhaseB__gen_docs_implementation.md)

---

## 1. Understanding

Implement all `# TODO: Phase B` functions in `docs/scripts/gen_docs.py`. The skeleton from Phase A has the data structures (STATIC_SOURCES, GLOB_SOURCES, REFERENCE_PATTERNS) and function signatures already in place. My job: fill in the logic for `extract_title`, `add_frontmatter`, `copy_with_frontmatter`, `copy_glob`, `validate_sources`, `resolve_references` (with sub-resolvers), and `main()`. Then add `project_root` parameter for testability, read `tfw.task_prefix` from PROJECT_CONFIG.yaml, write unit + integration tests, and verify the full `mkdocs build --strict` pipeline locally.

## 2. Entry Points

| File | Role |
|------|------|
| `docs/scripts/gen_docs.py` | Main target — 10 TODO functions to implement |
| `docs/mkdocs.yml` | Config — `gen-files` plugin calls `scripts/gen_docs.py` |
| `docs/requirements.txt` | Dependencies — needs `pytest`, `pyyaml` additions |
| `.tfw/PROJECT_CONFIG.yaml` | Source for `tfw.task_prefix` (currently `TFW`) |
| `.tfw/conventions.md` §16 | Compilable contract — authoritative spec |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | TS Step 5 says `resolve_references()` needs a `project_root` parameter for testability. The Phase A skeleton has `resolve_references(content: str)`. The sub-resolvers (`_resolve_artifact_ref`, etc.) also need `root` for glob lookups. I plan to make `resolve_references(content: str, project_root: Path = None)` where `None` defaults to auto-detected root, and pass `root` into sub-resolvers via closure or module-level variable. Acceptable? | **Yes. Use closure** — sub-resolvers as inner functions or partial application inside `resolve_references()`. Cleaner than module-level state. `None` → auto-detect via `Path(__file__).parent.parent.parent`. |
| 2 | TS says `D{N}` should resolve "only inside tables" (`(?<=\| )`). But conventions.md §16.2 says `D{N}` appears in "KNOWLEDGE.md §1 Source column" and "any inline mention in artifact prose". Restricting to tables-only will miss prose mentions. Which behavior: (a) tables-only as TS says, or (b) all occurrences as conventions.md implies? | **(b) All occurrences.** conventions.md §16.2 is authoritative. Add negative lookahead: don't resolve inside backtick blocks or existing markdown links `[D24](...)`. |

## 4. Recommendations (suggestions, not blocking)

1. **Phase reference resolver (`_resolve_phase_refs`)**: TS Step 5 mentions `RF TFW-18/A` pattern but the provided code doesn't include implementation. I'll implement it following the same glob pattern: search `tasks/TFW-18*/PhaseA/RF__PhaseA*.md`.

2. **`_resolve_principle_ref` (P{N})**: TS explicitly defers P{N} to Phase C. The skeleton has the function signature — I'll leave it as a no-op that returns the original text, keeping the signature for Phase C.

3. **`--strict` flag and warnings**: `mkdocs build --strict` treats warnings as errors. The nav in `mkdocs.yml` references pages like `reference/release.md` which may not exist (RELEASE.md is optional). `--strict` will fail on missing nav entries. I'll need to verify this doesn't block the build, or handle it in the nav config. This is a Phase A decision (mkdocs.yml structure), so I'll document any workaround in RF deviations if needed.

4. **TS says `resolve_references` runs inside `copy_with_frontmatter`** — meaning each file is resolved as it's processed. This is the right design (resolve per-file, not globally), and the output paths in resolved links should be relative to the page's location in the docs site. I'll use site-relative paths (from root), which is how MkDocs Material handles links.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Link path format**: The resolver generates links like `[RF TFW-18](tasks/TFW-18__knowledge/RF__TFW-18__knowledge.md)`. These are source-relative paths. In MkDocs, links between generated pages should use the *output* path, not the source path. Since tasks/ preserves structure (source = output), this works for task artifacts. But links TO static sources (like `knowledge-index.md` for D{N} refs, or `reference/tech-debt.md` for TD-{N}) need to be site-root-relative or page-relative. The TS code uses hardcoded output paths for D{N} and TD-{N} which is correct.

2. **Windows path separators**: `Path.relative_to()` on Windows produces `\` separators. MkDocs expects `/` in links. I'll convert to forward slashes in link generation.

3. **HL naming convention**: HL files use `HL-{PREFIX}-{N}__title.md` (dash-prefixed ID). The artifact ref regex `(HL|TS|RF|...) (TFW-\d+)` handles `HL TFW-18` syntax, but the actual convention is `HL-TFW-18` (with dash). The TS code handles this with a fallback glob. I'll ensure both `HL TFW-18` and `HL-TFW-18` patterns are resolved.

## 6. Inconsistencies with Code (spec vs reality)

1. **Skeleton has `REFERENCE_PATTERNS` list** (L44-53) that pairs regex patterns with method names as strings. The TS implementation doesn't use this list — it implements each sub-resolver as a separate `re.compile()` + `.sub()`. I'll follow the TS approach (explicit function calls in `resolve_references`) and remove the unused `REFERENCE_PATTERNS` constant, since it's dead code after implementation.

2. **`main()` skeleton** (L132-145) has `warnings = validate_sources()` which iterates `warnings`. But the current skeleton's `validate_sources()` returns `None` (TODO). After implementation, `validate_sources()` returns `list[str]`, so `for w in warnings` works. However, if validate_sources raises on missing required sources, `main()` should let that exception propagate (build fails).

---

*ONB — TFW-26 / Phase B: gen_docs.py Implementation | 2026-04-05*
