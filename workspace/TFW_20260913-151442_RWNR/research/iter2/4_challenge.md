# Challenge — Iteration 2: falsify the retirement configurations

> **Mindset:** Critic. A survivor must withstand wrong state, wrong owner, stale receiver, rewritten history, and misleading arithmetic.
> Parent: [HL-TFW_20260913-151442_RWNR](../../HL-TFW_20260913-151442_RWNR.md)
> Goal: decide whether Resume can be retired without loss of lifecycle safety, trace integrity, or a discoverable recovery path.

## Consistency Check

| Pair | Compatibility | Reason |
|---|---|---|
| pure Plan router × Plan-owned close writes | incompatible | Plan's Role Lock permits planning/control rulings, not closing effects or independent acceptance; routing may name the direct contract only |
| manifest omission × existing receiver convergence | incompatible | current sync copies target rows but never removes an absent-manifest command |
| permanent tombstone × exact ten-command/no-replacement surface | incompatible | a redirect remains an eleventh public or hidden continuation entry |
| whole-file aggregate identity × a truthful new changelog/knowledge record | incompatible | new additive history would fail even when every pre-existing statement remains exact |
| unexplained 2,685 × reproducible baseline/candidate arithmetic | incompatible | no named rule or Git revision produces both frozen operands |
| extracted continuation helper × “no renamed Resume” | incompatible | it preserves the same long-lived branching surface under another name |
| repeated lifecycle guards × one canonical selection/state owner | incompatible | guards drift and force non-Coordinator workflows to repeat discovery decisions |
| changed Plan still above 1,200 × the current Design Rule | incompatible | a disposition without compliance is insufficient when this change directly rewrites Plan |
| owned-only deletion × foreign-file preservation | compatible | preflight classifies exact old/current/foreign states and refuses before mutation |
| direct close contract × one public return command | compatible | Plan supplies discovery and stops; the conventions heading remains the sole effect owner |
| Plan ≤1,200 × complete moved-text accounting | compatible | the Plan cap and combined candidate sum are independent gates |

## Configuration Verdicts

| Config | Verdict | Decisive result |
|---|---|---|
| C1 | **Survives as mandatory fallback** | It preserves current safety if any C2 condition, amendment, migration, history, counter, or candidate test fails. It does not deliver the requested simplification. |
| C2 | **Sole retirement survivor, corrected** | It preserves one owner per behavior and passes the design models after adding `TARGET_CURRENT` as an idempotent migration class. |
| C3 | **Eliminated** | Existing receivers retain stale files under additive sync. |
| C4 | **Eliminated** | It duplicates exact selection/state policy and widens read/decision burden across roles. |
| C5 | **Eliminated** | It expands Plan into closing, repair, and acceptance work forbidden by its Role Lock. |
| C6 | **Eliminated** | It retains a replacement entry, overconstrains aggregate history, and relies on non-reproducible arithmetic. |
| C7 | **Eliminated** | A net-negative but still oversized changed Plan does not satisfy the explicit ≤1,200 design rule; the task must meet the cap or keep Resume. |

## Stress Tests

### C1: routing-only matrix and mutation boundary

An in-memory pure evaluator implemented the Extract E1 precedence and state table. Twenty-eight fixtures covered: new request, missing reference, collision, historical-only, malformed carrier, selected close, selected repair, `TODO`, `HL_DRAFT`, `RES`, unselected and selected `PHASES`, a terminal selected phase, prohibited nested `PHASES`, approved/unapproved `TS_DRAFT`, `ONB`, `RF`, incomplete/REVISE/REJECT/APPROVE `REV`, `KNW`, `BLOCKED`, `DONE`, `REJECTED`, `UNDECLARED`, and an unknown source value.

For each fixture the test serialized the complete input before and after evaluation and compared the exact route to the table. Result: `28 passed, 0 failed, 0 input mutations`. This is executable evidence that the proposed classification is total over the declared vocabulary and can be pure. It is not evidence that the repository's current Plan already implements it; Phase A must turn the same table into product tests over temporary repositories and prove path/byte identity before and after every routing-only case.

Attacks and outcomes:

