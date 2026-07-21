# HL — Phase A: Evidence Enforcement

> **Date**: 2026-07-17
> **Author**: Coordinator (Antigravity)
> **Status**: 📝 Phase HL
> **Parent HL**: [HL-TFW-47](../HL-TFW-47__codex_adapter_shortcut_skills.md)

---

## Context

> **Requires:** Independent
>
> **Key decisions from research:**
> - iter1 D1: File name `EV__{PREFIX}-{N}__{title}.md` (2-letter abbreviation)
> - iter1 D2: Structure = Environment header + per-AC evidence table + Verdict
> - iter1 D4: No template tiers — proportionality via row count
> - iter1 D6: Table columns identical to RF §5
> - iter1 D7: Attachments section optional (binary artifacts)
> - OQ1: RF §5 becomes one-line pointer to EV file
> - D16 (TFW-46): REVOKED — `evidence/` was optional, now mandatory
>
> **Files to read before writing TS:**
> 1. conventions.md §3 (Evidence Sections) — current pipeline definition
> 2. conventions.md §4 (Task Numbering) — folder structure to update
> 3. conventions.md §14 (Anti-patterns) — evidence anti-patterns
> 4. iter1/RES.md — all template design decisions
> 5. templates/TS.md — current TS template
> 6. templates/RF.md — current RF §5 template
> 7. workflows/handoff.md — Step 11 evidence collection

## Deliverables

1. Create `.tfw/templates/evidence/EV.md` — evidence template with Environment header, per-AC table, Verdict line, optional Attachments index.
2. Update conventions.md §4 — add `evidence/` as mandatory subfolder (single-phase and multi-phase).
3. Update conventions.md §3 — remove optional language, add folder creation requirement.
4. Update `.tfw/templates/TS.md` — add `## Evidence Artifacts` section.
5. Update `.tfw/templates/RF.md` §5 — replace inline table with pointer to EV file.
6. Update `.tfw/workflows/handoff.md` Step 11 — add explicit "create evidence/ folder" step.
7. Update KNOWLEDGE.md — revoke D16, extend D52 with mandatory folder.

---

*HL — Phase A: Evidence Enforcement | 2026-07-17*
