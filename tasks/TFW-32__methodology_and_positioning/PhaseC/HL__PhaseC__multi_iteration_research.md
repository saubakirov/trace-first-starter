# HL — TFW-32 / Phase C: Multi-Iteration Research Formalization

> **Date**: 2026-04-10
> **Author**: AI (Coordinator)
> **Status**: 📝 HL_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)

---

## 1. Vision

TFW research works in practice as multi-iteration — TFW-32 ran 4 iterations, VLM-3 ran 4 iterations. Each iteration discovered findings that previous ones missed or got wrong (superseded chain: D2→D10→D15). But the framework has zero structural support for this: one `/tfw-research` → one RES → done. Researchers rush to close ("SUFFICIENT"), coordinators track state in their heads, and the next iteration starts from scratch without knowing what the previous one concluded.

This phase formalizes multi-iteration research from 8 real iterations into structural enforcement: `iterations.yaml` control file, `researchN/` folder accumulation, researcher exit protocol, and a coordinator gate in `plan.md` that blocks TS until min_iterations are met.

**Impact:** After this phase, (1) coordinator declares iteration count and focus before research starts, (2) each researcher finds predecessor context in a control file, (3) researchers leave explicit gap lists and open threads for the next iteration, (4) coordinator cannot skip iterations — structural gate enforces minimum depth.

> "Without YAML or statuses, agents will fast-run every time. Agents always want to finish faster." — User (SS2)

## 2. Current State (As-Is)

### 2.1 Research workflow — single iteration only

| Aspect | Current state | Problem |
|--------|-------------|---------|
| Workflow entry | `/tfw-research` → `research/base.md` | Produces exactly one RES. No concept of "iteration 2" |
| State between iterations | None | Coordinator must manually brief next researcher with context from RES1 |
| Folder structure | `research/` with stage files (briefing, gather, extract, challenge) | Second iteration would overwrite first iteration's files |
| Exit protocol | RES Conclusion + "Continue with `/tfw-plan`" | No structured gap list, no open threads, no "what should the next iteration investigate" |
| Coordinator gate | plan.md Step 6: RESEARCH decision (yes/no) | No iteration tracking, no minimum depth enforcement |
| Configuration | `tfw.research` section in PROJECT_CONFIG.yaml | Has `max_passes` (3) but this is OODA loops per stage within one iteration, not iterations |

### 2.2 Evidence from real multi-iteration practice

| Project | Iterations | Key finding from later iterations |
|---------|-----------|----------------------------------|
| TFW-32 | 4 | Iteration 1 (D2) proposed wrong naming. Iteration 3 (D15) corrected it empirically. If stopped at 1: wrong naming deployed |
| TFW-32 | 4 | Iteration 4 discovered per-template naming (D22) — a design principle absent from iterations 1-3 |
| VLM-3 | 4 | Iteration 3 used sycophancy demolition to validate findings. Without it: 3 features would remain unvalidated |

Each iteration had a SPECIFIC trigger (FC15): error correction, gap filling, depth on a finding, or user-injected new direction. "Just run another iteration" without a trigger produces waste.

### 2.3 How researchers exit today

Current RES Conclusion paragraph + recommendation (SUFFICIENT / MORE NEEDED / BLOCKED). No structure. Examples from TFW-32:

- RES1: "Self-critique: H6 deferred without investigation." (Unstructured, buried in text)
- RES2: "Iteration Status" block with tested/deferred/gaps — **emergent pattern worth formalizing**
- RES3: "Iteration Status" + "Open Threads" table with thread/why/suggested focus — **best pattern, full structure**
- RES4: Same pattern, validated

The RES3/RES4 pattern emerged organically and was effective: the next researcher in iteration 4 read RES3's "Open Threads" and addressed exactly those threads.

## 3. Target State (To-Be)

### 3.1 Result Visualization

```
BEFORE:  /tfw-research → research/ → RES → done
                                             ↑ coordinator manually decides "more?"
                                               no structural enforcement, no state file

AFTER:
  Coordinator (plan.md Step 6):
    1. Reads HL §10 hypotheses
    2. Creates iterations.yaml (focus, min_iterations=2, hypotheses per iter)
    └→ /tfw-research (iteration 1):
         reads iterations.yaml → research/ → RES + Iteration Status block
    └→ /tfw-research (iteration 2):
         reads iterations.yaml + RES1 → research2/ → RES__iter2 + Iteration Status
    └→ ... (coordinator reads all RES files)
    └→ Coordinator: iterations ≥ min_iterations? Gaps resolved? → proceed to TS
                    iterations < min_iterations? → CANNOT proceed (hard gate)
```

