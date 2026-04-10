# TS — TFW-32 / Phase C: Multi-Iteration Research Formalization

> **Date**: 2026-04-10
> **Author**: AI (Coordinator)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> **Phase HL**: [HL Phase C](HL__PhaseC__multi_iteration_research.md)

---

## 1. Objective

Formalize multi-iteration research from 8 real iterations (TFW-32×4, VLM-3×4) into structural enforcement. After this phase: coordinator declares iteration count via `iterations.yaml`, researchers find predecessor context automatically, every RES has a mandatory Iteration Status block with gap lists and open threads, and plan.md blocks TS until `min_iterations` is met.

## 2. Scope

### In Scope
- Add `min_iterations` config key to PROJECT_CONFIG.yaml
- Add multi-iteration support to research workflow (`base.md`)
- Add coordinator iteration gate to plan.md
- Add `researchN/` folder naming and `RES__iterN__` file naming to conventions.md
- Add multi-iteration terms to glossary.md
- Document `iterations.yaml` format in conventions.md
- Update RES template with mandatory Iteration Status block

### Out of Scope
- Research mode files (focused.md, deep.md) — internal stage logic unchanged
- OODA loop changes — `loops_per_stage` and `max_passes` stay as-is
- Template content sections (Phase B scope, done)
- Workflow changes to docs.md, knowledge.md, review.md, handoff.md (not affected)
- Research briefing template structural changes (only add iteration-aware guidance)
- Creating `iterations.yaml` for existing tasks retroactively

## 3. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/PROJECT_CONFIG.yaml` | MODIFY | Add `min_iterations: 2` to `tfw.research` section |
| `.tfw/workflows/research/base.md` | MODIFY | Multi-iteration flow: Step 0 (resume from iterN), Step 3 (researchN/ folder), Step 4 (iter2+ briefing), Step 6 (Iteration Status requirement) |
| `.tfw/workflows/plan.md` | MODIFY | Step 6 extension: coordinator creates iterations.yaml, iteration gate after research returns |
| `.tfw/conventions.md` | MODIFY | §4 Research subfolder: add researchN/ naming, RES iteration naming, iterations.yaml format |
| `.tfw/glossary.md` | MODIFY | Add Iteration, iterations.yaml, min_iterations terms |
| `.tfw/templates/RES.md` | MODIFY | Add mandatory Iteration Status block before Conclusion |

**Budget:** 0 new files, 6 modifications. Within limits: max 14 files, max 12 modified, max 1200 LOC.

## 4. Detailed Steps

### Step 1: Add `min_iterations` to PROJECT_CONFIG.yaml

In `.tfw/PROJECT_CONFIG.yaml`, add `min_iterations` to the `tfw.research` section (after line 47, after `max_passes: 3`):

**After (insert line):**
```yaml
    min_iterations: 2           # Minimum research iterations before TS (coordinator gate)
```

### Step 2: Update conventions.md §4 — Research subfolder

In `.tfw/conventions.md`, replace the current "Research subfolder" subsection (lines 121-123):

**Before:**
```markdown
### Research subfolder

Research stage files are stored in `tasks/{ID}/research/`: `briefing.md`, `gather.md`, `extract.md`, `challenge.md`. File existence = stage completion. Final `RES__*.md` at task root = synthesis of all stages. Stage file format: see `.tfw/templates/research/` (briefing.md, gather.md, extract.md, challenge.md).
```

