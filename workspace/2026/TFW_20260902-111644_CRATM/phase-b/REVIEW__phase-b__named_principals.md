# REVIEW — TFW_20260902-111644_CRATM / Phase B: Named principals

> **Date**: 2026-09-06
> **Author**: Codex (Reviewer; on behalf of `saubakirov`)
> **Verdict**: 🔄 REVISE
> **RF**: [RF Phase B](RF__phase-b__named_principals.md)
> **TS**: [TS Phase B](TS__phase-b__named_principals.md), approved at `1e2631bff51b3b62673808d5de57f812883d814b`
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`

---

## 1. Map

The Executor added a provider-neutral named-principal contract to the four approved Markdown VALUE
owners: shared conventions, team profile, journal event, and external binding template. Candidate
`0ee39046b760d6d3e8d837c2377e49c1c95668bd` preserves four-key human profiles, makes agent
principals directly accountable to humans with one stable Boolean grant, permits optional durable
`writer` attribution, and leaves legacy `actor`, report-only readers, and real bindings unchanged.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|---|---|---|
| V-files | All six RF-claimed files | PARTIAL | 6/6 opened after escalation. All four VALUE files match the RF; ONB is complete; EV omits the executable `$validator` body behind three rows. |
| V-fixtures | Profile, event, and binding behavior | PARTIAL | Independent reconstruction passes all 17 documented outcomes (11 profile, 4 event, 2 binding), but `$validator \| python -` cannot replay the Executor's run without the variable definition required by AC-1/AC-2/AC-4. |
| V-tests | Configured and documentation checks | VERIFIED | 630 tests collected; 629 passed/1 skipped; project structural check, MkDocs build, and `git diff --check` pass. |
| V-compatibility | Legacy and protected surfaces | VERIFIED | 28/28 legacy `actor` blobs, the real four-key profile, reporter/tests, D79 Session identity, and Phase A protocol ranges are unchanged; Baseline/Candidate report-only archive replays are identical. |
| V-citations | Master/Phase HL §7.2 and ONB §7 | PARTIAL | Across 90 governing/application rows, 88 source chains resolve and 88 semantic identifications are exact. Master rows #2/#4 carry stale NS2 ordinals; Phase B B9 and ONB row #45 share one broken anchor, although the source item and application are real. |
| V-accounting | Independent value-bearing replay | VERIFIED | Approval `1e2631bff51b3b62673808d5de57f812883d814b`; Baseline `a048b2db5f44f5d748f22f3a0133f4ecf0acd9c4`; Candidate `0ee39046b760d6d3e8d837c2377e49c1c95668bd`; four literal `M` VALUE paths; 143 additions, 72 deletions, 215 touched text LOC; binary N/A; keep-one-phase trigger; immutable 4-file/240-LOC denominator; delegated authority and timing hold; Candidate is the first VALUE commit and no later VALUE exists. Replayed with `git diff --name-status --find-renames=50% -z a048b2db5f44f5d748f22f3a0133f4ecf0acd9c4 0ee39046b760d6d3e8d837c2377e49c1c95668bd -- .tfw/conventions.md .tfw/templates/team/profile.md .tfw/templates/journal/event.md .tfw/templates/bindings.yaml` and the identical `git diff --numstat` form. |

Raw log: [review/verify.md](review/verify.md). Verification limits: the Executor's omitted
`$validator` program and complete pre-commit staging transcript cannot be reconstructed from the
submitted trace. The resulting Candidate membership, documented fixture semantics, and all other
claims were independently checked; no substitute command was attributed to the Executor.

## 3. Judge

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD / all TS AC | ❌ | Implementation behavior for AC-1–AC-6 holds, but AC-1, AC-2, and AC-4 explicitly require exact parser-command evidence and the submitted program is absent. |
| 2 | Purpose and design | ✅ | Contract-baseline Vision and live NS1 require named, human-governed participants and inspectable continuation. Stable principals, direct accountability, writer attribution, and identity-only binding serve that purpose without Phase C–E/runtime excess. |
| 3 | Debt disposed by consequence | ✅ | Four §5 rows carry concrete pending Coordinator proposals, existing targets, and named consequences or material absences; no bare priority/backlog is used. |
| 4 | Style and standards | ✅ | VALUE prose is coherent, canonical, prohibition-based, within attention bounds, and diff-clean; pre-existing citation defects are separately exposed as trace debt. |
| 5 | Observations collected | ✅ | RF records the master-ordinal drift; Reviewer adds the evidence-provenance, staging-provenance, and broken-anchor observations. |
| 6 | RF §7–§9 complete | ✅ | RF explicitly states no Fact Candidates, no Strategic Insights, and no diagrams. |
| 7 | Evidence exists | ✅ | Every AC has an EV row and immutable accounting is separately recorded. |
| 8 | Evidence is sufficient | ❌ | Independent 17/17 reconstruction verifies behavior, not the undisclosed program behind the Executor's claimed run; EV's `6/6 VERIFIED` aggregate is therefore overstated. |
| 9 | Backward compatibility | ✅ | Legacy events/profile, reporter/tests, Phase A/D79 text, and all configured gates remain intact. |
| 10 | Safety | ✅ | Only four approved Markdown VALUE paths changed; no real binding, executable, config, test, runtime, provider state, or legacy rewrite was introduced. |

Purpose outcome: **aligned**, not `not fit for purpose`, and the reference set is internally coherent.
The independently recovered contract baseline, exact quoted clause, material harm, design assessment,
and KNOWLEDGE.md cross-check are recorded in [review/judge.md](review/judge.md).

## 4. Verdict

**🔄 REVISE**

The implementation, purpose, design, compatibility, safety, configured checks, and immutable
Baseline→Candidate accounting are sufficient. The result is not yet approvable because [§2
V-fixtures](#2-verify) and Judge rows 1/8 show that EV E1/E2/E4 cannot reproduce the Executor's fixture
run: the evidence records only `$validator | python -`, while AC-1, AC-2, and AC-4 explicitly require
the exact parser command. The approved TS already defines the behavior and evidence obligation, so
the return requires no VALUE change, TS sibling, or frozen-HL amendment.

### If REVISE — proposals to coordinator

1. **Close the exact validator-command evidence gap** — **basis:** approved TS AC-1 Evidence,
   AC-2 Gate/Evidence, and AC-4 Gate/Evidence. **Owner:** `saubakirov` from Phase B `status.md`.
   **Proposed route:** rung 1, because the correction is entirely inside the approved TS and does not
   change Candidate or any contract claim. **Observable completion:** the Coordinator accepts this
   exact bound in the live REVIEW; the same Executor appends, rather than rewrites, a Round 2 EV record
   containing a complete executable validator program, the exact 17 already documented fixture
   payloads, and fresh 17/17 output; RF appends the corresponding current evidence summary while
   preserving the original provenance limitation; Candidate remains
   `0ee39046b760d6d3e8d837c2377e49c1c95668bd` with no later VALUE; `/tfw-review` in this same
   Reviewer task independently replays the preserved program and rules the return.

The staging transcript and citation issues do not cite a failed Phase B implementation criterion or
frozen claim and therefore do not widen the executable REVISE round; they are disposition proposals
in §5 only.

## 5. Tech Debt Collected and Disposed

| # | Source | Severity | File | Description | Disposition |
|---|---|---|---|---|---|
| 1 | Verify discrepancy 1 / Judge rows 1, 8 | High | `evidence/EV__phase-b__named_principals.md` E1/E2/E4 | The evidence omits the executable `$validator` body, so the Executor's claimed fixture run cannot be replayed and three exact-command evidence clauses remain unmet. | **pending — coordinator**; proposed `paid — phase-b` through the rung-1 observable completion in §4. Existing target: `workspace/2026/TFW_20260902-111644_CRATM/phase-b/`. |
| 2 | Verify discrepancy 2 | Medium | Phase B Candidate/TRACE commit provenance | Candidate membership is exact and uncontaminated, but no durable complete pre-commit status, cached-name list, or `git commit --only -- <paths>` transcript proves the mandated procedure used by the Executor. | **pending — coordinator**; proposed `not material — owed but forbidden to pay retrospectively`: Git proves the safe result, while manufacturing missing historical shell output would violate Safety and Execution Honesty and Trace Discipline. |
| 3 | RF §6 observation 1 / Verify discrepancy 3 | Low | `HL-TFW_20260902-111644_CRATM.md` §7.2 #2/#4 | Human authority and Assurance are quoted correctly but labeled with stale NS2 ordinals 4/6 rather than current 5/7. Exact citation inspectability is reduced; meaning and application still hold. | **pending — coordinator**; proposed `promoted — TFW_20260902-111644_CRATM`, whose existing Phase E sweep owns remaining citation correction. Existing target: `workspace/2026/TFW_20260902-111644_CRATM/status.md`. |
| 4 | Verify discrepancy 4 | Low | `phase-b/HL__phase-b__named_principals.md` §7.2 B9 | The source file and FA15ES S6 item exist and support the application, but the link omits the rendered `-free` anchor suffix; ONB row #45 inherits the broken chain. | **pending — coordinator**; proposed `promoted — TFW_20260902-111644_CRATM`, whose existing Phase E sweep owns the remaining citation audit/correction. Existing target: `workspace/2026/TFW_20260902-111644_CRATM/status.md`. |

### Coordinator rulings — Round 2

Ruled by the Phase B Coordinator on 2026-09-06. These rulings close every `pending — coordinator`
proposal above without changing the first-round Reviewer record.

| Proposal | Ruling | Closed bound or disposition |
|---|---|---|
| §4 item 1 / §5 item 1 | **Accepted — rung 1; payment bound to Phase B Round 2** | The existing approved TS remains the implementation order and lifecycle remains `RF` until the same Executor accepts the return. The same Executor appends the required Round 2 ONB trace, then appends an EV Round 2 record containing the complete executable validator program, the exact 17 documented fixture payloads, and fresh 17/17 output. The Executor appends the current RF evidence summary while preserving the first-round provenance limitation. No VALUE file may change; Candidate remains exactly `0ee39046b760d6d3e8d837c2377e49c1c95668bd`, with no later VALUE commit. The return goes to the same Reviewer task for independent replay and verdict. Observable completion is a replayable preserved program, 17/17 independent replay, an unchanged Candidate, and a new review verdict. |
| §5 item 2 | **Accepted — not material; owed but forbidden to pay retrospectively** | Exact Candidate membership, attribution, and non-contamination are independently proven. Missing historical shell output must not be manufactured; no retrospective transcript is permitted. |
| §5 item 3 | **Accepted — promoted to `TFW_20260902-111644_CRATM`** | The existing task directory, `status.md`, and `PROPOSAL__TFW_20260902-111644_CRATM.md` already exist. Proposal §6 item 9 and frozen Master HL Phase E deliverable 6 / DoD 17 own review-debt disposal; Phase E will correct the two stale North Star ordinals. Phase B does not edit the frozen Master HL. |
| §5 item 4 | **Accepted — promoted to `TFW_20260902-111644_CRATM`** | The same existing proposal and frozen Phase E review-debt sweep own the broken Phase B B9 anchor. Phase B does not widen its evidence-only return or amend a frozen planning artifact. |

**Route:** existing approved `TS__phase-b__named_principals.md` plus this ruled live REVIEW govern
Round 2. Start `/tfw-handoff` in the same Executor task; after its RF return, start `/tfw-review` in
the same Reviewer task.

## 6. Traces Updated

- [x] Phase status and journal inspected; 🔄 REVISE authorizes no lifecycle transition or event from the Reviewer, so lifecycle remains `RF`.
- [ ] HL status if phase completes; §5 has no pending row — not applicable because the phase is not approved and four disposition proposals await one Coordinator ruling.
- [x] Stale project files checked — the project structural check is green; citation defects are §5 rows 3–4.
- [x] tfw-docs: N/A — REVISE does not enter KNW.
- [x] tfw-knowledge: N/A — REVISE does not enter KNW and RF/REVIEW contain no Fact Candidates.

## 7. Fact Candidates

No fact candidates.

> fact-candidates: processed 2026-09-06

---

*REVIEW — TFW_20260902-111644_CRATM / Phase B: Named principals | 2026-09-06*
