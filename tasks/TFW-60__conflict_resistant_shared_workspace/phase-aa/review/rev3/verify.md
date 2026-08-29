# Verify — revision 3 — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact — and for this pass there is no RF,
> so every claim below was taken from the commits, the evidence files and the code itself.
> Earlier passes stand: [`../verify.md`](../verify.md) · [`../rev2/verify.md`](../rev2/verify.md)
> **Counts deliberately not re-litigated** (owner's instruction). `census_r4.md` raised the two
> methods before acting; that is recorded, not reopened.

## Part 1 — the architectural change

### V1: is removing `actor` right, or is it a capability being dropped?

- **Claim:** the field answered nothing. **Verified at both corpora, read-only.**
  Upstream, 21 consecutive events carry the same value in `actor` and `on_behalf_of`. In the
  consumer it is `via` plus a session number. The field never carried an independent fact — it
  restated one of the other two.
- **The load-bearing question:** the frozen master HL §3.1 says a team must be able to answer
  *"who/what acted"* six months later. Two questions, and the surviving fields answer exactly
  two: `on_behalf_of` — who — and `via` — what. The **three**-field model was the one that
  over-claimed; the two-field model is closer to the frozen text, not further from it.
- **What is genuinely given up:** telling two concurrent sessions of one tool apart *inside the
  journal*. That was never delivered — it is what forced the per-session profiles — and Git
  commit attribution (D55, `[agent/task/scope/role]`) still answers it where it was always
  answered. The canon says the gap is open and names TFW-54 as its owner rather than papering it.
- **Match:** ✅ — and this is the right call, not merely a permitted one

### V2: does the fix cost any project data or work?
- **Claim** (`ac15_actor_tolerated.txt`): an already-written `actor` is tolerated, never
  rewritten; both consumers unchanged
- **Re-measured by me, read-only, against the live project:** under the code shipped at
  `2.0.0-dirty.2`, `innoforce-ai-first` reports *"2 problem(s) across 15 tasks"* — two events
  naming session handles whose profiles were deleted. Under the current code the same bytes give
  **"15 tasks validate against the closed schema."** `git status --porcelain` in that project:
  **empty**, before and after my reads
- **Match:** ✅ — a permanently-red gate in a live external project goes green with **zero bytes
  changed in that project.** That is the strongest single argument in the pass, and it is
  measured rather than asserted

### V3: is the removal complete?
- Grepped every instruction surface — payload workflows, templates, canon, glossary, migration
  guide, and the whole adapter layer. **Every surviving `actor` is prose narrating the
  retirement** (canon §4, the event template, `bindings.yaml`'s comment, the migration guide's
  *"change nothing"* paragraph). Zero live instructions to write the field
- It took **two** commits: `5e9b0a1` removed it from the canon and the release surface and
  missed eight workflows; `b75bef1` caught them. The executor's own note is accurate and
  unflattering — *"third occurrence of this class in this task, and the first where the
  measurement was already written down before the miss"*
- **Match:** ✅ complete now, and the class is in a registry rather than in memory

### V4: the token
- Four hex characters; re-draw on collision; the clock read **once** and never incremented —
  with the reason recorded (an arithmetic successor once wrapped `23:59:59` to `00:00:00`
  keeping yesterday's date). The invariant is stated as an invariant: *"If it ever acquires a
  second job, it is the wrong mechanism"*
- **Match:** ✅ — the mechanism matches the single job it declares

## Part 2 — the other eleven items

| Item | Verified | Result |
|---|---|---|
| 2 — no agent profile; the refusal names what to use | `PROVIDER_FAMILIES` **deleted**, not documented: with `actor` gone its only reader has no subject. The comment states the reasoning where the set used to be | ✅ better than specified |
| 5 — Step 6 gains the Claude Code row | Row 1 of the table, with the omission's cost recorded: *"both adapters are byte copies of the same workflows, only one was listed, and the unlisted one rotted"* | ✅ |
| 6 — no retired vocabulary in the adapter layer | `grep -rl 'Task Board' .claude .agent .agents AGENTS.md CLAUDE.md` → **0 files**. And the step takes its terms from the CHANGELOG rather than inlining them, *"an instruction that inlines the term it searches for becomes a hit on itself the moment it is copied into the layer being checked"* | ✅ sharp |
| 7 — `bindings.yaml` ships with its schema | `.tfw/templates/bindings.yaml`, and `update.md`:120 writes it **when the second profile appears** — the branch the report identified as running forever otherwise | ✅ |
| 8 — per-phase journals | `read_journal` walks `journal_dirs(task_dir)`, and a phase event is reported as `phase-a/journal/<name>.md` so a problem names a file the reader can find | ✅ the detail matters |
| 9 — `installed_from` | `update.md`:183 at Step 7, `templates/project_config.yaml`:17 defaulting to `unrecorded`, this repository's own set to `self` | ✅ |
| 10 — path check in three reference forms | `r4_gates.txt`: *"every path any payload file names, in all three reference forms — unresolved: none."* I replayed the equivalent independently in revision 2 and it is the gap that had let two defects live four releases | ✅ closes TD-193, TD-194 |
| 11 — §10.4 fixed as a rule, not an example | Two rules: a template carries its artifact's name; everything else is `lower_snake_case`. Gate output: **20 templates, 0 contradicting.** The canon records the refusal of the small fix explicitly | ✅ **my revision-2 objection honoured, not overridden** |
| 12 — the adapter README | The retracted sentence is gone; copies are declared the model, with two mechanisms named that make it true rather than hopeful | ✅ |

## Part 3 — AC-13 half two, ruled

The executor left E51 **DEFERRED** and routed the ruling here — correctly, and the EV says so:
*"whether the phase's declared outcome is thereby met is a reviewer's and the owner's ruling,
not the executor's to grant itself."*

**Independently verified against the live project, read-only, changing nothing:**

| The TS's three bullets | Measurement |
|---|---|
| a real external project, updated by its own operator | `innoforce-ai-first`, a different project and a different session, with no access to this phase's reasoning. Its report is its own document, filed verbatim |
| **zero files hand-carried** | 68 payload files at `v2.0.0-dirty.2`: **0 missing, 0 stray** in the consumer |
| **zero edits inside `.tfw/`** | 65 of 68 byte-identical. The three that differ are `CHANGELOG.md` (one commit behind — the run started before the tag's record was written), `knowledge_state.yaml` (⚫ project state, never overwritten) and `project_config.yaml` (🟡 part-project, merged). **No framework file was edited** |
| every delta the first consumer had to invent is unnecessary | board flags shipped, `team/README.md` withdrawn, tooling inside the payload — all three confirmed by the run |
| the run records what was confusing, not only what worked | five findings, four of which became AC-15 items |

`--check tasks` on that project with current code: **15 tasks validate.** `--check project`:
consistent. `git status --porcelain`: **empty** — my verification wrote nothing.

**Ruling: AC-13 half two is MET.** The findings it returned are what the criterion *asked for*
— it requires the run to record what was confusing — not evidence that it failed. And the
regress has to be named: `b75bef1`'s message says half two *"closes on a third external run."*
It does not. Requiring a fresh external run to certify each correction the previous run
produced defers the phase forever. DoD 19 says *an* external project completes the update from
the payload alone. One did, and I measured it.

## Commands Executed

| # | Command | Result |
|---|---|---|
| 1 | `pytest .tfw/scripts/ docs/scripts/ -q` | **260 passed, 1 skipped** — matches `r4_gates.txt` |
| 2 | `mkdocs build` | exit **0** |
| 3 | `--check index` · `tasks` · `project` | exit **0** each |
| 4 | retired-term grep over the adapter layer | **0 files** |
| 5 | payload diff of the live consumer against `v2.0.0-dirty.2` | 68 files, **0 missing, 0 stray**, 65 identical, 3 project-owned |
| 6 | `--check tasks --root <consumer>` under current code | **15 tasks validate** (was 2 problems) |
| 7 | `git status --porcelain` in the consumer, before and after | **empty** — nothing written to a project that is not ours |
| 8 | `actor` grep over every instruction surface | only retirement narration remains |
| 9 | workflow word counts, at `a0d22c5` → HEAD | see D3 below |

## Discrepancies Found

| # | Discrepancy | Severity |
|---|---|---|
| **D1** | **No RF for this pass.** Header says revision 2, cites TS revision 3, and the §3 table has no AC-15 row. The largest architectural change of the phase — a carrier-schema and filename-grammar change reaching the canon, eight workflows and their sixteen copies — has no executor declaration of what was done, what was decided or what was verified. The three evidence artifacts exist and are **not indexed in the EV** | **High** — blocking |
| **D2** | **The TS mandates in AC-15 what it forbids in §1, §7, §8 and §9.** §1 *"The model itself does not change… no carrier, schema… is touched"*; §7 *"❌ The model changed: any edit to a carrier schema, the event grammar…"*; §8 *"A finding about the model is filed, not fixed here"*; §9 *"changes no carrier they will extend."* The *"Why no amendment"* box answers the **master HL** §5/§6 and never touches the TS's own four statements. An executor reading §7 and AC-15 receives opposite orders | **High** — blocking, **coordinator's** |
| **D3** | `.tfw/VERSION` and `tfw.version` say **`2.0.0-dirty.3`**; the CHANGELOG's newest entry is `[2.0.0-dirty.2]` and `[Unreleased]` says *"Nothing pending."* **Eight payload files** tell a reader about `2.0.0-dirty.3` — the canon, the glossary, the migration guide, the event template, the adapter README. A project reading *"the actor field was removed at 2.0.0-dirty.3"* and turning to the changelog finds no such release. This is AC-14's own criterion, and the inverse of the defect the phase exists to remove | **High** — blocking |
| **D4** | **`update.md` 1165 → 1380 words against the §11 ceiling of 1200.** The one workflow this phase had deliberately brought *under* the ceiling (D9, by deleting duplication rather than content) is now 15% over. `r4_gates.txt` flags it and points at an RF that does not exist. `handoff`, `init`, `plan` and `review` are also over — all four were over before this pass and moved by +18…+38; `update.md` is the one this pass pushed across | **Medium** |
| **D5** | `via` is now validated by **nothing** — `PROVIDER_FAMILIES` was deleted — while the canon still states it as an enumeration, *"provider family — `claude`, `codex`, `gemini`"*. Under the project's own **Structural Enforcement** value, a rule that cannot reveal its own violation is advice. Either say `via` is free-form provider text, or check it | Low |
| **D6** | The second consumer **rewrote 12 command files from copies to thin adapters**, on the strength of `adapters/claude-code/README.md`'s *"Commands never duplicate workflow content — they reference it."* Item 12 deletes that sentence and declares copies the model. Nothing tells that project the rule it acted on has been retracted, and its thin adapters now diverge from the framework's declared shape | Medium |

**Escalation not required by rule** — the earlier passes ran at 100% and this pass was verified
end to end, including read-only measurement inside a live third-party project.

## Evidence Verification

| Artifact | Exists? | Matches claim? |
|---|---|---|
| `census_r4.md` | ✅ | ✅ measured at `fd85b7c` before the first edit; raises both counting methods and the appearing group **before acting** |
| `r4_gates.txt` | ✅ | ✅ every gate reproduced by me. It also self-reports the word-ceiling breach, which is the right instinct pointed at a missing document |
| `ac15_actor_tolerated.txt` | ✅ | ✅ re-measured independently against both live corpora |
| `second_consumer_manifest.md` | ✅ | ✅ |
| `FIELD-REPORT__…__second_external_update.md` | ✅ | ✅ filed verbatim, header note declares it filed-not-authored, no journal event — which is this phase's own canon applied, not an omission |
| **EV rows for AC-15's twelve items** | ❌ | **absent** — see D1 |

## Knowledge Citations Verified

No new citations. HL §7.2 and ONB §7 unchanged; 33 of 33 verified across the earlier passes.
Two baseline items were re-read because R4 turns on them, and both **support** the change:
§3.1's *"who/what acted"* is two questions and now has exactly two fields, and §7.2 citation 14
(PV 3 — D59, *"a session is not an independent person"*) is precisely the boundary the
per-session profiles violated.

## Checkpoint

**Self-check:**
- [x] Opened files and recorded findings? — canon, event template, `bindings.yaml`, `update.md`, the adapter README, `gen_index.py`'s identity and journal code, all three evidence artifacts
- [x] Ran build/test commands? — nine, including read-only measurement inside a live external project
- [x] Claim & Source checks — every R4 claim re-derived rather than accepted; the field report's own numbers checked against the project
- [x] Each AC verified against the actual file? — AC-15's twelve items individually; AC-13 half two ruled with independent measurement
- [x] KNOWLEDGE.md checked — D55 and D59 bear directly on the identity change and both hold
- [x] Evidence artifacts verified — four present and accurate, **EV indexing absent**

Stage complete: YES
