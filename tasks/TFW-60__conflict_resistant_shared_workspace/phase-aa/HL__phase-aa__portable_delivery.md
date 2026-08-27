# HL — TFW-60 / Phase AA: Portable Delivery

> **Date**: 2026-08-27
> **Author**: Claude Code (Coordinator)
> **Status**: 📝 HL_DRAFT — awaiting owner review
> **Parent HL**: [HL-TFW-60](../HL-TFW-60__conflict_resistant_shared_workspace.md)
> **Master freeze**: `2123de1` — baseline after amendment A4, which created this phase
> **Origin**: [FIELD-REPORT](../FIELD-REPORT__TFW-60__first_external_update.md) — `KZ-IT-telegram-list`, `1.3.0 → 2.0.0-dirty`, 2026-08-27
> **Authority**: derivation-only. Vision, Target State, Phases, DoD, DoF and Principles exist once, in the master HL.

---

## Phase Purpose

Phase A shipped a model that works. It did not ship a way to give that model to anyone else.

`2.0.0-dirty` was cut so the update path could be exercised before `2.0.0` was claimed. It was, once, and
the exercise reports its own ratio: *"the file copying took minutes; the rest of the session was
reconstructing what to do and in what order."* The update completed — and only because a person
hand-carried two scripts and a directory the payload does not contain, and reconstructed an order the
release states once, in a code fence, 150 lines into a CHANGELOG.

Phase AA closes the distance between *the framework works here* and *the framework can be handed over*.

## The Release in One View

```text
BEFORE — the payload boundary was never checked against the deliverable list

  /tfw-update carries ────────► .tfw/    rules · templates · workflows · adapters
                                           │
  Phase A's own deliverables               │  gen_index.py        ✖ outside
                                           │  migrate_board.py    ✖ outside
                                           │  team/README.md      ✖ outside
                                           │  a migration guide   ✖ does not exist
                                           ▼
  the receiving project gets rules that require tooling it was not given,
  and a CHANGELOG telling it to run a file it does not have


AFTER PHASE AA — everything the release asks for is either in the payload
                 or already in the receiving project

  .tfw/
   ├── scripts/            the tooling the rules require
   ├── migrations/2.0.0.md what to do, in what order, for a project that is not this one
   ├── templates/team_profile.md + a step that creates the acting profile
   └── workflows/update.md routes to the migration guide when the update crosses a major

  a board is found wherever the project keeps it
  a legacy directory the grammar does not match is reported as unresolved,
    never as "an idea that never became work"
  one command answers: is this project consistent with this release
```

## Direct Answers to the Scope Questions

| Question | Phase AA answer |
|---|---|
| Is Phase A reopened? | **No.** Its outcome — task-local state and coordination — is met and was approved over four review rounds. Delivering it elsewhere is a capability A never claimed. |
| Where does the tooling live? | Inside the payload. Exact path is a TS decision; `.tfw/scripts/` is the coordinator's recommendation. |
| Why not leave it in `docs/scripts/` and list it in the sync table? | Because `docs/` is documentation tooling and the receiving project may not have it at all — this consumer has `scripts/`. Placement followed proximity to `gen_docs.py`, not ownership. |
| May the tools keep resolving the project root by directory depth? | **No.** `parents[2]` makes the path load-bearing: a project that puts the tools anywhere else must edit `.tfw/` and forfeit clean updates. |
| Does a major release need a migration guide? | **Yes**, and its absence makes the release incomplete. Prose inside a CHANGELOG that documents *this repository's own* migration is not a procedure. |
| Must migration find a board it did not expect? | **Yes.** This consumer's board was at `tasks/README.md` under `## Board`, for a documented reason: its root `README.md` is fully regenerated. |
| What happens to a legacy directory the identifier grammar does not match? | It is reported as **unresolved**. Never as backlog, and never with a reason the source did not carry. |
| Is `team/` optional? | **No**, and nothing currently creates it. A project learned the profile was required because a framework test it was never told to run failed. |
| Is this repository admissible as the evidence fixture? | **No.** Every Phase A review round ran here, which is why none of this was found. At least one external project must complete the update untouched. |
| Does Phase AA change the task model? | **No.** No carrier, schema, vocabulary or lifecycle value changes. This phase is delivery. |
| Does it decide Git versus file synchronization? | **No.** Still [TFW-61](../../TFW-61__collaboration_transport_modes/PROPOSAL__TFW-61__collaboration_transport_modes.md). |

## What Phase AA Delivers

| Release surface | Concrete result | Closes |
|---|---|---|
| Payload completeness | Both scripts inside the payload, referenced by payload path, with root resolution that does not depend on depth | F1 |
| Participant delivery | A profile template in the payload plus an explicit step creating the acting profile before the first durable write | F7 |
| Migration guidance | A per-major migration guide, routed to from the update path; the ordering constraint stated where it is needed rather than buried | F2 |
| Board discovery | Migration locates a board wherever the project keeps it, and a refusal names the real cause | F3 |
| Honest classification | Directories outside the assumed grammar become `unresolved`; no generated artifact prints a reason the source never carried | F4 |
| Hand-authoring | A quoted example in the carrier template, and a validator that names the key it rejected | F5 |
| Container decision | `task_containers` presented as a decision with its real options, not as a value to preserve that did not exist before | F6 |
| Stable migration input | A committed revision by default, plus explicit guidance not to migrate while a participant is mid-gate | F8 |
| Post-update self-check | One command answering *is this project consistent with this release*, without knowing which framework test to run | rec 9 |
| Update-path technique | Diff every local `.tfw/` file against the pristine previous tag before merging — the check that collapsed three manual merges to zero | field report §3 |
| Adapter route repair | `/tfw-research` points at `.tfw/workflows/research/base.md`; the shipped template has named a non-existent file for two releases | TD-11 |
| Retired-key removal | `initial_seq` named in the update path as a key to remove, not left to inference | field report §6 |

