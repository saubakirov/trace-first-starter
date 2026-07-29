---
description: TFW Research — structured investigation between HL and TS, or standalone
---

# TFW Research — Comparative Decision Procedure

> 🔒 **ROLE LOCK: RESEARCHER**
> You write RES and research/ stage files only. You do NOT write HL, TS, ONB, RF, REVIEW, or code.

**Mindset:** Critical thinking partner. Reduce the uncertainty that can change a
product decision. Find missing evidence, expose exclusions, challenge assumptions, and
let reality change the disposition. Activity volume is not research sufficiency.

## Step 0: Resume & Iteration Detection

IF resuming (not fresh start): re-read this workflow + mode file.

**Iteration detection:**
1. Check `research/iterations.yaml`. IF exists → read it.
2. Determine current iteration number:
   - Count `research/iterN/` folders (N = highest folder number + 1, or 1 if none)
   - Cross-check with `research/iterations.yaml` → find first `status: pending` entry
3. IF current iteration > 1: read predecessor `research/iterN-1/RES.md` and any
   earlier RES files required by its open threads.

**Resume within iteration:**
Check current iteration's subfolder (`research/iterN/`): which stage files exist? → `research/iterN/RES.md` exists?
Resume from first missing stage. If RES.md for this iteration exists → this iteration complete.

## Step 1: Load Context

Read `conventions.md` §10. Verify loaded: AGENTS.md, conventions.md, glossary.md, KNOWLEDGE.md, Master HL (pipeline), relevant code.

## Step 2: Select Research Intensity

Read `project_config.yaml` → `tfw.research.default_mode`.
Present: "Recommend [{focused/deep}] intensity. Reason: {how added evidence breadth,
challenge depth, or uncertainty treatment changes decision risk}. Switch?"
🛑 WAIT — then load `research/{focused|deep}.md`.

