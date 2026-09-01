# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260830-194027_TLD](../../HL-TFW_20260830-194027_TLD.md)
> Goal: a review records the debt it found in its own task and writes nothing else; the registry becomes history.

## Dimensions

The retirement instruction is not one decision. Six independent degrees of freedom fall out of the
census below, and the HL currently fixes four of them without having seen this evidence.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| **D1 — What the prose does to the file** | rename verbatim, seal, warn *(HL's choice)* | seal, and require the reader to read one narrow class of row first | seal the file, lift a named class of live row out of it before sealing | leave it in place, renamed, no move |
| **D2 — Where the sealed file goes** | last configured task container *(HL's choice, H6)* | in the project root, renamed, not moved | a container the prose asks the reader to name | wherever the board snapshot went, found by looking |
| **D3 — When, relative to the 2.0.0 board migration** | after it, as a later step of the same guide | before it, independent of it | inside `update.md`, at whatever version the receiver arrives from | not sequenced at all — prose in the CHANGELOG |
| **D4 — Rows that are not debt** | sealed with everything else *(HL's choice)* | prose names the class, reader decides, no obligation | prose requires the class be checked before sealing | the offered follow-up task inherits them |
| **D5 — Who decides D2 and the offered task** | the agent, silently *(what the field reports observed)* | the prose imposes one answer for everyone | a gate puts it to the owner in the receiving project | prose imposes a default and names the escape |
| **D6 — What replaces discovery** | one search over REVIEW files, stated in canon *(HL's choice)* | nothing — the snapshot is the record | a derived index, generated | the disposition gate alone: nothing to find, because nothing is deferred |

## Findings

### G1 — The population is 25, not 19, and the missing six were selected out by a file

`find` over `d:/projects` for directories containing `.tfw/` returns **25 real projects** (two
further hits are artefacts: a build tree inside `KZ-IT-telegram-list/.git/` and a test fixture under
`vllm-local-coding/test/workspace/`). HL §2.8 measured 19.

Six projects carry `.tfw/` and a `TECH_DEBT.md` and are absent from §2.8:

| Project | TFW version | Words | Lines | Why §2.8 missed it |
|---|---|---:|---:|---|
| `KZ-IT-telegram-list` | 2.0.0-dirty.4 | 1 335 | 75 | outside `research/` |
| `capetown` | **1.0.0** | 572 | 31 | outside `research/` |
| `avtobys/business-card` | *(no `VERSION`)* | 394 | 23 | outside `research/`, and no `VERSION` file |
| `codex/генератор` | 0.8.7 | 46 | 7 | outside `research/` |
| `research/robert` | *(no `VERSION`)* | 321 | 14 | **inside the searched tree**, no `VERSION` file |
| `research/sqlrooms-demo` | *(no `VERSION`)* | 375 | 19 | **inside the searched tree**, no `VERSION` file |

Two mechanisms, and the second is the one that matters. `robert`, `sqlrooms-demo` and
`business-card` carry `.tfw/PROJECT_CONFIG.yaml`, `conventions.md`, `workflows/`, `templates/` and
`adapters/` — everything except `.tfw/VERSION`, which their installs predate. **A census keyed on
`.tfw/VERSION` cannot see a pre-VERSION install**, and three of them exist. Anything the retirement
plans to count, verify or reach must key on `.tfw/` itself.

`KZ-IT-telegram-list` is the sharper miss: HL §10 H3 names it *by name* as one of three field-report
sources, and §2.8's census does not contain it. It is on 2.0.0-dirty.4 — a project that meets this
change at its next update.

**Corrected population, and it makes §2.8's own point harder:** 25 of 25 carry the file, none is
empty, the smallest is 46 words. Version spread is 5 on 2.x (`steps-framework`, `helpdesk`,
`innoforce-ai-first`, `kaznpu-ai-lab`, `KZ-IT-telegram-list`), 1 on 1.0.0 (`capetown`), 16 on 0.x,
3 with no version file at all. §2.8's *"16 of 19 are on the 0.x line"* is also arithmetically off
against its own table, which lists 15.

### G2 — Nineteen distinct table shapes, six identifier grammars, and three files that are not tables

Measured across all 25 registries.

**Shape.** 17 are a single flat table under one heading. 7 are sectioned — by lifecycle
(`## Open Items` / `## Resolved Items`), by area (`## Backend` / `## Frontend` / `## Infra`), or by
both. 1 (`optimization-report`) has no table at all: `### TD-1: …` prose sections. 1
(`ai-first-devices`) is 149 `##` sections with 23 embedded tables — an issue tracker in Markdown,
one `## #189 — …` heading per item.

**Columns.** Twenty-four table-carrying registries produce **19 distinct header rows**. One shape
recurs five times (`# | Source | Severity | File(s) | Description | Status`); the other eighteen are
each unique. Four are wholly or partly in Russian (`# | Описание | Приоритет | Задача-источник |
Статус`). Widths run 5–7 columns. Column *names* for the same concept vary — `Source` /
`Источник` / `Origin Task` / `Задача-источник`; `Status` / `Статус` / `Action` /
`Owner / Next Step`.

**Identifiers.** `TD-N` in 14. Bare integers `1, 2, 3` in 6 — `business-card`, `codex/генератор`,
`robert`, `innoforce-blog`, `innoforce-contacts`, `kaznpu-ai-lab`. `TD#N` in
`aubakirov-home-assistant`. `#N` alone in `ai-first-devices`. HL §2.8 point 3 says *four* projects
carry rows with no `TD-N`; measured over the true population it is **six**, and two more use a
`TD#N` / `#N` grammar that a `TD-\d+` matcher also misses.

**What this settles.** A retirement that moves the file verbatim is the only instruction that can
address 25 files with 19 column sets, 6 identifier grammars and 3 non-tabular layouts. Anything that
parses, counts per class, or renumbers has 19 shapes to get right. This is direct support for the
HL's Principle 5 and for A1 — and it is a stronger argument than §2.8 currently makes, because it
rests on shape rather than on size.

But the same fact cuts the other way for the snapshot header: a header that states *"the row count
it captured"* (HL §4 deliverable 1) requires counting rows, and there is no row grammar common to
25 files. In `optimization-report` a row is an `###` heading; in `ai-first-devices` it is a `##`
heading; in `helpdesk` it is a table line in one of eight sections; in `atamat` the first column is
`Status`, not an identifier.

### G3 — H1 is false outside this repository. Two projects consume the registry as a live list

The briefing asked for counter-evidence first. It exists, in two projects, and it is not incidental.

**`helpdesk` (2.0.0-dirty.5) — the registry is a scoping input, by design:**

- `HD-15__quality_audit_tech_debt` is a whole task whose subject is the registry: *"Все 40 записей
  технического долга верифицированы"*, and its Result Visualization is explicit about the intended
  consumption — *«Агент через 1 месяц: открывает TECH_DEBT.md → видит N реальных items с
  верификацией → не тратит время на "а это ещё актуально?" → сразу оценивает scope.»*
- `HD-26/PhaseC` records reading it as a pre-TS gate: *"TECH_DEBT.md прочитан полностью (98 строк,
  ~50 open items)"*, and carries **AC-11** with a mechanical gate on the file:
  `grep '🔜|⬜' count post-Phase-C ≤ pre-Phase-C count − 7`.
- `HD-11/PhaseA` step 7 is *"TECH_DEBT.md Triage"* — close 14, won't-fix 13, add 2.

**`ai-first-devices` (0.9.0) — task scope is taken from registry rows:**

- `AFD-13` Phase C: *"**Scope (3 critical items from TECH_DEBT.md)**"* — TD-187, TD-188, #184, each
  with its own open question for the TS and its own DoD row.
- `AFD-14`: *"TECH_DEBT.md #199–#204 — открытые P0/P1/P2 этой задачи"*.
- `AFD-6`: *"Sources: iter11 RES (Codex audit), … TECH_DEBT.md (68 items)"*, with step 6.5 closing
  eight numbered rows.
- `AFD-18/phase-d2` scopes from #229 and #230.

**H1 as written — *"no completed task's trace shows an item being picked up from the registry rather
than from its REVIEW"* — is falsified.** Six tasks across two projects do exactly that.

**The correlation is the real finding.** Both consumers abandoned the canonical shape first.
`ai-first-devices` rewrote the registry into per-item prose sections with an explicit maintenance
rule in its own header — *«Закрытое/устаревшее — удаляется сразу (история в git). Номера (`#`)
стабильны; при закрытии — удаляем строку, номер не переиспользуем»* — and pushed deferred work into
a **second file, `ROADMAP.md`**. `helpdesk` sections by area, gates by release, and prunes:
*"closed (✅) and won't-fix (⛔) items removed after each release. Last cleanup: 2026-04-30."*
Every project that kept the canonical append-only flat table shows **zero** consumption.

So the canon's registry is consumed nowhere. Two projects made theirs consumable by turning it into
a different artefact, and each paid a price the HL's Principle 1 would refuse: a second registry, or
a standing cleanup ritual. **H1 is false as a factual claim and true as a claim about the canonical
mechanism** — and that distinction changes what the retirement prose has to say.

### G4 — Three registries carry live, non-debt payload that "seal unexamined" would take out of circulation

This is what nobody asked for, and it is the finding with the most consequence.

| Project | What is in the registry that is not debt | State |
|---|---|---|
| `helpdesk` | `## Release gates — v1.7.0 (HD-26)` — four rows marked `🚦 Release gate v1.7.0`, under the note *"Pending PO browser session before `git tag v1.7.0`"* | **live** — the file is the gate list blocking a tag |
| `research-yandex-cloud` | `## 🔴 Safety Rules (from incidents)` → `SR-1: Terraform Destroy Review` — five **MANDATORY RULES for AI agents**, written after an incident destroyed a VPN gateway | **live** — an operating rule for agents, not a defect |
| `ai-first-devices` | `#199`–`#204` marked 🔴 P0 / 🟠 P1, found by a *honest-reverify* pass; plus the file's own maintenance rules in its header | **live** — open production defects |

The HL's retirement text says the snapshot header *"states plainly that the rows were sealed
unexamined and that age is not evidence of importance, so a reader is warned rather than reassured"*
(DoD 13). Applied to `research-yandex-cloud`, that sentence retires a safety rule by describing it
as possibly-stale history. Applied to `helpdesk`, it seals a release blocker.

Note what this does **not** say. It does not argue for per-row triage — A1 refuses that, and this
evidence does not disturb it, because in all three cases the live content is **a named section or a
marked status token**, not a judgement about individual rows. The distinction the retirement
currently lacks is *class*, not *merit*.

### G5 — `tfw.task_containers` does not exist below 2.0.0, so H6's answer is undefined for 20 of 25 projects

H6 was closed on 2026-09-01 with: *"beside the board snapshot, and the rule already exists —
`migrate_board.py` `legacy_container()`: the last configured container."* Measured:

| Project | Version | `task_containers` | `initial_seq` | Config filename |
|---|---|---|---|---|
| `helpdesk` | 2.0.0-dirty.5 | `[workspace, tasks]` | — | `project_config.yaml` |
| `kaznpu-ai-lab` | 2.0.0-dirty.4 | `[workspace, tasks]` | — | `project_config.yaml` |
| `KZ-IT-telegram-list` | 2.0.0-dirty.4 | `[tasks]` | — | `project_config.yaml` |
| `capetown` | **1.0.0** | **absent** | present | `PROJECT_CONFIG.yaml` |
| `belarus-lukoil` | 0.8.2 | **absent** | present | `PROJECT_CONFIG.yaml` |
| `local-network` | 0.8.7 | **absent** | present | `PROJECT_CONFIG.yaml` |
| `optimization-report` | 0.8.5 | **absent** | present | `PROJECT_CONFIG.yaml` |

The key is introduced *by* the 2.0.0 migration — `migrations/2.0.0.md` says so outright:
*"`tfw.task_containers` does not exist before 2.0.0, so there is nothing to preserve — you are
choosing it."* Their config file is even named differently.

**Consequence for D3.** The retirement prose cannot name "the last configured container" to a
project that has not yet run the 2.0.0 migration — which is 20 of 25. Either the retirement is
sequenced strictly after that migration, or it must name a destination that exists unconditionally.
H6 is not wrong; it is under-specified in exactly the direction the briefing's question 2 pointed at.

### G6 — `migrations/2.0.0.md` mentions debt zero times, and the retirement breaks its one safety property

The migration guide is 277 lines across seven numbered steps. `grep -i debt` returns **nothing**.
There is no order dependency today because there is no debt step today; the order dependency is
created by writing one, and G5 fixes its position: after step 1 (payload) and after the config gains
`task_containers`.

The more interesting collision is a property the guide sells and the field reports confirm:

> *"Миграция аддитивна, и это снимает страх. Ни один существующий файл не открыт на запись; откат —
> удалить новые файлы. Оператор, знающий это, действует быстрее и не делает бэкапов доски."*
> — `FIELD-REPORT__TFW-60__fifth_external_update.md`

The board retirement is additive: the snapshot is written, the board is removed *last*, in step 5,
after everything is accounted for. **The debt retirement as specified deletes a root file** (HL §4
deliverable 1: *"`TECH_DEBT.md` deleted from the project root"*). It would be the first
non-additive step in the guide, and additivity is the property the one operator who wrote it down
named as the reason they moved fast without taking a backup.

### G7 — What the field reports say about prose of exactly this shape

Seven field reports, 17 047 words, five external update runs. Sorted by relevance to *"rename a root
file, write a header, optionally open one task"*:

**What prose achieves reliably.** A step that names an exact command, an exact path and a
verifiable check executes literally. The fifth report's list of what worked is entirely of this
kind: a pinned source; classification against a declared baseline (61 of 63 files `SAME_AS_1.0.0`);
`--check` output that *enumerates what it did not check* — *"это превращает «инструмент сказал ОК» в
«инструмент сказал ОК про вот это»"*; byte-copied adapters that caught four `.claude/commands/`
files silently lagging their own workflows.

**What prose does not achieve: it does not stop an agent from deciding.** The fifth report's
defect 2 is a table of three decisions that belonged to the owner and were taken by the agent
because the text merely implied them:

| Decision | Whose | Who took it |
|---|---|---|
| `tfw.task_containers` | owner | agent (`[tasks]`; owner changed it afterwards) |
| `team/{handle}.md` — who this is | owner | agent — **inferred from the git author**, which `conventions.md` §4 forbids in that many words |
| `build.verify` | owner | agent |

The retirement instruction contains two decisions of exactly this shape: **where the snapshot goes**
(D2, undefined below 2.0.0 per G5) and **whether to open the offered task** (D5). On this evidence
the agent will take both, silently, and the owner will find out afterwards.

**Third:** the first report's F2 — *"a major breaking release ships no migration guide"* — records
that the one ordering constraint that mattered appeared *once*, in a code fence, ~150 lines in. The
receiving agent still followed it. Placement did not defeat prose; **absence of an explicit gate
did.**

### G8 — The canon's own texts already say nobody is obliged to act on the registry

Not receiving-project evidence, but it is the mechanism behind G3 and it is one grep:

| File | Line | What it says |
|---|---|---|
| `review.md` | 132, 138 | *"Append to project-level `TECH_DEBT.md`"* — the write |
| `review.md` | 163 | skipping the triage is listed as an **anti-pattern** — the write is enforced |
| `docs.md` | 13 | *"Read `TECH_DEBT.md` — current entries"* — read as context |
| `resume.md` | 69 | *"extract accumulated items across phases"* |
| `resume.md` | **112** | **"Ignore `TECH_DEBT.md` items from previous phases"** |
| `conventions.md` | 15 | listed as a required project-root artifact |

`resume.md` reads the file at step 9 and instructs the reader to ignore most of what it read at
line 112. The obligation to write is enforced as an anti-pattern; the obligation to act does not
exist anywhere. That asymmetry is `knowledge/process.md` F30, in the canon's own words.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Population is 25, not 19; a `VERSION`-keyed census cannot see three pre-VERSION installs | none — the recount is complete and reproducible |
| 19 distinct column sets, 6 identifier grammars, 3 non-tabular files → verbatim move is the only instruction that scales; but "state the row count" has no common row grammar | how the header states a count it cannot compute uniformly — for Extract |
| H1 falsified: 6 tasks across `helpdesk` and `ai-first-devices` scope from the registry — and both consumers had first replaced the canonical shape | whether consumption survives the disposition gate — for Challenge |
| Three registries carry live non-debt payload: release gates, incident safety rules, open P0s | whether a *class* distinction can exist without becoming per-row triage (A1) — for Extract |
| `task_containers` absent in 20 of 25 → H6's destination is undefined pre-2.0.0 | the sequencing choice, D3 — for Extract |
| The migration guide is additive by design and says so; the debt retirement deletes a root file | whether deletion is required, or only canonical de-listing — for Challenge |
| Prose executes when it names a command and a check; it does not stop an agent deciding | which of D2/D5 needs a gate — for Challenge |

**Sufficiency:**
- [x] External source used? — 25 external project repositories, 7 field reports, `migrations/2.0.0.md`
- [x] Briefing gap closed? — all three guiding questions answered; question 3 produced G4, G5, G6
- [x] Dimensions identified? — six, each with ≥3 alternatives

Stage complete: YES
→ User decision: run without gates (owner, 2026-09-01). Researcher's verdict: **close the stage.**
One OODA loop, `focused` mode; no loop remains and none is needed — the counter-evidence hunt
succeeded on the first pass, which is the outcome that would have justified a second.
