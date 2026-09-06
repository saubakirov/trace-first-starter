# EV — TFW_20260902-111644_CRATM / Phase E: Integration gate

> **Date**: 2026-09-07
> **Author**: saubakirov (Codex Executor)
> **Task**: TFW_20260902-111644_CRATM
> **TS**: [Phase E integration-gate TS](../TS__phase-e__integration_gate.md)

---

## Environment

| Field | Value |
|---|---|
| OS | Windows, local Executor and independent Reviewer worktrees |
| Language / Runtime | Python 3.13.5; Git 2.42.0.windows.1; MkDocs 1.6.1 |
| Database | N/A |
| Deploy target | Saved local `master`; no tag, push, publication, or release |
| CI / Pipeline | Local configured pytest and MkDocs gates plus independent Reviewer replay |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | Replacement Candidate `b977b89be0c759297dd5653040564f0169ba3e56` has exact parents `cafd4947791d95907d1cd81fa10e1d9bbbe56578` then `2adf89918c64643f9edfde07182508decef1fde4`; preserves the immutable Phase-D tree, RTBO D82, final CRATM D83, no-runtime/no-index boundary, 8×3 workflow byte parity, and a zero conflict-marker/diff-error census. Executor and Reviewer each passed targeted, collect, full, and configured strict-build gates. Failed checkpoint `cc144e738d346112c4714f9ead41fe86ea62c663` remains reachable and is transparently superseded after one stale Key-Artifacts attribution was corrected with a row-specific regression guard. | Exact Git objects; local Windows/Python 3.13.5 | VERIFIED | `phase-e-integration-lineage.txt`; `phase-e-integration-tests.txt` |
| E2 | AC-2 | The distinct Phase E Reviewer independently returned interim PASS. Main then fast-forwarded saved `master` from `ae494e2a9f9ee82e5d0bd2a9d79e4e23d58a1822` to exact Candidate, with identical pre/post porcelain, an empty index, zero Candidate diff on all three protected targets, and all nine foreign-file SHA-256 values unchanged. Phase E remains `ONB`; no RF, final REVIEW, KNW, DONE, sweep, release, tag, push, or publication was produced. | Reviewer worktree and Main saved checkout | VERIFIED | `phase-e-integration-lineage.txt`; `phase-e-integration-tests.txt` |
| E-accounting | AC-1 | Approval source is the exact Phase E TS; Baseline is `957f7be8f5f208b87be12a8cd4d67b24af00cd1e`; Candidate is `b977b89be0c759297dd5653040564f0169ba3e56`; the literal 25-path VALUE selector yields 24 MODIFY + 1 CREATE, 495 additions + 476 deletions = 971 touched text LOC, no binary/non-text N/A, and remains below immutable 25/1,200 and owner 50/2,400. The exact NUL-safe `--name-status --find-renames=50% -z` and `--numstat --find-renames=50% -z` methods were used over the whole Baseline→Candidate delta; no hand subtraction, denominator ratchet, or unresolved phase attribution occurred. Configured project triggers remain 50 files / 5,000 LOC; the approved disposition is `KEEP_PHASE_E / INTEGRATION_GATE_FIRST`. | Git 2.42.0.windows.1, exact repository objects | VERIFIED | `phase-e-integration-lineage.txt` |

## Verdict

Evidence verdict: 3/3 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A.

This is the approved interim integration checkpoint only. It does not close Phase E or authorize its
remaining product, knowledge, review, release, or publication work.

## Attachments

| File | Description |
|---|---|
| `phase-e-integration-lineage.txt` | Candidate reconstruction, exact ancestry/tree/accounting, and saved-landing preservation proof. |
| `phase-e-integration-tests.txt` | Executor and independent Reviewer command results, semantic audits, and MkDocs invocation disclosure. |

---

*EV — TFW_20260902-111644_CRATM / Phase E: Integration gate | 2026-09-07*
