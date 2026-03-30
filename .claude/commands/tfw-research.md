# TFW Research — Structured Investigation

You are now running the **TFW Research** workflow.

## Role Lock

**🔒 COORDINATOR** — you may write RES files only. You MUST NOT write code, TS, ONB, RF, or REVIEW.
Agent operates in Read-only AG: reads project files and web sources, writes only to the RES file.

## Instructions

1. Load context in this order:
   - `AGENTS.md`
   - `.tfw/conventions.md`
   - `.tfw/glossary.md`
   - `KNOWLEDGE.md` (if exists)
   - Master HL for the task (pipeline mode)
   - Relevant code and artifacts

2. Read and follow the canonical workflow: `.tfw/workflows/research.md`

3. Determine entry mode:
   - **Pipeline** — after HL, before TS. RES file in task folder.
   - **Standalone** — any time, any topic. Create task folder if needed.

4. Run three stages: Gather → Extract → Challenge (order flexible).
   - Max 3 questions per stage (hard limit).
   - Checkpoint after each stage.
   - Final checkpoint: "Sufficient for TS?"

## User input

$ARGUMENTS
