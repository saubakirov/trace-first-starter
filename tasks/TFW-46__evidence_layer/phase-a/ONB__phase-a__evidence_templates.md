# ONB — TFW-46 / Phase A: Evidence Concept + Templates

> **Date**: 2026-07-07
> **Author**: Executor (Antigravity, Claude Opus 4.6)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-46](../HL-TFW-46__evidence_layer.md)
> **TS**: [TS Phase A](TS__phase-a__evidence_templates.md)

---

## 1. Understanding
Phase A establishes Evidence as a first-class concept in TFW by modifying conventions.md (§3, §12, §14) and three core templates (TS, RF, REVIEW stage files). The key design decisions from iter1-2 research are: "Evidence" as the term (D1), 4-status vocabulary VERIFIED/DEFERRED/BLOCKED/N/A (D2), separate §5 Evidence in RF with renumbering §5-8 → §6-9 (D5/D11), Evidence field in TS AC items parallel to Gate (D6/D10), Evidence Audit via judge.md check #7 + verify.md evidence section (D7/D12), and 5 anti-self-deception rules for §14 (D15). This phase is templates-and-conventions only — no workflow changes (Phase B), no glossary/adapters (Phase C).

## 2. Entry Points

| File | Why |
|------|-----|
| `.tfw/conventions.md` | §3 (add Evidence concept), §12 (honesty rules), §14 (anti-patterns) |
| `.tfw/templates/TS.md` | Add `Evidence:` field to AC items |
| `.tfw/templates/RF.md` | Insert §5 Evidence, renumber §5-8 → §6-9 |
| `.tfw/templates/review/judge.md` | Add check #7 (Evidence completeness) |
| `.tfw/templates/review/verify.md` | Add Evidence Verification section |
| `.tfw/templates/REVIEW.md` | Update §6 reference for renumbering |
| `.tfw/workflows/handoff.md` | Update RF section references (§5-8 → §6-9) |
| `.tfw/workflows/review.md` | Update Trust Protocol references |
| `.tfw/templates/HL.md` | Update Visual Sections table ref (RF §8 → §9) |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions | — |

## 4. Recommendations (suggestions, not blocking)

1. **Evidence concept placement in §3**: The TS says "Evidence is listed in the Visual Sections or Knowledge Capture Sections table" (AC-1 bullet 2). Evidence doesn't fit either — it's neither a visual section nor a knowledge capture section. It has its own cognitive mode (Observational/Verification) and its own per-template naming pattern (Evidence Plan / Evidence / Evidence Audit). I recommend adding a new **Evidence Sections (per-template)** table after Knowledge Input Sections, following the same D39 pattern. This keeps §3's structure clean.

2. **compilable_contract.md references**: The grep found 2 references in compilable_contract.md mentioning RF §6 and §5. These reference specific section *content* ("§6 FC Source column"), not section *numbers* in the RF template. After renumbering, RF §6 FC becomes §7 FC. The TS doesn't list compilable_contract.md in Affected Files, but AC-6 says "No stale references to old numbering remain in `.tfw/templates/` or `.tfw/workflows/`". The compilable_contract lives in `.tfw/` but is not a template or workflow. Recommend including it in the reference sweep anyway to avoid inconsistency.

3. **REVIEW.md §3 Judge table**: Currently has check #6 "RF completeness (§6-8 present)". After renumbering, this should read "§7-9 present". Since the REVIEW.md template mirrors the judge.md checklist, both need updating together.

4. **handoff.md step numbering note**: The TS §9 Cross-Phase Modifications says Phase B will add evidence collection as a new step. Phase A only updates reference numbers. I'll keep the current step numbering intact and only update section references within existing step descriptions.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **glossary.md references to RF sections**: The glossary mentions `RF §7 "Strategic Insights (Execution)"` (line 48) and `RF §8 Diagrams` is implicit in D39 references. These are glossary entries, not template/workflow files — out of scope per TS §2 (glossary = Phase C). But leaving stale refs in glossary while conventions.md is updated creates temporary inconsistency. This is acceptable since Phase C will fix it.

2. **CHANGELOG.md historical references**: Multiple CHANGELOG.md entries reference old RF §5, §6, §7, §8 numbers. Per TS §6 Technical Guidance and D11 from iter2: "CHANGELOG.md excluded (historical)." These are historical records and should NOT be updated. Confirming this interpretation.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS says 9 modified files**, Affected Files table lists exactly 9. Grep confirms these cover all active (non-historical) references. No inconsistency.

2. **TS AC-4 says "judge.md RF completeness check updated: §6-8 → §7-9"** — this is correct since RF renumbering shifts Fact Candidates (§6→§7), Strategic Insights (§7→§8), Diagrams (§8→§9). The current judge.md check #6 says "RF completeness (§6-8)" which should become "§7-9".

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | K1: README Values: Honesty Over Convincingness | ✅ | Applied — Evidence prevents confident-but-wrong RFs | Core motivation for the entire task |
| 2 | K2: README Values: Structural Enforcement | ✅ | Applied — Evidence artifacts as structural proof | Drives artifact-based design (D7, D15 R1) |
| 3 | K3: philosophy.md F4: Structural enforcement > format | ✅ | Applied — Evidence folder with artifacts > checkbox | Informs D16 folder convention |
| 4 | K4: philosophy.md F21: Explicit N/A pattern | ✅ | Applied — DEFERRED/N/A status vocabulary | Directly used in D2 vocabulary design |
| 5 | K5: philosophy.md F27: Observable progress | ✅ | Applied — Evidence artifacts in task folder | Supports evidence artifact storage |
| 6 | K6: process.md F14: Without YAML control | ✅ | Applied — Evidence statuses prevent fast-green | Supports D2 status vocabulary |
| 7 | K7: conventions.md §12: Never claim "run" outside session | ✅ | Applied — Evidence extends to require proof | Drives §12 extension in AC-5 |
| 8 | K8: conventions.md §14: RF before build/lint | ✅ | Applied — Analogous anti-pattern for evidence | Drives D15 R3 |
| 9 | K9: D41: Requirements-first TS with AC gates | ✅ | Applied — Evidence Plan extends AC gates | Evidence field parallel to Gate field |
| 10 | K10: D46: Trust Protocol in review | ✅ | Applied — Evidence Audit extends Trust Protocol | Drives D12 |
| 11 | K11: philosophy.md F13: Domain-agnostic | ✅ | Applied — No domain-specific examples in templates | Key constraint throughout |

No additional PV items found beyond coordinator's citations.

---

*ONB — TFW-46 / Phase A: Evidence Concept + Templates | 2026-07-07*
