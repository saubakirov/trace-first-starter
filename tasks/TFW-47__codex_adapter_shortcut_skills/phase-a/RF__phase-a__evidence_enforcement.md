# RF — TFW-47 / Phase A: Evidence Enforcement

> **Date**: 2026-07-17
> **Author**: Executor (Antigravity)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-47](../HL-TFW-47__codex_adapter_shortcut_skills.md)
> **TS**: [TS Phase A](TS__phase-a__evidence_enforcement.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|------------|
| `.tfw/templates/evidence/EV.md` | Structured evidence template: Environment header (5 fields), per-AC evidence table (6 columns), Verdict summary, optional Attachments index |
| `tasks/TFW-47.../phase-a/ONB__phase-a__evidence_enforcement.md` | Onboarding report — 0 blocking questions |
| `tasks/TFW-47.../phase-a/evidence/EV__phase-a__evidence_enforcement.md` | Evidence file for this phase |

### Modified Files
| File | Changes |
|------|---------| 
| `.tfw/conventions.md` | §3: mandatory folder language + EV file in pipeline table + template reference. §4: 2 EV naming rows in artifact table + evidence subfolder section + `evidence/` in multi-phase structure. §14: anti-pattern wording strengthened |
| `.tfw/templates/TS.md` | Added `### Evidence Artifacts` subsection after AC items with guidance and example table |
| `.tfw/templates/RF.md` | §5 replaced: inline evidence table → pointer to EV file + verdict summary |
| `.tfw/workflows/handoff.md` | Step 11 rewritten: 6 numbered substeps for evidence folder creation and population. Skip condition removed. Phase 3 §5 description updated |
| `KNOWLEDGE.md` | D53 added: evidence enforcement decision with D16 revocation |
| `README.md` | Task board: TFW-47 status → 🟢 RF, ONB link added |

## 2. Key Decisions

1. **D53 as new decision, not D52 edit**: D52 captures the original Evidence Layer design (TFW-46). D53 captures the enforcement extension. This preserves the trace: the reader sees D52 (concept introduced) → D53 (enforcement applied). Editing D52 inline would hide the evolution.

2. **Evidence Artifacts as TS subsection (### not ##)**: Placed as `### Evidence Artifacts` within §5 scope rather than a new top-level `## 5.1`. Avoids renumbering §6-§9 while keeping it logically connected to AC items.

3. **§3 pipeline table updated with 2 new rows**: Added explicit EV file row and changed RF row from "Observational / Verification" to "Summary / Reference". This makes the cognitive mode distinction clear: the executor's observational work lives in EV, RF §5 is just a pointer.

4. **Evidence subfolder section added to §4**: Parallels the existing "Research subfolder" and "Review subfolder" sections. Each mandatory subfolder type gets its own documentation block.

## 3. Acceptance Criteria

- [x] AC-1: EV template exists with Environment header, per-AC table, Verdict, Attachments, naming pattern
- [x] AC-2: conventions.md §3 mandatory language, §4 folder structure + naming, §14 anti-pattern update
- [x] AC-3: TS template Evidence Artifacts subsection with guidance and example
- [x] AC-4: RF template §5 pointer format, verdict preserved, inline table removed
- [x] AC-5: handoff.md Step 11 with create/copy/fill substeps, no skip condition
- [x] AC-6: KNOWLEDGE.md D53 added, D16 revocation explicit

## 4. Verification

- Lint: N/A — methodology documents, no code
- Tests: N/A — no test suite for markdown
- Verify: `grep -c "evidence/" conventions.md` = 6 hits (gate ≥3 ✅). No "optional" or "only when binary" language found ✅

## 5. Evidence

> **Cognitive mode:** Observational verification — evidence lives in the EV file, not inline.
> RF §5 is a summary pointer. Full evidence details: `evidence/EV__phase-a__evidence_enforcement.md`.

See [EV file](evidence/EV__phase-a__evidence_enforcement.md) for evidence details.

Evidence verdict: 0/6 VERIFIED, 0 DEFERRED, 0 BLOCKED, 6 N/A

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/conventions.md` | 40 | naming | `compilable_contract.md` listed in §2 Required Artifacts — references `.tfw/compilable_contract.md` but no EV entry added to compilable contract Source Manifest. Phase D should consider adding EV to the compilation source list |
| 2 | `.tfw/project_config.yaml` | 20-28 | naming | `tfw.templates` section doesn't list the EV template path. This is consistent with how research stage templates aren't listed either, but worth noting for future config sync |
| 3 | `.tfw/templates/review/verify.md` | — | naming | References "RF §5 artifacts" — still valid because RF §5 now points to EV, and artifact paths in EV resolve the same way. No change needed, but reviewer should be aware |

## 7. Fact Candidates

No fact candidates.

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

```
BEFORE (D52 — TFW-46):
  Coordinator → TS §5 Evidence field
  Executor   → RF §5 inline table (0/38 tasks did this)
  Reviewer   → review/verify.md checks RF §5

AFTER (D53 — TFW-47/A):
  Coordinator → TS §5 Evidence field + Evidence Artifacts section
  Executor   → evidence/EV__{...}.md (structured file, always created)
               RF §5 = pointer to EV file + verdict summary
  Reviewer   → review/verify.md checks EV file artifacts
```

---

*RF — TFW-47 / Phase A: Evidence Enforcement | 2026-07-17*
