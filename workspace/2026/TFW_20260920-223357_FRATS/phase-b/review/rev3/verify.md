# Verify — Phase B formal review round 3

> **Mindset:** Auditor; verify the repaired evidence rather than replay unchanged product work.
> **Test:** If RF Return Round 3 disappeared, would the committed harness/output and immutable objects
> independently establish the repaired claims?
> **Min verify ratio:** 0.42
> **Affected RF evidence files:** 4 (`.py`, `.txt`, EV, RF)
> **Files required:** ceil(4 × 0.42) = 2
> **Files verified:** 4/4, plus ruling, ONB, status/journal and immutable source objects.

## Verification Log

### V1 — `evidence/rung2-semantic-replay.py`

- **RF claim:** a self-contained task-local harness reads named immutable objects, defines every
  predicate/mutation, fails on ambiguity or unmet conditions and introduces no product runtime/test.
- **Actual:** the 302-line script uses `git show <ref>:<path>` for all semantic inputs, fixes TS,
  transcript-ruling, evidence-ruling and Candidate refs as constants, requires each mutation literal
  to occur exactly once, evaluates the positive source predicate, removes one named clause in memory,
  requires the same predicate to fail, checks the affected edge set and exits 1 on any assertion or
  Git failure. It lives only under task-local `evidence/` and imports no framework runtime.
- **Match:** ✅

### V2 — `evidence/rung2-semantic-replay.txt`

- **RF claim:** exact command, environment, immutable refs, harness hash, predicate contract, full
  output and exit status are durable.
- **Actual:** the recorded command runs successfully from the repository root. Fresh output is
  byte-for-byte equal after line-ending normalization to the `EXACT OUTPUT` block: 32 lines, 11
  static checks, 13 positive/negative cases, affected-edge summary and `OVERALL PASS`; exit 0. The
  fresh SHA-256 is exactly
  `b64ae4ba2da96c048cf155a872b4b5c854596cfa9147cf8bda158fcfd9c7d59c`.
- **Match:** ✅

### V3 — affected EV rows

- **RF claim:** E3-R3, E10-R3, E12-R3 and E-accounting-R3 supersede only the formerly unsupported
  replay claims and preserve Candidate/accounting.
- **Actual:** each row points to the executable harness and exact output. E3-R3 describes 13
  source-derived cases and their named mutations; E10-R3 identifies Plan/static and entry cases;
  E12-R3 identifies provider/observation cases; E-accounting-R3 names the prior independent
  accounting and the evidence-only ruling. No unaffected EV row is relabelled.
- **Match:** ✅

### V4 — RF Return Round 3

- **RF claim:** evidence-only repair, no Candidate movement, 4/4 affected rows verified and only AC-9
  remains downstream.
- **Actual:** the section names ruling `4cd43977…`, Candidate `93186cea…`, executable commit
  `4d1c25e…`, exact command/hash/output, affected records and a no-VALUE boundary. Git confirms the
  Candidate is an ancestor and Candidate→RF-transition has zero diff across all 47 VALUE/product
  surfaces. The ruling→transition range changes only ONB/REVIEW ruling/RF/EV/replay/status/journal.
- **Match:** ✅

## Commands Executed

| # | Command / check | Result |
|---:|---|---|
| 1 | `python workspace/2026/TFW_20260920-223357_FRATS/phase-b/evidence/rung2-semantic-replay.py` | PASS — Python 3.13.5; Git 2.42.0.windows.1; 32 lines; 11 static checks; 13/13 positive and 13/13 negative cases; exit 0. |
| 2 | Compare fresh stdout with the `.txt` `EXACT OUTPUT` block after CRLF→LF normalization | PASS — exact equality. |
| 3 | `Get-FileHash -Algorithm SHA256` on the harness | PASS — `b64ae4ba…d59c`, exact recorded value. |
| 4 | `git merge-base --is-ancestor 93186cea… 55ad930c…` | PASS — Candidate is an ancestor of the evidence return. |
| 5 | Candidate→RF-transition diff over canonical/shared/template/workflow/adapter/generated VALUE surfaces | PASS — no path and no byte changed. |
| 6 | Ruling→RF-transition `name-status`/`numstat` | PASS — task-local ONB, REVIEW ruling, RF, EV, replay, status and two journal events only; no VALUE/ASSURANCE/receiver path. |
| 7 | `git diff --check 4cd43977… 55ad930c…` | PASS — no output. |
| 8 | Compare harness/output at executable commit `4d1c25e…` with RF-transition `55ad930c…` | PASS — no later change. |
| 9 | Compare P0–P7 sources, master/phase HL and TS rev2 from REVIEW rev2 to the RF transition | PASS — no changed path; prior 20/20 citation verification remains applicable. |

