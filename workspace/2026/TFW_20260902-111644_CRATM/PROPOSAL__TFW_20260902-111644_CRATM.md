# PROPOSAL — TFW_20260902-111644_CRATM: Contextual Roles and Agent Team Mode

> **Date**: 2026-09-02
> **Author**: saubakirov via Codex Coordinator
> **Status**: 📋 PROPOSAL — not chartered; start with `/tfw-plan`
> **Abbreviation**: CRATM
> **Historical source**: [`TFW-54`](../../../tasks/TFW-54__agent_team_mode/PROPOSAL__TFW-54__agent_team_mode.md), read-only
> **Current field source for role semantics**: [`FA15ES`](../TFW_20260830-202031_FA15ES/HL-TFW_20260830-202031_FA15ES.md), reference only

---

## 1. Why a successor task exists

TFW-54 contains substantial planning for an Agent Team execution mode, named agent principals, a frozen per-task routing table, whole-workflow delegation, and cross-session Git safety. It also has a 624-line draft HL written against an earlier TFW state.

That historical task is now a sealed source. It must not be reopened, normalized, renamed, or updated in place. Several premises also changed after it was drafted:

- TFW-60 shipped task-local `status.md`, immutable journals, `team/`, external machine bindings, and collision-resistant task/event identities;
- the owner reversed TFW-54's earlier no-journal direction, and `dispatch` is now a declared journal event;
- the `actor` field was removed from new events until a task defines a meaningful named agent principal;
- TFW 2.1.0 removed the live root debt registry, so old deliverables that edit `TECH_DEBT.md` are obsolete;
- the Project North Star now defines workflows and implementations as condition-specific realizations of the methodology;
- current Codex task/thread capabilities are not the same environment the 2026-08-08 proposal assumed;
- Assisted 1.6 provides a field-tested distinction between organization role, project role, task owner, current participant, and AI task role.

This proposal creates one current place to re-plan the still-valid design without rewriting its provenance.

## 2. The problem now

Full TFW has the structural substrate for participants but stops one step before a working team model.

| Gap | Current Full state | Consequence |
|---|---|---|
| Human role context | `team/{handle}.md` has exactly `handle`, `name`, `type`, `since`; roles live only in prose in `team/README.md` | agents cannot reliably use organization or project role as structured context |
| Project-dependent role | profiles are project-local, but the schema carries no project role | the same person can correctly differ between projects only in prose |
| Agent participant | `type: agent` is admitted but deliberately usable by nothing | provider names and sessions cannot become accountable participants |
| Writer identity | events record human `on_behalf_of` and technology `via`; new events have no `actor` | two named agents cannot be distinguished as writers without inventing per-session identities |
| Task routing | no canonical per-task Role Assignment exists | participants cannot discover who coordinates, researches, executes, reviews, or receives their report from the HL |
| Delegated mode | CL and AG do not express a coordinator running several visible role sessions under one frozen HL | the owner must continue routing and answering workflow boundaries manually |
| Parallel trace safety | multiple sessions share one working tree and Git index; explicit-path staging and landing ownership are not canonical TFW rules | a correct task can be committed under the wrong task or absorb a sibling's staged changes |

The task is not merely “add two role fields.” Profile context, workflow assignment, writer attribution, authority, and provider provenance answer different questions. A useful design must keep them separate.

## 3. Proposed conceptual model

### 3.1 Four layers, four jobs

| Layer | Question | Candidate carrier | Must not become |
|---|---|---|---|
| Participant identity | Who does this stable handle name? | project-local `team/{handle}.md` | authentication or permission grant |
| Contextual role | What is this participant's organizational and project context here? | structured profile fields | workflow authority or an immutable historical claim |
| Task assignment | Who holds Coordinator, Researcher, Executor, and Reviewer for this task or phase? | frozen Role Assignment in the task HL | a global capability ranking or vendor policy |
| Durable write | Who performed this write, for whom, and through what tool? | event identity fields | filename uniqueness or session registry |

The same human may have different project roles because each project owns its own `team/` profile. The same named agent may also receive different workflow assignments in different tasks. Neither fact changes the Role Lock of the workflow it is executing.

### 3.2 Candidate profile extension

The first HL should decide whether the new fields are required or optional and how existing profiles migrate. The smallest candidate is flat and readable:

```yaml
---
handle: saubakirov
name: Sanzhar Aubakirov
type: human
since: 2026-08-27
organization_role: founder
project_role: methodology owner
---
```

