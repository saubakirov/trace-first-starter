# HL — TFW-60 / Phase A: Task State & Coordination

> **Date**: 2026-08-26
> **Author**: Claude Code (Coordinator)
> **Status**: 📝 HL_DRAFT — awaiting owner review
> **Parent HL**: [HL-TFW-60](../HL-TFW-60__conflict_resistant_shared_workspace.md)
> **Master freeze**: `c1782b3` — baseline after amendments A1, A2, A3
> **Research**: [Iteration 1](../research/iter1/RES.md) · [Iteration 2](../research/iter2/RES.md) · [Iteration 3](../research/iter3/RES.md) — `SUFFICIENT`
> **Authority**: derivation-only. Vision, Target State, Phases, DoD, DoF and Principles exist once, in the master HL.
> **Knowledge Gate**: passed — 2 tasks since sequence 58, below the configured interval of 5.
> **Supersedes**: the 585-line draft of the same name, which specified a deterministic state engine, an
> identity subsystem and a Git topology matrix. Amendments A2 and A3 and research iteration 3 removed all
> three. This is a rewrite, not an edit.

---

## Phase Purpose

Normal task creation, selection and lifecycle transitions currently converge on the root `README.md` Task
Board. Phase A moves live state and management history into the task's own folder, so two tasks advancing
at the same time change different files. The root keeps a permanent route to a rebuildable portfolio view;
neither the root nor that view can outrank task-local truth.

Phase A ships the **mode-agnostic core**. Collaboration transport — Git or file synchronization — is a
declared project mode owned by a separate task under amendment A3.

## The Release in One View

```text
BEFORE — every lifecycle transition edits a shared root

Task A ─┐
Task B ─┼──> README.md Task Board      live authority AND portfolio view
Task C ─┘             ▲
                      └── one file, every writer, permanent contention


AFTER PHASE A — authority is local, the view is derived

README.md ──── permanent low-churn route
                      │
                      ▼
work/00-INDEX.md      derived · non-authoritative · rebuildable · may be stale
                      │
      select a task, then re-read its authority
                      ▼
work/<year>/<id>__<slug>/
  ├── status.md          current state, short and bounded
  ├── journal/           one file per event, immutable once written
  │     20260819-140312__created.md
  │     20260826-091500__handoff.md
  └── role artifacts     HL · RES · TS · ONB · RF · REVIEW · evidence

team/<handle>.md         who may act — humans and agents, one file each

tasks/                   legacy {prefix}-{seq} corpus, frozen, never renamed
  └── README.md          why this container still exists


Different tasks are different directories. Same-task roles write their own
artifacts. Two participants appending events create two different files, so
concurrent writes cannot collide on one byte range.
```

## Direct Answers to the Scope Questions