The configured product suite was not rerun: Candidate, all product inputs and the suite oracle are
byte-identical to REVIEW revision 2, where 14 tests and the 54-schedule dry-run were independently
verified. The only changed executable is task-local evidence and was run directly above.

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---:|---|---|---|---|
| C1 | “Fresh replay: 32 output lines … exit 0” | RF Return Round 3 §4; transition event | Independent command execution and exact `.txt` comparison | ✅ — 32/32 exact; exit 0. |
| C2 | “13/13 positive plus 13/13 material-negative scenarios” | RF §4; EV E3-R3 | Executable `SCENARIOS`, `mutate`, `evaluate` and fresh stdout | ✅ — every source predicate resolves; every unique one-clause mutation makes it fail. |
| C3 | “Candidate remains `93186cea…`; this round changes TRACE only” | RF accounting; EV E-accounting-R3 | Git ancestry and exact Candidate→return VALUE/product diff | ✅ — no Candidate movement or product-path change. |
| C4 | AC-10/AC-12 exact-source support | EV E10-R3/E12-R3 | TS/ruling/Candidate objects named in harness | ✅ — exact static blocks and provider/entry/isolation predicates reproduce. |

The harness labels its affected scenario dimensions as activation, authority, continuation,
evidence, observation and provider. The canonical AC-3 edge names remain activation, authority,
evidence, recovery, continuation and exception. Cumulative `six-edge-replay.md` explicitly maps
durable return to recovery and invalid/stalled cases to exception, while unchanged executable rung-1
evidence retains the canonical recovery/exception checks. Thus full AC-3 coverage is established by
the cumulative evidence set; the new harness establishes the previously unsupported revision-2 and
isolation predicates rather than silently replacing the canonical oracle.

## Discrepancies Found

No discrepancies.

## Evidence Verification

| # | RF evidence ref | Artifact exists? | Matches claim? |
|---:|---|---|---|
| E3-R3 | `rung2-semantic-replay.py` + `.txt` | ✅ | ✅ — executable predicates, unique critical mutations, exact sources/output and exit independently reproduce. |
| E10-R3 | harness `static_checks` and entry/GATEWAY scenarios | ✅ | ✅ — exact Plan blocks, dispatch, ≤1,400 bound and affected entry cases pass. |
| E12-R3 | provider/observation scenarios | ✅ | ✅ — seven mappings, bounded signals/returns and prohibited inspection cases pass their source/mutation predicates. |
| E-accounting-R3 | prior table plus Git preservation check | ✅ | ✅ — immutable Candidate/accounting inputs are unchanged; this return changes TRACE/control records only. |
| E9-R2/R3 | downstream acceptance/Docs/terminal lineage | N/A yet | ✅ as DEFERRED — independent verdict is this round's output; D75 Docs effect and close remain correctly downstream. |

Affected evidence verdict is **4/4 VERIFIED**. Combined with unchanged REVIEW revision 2 results, the
Candidate evidence is 12/13 VERIFIED and one deliberately downstream AC-9 row.

## Knowledge Citations Verified

REVIEW revision 2 independently verified all 20 HL §7.2/ONB §7 citations. Git comparison proves that
the master citation list, P0–P7 sources, `KNOWLEDGE.md`, North Star, conventions, governing TS and
Candidate did not change in this evidence-only round. That verification therefore remains applicable.
ONB Return Round 4 additionally cites four already-resolved sources: REVIEW revision 2 §4/§8,
approved TS AC-3/AC-10/AC-12, transcript isolation/F19 and exact-path staging/K17; each resolves and
matches its asserted use.

| Set | Total | Resolved | Semantically verified | Irrelevant | Hallucinated |
|---|---:|---:|---:|---:|---:|
| Master HL §7.2 / inherited ONB | 20 | 20 | 20 | 0 | 0 |
| ONB Return Round 4 additions | 4 | 4 | 4 | 0 | 0 |

`KNOWLEDGE.md` remains unchanged. D75 still contains the known 112,536/−63.8% source inconsistency;
the accepted correction remains the separately ruled post-APPROVE Docs effect and is not evidence
work in this return.

## Checkpoint

**Self-check:**

- [x] Opened and recorded all 4/4 affected evidence files (minimum 2).
- [x] Independently ran the repaired harness and established applicability of unchanged evidence.
- [x] Claim & Source Checks cover the command/output, scenario count, Candidate identity and exact authority objects.
- [x] Every affected RF §3 acceptance claim was checked against actual files and immutable refs.
- [x] `KNOWLEDGE.md` currentness and the unchanged D75 route were checked.
- [x] All inherited and Return Round 4 knowledge citations resolve and remain semantically applicable.
- [x] Every affected RF §5/EV artifact exists and matches its assigned status.

Stage complete: **YES**

### Selected knowledge evidence

The material inputs are the Coordinator ruling at `4cd43977…`, ONB Return Round 4, executable replay
commit `4d1c25e…`, EV/RF commit `9f61f8e…`, RF transition `55ad930c…`, preserved Candidate and the
prior independent REVIEW revision 2. The repair is repository- and command-readable; no other role's
transcript, terminal, tool output or unreturned working tree was used. Uncertainty from the prior
verdict is closed: the durable harness now reproduces the exact predicates and mutations. Remaining
uncertainty is only the deliberately downstream independent verdict, D75 effect/follow-up and close.