Rules carried into planning:

1. `organization_role` and `project_role` are declared descriptive context, not authorization.
2. The external machine binding still selects only a handle. It never stores or overrides roles.
3. A participant may have different values in different projects without receiving a new global identity.
4. `unknown` and `not-applicable` need explicit semantics if admitted; blank strings must not silently mean both.
5. A separate `team_role` is added only if research proves that a project team is a distinct scope rather than another name for project role.
6. Historical events do not copy current profile roles. If role-at-time matters, it needs an explicit history design rather than pretending mutable profile text is historical evidence.

### 3.3 Human and agent profiles share a container, not necessarily every rule

The container remains `team/`. A provider family such as Codex or Claude is not a participant, and a session is not a durable principal. A future agent profile must name a stable principal that can be assigned, delegated to, and held inside an accountability chain.

The transferred TFW-54 constraints remain:

- never create one profile per session or per event;
- keep event filename uniqueness in the opaque token, not in identity;
- keep `via` as descriptive tool/provider provenance;
- keep human accountability resolvable even when agents launch other agents;
- a name grants no permission; Role Locks and the frozen contract grant the bounded work;
- offline name collision is a declared limitation, not an authentication guarantee.

Whether a new-event `actor` field returns, and whether it names both human and agent writers, is an open design question. The answer must compose with immutable legacy events that already carry an old tolerated `actor` field.

### 3.4 Role Assignment and Agent Team mode

The strongest surviving TFW-54 idea is a per-task routing contract inside the HL because every TFW role already reads that artifact.

Candidate shape:

```markdown
### Role Assignment 🔒 FROZEN

| Workflow role | Scope | Participant | Reports to | Channel |
|---|---|---|---|---|
| Coordinator | all | <team handle> | owner | current task |
| Researcher | all | <team handle> | coordinator | visible task/thread |
| Executor | phase-a | <team handle> | coordinator | visible task/thread |
| Reviewer | phase-a | <team handle> | coordinator | separate visible task/thread |
```

The table names participants, not vendors. Model and tool selection may be operational data, but it must not redefine what the assigned role is allowed to do. A row is likely a frozen claim; substitution should be explicit and traceable rather than silent.

The future HL must re-evaluate the working name `AT`, because a routing table, named participants, and structured contextual roles may describe a broader team model than a third execution-mode label alone.

### 3.5 Delegation uses current task-local coordination

The old draft said the workflow artifact itself was the dispatch record and rejected a journal record. That premise is superseded. Current TFW already declares `kind: dispatch`, whose single job is to record that work was handed to a named participant.

Planning should therefore test this minimal chain:

```text
frozen HL + Role Assignment
          ↓
task-local dispatch event → named participant + workflow + scoped refs
          ↓
role artifact (RES / ONB+RF / REVIEW)
          ↓
coordinator receives outcome and decides the next declared transition
```

Whole-workflow delegation remains the safe default because it has a role-owned artifact and a clear completion condition. The new task should not prohibit smaller coordination acts merely to preserve an old conclusion; it should determine whether `dispatch` plus scoped references already makes them inspectable.

Visible, addressable tasks/threads remain part of the owner's value. Tool-specific creation, waiting, messaging, and fallback mechanics belong in adapters or execution guidance, not in the methodology's vendor-neutral definition.

### 3.6 Shared-workspace trace integrity

The successor retains the two measured failures from TFW-54:

- broad staging can absorb another task's already-staged changes;
- a coordinator can land another session's deliverable under the wrong task subject.

The future HL should test and, if still absent, require:

1. stage only exact approved paths; no broad add or commit-all form;
2. audit the cached diff before every commit;
3. never commit a sibling task's hunk merely because it is already staged;
4. land a cross-session deliverable in its own task-attributed commit;
5. preserve unrelated dirty work and report overlap rather than normalizing it;
6. keep task ownership, acting role, accountable human, named writer, and tool provenance as separate facts.

This proposal does not assume one transport. Git versus file synchronization remains the subject of TFW-61.

## 4. Transfer ledger from sealed TFW-54

