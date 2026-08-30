# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42 (`tfw.review.min_verify_ratio`)
> RF files claimed: 26 counted (+ 6 byte copies excluded by S32)
> Files to verify: ⌈26 × 0.42⌉ = 11 — **24 of 26 opened or diffed, the remaining 2 (the two script test files) executed**; the two scratch fixtures rebuilt independently. Effective ratio 1.0.
> Measured at: working tree = `HEAD` = `afef18a`; the phase's last commit `af1a695`; implementation diffed as `b9baec2..d047286`. Clock at start of review: 2026-08-30 18:01:21 +05:00.

## Verification Log

### V1: `.tfw/workflows/update.md`
- **RF claim:** rewritten at 1174 words; Step −1; Step 0 pin from `target_ref`; Step 3 🛑 gate with three questions and the AG rule; Step 5 copy loop with exclusions printing `skipped:`; Step 6 `Kind` column, §9 pointer, allowlist wording; Step 7 `{upstream}@{verified-tag}`; Step 8a briefing.
- **Actual:** read in full. `wc -w` = **1174**. Step −1 present (three sentences). Step 0: `source_head=$(git -C {source} rev-parse --verify "$target_ref^{commit}")`, `target=$(git show "$source_head:.tfw/VERSION")`, `test "$target_ref" = "v$target"`; no `rev-parse HEAD` anywhere in the file. Step 3 carries the 🛑 heading, the three numbered questions with *asked, never inferred from `git config user.name`, an OS username or the upstream's profiles*, the AG sentence (*one message, continue through the read-only steps, stop at the first write*), *Record the answers in the checklist*. Step 5: the `find | while read -r` loop with `case "$rel" in project_config.yaml|knowledge_state.yaml) echo "skipped: …"`; the sentence *A copy that reports nothing skipped on a project that has both files is a failed step*; recheck against `$source_head`. Step 6: `Kind` column — 5 `copy`, 2 `block` (Claude rules, Codex routing); the three-case marker rule summarized with a pointer to conventions §9; allowlist reworded to *text whose purpose is to retire the term*. Step 7: the one form and *never a machine-local path*. Step 8a present, four blocks, *last message*, checklist records delivery. Copies in `.claude/commands/` and `.agent/workflows/` `cmp`-identical.
- **Match:** ✅ — with one gap noted under Discrepancies (D1): the commit-target path Step 0 admits in prose has no check in the block.

### V2: `.tfw/scripts/migrate_board.py`
- **RF claim:** `classify_status()` whole-or-refuse — one declared token, no second declared token, no `So` symbol after it; `U+FE0F`/`U+200D` skipped; result gains `signals`; manifest gains *Rows carrying more than one lifecycle signal* and *Phase directories*; *Task state written* note rewritten.
- **Actual:** function read (`:162–218`). Leading run of any `S`, invisibles and spaces stripped; first `[A-Z_]+` token matched against declared ids; trailing text with invisibles removed; `signals` = declared tokens found + characters where `_is_status_symbol()` (category `So`); non-empty → `UNDECLARED` verbatim. Ran it myself on ten cells: the `AILAB-2` shape → `UNDECLARED` signals `['RF','🔄','✅','🟢']`; `🟠 ONB (A+B)` → `ONB`; `blocked → TD-126` → `DONE`; `✅ DONE (KNW deferred)` → `UNDECLARED ['KNW']`; `✅ DONE (Phase A ✅)` → `UNDECLARED ['✅']`; `✅\uFE0F DONE` → `DONE`; `cost = 3 days, <1 %` → `DONE`; `+1 UX` → `DONE`, outcome keeps the `+`. Manifest strings at `:750–764` and `:833–849` match the RF wording.
- **Match:** ✅

### V3: `.tfw/scripts/gen_index.py`
- **RF claim:** `check_tasks()` — stateless phase directories: failure on a live task, informational line per terminal/stateless/malformed task, summary count, writes nothing; `check_project()` — `installed_from` machine-local report, never rewritten.
- **Actual:** `check_tasks()` read: for each `iter_phase_dirs()` entry with no `status.md`, reason chosen from the task's own state (`None` → *carries no status.md of its own*; `_error` → *malformed, reported above*; `lifecycle in TERMINAL` → *the task is DONE/REJECTED*; else a failure line to stderr and `failures += 1`); one `note:` line per task; summary line; exit from failures only. `check_project()` `:1332–1344`: `^[A-Za-z]:`, leading `/`, or `\` → problem text *is machine-local; … Not rewritten*; `self` and `unrecorded` exempt. Ran `--check tasks` on this repository: 6 informational lines over 17 directories (TFW-42/46/47/52/53/55), 54 validate, exit 0. Ran `--check project`: consistent.
- **Match:** ✅

