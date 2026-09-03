# TS revision 5 — TFW_20260902-175227_RCFR / Phase A: Budget-Safe Review Round 2 Repair

> **Date**: 2026-09-03
> **Author**: Codex (Coordinator), acting on behalf of `saubakirov`
> **Status**: ✅ APPROVED — saubakirov, 2026-09-03; standing completion instruction and root-coordinator confirmation after the rev4 budget STOP
> **Supersedes**: [TS revision 4](TS__phase-a__common_authority_and_context_topology__rev4.md) — revisions 1–4 remain immutable history
> **Returned by**: [REVIEW revision 2](REVIEW__phase-a__common_authority_and_context_topology__rev2.md) — 🔄 REVISE, one cited semantic item
> **Budget STOP**: rev4 incorrectly excluded mandatory traces from the already-established whole-tree metric; Executor stopped before implementation commit, RF, evidence, or final state
> **Master HL**: [Runtime Context Footprint Reduction](../HL-TFW_20260902-175227_RCFR.md), frozen baseline `2728dae78d55f6cb7daa39c82874ad5b43621f8a`
> **Ordered by**: Coordinator `saubakirov` via Codex

---

## 1. Round, Basis, and Restriction

R4 from revision 4 remains the only semantic change: baseline and candidate must independently
derive all six semantic record fields from their own source trees, with expected records used only
for comparison and a preserved-address candidate substitution changing a produced field before the
comparison rejects it. Basis: TS rev3 R2, Phase A AC-5 bullets 1/2/5, master HL DoF 5, REVIEW rev2
D1, and REVIEW rev1 D2.

The rev4 implementation surface could not meet the governing budget without compressing one test
file below a maintainable size. This revision applies a stricter, deletion-led repair: three other
already-approved code/test paths may be refactored only to preserve behavior while creating honest
budget room. Dense one-liners, semicolon packing, opaque tables, or weakened gates are prohibited.

## 2. Exact Scope

Only these existing implementation/test paths may change:

- `docs/scripts/test_runtime_context.py` — R4 plus readable data-driven compaction;
- `docs/scripts/test_integration.py` — behavior-preserving compaction only;
- `.tfw/scripts/test_gen_index.py` — behavior-preserving compaction only;
- `.tfw/scripts/gen_index.py` — behavior-preserving compaction only.

Round traces may append only to the existing ONB, RF, EV, `semantic-fixtures.txt`,
`knowledge-gate-replay.txt`, and `clean-receiver-adapters.txt`; final reconciliation may update
`.tfw/knowledge_state.yaml`, phase `status.md`, and phase journal. No new path is authorized.

Do not rewrite any prior TS, REVIEW, journal event, or earlier evidence section. Do not edit HL,
canonical workflows, adapter surfaces, Phase B/C, unrelated tasks, or any other implementation file.

## 3. Acceptance and Evidence

1. **R4 independent semantics.** All 19 P/R/E/V/C/A records construct `decision`,
   `refusal_reason`, `artifacts_created`, `artifacts_modified`, `citations`, and `gate` from the
   executing tree's observed content. Expected values cannot feed execution. Minimal anchor-only
   input fails. A resolvable semantic substitution completes execution, changes a produced field,
   and is rejected by the independent assertion.
   **Evidence:** targeted red/green output and before/after records in `semantic-fixtures.txt`.
2. **Compaction parity.** Outside R4, public CLI results, exit codes, JSON/schema behavior, collected
   tests, mutation failures, adapter/receiver checks, and all previously accepted assertions match
   the accepted candidate `ade6d41`. Named helpers and explicit scenario records remain readable.
   **Evidence:** pre/post command parity and full gate output in RF/EV and the existing raw evidence.
3. **Regression.** The actual read audit remains 45.4%/47.4%; K0–K9, 61-task reconciliation,
   19 semantic cases, P/R/E/V/C/A mutants, structural adverse probes, R03–R14, ten derived copies,
   four receivers, 11 commands, and plural Antigravity authority remain green.
   **Evidence:** targeted suites, audit, project check, and immediate state-last replay.
4. **Scope and readability.** Exactly the four code/test paths above plus permitted cumulative
   traces may change; no minification or loss of diagnostic clarity is accepted.
   **Evidence:** exact path/numstat report and Reviewer inspection.

## 4. Verification Order

1. Preserve rev4's committed red guards, then replace the uncommitted sketch with a readable
   implementation satisfying Acceptance 1.
2. Capture pre/post behavior for the three compaction-only files before accepting their refactor.
3. Run runtime-context, gen-index, combined runtime/integration, collect-only, full configured suite,
   `gen_index.py --check project`, and the immediate knowledge-pending replay. Report the immutable
   RDP task-check diagnostic without repairing it.
4. Append concise round material only after green execution; recompute task digests and write
   `.tfw/knowledge_state.yaml` last. Immediate replay must have no problems, removed, or pending IDs.

## 5. Budget and Stop Conditions

Use one metric only: additions plus deletions for the entire candidate tree relative to
`2728dae78d55f6cb7daa39c82874ad5b43621f8a`, including mandatory governing and lifecycle traces.
No surface is excluded. The Phase ceiling remains 4,600 and the project hard ceiling remains 5,000.

Executor RF handoff must be at or below **4,300 whole-tree changed LOC**, reserving at least 300 for
immutable REVIEW revision 3 and closure traces. Stop before commit/RF/state if this target requires
obscurity, weakens any accepted gate, changes behavior outside R4, creates a path, or cannot be met.

## 6. Completion Gate

The same Executor resumes from its stopped rev4 worktree, records this new authority, implements
only §2, reaches the ≤4,300 pre-review target, returns RF, commits, and stops. The Coordinator then
integrates exact commits into the isolated candidate and returns the same Reviewer for REVIEW rev3.
Master/shared branches and push remain prohibited.

---

*TS revision 5 — TFW_20260902-175227_RCFR / Phase A: Budget-Safe Review Round 2 Repair | 2026-09-03*
