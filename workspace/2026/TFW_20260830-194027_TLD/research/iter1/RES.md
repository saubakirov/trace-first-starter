# RES — TFW_20260830-194027_TLD: Task-local debt (iteration 1)

> **Date**: 2026-09-01
> **Author**: Claude Code (Researcher) · on behalf of `saubakirov`
> **Status**: 🔬 RES — iteration 1 complete
> **Parent HL**: [HL-TFW_20260830-194027_TLD](../../HL-TFW_20260830-194027_TLD.md)
> **Mode**: Pipeline · `focused` · run without gates at the owner's instruction, 2026-09-01

---

## Research Context

One light pass, asked for by the owner by name: look at the real projects on this machine, and find
what the debt retirement and the update path have to handle. Not an audit of this repository's 121
rows — amendment A1 forbids that work, and nothing here reads them. The subject is the receiving
projects: what their `TECH_DEBT.md` files actually look like, whether anything anywhere consumes a
registry as a live list, and what the migration text will have to say to a project we have never
seen.

The pass found three things the HL does not hold: the population it measured is incomplete and was
made so by a mechanism worth knowing about; H1 is false outside this repository, in a way that makes
the argument sharper rather than weaker; and three registries contain live content that is not debt
at all, which the retirement as drafted would file under history.

## Briefing

