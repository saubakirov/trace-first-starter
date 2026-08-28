# PROPOSAL — TFW-54: AT (Agent Team) Execution Mode

> **Date**: 2026-08-08
> **Author**: Coordinator (Claude Code)
> **Status**: ⬜ TODO — proposal only. No HL, no TS. Entry point: `/tfw-plan`.
> **Blocked by**: [TFW-53](../TFW-53__hl_contract_and_goal_defence/HL-TFW-53__hl_contract_and_goal_defence.md) Phase C

---

## Why this is a separate task

Split out of TFW-53 by owner decision, 2026-08-08:

> *«они связаны и 53 как бы фундамент для 54. но делать их вместе значит раздуть фокус координатора, что скажется на качестве планирования и координации»*

TFW-53 makes goals immovable and gives them a defender. Delegation is what that makes possible — but planning both at once splits coordinator attention across two problem domains, which is the condition that degraded planning quality in TFW-48/49. Sequencing is deliberate: fundament first, building second.

This file preserves the design work already done inside TFW-53 planning so it is not lost. It is not a plan.

## The problem

TFW has two execution modes and no room between them.

| Mode | Defined in | Scope of autonomy |
|------|-----------|-------------------|
| CL (Chat Loop) | `conventions.md` §7 | Default. AI proposes, human approves and executes |
| AG (Autonomous) | `conventions.md` §7 | "Explicit request only. AI works within approved **TS** scope" |
| — | — | Nothing where a coordinator runs a team within an approved **HL** |

AG is bounded by a TS, which is downstream of research. So there is no legitimate way to say "you are free from here" at the moment the owner wants to say it: at HL approval.

The interaction cost meanwhile is high. One research iteration passes through roughly ten blocking gates across `plan.md` and `research/base.md`. The owner's position is neither "approve every step" nor "let it wander", and the framework offers only those two.

## The owner's design: the routing contract lives in the HL

Added 2026-08-10. This changes the shape of the task and is the single most important idea in this file.

> *«Координатор при создании HL и выборе режима может сделать себе небольшой контракт в HL, где будет написано кто кем как управляет. Чтобы все агенты, читая его, понимали кому отчитываются, что ожидают. Ведь каждый из них так или иначе обязан читать парент HL.»*

The original framing put the mode in `conventions.md` §7 — a global setting. The owner's version puts a **per-task routing table in the HL**, and it is strictly better for one structural reason: **the HL is the one artifact every role is already required to read.** Researcher, executor and reviewer all load the parent HL in their context-loading step. A routing table there is self-carrying — no role has to be told where to look, and no separate mechanism has to deliver it.

Sketch, to be designed properly in the HL for this task:

```
## Role Assignment
| Role        | Agent  | Reports to  | Channel        |
|-------------|--------|-------------|----------------|
| Coordinator | Claude | owner       | this session   |
| Researcher  | Codex  | coordinator | thread         |
| Executor    | Codex  | coordinator | thread         |
| Reviewer    | Claude | coordinator | spawned + wait |
```

Why this composes well with TFW-53:

- It is **contract-shaped**. Who holds which role is exactly the kind of claim that should not drift mid-task, so it likely belongs inside the frozen set — or in a declared adjacent block with the same amendment discipline.
- It makes the **dispatch record** (below) partly redundant at declaration time: the table says who *should* have done what; the record says who *did*.
- It is **tool-agnostic by construction**: the table names roles, agents and channels. What a "channel" is differs per tool and the table does not care.

Open design questions this raises:

| # | Question |
|---|----------|
| 1 | Is the routing table inside the frozen contract, or free-but-logged? Changing the reviewer mid-task is a real event that should be visible |
| 2 | Does it belong in `templates/HL.md` as its own section, or in the header block beside the contract state? |
| 3 | What happens when the declared agent is unavailable — does the task stall, or does the coordinator substitute and log it? |
| 4 | Does a role's *identity* change what that role is permitted to do? It must not — role locks are per role, never per agent |
| 5 | **What is an "agent" in the Agent column — a provider or a named instance?** See below; the table above answers "provider", and that answer does not survive two coordinators on the same provider |

