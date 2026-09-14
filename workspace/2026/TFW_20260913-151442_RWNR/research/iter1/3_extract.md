# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260913-151442_RWNR](../../HL-TFW_20260913-151442_RWNR.md)
> Goal: Determine whether `/tfw-resume` is a necessary public command and retire it only after every continuity guarantee has a proven surviving route.

## Configuration Space

Only coherent final-state combinations are listed. “Shared” means an existing addressed conventions heading, not a public command or a second workflow. The tombstone option is included only as a migration shape; it is not a compliant final state.

| Config | D1: Returning-user entry topology | D2: Multi-phase choice owner | D3: Historical-only safety owner | D4: Closing and record-recovery entry | D5: Retirement propagation | D6: Assurance level | D7: Retained-surface denominator |
|--------|-----------------------------------|------------------------------------|-----------------------------------------|-------------------------------------------|----------------------------|---------------------|----------------------------------|
| C1 | Keep `/tfw-resume` | Resume | Resume-local | Resume → shared close/recovery | Keep current 11-command install/update | Current source/parity suite | Frozen 2,685 claim |
| C2 | `/tfw-plan <task>` is the sole general continuation entry | Compact Plan continuation gate | Plan consumes existing Discovery and phase-state rules | Existing Coordinator uses shared `Closing and record recovery`; Plan only names it and stops | Remove live command surfaces plus versioned ownership-checked stale-file migration | Executable fixtures + absence/parity + native command-entry evidence | One explicit counter over baseline and candidate |
| C3 | `/tfw-plan <task>` is the sole general continuation entry | New shared generic continuation contract consumed by Plan | Same new generic contract | Same new generic contract dispatches to shared close/recovery | Manifest/config removal plus migration | Executable fixtures + absence/parity | One explicit counter over baseline and candidate |
| C4 | Direct lifecycle-specific commands; Plan only for planning/revision | User names the phase before entry | Repeated lifecycle-local guards | Review return or direct Coordinator close/recovery | Remove live command surfaces plus migration | Per-command executable fixtures | One explicit counter over changed workflows |
| C5 | `/tfw-plan <task>` for general return, plus always-on root recognition of an explicit close/repair request | Compact Plan continuation gate | Plan consumes existing Discovery | Root adapter points to the shared close/recovery heading | Root blocks regenerated; owned stale commands removed by migration | Root-routing and lifecycle fixtures | One explicit counter including added root text |
| C6 | Temporary resume tombstone redirects to Plan, then disappears | Plan continuation gate | Plan consumes existing Discovery | Shared close/recovery | Two-release removal with temporary tombstone | Transitional and final absence suites | Both release candidates measured |

C5 is the combination not proposed in the Briefing: a direct natural-language control request is recognized by the always-on adapter root while all semantics remain in the shared conventions contract. It avoids a new public command but adds a second entry form and four adapter surfaces, so Challenge must decide whether it is useful routing or substitute ceremony.

## Findings

### E1: One-owner survivor map for all 12 responsibilities

The extracted candidate map uses C2. “Owner” names the single canonical decision owner; shared rules are inputs, not additional owners. Plan may inspect and route, but it does not perform Executor, Reviewer, closing, or recovery writes.

