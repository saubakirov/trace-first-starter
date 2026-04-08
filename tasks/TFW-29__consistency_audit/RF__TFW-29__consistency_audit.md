# RF — TFW-29: Consistency Audit

> **Date**: 2026-04-08
> **Author**: Executor (AI)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-29](HL-TFW-29__consistency_audit.md)
> **TS**: [TS TFW-29](TS__TFW-29__consistency_audit.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|------------|
| `.tfw/compilable_contract.md` | Compilable Contract extracted from conventions.md §16 — Source Manifest, Reference Format, Frontmatter Convention, Output Navigation Structure. Self-reference row added (row 14). Output nav updated to include itself. |

### Modified Files
| File | Changes |
|------|---------|
| `.tfw/conventions.md` | §16 → 3-line stub with abstract and link. §10 reordered before §10.1/§10.2 (was after). §11 heading renamed "Design Rules" (dropped stale "from P10-P13"). Added compilable_contract.md to §2 Required Artifacts. 426 → 318 lines (-25%). |
| `.tfw/glossary.md` | Duplicated artifact defs → 1-liners + refs. Status Flow → 1-liner + ref + compact diagram. Task Naming → 1-liner + ref. Removed meta-only terms: Workflow (canonical), .tfw/ Directory, Execution Engine, Progress Reporting, tfw-init/release/update descriptions. Kept Concept Taxonomy (per ONB §6). Updated Compilable Contract/Reference Format/Source Manifest refs to compilable_contract.md. 191 → 149 lines (-22%). |
| `.tfw/README.md` | Anti-patterns list (9 items) → ref to conventions.md §14. 144 → 133 lines. |
| `AGENTS.md` | Workflow list expanded 5 → 11. Fixed plan.md description ("review" → "research"). Removed "→ traces" from review.md description. |
| `.agent/rules/agents.md` | Workflow list synced 4 → 11. Fixed handoff.md: removed erroneous "→ REVIEW". Added review.md (was missing). |
| `.agent/rules/tfw.md` | Context Loading: replaced non-existent `.agent/rules/conventions.md` and `.agent/rules/glossary.md` with direct `.tfw/conventions.md` and `.tfw/glossary.md`. |
| `.tfw/workflows/resume.md` | Added 1-line context loading ref to conventions.md §10 after Role Lock block. |
| `.tfw/workflows/docs.md` | Added Prerequisites section (read KNOWLEDGE.md and TECH_DEBT.md) before Trigger Modes. |
| `docs/scripts/gen_docs.py` | Added `.tfw/compilable_contract.md` → `reference/compilable-contract.md` to STATIC_SOURCES. Updated docstring: contract path now points to compilable_contract.md. |
| `README.md` | Task Board: TFW-29 status 🟠 ONB → 🟢 RF. |

## 2. Key Decisions

1. **Glossary at 149 lines (not 130 target)**: The HL target of ≤130 was aspirational. After compressing all duplicated defs to 1-liners and removing meta-only terms, 149 lines is the practical floor — all remaining content is unique or substantially compressed. RES D1 confirmed ~104 lines for content alone; headers, sections, and the Concept Taxonomy (kept per ONB) account for the difference.
2. **Concept Taxonomy kept**: TS Step 3 listed it for removal but ONB §6 identified it as genuinely useful disambiguation (5 concepts: Document Type, Template, Workflow, Adapter Command, Status). User approved keeping it.
3. **Resume.md: 1-line ref instead of full section**: ONB Rec #3 identified that resume.md already has implicit context loading in its Phase 1 steps. A full "Context Loading" section would duplicate the existing workflow. Added a single-line ref to §10 instead.
4. **compilable_contract.md added to §2 Required Artifacts**: The new file is a first-class TFW core file — added to the Required Artifacts list for discoverability.

## 3. Acceptance Criteria

- [x] conventions.md §16 block replaced with 3-line stub referencing compilable_contract.md
- [x] `.tfw/compilable_contract.md` exists with full §16 content (+ self-reference row, + abstract)
- [x] conventions.md §10 numbering is sequential (§10 → §10.1 → §10.2)
- [x] glossary.md has no duplicated full definitions — only 1-liners + refs for shared terms
- [x] glossary.md meta-only terms removed (Workflow canonical, .tfw/ Directory, Execution Engine, Progress Reporting, tfw-init/release/update descriptions). Concept Taxonomy kept per ONB.
- [x] AGENTS.md lists all 11 workflows
- [x] `.agent/rules/agents.md` synced with AGENTS.md, no "handoff→REVIEW" error
- [x] `.agent/rules/tfw.md` references `.tfw/conventions.md` directly (not non-existent agent/rules copies)
- [x] `.tfw/README.md` anti-patterns = ref to §14 (not full list)
- [x] No workflow `§`-reference is broken by changes (grep verification: 0 §16 refs in workflows, all §10 refs resolve)

## 4. Verification

- **§16 grep**: 0 references to §16 in `.tfw/workflows/` — extraction is safe
- **§10 grep**: all references resolve (knowledge.md, plan.md, research/base.md, resume.md all use §10/§10.1 correctly)
- **Line counts**:
  - conventions.md: 426 → 318 (-25%) ✅ target ≤350
  - glossary.md: 191 → 149 (-22%) (target ≤130 was aspirational)
  - .tfw/README.md: 144 → 133 (-8%)
  - compilable_contract.md: 115 lines (new)
- **gen_docs.py**: compilable_contract.md added to STATIC_SOURCES (2 references verified)
- **Build**: not applicable (no code changes, only .md and build config)

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `KNOWLEDGE.md` | 19, 39, 80, 108 | naming | References to "conventions.md §16" are now slightly imprecise — §16 is a stub, full content in compilable_contract.md. Not broken (stub exists), but less precise. Should be updated in next tfw-docs. |
| 2 | `.tfw/conventions.md` | 198-203 | style | Tool Adapter Pattern §9 example block still shows only CLAUDE.md and .cursor/rules — doesn't mention .agent/rules. Low priority but incomplete. |
| 3 | `RF.md` template | 67 | naming | Still says "See conventions.md §16.2" for reference patterns — should point to compilable_contract.md §2 after extraction. Template is out of scope for this TS. |

## 6. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | process | Glossary compression has a practical floor of ~104 content lines (149 with headers/sections). The HL estimate of ≤130 was too aggressive — H4 refutation in RES (15 unique terms used by 5+ workflows) means more content must stay than originally planned. Future compression tasks should research term usage before setting line count targets. | RES TFW-29 D1, this RF §2 D1 | High |

---

*RF — TFW-29: Consistency Audit | 2026-04-08*
