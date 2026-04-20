# REVIEW — TFW-41 / Phase A: Templates and Conventions

> **Date**: 2026-04-20
> **Reviewer**: AI (separate review session)
> **Mode**: docs
> **RF reviewed**: `RF__PhaseA__templates_and_conventions.md`
> **TS used**: `TS__PhaseA__templates_and_conventions.md`
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`

---

## §1 Map Summary

Phase A is the foundation of TFW-41: it establishes the template and convention infrastructure that Phases B, C, D depend on. Three files modified: `TS.md` (full structural rewrite), `HL.md` (Phase Dependencies section added), `conventions.md` (4 anti-patterns appended to §14).

The RF is structurally complete: all 8 mandatory sections present. The key nuance to understand before judging is the section numbering shift — the executor inserted `## 3. Principles Check` (from AC-5), which shifted Acceptance Criteria from the example position (§4) to actual position (§5). This is a pre-existing conflict in the TS itself, acknowledged in RF §2 Key Decisions before any reviewer noted it.

---

## §2 Verify Summary

**Verification scope:** 3/3 files (100% — escalated from minimum 2).

| File | Verified | Finding |
|------|----------|---------|
| `.tfw/templates/TS.md` | ✅ | 84 lines (matches RF claim). All AC criteria satisfied against actual content. No code in AC section. Principles Check table present with correct columns. `[depends: AC-1]` example present. DoF section present. Cross-Phase Modifications section present. |
| `.tfw/templates/HL.md` | ✅ | 198 lines (matches RF claim). `### Phase Dependencies` subsection at correct location. Mermaid diagram template + dependency table both present. Multi-phase / omit instructions present. |
| `.tfw/conventions.md` | ✅ | 23 anti-patterns total (was 19 + 4 = 23, matches RF claim). 4 new patterns at lines 386-389, appended after existing 19. One-line prose format consistent with existing entries. |

All DoF gates passed. No discrepancies found.

The section-number deviation (AC-1 example says `## 4`, template has `## 5`) was assessed: the TS AC-1 criterion list does not require the *number* to be 4 — it requires the heading to be "Acceptance Criteria", AC-N pattern, Gate line, WHAT/HOW instruction, no code. All satisfied. Executor pre-documented this in Key Decision #1.

---

## §3 Judge Summary

**Universal checklist (6/6 ✅):** All AC items satisfied, no DoF triggered, all files present and matching, RF structure complete, observations present and structured, scope within budget.

**Docs-mode checklist (2/2 ✅):** Content quality — instructions are precise, domain-neutral, no unfilled placeholders. Source traceability — all RF claims link to TS ACs, execution observations, or direct file scans.

**HL §7 Principles (5/5 applicable ✅, 1 N/A):** Principles 1, 2, 4, 5, 6 enforced structurally in Phase A output. Principle 3 (Verify against fact) is Phase B scope (Pre-TS Gate) — legitimately N/A for Phase A.

**Issue register:** 2 informational items, both pre-documented by executor, no blocking issues.

---

## §4 Verdict

### ✅ APPROVE

**Rationale:**

1. **All 8 AC items verified** against actual file content. No gap between claimed and delivered.
2. **All 4 DoF hard-reject conditions** checked and not triggered.
3. **The numbering deviation** (AC → §5 instead of §4) is a well-reasoned structural decision, documented before review, and does not violate any verifiable TS criterion. The TS example code was illustrative; the criterion items are structural.
4. **Scope discipline**: 0 new files, 3 of 3 stated modifications made, no out-of-scope changes.
5. **Template quality**: The new `TS.md` template directly implements the TFW-41 vision — Requirements, not code. Domain-neutral. Gates over guidelines. An agent using this template will structurally produce better TSs.
6. **Conventions quality**: 4 new anti-patterns are precise, one-line, non-redundant with existing 19.

**Phase B may now proceed.** The pre-condition "Phase A ✅" is satisfied.

---

## §5 Tech Debt Collected

**RF Observations triage:**

| # | RF Obs | Promoted? | Severity | Rationale |
|---|--------|-----------|----------|-----------|
| 1 | `§4 Detailed Steps` was root cause of HD-16/C copy-paste — now resolved, recorded for trace | ❌ Not promoted | — | Historical trace item; no action needed. The issue is fixed by this phase. |
| 2 | Phase B should verify no workflow step references "§4 Detailed Steps" or "§5 Acceptance Criteria" by number | ✅ Promoted | Low | If workflow steps contain hardcoded section numbers, they will mismatch the new template. Phase B owns this but the risk should be tracked. |

**Tech Debt entry:**

```
TD-TFW41-A1 | Low | Workflow section-number references
After Phase A renumbered TS sections (Acceptance Criteria moved to §5, Technical Guidance to §6, etc.),
workflow files (handoff.md, plan.md, review.md) may reference old section numbers.
Phase B is assigned to verify and update workflows — this item tracks residual risk if Phase B misses specific references.
Source: RF TFW-41/PhaseA Observation #2.
```

---

## §6 Knowledge Workflows

- `tfw-docs`: **Pending** — Run after this REVIEW to update KNOWLEDGE.md §1-§3 with Phase A architectural decisions.
- `tfw-knowledge`: **Pending** — RF §6 contains 2 Fact Candidates (both Medium/High confidence) for consolidation.

> Both markers to be set to `Applied` after workflows complete → Task Board status → 📚 KNW → ✅ DONE (Phase A).

---

## §7 Fact Candidates (Reviewer)

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | philosophy | The structural conflict "AC-1 expected §4, but Principles Check insertion shifted to §5" reveals a meta-lesson: when writing TS for template-modification tasks, specify section **headings**, not section **numbers**, in AC items. Numbers are implementation details of the template itself. | Review observation | High |
| 2 | process | Phase A delivers a complete template rewrite with zero external dependencies and zero build steps. The absence of a lint/test gate is the correct decision for markdown-only phases — verify.md confirmed DoF gates served as the functional equivalent. Future reviewers of markdown-only phases should default to docs mode and use structural AC checks as the verification mechanism. | Review observation | High |

---

*REVIEW — TFW-41 / Phase A: Templates and Conventions | 2026-04-20*
