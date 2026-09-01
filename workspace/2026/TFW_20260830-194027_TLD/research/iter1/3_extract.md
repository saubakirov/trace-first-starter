# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260830-194027_TLD](../../HL-TFW_20260830-194027_TLD.md)
> Goal: a review records the debt it found in its own task and writes nothing else; the registry becomes history.

## Configuration Space

Six dimensions from Gather. D3 (sequencing) and D6 (discovery) are held aside from the cross-product
and treated separately below, because G5 fixes D3 to a single admissible value and D6 is settled by
the frozen §3 contract. The space below crosses **D1 × D2 × D4 × D5** and keeps every row that is
not immediately self-contradictory.

| Config | D1 — what the prose does | D2 — where it goes | D4 — non-debt rows | D5 — who decides | Reads as |
|---|---|---|---|---|---|
| **C1** | rename verbatim, seal, warn | last configured container | sealed with the rest | prose imposes one answer | **the HL as written** |
| C2 | rename verbatim, seal, warn | last configured container | sealed with the rest | gate asks the owner | HL + a gate |
| C3 | rename verbatim, seal, warn | root, renamed in place | sealed with the rest | prose imposes one answer | no destination decision at all |
| **C4** | rename verbatim, seal, warn | root when no container is configured, else the container | sealed with the rest | default imposed, escape named | **version-aware default** |
| C5 | rename verbatim, seal, warn | container the reader names | sealed with the rest | gate asks the owner | every receiver decides |
| **C6** | seal, and name the class first | root-or-container per C4 | prose names the class, reader decides, no obligation | default imposed, escape named | **class carve-out, no triage** |
| C7 | seal, and name the class first | last configured container | prose *requires* the class be checked | gate asks the owner | a checked carve-out |
| C8 | lift the live class out before sealing | last configured container | class relocated to knowledge / a task | gate asks the owner | pre-seal surgery |
| C9 | leave in place, renamed, canon de-lists it | root | sealed with the rest | prose imposes one answer | minimum-motion retirement |
| C10 | rename verbatim, seal, warn | wherever the board snapshot is, found by looking | sealed with the rest | prose imposes one answer | destination by discovery |
| C11 | seal, and name the class first | root-or-container per C4 | the offered follow-up task inherits the class | default imposed, escape named | carve-out deferred to the task |

Rows dropped as self-contradictory before listing: any row pairing *"lift the live class out"* (D1-C)
with *"sealed with everything else"* (D4-A); any row pairing *"the reader names the container"*
(D2-C) with *"the agent decides silently"* (D5-A) — the field reports show the agent then names it.

## Findings

### E1 — The HL's own enforcement argument does not require the move, only the rename

HL §10 answers *"Why not just stop writing to it and leave it in place?"* with: *"A live file the
canon still lists is a file the next agent appends to. **The rename is the enforcement** (PV 1,
Structural Enforcement)."*

Read that sentence against G5. The enforcement mechanism the HL names is the **rename plus the canon
de-listing**. The *relocation* carries no enforcement weight in the HL's own argument — it carries
tidiness (S7, *«кладбище уходит в старую папку таскы… морозится и не мешает больше»*) and symmetry
with `BOARD-SNAPSHOT.md`.

For this repository the two are the same act, because `tasks/` is already the frozen legacy container
by the 2026-08-30 ruling. **For 20 of 25 receiving projects they come apart**: there is no configured
container, `PROJECT_CONFIG.yaml` has no `task_containers` key, and the destination the frozen §4 text
names cannot be computed. C3 and C9 make this visible — they retire the registry with the full
enforcement the HL argues for and **zero destination decision**.

This is the combination the Briefing did not contain. It is not a proposal to change what this
repository does; `tasks/DEBT-SNAPSHOT.md` is correct here and S7 is the owner's ruling. It is a
proposal about what the *receiving* prose says to a project that has no `tasks/` container concept —
which is the majority, and which is the population §2.8 and S3 both say is the point of the task.

### E2 — Class is not merit: the carve-out A1 forbids and the carve-out it does not

A1's ruling is precise: *«мы не создаем задачи, мы просто хороним все долги, запечатываем и
предупреждаем об этом пользователя»*, resting on S8 — a debt not closed with its own task is never
closed. DoD 13 encodes it as *"The retirement reads no row and judges no row."*

G4 found three registries holding content that is not debt at all:

| Content | Where | What it actually is | Where it belongs under 2.0.0 |
|---|---|---|---|
| `## Release gates — v1.7.0`, 4 rows marked `🚦` | `helpdesk` | a list of things blocking a git tag | four tasks — a release gate *is* a task |
| `## 🔴 Safety Rules (from incidents)` → SR-1 | `research-yandex-cloud` | a mandatory operating rule for AI agents, written after an incident | `knowledge/` — it is a verified fact, not a defect |
| `#199`–`#204`, 🔴 P0 / 🟠 P1 | `ai-first-devices` | open production defects with a live owner | tasks, or the phases already scoping them |

**These are found by reading section headings and a status legend, not by reading rows.** The
distinction the retirement is missing is *class*, and class is visible at the table of contents. The
work is bounded by a project's heading count — 8 in `helpdesk`, 3 in `research-yandex-cloud`, 0 in
the 17 flat-table projects, where the carve-out costs nothing because there is nothing to see.

That is the difference between C6 and the thing A1 refuses. A1 refuses **merit** judgement: reading
121 rows and scoring which deserve a task. C6 asks for **class** recognition: noticing that a section
of your file is not debt before you file the whole file under history. One is O(rows) and needs
context nobody has; the other is O(headings) and needs none.