| Historical item | Successor disposition | Reason |
|---|---|---|
| owner approves a multi-phase HL and delegates the run | carry | core value remains |
| frozen per-task Role Assignment | carry and re-evaluate columns | self-carrying routing remains structurally strong |
| permissions are per role, never per agent | carry | prevents self-extending grants |
| named stable agent principal, never provider or session | carry | still required before meaningful writer attribution |
| `on_behalf_of` chain resolves to a human | carry as hypothesis | must compose with current journal grammar |
| event filename token is not identity | carry as fixed boundary | current TFW already ships this correction |
| whole-workflow delegation only | challenge | `dispatch` now exists and may safely support narrower scoped handoffs |
| no dispatch journal | retire | owner reversed it; current journal has `dispatch` |
| graceful degradation to subagents or one session | challenge | it may destroy the visibility and addressability that justify the mode |
| unavailable assigned participant always waits for owner | carry as hypothesis | amendment cost versus safe substitution needs current evidence |
| explicit-path staging and task-correct landing commit | carry | measured failures remain relevant |
| edit `TECH_DEBT.md` to close TD-144/TD-178 | retire | the live registry was removed in TFW 2.1.0; historical snapshot is immutable |
| ship as framework version 1.3.0 | retire | current version is 2.1.0; release scope belongs to a later approved HL |
| TFW-45 swarm boundary | carry | stage-level subagents and cross-workflow participants remain distinct |
| revision-agent freshness | keep external | TFW-58 owns revision-loop semantics |
| collaboration transport | keep external | TFW-61 owns Git versus file-sync mode |

## 5. New contribution from Assisted role practice

Assisted 1.6 distinguishes five facts: current participant, organization role, project role, immutable task owner, and AI task role. The implementations are independent, so this is evidence rather than a schema to copy.

The useful transfer is the distinction itself:

- a participant's contextual role is not the task owner;
- an organizational title is not the role played in this project;
- an AI's workflow role is not its provider, profile type, or permission set;
- changing the current participant does not rewrite the owner of an existing task;
- device-local selection binds a project to a participant, not to that participant's current roles.

These distinctions should be tested against Full's status, journal, Role Lock, profile, and binding carriers before the successor HL selects field names or cardinality.

## 6. Proposed scope for `/tfw-plan`

The next planning cycle should own one coherent Full TFW design:

1. structured organization/project role context in `team/` profiles;
2. backward-compatible migration for existing four-key human profiles;
3. the named-agent principal and lifecycle needed to activate `type: agent`;
4. durable writer attribution without reusing the filename token or provider field;
5. a frozen per-task Role Assignment and its amendment/substitution semantics;
6. coordinator-to-participant dispatch through current task-local journals;
7. an Agent Team execution contract bounded by the approved HL and Role Locks;
8. exact-path staging and task-correct landing rules for concurrent sessions;
9. adapters, validation, migration, glossary, documentation, and release consequences implied by the chosen design.

The scope must be split into phases if the current 50-file / 5,000-line phase budget would be exceeded. No implementation begins from this proposal.

## 7. Explicitly outside this proposal

- any edit to sealed `tasks/TFW-54__agent_team_mode/` or its status;
- any edit to Assisted, FA15ES, or the independent Assisted identity implementation;
- unification of Full and Assisted profile or binding schemas;
- an agent runtime, daemon, scheduler, lock server, database, or provider API inside TFW;
- permissions or authentication derived from profile roles;
- one agent profile per session, model, provider family, or event;
- transport-mode design owned by TFW-61;
- revision-loop design owned by TFW-58;
- thawing TFW-45 or merging its stage-level swarm into this task;
- automatic fallback that silently changes a frozen assignment;
- implementation, version bump, or changelog entry before an approved HL and TS.

## 8. Open hypotheses

| # | Hypothesis |
|---|---|
| H1 | Optional `organization_role` and `project_role` fields add useful structured context without forcing a breaking migration of existing Full profiles |
| H2 | A stable named agent principal can be defined without confusing a provider, model, persona, session, process, or human-accountable owner |
| H3 | A new-event writer field can name that principal while legacy `actor` remains readable and the opaque filename token remains identity-free |
| H4 | A frozen Role Assignment plus task-local `dispatch` events is sufficient to orient and audit delegated role work without a new artifact class |
| H5 | Whole-workflow delegation is a safe default but need not be an absolute prohibition once a dispatch event carries explicit scope and references |
| H6 | Visible peer tasks, subagents, and single-session sequencing can share one behavioral contract without falsely promising equal visibility, independence, or control |
| H7 | Structured participant roles remain descriptive context and never become an implicit authorization or a substitute for Role Locks |
| H8 | Exact-path staging and task-correct landing rules materially reduce cross-session trace corruption without requiring a new coordination runtime |