**After:**
```markdown
### Research subfolder

Research stage files are stored in `tasks/{ID}/research/`: `briefing.md`, `gather.md`, `extract.md`, `challenge.md`. File existence = stage completion. Final `RES__*.md` at task root = synthesis of all stages. Stage file format: see `.tfw/templates/research/` (briefing.md, gather.md, extract.md, challenge.md).

#### Multi-iteration research

When research spans multiple iterations, each iteration gets its own subfolder and RES:

| Iteration | Stage files folder | RES file (task root) |
|-----------|-------------------|---------------------|
| 1 | `research/` | `RES__{PREFIX}-{N}__{title}.md` |
| 2 | `research2/` | `RES__iter2__{title}.md` |
| 3 | `research3/` | `RES__iter3__{title}.md` |
| N | `researchN/` | `RES__iterN__{title}.md` |

**Trace rule:** Research folders accumulate — never delete or overwrite previous iteration's files. Each `researchN/` folder is a trace. Deleting them = deleting reasoning.

**Control file:** `iterations.yaml` at task root tracks iteration state. Created by coordinator in `plan.md` Step 6 before launching research. Format:

```yaml
task_id: PROJ-N
title: research focus description
min_iterations: 2       # from tfw.research.min_iterations or coordinator override
max_iterations: 5       # soft ceiling
iterations:
  - number: 1
    focus: "initial investigation of H1-H3"
    hypotheses: [H1, H2, H3]
    status: complete     # pending | in_progress | complete
    res_file: RES__PROJ-N__title.md
  - number: 2
    focus: "deepen findings from iter 1, test H4"
    hypotheses: [H4]
    status: pending
    res_file: RES__iter2__title.md
```

Coordinator updates `iterations.yaml` after each iteration (marks status, adds next iteration if needed). Researcher reads it at start to understand predecessor context and assigned hypotheses.
```

### Step 3: Update research workflow — multi-iteration flow

In `.tfw/workflows/research/base.md`, make four changes:

**3a.** Replace Step 0 (lines 12-16) to handle iteration detection:

**Before:**
```markdown
## Step 0: Resume

IF resuming (not fresh start): re-read this workflow + mode file.
Check task folder: `research/` exists? → which stage files exist? → `RES__*` exists?
Resume from first missing stage. If RES exists → research complete.
```

**After:**
```markdown
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
```

**3b.** Replace Step 3 (lines 30-32) to create iteration-aware subfolders:

**Before:**
```markdown
## Step 3: Create Research Subfolder

Create `research/` subfolder in task directory. Copy templates from `templates/research/`. Fill Goal from HL §1 Vision.
```

**After:**
```markdown
## Step 3: Create Research Subfolder

**Iteration 1:** Create `research/` subfolder in task directory.
**Iteration N > 1:** Create `researchN/` subfolder (e.g., `research2/`, `research3/`).

Copy templates from `templates/research/`. Fill Goal from HL §1 Vision.

**For iteration 2+:** Briefing MUST reference predecessor RES. Include:
- Predecessor decisions to build on (D-numbers with summaries)
- Open threads from predecessor Iteration Status block
- New hypotheses or user-injected directions since last iteration
```

**3c.** Replace Step 6 Synthesis (lines 66-73) to require Iteration Status:

**Before:**
```markdown
## Step 6: Synthesis

1. Read all stage files (briefing, gather, extract, challenge)
2. Write final `RES__*.md` using `templates/RES.md` — synthesize, don't copy-paste
3. HL Update Recommendations (table)
4. Fact Candidates — review conversation history first
5. Conclusion (1 paragraph)
6. **STOP.** "Research complete. Continue with `/tfw-plan` to update HL and write TS."
```

**After:**
```markdown
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
```

**3d.** Add `min_iterations` to the Limits table (after line 106):

**Before:**
```markdown
| Max passes | 3 | Soft | `max_passes` |
```

**After:**
```markdown
| Max passes | 3 | Soft | `max_passes` |
| Min iterations | 2 | Hard | `min_iterations` |
```

### Step 4: Add Iteration Status block to RES template

In `.tfw/templates/RES.md`, insert before the Conclusion section (before line 84, before `## Conclusion`):

