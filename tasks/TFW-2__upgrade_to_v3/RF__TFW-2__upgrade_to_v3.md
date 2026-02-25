# RF — TFW-2: Upgrade to TFW v3

> **Date**: 2026-02-25
> **Status**: ✅ Done
> **Source**: RBRT-6 / Phase C

## What Was Done

Upgraded trace-first-starter from TFW v2 to TFW v3.

### Copied from robert (.tfw/, 17 files)
- `.tfw/README.md` — replaced with stronger narrative draft (v2)
- `.tfw/conventions.md`, `.tfw/glossary.md`
- `.tfw/templates/` — HL, TS, RF, ONB, REVIEW
- `.tfw/workflows/` — plan, handoff, resume
- `.tfw/adapters/` — claude-code, cursor, antigravity
- `.tfw/init.md`, `.tfw/PROJECT_CONFIG.yaml` (generic template)
- Cleaned all robert/RBRT/nanobot references

### Rewritten root files
- `README.md` — v3 structure with 7-status lifecycle, Task Board, .tfw/ overview
- `AGENTS.md` — lean ~40 lines, refs .tfw/
- `TASK.md` — proper scope + DoD (merged SUCCESS_CRITERIA.md ideas)

### Created
- `TECH_DEBT.md` — empty registry

### Deleted (v2 artifacts)
- `AI_ENTRY_POINT.md` → content in .tfw/README.md + .tfw/conventions.md
- `SUCCESS_CRITERIA.md` → merged into TASK.md DoD
- `00_meta/` (HL_conventions.md, HL_glossary.md) → replaced by .tfw/

### Antigravity adapter
- `.agent/rules/tfw.md` — from template
- `.agent/workflows/tfw-plan.md`, `tfw-handoff.md`, `tfw-resume.md` — copied from .tfw/workflows/

## Observations
- .tfw/README.md had 2 nanobot references that needed cleaning — Phase A/B decontextualization was incomplete
- Original README author voice (Values table, Conduct) preserved in root README
