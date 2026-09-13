# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260913-151442_RWNR](../../HL-TFW_20260913-151442_RWNR.md)
> Goal: Determine whether `/tfw-resume` is a necessary public command and retire it only after every continuity guarantee has a proven surviving route.

## Consistency Check

### Incompatible pairs

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1: Returning-user entry topology | `/tfw-plan <task>` is the sole general entry | D2: Multi-phase choice owner | Resume workflow | A removed command cannot remain the sole owner of phase choice. |
| D1: Returning-user entry topology | `/tfw-plan <task>` is the sole general entry | D4: Closing/recovery entry | Plan performs closing/control writes | This widens Plan's frozen Role Lock and triggers HL DoF 4. Plan may only name the existing Coordinator route and stop. |
| D1: Returning-user entry topology | Retire Resume | D5: Retirement propagation | Canonical deletion only | Live configs, adapter sources/receivers, roots, docs, and update targets would disagree and recreate the command. |
| D1: Returning-user entry topology | Retire Resume | D5: Retirement propagation | Permanent tombstone or renamed wrapper | A live redirect is a replacement public resume surface, violating DoD 10/11 and DoF 5. |
| D3: Historical-only safety owner | Plan-local or shared guard | D6: Assurance level | Source-string assertions only | A string cannot prove the no-mutation outcome; a before/after state oracle is required. |
| D4: Closing/recovery entry | Root adapter owns the algorithm | D5: Retirement propagation | Thin adapter regeneration | Behavior-bearing adapter prose becomes a second authority and contradicts D15 plus `Command entry and evidence boundary`. |
| D5: Retirement propagation | Remove manifest row only | D6: Assurance level | Existing additive sync | The current sync writes declared commands but never removes absent ones; stale receivers survive. |
| D5: Retirement propagation | Scrub every textual match | D6: Assurance level | Historical byte preservation | Hundreds of matches are historical/evidence truth; global replacement destroys the record. |
| D7: Retained-surface denominator | Frozen 2,685 count | D7: Retained-surface denominator | Candidate-only generic whitespace count | Different counters make the inequality meaningless; baseline and candidate require one algorithm. |
| D2: Multi-phase choice owner | User preselects phase silently/default order | D6: Assurance level | Negative no-mutation scenarios | Silent/default selection directly contradicts the required WAIT and observable no-mutation guarantee. |

### Surviving configurations

| Config | D1 | D2 | D3 | D4 | Notes |
|--------|----|----|----|----|-------|
| C1 | Keep Resume | Resume | Resume-local | Resume exposes shared close/recovery | Behaviorally coherent, but contract-ineligible because the frozen target requires an evidence-backed retirement decision and one obvious entry. It remains the safe fallback if C2 cannot be proven. |
| C2 | Plan is sole general continuation entry | Compact Plan continuation gate | Plan consumes existing Discovery/state rules | Existing authorized Coordinator uses shared close/recovery | The only extracted configuration that satisfies the intended final surface without a new generic helper; survives architecturally but lacks implementation/scenario evidence. |
| C5 | Plan for general return plus root recognition only for an explicit selected close/repair | Compact Plan continuation gate | Plan consumes existing Discovery | Root is a thin pointer to shared close/recovery | Conditional unexpected survivor for discoverability only. It fails if the root contains branching semantics or becomes a second general continuation entry. |

### Eliminated configurations

- **C3 — new generic continuation contract:** eliminated unless reduced to narrow existing headings; a full new contract would be `resume.md` under another name and violate the no-hidden-helper rule.
- **C4 — direct lifecycle commands only:** behavior can be preserved, but the returning user must diagnose lifecycle before choosing a command, contradicting the frozen one-obvious-entry result.
- **C6 — permanent or final tombstone:** eliminated as the final state because a live `/tfw-resume` redirect is still a public replacement surface. A temporary migration notice can exist only outside the final live command set and must disappear before acceptance.

### Unexpected survivor

- **C5, narrowly construed:** a persistent adapter root may point an already explicit close/repair request to the existing shared Coordinator heading without owning any logic. This survives D15 only as a thin pointer and is not required by C2. Iteration 2 should decide whether the pointer adds real recoverability or merely recreates a second entry form.

## Findings

### C1: Immediate deletion is falsified by the current Plan source

