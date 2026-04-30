# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Mode: docs
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | All 3 ACs verified: 10/10 sub-items for AC-1, 3/3 for AC-2, 4/4 for AC-3. All DoF gate greps = 0 matches. See verify.md V1, V2 |
| 2 | Philosophy aligned | ✅ | P1 (Locality): RES.md path inside `research/iterN/`. P2 (Sort order): numbered stage files at every reference. P3 (Container): no `researchN/` remains. P4 (Casing): `phase-a/`. P5 (Optional enrichment): `agent`/`sources` marked optional. P7 (Tool-agnostic): no brand names in plan.md |
| 3 | Tech debt documented | ✅ | RF §5 Observations: 2 items (handoff.md TD-112 PhaseA refs, compilable_contract.md TD-111 PhaseA refs). Both correctly scoped as out-of-scope carryovers |
| 4 | Style & standards | ✅ | Artifact filename follows convention: `RF__phase-b__workflow_updates.md`. RF template structure followed. Key Decisions documented. No placeholder content |
| 5 | Observations collected | ✅ | 2 observations — both real issues (verified: handoff.md and compilable_contract.md do contain old `PhaseA` references). Quality filter: these are genuine remaining drift, not filler |
| 6 | RF completeness (§6-8) | ✅ | §6 Fact Candidates: "No fact candidates." (present, empty = valid). §7 Strategic Insights: "No strategic insights." (valid for docs-only phase). §8 Diagrams: "No diagrams." (valid — no architecture/flow changes) |

## Mode-Specific Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 7 | Content quality | ✅ | Both workflow files are clear, accurate, internally consistent. Template references are explicit (numbered file names). Plan.md Step 7 tree is readable. Multi-agent reference is exactly 1 sentence with cross-ref to conventions.md §4 |
| 8 | Source verification | ✅ | All claims traceable: RF §3 line references verified against actual file content. Deviations (Step 6c, `RES,` removal) justified in RF §2 Key Decisions with ONB/TS references |

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D38 (multi-iteration research) | Updated folder structure from `researchN/` to `research/iterN/` | No — D38 established the principle, TFW-42 refactors the implementation |
| 2 | D48 (naming normalization) | `PhaseA/` → `phase-a/` in plan.md | No — extends D48 to phase folder naming (consistent direction) |

No contradictions.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Checked RF §6-8 for presence AND quality (not just existence)?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"?
- [x] Fact Candidates from RF reviewed — any that need challenge?

Stage complete: YES
