# REVIEW — TFW_20260902-111644_CRATM / Phase A: Isolation and attribution for concurrent work

> **Date**: 2026-09-05
> **Author**: Codex (Reviewer)
> **Verdict**: ✅ APPROVE — current; historical 🔄 REVISE and Coordinator ruling remain below
> **RF**: [RF Phase A](RF__phase-a__isolation_and_attribution.md)
> **TS**: [TS Phase A](TS__phase-a__isolation_and_attribution.md), approved at `29a5c8a98af52493d142c9872ca97a22a5db4eda`
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> **Amended**: Round 2 in the same review cycle after final-integration tip `050bfb3bf69e3be4dd65fd62d6ba107a625ade3e`

---

## 1. Map

The Executor added the approved canonical worktree, exact-path staging, and producer-attributed
landing protocol, with short Handoff/Review enforcement edges and four byte-identical tracked copies.
The immutable Candidate is `e3f3b3c149f0ef03157f65890d89438d11b8fe6e`; later commits add only
Phase A TRACE. RF marks every AC complete while its own EV accurately leaves the actual post-review
cross-session landing as `DEFERRED`.

### Round 2 map update

Coordinator ruling `091cf865e8c58bd15db87ada321c0bc995e6ae3e` accepted the single rung-1
return. Qualifying reviewed landing `bb9c86f90208d9d58c62fe695e6d97d238ca28d7`, same-Executor
return `6d69eaafcbe80431d03ad12af664080cc0eccbba`, and final integration landing
`050bfb3bf69e3be4dd65fd62d6ba107a625ade3e` now supply the missing TRACE. Candidate,
all seven VALUE paths, the approved TS, and accounting remain unchanged.

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

### Round 2 verification update

| # | What was checked | Result | Evidence |
|---|---|---|---|
| R2-landing | Qualifying post-review landing | VERIFIED | `bb9c86f…` has approval + reviewed/ruling parents, tree equality with ruling, exact subject/trailers, and chronological REVIEW/ruling ancestry. |
| R2-history | Producer/landing path history and exact Candidate | VERIFIED | First-parent VALUE history exposes `bb9c86f…`; full history exposes `e3f3b3c…`; Candidate resolves and remains an ancestor. |
| R2-return | Same-Executor return and final Coordinator landing | VERIFIED | `b874e38…` → `df1013f…` → `6d69eaa…` changes only authorized task-local TRACE; `050bfb3…` lands that exact return. |
| R2-exclusion | Failed attempt and cleanup precondition | VERIFIED | `87c26bb…` is outside final ancestry and preserved on its separate ref; Executor worktree remains registered; no cleanup occurred. |
| R2-value/accounting | Late VALUE, governing TS, immutable replay | VERIFIED | Candidate→final seven-path diff is empty; TS blob remains `0d90b1dd…`; accounting remains 7, +97/−17, 114 against 7/160. |
| R2-evidence | Current RF/EV verdict | VERIFIED | E3b-R2 reproduces; current set is 7/7 VERIFIED, 0 DEFERRED/BLOCKED/N/A while historical E3b remains visible. |

Round 2 ran `git diff --check` and the project structural check successfully. The same Reviewer did
not repeat the full suite because no VALUE path changed after the already independent 2/2 and 306/306
passes. Full command evidence and limits are appended to [review/verify.md](review/verify.md).

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

