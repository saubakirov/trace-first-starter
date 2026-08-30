# ONB — TFW-60 / Phase AC: Update Without Guesswork

> **Date**: 2026-08-30
> **Author**: Claude Code (Executor), `on_behalf_of: saubakirov`, `via: claude-code`
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-60](../HL-TFW-60__conflict_resistant_shared_workspace.md) at `56c3d70`
> **Phase HL**: [HL Phase AC](HL__phase-ac__update_without_guesswork.md)
> **TS**: [TS Phase AC](TS__phase-ac__update_without_guesswork.md) — approved at revision 1
> **Origin read**: [fourth](../FIELD-REPORT__TFW-60__fourth_external_update.md) and [fifth](../FIELD-REPORT__TFW-60__fifth_external_update.md) field reports, every defect and §6
> **Predecessor read**: [Phase AB RF](../phase-ab/RF__phase-ab__honest_migration.md), REVIEW revision 2, and its `four_corpora_compatibility.txt`
> **Measured at**: `b9baec2` (TS approval), 2026-08-30 15:30. The working tree carries unrelated TFW-55 research and an `ASSISTED15` review; both stay out of every commit of this phase.

---

## 1. Understanding

Phase AC removes every place where the update path guesses or decides for the owner, in one release
surface. Five text carriers change (`update.md`, `plan.md`, `init.md`, `conventions.md`, `glossary.md`,
the HL, event, profile, status and config templates, the migration guide, `RELEASE.md`, the CHANGELOG,
two adapter templates) and two scripts change in one function each: `migrate_board.classify_status()`
learns to refuse a status cell carrying a second lifecycle signal, and `gen_index.check_tasks()` learns
to name a phase directory that has no state. Nothing is renamed, no key is added, no grammar changes.
Evidence is a fixture per behaviour and one measurement per gate, at a pinned commit.

Baseline confirmed before writing this file:

| Check | Measured |
|---|---|
| `python -m pytest .tfw/scripts/ docs/scripts/ -q` | **283 passed, 1 skipped**, 140 s |
| `--check tasks` · `--check project` | 54 tasks validate · consistent |
| `v2.0.0-dirty.4` → `51677ff` · `HEAD` → `b9baec2` · `VERSION` at tag | `2.0.0-dirty.4` — `HEAD` is ahead of the tag, which is exactly AC-1's live-source case |
| `update.md` word count | 840 |
| Workflow copies (`.claude/commands`, `.agent/workflows`) for update/plan/init | byte-identical |
| Phase directories without `status.md` | **17**, under TFW-42 (3), 46 (3), 47 (2), 52 (2), 53 (5), 55 (2); none of the six carries a task-level `status.md`; all six read terminal on the board snapshot — the TS figure holds |
| Retired-vocabulary hits outside the allowlist as worded today | 6 — `update.md:69`, `init.md:123`, four copies — the set both reports name |
| Markers in `CLAUDE.md.template` · in this repository's `CLAUDE.md` | 0 · 0 |
| Consumer corpora available locally | `innoforce-ai-first`, `kaznpu-ai-lab`, `helpdesk` — all on `.4`, all with `tasks/BOARD-SNAPSHOT.md`, all with `installed_from` written as a `D:/` path |

## 2. Entry Points

| Surface | Where | What changes |
|---|---|---|
| Pin | `update.md`:11–31, :83–91 | `source_head` derived from `target_ref^{commit}`; `VERSION` read from it and compared with the tag name; Step 5 recheck against the derived commit |
| Owner gate · briefing | `update.md`:63–73 (Step 3), new Step 8a; new `templates/briefing.md` | three questions before the first durable write; briefing from `Added` / `Fixed` / `Removed` |
| Copy exclusions | `update.md`:80–91 (Step 5) | `project_config.yaml`, `knowledge_state.yaml` never overwritten; the step prints what it skipped |
| Step 6 rows | `update.md`:99–107; `adapters/claude-code/CLAUDE.md.template`, `README.md`; `adapters/antigravity/tfw-rules.md.template`, `.agent/rules/tfw.md` | copy vs marker-bounded block per row; `TFW:CLAUDE` markers; `{version}` → `see .tfw/VERSION` |
| Provenance form | `update.md`:117–121; `templates/project_config.yaml`:13–17; `gen_index.check_project()` | `{upstream}@{verified-tag}`; a machine-local value reported, never rewritten |
| Status cell | `migrate_board.classify_status()`:162–181, `plan()`:865, `render_manifest()`:735–760 | whole-or-`UNDECLARED`; own manifest heading; phase directories named |
| Missing phase state | `gen_index.check_tasks()`:1186–1221, `iter_phase_dirs()`:464 | failure on a live task, informational line otherwise |
| Abbreviation | `conventions.md`:229–262, :369–398; `plan.md`:38–42, :55–72; `init.md`:113–114, :136–143; `glossary.md`:120; `templates/HL.md`:1–5 | initials of the approved title, proposed and approved with it |
| Release reach | `CHANGELOG.md` `.3` entry, `:297`, `:200–265`; `RELEASE.md` §5–6 | intervening-section pointer, verbatim retired quote, superseded-by marker, dead `TD-11` reference |
| Carriers | `templates/journal/event.md`:49, :70; `templates/team/profile.md`:12–16, :29–34; `templates/status.md`; `migrations/2.0.0.md`:59–64, :94, :39–40 | `via` free-form; one file per person and where a role goes; phase paragraph; one manifest location, `--working-tree`, commands from the root |
| Tests | `test_migrate_board.py`, `test_gen_index.py`, `docs/scripts/test_integration.py`:510–580 | `AILAB-2` fixture (two signals tested separately), phase-state check, markers, exclusion list |

