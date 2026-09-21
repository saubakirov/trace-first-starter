# TS — TFW_20260920-223357_FRATS / Phase A: Explicit Coordination, GATEWAY and Session Identity

> **Date**: 2026-09-21
> **Author**: Codex (Coordinator), acting as `saubakirov`
> **Status**: ✅ APPROVED — saubakirov, 2026-09-21
> **Approval**: Exact TS and immutable denominator approved: 47 VALUE files / 3,200 touched text LOC
> **Parent HL**: [Master HL](../HL-TFW_20260920-223357_FRATS.md)
> **Phase HL**: [Phase A derivation](HL__phase-a__explicit_coordination_gateway_and_session_identity.md)

---

## 1. Objective

Deliver one compact, provider-neutral coordination contract in which a correctly skill-activated
unit can work autonomously without inventing authority or conversational routes. The finished phase
must make the current Coordinator, owner ingress, dialogue boundary and activation authority
discoverable from task state; keep ordinary traffic vertical and durable; isolate iterative dialogue
behind a clean GATEWAY; and prove the result through exact schema, route, adapter and provider-native
evidence.

## 2. Scope

### In Scope

- Replace newly issued `CL`/`AG`/`AT` mode semantics with independent workflow autonomy, dialogue,
  activation and authority facts while retaining historical readability.
- Define one canonical coordination vocabulary and make task-bound workflow readers consume it
  before questions, dispatch acceptance or work.
- Extend current status and event contracts with the five-field routing spine and `gate_answer`.
- Define the gates-only route, exact iterative grants, GATEWAY/root-Coordinator separation and
  Reviewer independence.
- Require exact `/tfw-*` skill activation with task/phase and dispatch or owner-direct provenance;
  distinguish provision and continuation and refuse ad-hoc role prompts before material work.
- Preserve actual unit, parent, role/phase, native address/channel and dispatch provenance through
  immutable dispatch plus Briefing/RES, ONB/RF and REVIEW producer identity.
- Make stable named principals conditional on reusable attribution need and keep title, principal,
  unit, mandate, human accountability, capability and approval separate.
- Prevent unsolicited cross-role prework, distrust-only duplicate execution and peer correction
  dialogue without weakening required independent verification.
- Synchronize changed canonical behavior to the installed Codex, Claude and Antigravity surfaces and
  the maintained Cursor source; preserve receiver-safe update compatibility.
- Collect bounded, separately classified Codex, Claude and Antigravity observations.

### Out of Scope

- Phase B consistency/compression, filename-producer repair, D75 publication correction and receiver
  replay or mutation.
- Repository/worktree landing policy, target locks, release serialization, capability/IAM
  enforcement, signature/provenance infrastructure and changes from `FRATS-D01`.
- Framework versioning, CHANGELOG, release notes, tags, push, publication or deployment.
- New participant registries, mandatory artifacts, transcript stores, brokers, runtimes or global
  schedulers.
- Renaming or normalizing historical task artifacts, events, mode references or provider evidence.
- New permanent test files; task-local evidence and updates to the existing command-entry evaluator
  are sufficient for this phase.

## 3. Principles Check

| # | HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Autonomy follows activation, not a mode label | AC-1, AC-4 | No new-work mode value; accepted activation scenarios start autonomous Role-Locked work. |
| P2 | Explicit routes beat remembered conventions | AC-2, AC-3 | Complete routing spine resolves before work; missing/partial state refuses. |
| P3 | Vertical by default | AC-3 | Allowed-edge matrix has only unit↔own-Coordinator gates/returns under `tfw-gates-only`. |
| P4 | GATEWAY protects owner attention | AC-3 | Separate unit, title and negative ingress/workflow scenarios. |
| P5 | Activation is an address, not a briefing | AC-4 | Minimal activation succeeds; role prompt, “wait” and substantive briefing fail before work. |
| P6 | Roles contribute, they do not pre-solve one another | AC-6 | Cross-role prework and distrust-only repetition are rejected; named independent checks remain. |
| P7 | One truth, one owner, one reader path | AC-1, AC-7 | One normative semantic owner; copies are exact projections. |
| P8 | Subtraction without semantic loss | AC-1, AC-9 | Current behavior is simplified without a size quota; six semantic edges remain observable. |
| P9 | Structural enforcement | AC-2–AC-6 | State/event schemas, owned artifacts and refusal scenarios expose violations. |
| P10 | Native evidence before provider claims | AC-8 | Provider-native P0–P4 ledger; no translated or composed claim. |
| P11 | Independent review remains independent | AC-3, AC-6 | Reviewer never joins result-development dialogue and remains a distinct unit. |
| P12 | Receivers are evidence, not fixtures to rewrite | AC-8, AC-9 | No receiver mutation; observations are source/epoch bounded. |
| P13 | No receiver runtime tax | AC-1, AC-7 | Ordinary files and existing adapters only; no service, broker or maintained roster. |

## 4. Affected Files and Value-Bearing Accounting

Whole-file precedence makes shipped canonical sources, optional diagnostics and maintained adapter
surfaces `VALUE`. The existing command-entry evaluator is `ASSURANCE`. Task control and evidence
artifacts are `TRACE`; generated documentation is `DERIVED` and must reproduce cleanly but is not
committed as a Phase A output.

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `.tfw/conventions.md`, `.tfw/glossary.md` | MODIFY | `VALUE` | Single provider-neutral coordination authority and precise routing terms. |
| `.tfw/templates/status.md`, `.tfw/templates/journal/event.md` | MODIFY | `VALUE` | Closed routing spine, legacy-read boundary and authority-owned `gate_answer`. |
| `.tfw/templates/HL.md`, `.tfw/templates/bindings.yaml`, `.tfw/templates/team/profile.md` | MODIFY | `VALUE` | Remove active mode/LEAD assumptions while retaining optional stable attribution and frozen authority. |
| `.tfw/templates/research/1_briefing.md`, `.tfw/templates/RES.md`, `.tfw/templates/ONB.md`, `.tfw/templates/RF.md`, `.tfw/templates/REVIEW.md` | MODIFY | `VALUE` | Actual producer/parent/dispatch identity and writer-owned question/answer references. |
| `tools/tfw_state.py` | MODIFY | `VALUE` | Read/validate current and legacy status/event carriers without guessing routes. |
| `.tfw/workflows/{plan,research/base,handoff,review,docs,knowledge,release,init,update}.md` as expanded literally below | MODIFY | `VALUE` | Workflow-local activation, route, return, refusal and migration actions. |
| `.tfw/adapters/{codex/AGENTS.md.template,claude-code/CLAUDE.md.template,antigravity/tfw-rules.md.template,cursor/tfw.mdc.template}` plus `AGENTS.md`, `CLAUDE.md`, `.agents/rules/tfw.md` | MODIFY | `VALUE` | Persistent provider entry behavior and native mechanics without a second semantic contract. |
| `.claude/commands/tfw-{command}.md`, `.agents/workflows/tfw-{command}.md` for the nine changed commands listed below | MODIFY | `VALUE` | Exact manifest-derived copies of changed canonical workflows. |
| `docs/scripts/command_entry_eval.py` | MODIFY | `ASSURANCE` | Existing entry fixture understands the new required state and refusal routes; no new permanent test file. |

The exact VALUE selector is this literal 47-path set:

