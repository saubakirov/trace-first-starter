# TS revision 6 — TFW_20260902-175227_RCFR / Phase A: Owner Budget Override and Final R4 Repair

> **Date**: 2026-09-04
> **Author**: Codex (Coordinator), acting on behalf of `saubakirov`
> **Status**: ✅ APPROVED — saubakirov, 2026-09-04: “разрешаю превысить”
> **Supersedes**: [TS revision 5](TS__phase-a__common_authority_and_context_topology__rev5.md) — revisions 1–5 remain immutable history
> **Returned by**: [REVIEW revision 2](REVIEW__phase-a__common_authority_and_context_topology__rev2.md) — 🔄 REVISE, one semantic item
> **Master HL**: [Runtime Context Footprint Reduction](../HL-TFW_20260902-175227_RCFR.md), frozen baseline `2728dae78d55f6cb7daa39c82874ad5b43621f8a`
> **Ordered by**: Coordinator `saubakirov` via Codex

---

## 1. Owner Decision and Bound

The owner authorizes this Phase A candidate to exceed the configured 5,000 whole-tree LOC budget.
The phase-local override ceiling is **6,000 additions plus deletions** relative to `2728dae…`.
`.tfw/project_config.yaml` is not changed; the override applies only to this phase and is recorded
here. It covers accumulated immutable TFW planning/review/lifecycle traces, not additional product
scope.

The implementation/test/evidence bound remains **41 paths and 4,600 changed LOC**. No new path is
authorized. Report both counters independently: the 41-path implementation/test/evidence surface
and the complete candidate including immutable traces.

## 2. Ordered Repair and Exact Scope

R4 remains the only semantic change. Baseline and candidate executions must independently derive
all six semantic fields from their own source trees; expected values are comparison-only. A
preserved-address candidate substitution must complete execution, change a produced semantic field,
and be rejected by the independent assertion.

Implementation may modify only `docs/scripts/test_runtime_context.py`. The uncommitted revision-5
compaction experiment is not accepted: `.tfw/scripts/gen_index.py`, `.tfw/scripts/test_gen_index.py`,
and `docs/scripts/test_integration.py` must match committed Executor `f5cc3f1` exactly. No dense
packing or behavior-preserving compaction is required.

Round evidence may append only to existing ONB, RF, EV, and `semantic-fixtures.txt`; final
reconciliation may update `.tfw/knowledge_state.yaml`, phase `status.md`, and phase journal. Prior
TS, REVIEW, journal, and evidence content is immutable.

## 3. Acceptance and Impact

1. **Independent derivation.** Each of the 19 P/R/E/V/C/A executions constructs `decision`,
   `refusal_reason`, `artifacts_created`, `artifacts_modified`, `citations`, and `gate` from content
   read through that execution's `SourceTree`. An expected table cannot feed produced records.
   **Evidence:** per-field source provenance and baseline/candidate records in the existing semantic
   evidence file.
2. **Adverse proof.** Minimal anchor-only input fails. Changing an expected value leaves produced
   output unchanged and makes comparison fail. A resolvable semantic source substitution changes a
   produced field without changing expected data, then fails comparison.
   **Evidence:** targeted red/green tests and exact before/after record.
3. **No unrelated behavior change.** Knowledge Gate, integration/receiver behavior, read audit,
   plural Antigravity authority, structural mutants, R03–R14, and all accepted Phase A gates remain
   unchanged and green.
   **Evidence:** exact tree comparison for the three rejected compaction paths plus targeted/full
   suites and state replay.
4. **Budget override containment.** Implementation/test/evidence remains ≤4,600 across 41 paths;
   complete candidate remains ≤6,000. The margin cannot authorize another file or semantic change.
   **Evidence:** two named numstat reports against `2728dae…`.

Impact is intentionally narrow: R4 changes only the verification oracle used by repository tests.
It does not change shipped workflow decisions, adapter installation, command routing, Knowledge
Gate runtime behavior, or master/Phase B/C contracts.

## 4. Verification and Completion

Run runtime-context, gen-index, combined runtime/integration, collect-only, the full configured
suite, project consistency, task diagnostic, and immediate knowledge-pending replay. Preserve the
known immutable RDP 123>120 task diagnostic as an observation. Append evidence only after green;
write knowledge state last and require no pending/removed/problems.

The same Executor returns RF and stops. The Coordinator integrates exact commits only into the
isolated candidate and returns the same Reviewer for REVIEW revision 3. Master/shared branches and
push remain prohibited.

---

*TS revision 6 — TFW_20260902-175227_RCFR / Phase A: Owner Budget Override and Final R4 Repair | 2026-09-04*
