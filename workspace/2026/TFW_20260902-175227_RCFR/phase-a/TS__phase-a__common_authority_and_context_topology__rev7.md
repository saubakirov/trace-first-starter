# TS revision 7 — TFW_20260902-175227_RCFR / Phase A: Exact Evidence Correction

> **Date**: 2026-09-04
> **Author**: Codex (Coordinator), acting on behalf of `saubakirov`
> **Status**: ✅ APPROVED — `saubakirov`; standing instruction to complete Phase A and explicit 2026-09-04 authorization to exceed the configured whole-tree limit
> **Supersedes**: [TS revision 6](TS__phase-a__common_authority_and_context_topology__rev6.md) — revisions 1–6 remain immutable history
> **Returned by**: [REVIEW revision 3](REVIEW__phase-a__common_authority_and_context_topology__rev3.md) — 🔄 REVISE, evidence-only D1/D2
> **Reviewed candidate**: `09ba0704f1dc7c4979221d9d53ee52e4667ac68b`
> **Master HL**: [Runtime Context Footprint Reduction](../HL-TFW_20260902-175227_RCFR.md), frozen baseline `2728dae78d55f6cb7daa39c82874ad5b43621f8a`
> **Ordered by**: Coordinator `saubakirov` via Codex

---

## 1. Round and Basis

REVIEW revision 3 accepts the R4 implementation, all regression gates, both word reductions,
the 41-path implementation boundary, and the owner's Phase A budget exception. It returns only
two known-false evidence statements:

| Item | Ordered correction | Basis |
|---|---|---|
| E1 | Append to the existing EV a correction that supersedes `68 paths / 5,505 LOC` for reviewed candidate `09ba070` with the independently reproduced result: **69 paths; 4,278 additions + 1,239 deletions = 5,517 LOC**. Retain the correct scoped result **41 paths; 2,559 + 1,236 = 3,795 LOC**. | TS rev6 §3.4 requires exact two-counter evidence; REVIEW rev3 D1/V5/V6. |
| E2 | Append to `semantic-fixtures.txt` a correction that supersedes the claimed minimal-P1 failure on `refusal_reason` with the actual first failure: **`P1: artifacts_created semantic source resolved 0 times`**. | TS rev6 §3.2 requires the exact adverse result; REVIEW rev3 D2/V3/V6. |

These are evidence corrections, not a new implementation round. Previously accepted behavior and
the immutable earlier evidence remain history.

## 2. Exact Scope and What Is Not Re-done

Do not change code, tests, RF, either HL, any prior TS or REVIEW, canonical workflows, adapters,
derived copies, Phase B/C, or unrelated task traces. Append only to:

- `evidence/EV__phase-a__common_authority_and_context_topology.md`;
- `evidence/semantic-fixtures.txt`.

The handoff may make only the minimal canonical lifecycle writes required for the same Executor:
an ONB receipt if the workflow requires it, phase `status.md`, one phase journal event, and
`.tfw/knowledge_state.yaml` reconciled last. No other evidence file and no implementation path is
authorized.

Do not rerun the entire suite: REVIEW revision 3 independently passed the final serial suite and
accepted the implementation. Reproduce only the exact minimal-source adverse test, the scoped
41-path numstat, the reviewed-snapshot 69-path numstat, project consistency, and immediate
knowledge-pending replay.

## 3. Acceptance and Evidence

1. The two old statements remain visibly historical, followed by unambiguous append-only
   corrections naming this revision and reviewed commit `09ba070`.
2. The targeted adverse test passes and its direct execution reports
   `P1: artifacts_created semantic source resolved 0 times`.
3. Primary numstat against `2728dae…09ba070` reproduces exactly `69 / 4,278 / 1,239 / 5,517`;
   the approved implementation/test/evidence filter reproduces `41 / 2,559 / 1,236 / 3,795`.
4. No code blob changes. The final return reports its own post-trace whole-tree count separately
   from the reviewed-snapshot correction.
5. State is written last; immediate replay reports no pending, removed, or problem task IDs.

## 4. Budget Containment and Completion

The implementation/test/evidence ceiling remains **41 paths and 4,600 changed LOC**. Because the
mandatory REVIEW revision 3 already raised the complete candidate to 5,813 LOC and this repair,
REVIEW revision 4, and closure traces are mandatory history, the owner's phase-local trace ceiling
is contained at **7,000 additions plus deletions**. `.tfw/project_config.yaml` remains unchanged at
5,000; this exception cannot authorize code, another implementation path, or Phase B/C work.

The same Executor applies only §2, commits the evidence/lifecycle return, and stops. The Coordinator
integrates exact commits into the isolated candidate and resumes the same Reviewer for REVIEW
revision 4. Master/shared branches, merge, rebase, and push remain prohibited.

---

*TS revision 7 — TFW_20260902-175227_RCFR / Phase A: Exact Evidence Correction | 2026-09-04*