```powershell
$valuePaths = @(
  '.tfw/conventions.md',
  '.tfw/glossary.md',
  '.tfw/templates/status.md',
  '.tfw/templates/journal/event.md',
  '.tfw/templates/HL.md',
  '.tfw/templates/bindings.yaml',
  '.tfw/templates/team/profile.md',
  '.tfw/templates/research/1_briefing.md',
  '.tfw/templates/RES.md',
  '.tfw/templates/ONB.md',
  '.tfw/templates/RF.md',
  '.tfw/templates/REVIEW.md',
  'tools/tfw_state.py',
  '.tfw/adapters/codex/AGENTS.md.template',
  'AGENTS.md',
  '.tfw/adapters/claude-code/CLAUDE.md.template',
  'CLAUDE.md',
  '.tfw/adapters/antigravity/tfw-rules.md.template',
  '.agents/rules/tfw.md',
  '.tfw/adapters/cursor/tfw.mdc.template',
  '.tfw/workflows/plan.md',
  '.tfw/workflows/research/base.md',
  '.tfw/workflows/handoff.md',
  '.tfw/workflows/review.md',
  '.tfw/workflows/docs.md',
  '.tfw/workflows/knowledge.md',
  '.tfw/workflows/release.md',
  '.tfw/workflows/init.md',
  '.tfw/workflows/update.md',
  '.claude/commands/tfw-plan.md',
  '.agents/workflows/tfw-plan.md',
  '.claude/commands/tfw-research.md',
  '.agents/workflows/tfw-research.md',
  '.claude/commands/tfw-handoff.md',
  '.agents/workflows/tfw-handoff.md',
  '.claude/commands/tfw-review.md',
  '.agents/workflows/tfw-review.md',
  '.claude/commands/tfw-docs.md',
  '.agents/workflows/tfw-docs.md',
  '.claude/commands/tfw-knowledge.md',
  '.agents/workflows/tfw-knowledge.md',
  '.claude/commands/tfw-release.md',
  '.agents/workflows/tfw-release.md',
  '.claude/commands/tfw-init.md',
  '.agents/workflows/tfw-init.md',
  '.claude/commands/tfw-update.md',
  '.agents/workflows/tfw-update.md'
)
```

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | The literal 47-path `$valuePaths` array above; whole-file membership, no freehand exclusions. |
| Baseline / selector source | `c80c0dd5e79a6e996fdc68a89ad01b26887c638e`; this TS at its future owner-approval commit. |
| Candidate rule | First tested Executor commit with required VALUE+ASSURANCE, before EV/RF/REVIEW/final transition; excluded-only later writes do not move it; later VALUE requires a new Candidate and recomputation. |
| Logical VALUE files | 47 planned; rename = one. An already-compliant listed path stays unedited and is reported as zero-diff rather than changed for the count; the immutable planned denominator remains 47. |
| Touched text LOC | 1,900 additions + 1,300 deletions = 3,200 planned; numeric numstat fields; binary/non-text = per-file N/A. |
| Triggers / disposition | Config prompts at 50 VALUE files or 5,000 touched text LOC. The current 47/3,200 plan remains one phase because every path is one coordinated semantic/copy migration and splitting would create incompatible schemas/readers. Crossing either prompt requires a prospective cause/cost/assurance/split ruling before the added work. |
| Multiplier / authority | Immutable plan 47 files / 3,200 LOC; owner decision required at 94 files or 6,400 LOC, from any planned-zero class, or for a change to Goal, Value, outputs, AC, DoF, phase/ownership, architecture, target, interfaces, data, security, trust or authority. Below both multipliers, the Coordinator may admit only a necessary constituent with all those invariants fixed and a pre-work ruling. |
| Approval epoch / failure | Prospective owner approval of this exact TS and denominator; missing/mutable/mismatched/late = BLOCKED; metric-only N/A; unresolved phase attribution = INVALID; DEFERRED is non-terminal. |

```powershell
git diff --name-status --find-renames=50% -z c80c0dd5e79a6e996fdc68a89ad01b26887c638e <CANDIDATE_SHA> -- $valuePaths
git diff --numstat --find-renames=50% -z c80c0dd5e79a6e996fdc68a89ad01b26887c638e <CANDIDATE_SHA> -- $valuePaths
```

### Prospective scope rulings

None. The plan is below both configured decomposition prompts. The 47-file count is driven by one
canonical change plus mandatory installed copies, not by independent deliverables; splitting before
the schema, workflows and adapters agree would create a temporarily invalid product.

No task-local M1–M6 hard constraint is introduced. The phase's prohibitions are acceptance and
Role-Lock boundaries, not a new pre-act technical lock.

