# ONB — TFW-24: Researcher Role & RES State Machine

> **Date**: 2026-04-04
> **Author**: Executor
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-24](HL-TFW-24__res_state_machine.md)
> **TS**: [TS__TFW-24](TS__TFW-24__res_state_machine.md)

---

## 1. Understanding

Extract the Researcher as a 4th standalone role (alongside Coordinator, Executor, Reviewer) with its own Role Lock. Introduce a `research/` subfolder convention where each research stage writes its own file — file existence = state completion. Add Step 0 (Resume Protocol) to `base.md`. Convert `RES.md` template from stage-based to synthesis-based format. Update `HL.md` template §1 to Vision/Impact/Quote and §2/§5 to domain-agnostic phrasing. Update `plan.md` with Researcher handoff + Hard Stop. Sync 3 adapter files.

## 2. Entry Points

| File | Key Lines/Sections |
|------|--------------------|
| `.tfw/conventions.md` | §4 (naming), §8 (workflows table), §15 (role lock table) |
| `.tfw/glossary.md` | Coordinator role definition (~L97-101), Roles section (~L89-118) |
| `.tfw/workflows/research/base.md` | L7-8 (Role Lock), L12+ (Steps 1-7) |
| `.tfw/workflows/plan.md` | L64-74 (Step 6: RESEARCH decision) |
| `.tfw/templates/RES.md` | L50-102 (Stage sections), L127-155 (Closure) |
| `.tfw/templates/HL.md` | L9-12 (§1), L14-16 (§2), L42-44 (§5), L79+ (§10) |
| `.tfw/PROJECT_CONFIG.yaml` | L73-76 (RES status) |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions | — |

## 4. Recommendations (suggestions, not blocking)

1. **TS Step 4 (RES.md) says "Remove stage sections... Replace with synthesis structure" but lists 6 sections.** Current RES.md has Briefing, Hypotheses, Decisions, Open Questions, 3 Stage sections, Final Checkpoint, Closure (with HL Recommendations, FC, Conclusion). TS's synthesis structure = Decisions, Open Questions, Hypotheses, HL Update Recommendations, Fact Candidates, Conclusion. I will keep the header + Research Context + Briefing reference as TS instructs (L148: "Keep header... Briefing section stays in RES").

2. **TS HL §1 uses "Vision" as heading but existing TFW-24 HL uses "Goal & Value".** The template change is to the *template* not retroactive — understood, will apply to `templates/HL.md` only.

3. **TS Step 2 specifies Step 4 Briefing → `research/briefing.md` and Step 5 stages → individual files, but the OODA Stage Loop and Stage Checkpoint sections in base.md reference "Update RES" (L50) and "Update RES — Decisions and Open Questions" (L55).** After the change, these should reference stage files instead. I will update the OODA ACT step and Stage Checkpoint accordingly.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Word count tight.** base.md is currently 518 words (by my count of the 103-line file). Adding Step 0 (~30 words), subfolder instruction (~30 words), and Synthesis rewrite (~40 words) = ~618. May need to tighten existing text slightly to stay ≤600.

2. **Three-adapter sync.** TS lists 3 cp commands. `.agent/workflows/tfw-research.md` is a copy of `research/base.md`, `.agent/workflows/tfw-plan.md` and `.claude/commands/tfw-plan.md` are copies of `plan.md`. All three currently identical to their sources — confirmed by reading.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS §4 Step 1 says `conventions.md §4 (Artifact Naming)`** — in the actual file, §4 is titled "Task Numbering" (L74). Research subfolder convention fits here as an extension of the naming/folder rules. No conflict, just noting the title difference.

---

*ONB — TFW-24: Researcher Role & RES State Machine | 2026-04-04*