**Census, measured at onboarding:** the TS table's 23 counted paths are confirmed path by path;
1 new (`templates/briefing.md`); copies excluded per S32; ONB/RF/EV excluded per S46. One path the
table does not name is raised as Q2 below (`+1` if admitted → 24 counted, inside `50 / 50 / 5000 / 50`).

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | **Which Unicode symbols count as a second status signal?** AC-8 says *"no further status symbol (Unicode category S)"*. I ran that rule against the four pinned corpora **before writing any code**; the table below is the measurement. Under the literal rule, 11 rows change classification, and **three of them change on a plus sign or an arrow alone**: `TFW-52` `✅ DONE (… blocked → TD-126)`, `HD-30` `✅ DONE (… +1 UX TD-271)`, and `HD-31` — a **live `ONB` task** — on `A+B`. Category **S** contains four classes: `So` (other symbols — every emoji marker lives here: ✅ ❌ 🔄 🟢 🟡 ⬜), `Sm` (math: `+ = < > →`), `Sc` (currency), `Sk` (modifiers). `Sm`/`Sc`/`Sk` are prose punctuation on every board measured; `So` is the only class a person uses as a status marker. **Options:** (A) the TS as written, category S entire — 11 flips, three of them false refusals of plainly single-signal rows; a re-migration of this repository's own board would write `UNDECLARED` state for the closed `TFW-52`. (B) **recommended:** the rule names `So` — 8 flips, every one carrying either an emoji or a second declared token; `TFW-52`, `HD-30`, `HD-31` keep their reading; the TS sentence changes by one word (*category So*) and the fixture tests `→` as a non-signal. (C) a symbol counts only when adjacent to a token (`✅ APPROVE`) — rejected by me: that is the "closed phases then a live one" heuristic §6 forbids. The cost of choosing after the fixture is committed is one REVISE round. | _{coordinator fills in}_ |
| 2 | **Does `.tfw/adapters/cursor/tfw.mdc.template` enter the census?** AC-4 states *"the Claude rules and Codex routing rows are blocks, the rest are copies"*. The Cursor template carries `{version}` three times, exactly the TD-204 defect the Antigravity template has — so its row is neither a whole copy nor a marker block, and the Step 6 table cannot say what AC-4 requires it to say without either fixing the template or labelling the row. **Options:** (A) **recommended:** admit the path — same fix as TD-204 (`{version}` → *see `.tfw/VERSION`*), Cursor row becomes a whole copy; `+1` counted path, 24 of 50, no ruling needed under DoD 16. (B) leave it: the Cursor row reads *"rendered template — verified by reading"* and the defect is filed in RF §6 for the reviewer; AC-4's *"every row executable the same way"* then holds for six rows of seven and says so. | _{coordinator fills in}_ |

Status-cell measurement behind Q1 — four corpora, the committed `BOARD-SNAPSHOT.md` of each, current
`classify_status()` versus the AC-8 rule under both readings:

| Corpus | Rows | Flips, category S | of which on `+`/`→`/`=` **alone** | Flips, `So` only |
|---|---:|---:|---:|---:|
| framework (`tasks/BOARD-SNAPSHOT.md`) | 61 | 2 — `TFW-48` (🟡 in prose), `TFW-52` (`→`) | 1 | 1 |
| innoforce-ai-first | 17 | 1 — `INNO-9` (`RF`, `DONE`, ✅ in prose) | 0 | 1 |
| kaznpu-ai-lab | 4 | 1 — `AILAB-2` (the fifth-report row) | 0 | 1 |
| helpdesk | 32 | 7 — `HD-15/16/22/23` (✅ 🟢), `HD-19` (`KNW`), `HD-30` (`+`), `HD-31` (`+`) | 2 | 5 |
| **Total** | 114 | **11** | **3** | **8** |

