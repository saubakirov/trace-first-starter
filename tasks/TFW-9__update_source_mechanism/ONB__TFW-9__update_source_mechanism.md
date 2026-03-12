# ONB — TFW-9: Update Source Mechanism

> **Date**: 2026-03-12
> **Author**: Executor (AI)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-9](HL-TFW-9__update_source_mechanism.md)
> **TS**: [TS__TFW-9](TS__TFW-9__update_source_mechanism.md)

---

## 1. Understanding

Add a concrete source-resolution mechanism to `tfw-update` so agents know **where** to get upstream files, **how** to fetch them, and **where to stage** them locally. This means: (1) `tfw.upstream` config field in `PROJECT_CONFIG.yaml`, (2) `.tfw/.upstream/` gitignored staging directory, (3) Step 0 in `update.md` with fetch/cleanup commands, and (4) documentation updates in `init.md` and `glossary.md`.

## 2. Entry Points

| File | Current state | What changes |
|------|--------------|--------------|
| `.tfw/PROJECT_CONFIG.yaml` | No `upstream` field (22 lines) | Add `upstream` under `tfw:` after `version` |
| `.tfw/workflows/update.md` | Steps 1–8, prereqs reference vague "obtain upstream" (107 lines) | Replace prereqs, add Step 0 (fetch), add Step 9 (cleanup), update references |
| `.tfw/init.md` | Step 2 config example lacks `upstream`; no `.upstream/` gitignore mention (199 lines) | Add `upstream` to YAML example, add gitignore note |
| `.tfw/glossary.md` | `tfw-update` entry at line 124-125 is brief (134 lines) | Expand with source resolution mechanism mention |
| `.gitignore` | 2 lines (`digest.txt`, `digest.md`) | Add `.tfw/.upstream/` |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions | — |

The TS is clear and self-contained. All five files are readable, all edit locations are precise.

## 4. Recommendations (suggestions, not blocking)

1. **TS Step 2c says "update all upstream references"** but current `update.md` Steps 1-8 don't actually contain literal `upstream .tfw/VERSION` strings — they reference `{upstream VERSION}` in code blocks and "upstream" in prose within Step 3 categorization tables. I'll update the prose and template references to point to `.tfw/.upstream/.tfw/` where concrete file paths are appropriate, but will leave general category descriptions (like "Copy from upstream directly") as-is since they describe the concept, not a file path.

2. **Acceptance criterion**: `grep "Obtain upstream" .tfw/workflows/update.md` returns 0. The current file has `Obtain upstream` on lines 14-15 in Prerequisites. Replacing Prerequisites per TS Step 2a will satisfy this — confirmed.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **No risks beyond TS coverage.** The TS already covers auth (CL mode), leftover staging dir (gitignored), and existing-project gitignore gap.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS says `initial_seq: 9` in PROJECT_CONFIG but step 1 YAML example omits it.** The TS Step 1 example shows `version`, `upstream`, `task_prefix` — it omits `id_format` and `initial_seq`. This is fine — the example is a snippet showing what to add, not the full file. I'll insert only the `upstream` line, preserving all existing fields.

2. **TS line numbers for prerequisites**: TS says "lines 13-15" for prerequisites. Actual file has prerequisites at lines 13-15 (counting from line 1 of the file content). Confirmed correct.

---

*ONB — TFW-9: Update Source Mechanism | 2026-03-12*