A direct source check found that current `plan.md` contains none of `historical_containers`, `Historical read:`, `Build the Matrix`, `Which phase should we work on?`, `Closing and record recovery`, `PHASES`, `BLOCKED`, `REJECTED`, or `UNDECLARED`. Its Role Lock also does not permit status/journal writes. Current `resume.md` contains the historical stop, matrix, phase-choice question, and close/recovery route.

Therefore the strongest naïve claim — “Resume is redundant now, so delete it first” — is false. Phase A must establish and test C2's survivor routes before Phase B removes the command. This refutes H1's literal phrase “already covered” as an implementation statement while leaving its user-job/no-independent-public-value claim viable.

### C2: Adversarial lifecycle matrix

| Scenario | Attack | Evidence in the current repository | C2 result |
|---|---|---|---|
| Multi-phase, no phase selected | Plan might assume declaration order, use task `PHASES` as a rollup, or mutate one phase | `resume.md` requires every phase's local state, a matrix, an explicit question, and stop; runtime semantic model asserts `S1-resume.gate == WAIT`; Plan lacks this branch today | **Conditional survivor.** Add the gate to Plan and require phase/status/journal before/after hashes plus a malformed-phase refusal. |
| Multi-phase, one exact phase selected | Generic task routing might still summarize or choose another phase | `A phase carries its own state` forbids task rollup; exact selected phase has its own status/journal | **Survives by authority.** Test that only the selected phase is routed and no state changes before its destination workflow acts. |
| Historical-only exact task | Plan might create modern status, choose a phase, close, repair, or normalize the trace | Current Resume explicitly stops read-only before all those acts; `test_slc_history_gate_and_resume_guards_precede_current_work` checks ordering, not actual unchanged bytes | **Evidence blocked.** C2 is valid only with an executable historical fixture and whole-tree before/after oracle. |
| Whole-ID collision across active/historical union | Container order might silently select one | `Discovery` and Resume refuse whole-ID collision | **Survives by authority.** Plan must consume the same union and refusal; negative scenario required. |
| `UNDECLARED` | Router might normalize to a known state | `Task Statuses` allows only accountable-owner resolution and forbids tooling normalization | **Survives by authority.** Plan route table must stop and name the owner; no guessed command. |
| Malformed or interrupted current carrier | Router might treat intent as execution or reconstruct a past timestamp | `Closing and record recovery` permits record-only repair only when result/oracle/authority/dependencies are reconstructably unchanged and preserves old event bytes | **Conditional survivor.** Needs positive repair and uncertain-lineage refusal fixtures; Plan must only name this route. |
| `BLOCKED` | Router might jump directly back to ONB or planning | Shared contract requires the cited dependency/ruler and return to the rung table's required state; direct KNW→ONB is forbidden | **Survives by authority.** Scenario must cover resolved and unresolved bounds. |
| `DONE` | General continuation might reopen work | `DONE` is terminal accepted state | **Survives.** Plan reports terminal state and performs no mutation. |
| `REJECTED` | General continuation might treat it as BLOCKED | `REJECTED` is terminal with no outgoing edge | **Survives.** Plan reports terminal and stops; only an accountable owner may address a contradictory carrier. |
| `TS_DRAFT` | Status alone cannot reveal whether execution is approved | TS template begins Awaiting approval; real TS headers record explicit APPROVED and handoff reads the highest approved TS lineage | **Conditional survivor.** Plan must inspect the exact TS approval lineage; it may not route every `TS_DRAFT` blindly to Handoff. |
| `ONB` | A fresh Executor or Coordinator might take over | Handoff requires same returned Executor under AT and its own authority/lineage | **Survives if route names the same Executor.** Plan does not execute. |
| `RF` or active `REV` | Plan might approve, repair, or choose a new reviewer | Review owns independent judgment; Plan only receives returned proposals for Step 8 | **Survives.** Route to the independent Reviewer or rule an already returned REVISE; distinguish in-progress from returned lineage. |
| REVISE rung 1/2/3 or mixed | A simplified router might collapse every return into one TS revision | Existing Plan Step 8 and the shared rung table already distinguish all cases and stops | **Survives strongly.** No Resume-specific behavior is needed; regression tests already detect universal-route contradictions. |
| `KNW` close | Plan might write DONE immediately after APPROVE | Review Step 7 returns to existing Coordinator; shared close requires capture/final-effect checks and independent judgment of changed claims | **Survives only with role separation.** Plan names the shared route and stops; adding close writes to Plan falsifies C2. |

### C3: Closing and record recovery are not safely absorbed by Plan

