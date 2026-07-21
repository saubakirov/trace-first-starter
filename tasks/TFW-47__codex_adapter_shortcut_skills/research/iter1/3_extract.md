# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-47](../../HL-TFW-47__codex_adapter_shortcut_skills.md)
> Goal: Every completed task produces a mandatory `evidence/` folder with a structured EV template file.

## Configuration Space

Cross-referencing Gather's 4 dimensions. Pruning obviously contradictory combinations upfront (e.g., freeform narrative + per-AC rows). Showing viable configurations only.

| Config | D1: Structure depth | D2: AC coupling | D3: Proportionality | D4: Environment depth |
|--------|--------------------|-----------------|--------------------|----------------------|
| C1 | Sections (env + table + verdict) | Per-AC rows | Row-level N/A | OS + tools + timestamp |
| C2 | Sections (env + table + verdict) | Per-AC rows | Row-level N/A | + DB/runtime + deploy target |
| C3 | Flat table only | Per-AC rows | Row-level N/A | OS + tools + timestamp |
| C4 | Full report (env + per-AC sections + attachments) | Per-AC rows | Section-level optionality | + DB/runtime + deploy target |
| C5 | Sections (env + table + verdict) | Per-verification-act rows | Row-level N/A | OS + tools + timestamp |
| C6 | Minimal header + freeform | Freeform narrative | Single template, min bar | Freeform text block |
| C7 | Sections (env + table + verdict) | Per-AC rows | Single template, min bar = env + 1 row | + DB/runtime + deploy target |
| C8 | Template tiers (minimal/full) | Per-AC rows (full) / freeform (minimal) | Template tiers | OS + tools + timestamp |

## Findings

### E1: C1/C2 are the AFD-36 proof-of-concept extraction

AFD-36/A's §5 Evidence is structurally C1/C2 already:
- **Environment** = per-row (not header), but same info could be a header
- **Table** = per-AC rows with `# | AC | What was verified | Environment | Result | Artifact`
- **Verdict** = summary line at bottom
- **Environment depth** varies: some rows mention "JVM unit + PostgreSQL 16 Testcontainer + beta PostgreSQL" (C2-level), others just "H2 unit" (C1-level)

The working proof favors **C2** — environment depth should be flexible (some rows need DB versions, others don't), and a header block captures the common denominator (OS, tools, date).

### E2: C3 (flat table only) mirrors current RF §5

C3 is literally what's already in the RF template. Moving it unchanged to a separate file gains nothing except file existence. The EV file needs to add value over RF §5 — the value is the **environment header** and the **attachments index** that RF doesn't have room for.

This eliminates C3: if it's identical to RF §5, why create a separate file?

### E3: C4 (full report) is over-engineered

Per-AC *sections* (not rows) would mean HD-30/A's 11 ACs generate 11 markdown sections. AFD-36 showed 7 rows work fine in a table. Full sections add no information over table rows for most ACs.

Exception: complex ACs with multi-step verification (e.g., EXPLAIN ANALYZE plans spanning 40 lines). These are handled by the `Artifact` column pointing to files in `evidence/`, not by expanding the template.

### E4: C6 (minimal + freeform) defeats the purpose

HL §1: "structured template capturing real verification results." Freeform defeats structure. D52 established the 4-status vocabulary specifically to prevent hand-wavy claims. Freeform would regress to the current inline-RF problem.

### E5: C8 (template tiers) creates decision fatigue

Which tier to use? Agents will either always pick "minimal" (path of least resistance — the same reason 0/38 tasks created the folder) or require coordinator guidance (adds overhead). Single template with N/A rows is simpler and self-documenting.

### E6: C5 (per-verification-act) vs C1/C2 (per-AC)

Per-verification-act means one row per observation, which may combine multiple ACs ("deployed to beta — AC-3, AC-4, AC-5 all verified in one deploy"). This is what AFD-36 did with E6 covering AC-4 from a different angle than E4.

Trade-off: per-AC is more traceable (every AC gets explicit coverage), per-verification-act is more natural (one deploy = one observation). The table can handle both: AC column accepts "AC-3, AC-4" when a single verification covers multiple ACs.

**Resolution:** Per-AC is the primary structure, but the AC column allows comma-separated ACs when appropriate. This is C1/C2, not C5.

### E7: Non-obvious combination — C7 (single template with flexible minimum bar)

C7 combines sections structure (C1/C2 quality) with the simplest proportionality: no template tiers, no section optionality — just "fill what you verified, N/A what you didn't." The minimum bar (environment + 1 verification row) ensures even trivial tasks produce a non-empty file.

This is the **unexpected survivor**: it's simpler than C1/C2 (no "required vs optional sections" distinction) while maintaining structure. The environment header is always filled; the table always has at least one row.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| 8 configurations built from 4 dimensions | — |
| C3, C4, C6, C8 eliminated with reasons | — |
| C1/C2/C7 survive; C5 absorbed into C1/C2 | — |
| C7 = unexpected survivor (simplest viable) | — |
| AFD-36 = empirical proof for C2 structure | — |

**Sufficiency:**
- [x] External source used? (ISO 29119 structure validated C1/C2 environment+traceability)
- [x] Briefing gap closed? (Structure depth, AC coupling, proportionality, environment depth all resolved)
- [x] Configuration Space built from Gather dimensions? (8 configs from 4 dimensions)

Stage complete: YES
→ User decision: proceed to Challenge