**Actions (not budget dimensions):** 47 MODIFY `VALUE`; 1 MODIFY `ASSURANCE`; no planned VALUE
CREATE/DELETE/RENAME. Phase control, EV/RF and bounded evidence attachments are `TRACE`.
**Immutable owner-approved denominator:** 47 VALUE files and 3,200 touched text LOC; never ratchets.

## 5. Acceptance Criteria

Each AC is independently verifiable. Dependencies prevent a workflow/copy change from outrunning
the shared semantics it consumes.

### AC-1: One current coordination vocabulary

Current normative surfaces define workflow autonomy, provision, activation, continuation, TFW gate,
durable return, iterative dialogue, routing spine, Coordinator and GATEWAY once. `CL`, `AG`, `AT` and
LEAD remain readable as historical terms but are never issued as current task controls.

- [ ] `conventions.md` owns the complete provider-neutral model; the glossary routes each term to it.
- [ ] Workflows contain only role-local actions/refusals and adapters only provider-native mechanics.
- [ ] A dispositioned census identifies every remaining active-tree `CL`/`AG`/`AT`/LEAD occurrence
  as historical compatibility, preserved evidence or a defect; no unexplained current issuer remains.
- [ ] No new runtime, registry, mandatory phase artifact or provider-specific core rule is introduced.

Gate: source/reader/remaining-occurrence census with all current issuers at zero and every retained
historical occurrence dispositioned in Phase A evidence.
Evidence: N/A — provider-independent semantic ownership is verified from the repository and copies.

### AC-2: Closed routing spine with safe compatibility [depends: AC-1]

Every newly created or currently written task/phase status contains exactly the five coordination
facts in addition to the existing closed schema:

- `coordinator_route`: one quoted, non-empty provider-native unit address;
- `owner_gateway`: `owner:{declared-human-handle}` or
  `gateway:{non-empty-provider-native-unit-address}`;
- `dialogue`: exactly `tfw-gates-only` or `iterative`;
- `activation`: exactly `owner-only` or `delegated:{immutable-mandate-ref}`; and
- `coordination_authority`: one quoted exact local authority reference plus immutable epoch.

- [ ] The five fields are all-or-none for legacy reads and all required for a new/current write;
  partial sets, empty values, placeholders and unresolved route/authority are rejected.
- [ ] A complete pre-A3 status remains readable without byte changes and is reported as legacy
  coordination state; it cannot activate new work until an authorized current migration supplies all
  five fields.
- [ ] Terminal historical tasks and immutable events are never bulk-normalized.
- [ ] The current Phase A status is migrated only after the Candidate implements and validates the
  new schema; the migration does not invent a same-state transition or event kind.

Gate: positive/current, complete-legacy, partial, empty, invalid-enum, unresolved-authority and
terminal-history fixtures through the template contract and `tools/tfw_state.py`.
Evidence: `evidence/coordination-scenarios.md` records exact inputs, verdicts and current-carrier migration.

### AC-3: Vertical gates and isolated iterative dialogue [depends: AC-1, AC-2]

- [ ] Under `tfw-gates-only`, the only communication edge for a working unit is unit↔its own
  Coordinator, and only for declared TFW gates, structured status/correction and durable returns.
- [ ] Worker↔worker, worker↔foreign-Coordinator, worker↔owner and worker↔GATEWAY attempts refuse even
  when the provider can technically send them.
- [ ] `iterative` requires an owner-approved exact peer grant naming the two units, purpose, boundary,
  consolidator, durable output and stop; no grant or an over-broad grant refuses.
- [ ] Iterative work has distinct GATEWAY and root Coordinator units. GATEWAY is the sole clean
  owner-facing ingress, performs no workflow role, receives no raw worker traffic and joins no peer
  dialogue.
- [ ] An independent Reviewer cannot be a dialogue peer for the result it later reviews.
- [ ] GATEWAY navigation is exactly `GATEWAY · {TASK}` or `GATEWAY · {handle} · {TASK}`; the optional
  stable handle grants no authority.