### Round 2 current judgment

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD / all TS AC | ✅ | E3b-R2 and independent replay close AC-3; every other AC remains green. |
| 2 | Purpose and design | ✅ | Baseline/NS1 alignment is unchanged; the missing inspectable landing chain now exists. |
| 3 | Debt disposed by consequence | ✅ | Coordinator ruled all four rows once; current dispositions below contain no pending item. |
| 4 | Style and standards | ✅ | Exact-path TRACE return, preserved history, clean diff and structure. |
| 5 | Observations collected | ✅ | Three original observations remain visible and ruled; no new observation. |
| 6 | RF §7–§9 complete | ✅ | No new Fact Candidate/insight; the lifecycle diagram remains accurate. |
| 7 | Evidence exists | ✅ | E3b-R2 is appended; historical E3b is not rewritten. |
| 8 | Evidence is sufficient | ✅ | Metadata, tree, ancestry, history, trailers, refs, worktree, and no-late-VALUE checks establish AC-3. |
| 9 | Backward compatibility | ✅ | VALUE blobs did not move; first-round tests remain applicable; TRACE checks pass. |
| 10 | Safety | ✅ | Exact Candidate is durable, failed trace preserved, and no cleanup was performed. |

Purpose outcome: **aligned**, not `not fit for purpose`, and the reference set is internally coherent.
The precise clause, material harm, and independent baseline recovery are recorded in
[review/judge.md](review/judge.md).

## 4. Verdict

### Round 1 verdict — historical

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

### Coordinator rulings — 2026-09-05

| Item | Ruling | Governing bound / disposition |
|---|---|---|
| §4 proposal 1 / §5 row 1 | **✅ ACCEPTED — rung 1** | The existing approved TS remains the complete implementation order; no TS sibling and no frozen-HL amendment are authorized. The closed return bound is exactly the proposal's observable completion: create one qualifying post-review Coordinator landing on the accepted Reviewer lineage, preserve exact Candidate `e3f3b3c149f0ef03157f65890d89438d11b8fe6e`, verify attribution/path history/reachability before cleanup, then return only the resulting landing evidence to the same Executor and Reviewer. Historical `87c26bbcea64f3e2dcf4b6ebd094b4dc0da769ff` is preserved as a rejected, non-qualifying pre-review attempt and is excluded from final ancestry. |
| §5 row 2 | **✅ ACCEPTED — promoted** | The stale manifest target is outside Phase A's seven-path selector and remains unchanged. It is promoted to the existing master task `TFW_20260902-111644_CRATM`, whose Phase E adapter sweep must dispose of the singular/plural target mismatch before that task closes. |
| §5 row 3 | **✅ ACCEPTED — not material for Phase A** | The two stale NS2 ordinals reduce exact citation labeling but do not change the resolving links, quoted clauses, implementation, accounting, or Phase A purpose. The Master HL is outside the approved selector and is not edited in this round. |
| §5 row 4 | **✅ ACCEPTED — not owed by Phase A** | The immutable RDP event predates Baseline, is byte-identical at Candidate, belongs to another task, and affects only a non-gating census. Phase A neither edits it nor widens HC-1. |

All four Reviewer proposals are now ruled once. Only the accepted rung-1 return is executable; the
governing artifact remains the approved TS plus the closed bound above. Start `/tfw-handoff` with the
same Executor after the qualifying Coordinator landing exists.

### Round 2 current verdict

**✅ APPROVE**

The accepted rung-1 condition is paid. Round 2 independently reproduces the qualifying landing,
producer/acting-role attribution, reviewed lineage, exact Candidate reachability, excluded failed
attempt, final Executor-return landing, and preserved cleanup precondition. There is no late VALUE,
the immutable 7/+97/−17/114 accounting remains exact, and current EV is 7/7 VERIFIED. All ten current
Judge rows pass. The historical REVISE and its Coordinator ruling remain the visible trace of why the
second review was required.

## 5. Tech Debt Collected and Disposed

### Round 1 proposals — historical