```
FOLDER STRUCTURE (after 3 iterations):
  tasks/PROJ-N__title/
    iterations.yaml                      ← coordinator control file
    research/                            ← iteration 1 stage files
      briefing.md, gather.md, extract.md, challenge.md
    research2/                           ← iteration 2 stage files
      briefing.md, gather.md, extract.md, challenge.md
    research3/                           ← iteration 3 stage files
      briefing.md, gather.md, extract.md, challenge.md
    RES__PROJ-N__title.md                ← iteration 1 RES
    RES__iter2__title.md                 ← iteration 2 RES
    RES__iter3__title.md                 ← iteration 3 RES
```

```
RESEARCHER EXIT PROTOCOL (mandatory in every RES):

  ## Iteration Status
  - **Iteration:** N of M (min) / K (max)
  - **Hypotheses tested:** H1 (status), H2 (status)...
  - **Hypotheses deferred:** HN (reason)
  - **Gaps discovered:** list
  - **Superseded decisions:** DN supersedes DM (reason)

  ### Open Threads (for next iteration)
  | # | Thread | Why it matters | Suggested focus |
  |---|--------|---------------|-----------------|
  | 1 | {thread} | {impact} | {what to do} |

  ### Recommendation
  - [ ] SUFFICIENT
  - [ ] MORE NEEDED
  - [ ] BLOCKED
```

### 3.2 Value Flow

```
COORDINATOR PAIN              RESEARCH PIPELINE                    VALUE DELIVERED
──────────────────            ──────────────                       ──────────────
"Researcher closed too      → iterations.yaml (min=2,         →  Structural depth:
 early, missed critical       focus per iteration)                 can't skip iterations
 findings in iteration 1"                                         even when researcher
                            → researchN/ folders                   says "SUFFICIENT"
"No state between             (trace preservation)
 iterations, next           → Iteration Status block           →  Next researcher
 researcher starts            (gaps + threads + superseded)        knows exactly what
 from scratch"                                                     to investigate
                            → Coordinator gate in plan.md      →  TS cannot be written
"I track iteration            (iterations < min → BLOCK)           until minimum depth
 state manually in                                                 is guaranteed
 my head"
```

## 4. Scope

### In scope

1. Design `iterations.yaml` format: fields, lifecycle, who creates/reads/updates
2. Add `tfw.research.min_iterations` config key to PROJECT_CONFIG.yaml (default: 2)
3. Formalize researcher exit protocol — Iteration Status block template
4. Add iteration 2+ briefing guidance to research workflow (references predecessor RES)
5. Add coordinator iteration gate to plan.md (Step 6 extension)
6. Update research workflow (`base.md`) with multi-iteration flow
7. Update glossary with new terms: Iteration, iterations.yaml, min_iterations
8. Update conventions.md §4 with `researchN/` folder naming and RES iteration naming

### What is NOT in scope

- Renaming anything in research workflow (Phase B scope, done)
- Modifying RES template content sections (Phase B scope, done)
- Positioning/README changes (Phase D scope)
- Knowledge consolidation (Phase E scope)
- Research mode files (focused.md, deep.md) — internal mode logic stays unchanged
- OODA loop changes within a single stage — `loops_per_stage` and `max_passes` remain as-is

## 5. Key Research Decisions

| # | Decision | One-line summary |
|---|----------|-----------------|
| D4 | iterations.yaml + exit protocol | Each researcher writes per-iteration RES. Coordinator consolidates by reading ALL |
| D14 | Enforcement: YAML + coordinator hard gate + min_iterations | Without YAML, agents fast-run. Gate is in COORDINATOR pipeline (plan.md), not researcher |
| D18 | `researchN/` folders accumulate, don't overwrite | TFW trace philosophy: deleting stage files = deleting traces. research3 referenced research1 findings |
| D19 | Full design: iterations.yaml + exit protocol + briefing for iter2+ + coordinator gate | min_iterations=2 configurable hard floor. Researcher exit = mandatory Iteration Status block |

## 6. Deliverables

1. **`iterations.yaml` format spec** — fields: `task_id`, `title`, `created_by`, `iterations` array (each: `number`, `focus`, `hypotheses`, `status`, `res_file`), `min_iterations`, `max_iterations`
2. **`tfw.research.min_iterations`** config key in PROJECT_CONFIG.yaml — default: 2
3. **Researcher exit protocol** — mandatory Iteration Status block at end of every RES (Iteration N/M, tested/deferred hypotheses, gaps, superseded decisions, Open Threads table, Recommendation)
4. **Iteration 2+ briefing template** — references predecessor RES, reads iterations.yaml, carries forward unresolved hypotheses and open threads
5. **Coordinator iteration gate** — plan.md Step 6 extension: after RESEARCH returns, coordinator checks iterations vs min_iterations. If under → must launch another iteration. Cannot proceed to Step 7 (TS)
6. **Research workflow update** — `base.md` Step 0 (Resume) and Step 3 (Create subfolder) updated for `researchN/` pattern. Step 6 (Synthesis) updated with Iteration Status block requirement
7. **Glossary updates** — Iteration, iterations.yaml, min_iterations terms
8. **Conventions update** — §4 naming rules for `researchN/` folders and `RES__iterN__` files

## 7. Definition of Done (DoD)

