# RF — TFW-46 / Phase A: Evidence Concept + Templates

> **Date**: 2026-07-07
> **Author**: Executor (Antigravity, Claude Opus 4.6)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-46](../HL-TFW-46__evidence_layer.md)
> **TS**: [TS Phase A](TS__phase-a__evidence_templates.md)
> **ONB**: [ONB Phase A](ONB__phase-a__evidence_templates.md)

---

## 1. What Was Done

Evidence Layer Phase A: established Evidence as a first-class concept in TFW conventions, added Evidence fields to TS and RF templates, added Evidence Audit to review stage templates, extended honesty rules and anti-patterns in conventions.md, and renumbered RF §5-8 → §6-9 across all active references.

### Files Modified

| # | File | Change |
|---|------|--------|
| 1 | [conventions.md](../../.tfw/conventions.md) | §3: Evidence Sections table, Visual Sections §8→§9, Knowledge Capture §6→§7 and §7→§8. §12: evidence honesty rule. §14: RF §6-8→§7-9, 5 anti-self-deception anti-patterns |
| 2 | [TS.md](../../.tfw/templates/TS.md) | Evidence field instruction block + `Evidence:` field in AC items |
| 3 | [RF.md](../../.tfw/templates/RF.md) | New §5 Evidence section with table + 4-status vocabulary. Renumbered §5→§6, §6→§7, §7→§8, §8→§9. Updated internal cross-refs (§6→§7, §7→§8) |
| 4 | [judge.md](../../.tfw/templates/review/judge.md) | Check #7 Evidence completeness. Updated #3 §5→§6, #6 §6-8→§7-9. Updated checkpoint §6-8→§7-9 |
| 5 | [verify.md](../../.tfw/templates/review/verify.md) | Evidence Verification section with table. Evidence checkpoint item |
| 6 | [REVIEW.md](../../.tfw/templates/REVIEW.md) | Judge table #6 §6-8→§7-9 |
| 7 | [handoff.md](../../.tfw/workflows/handoff.md) | Phase 3 section refs §5-8→§6-9, tip §6→§7 |
| 8 | [review.md](../../.tfw/workflows/review.md) | Trust Protocol §5→§6 |
| 9 | [HL.md](../../.tfw/templates/HL.md) | Visual Sections hint (RF §9), Strategic Insights cross-ref §6→§7 |
| 10 | [compilable_contract.md](../../.tfw/compilable_contract.md) | RF §6 FC→§7 FC _(deviation: outside TS scope, prevents stale ref)_ |
| 11 | [knowledge.md](../../.tfw/workflows/knowledge.md) | RF §7→§8 Strategic Insights _(found during verification sweep)_ |
| 12 | [README.md](../../README.md) | Task board: 🟡 TS_DRAFT→🟢 RF, added ONB link |

## 2. Key Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| K1 | Added Evidence Sections as new §3 subsection (not merged into Visual or Knowledge Capture tables) | Evidence has a distinct cognitive mode (Observational/Verification) and per-template naming pattern (D8/D39). Merging into Visual Sections (which are about diagrams/visualization) would conflate purposes. A dedicated table makes the three-role pipeline explicit |
| K2 | HL.md §11 cross-ref updated from §6→§7 even though HL doesn't have its own Fact Candidates section | The (§6) in HL template was a cross-template reference to RF's Fact Candidates. After renumbering, keeping §6 would point to RF's Observations instead. Updated to §7 to maintain correct cross-reference semantics |
| K3 | compilable_contract.md and knowledge.md updated despite being outside TS affected files list | AC-6 scopes to `.tfw/templates/` and `.tfw/workflows/`. knowledge.md is in workflows/ so it's in scope. compilable_contract.md is in `.tfw/` root — outside strict scope. Updated anyway because leaving `RF §6 FC` when FC is now §7 creates an immediate inconsistency in a file used by build tooling |
| K4 | Evidence field instruction uses the "same as §6 Technical Guidance" MAY-deviate pattern | Per D10: Evidence field = guidance, not mandate. Linking to the existing §6 pattern establishes consistency — coordinators and executors already understand this contract. No new learning needed |

