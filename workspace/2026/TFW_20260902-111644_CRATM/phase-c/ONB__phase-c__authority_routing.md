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

## 8. Return Round 1 — Coordinator-ruled Rung 1

### 8.1 Accepted bound and lineage

- Prior Executor trace tip: `f36c426b9d70695e3cd2639d87885aac3af5170b`.
- Live Reviewer/Coordinator ruling tip: `2d6e0f95696d12ed044305d4cf99b78d292338da`;
  its parent lineage contains the `🔄 REVISE` REVIEW and the prior Executor tip.
- Phase state is `RF`; exactly one approved `TS__phase-c__authority_routing.md` exists. The live
  REVIEW's `Coordinator ruling — return round 1` accepts all five proposals as Rung 1. No TS sibling,
  HL amendment, scope change, or different recipient exists.
- The same clean detached worktree was aligned to the ruling tip before this append. Bootstrap with
  full HEAD/status/cached names and confirmation that the ruling was read was sent to the Coordinator.

### 8.2 Work accepted for this round

1. Replace both live §14 owner-signing formulations with valid rule-8 verdict/application language;
   only the named human exceptions may retain owner routing. Re-run the live census.
2. Make rule 8 state the prior guarantee (“only the owner rules”) and the new ordinary delegated
   guarantee (nearest eligible non-proposer, otherwise governing owner) explicitly.
3. Put an ordinary-CL/no-delegation branch before Plan 6d delegated-prefix validation, synchronize
   only the two accepted Plan copies, and test the actual parsed Plan consumer plus an output-changing
   contradiction mutant.
4. Because VALUE changes, create a replacement Candidate under the unchanged Baseline, literal
   twelve-path selector, immutable 12/320 denominator, and two ASSURANCE owners. Capture complete
   pre-commit status, cached names, exact pathspec, and real `git commit --only` command/output before
   appending EV.
5. Re-run the EV validator extraction and hash exact stdout including its terminal LF. Name the byte
   boundary and digest; label fenced bytes separately if retained. Never reconstruct round-zero shell
   history or claim unsupported byte equality.

### 8.3 Questions, recommendations, and risks

No blocking questions. The Coordinator ruling is terminal, exact, and within the existing TS.

Recommendations:

1. Model the Plan 6d consumer as a source-derived decision projection with explicit `ordinary_cl`
   and `delegated` inputs. Mutating the branch order must change the produced decision before the
   independent expectation rejects it.
2. Preserve pre-commit evidence in the command output returned by the commit invocation itself, then
   append that untouched transcript to EV only after Git returns the replacement Candidate SHA.

Risks:

1. Plan has narrow attention slack; minimum substitutions and immediate route/corpus measurement are
   required. No cap edit is authorized.
2. The live census must classify current enforcement, not merely suppress legacy substrings; the two
   §14 lines must no longer admit a universal owner-signing interpretation.
3. Exact stdout and fenced content differ by the terminal LF. Their digests must never be conflated.
4. Any VALUE edit after the replacement Candidate invalidates it and requires another full candidate
   and accounting replay.

### 8.4 Prior evidence and knowledge

Approved round-zero implementation that was not returned is not redone. The §7 citation applications
above remain valid and are not re-adjudicated. Return evidence is cumulative: ONB, EV, and RF receive
numbered append-only Round 1 sections; the rejected REVIEW and earlier evidence remain openable.

---

*ONB — TFW_20260902-111644_CRATM / Phase C: Authority routing | 2026-09-06*