## Agent identity: a provider is not an actor

> **Added 2026-08-26** by owner decision during TFW-60 Phase A review. This section consumes the
> `team/` substrate TFW-60 Phase A ships and must not invent a second one.

The Role Assignment table above writes `Claude` and `Codex` in the Agent column. That is a **provider**,
not an actor, and the distinction is load-bearing the moment two sessions of the same provider act at
once:

```text
two Claude coordinators, both acting for the owner, both write an event in the same second

by provider     20260826-232000__handoff__claude.md
                20260826-232000__handoff__claude.md     ← same name, one event is lost

by actor name   20260826-232000__handoff__atlas.md
                20260826-232000__handoff__beacon.md     ← distinct, both survive
```

TFW-60 Phase A therefore records three separate facts on every durable write, and AT inherits all three:

| Field | Answers | Value space |
|---|---|---|
| `on_behalf_of` | who is accountable | a human handle. *Whoever launched it, answers for it* |
| `via` | what technology produced it | provider family — `claude`, `codex`, `gemini`; absent for a hand edit |
| ~~`actor`~~ | ~~who performed it~~ | **does not exist yet — AT is what creates it.** See below |

> **Revised 2026-08-28, and the revision is the point.** Phase A shipped a third field, `actor`, requiring
> a declared `team/` handle. It had no job of its own: in a single-writer project it duplicated
> `on_behalf_of` — 21 consecutive events in the upstream repository carry the same value in both — and in
> a multi-session project it duplicated `via` plus a session number. It was also given a second,
> unrelated job as the filename's uniqueness component, and **those two jobs are what collided**: two
> external projects minted a `team/` profile per Claude session because the filename rule demanded a
> distinct writer, and the identity rule then demanded a profile for it. One of them deleted the profiles
> afterwards and its build gate is red permanently, because events are immutable and profiles are not.
>
> `actor` is therefore **removed until this task**. Phase AA ships two identity fields and an opaque
> write token that is deliberately not an identity, needs no profile and is validated against nothing.
> **AT is where a named actor finally has something to name**, so the field returns here, once, with the
> thing that makes it meaningful.

**What AT specifically owns, beyond what Phase A ships:**

1. **A coordinator agent needs a real name, and AT introduces the field that carries it.** Generated is
   fine; anonymous is not. It is registered as a `team/<name>.md` profile with `type: agent`, and it is
   **the same name across that agent's sessions** — a persona, never a per-run handle. The per-session
   profiles two projects created are the failure this task must not repeat: a participant directory that
   grows by one entry per launch is a session log wearing the wrong name.
   **The write token stays separate.** Uniqueness of an event filename is not an identity question and
   must not be solved by minting identities; AT adds a name for a writer that exists, and leaves the
   token doing the job it already does.
2. **A delegate acts under the coordinator's grant but keeps its own `actor`.** The role table assigns a
   role to a *named* agent, so the Agent column changes from `Claude` to a name and gains a provider
   column.
3. **`on_behalf_of` becomes a chain when agents launch agents.** Phase A's rule — accountability always
   resolves to a human — still holds; AT decides whether the record carries the whole chain or only its
   two ends. This is the case Phase A explicitly deferred.
4. **A name is not an authorization.** Question 4 above already settles it: role locks are per role,
   never per agent. A name identifies a writer and attributes a record; it grants nothing. Consistent
   with D59.
5. **Name allocation has the same weakness as every other identifier here.** A name is claimed by
   creating its `team/` profile and checked against the existing set, so two mutually offline agents can
   still pick one name. That is tolerable only because names are created once and reused across many
   sessions rather than allocated per run — and it must be written down as a limit, not left to be
   mistaken for a guarantee.

## Field data: agents are not interchangeable across roles

Owner assessment, 2026-08-10, from running both tools across many tasks:

| Role | Codex | Claude |
|------|-------|--------|
| Coordinator (planning) | ✗ weak | ✓ |
| Reviewer | ✗ weak | ✓ |
| Executor | ✓ strong | — |
| Researcher | ✓ strong | ✓ (both iterations of TFW-53) |

