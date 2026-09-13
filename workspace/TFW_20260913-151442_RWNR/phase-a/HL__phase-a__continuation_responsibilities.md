# Phase HL — TFW_20260913-151442_RWNR / A: Rehome continuation responsibilities

> **Date**: 2026-09-13
> **Author**: robert, Coordinator unit `01a09a92-18fb-7da1-a639-6a86844bf147`
> **Status**: 🟡 DERIVED — Phase A TS draft awaits owner approval; `status.md` owns live state
> **Parent**: [Master HL](../HL-TFW_20260913-151442_RWNR.md), Phase A
> **Governing master contract**: frozen by `saubakirov`; A1 re-freeze `74e63242a1a713c8a2c4490edda24f84bfc68153`
> **G1**: C2 approved with binding minimal-Plan and identity-continuity clarification in [dispatch 4ded](../journal/20260913-190312__dispatch__4ded.md)
> **Planning baseline**: `f6e85aa898061779c6b37bba34dc97e28c76f01f`
> **Research basis**: [Iteration 2 RES](../research/iter2/RES.md) · [Extract](../research/iter2/3_extract.md) · [Challenge](../research/iter2/4_challenge.md)

## Parent Derivation

This phase implements only master HL §4 Phase A and inherits master DoD 4–10 and 15–17, DoF 2–5, 9, 10 and 13, and all master principles without changing them. Vision, acceptance, failure and principles remain solely in the frozen master HL.

The owner's G1 clarification is a free deliverable refinement under `conventions.md` → `HL Contract` rule 6. It specifies how the already-approved Phase A outcome is met: make the smallest routing-only Plan correction, re-resolve AT and session identity on every continuation, distinguish the named exact root from same-principal children, and stop on unresolved identity/mandate facts. The unchanged master DoD and DoF accept all of those results, so no frozen tripwire or §12 amendment is created.

## Starting Point

- At immutable baseline `f6e85aa`, canonical Plan and its two tracked full-copy receivers are byte-identical to blob `81f7d78bd7f270871bc4ee325789a3f457059812`; strict UTF-8 Unicode `\S+` counts Plan at 2,021 words.
- Plan has a session-identity checkpoint and an approved-TS handoff route, but it does not yet own the exact existing-task/historical/phase/state pre-route from RES Extract E1.
- The central `Session identity` and AT continuation contracts already own the root predicate, title grammar, authoritative sources, readback behavior, and missing/ambiguous-fact wait. Plan should reference those contracts, not copy their prose.
- Resume remains present and authoritative during Phase A. Its workflow, skill, manifest/config rows, adapter receivers, docs and history are outside the Phase A mutation set.
- Research fixed the no-loss envelope: the 28-case pure routing model, four receiver migration outcomes including `TARGET_CURRENT`, 179 immutable task traces, three additive aggregates, and `B = 2,737` with Candidate Plan ≤1,200.
- This is the first implementation phase, so the predecessor-RF Pre-TS Gate is not applicable.

## Finished Phase View

```text
/tfw-plan <exact task-or-phase>
          |
          +-- resolve active/history scope and authoritative carriers -- invalid/history --> report + STOP
          |
          +-- re-resolve continuation AT/identity every time
          |       exact named root --------------------> LEAD · {handle} · {TASK}
          |       non-AT or same-principal child ------> PLAN · {TASK}
          |       absent/ambiguous/stale/wrong root ---> ask/report + STOP, no claimed LEAD
          |       title transport ---------------------> reapply + exact readback
          |
          +-- inspect only; select no phase; perform no lifecycle effect
                  Plan | Research | Handoff | Review | Coordinator control | wait/terminal

Phase A acceptance: routing/no-mutation scenarios pass, Plan ≤ 1,200 words,
complete C < 2,737, history and receiver-migration oracles pass, Resume remains intact.
Any miss: C1 keeps Resume.
```

## Execution Boundary

### Included

- Rewrite and deduplicate only canonical `.tfw/workflows/plan.md` enough to add one early existing-task inspector/router before the Knowledge Gate and every Plan write while meeting the independent 1,200-word cap.
- Synchronize only the tracked byte-copy Plan receivers in `.agents/workflows/` and `.claude/commands/`; the thin Codex Plan skill remains unchanged.
- Apply the full Extract E1 lifecycle table, phase-local truth, historical-only stop, exact Coordinator-control address, and route-output-not-invocation boundary.
- Add source-derived tests for the 28 routing cases and explicit continuation identity cases: ordinary non-AT Plan; valid named AT exact root; same-principal child; absent, ambiguous, stale, or wrong-root mandate/identity; and per-continuation title reapply plus exact readback.
- Make every pre-route case byte/path read-only, including cases that later continue into existing Plan gates.
- Establish executable Phase A assurance for the four-class version-addressed receiver preflight, connected-group refusal, ten-command/four-adapter convergence, repeat no-diff behavior, split history oracle, and comparable word counter.
- Produce an immutable Candidate and evidence package. C1 remains the terminal fallback for any failed condition.

