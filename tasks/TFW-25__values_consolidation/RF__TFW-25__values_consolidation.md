# RF — TFW-25: Values & Principles Consolidation

> **Date**: 2026-04-04
> **Author**: Executor (AI)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-25](HL-TFW-25__values_consolidation.md)
> **TS**: [TS-TFW-25](TS__TFW-25__values_consolidation.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|------------|
| `tasks/TFW-25.../ONB__TFW-25__values_consolidation.md` | Executor onboarding report |

### Modified Files
| File | Changes |
|------|---------| 
| `.tfw/README.md` | §Values rewritten: 5→8 items. Added "Traces Over Code", "Structural Enforcement", "Naming Creates Behavior". Renamed "Determinism and Safety" → "Honesty Over Convincingness" (rewrote from rules list to genuine value statement). Enriched "Candor" with P9 coordinator mindset |
| `KNOWLEDGE.md` | §0: 14→7 principles (removed P4, P6, P10-P14). §3: 35→13 Legacy items (removed 22 pre-TFW-22 resolved items, added 1 TFW-25 item). §4 Tech Stack: removed entirely. §5→§4: renumbered, updated fact counts. P1 source updated `§Thesis`→`§Values` |
| `knowledge/convention.md` | 12→6 facts. Removed F4 (checkpoint fields), F6 (Config Sync Registry scope), F8 (§3.1 domain-agnostic), F9 (filesystem state machine), F10 (RES = synthesis), F12 (stage templates). Old F5→F4, F7→F5, F11→F6. Updated §5→§4 cross-ref |
| `knowledge/process.md` | 10→5 facts. Removed F2 (knowledge ≠ docs), F3 (scan conversation for FCs), F8 (crash → gate skipping), F9 (4 roles), F10 (resume protocol). Old F4→F2, F5→F3, F6→F4, F7→F5. Updated §5→§4 cross-ref |
| `knowledge/philosophy.md` | Updated §5→§4 cross-ref only. F4 kept as-is (contains unique user quote) |
| `knowledge/constraint.md` | Updated §5→§4 cross-ref only |
| `.tfw/conventions.md` | Added `### Design Rules (from P10-P13)` subsection under §11 Quality Standard with 4 compressed rules: token density, inline enforcement, DNA/library, progressive disclosure |
| `README.md` | Task board: TFW-25 status → `🟢 RF`, added TS/ONB links |

## 2. Key Decisions

1. **Design Rules placement**: Inserted under `## 11) Quality Standard` as a `###` subsection rather than creating a new `## 16)` section. These are quality-adjacent design constraints — keeping them in §11 is more natural than creating a separate section.
2. **philosophy/F4 kept as-is**: TS said "compress F4 (will be in README values)" but F4 contains a unique user quote (`«Дело не в формате, дело в структурности процесса»`) not present in README Values. Kept without compression per HL principle "Promote up, don't duplicate → if fact has unique content, keep it."
3. **§5→§4 renumbering propagated to all 4 topic files**: Cross-references in knowledge/ files pointed to KNOWLEDGE.md §5. After §4 Tech Stack removal, the Project Facts section became §4. Fixed in all files.
4. **Legacy: removed 22 items (not 18)**: TS said remove 18, but the actual content had 23 pre-TFW-22 items (TS miscounted Naming Rules and Pattern B items as TFW-22+ era, they're TFW-19/21 era). Kept all TFW-22 through TFW-24 items (11) + added 1 TFW-25 item = 13 Legacy items total.

## 3. Acceptance Criteria

- [x] AC-1: `.tfw/README.md` §Values has exactly 8 values: Traces, Candor, Completeness, Honesty, Structural Enforcement, Naming, SSOT, Portability
- [x] AC-2: `KNOWLEDGE.md` §0 has exactly 7 principles (P1, P2, P3, P5, P7, P8, P9)
- [x] AC-3: `KNOWLEDGE.md` §3 has 13 Legacy items (all TFW-22+, plus 1 TFW-25 consolidation entry)
- [x] AC-4: `KNOWLEDGE.md` §4 Tech Stack section removed
- [x] AC-5: `KNOWLEDGE.md` §4 (was §5) fact counts updated (6/5/4/3 = 18 total)
- [x] AC-6: `knowledge/convention.md` has exactly 6 facts (renumbered)
- [x] AC-7: `knowledge/process.md` has exactly 5 facts (renumbered)
- [x] AC-8: `.tfw/conventions.md` contains P10-P13 content (Design Rules subsection under §11)
- [ ] AC-9: KNOWLEDGE.md total ≤120 lines → **138 lines**. Overrun from Architecture Decisions table (D1-D33 = 34 rows). See §2 below.
- [x] AC-10: No dead cross-references (grep verified: all knowledge/ files updated §5→§4)
- [x] AC-11: Adapters NOT in scope (Phase B)

### AC-9 deviation explanation
KNOWLEDGE.md is 138 lines, exceeding ≤120 target by 18 lines. The Architecture Decisions table (§1) contains 33 decisions across 34 rows — this is 68 lines including table markup. The pruning removed ~40 lines (§0 shrunk by 10, §3 shrunk by 22, §4 removed = 10). Target assumed more compression in §1 and §2, which are outside TS scope. The prunable content (§0, §3, §4) is fully processed.

## 4. Verification

- Line count: `wc -l KNOWLEDGE.md` → 138 lines (down from 179, target ≤120)
- Fact counts: `grep -c "^| F" knowledge/*.md` → convention:6, process:5, philosophy:4, constraint:3 (total: 18)
- P# count: `grep "| P[0-9]" KNOWLEDGE.md` → 7 principle rows in §0 + 1 legacy mention in §3
- Dead refs: `grep "§5" knowledge/*.md` → 0 matches (all updated to §4)
- Values count: README.md has 8 `### ` entries under §Values and Principles

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `KNOWLEDGE.md` | 39-75 | perf | §1 Architecture Decisions table (D1-D33) is 34 rows, most with long rationale text. This is the main driver of KNOWLEDGE.md exceeding 120-line target. Candidate for compression in a future task |
| 2 | `.tfw/templates/KNOWLEDGE.md` | — | style | Template still references `## 5. Project Facts` — should be updated to `## 4.` to match live KNOWLEDGE.md post-pruning |

## 6. Fact Candidates

> Reviewing conversation — user said "Continue" with no additional direction. No new strategic knowledge emerged from this execution-only session.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | convention | "Honesty Over Convincingness" replaces "Determinism and Safety" as TFW's safety value. Key reframe: confidence without correctness is the deadliest failure mode. Implementation rules (no fabrication, no CL bypass) remain in conventions.md §12 | RES R7, HL §3 | High |

---

*RF — TFW-25: Values & Principles Consolidation | 2026-04-04*
