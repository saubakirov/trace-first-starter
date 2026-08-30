# HL — TFW-60 / Phase AC: Update Without Guesswork

> **Date**: 2026-08-30
> **Author**: Claude Code (Coordinator), `on_behalf_of: saubakirov`
> **Status**: 📝 HL_DRAFT — awaiting owner review
> **Parent HL**: [HL-TFW-60](../HL-TFW-60__conflict_resistant_shared_workspace.md)
> **Master freeze**: `56c3d70` — baseline after amendment A6
> **Authority**: derivation-only. Vision, Target State, Phases, DoD, DoF and Principles exist once, in the master HL.
> **Origin**: the [fourth](../FIELD-REPORT__TFW-60__fourth_external_update.md) and [fifth](../FIELD-REPORT__TFW-60__fifth_external_update.md) field reports, both on `v2.0.0-dirty.4`
> **Predecessor**: Phase AB, approved at review revision 2 on 2026-08-30 and released as `2.0.0-dirty.4`

---

## Phase Purpose

Phase AA made the framework deliverable; Phase AB made the migration tools tell the truth about
identifiers. Two more real projects then ran the corrected tag — one updating *within* the line, one
migrating onto it for the first time with the owner absent — and the procedure held where it had been
tested and guessed where it had not.

The guesses are of one kind. The pin step guesses that the source stands on its release. The migration
guesses a status from its first token. The copy step guesses that every payload file is the framework's
to overwrite. The update guesses who the owner is, where tasks go and what `build.*` should be — and
then tells the owner what changed in the procedure's words, not theirs. And the coordinator of this task
guessed an abbreviation for a task that had no title.

This phase removes the guessing. Where the procedure cannot know, it asks; where a tool cannot read the
whole, it refuses and says so; where an instruction cannot be executed as written, it is rewritten.

## The Release in One View

```text
BEFORE — five places the update guesses

  Step 0     source_head = HEAD ──────────── tag ≠ HEAD on any live source → check can never pass
  Step 3     "choose containers deliberately" ── agent decides; handle read from git user.name
  Step 5     cp -r .upstream/.tfw/. .tfw/ ─── receiver's project_config.yaml overwritten
  migrate    "✅ DONE (A/V/B/C) · 🔄 Phase D" ── first token wins → main task closed, nothing written
  plan       ABBR = "UPD" ────────────────── an opaque code with no title behind it

AFTER — Phase AC

  Step −1    read the TARGET's update.md, follow it, not this file
  Step 0     operator names the tag → commit derived from it → VERSION read from that commit
  Step 3     🛑 three questions before the first durable write: who · where · build.*
  Step 5     copy with declared exclusions; the step prints what it skipped
  migrate    status cell parsed whole or UNDECLARED + lifecycle_verbatim, under its own heading;
             every phase directory named; "phase state is not written by migration"
  --check    "N phase directories carry no state file"
  Step 8a    briefing in the project's language: what is now possible · what stopped breaking ·
             what no longer has to be done
  plan       title first, then its initials — "Conflict Resistant Shared Workspace" → CRSW —
             both approved in one exchange, both in the HL header
```

## Direct Answers to the Scope Questions

