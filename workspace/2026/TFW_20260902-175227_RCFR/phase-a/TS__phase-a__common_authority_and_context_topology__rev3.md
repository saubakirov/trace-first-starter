# TS revision 3 — TFW_20260902-175227_RCFR / Phase A: Review Round 1 Repair

> **Date**: 2026-09-03
> **Author**: Codex (Coordinator), acting on behalf of `saubakirov`
> **Status**: ✅ APPROVED — saubakirov, 2026-09-03; explicit standing instruction to complete Phase A through the same Executor and Reviewer tasks
> **Supersedes**: [TS revision 2](TS__phase-a__common_authority_and_context_topology__rev2.md) — the highest ordinal governs; revisions 1–2 remain history
> **Returned by**: [REVIEW round 1](REVIEW__phase-a__common_authority_and_context_topology.md) — 🔄 REVISE, three cited items
> **Parent HL**: [Phase A derivation](HL__phase-a__common_authority_and_context_topology.md)
> **Master HL**: [Runtime Context Footprint Reduction](../HL-TFW_20260902-175227_RCFR.md), frozen baseline `2728dae78d55f6cb7daa39c82874ad5b43621f8a`
> **Ordered by**: Coordinator `saubakirov` via Codex

---

## 1. Round and Basis

This is review round 1's repair order and TS revision 3. The REVIEW verified the digest transaction, derived-copy equality, exact command set, scope, and frozen boundaries, but found three candidate-sensitive failures. All three are repairs inside the approved Phase-A outcome and existing file surface; no master-HL claim, Phase B/C responsibility, or adapter command set changes.

| # | Ordered repair | Basis | Required result |
|---|---|---|---|
| R1 | Remove or explicitly neutralize the universal full-library preload in every Phase-A-owned active bootstrap, including root `AGENTS.md` and tracked `.agent/rules/agents.md`. Make the read audit discover the actual active root → skill → workflow → addressed-range graph instead of consuming a hand-authored candidate edge list. | AC-1 bullets 1 and 4; AC-6 bullets 2–4; master HL DoF 1 and 6; REVIEW D1 | No active root instruction requires full `conventions.md`, full `glossary.md`, or full `KNOWLEDGE.md`; the real transitive/repeated `\S+` audit shows at least 30% reduction for both `/tfw-plan` and `/tfw-knowledge`. |
| R2 | Replace fixed semantic records, post-construction tuple mutations, self-declared omitted edges, and non-resolving G4 ledger rows with clean-input baseline/candidate executions whose outputs are derived from the source trees. Inject one source-level mutant per P/R/E/V/C/A family and independently exercise an omitted read edge plus missing/duplicate headings. Resolve every R03–R14 ledger condition/action/authority/test/history target against real files/headings. | AC-5 bullets 1, 2, and 5; AC-2 bullet 4; master HL DoF 5; REVIEW D2 | The suite fails when either source tree is absent, derives actual `{decision, refusal, artifact effects, citations, gate}` records for both baseline and candidate, accepts equivalent behavior, and rejects every real source mutation and missing edge/address. |
| R3 | Make official plural Antigravity discovery (`.agents/rules`, `.agents/workflows`) the single runtime authority everywhere, and add a cross-surface test covering the conventions route, glossary route, manifest, and clean receiver. | AC-2 one-authority contract; AC-4 bullets 1 and 3; master HL DoF 2 and 4; REVIEW D3; research iteration 2 R34/R37 | Flipping any one Antigravity surface back to singular `.agent/*` fails; all authoritative surfaces and the receiver agree on plural `.agents/*`. Legacy tracked singular command copies remain compatibility artifacts only and are not advertised as runtime discovery. |

## 2. Exact Scope

Implementation may modify only these already-approved Phase-A files:

- `AGENTS.md` and `.agent/rules/agents.md` for R1.
- `docs/scripts/test_runtime_context.py` for R1–R2.
- `.tfw/conventions.md`, `.tfw/glossary.md`, `.tfw/adapters/manifest.yaml`, and `docs/scripts/test_integration.py` for R2–R3.
- Existing five Phase-A evidence files, the cumulative ONB/RF/EV, `.tfw/knowledge_state.yaml`, phase `status.md`, and phase journal for round traces and state-last reconciliation.

No new file is authorized. Do not edit frozen HL, prior TS/REVIEW files, Phase B/C workflows, unrelated task traces, adapter algorithms already verified, or the ten derived workflow copies unless a changed canonical workflow makes an exact byte-copy update mechanically necessary. Such a necessity is a scope STOP before the copy is touched.

## 3. What Is Not Re-done

- ONB Q1–Q3 remain answered; add only a numbered revision-3 return subsection describing this order and any new blocker.
- K0–K9, the 61-task digest resolver, state-last algorithm, manifest exact 11-command roles, four clean receivers, and ten rev2-derived copy pairs remain accepted unless a repair regresses them.
- Do not recreate test-first history, revision-1/2 RF text, EV rows, raw evidence, or REVIEW round 1. Append round-specific subsections; rejected evidence remains openable.
- The immutable RDP journal observation is disposed as `not material — owed and forbidden to pay`; do not repair or rewrite it.

## 4. Verification and Evidence Order

1. Add failing source-sensitive tests for R1–R3 before changing their implementation inputs; preserve red and green proof in the existing evidence files.
2. Run the semantic suite against baseline `2728dae…` and the current candidate from real source roots. A nonexistent source root, a source-level family mutant, an omitted graph edge, and a missing/duplicate heading must fail for the reason each fixture names.
3. Run the active-graph whitespace audit from actual root instructions with transitive and repeated reads counted. Report raw rows and totals; both owned commands must reach at least 30% reduction without substituting research projections.
4. Run the Antigravity cross-surface mutation test and the full four-vendor empty-receiver/11-command contract.
5. Re-run `python -m pytest .tfw/scripts/test_gen_index.py -q`, `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q`, collect-only, the full configured suite, and `python .tfw/scripts/gen_index.py --check project`. Report the known unrelated `--check tasks` failure without modifying it.
6. Append round-2 sections to RF, EV, and each touched raw evidence file. Replace no earlier result. Record corrected measurements and explicitly supersede the rejected round-1 claims.
7. After every final RF/EV/review-relevant selected section exists, recompute all task digests, require `problems=[]` and `removed_task_ids=[]`, then write `.tfw/knowledge_state.yaml` last. Immediate replay must show `migration_required=false` and no pending IDs.

## 5. Budget and Stop Conditions

The cumulative implementation/test/evidence surface remains revision 2's 34 modified + 2 new + 5 evidence = 41 files. Review and lifecycle traces remain separate. Expected cumulative changed LOC remains at or below 4,600; the project hard ceiling is 5,000. Stop before any 42nd implementation/test/evidence file, any sixth evidence file, any cumulative total above 5,000 changed LOC, any frozen/Phase B/C edit, or any semantic conflict with the RDP meanings preserved at baseline.

## 6. Completion Gate

The Executor resumes the existing task, moves `TS_DRAFT → ONB`, appends the cumulative artifacts, implements only R1–R3, produces corrected evidence/RF, moves `ONB → RF`, commits locally, and stops. The Coordinator then integrates exact commits only into the isolated candidate branch and returns the same existing Reviewer task for REVIEW revision 2. Master/shared branches and push remain prohibited.

---

*TS revision 3 — TFW_20260902-175227_RCFR / Phase A: Review Round 1 Repair | 2026-09-03*