| ID | Single canonical owner / role | Surviving canonical source | One surviving route | Required delta from current state |
|---|---|---|---|---|
| R1 exact task resolution | Plan / Coordinator | Plan Read Contract consuming config plus `conventions.md` → `Discovery` | `/tfw-plan <exact-task-id>` resolves the deduplicated active-plus-historical union; collision refuses | Add `historical_containers` and the exact-reference membership gate to Plan; do not add a new workflow |
| R2 historical-only protection | Plan / Coordinator, read-only | Plan existing-task continuation gate consuming `Discovery` | `/tfw-plan <historical-only-id>` reports historical access and stops before planning, phase choice, close, recovery, or writes | Copy only the stop invariant, not Resume's algorithm; test before/after tree bytes |
| R3 current state and lineage | Plan / Coordinator | Plan Read Contract plus task/phase `status.md` and journal | `/tfw-plan <task>` verifies the authoritative state and highest cited lineage before any route | Tighten the existing known-task preflight; indexes/globs remain non-authoritative |
| R4 multi-phase state inspection | Plan / Coordinator | Plan continuation gate consuming `A phase carries its own state` | Task `PHASES` with no selected phase reads every live phase state/journal and refuses malformed input | Add the compact inspection branch before planning work |
| R5 returned REVIEW preservation | Plan / Coordinator | Plan continuation gate consuming highest live REVIEW and `The 🔄 REVISE route` | The same `/tfw-plan <task>` view reports verdict/dispositions; REVISE continues through existing Plan Step 8 | Add read/preserve behavior only; no backlog reconstruction |
| R6 session identity | Plan / Coordinator | Existing `conventions.md` → `Session identity` | The resolved Plan unit applies `PLAN`/qualified LEAD title before matrix, question, or stop | Replace Resume-only consumer assertions; do not change the central identity predicate except to remove `RESUME` after the command disappears |
| R7 selected close and record recovery | `Closing and record recovery` / existing authorized Coordinator | Existing `conventions.md` heading plus `Task control files` and `Which handle a machine acts as` | Reviewer APPROVE returns directly to this route; a returning Plan invocation names this exact route and stops | Remove “`/tfw-resume` also exposes it”; add scenario entry that proves Plan does not write closing/control artifacts |
| R8 phase status matrix | Plan / Coordinator | Compact Plan continuation gate; row shape remains source-owned there | `/tfw-plan <multi-phase-task>` presents phase, description, authority, lifecycle, REVIEW verdict, exact route | Move the observable table contract, not all Resume prose |
| R9 human phase decision | Plan / Coordinator | Same compact Plan gate | After matrix: ask which phase to plan and stop; no order/default/automatic phase | Add one explicit WAIT and negative auto-selection test |
| R10 lifecycle route selection | Plan / Coordinator as router only | Compact Plan route table consuming `Task Statuses` | `TODO/HL_DRAFT/TS_DRAFT → plan`; `RES → /tfw-research`; `PHASES → phase gate`; `ONB → /tfw-handoff`; `RF/REV → /tfw-review`; `KNW → Closing and record recovery`; `DONE/REJECTED → terminal report`; `BLOCKED/UNDECLARED/malformed → named authority/gap and stop` | Add a state-to-route table before the Knowledge Gate; require approved-TS lineage to distinguish TS approval from draft |
| R11 acting attribution before control writes | existing authorized Coordinator | Existing `conventions.md` → `Which handle a machine acts as` | Only the direct close/recovery route resolves writer before a durable control write; Plan's routing-only path writes nothing | Ensure the direct route's read contract includes the identity heading; no adapter, Git, OS, or title inference |
| R12 Role Lock boundary | Plan / Coordinator for continuation decision | Existing `conventions.md` §15 plus each destination workflow's own lock | Plan inspects/routes only; Researcher, Executor, Reviewer, and closing Coordinator retain their current artifacts and stops | Remove the Resume row after all destination tests exist; do not add closing/control records to Plan's permitted artifacts |

This map assigns every responsibility once without a public replacement command. It also exposes the hard architectural seam: R7 cannot be “moved into Plan” because that would widen Plan's permitted artifacts. Plan can name the existing Coordinator control route; the route itself remains `Closing and record recovery` and is already the destination of Review Step 7.

### E2: Lifecycle route and transition matrix

