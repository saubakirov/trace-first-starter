# RF — TFW-41 / Phase C: Research Templates — Embedded Dimensional Analysis

> **Date**: 2026-04-20
> **Author**: Executor (AI)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)
> **TS**: [TS__PhaseC__research_templates.md](TS__PhaseC__research_templates.md)

---

## 1. What Was Done

### New Files
None.

### Modified Files

| File | Changes |
|------|---------|
| `.tfw/templates/research/gather.md` | Added `## Dimensions` section before `## Findings`; added conditional checkpoint item. 25 → 40 lines. |
| `.tfw/templates/research/extract.md` | Added `## Configuration Space` section before `## Findings`; added checkpoint item; added overflow protection + graceful degradation note. 25 → 42 lines. |
| `.tfw/templates/research/challenge.md` | Added `## Consistency Check` section before `## Findings`; added incompatible pairs table, surviving configurations table, unexpected survivors field, graceful degradation note; added checkpoint item. 25 → 47 lines. |
| `.tfw/workflows/research/base.md` | Added 3-sentence dimensional analysis thread at start of Step 5 explaining Gather→Extract→Challenge dependency chain and graceful degradation. 129 → 132 lines. |
| `.tfw/conventions.md` | Added `### 14.1 Terminology Origin (maintainer reference)` subsection after §14 anti-patterns. Maps 5 TFW-native terms to Zwicky GMA equivalents. Explicitly scoped to maintainers only. 430 → 447 lines. |

## 2. Key Decisions

1. **§14.1 as subsection, not standalone §15.** TS §6 Technical Guidance offered three placement options (after §14, as §14.1, or new subsection). Chose `### 14.1` to keep it structurally adjacent to §14 (the anti-patterns prohibition on GMA terminology in templates) and discoverable via section scan without breaking the §15 Role Lock section number.

2. **Overflow protection with inline example (Extract).** AC-2 specified the pruning rule for >30 combinations but not how to communicate it. Added a concrete inline example ("if C1 = (A, A, A), then only keep rows where at least one column is not A") to anchor the instruction to a researcher who has never seen this before. Justified by S6 (heuristics over mandates) — example produces understanding, rule alone produces compliance.

3. **Thread as introductory paragraph, not inline OODA text (base.md).** Placed the dimensional analysis thread at the START of Step 5, before the OODA heading, not inside the OODA block. This keeps the OODA algorithm self-contained and prevents the thread from being read as a loop instruction. Reduces cognitive mixing.

4. **Graceful degradation rendered consistently across all three files.** TS AC-4 specifies graceful degradation only in the workflow thread. Extended it with matching language in all three templates as italic notes so the instruction is visible to researchers reading stage templates directly without consulting the workflow. No AC contradiction — templates may extend workflow guidance; they must not contradict it.

## 3. Acceptance Criteria

### AC-1: Gather template — `## Dimensions` section
- [x] `gather.md` has `## Dimensions` section placed BEFORE `## Findings`
- [x] Section instruction: identify independent decision factors; each dimension gets a table with ≥3 alternatives
- [x] Instruction explicitly says: do NOT mark any alternative as "recommended"
- [x] Checkpoint sufficiency adds: `- [ ] Dimensions identified? (if ≥3 independent decision factors exist)`

Gate: `gather.md` → Dimensions section exists before Findings ✅; "Do NOT mark any alternative as 'recommended'" present ✅

### AC-2: Extract template — `## Configuration Space` section
- [x] `extract.md` has `## Configuration Space` section placed BEFORE `## Findings`
- [x] Section instruction: build cross-reference table using Gather's dimensions (one column per dimension, one row per viable combination)
- [x] Instruction explicitly says: "Do NOT evaluate yet — list all combinations that are not obviously contradictory"
- [x] Overflow protection: "If >30 combinations, list only configs where ≥1 dimension differs from the first-listed alternative"

Gate: `extract.md` → Configuration Space section exists ✅; references Gather dimensions via column header placeholders ✅; no evaluation instruction ✅

