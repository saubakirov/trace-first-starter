---
description: TFW Research — structured investigation between HL and TS, or standalone
---

# TFW Research — Core Algorithm

> 🔒 **ROLE LOCK: RESEARCHER**
> You write RES and research/ stage files only. You do NOT write HL, TS, ONB, RF, REVIEW, or code.

**Mindset:** Find gaps, expose blind spots, demand proof; observe, infer, question.

## Read Contract

Root instructions are already active. Read this workflow completely, then select inputs in this
order. Every shared range is addressed by its unique Markdown heading.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | selected task `status.md` and `journal/` | current lifecycle and lineage | task-local |
| 2 | master HL, `research/iterations.yaml`, and predecessor `research/iterN/RES.md` only for iteration 2+ | question, approved context, iteration/resume state | governing task artifacts |
| 3 | `.tfw/project_config.yaml` keys under `tfw.research` | mode and limits | project config |
| 4 | `.tfw/conventions.md` headings `HL (High Level)`, `Session identity`, `Commit Attribution`, `Fact Categories`, and `Anti-patterns (prohibited)` | contract, identity, attribution, candidate routing, prohibitions | shared rule |
| 5 | HL §7.2 citations and newly relevant knowledge | research evidence and decision context | named source |
| 6 | `.tfw/workflows/research/{mode}.md`, then only the first incomplete stage template; `.tfw/templates/RES.md` at synthesis | mode behavior and output form | workflow/template |

Full `AGENTS.md`, `conventions.md`, `glossary.md`, and `KNOWLEDGE.md` are not reloaded. Completed
stage files are read only for resume or synthesis; §14.1 history is read only when a compatibility
question triggers it. Missing or duplicate addressed headings are a hard stop under
`conventions.md` → `Context Selection`.

## Step 0: Resume & Iteration Detection

IF resuming (not fresh start): re-read this workflow + mode file.

**Iteration detection:**
1. Check `research/iterations.yaml`. IF exists → read it.
2. Determine current iteration number:
   - Count `research/iterN/` folders (N = highest folder number + 1, or 1 if none)
   - Cross-check with `research/iterations.yaml` → find first `status: pending` entry
3. IF current iteration > 1: read predecessor `research/iterN/RES.md` files for context.

**Resume within iteration:**
Check current iteration's subfolder (`research/iterN/`): which stage files exist? → `research/iterN/RES.md` exists?
Resume from first missing stage. If RES.md for this iteration exists → this iteration complete.

## Session identity checkpoint

After task and iteration resolution, apply `Session identity` with `WORK=RESEARCH` before any
research write, question, wait, or stage work. Iteration never supplies `PHASE`; only governing
task/phase state may do so.

## Who Is Acting

Resolve the acting handle **before the first durable write** — before any `status.md` change,
any journal event, any commit. Once per session, not per turn.

| Situation | What happens |
|---|---|
| One profile in `team/` | it is used, silently |
| Several profiles | read the binding on **this machine** — `~/.tfw/bindings.yaml`, or `%LOCALAPPDATA%\tfw\bindings.yaml` |
| No binding · a shared device · a copied binding · a handle whose profile is gone | **ask exactly one short question**, then proceed |

Identity is never inferred from an OS username, hostname, folder name or account display
string. Every event this session writes carries `on_behalf_of` (always a human) and `via`
(the tool). A writer is not named yet — that is TFW-54 — so do not create a profile per
session. → `conventions.md` §4

## Step 1: Load Context

Apply the Read Contract once. Read relevant code and external sources only when the current
question or stage requires them.

## Step 2: Select Mode

Read `project_config.yaml` → `tfw.research.default_mode`.
Present: "Recommend [{mode}]. Reason: {specific}. Switch? [focused/deep]"
🛑 WAIT — then load `research/{mode}.md`.

**Entry:** Pipeline uses its task; Standalone creates a first-container task at `RES`.

## Step 3: Create Research Subfolder

**Iteration 1:** create `research/iter1/` (and its container).
**Iteration N > 1:** create `research/iterN/`.

**For iteration 2+:** Briefing MUST reference predecessor `research/iterN-1/RES.md`. Include:
- Predecessor decisions to build on (D-numbers with summaries)
- Open threads from predecessor Iteration Status block
- New hypotheses or user-injected directions since last iteration

## Step 4: Briefing Protocol

Copy the Briefing template into `iterN/`; adopt its **Mindset**.

Fill Briefing:
1. Research Plan (3-5 bullets per stage)
2. Hypotheses from HL §10 (pipeline mode)
3. Scope intent (in/out)
4. Guiding questions (≤3)
🛑 WAIT

## Step 5: Run Stages (Gather → Extract → Challenge)

**Dimensional analysis:** Gather defines Dimensions; Extract forms Configuration Space; Challenge yields consistent survivors. Feed forward; below three dimensions use a matrix.

**FOR EACH stage** (Gather → Extract → Challenge):
1. **Copy** stage template from `templates/research/` into `research/iterN/`
2. **Read the Mindset block** — adopt this cognitive mode
3. **Execute** OODA Stage Loop (below)
4. **Complete** Checkpoint in stage file
5. 🛑 **STOP** — present findings, wait for user before next stage

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

1. Read all stage files (`1_briefing.md`, `2_gather.md`, `3_extract.md`, `4_challenge.md`)
2. Write `research/iterN/RES.md` using `templates/RES.md` — synthesize, don't copy-paste
3. **HL Update Recommendations — two classes, never one table**, each row naming its target HL section:
   - `Refinements` → free sections (§2, §7.2, §8-§11). The coordinator applies them
   - `Amendment Proposals` → frozen sections (§1, §3-§7). No evidence, cost and considered alternative = not a proposal
   Empty class → say so. **You classify; you never edit the HL** — the coordinator applies or escalates. Column grammar: `templates/RES.md`
4. Fact Candidates — review conversation history first
5. **Findings Map** — visualize findings, or state "No findings map."
6. **Iteration Status block** (mandatory) — see RES template
7. Conclusion (1 paragraph)
8. **STOP.** "Research iteration {N} complete. Continue with `/tfw-plan` to review iterations and decide next step."

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
- MUST: Briefing precedes stages; Synthesis follows
- MUST: ≤3 questions per turn
- MUST: write the stage file before each WAIT
- MUST: STOP after writing final RES (never proceed to HL/TS)
- MUST: produce HL recommendations every iteration — classified, never applied
- NEVER: skip to conclusions without data
- NEVER: treat user tech claims as proven
- NEVER: run stages silently
→ `conventions.md` §14

## Limits

> From `project_config.yaml` (`tfw.research`). Defaults below.

| Parameter | Default | Type | Config key |
|-----------|---------|------|------------|
| Web queries per stage | 5 | Soft | `max_web_queries_per_stage` |
| Project files per stage | 15 | Soft | `max_files_per_stage` |
| Questions per turn | 3 | Hard | `max_questions_per_turn` |
| Max passes | 3 | Soft | `max_passes` |
| Min iterations | 2 | Hard | `min_iterations` |
