# REVIEW — TFW-31: Quick Start — Agent-First Rewrite

**Date:** 2026-04-09
**Reviewer:** Antigravity (Reviewer mode)
**TS:** [TS-TFW-31](TS__TFW-31__quick_start_agent_first.md)
**RF:** [RF-TFW-31](RF__TFW-31__quick_start_agent_first.md)

---

## §1 Checklist

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| 1 | **DoD met?** | 🔄 Partial | 12/13 items met. 3 broken references left in live files (see §2) |
| 2 | **Quality** | ✅ Pass | quickstart.md is clean, domain-agnostic, 46 lines. README prompts self-contained |
| 3 | **Philosophy aligned** | ✅ Pass | quickstart.md separates learning from execution. Domain-agnostic throughout |
| 4 | **Tech debt** | ⚠️ Issues | 3 live broken refs to deleted `.tfw/init.md` (see §2) |
| 5 | **Breaking changes** | ⚠️ Caution | `.tfw/init.md` deleted — projects that fork/copy the starter may reference it |
| 6 | **Style & standards** | ✅ Pass | init.md Tutorial Mode mini-examples are concrete and helpful |

## §2 Findings

### 🔴 Broken references (must fix before APPROVE)

Deleting `.tfw/init.md` left 3 live references in framework core files:

| # | File | Line | Current | Fix |
|---|------|------|---------|-----|
| 1 | `.tfw/compilable_contract.md` | 15 | `.tfw/init.md` → `getting-started.md` | → `.tfw/quickstart.md` |
| 2 | `.tfw/compilable_contract.md` | 97 | `.tfw/init.md` in nav diagram | → `.tfw/quickstart.md` |
| 3 | `.tfw/conventions.md` | 209 | "See `.tfw/init.md` for setup" | → `.tfw/quickstart.md` |
| 4 | `.tfw/workflows/update.md` | 72 | `.tfw/init.md` in update checklist | → `.tfw/quickstart.md` |

### 🟡 Observations

| # | Type | Detail |
|---|------|--------|
| 1 | consistency | init.md Tutorial Mode line 23 says "If tutorial mode, suggest:" but previously said "Regardless of tutorial mode, suggest:" — the philosophy recommendation should be regardless of mode, not conditional |
| 2 | content | init.md mini-examples use `RND` prefix but TS specified `LEE`. Minor difference, `RND` is more generic — acceptable |
| 3 | scope | init.md Phase 2 Interview still has code-specific question: "What are your build/test/lint commands?" — should be more domain-agnostic or marked as software-specific. Out of scope for this task but noted |
| 4 | positive | quickstart.md Step 2 "Do not skip — each builds on the previous" is well done — enforces strict reading order |
| 5 | positive | CTA (star) placement after Phase 5 Verify is correct — after value delivery |

## §3 Tech Debt Collected

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| 1 | Review obs. 3 | Low | `.tfw/workflows/init.md` | Phase 2 Interview has code-specific question "build/test/lint commands" — should be domain-agnostic or conditional on project type | → backlog |
| 2 | Review | Low | Historical task artifacts | 40+ references to deleted `.tfw/init.md` in `tasks/` folder — historical, no action needed but noted | → accept (historical) |

## §4 Verdict

### 🔄 REVISE

**Reason:** 4 broken references to deleted `.tfw/init.md` in live framework files must be fixed before approval. These are in compilable_contract.md, conventions.md, and update.md — core files that agents and the doc pipeline actively read.

**Fix scope:** Update 4 lines across 3 files. No design changes needed.

After fix → re-verify → ✅ APPROVE.

## §5 Fact Candidates

| # | Fact | Category | Source |
|---|------|----------|--------|
| 1 | TFW has a chicken-and-egg problem at init: execution workflows assume context that doesn't exist yet. Fix: separate learning (quickstart.md) from execution (init.md) | architecture | TFW-31 RES |
| 2 | CTA (star, share) goes after value delivery, not during onboarding — standard marketing pattern | process | User insight |
| 3 | TFW is domain-agnostic — all examples, prompts, and workflows should use "decisions, reasoning, knowledge" not code-specific terminology | philosophy | User insight |
| 4 | Self-contained prompts: user copies prompt from README into agent — prompt must include everything (repo URL, what TFW is, what to read) because agent doesn't see surrounding context | convention | User insight |
