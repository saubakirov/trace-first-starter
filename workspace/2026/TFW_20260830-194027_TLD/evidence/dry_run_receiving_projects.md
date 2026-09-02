# Dry run — the receiving instruction against three real registries

> **Date**: 2026-09-02 · **Author**: Claude Code (Executor) · **Covers**: AC-7, AC-8
> **Subject**: `.tfw/migrations/2.0.0.md` step 6 *Retire the debt registry*, and the condensed form in
> `.tfw/CHANGELOG.md` § *Updating from 2.0.0*.

## Read-only declaration

**No file in any project other than this one was created, modified, moved or deleted.** Every observation
below was taken with `wc -l -w`, `grep -n '^#'`, `ls` and `cat .tfw/VERSION` — read commands only. No editor
was opened on any sibling tree, no `git` command was run inside one, and no row of any sibling registry was
read. Recognition was performed exactly as the instruction prescribes it: at heading level.

The three projects were chosen for opposite shapes, per TS AC-7 and AC-8.

| Project | TFW | Size | Shape | `tasks/` | `BOARD-SNAPSHOT.md` |
|---|---|---:|---|---|---|
| `helpdesk` | 2.0.0-dirty.5 | 129 lines · 3 509 words | 8 headings, sectioned by area, release-gate section | ✅ | ✅ |
| `optimization-report` | 0.8.5 | 13 lines · 75 words | prose, no table, one `###` per item, Russian | ✅ | ❌ |
| `research-yandex-cloud` | 0.9.0 | 75 lines · 1 481 words | sections + a safety section | ✅ | ❌ |

---

## 1 · `helpdesk` — the sectioned registry with a live release gate

**What the agent sees at heading level** (the only reading the instruction permits):

```
1:# Tech Debt Registry
7:## Status legend
18:## Release gates — v1.7.0 (HD-26)
29:## Backend
69:## Frontend
98:## Tests / quality
107:## Documentation
116:## Infra / deployment
124:## Deferred / scoped
```

**What the agent would do.** Move the file whole to `tasks/DEBT-SNAPSHOT.md`; `tasks/` exists and already
holds `BOARD-SNAPSHOT.md`, so the confirmation the prose offers actually confirms something here. Write the
header with 129 lines, 3 509 words and the source revision. Stop.

**What the agent would ask.** *Nothing.* `## Release gates — v1.7.0 (HD-26)` is a release gate, and the step
names that case explicitly: *"A release gate, an open defect, a roadmap item, a row whose own text says it
needs its own task — sealed with the rest."* This is the exception working: the most temptingly live-looking
section in the corpus is disposed of by one sentence, without a judgement call.

**`## Deferred / scoped` is the retirement's own thesis, sitting in a real project's file.** A section whose
name is the failure mode. Sealed with everything else, unread.

---

## 2 · `optimization-report` — 75 words, prose, no table

**What the agent sees:**

```
1:# TECH_DEBT — Transit Optimization Research
3:## Текущие задолженности
5:### TD-1: Шымкент — консолидация скриптов
10:### TD-2: venv в корне проекта
```

**What the agent would do.** The same three steps. No branch on size fires: the file is the smallest in the
25-project census and is retired by the identical procedure, with no request to clean it up first. Header
states 13 lines, 75 words.

**What the agent would ask.** Nothing — no safety heading.

**Cost of the exception where it does not apply: one `grep '^#'` over a 13-line file.** This is the
24-of-25 case AC-8 requires to be invisible, and it is.

---

## 3 · `research-yandex-cloud` — the one project with a safety section

**What the agent sees:**

```
1:# TECH_DEBT.md — Research Yandex Cloud
8:## Active Items
46:## Resolved Items
57:## 🔴 Safety Rules (from incidents)
59:### SR-1: Terraform Destroy Review (TD-9, 2026-03-04)
```

`## Active Items` and `## Resolved Items` are debt and are sealed. `## 🔴 Safety Rules (from incidents)` is
the one class the step rescues, and it is recognised from the heading alone — the words *safety* and
*incidents* are both in it. No row was read to reach that conclusion, and none needed to be.

**The question the agent would ask, in full:**

> Your `TECH_DEBT.md` carries a section headed `## 🔴 Safety Rules (from incidents)` at line 57. Retiring
> the registry seals that section with the rest of the file, and a rule written after an accident stops
> applying once it is sealed. I have not read the rules themselves.
>
> Shall I create one task to lift those safety rules out to where they apply, before I seal the file?
>
> If you say nothing, or say no, I seal the whole file including that section and tell you I did.

