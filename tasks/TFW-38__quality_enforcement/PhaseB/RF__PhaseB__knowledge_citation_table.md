# RF — TFW-38 / Phase B: Knowledge Citation Table

> **Date**: 2026-04-15
> **Author**: Executor
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> **TS**: [TS Phase B](TS__PhaseB__knowledge_citation_table.md)

---

## 1. What Was Done

### Modified Files
| File | Changes |
|------|---------|
| `.tfw/templates/HL.md` | Added §7.2 Knowledge Citations after §7.1 Quality Contract (lines 103-113). Table with PV Index scan instruction, 4-column format (Source, Item, How it applies), bootstrap note for new projects. |
| `.tfw/templates/ONB.md` | Added §7 Knowledge Citations after §6 Inconsistencies (lines 32-43). Executor-facing table: references HL §7.2, 5-column format (HL ref, Read?, Applied/N/A, Notes), NEW row support, bootstrap confirmation note. |
| `.tfw/templates/review/verify.md` | Added Knowledge Citations Verified section (lines 33-42) between Discrepancies and Checkpoint. Link resolution table (Artifact, Citation, Link resolves?, Item exists?). Updated Checkpoint self-check: replaced old KNOWLEDGE.md bullet with expanded citation verification (total/verified/hallucinations count). |
| `.tfw/workflows/plan.md` | Step 3 item 4: replaced "Check KNOWLEDGE.md" with "Scan Project Values (PV)" (lines 36-41). Full PV scan with priority tiers (full scan 1-4, skim 5-7), targets HL §7.2 table, includes bootstrap note. |
| `.tfw/workflows/handoff.md` | Phase 1 step 2: added citation-reading sub-bullet (lines 36-38) before KNOWLEDGE.md inconsistency check. Instructs executor to read HL §7.2, fill ONB §7, add NEW items coordinator missed. |
| `.agent/workflows/tfw-plan.md` | Adapter re-synced from `.tfw/workflows/plan.md`. |
| `.agent/workflows/tfw-handoff.md` | Adapter re-synced from `.tfw/workflows/handoff.md`. |

## 2. Key Decisions

1. **plan.md item 4: full replacement (not amendment).** Per coordinator answer Q1: old Phase A text was a draft, Phase B text is canonical. One instruction, one location — no legacy wording preserved.
2. **handoff.md: sub-bullet under step 2 (not new numbered step).** Per coordinator answer Q2: citation reading and inconsistency checking are both "understand the landscape" activities. Grouped together, not separated. Citation instruction placed as first knowledge-related item, directly before the existing KNOWLEDGE.md inconsistency bullet.
3. **verify.md: KNOWLEDGE.md bullet preserved + citation bullet added.** The old KNOWLEDGE.md self-check ("contradictions with changes documented?") was kept as a separate line. The new citation verification ("links resolve, items exist?") added below it. This preserves the contradiction check that existed before Phase B — citations and contradictions are different checks.
4. **ONB template: example row included.** Added a single example row with `{D-number or F-number from HL §7.2}` placeholder to show executors the expected format (per TS Step 3 example pattern).

## 3. Acceptance Criteria

- [x] HL template has §7.2 Knowledge Citations (after §7.1 Quality Contract)
- [x] ONB template has §7 Knowledge Citations (after §6 Inconsistencies)
- [x] review/verify.md has Knowledge Citations Verified section (links resolve check)
- [x] verify.md self-check counts total/verified/hallucination citations
- [x] plan.md Step 3 references PV Index from glossary.md
- [x] handoff.md Phase 1 instructs executor to read HL §7.2 → fill ONB §7
- [x] Cascade model enforced: coordinator scans (full), executor references (HL §7.2), reviewer verifies (links)
- [x] "No applicable knowledge items." documented as valid N/A (including bootstrap note for new projects)
- [x] Table name unified: "Knowledge Citations" in HL, ONB, and verify.md ("Knowledge Citations Verified" in verify.md — same base name, "Verified" = stage-specific qualifier)

## 4. Verification

- Lint: N/A (markdown files, no linter configured)
- Tests: N/A (no automated tests for workflow/template files)
- Verify: Manual — all 9 acceptance criteria verified via file inspection:
  - HL.md lines 103-113: §7.2 Knowledge Citations ✅
  - ONB.md lines 32-43: §7 Knowledge Citations ✅
  - verify.md lines 33-42: Knowledge Citations Verified ✅
  - verify.md lines 50-52: citation count in self-check ✅
  - plan.md lines 36-41: PV Index scan with glossary.md reference ✅
  - handoff.md lines 36-38: HL §7.2 → ONB §7 instruction ✅
  - Cascade: plan.md (coord full scan) → handoff.md (executor reads HL §7.2) → verify.md (reviewer verifies links) ✅
  - Bootstrap: HL.md L113, ONB.md L43 both have N/A wording ✅
  - Naming: "Knowledge Citations" unified across all 3 templates ✅
  - Adapter sync: tfw-plan.md + tfw-handoff.md match canonical ✅

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/templates/HL.md` | 103 | style | §7.2 uses `###` (H3) — same level as §7.1 Quality Contract. Consistent. But §7 itself is `##` (H2). If future §7.3 is added, the heading hierarchy stays clean (H2 → H3 → H3). |
| 2 | `.tfw/workflows/handoff.md` | 36 | style | Citation instruction is a `- ` bullet but uses multi-line continuation with leading spaces. Other bullets in the same list are single-line. Consistent with TS Step 6 formatting but visually different from sibling bullets. If future edits are needed, this multi-line format may be harder to match for string-based edits. |

## 6. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | philosophy | User chose full replacement over amendment for plan.md Step 3 item 4: "The TS text is the canonical version. The old text was Phase A draft — Phase B supersedes it. Keep it clean: one instruction, one location." Direct evidence: incremental amendments to the same instruction across phases produce confusing layered text. Clean replacement is preferred. | User answer Q1, TFW-38/B | High |
| 2 | process | User prefers grouping related concerns over structural separation: citation reading and inconsistency checking both go under "Analyze the task" (step 2) as sub-bullets, not as separate numbered steps. Rationale: "keeps the outline clean." Pattern: semantic grouping > numbering granularity. | User answer Q2, TFW-38/B | High |

## 7. Strategic Insights (Execution)

No strategic insights.

## 8. Diagrams

No diagrams.

---

*RF — TFW-38 / Phase B: Knowledge Citation Table | 2026-04-15*
