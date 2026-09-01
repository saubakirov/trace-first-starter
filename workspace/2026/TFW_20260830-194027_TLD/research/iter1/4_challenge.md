# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260830-194027_TLD](../../HL-TFW_20260830-194027_TLD.md)
> Goal: a review records the debt it found in its own task and writes nothing else; the registry becomes history.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|---|---|---|---|---|
| D2 | last configured container | D3 | before the board migration | the key does not exist yet — 20 of 25 configs have no `task_containers`, and the file is still named `PROJECT_CONFIG.yaml` (G5) |
| D2 | container the reader names | D5 | agent decides silently | the field reports record the agent naming it — `task_containers` was set by the agent in the fifth run and changed by the owner afterwards (G7) |
| D1 | lift the live class out before sealing | D4 | sealed with everything else | contradiction in terms |
| D1 | lift the live class out before sealing | A1 | migration triages nothing | lifting requires deciding *where each lifted item goes* — that is disposition at migration, which A1 removed |
| D4 | prose *requires* the class be checked | D5 | prose imposes one answer | a requirement with no gate and no check is the shape `constraint.md` F3 already recorded as producing compliance theatre |
| D1 | leave in place, renamed, no move | §3.1 (frozen) | snapshot beside `BOARD-SNAPSHOT.md` | frozen contract for this repository; admissible only as receiving-project prose, never as this repo's own act |
| D6 | a derived index, generated | Principle 6 (frozen) | nothing a receiver must run | eliminated by the contract |
| D6 | nothing — the snapshot is the record | DoF 5 (frozen) | the canon must state an operation that lists open items | eliminated by the contract |

**Surviving configurations:**

| Config | D1 | D2 | D4 | D5 | Notes |
|---|---|---|---|---|---|
| **C1** | seal verbatim, warn | last configured container | sealed with the rest | prose imposes one answer | the HL as written; survives, but D2 is undefined for 20 of 25 receivers |
| **C4′** | seal verbatim, warn | **`tasks/`, beside the board snapshot** | sealed with the rest | default imposed, escape named | C4 with the destination measured rather than computed — see C-1 |
| **C6** | seal, name the class first | `tasks/` per C4′ | prose names the class, reader decides, no obligation | default imposed, escape named | the class carve-out — see C-2 |
| C2 | seal verbatim, warn | last configured container | sealed with the rest | gate asks the owner | survives; strictly better than C1 on G7 evidence, strictly worse than C4′ on G5 |
| C7 | seal, name the class first | last configured container | class check **required** | gate asks the owner | survives the pairwise check but fails C-3 below |

Eliminated: C3, C9 (fail the frozen §3.1 contract for this repository, and C4′ dominates them for
receivers — see C-1). C5, C10 (D5 incompatibility, and C10 asks the reader to search for a file that
20 of 25 do not have). C8 (A1 incompatibility). C11 (the offered task is optional by A1, so a class
that is live cannot be made to depend on it).

**Unexpected survivors:**

- **C4′** — the destination stops being a computation and becomes an observation. Nothing new is
  named, configured or computed, which is exactly what H6's closure asked for, and it works for the
  20 projects for which the current wording does not.
- **C6** — a carve-out that A1 does not forbid, because it operates on section headings rather than
  on rows. It was not in the Briefing, and it is the only surviving answer to G4.

## Findings

### C-1 — `tasks/` exists in 25 of 25, so the destination needs no config key at all

The strongest attack on C4′ is that a fallback destination weakens the −1 artifact count: a snapshot
in the project root leaves the root with the same number of files it started with. The attack lands
against the root fallback, and it is why C3 and C9 lose. But it evaporates against what was measured.

