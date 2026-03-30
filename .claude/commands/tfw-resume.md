# TFW Resume — Phase Status Bootstrap

You are now running the **TFW Resume** workflow.

## Role Lock

**COORDINATOR** — you may read artifacts, build a status matrix, and write Phase HL + TS. You MUST NOT execute, write ONB, write RF, or write code.

## Instructions

1. Load context in this order:
   - `AGENTS.md`
   - `.tfw/conventions.md`
   - `.tfw/glossary.md`
   - `KNOWLEDGE.md` (if exists)

2. Read and follow the canonical workflow: `.tfw/workflows/resume.md`

3. Execute the workflow phases:
   - **Phase 1**: Locate Task — user specifies task folder, read Master HL, extract vision/phases/principles
   - **Phase 2**: Build Status Matrix — scan for all phase artifacts, build and present the matrix table
   - **Phase 3**: Report & Decide — present structured resume report, ask user which phase to work on next

4. After user confirms:
   - Write Phase HL + TS for the chosen phase
   - Present for approval
   - After approval, instruct: "Start `/tfw-handoff` to begin execution."

## User input

$ARGUMENTS
