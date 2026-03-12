# RF — TFW-9: Update Source Mechanism

> **Date**: 2026-03-12
> **Author**: Executor (AI)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-9](HL-TFW-9__update_source_mechanism.md)
> **TS**: [TS__TFW-9](TS__TFW-9__update_source_mechanism.md)

---

## 1. What Was Done

### Modified Files

| File | Changes |
|------|---------|
| `.tfw/PROJECT_CONFIG.yaml` | Added `tfw.upstream` field with default `https://github.com/saubakirov/trace-first-starter` |
| `.tfw/workflows/update.md` | Added Step 0 (Fetch Upstream) with Linux/macOS + Windows commands; replaced vague prerequisites with concrete `.tfw/.upstream/` paths; updated all upstream file references to `.tfw/.upstream/.tfw/`; added Step 9 (Cleanup); updated Source header |
| `.tfw/init.md` | Added `upstream` to Step 2 config YAML example; added gitignore note about `.tfw/.upstream/` near Step 4 |
| `.tfw/glossary.md` | Expanded `tfw-update` entry with source resolution from `tfw.upstream` and `.tfw/.upstream/` staging |
| `.gitignore` | Added `.tfw/.upstream/` entry |

## 2. Key Decisions

1. **Full rewrite of `update.md`** rather than surgical multi-edit — the file needed structural changes (new Step 0 and Step 9, prereqs rewrite, reference updates across all steps). Rewrite was cleaner and less error-prone than patching 10+ locations.

2. **Kept conceptual "upstream" in prose** — in Step 3 category table, phrases like "Copy from `.tfw/.upstream/.tfw/` directly" now reference the concrete path. But high-level descriptions like "file not customized by project" remain conceptual. This matches ONB Recommendation #1.

3. **Added Windows PowerShell commands** alongside Linux/macOS in Step 0 and Step 9 — TS specified both platforms; consistent with OS-portability principle (HL P1, P5).

## 3. Acceptance Criteria

- [x] `PROJECT_CONFIG.yaml` has `tfw.upstream` with default GitHub URL
- [x] `update.md` Step 0 exists with fetch commands (Linux + Windows)
- [x] `update.md` references point to `.tfw/.upstream/.tfw/` not vague "upstream"
- [x] `update.md` Step 9 (cleanup) exists
- [x] `.gitignore` contains `.tfw/.upstream/`
- [x] `init.md` shows `tfw.upstream` in config example
- [x] `glossary.md` tfw-update entry mentions source resolution
- [x] `grep "Obtain upstream" .tfw/workflows/update.md` returns 0 results

## 4. Verification

- Lint (`echo "configure your lint command"`): N/A — no code, only markdown/yaml
- Tests (`echo "configure your test command"`): N/A — no executable tests
- Verify: All 8 acceptance criteria checked via file content inspection ✅

## 5. Deviations from TS

| # | TS Says | What Was Done | Justification |
|---|---------|---------------|---------------|
| 1 | Step 2: surgical edits to update.md (2a-2d) | Full file rewrite | Too many interlocking changes across 107 lines; rewrite was safer and produced identical result |
| 2 | Step 9 cleanup shows only bash | Added Windows PowerShell equivalent | Consistency with Step 0 which has both platforms per TS |

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/conventions.md` | 146 | todo | `update.md` workflow entry mentions "Compare versions → categorize changes → update checklist → re-sync adapters" — could add "fetch upstream" to match new Step 0 |
| 2 | `.tfw/workflows/update.md` | 9 | style | Source header now says `tfw.upstream` but `.tfw/README.md` may still reference the old description of the update workflow |

---

*RF — TFW-9: Update Source Mechanism | 2026-03-12*
