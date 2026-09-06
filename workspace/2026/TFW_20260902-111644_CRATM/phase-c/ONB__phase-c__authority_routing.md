# ONB — TFW_20260902-111644_CRATM / Phase C: Authority routing

> **Date**: 2026-09-06
> **Author**: Codex (Executor, acting as `saubakirov`)
> **Status**: 🟠 ONB — Accepted; no blockers
> **Parent HL**: [Master HL](../HL-TFW_20260902-111644_CRATM.md) · [Phase HL](HL__phase-c__authority_routing.md)
> **TS**: [TS Phase C](TS__phase-c__authority_routing.md)

---

## 1. Understanding

Phase C replaces the current owner-only frozen-amendment route with one canonical, human-rooted,
child-only authority resolver. The governing phase `status.md.owner` plus a separate recorded root
authorization supplies the human root; profile accountability, binding, title, provider, workflow
role, event attribution, and `on_behalf_of` never do. Ordinary `EXTEND`/`SUPERSEDE` proposals route
to the nearest immutable `true` grant whose stable principal differs from the preserved originating
proposer, otherwise to the governing owner. Strategic and malformed cases remain human or refuse.
All canonical consumers, six accepted tracked copies, and the two authorized repository-assurance
modules must agree without entering Phase D/E or changing earlier contracts.

## 2. Entry Points

- Canonical authority and lifecycle owners: `.tfw/conventions.md` headings `HL Contract`,
  `The 🔄 REVISE route`, and `Anti-patterns (prohibited)`.
- Decision consumers: `.tfw/workflows/plan.md`, `.tfw/workflows/review.md`, and
  `.tfw/workflows/handoff.md`.
- Output forms: `.tfw/templates/HL.md` §12 and `.tfw/templates/RES.md` amendment recommendations.
- Accepted copies: the matching Plan/Review/Handoff files under `.agent/workflows/` and
  `.claude/commands/`.
- Repository assurance: `docs/scripts/test_runtime_context.py` source-derived semantic and Rung
  records; `docs/scripts/test_integration.py` copy/consumer integration checks.
- Protected prior semantics: `.tfw/conventions.md` principal, binding, worktree, exact-path staging,
  landing, Session identity, and Role Lock ranges; Phase B RF and final REVIEW revision 2.

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions. The explicit AG execution grant, Git approval ref
`1f1173d968e9b74a5e06e3e2070ae604c2844ca5`, approved planning content
`95eb2ab510ed8d89205ed5fe498ccb061c112888`, literal selector, cascade ruling, HC-C1/C2, and immutable
12-VALUE-file / 320-LOC denominator leave one executable bound.

## 4. Recommendations (suggestions, not blocking)

1. Replace superseded owner-only sentences by minimum substitutions and keep the traversal algorithm
   only in `HL Contract`; every other carrier should name its inputs, output, and canonical reference.
2. Preserve proposer origin explicitly at transcription and make terminal signature validation a Plan
   pre-act gate; this prevents both writer substitution and same-principal session laundering.
3. Add the complete authority fixture/mutant matrix to the existing runtime-context module and keep
   integration assurance focused on exact canonical/copy parity and Rung-3 consumer behavior.

## 5. Risks Found (edge cases, potential issues not in TS)

1. The current `P2` semantic oracle and exact Rung-3 record encode owner-only wording; changing prose
   without updating their source-derived derivation would either fail or preserve a false contract.
2. Route ceilings have little slack. Every canonical edit must be measured before Candidate; no cap
   constant or expectation may be changed to make the result pass.
3. A broad owner-only census includes legitimate human exceptions, TS approval, budget authority, and
   historical statements. Classification must distinguish them rather than mechanically remove words.
4. The approved worktree is detached at the approval commit. Candidate reachability and attribution
   therefore depend on the exact local commit chain being preserved for the separate Reviewer.

## 6. Inconsistencies with Code (spec vs reality)

1. Expected pre-change gap: `HL Contract` rules 3 and 8, the Rung-3 row, Plan, Handoff, HL/RES forms,
   and assurance records still require an owner verdict. This is the approved Phase C delivery gap,
   not a planning contradiction.
2. No unexpected selector, baseline, Phase B, copy-parity, or approval-lineage inconsistency was found.
   Baseline `fb08c120a91aca4c9ceaea859d46dd49c032afd0` is an ancestor of approval; its only path changes to
   the approval ref are authorized Phase C planning TRACE files.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | C1 — NS1 Purpose and NS3 Non-goals | ✅ | Apply | Keep continuity inspectable and human-governed; add no vendor runtime or replacement authority. |
| 2 | C2 — Methodology values and Success Criteria | ✅ | Apply | Refusal, stable names, signed ruler, and source-derived tests make violations observable. |
| 3 | C3 — `philosophy.md` F37 | ✅ | Apply | Treat every grant as a ceiling; self-grant and self-ruling return to the owner. |
| 4 | C4 — D59, D63, D73–D77, D79–D80 | ✅ | Apply | Preserve independence distinctions, frozen claims, selective reads, immutable VALUE, worktree/Candidate, navigation-only title, and stable principal semantics. |
| 5 | C5 — conventions authority/REVISE/Role Lock/anti-pattern ranges | ✅ | Apply | Put one resolver in `HL Contract` and enforcement edges only at actual workflow and prohibition sites. |
| 6 | C6 — `convention.md` F5 | ✅ | Apply | Synchronize only the six accepted singular copies byte-for-byte with their canonical workflows. |
| 7 | C7 — `process.md` F30, F36, F38, F46 | ✅ | Apply | Ship the complete consumer cascade, enforce bounds before acts, and preserve shared-file sequencing. |
| 8 | C8 — `constraint.md` F2, F12, F14 | ✅ | Apply | Use minimum necessary wording, keep obligations in repository files, and stop at the independent-review boundary. |
| 9 | C9 — `risk.md` F1 | ✅ | Apply | Inspect full status/cached names and commit only exact full paths. |
| 10 | C10 — `stakeholder.md` F6 | ✅ | Apply | Reduce routine owner routing without weakening named human exceptions or oversight. |

No new PV item beyond the phase HL §7.2 set is required for this implementation.

---

*ONB — TFW_20260902-111644_CRATM / Phase C: Authority routing | 2026-09-06*