**On silence or a no:** the file is sealed whole and the agent says so. Nothing is created.

**On a yes:** exactly one task, and nothing else:

```
workspace/2026/TFW_<stamp>_<ABBR>/
  status.md      lifecycle: TODO, owner: <the human>, authority: its HL
  journal/<stamp>__created__<token>.md
```

carrying the goal *lift the safety rules out of the sealed registry to where they apply, and touch nothing
else*. The agent then seals the registry and stops; the lifting happens afterwards, in that task, never
inside the retirement. This is the single optional follow-up DoD 13 allows — there is no second route, and
the step offers none.

---

## Every point where the text implies a decision it does not gate

This is what the dry run exists to find (HL §9, three recorded instances of an agent taking an implied
decision). Six were found. Two are material.

| # | The implication | Where | Material? | What the receiving agent might do instead |
|---|---|---|---|---|
| 1 | **The move mechanism is unnamed.** *"Move `TECH_DEBT.md` to `tasks/DEBT-SNAPSHOT.md`"* does not say `git mv`, `cp`+`rm`, or an editor | guide step 6.1; CHANGELOG step 1 | **Yes, mildly** | Under git, `cp`+`rm` loses the file's history and makes byte-identity an assertion rather than a fact. Under file synchronization (no git) `git mv` is not available at all. Naming a command would violate AC-7's *"no command a receiver must run"*, so the honest fix is a clause — *however your project moves files; if it is under version control, move it in a way that keeps its history* |
| 2 | **The source revision is asked for, with no source named.** The header must state *"the revision you took it from"*, and the step deliberately prescribes no command | guide step 6.2; CHANGELOG step 2 | **Yes** | A project not under version control has no revision, and the text does not say what to write then. An agent may invent one, omit it silently, or write a date. AC-7 forbids requiring a command, so the fix is again a clause, not a command: *"the revision if your project has one; the date if it does not"* |
| 3 | **Ordering against the payload update is not gated in the condensed form.** The guide is safe — step 1 already replaced the canon. The CHANGELOG's condensed version puts *"Take the payload's canon"* at step 3, after sealing | CHANGELOG § *Updating from 2.0.0* | No, but worth stating | A receiver who seals first and updates later has a window in which their installed `review.md` still says *"Append to project-level `TECH_DEBT.md`"* — and the next review recreates the file it just retired. Harmless if the update follows immediately, which is the normal case |
| 4 | **The `BOARD-SNAPSHOT.md` confirmation is empty for an unmigrated project.** *"`tasks/`, the same directory step 2 put `BOARD-SNAPSHOT.md` in"* — 2 of the 3 projects here have `tasks/` and no board snapshot | guide step 6.1 | No | The destination is still named outright, so nothing is derived and nothing breaks; the reassurance simply says nothing. A reader of the *guide* has always just done step 2, so the case cannot arise there |
| 5 | **In a heading-per-item project, heading-level recognition is item-level recognition.** `optimization-report` carries `### TD-1:` and `### TD-2:` as its items; `ai-first-devices` carries 149 such sections | guide step 6, the exception | No — but it bounds a claim | Nothing below a heading is read, so the rule holds as written. What changes is how much a heading scan reveals: in a flat-table project it reveals almost nothing, in a section-per-item project it reveals every item's title. The *"no triage"* guarantee is weaker there by construction, not by the agent's choice |
| 6 | **A 0.x reader landing in the wrong CHANGELOG section.** *"create one task in your workspace under the current identifier grammar"* is unevaluable at 0.9.0: no `workspace/` container, no `tfw.task_containers`, no `id_format` | CHANGELOG § *Updating from 2.0.0* | No — gated by the section title | The section says *Updating from 2.0.0*, and a 0.x project is routed to the migration guide, where step 3 has already delivered both. An agent that reaches the section by grepping the CHANGELOG for `TECH_DEBT` would land outside its stated audience. This is the same shape as the H6 destination defect — a rule that reads a 2.0.0 concept — and it is why the *destination* was measured rather than computed |

**Nothing in the step requires a command, a script or a check.** Verified by reading it end to end: the
only shell text in guide step 6 is the file path `tasks/DEBT-SNAPSHOT.md` and the example heading
`## 🔴 Safety Rules (from incidents)`. Both are strings to look for, not things to run.

---

*Dry run — TFW_20260830-194027_TLD | 2026-09-02*