The countercase for keeping Resume is strongest at interrupted closing and carrier recovery, because Resume is the only current public command that explicitly exposes that shared contract. However the behavior's authority is already outside Resume: `conventions.md` says the existing authorized Coordinator owns it, and `review.md` Step 7 returns APPROVE directly there. Resume is a discoverability/caller layer, not the canonical owner.

C2 survives only under three constraints:

1. Plan's permitted artifacts remain unchanged; it cannot write closing status/events or separately attributed REVIEW follow-ups.
2. A Plan continuation result for `KNW` or a reconstructable carrier names `Closing and record recovery` and stops, preserving the existing Coordinator and independent Reviewer.
3. Iteration 2 proves how an interrupted, newly opened session reaches that exact route without a new slash command, alias, generic hidden workflow, or behavior-bearing adapter. If it cannot, C1 (keep Resume) wins on recoverability.

### C4: Role Locks and lifecycle-specific routes survive only as routing, not role fusion

The responsibility map passed the role-boundary attack because C2 gives Plan inspection and routing only:

- `RES` still returns to `/tfw-research`, whose filesystem stage state resumes independently of Resume.
- approved `TS_DRAFT` and `ONB` route to `/tfw-handoff`; Plan never writes ONB/RF or implementation.
- `RF`/active `REV` route to the independent `/tfw-review`; Plan cannot create REVIEW proposals or accept its own material work.
- REVISE returns to existing Plan Step 8 for a Coordinator ruling, then to the same Executor/Reviewer under the rung table.
- `KNW` uses the shared close/recovery Coordinator contract, not Plan's artifact permission set.

Any proposal that adds selected closing/control records to Plan's Role Lock, embeds Research/Handoff/Review work in Plan, or creates a new “continuation” workflow is a falsification, not a refinement.

### C5: Adapter parity and clean install are tractable; existing update is not yet proved

Forty-six focused current-state tests passed in 4.14 seconds. They cover current secondary route/source contracts, omission/address/preload mutants, lifecycle semantics, stale/competing authority detection, exact receiver parity, clean four-adapter installation, idempotent sync, REVISE routing, and Plan/Resume navigation behavior. These results prove the present command's R0/R1 and modeled semantics; they do not prove its safe removal.

The clean-install attack is answerable: the installation helper iterates manifest commands, so a coherent ten-command manifest plus updated expected-set tests can produce no Resume receiver for Codex, Claude, Cursor, or Antigravity. Root managed blocks and current docs must also lose the route.

The existing-update attack falsifies manifest-only deletion. `_sync_from_manifest` copies each declared command and does not enumerate/delete commands absent from the manifest. `update.md` overlays `.tfw/` and demands an exact command set, so stale canonical and receiver files would remain and cause disagreement. H3 stays blocked until a version-addressed migration proves all of:

- exact owned stale path list for canonical/config/adapter sources and every selected receiver;
- byte/path/managed-ownership checks before deletion;
- foreign/unmarked collision refusal;
- root-block regeneration with outside text preserved;
- absent Cursor receiver treated as success, not created for cleanup;
- the tracked singular `.agent/rules/agents.md` compatibility surface explicitly updated or preserved according to its ownership;
- second update produces no recreation and no diff.

### C6: No-replacement and historical-truth attacks

C2 introduces no new public command, alias, wrapper, tombstone, or generic helper. C3 and permanent C6 were eliminated precisely because they recreate Resume under another name. C5 remains conditional only as a thin pointer for a selected close/repair; if it accepts general continuation or owns branching, it is a forbidden replacement.

At immutable baseline `a2363fd`, the broad history selector identified 182 protected pre-existing paths: 55 under `tasks/`, 124 under historical/current `workspace/` tasks other than RWNR, and 3 durable aggregate files (`.tfw/CHANGELOG.md`, `KNOWLEDGE.md`, `knowledge/stakeholder.md`). The sorted baseline tree-entry manifest has SHA-256 `9248a1855d64dfbff15840c1cfb4a2fcf12ca07f3fa14c165861d283cdc089b5`.

The attack reveals that one hash policy cannot govern all 182 paths. The 179 task-trace files can require whole-file byte identity. The three aggregate history/knowledge files may legitimately receive new append-only/current decision material, so their pre-existing statements need range/blob preservation rather than whole-file equality. H3 remains blocked until iteration 2 freezes the exact selector and split oracle. Global text replacement, renaming old artifacts, or deleting historical command names is disallowed.

