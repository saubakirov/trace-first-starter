# Review Stage 1: Map — TFW-41 / Phase A

> **Reviewer**: AI (separate review session)
> **Date**: 2026-04-20
> **Mode**: docs

---

## Task Identity

| Field | Value |
|-------|-------|
| Task ID | TFW-41 |
| Phase | A — Templates and Conventions |
| TS file | `TS__PhaseA__templates_and_conventions.md` |
| RF file | `RF__PhaseA__templates_and_conventions.md` |
| Parent HL | `HL-TFW-41__execution_quality_gates.md` |
| Executor | AI (autonomous session, 2026-04-20) |
| Status claimed | 🟢 RF — Complete |

---

## What This Phase Was Supposed to Do

Phase A is the **foundation phase** of TFW-41. It establishes the template infrastructure that all subsequent phases (B, C, D) depend on. Three specific changes:

1. **Rewrite `TS.md`** — Replace procedural §4 (Detailed Steps) with requirements-first structure: Principles Check (§3), Acceptance Criteria (§5), Technical Guidance (§6), Definition of Failure (§7), Cross-Phase Modifications (§9). The core shift: TS must say WHAT, not HOW.
2. **Add Phase Dependencies to `HL.md`** — Mermaid diagram + dependency table as `### Phase Dependencies` subsection in §4, enabling any coordinator to write any Phase TS without reading all prior research.
3. **Add 4 anti-patterns to `conventions.md` §14** — Formalizing observations from HD-16/HD-18 into the canonical anti-pattern list.

**Why it matters:** This phase directly addresses Problems 4, 5, 7 from HL §2 (code-in-TS, plan≠fact drift) and HD-16/HD-18 root causes. All subsequent phases reference the new template structure.

---

## RF Structure Assessment

| RF Section | Present | Notes |
|-----------|---------|-------|
| §1 What Was Done | ✅ | New/modified files table with detailed change descriptions |
| §2 Key Decisions | ✅ | 5 decisions, including the §4↔§5 numbering conflict |
| §3 Acceptance Criteria | ✅ | All 8 AC items checked, with notes on deviations |
| §4 Verification | ✅ | Line counts, DoF gate checks |
| §5 Observations | ✅ | 2 items in structured table |
| §6 Fact Candidates | ✅ | 2 items |
| §7 Strategic Insights | ✅ | Declared empty with rationale |
| §8 Diagrams | ✅ | Declared N/A with rationale |

All mandatory RF sections are present. No structural gaps.

---

## Key Deviation to Understand

The RF declares a numbering shift: AC-1 expected `## 4. Acceptance Criteria` but the final template has `## 5. Acceptance Criteria` because AC-5 (Principles Check) was inserted as `## 3. Principles Check`, shifting all subsequent sections. The executor documented this in §2 (Key Decisions #1) and §3 (notes under AC-1 and AC-4). The section **headings** match the TS intent; only **numbers** drifted. This is a pre-existing structural conflict in the TS itself, acknowledged in Key Decision #1.

---

## Self-Check Gate

- [x] RF file read completely before writing this map
- [x] TS file read — scope, ACs, DoF known
- [x] HL file read — vision, principles, phase context known
- [x] Key deviation (numbering conflict) understood before judging
- [x] No judgment made yet — pure mapping

---

*map.md — TFW-41 / Phase A review | 2026-04-20*