[`1_briefing.md`](1_briefing.md). Scope: every project carrying `.tfw/`; their registries' form,
identifier grammar and live content; their installed version and config keys; their task corpora as
evidence for or against H1; `.tfw/migrations/2.0.0.md`; the seven TFW-60 field reports. Explicitly
out of scope: this repository's 121 rows, and any per-row judgement anywhere.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | The census keys on `.tfw/`, never on `.tfw/VERSION` | Three projects — `robert`, `sqlrooms-demo`, `avtobys/business-card` — carry a complete `.tfw/` with no `VERSION` file. A `VERSION`-keyed enumeration cannot see a pre-VERSION install (G1) |
| D2 | The true population is **25**, and 25 of 25 carry a non-empty registry | Measured across `d:/projects` at depth ≤ 3, excluding two artefacts (a `.git` build tree, a test fixture). §2.8's own conclusion holds and strengthens (G1) |
| D3 | A verbatim move is the only retirement instruction that scales | 19 distinct column sets, 6 identifier grammars, 3 files that are not tables. Anything that parses has 19 shapes to get right (G2) |
| D4 | H1 splits: **H1a** (nothing consumes a *canonical* registry) confirmed in 23 of 25; **H1b** (nothing consumes *any* registry) falsified | Six tasks across `helpdesk` and `ai-first-devices` scope from registry rows. Both projects had first replaced the canonical shape. The retirement's case needs only H1a (G3, E3) |
| D5 | Three registries carry live, non-debt payload; the missing distinction is **class**, not merit | A release-gate list blocking a tag, an incident-derived safety rule for agents, an open P0 list. All three are visible at heading level, none requires reading a row (G4, E2) |
| D6 | The receiving destination is `tasks/`, measured — not "the last configured container", computed | `tasks/` exists in 25 of 25; the 4 migrated projects all put `BOARD-SNAPSHOT.md` there; `task_containers` is absent in 20 of 25 because 2.0.0 introduces it (G5, C-1) |
| D7 | The retirement is a step of `migrations/2.0.0.md`, after the payload update and after the config gains `task_containers` | The other three sequencings are each eliminated by recorded evidence: an undefined key, an `update.md` that is the version being replaced, or CHANGELOG prose (E4) |
| D8 | The retirement withdraws an obligation and must say it does not impose a prohibition | Otherwise `ai-first-devices` reads "seal your registry" and seals a live P0 list. DoD 1 governs what the canon *instructs*; DoF 2 governs what this task *introduces*. Neither forbids a project keeping its own file (C-3) |
| D9 | The receiving snapshot header states lines, words and source revision — not a row count | "Row" is undefined across 19 shapes; `wc -l`, `wc -w` and `git rev-parse HEAD` are defined everywhere and checkable in one command. This repository's own snapshot still states 121 rows correctly (E5) |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Is the population 19? | ✅ closed | No — 25. Six projects were outside the searched tree or invisible to a `VERSION`-keyed census (G1) |
| Q2 | Does the 2.0.0 board migration interact with the debt retirement in an order-dependent way? | ✅ closed | Yes, in one direction only: the destination the frozen §4 text names does not exist before the migration runs. `migrations/2.0.0.md` mentions debt zero times today (G5, G6) |
| Q3 | Is there counter-evidence to H1 — a task whose origin is a registry row? | ✅ closed | Yes, six of them, in two projects (G3) |
| Q4 | What do the field reports say about prose of this shape? | ✅ closed | Prose executes when it names a command, a path and a check. It does not stop an agent taking a decision the text merely implies — three such decisions were taken by the agent in the fifth run (G7) |
| Q5 | Anything the retirement should account for that §2 does not name? | ✅ closed | Three registries hold live non-debt content (G4); the retirement is the first non-additive step in a guide that advertises additivity (G6); the receiving row count is not computable (E5) |
| Q6 | Does the class carve-out stay bounded in practice, or drift into triage? | 🟡 open | Depends on drafting discipline, not on evidence. Three bounds stated in C-2; if they cannot be held, drop the carve-out rather than half-write it |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | Nothing consumes `TECH_DEBT.md` as a live list; no completed task's trace shows an item picked up from the registry rather than from its REVIEW | verify at TS | 🔴 **falsified as stated · confirmed as split** | `helpdesk` HD-15 (a task whose subject is verifying 40 rows, with *«агент открывает TECH_DEBT.md … сразу оценивает scope»* as its stated value), HD-26/PhaseC (read as a pre-TS gate, AC-11 gates the file mechanically), HD-11/PhaseA step 7 (triage: close 14, won't-fix 13). `ai-first-devices` AFD-13 Phase C (*"Scope (3 critical items from TECH_DEBT.md)"*), AFD-14 (#199–#204), AFD-6 (68 items), AFD-18/phase-d2 (#229, #230). **H1a** — nothing consumes a canonical flat append-only registry — holds in 23 of 25, and `resume.md:112` instructs the reader to ignore what `resume.md:69` just read |
| H3 | A receiving project can retire its own registry from prose alone, with no row lost | open | 🟢 **supported, with one named failure mode** | Five external update runs executed prose literally where it named a command, a path and a check. The recorded failure is different: three owner decisions were taken silently by the agent because the text implied them without gating them. The retirement carries two decisions of that shape; D6 removes one and an explicit default-plus-escape removes the other (G7, C-5) |
| H6 | Snapshot destination = the last configured task container | closed by the owner, 2026-09-01 | 🟡 **outcome right, mechanism undefined for 20 of 25** | `task_containers` is introduced *by* 2.0.0 and is absent from every pre-2.0.0 config, which is also named `PROJECT_CONFIG.yaml`. Measured: `tasks/` exists in 25 of 25, and 4 of 4 migrated projects hold `BOARD-SNAPSHOT.md` there. The owner's answer is correct everywhere it can be evaluated; the *rule cited for it* cannot be evaluated in 20 projects (G5, C-1) |
| H2 | All 1 659 `TD-N` citations resolve after the rename | verify at TS | ⚪ not tested | Inside this repository, one line in `compilable_contract.md`. Out of this iteration's declared subject |

## HL Update Recommendations

> The researcher classifies. The researcher never applies.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2.8 | Correct the census: population is **25, not 19**. Add the six missed projects with versions and word counts, and state the mechanism — three carry a complete `.tfw/` with no `VERSION` file, so a `VERSION`-keyed enumeration cannot see them. Note that `KZ-IT-telegram-list`, named by H3 as a field-report source, is absent from the table. Fix *"16 of 19 are on the 0.x line"* — the table lists 15; corrected spread is 5 on 2.x, 1 on 1.0.0, 16 on 0.x, 3 unversioned | G1 |
| R2 | §2.8 point 3 | *"Four projects carry rows with no `TD-N`"* → **six**, plus two more using `TD#N` / `#N` that a `TD-\d+` matcher also misses. Add the shape census: 19 distinct column sets across 24 table-carrying files, one shape recurring 5 times and 18 unique; 17 flat tables, 7 sectioned, 1 pure prose, 1 with 149 per-item sections. This makes the verbatim-move argument rest on shape rather than on size | G2 |
| R3 | §2 (new §2.9) | **Three registries carry live content that is not debt**: `helpdesk` — four rows marked `🚦 Release gate v1.7.0`, the list blocking a `git tag`; `research-yandex-cloud` — `## 🔴 Safety Rules (from incidents)`, five mandatory rules for AI agents written after an incident destroyed a VPN gateway; `ai-first-devices` — `#199`–`#204`, open P0/P1 defects. All three are visible at heading level | G4 |
| R4 | §2 (new §2.10) | **Consumption correlates with abandoning the canonical shape.** `ai-first-devices` rebuilt the registry as an issue tracker (149 per-item sections, closed rows deleted on sight, deferrals pushed to a second file `ROADMAP.md`); `helpdesk` sectioned by area with release gates and a cleanup after every release. Both consume. All 23 projects that kept the canonical flat append-only table consume nothing. The rebuild cost is on their own record: AFD-46 documents a citation that failed because two registries shared one numbering grammar (*«TD-111 в TECH_DEBT.md не существует — это `ROADMAP.md` #111»*), and AFD-48 Phase B had to restore header rules deleted by accident | G3, C-3 |
| R5 | §8 Dependencies | Add the measured container facts: `tasks/` exists in **25 of 25**; `BOARD-SNAPSHOT.md` sits in `tasks/` in **4 of 4** migrated projects; `tfw.task_containers` is absent in **20 of 25** and their config is named `PROJECT_CONFIG.yaml`. Also: `.tfw/migrations/2.0.0.md` currently mentions debt **zero times** — the order dependency is created by writing the step, not inherited | G5, G6, C-1 |
| R6 | §9 Risks | Add: **the retirement may read as a prohibition.** Two projects run their own registry deliberately. DoD 1 constrains what the canon instructs and DoF 2 what this task introduces; neither forbids a project keeping a file. If the receiving prose reads *"your registry is now history"*, `ai-first-devices` seals a live P0 list. Mitigation: one sentence — the obligation is withdrawn, nothing is forbidden | C-3 |
| R7 | §9 Risks | Add: **two implied decisions will be taken by the receiving agent.** Field-report evidence: in the fifth external update the agent set `task_containers`, chose the `team/` handle — inferring it from the git author, which `conventions.md` §4 forbids — and set `build.verify`, all because the text implied them without gating them. The retirement implies *where the snapshot goes* and *whether to open the offered task*. Mitigation: a named destination that exists everywhere, and a default stated with its escape at the point of decision | G7, C-5 |
| R8 | §9 Risks | Add: **the retirement is the first non-additive step in a guide that advertises additivity.** The fifth field report names it as the reason the operator moved fast without a backup — *«Ни один существующий файл не открыт на запись; откат — удалить новые файлы»*. The move is reversible and nothing is lost, but the guide can no longer make that claim, so the step must state its own rollback rather than let the reader infer it | G6, C-5 |
| R9 | §9 Risks | Add: **the receiving snapshot header cannot state a checked row count.** "Row" is a table line in 17 projects, an `##` heading in one, a `###` heading in another, and in `atamat` the first column is `Status`, so a `TD-`-anchored count returns zero. Mitigation: the receiving header states lines, words and source revision — defined everywhere, checkable in one command. This repository's own snapshot is unaffected and still states 121 rows | E5 |
| R10 | §10 H1 | Rewrite H1 as the split it survives as: **H1a** — nothing consumes a canonical TFW debt registry — *confirmed*, 23 of 25, with `resume.md:112` as the canon-side proof; **H1b** — nothing consumes any registry anywhere — *falsified*, six tasks in two projects. Record that the retirement's justification needs only H1a, and that the two counter-examples both bought consumption by rebuilding the artefact | G3, E3 |
| R11 | §10 H3 | Record the answer: prose executes reliably when it names an exact command, an exact path and a verifiable check — five external runs did so literally. It does not prevent an agent from taking a decision the text merely implies. The retirement's prose risk is therefore not comprehension; it is un-gated implication | G7 |
| R12 | §10 H6 | Record the mechanism gap without reopening the owner's ruling: the outcome is right in every case that can be measured, and the rule cited for it — `legacy_container()` over `tfw.task_containers` — cannot be evaluated in 20 of 25 projects. See A1 below for the proposed wording change | G5, C-1 |
| R13 | §11 | New insight, agent-measured rather than owner-stated, so flag it as such: **the mechanism was not adopted, it was replaced.** The two projects with real production stakes each rewrote the registry into a different artefact rather than using the one TFW ships. That is the strongest available statement of §2.6's diagnosis — the append is the defect — because it shows the users who most needed a debt list building their own | G3, C-3 |

### Amendment Proposals — frozen sections, owner verdict required

| # | § | Type | Proposed change | Evidence | Cost | Alternatives considered |
|---|---|------|-----------------|----------|------|------------------------|
| A1 | §4 deliverable 1 | `SUPERSEDE` | The receiving instruction names the destination **as measured, not as computed**: `tasks/DEBT-SNAPSHOT.md`, beside the board snapshot. Drop the appeal to *"the last configured task container, which `migrate_board.py` `legacy_container()` already computes"* from the **receiving-project** wording; this repository's own destination is unchanged | `tfw.task_containers` is introduced by 2.0.0 and absent from 20 of 25 configs, which are also named `PROJECT_CONFIG.yaml` (G5). `tasks/` exists in **25 of 25**; all 4 migrated projects hold `BOARD-SNAPSHOT.md` there; there is **no** project where the computed rule and the measured directory disagree (C-1) | One sentence rewritten in §4 and in the migration step. No outcome changes for any project that can be measured today | (a) Keep the computed rule and sequence the retirement after the migration — rejected: it still names a key to a reader who may run the step from a 0.x checkout, and the fifth field report shows what an agent does with an unresolvable implication. (b) Fall back to the project root — rejected: it leaves a file in the root and forfeits the −1 count. (c) Ask the reader to name a container — rejected: D5 evidence says the agent names it. **Granularity note for the coordinator:** the declarative claim *"the snapshot goes beside the board snapshot, in the legacy container"* is unchanged; only the justification offered for it moves. If §3 rule 15's granularity rule puts the justification below the frozen unit, this is a Refinement to §4 and needs no verdict |
| A2 | §5 DoD 13 · §4 deliverable 1 | `EXTEND` | The retirement adds a **class check at heading level, with no obligation attached**: before sealing, the reader looks at their own section headings, and the prose names a closed list of things that are not debt — *a release gate, an operating rule, an open incident*. A gate is a task; a rule is knowledge; everything else seals unread. DoD 13's *"reads no row and judges no row"* is preserved verbatim and the new sentence says so explicitly | Three of 25 registries hold live non-debt content today: a release-gate list blocking `git tag v1.7.0` (`helpdesk`), five mandatory incident-derived rules for AI agents (`research-yandex-cloud`), open P0/P1 defects (`ai-first-devices`) (G4). The retirement as drafted files all three under *"sealed unexamined … age is not evidence of importance"* | Bounded by heading count: 0 in the 17 flat-table projects, 8 at the corpus maximum. Costs one paragraph of prose and one glance from the reader. Reopens nothing A1 closed: the check is O(headings), the class list is closed and non-evaluative, and no obligation is attached | (a) Seal everything, accept the loss — rejected: sealing a live safety rule and a release blocker is a loss the task never intended and cannot undo from the framework side. (b) Require the check — rejected as C7: a requirement with no gate and no verifiable output is the shape of `review.md` Step 5's filter, which watched the file grow 8×. (c) Lift the live class out before sealing — rejected: relocating each item is disposition at migration, which A1 removed. (d) Let the offered follow-up task inherit the class — rejected: that task is optional by A1, so live content cannot depend on it |

> A2 is the one place this iteration argues against the drafted contract, and it argues narrowly.
> A1-the-amendment refused **merit** judgement — reading rows and scoring which deserve a task. A2
> asks for **class** recognition, which is read off the table of contents. If the coordinator judges
> that the distinction cannot be held in drafting, the finding should land in §9 as a risk and the
> carve-out should be dropped rather than half-written (C-2).

## Fact Candidates

**No fact candidates.** Everything this iteration found is agent-discoverable by reading files and
running counts, which is the Human-Only Test's definition of *not* a fact candidate. The findings
belong in HL §2 as refinements R1–R4, where they are already classified.

## Strategic Insights (Research)

**No strategic insights.** The only owner input this iteration was the instruction to run without
gates (recorded in `1_briefing.md` § User Direction). R13 records an agent-measured pattern and is
deliberately filed as a §11 refinement flagged as agent-sourced, not as a human-sourced insight.

## Findings Map

**H1, and where it actually holds.**

```text
                     "Nothing consumes TECH_DEBT.md as a live list"
                                        │
                    ┌───────────────────┴───────────────────┐
                    │                                       │
              H1a — canonical shape                   H1b — any registry
        flat append-only table, as review.md          anywhere, any shape
                  prescribes it                                │
                    │                                          │
              ✅ CONFIRMED · 23 of 25                    🔴 FALSIFIED · 2 of 25
                    │                                          │
      zero task traces scope from it             helpdesk ── HD-15, HD-26, HD-11
      resume.md:69 reads it                      ai-first-devices ── AFD-6, 13, 14, 18
      resume.md:112 says ignore it                             │
      docs.md reads it, acts on nothing            both replaced the canonical shape FIRST
                    │                                          │
                    │                              ai-first-devices → issue tracker
                    │                                  + a SECOND registry (ROADMAP.md)
                    │                                  → AFD-46: a TD-N citation that
                    │                                    resolved to the wrong file
                    │                              helpdesk → area sections + release
                    │                                  gates + cleanup every release
                    │                                          │
                    └──────────────► the retirement needs only H1a ◄──────────┘
                                     H1b's falsity locates the case, not weakens it
```

**What the retirement must handle, by where it is visible.**

```text
                          a receiving TECH_DEBT.md
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
   heading level              row level                   file level
   (25 files: 0–8 headings)   (121 rows here, 19 shapes)  (always one file)
        │                           │                           │
   ┌────┴────┐                      │                     ┌─────┴─────┐
   │         │                 ✋ A1 REFUSES          destination     count
release   safety rule          read no row            tasks/         lines·words·rev
 gate     open incident        judge no row           25 of 25       "rows" undefined
   │         │                      │                 (C-1, A1)      across 19 shapes
   └────┬────┘                      │                                (E5, R9)
        │                           │
   A2 asks for THIS ────────────────┘
   O(headings), closed list,         and nothing more
   no obligation
```

## Iteration Status

- **Iteration:** 1 of 1 (min) / 2 (max), per `research/iterations.yaml`
- **Hypotheses tested:** H1 (falsified as stated, confirmed as H1a), H3 (supported, one named failure mode), H6 (outcome right, mechanism undefined for 20 of 25)
- **Hypotheses deferred:** H2 — a one-line check inside this repository, outside this iteration's declared subject; it belongs to the TS as HL §10 already says
- **Gaps discovered:** the census population and its selection mechanism (R1); three registries holding live non-debt content (R3); the non-computability of a receiving row count (R9); the additivity property the retirement breaks (R8)
- **Superseded decisions:** none. D6 refines H6's mechanism without disturbing the owner's 2026-09-01 ruling on the outcome

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | Q6 — can the class carve-out (A2) stay at heading level in drafting? | If it drifts into row reading, it becomes the analysis A1 refused, at receiving-project scale | Not a research question. It is answered by writing the paragraph and testing it against `helpdesk` (8 headings) and `optimization-report` (prose, no table). A TS drafting exercise, not an iteration |
| 2 | H2 — citation resolution after the rename | DoF 3 forbids a citation ceasing to resolve | One line in `compilable_contract.md` §2. HL §10 already routes it to the TS |

> Neither thread justifies a second iteration. Thread 1 is drafting, thread 2 is inspection — the
> same standard the coordinator applied on 2026-09-01 when overriding `min_iterations`.

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [ ] MORE NEEDED
- [ ] BLOCKED

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

One pass over 25 receiving projects, their configs, their task corpora, the 2.0.0 migration text and
seven field reports. It confirmed the retirement's central claim and broke three of its supporting
ones. The claim that survives is the one that matters: no project consumes a canonical TFW debt
registry, and the canon's own `resume.md` reads the file at step 9 and tells the reader to ignore it
at line 112. What broke: the census is 25, not 19, and was made 19 by keying on a file three
projects do not have; H1 is false as written, because two projects do scope tasks from their
registry — having first rebuilt it into something else and paid for the rebuild in a failed citation
and a standing cleanup ritual; and the destination the frozen contract computes cannot be computed
by 20 of 25 receivers, though the directory it resolves to exists in all 25. The finding nobody
asked for is the one I would defend hardest: three registries hold a release blocker, an
incident-derived safety rule for agents, and an open P0 list, and the retirement as drafted files
all three under *"sealed unexamined, age is not evidence of importance"*. That is worth one
paragraph of prose at heading level — and nothing more, because A1 is right that reading rows is the
work this task exists to stop paying for. **Self-critique:** the strongest thing here — H1's
falsification — was reachable from this repository alone by grepping two sibling projects, and the
HL deferred it to the TS as *"one pass over the closed rows"*; had the TS been written first, the
counter-example would have surfaced during drafting and cost more. Against that, this pass did not
open a single one of the 121 rows, did not test H2, and leaves Q6 answerable only by writing the
paragraph it proposes.

---

*RES — TFW_20260830-194027_TLD: Task-local debt (iteration 1) | 2026-09-01*
