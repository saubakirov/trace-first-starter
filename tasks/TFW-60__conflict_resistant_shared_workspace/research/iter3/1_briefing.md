# Briefing — "What should we investigate?"

> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW-60](../../HL-TFW-60__conflict_resistant_shared_workspace.md) — 🔒 FROZEN 2026-08-26
> Predecessors: [iteration 1 RES](../iter1/RES.md) · [iteration 2 RES](../iter2/RES.md) — both closed
> Goal: several humans and agents advance different tasks in one synchronized folder without editing
> the same project-root registries first.
> Mode: deep (`loops_per_stage: 3`) · Iteration 3 of min 2 / max 5, opened above `min_iterations`

---

## Why this iteration exists

Iterations 1 and 2 examined carriers, journal grammar, migration and Git landing, and closed C1-R2 as
sufficient. That verdict stands for what they examined. It does not cover two mechanisms the Phase A
draft made mandatory **after** iteration 2 closed:

| Mechanism | Entered through | Occurrences in the ten iteration-1/2 files |
|---|---|---:|
| Deterministic local state engine + agent-only `tfw-status` skill | §11 S24, S27 | 0 |
| Participant profiles, machine-local TFW home, `device_instance_id` | §11 S28, S29 | 0 |

**Verified independently at briefing time** (`grep -ri` over `research/iter1/` and `research/iter2/`,
10 files, 2 443 lines): `tfw-status` 0, `state engine` 0, `deterministic engine` 0, `engine` 0,
`people/` 0, `device_instance` 0, `device instance` 0, `TFW home` 0, `LOCALAPPDATA` 0, `XDG_CONFIG` 0,
`binding.yaml` 0, `profile_id` 0. The two non-zero hits are `machine-local` (5) and `executable` (4),
and every one of them is about **Git directory/index placement or an executable Git preflight probe** —
none is about a state engine or an identity subsystem. The master HL's zero-occurrence claim is
**confirmed as measured**.

## The default verdict is REMOVE

Master HL §7.1: *"No new artifact is admitted without showing which existing responsibility it owns and
which duplicate write it removes."* This iteration inverts the burden of proof. A mechanism survives
only if it can name (a) the existing responsibility it absorbs and (b) the duplicate write it removes.
"It would be more rigorous" is not an answer. Neither is "removing it is risky".

Equally: the owner's belief that a strict skill suffices is a **position to test**, not a conclusion to
confirm. If a concrete failure scenario exists that only executable code closes, this iteration says so
plainly.

## Research Plan

### Gather — collect, do not judge

- **Primary field evidence.** `H:\My Drive\Innoforce AI-First Knowledge\innoforce_starter_v1.4` — a
  shipped Assisted v1.4 starter living inside a live Google Drive for desktop mount. Characterise:
  provider-written artifacts in the tree; presence/absence of `.git`; task-ID grammar; participant
  resolution; the identification Gate; the absence of a status carrier and task board; whether
  `шаблоны/build_a4.py` is a state engine (expected: no, a document builder).
- **Version archaeology.** The same Drive folder holds v1.0, v1.2, v1.3 and v1.4 of the same starter
  side by side. Compare what each shipped. If an earlier version shipped executable lifecycle
  machinery and a later one removed it, that is a natural experiment on exactly the H5 question, run
  in exactly the H7 environment.
- **Skill strictness.** Read all four `.agents/skills/*/SKILL.md` in the starter and judge how strictly
  a skill actually constrains an agent — what it enforces structurally versus what it merely asks for.
- **Repository baseline for H6.** Measure the current write surface for status exactly: which files
  carry a Task Board write instruction, how many copies each canonical edit costs, what the docs
  generator reads, and what the configured budgets are.
- **Git topology, primary sources.** Establish from Git's own documentation and from read-only
  inspection of this repository's `.git` what is actually documented about repositories on
  synchronized/network storage, and what merely follows from an unverified premise.
- **In-repo Assisted counterpart.** `editions/02-assisted/` — compare to the shipped v1.4 to see
  whether the repository's own idea of Assisted matches the artifact in the field.

### Extract — build the configuration space

Iterations 1-2 already ran a full morphological pass on carriers. This iteration does **not** reopen
them. Its dimensions are the ones the earlier passes never had:

- **D-I Mutation enforcement:** deterministic engine · thin executable validator, advisory · skill
  contract only · structural filesystem gate (path/name uniqueness).
- **D-II Identifier grammar:** monotonic per-task counter · timestamp identifier · content-addressed ·
  no explicit identifier (position in file is the identity).
- **D-III Cross-file duplication:** snapshot duplicates journal head (`last_event_id`) · snapshot is
  disjoint from journal · single file carries both · no journal at all.
- **D-IV Participant resolution:** shared registry · machine-local binding + shared profiles ·
  shared profiles + one question, no binding · no participant concept.
- **D-V Machine-local footprint:** standard TFW home (device + binding + preferences + Git paths) ·
  Git paths only · nothing outside the project.