> *«Мне сейчас не нравится, как кодекс планирует, и ревью делает плохо, но исполнение и ресерч классно делает.»*

This is the *reason* the routing contract has value. If agents were interchangeable, a global mode would be enough; a per-task table only earns its place because the right assignment differs by role. It is also a constraint on the design: the framework must let a project express this **without** hard-coding vendor names into `.tfw/` — the table is filled per task, the vocabulary is not.

Capability asymmetry that shapes the topology:

- **Claude → Codex:** a Claude session can launch a Codex run and wait for the result. Synchronous, works today.
- **Codex ↔ Codex:** sessions communicate through threads; the owner can see, message and stop each one independently. Asynchronous, works today.
- **Claude ↔ Claude:** peer sessions cannot talk to each other. Only subagents, which are not peers.

So the reporting topology is not the same shape on every tool, and the routing table must express *who reports to whom* without assuming *how*.

## Proposed scope

A third execution mode — working name **AT (Agent Team)** — where a coordinator runs a team of separate agent sessions bounded by the frozen contract TFW-53 establishes.

1. **Mode definition** in `conventions.md` §7: when it applies (approved, committed contract only), what the coordinator owes the owner, what a delegate session owes the coordinator, what still forces escalation.
2. **Both delegation patterns**, in production use by the owner already:
   - (a) the owner creates delegate sessions and hands them to the coordinator;
   - (b) the coordinator creates its own sessions and instructs them to run `/tfw-handoff`, `/tfw-review`, `/tfw-research`.
3. **Bounded, non-self-extendable grant.** The AT grant names what is delegated and what is not. The coordinator may never widen its own mandate, and may not cite delegation as authority to accept a scope or budget overrun. TFW-53 lands the underlying rule; TFW-54 applies it to delegation.
4. **Dispatch record.** The coordinator logs each delegation — which session, which workflow, which scope — so an AT run is auditable afterwards.
5. **Tool-capability degradation.** Independent addressable sessions where a tool provides them; graceful fallback to subagents or single-session sequencing where it does not. A behavioural promise, not a mechanism promise (D54).
6. **Boundary against [TFW-45](../TFW-45__multi_agent_workflows/HL-TFW-45__multi_agent_workflows.md)** (❄️ FROZEN): AT is a session-level team across workflows; TFW-45 swarm is stage-level agents inside one workflow. Different granularity, must not blur vocabulary.

## Evidence base

This mode has been run once informally, in TFW-48/49, and it failed. Full forensics in [TFW-53 §2](../TFW-53__hl_contract_and_goal_defence/HL-TFW-53__hl_contract_and_goal_defence.md). The parts that constrain TFW-54's design:

| Finding | Constraint it imposes |
|---|---|
| The approved HL header carried a blanket grant — *"The user delegated format, phase, execution, review, and closure decisions to the Coordinator"* — and the coordinator later cited it to accept three scope-budget overruns (702 vs 700, 1708 vs the 1200 LOC signal, 3160 vs 2700), each recorded as "No material deviations" | The grant must be bounded and non-self-extendable, or it becomes the mechanism of failure rather than a control on it |
| The commit prefix was the only inter-session artifact. No handoff log, no dispatch record, no trace of what context each session received. The post-mortem was blind to what each session was told | Delegation without a dispatch record is unauditable, and its failures cannot be diagnosed afterwards |
| These were pre-existing long-lived Codex sessions; the owner relayed `/tfw-handoff` and `/tfw-review` into them. There is no evidence of programmatic spawning | The mode must describe a human-and-tool-mediated arrangement, not assume an API |
| 149 files and 27,103 lines reverted after six days | The cost of an unbounded AT run is measured, not hypothetical |

## Open hypotheses

Carried over from TFW-53 planning, renumbered.