| Check | Result |
|---|---|
| Projects with a `tasks/` directory | **25 of 25** |
| Projects with `workspace/` as well | 4 — `helpdesk`, `innoforce-ai-first`, `kaznpu-ai-lab`, `robert` |
| Migrated projects, and where their `BOARD-SNAPSHOT.md` sits | 4 of 4 — `helpdesk`, `innoforce-ai-first`, `kaznpu-ai-lab`, `KZ-IT-telegram-list`, all in `tasks/` |
| Projects where "last configured container" resolves to something other than `tasks/` | **0** |

The rule the HL cites and the directory that actually exists give the same answer in every case that
can be measured — and the directory exists in the twenty cases where the rule cannot be evaluated at
all. The receiving prose does not need `legacy_container()`; it needs one sentence naming
`tasks/DEBT-SNAPSHOT.md`, beside the board snapshot the reader has just written or will write.

This changes no outcome for this repository, whose last configured container is `tasks/`. It changes
whether the instruction is executable by the majority of its audience.

### C-2 — The case against C6: "read your headings" is the camel's nose, and the answer is a closed list

The honest attack on the class carve-out is that it reopens the door A1 closed. An agent told to
*look at* its registry will read it; an agent that reads it will start judging; and the whole
economy of A1 was that nobody pays to read 121 rows.

Three things bound it, and they have to all hold or C6 should be dropped:

1. **It is O(headings), not O(rows).** 17 of 25 registries have no `##` sections at all — the
   instruction is a no-op there and costs one glance. The maximum in the corpus is 8 (`helpdesk`).
2. **The class list must be closed and non-evaluative.** *A release gate. An operating rule. An
   open incident.* Not *"important"*, not *"still relevant"*, not *"worth keeping"* — every one of
   those is merit language and would reintroduce exactly what A1 refused. `constraint.md` F3 is the
   record of what open-ended quality language produces.
3. **No obligation attached.** The prose states the class and stops. This is why C7 loses: a
   *required* check with no gate and no verifiable output is the shape that produced a filter in
   `review.md` Step 5 which watched the file grow from 1 463 to 12 352 words.

If any of the three cannot be held in the drafting, the finding still stands as a risk in §9 and the
carve-out should be dropped rather than half-written.

### C-3 — The strongest case FOR the registry, argued properly, and where it breaks

The Briefing's Challenge instruction was to argue the opposite: that the registry is the only
project-level memory of unfinished work and its loss is unrecoverable. Built on this evidence, the
case runs:

> Consumption is not absent — it is *concentrated*. The two projects that consume the registry are
> the two with real production stakes: a helpdesk serving users and a device fleet in the field.
> Every project that does not consume it is a documentation project, a prototype or a research
> repository. The registry is not dead; it is alive exactly where the stakes are, and retiring it
> optimises for 23 low-stakes projects at the cost of the 2 that carry production.

This is the best version, and it is worth stating because it is not obviously wrong. It breaks on
two facts.

**First — neither consumer uses the artefact TFW ships.** `ai-first-devices` deleted the table and
built an issue tracker: 149 per-item prose sections, stable numbers, closed items removed on sight,
a second file (`ROADMAP.md`) for deferrals. `helpdesk` sectioned by area, added release gates and a
cleanup ritual. What is alive in those projects is *their* artefact. Retiring TFW's obligation takes
nothing from them, because TFW's version of the mechanism is not what they are using.

**Second — the cost of the rebuild is on the record, in their own files.** `ai-first-devices` runs
two registries with one numbering grammar, and it has already cost a real citation failure: HL AFD-46
records *«Пропоузал ссылается на … (TD-111). **TD-111 в TECH_DEBT.md не существует** — это
`ROADMAP.md` #111»*. Its own header rules were deleted by accident and had to be restored as a DoD
item in AFD-48 Phase B. `helpdesk` pays a cleanup after every release. Both are DoF 9 in the wild —
the outlet reappearing under another name — happening *because* the mechanism was kept and improved
rather than retired.