Gate: an allowed/prohibited edge matrix plus positive and negative iterative-grant scenarios; every
route names its durable carrier and refusal point.
Evidence: bounded native communication observations are recorded separately under AC-8.

### AC-4: Skill activation and reconstructable unit lineage [depends: AC-1, AC-2, AC-3]

- [ ] Provision creates only an addressable unit and grants no work.
- [ ] Valid activation contains only the exact `/tfw-*` skill, task/phase identity, immutable dispatch
  or explicit owner-direct provenance, and an exact continuation reference when resuming.
- [ ] “You are the Researcher/Executor/Reviewer”, “wait”, copied solution text and long briefing
  prompts do not activate work; the destination refuses before material work.
- [ ] Dispatch preserves actual source, destination, parent, role/scope, native address/channel,
  governing state/authority and originating proposer. Continuation resumes the same unit at the
  named authoritative gate and cannot silently replace it.
- [ ] GATEWAY may provision or activate a separate Coordinator only when `activation` carries the
  exact delegated authority; GATEWAY never invokes `/tfw-plan` as its own workflow.
- [ ] Ordinary owner-launched units do not resolve or invent an agent principal unless stable reusable
  attribution is materially required; accountable human, actual `via` and unit provenance remain.
- [ ] Session titles are applied at the earliest valid state checkpoint, read back where supported,
  reported once on failure and never treated as authority.

Gate: owner-direct, delegated-dispatch, continuation, prompt-only, briefing-biased, wrong-unit,
missing-skill and unavailable-holder scenarios with reconstructable trace and exact refusal.
Evidence: `evidence/coordination-scenarios.md` plus provider-native observations under AC-8.

### AC-5: Authority-owned gate answers [depends: AC-2, AC-4]

- [ ] `gate_answer` is a current immutable journal kind owned/written by the answering authority; its
  refs resolve to current status, the blocked role artifact and governing HL/TS authority.
- [ ] Its body identifies the question, answer, answerer/source, epoch, governing reference and
  operational effect without copying a chat transcript.
- [ ] ONB owns only the blocking question, blocker, `gate_answer` reference and resulting operational
  effect. Executor never appears to answer itself and the answer authority never edits ONB.
- [ ] Any answer that changes scope, acceptance, architecture, authority or an owner reservation is
  rejected as `gate_answer` and routes to TS revision or HL §12.
- [ ] Missing, stale, foreign, unverifiable or contradictory answer refs keep the unit blocked.

Gate: accepted factual answer plus self-answer, cross-task, stale-source, missing-ref and hidden
amendment negative fixtures through event/status validation and ONB inspection.
Evidence: N/A — immutable carrier behavior is verified from repository fixtures and exact refs.

### AC-6: Role-owned inputs and producer provenance [depends: AC-3, AC-4]

- [ ] Research Briefing/RES, ONB/RF and REVIEW identify their actual producer unit, parent and dispatch
  or explicit owner-direct source; mismatch with status/dispatch refuses work.
- [ ] A role consumes prior artifacts at their stated evidence level and never supplies unsolicited
  work for another Role Lock.
- [ ] Distrust alone creates no repeat-work obligation. Repetition names either an explicit workflow
  independence duty or a concrete contradiction/evidence gap.
- [ ] A detected discrepancy is recorded once in the detecting role's owned artifact and returned
  through that unit's own Coordinator, without peer debate.
- [ ] Required independent review, source checks and acceptance remain intact.

Gate: role/artifact matrix with positive independent-review cases and negative prework,
distrust-only duplication, peer-correction and producer-mismatch cases.
Evidence: N/A — role ownership is verified from templates, workflow routes and fixtures.

### AC-7: Canonical, adapter and migration parity [depends: AC-1, AC-2, AC-3, AC-4, AC-5, AC-6]

- [ ] Every changed Claude and Antigravity command copy is byte-identical to its manifest-defined
  canonical workflow; Codex, Claude and Antigravity managed persistent content matches its source;
  the maintained Cursor source expresses the same semantics without an installed-target claim.
