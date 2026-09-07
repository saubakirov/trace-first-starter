# REVIEW rev2 — TFW_20260902-111644_CRATM / Phase D: Team mode and Role Assignment

> **Date**: 2026-09-06
> **Author**: Codex (same independent Reviewer; acting as `saubakirov`)
> **Verdict**: 🔄 REVISE
> **Review scope**: bounded source-grounded recheck of supplied-versus-additional profile admission
> **RF**: [RF Phase D](RF__phase-d__team_mode_and_role_assignment.md), returned state tip `093449fa3429409df00fc90d330236c5ea369a60`
> **TS**: [TS Phase D](TS__phase-d__team_mode_and_role_assignment.md), approved at `6a7ede0549dca272c149b0294a972c013d5cb291`
> **Candidate**: `9edbebcf68872a72a9274765ad053e8d25fa66ac`
> **Prior REVIEW**: [original approval](REVIEW__phase-d__team_mode_and_role_assignment.md), commit `9bea59d4bcd4cae2976e28c208784c5ae62b55ce`
> **Closure tip inspected**: `881f6e240db52e01bac1403cd4a807ddfde3172d`
> **Stage files**: `review/rev2/map.md`, `review/rev2/verify.md`, `review/rev2/judge.md`

---

## 1. Map

This revision leaves Candidate and the completed closure untouched and rechecks one source boundary.
The approved TS distinguishes the supplied initial Codex profile, which may carry its disclosed G1–G7
evidence limit without claiming G8 reliability, from every additional provider profile, which must
pass all eight gates in one native run. The adapter supplies the limited initial profile, but canonical
`.tfw/conventions.md:824` says without qualification that every profile joins only after the complete
native trial.

Existing assurance checks the eight canonical gate headings and the adapter's evidence-limit sentence
as separate records. It has no admission decision spanning those records and no mutant that changes
the supplied/additional distinction. Candidate→closure leaves all eighteen implementation blobs
unchanged; the original debt rulings and closure documentation therefore remain separate and intact.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|------------------|--------|----------|
| V1 | Approved source intent | VERIFIED | TS lines 78–82 distinguish the supplied G1–G7/no-G8 profile from any additional profile; AC-1 lines 277–278, HC-D3 line 253, and AC-4 lines 348–360 repeat the two sides. Research iter3 D3/H10/A1/Q4 corroborates the evidence boundary. |
| V2 | Delivered canonical and adapter sources | FAILED | Canon line 824 quantifies over “A profile” and requires all eight; adapter line 22 and native evidence disclose only G1–G7/no G8. The canon therefore rejects the only supplied first-release profile required by TS. |
| V3 | Required positive and negative cases | FAILED / VERIFIED | Positive supplied fixture expects `ADMIT_SUPPLIED_LIMITED` but canon returns `REJECT_NO_G8`; negative additional incomplete fixture correctly returns `REJECT_NO_NATIVE_G8`. |
| V4 | Required output-changing mutants | VERIFIED as missing assurance | Universal-gate mutant changes the supplied positive output and is rejected by TS; partial-receipt mutant changes the additional negative output and is rejected by TS/HC-D3/canon. Neither exists in current assurance. |
| V5 | Existing Phase D tests | INSUFFICIENT | Eight bounded tests pass around the contradiction. The parser treats canon completeness and adapter limitation independently; native mutants only omit one heading. One ninth test fails only because post-review `KNOWLEDGE.md` is visible at closure, not because of admission. |
| V6 | Candidate and closure integrity | VERIFIED | All eighteen approved VALUE/ASSURANCE blobs are byte-identical from Candidate to closure tip. D82, prior REVIEW dispositions, phase `DONE`, and closure journals were inspected and not changed. |
| V-accounting | Independent value-bearing replay | VERIFIED unchanged | Approval `6a7ede0549dca272c149b0294a972c013d5cb291`; Baseline `8e68ab37d300122ff110500ad58f354f76b6210f`; Candidate `9edbebcf68872a72a9274765ad053e8d25fa66ac`; 16 literal VALUE members; 180 additions + 423 deletions = 603 touched LOC; immutable plan 16/640. A ruled later VALUE fix must create and recompute a replacement Candidate under AC-6. |

Raw source comparisons, the two fixtures, both mutants, commands, evidence audit, and verification
limits are recorded in [verify.md](review/rev2/verify.md). No full suite was run because the recheck
found a dispositive source contradiction before any authorized correction.

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD / all TS AC | ❌ | AC-1/AC-4 conflict in delivered canon; AC-5 lacks the cross-rule cases and mutants. |
| 2 | Purpose and design | ❌ | Purpose remains aligned with master HL §1 and NS1 human-governed continuity, but design soundness fails because canon rejects its only supplied profile. |
| 3 | Debt disposed by consequence | ✅ | Both original rows retain the Coordinator's terminal `not material — owed and forbidden to pay` rulings and barring clauses. |
| 4 | Style and standards | ❌ | The canonical universal quantifier exceeds the approved non-supplied scope and reverses a required positive case. |
| 5 | Observations collected | ✅ | Original observations remain; the new material mismatch is a verdict finding, not deferred debt. |
| 6 | RF §7–§9 complete | ✅ | Sections remain present and adequate; no new Fact Candidate, Strategic Insight, or Diagram is owed. |
| 7 | Evidence exists | ✅ | EV and all attachments exist; native evidence supplies the exact limited-profile fixture. |
| 8 | Evidence is sufficient | ❌ | Green heading/parser checks do not establish admission behavior or reconcile canon with the adapter. |
| 9 | Backward compatibility | ✅ | All predecessor/copy/receiver blobs remain unchanged; the failure is within new Phase D behavior. |
| 10 | Safety | ✅ | Reviewer changed only revision trace files and performed no implementation, dispatch, lifecycle, release, push, or destructive action. |