| Question | Phase A answer |
|---|---|
| Is a live Task Board needed in root `README.md`? | **No.** README becomes a stable route; the board is removed. |
| Where is the authoritative current state? | In the task's own short state file — not in HL, README, a marker filename or a folder location. |
| Is an on-demand-only view enough? | **No.** The index is persisted so a person can browse without knowing a command. It stays derived and disposable. |
| Where does coordination history live? | In the task's `journal/`, one file per event, carrying typed events and artifact references — not chat transcripts. |
| Who allocates event identifiers? | Nobody. The event's identifier **is** its filename, taken from the clock. There is no counter to read and no pointer to synchronize. |
| Does Phase A ship executable code? | **Only where an agent cannot be reliable:** deterministic index generation and migration accounting. State transitions and journal appends are ordinary file writes performed by the existing lifecycle skills. |
| Is there a mandatory mutation interface or state engine? | **No.** Removed by research iteration 3. A framework that stops working when a runtime is absent is not the product being built. |
| Is a single-writer gate required? | **No.** One file per event removes the contention a single-writer rule existed to prevent. |
| How is a task identifier allocated? | From the clock, never from a project-wide maximum — master HL DoD 18, amendment A1. Exact grammar is a TS decision. |
| Where do tasks live? | Under a configured container path, nested by creation year. Default `tasks/` for a new project; this repository uses `work/` so the legacy corpus keeps `tasks/`. |
| Can a task folder move between years or states? | **No.** The year is the year of creation and never changes. No lifecycle state is expressed by moving a directory. |
| What happens to existing `{prefix}-{seq}` tasks? | Nothing. They are not renamed, moved or reorganized. Both grammars remain readable. |
| Who is acting in this session? | A participant profile in `team/`. One profile is used silently; several mean a private-device binding; anything ambiguous asks one short question and never guesses from an OS username or hostname. |
| Is that authentication? | **No.** It is declared attribution and provenance. |
| Is there a device registry or device identifier? | **No.** Removed by research iteration 3: the draft conceded it authorizes nothing, travels with a copied profile and cannot be detected reliably. |
| Does Phase A decide Git versus file synchronization? | **No.** Amendment A3 moved transport rules to the mode task. |
| Does Phase A solve root `TECH_DEBT.md` or `KNOWLEDGE.md` contention? | **No.** Phases B and C, in that order. |

## What Phase A Delivers

| Release surface | Concrete result |
|---|---|
| Task container | Configured relative container path, nested by immutable creation year; stable paths through `DONE` and `REJECTED` |
| Task identity | Clock-derived identifier requiring no project-wide read; both new and legacy grammars readable |
| Task state | Short bounded state file: identity, goal and value summaries, lifecycle, current owner, continuation or terminal facts |
| Coordination record | `journal/` with one immutable file per event, a closed event vocabulary, references instead of copied prose, and a finite entry-length ceiling |
| Participants | `team/<handle>.md`, one profile per participant with an explicit `human` or `agent` type; private-device binding stays off the shared tree |
| Portfolio discovery | Permanent README route plus a persisted, deterministically generated index pinned to the top of the container listing |
| Different-task concurrency | Disjoint task-local writes; no root edit on a normal transition |
| Same-task coordination | Role artifacts stay role-owned; events are additive files, so concurrent appends cannot conflict |
| Lifecycle integration | Task creation, planning, research, handoff, review, resume, rejection and release read task-local state instead of a live root table |
| Legacy compatibility | Exact accounting of the existing corpus; nothing renamed, moved or invented; unresolved and malformed entries stay visible and non-actionable |
| Migration surface | `CHANGELOG` entry, migration guidance describing the container choice as one configuration value, and a `tasks/README.md` explaining why a second container exists |
| Framework release | Canonical rules, configuration, templates, adapters, Quick Start and documentation generation describe the shipped model; version becomes `2.0.0` under the `RELEASE.md` MAJOR rule |

## Where Executable Code Is and Is Not

Research iteration 3 refuted "no code at all" and confirmed "no state engine". The line falls here:

| Operation | Performed by | Why |
|---|---|---|
| Create a task, write state, append an event | Existing lifecycle skills, as ordinary file writes | The carrier grammar removes every operation that needed an implementation: no identifier allocation, no cross-file transaction, no chain verification |
| Generate the index across the whole corpus | Deterministic code | Reproducible aggregation over a hundred-plus directories is not something an agent does reliably |
| Account for the legacy corpus during migration | Deterministic code | Exact accounting with zero invented facts is a counting problem, not a judgement problem |

No component may be required for a task to be read or advanced. If index generation is unavailable, the
task is still authoritative and still workable; discovery degrades and says so. This boundary is what
distinguishes a framework from a runtime, and `.tfw/README.md` NS3 names a runtime as a non-goal.

## The Journal

One file per event, named from the clock, written once and never rewritten. A correction is a new event.

```text
work/2026/20260819-140312__conflict_resistant_shared_workspace/journal/
├── 20260819-140312__created.md
├── 20260826-091500__handoff.md
└── 20260826-164500__transition.md
```

