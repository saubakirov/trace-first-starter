# Challenge — What breaks the apparently simple topology?

> Mindset: Critic. Distinguish a coherent design from a demonstrated native cycle.
> Parent: [approved HL](../../HL-TFW_20261027-161333_CMODES.md).
> Goal: One Coordinator can govern dependent phase scopes with independent roles and no ambiguous native edge.
> Producer/recipient: `/root/cmodes_research` → `/root`; own source `01a17db6-0f53-7603-878a-adaa590010e4`.
> Authority: HL freeze `28af8624b5a42f5078e6303ca844dabd1fbbcab6`; baseline/native-gates/tfw-gates-only, original dispatch/source binding in Briefing. Originating proposer: none.
> Epoch: product `c852d40c63b9c1d601d55fcd0552d03a47e157b0`, accepted Extract `b64c24171b8488cd207901eace3058929b53ef37`; 2026-10-27. Focused, one pass.

## Consistency Check

| Dimension A / alternative | Dimension B / alternative or retained constraint | Result |
|---|---|---|
| D1-A, actual human upward | D2-A or B | Compatible only when root holder and owner match and workers still use `coordinator_route`; phase completion is a local record, not an owner notification. |
| D1-B, local task relation | D2-A or B | Compatible only with a defined non-send route variant and exact task/holder checks; no adapter may treat the task ID as a native address. |
| D1-C, equal-address parent | D2-A or B | Compatible only after separating parent-scope aggregation from actual unit messaging; simply removing the equality prohibition is incompatible with no-self-send. |
| Any D1 | D2-C, inferred mode | Incompatible with explicit pre-launch selection and manual/visible distinction; already excluded in Extract. |
| Any D1/D2 | D3-B replacement without a real grant or with the old native identity | Incompatible with bounded authority and attributable correction lineage. |
| Any D1/D2 | D3-A resume without current path/base/selection verification | Incompatible with fixed Candidate and safe continuation. |
| Any D1/D2 | A continued Executor presented as independent Reviewer | Incompatible with frozen DoD 3 and role independence. |

No supported pairwise argument proves C1–C6 inherently impossible after coherent contract changes. The following are conditional survivors, ranked by the amount and kind of new meaning they require; this is a Research recommendation, not an architecture verdict.

| Config | D1 | D2 | D3 | Disposition |
|---|---|---|---|---|
| C2 | Actual human upward for same-holder phase | Explicit current mode | Ordered validated recovery | Preferred: native routes continue to mean actual recipients, and current mode is inspectable before dispatch. |
| C1 | Actual human upward | Source-only mode | Same | Viable fallback if the Coordinator rejects the additional field and accepts that mode resolution remains source inspection rather than a machine-visible current branch. |
| C3/C4 | Local task relation | Source-only / explicit mode | Same | Coherent but requires a new non-transport route variant whose sole effect is derivable from exact root-holder equality. No demonstrated extra value over C1/C2 here. |
| C5/C6 | Equal-address parent pointer | Source-only / explicit mode | Same | Coherent only with special non-send semantics for a field that currently names an address. More vulnerable to a missed old consumer; no demonstrated benefit beyond preserving the old string shape. |

Unexpected survivor: C1. It adds no status mode field and can still be governed by a verified immutable selection. The reason to prefer C2 is not that C1 is impossible: C2 makes the chosen operating mode directly inspectable to current state consumers without mining narrative or dispatch shape.

## Findings

### CH1 — Two phase scopes do not require two Coordinator identities

Illustrative symbols below are design variables, not fabricated native addresses or task state. C is the actual task Coordinator, H the declared human, EA/EB distinct phase Executors, and RA/RB independent Reviewers. The minimal direct-phase C2 route table is:

| Scope | Worker recipient | Coordinator upward recipient | Local action |
|---|---|---|---|
| Task | C | H | Own readiness, owner decisions and final integration. |
| Phase A | C | H | Read/write A's own bounded planning/state; receive EA/RA; record A's accepted bounded result. |
| Phase B | C | H | Validate A's required result before B specification/launch; receive EB/RB; preserve B state separately. |
| Existing delegated phase form | Distinct phase Coordinator P | C | Preserve the ordinary P-to-C phase return where that arrangement is actually selected. |

