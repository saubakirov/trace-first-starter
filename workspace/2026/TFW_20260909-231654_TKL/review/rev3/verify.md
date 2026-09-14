# Verify — R2 REVIEW carrier correction

> **Reviewer:** robert, Reviewer task `01a09aaf-9af3-7d13-8ef8-59d3bc84d5e7`
> **Substantive evidence source:** commit `2cc0143875ee275bc01495f728fc631b24e4d59c`
> **Min verify ratio:** `0.42`
> **New RF/VALUE/ASSURANCE claims:** `0`; this is a record-only carrier correction

## Verification Log

### V1 — revision topology

- **Claim:** R2 is a separate REVIEW repair round and must be the next immutable sibling.
- **Actual:** revision 1 is the unsuffixed REVIEW; revision 2 is
  `REVIEW__TFW_20260909-231654_TKL__rev2.md`. R2 followed the R1 REVISE and Coordinator ruling
  `16bc29cd...`, traversed `RF → ONB → RF`, produced Candidate `a99ba6cd...`, and received its own
  independent judgment at `2cc0143`. Under `The revision suffix, and what it generates`, the highest
  valid current REVIEW must therefore be sibling `__rev3`, naming revision 2 and the governing source.
- **Match:** ✅

### V2 — preservation of the misplaced source

- **Claim:** revision 2 and the three `review/rev2/` stage files remain unchanged history.
- **Actual:** before authoring revision 3, the four `2cc0143` paths match their committed Git blobs.
  Their SHA-256 values are `f2206ea5...` (REVIEW rev2), `0583198d...` (map), `eea88fe2...`
  (verify) and `49337b84...` (judge). Revision 3 references rather than edits them.
- **Match:** ✅; exact hashes were rechecked at the final carrier-only pre-commit gate.

### V3 — substantive verdict identity

- **Claim:** the carrier correction changes no R2 finding or proposal.
- **Actual:** revision 3 retains the `2cc0143` conclusions: AC-5 and affected AC-9 PASS; affected
  AC-8/final Executor report rendering PASS within recorded limits; accounting is 58 VALUE,
  53M/4A/1D and `+1235/-1005 = 2240`; AC-7 and dependent AC-11 remain BLOCKED; verdict remains
  🔄 REVISE with the same single rung-1 proposal and origin
  `{principal: robert, unit: Reviewer 01a09aaf-9af3-7d13-8ef8-59d3bc84d5e7}`.
- **Match:** ✅; no substantive re-evaluation performed.

### V4 — actual MkDocs observation paths

- **Persisted Candidate-checkpoint build:**
  - receipt: `C:\Users\c0rpa\.codex\worktrees\19a7\steps-framework\workspace\2026\TFW_20260909-231654_TKL\evidence\r2-checkpoint\05-docs-build\receipt.json`
  - stdout: `C:\Users\c0rpa\.codex\worktrees\19a7\steps-framework\workspace\2026\TFW_20260909-231654_TKL\evidence\r2-checkpoint\05-docs-build\stdout.raw`
  - stderr: `C:\Users\c0rpa\.codex\worktrees\19a7\steps-framework\workspace\2026\TFW_20260909-231654_TKL\evidence\r2-checkpoint\05-docs-build\stderr.raw`
  - actual output: `C:\Users\c0rpa\AppData\Local\Temp\TFW_TKL_NATIVE_01a09a0c\r2-current-description-site`
- **Later Reviewer final-report observation:** actual output remains at
  `C:\Users\c0rpa\AppData\Local\Temp\TFW_TKL_REVIEW_01a09aaf\r2-final-site-1409cbd`
  with 2,058 files. It ran interactively and did **not** create local receipt/stdout/stderr files;
  its command transport is not retroactively promoted to a persisted raw artifact. Revision 3 states
  this limit explicitly and does not run a replacement build.
- **Match:** ✅ path existence checked for all five distinct paths: three persisted raw artifacts and
  the two output directories.

## Commands Executed

| # | Command / read | Result |
|---|---|---|
| 1 | Resolve highest REVIEW lineage and read `Artifact file naming` revision rule | `__rev3` required for the distinct R2 return |
| 2 | Hash the four `2cc0143` files and compare their Git blobs | exact before authoring and at the final pre-commit gate |
| 3 | `Test-Path` persisted receipt/stdout/stderr and both MkDocs output roots | all six paths exist |

No build, test, native case, accounting replay or substantive review stage was repeated.

## Claim & Source Checks

| # | Claim / citation | Traces to | Holds? |
|---|---|---|---|
| C1 | REVIEW revisions are immutable siblings and consumers select the highest valid lineage | `.tfw/conventions.md` → `The revision suffix, and what it generates` | ✅ |
| C2 | R2 is distinct from R1 | ruling `16bc29cd...`, Candidate `a99ba6cd...`, return `b91ec17...`, verdict source `2cc0143` | ✅ |
| C3 | R2 conclusions and single proposal remain unchanged | exact `2cc0143` REVIEW/stage bytes | ✅ |

## Discrepancy and resolution

`2cc0143` placed the independent R2 verdict inside revision 2. Revision 3 is the current carrier
correction; it preserves the erroneous placement as source history and does not claim that revision 2
was validly the highest R2 carrier.

## Evidence Verification

The substantive R2 evidence audit remains [revision 2 Verify](../rev2/verify.md), committed at
`2cc0143`. This correction adds no RF §5 evidence claim. The only new evidence is naming lineage,
source-byte preservation and real local observation-path existence, all checked directly above.

## Knowledge Citations Verified

The fifteen substantive PV/citation rows remain the exact `2cc0143` audit and are unaffected by a
filename carrier correction. No new knowledge claim or citation is introduced; repeating the full PV
scan would add no affected verification under D86.

## Checkpoint

- [x] Verified the exact revision rule and R2 lineage.
- [x] Preserved the four `2cc0143` source files by hash and Git identity.
- [x] Kept every substantive conclusion, limit and proposal unchanged.
- [x] Named real persisted MkDocs receipt/stream/output paths and disclosed the later interactive build's absent raw files.
- [x] Performed no replacement build, test, native run or full-stage replay.

Stage complete: **YES**