```markdown
## Iteration Status

> **Mandatory block.** Every RES must include this, even for single-iteration research.

- **Iteration:** {N} of {min} (min) / {max} (max)
- **Hypotheses tested:** {H1 (status), H2 (status)...}
- **Hypotheses deferred:** {HN (reason) — or "None"}
- **Gaps discovered:** {list — or "None"}
- **Superseded decisions:** {DN supersedes DM (reason) — or "None"}

### Open Threads (for next iteration)

> If no open threads — write "No open threads."

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | {thread description} | {impact if not addressed} | {what next iteration should do} |

### Recommendation
- [ ] **SUFFICIENT** — proceed to `/tfw-plan` to update HL and write TS
- [ ] **MORE NEEDED** — {specify what and why}
- [ ] **BLOCKED** — {specify blocker}

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.
```

### Step 5: Add coordinator iteration gate to plan.md

In `.tfw/workflows/plan.md`, replace Step 6 (lines 65-75):

**Before:**
```markdown
## Step 6: RESEARCH decision

Review HL §10. Present: «N hypotheses need research. Blind spots: [list]. Recommend: RESEARCH / skip.»
- Default recommendation: **run RESEARCH**
- Frame as risk reduction: "Without RESEARCH, we are assuming X, Y, Z — are we confident enough?"
- Skipping requires concrete justification (not just "task is simple")

IF user approves research → "Start `/tfw-research`. Researcher role takes over." **STOP.**
IF user skips → confirm, proceed to Step 7.

After RESEARCH: read RES Closure → update HL → present diff to user → user confirms → proceed to Step 7.
```

**After:**
```markdown
## Step 6: RESEARCH decision & iteration management

### 6a. Initial RESEARCH decision

Review HL §10. Present: «N hypotheses need research. Blind spots: [list]. Recommend: RESEARCH / skip.»
- Default recommendation: **run RESEARCH**
- Frame as risk reduction: "Without RESEARCH, we are assuming X, Y, Z — are we confident enough?"
- Skipping requires concrete justification (not just "task is simple")

IF user skips → confirm, proceed to Step 7.
IF user approves research:

### 6b. Create iterations.yaml

Create `iterations.yaml` in task folder. Fields:
- `task_id`, `title`
- `min_iterations`: from `PROJECT_CONFIG.yaml` → `tfw.research.min_iterations` (default: 2). Coordinator can override per task.
- `max_iterations`: soft ceiling (default: 5)
- `iterations`: array with first entry: `number: 1`, `focus`, `hypotheses`, `status: pending`

**Then:** "Start `/tfw-research`. Researcher role takes over." **STOP.**

### 6c. Iteration gate (after each research iteration returns)

Read all `RES__*` files and `iterations.yaml`. For each completed iteration:
1. Update `iterations.yaml`: mark iteration `status: complete`, record `res_file`
2. Read Iteration Status block from RES: gaps, open threads, recommendation
3. Update HL with research findings (present diff to user)

**Gate check:**
- IF completed iterations < `min_iterations` → **MUST** launch next iteration.
  Add next entry to `iterations.yaml` (focus = gaps/threads from previous RES).
  "Starting iteration {N}. `/tfw-research`." **STOP.**
- IF completed iterations ≥ `min_iterations`:
  - IF researcher recommends MORE NEEDED and coordinator agrees → launch next iteration
  - IF researcher recommends SUFFICIENT or coordinator overrides → proceed to Step 7
  - Coordinator may override `min_iterations` with documented justification

After all iterations complete: update HL → present diff to user → user confirms → proceed to Step 7.
```

### Step 6: Update glossary.md — add multi-iteration terms

In `.tfw/glossary.md`, insert three new terms after "Pass (Research)" (after line 110, before "## Read-only AG"):