### V4: `.tfw/scripts/test_migrate_board.py` · V5: `.tfw/scripts/test_gen_index.py`
- **RF claim:** +11 and +12 tests; 22 of 28 fail before, 28 pass after; suite 315 passed, 1 skipped.
- **Actual:** full suite run by the reviewer: **315 passed, 1 skipped in 153.58 s**, exit 0 (baseline in ONB: 283 + 1). The before/after list in `status_cell_before_after.txt` §1 names 22 failing test ids whose names match the RF's fixture description (`AILAB-2` exact shape, second emoji alone, second token alone, `→ + = <` non-signals, variation selector, refused row receives state, manifest headings, phase listing, live/terminal/stateless/malformed, one line per task, repository census, `installed_from` ×3).
- **Match:** ✅

### V6: `docs/scripts/test_integration.py`
- **RF claim:** block sync helpers and three tests; root `CLAUDE.md` block checked with installed copies; no `{version}` in templates; project-owned payload files derived and required in Step 5; TD-198 row; staging `update.md` path exempted.
- **Actual:** diff read. `MANAGED_BLOCK` regex, `_managed_block()` (asserts ≤ 1 block per file, returns `None` without markers), `_sync_block()`; `test_installed_adapter_copies_match_their_sources` now compares the `TFW:CLAUDE` body of root `CLAUDE.md` with the template's; `test_a_marker_bounded_sync_leaves_project_text_untouched`; `test_a_file_without_markers_is_reported_and_left_untouched`; `test_no_adapter_template_requires_a_version_substitution` (three templates, plus byte equality of the Antigravity rule and its template); `test_every_project_owned_payload_file_is_excluded_from_the_copy` derives `{p.name for p in .tfw/*.yaml if templates/p.name exists}` = `{project_config.yaml, knowledge_state.yaml}` and requires each name in Step 5's `case` line plus `skipped:` in the step; `RETIRED_WORDINGS` gains *Commands never duplicate workflow content*; `NON_REPO_PATHS` gains `.tfw/.upstream/.tfw/workflows/update.md`.
- **Match:** ✅

### V7: `.tfw/conventions.md`
- **RF claim:** §4 Identifier — acronym of the approved title, proposed with it, *never derived silently* said both ways; §4 Artifact file naming — current-grammar rows, no title appended; §9 — the one marker rule, three cases.
- **Actual:** diff read and the live file read in full. §4 `:235–250`: *acronym of the approved full title — the initials of its significant words* with `CRSW` and `ASSISTED15`; *proposes the full title and its initials together, in one exchange*; *`UPD` for a task with no title behind it is the anti-pattern*; *never created without the owner's approval*. `:378–379` two current-grammar rows; `:394–400` the no-title rule with the rejected example. §9 `:703–718`: *whole copies or marker-bounded blocks, and nothing of a third kind*; the three-row table; *Exactly one managed block per file*.
- **Match:** ✅

### V8: `.tfw/glossary.md` · `.tfw/workflows/plan.md` · `.tfw/workflows/init.md` · `.tfw/templates/HL.md`
- **RF claim:** the same abbreviation rule in each carrier's words; worked examples title → initials; HL header **Title** then **Abbreviation**.
- **Actual:** diffs read. Glossary *Task Naming*: initials of the approved full title, `CRSW`, proposed together with the title, approved with it. `plan.md` Step 3.5 (`:40–44`) and Step 4.2 (`:60`, `:70`); `init.md` Batch 1 (`:113–116`, `ITFW`/`INIT`) and Mini-Setup 6 (`:139–140`). `templates/HL.md:5–6`: `> **Title**` then `> **Abbreviation**`, adjacent. Copies of `plan.md`/`init.md` byte-identical in both adapter directories.
- **Match:** ✅

