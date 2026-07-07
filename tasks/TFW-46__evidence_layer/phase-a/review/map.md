# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase A](../RF__phase-a__evidence_templates.md)
> TS: [TS Phase A](../TS__phase-a__evidence_templates.md)
> Mode: code

## Understanding

Phase A established Evidence as a first-class TFW concept. The executor: (1) added an "Evidence Sections" subsection to conventions.md §3 defining the concept, status vocabulary (VERIFIED/DEFERRED/BLOCKED/N/A), and the three-role pipeline (Coordinator designs → Executor collects → Reviewer audits); (2) added an `Evidence:` field to TS template AC items parallel to `Gate:`; (3) inserted a new §5 Evidence section in the RF template with a structured table and renumbered §5-8 → §6-9; (4) extended judge.md with check #7 (Evidence completeness) and verify.md with an Evidence Verification section; (5) added 5 anti-self-deception anti-patterns to conventions.md §14 and an evidence honesty rule to §12; (6) updated cross-file references across 12 files for the renumbering, including 2 files (compilable_contract.md, knowledge.md) beyond the original 9 in the TS affected files list.

Key decisions: Evidence Sections as a standalone §3 subsection (not merged into Visual or Knowledge tables), HL §11 cross-ref update (§6→§7) for semantic correctness, 2 out-of-scope files updated to prevent stale references in build tooling.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1: Evidence concept in conventions.md §3 | Evidence Sections subsection with status vocabulary, role pipeline, per-template table. No domain-specific examples | ✅ |
| AC-2: Evidence field in TS template AC items | `Evidence:` field added after `Gate:`, instruction block with grammar options, MAY-deviate noted | ✅ |
| AC-3: §5 Evidence in RF template + renumber | §5 Evidence with table + verdict line. §5→§6, §6→§7, §7→§8, §8→§9. Internal cross-refs updated | ✅ |
| AC-4: Evidence audit in review stage templates | judge.md check #7 added, verify.md Evidence Verification section added with table, checkpoints updated | ✅ |
| AC-5: Anti-self-deception rules in §12/§14 | §12 extended, 5 anti-patterns added to §14, all domain-agnostic | ✅ |
| AC-6: Cross-file reference updates | 9 TS-listed files + 2 additional. Grep confirms 0 stale references in templates/ and workflows/ | ✅ |

## Deviations from TS

1. **compilable_contract.md** updated (RF §6 FC → §7 FC) — outside TS §4 affected files list. Executor documented as K3 deviation with rationale (prevents stale ref in build tooling). Reasonable.
2. **knowledge.md** updated (RF §7 → §8 Strategic Insights) — inside `.tfw/workflows/` so arguably in AC-6 scope ("No stale references... in `.tfw/templates/` or `.tfw/workflows/`"). Not a true deviation.
3. **README.md** Task Board updated — standard housekeeping, not a deviation.
4. 12 files modified vs 9 in TS. 3 extra: compilable_contract.md (deviation), knowledge.md (in scope), README.md (housekeeping). Within scope budgets.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES
