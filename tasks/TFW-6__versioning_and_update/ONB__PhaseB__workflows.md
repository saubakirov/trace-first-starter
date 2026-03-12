# ONB — TFW-6 / Phase B: Workflows

> **Date**: 2026-03-12
> **Author**: Executor (AI)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-6](HL-TFW-6__versioning_and_update.md)
> **TS**: [TS Phase B](TS__PhaseB__workflows.md)

---

## 1. Understanding

Phase B creates two canonical workflows (`tfw-release`, `tfw-update`) in `.tfw/workflows/`, their Antigravity adapter copies in `.agent/workflows/`, and updates `conventions.md` (§8 Workflows table + §2 Required Artifacts) and `glossary.md` (5 new terms). All content is specified verbatim in the TS.

## 2. Entry Points

| File | Action | Notes |
|------|--------|-------|
| `.tfw/workflows/release.md` | CREATE | General release process, references RELEASE.md |
| `.tfw/workflows/update.md` | CREATE | Downstream upgrade process with 🟢🟡🔴 categorization |
| `.agent/workflows/tfw-release.md` | CREATE | Identical copy of release.md |
| `.agent/workflows/tfw-update.md` | CREATE | Identical copy of update.md |
| `.tfw/conventions.md` | MODIFY | §8 table + §2 RELEASE.md entry |
| `.tfw/glossary.md` | MODIFY | 5 new terms |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. TS content is fully specified. | — |

## 4. Recommendations (suggestions, not blocking)

1. **TS Step numbering skip.** TS §4 labels steps as "Step 1, 2, 3 (adapter copies), 4, 5" but combines adapter creation into one step (Step 3). Conventions.md update is labeled "Step 4" and glossary update is "Step 5". I will follow TS step labels exactly.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Nested code fences in release.md.** The release workflow TS contains a Markdown code block inside the workflow content (the CHANGELOG entry template uses triple backticks). Since the workflow file itself is Markdown, this is fine — they are at different nesting levels. No issue.

## 6. Inconsistencies with Code (spec vs reality)

1. **conventions.md §8 is titled "Workflows" but uses a different table structure than TS.** Current §8 has columns `Workflow | Role | Purpose` — which matches the TS exactly. No inconsistency.

---

*ONB — TFW-6 / Phase B: Workflows | 2026-03-12*