The real human route belongs to C while it works in a phase scope. It does not authorize EA/RA/EB/RB to contact H. `handoff.md` and `review.md` explicitly direct workers to `coordinator_route`; Research follows the same local Coordinator rule. Phase completion by C is a local durable checkpoint under the phase's existing artifact/state owners, not `PHASE_READY` sent C-to-C. The task then evaluates dependencies from that durable phase result. No imaginary dispatch to C-as-a-child is created.

This distinction protects the current ancestor/cycle prohibition for actual unit edges while allowing one unit to act in several authorized scopes. Phase root/owner/holder equality is a necessary check; the same owner alone is insufficient. Mode and holder topology are related but separate: `manual` describes who starts roles, and `visible-agents` describes their hosting. A new mode field must not invent a general ban on every other explicitly authorized topology. The required subagent path specifically retains the one main Coordinator.

### CH2 — Adversarial scenarios against C2 and shared survivors

These are source-based scenario analyses. No rewritten reader, real two-phase task, interruption or independent Reviewer was executed during this stage.

| Scenario | Required result / oracle | Outcome of source-based analysis |
|---|---|---|
| A unfinished; B requests implementation | B cannot advance until its actual predecessor condition and approved B TS hold; C records the existing pending dependency | Fits phase-local lifecycle and existing Pre-TS check; no extra Coordinator is necessary. Actual native path still owed. |
| Phase says owner H but local recipient is foreign X | Reject the direct-phase form unless X equals the exact governing task Coordinator and owner/authority lineage agree | C2 remains safe only with both holder and parent checks; checking the human alone would fail. |
| Worker reads phase owner upward | Worker still returns to local `coordinator_route`; only C acts on its upward route | Existing worker workflows already support this separation. All changed common wording must preserve it. |
| Same C in root/phase; old generic phase return code | Record local phase completion; do not invoke native send to C | C2 keeps actual recipients distinct; C5/C6 require a special equality branch everywhere and are more fragile. |
| Complete historical five-field or seven-field carrier lacks new mode | Preserve its epoch and valid original choices; no inferred enum, migration or fresh native launch grant | Old mode absence remains compatible. A current mode write adopts current full shape at a safe explicit checkpoint. |
| Historical partial route or half selection pair | Refuse dependent activation; do not fill missing facts by guessing or call it valid legacy | Existing partial-spine refusal remains. A new mode without its required current selection is also incomplete. |
| Status mode disagrees with frozen baseline/event | Refuse dependent launch until the owning Coordinator resolves the actual current selection; parser enum success is insufficient | Extra field has a real consistency cost; source/current comparison is mandatory, not presumed from source existence. |
| Future-effective event or unrelated phase selection | Keep current state until the named checkpoint; require exact covered phase/role scope on adoption | A new root selection cannot silently mutate phase authority. Local adoption and delivered revocation remain explicit. |
| Independent review sees an Executor's changing branch | Review fixed reachable Candidate; stop conflicting mutation or use an exact isolated snapshot; unrelated later trace cannot redefine the reviewed product | Native agent separation alone fails this oracle. Rung-1 correction returns to the original Executor and original independent Reviewer. |
| Same native ID resumes in a missing/wrong worktree | Stop mutation and reconstruct actual base/path/authority; do not treat ID or old cwd as proof | Supported by current local worktree caveat and documented Claude fallback. Resume is not equivalent to checkout preservation. |
| Native unit cannot resume | Preserve artifacts and source bounds, obtain valid replacement authority, bind a genuinely new unit and its predecessor, or keep the exact owner action pending | No identity reuse by name, assumed permission or relayed transcript. Human cancellation is not overridden. |
| More phases than concurrent native slots | Schedule ready scopes and active workers within observed capacity; preserve exact correction identity; report a real capacity blocker | A limit on simultaneous units is not a limit on total phases. If idle retained workers consume all slots, retirement/replacement needs explicit supported lifecycle and authority; do not assume completion frees a slot. |

### CH3 — One field must earn its maintenance cost

Proposed `coordination_mode` has one job: expose the selected owner interaction/hosting mode at the effective task/phase state, before any worker exists. Proposed vocabulary is `manual`, `visible-agents`, `subagents`. Its authority remains the actual immutable baseline or selected event, not the enum. The current seven routing/selection fields keep their jobs; new current writes would add this field while legacy complete carriers remain readable. Do not add a second topology registry or copy the entire selection into status.

