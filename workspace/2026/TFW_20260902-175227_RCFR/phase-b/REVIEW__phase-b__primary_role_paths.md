# REVIEW — TFW_20260902-175227_RCFR / Phase B: Primary Role Paths

> **Date**: 2026-09-04
> **Author**: Codex (Reviewer), acting on behalf of `saubakirov`
> **Verdict**: 🔄 REVISE
> **Amended**: 2026-09-04 — supplemental Reviewer-routing finding added in place while this REVIEW remains live
> **RF**: [RF Phase B](RF__phase-b__primary_role_paths.md)
> **TS**: [TS Phase B](TS__phase-b__primary_role_paths.md)
> **Candidate**: `272a7cf737c84958d81c41257cc9c2568c74ee0f`
> **Stage files**: [`review/map.md`](review/map.md), [`review/verify.md`](review/verify.md), [`review/judge.md`](review/judge.md)
> This file is a synthesis of stage findings. Reference stage files for raw evidence.

---

## 1. Map

Phase B replaces duplicate preload and repeated role prose with thin skills and selective canonical workflows for Coordinator, Researcher, Executor, and Reviewer. Its bounded surface is four workflows, their generated copies, four skills and installed copies, one adapter manifest, and two validation files; all 23 claimed implementation/test files and the Phase A predecessor contract were mapped.

The architecture keeps task-local authority first, addressed shared reads at their decision checkpoints, templates at artifact-entry gates, explicit role locks, and adapter parity. The RF declares all six acceptance criteria complete and supplies one EV index plus four attached evidence transcripts.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|------------------|--------|----------|
| 1 | Governing source, baseline, surface, and budgets | ✅ | Candidate is exactly `272a7cf`; immutable baseline `80382fbf…` and all five baseline counts reproduce; 23 files and 1,005 changed LOC are within TS limits; frozen exclusions are untouched. |
| 2 | Four workflows, eight skill files, eight generated workflow copies, and manifest | ✅ | All 23 implementation/test files were inspected after escalation; canonical/installed skills and canonical/generated workflows are byte-equal; algorithms, roles, gates, and stops are present. |
| 3 | Targeted and full regression gates | ✅ | 143 targeted tests pass; 437 tests collect; full suite is 436 passed/1 skipped; project check passes. |
| 4 | Clean receivers, reinstall repair, idempotence, and preservation | ✅ | Four receiver scenarios expose 11/11 artifacts; integration coverage and direct hashes confirm parity and repair behavior. |
| 5 | Complete symmetric read graph and exact reduction evidence | ❌ | Candidate Researcher graphs omit required Gather, Extract, and Challenge template reads. Corrected Researcher totals are 6,103/6,168, individual reductions remain 79.7%/79.5%, and combined reduction becomes 71.8%; the 30% floor holds, but graph completeness and the published 72.4% do not. |
| 6 | Independent semantic oracle and deliberate mutants | ❌ | Ordinary P/R/E/V/C/A records match, but the shared family mutants fail at missing probe anchors before any changed record is produced. Only E3 demonstrates the required produced-output change. |
| 7 | Knowledge/PV citations and predecessor | ✅ | All 20 master-HL/ONB applications resolve and match after a full P0–P4 and relevant P5–P7 scan; Phase A RF/approved REVIEW and D73 are consistent. |
| 8 | Repository diagnostics and exclusions | ✅ with known exception | `--check project` passes; `--check tasks` reports only the approved immutable RDP 123>120 event-summary diagnostic, which Phase B was forbidden to edit. |
| 9 | Reviewer three-rung route, authority, state effects, and oracle coverage | ❌ | Rung 1 is simultaneously routed direct to execution with no state move and routed through Coordinator/TS revision with `TS_DRAFT`; V1–V4/C1 contain no rung-specific case. This review's own first transition reproduced the ambiguity. |

> Raw verification log: see `review/verify.md`. Verification was not limited: the first discrepancy expanded the sample from the required 10 files to all 23.

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ❌ | AC-1, AC-4, and AC-6 fail the complete-graph, three-rung routing, and per-family output-changing-mutant conditions; frozen DoD 3/6/10, Principles 2/9, and Quality Contract 1 are not established. |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ❌ | Purpose is aligned to frozen HL §1 and NS1: it removes context tax while preserving inspectable continuation. Design soundness fails because the proof omits inputs/output-changing mutants and the active Reviewer authorities prescribe incompatible next acts for rung 1. |
| 3 | Debt disposed | ✅ | The sole RF observation is the same immutable RDP diagnostic already ruled by the Phase A Coordinator as `not material — owed and forbidden to pay`; its red-signal consequence and TS/journal bar remain explicit in §5. |
| 4 | Style & standards | ❌ | Naming, adapters, and diff hygiene hold, but competing mandatory rung-1 rules violate frozen DoD 6 and DoF 3's one-authority standard. |
| 5 | Observations collected | ✅ | RF records the real out-of-scope RDP diagnostic; material audit/oracle defects are verdict items below. |
| 6 | RF completeness (§7–9 present) | ✅ | Fact Candidates, Strategic Insights, and Diagrams are present and adequate; no Human-Only claim was omitted. |
| 7 | Evidence completeness — does it exist? | ✅ | EV covers E1–E6 and all referenced transcripts exist with allowed statuses. |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | Evidence establishes thresholds, tests, scope, parity, and receivers, but not complete Researcher graphs, output-changing mutants in all six families, or rung-specific Reviewer recipient/state behavior. |
| 9 | Backward compatibility | ✅ | Ordinary semantic records and consumer surfaces show no newly introduced break. The routing contradiction predates Phase B, so it is an unresolved AC-4 authority defect rather than a new compatibility regression. |
| 10 | Safety | ✅ | No secret, credential, network/destructive behavior, or immutable-history edit appears in the result. |

