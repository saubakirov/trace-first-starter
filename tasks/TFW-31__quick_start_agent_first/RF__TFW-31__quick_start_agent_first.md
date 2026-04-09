# RF — TFW-31: Quick Start — Agent-First Rewrite (v3)

**Date:** 2026-04-09
**Executor:** Antigravity

---

## §1 Changes

### [NEW] .tfw/quickstart.md
- 4-step reading list for AI agents (46 lines)
- Step 1: Get TFW files (clone URL)
- Step 2: Learn TFW (read philosophy → glossary → conventions, in order)
- Step 3: Recommend philosophy to human
- Step 4: Run init.md
- Domain-agnostic language throughout ("decisions, reasoning, knowledge" — not "code")

### README.md (lines 42–82)
- 3 self-contained prompt blocks (new project / existing / already set up)
- Each prompt includes "Trace-First Workflow (TFW)" description + repo URL
- Each prompt references quickstart.md as entry point
- FAQ (3 questions), including "Can I use TFW for non-code work?"
- Philosophy link with "5 minutes" framing

### .tfw/workflows/init.md
- Phase 0 Bootstrap removed (was wrong approach — learning ≠ execution)
- Tutorial Mode enriched with mini-examples:
  - Task prefix: `LEE` → LEE-1, LEE-2, LEE-3
  - Task Board: ASCII table with realistic entries (Sales analysis, Client onboarding)
- Philosophy recommendation preserved in Tutorial Mode
- `.claude/commands/` copy instruction preserved in Phase 4
- Star CTA added after Phase 5 Verify (after value delivery, not during onboarding)

### docs/scripts/gen_docs.py
- Line 21: `.tfw/quickstart.md` → `getting-started.md` (was `.tfw/init.md`)
- Line 524: static_map entry updated to match

---

## §2 DoD Checklist

- [x] `.tfw/quickstart.md` exists with 4-step reading list
- [x] quickstart.md language is domain-agnostic
- [x] quickstart.md includes repo URL, reading order, human recommendation, pointer to init.md
- [x] README Quick Start has 3 self-contained prompt blocks
- [x] Each prompt includes "Trace-First Workflow (TFW)" description + repo URL
- [x] Each prompt has `<placeholder>` for project description
- [x] FAQ is 3 questions, domain-agnostic
- [x] init.md Phase 0 removed
- [x] init.md Tutorial Mode has mini-examples (prefix, task board)
- [x] init.md Phase 4 still has `.claude/commands/` copy instruction
- [x] gen_docs.py maps quickstart.md → getting-started.md
- [x] Star CTA in Phase 5 (after value delivery)
- [x] No other sections of README.md modified

---

## §3 Test Results

Structural verification:
- quickstart.md exists at `.tfw/quickstart.md` ✅
- README Quick Start section intact (lines 42–82) ✅
- init.md no longer has Phase 0 ✅
- init.md Tutorial Mode has mini-examples ✅
- gen_docs.py STATIC_SOURCES line 21 points to quickstart.md ✅
- gen_docs.py static_map line 524 points to quickstart.md ✅

---

## §4 Deviations from TS

| # | Deviation | Justification |
|---|-----------|---------------|
| 1 | README and gen_docs.py were already partially updated by previous executor iteration | Verified state matches TS v3 requirements, no re-edit needed |
| 2 | Added star CTA to init.md Phase 5 | Per user request during TS review, CTA after value delivery |

---

## §5 Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/init.md` | 1–21 | duplication | Old pointer file at `.tfw/init.md` still exists alongside `.tfw/workflows/init.md`. Now that quickstart.md is the "Getting Started" entry, this pointer file's role is unclear |

---

## §6 Fact Candidates

| # | Fact | Category | Source |
|---|------|----------|--------|
| 1 | TFW onboarding has a chicken-and-egg problem: init.md assumes context from AGENTS.md, but AGENTS.md doesn't exist yet. Solution: separate learning (quickstart.md) from execution (init.md) | Architecture | Research + user feedback |
| 2 | CTA (star, share) should come after value delivery, not during onboarding — standard marketing pattern | UX | User insight |
| 3 | TFW is domain-agnostic — examples and prompts should use "decisions, reasoning, knowledge" not "code" | Positioning | User insight |
| 4 | Self-contained prompts: when user copies from README, the prompt must include everything (repo URL, what TFW is, what to read) — agent doesn't see README context around the prompt | UX | User insight |