| Observed state/condition | Read-only continuation decision | Sole next owner/route | Permitted state effect |
|---|---|---|---|
| `TODO` or `HL_DRAFT` | Planning is incomplete | Plan / Coordinator | Plan may create/revise HL within the frozen-contract rules |
| `RES` | Research state and `iterations.yaml` decide first missing stage/iteration | `/tfw-research` / Researcher | Research writes only stage files and RES; Coordinator later records iteration completion |
| `PHASES`, no phase selected | Read every declared live phase; show matrix; wait | Plan / Coordinator | No mutation before explicit phase choice |
| `PHASES`, one phase selected | Apply that phase's own state row below | Owner determined by phase state | Task-level `PHASES` is not rolled up or rewritten |
| `TS_DRAFT`, not approved | Approval/revision remains open | Plan / Coordinator | TS may be revised/approved; no execution write |
| `TS_DRAFT`, exact approved TS/value lineage present | Planning is complete | `/tfw-handoff` / same Executor | Executor acceptance moves `TS_DRAFT → ONB` with status then event |
| `ONB` | Execution or accepted REVISE return is active | `/tfw-handoff` / same Executor | Executor completes to `RF`; Coordinator never executes |
| `RF` | Result awaits independent judgment | `/tfw-review` / independent Reviewer | Review starts `REV`; APPROVE later enters `KNW`; REVISE alone does not move lifecycle |
| `REV` | Review is in progress or returned | `/tfw-review` if same review continues; returned proposals go to Plan Step 8 | Rung 1 acceptance later permits `RF → ONB`; any rung 2 uses `TS_DRAFT → ONB`; rung 3 stays unchanged until verdict |
| `KNW` | Capture/final effects and accepted-result checks remain | `Closing and record recovery` / existing authorized Coordinator | Only after checked effects: `KNW → DONE`; material failure may record `BLOCKED` |
| `BLOCKED` | Read the cited dependency and ruler; never guess | Named existing authority from the blocking record | Return only to the rung/state required by the resolved bound |
| `DONE` | Terminal accepted state | none; report | No mutation |
| `REJECTED` | Terminal unsuccessful state | none; only accountable owner may address contradiction | No outgoing lifecycle edge |
| `UNDECLARED`, malformed carrier, or interrupted status/event pair | Distinguish owner resolution from reconstructable record-only repair | owner for `UNDECLARED`; authorized Coordinator for exact record repair | Preserve past event bytes; append only the truthful present recovery act; uncertain lineage stops |
| historical-only path | Historical state is context, not live work | none from this invocation | Zero mutation; later continuation requires separate authority |

The matrix shows that Resume itself does not own a unique product transition. Its unique value is pre-route inspection and stopping behavior. Every write already belongs to Plan, Research, Handoff, Review, or the shared Coordinator close/recovery contract.

### E3: Configuration comparisons and contradictions

| Config | What it preserves | Structural cost or contradiction to challenge |
|---|---|---|
| C1 keep Resume | All current behavior with no migration risk | Fails the frozen one-entry target and owner-observed redundancy; keeps duplicate choice and 11-command surface |
| C2 Plan gate + existing shared rules | One public continuation entry, current Role Locks, no new command, small semantic move | Plan grows locally while already over 1,200 words; explicit close/recovery follow-up must remain usable without Plan performing it |
| C3 new shared generic contract | Keeps Plan short and centralizes protection | Risks recreating `resume.md` as a hidden helper under another name, prohibited if it becomes the same long-lived coordination layer |
| C4 direct lifecycle commands | Minimal routing logic and strongest Role Lock separation | Fails the one-obvious-entry experience because the returning user must diagnose state before choosing a command |
| C5 root natural-language close recognition | Gives interrupted closing/recovery a discoverable non-command entry | Four adapters gain behavior-bearing routing text unless the root is only a thin pointer; could reintroduce drift |
| C6 tombstone migration | Gives users an explicit deprecation path | Final live tombstone still occupies a public command slot and delays the requested subtraction; only defensible as temporary migration evidence |

No configuration may count a new generic workflow, alias, wrapper, or tombstone as “retirement.” A shared heading is acceptable only when it owns one narrow invariant already natural to conventions; a hidden near-copy of Resume is not.

### E4: Distribution and migration contract extracted from C2

Clean installation and existing update need separate acceptance paths:

1. **Clean source:** remove the canonical Resume workflow, Codex skill source, manifest row, config template row, and command-list/root-template mentions; update current docs and tests.
2. **Clean receiver:** install the manifest-declared command set into all four adapter layouts and assert no `tfw-resume` target is created. Absence must include the unselected Cursor target even when Cursor is not installed locally.
3. **Existing receiver:** a version-addressed migration enumerates each framework-owned stale source and adapter target. Delete only when ownership is established by exact path plus expected source/copy or recorded managed ownership; foreign/unmarked collisions are reported, not removed.
4. **Overlay limitation:** ordinary manifest sync is additive/repairing and does not delete commands absent from the new manifest. A second update must prove no stale file is recreated and no diff remains.
5. **Root blocks:** regenerate the new command tables through exact-copy or marker-bounded sync; preserve all text outside managed blocks. The tracked singular `.agent/rules/agents.md` requires an explicit compatibility disposition because it is live but outside the current plural manifest topology.
6. **History:** hash the 3 durable history/knowledge paths and 179 historical task-trace paths before implementation and require identical bytes afterward. New migration/changelog statements may describe retirement; old statements are not rewritten.