C2's cost is coordinated changes to the closed allowed-key set, new-write validation, status/HL/event guidance, current workflow consumers and shipped entries. It also requires an explicit direct-phase parent/holder rule and mode/source mismatch behavior. Benefits are an inspectable choice and routes that always name an actual human or Coordinator. Rejecting the field leaves C1 viable, but each mode-sensitive consumer must then inspect the exact source; it cannot silently infer `subagents` from equal routes or a child receipt. Rejecting both C1 and C2 in favor of C3–C6 pays for an additional route meaning without eliminating source validation.

No new permanent tests are proposed. Approved implementation can use existing checks and bounded scenario evidence; the owner decides any extra permanent maintenance burden. No quantitative implementation cost is known before the TS delivery set/denominator.

### CH4 — Worktree separation is necessary evidence, not a whole review boundary

The [official Git worktree manual](https://git-scm.com/docs/git-worktree#_refs), fetched in this stage, confirms per-worktree HEAD/index alongside mostly shared refs. Therefore an immutable Candidate SHA, explicit workdir and actual reachable authority are stronger anchors than branch labels or the mere existence of a worktree. Git worktrees do not prove context independence, provider permissions or role judgment.

Actual checks during Challenge: own `git rev-parse --show-toplevel` returned the managed `cmodes-research` checkout; HEAD was `b64c24171b8488cd207901eace3058929b53ef37`; frozen authority `28af8624b5a42f5078e6303ca844dabd1fbbcab6` resolved as a commit; the diff from product checkout contained only Briefing/Gather/Extract; the working tree was clean before this stage write. These checks verify this Researcher's scope and reachable history only. They are not tests of C2, a changed parser, host restart or another role.

### CH5 — Hypothesis verdict and remaining acceptance proof

H1 is partially supported: exact native identity, a local same-session durable return/continuation and own-worktree trace isolation are observed here; primary documents support further surface-specific mechanisms. Independent Review, stopped-worker recovery, host restart, slot lifecycle and a complete cross-platform task cycle remain unproved. A blanket H1=true would be false precision.

H2 has a coherent surviving design, C2, with C1 a lower-schema fallback. The current implementation still rejects the same-holder phase and has not been modified. The key architectural fact is separating a bounded scope from the actual working unit and separating local aggregation from a native message. Product acceptance still requires actual current consumers and scenario evidence, not merely this table.

Iteration 2 should attack the selected C2/C1 representation with the final planned acceptance examples, the safe mode-switch path and the returned ECFIX interface. ECFIX owns source discovery, numeric categories, copied-history and reconciliation; this research supplies only the ordinary task/phase/role/parent/source/return lineage. Its missing accepted result prevents dependent economics acceptance, not this bounded H1/H2 conclusion.

## Checkpoint

| Found | Remaining |
|---|---|
| C2 is the preferred coherent survivor; C1 is a concrete fallback | Coordinator/owner architecture selection through Plan; no product approval from Research. |
| Same-holder phases can preserve exact state and real upward recipients without self-send | Implement and independently verify direct-phase consumers; actual two-phase dependent run remains owed. |
| Explicit mode pays for inspectability but needs source/current consistency | Final schema/adoption details and receiving-context checks belong to specification and delivery. |
| Source-based adverse scenarios identify precise failure oracles | Native interruption/restart, independent fixed-Candidate review, capacity lifecycle and named Claude execution remain unproved. |

**Sufficiency:**
- [x] External source used for shared-ref and Candidate reasoning.
- [x] Briefing gap closed for iteration-1 Challenge: surviving design and residual proof are explicit.
- [x] Pairwise constraints checked; conditional survivors and reasons for preference are recorded.

Material handover: this exact Researcher returns source-based analysis and its own bounded Git observations at the stated epochs. Current knowledge is applied only in its surviving scope; no history is rewritten and no new authority or provider guarantee is asserted. Recommend closing Challenge and authoring iteration-1 RES with C2 preferred, C1 fallback and all unproved native checks retained. Question: accept the stage for synthesis under those limits?

Stage complete: YES
→ Coordinator decision: `/root` accepted Challenge `2a3e2ee41d8692db6ba3e514c5973bbe435b441b` for synthesis on 2026-10-27. RES must retain C2 as a recommendation and C1 as viable, H1 partial and H2 coherent-but-unimplemented, missing native checks and the ECFIX boundary. Own numeric accountability is required before the final immutable return; iteration 2 remains Coordinator-prepared.
