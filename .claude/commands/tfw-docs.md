# TFW Docs — Knowledge Update

You are now running the **TFW Docs** workflow.

## Role Lock

**COORDINATOR** — knowledge update only. No execution, no code changes.

## Instructions

1. Read and follow the canonical workflow: `.tfw/workflows/docs.md`

2. Determine trigger mode from user input:
   - **Manual**: `/tfw-docs {TASK-ID}` — update knowledge from a specific RF
   - **Batch**: `/tfw-docs --scan` — scan all REVIEWs without a `tfw-docs:` marker

3. Triage gate (1-second decision):
   - Was this a significant task? (architecture change, strategic decision, deprecation, new convention)
   - **YES** — run the knowledge update checklist
   - **NO** (bugfix, small refactor) — write `tfw-docs: N/A (minor)` in REVIEW

4. Knowledge update checklist:
   | # | Question | If YES, update | Section |
   |---|----------|----------------|---------|
   | 1 | Architecture changed? | `KNOWLEDGE.md` | Architecture Map |
   | 2 | New decision (D-record)? | `KNOWLEDGE.md` | Architecture Decisions |
   | 3 | Something deprecated/dropped? | `KNOWLEDGE.md` | Legacy & Deprecation |
   | 4 | New tech debt discovered? | `TECH_DEBT.md` | (append) |
   | 5 | New principle or convention? | `KNOWLEDGE.md` or conventions | Philosophy / Rules |

5. Present a diff preview. Wait for user approval before applying changes.

6. Mark in REVIEW: `tfw-docs: Applied — updated Sections X, Y` or `tfw-docs: N/A (minor)`

## User input

$ARGUMENTS
