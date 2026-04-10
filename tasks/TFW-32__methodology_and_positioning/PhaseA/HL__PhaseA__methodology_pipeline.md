# HL — TFW-32 / Phase A: Methodology Pipeline Fixes

> **Date**: 2026-04-10
> **Author**: AI (Coordinator)
> **Status**: 📝 HL_DRAFT — Awaiting review
> **Parent HL**: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)

---

## 1. Vision

The docs-vs-knowledge collision is fixed. `tfw-docs` owns KNOWLEDGE.md §1-§3 + TECH_DEBT.md (Combination: explicit→explicit). `tfw-knowledge` owns `knowledge/*.md` + KNOWLEDGE.md §4 index (Externalization: tacit→explicit). The pipeline has a visible `📚 KNW` status between REV and DONE, with REVIEW markers that make knowledge capture trackable. No workflow writes to the same section as another.

**Impact:** After this phase, (1) agents never refuse to work because "already captured," (2) every task explicitly tracks whether docs and knowledge steps were completed, (3) the orphaned §0 Philosophy moves to its canonical home in `knowledge/philosophy.md`.

> "Documentation captures what exists. Knowledge captures what only humans know. Mixing them in one workflow breaks both."

## 2. Current State (As-Is)

### 2.1 docs-vs-knowledge collision

| Aspect | Current state | Problem |
|--------|---------------|---------|
| tfw-knowledge Phase 4 | Writes to KNOWLEDGE.md §1 (Architecture Decisions) and §2 (Key Artifacts) | Encroaches on tfw-docs territory |
| tfw-docs | Writes to KNOWLEDGE.md §1-§3 + TECH_DEBT.md | After tfw-knowledge runs, docs agent says "already captured" and refuses |
| SECI mapping | tfw-docs = Combination (explicit→explicit). tfw-knowledge = Externalization (tacit→explicit) | Different cognitive processes — validated by Nonaka-Takeuchi theory (RES1 D1) |

**Evidence of collision (user report):** Agent refused to run tfw-docs after tfw-knowledge had already updated §1/§2. This is a blocking workflow bug.

### 2.2 No knowledge status in pipeline

Current pipeline:
```
... → 🔍 REV → ✅ DONE
```

Knowledge collection happens via Knowledge Gate in plan.md — gates the NEXT task, not current. Result: 21 RF files with zero project facts recorded (TFW-18 analysis).

### 2.3 KNOWLEDGE.md §0 orphaned

§0 "Philosophy & Principles" is set by user once, never updated by any workflow. Content already exists in `knowledge/philosophy.md` (14 facts). Duplication with no updater.

## 3. Target State (To-Be)

### 3.1 Result Visualization

```
BEFORE (collision):
  tfw-knowledge Phase 4 ──writes──→ KNOWLEDGE.md §1/§2 ←──writes── tfw-docs
                                     (COLLISION)

AFTER (clear boundaries):
  tfw-docs ──writes──→ KNOWLEDGE.md §1 Architecture + §2 Key Artifacts + §3 Legacy
                        (exclusive: Combination, explicit→explicit)

  tfw-knowledge ──writes──→ knowledge/*.md (verified facts) + KNOWLEDGE.md §4 (index only)
                             (exclusive: Externalization, tacit→explicit)

  KNOWLEDGE.md §0 ──→ DELETED (content verified in knowledge/philosophy.md)
```

```
PIPELINE (before → after):

  BEFORE: ... → 🔍 REV → ✅ DONE

  AFTER:  ... → 🔍 REV → 📚 KNW → ✅ DONE
                            ↑
                            tfw-docs (always) → recommends tfw-knowledge (conditional)
```

```
REVIEW MARKERS:
  ## 4. Traces Updated
    ...
    - [ ] tfw-docs: {Applied — updated Sections X, Y / N/A (minor)}
    - [ ] tfw-knowledge: {Applied / N/A / Deferred to batch}
```

## 4. Deliverables