```markdown
## Iteration (Research)
One full round of `/tfw-research` within a multi-iteration task. Each iteration has its own subfolder (`researchN/`), its own RES file (`RES__iterN__*.md`), and a mandatory Iteration Status block. Iteration 1 = standard research. Iteration 2+ = builds on predecessor findings, addresses open threads and gaps. Minimum iterations configurable via `tfw.research.min_iterations` in PROJECT_CONFIG.yaml (default: 2). → conventions.md §4 Research subfolder

## iterations.yaml
Control file at task root for multi-iteration research. Created by coordinator in `plan.md` Step 6b. Contains: `task_id`, `title`, `min_iterations`, `max_iterations`, and an `iterations` array tracking each iteration's number, focus, hypotheses, status, and RES file path. Coordinator owns this file — researchers read it, coordinator updates it. → conventions.md §4 Research subfolder

## min_iterations
Configurable hard floor for research iterations. Default: 2 (from `tfw.research.min_iterations` in PROJECT_CONFIG.yaml). Coordinator gate in `plan.md` Step 6c blocks TS until this many iterations complete. Coordinator can override per task in `iterations.yaml`. Rationale: researchers optimize for speed, structural enforcement ensures minimum depth. → plan.md Step 6c
```

### Step 7: Verify Iteration Status block in existing RES template

In `.tfw/templates/RES.md`, verify that the Conclusion section (currently line 84) has no conflicting content. The Iteration Status block from Step 4 goes BEFORE Conclusion. The final template order should be:

```
... Findings Map → Iteration Status → Conclusion → footer
```

No other changes to RES template — the Fact Candidates, Strategic Insights (Research), and Findings Map sections were already added in Phase B.

## 5. Acceptance Criteria

- [ ] `tfw.research.min_iterations: 2` exists in PROJECT_CONFIG.yaml under `tfw.research`
- [ ] conventions.md §4 has "Multi-iteration research" subsection with: `researchN/` naming table, trace rule, `iterations.yaml` format (YAML block with all fields)
- [ ] research/base.md Step 0 detects iterations: checks `iterations.yaml`, counts `researchN/` folders, reads predecessor RES
- [ ] research/base.md Step 3 creates `researchN/` for iteration N>1 and includes iter2+ briefing guidance
- [ ] research/base.md Step 6 names RES files per iteration (`RES__iterN__`) and requires Iteration Status block
- [ ] research/base.md Limits table includes `min_iterations` row with default 2 and config key
- [ ] plan.md Step 6 has three sub-steps: 6a (decision), 6b (create iterations.yaml), 6c (iteration gate)
- [ ] plan.md Step 6c gate logic: iterations < min → MUST launch next; iterations ≥ min → coordinator decides
- [ ] plan.md Step 6c specifies: update HL after each iteration, present diff, user confirms
- [ ] RES template has Iteration Status block (Iteration N/M, tested/deferred hypotheses, gaps, superseded decisions, Open Threads table, Recommendation) before Conclusion
- [ ] glossary.md has "Iteration (Research)", "iterations.yaml", "min_iterations" entries with cross-references
- [ ] STOP message in research/base.md Step 6 says "iteration {N} complete" not just "research complete"

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| iterations.yaml format too complex for agents to parse | Keep YAML minimal: flat array, no nesting beyond iteration entries. Living example in conventions.md |
| plan.md Step 6 becomes too long (3 sub-steps) | Sub-steps are sequential: 6a happens once (start), 6c repeats per iteration. Clear flow |
| Iteration Status block adds boilerplate to simple single-iteration research | Block is mandatory but lightweight. "No open threads" and "None" defaults prevent bloat |
| Research workflow becomes complex with iteration detection | Step 0 detection is read-only. If no iterations.yaml → standard single-iteration flow (backwards compatible) |
| Backwards compatibility — existing tasks without iterations.yaml | All changes are additive. No iterations.yaml → workflow behaves exactly as before |

> **Cross-references**: D4 (iterations.yaml + exit protocol), D14 (YAML + coordinator hard gate + min_iterations), D18 (researchN/ folders, accumulate don't overwrite), D19 (full design). HL Phase C §5. Master HL §4 Phase C.

---

*TS — TFW-32 / Phase C: Multi-Iteration Research Formalization | 2026-04-10*