- [ ] Codex skill routers remain thin and unchanged unless a concrete activation defect proves a
  required local action; if changed, their canonical and installed copies enter VALUE through a
  prospective scope ruling before the edit.
- [ ] `update.md` preserves historical artifacts/modes, refuses to guess routing facts, migrates only
  an active writable carrier with complete authority, and reports unresolved selection as owner work.
- [ ] Existing documentation generation/integration and blob-size checks pass. No new permanent test
  is added solely to satisfy this task.
- [ ] Candidate accounting uses the literal 47-path selector, reports every actual changed member and
  every justified zero-diff member, and receives a valid prospective scope ruling before any VALUE
  path outside the selector is edited.

Gate: manifest-derived parity, managed-block comparison, configured build commands and NUL-safe
Baseline→Candidate accounting.
Evidence: `evidence/copy-and-suite.txt` records exact commands, versions, exits and limits.

### AC-8: Provider-native evidence without composition [depends: AC-7]

For each of Codex, Claude and Antigravity, predeclare and attempt the same bounded native sequence:
resolve authoritative task/phase state; invoke the exact skill; apply the required title at its
checkpoint; obtain native readback when the surface exposes one; perform one allowed vertical gate
return; and demonstrate or explicitly bound one prohibited direct edge without sending material work.

- [ ] Every observation records provider/product, version, native surface, date, actual unit/address,
  action, checkpoint, result, readback method and unsupported claims.
- [ ] P0–P4 is assigned independently per provider: documentation, one operation, exact readback,
  predefined checkpoint series and full end-to-end reliability are never conflated.
- [ ] A missing native capability is recorded as a bounded limit, not translated through another
  provider, hidden helper, relay or fabricated success.
- [ ] No reliability percentage or cross-provider conclusion is made from the bounded trials.
- [ ] Any native result contradicting the A3 carrier/routing model stops Phase A and routes the exact
  contradiction to the Coordinator; a mere missing P3/P4 result is reported honestly and cannot be
  relabelled as proof.

Gate: independent provider ledgers and artifact-backed readbacks; Reviewer verifies each claim only
against that provider's own evidence.
Evidence: `evidence/provider-native.md` plus native screenshots/receipts where the surface supports capture.

### AC-9: Whole-phase semantic and quality gate [depends: AC-1, AC-2, AC-3, AC-4, AC-5, AC-6, AC-7, AC-8]

- [ ] Activation, authority, evidence, recovery, continuation and exception paths each have one
  positive and one material negative scenario, and all twelve outcomes match the frozen HL.
- [ ] The configured repository test command passes; the documentation generator/integration checks
  and Git blob-size boundary remain intact.
- [ ] No receiver project is modified, no historical artifact is renamed/normalized, and no deferred
  FRATS-D01 control appears in the Candidate.
- [ ] RF reports exact limitations, remaining historical compatibility and all observations; EV has
  one row per AC; independent REVIEW evaluates purpose and every provider limit.