Stated as a rule the prose can carry, with no obligation attached:

> Before you seal it, read your own section headings. If a section of your registry is not debt —
> a release gate, an operating rule, an open incident — it does not become history by being in this
> file. A gate is a task. A rule is knowledge. Everything else seals unread.

### E3 — H1 splits into two claims, and the retirement only needs the second

G3 falsifies H1 as stated and confirms the mechanism underneath it. Written out as two claims:

| | Claim | Verdict | Evidence |
|---|---|---|---|
| **H1a** | Nothing consumes a **canonical** TFW debt registry — the append-only flat table `review.md` prescribes | **confirmed**, 23 of 25 projects | zero task traces scoping from the registry in any project that kept the canonical shape; `resume.md:112` instructs the reader to ignore it; `docs.md` reads it as context and acts on nothing |
| **H1b** | Nothing consumes **any** debt registry, anywhere | **false** | `helpdesk` HD-15 / HD-26 / HD-11 and `ai-first-devices` AFD-6 / AFD-13 / AFD-14 / AFD-18 scope tasks from registry rows |

The retirement's justification needs H1a and nothing more. H1b's falsity does not weaken the case;
it *locates* it. Both consumers first replaced the canonical artefact with something else — an issue
tracker with a deletion policy and a second file for deferrals, or an area-sectioned board with a
periodic cleanup ritual. Consumption did not come free from the mechanism; it was bought by rebuilding
the mechanism, at a cost the HL's Principle 1 would refuse in both cases.

The honest version of the argument is therefore sharper than the HL's: *the canonical registry is
consumed by no one; the two projects that made theirs consumable did so by turning it into a
different artefact and paying a maintenance price. Retirement takes nothing from the 23, and takes
from the 2 exactly the artefact the canon never gave them.*

### E4 — D3 has one admissible value, and D6 is already answered

**D3 (sequencing).** G5 eliminates three of four alternatives outright:

- *before the board migration* — the destination key does not exist yet; the prose would name
  `task_containers` to a config that has no such key, in a file that is not even called
  `project_config.yaml` yet.
- *inside `update.md`, at whatever version the receiver arrives from* — the fifth field report's
  defect 3 records that `/tfw-update` loads the **project's own** `update.md`, i.e. the old one, so
  an instruction placed there is executed by the version being replaced.
- *unsequenced, prose in the CHANGELOG* — the first report's F2 is exactly this failure, recorded.

What survives: **a step in the migration guide, after the payload update and after the config gains
`task_containers`.** In the current guide that is after step 1, and — because a receiver on 0.x has
to choose the container anyway — most naturally beside or after step 5, where the board is removed.

**D6 (discovery).** §3.1 is frozen and answers it: one search across REVIEW files, plus the
disposition gate that means there is little left to search for. G3 supplies the one thing worth
saying about it: `helpdesk`'s four release-gate rows are the concrete test of whether the gate
subsumes the view. Under the gate each of those four becomes a task, and a release blocker expressed
as a task is *more* visible than a row in a section of a root file, not less. The trade is four task
folders against one section — and the HL's own Principle 1 accepts that, because a task is not a
maintained shared list.

### E5 — Two counts the snapshot header cannot state uniformly

HL §4 deliverable 1 requires the snapshot header to carry *"the row count it captured"*, and §7.1
requires *"its row count is stated and checked against the source."* For this repository that is
exact and cheap: 121 rows, one flat table, `TD-33 … TD-215`.

For a receiving project it is not defined. G2: a row is a table line in 17 projects, an `##` heading
in one, a `###` heading in another, a table line inside one of eight sections in another, and in
`atamat` the first column is `Status`, so a naive "count lines starting with `| TD-`" returns zero.
Six projects have no `TD-N` at all; two more use `TD#N` or bare `#N`.

The receiving prose therefore cannot ask for a checked row count without asking the reader to invent
a row grammar for their own file — which is the class of instruction the field reports show gets
invented differently each time. What it *can* ask for is a count that is well-defined everywhere and
verifiable in one command: **lines, words, and the source revision**. `wc -l`, `wc -w`, `git rev-parse
HEAD`. Nothing is judged, nothing is parsed, and the check is mechanical.

This does not touch this repository's own snapshot, which states 121 rows correctly.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C3/C9: the HL's own enforcement argument (rename + de-list) does not need the move; the move is undefined for 20 of 25 receivers | whether the root-or-container default survives pairwise attack — for Challenge |
| C6: class ≠ merit. Reading section headings is O(headings) and A1 refuses O(rows) | whether "read your headings" degrades into triage in practice — for Challenge |
| H1 splits into H1a (confirmed, 23/25) and H1b (false, 2/25); the case needs only H1a | whether losing a used list in 2 projects is acceptable — for Challenge |
| D3 has exactly one admissible value: a step in the migration guide, after the payload and after the config gains `task_containers` | none |
| The snapshot header's "row count" is undefined for receivers; lines + words + revision is defined everywhere | none |

**Sufficiency:**
- [x] External source used? — the receiving-project census and field reports carried from Gather; `migrations/2.0.0.md` re-read for D3
- [x] Briefing gap closed? — the configuration space contains three combinations absent from the Briefing (C3/C9, C4, C6)
- [x] Configuration Space built from Gather dimensions? — D1 × D2 × D4 × D5, with D3 and D6 resolved separately and the reason stated

Stage complete: YES
→ User decision: run without gates (owner, 2026-09-01). Researcher's verdict: **close the stage.**
