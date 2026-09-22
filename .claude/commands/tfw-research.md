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

## Step 0 — Resume & Iteration Detection

On resume, reread this workflow and mode. For pipeline research, require the Coordinator-prepared
`research/iterations.yaml`; a missing, malformed or incomplete pending entry returns to the
Coordinator before research work. The Researcher never creates or edits this file. Current iteration
is the first pending entry, cross-checked against `iterN/` folders (highest + 1, else 1); for N>1 read
predecessor RES files. In current `iterN/`, inspect stage/RES files. Resume from first missing stage.
Existing RES completes the iteration. Standalone research may infer iteration 1 when no control file
exists; it does not claim a Coordinator-governed iteration.

## Session identity checkpoint

After task and iteration resolution, apply `Session identity` with `WORK=RESEARCH` before any
research write, question, wait, or stage work. Iteration never supplies `PHASE`; only governing
task/phase state may do so.

## Activation and routing checkpoint

Apply the active root activation/routing contract before Step 1. Task-bound current work requires a
complete spine; total legacy absence is read-only and partial/mismatched routing refuses. Delegation
verifies its cited mandate/direct dispatch; owner-direct work invents no principal. Resolve the
iteration, keep the same Researcher unit, and record producer/routing provenance in Briefing and RES.

## Knowledge at use and return

At each use/return checkpoint, read and apply `Current knowledge use` and `Knowledge handover`.
Research stage/RES sections preserve exact source/version, producer unit, inspected scope, material
or justified-none, uncertainty and continuation for the authorized Coordinator.

## Step 1 — Load Context

Apply the Read Contract once. Read relevant code and external sources only when the current
question or stage requires them.

## Step 2 — Select Mode

Read `project_config.yaml` → `tfw.research.default_mode`.
Present: "Recommend [{mode}]. Reason: {specific}. Switch? [focused/deep]"
🛑 WAIT — then load `research/{mode}.md`.

**Entry:** Pipeline uses its task; Standalone creates a first-container task at `RES`.

## Step 3 — Create Research Subfolder

Create `research/iterN/` and its container when needed. For N>1, Briefing cites predecessor RES decisions, open threads, and new hypotheses/directions.

## Step 4 — Briefing Protocol

Copy the Briefing template into `iterN/`; adopt its **Mindset**.

Fill Briefing:
1. Research Plan (3-5 bullets per stage)
2. Hypotheses from HL §10 (pipeline mode)
3. Scope intent (in/out)
4. Guiding questions (≤3)
🛑 WAIT

## Step 5 — Run Stages (Gather → Extract → Challenge)

Gather sets dimensions; Extract maps configurations; Challenge tests survivors. Feed forward; below three dimensions use a matrix.

For each stage, copy its numbered template (`2_gather.md`, `3_extract.md`, or `4_challenge.md`), adopt Mindset, run OODA, complete the stage-file checkpoint, present findings, then STOP and wait before next stage.

### OODA Stage Loop

Repeat up to YAML `loops_per_stage`: **OBSERVE** via web/files/code/user; **ORIENT** against expectations; **DECIDE** with `External source used?`, Briefing-gap, and mode checks; **ACT** by updating the stage and next action. ALL met → STAGE CHECKPOINT. NOT met + loops → OBSERVE. NOT met + no loops → report, exit.

### Stage Checkpoint

Present findings and ≤3 questions; mark `Stage complete: YES`; recommend close/deeper; 🛑 WAIT.

## Step 6 — Synthesis

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