## 4. Verdict

**🔄 REVISE**

The result is fit for the frozen purpose and the implementation remains within its authorized scope, but the RF's complete-graph, semantic-oracle, and Reviewer-routing acceptance claims are not true. Green suites cannot substitute for explicit TS conditions they do not exercise. The first two defects are correctable inside the approved TS; the third requires a TS revision, but none requires a frozen-HL change, so REJECT remains disproportionate and APPROVE would violate the citation bar.

### Items proposed to the coordinator

1. **Rung 1 — complete the candidate Researcher read graph and regenerate its evidence.** Include all mandatory staged template reads (`1_briefing.md`, `2_gather.md`, `3_extract.md`, `4_challenge.md`) in both focused and deep candidate paths, apply the same edge/classification rules to baseline and candidate, add a failure that detects an omitted required stage read, and regenerate E1/E6 plus the runtime/verification transcripts with exact totals. **Owner:** Executor. **Observable completion:** the generated graph enumerates all four stage templates for both modes, an injected omission fails independently, and recomputed reductions still clear 30%. **Basis:** TS AC-1 bullets 2–3; TS AC-6 bullets 3–4; frozen master-HL DoD 3 and Quality Contract 1.
2. **Rung 1 — demonstrate an output-changing deliberate mutant for every semantic family.** Add at least one source-derived substitution in each P/R/E/V/C/A family that completes production of a changed `SemanticRecord` before the independent expected comparison rejects it; keep expected data outside production and regenerate E3/E6 plus semantic/verification transcripts. **Owner:** Executor. **Observable completion:** six family assertions first prove a record was produced and differs in a named field, then prove the independent comparison rejects it. **Basis:** TS AC-6 bullets 1–2.
3. **Rung 2 — pending — Coordinator: establish one authoritative three-rung Reviewer route.** Revise TS §4/budget to authorize `.tfw/conventions.md` in addition to the already exhausted 23-file surface, then reconcile `.tfw/workflows/review.md:143,153,159`, `.tfw/conventions.md:580–600,897–900,932–939`, generated workflow copies, D72, and the semantic proof. The chosen contract must state, for each rung, who receives the item, whether a TS revision is required, and when lifecycle changes; it must not leave rung 1 both “back to execution / nothing moves / needs no coordinator” and “Coordinator / TS revision / TS_DRAFT.” **Owner:** Coordinator for the TS revision; Executor for the ordered implementation. **Observable completion:** independent rung-1, rung-2, and rung-3 cases assert recipient, artifact authority, lifecycle transition or its absence, and hard stop; contradictory-clause mutants fail; canonical/generated copies match; a self-host Reviewer can follow the same route without choosing between sources. **Basis:** TS AC-4 bullet 2 and Evidence observable success; TS §4 lines 60–78 and 23-file budget; frozen master-HL DoD 6/10, DoF 3, Principles 2/6, and Quality Contract 4.

These are Reviewer proposals, not an ordered round. Items 1–2 remain rung 1; item 3 is rung 2 and requires the Coordinator. Return the work to the Coordinator; start `/tfw-plan` to order the round. The Reviewer does not edit the TS, RF, evidence, implementation, or dispatch an Executor.

## 5. Tech Debt Collected and Disposed

| # | Source | Severity | File | Description | Disposition |
|---|--------|----------|------|-------------|-------------|
| 1 | RF observation 1 | Medium | `workspace/2026/TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md` | The immutable pre-existing summary is 123 code points, leaving `--check tasks` red and creating a signal that can be normalized as noise. | **not material — owed and forbidden to pay — coordinator, 2026-09-03.** Existing ruling carried from Phase A REVIEW §5. Payment is barred because journal events are immutable and Phase B TS §2/AC-6 explicitly excludes unrelated RDP repair; the named red-signal consequence remains. |

No disposition is pending. The Reviewer has not made a new ruling; this row carries the Coordinator's existing ruling for the identical immutable observation.

## 6. Traces Updated

- [x] Phase `status.md` — remains `TS_DRAFT`. The earlier `RF → TS_DRAFT` event is immutable and is now direct evidence of the routing conflict: it followed the universal Hard Stop before any TS change, contrary to the rung table. The Reviewer does not conceal the defect by reversing that state under another disputed rule.
- [x] HL status — N/A; 🔄 REVISE does not complete Phase B or alter the frozen master HL.
- [x] Phase `status.md` — `updated` reflects this amended live review; no counter was allocated.
- [x] Phase journal — no new event: lifecycle did not change during the addendum, the closed vocabulary has no review-amendment kind, and the existing event was not edited.
- [x] §5 — no row left undisposed; the sole row carries its existing Coordinator ruling.
- [x] Other project files — checked for stale information; three acceptance claims and the D72 alignment question are identified for the repair round, not edited by the Reviewer.
- [x] tfw-docs: N/A — 🔄 REVISE does not enter KNW.
- [x] tfw-knowledge: N/A — 🔄 REVISE does not enter KNW and no Human-Only Fact Candidate exists; any D72 wording reconciliation follows an approved implementation.

## 7. Fact Candidates

> fact-candidates: processed 2026-09-04

No fact candidates. The immutable RDP instruction restates an existing Coordinator ruling, and the supplemental routing hypothesis was independently recoverable from repository sources; neither is a new Human-Only project fact.

---

*REVIEW — TFW_20260902-175227_RCFR / Phase B: Primary Role Paths | 2026-09-04*