- **Historical collision/order attack:** order never selects a winner; collision and historical-only both stop before Knowledge Gate or repair.
- **Phase rollup attack:** an unselected `PHASES` task can only render phase-local rows and wait; it cannot select “next,” create Phase HL/TS, or change status.
- **Approval shortcut attack:** `TS_DRAFT` routes to Handoff only with exact approval lineage; `REV`/APPROVE with an unadvanced carrier routes to record recovery, not directly to `DONE`.
- **Terminal/unknown attack:** `DONE` and `REJECTED` have no edge; `UNDECLARED` and unknown values stay verbatim and require the accountable owner.
- **Write-smuggling attack:** `NEW` and the two Plan-continuation results authorize only entry to the existing later gates; the pre-route evaluator itself remains read-only.

### C2: fresh close/recovery access and authority leakage

Nine source assertions checked that the close heading is unique; names the authorized Coordinator; says the contract is used directly; introduces no closing artifact, registry, or executable; separates record-only repair; and is the exact target named by Review after APPROVE/`KNW`. They also checked Plan's current no-code/artifact boundary. Result: `9 passed, 0 failed`.

The strongest countercase was a fresh interrupted close after Resume disappears. C2 still has a complete path:

1. the user invokes the sole general return entry with an exact task/phase;
2. Plan's pure pre-route observes `KNW` or the APPROVE/carrier mismatch;
3. Plan prints the fixed `Coordinator control` text and stops;
4. the next selected natural-language request reads the unique conventions heading directly.

This costs one explicit stop/selection in a fresh session, but it preserves authority and discoverability without another public entry. The normal route is shorter: Review already returns the exact accepted result to the existing Coordinator and names the heading. A root/adaptor shortcut that branches on lifecycle was rejected because it would be a hidden Resume. A root may carry only the generic command map; the behavior remains Plan plus the existing heading.

### C3: owned deletion, refusal, clean install, and repeat

The first migration-model run failed its second-run case: it recognized only old exact roots, so the already-updated singular managed block was incorrectly treated as foreign. That is a genuine idempotence defect in the first formulation. The corrected preflight adds:

| Observation | Corrected class | Effect |
|---|---|---|
| bytes/block equal the pinned target | `TARGET_CURRENT` | success/no-op; never delete or rewrite |

The corrected in-memory connected-group model then executed seven cases:

| Case | Result |
|---|---|
| all six stale source/receiver subjects old-exact; exact default config; owned singular block; foreign neighbor | pass: retired paths/key removed, target block installed, neighbor exact |
| Cursor old destination absent | pass: absence accepted, no stale file created |
| Claude receiver contains foreign bytes | pass: group refused and complete input map unchanged |
| singular compatibility root unmarked/foreign | pass: group refused and root unchanged |
| project config has customized Resume target | pass: group refused and config unchanged |
| candidate manifest command set | pass: ten unique commands, no `resume` |
| second run over the target-current result | pass: not refused, no changes, identical state |

Final result: `7 passed, 0 failed`. The design therefore needs four preflight outcomes, not three: `ABSENT`, `OWNED_EXACT`/`OWNED_BLOCK`, `TARGET_CURRENT`, and `FOREIGN_OR_DRIFTED`. Phase A assurance must exercise real temporary receiver trees and exact old/candidate blobs; this model proves the branching contract but does not substitute for receiver implementation.

### C4: split history oracle and deliberate mutants

The baseline selector was rerun from Git objects and reproduced `205 = 23 live + 179 task + 3 aggregate`. The sorted 179 task entries reproduced SHA-256 `ed52c4c26845e90c14a569f867ec2200b18da44374f7df2fd897bf7fb58bef96`. A one-byte manifest mutation changed the hash and was rejected.

For each aggregate baseline blob, a raw-line-subsequence checker executed four cases:

| Aggregate | identity | inserted new record | edited first baseline line | reordered first two baseline lines |
|---|---:|---:|---:|---:|
| `.tfw/CHANGELOG.md` | pass | pass | rejected | rejected |
| `KNOWLEDGE.md` | pass | pass | rejected | rejected |
| `knowledge/stakeholder.md` | pass | pass | rejected | rejected |

Phase A evidence must compare to that exact digest. The split oracle admits a truthful additive record while detecting deletion, edit, reordering, path loss, mode change, or task-trace mutation.

