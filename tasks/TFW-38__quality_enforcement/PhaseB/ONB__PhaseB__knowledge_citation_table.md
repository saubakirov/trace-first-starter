# ONB — TFW-38 / Phase B: Knowledge Citation Table

> **Date**: 2026-04-15
> **Author**: Executor
> **Status**: 🟠 ONB — Answered
> **Parent HL**: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> **TS**: [TS Phase B](TS__PhaseB__knowledge_citation_table.md)

---

## 1. Understanding

Make Project Values citations traceable and verifiable across the Coordinator→Executor→Reviewer cascade. Currently agents claim "per D28" without links — could be hallucinated. After: HL §7.2 has a citation table with links (coordinator fills via full PV scan), ONB §7 has executor confirmation table (references HL §7.2), and verify.md has a link-resolution check section. Five files modified, zero new files.

## 2. Entry Points

| File | Current state | What changes |
|------|--------------|--------------|
| `.tfw/templates/HL.md` (L92-102) | §7 Principles → §7.1 Quality Contract → §8 Dependencies | Insert §7.2 Knowledge Citations between §7.1 and §8 |
| `.tfw/templates/ONB.md` (L29-37) | §6 Inconsistencies → cross-ref footer → closing | Insert §7 Knowledge Citations between §6 and footer |
| `.tfw/templates/review/verify.md` (L27-43) | Discrepancies → Checkpoint | Insert Knowledge Citations Verified between them; update Checkpoint |
| `.tfw/workflows/plan.md` (L36) | Step 3 item 4: "Check KNOWLEDGE.md..." | Replace with PV-scan instruction pointing to HL §7.2 |
| `.tfw/workflows/handoff.md` (L36) | Phase 1 item: "Inconsistencies between HL/TS/KNOWLEDGE.md and actual code" | Add citation-read instruction before it |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | TS Step 5 says to update plan.md Step 3 — the current Step 3 item 4 already reads: "Check KNOWLEDGE.md — scan Architecture Decisions, known conventions, and prior task findings. If any are relevant to this task, cite them in HL §4 (Phase Context). If none apply: write 'No applicable knowledge items.'" This references HL §4. The TS says the citation target is now HL §7.2 (not §4). Should I (a) replace item 4 entirely with the TS Step 5 text, or (b) amend it to keep the existing "scan Architecture Decisions" language but redirect to §7.2 + add PV Index reference? | **(a) Replace entirely.** The TS Step 5 text is the canonical version. It references PV Index from glossary.md, specifies full scan vs skim priorities, and targets §7.2. The old text was Phase A draft — Phase B supersedes it. Keep it clean: one instruction, one location. |
| 2 | TS Step 6 says to "Amend existing KNOWLEDGE.md instruction" in handoff.md Phase 1. The current handoff.md Phase 1 step 2 line 36 mentions KNOWLEDGE.md in the inconsistency check. The instruction is to add citation-reading before this line. Should this citation instruction be a new sub-bullet under step 2, or inserted as a separate numbered step before step 2? The TS shows a markdown snippet but doesn't specify structural placement within the numbered list. | **New sub-bullet under step 2.** Citation reading and inconsistency checking are both part of "understand the landscape" (Phase 1). Keep them grouped. Add the citation instruction as the first sub-bullet, existing inconsistency check becomes second sub-bullet. Don't create a new numbered step — keeps the outline clean. |

## 4. Recommendations (suggestions, not blocking)

1. **ONB section numbering shift.** Adding §7 to ONB.md shifts the cross-reference footer from after §6 to after §7. The footer has no §-reference so it's not breaking. But downstream users referencing "ONB §6" for inconsistencies will remain correct. Clean transition.

2. **HL.md §7.2 instruction text — consider adding glossary reference.** TS Step 2 text says "scan PV Index (glossary.md → Project Values)". I suggest adding a direct relative path reference: `(see glossary.md → Project Values → PV Index)` — making it explicit that the PV Index definition lives in glossary.md, not just a name to search for.

3. **verify.md Checkpoint consolidation.** The TS Step 4 says to "replace current KNOWLEDGE.md bullet" in the self-check. The current verify.md checkpoint has a KNOWLEDGE.md bullet (line 39-41). Replacing it with the expanded version (total/verified/hallucinations count) makes sense — this supersedes rather than extends. The old check ("contradictions with changes") is subsumed by the new one.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Adapter resync.** TS §3 lists 5 files but doesn't mention adapter copies. Based on Phase A/A.2 precedent, `tfw-plan.md` and `tfw-handoff.md` adapters need resync. This adds 2 more file modifications to the actual changeset (7 total from 5 canonical). Within scope budgets.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS says "Insert after §7.1 Quality Contract (line 101)"** — actual line 102 is `## 8. Dependencies`. Line 98-101 contain §7.1 Quality Contract. The insertion point is correct (after §7.1, before §8), the line number is approximate — will use content matching instead.

2. **TS says "Insert after §6 (Inconsistencies with Code), before the cross-references footer"** for ONB — accurate. ONB.md line 29: `## 6. Inconsistencies with Code`, line 32: cross-ref footer. Insertion point between lines 31 and 32.

3. **TS Step 5 references "plan.md Step 3 item 4"** — the current plan.md Step 3 has items numbered 1-5 (not labeled "item 4" explicitly, they're markdown numbered list). Item 4 (currently: "Check KNOWLEDGE.md — scan Architecture Decisions...") is indeed the target. Phase A already added this item — now we're enhancing it with the PV Index scan instruction.

> **Cross-references**: HL-TFW-38 §4 Phase B, D19, D28, D39. S8, S9.

---

*ONB — TFW-38 / Phase B: Knowledge Citation Table | 2026-04-15*
