# Verify — Review Revision 4: “Are the claims true?”
> **Mindset:** Auditor. The RF is a declaration, not a fact.
> **Test:** “If I removed the RF, would the evidence alone prove the work was done?”
> **Min verify ratio:** 0.42 default
> **RF files claimed:** 10 return paths
> **Minimum:** 5 paths; **actual:** 10/10 return paths inspected, with immutable blob checks for the accepted implementation, HL, prior TS/REVIEW, common authority, and other evidence

## Verification Log

### V1: candidate identity and exact delegation lineage
- **RF claim:** Revision 8 is complete at the supplied evidence-return candidate.
- **Actual:** Clean review-3 HEAD `4e75ba46fe74cf3469165024eadce382e1c326b0` and supplied candidate base `bd5a844` share tree `b5baefc59404dbcd6b3c7400bea30b0ade84226b`. The four supplied commits were applied in the exact order TS7 → TS8 → ONB/handoff → RF/evidence/state. Local parent `61e1fd807515f2b077e4a3dedb46dbdc3476608e` and supplied candidate `2535102a1af25f38af226d1f88e42ba4a647c57f` share tree `993c23afe85c666088f68c839be7c00e100eb17f`. The worktree was clean before review writes.
- **Match:** ✅

### V2: REVIEW revision 3 D1 — exact counters
- **RF claim:** The EV append supersedes the stale whole-tree observation with exact fixed-snapshot counters while retaining the correct scoped result.
- **Actual:** Independent `git diff --numstat 2728dae…09ba070` replay gives **69 paths, 4,278 additions, 1,239 deletions, 5,517 LOC**. Filtering the 36 non-task implementation/test paths plus five Phase-A evidence paths gives **41 paths, 2,559 additions, 1,236 deletions, 3,795 LOC**. EV retains the historical `68 / 5,505` line, names revision 8 and `09ba070`, and explicitly supersedes it with both exact results.
- **Match:** ✅ — D1 closed

### V3: REVIEW revision 3 D2 — exact minimal-source failure
- **RF claim:** The semantic evidence append supersedes the stale `refusal_reason` statement with the exact first failure.
- **Actual:** The exact adverse test passes **1 passed, 72 deselected**. Direct execution using the same heading-plus-anchor fixture exits 1 with `P1: artifacts_created semantic source resolved 0 times`. `semantic-fixtures.txt` retains the old statement as history, names revision 8 and `09ba070`, and calls the new result its exact superseding result.
- **Match:** ✅ — D2 closed

### V4: append-only boundary and immutable blobs
- **RF claim:** No implementation, test, HL, prior TS, REVIEW, workflow, adapter, derived-copy, unrelated trace, or other evidence changed.
- **Actual:** `git diff --name-status 4e75ba4…2535102` contains exactly ten authorized paths. The only evidence changes are EV and `semantic-fixtures.txt`; the other three Phase-A evidence blobs are identical. Runtime implementation/test, gen-index implementation/test, integration test, `AGENTS.md`, conventions, glossary, `KNOWLEDGE.md`, master/phase HL, TS rev6, and REVIEW rev3 blobs are exact. The only TS differences are new immutable revisions 7 and 8; all prior TS and review-stage artifacts are unchanged.
- **Match:** ✅

### V5: project, state, and lifecycle replay
- **RF claim:** Project consistency and immediate state-last knowledge replay pass; lifecycle returns to RF under TS rev8.
- **Actual:** `--check project` passes. At the returned candidate, `--knowledge-pending --format json` reports 61 current task digests with `migration_required: false` and empty `pending_task_ids`, `removed_task_ids`, and `problems`. Status names `RF`, authority TS rev8, and timestamp `20260904-094900`; matching handoff and transition events record `TS_DRAFT → ONB → RF`. The task diagnostic retains only the immutable RDP 123>120 problem plus informational legacy phase-state notes.
- **Match:** ✅