### V9: `.tfw/adapters/claude-code/CLAUDE.md.template` · `CLAUDE.md` (root)
- **RF claim:** markers around the `## TFW` section; block brought current (`status.md` in context loading, `/tfw-knowledge`, `/tfw-config`, `Version: see .tfw/VERSION`); root `CLAUDE.md` carries the block byte-identical; Conduct and Execution Modes follow it.
- **Actual:** template read: markers at `:15` and `:54`; context loading item 5 = *The selected task's `status.md` — its live state, and the only authority for it*; command table has 12 rows including `/tfw-knowledge` and `/tfw-config`; `Version: see .tfw/VERSION`; no `{version}`. Root `CLAUDE.md`: markers at `:3` and `:42`; `diff` of the two marker-bounded regions: **identical**. Diff of root `CLAUDE.md` shows Key References moved inside the block and Conduct/Execution Modes text unchanged.
- **Match:** ✅

### V10: `.tfw/adapters/claude-code/README.md` · `.tfw/adapters/codex/README.md`
- **RF claim:** Claude README gains *The managed block* section and says what is outside is the project's; Codex README step 3 becomes *report and leave*, pointer to §9.
- **Actual:** Claude README `:23–45` read — setup step 2 says everything outside the block is yours; `## The managed block` names the markers, what is inside, the region-only `cmp`, and the three-case rule with the §9 pointer. Codex README diff: `:104` *append the complete block* → *report it and leave it untouched … the marker rule in `.tfw/conventions.md` §9*. The *absent → create with the block* bullet stays (§9 case 2).
- **Match:** ✅

### V11: `.tfw/adapters/antigravity/tfw-rules.md.template` · `.agent/rules/tfw.md` · `.tfw/adapters/cursor/tfw.mdc.template`
- **RF claim:** Antigravity template = rendered rule byte for byte, `{version}` gone; Cursor `{version}` ×3 gone, a whole copy.
- **Actual:** `cmp .agent/rules/tfw.md .tfw/adapters/antigravity/tfw-rules.md.template` — identical. `grep -c "{version}"` on the three templates: 0, 0, 0. Both templates read: `Version: see .tfw/VERSION`.
- **Match:** ✅

### V12: `.tfw/CHANGELOG.md`
- **RF claim:** `.3` entry dated addendum quoting the retired sentence and what a thinned project does (TD-198); `.2` entry dated closing line on the `TD-11` paragraph (TD-191); `2.0.0-dirty` entry `> **Superseded by**` above the migration fence (TD-190); no entry rewritten in substance; `[Unreleased]` untouched.
- **Actual:** diff `b9baec2..d047286` shows exactly three hunks: a 16-line `### Added 2026-08-30 — the wording this release retired, verbatim (TD-198)` block under `.3` quoting *"Commands never duplicate workflow content — they reference it"*; one italic sentence appended to the `TD-11` paragraph dated 2026-08-30; a three-line blockquote `> **Superseded by** .tfw/migrations/2.0.0.md (2026-08-30)` above the fence. No deletions of existing prose other than the one line re-flowed to append the sentence. `[Unreleased]` reads *Nothing pending.*
- **Match:** ✅

### V13: `RELEASE.md`
- **RF claim:** §5 three checklist items — reach every earlier tag and open with Step −1; quote reversed wording verbatim; superseded-by line, entries append-only; §6 step 3 names them.
- **Actual:** diff read: three `- [ ]` items added to §5 with exactly that content; §6 step 3 rewritten to *with its updating section written for a receiver on any earlier tag of the line (see §5), the retired wordings quoted, and `> **Superseded by**` lines on anything it replaces*.
- **Match:** ✅

### V14: `.tfw/templates/journal/event.md` · `.tfw/templates/team/profile.md` · `.tfw/templates/status.md` · `.tfw/templates/project_config.yaml`
- **RF claim:** `via` free-form at `:49`, `:70` (TD-200); profile: one file per person, role in `team/README.md`, `since` defined, `type: agent` admitted and unusable (TD-203); status template: the phase sentence, when to use which, written by hand never by migration; config template: `installed_from` one form, never a machine path, `self` for the framework, `← PROJECT` kept.
- **Actual:** `event.md:49` *free-form, non-empty provider or tool text — `claude-code`, `codex`. Absent for a hand edit*; `:70` *non-empty free-form provider/tool text*; "provider family is not a writer" reworded to *`via` is descriptive provenance, not a registry value and not a writer — two sessions of one tool are two writers*. `profile.md:15–19`: *one file per PERSON*; *WHERE A ROLE GOES … `team/README.md`, a file the parser skips*; *`since` is the date the participant joined the project*; *`type: agent` IS ADMITTED BY THE SCHEMA AND USABLE BY NOTHING*. `status.md:52–60`: the phase sentence, *Which one to use*, *written by hand when its directory is created, and never by migration*. `project_config.yaml:13–21` as claimed; marker `← PROJECT: set by each update`.
- **Match:** ✅

