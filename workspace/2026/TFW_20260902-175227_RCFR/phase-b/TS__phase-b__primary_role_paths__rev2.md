# TS revision 2 — TFW_20260902-175227_RCFR / Phase B: Proof and Rung Routing Repair

> **Date**: 2026-09-04
> **Author**: Codex (Coordinator), acting on behalf of `saubakirov`
> **Status**: ✅ APPROVED — `saubakirov`; standing authorization to complete Phase B and explicit routing correction issued 2026-09-04
> **Supersedes**: [TS revision 1](TS__phase-b__primary_role_paths.md) — revision 1 remains immutable history
> **Returned by**: [Phase B REVIEW](REVIEW__phase-b__primary_role_paths.md) — 🔄 REVISE, two rung-1 proof defects and one rung-2 routing defect
> **Reviewed candidate**: `272a7cf737c84958d81c41257cc9c2568c74ee0f`
> **Master HL**: [Runtime Context Footprint Reduction](../HL-TFW_20260902-175227_RCFR.md), frozen baseline `2728dae78d55f6cb7daa39c82874ad5b43621f8a`
> **Ordered by**: Coordinator `saubakirov` via Codex

---

## 1. Round and Coordinator Rulings

The implementation direction, fixed baseline, role compression, adapter topology, budgets, and
all green behavior accepted by the REVIEW remain in force. This revision orders only the three
cited findings below. The Coordinator rules all three proposals in one act:

| Item | Rung | Coordinator ruling | Basis | Observable completion |
|---|---:|---|---|---|
| R1 | 1 | **Accepted and ordered in this phase.** Complete the Researcher candidate graph and replace the overstated evidence. | Revision 1 AC-1 bullets 2–3; AC-6 bullets 3–4; frozen DoD 3 and Quality Contract 1. | Both modes enumerate all four stage templates, an omitted-stage mutant fails independently, and exact recomputed reductions remain above 30%. |
| R2 | 1 | **Accepted and ordered in this phase.** Replace anchor-removal family checks with genuine output-changing semantic mutants. | Revision 1 AC-6 bullets 1–2. | Each P/R/E/V/C/A family first produces a changed semantic record, then the independent comparison rejects it. |
| R3 | 2 | **Accepted; discharged by this TS revision.** Add `.tfw/conventions.md` to the authorized surface and establish one rung-specific route across every executable consumer. | Revision 1 AC-4 bullet 2 and its Evidence contract; frozen DoD 6/10, DoF 3, Principles 2/6, and Quality Contract 4. | Rung 1, 2, and 3 cases agree on recipient, governing artifact, lifecycle effect, and hard stop; contradictory-clause mutants fail. |

No item is promoted, rejected, deferred, or routed to an HL amendment. R1 and R2 were already
inside revision 1; R3 alone changes the TS and therefore legitimately keeps this phase in
`TS_DRAFT` until the same Executor accepts revision 2.

## 2. Authoritative Three-Rung Decision

`conventions.md` → `The 🔄 REVISE route` is the single routing authority. Workflows consume it and
must not restate a competing universal route.

1. The Reviewer identifies the breached TS criterion or frozen claim, assigns a rung, proposes the
   item, and stops without ruling a disposition or changing lifecycle merely because the verdict is
   REVISE.
2. The Coordinator rules every proposal once at review close.
3. **Rung 1 only:** the existing approved TS remains governing. The Coordinator records the ruled,
   closed bound in the live REVIEW; lifecycle remains `RF` until the same Executor accepts the
   bounded return, then the Executor records `RF → ONB`. No TS sibling is created.
4. **Any rung 2:** the Coordinator writes one TS sibling for the whole mixed round, records the
   rulings and basis there, sets its authority and `TS_DRAFT` once, and the same Executor later
   records `TS_DRAFT → ONB`.
5. **Rung 3:** the Coordinator files the `amendment_escalated` event and HL §12 proposal and waits
   for the owner. No Executor is dispatched until the owner verdict leaves an executable bound.
6. Reviewer, Coordinator, and Executor hard stops name the next legal role and artifact for the
   applicable rung; none may collapse all REVISE verdicts into the rung-2 route.