| # | Source | Severity | File | Description | Disposition |
|---|---|---|---|---|---|
| 1 | Verify discrepancy 1 / Judge rows 1, 8 | High | Phase A integration history and `EV__phase-a__isolation_and_attribution.md` E3b | RF marks AC-3 complete without a qualifying post-review landing and exact-Candidate reachability observation. Leaving it open makes the new crossing rule unproved on its own delivery and permits cleanup without the required durable chain. | **pending — coordinator**; proposed `paid — phase-a` through the rung-1 observable completion in §4. The existing target is `workspace/2026/TFW_20260902-111644_CRATM/phase-a/`. |
| 2 | RF §6 observation 1 | Medium | `.tfw/adapters/manifest.yaml:85` | Manifest names plural `.agents/workflows/…` while the approved TS and live tracked copies use singular `.agent/workflows/…`. If unresolved, a future manifest-driven sync can miss the live copy and damage continuation/parity. | **pending — coordinator**; proposed `promoted — TFW_20260902-111644_CRATM` because the existing master task owns the Phase E adapter sweep. Target exists at `workspace/2026/TFW_20260902-111644_CRATM/status.md`. |
| 3 | RF §6 observation 2 / Verify discrepancies 2–3 | Low | `HL-TFW_20260902-111644_CRATM.md` §7.2 #2/#4 | NS2 labels say principles 4/6 while the quoted live clauses are 5/7. Exact citation inspectability is reduced, but the links, quoted clauses, and applications remain semantically correct. | **pending — coordinator**; proposed `not material — owed but forbidden to pay in Phase A`: the approved seven-path selector excludes Master HL and Reviewer/Executor Role Locks forbid the edit; no Phase A VALUE or purpose claim changes. |
| 4 | RF §6 observation 3 | Low | `workspace/2026/TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md:9` | Immutable other-task event summary is 123 code points against the 120 census ceiling, unchanged from Baseline. | **pending — coordinator**; proposed `not material — not owed by Phase A`: the event is immutable, outside this task, and affects only an extra non-gating task census; it changes no Phase A purpose, authority, inspectability, or continuation result. |

### Round 2 current dispositions

The table below transcribes, but does not re-rule, the Coordinator decisions already committed in
`091cf865e8c58bd15db87ada321c0bc995e6ae3e`; it supersedes the historical pending cells above.

| # | Current disposition | Existing target and consequence |
|---|---|---|
| 1 | **paid — phase-a** | Qualifying `bb9c86f…`, E3b-R2, and final `050bfb3…` close the AC-3 evidence harm in the existing Phase A directory. |
| 2 | **promoted — TFW_20260902-111644_CRATM** | Existing master task/status owns the Phase E adapter sweep; the singular/plural manifest risk remains visible there. |
| 3 | **not material — owed but forbidden to pay in Phase A** | Exact ordinals affect labeling, not resolving links, quoted clauses, current VALUE, accounting, or purpose; Master HL is outside the selector. |
| 4 | **not material — not owed by Phase A** | Immutable other-task history affects only a non-gating census and changes no Phase A purpose, authority, inspectability, or continuation result. |

## 6. Traces Updated

### Round 1 trace state — historical

- [x] Phase status and journal inspected; 🔄 REVISE authorizes no lifecycle transition or event from the Reviewer.
- [ ] HL status if phase completes; §5 has no pending row — not applicable yet because the phase is not approved and all four disposition proposals await Coordinator ruling.
- [x] Stale project files checked — project structural check is green; the known RDP task-census item is §5 row 4.
- [x] tfw-docs: N/A — REVISE does not enter KNW.
- [x] tfw-knowledge: N/A — REVISE does not enter KNW and RF/REVIEW contain no Fact Candidates.

### Round 2 current trace and routing

- [x] Phase lifecycle routed `RF → KNW` after ✅ APPROVE, with one task-local transition event written from the observed clock.
- [x] Current §5 has no pending row; all dispositions reflect the committed Coordinator ruling.
- [x] Master task remains `PHASES`; no prohibited task-level phase rollup or HL edit was made.
- [x] tfw-docs: Applied — updated Sections 1–2 (Architecture Map, D77, and Key Artifacts).
- [x] tfw-knowledge: N/A — RF/REVIEW contain no Fact Candidates.

## 7. Fact Candidates

No fact candidates.

> fact-candidates: processed 2026-09-05

---

*REVIEW — TFW_20260902-111644_CRATM / Phase A: Isolation and attribution for concurrent work | 2026-09-05*
