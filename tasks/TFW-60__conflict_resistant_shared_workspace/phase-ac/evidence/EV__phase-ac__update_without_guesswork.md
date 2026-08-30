# EV — TFW-60 / Phase AC: Update Without Guesswork

> **Date**: 2026-08-30
> **Author**: Claude Code (Executor), `on_behalf_of: saubakirov`, `via: claude-code`
> **Task**: TFW-60
> **TS**: [TS Phase AC](../TS__phase-ac__update_without_guesswork.md) — revision 2, amendment A7 approved
> **Measured at**: `d047286` (implementation), against `b9baec2` (TS approval) as the before-state

---

## Environment

| Field | Value |
|-------|-------|
| OS | Windows 11 Pro 10.0.26200, Git Bash (POSIX sh) for every command in this folder |
| Language / Runtime | Python 3.13.5, pytest; Git 2.42.0.windows.1 |
| Database | N/A |
| Deploy target | this repository (framework as its own consumer); a scratch clone of it under the session scratchpad for the pin runs; three local consumer checkouts read-only (`innoforce-ai-first`, `kaznpu-ai-lab`, `helpdesk`, all on `2.0.0-dirty.4`); fixture projects under the scratchpad for the copy, marker, gate and dry-run tests |
| CI / Pipeline | local — `python -m pytest .tfw/scripts/ docs/scripts/ -q` |

