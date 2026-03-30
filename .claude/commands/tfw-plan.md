# TFW Plan — Task Inception

You are now running the **TFW Plan** workflow.

## Role Lock

**COORDINATOR** — you may write HL and TS only. You MUST NOT write ONB, RF, or execute code.

## Instructions

1. Load context in this order:
   - `AGENTS.md`
   - Project Task Board (`README.md`)
   - `.tfw/conventions.md`
   - `.tfw/glossary.md`
   - `KNOWLEDGE.md` (if exists)
   - Relevant existing HL/TS/RF files

2. Read and follow the canonical workflow: `.tfw/workflows/plan.md`

3. Execute the workflow phases:
   - **Phase 1**: Research & Analysis — understand the problem, ask clarifying questions (max 3-5)
   - **Phase 2**: Write HL — create task folder, write HL using `.tfw/templates/HL.md`, update Task Board
   - **Phase 3**: Review & Refine — present HL for user approval, iterate
   - **Phase 3.5**: RESEARCH Gate — recommend RESEARCH or skip, wait for user confirmation
   - **Phase 4**: Decide scope — small task: write TS, get approval, STOP. Large task: define phases, write Phase A HL + TS

4. Read `.tfw/PROJECT_CONFIG.yaml` for task prefix and naming.

## Hard Stop

After TS is approved, you MUST stop. Do NOT proceed to execution. Tell the user:
"Planning complete. TS approved. Start `/tfw-handoff` to begin execution."

## User input

$ARGUMENTS
