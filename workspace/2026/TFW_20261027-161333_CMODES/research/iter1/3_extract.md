# Extract — What combinations are missing from the current design?

> Mindset: Analyst. Expose compatible configurations before judging survivors.
> Parent: [approved HL](../../HL-TFW_20261027-161333_CMODES.md).
> Goal: Preserve phase-local state and independent roles with one Coordinator across subagent phases.
> Producer/recipient: `/root/cmodes_research` → `/root`; own source `01a17db6-0f53-7603-878a-adaa590010e4`.
> Authority: HL freeze `28af8624b5a42f5078e6303ca844dabd1fbbcab6`; same dispatch, baseline/native-gates/tfw-gates-only and own source binding as Briefing. Originating proposer: none.
> Epoch: product checkout `c852d40c63b9c1d601d55fcd0552d03a47e157b0`; accepted Gather `a09cc19b7d5793f2b1c1b020f4a0e6c6adc67a47`; 2026-10-27 official source retrieval. One focused OODA pass.

## Configuration Space

Gather's D3 is an ordered policy rather than three mutually exclusive product modes: continue the exact valid unit when available; otherwise seek an authorized replacement from durable files; if native recovery is absent or human cancellation applies, keep the next action pending for the responsible owner. A replacement is not called same-unit continuation. No research mandate grants arbitrary role replacement.

For D1, all configurations retain each phase's own status/journal/HL derivation/TS/worker results. The task's PHASES state does not aggregate lifecycle or delete phase ownership. Values below are design sketches, not newly valid syntax.

| Config | D1: representation of a phase governed by the task's same physical Coordinator | D2: current mode carrier | D3: recovery when a worker cannot continue |
|---|---|---|---|
| C1 | A: same Coordinator recipient; upward human route; root-holder identity checked separately | A: verified baseline/selection event only | Ordered A → bounded B → explicit C |
| C2 | A: same Coordinator recipient; upward human route; root-holder identity checked separately | B: explicit current status mode checked against selection | Same ordered policy |
| C3 | B: explicit local task-owned relation, e.g. upward value `task:<task-id>`; root identity supplies actual holder | A: verified baseline/selection event only | Same ordered policy |
| C4 | B: explicit local task-owned relation, e.g. upward value `task:<task-id>`; root identity supplies actual holder | B: explicit current status mode checked against selection | Same ordered policy |
| C5 | C: keep `coordinator:<root-native-address>` with equal local recipient; equal-address case means local scope aggregation | A: verified baseline/selection event only | Same ordered policy |
| C6 | C: keep `coordinator:<root-native-address>` with equal local recipient; equal-address case means local scope aggregation | B: explicit current status mode checked against selection | Same ordered policy |

D2-C (infer mode from dispatch/agent shape) is excluded as an obvious contradiction: before the first worker dispatch there is no shape, and a manually created visible role looks like an automatically created one after creation. It cannot express an effective owner choice independent of capability and launch receipts. Three D1 × two remaining D2 combinations × one ordered D3 policy give the six configurations above. This includes a previously unproposed combination: an explicit local task relation with the existing selection source and no extra status mode field (C3).

## Findings

### E1 — Compare meaning and obligations, not labels

| Configuration family | Meaning of phase upward value | Additional contract work | Distinct risk to challenge |
|---|---|---|---|
| C1/C2: human upward | The same actual task Coordinator retains its real human escalation route while operating a phase scope | Validate root holder and human owner match; make phase completion a local checkpoint, not a worker-to-owner message; retain delegated phase route for other selected topology | A careless reader may send routine phase traffic directly to the owner or admit an unrelated holder merely because the owner matches. |
| C3/C4: local task relation | The parent relationship explicitly names task scope; transport resolves only for actual inter-unit edges | Add one new route variant and define non-send semantics; validate exact local root ID and holder; preserve existing owner/coordinator/legacy variants | A route field becomes both structural relation and transport; adapters may invent a native target from the task ID or recursively resolve the same holder. |
| C5/C6: equal-address parent | Existing upward coordinator pointer names the parent scope's holder even when physically the same | Permit equality only under verified selected single-holder topology; suppress native self-send; preserve rejection of real unit cycles | Existing wording and helpers treat the value as a native message edge. One missed consumer creates a self-send or repeated local return. |
| C1/C3/C5: source-only mode | Effective status points to the immutable source that carries selected mode | Define precise mode vocabulary in baseline/event and require every relevant agent/reader to resolve it; define machine check scope honestly | Existing source checks prove object/envelope, not semantic mode; mechanical validation may need new structured parsing or remain only a shape check. |
| C2/C4/C6: status mode | A proposed `coordination_mode` field carries current `manual`, `visible-agents` or `subagents`; immutable selection still supplies authority | Extend the allowed status-key set and current-write contract; compare the value with actual approved selection at adoption; legacy absence preserves original authority | Duplicated effective value can disagree with source; a parsed enum never proves human consent. |