Every `So` flip is a row a person would also read as carrying two signals. `TFW-48` is instructive:
`❌ REJECTED — … (last live status was 🟡 TS (D))` — the board author quoted a previous status inside
the outcome; refusing it is correct by the rule and costs one `transition` event from the owner if
ever re-migrated. The three `Sm` flips are not that: nobody reads `A+B` as a status.

## 4. Recommendations (suggestions, not blocking)

1. **AC-7 executor decision — the exclusion list carries both files; the payload keeps carrying
   `knowledge_state.yaml`.** Reason: the only way to stop the payload carrying it is a root
   `.gitattributes` with `export-ignore` — a new root file outside the TS census that governs `git
   archive` only; a receiver that copies a local checkout would still get the file. The exclusion list
   sits beside the copy step, covers every materialization, and is what the payload test can enumerate.
   Recorded in the RF as the TS requires. If the coordinator prefers the smaller payload, say so here
   and I will raise the `.gitattributes` path for the census instead.
2. **AC-4 block boundary in `CLAUDE.md.template`:** markers bound the `## TFW …` section — context
   loading, slash commands, templates, key references — because that is the part a release changes.
   Project identity, the five mandatory rules, execution mode and code standards stay outside as
   project-owned text. `{version}` inside the block becomes *Version: see `.tfw/VERSION`* (the TD-204
   form), otherwise the block can never be compared by `cmp`.
3. **This repository's own `CLAUDE.md` is left without markers** — it is not in the census, it is far
   richer than the template, and the first-run rule then applies to us as to any consumer: the update
   *reports* it. The RF states that plainly instead of inserting a block nobody asked for.
4. **TD-198's mechanical form:** add the retired sentence *"Commands never duplicate workflow content —
   they reference it"* as a row of `RETIRED_WORDINGS` in `test_integration.py`. The registry's own
   comment says to add a row whenever a release replaces a normative wording, and this one was skipped
   at `.3`. It scans the installed adapter surface (`CLAUDE.md`, `AGENTS.md`, copies), which is
   precisely where the fourth report found the stale principle. `.tfw/adapters/claude-code/README.md`
   quotes the sentence in a blockquote and is outside both scans, so the row is safe. Inside the Tests
   group; no new path.
5. **AC-1's failing run happens in a scratch clone.** A fabricated tag whose `VERSION` disagrees with
   its name is a durable ref; it is created in a clone under the scratchpad, never in this repository.
   Commands and output go verbatim into `evidence/pin_on_live_source.txt`.
