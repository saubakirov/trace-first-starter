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

On resume, reread this workflow and mode. Read `research/iterations.yaml` when present. Current iteration is the first pending entry, cross-checked against `iterN/` folders (highest + 1, else 1); for N>1 read predecessor RES files. In current `iterN/`, inspect stage/RES files. Resume from first missing stage. Existing RES completes the iteration.

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

Set optional `writer` to the acting principal only when **Who Is Acting** resolves one; otherwise omit the field. Never create a profile per session.

## Agent Team checkpoint

When AT is declared, resolve the selected LEAD principal and mandate separately from this Researcher's
actual address, parent Coordinator unit, role/scope, direct channel, `Autonomous from`, governing
status, exact gate and dispatch refs before Step 1; recheck all on every continuation. Restate both
layers, authoritative sources and proposal origin `{principal, unit}` or `none` in Briefing and RES;
forwarding or restart never changes origin. Shared principal attribution grants nothing to this child.
Missing, conflicting, foreign, wrong-parent/address, or `—` authority requires a direct Coordinator
report and wait. Every WAIT and final RES return directly; continue in this Researcher. If
unavailable, require owner-approved §12 `SUPERSEDE` before bounded replacement dispatch. Non-AT
execution and Role Lock are unchanged.

## Step 1: Load Context

Apply the Read Contract once. Read relevant code and external sources only when the current
question or stage requires them.

## Step 2: Select Mode

Read `project_config.yaml` → `tfw.research.default_mode`.
Present: "Recommend [{mode}]. Reason: {specific}. Switch? [focused/deep]"
🛑 WAIT — then load `research/{mode}.md`.

**Entry:** Pipeline uses its task; Standalone creates a first-container task at `RES`.

## Step 3: Create Research Subfolder

Create `research/iterN/` and its container when needed. For N>1, Briefing cites predecessor RES decisions, open threads, and new hypotheses/directions.

## Step 4: Briefing Protocol

Copy the Briefing template into `iterN/`; adopt its **Mindset**.

Fill Briefing:
1. Research Plan (3-5 bullets per stage)
2. Hypotheses from HL §10 (pipeline mode)
3. Scope intent (in/out)
4. Guiding questions (≤3)
🛑 WAIT

## Step 5: Run Stages (Gather → Extract → Challenge)

Gather sets dimensions; Extract maps configurations; Challenge tests survivors. Feed forward; below three dimensions use a matrix.

For each stage, copy its numbered template (`2_gather.md`, `3_extract.md`, or `4_challenge.md`), adopt Mindset, run OODA, complete the stage-file checkpoint, present findings, then STOP and wait before next stage.

### OODA Stage Loop

Repeat up to YAML `loops_per_stage`: **OBSERVE** via web/files/code/user; **ORIENT** against expectations; **DECIDE** with `External source used?`, Briefing-gap, and mode checks; **ACT** by updating the stage and next action. ALL met → STAGE CHECKPOINT. NOT met + loops → OBSERVE. NOT met + no loops → report, exit.

### Stage Checkpoint

Present findings and ≤3 questions; mark `Stage complete: YES`; recommend close/deeper; 🛑 WAIT.

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

Trust business/domain facts but clarify. Verify technical approaches externally; test or source numbers/claims. Trust reported outcomes, not their explanation.

## Rules

- MUST: external research every stage
- MUST: written stage file and checkpoint before advancing or WAIT
- MUST: Briefing precedes Gather → Extract → Challenge; Synthesis follows
- MUST: ≤3 questions per turn
- MUST: STOP after writing final RES (never proceed to HL/TS)
- MUST: classify, never apply, HL recommendations each iteration
- NEVER: skip to conclusions without data, treat user technical claims as proven, or run stages silently
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