The stale managed-file deletion gap remains unresolved evidence, not an assumed implementation detail. Iteration 2 must determine the exact owned path list, migration version boundary, and foreign-file refusal behavior.

### E5: Baseline accounting constraint

The frozen comparison remains 2,685 words, but the original counting function is still unknown. C2 can only satisfy H4 if one reproducible counter is applied to the immutable baseline commit and candidate, including every new canonical continuation instruction rather than hiding words in conventions or adapters. The current physical byte/line values anchor the baseline files, while the generic whitespace result of 2,737 is a diagnostic discrepancy. Plan's >1,200-word condition needs an explicit architectural disposition even if total retained instructions shrink.

Possible accounting treatments to challenge are:

- recover the original 1,995/690 counter and freeze it as the acceptance oracle;
- explicitly rebase both immutable baseline and candidate under a newly defined lexical counter while retaining 2,685 as the owner-approved historical denominator;
- use paired word, byte, and semantic-route counts, with the word comparison still decisive under one named algorithm.

Changing only the candidate counter, excluding moved shared text, or declaring subtraction from deleted bytes without counting additions would not test H4.

### E6: Provisional hypothesis impacts

| Hypothesis | Extract impact | Current disposition before Challenge |
|---|---|---|
| H1 | No canonical workflow calls Resume, and all product transitions already belong elsewhere. However Plan does not currently implement historical-only and phase-choice gates, so “already covered” is true at user-job/owner level but false as a literal current implementation claim. | Plausible after a bounded Plan routing delta; not confirmed |
| H2 | C2 assigns one owner and route to all 12 responsibilities without granting Plan closing, execution, review, or research writes. R7 is preserved only by keeping the existing shared Coordinator route separate from Plan. | Strong candidate; must survive adversarial scenarios |
| H3 | The 23 live paths are classifiable and clean install can omit Resume, but additive update sync leaves stale absent-manifest files. Historical preservation has a candidate hash boundary, not yet a frozen oracle. | Unresolved; migration gap blocks confirmation |
| H4 | Removing 690 contract words creates headroom for a compact route gate, but the baseline counter is unreproducible and Plan is already over its design limit. | Unresolved; measurement and architecture gap block confirmation |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C2 provides exactly one owner and one canonical route for R1–R12 without a replacement public command. | Challenge the map with concrete multi-phase, history, recovery, wrong-role, install/update, and no-alias counterexamples. |
| The complete lifecycle/state route matrix distinguishes read-only routing from authorized transitions. | Verify approved-TS detection and interrupted `REV`/`BLOCKED` cases cannot be guessed from status alone. |
| Clean install can follow the reduced manifest; existing update cannot rely on additive sync. | Specify and test the versioned ownership-checked deletion list, including singular legacy root treatment. |
| Historical preservation has a bounded 182-path census. | Produce an immutable pre-change hash oracle and decide whether current knowledge files are protected bytes or append-only decision surfaces. |
| The 2,685 baseline is carried unchanged. | Recover/define its counter and count all moved canonical text; give oversized Plan an architectural disposition. |

**Sufficiency:**
- [x] External source used? Current canonical status/transition contracts, adapter root templates, and Git history of Resume's historical/access/recovery changes were inspected.
- [x] Briefing gap closed? Every gathered responsibility now has one candidate canonical owner, role, and route.
- [x] Configuration Space built from Gather dimensions? Six coherent configurations cover all seven dimensions and include a previously unproposed root-recognition combination.

Stage complete: YES
→ User decision: No user input is required for iteration 1; proceed to Challenge C2 against the required adversarial scenarios while keeping H3/H4 evidence constraints open.