Purpose outcome: **Aligned**; design outcome: **unsound within the approved TS**. Contract baseline
`11888e547b0b37dc09469aee8fe2fd897d797906` and the Project North Star were read separately. The
material harm is not a wording preference: an authorized participant cannot reconstruct a single
legal admission result for the only shipped profile.

## 4. Verdict

**🔄 REVISE**

One material Candidate defect is confirmed. The delivered canonical rule makes a complete native
eight-gate run mandatory for every profile, contradicting the approved supplied-profile exception and
the adapter's disclosed G1–G7/no-G8 state. Current assurance cannot reveal the contradiction because
it validates those facts independently.

### If REVISE — proposals to coordinator

1. **Restore the supplied-versus-additional admission distinction and prove it behaviorally.**
   **Basis:** approved TS scope lines 78–82; AC-1 lines 277–278; HC-D3 line 253; AC-4 lines 348–360;
   AC-5's source-derived negative-case and output-changing-mutant requirement. **Owner/rung:** Phase
   Coordinator, **Rung 1**, because the desired outputs, affected literal VALUE/ASSURANCE selectors,
   and evidence method already exist in the approved TS. **Observable completion condition:**
   provider-neutral canon admits the supplied initial profile only with its G1–G7/no-G8 limitation
   explicit; rejects every additional profile lacking one native all-eight run; keeps partial evidence
   non-composable; source-derived assurance exercises both cases and independently rejects universal-
   gate and partial-composition mutants; a replacement Candidate is tested and AC-6 accounting is
   recomputed from the immutable Baseline.

**Proposed correction bound:** modify only `.tfw/conventions.md` and the necessary Phase D assurance
inside `docs/scripts/test_runtime_context.py`; retain the adapter/managed receiver wording unless exact
parity mechanically requires otherwise. Preserve all eight gate definitions, human-rooted authority,
Role Locks, direct routing, worktree isolation, provider-homogeneous first release, Claude protection,
no reliability claim, prior closure corrections, and both original debt dispositions. Do not create a
new profile, run a provider trial, change HL/TS, broaden authority, or fold the unrelated post-closure
`KNOWLEDGE.md` test-context observation into this round.

This is one proposal, not an acceptance ruling or implementation order. It returns to the Phase
Coordinator; the standing Main hold remains in force pending Main's source-grounded ruling.

## 5. Tech Debt Collected and Disposed

The two original rows and their Coordinator rulings are preserved verbatim in substance. Neither is
reopened by this bounded recheck, and the new admission failure is not classified as debt.

| # | Source | Severity | File | Description | Disposition |
|---|---|---|---|---|---|
| 1 | RF §6 observation 1 | Med | `.tfw/scripts/gen_index.py:746` | The event reader omits template-valid `writer`, so task-wide validation remains red for valid current events. | **not material — owed and forbidden to pay (Coordinator ruling, 2026-09-06).** The approved TS excludes this runtime/script repair and master A1/A2 rejected that carrier. |
| 2 | RF §6 observation 2 | Low | `workspace/2026/TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md:9` | Immutable historical event summary is 123 code points against today's 120 limit. | **not material — owed and forbidden to pay (Coordinator ruling, 2026-09-06).** The TS names this repair out of scope and immutable history forbids payment here. |

## 6. Traces Updated

- [x] Reviewer revision artifacts added as `__rev2` / `review/rev2/`; original REVIEW and stage files remain unchanged.
- [x] Phase lifecycle and outcome remain at the recorded `DONE` closure; no retrospective status or journal rewrite and no new transition event.
- [x] Task-level lifecycle remains `PHASES`; master/phase HL and approved TS remain unchanged.
- [x] Candidate, prior review commit, closure tip, D82, and both terminal debt rulings preserved.
- [x] tfw-docs: **Applied previously and preserved; not rerun for a REVISE proposal.**
- [x] tfw-knowledge: **N/A — no Fact Candidates.**

## 7. Fact Candidates

No fact candidates. Main's inspected owner clarification remains unruled context and supplied no
authority to alter the contract, correction bound, lifecycle, or implementation.

> fact-candidates: processed 2026-09-07

## 8. Coordinator ruling — combined A7 revision round

**Ruled 2026-09-06 by the Phase D Coordinator under Main's owner-authorised bound.** The Reviewer's
admission finding is accepted as material, but its proposed rung-1 two-file correction is superseded
by the later owner-approved A7 model change. A7 is the resolved rung-3 act; together the two findings
leave one executable rung-2 planning round governed by
[`TS__phase-d__team_mode_and_role_assignment__rev2.md`](TS__phase-d__team_mode_and_role_assignment__rev2.md).

The revised round must correct both the complete principal/unit/mandate model and combined profile
admission. It preserves the original Candidate, closure, REVIEWs and DONE event as history. The live
phase-state reconciliation is case-specific and is not a fabricated `DONE → TS_DRAFT` transition.
Implementation remains **HOLD** until Main approves the exact TS revision and its VALUE plan; after
approval the same existing Executor and independent Reviewer are the only recipients.

---

*REVIEW rev2 — TFW_20260902-111644_CRATM / Phase D: Team mode and Role Assignment | 2026-09-06*
