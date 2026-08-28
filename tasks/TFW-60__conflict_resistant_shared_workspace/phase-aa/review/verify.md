# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: **0.42** (`tfw.review.min_verify_ratio`)
> RF files claimed: **33** — 1 created, 7 moved, 25 modified
> Files to verify: ⌈33 × 0.42⌉ = **14**
> **Discrepancies found → escalated to 100%.** All 33 files opened or diffed; the whole
> change set (`git diff f14f744~1 HEAD`, 49 paths including this task's own artifacts) was
> enumerated and reconciled against the census.

## Verification Log

### V1: `.tfw/scripts/gen_index.py` · `migrate_board.py` · their two test files — AC-1, AC-3, AC-4, AC-5, AC-8, AC-9
- **RF claim:** moved with `git mv`, history follows; marker-based root resolution; `--check {index,tasks,project}`; board locator and committed-revision default on one code path; unmatched directories reported; key-naming validator; ASCII messages; tolerant streams; +33 tests
- **Actual:** all four at `.tfw/scripts/`; `docs/scripts/` retains only `gen_docs.py`, `test_gen_docs.py`, `test_integration.py`. `git diff --name-status` records `R063`/`R069`/`R075`/`R065` — renames, not copy-and-delete. `find_project_root` (L75–100) walks upward for `.tfw/`, skips any candidate containing `.upstream`, and **raises `SystemExit` with no fallback** when no root is found. `git grep 'parents\[2\]'` over the payload returns only a docstring explaining the old answer and two `PROJECT_ROOT` constants inside test files. `read_board` (L648) is one function taking `board`, `revision`, `working_tree`; the default path is `git show {revision}:{board}` and a non-zero return **refuses**, naming `--working-tree` and printing the revision it tried. `set(gen_index.CHECKS) == {"index","tasks","project"}`; `"--validate"` and `"--doctor"` appear nowhere as argparse strings
- **Match:** ✅

### V2: `.tfw/migrations/2.0.0.md` — AC-2, AC-4, AC-6, AC-8
- **RF claim:** the one created file, written for a project that is not this one; ordering constraint stated where a reader would violate it; names `build.*`, the quiescence rule and the `task_containers` decision; tells the operator an unresolved directory may be renamed by hand; `--check project` as the last step
- **Actual:** read in full. No `[workspace, tasks]`, no 7,505 references, no 666 files — every path and command is one a receiving project has. "The order" states *migrate, then generate, then remove the board* at the head and repeats the consequence at each step, with step 5 carrying *"the one unrecoverable mistake in this procedure."* § "Before you start" carries quiescence with its measured reason (the source board rewritten three times during the first real migration). § "What the manifest will tell you about odd directories" says the tool will not rename and a person may. § "`build.*` in your config keeps pointing at the old path" is present. Step 7 is `--check project`
- **Match:** ✅

### V3: `.tfw/conventions.md` · `.tfw/glossary.md` — AC-1, AC-2, AC-4, AC-14
- **RF claim:** payload paths; four new canon sections
- **Actual:** diffed. §2 gains three payload entries (`scripts/gen_index.py`, `scripts/migrate_board.py`, `migrations/{major}.md`). Four canon sections added and verified in place: *some artifacts legitimately have no journal event* (§4, after the immutability rule); *a directory the grammar does not match is reported, never described* (§4 Discovery); *Where the tooling lives* (§4); *A major release ships a migration guide* (§4). §5 gains the two-act `UNDECLARED` table. Glossary's `UNDECLARED`, `Topic File` and `Portfolio index` entries updated
- **Match:** ✅

### V4: `.tfw/templates/status.md` — AC-5, AC-14 · **DISCREPANCY**
- **RF claim:** "quoted example + worked example" (§1); E20 *"the template's example quotes its prose values"*; E21 *"a complete worked example … checked against the real validator"*. AC-14 fourth bullet: the canon must stop reading the `UNDECLARED` prohibition as absolute
- **Actual:** the quoting rule, the invalid/valid pair and the worked example are all present and correct, and `test_the_status_template_examples_parse_and_validate` drives both through `gen_index.validate_status`. **But line 92 still reads:** *"Normalizing such a value to a declared one is prohibited."* — the identical sentence the same commit **rewrote** in `glossary.md`, verified by diffing `f14f744~1:.tfw/glossary.md` against `HEAD` (old text: *"**Normalizing such a value to a declared one is prohibited**"*). The payload now states two different rules about the same act. Separately, line 78 reads *"the four keys that are never prose — id, lifecycle, owner, authority, created, updated"* — **six** keys are listed
- **Match:** ⚠️ **partial** — AC-5's own bullets hold; the AC-14 sweep left its third copy standing, in the file a person hand-authoring the carrier reads

### V5: `.tfw/workflows/update.md` — AC-2, AC-6, AC-7, AC-10
- **RF claim:** Step 3 guide routing, Step 3a pristine-tag diff, the two decisions, the `team/` step, local-source form, Step 8 self-check; 1165 words under the 1200 ceiling
- **Actual:** read in full. Step 3 routes to `.tfw/.upstream/.tfw/migrations/{major}.md` and states a major release without one is incomplete. Step 3a's loop is `git -C {source} …` with the comment *"In the SOURCE tree, not yours"* and the measured three-merges-to-zero reason. Step 3b carries `task_containers` as a two-option decision that *"does not exist before 2.0.0, so there is nothing to preserve"*, `initial_seq` as a key to delete, and *"**Preserved does not mean correct.** `build.*` is yours and is never overwritten."* § "Create `team/`" says *before the first durable write, this update's own commit included*. Step 0 accepts a local working tree and requires `git status --porcelain -- .tfw/` to print nothing. Step 8 is `--check project`. `wc -w` → **1165**
- **Match:** ✅

### V6: `.tfw/workflows/plan.md` — AC-12
- **RF claim:** `Step 0` removed; naming is step 3 of Step 4, after the identifier exists
- **Actual:** diffed. `## Step 0: Name This Session` deleted. Step 4 item 3 is a numbered step, names `Coordinator | {ID}` with ` | Phase {X}` when given one, explains why it is not step 0, and says *"Repeat this step whenever the slug changes."* Step 3's *"Ask clarifying questions / 🛑 WAIT"* still precedes Step 4, so the question-first order the owner wanted kept is intact
- **Match:** ✅

### V7: `.tfw/workflows/init.md` · `.tfw/workflows/knowledge.md` — AC-1, AC-7, AC-9
- **RF claim:** payload paths; AC-7 `team/` step; `--check project` confirmation
- **Actual:** diffed. `init.md` step 3 creates `team/` **together with its first profile** with the reason stated, renumbering 3–7 to 4–8; new step 8 is `--check project`. Steps writing `status.md` and the first journal event are step 7 — after step 3, so "before the first durable write" holds on `conventions.md` §4's own definition of that phrase. `knowledge.md:71` now names `templates/knowledge/topic.md`
- **Match:** ✅

### V8: `.tfw/templates/team/profile.md` — AC-7
- **RF claim:** cut to its own job, 50 → 33 lines; cites `conventions.md` §4 rather than restating the identity canon
- **Actual:** 33 lines. Carries what `team/` is, the four-key bound table, and *"Create this file BEFORE the first durable write."* The identity-field canon, binding resolution and the shared-tree rule are cited, not copied: *"They are not repeated here: a second copy of a rule is a second thing to keep true."* No `.tfw/templates/team_readme.md` exists
- **Match:** ✅

### V9: `.tfw/templates/project_config.yaml` · `.tfw/project_config.yaml` — AC-9
- **RF claim:** the five-line disambiguating comment deleted, not rewritten; `build.verify` is `--check tasks`; the template's `verify` is a real command
- **Actual:** diffed. The project config's `build` block goes 9 lines → 6; the comment beginning *"NOT `gen_index.py --check`: that asks whether the shared index is current…"* is gone, and `verify` is `python .tfw/scripts/gen_index.py --check tasks`. The template's `verify` placeholder is replaced by the same real command, with a new note that `build.*` is a preserved project section and therefore keeps a stale path silently
- **Match:** ✅

### V10: `.tfw/adapters/claude-code/CLAUDE.md.template` · `claude-code/README.md` · `antigravity/README.md` — AC-11
- **RF claim:** TD-11 in all three, not one
- **Actual:** diffed. All four occurrences (template :31, claude-code README :43, antigravity README :22 and :64) now name `.tfw/workflows/research/base.md`. `grep -rn "workflows/research\.md"` over the whole tree outside `tasks/` returns **one** hit — `.tfw/CHANGELOG.md:102`, the entry describing the fix
- **Match:** ✅

### V11: `docs/scripts/gen_docs.py` · `docs/scripts/test_integration.py` — AC-1, AC-11, AC-5
- **RF claim:** cross-directory import bootstrap; +7 tests
- **Actual:** diffed. `gen_docs.py` replaces `sys.path.insert(parent)` and `parent.parent.parent` with a local `_find_root` walking upward for `.tfw/`, and points `sys.path` at `{root}/.tfw/scripts` absolutely because mkdocs runs the file with `docs/` as its config root. `test_integration.py` gains six named tests: the two adapter-path checks, the self-test that proves the check fires, the copy-vs-source comparison, the status-template validator drive, and the ASCII class check — with an annotated two-entry `NON_REPO_PATHS` allowlist
- **Match:** ✅

### V12: `.tfw/VERSION` · `.tfw/CHANGELOG.md` · `README.md` — AC-14
- **RF claim:** `2.0.0-dirty.2`, the entry, the payload path
- **Actual:** `cat .tfw/VERSION` → `2.0.0-dirty.2`; `project_config.yaml:7` matches. `git tag -l` → latest is `v2.0.0-dirty`; **no `v2.0.0-dirty.2` tag**, correct per the ONB Q3 (b) ruling. The CHANGELOG entry opens by justifying `-dirty.2` over `2.0.1-dirty`, carries § "Why this release exists" naming what the first external update found *including that the framework could not deliver its own tooling*, and closes with an explicit note that the older entry's code fence is a record and the reader should follow `.tfw/migrations/2.0.0.md` instead. `README.md:257` names `.tfw/scripts/gen_index.py`
- **Match:** ✅

### V13: `team/README.md` — R3 template move
- **RF claim:** "the template link the move would have broken"
- **Actual:** the one changed line points at `.tfw/templates/team/profile.md`; the file resolves
- **Match:** ✅

### V14: the three moved templates — R3
- **RF claim:** `git mv`, references updated, no new files, flat namespace shrinks by 3
- **Actual:** `git diff --name-status` shows `R100` for `journal_event.md → journal/event.md` and `topic_file.md → knowledge/topic.md` (byte-identical). `team_profile.md → team/profile.md` shows as `A`/`D` across the full range only because commit `80c2ed5` rewrote it 50 → 33 lines after the move; `git log --follow` on the new path returns 3 commits, so history followed. No `team_profile.md`, `journal_event.md` or `topic_file.md` remains
- **Match:** ✅

### V15: adapter copies — 8 workflow copies + the 11 Codex skills
- **RF claim:** re-synced, verified byte-identical; "all 22 workflow copies and 11 Codex skills → all identical"
- **Actual:** `cmp` over every `.claude/commands/tfw-*.md` and `.agent/workflows/tfw-*.md` against its `.tfw/workflows/` source → **11 + 11 identical, 0 diff**. The only unmatched name is `tfw-task`, a meta-workflow with no canonical file, which predates this phase. `cmp` over all 11 `.tfw/adapters/codex/skills/*/SKILL.md` against `.agents/skills/` → **11 identical**
- **Match:** ✅

### V16: the never-modify classes
- **RF claim:** 82 historical trace artifacts, 11 provenance comments, `KNOWLEDGE.md`'s historical rows — bytes unchanged
- **Actual:** `git diff --name-status f14f744~1 HEAD` touches **no** file under `tasks/` other than this phase's own artifacts and this task's two journal events. `KNOWLEDGE.md` is not in the change set at all. `git grep -l "Written by docs/scripts/migrate_board.py"` returns 14 today against the census's 13 — the difference is this phase's own RF and evidence, which quote the string
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only` | **254 tests collected**, no collection errors — matches RF |
| 2 | `python -m pytest .tfw/scripts/ -q` | **158 passed, 1 skipped** in 11.97 s |
| 3 | `python -m pytest docs/scripts/ -q` | **95 passed** in 248.66 s |
| 4 | (1)+(2)+(3) → full suite | **253 passed, 1 skipped** — matches RF exactly, against the ONB's recorded 220-passed baseline. Net **+33** |
| 5 | `python .tfw/scripts/gen_index.py --check tasks` | exit **0** — *53 tasks validate against the closed schema*, and the output names what it did not check |
| 6 | `python .tfw/scripts/gen_index.py --check project` | exit **0** — version `2.0.0-dirty.2`, 1 participant, creates in `workspace`, resolves across `[workspace, tasks]` |
| 7 | `python .tfw/scripts/gen_index.py --check index` | exit **0** — index up to date |
| 8 | `git grep -n "docs/scripts/gen_index\|docs/scripts/migrate_board" -- . \| grep -v "^tasks/"` | **11 hits, identical to `ac1_gate.txt` line for line** — 8 CHANGELOG, 1 guide, 1 deliberate test fixture, 1 `KNOWLEDGE.md:22` |
| 9 | `wc -w .tfw/workflows/update.md` | **1165** — under the §11 ceiling of 1200 |
| 10 | `cmp` sweep over 22 workflow copies + 11 Codex skills | **all identical** |
| 11 | `git log --oneline --follow` on each moved file | gen_index **9**, migrate_board **6**, team/profile **3**, journal/event **3**, knowledge/topic **5** — history follows every move |
| 12 | independent AST-free diff of `parse_board` across the move | **42 → 47 lines** whole-function; exactly two code lines differ — the signature gaining `heading: str = BOARD_HEADING`, and the locator using it. Every row-reading line byte-identical |
| 13 | `python -m mkdocs build --config-file docs/mkdocs.yml` | started; the 95-test `docs/scripts/` suite that passed in (3) runs `mkdocs` builds internally, which is the same gate |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | *"253 passed, 1 skipped … Baseline before the phase: 220 passed, 1 skipped. Net +33"* | RF §4 | Re-run: 158+95 = **253 passed, 1 skipped**, 254 collected. Baseline traced to ONB § "Baseline measurements taken before any edit" → `pytest docs/scripts/ -q` → 220 passed, 1 skipped | ✅ |
| C2 | *"the row parser is untouched, **measured rather than asserted** … exactly one line changed — the locator"* | RF §3 AC-3, EV E13, `ac3_parser_untouched.txt` | Independently re-diffed (command 12). The row-reading body is byte-identical; the locator became a parameter. The artifact's declared method excludes the docstring — it also excludes the `def` line, so the signature change that carries the parameter is not shown. Substance holds; presentation understates by one line | ✅ (with note) |
| C3 | *"`parents[2]` would have resolved **wrong in two of three**"* | EV E2, `fixture_report.md` § F1 | `fixture_run.txt` § "AC-1's real gate" prints, per placement, what `parents[2]` would give against what the tool resolved. `tools/` → a directory **outside the project**; `a/b/c/d/` → two levels short; `tools/tfw/` → right by luck. Two of three, as claimed | ✅ |
| C4 | *"0 files hand-carried, **0 framework files edited inside `.tfw/`**"* | EV E47 | `fixture_run.txt` prints **`framework files edited inside .tfw/: 1`** — `.tfw/scripts/__pycache__/gen_index.cpython-313.pyc`. Reconciled in `fixture_report.md` (*"Python bytecode written by running the tool, not an edit"*), which E47 also cites, and the guide gained a `.gitignore` line for it. The EV row itself carries the bare `0` with no caveat | ⚠️ reconciled, but not at the row |
| C5 | *"`git log --follow` returns 8 commits for `gen_index.py`, 5 for `migrate_board.py`"*, in a file headed *"Pinned at `1079020`"* | RF §1 | At `1079020` the values are **9 and 6**; at `80c2ed5` they are **8 and 5**. The numbers are true, taken one commit before the declared pin. `fixture_run.txt`'s own header likewise records `source: … at 80c2ed5` for the first pass | ⚠️ measured off-pin |
| C6 | *"`--validate` and `--doctor` appear nowhere in the source, asserted by a test"* | EV E33 | `test_the_three_checks_are_one_flag_with_a_subject` asserts `'"--validate"'` and `'"--doctor"'` are absent from `gen_index.py` — i.e. absent as argparse strings. Prose mentions survive in a comment at `gen_index.py:1090` explaining the retirement and in one test docstring. The test's guarantee is narrower than E33's sentence, and correctly so | ✅ |
| C7 | ONB §7 knowledge citations, PV 0–4 in full, PV 5–7 by relevance | ONB §7, HL §7.2 | See the table below — 29 of 29 resolve | ✅ |

## Discrepancies Found

| # | Discrepancy | Severity |
|---|---|---|
| **D1** | `.tfw/templates/status.md:92` still reads *"Normalizing such a value to a declared one is prohibited."* — verbatim the sentence commit `f14f744` **rewrote** in `glossary.md` and replaced in `conventions.md` §5 with the two-act rule. The payload now states two different rules about the same act, and the absolute one is in the canonical carrier template a receiving project hand-authors from. AC-14's fourth bullet exists because *"the prohibition reads as absolute and projects will either strand tasks or resolve them without a trace"*; RF §3 marks AC-14 ✅, and E56 cites only `conventions.md` and `glossary.md` | **Medium** |
| **D2** | Same file, line 78: *"the four keys that are never prose — id, lifecycle, owner, authority, created, updated"* — six keys are listed. In a template AC-5 rewrote specifically so a person hand-authoring the carrier gets it right | Low |
| **D3** | RF §1 heads its table **"Modified — 25"**, a figure `census.md` reaches by classifying the four scripts as *moves* and excluding them from the modified count. The RF's own table then lists those four scripts as Modified rows, along with `templates/project_config.yaml` and `templates/team/profile.md`, which the census does not count either. Counting distinct paths in the RF's table gives ~31. No budget limit is crossed under the census's declared method, and the census was raised to the coordinator before acting — but the number in the RF is not the number of rows in the RF | Low |
| **D3a** | The TS's basis for treating the scripts as moves — *"The 2,864 lines of script relocate rather than get rewritten, so they cost a move and their path constants"* — did not survive execution: `gen_index.py` changed **507** lines and `migrate_board.py` **246**. A coordinator estimate the work invalidated; the executor raised a census group and proceeded, which is the return-to-coordinator rule working | Low — informational |
| **D4** | Evidence pinning. RF and EV both declare *"Pinned at `1079020`"*; RF §1's `git log --follow` counts are the values at `80c2ed5` (C5), and `fixture_run.txt`'s first pass is headed at `80c2ed5` too. TS §6: *"Evidence is measured at a pinned commit and never against HEAD"* | Low |
| **D5** | EV E47's bare *"0 framework files edited inside `.tfw/`"* against its own artifact's *"framework files edited inside .tfw/: 1"* (C4). Reconciled one file away, not at the row | Low |
| **D6** | RF §4 / E60 claim runtime ASCII is enforced *"as a class"*. `test_every_runtime_message_is_ascii` is a line scanner — it toggles on `print(`/`SystemExit(` and resets on a line ending in `)`, so a message built into a variable and printed later escapes it. It caught five real occurrences and is worth having; the claim is stronger than the mechanism | Low |

**Escalation:** D1 triggered 100% verification. All 33 RF-claimed files were opened or diffed,
and the full 49-path change set was enumerated against `census.md`. Nothing further surfaced:
the remaining files match their claims exactly.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1–E5 | AC-1 — `fixture_run.txt`, `ac1_gate.txt`, `git show --stat f14f744` | ✅ | ✅ — `ac1_gate.txt`'s 11 classified hits reproduce line for line at HEAD (command 8) |
| E6–E10 | AC-2 — `.tfw/migrations/2.0.0.md`, `fixture_run.txt` steps 1–7 | ✅ | ✅ — guide read in full (V2); Step 3 route fires in the transcript |
| E11–E13 | AC-3 — `fixture_run.txt`, `ac3_parser_untouched.txt` | ✅ | ✅ — independently re-diffed (C2); both board attempts quoted, refusal names relocation first |
| E14–E18 | AC-4 — `fixture_manifest.md`, `fixture_index.md`, `fixture_run.txt` | ✅ | ✅ — `Unresolved inputs — 2`, no `Backlog` section, `backlog idea, never started` absent |
| E19–E22 | AC-5 — `ac5_validator.txt`, `.tfw/templates/status.md` | ✅ | ✅ for the AC's own bullets — before/after for all five keys is quoted verbatim. See **D1/D2** for what the same file still carries |
| E23–E24 | AC-6 — `update.md`, `fixture_run.txt` | ✅ | ✅ — both decisions recorded as made, with reasons |
| E25–E27 | AC-7 — `init.md`, `update.md`, `.tfw/templates/team/profile.md`, `fixture_run.txt` | ✅ | ✅ — 33-line profile template verified; *"wrote team/saubakirov.md from the payload template, no file hand-carried"* |
| E28–E32 | AC-8 — named tests, `read_board()`, `fixture_run.txt` | ✅ | ✅ — `read_board` read directly (V1); `board source: git show HEAD:tasks/README.md` printed on every run |
| E33–E38 | AC-9 — six named tests, `project_config.yaml` diff | ✅ | ✅ — three subjects re-run here (commands 5–7); comment deletion confirmed 9 lines → 6 |
| E39–E41 | AC-10 — `update.md` Step 3a / Step 0, `fixture_run.txt` | ✅ | ✅ — *"CUSTOMIZED ×2, customized files: 2"* of ~38 |
| E42–E44 | AC-11 — three named tests | ✅ | ✅ — re-verified independently (V10, V15): 4 route fixes, 22+11 copies identical |
| E45–E46 | AC-12 — `.tfw/workflows/plan.md` | ✅ | ✅ — diffed (V6) |
| E47–E50 | AC-13 half one — `fixture_report.md`, `fixture_run.txt` | ✅ | ⚠️ — the run is real and complete; **E47's `0 edited` is contradicted by its own transcript's `1`** and reconciled only in the sibling artifact (**D5**) |
| **E51** | **AC-13 half two — DEFERRED** | — | ✅ **correctly deferred.** The blocker is named, the closing artifact is named, and TS §7 makes any other answer a rejection. This is the honest outcome |
| E52–E57 | AC-14 — `VERSION`, `project_config.yaml`, `CHANGELOG.md`, `conventions.md`, `glossary.md` | ✅ | ⚠️ — E52, E54, E55, E57 hold as verified. **E56's canon claim holds for the two files it cites and leaves a third contradicting copy in the payload (D1)** |
| E53 | AC-14 tag — **N/A** | — | ✅ — `git tag -l` confirms no `v2.0.0-dirty.2`. Correctly out of executor scope per ONB Q3 (b) |
| E58–E60 | budget · DoF | ✅ | ✅ for E58 (census re-derived) and E59 (`phases/` → no matches). **E60's "as a class" overstates a heuristic (D6)** |

**Totals:** 60 evidence items, **60 artifacts resolve**, 55 match their claims cleanly,
4 carry the notes above (E19–E22 via D1/D2, E47 via D5, E56 via D1, E60 via D6), 1 correctly
DEFERRED, 1 correctly N/A. **No evidence artifact is missing, and no green signal was found
sitting over a red one** — the one place that risk was live, `KNOWLEDGE.md:22`, is named in
AC-1's own gate text so the RF could not report around it.

## Knowledge Citations Verified

> Scanned PV priorities 0–4 in full and 5–7 by relevance. Master HL §7.2 carries 29 items;
> ONB §7 confirms all 29 and adds four of its own (N1–N4).

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | HL §7.2 #1 · ONB #1 | PV 0 — `README.md` opening · § How It Works | ✅ | ✅ | ✅ — bounded resumability without promising lossless context | ✅ — AC-2's guide and AC-9's self-check are what a receiving project resumes from |
| 2 | HL §7.2 #2 · ONB #2 | PV 0 — `.tfw/README.md` [NS1](#), [NS2](#) principles 3 and 5 | ✅ anchors `id="ns1"`, `id="ns2"` present at :72, :79 | ✅ | ✅ — NS1 *"another authorized person or agent can … continue without rebuilding the original conversation"*; NS2 §5 *"Continuation over isolated output"* | ✅ — a project told to run a file it does not have cannot continue. AC-1 is this clause made true off-site |
| 3 | HL §7.2 #3 · ONB #3 | PV 1 — § Methodology values, **Structural Enforcement** | ✅ anchor `id="methodology-values"` at :91 | ✅ | ✅ — *"a rule that cannot reveal its own violation is only advice"* | ✅ — AC-11's path test and AC-1's depth fixture are the structural forms; `parents[2]` passing by coincidence is the prose-wearing-a-test's-clothes case |
| 4 | HL §7.2 #4 · ONB #4 | PV 1 — § Methodology values + § Where truth belongs, *one authoritative owner per truth type* | ✅ both anchors present | ✅ | ✅ — *"assigns one authoritative owner to each kind of truth rather than forcing every truth into one monolithic file"* | ✅ — the load-bearing constraint on AC-9. Verified operative: `test_no_check_subject_writes_anything` byte-compares the tree across all three subjects |
| 5 | HL §7.2 #5 · ONB #5 | PV 1 — § Methodology values (**Portability**) + § Success Criteria | ✅ | ✅ | ✅ — *"no vendor may become the sole home of project memory"*; criterion 4 *"does not require the recipient to reconstruct missing work"* | ✅ — **the phase's own clause.** A payload that cannot carry its own tooling makes the recipient reconstruct it |
| 6 | HL §7.2 #6 · ONB #6 | PV 2 — `knowledge/philosophy.md` **F4** | ✅ | ✅ `philosophy.md:11` | ✅ — structural enforcement beats state tables | ✅ |
| 7 | HL §7.2 #7 · ONB #7 | PV 2 — **F11** | ✅ | ✅ `:18` | ✅ — avoid extra entities | ✅ — and it is what R3's two withdrawals enforce |
| 8 | HL §7.2 #8 · ONB #8 | PV 2 — **F27** | ✅ | ✅ `:34` | ✅ | ✅ — shapes `--check`'s per-subject output |
| 9 | HL §7.2 #9 · ONB #9 | PV 2 — **F34** | ✅ | ✅ `:41` | ✅ | ✅ — ONB Q1 is this clause: *"an external project"* is unusable until a named fixture is authorized |
| 10 | HL §7.2 #10 · ONB #10 | PV 2 — **F38** | ✅ | ✅ `:45` | ✅ — coordinator attention is finite | ✅ — eight questions batched into one file |
| 11 | HL §7.2 #11 · ONB #11 | PV 3 — `KNOWLEDGE.md` **D31**, **D50** | ✅ | ✅ `:65`, `:84` | ✅ | ✅ |
| 12 | HL §7.2 #12 · ONB #12 | PV 3 — **D37** | ✅ | ✅ `:71` | ✅ — tfw-docs owns §1–§3, tfw-knowledge owns `knowledge/*` | ✅ — **N/A justified per row**, and it is why ONB Q5 offered option (b) rather than editing `KNOWLEDGE.md:22` |
| 13 | HL §7.2 #13 · ONB #13 | PV 3 — **D43** | ✅ | ✅ `:77` | ✅ — *"Executor confirms or extends"* is the cascade | ✅ — ONB §7 is the executor link, filled per row |
| 14 | HL §7.2 #14 · ONB #14 | PV 3 — **D55**, **D59** | ✅ | ✅ `:89`, `:93` | ✅ — D59: *"declared attribution ≠ authentication"*, capability boundaries | ✅ — commits carry `[claude-code/TFW-60/phase-aa/executor]` (verified in `git log`); D59 is exactly ONB Q3, and the tag was **not** cut |
| 15 | HL §7.2 #15 · ONB #15 | PV 3 — **D65** | ✅ | ✅ `:99` | ✅ — reverting a result never reverts its trace | ✅ — the 82 never-modify artifacts and 11 provenance comments, verified untouched (V16) |
| 16 | HL §7.2 #16 · ONB #16 | PV 4 — `conventions.md` §§3–5 | ✅ | ✅ | ✅ | ✅ — §4's identifier rules are what collapse AC-4 to *reported* |
| 17 | HL §7.2 #17 · ONB #17 | PV 4 — §13, §14 | ✅ | ✅ | ✅ | ✅ — `git mv` rather than copy-and-delete; verified as `R0xx` in `--name-status` |
| 18 | HL §7.2 #18 · ONB #18 | PV 5 — `knowledge/convention.md` **F22** | ✅ | ✅ `convention.md:29` | ✅ — the board is a process artifact | ✅ — **N/A justified**: Phase A retired the live board; AA only makes its *location* an input |
| 19 | HL §7.2 #19 · ONB #19 | PV 6 — `knowledge/process.md` **F7**, **F30** | ✅ | ✅ `:14`, `:37` | ✅ — *"Capture without an enforcement site does not change behaviour"* | ✅ — AC-2's routing from the step that needs it is the enforcement half |
| 20 | HL §7.2 #20 · ONB #20 | PV 7 — `knowledge/risk.md` **F1** | ✅ | ✅ `risk.md:11` | ✅ — two sessions, one index; verbal warning 0/1 | ✅ — operative: the fixture is a separate clone with its own index |
| 21 | HL §7.2 #21 · ONB #21 | PV 7 — `knowledge/constraint.md` **F1**, **F3** | ✅ | ✅ `:8`, `:10` | ✅ | ⚠️ — the ONB's *application* names `team_readme.md` and `.tfw/scripts/README.md`, both **withdrawn at TS R3 after the ONB was written**. The citation and meaning are right; the application is stale by design, and the R3 outcome honours F3 more strictly than the ONB's reading did |
| 22–29 | HL §7.2 #22–#29 · ONB #22–#29 | RES 1 — YAML 1.2.2 · RFC 8259 · Git/rev-parse/add · Google Drive · OneDrive · Dropbox · five external systems · RES 2 — git trailers | ✅ all URLs well-formed and named | ✅ | ✅ — YAML 1.2.2's plain-scalar rule is AC-5's actual root cause and is correctly the basis of both the quoted example and the validator message | ✅ — five correctly **N/A** with a per-row reason (JSONL not chosen; transport is TFW-61; Phase A's L3 untouched); #28 applied as counter-evidence, which is a legitimate use |
| N1–N4 | ONB § "New items the coordinator did not cite" | `conventions.md` §10.4 · §11 · §10.3 · `templates/journal_event.md` | ✅ ×3 | ✅ ×3 | ✅ | ⚠️ **N4's path `.tfw/templates/journal_event.md` no longer exists** — this phase moved it to `templates/journal/event.md`. The ONB predates the move; the item it cites (closed `kind` vocabulary, clock-read timestamp) exists at the new path and is what AC-14's fifth bullet writes into the canon |

**Totals: 29 HL §7.2 citations + 4 ONB additions = 33. Resolved: 33. Semantically verified: 33.
Irrelevant: 0. Hallucinated: 0.** Two application notes (#21, N4) are both artifacts of the
ONB being written before TS R3 and before the template move — historical, not defects in the
result.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings? — **100%**, escalated on D1: all 33 claimed files plus the full 49-path change set
- [x] Ran at least 1 build/test command? — 13 commands, including the full suite, all three `--check` subjects, the AC-1 gate grep, the `cmp` sweep and an independent `parse_board` diff
- [x] Claim & Source Checks filled — C1–C7: seven claims spot-checked by re-derivation, every citation traced, the test counts and the `parents[2]` numbers checked against primary output rather than against the RF's summary
- [x] Each RF §3 (AC) checkmark verified against actual file? — 15 rows, all traced
- [x] KNOWLEDGE.md checked — contradictions with changes documented? — `KNOWLEDGE.md` is untouched by this phase, correctly; `:22`'s stale path is a **known, declared** exception named inside AC-1's own gate and filed as RF §6 observation 1 for `/tfw-docs`
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: **33**, resolved: **33**, semantically verified: **33**, irrelevant: **0**, hallucinated: **0**
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: **60**, verified: **58 clean + 4 with notes** (overlapping), missing: **0**, deferred: **1**, N/A: **1**

Stage complete: YES
