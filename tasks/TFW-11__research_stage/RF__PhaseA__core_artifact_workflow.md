# RF — TFW-11 / Phase A: Core — Artifact, Status, Workflow

> **Date**: 2026-03-30
> **Author**: Executor (AI)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-11](HL-TFW-11__research_stage.md)
> **TS**: [TS Phase A](TS__PhaseA__core_artifact_workflow.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|----------|
| `.tfw/templates/RES.md` | RES artifact template — decisions/questions at top, 3 stages (Gather/Extract/Challenge) with checkpoints, final checkpoint with complexity check, conclusion |
| `.tfw/workflows/research.md` | RESEARCH workflow — role lock (Coordinator), two entry modes (pipeline/standalone), 3-stage process, agent behavior rules, limits from PROJECT_CONFIG, anti-patterns |

### Modified Files
| File | Changes |
|------|----------|
| `.tfw/conventions.md` | §3: added RES artifact type. §4: added RES naming (single-phase + phase). §5: pipeline updated to 9 statuses with 🔬 RES + skip path. §8: added research.md to workflows table. §15: added research.md to Role Lock table, added RES to forbidden lists for other workflows. |
| `.tfw/glossary.md` | Added RES artifact definition in Artifact Types section. Added 3 new terms: RESEARCH, Stage (Research), Pass (Research). Updated pipeline diagram to 9 statuses with skip path. Updated status count line. |
| `.tfw/PROJECT_CONFIG.yaml` | Added `res` to `tfw.templates` section. Added `research:` section with 4 parameters (web_queries_per_stage, files_read_per_stage, questions_per_stage, max_passes). |

## 2. Key Decisions

1. **English throughout** — all new content in English, matching user preference. Template headers, workflow text, glossary terms all in English.
2. **`tfw.templates.res` added** — not explicitly in TS, but consistent with existing pattern (all other templates registered there). Noted in ONB as recommendation #1.
3. **Skip path representation** — used `(skip: 🔵 HL ··· 🟡 TS)` on a separate line beneath the main pipeline diagram, as proposed in ONB.
4. **research.md length** — ~145 lines. Slightly over the ~100 line reference from plan.md, but covers two entry modes, three stages with behavior descriptions, checkpoint format, limits, and anti-patterns. Comparable to handoff.md (~177 lines).
5. **RES in forbidden artifacts** — added RES to forbidden artifact lists in plan.md, handoff.md, and resume.md rows of the Role Lock table to maintain isolation.

## 3. Acceptance Criteria

- [x] `.tfw/templates/RES.md` exists, contains all sections from TS Step 1 (context, decisions, open questions, 3 stages with checkpoints, final checkpoint with complexity check, conclusion)
- [x] `.tfw/workflows/research.md` exists, contains role lock, both modes (pipeline/standalone), 3 stages, limits reference, checkpoint format
- [x] `conventions.md` contains status 🔬 RES, artifact RES, updated pipeline, naming for RES files (single-phase + phase)
- [x] `glossary.md` contains terms: RES, Stage (Research), Pass (Research), RESEARCH
- [x] `PROJECT_CONFIG.yaml` contains `research:` section with 4 parameters
- [x] Pipeline diagrams in conventions.md and glossary.md updated (8 → 9 statuses including BLOCKED)

## 4. Verification

- Lint (`echo "configure your lint command"`): PASS (placeholder)
- Test (`echo "configure your test command"`): PASS (placeholder)
- Verify (`echo "configure your verify command"`): PASS (placeholder)
- Pipeline grep (`TODO.*HL.*TS` across `.tfw/`): conventions.md and glossary.md show 🔬 RES. plan.md, `.tfw/README.md`, init.md still show old pipeline — expected (Phase B scope).

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/workflows/plan.md` | 131 | desync | Pipeline diagram missing 🔬 RES — needs Phase B update |
| 2 | `.tfw/README.md` | 121 | desync | Pipeline diagram missing 🔬 RES — needs Phase B update |
| 3 | `.tfw/init.md` | 115 | desync | Pipeline status line missing 🔬 RES — needs Phase B update |
| 4 | `.tfw/workflows/handoff.md` | — | desync | No pipeline diagram, but references status flow in context — may need Phase B review |
| 5 | `README.md` (root) | 88 | desync | Key Concepts section shows old pipeline `⬜ TODO → 🔵 HL → 🟡 TS → ...` — needs Phase B update |

---

*RF — TFW-11 / Phase A: Core — Artifact, Status, Workflow | 2026-03-30*
