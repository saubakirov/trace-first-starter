# TS — TFW-41 / Phase D: Glossary and Adapter Sync

> **Date**: 2026-04-20
> **Author**: Coordinator (AI)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)

---

## 1. Objective

Sync glossary and tool adapters with all changes from Phases A, B, and C. Add 14 new terms to `glossary.md` covering execution gates (Phase A/B) and dimensional analysis (Phase C). Sync Antigravity adapter workflows with modified source workflows. This phase completes TFW-41 — after it, all templates, workflows, glossary, and adapters reflect the new quality gate model.

## 2. Scope

### In Scope
- Modify `glossary.md` — add 14 new terms
- Sync `.agent/workflows/` adapter files with modified source workflows (handoff, plan, review, research)

### Out of Scope
- Template changes (Phase A — done)
- Workflow changes (Phase B — done)
- Research template changes (Phase C — done)
- VERSION bump (separate `/tfw-release` after all phases complete)

## 3. Principles Check

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P2 | Requirements, not implementation | AC-1 | Glossary entries describe WHAT terms mean, not implementation details |
| P6 | Domain-agnostic by default | AC-1 | All definitions use domain-neutral language |

## 4. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/glossary.md` | MODIFY | Add 14 new terms |
| `.agent/workflows/tfw-handoff.md` | MODIFY | Sync with `.tfw/workflows/handoff.md` |
| `.agent/workflows/tfw-plan.md` | MODIFY | Sync with `.tfw/workflows/plan.md` |
| `.agent/workflows/tfw-review.md` | MODIFY | Sync with `.tfw/workflows/review.md` |
| `.agent/workflows/tfw-research.md` | MODIFY | Sync with `.tfw/workflows/research/base.md` |

**Budget:** 0 new files, 5 modifications. Defaults: max 14 files, max 8 new, max 1200 LOC.

## 5. Acceptance Criteria

### AC-1: Glossary — 14 new terms

All terms introduced in Phases A, B, and C are documented in `glossary.md` with concise, self-contained definitions.

**Execution gate terms (from Phases A/B):**
- [ ] **Acceptance Criteria (TS)** — TS §5 section defining WHAT results should achieve with verifiable gates
- [ ] **Technical Guidance** — TS §6 section providing reference context, not implementation instructions
- [ ] **Definition of Failure (TS)** — TS §7 section with hard reject conditions for RF
- [ ] **Principles Check** — TS §3 table mapping HL §7 principles to specific AC items with gates
- [ ] **AC Dependency Annotation** — `[depends: AC-X]` syntax in TS §5 marking prerequisite relationships between AC items
- [ ] **Execution Loop** — Self-verification cycle where executor checks prerequisite AC gates before implementing dependent ACs. Triggered by `[depends]` annotations.
- [ ] **Pre-TS Gate** — Coordinator reads RF of latest completed phase before writing next phase TS
- [ ] **Pre-RF Gate** — Executor opens RF template and reads section headings before writing RF
- [ ] **Session Naming** — Step 0 convention: name session as `Role | Task-ID | Phase` at workflow start
- [ ] **Phase Dependencies** — HL §4 section (mermaid + table) visualizing phase order, shared files, and parallel execution options

**Dimensional analysis terms (from Phase C):**
- [ ] **Dimension** (Research) — independent decision factor identified during Gather stage, with ≥3 alternatives
- [ ] **Configuration Space** (Research) — cross-reference table in Extract, combining Gather dimensions into viable configurations
- [ ] **Consistency Check** (Research) — pairwise elimination in Challenge, removing incompatible configurations
- [ ] **Surviving Configuration** (Research) — configuration that passes all pairwise consistency checks

Gate: Read `glossary.md` → all 14 terms present, each has a concise definition

### AC-2: Adapter sync — Antigravity workflows  [depends: AC-1]

Adapter files in `.agent/workflows/` must match their source workflows in `.tfw/workflows/`.

- [ ] `tfw-handoff.md` content matches `.tfw/workflows/handoff.md`
- [ ] `tfw-plan.md` content matches `.tfw/workflows/plan.md`
- [ ] `tfw-review.md` content matches `.tfw/workflows/review.md`
- [ ] `tfw-research.md` content matches `.tfw/workflows/research/base.md`
Gate: Diff each adapter file against its source → no content differences (metadata/frontmatter may differ)

## 6. Technical Guidance

> Reference material, not instructions. Executor MAY deviate with justification in RF.

- **Glossary structure:** terms are grouped by concept area (Execution Modes, Artifact Types, Knowledge Terms, etc.). Execution gate terms fit best as a new `## Execution Gates` section. Dimensional analysis terms fit best as a new `## Research — Dimensional Analysis` section. Alternatively, group with existing `## RESEARCH` section.
- **Glossary length:** currently 197 lines, 12960 bytes. Adding 14 terms at ~2 lines each = ~28 lines → target ~225 lines.
- **Glossary definition style:** single paragraph per term. References use `→ conventions.md §N` or `→ workflow.md Step N` format. See existing entries for pattern.
- **Adapter sync pattern:** adapters in `.agent/workflows/` are exact copies of `.tfw/workflows/` source files. The sync is a file copy, not a merge. Phase B RF confirms: handoff.md 161 lines, plan.md 153 lines, review.md 153 lines. Phase C RF confirms: research/base.md 132 lines.
- **Phase C observation (from RF §5):** `briefing.md` doesn't reference Dimensions section. This is a Phase D-scope candidate but low priority — dimensions are naturally discovered during Gather, not pre-planned in briefing.

## 7. Definition of Failure

- ❌ Any of the 14 terms missing from glossary → reject RF
- ❌ Any glossary definition uses domain-specific examples (code, CSS, API) → reject RF
- ❌ Any adapter file differs from its source workflow after sync → reject RF

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Glossary becomes too long / loses scannability | Group terms under clear section headings. Keep definitions to 1-2 sentences each. |
| Adapter sync misses a file | AC-2 lists all 4 adapters explicitly. Executor checks each. |

## 9. Cross-Phase Modifications (multi-phase only)

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `.tfw/glossary.md` | No other phase modifies glossary | Phase D owns glossary exclusively |
| `.agent/workflows/tfw-handoff.md` | Phase B modified source `.tfw/workflows/handoff.md` | Adapter must reflect Phase B changes |
| `.agent/workflows/tfw-plan.md` | Phase B modified source `.tfw/workflows/plan.md` | Adapter must reflect Phase B changes |
| `.agent/workflows/tfw-review.md` | Phase B modified source `.tfw/workflows/review.md` | Adapter must reflect Phase B changes |
| `.agent/workflows/tfw-research.md` | Phase C modified source `.tfw/workflows/research/base.md` | Adapter must reflect Phase C changes |

> **Cross-references**: HL-TFW-41 §4 Phase D, DR11 (native terminology), Phase A RF (TS section numbers), Phase B RF (workflow line counts, step renumbering), Phase C RF (§14.1 terminology origin, briefing.md observation).

---

*TS — TFW-41 / Phase D: Glossary and Adapter Sync | 2026-04-20*