### Excluded

- Deleting, redirecting, renaming, or editing Resume; changing its skill, manifest/config registration, adapter receivers, live documentation, or update migration guide.
- Adding a continuation helper, replacement public command, alias, tombstone, registry, hidden dispatcher, or behavior-bearing adapter.
- Letting Plan execute Research, Handoff, Review, close/repair, lifecycle transitions, phase choice, approvals, or any write authorized by another workflow.
- Inventing a release version or migration filename; Phase B and G2 own actual retirement/update effects.
- Rewriting the 179 historical task traces or pre-existing bytes/line order in the three aggregate histories.
- TKL mutation, knowledge consolidation, release work, review, or owner TS approval.

## Exact Continuation Boundary

The Phase A TS binds the complete state routing contract from RES Extract E1. Its identity refinement has five observable classes:

| Continuation facts | Required result |
|---|---|
| No AT mandate governs the selected task/phase | ordinary `PLAN · {TASK}[ · {PHASE}]`; continue only through the state route |
| Valid selected agent, acting handle match, exact mandate root equals current Coordinator unit | `LEAD · {handle} · {TASK}[ · {PHASE}]`; exact readback before routing |
| Same selected principal, but current unit is a child including a Coordinator child | ordinary `PLAN` title with no handle; never inherit root identity or grant |
| AT continuation is indicated but mandate/selection/handle/root/current-unit/direct-dispatch fact is absent, ambiguous, stale, foreign, or wrong-root | name the defect, ask or report through the direct channel, and stop without writes or a claimed LEAD title |
| Rename/readback transport is unavailable or altered after authoritative identity resolved | follow central fail-soft behavior: report once and continue unclaimed; never treat the visible title as authority |

Every continuation repeats resolution and title application from task/phase state, ordered journal, governing HL and direct dispatch. Chat history, the prior visible title, principal attribution alone, OS identity, and a forwarded selection are not sources.

## File and Assurance Topology

| Surface | Phase A treatment |
|---|---|
| `.tfw/workflows/plan.md` | sole canonical behavior change; routing only, strict cap ≤1,200 |
| `.agents/workflows/tfw-plan.md`, `.claude/commands/tfw-plan.md` | exact byte copies after canonical behavior passes |
| `docs/scripts/test_runtime_context.py` | source-derived routing/identity scenarios, precedence and semantic mutants |
| `docs/scripts/test_repository_contracts.py` | no-mutation, copy parity, history, receiver migration and word-accounting oracles |
| `phase-a/evidence/` | immutable Candidate receipts, raw test output and per-AC EV; never runtime input |

The exact owner-facing VALUE proposal is three modified paths and at most 900 touched text LOC. The Plan full-copy receivers are VALUE for repository delivery but contribute once at canonical source to A1's instruction-surface formula after byte parity. Tests are ASSURANCE; phase control/evidence files are TRACE.

## Dependencies and Fallback

| Dependency | Phase-A state |
|---|---|
| Frozen master and A1 | satisfied by re-freeze `74e6324` |
| G1 C2 decision | satisfied by direct owner approval and dispatch 4ded |
| Exact TS/VALUE approval | pending; no Executor dispatch or implementation before the owner approves this package |
| Phase B | blocked until independent Phase A APPROVE and accepted control records |
| C1 | remains available without amendment; any acceptance miss keeps Resume and blocks retirement |

## Phase-Local Risks

| Risk | Control |
|---|---|
| Compression deletes a current Plan gate | source-derived anchors, full relevant suites, 28-state tests and deliberate mutants |
| A child inherits the LEAD name or an invalid root silently becomes ordinary Plan | explicit non-AT versus invalid-AT cases; authoritative re-resolution and stop-before-write assertions |
| Tests model intent but not repository mutation | temporary-repository byte/path before/after evidence for every pre-route result |
| Phase A accidentally begins retirement | exact diff allowlist excludes all Resume/manifest/config/migration/docs paths |
| History or foreign receiver material is damaged later | immutable split-history and four-class all-preflight oracles become Phase B prerequisites |
| Accounting hides moved text in another instruction source | baseline-to-Candidate instruction-domain scan; unclassified additions fail and select C1 |

## Knowledge Application

Master HL §7.2 rows 1–32 remain controlling. Row 33 adds the directly relevant P4 application: central `Session identity` and AT continuation rules own the identity predicate and wait behavior, while Plan owns only the checkpoint and route. No new fact candidate or knowledge mutation arises from this derivation.

---

*Phase HL — TFW_20260913-151442_RWNR / A: Rehome continuation responsibilities | 2026-09-13*
