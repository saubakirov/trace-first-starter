# RF — TFW-24: Researcher Role & RES State Machine

> **Date**: 2026-04-04
> **Author**: Executor
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-24](HL-TFW-24__res_state_machine.md)
> **TS**: [TS__TFW-24](TS__TFW-24__res_state_machine.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|------------|
| `tasks/TFW-24__res_state_machine/ONB__TFW-24__res_state_machine.md` | Onboarding report |

### Modified Files
| File | Changes |
|------|---------| 
| `.tfw/conventions.md` | §4: added Research subfolder convention. §8: research/base.md role → Researcher. §15: research/base.md → Researcher with Permitted `RES, research/ stage files` |
| `.tfw/glossary.md` | Coordinator: removed "Conducts RESEARCH and writes RES files". Added Researcher (AI) role definition with Hard Stop |
| `.tfw/workflows/research/base.md` | Role Lock → `RESEARCHER`. Added Step 0 (Resume Protocol). Step 3 → subfolder creation. Steps 4/5 → stage files. Removed Step 6 (Final Checkpoint — section removed from RES template). Renumbered old Step 7 → Step 6 (Synthesis + Hard Stop). Added 2 MUST rules. OODA ACT → "Update stage file" |
| `.tfw/workflows/plan.md` | Step 6: "Start `/tfw-research`. Researcher role takes over." + **STOP**. Footer self-check: added Researcher handoff check |
| `.tfw/templates/RES.md` | Removed 3 stage sections (Gather/Extract/Challenge) + Final Checkpoint. Reshaped to synthesis format: Decisions, Open Questions, Hypotheses, HL Update Recommendations, Fact Candidates, Conclusion. Briefing section references `research/briefing.md` |
| `.tfw/templates/HL.md` | §1 → Vision + Impact + stakeholder Quote. §2 → domain-agnostic. §5 → domain-agnostic (covers §4 deliverables). §10 → added "Why Not Just...?" section |
| `.tfw/PROJECT_CONFIG.yaml` | RES status `role: coordinator` → `role: researcher` |
| `.agent/workflows/tfw-plan.md` | Synced from `.tfw/workflows/plan.md` |
| `.agent/workflows/tfw-research.md` | Synced from `.tfw/workflows/research/base.md` |
| `.claude/commands/tfw-plan.md` | Synced from `.tfw/workflows/plan.md` |

## 2. Key Decisions

1. **Merged Step 6 (Final Checkpoint) into Step 6 (Synthesis).** The RES template no longer has a "Final Checkpoint" section (stage sections were removed), so the old Step 6 referencing it was dead. This also saved ~30 words needed to meet the 600-word budget.

2. **Compressed Step 3 (subfolder creation) via conventions ref.** Instead of repeating the file list and format in base.md, it now references `conventions.md §4 (Research subfolder)` where the canonical definition lives. Follows the ref-inside-step pattern (P12/D25).

3. **OODA ACT step changed from "Update RES" to "Update stage file."** Logical consequence of the subfolder architecture — during stages the agent writes to individual files, not the final RES.

## 3. Acceptance Criteria

- [x] `conventions.md` §8 shows Researcher for research/base.md
- [x] `conventions.md` §15 shows Researcher with correct Permitted/Forbidden
- [x] `conventions.md` §4 has research subfolder convention
- [x] `glossary.md` has Researcher entry, Coordinator no longer mentions research
- [x] `base.md` Role Lock = `RESEARCHER` (not Coordinator)
- [x] `base.md` has Step 0 (Resume Protocol)
- [x] `base.md` stages write to individual stage files in `research/`
- [x] `base.md` Step 6 = Synthesis + Hard Stop (was Step 7, renumbered after Final Checkpoint removal)
- [x] `plan.md` Step 6 hands off to Researcher, not self-switches
- [x] `templates/RES.md` has synthesis structure (no stage sections)
- [x] `templates/HL.md` §1 = Vision + Impact + stakeholder Quote
- [x] `templates/HL.md` §10 = has "Why Not Just...?" section
- [x] `templates/HL.md` §2, §5 = domain-agnostic
- [x] `PROJECT_CONFIG.yaml` RES role = researcher
- [x] Zero occurrences of "Coordinator (Research Mode)" in `.tfw/`
- [x] All 3 adapters synced
- [x] `base.md` ≤ 600 words (exactly 600)

## 4. Verification

- Lint (`echo "configure your lint command"`): N/A (markdown-only project)
- Tests (`echo "configure your test command"`): N/A
- Verify (`echo "configure your verify command"`): Passed
- "Coordinator (Research Mode)" grep in `.tfw/`: **0 results** ✅
- `wc -w base.md`: **600 words** ✅

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/conventions.md` | L129 | naming | §10.1, §10.2, §10 are numbered out of order (10.1 before 10) — inherited from previous tasks |
| 2 | `.tfw/glossary.md` | L66 | style | RESEARCH entry says "Optional — user can skip with confirmation" but this is now handled by plan.md Step 6, creating slight duplication |
| 3 | `.tfw/workflows/research/base.md` | — | style | Step numbering now 0-6 (was 1-7). Step 6 was previously "Final Checkpoint → Closure" — compressed well but the Closure concept (HL update recommendations) is now embedded in Synthesis, which works but future agents may not associate "Synthesis" with "writes HL recommendations" |

## 6. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | process | Researcher is the 4th role in TFW, extracted from Coordinator same pattern as Reviewer (TFW-8). 4 roles: Coordinator, Researcher, Executor, Reviewer | HL-TFW-24, this RF | High |
| 2 | convention | Research stage files live in `tasks/{ID}/research/` subfolder. File existence = stage completion (filesystem-level state machine). Files: briefing.md, gather.md, extract.md, challenge.md | conventions.md §4 | High |
| 3 | convention | RES template is a synthesis document — stage-level details stay in research/ subfolder files. Different structure to prevent copy-paste | HL-TFW-24 P3, RES.md template | High |
| 4 | process | base.md Step 0 (Resume Protocol) enables crash-resilient research by checking filesystem state: research/ exists? → which files? → RES exists? | base.md L12-16 | High |

---

*RF — TFW-24: Researcher Role & RES State Machine | 2026-04-04*