This preserves D72's citation bar and named acceptance authority while correcting its over-broad
derived claim that every round needs a TS revision. `KNOWLEDGE.md` is not an Executor artifact and
must not be edited in this round; after APPROVE, `/tfw-docs` must reconcile the D72/Correction Loop
description with the verified route before Phase B closes.

## 3. Exact Scope

### Implementation and test files permitted in this round

| File | Action | Purpose |
|---|---|---|
| `.tfw/conventions.md` | MODIFY | make status text, three-rung table, Role Lock, and Hard Stop mutually consistent |
| `.tfw/workflows/plan.md` | MODIFY | branch post-review handling: live REVIEW bound for rung 1, TS revision only for rung 2, amendment route for rung 3 |
| `.tfw/workflows/review.md` | MODIFY | propose without generic state movement; return to Coordinator for one ruling act |
| `.tfw/workflows/handoff.md` | MODIFY | accept either a ruled rung-1 REVIEW bound under the same TS or a rung-2/mixed TS revision |
| `.claude/commands/tfw-{plan,handoff,review}.md` | MODIFY | exact copies of the three canonical workflows |
| `.agent/workflows/tfw-{plan,handoff,review}.md` | MODIFY | exact legacy installed copies of the three canonical workflows |
| `docs/scripts/test_runtime_context.py` | MODIFY | complete Researcher graph, output-changing family mutants, and rung-specific semantic cases |
| `docs/scripts/test_integration.py` | MODIFY | exact copy/routing/contradiction and clean-receiver regressions |

No other implementation, test, adapter, skill, template, manifest, configuration, or knowledge file
may change. In particular, do not modify `KNOWLEDGE.md`, `.tfw/knowledge_state.yaml`, `tasks/`,
`TFW-36`, the immutable RDP event, the master/phase HL, revision 1, or the live REVIEW.

### Cumulative budget

Revision 1 changed 23 implementation/test files and 1,005 LOC. Revision 2 authorizes one new
distinct implementation path, `.tfw/conventions.md`, and reopens only the eleven listed existing
paths. The cumulative ceiling is **24 distinct implementation/test files and 3,500 changed LOC**;
the round itself may modify at most **12 implementation/test files**. This remains below project
limits, so no budget override is granted or required. Phase ONB/RF/REVIEW appendices, status/journal
events, and the five existing evidence artifacts remain trace files under the project budget.

## 4. Acceptance Criteria

### AC-R1: Complete and symmetric Researcher graph

- [ ] Focused and deep candidate graphs enumerate `1_briefing.md`, `2_gather.md`, `3_extract.md`,
  and `4_challenge.md` in mandatory stage order, with purpose/authority classification on every edge.
- [ ] Baseline and candidate apply identical transitive, dynamic, exclusion, and repeat rules.
- [ ] Removing any required stage-template edge fails a dedicated graph-completeness assertion,
  independently of word totals and generated report text.
- [ ] Evidence supersedes the published 5,362/5,427 and 72.4% claims with exact full-path totals;
  the preliminary corrected values 6,103/6,168 and 71.8% are remeasured rather than trusted.

Gate: targeted graph tests and raw audit against baseline `80382fbffd52b1f13cb3b38e8e450ecc0fef2fd5`.

Evidence: append corrected focused/deep edges, totals, and omission failure to
`runtime-context-primary-roles.txt`, `verification-primary-roles.txt`, and the EV.

### AC-R2: Output-changing mutants in every semantic family [depends: AC-R1]

- [ ] At least one source-derived substitution in each P/R/E/V/C/A family reaches production of a
  `SemanticRecord` and changes a named field before validation.
- [ ] A separate assertion proves the changed projection differs from the independent expected
  record; the comparison then rejects it for that difference, not for a missing probe/anchor.
- [ ] Expected records remain unreachable from production derivation, and existing ordinary
  P1–P4/R1–R3/E1–E4/V1–V4/C1–C3/A1 records still match.

Gate: targeted semantic tests plus a transcript naming family, scenario, changed field, produced
value, expected value, and rejection result.