The difference between source-only and explicit-status mode is one proposed status field, not a justified new registry. No new task-ID system, per-role roster file, daemon, event replay or status service is needed by any survivor. Exact implementation effort/denominator remains for the Coordinator's researched TS; this table claims no file/LOC/time estimate.

### E2 — What the current reader can and cannot prove

At this epoch `STATUS_KEYS` rejects unknown fields; adding a mode field requires a real schema change. `verify_baseline_source` checks that the cited immutable object starts with an HL heading. `verify_selection_source` verifies commit existence, exact event bytes, event envelope/kind and owner equality. It does not parse the human's answer, topology, phase scope, effect time or reservations from prose. Existing workflow rules already require agents to inspect those meanings.

Consequently, none of C1–C6 may claim that parser success authenticates consent. C1/C3/C5 cannot obtain a machine-selected topology merely by locating an HL. C2/C4/C6 can give the reader an explicit syntax branch, but must still refuse a missing/contradictory mandate during activation. Improving validation must stay proportionate: machine checks can verify fields, parent identity, combinations and source reachability; authorized agents validate human-rooted meaning. Making ordinary operation depend on a new NLP parser or replay engine contradicts the existing portable-file architecture.

### E3 — All modes retain the same work and acceptance

| Selected mode | Single phase | Multiple phases | Owner action that remains real |
|---|---|---|---|
| Manual | Owner starts distinct role units; one task Coordinator holds its ordinary scope | Existing separately bounded phase-Coordinator arrangement remains usable; explicit task-local authority determines each role | Actual launches and reserved decisions; manual launch does not automatically select manual return transport. |
| Visible agents | Authorized Coordinator provisions visible distinct roles where native capability permits | Existing distinct phase-Coordinator route remains usable; bounded results go upward to task Coordinator | Provider-required creation actions and reserved HL/TS/overrun/acceptance decisions. |
| Subagents | Same task Coordinator launches distinct Researcher, Executor and independent Reviewer | Same task Coordinator owns ready phase planning and receives those phases' distinct workers; phase state remains separate | Missing actual native capability or authority and reserved decisions; phase count alone adds no owner click or phase Coordinator. |

These are required behavior paths, not a declaration that manual/visible users can never choose another authorized topology. The research adds no new restriction beyond the approved target. Each selected topology must be explicit enough to interpret its phase state. A worker always returns to its recorded local Coordinator; only the actual task Coordinator presents owner gates. When one unit holds task and phase scope, it records the bounded phase outcome locally and advances dependency checks, without messaging itself or pretending another agent returned it.

### E4 — State adoption and recovery stay bounded

For all six configurations:

