# ONB — TFW-10: Version String Sweep

> **Date**: 2026-03-14
> **Author**: Executor
> **Status**: 🟠 ONB — No blocking questions
> **Parent HL**: [HL-TFW-10](HL-TFW-10__version_string_sweep.md)
> **TS**: [TS__TFW-10](TS__TFW-10__version_string_sweep.md)

---

## 1. Understanding

Replace 14 occurrences of `TFW v3` across 10 files with `TFW 0.4`, preserving the `.tfw/README.md` Evolution section where `v3` is historical narrative. Deliver as branch `fix/version-string-sweep` + PR against `master`.

## 2. Entry Points

All changes are in 8 `.tfw/` files and 2 root files, all text substitutions. Target lines are confirmed from live grep output (Step Id: 16). No code files involved.

## 3. Questions (blocking)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions | — |

## 4. Recommendations

1. **Root README.md h1** — TS specifies removing `v3` from the title entirely (`# Trace-First Workflow (TFW) — Canonical Starter`). This is correct: the h1 is a product name, not a version label.
2. **AGENTS.md line 4** — TS says replace with "Follow TFW conventions…". Dropping the version reference entirely is cleaner than substituting `0.4`, since AGENTS.md is copied into downstream projects and will drift from the actual version.

## 5. Risks Found

1. **Scope budget (10 files > 7)** — flagged in TS, acknowledged. All changes are mechanical string substitutions; budget rationale (AI complexity) does not apply. Proceeding without split.
2. **`.tfw/README.md` Evolution section** — lines 266–290 contain `v3` in historical context. Will verify with explicit grep after sweep.

## 6. Inconsistencies with Code

1. TS §3 table lists `.tfw/adapters/antigravity/README.md` line 34 as `# TFW v3 (from step 1)` — actual text is `├── tfw.md                  # TFW v3 (from step 1)`. Replacement will target just the `TFW v3` substring, leaving the surrounding tree structure intact.

---

*ONB — TFW-10: Version String Sweep | 2026-03-14*
