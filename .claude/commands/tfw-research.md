# TFW Research — Core Algorithm

> 🔒 **ROLE LOCK: RESEARCHER**
> You write RES and research/ stage files only. You do NOT write HL, TS, ONB, RF, REVIEW, or code.

**Mindset:** Critical thinking partner. Find what's missing, show blind spots, demand proof. Lead with observations: "I notice X, which means Y." Then ask: "Is that intentional, or did we miss Z?"

## Step 0: Resume

IF resuming (not fresh start): re-read this workflow + mode file.
Check task folder: `research/` exists? → which stage files exist? → `RES__*` exists?
Resume from first missing stage. If RES exists → research complete.

## Step 1: Load Context

Read `conventions.md` §10. Verify loaded: AGENTS.md, conventions.md, glossary.md, KNOWLEDGE.md, Master HL (pipeline), relevant code.

## Step 2: Select Mode

Read `PROJECT_CONFIG.yaml` → `tfw.research.default_mode`.
Present: "Recommend [{mode}]. Reason: {specific}. Switch? [focused/deep]"
🛑 WAIT — then load `research/{mode}.md`.

**Entry:** Pipeline (task exists, RES in task folder) or Standalone (create task folder, Task Board `🔬 RES`).

## Step 3: Create Research Subfolder

Create `research/` subfolder in task directory. Copy templates from `templates/research/`. Fill Goal from HL §1 Vision.

## Step 4: Briefing Protocol

Write Briefing to `research/briefing.md` (use `templates/research/briefing.md`):
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
2. Write final `RES__*.md` using `templates/RES.md` — synthesize, don't copy-paste
3. HL Update Recommendations (table)
4. Fact Candidates — review conversation history first
5. Conclusion (1 paragraph)
6. **STOP.** "Research complete. Continue with `/tfw-plan` to update HL and write TS."

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