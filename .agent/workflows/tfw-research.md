---
description: TFW Research — structured investigation between HL and TS, or standalone
---

# TFW Research — Core Algorithm

> 🔒 **ROLE LOCK: RESEARCHER**
> You write RES and research/ stage files only. You do NOT write HL, TS, ONB, RF, REVIEW, or code.

**Mindset:** Critical thinking partner. Find what's missing, show blind spots, demand proof. Lead with observations: "I notice X, which means Y." Then ask: "Is that intentional, or did we miss Z?"

## Step 0: Resume & Iteration Detection

IF resuming (not fresh start): re-read this workflow + mode file.

**Iteration detection:**
1. Check task folder for `iterations.yaml`. IF exists → read it.
2. Determine current iteration number:
   - Count `researchN/` folders (N = highest folder number + 1, or 1 if none)
   - Cross-check with `iterations.yaml` → find first `status: pending` entry
3. IF current iteration > 1: read predecessor RES files for context.

**Resume within iteration:**
Check current iteration's subfolder: which stage files exist? → `RES__*` for this iteration exists?
Resume from first missing stage. If RES for this iteration exists → this iteration complete.

## Step 1: Load Context

Read `conventions.md` §10. Verify loaded: AGENTS.md, conventions.md, glossary.md, KNOWLEDGE.md, Master HL (pipeline), relevant code.

## Step 2: Select Mode

Read `PROJECT_CONFIG.yaml` → `tfw.research.default_mode`.
Present: "Recommend [{mode}]. Reason: {specific}. Switch? [focused/deep]"
🛑 WAIT — then load `research/{mode}.md`.

**Entry:** Pipeline (task exists, RES in task folder) or Standalone (create task folder, Task Board `🔬 RES`).

## Step 3: Create Research Subfolder

**Iteration 1:** Create `research/` subfolder in task directory.
**Iteration N > 1:** Create `researchN/` subfolder (e.g., `research2/`, `research3/`).

Copy templates from `templates/research/`. Fill Goal from HL §1 Vision.

**For iteration 2+:** Briefing MUST reference predecessor RES. Include:
- Predecessor decisions to build on (D-numbers with summaries)
- Open threads from predecessor Iteration Status block
- New hypotheses or user-injected directions since last iteration

## Step 4: Briefing Protocol

Write Briefing to current iteration's subfolder (`research/briefing.md` or `researchN/briefing.md`) using `templates/research/briefing.md`:
1. Research Plan (3-5 bullets per stage)
2. Hypotheses from HL §10 (pipeline mode)
3. Scope intent (in/out)
4. Guiding questions (≤3)
🛑 WAIT

## Step 5: Run Stages (Gather → Extract → Challenge)

Cover all three. Order flexible. Each stage uses its template (`templates/research/`). Each uses the OODA loop below.

### OODA Stage Loop

FOR EACH stage, repeat up to `loops_per_stage` (from YAML):

**OBSERVE:** Gather data — web search, file read, codebase, user input.
**ORIENT:** "Does this confirm or challenge what I thought?"
**DECIDE:** Sufficiency Verdict:
  Generic: ☐ External source used? ☐ Briefing gap closed?
  Mode-specific: ☐ {from mode file}
  ALL met → STAGE CHECKPOINT. NOT met + loops left → OBSERVE. NOT met + no loops → report, exit.
**ACT:** Update stage file. Formulate next action.

### Stage Checkpoint

1. Present findings + questions (≤3)
2. Update stage file — mark `Stage complete: YES`
3. Recommend: close stage / dig deeper
🛑 WAIT

## Step 6: Synthesis

1. Read all stage files (briefing, gather, extract, challenge)
2. Write `RES__*.md` using `templates/RES.md` — synthesize, don't copy-paste
   - Iteration 1: `RES__{ID}__{title}.md`
   - Iteration N > 1: `RES__iterN__{title}.md`
3. HL Update Recommendations (table)
4. Fact Candidates — review conversation history first
5. **Iteration Status block** (mandatory) — see RES template
6. Conclusion (1 paragraph)
7. **STOP.** "Research iteration {N} complete. Continue with `/tfw-plan` to review iterations and decide next step."

## Trust Protocol

| Input Type | Trust Level | Behavior |
|-----------|-------------|----------|
| Business/domain | Trust as-is | Clarify only |
| Technical approach | Verify | Cross-check externally |
| Numbers/claims | Empirical | Test or find evidence |
| "I tried this" | Trust outcome | Verify reason |

## Rules

- MUST: external research every stage
- MUST: checkpoint before advancing
- MUST: Briefing before stages, Synthesis after
- MUST: ≤3 questions per turn
- MUST: write stage file before every WAIT gate
- MUST: STOP after writing final RES (never proceed to HL/TS)
- NEVER: skip to conclusions without data
- NEVER: treat user tech claims as proven
- NEVER: run stages silently
→ `conventions.md` §14

## Limits

> From `PROJECT_CONFIG.yaml` (`tfw.research`). Defaults below.

| Parameter | Default | Type | Config key |
|-----------|---------|------|------------|
| Web queries per stage | 5 | Soft | `max_web_queries_per_stage` |
| Project files per stage | 15 | Soft | `max_files_per_stage` |
| Questions per turn | 3 | Hard | `max_questions_per_turn` |
| Max passes | 3 | Soft | `max_passes` |
| Min iterations | 2 | Hard | `min_iterations` |