Nothing in any consumer checkout was written; each consumer read is a `grep`, `git show` or `sha256sum`.
The fabricated tag and the dry-run payload tag exist only in the scratch clone.

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Step 0 as rewritten, run on a clone whose `HEAD` is 29 commits past `v2.0.0-dirty.4`: the operator names the tag, `source_head` is derived from it, `VERSION` at that commit equals the tag's name → PASS. The old Step 0 on the same source → STOP (the fourth report's defect 6, reproduced) | scratch clone | VERIFIED | `pin_on_live_source.txt` Run 1, 1b |
| E2 | AC-1 | A fabricated tag `v9.9.9-fabricated` on the `.4` commit: `VERSION` reads `2.0.0-dirty.4` ≠ tag name → STOP; a tag that does not exist → `rev-parse --verify` fails, nothing pinned | scratch clone | VERIFIED | `pin_on_live_source.txt` Run 2, 3 |
| E3 | AC-1 | Step 5 recheck compares the tag's commit with the derived pin: a source that moved *elsewhere* (new commit on `HEAD`) is not reported; the tag itself moved → STOP before adapter sync. `status --porcelain -- .tfw/` rule kept as written | scratch clone | VERIFIED | `pin_on_live_source.txt` last section; `update.md` Step 0/5 |
| E4 | AC-2 | A `.2` reader follows the proposed `.5` updating section to every instruction of the `.3` and `.4` sections through two pointer lines; the `.3` entry gained the verbatim retired sentence (TD-198) and what a project that went thin does; the `.2` `TD-11` paragraph closed with a dated line (TD-191); the `2.0.0-dirty` fence carries `> **Superseded by**` (TD-190); nothing rewritten in substance | repository, CHANGELOG | VERIFIED | `skipped_tag_read_through.txt`; `.tfw/CHANGELOG.md` diff |
| E5 | AC-2 | `update.md` opens with Step −1; the migration guide's step 1 opens with the same instruction; RELEASE.md §5 carries the three rules (reach every tag, quote retired wording, superseded-by line) and §6 step 3 names them | repository | VERIFIED | `update.md`:11–15; `2.0.0.md`:55–59; `RELEASE.md`:46–48, :57 |
| E6 | AC-2 | The `.5` entry's own updating section — `/tfw-release` writes it after review; the RF hands over its required content | — | DEFERRED — `/tfw-release`, per TS AC-11 | `skipped_tag_read_through.txt` §"What the .5 entry must say" |
| E7 | AC-3 | Allowlist reworded to *text whose purpose is to retire the term*; the six known hits (`update.md`, `init.md`, four copies) plus the guide's deletion instruction classified with their preceding line: 7 of 7 inside, **0 outside** on this repository | repository | VERIFIED | `gates_and_word_count.txt` §"This repository" |
| E8 | AC-3 | Same search on consumer `innoforce-ai-first` (installed `.4` payload and adapter layers, read-only): 5 hits, all retirement instructions, **0 outside**; its live config carries no retired key | consumer, read-only | VERIFIED | `gates_and_word_count.txt` §"Consumer" |
| E9 | AC-4 | `CLAUDE.md.template` carries `<!-- TFW:CLAUDE:START/END -->` around the `## TFW` section; the block is brought current (context loading names `status.md`, command table carries `/tfw-knowledge` and `/tfw-config`, `Version: see .tfw/VERSION`) | repository | VERIFIED | `markers_and_exclusions.txt` AC-4.1; template |
| E10 | AC-4 | Fixture `CLAUDE.md` with project text above and below a stale block: after sync the marker-bounded region `cmp`-equals the template's and every byte outside is unchanged; the same as a test (`test_a_marker_bounded_sync_leaves_project_text_untouched`) | fixture | VERIFIED | `markers_and_exclusions.txt` AC-4.2 |
| E11 | AC-4 | First-run rule: a file without markers is reported and left untouched — the test `test_a_file_without_markers_is_reported_and_left_untouched`, and a read-only dry check on `innoforce-ai-first/CLAUDE.md` (0 markers; sha256 unchanged). The rule stated once in conventions §9; Step 6, both adapter READMEs point to it; Codex README `:104` no longer appends | fixture; consumer read-only | VERIFIED | `markers_and_exclusions.txt` AC-4.3; `conventions.md` §9 |
| E12 | AC-4 | Step 6 table carries a `Kind` column: Claude rules and Codex routing are blocks, five rows are copies. Antigravity template = rendered `.agent/rules/tfw.md` byte for byte; Cursor template and Claude template carry no `{version}` (R2); test `test_no_adapter_template_requires_a_version_substitution` | repository | VERIFIED | `markers_and_exclusions.txt` AC-4.5; `update.md`:115–123 |
| E13 | AC-4 | The framework is its own first consumer: root `CLAUDE.md` carries the block, 38 lines between markers identical to the template's; checked by `test_installed_adapter_copies_match_their_sources` (R2) | repository | VERIFIED | `markers_and_exclusions.txt` AC-4.4 |
| E14 | AC-5 | Form `{upstream}@{verified-tag}` stated in `update.md` Step 7 and `templates/project_config.yaml`; `--check project` on fixtures: `D:/…@v…` → 1 problem *machine-local*, config byte-identical; `steps-framework@v…`, a URL, `self`, `unrecorded` → consistent | fixtures | VERIFIED | `installed_from_check.txt` |
| E15 | AC-6 | Step 3 gate: three questions (handle asked, never inferred; containers; `build.*`), AG-mode rule (one message, read-only steps continue, stop at the write), answers recorded in the checklist | repository | VERIFIED | `update.md`:50–66 |
| E16 | AC-6 | AG-mode dry run against a fixture consumer on `.3` (no `team/`, placeholders, own `knowledge_state.yaml`) with a scratch-clone target carrying this phase's payload: Steps −1, 0, 1, 2 executed, Step 3 stopped with the three questions as one message; fingerprint of every fixture file outside staging identical before/after; `git status` empty; no `team/` created; `git user.name` (`Fixture Owner`) present in the environment and not used | fixture + scratch clone | VERIFIED | `gates_and_word_count.txt` §"AG-mode dry run" |
| E17 | AC-6 | Step 8a and `templates/briefing.md`: four blocks from `Added` / `Changed` / `Fixed` / `Removed` (A7), absent section → *nothing in this release*, no free text, last message, checklist records delivery. Rendered for this repository's `.3 → .5` delta — `.4` bullets from the CHANGELOG, `.5` bullets from the RF's proposed entry, labelled as such | repository | VERIFIED — `.5` bullets to be re-derived when `/tfw-release` cuts the entry | `briefing_dirty3_to_dirty5.md`; `templates/briefing.md` |
| E18 | AC-6 | `update.md` word count with Steps −1, 3, 5, 6-column, 8a: **1174** (ceiling 1200); copies byte-identical | repository | VERIFIED | `gates_and_word_count.txt` §"word count" |
| E19 | AC-7 | Step 5 names the two exclusions and carries the copy loop that prints `skipped:`; fixture with customized `project_config.yaml` and non-framework `knowledge_state.yaml`: both byte-identical after the copy, both printed as skipped, other files copied | fixture | VERIFIED | `markers_and_exclusions.txt` §AC-7 |
| E20 | AC-7 | Executor decision recorded: exclusion list carries both files, payload keeps carrying them (R2 accepted). `test_every_project_owned_payload_file_is_excluded_from_the_copy` derives the project-owned set from the payload (root `.yaml` with a template counterpart) and requires each name in Step 5's `case` pattern | repository | VERIFIED | `markers_and_exclusions.txt` last section; `test_integration.py` |
| E21 | AC-8 | `classify_status()`: one declared token + free text with no further declared token and no `So` symbol; `U+FE0F`/`U+200D` skipped. Fixture rows: `AILAB-2` exact shape, second emoji alone, second token alone, `→`/`+`/`=`/`<` as non-signals, bare variation selector — **22 of 28 new tests fail before, 28 pass after** | repository | VERIFIED | `status_cell_before_after.txt` §1 |
| E22 | AC-8 | An `UNDECLARED` multi-signal row is never terminal and never skipped: `plan()` writes `status.md` at `UNDECLARED` with `lifecycle_verbatim`, no `outcome`; a single terminal token still closes a row | fixture | VERIFIED | `status_cell_before_after.txt` §1, §5 |
| E23 | AC-8 | Manifest: new heading *Rows carrying more than one lifecycle signal* naming each row and its signals; *Task state written* note no longer says *Only for non-terminal tasks*; *Phase directories* section names every `phase-*` of every matched task with present/absent and the sentence *phase state is not written by migration; author `{phase}/status.md` by hand* | fixture (kaznpu shape) | VERIFIED | `status_cell_before_after.txt` §5 |
| E24 | AC-8 | `--check tasks` on a fixture: live task + stateless phase → **failure** naming `phase-b`; terminal task → informational; task without its own `status.md` → informational; malformed task state → informational with the reason. Nothing written | fixture | VERIFIED | `status_cell_before_after.txt` §2 |
| E25 | AC-8 | `--check tasks` on this repository: 6 informational lines (one per task, R2) over 17 directories under TFW-42/46/47/52/53/55, 54 tasks validate, exit 0; also a repository test | repository | VERIFIED | `status_cell_before_after.txt` §3 |
| E26 | AC-8 | Four pinned corpora (framework `eadfb13`, innoforce `58329e7`, kaznpu `744cad3`, helpdesk `aec5f2d`), 114 identified rows: **8 class changes**, every one a second `So` symbol or a second declared token; 3 text-only differences where `+`/`→` now survive in the outcome; 103 rows identical | four corpora at pins | VERIFIED | `status_cell_before_after.txt` §4 |
| E27 | AC-8 | `templates/status.md` carries the phase sentence and says when to use which; the migration guide says all of it in the order met (step 1 Step −1 → step 2 manifest sections → step 3a phase state by hand → `--check tasks`) | repository | VERIFIED | `carriers.txt`; `2.0.0.md`:113–123, :183–195 |
| E28 | AC-9 | One rule, five carriers: conventions §4 Identifier (acronym of the approved title, proposed with it, *never derived silently* said both ways, `UPD` anti-pattern), Artifact file naming (current-grammar rows, no title appended), `plan.md` 3.5 and 4.2, `init.md` Batch 1 and Mini-Setup 6, glossary Task Naming, HL template **Title** then **Abbreviation** | repository | VERIFIED | `carriers.txt` §AC-9 |
| E29 | AC-9 | `gen_docs.py` `task_id_source` resolves `HL-TFW_20260829-172110_ABT.md` and `RES__TFW_20260829-172110_ABT.md` to `TFW_20260829-172110_ABT`; `gen_index.parse_identifier` agrees | repository | VERIFIED | `carriers.txt` addendum |
| E30 | AC-10 | `event.md` `:49`, `:70`: `via` free-form non-empty provider/tool text (TD-200); `profile.md`: one file per person, role and context in `team/README.md`, `since` defined, `type: agent` admitted and unusable (TD-203); guide: one manifest location, `--working-tree` sentence, `cd .tfw` rewritten, every command from the root | repository | VERIFIED | `carriers.txt` §AC-10 |
| E31 | AC-10 | `grep` for the four retired wordings (*provider family*, *humans and agents alike*, `cd .tfw`, `--manifest MIGRATION.md`) over the three templates and the guide: no match; the guide's retired-files command run from the project root as written, one `RETIRED:` line on a deliberately thinned staging copy, no `cd` survived | repository | VERIFIED | `carriers.txt` §AC-10 |
| E32 | AC-11 | RF §1 states what a project on `.2`, `.3` or `.4` must know, in the form of the `.5` updating section | — | VERIFIED | RF §1; `skipped_tag_read_through.txt` |
| E33 | AC-11 | Every fifth-report §6 item and fourth-report defect 7: fixed with a one-line reason or recorded in RF §6 | — | VERIFIED | RF §3 AC-11, §6 |
| E34 | AC-11 | Version bump, CHANGELOG entry and tag as one act; the tag verified to exist | — | DEFERRED — `/tfw-release`, after review | — |
| E35 | AC-11 | One consumer already on the line updates to the new tag from Step −1 with the pin, the three questions and the briefing on record | — | DEFERRED — field run, after the tag exists | — |
| E36 | AC-11 | `2.0.0` not claimed: `VERSION` still `2.0.0-dirty.4`; nothing in this phase names `2.0.0` as released | repository | VERIFIED | `git show HEAD:.tfw/VERSION` |
| E37 | regression | Full suite `python -m pytest .tfw/scripts/ docs/scripts/ -q`: **315 passed, 1 skipped** (283 + 1 before; +32 tests); `--check tasks` 54 validate; `--check project` consistent | repository | VERIFIED | RF §4 |

