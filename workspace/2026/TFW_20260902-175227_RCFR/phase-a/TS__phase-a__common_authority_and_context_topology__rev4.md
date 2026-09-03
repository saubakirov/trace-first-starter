# TS revision 4 — TFW_20260902-175227_RCFR / Phase A: Review Round 2 Repair

> **Date**: 2026-09-03
> **Author**: Codex (Coordinator), acting on behalf of `saubakirov`
> **Status**: ✅ APPROVED — saubakirov, 2026-09-03; explicit standing instruction to complete Phase A through the same Executor and Reviewer tasks
> **Supersedes**: [TS revision 3](TS__phase-a__common_authority_and_context_topology__rev3.md) — the highest ordinal governs; revisions 1–3 remain history
> **Returned by**: [REVIEW revision 2](REVIEW__phase-a__common_authority_and_context_topology__rev2.md) — 🔄 REVISE, one cited item
> **Parent HL**: [Phase A derivation](HL__phase-a__common_authority_and_context_topology.md)
> **Master HL**: [Runtime Context Footprint Reduction](../HL-TFW_20260902-175227_RCFR.md), frozen baseline `2728dae78d55f6cb7daa39c82874ad5b43621f8a`
> **Ordered by**: Coordinator `saubakirov` via Codex

---

## 1. Round and Basis

This is review round 2's repair order and TS revision 4. REVIEW revision 2 independently
accepted R1, R3, scope, frozen boundaries, the 30% reductions, and every structural part of R2.
One local R2 acceptance breach remains; it does not change a frozen claim, phase boundary, or
approved file surface.

| # | Ordered repair | Basis | Required result |
|---|---|---|---|
| R4 | Replace the shared `OUTCOMES`-fed result path with baseline and candidate executions that independently derive every semantic record field from their respective clean source trees. Keep expected assertions outside the production path. Add an adverse candidate-source substitution that preserves a resolvable source/address but changes a derived semantic result and is rejected. | TS rev3 R2; Phase A AC-5 bullets 1, 2, and 5; master HL DoF 5; REVIEW rev2 D1; REVIEW rev1 D2 | For all 19 P/R/E/V/C/A scenarios, both sides construct `{decision, refusal_reason, artifacts_created, artifacts_modified, citations, gate}` from observed source content without reading or copying an expected record. Correct baseline/candidate behavior matches the independent expected assertions. A wrong expected value cannot alter produced output; a semantic source mutation changes or invalidates produced output and fails the gate. |

## 2. Exact Scope

Implementation may modify only `docs/scripts/test_runtime_context.py`. Round evidence may append
only to the existing `phase-a/evidence/semantic-fixtures.txt`, cumulative ONB, RF, and EV; final
state-last reconciliation may update `.tfw/knowledge_state.yaml`, phase `status.md`, and the phase
journal. No new file or other implementation path is authorized.

Do not edit frozen or phase HL, prior TS/REVIEW files, R1/R3 production inputs, Phase B/C,
unrelated task traces, adapter surfaces, canonical workflows, derived copies, or the RDP event.
Any need to touch one is a scope STOP before the edit.

## 3. What Is Not Re-done

- The actual root → skill → workflow audit and its 45.4%/47.4% reductions remain accepted.
- The nonexistent-root, omitted-route, missing/duplicate-heading, six family source-mutant, and
  R03–R14 resolution checks remain accepted and must stay green.
- The digest transaction, 61-task replay, ten derived copies, exact 11-command manifest, four
  clean receivers, and plural Antigravity authority remain accepted and must stay green.
- Earlier ONB/RF/EV/raw-evidence and REVIEW revisions remain immutable history. Append a concise
  round-2 subsection; do not reconstruct or erase rejected evidence.
- The immutable RDP 123>120 diagnostic remains `not material — owed and forbidden to pay`.

## 4. Acceptance and Evidence

1. **Independent derivation.** Neither source execution can import an expected tuple, shared
   outcome table, or values produced for the other source. Each of the six projected fields is
   causally traceable to content read from that execution's own `SourceTree`.
   **Evidence:** targeted tests plus `semantic-fixtures.txt` identify the source clause(s) and
   produced six-field record for both sides in all 19 cases.
2. **Oracle separation.** Expected assertions are immutable inputs to comparison only; changing
   an expected value cannot change either produced record and instead makes the assertion fail.
   A minimal source that merely preserves the old anchor cannot manufacture a valid record.
   **Evidence:** red/green guard tests and raw failure reason in `semantic-fixtures.txt`.
3. **Semantic sensitivity.** At least one candidate-source mutation preserves file and heading
   resolution while substituting a real decision, refusal, artifact effect, citation, or gate;
   the candidate execution changes or refuses and the semantic gate rejects it without editing
   the expected oracle. Existing P/R/E/V/C/A mutants remain source-level and green.
   **Evidence:** before/after produced record and rejected assertion/error in
   `semantic-fixtures.txt`.
4. **Regression and scope.** All prior accepted gates remain green; no new implementation,
   evidence, or lifecycle surface appears beyond §2.
   **Evidence:** targeted/full command outputs, exact changed-path list, and cumulative LOC in RF/EV.

## 5. Verification and Evidence Order

1. Add failing tests for oracle separation, minimal-source rejection, and a semantic substitution
   before repairing the execution path; preserve concise red output in existing evidence.
2. Run the 19-case baseline/candidate equality from Git baseline `2728dae…` and the current source
   tree, and show every projected value was derived independently.
3. Re-run `python -m pytest docs/scripts/test_runtime_context.py -q`,
   `python -m pytest .tfw/scripts/test_gen_index.py -q`, the combined runtime/integration gate,
   collect-only, the full configured suite, and `python .tfw/scripts/gen_index.py --check project`.
   Report the known unrelated `--check tasks` failure without modifying it.
4. Append round-2 results to ONB, RF, EV, and `semantic-fixtures.txt`; supersede the rejected AC-5
   claim explicitly while retaining it as history.
5. After final selected sections exist, recompute all task digests, require no problems or removed
   IDs, write `.tfw/knowledge_state.yaml` last, and require immediate replay with no pending IDs.

## 6. Budget and Stop Conditions

The implementation/test/evidence surface remains 41 paths and 3,504 cumulative changed LOC at
candidate `ade6d41`; mandatory TS/REVIEW/status/journal traces are accounted separately and are
not implementation budget. The unchanged ceiling is 4,600 cumulative implementation/test/evidence
LOC and 41 paths. Use deletion-led replacement if needed; do not spend the available margin on
unrelated cleanup.

Stop before a 42nd implementation/test/evidence path, any new file, a cumulative scoped total above
4,600, an edit outside §2, a source execution coupled to expected values, or a mutation that proves
only anchor removal instead of changed semantic behavior.

## 7. Completion Gate

The same Executor task resumes, moves `TS_DRAFT → ONB`, appends the existing traces, implements only
R4, returns corrected evidence/RF, moves `ONB → RF`, commits locally, and stops. The Coordinator
integrates exact commits only into the isolated candidate branch and returns the same Reviewer task
for REVIEW revision 3. Master/shared branches and push remain prohibited.

---

*TS revision 4 — TFW_20260902-175227_RCFR / Phase A: Review Round 2 Repair | 2026-09-03*