### V15: `.tfw/templates/briefing.md` (new)
- **RF claim:** four blocks bound to `Added`/`Changed`/`Fixed`/`Removed`; absent section → *nothing in this release*; no free text; last message; delivery recorded.
- **Actual:** file read: four `##` blocks in that order with an HTML comment naming the source section on each; canonical-template comment states *FOUR BLOCKS, FOUR CHANGELOG SECTIONS, and nothing else*, the *nothing in this release* rule, that `Why this release exists`/`Verification`/`Known open`/`Canon` are not read, *NO FREE TEXT*, and the delivery/checklist rule. The rendered `briefing_dirty3_to_dirty5.md` follows it: every bullet prefixed by the entry it comes from; `.4` has *nothing in this release* under Added and Removed.
- **Match:** ✅

### V16: `.tfw/migrations/2.0.0.md`
- **RF claim:** step 1 opens with the target's `update.md`; every command from the root (`cd .tfw` rewritten); `--working-tree` sentence; one manifest location `tasks/MIGRATION-2.0.0.md`; the two manifest sections to read; step 3a phase state by hand; multi-signal rows under `UNDECLARED`; three grammars unchanged.
- **Actual:** diff read — all eight present: `:42–44` `--working-tree` sentence; `:55–58` *First: open the target's `update.md`, not yours*; `:66–69` the `find .tfw/templates .tfw/workflows` form; `:73–74` *Every command in this guide runs from the project root*; `:104–109` `--manifest tasks/MIGRATION-2.0.0.md` and *One location for the manifest*; `:113–123` the two sections; `:151–153` three grammars unchanged; `:167–178` `### 3a. Author phase state by hand`; `:257–260` two-signal cells under `UNDECLARED`. Grep for the four retired wordings over the three templates and the guide: **no match** (exit 1).
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | **315 passed, 1 skipped**, 153.58 s, exit 0 — equals RF §4 |
| 2 | `python .tfw/scripts/gen_index.py --check tasks` | 6 `note:` lines over 17 directories; *54 tasks validate*; exit 0 |
| 3 | `python .tfw/scripts/gen_index.py --check project` | *consistent with the release it declares*; `2.0.0-dirty.4`, 1 participant, creates in `workspace` |
| 4 | `wc -w .tfw/workflows/update.md` | 1174 |
| 5 | `cmp` × 6 workflow copies · `cmp .agent/rules/tfw.md …template` · `diff` of the two `TFW:CLAUDE` regions | all identical |
| 6 | `grep -c "{version}"` over three adapter templates | 0 · 0 · 0 |
| 7 | `classify_status()` on ten hand-picked cells (see V2) | matches the RF rule on every cell, including `A+B`, `→`, `=`/`<`, a bare `U+FE0F` |
| 8 | Fixture `fx_if` (scratchpad): `--check project` with `installed_from: "D:/…@v2.0.0-dirty.4"` → then `steps-framework@…` → then a URL | machine-local: *1 problem(s) … is machine-local … Not rewritten*, **exit 1**; symbolic and URL: consistent, exit 0 |
| 9 | Fixture `fx_ph` (scratchpad): task at `PHASES`, `phase-a/status.md` present, `phase-b/` empty → `--check tasks`; then the task set `DONE` | live: *1 phase directory carry no status.md while the task is PHASES: phase-b — author … phase state is not written by migration*, **exit 1**; terminal: `note: … informational, the task is DONE`, exit 0. Nothing written to `phase-b/` |
| 10 | `git diff --shortstat b9baec2 d047286 -- <26 counted paths>` | 26 files, 943+ / 172− — equals the RF header |
| 11 | `git diff 56c3d70 e8690c7` and `git diff e8690c7 HEAD` on the master HL | first = A7 only (deliverable 6 + §12 row); second = empty |
| 12 | `git tag -l` in this repository | no `v9.9.9-fabricated`, no `v2.0.0-dirty.5-dryrun` — the scratch-clone claim holds |
| 13 | `git -C {consumer} status --short` for `innoforce-ai-first`, `kaznpu-ai-lab`, `helpdesk` | first two clean; `helpdesk` carries HD-31 work of another session, no `.tfw/` or adapter change — nothing written by this phase |
| 14 | `grep -rn -E "provider family\|humans and agents alike\|cd \.tfw\|MIGRATION\.md\b"` over the three templates and the guide | no match, exit 1 |
| 15 | `python -c "import gen_docs"` from `docs/` | fails on `docs_dir` configuration — confirms RF §6 O8 (module-load import) |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | *"over 114 rows on four pinned corpora, category S entire refused three single-signal rows … `So` refuses exactly the eight rows"* | RF §2 item 1; ONB §3 Q1 table | `status_cell_before_after.txt` §4 lists the four pins (`eadfb13`, `58329e7`, `744cad3`, `aec5f2d`), 61+17+4+32 = 114 rows, the 8 CLASS rows each with its second signals, the 3 TEXT-only rows; command 7 reproduces the rule on the three `Sm` rows | ✅ |
| C2 | *"22 of 28 new tests fail before, 28 pass after"* and *"315 passed, 1 skipped"* | RF §3 AC-8, §4 | `status_cell_before_after.txt` §1 (22 `FAILED` ids, `22 failed, 6 passed`; `28 passed`); command 1 reproduces 315/1 | ✅ |
| C3 | *"Step 0 … on a clone 29 commits ahead of `v2.0.0-dirty.4`, PASS; fabricated tag, STOP"* | RF §3 AC-1 | `pin_on_live_source.txt`: source `HEAD 4fe3b1d`, tag `51677ff`, Run 1 PASS with `source_head=51677ff…`, Run 1b the old rule STOP, Run 2 `v9.9.9-fabricated` STOP, Run 3 missing tag STOP, Step 5 recheck both branches. The SHAs are this repository's | ✅ |
| C4 | *"the owner wants change presented positively … 'because people do not like change'"* | RF §7 FC1; A7 evidence | Fifth field report `:58–60`: «Я ожидал, что ты меня заонбордишь нормально… спросишь кто, где я хочу хранить задачи… преподносилось положительно» | ✅ |
| C5 | *"`gen_docs.py`'s `task_id_source` resolves both examples"* | RF §3 AC-9 gate; EV E29 | `carriers.txt`: the direct call **failed** (`mkdocs.yml` import at module load, O8); the addendum extracted the regex from the file and matched the two filenames by hand. Independently: `docs/scripts/test_gen_docs.py::test_current_identifier_artifact_phase_hl_and_bare_refs_resolve` (pre-existing, Phase AB) writes `HL-TFW_20260829-010832_CRSW.md` and asserts `[HL-{task_id}]` resolves — the same grammar as the example, run inside the green suite | ⚠️ holds, by a test the EV does not cite — see D2 |
| C6 | TD-190, TD-191, TD-198, TD-200, TD-201, TD-203, TD-204 are the debt rows the RF says it closes | RF §1 table; TS §2 | `TECH_DEBT.md:104–118`: all seven rows exist, all `⬜ Open/Backlog` before this phase, and each row's description matches the fix delivered (V12–V16, V7, V11) | ✅ |