1. **Fix tfw-knowledge Phase 4** — strip §1/§2 writes. Phase 4 scope = staleness check + KNOWLEDGE.md §4 update + knowledge_state.yaml update only
2. **Fix tfw-docs scope** — clarify: KNOWLEDGE.md §1-§3 + TECH_DEBT.md. Add explicit "Out of scope: knowledge/ topic files, §4 index"
3. **Remove KNOWLEDGE.md §0** — verify every principle in §0 has a corresponding fact in knowledge/philosophy.md before removing
4. **Update KNOWLEDGE.md §4 header** — renumber sections (§0 removed → §1-§3 become §0-§2, §4 becomes §3)... **No** — renumbering is costly (every reference breaks). Instead: remove §0 content, keep §1-§4 numbering intact
5. **Add `📚 KNW` status** — conventions.md §5, PROJECT_CONFIG.yaml tfw.statuses, glossary.md
6. **Add REVIEW markers** — REVIEW template §4 Traces Updated: `tfw-docs` and `tfw-knowledge` markers
7. **Update review.md workflow** — Step 6 references KNW status and docs/knowledge markers
8. **Update tfw-docs workflow** — add orchestration note: "After tfw-docs, recommend tfw-knowledge if Fact Candidates exist in RF/REVIEW/RES"
9. **Update tfw-knowledge workflow** — header: Output = `knowledge/*.md` + KNOWLEDGE.md §4 + knowledge_state.yaml (remove §1/§2 mention)

## 5. Definition of Done (DoD)

- ✅ 1. tfw-knowledge Phase 4 does NOT write to KNOWLEDGE.md §1 or §2
- ✅ 2. tfw-docs has explicit scope: KNOWLEDGE.md §1-§3 + TECH_DEBT.md
- ✅ 3. KNOWLEDGE.md §0 content removed (verified against knowledge/philosophy.md — zero information loss)
- ✅ 4. `📚 KNW` status exists in conventions.md, PROJECT_CONFIG.yaml, glossary.md
- ✅ 5. REVIEW template has `tfw-docs` and `tfw-knowledge` markers in §4 Traces Updated
- ✅ 6. review.md workflow references KNW transition and markers
- ✅ 7. Pipeline diagram in conventions.md and glossary.md shows KNW between REV and DONE
- ✅ 8. README.md status legend updated with KNW

## 6. Definition of Failure (DoF)

- ❌ 1. tfw-docs and tfw-knowledge still write to the same KNOWLEDGE.md sections
- ❌ 2. KNW status added but no workflow references it (orphan status)
- ❌ 3. §0 removed but information lost (principle not in knowledge/philosophy.md)
- ❌ 4. Renumbering cascades to other files (scope creep)

**On failure:** Revert workflow changes, keep §0 until verified.

## 7. Principles

1. **SECI separation** — docs = Combination (explicit→explicit). Knowledge = Externalization (tacit→explicit). Different cognitive processes → different workflows.
2. **Exclusive territory** — each workflow writes to specific sections. No overlap.
3. **Verify before delete** — §0 removal only after 1:1 mapping to knowledge/philosophy.md confirmed.
4. **No renumbering** — removing §0 means deleting content, not shifting all section numbers.

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| TFW-32 Master HL approved | ✅ |
| RES1-RES4 complete | ✅ |
| knowledge/philosophy.md exists (14 facts) | ✅ To verify |

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| §0 removal loses information | Medium | High | Pre-check: map each P1-P10 to knowledge/philosophy.md fact |
| Adding KNW breaks existing task flow | Low | Medium | KNW is skippable (N/A marker). Existing DONE tasks not affected |
| Workflow changes introduce new desyncs | Low | Medium | Budget check: all changes within scope budget |

## 10. RESEARCH Case

Research complete at master HL level (4 iterations). No additional research needed for Phase A — all decisions (D1, D3, D6, D7, D8) are validated.

---

*HL — TFW-32 / Phase A: Methodology Pipeline Fixes | 2026-04-10*
