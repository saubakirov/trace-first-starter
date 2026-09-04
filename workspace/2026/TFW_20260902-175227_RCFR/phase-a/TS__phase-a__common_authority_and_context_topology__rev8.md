# TS revision 8 — TFW_20260902-175227_RCFR / Phase A: Evidence Return Contract

> **Date**: 2026-09-04
> **Author**: Codex (Coordinator), acting on behalf of `saubakirov`
> **Status**: ✅ APPROVED — `saubakirov`; standing Phase A completion instruction and explicit whole-tree overrun authorization
> **Supersedes**: [TS revision 7](TS__phase-a__common_authority_and_context_topology__rev7.md) — revisions 1–7 remain immutable history
> **Returned by**: [REVIEW revision 3](REVIEW__phase-a__common_authority_and_context_topology__rev3.md) — 🔄 REVISE, evidence-only D1/D2
> **Reviewed candidate**: `09ba0704f1dc7c4979221d9d53ee52e4667ac68b`
> **Ordered by**: Coordinator `saubakirov` via Codex

---

## 1. Contract Correction

Revision 7 correctly orders the two evidence fixes but says not to change RF. Canonical
`/tfw-handoff` requires every returned round to append its own ONB/RF account. This revision changes
only that procedural restriction: prior RF and ONB text remain immutable, while one concise
revision-8 subsection may be appended to each. Every other requirement and basis in revision 7
continues to govern.

## 2. Exact Work

1. Append to `evidence/EV__phase-a__common_authority_and_context_topology.md` that the reviewed
   candidate `09ba070` is **69 paths; 4,278 additions + 1,239 deletions = 5,517 LOC**, superseding
   its stale `68 / 5,505` line. Retain the correct scoped **41 paths / 3,795 LOC** result.
2. Append to `evidence/semantic-fixtures.txt` that the exact minimal-P1 failure is
   **`P1: artifacts_created semantic source resolved 0 times`**, superseding the stale
   `refusal_reason` statement.
3. Reproduce only the targeted adverse test and the two fixed-snapshot numstat counters. Append
   the concise return to the existing ONB and RF, reconcile `.tfw/knowledge_state.yaml` last, and
   write only the canonical phase status/journal transitions.

No code, test, HL, TS, REVIEW, workflow, adapter, derived-copy, Phase B/C, unrelated trace, or other
evidence file may change. Do not rerun the full suite already accepted by REVIEW revision 3.

## 3. Acceptance and Bound

- Both append-only corrections name revision 8 and commit `09ba070`; the old observations remain
  visible as history and cannot be mistaken for current evidence.
- The adverse test passes and direct execution yields the exact `artifacts_created` error.
- Fixed-snapshot counters reproduce `69 / 4,278 / 1,239 / 5,517` whole and
  `41 / 2,559 / 1,236 / 3,795` scoped.
- The final RF separately reports the post-trace candidate count; immediate state replay has no
  pending, removed, or problem task IDs.
- The implementation/test/evidence limit remains **41 paths / 4,600 LOC**. The phase-only
  all-trace ceiling remains **7,000 LOC**; `.tfw/project_config.yaml` remains 5,000 and unchanged.

The same Executor commits and stops after RF. The Coordinator integrates exact commits and resumes
the same Reviewer for REVIEW revision 4. Master/shared branches, merge, rebase, and push remain
prohibited.

---

*TS revision 8 — TFW_20260902-175227_RCFR / Phase A: Evidence Return Contract | 2026-09-04*
