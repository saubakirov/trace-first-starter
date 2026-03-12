# ONB — TFW-6 / Phase A: Core Versioning Infrastructure

> **Date**: 2026-03-12
> **Author**: Executor (AI)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-6](HL-TFW-6__versioning_and_update.md)
> **TS**: [TS Phase A](TS__PhaseA__versioning_infra.md)

---

## 1. Understanding

Phase A establishes the version tracking foundation for TFW. Scope: create 4 new files (`.tfw/VERSION`, `.tfw/CHANGELOG.md`, `.tfw/templates/RELEASE.md`, root `RELEASE.md`) and modify 2 existing files (`.tfw/PROJECT_CONFIG.yaml`, `.tfw/init.md`). All content is precisely specified in the TS. No code — pure Markdown/YAML artifacts.

## 2. Entry Points

| File | Action | Notes |
|------|--------|-------|
| `.tfw/VERSION` | CREATE | Single-line `0.3.0` |
| `.tfw/CHANGELOG.md` | CREATE | Retroactive entries cross-referenced with `.tfw/README.md` §Evolution |
| `.tfw/PROJECT_CONFIG.yaml` | MODIFY | Add `version: "0.3.0"` under `tfw:` |
| `.tfw/templates/RELEASE.md` | CREATE | Scaffold template with 6 sections |
| `RELEASE.md` (root) | CREATE | Populated instance for trace-first-starter |
| `.tfw/init.md` | MODIFY | Add version tracking section + RELEASE.md mention |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. TS is fully specified, content is exact. | — |

## 4. Recommendations (suggestions, not blocking)

1. **TS Step 6 integration points are clear enough.** The TS specifies inserting content at three points (Step 2.5, Step 4 addition, Verification addition). The current `init.md` structure maps cleanly to these insertion points. No risk of ambiguity.

2. **CHANGELOG 0.3.1 entry lists Phase B workflows.** The TS specifies including `tfw-release` and `tfw-update` workflows in the `[0.3.1]` CHANGELOG entry, but these are created in Phase B. This is fine — the CHANGELOG is describing the _release_ (which includes all phases), not just Phase A. Noting for traceability.

3. **`tfw.version` field naming.** The TS clarifies (Step 3) that the YAML field is `version` (not `tfw_version`) since it's nested under the `tfw:` namespace. The HL §3 mentions `tfw_version` in prose. TS takes precedence — using `version` under `tfw:`.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **`PROJECT_CONFIG.yaml` field ordering.** Current file has `task_prefix` immediately after `tfw:`, followed by `id_format`, `initial_seq`, `templates`. The TS says to add `version` under `tfw:` but does not specify position. I will place it as the first field under `tfw:` (before `task_prefix`) since version is the most fundamental metadata.

2. **init.md Step 2.5 numbering.** The TS labels the new section "Step 2.5". The current init.md uses "Step 2", "Step 3", etc. with `##` headers. Inserting "Step 2.5" as a heading works but is unusual. Will implement as specified.

## 6. Inconsistencies with Code (spec vs reality)

1. **`PROJECT_CONFIG.yaml` current structure.** The TS Step 3 shows the YAML snippet as:
   ```yaml
   tfw:
     version: "0.3.0"
     task_prefix: PROJ
     ...
   ```
   Actual file also has `id_format`, `initial_seq`, and a `templates:` block. No conflict — just noting that the TS shows a simplified snippet, not the full file.

---

*ONB — TFW-6 / Phase A: Core Versioning Infrastructure | 2026-03-12*
