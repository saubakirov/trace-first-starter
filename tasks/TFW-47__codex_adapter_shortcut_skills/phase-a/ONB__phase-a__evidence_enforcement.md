# ONB — TFW-47 / Phase A: Evidence Enforcement

> **Date**: 2026-07-17
> **Author**: Executor (Antigravity)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-47](../HL-TFW-47__codex_adapter_shortcut_skills.md)
> **TS**: [TS Phase A](TS__phase-a__evidence_enforcement.md)

---

## 1. Understanding

Phase A makes `evidence/` a mandatory subfolder in every TFW task directory. The core deliverable is a structured EV template (`.tfw/templates/evidence/EV.md`) with environment header, per-AC evidence table, verdict summary, and optional attachments index. This replaces inline RF §5 evidence tables — RF §5 becomes a pointer to the EV file. Six files total: 1 new (EV template), 5 modified (conventions.md §3/§4/§14, TS template, RF template, handoff.md, KNOWLEDGE.md). The change revokes D16 (optional) and extends D52 (mandatory folder).

## 2. Entry Points

| File | Purpose |
|------|---------|
| `.tfw/conventions.md` L107-119 | §3 Evidence Sections — pipeline definition |
| `.tfw/conventions.md` L121-228 | §4 Task Numbering — folder structures |
| `.tfw/conventions.md` L403-432 | §14 Anti-patterns — evidence items |
| `.tfw/templates/TS.md` L39-61 | §5 Acceptance Criteria — Evidence field |
| `.tfw/templates/RF.md` L39-49 | §5 Evidence — inline table to replace |
| `.tfw/workflows/handoff.md` L85-90 | Step 11 — evidence collection |
| `KNOWLEDGE.md` L83 | D52 row |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions | — |

All design decisions resolved by iter1 research (D1-D7). OQ1 (RF §5 relationship) decided in TS: pointer format. All affected files and sections are well-defined. TS is clear and complete.

## 4. Recommendations (suggestions, not blocking)

1. **EV naming table in conventions.md §4**: The artifact naming table (L127-139) currently has 11 rows. I'll add 2 rows (single-phase EV, phase EV) — consistent with existing pattern.

2. **conventions.md §3 Evidence Sections table update**: The per-template table (L114-119) currently references "RF §5 Evidence" for executor output. After this change, executor output moves to `evidence/EV file`. I'll update the table entry to reference both the EV file (primary) and RF §5 pointer (secondary).

3. **§14 anti-pattern wording**: Current item "Executor marks evidence VERIFIED without artifact reference (file path or inline output)" at L428 can be strengthened — artifact references should now point to `evidence/` folder paths. I'll update the wording to reflect mandatory evidence folder.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Review templates not in scope but reference RF §5**: `review/verify.md` and `review/judge.md` reference "RF §5 artifacts." TS explicitly puts this out of scope ("they reference artifact paths — EV file path works the same way"). Confirmed: the pointer in RF §5 means artifact paths still resolve. No action needed in Phase A.

2. **project_config.yaml templates section**: The `tfw.templates` section in `project_config.yaml` (L20-28) lists template paths. The EV template lives in a subfolder (`evidence/EV.md`), not at templates root. This is consistent with how `research/` stage templates work (`.tfw/templates/research/*.md`). No config update needed per TS scope.

## 6. Inconsistencies with Code (spec vs reality)

1. **No inconsistencies found.** The TS accurately reflects the current state of all target files. Conventions.md §3 uses "optional" language for evidence folder (as described). RF template §5 has the inline table. Handoff.md Step 11 has the skip condition. All match TS description.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | KC1: D52 (Evidence Layer) | ✅ | Applied — the EV template reuses D52's 4-status vocabulary and table columns | Foundation being extended |
| 2 | KC2: D16 (optional evidence/) | ✅ | Applied — revocation is the primary purpose of this phase | Being revoked |
| 3 | KC3: F5 (workflows = source of truth) | ✅ | N/A — Phase A doesn't create adapters | Codex-relevant, Phase B-C |
| 4 | KC4: D15 (thin adapters) | ✅ | N/A — same as KC3 | Codex-relevant |
| 5 | KC5: D50 (adapter sync) | ✅ | N/A — Phase A only | |
| 6 | KC6: F3 (naming creates behavior) | ✅ | Applied — EV naming follows D28 (2-letter abbreviation, consistent with HL/TS/RF) | |
| 7 | KC7: F4 (agents = IDE systems) | ✅ | N/A — not directly relevant to evidence template design | |
| 8 | KC8: conventions.md §12 (VERIFIED needs artifact ref) | ✅ | Applied — EV template's Artifact column enforces this structurally | |
| 9 | KC9: conventions.md §14 (anti-pattern: VERIFIED without artifact) | ✅ | Applied — mandatory folder makes the anti-pattern structurally impossible | |

No new PV items found that coordinator missed.

---

*ONB — TFW-47 / Phase A: Evidence Enforcement | 2026-07-17*
