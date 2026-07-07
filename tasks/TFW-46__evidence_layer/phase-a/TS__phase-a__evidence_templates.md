# TS — TFW-46 / Phase A: Evidence Concept + Templates

> **Date**: 2026-07-07
> **Author**: Coordinator (Antigravity, Claude Opus 4.6)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-46](../HL-TFW-46__evidence_layer.md)

---

## 1. Objective
Establish Evidence as a first-class concept in TFW conventions and inject it into the three core templates (TS, RF, REVIEW stage files). After this phase, coordinators can design evidence requirements, executors can record evidence, and reviewers can audit evidence — using the existing template structure with minimal additions.

## 2. Scope

### In Scope
- Evidence concept definition in conventions.md (§3, §12, §14)
- Evidence field in TS template AC items (parallel to Gate)
- Evidence section (§5) in RF template + renumber §5-8 → §6-9
- Evidence check (#7) in review/judge.md template
- Evidence verification section in review/verify.md template
- Reference updates for renumbering across all `.tfw/` files

### Out of Scope
- Workflow updates (handoff.md, plan.md, review.md) — Phase B
- Glossary updates — Phase C
- Adapter syncing — Phase C
- Version bump — Phase C
- Evidence folder naming convention details — stays as guidance, not template mandate

## 3. Principles Check

> Map HL §7 principles to specific AC items. Each principle MUST have at least one AC enforcing it.

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P1 | Real over synthetic | AC-1 (Evidence concept separates §4 synthetic from §5 real) | conventions.md §3 text |
| P2 | Honest incompleteness | AC-1, AC-3 (DEFERRED/BLOCKED/N/A statuses in vocabulary) | RF template §5 status column |
| P3 | Coordinator designs, executor collects | AC-2 (Evidence field in TS), AC-3 (Evidence section in RF) | TS template Evidence field, RF template §5 |
| P4 | Domain-agnostic by default | AC-1, AC-2 (no domain-specific examples in templates) | Template review — no code/UI-specific examples |
| P5 | Proportional to risk | AC-2 (Evidence field can be N/A, coordinator calibrates) | TS template Evidence field grammar |
| P6 | Tooling proactivity | N/A — Phase B (handoff workflow guidance) | |
| P7 | Artifacts over claims | AC-5 (anti-self-deception rules require artifact references) | conventions.md §14 rules |

## 4. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/conventions.md` | MODIFY | §3 add Evidence concept, §12 extend honesty rules, §14 add 5 anti-self-deception anti-patterns |
| `.tfw/templates/TS.md` | MODIFY | Add `Evidence:` field to AC items (parallel to `Gate:`) |
| `.tfw/templates/RF.md` | MODIFY | Insert §5 Evidence table, renumber §5-8 → §6-9 |
| `.tfw/templates/review/judge.md` | MODIFY | Add check #7 (Evidence completeness) |
| `.tfw/templates/review/verify.md` | MODIFY | Add Evidence Verification section |
| `.tfw/templates/REVIEW.md` | MODIFY | Update §6 reference (RF completeness check mentions §6-8 → §7-9) |
| `.tfw/workflows/handoff.md` | MODIFY | Update RF section references (§5-8 → §6-9 in step descriptions) |
| `.tfw/workflows/review.md` | MODIFY | Update Trust Protocol references (§5 Observations → §6) |
| `.tfw/templates/HL.md` | MODIFY | Update §3 Visual Sections table reference (RF §8 → §9) |

**Budget:** 0 new files, 9 modifications. Defaults: max 26 files, max 18 new, max 500 LOC.

## 5. Acceptance Criteria

> Describe WHAT the result should achieve, not HOW to implement it.
> Each AC must be independently verifiable. Mark dependencies with `[depends: AC-X]`.

### AC-1: Evidence concept in conventions.md §3
The Artifact Types section defines Evidence as a distinct concept — separate from Verification (§4 in RF), with its own cognitive mode, status vocabulary, and role pipeline.
- [ ] §3 has a new subsection for Evidence describing: what it is (real-world verification of completed work), how it differs from Verification (synthetic vs real), status vocabulary (VERIFIED / DEFERRED / BLOCKED / N/A), and the three-role pipeline (Coordinator designs → Executor collects → Reviewer audits)
- [ ] Evidence is listed in the Visual Sections or Knowledge Capture Sections table with its cognitive mode
- [ ] The text uses no domain-specific examples (no "screenshots", "curl", "browser" — those are Evidence types, not the concept)

Gate: Read conventions.md §3 — Evidence concept is clear, domain-agnostic, and distinct from existing Verification
Evidence: N/A — conventions.md is a definition document; real validation = when executors use it (Phase B+)

### AC-2: Evidence field in TS template AC items
Each AC item in the TS template has an `Evidence:` field parallel to the existing `Gate:` field. Gate = synthetic verification (how to verify with tools). Evidence = real-world verification (how to verify in live environment). Evidence field follows MAY-deviate semantics (like §6 Technical Guidance).
- [ ] TS template §5 AC items show `Evidence:` field after `Gate:` field
- [ ] The Evidence field grammar supports: full spec, minimal spec, N/A with reason, DEFERRED with reason, empty (executor decides)
- [ ] The template includes a brief instruction block explaining Evidence field semantics (coordinator guidance, executor MAY deviate)

Gate: Read TS template §5 — Evidence field present, grammar clear, MAY-deviate noted
Evidence: N/A — template is a specification; validation = when coordinators write TS with it

### AC-3: Evidence section in RF template  [depends: AC-1]
RF template has a new §5 Evidence section with a structured table. Existing §5-8 renumbered to §6-9.
- [ ] RF template has §5 Evidence with instruction block (cognitive mode: "I observed this in reality — artifacts or honest gaps") and structured table: `| # | AC | What was verified | Environment | Result | Artifact |`
- [ ] Result column uses only the 4-status vocabulary from AC-1
- [ ] Evidence verdict line at bottom: `Evidence verdict: {N}/{M} VERIFIED, {X} DEFERRED, {Y} BLOCKED, {Z} N/A`
- [ ] Existing §5 Observations → §6, §6 Fact Candidates → §7, §7 Strategic Insights → §8, §8 Diagrams → §9
- [ ] All internal RF template references updated (if any cross-reference between sections)

Gate: Read RF template — §5 Evidence present, §6-9 renumbered correctly, no broken internal refs
Evidence: N/A — template spec

### AC-4: Evidence audit in review stage templates  [depends: AC-3]
Review stage templates (judge.md, verify.md) include evidence audit capabilities. No new REVIEW.md section needed — evidence checking extends existing stages.
- [ ] judge.md has check #7: Evidence completeness — "All TS Evidence fields covered in RF §5?"
- [ ] verify.md has Evidence Verification section with table: `| # | RF Evidence ref | Artifact exists? | Matches claim? |`
- [ ] verify.md checkpoint updated to include evidence verification self-check
- [ ] judge.md RF completeness check updated: §6-8 → §7-9 (renumbering)

Gate: Read judge.md and verify.md — evidence items present, renumbering correct
Evidence: N/A — template spec

### AC-5: Anti-self-deception rules in conventions.md §12 and §14  [depends: AC-1]
Conventions.md gets evidence-specific honesty rules (§12) and anti-patterns (§14) that structurally prevent false-green evidence.
- [ ] §12 extended with evidence honesty rules: evidence requires real-environment observation, VERIFIED requires artifact reference
- [ ] §14 has 5 new anti-patterns (adapted from compliance + a project runbook): (1) VERIFIED without artifact = violation, (2) N/A without justification = violation, (3) Evidence written before collected = violation, (4) Reviewer approves without checking artifacts = violation, (5) DEFERRED without specific blocker = violation
- [ ] Anti-patterns are domain-agnostic (no project-specific traps — those belong in project conventions)

Gate: Read §12 and §14 — 5 anti-patterns present, each with rationale
Evidence: N/A — convention spec

### AC-6: Cross-file reference updates for renumbering  [depends: AC-3]
All `.tfw/` files that reference RF section numbers (§5 Observations, §6 Fact Candidates, §7 Strategic Insights, §8 Diagrams) are updated to reflect the new numbering (§6, §7, §8, §9).
- [ ] REVIEW.md — RF completeness reference updated
- [ ] handoff.md — RF section references in Phase 3 updated
- [ ] review.md — Trust Protocol and Step 6 references updated
- [ ] HL.md — Visual Sections table (RF §8 Diagrams → §9) updated
- [ ] conventions.md — §3 Visual Sections and Knowledge Capture tables updated
- [ ] No stale references to old numbering remain in `.tfw/templates/` or `.tfw/workflows/`

Gate: `grep -rn "§[5-8]" .tfw/` — verify no stale references to old RF section numbers (context-aware: only RF-related refs, not TS §5 or HL §8)
Evidence: N/A — mechanical operation

## 6. Technical Guidance

> Reference material, not instructions. Executor MAY deviate with justification in RF.

- **Research decisions to apply**: D1 (term), D2 (vocabulary), D3 (proportional), D4 (mixed storage), D5 (separate §5), D6 (Evidence field in AC), D7 (extends REVIEW), D8 (per-template naming), D10 (MAY deviate), D11 (table format), D12 (judge #7 + verify section), D14 (two mediums), D15 (5 anti-patterns). See [iter1/RES.md](../research/iter1/RES.md) and [iter2/RES.md](../research/iter2/RES.md).
- **Renumbering precedent**: TFW-25 renumbered §5→§4, TFW-41 renumbered §4→§5. Same mechanical pattern. Use `grep -rn` to find all references before and after.
- **Evidence field grammar from D10**: Full spec / Minimal spec / N/A / DEFERRED / Empty — see iter2 RES D10 for exact formats.
- **Anti-self-deception rules from D15**: 5 rules with rationale from compliance + a project runbook — see iter2 RES D15 table.
- **conventions.md §3 Evidence subsection**: Model after existing artifact type entries (HL, RES, TS, RF, ONB, REVIEW). Short definition + format reference + cognitive mode distinction.
- **Evidence cognitive mode for Visual Sections table**: Observational / Verification — "I observed this outcome in the real environment."

## 7. Definition of Failure

- ❌ Evidence concept uses code-specific examples (screenshots, curl, adb) — must be domain-agnostic
- ❌ Evidence field in TS is mandatory for every AC (must allow N/A, empty) — proportionality violated
- ❌ Renumbering leaves stale references in `.tfw/` files — broken cross-references
- ❌ Anti-patterns are project-specific rather than framework-level — wrong scope

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Renumbering breaks references in files outside `.tfw/` (user project task files) | Out of scope — renumbering applies only to `.tfw/` templates and workflows. Existing project RFs keep their numbering until next task |
| Evidence instruction block in RF template is too long | Keep to 3 lines max (cognitive mode + scope + key rule). Details in conventions.md |
| conventions.md §3 grows too large with Evidence subsection | Evidence is a concept, not an artifact type — model after Fact Candidates entry (compact) |

## 9. Cross-Phase Modifications (multi-phase)

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `conventions.md` | Phase B (§8 Workflows reference) | Phase A modifies §3, §12, §14. Phase B modifies §8 to reference evidence collection step. No overlap |
| `review.md` | Phase B (workflow steps) | Phase A only updates reference numbers. Phase B adds Evidence Audit step to workflow |
| `handoff.md` | Phase B (Step 11) | Phase A only updates reference numbers. Phase B adds evidence collection step |

> **Cross-references**: RES iter1 D1-D8, RES iter2 D9-D16, HL TFW-46 §7 Principles, conventions.md §3/§12/§14

---

*TS — TFW-46 / Phase A: Evidence Concept + Templates | 2026-07-07*
