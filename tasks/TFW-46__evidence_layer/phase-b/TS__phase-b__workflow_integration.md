# TS — TFW-46 / Phase B: Workflows + Integration

> **Date**: 2026-07-07
> **Author**: Coordinator (Antigravity, Claude Opus 4.6)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-46](../HL-TFW-46__evidence_layer.md)

---

## 1. Objective
Integrate the Evidence concept (established in Phase A) into the three TFW workflows that govern the task lifecycle: plan.md (coordinator designs evidence requirements), handoff.md (executor collects evidence), review.md (reviewer audits evidence). After this phase, the Evidence lifecycle is active end-to-end — coordinators are prompted to write Evidence fields, executors have a distinct step for evidence collection, and reviewers have Trust Protocol entries for evidence claims.

## 2. Scope

### In Scope
- handoff.md — new Step 11 (Evidence Collection) between build gate and Pre-RF Gate
- handoff.md — §5 Evidence added to mandatory RF section list in Step 12
- review.md — Trust Protocol extended with evidence-specific entries
- review.md — Step 3 (Verify) reference to evidence audit in verify.md
- plan.md — coordinator reminder to write Evidence fields when writing TS AC items
- Fix TD-1 from Phase A (RF.md line 68 stale `§5 Observations` → `§6`)

### Out of Scope
- Glossary updates — Phase C
- Adapter syncing — Phase C
- Version bump — Phase C
- Tool-specific MCP/Playwright guidance (stays project-level, per D13 three-level cascade)

## 3. Principles Check

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P1 | Real over synthetic | AC-1 (Step 11 instruction distinguishes real from synthetic) | handoff.md Step 11 text |
| P2 | Honest incompleteness | AC-1 (DEFERRED/BLOCKED guidance in Step 11) | handoff.md Step 11 |
| P3 | Coordinator designs, executor collects | AC-3 (plan.md reminder), AC-1 (executor step) | plan.md + handoff.md |
| P4 | Domain-agnostic by default | AC-1 (no domain-specific tool names in workflow) | Review of Step 11 text |
| P5 | Proportional to risk | AC-1 (skip when no Evidence fields in TS) | handoff.md Step 11 proportionality clause |
| P6 | Tooling proactivity | AC-1 (proactive tooling note in Step 11) | handoff.md Step 11 |
| P7 | Artifacts over claims | AC-2 (Trust Protocol: VERIFIED without artifact = Challenge) | review.md Trust Protocol |

## 4. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/workflows/handoff.md` | MODIFY | New Step 11 (Evidence Collection), renumber Steps 11-12 → 12-13, add §5 to mandatory RF sections |
| `.tfw/workflows/review.md` | MODIFY | Trust Protocol: 2 new evidence entries. Step 3 Verify: reference evidence audit |
| `.tfw/workflows/plan.md` | MODIFY | Step 7: coordinator reminder to write Evidence fields in TS AC items |
| `.tfw/templates/RF.md` | MODIFY | Fix TD-1: line 68 stale `§5 Observations` → `§6 Observations` |

**Budget:** 0 new files, 4 modifications. Defaults: max 26 files, max 18 new, max 500 LOC.

## 5. Acceptance Criteria

### AC-1: Evidence Collection step in handoff.md
A new Step 11 (Evidence Collection) is inserted between the current Step 10 (build gate) and Step 11 (Pre-RF Gate). Current Steps 11-12 renumber to 12-13. The step guides executors to collect real-environment evidence for each TS AC item that has an Evidence field.
- [ ] Step 11 exists between build gate and Pre-RF Gate with clear title (e.g., "Collect evidence")
- [ ] Step instructs executor to walk through TS AC items with Evidence fields and verify each in a real environment
- [ ] Step includes proportionality clause: if no TS AC items have Evidence fields, this step is skipped
- [ ] Step includes honest-incompleteness guidance: DEFERRED/BLOCKED with reason when evidence can't be collected
- [ ] Step includes proactive tooling note: executor should seek/configure tools (MCP, browser, CLI) if needed for evidence collection
- [ ] Step does NOT name specific tools (Playwright, adb, etc.) — stays domain-agnostic
- [ ] Steps 11-12 (Pre-RF Gate and Create RF) renumbered to 12-13
- [ ] Step 12 (formerly 11, Pre-RF Gate) unchanged in content
- [ ] Step 13 (formerly 12, Create RF) mandatory sections list includes **§5 Evidence**
- [ ] Step 13 includes `Never omit §5.` alongside existing `Never omit §7-9.` (updated from §6-8)

Gate: Read handoff.md — Step 11 present, numbering correct, mandatory sections updated
Evidence: N/A — workflow spec

