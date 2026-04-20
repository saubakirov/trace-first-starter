# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF__PhaseC__research_templates.md](../RF__PhaseC__research_templates.md)
> TS: [TS__PhaseC__research_templates.md](../TS__PhaseC__research_templates.md)
> Mode: docs

## Understanding

Phase C of TFW-41 embeds Zwicky's General Morphological Analysis into the three research stage templates (Gather, Extract, Challenge) using TFW-native terminology — no methodology names exposed to researchers. The executor added three new template sections (`## Dimensions`, `## Configuration Space`, `## Consistency Check`) before `## Findings` in each respective template, wired them with a cross-stage dependency (Extract's column headers reference Gather's Dimension names), added a 5-sentence connecting paragraph in `research/base.md` Step 5, and documented the Zwicky origin in `conventions.md §14.1` (maintainer-only scope). 5 file modifications, 0 new files.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1: gather.md has `## Dimensions` before `## Findings`; ≥3 alternatives; no "recommended"; checkpoint item | RF §3 AC-1: all items checked ✅ | ✅ |
| AC-2: extract.md has `## Configuration Space` before `## Findings`; references Gather dims; no eval; overflow protection | RF §3 AC-2: all items checked ✅ | ✅ |
| AC-3: challenge.md has `## Consistency Check` before `## Findings`; pairwise instruction; unexpected survivors | RF §3 AC-3: all items checked ✅ | ✅ |
| AC-4: research/base.md Step 5 has dimensional analysis paragraph ≤6 lines; graceful degradation; no GMA terms | RF §3 AC-4: all items checked ✅ | ✅ |
| AC-5: conventions.md has origin note; 5 terms mapped; explicitly maintainer-facing | RF §3 AC-5: all items checked ✅ | ✅ |
| DoF: No "Zwicky"/"GMA"/"morphological" in researcher-facing templates | RF §4: grep 0 results | ✅ |
| DoF: Configuration Space references Gather dimensions | RF §8 diagram + extract.md reviewed | ✅ |
| Technical Guidance: template sizes ~35-40 lines; base.md ~135 lines | RF §4: gather 40, extract 42, challenge 47, base 131/132 lines | ✅ (challenge 47 justified) |
| Technical Guidance: thread ≤8 lines (DoF) | RF §3 AC-4: 3 sentences, 1 paragraph — well within budget | ✅ |

## Deviations from TS

1. **challenge.md: 47 lines vs 35-40 target.** RF §2 Decision 2 and §4 justify: 4 subsections (incompatible pairs table, surviving configs table, unexpected survivors field, graceful degradation note) require more space. TS §6 guidance was advisory ("~35-40 lines each"). Within DoF tolerance — no DoF triggered.
2. **base.md: 131 lines (RF says 132 in §1, actual file = 131).** Minor discrepancy in RF's own self-reporting. Actual file verified: 131 lines. Net delta from 129 is +2, not +3. Not a DoF violation — TS said "adds ~5-6 lines" and the actual thread is 5 lines. Line count discrepancy is in RF metadata only.
3. **Conventions insertion as `### 14.1` (subsection) not a free-standing paragraph.** ONB §4 pre-announced this recommendation; no objection was required. Outcome consistent with TS §6 guidance ("or as a subsection of §14 / new §14.1").

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES
