# PROPOSAL — TFW_20260902-222456_RTBO: Retire the board obligation

> **Date**: 2026-09-02
> **Author**: Claude Code (Coordinator)
> **Status**: ⬜ TODO — proposal only. No HL, no TS until the owner takes it.
> **Entry point**: **`/tfw-plan`** — see *Why this needs a contract* below.
> **Origin**: owner instruction, 2026-09-02, immediately after a malformed journal summary in
> `TFW_20260902-112841_RDP` turned the whole test suite red through `build.verify`.

---

## The finding

`00-INDEX.md` — the task board — is a **derived** view. The canon says so in the strongest terms it has,
in `conventions.md`'s Discovery rules:

> *"It is never authoritative… Absent, stale or malformed, the index degrades discovery and changes no
> task state — the project stays workable and says visibly that the view is behind."*

And yet, until 2026-09-02, its checker was `build.verify` — a **blocking gate**. So a view the canon
declares never authoritative could stop every unrelated piece of work in the repository, and on
2026-09-02 it did: **one journal event's summary line was 123 code points against a ceiling of 120**, and
the whole suite went red. Nothing was broken. Nothing was lost. No receiving project could have been
affected. One sentence was three characters long.

**That specific gate is already gone** — `build.verify` removed from both `project_config.yaml` files, the
`Verify` line removed from `templates/RF.md`, and one test's assertion on the *live corpus's* exit code
removed, in commit `859dc74`. This task is not that. **This task removes the obligation everywhere else it
is written.**

## The owner's instruction, 2026-09-02

> *«убери молча эту проверку при сборке доски. чтобы она никому нигде не мешала. эта доска вообще не нужна
> больше. никто туда смотреть не будет… она нужна по сути как механизм понять список и статусы актуальные,
> агенты про это знать должны, но ворота это быть не должны. мешать не должны. постоянно выполнять не
> надо. нам здесь только нужно и то только потому, что гитхаб его используют. наверное и там тоже стоит
> отключить, список задач там не нужен.»*

Three things are being said, and they are not the same thing:

| The instruction | What it means concretely |
|---|---|
| **not a gate** | nothing blocks on the board's state. Done on 2026-09-02 |
| **not a step, not run constantly** | no workflow tells a role to generate or check it as part of doing something else |
| **still the mechanism for the list and the statuses** | an agent that needs *which tasks exist and what state each is in* runs it on demand and gets an answer |

The board is not being deleted. **The duty to keep it is.**

## Measured footprint, 2026-09-02

`gen_index` or `00-INDEX` is named **24 times across 9 canon and root files**, plus the adapter copies:

| File | Mentions |
|---|---|
| `KNOWLEDGE.md` | 6 |
| `.tfw/workflows/init.md` | 5 |
| `.tfw/conventions.md` | 4 |
| `README.md` | 4 |
| `.tfw/README.md` · `.tfw/glossary.md` · `.tfw/quickstart.md` · `.tfw/templates/status.md` · `.tfw/workflows/update.md` | 1 each |
| `.claude/commands/tfw-init.md` · `tfw-update.md` · `.agent/workflows/tfw-init.md` · `tfw-update.md` | adapter copies of the two workflows above |

Not every mention is an obligation. Some are description — *the board is derived, never trust it* — and
that wording is the reason this task exists and must **stay**. The task's first job is to sort the 24 into
**description**, **obligation** and **stale**, and only the second and third change.

## The GitHub question, which is the owner's to answer

`.github/workflows/docs.yml` runs `mkdocs build` on every push to `master`; the docs build imports
`gen_index` through `docs/scripts/gen_docs.py` and publishes a task list to the site.

The owner's reading: *«список задач там не нужен»*. If that holds, the docs build stops rendering the task
list and `gen_docs.py`'s dependency on the resolver either goes or shrinks to path parsing. **That is a
real decision with a real consequence** — the published site loses a page — so it belongs in the HL as a
declared outcome, not in an executor's judgement.

## What must NOT happen