## The Owner's Own Additions

Three items came from the owner rather than the consumer report. They are recorded distinctly because
their authority is different, and one of them is deliberately out of theme.

**Session naming is broken for a new task.** `plan.md` Step 0 requires `Coordinator | {TASK-ID}` *"before
doing anything else"*, and the identifier does not exist until Step 4. The instruction is unsatisfiable,
so what actually happens is a name carrying a role and a slug. `handoff.md` works because its task
already exists.

The owner's constraint on the fix is explicit and worth preserving: **the question-first flow stays.**
Making the coordinator understand the task and ask before creating a folder is the right order and the
owner values it. So naming is not moved earlier — the rename is placed after the identifier exists, and
it repeats if the slug changes. Two named preferences to satisfy: a phase belongs in the session name
when the agent is given one, and the rename must be a step rather than a habit, because a habit is what
already failed here.

> This item is **out of Phase AA's theme.** It serves session hygiene, not portable delivery. It is
> carried here rather than deferred because it is a small edit in a file this phase is already opening,
> and a separate task for three lines would not be scheduled. Recorded plainly rather than smuggled.

**A stray empty `phases/` directory** appeared at `tasks/TFW-4__showcase_reorg/phases/phase-d` in the
consumer. Nothing in `.tfw/` or in either script references `phases/` — verified, zero occurrences — so
it is not produced by anything this release ships. Phase AA does not chase it; the honest action is to
find its author in the consumer's own history, and the TS records the check rather than the blame.

**F9 — an inbound external record has no journal kind.** The field report is a coordination-relevant
event with no `kind` that fits, and the reporter wrote no event rather than inventing one or misfiling it
as an amendment escalation. That restraint was correct. The decision it defers — whether the closed
vocabulary gains a kind, or whether some artifacts legitimately have no event — belongs to this phase
because this phase is where the second such record will arrive.

## What Phase A Got Right, and Must Survive

Stated because a corrective phase invites the belief that everything is broken.

- **The closed schema held under a live race.** Another agent rewrote the consumer's board three times
  during the update; `status.md` did not corrupt, because the schema forbids exactly the content that was
  moving. Volatile prose has nowhere to go in the carrier. The design paid off in the conditions it was
  built for.
- **`migrate_board.py`'s accounting is trustworthy** — it refuses an empty board, refuses to overwrite,
  and names every identifier rather than asserting a count. The consumer acted on its manifest.
- **`gen_index.py` argues for its own irrelevance** — it declares non-authority, names its source count
  and freshness, and routes the reader back to `status.md`.

Nothing in this phase may weaken any of the three.

## Explicitly Not in Phase AA

- any change to the state carrier, the event grammar, the lifecycle vocabulary or the identifier rules —
  the model is not under revision here;
- task-local debt and knowledge staging — Phases B and C;
- transport mode — TFW-61;
- the Assisted edition's folder-moving status model — TD-182, deferred to its own task by owner decision;
- a package manager, an installer, a version-negotiation protocol or a network fetch: the payload is
  still ordinary files copied from a directory;
- retrofitting the consumer project — its local deltas are its own, and this phase makes them
  unnecessary next time rather than reaching into it.

## Decisions Left to the Phase AA TS

1. Exact payload path for the tooling, and how project-root resolution replaces `parents[2]`.
2. Whether the board locator is configuration, CLI flags, or both — a patch adding `--board` and
   `--board-heading` exists in the consumer with all 60 migration tests green, and is available.
3. Migration-guide location and the rule that routes the update path to it.
4. Whether the closed journal vocabulary gains a kind for an inbound external record, or whether the
   canon states that some artifacts have no event (F9).
5. Exact form of the post-update self-check and what it declines to check.
6. Exact file, new-file and LOC census. Phase A's overrun ruling does not extend here; AA measures itself.
7. Where the session-naming step lands in `plan.md` so the question-first order survives.

The TS may decide within these bounds. It may not change the carrier, reopen Phase A's outcome, absorb
Phase B or C, or accept this repository as its only evidence fixture.

## Phase-Local Risks

| Risk | Control carried into TS and evidence |
|---|---|
| Moving the scripts breaks this repository while fixing others | The move is a deliverable with its own regression: tests, `conventions.md`, `init.md` and CHANGELOG prose all follow the path in one pass, and the suite runs before and after |
| The migration guide becomes another unread wall | It is per-major and routed to from the update step that needs it; the ordering constraint appears where a reader is about to violate it, not in a summary |
| A second external project reveals a third class of assumption | Expected, and the reason DoD 19 says *an external project* rather than *this consumer's project*. One external fixture is the floor, not the ceiling |
| The self-check becomes a second authority | It reports and exits; it repairs nothing and writes nothing |
| The out-of-theme session-naming item grows | Bounded to the rename step and its repeat-on-slug-change. Anything larger returns to the coordinator |
| Phase AA is treated as licence to revisit Phase A | The declared outcome is delivery. A finding about the model itself is filed, not fixed here |

---

*HL — TFW-60 / Phase AA: Portable Delivery | 2026-08-27*