## Discrepancies Found

- **D1 — `update.md` Step 0, commit-target path (Low).** Prose: *"The operator names the target — a tag, or a commit when the owner deliberately takes an untagged payload and says so in the checklist."* The block that follows tests `"$target_ref" = "v$target"`; with a commit named, `$target_ref` is a SHA and the test cannot pass, and the stop sentence names only *tag missing or `VERSION` disagrees*. A receiver following the block literally in the commit case stops without being told what check replaces the tag test. The TS (AC-1 bullet 1) admits the commit case and states no check for it either, so this is not a missed AC item; it is the workflow leaving one admitted path without an executable instruction — the class deliverable 2 exists to close. → TD (Low), not a REVISE ground: the tag path, which every gate and every field run uses, is complete.
- **D2 — EV E29 evidence sufficiency (Low, review note).** The gate *"`gen_docs.py` resolves the example filename"* is marked VERIFIED on a hand-extracted regex after the direct call failed. The claim is true and is established by an existing test in the suite (C5), which the EV should have cited instead. No file change needed; recorded for Judge row 8.

Both are below the bar that would flip a verdict; since verification already stands at 100% of the counted set, no further escalation is available or needed.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | `evidence/EV__phase-ac__update_without_guesswork.md` — 37 rows, 34 VERIFIED / 3 DEFERRED | ✅ 87 lines | ✅ — 37 rows counted; E6, E34, E35 DEFERRED each name the blocker (`/tfw-release`, the tag, the field run), as the TS assigns |
| E2 | `pin_on_live_source.txt` (AC-1) | ✅ 40 lines | ✅ — four runs plus the Step 5 recheck, commands verbatim, SHAs are this repository's; no fabricated tag in this repository (command 12) |
| E3 | `skipped_tag_read_through.txt` (AC-2) | ✅ 78 lines | ✅ — the proposed `.5` section, steps A–D, the two closed dead references, what was appended and not; consistent with the CHANGELOG diff (V12) |
| E4 | `gates_and_word_count.txt` (AC-3, AC-6) | ✅ 110 lines | ✅ — 7/7 hits inside on this repository, 5/5 on `innoforce-ai-first`, 0 outside on both; 1174 words (reproduced); AG dry-run transcript with fingerprint `ed9b10eece8257e2` before/after, `git user.name` = `Fixture Owner` present and unused, no `team/` created. The dry run is an agent following the rewritten text in a scratch fixture; the fixture no longer exists, so the transcript is not re-runnable — see judge row 8 |
| E5 | `markers_and_exclusions.txt` (AC-4, AC-7) | ✅ 66 lines | ✅ — marker lines, region `cmp` before/after, consumer dry check (sha256 unchanged), 38-line block identical (reproduced), `{version}` census (reproduced), the copy loop output with two `skipped:` lines and two `cmp` identical, 5 targeted tests passed |
| E6 | `installed_from_check.txt` (AC-5) | ✅ 67 lines | ✅ — four forms, exit codes 1/0/0/0, config byte-identical; reproduced on my own fixture (command 8) |
| E7 | `status_cell_before_after.txt` (AC-8) | ✅ 141 lines | ✅ — 22-fail/28-pass, three `--check tasks` fixture runs (reproduced on my own fixture, command 9), the repository run (reproduced), four pinned corpora 8 CLASS / 3 TEXT / 103 identical, the manifest's new sections |
| E8 | `carriers.txt` (AC-9, AC-10) | ✅ 105 lines | ⚠️ — five excerpts match the live files (V7, V8); grep clean (reproduced); root-run command with one `RETIRED:` line; **the `gen_docs.py` resolution is a hand-check after a failed import** (D2) — established instead by the suite's existing test |
| E9 | `briefing_dirty3_to_dirty5.md` (AC-6) | ✅ 54 lines | ✅ — four blocks, every bullet tagged `.4`/`.5`, *nothing in this release* where `.4` has no section; `.5` bullets marked as re-derived at release |