- **`gen_index.py` is not deleted.** It is the only thing that can answer *which tasks exist and in what
  state*, which is the use the owner explicitly kept — and `gen_docs.py` imports it. Deleting it breaks
  the documentation build.
- **The Discovery rules are not softened.** *"Never authoritative"* and *"reports every legacy, malformed
  or unresolved input rather than dropping it"* are the two clauses that made this diagnosis possible.
  They stay verbatim.
- **No replacement mechanism is invented.** The answer to *how do I see the list* is: run the tool. Not a
  new file, not a new command, not a cache.
- **The board's absence does not become a new obligation either.** A project that wants to keep generating
  it on a schedule is doing nothing wrong. What is withdrawn is the *duty*, exactly as
  `TFW_20260830-194027_TLD` withdrew the duty to keep a debt registry without forbidding anyone's file.

## Definition of done, informally

1. The 24 mentions are sorted into description, obligation and stale, with the count for each recorded.
2. **No workflow prescribes generating or checking the board as a step.** `init.md`'s five mentions are
   the main body of this: a project set up today is told to produce a board.
3. `KNOWLEDGE.md`'s six mentions agree with whatever is decided — they are read in full by every
   coordinator, so a stale one there is an input to every future plan.
4. The GitHub docs decision is taken by the owner and implemented either way.
5. Both adapter sets and both marker blocks re-synced; every whole copy verifies by `cmp`.
6. `.tfw/CHANGELOG.md` records it for receivers, including what a project that already runs the board on a
   schedule should do — namely, whatever it likes.
7. **Nothing new is added.** Net maintained artifact count falls or holds.

## Why this needs a contract, and not `/tfw-config`

`TFW_20260902-153617_RTMW` was pure deletion — two orphan files and eleven references — so it entered
through `/tfw-config`. This one is not. It carries **two design decisions** the owner has to declare
before anyone edits: whether the published documentation keeps a task list, and where the line falls
between *description of a derived view* and *obligation to maintain one*. Sorting 24 mentions by that line
is exactly the kind of judgement that produces drift when it is left to an executor. So: `/tfw-plan`, an
HL, a frozen declared outcome.

## Promoted into this proposal, 2026-09-02

**One item, from `REVIEW__TFW_20260902-112841_RDP__rev4.md` §5 row 5, ruled `promoted` by the coordinator.**

When `build.verify` was removed from `.tfw/templates/project_config.yaml`, the shipped `build:` block was
left carrying only `echo` placeholders. Before that, the removed key was annotated *"A real command, not a
placeholder: every TFW project ships this tool, so this one works from the moment the payload lands"* — so
a new project's first executor build gate ran something. It now runs two `echo`s and passes, and the
template's own comment two lines below says exactly what that means: *"a placeholder means the executor's
build gate in handoff.md verifies nothing."*

**The owner forbade the board being a gate, not the template shipping a working command.** Those are
different changes and only the first was instructed; the second happened as a side effect. Nothing is
broken and nothing is urgent — `lint` and `test` were placeholders before today too — but the shipped
default moved from *verifies one thing* to *verifies nothing*, and this task's subject is precisely the
un-gating's aftermath.

**The question for the HL, not a foregone answer:** should the template ship any working default under
`build:`, and if so what — given that the only universally-available command TFW ever had was the board's
own checker, which is the thing being retired.

## One candidate worth carrying into the HL's research

**The summary ceiling may have no reason to exist once the board is not a gate.** `max_summary_length` is
read by exactly one consumer — the board's own generator — and its purpose is that a line renders short in
a table. That is a **display** concern: the right place to shorten is at generation, not to forbid at
write time. The general defect is already measured and recorded as fact candidate **F12** in
`TFW_20260902-112841_RDP`:

> a ceiling whose only reader runs *after* the write, on a file the canon calls immutable, is a limit that
> cannot be complied with — one keystroke reddens a gate permanently.

That is the incident that opened this task, stated as a class rather than as an event. Whether the ceiling
goes, moves to generation, or stays is a research question, not a foregone conclusion — but it should not
be discovered a third time.

---

*PROPOSAL — TFW_20260902-222456_RTBO: Retire the board obligation | 2026-09-02*