- **D-VI Git topology:** `.git` inside the sync root · `.git` outside (G-B) · per-participant pinned
  external (G-A) · no Git.

Cross-reference these against the six responsibilities the Phase A draft assigns to executable code
(draft lines 208-216) and ask, per responsibility: **does it still exist if the carrier grammar
changes?**

### Challenge — attack, then subtract

- Hunt honestly for a concrete failure scenario that **only** executable code closes. State it plainly
  if found.
- Re-derive the minimum Phase A that stops the original pain (master HL §§1-2, S1) and measure it
  against the configured budgets. Measure the draft the same way.
- Trace the H7 dependency chain explicitly: if the "synchronized `.git` breaks the repository" premise
  falls, what else falls with it — the machine-local profile, the G-A/G-B matrix, L3?
- Test whether a shared mutable device list recreates the contention TFW-60 exists to remove.
- Consistency-check surviving configurations pairwise; keep only what a Phase A can actually ship.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H5 | No executable code is required. A strict skill invoked by a slash command, plus a carrier grammar that needs no ID allocation, no cross-file transaction and no chain verification, produces homogeneous records without a deterministic state engine. Refuted only by a concrete failure scenario that executable code alone closes | needs-research — iteration 3 |
| H6 | The declared Phase A outcome is reached by removing and reclassifying existing artifacts rather than adding `status.yaml`, `journal/`, two JSON schemas, `task_state.md`, `workflows/status.md`, a state engine, `people/` and a machine-local TFW home. The baseline is the smallest repository change that stops two tasks colliding in root `README.md` | needs-research — iteration 3 |
| H7 | The set of things that must live outside the synchronized project folder is smaller than the Phase A draft claims, and part of that draft rests on untested folklore rather than observation — starting with the claim that a synchronized `.git` breaks | needs-research — iteration 3 |
| H8 | Session-start participant recognition, private-device binding and multi-person transparency are reached through the existing Assisted `people/<handle>.md` model plus a minimal addition, without a Phase A identity subsystem. Whether a device registry is needed at all is part of the hypothesis, not a premise | needs-research — iteration 3 |

## Scope Intent

**In scope**

- The two post-iteration-2 additions (S24/S27 engine and skill; S28/S29 participant/device subsystem).
- The minimum-change baseline for the declared Phase A outcome, measured in files and LOC.
- What genuinely must live outside a synchronized project folder, and the cost of putting it there.
- The shipped Assisted v1.4 starter as primary field evidence, including its version history.

**Out of scope**

- Reopening the C1-R2 carrier families that iterations 1-2 eliminated (C2-C5, G-C, on-demand-only
  view, timestamp recovery, service/database authority) unless direct counter-evidence forces it.
- Phase B debt and Phase C knowledge architecture.
- Writing anything into any HL. Findings that touch §1, §3, §4, §5, §6 or §7 are transcribed here as
  §12 amendment proposals with evidence, cost and a considered alternative, and go no further.
- Any state-changing Git command. Master HL §2.1 risk F1 records that two sessions sharing one index
  already produced a misattributed commit; reproducing that defect inside the task designed to fix it
  is not acceptable. Read-only Git inspection only. This constrains the H7 method: no temporary
  repository can be built and committed into, so H7 rests on primary sources plus read-only
  observation of an existing `.git` and of a live provider mount.

## Evidence classes (carried forward from iteration 2, unchanged)

`FA` fresh agent · `UH` usability heuristic · `DF` deterministic fixture · `RR` repository/runtime ·
`PS` primary source · `NH` non-technical human · `PR` provider runtime.

**Boundary declared at briefing time, before the work:**

- `NH` — **not available to this iteration.** No non-technical participant was observed. It remains a
  mandatory Phase-A acceptance obligation, exactly as iteration 2 left it.
- `PR` — **partially available for the first time.** A live Google Drive for desktop mount containing
  a shipped Assisted starter is directly observable. This supplies provider-written artifacts and the
  no-`.git` topology. It does **not** supply offline fork, reconnect, conflict-copy naming or
  multi-device reconciliation: the folder holds no active task and no second device is observable.
- A heuristic or fixture is never relabelled `NH` or `PR`. Where a consequence is inferred from a `PR`
  observation rather than observed, it is labelled inference and says what would confirm it.

## Guiding Questions

1. Does any of the six responsibilities the Phase A draft assigns to executable code survive a change
   of carrier grammar — or are they artifacts of the grammar C1-R2 happened to choose?
2. What is the smallest repository change after which two tasks stop colliding in root `README.md`,
   measured in modified files, new files and LOC?
3. Is "a synchronized `.git` breaks the repository" an observation, a documented claim, or folklore —
   and what depends on it?

## User Direction

No human owner input in this thread. The coordinator holds the gates and set the mandate: subtraction
is the default verdict; every finding is measured against the original pain, not against the elegance
of the mechanism; frozen sections stay frozen; the scope budget `30 / 15 / 30 / 3000` is a research
input, not a TS afterthought.

---
Stage complete: YES
