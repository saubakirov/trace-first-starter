# ONB — TFW-12: Config Centralization

> **Date**: 2026-03-30
> **Author**: Executor (AI)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-12](HL-TFW-12__scope_budget_centralization.md)
> **TS**: [TS-TFW-12](TS__TFW-12__config_centralization.md)

---

## 1. Understanding

Centralize 4 categories of duplicated parameters (scope budgets, version strings, template list, workflow list) into `PROJECT_CONFIG.yaml` as single source of truth. Phase A: add YAML sections + update 7 core docs with Pattern A/B/D references. Phase B: update 8 adapter/init/project-specific files with Pattern C/D + resolve TD-25/TD-26.

## 2. Entry Points

| File | Role |
|------|------|
| `.tfw/PROJECT_CONFIG.yaml` | Target config — add 4 sections |
| `.tfw/conventions.md` | §6 scope budgets (Pattern A) + title fix (Pattern D) |
| `.tfw/README.md` | §Scope Budgets (Pattern A) + prose version cleanup |
| `.tfw/workflows/plan.md` | §Scope Budget (Pattern A) |
| `.tfw/glossary.md` | Title (Pattern D) + inline budgets (Pattern B) |
| `.tfw/templates/TS.md` | L27 budget line (Pattern B) |
| `README.md` | Key Concepts budgets + version |
| `.tfw/adapters/*/` | 3 templates → Pattern C |
| `.tfw/init.md` | Config example + {version} instructions |
| `CLAUDE.md` | Version + list references |
| `.agent/rules/tfw.md` | TD-26 fix |
| `TECH_DEBT.md` | Mark TD-25, TD-26 resolved |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. Scope is clear, all files readable, patterns well-defined in RES. | — |

## 4. Recommendations (suggestions, not blocking)

1. **CLAUDE.md template L41**: lists `KNOWLEDGE` in templates but not `RELEASE`. TS item #8 says "reference config for lists" — I'll make the template reference `PROJECT_CONFIG.yaml` for the full list, which will also fix this omission.
2. **Antigravity tfw-rules template L12**: lists `(HL, TS, RF, ONB, RES, REVIEW)` — missing KNOWLEDGE and RELEASE. Same fix: reference config.
3. **Cursor template L13**: same — lists `(HL, TS, RF, ONB, RES, REVIEW)`. Same fix.
4. **init.md L196**: "Template structure" section has hardcoded `# TFW 0.5` — within scope of Phase B version cleanup.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **`.tfw/README.md` L166**: prose says `TFW 0.5 defines the following canonical workflows`. This is a version-in-prose instance not explicitly listed in TS §4 item #3, but falls under "remove `TFW 0.5` from prose". Will remove version prefix.
2. **`.tfw/README.md` L209**: prose says `TFW 0.5 defines four explicit roles`. Same pattern — will remove version prefix.
3. **Phase B scope ≤6 modified exceeded by 2**: TS already acknowledges this (L127: "justified — all single-line mechanical edits"). Accepted.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS §2 shows `tfw.version` with comment `# Installed TFW version`** — current PROJECT_CONFIG.yaml L7 has comment `# Installed TFW version (update via tfw-update)`. Minor — I'll keep the existing comment as it's more informative.
2. **TS §4 item #3 says `.tfw/README.md`: "Tree comments: reference config for lists"** — the tree at L63-81 uses inline comments like `# HL, TS, RF, ONB, RES, REVIEW, KNOWLEDGE, RELEASE templates`. These are file tree annotations, not standalone lists. Replacing them with a config reference would hurt readability of the tree. Recommend keeping tree comments as-is since they're visual and not authoritative.

---

*ONB — TFW-12: Config Centralization | 2026-03-30*