An event records its time, kind, actor, the state change it caused, at least one reference to a canonical
artifact, and at most one bounded summary. Event content never copies HL, RES, RF, REVIEW, evidence or
chat bodies.

The closed vocabulary is `created`, `dispatch`, `handoff`, `transition` (blockage and resumption are typed
transitions), `ownership_changed`, `amendment_escalated`, and `consolidation` reserved for later phases.

**Entry length has a finite ceiling checkable by eye.** Content that exceeds it moves into an artifact and
the entry keeps a reference. The ceiling is fixed on measurement; the iteration-1 fixture value of 240
code points carries no privileged status. This is the single control that stops the journal becoming the
next README, and it is the reason the journal is a separate component rather than an HL section.

## Migration Boundary

Migration runs against an isolated copy or a manifest before any project write, and it accounts for the
measured corpus exactly:

```text
60 board rows + 51 task directories = 111 source occurrences
                                └──> 60 logical task identities
                                     51 matched
                                      9 board-only
                                      0 directory-only
                                      0 duplicate identities
```

Legacy directories keep their paths, their bytes and their identifiers. Proposals without an HL, broken
links, phase-case variants and rejected traces survive as they are. Task state is created only from
verified facts; a missing goal, value, owner, lifecycle or terminal fact is not invented. Entries that
cannot be resolved stay discoverable and non-actionable with a stable diagnostic.

The 7,051 references across 653 files and the 249 commit subjects in immutable history are the reason
nothing is renamed. Preserving them is not conservatism; a trace that needs a translation table to be
read has already lost the property the framework exists to provide.

## Explicitly Not in Phase A

- a deterministic state engine, a mandatory mutation interface, a required runtime, a daemon, an MCP
  server or any component whose absence stops a task from being read or advanced;
- schema files, sealed journal segments, digest chains, rollover machinery, monotonic event counters or a
  pointer field duplicating a journal fact;
- a device registry, a device instance identifier or an observed-instance report;
- a session-name gate as a structural requirement;
- transport rules for Git or file synchronization, topology matrices, landing protocols, manifests or
  machine-local path profiles — amendment A3 moved these to the mode task;
- renaming, moving or reorganizing any existing task directory;
- moving a task between year folders or expressing lifecycle state by moving a directory;
- task-local debt capture or removal of root `TECH_DEBT.md` — Phase B;
- task-local knowledge staging or redesign of `KNOWLEDGE.md` and `knowledge/` — Phase C;
- implementation or re-planning of TFW-54, and implementation of TFW-57;
- copying chat or artifact bodies into the journal;
- evidence-free numerical defaults for any ceiling;
- resolving the adapter duplication: byte copies are excluded from budget accounting by recorded owner
  ruling (S32), and neither references nor a generator will replace them (S33).

## Decisions Left to the Phase A TS

The architecture is closed by the master contract and three research iterations. The TS makes bounded
delivery decisions without reopening eliminated alternatives:

1. Exact file, new-file, modified-file and LOC census against the configured `30 / 15 / 30 / 3000`
   budgets, counting originals only per S32. The owner has ruled that Phase A may exceed the budget rather
   than split (S42); DoF 12 makes that ruling valid only against exact counts, so the census is a TS
   deliverable and returns to the owner if it departs materially from the ~51-original estimate.
2. Exact identifier grammar satisfying DoD 18. `YYYYMMDD-HHMMSS__slug` is the owner's selection; the TS
   fixes character set, collision behaviour and the legacy-compatibility reader.
3. Exact fields and bounds of the task state file, and its format. It must stay short enough to read at a
   glance and closed enough to parse without ambiguity.
4. Exact event filename grammar and the measured journal entry-length ceiling, with the measurement
   recorded.
5. Exact `team/` profile grammar and the session participant-resolution steps, preserving the declared
   attribution boundary and the one-question fallback.
