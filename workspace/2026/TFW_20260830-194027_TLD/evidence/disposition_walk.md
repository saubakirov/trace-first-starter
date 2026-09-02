# Disposition walk — the gate against one real closed review

> **Date**: 2026-09-02 · **Author**: Claude Code (Executor) · **Covers**: AC-4, and HL DoF 10
> **Subject review**: [`tasks/TFW-60__conflict_resistant_shared_workspace/phase-ac/REVIEW__phase-ac__update_without_guesswork.md`](../../../../tasks/TFW-60__conflict_resistant_shared_workspace/phase-ac/REVIEW__phase-ac__update_without_guesswork.md)
> **Why this one**: the TS names it. It filed ten items, `TD-206`–`TD-215`, and separately closed seven —
> the largest single debt event in the corpus, reviewed under the old rule five days before the new one.

## Method

Each of the ten rows is taken as written and run through the gate: `paid` as a phase of this task,
`promoted` to a task, or `not material` on the record — and the existence test, *does the thing the
disposition names exist at the moment it is written?* Nothing was re-investigated; the row's own text and
the tree as it stood on 2026-08-30 are the whole input. **No row of the sealed registry was opened.**

## The ten items

| # | The row, in brief | What it said then | Does that name something that existed? | Disposition under the gate |
|---|---|---|---|---|
| TD-206 | `update.md` Step 0 admits a commit target in prose; the block checks tag equality only | `→ backlog: one sentence, 26 words of ceiling left` | **No.** "Backlog" is the graveyard | **not material** — a stated limitation of a prose admission, not a defect. Recorded as such in the 2.0.0 CHANGELOG's *Known open*, which is where it in fact ended up |
| TD-207 | A live task with no `status.md`; the gate reads its stateless phases as history | `→ owner: author the state, or close the research` | **Partly.** The owner exists; the ruling did not yet | **pending — owner**, then **not material** — the owner's frozen-corpus ruling of 2026-08-30 made it moot, and the CHANGELOG says so. A textbook `pending` that converted |
| TD-208 | No template for the permanent README route; hand-rewritten in three places | `→ next payload-boundary phase` | **No.** No such phase existed or was scheduled | **not material** — three hand edits on a container change that happens once per major version |
| TD-209 | A stale `00-INDEX.md` in a non-first container is never named | `→ Phase B (touches gen_index.py)` | **No — and this is the finding.** `phase-b/` did not exist, and **amendment A8 dropped Phase B entirely on 2026-08-30**, five days later | **promoted** or **not material**. Whichever the reviewer chose, the gate would have forced the choice *instead of* pointing at a phase that was cancelled |
| TD-210 | `created` seconds provenance unstated; `--check project` green while the board still stood | `→ next scripts pass` | **No.** Names nothing | **not material** |
| TD-211 | The payload ships this repository's own config and knowledge state | `→ owner ruling on the payload boundary` | **Partly** — as TD-207 | **pending — owner**. Still open at 2.0.0 by the owner's own listing. Legitimate, and it keeps the task honest rather than closing it over an open question |
| TD-212 | `team/README.md` keeps wording a sibling change removed | `→ backlog: one sentence` | **No** | **not material** |
| TD-213 | `mkdocs_gen_files` at module load blocks importing the resolver outside a build | `→ backlog, pairs with TD-79` | **No** | **not material** — a test-ergonomics limitation, and pairing it with another open row is two graveyard entries, not a disposition |
| TD-214 | `--check project` reads `team/` but not who references it | `→ backlog: a cross-check line or a "not checked" sentence` | **No** | **not material** |
| TD-215 | The `.5` CHANGELOG entry names `CLAUDE.md` for the marker rule and not `AGENTS.md` | `→ /tfw-release: one clause in item 5` | **No.** A workflow is not a vessel | **promoted**, or **paid** if written during the release itself — and it *was* in fact paid: 2.0.0 § *Updating from 1.x* item 4 names both blocks |

**Tally under the gate:** `not material` **6** · `pending — owner` **2** · `promoted` **1–2** · `paid` **0–1**.

Separately, the same review closed seven items — `TD-190`, `TD-191`, `TD-198`, `TD-200`, `TD-201`,
`TD-203`, `TD-204` — inside the phase. Those are `paid`, under a name the old canon did not have.

## What the walk cost

Roughly **twelve minutes** for ten items, and the time went almost entirely into one question per row:
*does the thing this points at exist?* The dispositions themselves were quick — the reviewer had already
decided each item's fate; they had simply written the decision in a vocabulary that did not have to be
true. Checking `phase-b/` would have taken one `ls`.

## The honest verdict on ceremony — DoF 10

**Six of ten came out `not material`, and that is uncomfortable enough to state plainly rather than
explain away.** DoF 10 names exactly this: *"not material becomes the default an agent writes to clear the
gate."* Two readings are available and the walk supports the second.

**Reading A — the gate is ceremony.** Most items get the cheapest label, so the gate has converted a
one-word `→ backlog` into a one-sentence `not material — {reason}` and changed nothing.

**Reading B — `not material` was always the true answer, and the old channel let the reviewer avoid
saying it.** Six of those items sat in a registry for months and nobody acted on any of them. `→ backlog`
was not a milder verdict than `not material`; it was the *same* verdict, deferred, unsigned, and costing
a row in a file that grew to 12 352 words on exactly this kind of entry.

**What decides between them is whether the ruling must carry a reason, and it must.** The template writes
the column as `not material — {the ruling}` and `judge.md` row 3 asks the reviewer to name, per row, what
the disposition names. A bare `not material` with an empty reason is Reading A and fails the row. The six
above each produced a specific sentence in under a minute, which is the test passing.

**And the gate found something on its first real walk.** `TD-209` pointed at `Phase B` of a task whose
Phase B was dropped by amendment five days later. Under the old rule that row read as a plan; under the
existence test it is caught at the moment it is written. One finding in one review is not a firing rate,
and it is not offered as one — but it is the difference between a gate that could fire and a gate that has.

**Residual concern, recorded rather than resolved.** `paid` is awkward from the reviewer's chair. A
reviewer cannot write code or docs, so "pay it as a phase of this task" means either *it was already fixed
during the phase* — the seven closures above — or *the verdict becomes 🔄 REVISE and the executor pays it*.
The canon does not say this, and a reviewer meeting the gate for the first time may read `paid` as
something they are expected to do themselves and hit the role lock. It is a wording gap, not a design
fault, and it belongs in this task's own REVIEW §5 rather than in an unrequested edit to the workflow.

---

*Disposition walk — TFW_20260830-194027_TLD | 2026-09-02*