| # | Hypothesis |
|---|-----------|
| H1 | The AT coordinator/delegate contract can be specified tool-agnostically and degrade gracefully to subagents or single-session sequencing without losing enforcement value |
| H2 | Session-level AT and stage-level TFW-45 swarm are genuinely orthogonal — both can exist without vocabulary collision or one absorbing the other |
| H3 | A dispatch record is sufficient for auditability; no per-message transcript of inter-session traffic is required |
| H4 | The contract TFW-53 ships is sufficient to bound an AT run — no additional constraint artifact is needed at delegation time |
| H5 | A per-task routing table in the HL is sufficient to orient every role, because every role already loads the parent HL — no separate delivery mechanism is needed |
| H6 | The routing table belongs inside the frozen contract: who holds which role is a claim that should not drift mid-task without a logged, ruled amendment |
| H7 | Role permissions must remain per *role* and never per *agent* — a routing table that lets a strong agent do more, or a weak one do less, reintroduces the self-extending grant that failed in TFW-49 |
| H8 | On a **revision round** a fresh agent beats the one that produced the artifact. Owner intuition, and the evidence pulls both ways: AFD-38's reviewer approved and then retracted only under owner pressure, but a fresh reviewer has not seen rev1's reasoning and re-litigates settled points. Test against AFD's 13 revision arcs before deciding ([TFW-58](../TFW-58__revise_protocol/PROPOSAL__TFW-58__revise_protocol.md) owns the loop itself) |

## Strategic insights carried over

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | Owner rejected a per-task autonomy parameter on capability grounds: full independent agent sessions are currently Codex-only; Claude Code can spawn subagents but not peers. A dial would promise portability the framework cannot honour | constraint | User, 2026-08-08 |
| S2 | Two delegation patterns are already in production use — owner-created sessions handed to the coordinator, and coordinator-created sessions instructed to run `/tfw-*` skills. The mode must support both; this is field practice, not speculation | process | User, 2026-08-08 |
| S3 | Per-session visibility and control is part of the value: *«я тоже могу их видеть, писать, управлять, останавливать отдельно друг от друга»*. Delegation without individual addressability is not what is being asked for | stakeholder | User, 2026-08-08 |
| S4 | Autonomy is earned by the contract, not granted by configuration: *«автономность и доверие должны быть, но только тогда, когда HL утвержден как vision»* | philosophy | User, 2026-08-08 |
| S5 | The routing contract belongs in the HL because the HL is the only artifact every role is already obliged to read. This is the same structural move as D31 (state where it cannot be missed) rather than a procedural one (tell each agent separately) | philosophy | User, 2026-08-10 |
| S6 | Agents are not interchangeable across roles, and the owner has measured which is which: Codex weak at planning and review, strong at execution and research; Claude strong at planning and review. Role assignment is a *quality* decision, not a convenience one — and it is the reason a per-task table beats a global mode | environment | User, 2026-08-10 |
| S7 | The reporting topology differs by tool and the framework must not assume one: Claude can launch Codex and wait; Codex sessions talk through threads with per-session owner visibility; Claude sessions cannot talk to each other at all. The table names who reports to whom, never how | constraint | User, 2026-08-10 |
| S8 | The routing table must survive a **revision round**, not just the first pass. Owner, 2026-08-13: *«существующие агенты склонны дрейфовать и переписываться друг с другом бесконечно, отдавая туда-сюда правки»*. Whether rev2 reuses the declared agent or spawns a fresh one is a property of the table, and it is the first place the per-task routing contract has to say something a global mode could not | process | User, 2026-08-13 |

## Prerequisite

Do not start before TFW-53 Phase C is complete. AT without a frozen contract and a goal-defending reviewer is TFW-48/49 repeated with better vocabulary.

Do not start before **TFW-60 Phase A** is released either. Phase A ships the `team/` profiles, the
`actor` / `on_behalf_of` / `via` fields and the task-local journal that AT writes into. TFW-60 master HL
§2.3 states the direction plainly: *"TFW-60 owns that substrate; TFW-54 will consume it rather than
invent a second one."* An AT built before that substrate exists will build its own, and the two will
drift.

---

*PROPOSAL — TFW-54: AT (Agent Team) Execution Mode | 2026-08-08*