6. Exact container configuration key, its default, and the migration guidance presenting the container
   choice as one setting rather than two supported layouts (S39).
7. Exact index generator interface and its degraded-state reporting, kept independent of task state
   writes.
8. Exact compatibility output for board-only, malformed and unresolved legacy inputs.
9. Which retired debt is closed in the same release: TD-81 and TD-177 die with the Task Board.

The TS may not restore a live root authority, make the derived index authoritative, move active task
paths, require a service or runtime, reintroduce an identifier counter, or absorb Phase B or C.

## Source Authority

| Source | What Phase A inherits |
|---|---|
| [Master HL](../HL-TFW-60__conflict_resistant_shared_workspace.md) at `c1782b3` | Frozen Vision, Phase A declared outcome, DoD including item 18, DoF, principles, and amendments A1–A3 |
| [RES iteration 1](../research/iter1/RES.md) | Elimination of live README authority, on-demand-only discovery, status markers, unbounded Markdown control and combined status/history |
| [RES iteration 2](../research/iter2/RES.md) | The authority/projection/journal separation, exact corpus census and the evidence-class discipline |
| [RES iteration 3](../research/iter3/RES.md) | Removal of the state engine and identity subsystem; the carrier-before-mechanism finding; the Git primary-source result behind A2 |
| [`.tfw/README.md`](../../../.tfw/README.md) NS1–NS3 | Purposeful human-governed continuity, selected traces, assurance proportional to risk, and runtime named as a non-goal |
| [`KNOWLEDGE.md`](../../../KNOWLEDGE.md) D24, D31, D50, D59, D63, D65 | No scripts as sync engine, filesystem state, locality, claim boundaries, derivation-only Phase HL, retained rejected traces |
| [`RELEASE.md`](../../../RELEASE.md) | MAJOR bump rule: status flow changed and a required file removed |

Evidence obligations are the master HL's, not this file's: §5 as amended by A1 and A2, and §7.1. Two
observations research recorded as unmet belong to [TFW-61](../../TFW-61__collaboration_transport_modes/PROPOSAL__TFW-61__collaboration_transport_modes.md),
not here: a genuinely non-technical participant, and any real-provider transport claim. Phase A must say
so in its RF rather than let silence read as coverage.

## Phase-Local Risks

| Risk | Control carried into TS and evidence |
|---|---|
| The derived index is mistaken for truth | Declared authority, source count and freshness, acting readers re-read task state, and fixtures for absent, stale and malformed conditions |
| The journal becomes the next README | Finite measured entry ceiling, closed vocabulary, references rather than copied prose, and immutability once written |
| Two containers become unexplainable | `tasks/README.md`, CHANGELOG entry and migration guidance ship in this phase, not later |
| Someone tidies a task into a different year folder | The year is a prohibition, not a convention (S37); lifecycle never moves a directory |
| The short state file drifts back toward prose | Closed field set with bounds; the phase adds no free-text field that invites explanation |
| Migration invents facts to look clean | Exact accounting, verified facts only, byte and path preservation, visible non-actionable unresolved entries |
| Phase A exceeds the configured budget | Exact census of originals before the TS; releasable split or an evidenced owner ruling, never silent omission of adapters, docs or migration |
| A non-technical participant cannot use the result | Design control only: the field set stays small, closed and bounded. **Phase A asserts readability as intent and does not claim it as observed** — the observation moves to [TFW-61](../../TFW-61__collaboration_transport_modes/PROPOSAL__TFW-61__collaboration_transport_modes.md), where that participant actually appears (S43). NS3 forbids an untested claim of comprehension, so the RF must state the gap rather than imply coverage |
| Phase A is called releasable while its budget overrun is unmeasured | The owner ruled the overrun acceptable (S42), and DoF 12 makes that ruling valid only against exact counts; the TS carries the census and returns to the owner if it departs materially from the estimate |

---

*HL — TFW-60 / Phase A: Task State & Coordination | 2026-08-26*