## 9. Research triggers

The eventual HL should recommend focused research because four decisions can reshape the architecture:

1. **Identity ontology:** compare human, automation, agent principal, provider, model, persona, session, writer, accountable owner, and workflow role; eliminate overloaded fields.
2. **Migration:** test optional versus required role fields on current profiles and update scenarios without rewriting historical events.
3. **Coordination replay:** replay TFW-48/49 and current multi-task Codex work against Role Assignment, dispatch, amendments, and exact-path staging.
4. **Capability reality:** verify current addressable-task, waiting, interruption, visibility, and fallback behavior in the supported tools; keep mechanism-specific facts in adapters.
5. **Boundary challenge:** test TFW-45, TFW-58, and TFW-61 overlaps so the successor owns no second swarm, revision protocol, or transport model.

## 10. Dependencies and sources

| Source or dependency | Status | Use |
|---|---|---|
| [Project North Star](../../../.tfw/README.md#ns1) | ✅ current | purpose, principles, proportional assurance, human authority |
| [TFW-53](../../../tasks/TFW-53__hl_contract_and_goal_defence/HL-TFW-53__hl_contract_and_goal_defence.md) | ✅ complete | frozen contract, amendments, delegated-authority ceiling, Purpose Check |
| [TFW-60](../../../tasks/TFW-60__conflict_resistant_shared_workspace/HL-TFW-60__conflict_resistant_shared_workspace.md) | ✅ substrate shipped | task-local state, journal, profiles, bindings, actor deferral, dispatch vocabulary |
| [TFW-54 proposal](../../../tasks/TFW-54__agent_team_mode/PROPOSAL__TFW-54__agent_team_mode.md) | 🔒 read-only history | original owner intent, topology, identity and delegation hypotheses |
| [TFW-54 draft HL](../../../tasks/TFW-54__agent_team_mode/HL-TFW-54__agent_team_mode.md) | 🔒 read-only history | refined design, field measurements, obsolete assumptions to classify |
| [TFW-45](../../../tasks/TFW-45__multi_agent_workflows/PROPOSAL__TFW-45__review_swarm_consolidator.md) | ❄️ frozen | stage-level swarm boundary only |
| [TFW-58](../../../tasks/TFW-58__revise_protocol/PROPOSAL__TFW-58__revise_protocol.md) | proposal | revision-loop boundary |
| [TFW-61](../../../tasks/TFW-61__collaboration_transport_modes/PROPOSAL__TFW-61__collaboration_transport_modes.md) | proposal | collaboration-transport boundary |
| [Full team profile template](../../../.tfw/templates/team/profile.md) | ✅ current | current closed four-key schema and agent deferral |
| [FA15ES HL](../TFW_20260830-202031_FA15ES/HL-TFW_20260830-202031_FA15ES.md) | 🔒 independent task | Assisted role distinctions as field evidence, never implementation authority |

## 11. Strategic insights

| # | Insight | Source |
|---|---|---|
| S1 | The user's desired outcome is still the strong form: approve the contract and return to a finished result, not merely reduce how often gates are shown | transferred from TFW-54 |
| S2 | Agents are not interchangeable across workflow roles; assignment is a quality decision, while permissions remain role-defined | transferred from TFW-54 |
| S3 | Per-session visibility, messaging, interruption, and independent addressability are part of the value and cannot be silently replaced by opaque subagents | transferred from TFW-54 and FA15ES planning |
| S4 | `team/` and `workspace/` are useful common terms across TFW realizations, but a shared noun does not make their technical schemas identical | owner, FA15ES correction 2026-09-02 |
| S5 | Organization role and project role are different dimensions. Project-local profiles naturally let one person carry different project roles in different repositories | owner, 2026-09-02; Assisted 1.6 field model |
| S6 | Roles describe context. Authority still comes from the human owner, frozen contract, explicit assignment, and Role Lock | synthesis from Project North Star and owner correction |
| S7 | The historical proposal is valuable evidence but not current authority. Carrying it means classifying each claim, not copying obsolete premises into a new HL | owner request 2026-09-02 |

## 12. Next decision

Run `/tfw-plan` on this task. The coordinator should use this proposal as input, verify the current carriers and tool capabilities, present an updated finished-state visualization, and ask the owner to approve a new HL contract. Nothing in this proposal authorizes implementation.

---

*PROPOSAL — TFW_20260902-111644_CRATM: Contextual Roles and Agent Team Mode | 2026-09-02*