1. At startup, explain and record the owner's operating choice before using it. A provider can expose an option without authorizing a launch. New mode syntax has a current contract; historical absence is not silently converted to `visible-agents` or `manual` because old Claude compact operation also exists.
2. Legacy complete carriers keep their actual authority and readable history. Partial carriers still refuse. No old event/HL is rewritten. A new implementation does not promote an active historical task to current native subagent operation.
3. A mode/topology switch records the actual human selection and effect checkpoint under the HL ceiling. While it is pending, old effective state governs. Stop new incompatible launches; preserve outstanding worker artifacts and fixed Candidates. Adopt each covered phase explicitly rather than continuously inheriting root live state.
4. At an effective same-holder phase, validate exact parent task, matching actual Coordinator and phase-scoped authority. At a delegated phase, retain a distinct actual holder and upward address. In either case a foreign/sibling event, stale selection or ungranted replacement blocks the dependent act.
5. After interruption, validate current source, native ID, worktree/base, own artifact and unfinished act before continuing. Same agent ID is insufficient if the worktree or Candidate changed. A fresh replacement receives command-only activation and current durable context; the predecessor result remains attributable and no accepted work is silently replayed.
6. Scheduling considers actual available slots. Phase count does not equal concurrent worker count. Reuse the same Executor and independent Reviewer within their valid correction lineage when supported; do not manufacture identity or call a new worker the old one to save slots.

### E5 — Native isolation needs exact base and working-directory checks

The [official Claude worktree page](https://code.claude.com/docs/en/worktrees#isolate-subagents-with-worktrees), fetched for this stage, documents subagent worktrees branching from the default branch unless configured otherwise. It also states that instruction files initially come from the main conversation, and that a missing worktree on session resume can clear the old binding and fall back to the launch directory. Thus worktree creation or same-ID resume cannot by itself prove the worker sees the approved task state. Before mutation or review, verify actual path and reachable authority/Candidate; after resume repeat the check. These are documented Claude behaviors, not experiments performed here.

For this Codex child, the managed worktree was explicitly created from observed HEAD and returned its actual path; the app said it cannot change this child's working directory automatically. Exact `workdir` remained necessary. The observed successful stage commits establish this child's bounded trace isolation only. Independent Reviewer judgment and cross-platform behavior remain the missing proofs from Gather.

### E6 — Economics handover interface without taking ECFIX's work

All configurations can use existing dispatch/role-return records to carry the same finite tuple: task ID, phase scope if real, role, actual unit ID, parent unit, selected authority epoch, returned artifact revision, native source binding and correction/replacement relationship. Phase-local scope and physical native unit must not collapse into one key: one Coordinator can contribute to several scopes, while an Executor and Reviewer stay distinct units.

CMODES supplies that lineage; ECFIX decides its accepted numeric source/range and reconciliation interface. The existing optional analytical `coordination_mode` name is not a separate source of authorization. No child collector, copied-history experiment, automatic usage split or double-counting rule is authored here. The unresolved returned ECFIX contract remains H3/iteration 2.

## Checkpoint

| Found | Remaining |
|---|---|
| Six coherent candidate configurations; inference-only mode excluded for a concrete ambiguity | Challenge self-routing, wrong-holder admission and selection mismatch for each family. |
| Exact existing parser/source-verification boundary | Choose whether one explicit current field pays for itself or source-only mode stays sufficient. |
| Common mode paths, legacy preservation and safe adoption rules | Challenge two-phase dependency, correction, stopped/replaced worker and owner reservation scenarios. |
| External worktree base/resume limitations | Native interruption/restart and independent Review remain unproved; no full-cycle claim. |

**Sufficiency:**
- [x] External primary source fetched and used for a material new constraint.
- [x] Briefing gap closed for Extract: compatible representations and obligations are visible.
- [x] Configuration space built from Gather D1–D3; no preferred product configuration declared yet.

Material handover: same Researcher and exact parent, at the stated epochs. This is a source-based design comparison, not a product change or accepted architecture. PCUX core/profile ownership, ATC historical semantics, GSC role-owned material and TEQM finite sources remain preserved. Recommend closing Extract and running the existing Challenge checkpoint against C1–C6, grouping shared D1/D2 properties to avoid repetition. Question: accept this comparison and proceed to Challenge?

Stage complete: YES
→ Coordinator decision: `/root` accepted Extract at `b64c24171b8488cd207901eace3058929b53ef37` on 2026-10-27 and authorized Challenge across shared families. Required emphasis: two dependent phases, self-send/worker-to-owner avoidance, old complete/partial carriers, contradictory or stale selection, fixed Candidate with separate Reviewer, and actual path/base on resume/replacement. Architecture remains unapproved; ECFIX keeps numeric/source/reconciliation ownership.
