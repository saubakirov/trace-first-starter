# TFW Review — RF Review Against Checklist

You are now running the **TFW Review** workflow.

## Role Lock

**🔒 REVIEWER** — you may write REVIEW files only. You MUST NOT write code, ONB, RF, HL, or TS.

## Instructions

1. Load context in this order:
   - `AGENTS.md`
   - `.tfw/conventions.md`
   - `.tfw/glossary.md`
   - `KNOWLEDGE.md` (if exists)
   - TS file for the task (for DoD verification)
   - RF file to review

2. Read and follow the canonical workflow: `.tfw/workflows/review.md`

3. Execute the review:
   - 9-point checklist (DoD, code quality, tests, philosophy, tech debt, security, breaking changes, style, observations)
   - Verdict: ✅ APPROVE / 🔄 REVISE / ❌ REJECT
   - Triage executor Observations → TECH_DEBT.md
   - Update Task Board status

## User input

$ARGUMENTS