### V6: post-trace bound and diff hygiene
- **RF claim:** The separately measured post-trace return is 78 paths and 6,065 LOC, under the owner-approved 7,000 phase-only all-trace ceiling.
- **Actual:** `git diff --numstat 2728dae…2535102` gives **78 paths, 4,826 additions, 1,239 deletions, 6,065 LOC**; local tree-identical HEAD gives the same result. Both the fixed candidate diff and the return diff pass `git diff --check`.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | base/candidate tree and exact four-commit lineage checks | Base trees equal; return trees equal; exact supplied order applied; clean before review writes |
| 2 | `python -m pytest docs/scripts/test_runtime_context.py -q -k "test_round2_minimal_anchor_only_source_cannot_manufacture_a_record"` | **1 passed, 72 deselected** |
| 3 | direct execution of the test’s P1 heading-plus-anchor fixture | Expected exit 1; exact error `P1: artifacts_created semantic source resolved 0 times` |
| 4 | fixed whole `git diff --numstat 2728dae…09ba070` | **69 / 4,278 / 1,239 / 5,517** |
| 5 | fixed scoped numstat filter | **41 / 2,559 / 1,236 / 3,795** |
| 6 | post-trace `git diff --numstat 2728dae…2535102` | **78 / 4,826 / 1,239 / 6,065**, below 7,000 |
| 7 | `python .tfw/scripts/gen_index.py --check project` | PASS |
| 8 | `python .tfw/scripts/gen_index.py --knowledge-pending --format json` | 61 current; pending/removed/problems empty; migration false |
| 9 | `python .tfw/scripts/gen_index.py --check tasks` | Sole problem is unchanged RDP 123>120; six informational historical groups |
| 10 | return-path enumeration and representative blob comparisons | Exactly 10 authorized paths; all excluded/prior blobs exact |
| 11 | `git diff --check` on fixed candidate and evidence-return ranges | PASS |

The full suite was deliberately not rerun: TS revision 8 prohibits reopening REVIEW revision 3’s
accepted R4/full-suite result.

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | Reviewed snapshot is 69 paths and 5,517 LOC | RF §12.3–§12.4; EV R8-E2 | Primary fixed-snapshot numstat | ✅ |
| C2 | Scoped snapshot remains 41 paths and 3,795 LOC | RF §12.3–§12.4; EV R8-E2 | Explicit non-task-plus-five-evidence filter | ✅ |
| C3 | Minimal P1 first fails on `artifacts_created` | RF §12.3–§12.4; EV R8-E1; semantic append | Targeted pytest and exact direct probe | ✅ |
| C4 | Prior false observations remain visible but are superseded | EV revision-6/revision-8 sections; semantic revision-6/revision-8 sections | Direct file inspection | ✅ |
| C5 | Only authorized evidence/lifecycle/governing files changed | RF §12.1; TS rev8 §2 | Complete `4e75ba4…2535102` path diff and blob identities | ✅ |
| C6 | Post-trace candidate is 78 paths and 6,065 LOC | RF §12.4 | Primary post-trace numstat | ✅ |

## Discrepancies Found

None. REVIEW revision 3 D1 and D2 are closed exactly and append-only. No new acceptance,
authority, evidence, scope, or lifecycle discrepancy was found.

## Evidence Verification

| # | RF/EV revision-8 evidence ref | Artifact exists? | Matches claim? |
|---|-------------------------------|-----------------|----------------|
| R8-E1 | Targeted adverse test and exact direct error | ✅ | ✅ — reproduced independently |
| R8-E2 | Whole and scoped fixed-snapshot counters | ✅ | ✅ — both reproduced exactly |
| RF §12 post-trace | Separate all-trace counter and ceiling | ✅ | ✅ — 6,065 < 7,000 |
| State-last replay | Project and knowledge state checks | ✅ | ✅ — clean current/processed reconciliation at candidate |

## Knowledge Citations Verified

No new knowledge citation was introduced by revision 8. The 13 master-HL §7.2 / cumulative ONB §7
applications retain exact source blobs and their REVIEW revision 3 verification. `KNOWLEDGE.md` still
contains the already-recorded stale Architecture Map `Adapters` row, so `/tfw-docs` remains required
after approval; the Reviewer did not edit it.

## Checkpoint

**Self-check:**
- [x] Inspected 10/10 evidence-return paths and the immutable exclusion surfaces?
- [x] Reproduced both exact counters, the targeted adverse test, and the direct failure text?
- [x] Verified old observations remain visible and explicitly superseded?
- [x] Verified project/state/lifecycle and the separately bounded post-trace candidate?
- [x] Avoided rerunning or re-reviewing the accepted implementation and full suite?
- [x] Checked evidence existence and sufficiency independently?

Stage complete: YES