Gate: six-edge scenario matrix, configured `python -m pytest tools/tests/ docs/scripts/ -q`, clean
exact-path diff review and independent `/tfw-review`.
Evidence: `evidence/EV__phase-a__explicit_coordination_gateway_and_session_identity.md` indexes all Phase A evidence.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-a__explicit_coordination_gateway_and_session_identity.md` | Required per-AC evidence, environment and verdict summary. |
| `evidence/coordination-scenarios.md` | Status, activation, routing, answer and role-ownership positive/negative cases. |
| `evidence/provider-native.md` | Separate Codex, Claude and Antigravity P0–P4 observations and limits. |
| `evidence/copy-and-suite.txt` | Manifest parity, managed-block checks, configured suite and accounting output. |

## 6. Technical Guidance

- Prefer one new `Coordination` authority in `conventions.md` over scattering replacement prose.
- Treat the five coordination fields as one all-or-none schema version in behavior, without adding a
  status schema-version field or normalizing sealed history.
- Keep provider address syntax opaque to the core; adapters may document how their native unit id is
  obtained and read back.
- Keep `gate_answer` within the existing journal carrier and current frontmatter vocabulary; place
  answer detail in the body and exact sources in refs rather than inventing answer fields/artifacts.
- Update existing fixtures/evaluators only where they are actual readers. Use task-local evidence for
  the phase-specific scenario matrix instead of creating a permanent test hierarchy.
- Generate installed workflow copies from canonical sources and validate them through the manifest;
  never hand-edit a copy into a second implementation.
- Preserve old task artifacts, changelog entries, migrations and research statements as history even
  when their CL/AG/AT/LEAD semantics are superseded for new work.

## 7. Definition of Failure

- ❌ A new task can still issue `CL`, `AG` or `AT`, or autonomy is inferred from a title/provider.
- ❌ A unit starts material work from a role prompt, “wait” instruction or briefing without its exact skill.
- ❌ Status omits, partially carries or guesses current routing facts; status becomes a worker roster.
- ❌ Gates-only traffic reaches a sibling, foreign Coordinator, owner or GATEWAY.
- ❌ GATEWAY performs workflow work, becomes root Coordinator, receives raw worker chat or joins dialogue.
- ❌ An iterative grant lacks exact peers/purpose/boundary/consolidator/output/stop, or includes its independent Reviewer.
- ❌ Executor appears to answer its own blocker, answer authority edits ONB, or `gate_answer` changes HL/TS authority.
- ❌ Unsolicited prework or distrust-only repetition crosses a Role Lock or starts a peer dispute.
- ❌ Historical tasks/events are rewritten, a receiver project changes, or FRATS-D01 controls enter scope.
- ❌ Canonical and installed adapter surfaces diverge or provider evidence is translated/composed.
- ❌ A new permanent test, runtime, registry, mandatory artifact or generic transcript store is introduced without owner approval.
- ❌ A VALUE path outside the selector is edited without a prospective authorized ruling, or an
  omitted listed path leaves its required behavior uncovered or is changed merely to hit the count.

**On failure:** stop before further mutation, preserve the exact carrier/evidence, record the failed AC
in RF/EV or the active owned artifact, and return it through the Phase A Coordinator. Architecture or
authority conflicts route to the owner through the master HL amendment channel; they are not patched
through dialogue or widened execution.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Compatibility makes the new schema optional forever. | Legacy absence is read-only compatibility; every current write/activation requires complete fields. |
| Forty-seven VALUE paths obscure one semantic change. | Literal selector, one canonical authority, manifest copies and exact Candidate accounting. |
| Provider address formats leak into core semantics. | Core requires a non-empty native address; each adapter owns extraction/readback details. |
| GATEWAY and root Coordinator collapse during implementation. | Separate status facts, titles and negative scenarios; no dual-role success case. |
| Gate answers become informal chat receipts. | Immutable authority-owned event with exact refs/epoch and hard escalation boundary. |
| Native trials consume time without proving reliability. | Fixed bounded sequence and P0–P4 classification; no repeated run after the claim boundary is established. |
| Current active task cannot dogfood fields before schema exists. | Master HL §4.1 remains temporary authority; migrate Phase A status after Candidate, before RF, without invented history. |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| `.tfw/conventions.md`, `.tfw/glossary.md` | Phase B | Phase B may compress only from the accepted Phase A semantics and six-edge proof. |
| changed workflows and role templates | Phase B | Preserve activation/routing/answer/provenance behavior; no reconstruction from chat or older modes. |
| adapter persistent sources and installed workflow copies | Phase B | Re-sync any Phase B canonical edit in the same Candidate; Phase A parity is the baseline. |
| `tools/tfw_state.py`, `docs/scripts/command_entry_eval.py` | Phase B only if an actual reader change requires it | Preserve Phase A current/legacy status and event behavior; avoid test-only churn. |

---

*TS — TFW_20260920-223357_FRATS / Phase A: Explicit Coordination, GATEWAY and Session Identity | 2026-09-21*
