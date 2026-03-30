# TFW Handoff — Task Execution

You are now running the **TFW Handoff** workflow.

## Role Lock

**🔒 EXECUTOR** — you may write ONB and RF only. You MUST NOT write HL, TS, REVIEW, or change scope.

## Instructions

1. Load context in this order:
   - `AGENTS.md`
   - `.tfw/conventions.md`
   - `.tfw/glossary.md`
   - `KNOWLEDGE.md` (if exists)
   - Master HL for the task
   - Phase HL (if multi-phase)
   - TS file for the task
   - Related HL/TS/RF files referenced in the task
   - Relevant code files listed in TS

2. Read and follow the canonical workflow: `.tfw/workflows/handoff.md`

3. Execute the workflow phases:
   - **Phase 1**: Executor Onboarding — read all context, write ONB using `.tfw/templates/ONB.md`, update Task Board to ONB. Wait for user to resolve blocking questions.
   - **Phase 2**: Execution — implement TS steps, run tests/lint/verify from `.tfw/PROJECT_CONFIG.yaml`, update Task Board to RF.
   - **Phase 3**: Write RF — document results using `.tfw/templates/RF.md`. MUST include Observations table.

## Critical Rules

- Never write RF before build/lint passes.
- Never skip the ONB phase.
- Never modify files outside TS scope.
- Observations section in RF is mandatory (write "No observations." if none).

## 🛑 Executor STOP

Your work is done after RF. Do NOT proceed to review. Tell the user:
"RF is complete. Start `/tfw-review` to review the results."

## User input

$ARGUMENTS