### C5: counter provenance, boundary mutants, and Plan cap

The strict UTF-8/Unicode `\S+` counter was run twice on the immutable blobs: Plan `2,021`, Resume `716`, total `2,737`; repeat results were identical. Searching every Git revision of each workflow produced zero Plan hits for `1,995` and zero Resume hits for `690`. This falsifies the proposition that the frozen 2,685 can be recovered from repository history under the repository's counter.

Boundary tests kept the two gates separate:

| Synthetic boundary | Result |
|---|---|
| Plan 1,200 + counted additions 1,536 = 2,736 | passes both gates |
| Plan 1,200 + counted additions 1,537 = 2,737 | fails strict net-subtraction gate |
| Plan 1,201 + zero additions | fails Plan cap despite a low combined total |
| two words moved onto candidate-side added line | contributes two, not zero |

These are arithmetic/oracle tests, not a candidate implementation measurement. They make H4 falsifiable at Phase A and prevent three false greens: using different counters, hiding text outside Plan, or treating Resume deletion as a waiver for an oversized Plan. The repository history's 1,195-word Plan shows the cap is not structurally impossible, but only candidate behavior tests can prove that the current contract survived the rewrite.

### C6: H1–H4 decision verdicts

| Hypothesis | Iteration-2 verdict | Decision meaning |
|---|---|---|
| H1 | **Literal form remains refuted; narrowed value claim confirmed for G1.** | Current Plan does not cover Resume. In C2, however, Resume owns no product transition or independent authority; one Plan router plus existing owners covers the user job without a second command. |
| H2 | **Confirmed architecturally and by the pure route/authority models.** | Every R1–R12 protection has one existing owner, complete state case and stop. Plan gains inspection/routing only; no Role Lock is widened. |
| H3 | **Confirmed as a complete implementable contract, not yet an implementation result.** | Owned/absent/current/foreign states, all-preflight refusal, four adapters, singular root, clean ten-command install, repeat idempotence, and the split history oracle are exact and mutant-tested. |
| H4 | **Confirmed as an exact acceptance contract conditional on the frozen amendment.** | `W`, baseline 2,737, moved-text sum, strict `C < B`, and Plan ≤1,200 are reproducible. The current 2,685 claim is not. Owner rejection of the correction or any candidate miss selects C1. |

## G1 Recommendation

Research is **SUFFICIENT** for the owner to decide G1. Approve C2 only together with the classified denominator/counter amendment and the following non-negotiable Phase A conditions:

1. implement the exact pure Plan matrix before deleting Resume;
2. preserve the direct non-command Coordinator route and Plan stop;
3. add the version-addressed four-class migration with all-preflight refusal and ten-command convergence;
4. pass the fixed 179-task and 3-aggregate oracles;
5. produce an immutable Candidate with Plan ≤1,200 and complete counted surface `< 2,737`.

Failure of any condition, inability to classify moved instructions, or rejection of the amendment means **keep Resume (C1)**. No iteration 3 is needed to make this architectural choice; implementation and candidate evidence belong after approved TS.

## Checkpoint

| Found | Remaining |
|---|---|
| C2 is the only retirement configuration compatible with Role Locks, update semantics, history, and the design cap. | Owner G1 verdict and amendment verdict; then Coordinator TS if approved. |
| 28/28 route, 9/9 authority, 7/7 corrected migration, and all history/counter mutant cases passed. | Real Phase A implementation/candidate tests; these are not Researcher work. |
| One idempotence defect was found and corrected with `TARGET_CURRENT`. | The TS must retain this fourth class explicitly. |
| H1 is honestly narrowed; H2–H4 are decision-ready, with H3/H4 distinguished from implementation completion. | None requiring another research iteration. |

**Sufficiency:**
- [x] External source used? Canonical sources, immutable Git objects/history, current test implementation, and executable in-memory models.
- [x] Briefing gap closed? All five iteration-2 gaps have exact contracts, positive/negative cases, fallback, and owner-decision implications.
- [x] Pairwise incompatibility checked? Eleven pairs were checked; C2 survives for retirement and C1 survives only as fallback.

Stage complete: YES
→ User decision: owner G1 verdict after RES synthesis; do not start TS here.