## 3. Acceptance Criteria

- [x] **AC-1: Evidence concept in conventions.md §3** — Evidence Sections subsection added with description (what it is, how it differs from Verification, status vocabulary, three-role pipeline). Per-template table with 4 rows and cognitive modes. No domain-specific examples.
- [x] **AC-2: Evidence field in TS template** — `Evidence:` field added after `Gate:` in both AC items. Instruction block with grammar options (full spec, minimal, N/A, DEFERRED, empty). MAY-deviate instruction.
- [x] **AC-3: §5 Evidence section in RF template** — New §5 with cognitive mode instruction, 6-column table (AC, What, Environment, Result, Artifact), evidence verdict line. §5-8 renumbered to §6-9. Internal cross-refs updated (§6→§7, §7→§8).
- [x] **AC-4: Evidence Audit in review stage files** — judge.md: check #7 added, #3 updated (§5→§6), #6 updated (§6-8→§7-9), checkpoint updated. verify.md: Evidence Verification section with table and N/A fallback, checkpoint item added.
- [x] **AC-5: Anti-self-deception rules** — §12 extended with evidence honesty rule. §14: 5 anti-patterns added (R1-R5 from D15). All domain-agnostic.
- [x] **AC-6: Cross-file reference updates** — All 9 TS-listed files updated + 2 additional files found during verification sweep. Final grep shows zero stale references to old numbering in templates/ and workflows/ (excluding CHANGELOG.md historical entries).

## 4. Verification

- Lint (`echo "configure your lint command"`): N/A (markdown-only changes)
- Tests (`echo "configure your test command"`): N/A (no executable tests for .tfw)
- Verify (`echo "configure your verify command"`): N/A (no verify command configured)

**Manual verification performed:**
1. Grep for `§5 Observations|§6 Fact|§7 Strategic|§8 Diagrams` across `.tfw/` — 0 results
2. Grep for `§6-8` range reference across `.tfw/` — 0 results
3. Grep for `RF §[5-8]` across `.tfw/` — only new references (§5 Evidence, §6 Observations, §7 FC, §8 SI) and CHANGELOG.md historical entries

## 5. Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Evidence Sections table present in conventions.md §3 with 4 cognitive modes | Local file | VERIFIED | conventions.md lines 107-119 (diff output above) |
| E2 | AC-2 | Evidence field and instruction block present in TS template | Local file | VERIFIED | TS.md diff output above |
| E3 | AC-3 | §5 Evidence section present, §6-9 renumbered, cross-refs updated | Local file | VERIFIED | RF.md diff output — 6 replacement chunks |
| E4 | AC-4 | judge.md check #7 and verify.md Evidence Verification section present | Local file | VERIFIED | judge.md and verify.md diff outputs above |
| E5 | AC-5 | 5 anti-patterns in §14 + §12 honesty rule present | Local file | VERIFIED | conventions.md diff output — chunks 4-6 |
| E6 | AC-6 | No stale references in templates/ or workflows/ | grep output | VERIFIED | Final sweep: `§5 Observations|§6 Fact|§7 Strategic|§8 Diagrams` = 0 results; `§6-8` = 0 results |

Evidence verdict: 6/6 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `compilable_contract.md` | 69 | stale-ref | `REVIEW.md §5 FC Source column` — REVIEW §5 is Tech Debt, not Fact Candidates. REVIEW §7 is Fact Candidates. Pre-existing error, not introduced by this change |
| 2 | `glossary.md` | 48 | stale-ref | `RF §7 "Strategic Insights (Execution)"` — should be §8 after renumbering. Glossary update is Phase C scope per TS §9 |
| 3 | `HL.md` | 36 | style | Added §9 Diagrams parenthetical to Result Visualization blockquote — this is a hint, not a dedicated Visual Sections table row. HL.md doesn't have an explicit Visual Sections cross-ref table like conventions.md |

## 7. Fact Candidates

No fact candidates.

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

No diagrams.

---

*RF — TFW-46 / Phase A: Evidence Concept + Templates | 2026-07-07*