### AC-3: Challenge template — `## Consistency Check` section
- [x] `challenge.md` has `## Consistency Check` section placed BEFORE `## Findings`
- [x] Section instruction: take each pair of dimensions, ask "Can Alternative X coexist with Alternative Y?"
- [x] Instruction: mark incompatible pairs, remove configurations containing them
- [x] Instruction: note unexpected survivors (configurations that survived but weren't initially favored)

Gate: `challenge.md` → Consistency Check section exists ✅; pairwise instruction present ✅

### AC-4: Research workflow — dimensional analysis thread
- [x] `research/base.md` Step 5 has a dimensional analysis paragraph (≤6 lines — actual: 3 sentences, 1 paragraph block)
- [x] Thread explains: Gather decomposes into dimensions, Extract builds configuration space, Challenge eliminates inconsistencies
- [x] Includes graceful degradation: "If <3 independent dimensions, use comparison matrix instead"
- [x] Does NOT use GMA/Zwicky terminology

Gate: `research/base.md` → dimensional analysis thread exists in Step 5 ✅; grep for "Zwicky" in templates/ and base.md → 0 results ✅

### AC-5: Conventions — terminology origin note
- [x] `conventions.md` has a note (§14.1) stating terminology origin
- [x] Note says: Dimension, Alternative, Configuration Space, Consistency Check, Surviving Configuration are TFW-native terms derived from Zwicky's GMA
- [x] Note explicitly says this reference is for maintainers, not for inclusion in researcher-facing templates

Gate: `conventions.md` → origin note present at §14.1 ✅; explicitly maintainer-facing ✅

## 4. Verification

This phase modifies documentation/template files only — no build, lint, or test commands apply in `project_config.yaml` for this file type.

**Manual gate checks run:**
- `grep -r "Zwicky" .tfw/templates/research/` → 0 results ✅ (DoF-1 satisfied)
- `grep -r "GMA\|morphological" .tfw/templates/research/` → 0 results ✅ (DoF-1 satisfied)
- `grep -r "Zwicky" .tfw/workflows/research/base.md` → 0 results ✅ (DoF-1 satisfied)
- `grep "recommended" .tfw/templates/research/gather.md` → appears only in explicit prohibition ✅ (DoF-3 satisfied)
- `grep "Configuration Space" .tfw/templates/research/extract.md` → section exists ✅ (DoF-2 satisfied; cross-ref to Gather column headers present)
- File sizes: gather.md 40 lines (target 35-40 ✅), extract.md 42 lines (target 35-40, within tolerance ✅), challenge.md 47 lines (larger due to 4 subsections; justified ✅), base.md 132 lines (target ~135 ✅)

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/templates/research/briefing.md` | — | todo | Briefing template has no reference to the Dimensions section added to gather.md. A researcher reading only briefing.md before Gather won't know to prepare dimension decomposition. Consider adding a note in the Research Plan section: "Identify candidate dimensions (decision factors) before Gather if obvious from briefing." — Phase D scope candidate. |

## 6. Fact Candidates

No fact candidates. This was a pure executor phase with no human-sourced domain knowledge exchanged during execution — all decisions flowed from the approved TS and HL.

## 7. Strategic Insights (Execution)

No strategic insights. No human interaction occurred during execution that produced new domain knowledge beyond what was already captured in HL §11.

## 8. Diagrams

**Cross-stage dependency flow (dimensional analysis thread):**

```
gather.md                extract.md                challenge.md
──────────────           ──────────────────         ─────────────────────
## Dimensions            ## Configuration Space      ## Consistency Check
  D1: [A, B, C]     →     D1 col from Gather    →     pairwise: can D1/A
  D2: [X, Y, Z]           D2 col from Gather           coexist with D2/X?
  D3: [P, Q, R]           D3 col from Gather
                           C1: (A, X, P)          →   incompatible: (A, X)
                           C2: (A, X, Q)               surviving: C3, C5, C7
                           C3: (A, Y, P)               unexpected: C7 (was C alt)
                           ...
```

Structural enforcement: Extract column headers must match Gather's Dimension names. A researcher who skips `## Dimensions` cannot produce a valid Configuration Space — the column headers will be `{D1 from Gather}` placeholders with no values to fill.

---

*RF — TFW-41 / Phase C: Research Templates — Embedded Dimensional Analysis | 2026-04-20*