**What survives the rebuttal.** One thing, and it must be said in the prose: **the retirement
withdraws an obligation; it does not impose a prohibition.** DoD 1 is about what the canon
*instructs*; DoF 2 is about what this task *introduces*. Nothing in the contract forbids a project
from keeping a file it finds useful. If the receiving instruction reads as *"your registry is now
history, seal it"*, `ai-first-devices` will seal a live P0 list, and that is a loss this task never
intended and cannot undo from here. One sentence prevents it.

### C-4 — DoF 10 attacked: does "not material" become the cheap default?

DoF 10 names the failure and the HL leaves the mitigation to the TS. Two pieces of corpus evidence,
pointing opposite ways.

**Against the gate.** `constraint.md` F3, 2026-04-03: *"Agents generate filler facts and tech debt
just because template sections exist."* A three-way choice with one zero-cost branch is a one-way
choice with extra steps.

**For the gate, and it is the sharper of the two.** Today the zero-cost escape already exists and is
*cheaper than the gate's*: **not writing the row at all.** Nothing counts what a review declined to
notice. The gate does not create a cheap exit; it makes the existing one visible and signed. A
written *"not material, because X"* is strictly more inspectable than silence, and the corpus shows
that outcome being written with substance when the person writing it is the person who found the
item — `aubakirov-home-assistant` row 1 carries a dated `❌ won't-fix` with three lines of reasoning
and a pointer to where the correction actually lives; `sqlrooms-demo` TD-2 carries `⛔ Won't fix —
SQLRooms abandoned`.

This does not disprove DoF 10. It reframes what the TS has to design against: not *"stop the cheap
option"* — the cheap option is already there and always was — but *"make the cheap option leave a
signature."*

### C-5 — The migration step will be executed by an agent that decides what the text implies

G7's table is the most transferable evidence in this iteration, and it applies to the retirement
without adjustment. The retirement contains two implied decisions:

| Implied decision | What the field reports predict | What removes the prediction |
|---|---|---|
| Where the snapshot goes | agent picks, owner finds out later (`task_containers`, fifth report) | C4′ — one named destination that exists everywhere, so there is nothing to pick |
| Whether to open the offered task | agent opens it, or silently does not | prose that states the default *and* names the escape, in one sentence, at the point of decision |

And one property the guide currently sells that the retirement changes: the fifth report singles out
additivity — *"Ни один существующий файл не открыт на запись; откат — удалить новые файлы"* — as the
reason the operator moved fast without taking a backup. The retirement moves a tracked file. The
move is reversible (`git mv` back, and the content is in history either way), so the loss is not of
recoverability but of the *sentence* — the guide can no longer say "nothing existing is touched", and
the step should say what rollback is instead of leaving the reader to infer it.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| `tasks/` exists in 25 of 25 and holds the board snapshot in 4 of 4 migrated projects → C4′ dominates C1 on executability and loses nothing | none |
| C6 survives, conditional on three bounds: O(headings), a closed non-evaluative class list, no obligation | drafting discipline — a TS concern, flagged for §9 |
| The best case for keeping the registry breaks on the fact that neither consumer uses the shipped artefact, and both are paying DoF 9 costs to keep theirs | none |
| The retirement withdraws an obligation and must not read as a prohibition — otherwise a live P0 list gets sealed | one sentence in the receiving prose |
| The gate's cheap exit already exists as silence; the TS problem is signature, not prevention | TS design, out of scope here |
| Two implied decisions will be taken by the receiving agent unless the text closes them | C4′ closes one; the other needs an explicit default + escape |

**Sufficiency:**
- [x] External source used? — 25 receiving projects re-queried for container layout; `AFD-46`, `AFD-48`, `aubakirov-home-assistant`, `sqlrooms-demo` read as counter-evidence
- [x] Briefing gap closed? — the opposing case was built and tested rather than asserted
- [x] Pairwise incompatibility checked? Surviving configurations listed? — 8 incompatible pairs, 5 survivors, 6 eliminations each with a reason

Stage complete: YES
→ User decision: run without gates (owner, 2026-09-01). Researcher's verdict: **close the stage and
synthesise.**