## Knowledge Citations Verified

HL §7.2 carries 29 rows (master HL, free section, unchanged by this phase); ONB §7 confirms all 29 and adds N1–N3. PV priorities 0–4 scanned in full; 5–7 by relevance. Every link resolved with `grep` against the live files at review.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | HL §7.2 #1 / ONB 1 | PV 0 — `README.md` opening, § How It Works: resumability from shared traces | ✅ | ✅ | ✅ | ✅ — the briefing and the three questions make an update resumable by the owner, not only the agent |
| 2 | HL §7.2 #2 / ONB 2 | PV 0 — `.tfw/README.md#ns1`, `#ns2` principles 3 and 5 | ✅ anchors present at `:72`, `:79` | ✅ | ✅ NS1 *continue without rebuilding the original conversation*; NS2-3 *Selected Trace*; NS2-5 *Continuation over isolated output* | ✅ — `UNDECLARED` keeps the cell verbatim; the checklist and briefing are the continuation record |
| 3 | HL §7.2 #3 / ONB 3 | PV 1 — Methodology values, *Structural Enforcement* | ✅ `#methodology-values` | ✅ | ✅ *a rule that cannot reveal its own violation is only advice* | ✅ — word-count gate, exclusion-list test, phase-state line, `installed_from` check, TD-198 registry row; checked separately from priority 0 though both live in `.tfw/README.md` |
| 4 | HL §7.2 #4 / ONB 4 | PV 1 — *Where truth belongs* | ✅ | ✅ | ✅ one authoritative owner per truth | ✅ — a status the tool cannot read whole is refused; the owner resolves with an event |
| 5 | HL §7.2 #5 / ONB 5 | PV 1 — Methodology values *Portability* + Success Criteria | ✅ | ✅ | ✅ | ✅ — `git rev-parse`, `cmp`, `find` — no provider API |
| 6 | HL §7.2 #6–10 / ONB 6–10 | PV 2 — `knowledge/philosophy.md` F4, F11, F27, F34, F38 | ✅ | ✅ all five rows present | ✅ F4 structural gates; F11 no extra entities; F27 observable progress; F34 vague request → usable result; F38 finite attention | ✅ — F11's application to the one new artifact (`briefing.md` replaces the improvised summary) is the §7.1 "which duplicate write it removes" answer; F34 is the fifth report's owner account |
| 7 | HL §7.2 #11–15 / ONB 11–15 | PV 3 — `KNOWLEDGE.md` D31, D50, D37, D43, D55, D59, D65 | ✅ | ✅ | ✅ | ✅ — D37/D43 correctly N/A; D65 → CHANGELOG appended never rewritten; D55/D59 → commit grammar, handle never inferred |
| 8 | HL §7.2 #16–17 / ONB 16–17 | PV 4 — `conventions.md` §§3–5, §13, §14 | ✅ | ✅ | ✅ §5 `UNDECLARED` two-act table; §4 *Which handle a machine acts as* | ✅ |
| 9 | HL §7.2 #18 / ONB 18 | PV 5 — `knowledge/convention.md` F22 | ✅ | ✅ | ✅ | ✅ N/A stated with reason |
| 10 | HL §7.2 #19 / ONB 19 | PV 6 — `knowledge/process.md` F7, F30 | ✅ | ✅ | ✅ | ✅ — checklist records the three answers and the delivery |
| 11 | HL §7.2 #20–21 / ONB 20–21 | PV 7 — `knowledge/risk.md` F1; `knowledge/constraint.md` F1, F3 | ✅ | ✅ | ✅ | ✅ — F3 grounds the briefing's *no free text* |
| 12 | HL §7.2 #22–29 / ONB 22–29 | RES 1–2 external sources | ✅ (external URLs not re-fetched; unchanged since the freeze) | — | — | ✅ — #24 `git-rev-parse` is the pin mechanism; the rest N/A with reasons |
| 13 | ONB N1 | PV 3 — `KNOWLEDGE.md` D69 | ✅ | ✅ | ✅ one dispatcher, `malformed` the only fallback; `ABBR` owner-approved in the planning exchange | ✅ — AC-8 applies the rule to the second cell; AC-9 gives the approval its subject. **Note for `/tfw-docs`:** D69's abbreviation sentence now lags the shipped rule (initials of the title, proposed with it) — an index update, not a contradiction |
| 14 | ONB N2 | PV 4 — `conventions.md` §10.3 File Classification | ✅ | ✅ | ✅ *State files are NEVER sourced from upstream* | ✅ — grounds AC-7 and O11 |
| 15 | ONB N3 | PV 4 — `conventions.md` §11 Design Rules ≤ 1200 words | ✅ | ✅ | ✅ | ✅ — the AC-6 ceiling is the framework's own rule |

Total: 32 (29 + N1–N3), resolved: 32, semantically verified: 32, irrelevant: 0, hallucinated: 0.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings? — 24 of 26 read, 2 executed; ratio 1.0
- [x] Ran at least 1 build/test command (or documented why not)? — 15 commands, including the full suite
- [x] Claim & Source Checks filled — 2-3 key claims spot-checked, every citation traced to a real artifact, data claims checked against a primary source (or explicit N/A with a reason)? — C1–C6
- [x] Each RF §3 (AC) checkmark verified against actual file? — V1–V16 cover every ticked box; the two unticked AC-11 boxes are release/field acts
- [x] KNOWLEDGE.md checked — contradictions with changes documented? — none; D69 lags the abbreviation rule (index update for `/tfw-docs`)
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist, meanings match, applications are relevant)?
  - Total: 32, resolved: 32, semantically verified: 32, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified (files exist, claims match)?
  - Total evidence items: 37 EV rows in 9 artifacts; verified: 34 as VERIFIED with one ⚠️ (E29 → D2), 3 DEFERRED with named blockers; missing: 0

Stage complete: YES
