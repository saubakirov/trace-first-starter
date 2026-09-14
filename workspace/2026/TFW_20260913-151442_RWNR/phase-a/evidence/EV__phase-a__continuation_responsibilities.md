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

## Revision Round 1 — Corrected Assurance Evidence

> **Date**: 2026-09-13
> **Replacement Candidate / producer**: `ddb6fc4a1ab528525abd1020ee2fb562d4e10f65`
> **Prior rejected Candidate**: `c319269d24abb89a58e2dc1a18ada1ea4ecb8120`
> **Independent REVIEW producer**: `99685b70c18bc19fcda7c7543d2d0545acc2912b`
> **Coordinator ruling / restart base**: `d68e797c60811c4566be68397dc83da9d4f5089c`

The original evidence rows above are preserved as the prior epoch; independent REVIEW §2 and
`review/verify.md` disproved their AC-2–AC-6 assurance sufficiency. They are not relabeled. The rows
below are new observations for the Coordinator-ruled rung-1 return and replacement Candidate.

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| R1-E1 | AC-1 | `git diff --exit-code` from prior Candidate to replacement Candidate is empty for canonical Plan, both Plan receivers and all three named Resume surfaces. The replacement commit itself contains only the two approved ASSURANCE paths. Recomputed VALUE remains the same three MODIFY paths, SHA-parity Plan/C 1,199, and 255 additions + 492 deletions = 747 touched text LOC. | Git objects at replacement Candidate; strict UTF-8 counter | VERIFIED | `phase-a-accounting__round-1.json`; `phase-a-tests__round-1.txt` |
| R1-E2 | AC-2 | Each of 28 cases is materialized as an active/historical filesystem with request, config, task/phase status, selected-carrier authority, ordered journal, approval/REVIEW inputs and binary sentinel as applicable. The evaluator reads those carriers plus parsed Candidate Plan table semantics. Every receipt exposes the observed inputs and equal repository pre/post SHA-256. Collision/history/phase/approval/terminal/unknown and wrong-RES mutations change the observable result and are independently rejected. | Python 3.13.5; isolated temporary Git repositories | VERIFIED | `phase-a-routing__round-1.json`; `phase-a-tests__round-1.txt` |
| R1-E3 | AC-3 | Ten identity cases materialize status, authority-selected principal, session acting/current unit and role, ordered created/dispatch journal, root/destination/parent/channel edge and title readback. Every case exposes source/carrier identities and equal pre/post hashes; invalid indicated-AT cases stop unchanged. Child-LEAD, inference, skipped re-resolution, forwarded selection, principal-only dispatch, missing readback and altered readback adversaries change projection and reject or continue unclaimed as required. | Candidate Plan source plus materialized authority/session/journal carriers | VERIFIED | `phase-a-routing__round-1.json` |
| R1-E4 | AC-4 | Route outputs are parsed from Candidate Plan selection clauses and lifecycle rows after the materialized carrier is observed. The source-effect projection detects smuggled `status.md` writes and workflow invocation; the Reviewer’s write-smuggling counterexample is recorded as a prior false green, now changes the projection and rejects while repository hashes remain equal. Coordinator-control routes continue to resolve from the shipped Plan source. | Source-semantic parser and before/after repository hashes | VERIFIED | `phase-a-routing__round-1.json`; `phase-a-tests__round-1.txt` |
| R1-E5 | AC-5 | Config and all four supported adapters are classified as one five-subject connected group before any write. The old-exact Antigravity/foreign-Claude adversary refuses with identical whole-group pre/post SHA-256; no adapter result is applied. The clean group covers absent, owned and target-current classes, converges ten unique commands for all four adapters, and has an empty second run. Replacement-Candidate history independently reproduces 179 task entries and all three aggregate subsequences. Resume is unchanged. | Isolated connected receiver roots; Candidate Git history | VERIFIED | `phase-a-receiver-migration__round-1.json`; `phase-a-history__round-1.json` |
| R1-E6 | AC-6 | After replacement Candidate freeze, the exact targeted suite passed 355/355; configured collection found 625 tests; configured suite passed 624 with one platform skip and zero failures. All 15 adversarial families change observable projection and reject; the three Reviewer counterexamples explicitly record their legacy false-green status and corrected rejection. | Local pytest at immutable replacement Candidate | VERIFIED | `phase-a-tests__round-1.txt`; round-1 structured receipts |
| R1-E-accounting | AC-1 / approved accounting contract | Approval remains proposal `413945ca0a4f34065ff22b8b24f47bf694d72710`, TS blob `d15c5dc8b25c2751ed289a418f937226608333dc`, owner event `journal/20260913-194049__dispatch__f58c.md`; Coordinator rung-1 ruling is `d68e797c60811c4566be68397dc83da9d4f5089c`. Full Baseline `f6e85aa898061779c6b37bba34dc97e28c76f01f` → replacement Candidate `ddb6fc4a1ab528525abd1020ee2fb562d4e10f65`; literal VALUE membership remains MODIFY/VALUE for `.tfw/workflows/plan.md`, `.agents/workflows/tfw-plan.md`, `.claude/commands/tfw-plan.md`, each 85 additions + 164 deletions, totaling 255 + 492 = 747 touched text LOC and 3 logical files. The two round changes are ASSURANCE; TRACE is excluded; binary/non-text N/A. Phase attribution is exactly Phase A with no INVALID ambiguity. No 50-file/5,000-LOC or 2× trigger fires; no split is useful. Immutable `3/900` authority predates all work and did not ratchet; replacement Candidate was frozen before this EV/RF epoch. Reproduction remains the approved NUL-safe `git diff --name-status/--numstat --find-renames=50% -z <Baseline> <Candidate> -- <three literal VALUE paths>`; visible NUL escaping and raw results are in the text receipt. | Git 2.42.0.windows.1; immutable replacement Candidate | VERIFIED | `phase-a-accounting__round-1.json`; `phase-a-tests__round-1.txt` |

Revision-round-1 evidence verdict: 7/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A. Independent
acceptance remains the same Reviewer’s next act; this Executor evidence does not supply that verdict.

---

*EV — TFW_20260913-151442_RWNR / Phase A: Rehome continuation responsibilities | 2026-09-13*
