# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase A](../RF__phase-a__evidence_enforcement.md)
> TS: [TS Phase A](../TS__phase-a__evidence_enforcement.md)
> Mode: docs

## Understanding

The executor created a structured EV (Evidence) template at `.tfw/templates/evidence/EV.md` and updated 5 framework files to make `evidence/` a mandatory subfolder in every task directory. The core change is: evidence moves from inline RF §5 text to a dedicated file in `evidence/`, RF §5 becomes a pointer. D16 (optional evidence folder from TFW-46) was revoked via a new D53 decision in KNOWLEDGE.md, not by editing D52 — preserving the decision trace.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1: EV template with Environment, per-AC table, Verdict, Attachments, naming | RF §3: AC-1 ✅ — "EV template exists with Environment header, per-AC table, Verdict, Attachments, naming pattern" | ✅ |
| AC-2: conventions.md §3 mandatory, §4 folder + naming, §14 anti-pattern | RF §3: AC-2 ✅ — "conventions.md §3 mandatory language, §4 folder structure + naming, §14 anti-pattern update" | ✅ |
| AC-3: TS template Evidence Artifacts subsection | RF §3: AC-3 ✅ — "TS template Evidence Artifacts subsection with guidance and example" | ✅ |
| AC-4: RF template §5 pointer, verdict preserved, inline removed | RF §3: AC-4 ✅ — "RF template §5 pointer format, verdict preserved, inline table removed" | ✅ |
| AC-5: handoff.md Step 11 create/copy/fill substeps, no skip | RF §3: AC-5 ✅ — "handoff.md Step 11 with create/copy/fill substeps, no skip condition" | ✅ |
| AC-6: KNOWLEDGE.md D53, D16 revocation | RF §3: AC-6 ✅ — "KNOWLEDGE.md D53 added, D16 revocation explicit" | ✅ |

## Deviations from TS

1. **D53 as new decision (not D52 edit)**: TS said "revoke D16, extend D52." Executor created D53 instead of editing D52 inline. RF §2 Key Decision #1 explains the rationale: "preserves the trace: reader sees D52 (concept) → D53 (enforcement)." This is a positive deviation — better trace discipline than the TS prescribed.

2. **Evidence Artifacts as `###` not `##`**: TS AC-3 said "new section added after §5." Executor placed it as a subsection (`###`) within §5 scope. RF §2 Key Decision #2 explains: avoids renumbering §6-§9. Reasonable.

3. **§3 pipeline table got 2 new rows**: Not explicitly called for in TS, but a natural consequence of adding EV file as a new artifact type. The cognitive mode distinction (EV = Observational/Verification, RF = Summary/Reference) is correct and well-explained.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES
