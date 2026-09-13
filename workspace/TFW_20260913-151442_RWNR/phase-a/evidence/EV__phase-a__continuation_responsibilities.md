# EV — TFW_20260913-151442_RWNR / Phase A: Rehome continuation responsibilities

> **Date**: 2026-09-13
> **Author**: robert, Executor unit `01a09b39-f0c0-70c0-9b53-6981647e72fb`
> **Task**: TFW_20260913-151442_RWNR
> **TS**: [TS Phase A](../TS__phase-a__continuation_responsibilities.md)
> **Candidate / producer**: `c319269d24abb89a58e2dc1a18ada1ea4ecb8120`

---

## Environment

| Field | Value |
|---|---|
| OS | Windows |
| Language / Runtime | Python 3.13.5; Git 2.42.0.windows.1 |
| Database | N/A |
| Deploy target | N/A — repository workflow and assurance change |
| CI / Pipeline | Local pytest at immutable Candidate |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | Candidate changes only the three approved VALUE paths plus two approved ASSURANCE paths. Canonical Plan and receivers have SHA-256 `47c79864b215c176e170da39e2b26067ecb04d60c894440c992e47b7e12b5749`; Plan and complete retained instruction surface are 1,199 words, below 1,200 and baseline 2,737. No new/unclassified instruction source or Resume path changed. | Candidate Git tree; strict UTF-8 Unicode `\S+`; NUL-safe Git diff | VERIFIED | `phase-a-accounting.json`; `phase-a-tests.txt` |
| E2 | AC-2 | All 28 source-derived selection, phase, lifecycle, approval, review, terminal and unknown-state fixtures produced the exact result/route. Every temporary-repository before/after path-byte map was identical, and collision/history/phase/approval/terminal/unknown mutants changed projection and were rejected. | Python 3.13.5; temporary Git repositories | VERIFIED | `phase-a-routing.json`; `phase-a-tests.txt` |
| E3 | AC-3 | Ten continuation identity cases distinguish non-AT, valid root, same-principal child, missing/ambiguous/stale/foreign/wrong-root facts, rename failure and altered readback. Valid root alone claims LEAD; children remain PLAN; invalid indicated AT stops; transport failures continue unclaimed. | Source-derived Plan and central session-identity contract | VERIFIED | `phase-a-routing.json` |
| E4 | AC-4 | The pre-route contract returns routes only, never invokes another workflow or performs phase choice, transition, approval, close/repair, review, implementation or knowledge effects. `KNW`, close/repair and APPROVE-carrier mismatch resolve to the fixed `Closing and record recovery` Coordinator control address; all seven semantic mutant families fail independently. | Source projection and full contract regression suite | VERIFIED | `phase-a-routing.json`; `phase-a-tests.txt` |
| E5 | AC-5 | Phase A leaves all Resume/live-retirement paths unchanged. Temporary receiver trials cover `ABSENT`, `OWNED_EXACT`, `OWNED_BLOCK`, `TARGET_CURRENT` and `FOREIGN_OR_DRIFTED`, preserve refused groups, converge four adapters to ten commands and produce an empty second run. The 179 task-tree entries reproduce digest `ed52c4c26845e90c14a569f867ec2200b18da44374f7df2fd897bf7fb58bef96`; all three aggregate baseline blobs remain ordered raw-line subsequences and destructive mutants fail. | Candidate Git objects and isolated receiver trees | VERIFIED | `phase-a-receiver-migration.json`; `phase-a-history.json` |
| E6 | AC-6 | Candidate-bound targeted suite passed 355/355; configured collection found 625 tests; configured suite passed 624 with one platform skip and zero failures. Candidate contains exactly the five approved VALUE/ASSURANCE paths; all evidence files are TRACE-only and are not runtime readers. | Local pytest at Candidate | VERIFIED | `phase-a-tests.txt`; four structured JSON receipts |
| E-accounting | AC-1 / approved accounting contract | Approval: `413945ca0a4f34065ff22b8b24f47bf694d72710`, TS blob `d15c5dc8b25c2751ed289a418f937226608333dc`, owner act `journal/20260913-194049__dispatch__f58c.md`. Full Baseline `f6e85aa898061779c6b37bba34dc97e28c76f01f` → Candidate `c319269d24abb89a58e2dc1a18ada1ea4ecb8120`; literal selector contains three MODIFY/VALUE paths, each 85 additions + 164 deletions, totaling 255 + 492 = 747 touched text LOC and 3 logical files. ASSURANCE and TRACE are excluded by approved membership; binary/non-text is N/A. Phase attribution is exactly Phase A, no INVALID ambiguity. Below 50-file/5,000-LOC and 2× triggers, so no split/return trigger fires. The immutable `3 VALUE files / 900 touched text LOC` denominator was approved before work and Candidate was frozen before EV/RF. Exact method: `git diff --name-status/--numstat --find-renames=50% -z <Baseline> <Candidate> -- <three literal paths>`; NUL bytes are visibly escaped in the text receipt. | Git 2.42.0.windows.1; immutable Candidate | VERIFIED | `phase-a-accounting.json`; `phase-a-tests.txt` |

## Verdict

Evidence verdict: 7/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

---

*EV — TFW_20260913-151442_RWNR / Phase A: Rehome continuation responsibilities | 2026-09-13*