## Verdict

Evidence verdict: **34/37 VERIFIED, 3 DEFERRED, 0 BLOCKED, 0 N/A** — the three deferred rows are the `.5`
CHANGELOG entry, the tag and the consumer run, all of which the TS assigns to `/tfw-release` and the
field after review.

## Attachments

| File | Description |
|------|-------------|
| `pin_on_live_source.txt` | AC-1 — Step 0 old vs new on a live source, fabricated tag, missing tag, Step 5 recheck; commands verbatim |
| `skipped_tag_read_through.txt` | AC-2 — the `.2` reader's path; the `.5` updating section the RF hands to `/tfw-release`; what was appended to the CHANGELOG |
| `gates_and_word_count.txt` | AC-3, AC-6 — allowlist runs on the repository and one consumer, word count, the AG-mode dry-run transcript |
| `markers_and_exclusions.txt` | AC-4, AC-7 — marker regions before/after, consumer dry check, template `{version}` census, the copy step output and `cmp` |
| `installed_from_check.txt` | AC-5 — `--check project` on four `installed_from` forms; the three consumers' current values |
| `status_cell_before_after.txt` | AC-8 — the fixture failing before / passing after, `--check tasks` runs, four pinned corpora identifier by identifier, the manifest's new sections |
| `carriers.txt` | AC-9, AC-10 — the five excerpts, `gen_docs` resolution, the grep, the root-run command |
| `briefing_dirty3_to_dirty5.md` | AC-6 — the briefing rendered for this repository's `.3 → .5` delta |

---

*EV — TFW-60 / Phase AC: Update Without Guesswork | 2026-08-30*