### AC-2: Trust Protocol extended in review.md
Review.md Trust Protocol table gets 2 new entries for evidence-specific claims, following the existing trust-level pattern (Trust / Verify / Challenge).
- [ ] Entry for `"Evidence: VERIFIED"` claims — Trust Level: **Verify** — Reviewer Action: check artifact exists and matches claim (reference verify.md Evidence Verification section)
- [ ] Entry for `"Evidence: N/A"` or `"No evidence needed"` claims — Trust Level: **Challenge** — Reviewer Action: check if TS had Evidence fields; if yes, challenge the N/A
- [ ] Existing entries unchanged
- [ ] Entries reference correct RF section numbers (post-renumbering)

Gate: Read review.md Trust Protocol — 2 new entries present, trust levels correct
Evidence: N/A — workflow spec

### AC-3: Evidence reminder in plan.md
Plan.md Step 7 (Write TS) includes a reminder for coordinators to write Evidence fields in TS AC items when writing acceptance criteria.
- [ ] Step 7 has a brief note (1-3 lines) reminding coordinator to consider Evidence fields for each AC item
- [ ] Note references the Evidence field grammar (full spec / minimal / N/A / DEFERRED / empty)
- [ ] Note emphasizes proportionality: trivial tasks may have all Evidence fields N/A or empty
- [ ] Note does NOT duplicate TS template instructions — just a pointer

Gate: Read plan.md Step 7 — evidence reminder present, proportional, concise
Evidence: N/A — workflow spec

### AC-4: Review.md Step 3 evidence reference  [depends: AC-2]
Review.md Step 3 (Verify) mentions that verify.md now includes an Evidence Verification section, so reviewers know to check evidence artifacts during verification.
- [ ] Step 3 description or bullet points reference evidence verification alongside existing file-checking and command-running guidance
- [ ] Reference is brief (1 line) — details are in verify.md template itself

Gate: Read review.md Step 3 — evidence reference present
Evidence: N/A — workflow spec

### AC-5: Fix TD-1 from Phase A
RF.md line 68 has a stale internal cross-ref: `§5 Observations` should be `§6 Observations` (post-renumbering).
- [ ] RF.md instruction block references `§6 Observations` instead of `§5 Observations`

Gate: Read RF.md — stale ref fixed
Evidence: N/A — single-line fix

## 6. Technical Guidance

> Reference material, not instructions. Executor MAY deviate with justification in RF.

- **D9 (iter2)**: Evidence Collection = new Step 11 in handoff.md. Placement survives 6 stress-test scenarios (Challenge C1 in iter2). Natural cognitive transition: "code compiles/tests pass" → "it actually works in real conditions" → "document what happened."
- **D13 (iter2)**: Three-level tooling cascade — TFW provides general guidance (handoff.md), coordinator specifies per-AC (TS), executor discovers/configures (runtime). Step 11 is the "framework level" of the cascade.
- **handoff.md step numbering**: Current Steps 7-12. After Phase A renumbering, Steps 11-12 reference §6-9. After this phase: Steps 11→12 (Pre-RF Gate), 12→13 (Create RF), new Step 11 inserted.
- **review.md Trust Protocol pattern**: Each entry has 3 columns (RF Claim Type, Trust Level, Reviewer Action). Trust levels: Trust (accept as-is), Verify (check claim), Challenge (push back if suspicious). Evidence entries follow same pattern.
- **plan.md evidence reminder location**: Step 7 → within "Write TS" instruction, after budget check. Coordinator is already in "writing AC items" cognitive mode — natural place for Evidence field reminder.

## 7. Definition of Failure

- ❌ Step 11 names specific tools (Playwright, adb, curl) — must stay domain-agnostic
- ❌ Step 11 is mandatory regardless of TS content — must skip when no Evidence fields exist (proportionality)
- ❌ Trust Protocol entries break existing entry semantics
- ❌ Plan.md reminder duplicates TS template instructions verbatim

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Step renumbering in handoff.md conflicts with Phase A renumbering | Phase A only updated RF section references (§5-8→§6-9). This phase renumbers workflow steps (11-12→12-13). No overlap |
| Executor adds too much text to Step 11 | Keep to same density as Steps 9-10 (~3-5 lines). Details belong in conventions.md and templates, not workflow |
| plan.md reminder feels redundant with TS template | Reminder is a pointer ("consider Evidence fields"), not instruction duplication. Same pattern as Step 4a's PV scan reminder |

## 9. Cross-Phase Modifications (multi-phase)

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `handoff.md` | Phase A (§ renumbering) | Phase A updated RF section refs. Phase B adds Step 11 + renumbers Steps. No conflict |
| `review.md` | Phase A (§ renumbering) | Phase A updated §5→§6 in Trust Protocol. Phase B adds 2 new Trust Protocol entries. No conflict |
| `RF.md` | Phase A (§5 Evidence + renumbering) | Phase B only fixes TD-1 stale ref. No structural change |

> **Cross-references**: RES iter2 D9 (handoff placement), D13 (tooling cascade), HL TFW-46 §7 P1-P7, Phase A REVIEW TD-1

---

*TS — TFW-46 / Phase B: Workflows + Integration | 2026-07-07*