| Question | Phase AC answer |
|---|---|
| Does this reopen Phase AA or AB? | **No.** Both declared outcomes are met and were measured. AC closes their residue — the same relation AA had to A and AB had to AA |
| Why one phase for text fixes *and* a parser change? | One release surface, one tag, one external run. The status cell is one cell, and its rule already exists (the identifier's); splitting it into a phase of its own would double the runs to certify ten lines |
| Does the identifier grammar change? | **No.** Only how the abbreviation is *chosen*: the initials of the approved title, proposed with the title, approved with it. `ASSISTED15` for *Assisted 1.5* is the pattern; `UPD` for nothing is the anti-pattern |
| Are existing tasks or events renamed? | **No.** DoD 10 and DoF 8 stand. Statuses already migrated are not rewritten; a receiver re-running migration on a committed board gets the corrected reading |
| Does the update stop asking in AG mode? | **No.** The three questions go out as one message before the first durable write. An absent owner is asked first and answered later — never decided for |
| Does the briefing replace the CHANGELOG? | **No.** It is derived from it: `Added` → what is now possible, `Fixed` → what stopped breaking, `Removed` → what no longer has to be done, in `content_language` |
| Does the payload stop carrying `knowledge_state.yaml`? | **TS decision.** The deliverable is that the receiver's copy is never overwritten and the copy step says what it skipped; whether that is an exclusion list or a smaller payload is decided with the exact file census |
| Does the phase touch `status.md` keys, the event schema or the index format? | **No.** `templates/status.md` gains the phase paragraph a phase file already carries in this repository; no key changes |
| Is `2.0.0` claimed after this phase? | **No.** Owner ruling 2026-08-30. The phase ships as the next `2.0.0-dirty` tag |
| Which fifth-report items are *not* here? | Report 4 defect 7 (`--check project` and dangling `team/` references — filed, `--check tasks` already catches it); report 5 §6 items on `since`, `created` seconds provenance, README route template, stale index in a non-first container, and `--check project` before migration — filed for the TS observations, not deliverables |

## What Phase AC Delivers

| Release surface | Concrete result | Master HL §4 deliverable |
|---|---|---|
| Source pin | Derived from the tag the operator names; `VERSION` read from that commit and compared with the tag's name; a live source is a valid source | 1 |
| Update path across tags | Each release's updating section reaches a receiver on any earlier tag; retired normative wording quoted verbatim (TD-198); dead CHANGELOG references corrected (TD-190, TD-191); `update.md` opens with *read the target's `update.md`* | 2 |
| Retired-vocabulary gate | Allowlist admits text whose purpose is to retire the term; literally green on a correct project | 3 |
| Step 6 executability | Marker-bounded rows and whole-copy rows told apart; Claude rules gain markers; Antigravity template aligned with its rendering (TD-204) | 4 |
| Provenance record | `installed_from` has one form — upstream reference and verified tag — never a machine path | 5 |
| Owner in the loop | 🛑 before the first durable write: handle (asked, never inferred), containers, `build.*`; briefing step after verification, in the project's language | 6 |
| Payload copy | Declared exclusions; the copy step prints what it skipped | 7 |
| Migration honesty, status cell | Whole-or-`UNDECLARED` with `lifecycle_verbatim` under its own manifest heading; phase directories named with "phase state is not written by migration"; `--check tasks` reports phase directories without state; `templates/status.md` carries the phase paragraph | 8 |
| Abbreviation | Initials of the approved title, proposed and approved with it; HL header carries both; artifact naming under the current grammar stated with an example (TD-201) | 9 |
| Carrier agreement | `templates/journal/event.md` on `via` (TD-200); `templates/team/profile.md` on agents and where a role goes (TD-203); migration guide: one manifest location, when `--working-tree` is right, commands from the project root | 10 |
| Release | Next `2.0.0-dirty` tag; at least one consumer already on the line updates to it; `2.0.0` unclaimed | 11 |

## Explicitly Not in Phase AC

- claiming `2.0.0` — owner ruling 2026-08-30, superseding the 2026-08-29 ruling;
- any change to the identifier grammar, `status.md` keys, the journal event schema or the index format;
- renaming, moving or rewriting any task directory, event or already-migrated `status.md` — here or in a consumer;
- retrofitting the four consumer projects; they update when the tag lands;
- the `actor` field (TFW-54), transport mode (TFW-61), Phase B debt locality, Phase C knowledge staging;
- the minor fifth-report items listed in the last row of the scope table — observations for the TS, not deliverables;
- a payload-apply script as a *requirement*: it is one admissible mechanism for deliverable 7, chosen or rejected at TS on the exact census.

## Evidence Required Before Phase AC Can Be Called Released

Inherited from master HL §5 — DoD 10, DoD 11, DoD 19 — and §7.1. This file creates no second Definition of Done.

| Evidence class | Required observation |
|---|---|
| Pin on a live source | Step 0 executed as written against this repository with `HEAD` ahead of the target tag: passes; against a tag whose `VERSION` disagrees with its name: stops |
| Skipped tag | A receiver on tag *N−2* reads the *N* entry and reaches every instruction it needs without opening the *N−1* entry unguided |
| Gate reachability | The retired-vocabulary check is literally zero outside the allowlist on this repository and on one consumer, with the allowlist stated |
| Step 6 by markers | The Claude rules block on a consumer with a hand-edited `CLAUDE.md` is verified by `cmp` on the marker-bounded region, project text outside it untouched |
| Owner's questions | An AG-mode run against a fixture project produces the three questions before any file is written, and no `team/` profile is created from a Git identity |
| Copy exclusions | A payload copy onto a fixture with a customized `project_config.yaml` and a non-framework `knowledge_state.yaml` leaves both byte-identical and prints both as skipped |
| Status cell | The exact `AILAB-2` row shape as a fixture: `UNDECLARED`, `lifecycle_verbatim` carries the cell, the manifest lists it under its own heading, no terminal classification; a task with `phase-*` directories is listed with each phase named and the hand-authoring notice printed |
| Missing phase state | `--check tasks` on a task directory with a phase directory lacking `status.md` names the directory; on this repository it names none |
| Abbreviation | `plan.md` and `init.md` read: title first, initials proposed with it, both approved; the HL template header carries both fields; TD-201's example resolves through `gen_docs.py` |
| Carrier agreement | `grep` for the retired wordings in the three templates and the guide returns nothing; the guide's commands run from the project root as written |
| Regression | Every Phase AB test still passes; the four pinned corpora parse identically before and after |
| Field | One consumer already on the line updates to the new tag following the target's `update.md` from Step −1, with the pin, the three questions and the briefing on record |

## Source Authority for Phase AC

| Source | What Phase AC inherits |
|---|---|
| [Master HL](../HL-TFW-60__conflict_resistant_shared_workspace.md) at `56c3d70` | Frozen purpose, Phase AC declared outcome and eleven deliverables, DoD 10/11/19, DoF, principles |
| [Fourth field report](../FIELD-REPORT__TFW-60__fourth_external_update.md) | Defects 2–6 and 8, measured on an incremental update; the first field measurement of DoD 1 (19 foreign commits, 0 conflicts) |
| [Fifth field report](../FIELD-REPORT__TFW-60__fifth_external_update.md) | Defects 1–5 and the owner's account of what an update should have asked and said |
| Phase AB RF and REVIEW revision 2 | The dispatcher whose rule the status cell now follows; TD-200, TD-201 |
| Phase AA REVIEW revision 3 | TD-198: a consumer acted on a rule the release retracted |
| `conventions.md` §4 | Identifier, *Which handle a machine acts as* (never inferred from an OS or Git identity), Artifact file naming |

## Phase-Local Risks

| Risk | Control carried into TS/evidence |
|---|---|
| The phase drifts into a redesign of `update.md` | The word ceiling (1200) stays; every deliverable is a step rewritten or added, not a new document; census before TS |
| `UNDECLARED` for multi-token cells strands real tasks | It is the rule conventions §5 already gives — a person resolves with a `transition` event carrying `from: UNDECLARED`; the manifest names each such row so nothing is stranded silently |
| Asking the owner in AG mode blocks unattended updates | One message, before the first durable write; the run may proceed to read-only steps and stop at the write. That is the boundary AG already has for approvals |
| A briefing template becomes a second CHANGELOG | Derived from three CHANGELOG sections, no free text of its own; the template fixes structure, not content |
| Copy exclusions rot as the payload changes | The exclusion list lives beside the copy step and is checked by the payload test that already enumerates every payload path |
| Markers in `CLAUDE.md.template` break consumers whose `CLAUDE.md` has none | First sync inserts the block; a file without markers is reported, not overwritten — the same first-run rule the Codex adapter uses |
| The abbreviation rule is read as "derive silently" | The wording says the opposite in both directions: never invented apart from the title, never created without approval |
| Scope crosses the 30-file budget once copies are counted | Copies are excluded per S32 (Phase A ruling); exact census at TS; if the counted set exceeds 30, split by surface or seek the ruling DoD 16 requires |

---

*HL — TFW-60 / Phase AC: Update Without Guesswork | 2026-08-30*