### C7: Instruction-surface accounting remains blocked

The frozen contract says 2,685 words (Plan 1,995 + Resume 690), while a generic whitespace count over the same byte-identical files says 2,737 (2,021 + 716). This attack prevents a false green H4 result: subtracting 690 under one counter and adding candidate text under another is invalid.

C2 is structurally capable of net subtraction because it needs a compact pre-routing table and references existing `Discovery`, phase-state, REVISE, Role Lock, and close/recovery contracts instead of copying 83 Resume lines. Capability is not proof. Iteration 2 must:

1. recover the original counter or explicitly rebase both `a2363fd` baseline files and candidate under one named counter while retaining 2,685 as the historical owner-approved denominator;
2. count every added canonical word wherever it moves, including conventions or root routing text;
3. prove retained total is below the comparable baseline;
4. give Plan's existing >1,200-word file an architectural disposition rather than treating net subtraction as a waiver.

H4 stays blocked.

### C8: Adversarial hypothesis verdicts

| Hypothesis | Falsification attempt | Iteration-1 verdict |
|---|---|---|
| H1 | Delete Resume today and rely on current Plan | **Partly refuted.** Current Plan lacks the unique selection/safety gates, so “already covered” is false as implementation. The narrower claim that Resume has no independent public-user value survives if C2 is implemented first. |
| H2 | Force each unique protection into an existing owner without Role Lock expansion or a renamed helper | **Survives architecturally, not empirically.** R1–R12 each have one owner/route under C2; interrupted close/recovery discoverability and executable no-mutation proof remain decisive. |
| H3 | Remove the manifest row and expect every clean/existing receiver to converge while history stays untouched | **Blocked and the naïve mechanism is refuted.** Clean install is tractable; additive update leaves stale files; the split history oracle is unfinished. |
| H4 | Claim that deleting Resume automatically beats 2,685 and fixes Plan size | **Blocked and the automatic claim is refuted.** The counter is unreproduced, moved text must be counted, and oversized Plan still needs a disposition. |

## Required Focus for Iteration 2

1. Specify the minimal Plan continuation gate and execute a state-fixture matrix covering exact selection, multi-phase wait/no mutation, historical-only no mutation, malformed/UNDECLARED, BLOCKED, terminal, approved/unapproved TS, RF/REV, REVISE, and KNW routing without Plan writes.
2. Resolve interrupted close/record-recovery discoverability with one exact non-command canonical route and prove the existing Coordinator/Reviewer authority chain; reject any alias, wrapper, generic hidden workflow, or behavior-bearing adapter.
3. Design and test the version-addressed removal migration for all owned stale sources/receivers, including absent Cursor, foreign/unmarked refusal, singular compatibility root, second-run idempotence, and clean ten-command installation.
4. Freeze the split historical oracle: whole-file bytes for 179 task traces and pre-existing-statement preservation for the 3 aggregate files.
5. Recover or redefine one word-count algorithm across immutable baseline and candidate, include moved canonical text, and state the architectural disposition for Plan's >1,200-word limit.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Immediate deletion and manifest-only removal are falsified. | Prove C2's actual Plan gate and migration before any retirement decision. |
| C2 preserves all Role Locks in architecture and gives R1–R12 one owner/route. | Resolve fresh-session access to selected close/recovery without a new public or hidden command. |
| Current assurance is green: 46 focused tests passed. | Replace Resume-presence tests with executable post-retirement behavior/absence/no-mutation tests at R2–R4. |
| A baseline history selector and aggregate tree-entry digest exist for 182 paths. | Split 179 whole-file immutable traces from 3 append-capable aggregate files and freeze the exact oracle. |
| H1 is narrowed; H2 survives conditionally. | H3 and H4 remain blocked on migration, history, counter, and Plan-size evidence. |

**Sufficiency:**
- [x] External source used? Current canonical sources, immutable Git history/tree entries at `a2363fd`, adapter sync implementation in maintainer tests, and 46 executed focused checks.
- [x] Briefing gap closed? Every mandated adversarial scenario and the full lifecycle matrix was attacked; falsifications and surviving conditions are explicit.
- [x] Pairwise incompatibility checked? Ten incompatible pairs, three survivors, three eliminations, and one unexpected conditional survivor are recorded.

Stage complete: YES
→ User decision: Iteration 1 is not sufficient for G1. Accept this Challenge and synthesize a RES recommending mandatory focused iteration 2 on the five evidence gaps above.