Evidence: append the six output-changing cases to `semantic-primary-roles.txt`,
`verification-primary-roles.txt`, and the EV.

### AC-R3: One executable three-rung route [depends: AC-R2]

- [ ] `conventions.md` contains one non-contradictory mapping for rung 1/2/3 consistent with §2.
- [ ] `review.md`, `plan.md`, `handoff.md`, their generated copies, and Role Lock Hard Stops delegate
  to that mapping and expose no universal `REVISE → TS_DRAFT/TS revision` instruction.
- [ ] Isolated rung-1, rung-2, rung-3, and mixed-round cases assert recipient, Coordinator ruling
  site, governing artifact, lifecycle before/after Executor acceptance, and exact hard stop.
- [ ] A self-host Reviewer can follow the route without choosing between sources; injected
  contradictions in status, recipient, artifact, or hard stop fail independently.
- [ ] Rung 1 requires neither a TS revision nor a Coordinator-authored implementation order; rung 2
  cannot reach the Executor until a TS revision exists; rung 3 cannot reach execution before an
  owner verdict.

Gate: source-derived route records and mutants plus integration assertions over canonical and
generated workflow copies.

Evidence: append route cases and adverse results to `semantic-primary-roles.txt`,
`verification-primary-roles.txt`, and the EV.

### AC-R4: Parity, reductions, and regression closure [depends: AC-R3]

- [ ] Canonical `plan`, `handoff`, and `review` workflows remain byte-equal to both tracked copies;
  all four supported clean receivers retain the exact 11-command role/path contract.
- [ ] Every primary path remains at least 30% below its immutable Phase B baseline after the complete
  graph and routing changes; the combined trajectory remains at least 30% below 241,322 words.
- [ ] Targeted tests, configured collection, configured full suite, and project check pass. Task
  diagnostics contain only the approved immutable RDP 123>120 exception.
- [ ] The diff stays inside the exact round surface and cumulative budget; `tasks/` and every named
  exclusion remain byte-unchanged from candidate `272a7cf`.
- [ ] ONB, RF, EV, and raw evidence append a revision-2 account rather than overwriting the rejected
  claims, then the Executor stops at RF and returns to the same Reviewer.

Gate: `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q`,
`python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only`,
`python -m pytest .tfw/scripts/ docs/scripts/ -q`,
`python .tfw/scripts/gen_index.py --check project`, plus the known-exception task diagnostic.

Evidence: append to the existing five Phase B evidence artifacts; no sixth evidence file.

## 5. What Is Not Re-done

- Do not redesign the minimal skills, adapter manifest, templates, or already verified Coordinator,
  Executor, and Reviewer fixed-path edges beyond the exact routing corrections above.
- Do not repeat research or reopen the frozen HL; the REVIEW cites the governing ACs and no rung-3
  item exists.
- Do not repair the RDP diagnostic or any unrelated repository issue.
- Do not create a new Executor or Reviewer task. The same Executor appends the return, and the same
  Reviewer writes `REVIEW__phase-b__primary_role_paths__rev2.md` with `review/rev2/` stage traces.

## 6. Definition of Failure

- ❌ A Researcher total omits any mandatory stage template or uses asymmetric baseline/candidate rules.
- ❌ Any P/R/E/V/C/A mutant is rejected before a changed semantic output exists.
- ❌ Any executable source still tells rung 1 both “same TS/no state move” and “TS revision/TS_DRAFT”.
- ❌ A rung-specific case cannot identify recipient, ruling site, governing artifact, lifecycle effect,
  and hard stop from repository state alone.
- ❌ `KNOWLEDGE.md`, a skill, manifest, template, configuration key, or any file outside §3 changes.
- ❌ Any primary reduction falls below 30%, parity/receiver behavior regresses, a configured gate
  fails, or the cumulative Phase B scope exceeds 24 files / 3,500 LOC.

The same Executor works this approved revision and stops after cumulative RF. The Coordinator then
integrates the exact commits and resumes the same Reviewer; no merge, rebase, or push is authorized.

---

*TS revision 2 — TFW_20260902-175227_RCFR / Phase B: Proof and Rung Routing Repair | 2026-09-04*
