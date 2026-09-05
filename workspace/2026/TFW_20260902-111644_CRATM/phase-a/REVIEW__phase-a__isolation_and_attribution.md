# REVIEW — TFW_20260902-111644_CRATM / Phase A: Isolation and attribution for concurrent work

> **Date**: 2026-09-05
> **Author**: Codex (Reviewer)
> **Verdict**: 🔄 REVISE
> **RF**: [RF Phase A](RF__phase-a__isolation_and_attribution.md)
> **TS**: [TS Phase A](TS__phase-a__isolation_and_attribution.md), approved at `29a5c8a98af52493d142c9872ca97a22a5db4eda`
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`

---

## 1. Map

The Executor added the approved canonical worktree, exact-path staging, and producer-attributed
landing protocol, with short Handoff/Review enforcement edges and four byte-identical tracked copies.
The immutable Candidate is `e3f3b3c149f0ef03157f65890d89438d11b8fe6e`; later commits add only
Phase A TRACE. RF marks every AC complete while its own EV accurately leaves the actual post-review
cross-session landing as `DEFERRED`.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|---|---|---|
| V-files | All seven claimed VALUE files | VERIFIED | 7/7 opened after escalation; canonical headings, both checkpoint edges, and all four tracked-copy paths match RF claims. |
| V-tests | D75/runtime-context gates and full repository suite | VERIFIED | Independent Reviewer runs: targeted 2/2 in 26.31 s; full `python -m pytest docs/scripts` 306/306 in 284.11 s. |
| V-staging | Exact-path Candidate trace and an unrelated-staged-sibling fixture | VERIFIED | Executor transcript shows complete status, exact seven cached names, and `commit --only`; independent fixture committed only `selected.md` and preserved staged `sibling.md`. |
| V-parity | Canonical/adapter copies | VERIFIED | Handoff triplet blob `9f24b5c…`; Review triplet blob `e84d551…`; working-tree SHA-256 groups also match. |
| V-citations | Master/Phase HL §7.2 and ONB §7 | PARTIAL | 98/98 artifact-citation occurrences resolve; 96/98 are exact. Master #2 and #4 use stale NS2 ordinals 4/6 for live principles 5/7; ONB already identifies both. |
| V-landing | Actual post-review crossing landing and exact Candidate retention | BLOCKED | EV E3b is `DEFERRED`. No qualifying landing is on current lineage. Historical `87c26bb…` predates REVIEW, contains no review artifact, and is not an ancestor of review-ready HEAD. |
| V-accounting | Independent value-bearing replay | VERIFIED | Approval `29a5c8a…`; Baseline `11888e5…`; Candidate `e3f3b3c…`; seven literal `M` VALUE paths; 97 additions, 17 deletions, 114 touched LOC; binary N/A; keep-one-phase trigger; immutable 7/160 denominator; no authority threshold or HC-1 change; NUL-safe `--name-status` and `--numstat` commands reproduced the EV exactly. |

Raw log: [review/verify.md](review/verify.md). Verification limit: a post-review landing cannot be
observed before this REVIEW exists in a durable Reviewer TRACE; no substitute SHA or pre-review
landing was accepted.

## 3. Judge

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD / all TS AC | ❌ | AC-1, AC-2 and AC-4–AC-6 reproduce; AC-3 lacks its required actual reviewed landing evidence. |
| 2 | Purpose and design | ✅ | Contract-baseline HL and NS1 require inspectable authority and continuation; isolation plus attributed path history directly prevents foreign staging/misattribution harm. Design stays prose over Git, no lock/runtime/provider canon. |
| 3 | Debt disposed by consequence | ✅ | Four §5 rows have concrete pending Coordinator proposals, existing targets, and named consequences or absences; none uses a bare priority/backlog. |
| 4 | Style and standards | ✅ | Literal scope, unique headings, named prohibitions, exact staging, Candidate order, Markdown checks, and copy parity hold. |
| 5 | Observations collected | ✅ | RF's three observations are real and source-backed; each is triaged in §5. |
| 6 | RF §7–§9 complete | ✅ | Explicit no Fact Candidates, explicit no Strategic Insights, and a coherent lifecycle diagram. |
| 7 | Evidence exists | ✅ | All seven EV rows and every TS evidence field exist; statuses are valid and candid. |
| 8 | Evidence is sufficient | ❌ | Six VERIFIED rows establish their claims; E3b's honest DEFERRED status cannot establish RF §3's completed AC-3 checkmark. |
| 9 | Backward compatibility | ✅ | Selective reads, Candidate/accounting/Purpose order, unique headings, adapter parity, structure, and 306-test suite all hold. |
| 10 | Safety | ✅ | No secret, executable surface, destructive cleanup, or irreversible operation was introduced or performed. |

Purpose outcome: **aligned**, not `not fit for purpose`, and the reference set is internally coherent.
The precise clause, material harm, and independent baseline recovery are recorded in
[review/judge.md](review/judge.md).

## 4. Verdict

**🔄 REVISE**

The implementation, design, compatibility, tests, citations' substantive meaning, and immutable
accounting are sufficient. The verdict remains open because [§2 V-landing](#2-verify) and Judge rows
1/8 show one explicit contract gap: RF §3 claims AC-3 complete while EV E3b says the required actual
post-review landing/reachability observation has not happened. The approved TS already contains the
complete rule and evidence condition, so no TS revision or frozen-HL change is proposed.

### If REVISE — proposals to coordinator

1. **Close the actual reviewed crossing-landing evidence gap** — **basis:** governing TS AC-3,
   especially its Gate/Evidence requirement for the Phase A landing, producer-attributed path
   history, and exact Candidate reachability before cleanup. **Owner:** `saubakirov` from Phase A
   `status.md`. **Proposed route:** rung 1, because the repair changes neither the approved TS nor a
   frozen HL claim. **Observable completion:** the Coordinator rules this proposal in the live REVIEW;
   a new post-review Coordinator landing on the accepted integration lineage contains the durable
   Reviewer result, is recoverable by the producer task/phase and acting landing role, retains exact
   Candidate `e3f3b3c149f0ef03157f65890d89438d11b8fe6e`, and is verified before any worktree cleanup;
   the same Executor then records the ruled return evidence under the existing TS, after which
   `/tfw-review` verifies the returned lineage.

The two stale citation ordinals and the two other RF observations do not cite a failed Phase A AC or
frozen claim and therefore do not widen the REVISE round; they are disposition proposals in §5 only.

## 5. Tech Debt Collected and Disposed

| # | Source | Severity | File | Description | Disposition |
|---|---|---|---|---|---|
| 1 | Verify discrepancy 1 / Judge rows 1, 8 | High | Phase A integration history and `EV__phase-a__isolation_and_attribution.md` E3b | RF marks AC-3 complete without a qualifying post-review landing and exact-Candidate reachability observation. Leaving it open makes the new crossing rule unproved on its own delivery and permits cleanup without the required durable chain. | **pending — coordinator**; proposed `paid — phase-a` through the rung-1 observable completion in §4. The existing target is `workspace/2026/TFW_20260902-111644_CRATM/phase-a/`. |
| 2 | RF §6 observation 1 | Medium | `.tfw/adapters/manifest.yaml:85` | Manifest names plural `.agents/workflows/…` while the approved TS and live tracked copies use singular `.agent/workflows/…`. If unresolved, a future manifest-driven sync can miss the live copy and damage continuation/parity. | **pending — coordinator**; proposed `promoted — TFW_20260902-111644_CRATM` because the existing master task owns the Phase E adapter sweep. Target exists at `workspace/2026/TFW_20260902-111644_CRATM/status.md`. |
| 3 | RF §6 observation 2 / Verify discrepancies 2–3 | Low | `HL-TFW_20260902-111644_CRATM.md` §7.2 #2/#4 | NS2 labels say principles 4/6 while the quoted live clauses are 5/7. Exact citation inspectability is reduced, but the links, quoted clauses, and applications remain semantically correct. | **pending — coordinator**; proposed `not material — owed but forbidden to pay in Phase A`: the approved seven-path selector excludes Master HL and Reviewer/Executor Role Locks forbid the edit; no Phase A VALUE or purpose claim changes. |
| 4 | RF §6 observation 3 | Low | `workspace/2026/TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md:9` | Immutable other-task event summary is 123 code points against the 120 census ceiling, unchanged from Baseline. | **pending — coordinator**; proposed `not material — not owed by Phase A`: the event is immutable, outside this task, and affects only an extra non-gating task census; it changes no Phase A purpose, authority, inspectability, or continuation result. |

## 6. Traces Updated

- [x] Phase status and journal inspected; 🔄 REVISE authorizes no lifecycle transition or event from the Reviewer.
- [ ] HL status if phase completes; §5 has no pending row — not applicable yet because the phase is not approved and all four disposition proposals await Coordinator ruling.
- [x] Stale project files checked — project structural check is green; the known RDP task-census item is §5 row 4.
- [x] tfw-docs: N/A — REVISE does not enter KNW.
- [x] tfw-knowledge: N/A — REVISE does not enter KNW and RF/REVIEW contain no Fact Candidates.

## 7. Fact Candidates

No fact candidates.

---

*REVIEW — TFW_20260902-111644_CRATM / Phase A: Isolation and attribution for concurrent work | 2026-09-05*