Focused/deep are qualitative intensities within the same procedure. They do not select
an inquiry method and cannot prove procedure fit or completion. Operational owner:
[Research Intensity](../../conventions.md#research-intensity-and-closure).

**Entry:** Pipeline (task exists, RES in task folder) or Standalone (create task folder, Task Board `🔬 RES`).

## Step 3: Create Research Subfolder

**Iteration 1:** Create `research/iter1/` subfolder in task directory (create `research/` container if needed).
**Iteration N > 1:** Create `research/iterN/` subfolder (e.g., `research/iter2/`, `research/iter3/`).

**For iteration 2+:** Briefing MUST reference predecessor `research/iterN-1/RES.md`. Include:
- Predecessor decisions to build on (D-numbers with summaries)
- Open threads from predecessor Iteration Status block
- New hypotheses or user-injected directions since last iteration

## Step 4: Briefing and Procedure-Fit Gate

Copy `templates/research/1_briefing.md` into `research/iterN/`. Read the **Mindset** block — adopt this cognitive mode.

Fill Briefing:
1. Product purpose, applicable Project Values, and decision-changing uncertainty
2. The material alternatives, relationships, or configuration question
3. What result would change the approach
4. Research Plan: only actions needed to support or limit that decision
5. Hypotheses from HL §10 (pipeline mode)
6. Scope/corpus intent, evidence families, and exclusions
7. Only decision-changing questions; prioritize/split if the user cannot answer safely or coherently in one turn

**Fit decision:** Apply the
[Comparative Decision Procedure](../../conventions.md#comparative-decision-procedure)
only when the uncertainty requires comparing material alternatives, relationships, or
configurations.

- **FIT:** record why, complete Briefing, and continue.
- **MISMATCH:** record the unresolved information need and return it to the
  Coordinator/user. Do not select, name, simulate, or load a substitute strategy. Write
  the Briefing trace before stopping.

On **FIT**, write and present the Briefing trace, then 🛑 WAIT.

## Step 5: Run Stages (Gather → Extract → Challenge)

**Cross-stage natural dependency:** Gather establishes material decision factors,
alternatives, relationships, evidence families, and exclusions. Extract structures
consequential relationships or configurations from those Gather outputs. Challenge
attacks the Extract result with counter-evidence, incompatibilities, and edge/failure
cases. Do not invent factors or alternatives to fill a table. When a configuration
representation adds no decision value, use a legible comparison and preserve the same
Gather → Extract → Challenge dependency.

**FOR EACH stage** (Gather → Extract → Challenge):
1. **Copy** stage template from `templates/research/` into `research/iterN/`
2. **Read the Mindset block** — adopt this cognitive mode
3. **Execute** Evidence-Based Stage Loop (below)
4. **Complete** Checkpoint in stage file
5. 🛑 **STOP** — present findings, wait for user before next stage

### Evidence-Based Stage Loop

FOR EACH stage, repeat only while a named evidence gap can still change a material
disposition:

**OBSERVE:** Gather from the declared corpus/evidence families—project files, sources,
user input, environment, or other claim-appropriate observations.
**ORIENT:** State what the evidence confirms, challenges, excludes, or leaves unknown.
**DECIDE:** Evaluate the [Research Intensity and Closure
contract](../../conventions.md#research-intensity-and-closure):
  - material coverage and exclusions are explicit;
  - counter-evidence is addressed proportionately;
  - decision effect or unresolved result is stated;
  - open gaps/blockers have an owner or authority outcome;
  - further available evidence is no longer changing a material disposition, or the
    unavailable evidence and limitation are explicit.

  Sufficient or honestly unresolved → STAGE CHECKPOINT.
  A named gap can still change the decision → OBSERVE again.
  No obtainable evidence can close the gap → checkpoint as insufficient/unresolved.
**ACT:** Update stage file. Formulate next action.

### Stage Checkpoint

1. Present the supported disposition or explicit unresolved result, exclusions, and
   only decision-changing questions
2. Update stage file — mark `Stage complete: YES`
3. Run the
   [Research Learning Receipt](../../conventions.md#research-learning-receipts)
   selection test. Record each selected signal's disposition and required relation, or
   write **“No selected signal.”**
4. Recommend: close stage / continue for a named evidence gap
🛑 WAIT

## Step 6: Synthesis

1. Read all stage files (`1_briefing.md`, `2_gather.md`, `3_extract.md`, `4_challenge.md`)
2. Write `research/iterN/RES.md` using `templates/RES.md` — synthesize, don't copy-paste
3. HL Update Recommendations — consume applicable research decisions and Strategic
   Insight destinations
4. Fact Candidates — include only selected promote/merge/derive signals that require
   durable project verification. Preserve source, destination/backlink, and responsible
   actor. Leave reject/task-local/defer receipts resolvable in stage traces or existing
   open-thread/decision fields.
5. Strategic Insights — record human insight, analytical implication, and HL/decision
   disposition
6. **Findings Map** — visualize research findings. If no visualization is relevant:
   "No findings map."
7. **Iteration Status block** — name the entry trigger, closure claim, unresolved gaps,
   and Coordinator authority; do not use a completed count as sufficiency
8. Conclusion
9. **STOP.** "Research iteration {N} complete. Continue with `/tfw-plan` to review the
   closure claim and decide whether a named trigger warrants another iteration."

## Trust Protocol

| Input Type | Trust Level | Behavior |
|-----------|-------------|----------|
| Business/domain | Trust as-is | Clarify only |
| Technical approach | Verify | Cross-check externally |
| Numbers/claims | Empirical | Test or find evidence |
| "I tried this" | Trust outcome | Verify reason |

## Rules

- MUST: use claim-appropriate evidence from the declared corpus/families and expose exclusions; a newly fetched external source is not mandatory when a stage legitimately structures or challenges an already declared corpus
- MUST: checkpoint before advancing
- MUST: Briefing before stages, Synthesis after
- MUST: ask only decision-changing questions; prioritize and split when needed
- MUST: write stage file before every WAIT gate
- MUST: STOP after writing final RES (never proceed to HL/TS)
- MUST: preserve the complete filesystem floor for any claimed completed procedure:
  `1_briefing.md` → `2_gather.md` → `3_extract.md` → `4_challenge.md` → `RES.md`
- NEVER: skip to conclusions without data
- NEVER: treat user tech claims as proven
- NEVER: run stages silently
- NEVER: continue after a procedure-fit mismatch or choose a substitute method
→ `conventions.md` §14

## Numeric Authority

Research config keys and exact values remain unchanged for Phase E migration, but they
do not decide procedure fit, stage sufficiency, or iteration closure. Apply the
[Phase B Research Numeric Disposition
Ledger](../../conventions.md#phase-b-research-numeric-disposition-ledger):

- corpus/source coverage, exclusions, claim risk, and saturation replace query/file
  quotas;
- decision-changing questions replace a universal per-turn cap;
- `max_passes` is unconsumed residue;
- `min_iterations` is compatibility metadata, not a universal closure floor;
- `loops_per_stage` does not prove focused/deep completion;
- another iteration requires a named trigger and Coordinator/user authority.