- ✅ 1. `iterations.yaml` format is documented (fields, lifecycle, example)
- ✅ 2. `tfw.research.min_iterations: 2` exists in PROJECT_CONFIG.yaml
- ✅ 3. Researcher exit protocol is documented with mandatory fields (Iteration Status block)
- ✅ 4. Research workflow Step 0 handles iteration resume (detects `researchN/` folders)
- ✅ 5. Research workflow Step 3 creates `researchN/` for iteration N>1
- ✅ 6. Research workflow Step 6 requires Iteration Status block in every RES
- ✅ 7. plan.md Step 6 has iteration gate: cannot proceed to TS if iterations < min_iterations
- ✅ 8. Iteration 2+ briefing references predecessor RES and iterations.yaml
- ✅ 9. glossary.md has Iteration, iterations.yaml, min_iterations entries
- ✅ 10. conventions.md has `researchN/` and `RES__iterN__` naming rules

## 8. Definition of Failure (DoF)

- ❌ 1. Multi-iteration adds ceremony but no structural enforcement (min_iterations ignored by coordinator)
- ❌ 2. iterations.yaml format is so complex that agents fail to parse it
- ❌ 3. Exit protocol creates friction without useful gaps/threads for next iteration
- ❌ 4. plan.md gate is too rigid — blocks tasks where 1 iteration genuinely suffices

**On failure:** Simplify iterations.yaml to minimal viable fields. Add coordinator override mechanism for min_iterations with documented justification.

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| iterations.yaml format too complex for agents | Low | Medium | Keep YAML minimal: task, iterations array, min/max. Test with live example from TFW-32 |
| min_iterations=2 adds overhead for simple tasks | Low | Low | Configurable. Coordinator can set min=1 per task in iterations.yaml. PROJECT_CONFIG = default |
| researchN/ folders clutter task directory | Low | Low | Traces have value. This task's own 4 research folders are proof. Disk cost negligible |
| Exit protocol becomes boilerplate | Medium | Medium | RES3/RES4 Iteration Status blocks were useful in practice. Format is proven, not theoretical |
| plan.md gate conflicts with existing research decision flow | Low | Medium | Gate extends Step 6, doesn't replace. After research returns → check iteration count → decide |

## 10. RESEARCH Case

### Research Complete at Master HL Level

All multi-iteration decisions were made during 4 iterations of TFW-32 research. No additional research needed for this phase.

| # | Hypothesis | Status | Evidence |
|---|----------|--------|---------|
| H7 | Multi-iteration research should be formalized | ✅ CONFIRMED | 8 real iterations. Every later iteration found what early ones missed. D19: full design |
| H7b | Structural enforcement needed (YAML + gate) | ✅ CONFIRMED | User: "without YAML, agents fast-run." D14: 4 failure scenarios tested |
| H7c | Self-leading with min_iterations=2 | ✅ CONFIRMED | D19: full design validated. RES3/RES4 exit protocol emerged and proved useful |

### Living example: this task

TFW-32 itself is the proof-of-concept. The `research/`, `research2/`, `research3/`, `research4/` folders and RES1-RES4 files at task root demonstrate the exact pattern being formalized:
- Coordinator launched 4 iterations with specific foci
- Each researcher wrote stage files in `researchN/` + per-iteration RES on task root
- Superseded decisions chain (D2→D10→D15) demonstrates why >1 iteration matters
- RES3/RES4 exit protocol (Iteration Status + Open Threads) was read by subsequent iterations

## 11. Dependencies

| Dependency | Status |
|------------|--------|
| Phase A (pipeline fixes) — conventions.md, PROJECT_CONFIG.yaml | ✅ Complete |
| Phase B (naming & templates) — RES template has Iteration Status section | ✅ Complete |
| VLM-3 research (external project) — 4 iterations for pattern extraction | ✅ Complete (external) |

### Shared files with Phase A/B

⚠️ This phase touches conventions.md, glossary.md, and PROJECT_CONFIG.yaml — same files as Phase A and B. Since A and B are complete, no merge risk. Execute sequentially (Phase C after Phase B review).

## 12. Strategic Insights (Planning)

> Carried from Master HL §11. Only insights directly relevant to Phase C.

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S12 | «Researcher rushes to close. Coordinator decides how many iterations» — researchers optimize for speed, not depth. Structural enforcement is necessary | process | User |
| S7 | Knowledge Pipeline = killer feature. Multi-iteration research is part of this pipeline | philosophy | VLM-3 RES3 |
| S13 | «Section name = strongest single-word prompt. If named right, AI needs fewer instructions» — applies to iterations.yaml field names too | philosophy | User |
| S17 | «Collection algorithm reads each section — agent doesn't need standardized names to collect» — but agents DO need structural cues (iterations.yaml) to know they're in iteration N, not iteration 1 | process | User |

---

*HL — TFW-32 / Phase C: Multi-Iteration Research Formalization | 2026-04-10*