6. **AC-8 before/after evidence at pins, not working trees:** each consumer's snapshot is read with
   `git -C {consumer} show {pin}:tasks/BOARD-SNAPSHOT.md` at the commit its own `installed_from`
   update landed on (`01ec75b`, `018a194`, and helpdesk's), so the comparison is reproducible.
7. **`--check tasks` on a phase directory without state when the task's own `status.md` is malformed:**
   informational, not a second failure — the malformed state is already the failure, and a gate cannot
   read whether the task is live. Stated in the message so nobody reads the silence.
8. **`--check project` on `installed_from`:** report when the value starts with `[A-Za-z]:`, `/` or
   contains `\`; `self` and the template's `unrecorded` stay valid; a URL (`https://…@v…`) passes.
   The message is *machine-local; record the upstream reference* and nothing is rewritten.
9. **Word ceiling:** the four additions (−1, 3-gate, 5-exclusions, 8a) plus a Step 6 column are
   roughly 300 words against a 360-word margin. Duplication removed first: Step 3's `team/` paragraph
   folds into the gate, Step 5's two-line recheck becomes one line against the derived commit, Step 8's
   verification list stops repeating Step 6. The count is measured after every edit and is an AC gate.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **A second declared token in outcome prose is a signal by the rule** — `HD-19` `✅ DONE (KNW
   deferred …)` and `INNO-9` flip on words (`RF`, `DONE`, `KNW`) used as vocabulary inside prose. The
   rule is what the TS asks for and it is the conservative direction; the fixture will test a token
   alone (no emoji) so the behaviour is deliberate, not incidental. The manifest heading names each
   such row, which is the control §8 already gives.
2. **Variation selectors and joiners.** `✅` often arrives as `U+2705 U+FE0F`; `U+FE0F` is category
   `Mn`, not `S`, and today's code strips it by literal. The new scanner must skip `U+FE0F` and
   `U+200D` explicitly or a bare selector after the first token would be neither symbol nor text.
   Covered by a fixture row.
3. **`UNDECLARED` rows now receive `status.md` where they received nothing before.** For a terminal
   row carrying a stray emoji this is a new file at `UNDECLARED` on a closed task. That is the TS's
   intent (never terminal by the first token) and conventions §5 gives the resolution; the manifest's
   *Task state written* note will say so in one sentence. Already-migrated projects are untouched.
4. **Step −1 is unreachable for a receiver on 1.x by construction** — its installed `update.md` cannot
   carry it. The TS already routes it through the migration guide's *Updating from 1.x* position and
   the CHANGELOG; I will also put it in the new entry's updating section so a `.2`–`.4` receiver,
   whose installed workflow lacks Step −1 too, meets it in the first file the release tells them to open.
5. **The briefing's inputs are the intervening entries' `Added` / `Fixed` / `Removed` sections.** The
   `.3` and `.4` entries have no `Removed` section, and `.2` has `Changed` and `Canon`. The template
   must say what to do when a section is absent (the block says *nothing in this release* rather than
   inventing content) and must not read `Changed` — that is the free text the risk table forbids.
6. **`check_tasks` output grows by 17 lines on this repository.** They are informational, printed to
   stdout, exit code unchanged. A consumer piping the gate into a CI log sees them once per run; that
   is the report the fifth report asked for, stated once per directory.
7. **The TFW-55 directory is live in the working tree while its board row reads `DONE`** —
   `research/iter2/` is uncommitted and `iterations.yaml` modified, with no `status.md` at task or
   phase level. Under AC-8 its two stateless phase directories are *informational*, which is correct
   by the rule; but the rule's premise ("a terminal legacy task is history") is not true of TFW-55.
   Out of my scope; recorded here so the coordinator sees it before the reviewer does.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS AC-4 says the Codex adapter's first-run rule is *"reported and left untouched"*.** The Codex
   README step 3 actually says: *"If it has no markers, append the complete block."* Codex appends;
   the TS asks Claude to report. I follow the TS — a hand-edited `CLAUDE.md` with an unmarked TFW
   section would otherwise carry two — and the RF will word the Claude README rule as its own, not as
   "the Codex rule restated".
2. **Cursor row** — see Q2. The TS census names the Antigravity template and its rendering but not the
   Cursor template, which has the same three `{version}` placeholders.
3. **TS §4 cites `plan():863` for the terminal skip**; it is `:865` at `b9baec2`. Cosmetic.
4. **Phase HL evidence table says the Step 6 marker gate runs *"on a consumer with a hand-edited
   `CLAUDE.md`"*; the TS gate says a fixture.** The TS governs. I will run the fixture and, in
   addition, a read-only dry check on `innoforce-ai-first/CLAUDE.md` (no markers → the report-and-leave
   branch), which costs nothing and touches nothing.
5. **`update.md` Step 7 form `{resolved-source}@{verified-tag-or-commit}`** is what all three local
   consumers followed — and all three wrote a `D:/` path. The TS diagnosis is confirmed on three of
   three; the new `--check project` line will fire on each of them at their next update, which is the
   intended effect.
6. **`templates/project_config.yaml` marks `installed_from` as `← PROJECT: set by each update`**, while
   `innoforce-ai-first` carries it as `← FRAMEWORK`. The TS does not decide the marker; the Step 3
   classification says the *value* is project-written and the *key* is framework-shipped. I keep the
   template's `← PROJECT` and say so in the RF.

## 7. Knowledge Citations

> HL §7.2 (master HL) — 29 items. Each read; application or N/A stated.

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | PV 0 — `README.md` opening, § How It Works | ✅ | Applied — the briefing and the three questions make an update resumable by the owner, not only by the agent that ran it | |
| 2 | PV 0 — `.tfw/README.md` NS1, NS2 (principles 3, 5) | ✅ | Applied — `UNDECLARED` keeps the trace whole rather than thinner: the cell survives verbatim | |
| 3 | PV 1 — Methodology values, Structural Enforcement | ✅ | Applied — every rule this phase adds has a gate or test: word count, exclusion list in the payload test, phase-state line in `--check tasks`, `installed_from` form in `--check project`, TD-198 row in the registry (rec. 4) | |
| 4 | PV 1 — Methodology values, Where truth belongs | ✅ | Applied — a status the tool cannot read whole is refused, not resolved; the owner resolves with an event | |
| 5 | PV 1 — Methodology values, Success Criteria | ✅ | Applied — no provider API anywhere; `git rev-parse` and `cmp` are the whole mechanism | |
| 6 | PV 2 — philosophy F4 | ✅ | Applied — a phase directory without `status.md` is a filesystem fact the gate reads; no state table | |
| 7 | PV 2 — philosophy F11 | ✅ | Applied — `templates/briefing.md` is the one new artifact; it owns *what changed, for the owner* and removes the free-text summary the agent otherwise improvises. It is derived from the CHANGELOG and carries no free text of its own | |
| 8 | PV 2 — philosophy F27 | ✅ | Applied — the copy step prints what it skipped; the manifest names each phase directory | |
| 9 | PV 2 — philosophy F34 | ✅ | Applied — the owner's account ("спросишь кто, где…") is the requirement; the three questions are its discovered shape | |
| 10 | PV 2 — philosophy F38 | ✅ | Applied — one surface, one tag; Q1/Q2 are the only decisions returned | |
| 11 | PV 3 — D31, D50 | ✅ | Applied — nothing moves; state is added where it was missing, at stable paths | |
| 12 | PV 3 — D37 | ✅ | N/A — knowledge write territories untouched; `KNOWLEDGE.md` belongs to `/tfw-docs` | |
| 13 | PV 3 — D43 | ✅ | N/A — no citation cascade changes | |
| 14 | PV 3 — D55, D59 | ✅ | Applied — commits under `[claude-code/TFW-60/phase-ac/executor]`; the handle is asked, never inferred from a Git identity (DoF) | |
| 15 | PV 3 — D65 | ✅ | Applied — no CHANGELOG entry is rewritten; additions are appended and dated (AC-2) | |
| 16 | PV 4 — conventions §§3–5 | ✅ | Applied — §5's `UNDECLARED` two-act table is the resolution path for every refused row; §4 *Which handle a machine acts as* is the text the Step 3 gate cites | |
| 17 | PV 4 — conventions §13, §14 | ✅ | Applied — nothing is deleted; the `.2` fence gains a superseded-by line and keeps its bytes | |
| 18 | PV 5 — convention F22 | ✅ | N/A — the board is already retired here; relevant only as history behind the migration guide | |
| 19 | PV 6 — process F7, F30 | ✅ | Applied — the checklist records the three answers and that the briefing was delivered, so the next session has them | |
| 20 | PV 7 — risk F1 | ✅ | N/A — single session, explicit-path staging as always | |
| 21 | PV 7 — constraint F1, F3 | ✅ | Applied — the briefing template fixes structure only, so it cannot generate filler; `team/README.md` is where a role goes, not a fifth key | |
| 22 | RES 1 — YAML 1.2.2 | ✅ | N/A — no schema change | |
| 23 | RES 1 — RFC 8259 | ✅ | N/A | |
| 24 | RES 1 — Git, `git-rev-parse`, `git-add` | ✅ | Applied — `git rev-parse "$target_ref^{commit}"` is the pin; `git show {commit}:.tfw/VERSION` reads the version from the pinned tree | |
| 25 | RES 1 — Google Drive troubleshooting | ✅ | N/A — transport is TFW-61 | |
| 26 | RES 1 — OneDrive sync | ✅ | N/A | |
| 27 | RES 1 — Dropbox conflicted copies | ✅ | N/A | |
| 28 | RES 1 — gsd-pi, BMAD, Hermes, Spec Kit, OpenSpec | ✅ | N/A | |
| 29 | RES 2 — `git-interpret-trailers`, `git-log`, `git-merge-base` | ✅ | N/A — landing protocol is out of this phase | |

**New items the coordinator did not cite:**

| # | Source | Item | How it applies |
|---|---|---|---|
| N1 | PV 3 — `KNOWLEDGE.md` D69 | One dispatcher, `malformed` the only fallback; the owner-approved abbreviation is a recorded act | AC-8 applies D69's rule to the second cell; AC-9 gives the approval its subject — a title | 
| N2 | PV 4 — `conventions.md` §10.3 File Classification | State files are **never** sourced from upstream, only from templates | Grounds the AC-7 decision: the exclusion list makes the copy step obey a rule the conventions already state | 
| N3 | PV 4 — `conventions.md` §11 Design Rules | Workflow instructions ≤ 1200 words | The AC-6 ceiling is the framework's own rule, not a phase-local number | 

---

*ONB — TFW-60 / Phase AC: Update Without Guesswork | 2026-08-30*
