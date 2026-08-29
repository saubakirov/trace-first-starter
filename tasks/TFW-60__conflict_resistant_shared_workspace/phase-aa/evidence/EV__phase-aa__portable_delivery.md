# EV — TFW-60 / Phase AA: Portable Delivery

> **Date**: 2026-08-27
> **Author**: Claude Code (Executor), `actor: saubakirov`, `via: claude`
> **Task**: TFW-60
> **TS**: [TS Phase AA](../TS__phase-aa__portable_delivery.md) at revision 3
> **Pinned at**: `1079020` for every measurement in this file, re-checked at revision 2 (see
> the revision note below). Two unrelated files (TFW-55, TFW-54) are dirty in the working
> tree and are **deliberately excluded** from every commit of this phase — per the ONB Risk 6
> ruling, another task's artifacts are not committed to make this measurement clean.
>
> **Revision 2** — 2026-08-28, after REVIEW `440d6fd` returned 🔄 REVISE. Three rows are
> corrected in place and none is re-run: **E47** carries its `__pycache__` caveat at the row
> instead of in a sibling artifact; **E60** states what its test enforces rather than claiming
> a class it does not reach; **E13**'s artifact now records both parser measurements. Two rows
> are **added** — E61 and E62 — for the revision's own work.

---

## Environment

| Field | Value |
|-------|-------|
| OS | Windows 11 Pro 10.0.26200 |
| Language / Runtime | Python 3.13.5 |
| Shell | Git Bash (POSIX sh) |
| Deploy target | n/a — the deliverable is a payload of ordinary files |
| CI / Pipeline | local. `.github/workflows/docs.yml` runs `mkdocs build` only and **no pipeline runs pytest**, verified |
| External fixture | `KZ-IT-telegram-list` cloned at `c919640` into the session scratch directory, TFW `1.3.0`. The live project was never written to |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Four scripts live at `.tfw/scripts/`, moved with `git mv`. `git log --follow` returns 8 commits for `gen_index.py` and 5 for `migrate_board.py` — history followed | source repo at `1079020` | VERIFIED | `git log --oneline --follow`, quoted in [fixture_run.txt](fixture_run.txt) header; renames visible as `{docs => .tfw}/scripts/...` in `git show --stat f14f744` |
| E2 | AC-1 | **The depth test that actually observes the defect.** Tools copied to `tools/`, `tools/tfw/` and `a/b/c/d/` inside the fixture. `parents[2]` would have resolved **wrong in two of three** — `tools/` to a directory outside the project entirely. The marker search resolved correctly in all three | fixture project | VERIFIED | [fixture_run.txt](fixture_run.txt) § "AC-1's real gate", and [fixture_report.md](fixture_report.md) § F1 |
| E3 | AC-1 | Gate grep: every hit outside `tasks/` classified — 8 in the CHANGELOG (historical entry + the new entry quoting the old path to explain the finding), 1 in the guide (explains the provenance comment), 1 in a test (a deliberate stale-path fixture), 1 in `KNOWLEDGE.md` (the known exception named in AC-1's own gate). 26 historical trace artifacts and 11 provenance comments untouched | source repo | VERIFIED | [ac1_gate.txt](ac1_gate.txt) |
| E4 | AC-1 | No `.tfw/scripts/README.md` exists (R3). Root-resolution rule stated in `--help` output and in `conventions.md` § "Where the tooling lives" | source repo | VERIFIED | `ls .tfw/scripts/` → 4 files, no README; `conventions.md` §4 |
| E5 | AC-1 | Full suite from the new location: **253 passed, 1 skipped** (baseline before the phase: 220 passed, 1 skipped). `mkdocs build` exit 0 | local | VERIFIED | `pytest .tfw/scripts/ docs/scripts/ -q`; `python -m mkdocs build --config-file docs/mkdocs.yml` → `Documentation built in 264.34 seconds`, EXIT=0 |
| E6 | AC-2 | `.tfw/migrations/2.0.0.md` exists and names no fact private to this repository — no `[workspace, tasks]`, no 7,505 references, no 666 files. The ordering constraint is stated at each step that would violate it, and again as the one unrecoverable mistake at step 5 | source repo | VERIFIED | `.tfw/migrations/2.0.0.md` |
| E7 | AC-2 | The guide was followed end to end by a reader who never opened the CHANGELOG, reaching `--check project` exit 0 | fixture project | VERIFIED | [fixture_run.txt](fixture_run.txt), steps 1–7 |
| E8 | AC-2 | `update.md` Step 3 routes to `.tfw/.upstream/.tfw/migrations/{major}.md`; the fixture's `1.3.0 → 2.0.0-dirty.2` crossed a major and the route fired | fixture project | VERIFIED | [fixture_run.txt](fixture_run.txt) § Step 3 → `2.0.0.md` |
| E9 | AC-2 | The guide names `build.*` as an operator edit (R2), the quiescence rule from AC-8, and the `task_containers` decision from AC-6 | source repo | VERIFIED | `.tfw/migrations/2.0.0.md` §§ "Before you start", "The order" step 1, "build.* keeps pointing at the old path" |
| E10 | AC-2 | The canon states a major release without a migration guide is incomplete | source repo | VERIFIED | `conventions.md` § "A major release ships a migration guide"; also §2 required-artifacts list |
| E11 | AC-3 | Fixture whose board is at `tasks/README.md` under `## Board`: with `--board`/`--board-heading` → **4 data rows**. Run with defaults → the refusal | fixture project | VERIFIED | [fixture_run.txt](fixture_run.txt) § "guide step 2", both attempts quoted |
| E12 | AC-3 | The zero-row refusal names **relocation first**, then the heading, then removal. Asserted by a test on ordering, not only on presence | local + fixture | VERIFIED | `test_a_zero_row_result_names_relocation_before_removal`; refusal text in [fixture_run.txt](fixture_run.txt) |
| E13 | AC-3 | The row parser is untouched, **measured rather than asserted, both ways**: whole-function **40 → 45** lines with four differing code lines forming two replacements — the signature gaining the parameter and the locator using it — plus five added docstring lines; body-only **34 → 34** with one replacement. Every line that reads a row is byte-identical under either count. A nine-column header parses unmodified | local | VERIFIED | [ac3_parser_untouched.txt](ac3_parser_untouched.txt); `test_the_row_parser_is_untouched_by_a_wider_table` |
| E14 | AC-4 | The exact corpus that produced the finding: `TFW-01_single_underscore` beside `TFW-3__double__underscore`. Both appear. `backlog idea, never started` appears **nowhere** in the manifest, and the generated index has **no `Backlog` section at all** | fixture project | VERIFIED | [fixture_manifest.md](fixture_manifest.md), [fixture_index.md](fixture_index.md), and the assertions in [fixture_run.txt](fixture_run.txt) |
| E15 | AC-4 | Reported, never matched: `parse_identifier("TFW-01_single_underscore")` still returns `None` — no identifier rule changed | local | VERIFIED | `test_the_single_underscore_legacy_form_is_reported_not_matched` |
| E16 | AC-4 | The reason asserts only what is observable. A test forbids the words `idea`, `never started` and `backlog` in the rendered row | local | VERIFIED | `test_the_unresolved_reason_asserts_only_what_is_observable` |
| E17 | AC-4 | Manifest and index agree on classification and count: 2 unresolved in both, from one shared classification. Every identifier resolves by name | fixture project | VERIFIED | [fixture_manifest.md](fixture_manifest.md) § Reconciliation and § "Every board identifier, by name" |
| E18 | AC-4 | The migration guide tells the operator an unresolved directory may be renamed by hand | source repo | VERIFIED | `.tfw/migrations/2.0.0.md` § "What the manifest will tell you about odd directories" |
| E19 | AC-5 | Five values containing a colon-space, each error naming its key. Before: `unparseable front matter: ScannerError`, five times, no key | local | VERIFIED | [ac5_validator.txt](ac5_validator.txt) — before and after |
| E20 | AC-5 | The template's example quotes its prose values — all four, not only `title` — and states the rule with the invalid and valid forms side by side | source repo | VERIFIED | `.tfw/templates/status.md` |
| E21 | AC-5 | A complete worked example is reachable from the template **and is checked against the real validator**, so the template cannot ship an invalid example again | local | VERIFIED | `test_the_status_template_examples_parse_and_validate` |
| E22 | AC-5 | The no-mark fallback path is exercised, not assumed | local | VERIFIED | `test_a_parse_failure_with_no_mark_still_reports_something_usable` |
| E23 | AC-6 | `update.md` presents `task_containers` as a choice with its two real options and states it does not exist before 2.0.0; `initial_seq` is named as a key to delete | source repo | VERIFIED | `.tfw/workflows/update.md` § "Two keys that are decisions" |
| E24 | AC-6 | An operator following `update.md` made both choices deliberately: `[tasks]` chosen with a stated reason, `initial_seq: 3` deleted | fixture project | VERIFIED | [fixture_run.txt](fixture_run.txt) § "the two decisions update.md puts to the operator" |
| E25 | AC-7 | **No README template ships.** `update.md` and `init.md` create `team/` together with its first profile, and `init.md` does so at step 3 — before the first durable write, which its own step 7 is | source repo | VERIFIED | `.tfw/workflows/init.md` step 3; `.tfw/workflows/update.md` § "Create `team/`" |
| E26 | AC-7 | `.tfw/templates/team/profile.md` carries the short orientation and cites `conventions.md` §4 rather than restating the identity canon | source repo | VERIFIED | `.tfw/templates/team/profile.md` — 33 lines, down from 50 |
| E27 | AC-7 | A fixture with no `team/` : the step fired, the profile was written **from the payload template with nothing hand-carried**, and `--check project` reports the absence when it is missing | fixture project | VERIFIED | [fixture_run.txt](fixture_run.txt) § "guide step 6"; `test_check_project_reports_a_missing_team_directory` |
| E28 | AC-8 | `read_board()` defaults to a committed revision; the working tree is `--working-tree`. Asserted directly, and every one of the 45 migration tests now runs through the committed path because the fixture is a repository | local | VERIFIED | `test_the_committed_revision_is_the_default_source`; `_project(commit=True)` by default |
| E29 | AC-8 | AC-8's stated gate: the working-tree board changed during a run and the result is unaffected | local | VERIFIED | `test_a_working_tree_change_during_a_run_does_not_affect_the_result` |
| E30 | AC-8 | With no committed board the run **refuses**, names `--working-tree` and prints the revision it tried. No silent fallback | local | VERIFIED | `test_no_committed_board_refuses_and_names_the_opt_in` |
| E31 | AC-8 | AC-3 and AC-8 are one code path: `git show REV:<board-path>`, so a logged revision is always the revision read | local + fixture | VERIFIED | `read_board()` single implementation; `board source: git show HEAD:tasks/README.md` in [fixture_run.txt](fixture_run.txt) |
| E32 | AC-8 | The guide states the quiescence rule and gives its measured reason | source repo | VERIFIED | `.tfw/migrations/2.0.0.md` § "Before you start" |
| E33 | AC-9 | Three checks, one flag, three subjects. `--validate` and `--doctor` appear nowhere in the source, asserted by a test | local | VERIFIED | `test_the_three_checks_are_one_flag_with_a_subject` |
| E34 | AC-9 | The five-line disambiguating comment in `project_config.yaml` is **deleted**, not rewritten, and `build.verify` is `--check tasks` | source repo | VERIFIED | `git diff` on `.tfw/project_config.yaml`: `build` block 9 lines → 6 |
| E35 | AC-9 | `--check project` on this repository: exit 0, reporting version, participants and containers. On deliberately broken fixtures: missing `team/`, a `build` command naming a dead path, and a retired key each exit 1 | local | VERIFIED | four tests: `..._passes_on_a_consistent_project`, `..._reports_a_missing_team_directory`, `..._reports_a_build_command_naming_a_missing_path`, `..._reports_a_retired_key` |
| E36 | AC-9 | Every subject reports and exits — no check writes anything, asserted by byte-comparing the whole tree before and after all three | local | VERIFIED | `test_no_check_subject_writes_anything` |
| E37 | AC-9 | Each subject names what it did not check; `--check tasks` states it does not answer index freshness — the fact the deleted comment used to carry | local | VERIFIED | `test_check_tasks_says_it_does_not_answer_index_freshness`, `test_check_project_passes_on_a_consistent_project` |
| E38 | AC-9 | `--check project` is the last step of the migration guide, and of `init.md` | source repo | VERIFIED | `.tfw/migrations/2.0.0.md` step 7; `.tfw/workflows/init.md` step 8 |
| E39 | AC-10 | `update.md` Step 3a instructs the pristine-tag diff, states the measured reason, and says **whose** tag — the source's. The fixture has no TFW tags of its own, which is why this matters | source repo + fixture | VERIFIED | `.tfw/workflows/update.md` Step 3a; [fixture_run.txt](fixture_run.txt) § Step 3a |
| E40 | AC-10 | The sequence run against the source's `v1.3.0`: **2 customized files of ~38**, both project-owned. Everything else byte-identical and safely overwritten | fixture project | VERIFIED | [fixture_run.txt](fixture_run.txt) § Step 3a output |
| E41 | AC-10 | `tfw.upstream` accepts a local working tree, and the operator is told to verify the source's own `.tfw/` is clean at the tag. Verified clean before the run | source repo + fixture | VERIFIED | `.tfw/workflows/update.md` Step 0; `git status --porcelain -- .tfw/` empty, in [fixture_run.txt](fixture_run.txt) |
| E42 | AC-11 | `/tfw-research` routes to `.tfw/workflows/research/base.md` in **all three** adapter sources that named the non-existent file — the template plus the two READMEs added to the census at R2 | source repo | VERIFIED | `test_every_path_an_adapter_source_names_resolves` |
| E43 | AC-11 | The check fails first, then passes. A deliberately broken entry is caught, a good one is not flagged, and an annotated exemption is honoured | local | VERIFIED | `test_the_adapter_path_check_actually_fires`; the two checks failed on the three real broken files before the fix (recorded in the RF) |
| E44 | AC-11 | Propagated copies match their sources — all 22 workflow copies and all 11 Codex skills byte-identical | local | VERIFIED | `test_installed_adapter_copies_match_their_sources`; `cmp` sweep → "all copies in sync" |
| E45 | AC-12 | `plan.md`'s naming step is step 3 of Step 4, **after** the identifier exists. `Step 0` is gone. The question-first order is intact: Step 3 still asks and waits before any folder is created | source repo | VERIFIED | `.tfw/workflows/plan.md` — Step 3 § "Ask clarifying questions / 🛑 WAIT" precedes Step 4 |
| E46 | AC-12 | It is a numbered step, it repeats on a slug change, and it carries the phase when one was given | source repo | VERIFIED | `.tfw/workflows/plan.md` Step 4 item 3 |
| E47 | AC-13 half one | External corpus at `1.3.0` cloned to scratch; full `1.3.0 → 2.0.0-dirty.2` update completed. **0 files hand-carried. 0 framework files edited inside `.tfw/` — the transcript's own line reads `framework files edited inside .tfw/: 1`, and that one file is `.tfw/scripts/__pycache__/gen_index.cpython-313.pyc`, Python bytecode written by running the tool.** It is not an edit, and it produced its own finding: a receiving project whose `.gitignore` never needed a Python entry sees the payload dirty its tree on first use. Every local delta the first consumer invented is now unnecessary | fixture project | VERIFIED | [fixture_report.md](fixture_report.md) § finding 3, [fixture_run.txt](fixture_run.txt) § "AC-13 claim 1" |
| E48 | AC-13 half one | The live consumer project was **never written to** | — | VERIFIED | every fixture command ran under the scratch path; `git -C /d/projects/KZ-IT-telegram-list status` was read only |
| E49 | AC-13 half one | The fixture was pointed at a **commit SHA**, not a tag | fixture project | VERIFIED | `git -C {source} archive 1079020` in [fixture_run.txt](fixture_run.txt) |
| E50 | AC-13 half one | What was confusing is recorded, not only what worked — three items, plus three findings the fixture produced that no test here could have | — | VERIFIED | [fixture_report.md](fixture_report.md) §§ "Two findings…", "What was confusing" |
| E51 | **AC-13 half two** | **At least one real external project, updated by its own operator.** The executor cannot close this: a clone in a scratch directory driven by the author of the code is a development fixture, not acceptance evidence | — | **DEFERRED** | Blocker: requires the owner's own run on a real project, filed at task root as `FIELD-REPORT__TFW-60__second_external_update.md`. Per the ONB Q1 ruling and TS §7, an RF claiming this passed on the executor's own clone must be rejected. **Update, 2026-08-28: that artifact now exists — see E63.** The status here is deliberately left **DEFERRED**: E63 records what arrived and what I measured about it, and whether the phase's declared outcome is thereby met is a reviewer's and the owner's ruling, not the executor's to grant itself |
| E52 | AC-14 | `2.0.0-dirty.2` in `.tfw/VERSION` and `tfw.version`. Semver checked: `2.0.0-dirty.2 > 2.0.0-dirty` (larger pre-release set) and `< 2.0.0`, so the claim stays unmade. **Not** numbered as a patch | source repo | VERIFIED | `cat .tfw/VERSION` → `2.0.0-dirty.2`; `project_config.yaml:7` |
| E53 | AC-14 | The tag is **not** cut by the executor, per the ONB Q3 ruling (b): a tag on unreviewed work asserts releasability, which is the reviewer's finding | source repo | N/A | Intentionally out of the executor's scope. `git tag -l` shows no `v2.0.0-dirty.2` |
| E54 | AC-14 | The CHANGELOG entry states what the first external update found, including that the framework could not deliver its own tooling | source repo | VERIFIED | `.tfw/CHANGELOG.md` § `[2.0.0-dirty.2]` → "Why this release exists" |
| E55 | AC-14 | The current migration instruction no longer names a file a reader does not have: the guide is the procedure, and the new entry says explicitly to follow it rather than the old code fence | source repo | VERIFIED | `.tfw/CHANGELOG.md` § "Migration from `2.0.0-dirty`" closing note |
| E56 | AC-14 | The canon separates the two `UNDECLARED` acts — migration never normalizes, an accountable owner may resolve through a recorded transition | source repo | VERIFIED | `conventions.md` §5 table; `glossary.md` § UNDECLARED |
| E57 | AC-14 | The canon states that some artifacts legitimately have no journal event, so the closed vocabulary stays closed | source repo | VERIFIED | `conventions.md` §4, after the immutability rule |
| E58 | budget | Census counted before the first edit and re-derived after: **1 created, 7 moved, 25 modified** against limits of 15 new and 30 modified. `docs/mkdocs.yml` turned out to need no change, so the count is 25 rather than the 26 the census projected | source repo | VERIFIED | [census.md](census.md); `git show --stat` |
| E59 | DoF | The stray `phases/` directory: `git grep -c "phases/" -- .tfw/ docs/scripts/` → **no matches, exit 1**. Nothing this release ships produces it. Recorded, not chased | source repo | VERIFIED | command re-run at the pinned commit, output in [census.md](census.md) § "Also checked" |
| E60 | DoF | Runtime output is ASCII, enforced by a test rather than by fixing the occurrences found. **What the test actually enforces**, stated so its silence is not over-read: it scans payload script lines, toggles on a `print(` or `SystemExit(` and resets at a line ending in `)`, then rejects any non-ASCII character inside that span. So it covers a literal passed to a print or a raise — which is every case in these two files — and does **not** reach a message assembled into a variable and printed later. It caught 5 real occurrences, 2 of them written by this phase | local | VERIFIED | `test_every_runtime_message_is_ascii`; failing output recorded in RF §4 |
| E61 | REVIEW item 1 · AC-14 | **The payload no longer contradicts itself on the `UNDECLARED` rule.** `.tfw/templates/status.md` stated the retired absolute prohibition — verbatim the sentence this phase rewrote in `conventions.md` §5 and `glossary.md`. Corrected to the two-act rule, citing §5 rather than restating the table. Generalized: the retired **string** was grepped across the whole tree. It now appears in three places, none of them an instruction — the test registry that retires it, the historical field report that quotes it as the defect, and this row. A *paraphrase* of it — `normalizing it away is prohibited` — stands in `.tfw/CHANGELOG.md`'s `[2.0.0-dirty]` entry and is deliberately left: a changelog records what a release shipped | source repo | VERIFIED | `.tfw/templates/status.md`; `git grep -n "Normalizing such a value"` → 3 hits, all classified; `git grep -n prohibited -- .tfw/` → the paraphrase at `CHANGELOG.md:168` |
| E62 | REVIEW fact candidate 1 | **The class is now detectable rather than remembered.** `test_no_normative_file_states_a_retired_rule` checks a named registry of retired wordings against every file in the payload that *instructs* — templates, workflows, migrations, `conventions.md`, `glossary.md`, `README.md`, `quickstart.md`, `compilable_contract.md`. `CHANGELOG.md` is excluded by a stated rule, not a convenience: a changelog records. **Proven against the real defect:** run over `440d6fd:.tfw/templates/status.md` it reports the retired sentence at line 92; over the fixed file it is clean | local | VERIFIED | `test_no_normative_file_states_a_retired_rule`, `test_the_retired_rule_check_actually_fires`; before/after run recorded in RF §4 revision 2 |
| E63 | AC-13 half two — **the closing artifact arrived** | A second real external project, `innoforce-ai-first`, completed the full `1.3.0 → 2.0.0-dirty.2` update **and the board migration**, run by an operator who is not the author of this code. Its own report is filed at task root as `FIELD-REPORT__TFW-60__second_external_update.md`, copied verbatim and not authored here. **What I verified, read-only, without touching the project:** its delivered `.tfw/` against `v2.0.0-dirty.2` — **0 files missing, 0 stray framework files**, the only difference being `CHANGELOG.md` one commit behind because the run started before the tag's own record was written; `--check project` exit 0 (version, 2 participants, `task_containers` declared as a deliberate `[workspace, tasks]`); `--check tasks` exit 0 over **15 tasks**. Its own numbers: 17 board rows and 15 directories reconciled to 16 entities with **0 unaccounted**, 11 `status.md` written, **0 directories the grammar failed to match**, 1 `UNDECLARED` resolved by the owner through a recorded `transition`, 158 payload tests passing | second consumer project | VERIFIED **as a measurement**, not as a verdict | [FIELD-REPORT](../../FIELD-REPORT__TFW-60__second_external_update.md), [second_consumer_manifest.md](second_consumer_manifest.md) |
| E64 | AC-15 items 1–4 · **the ruling's whole argument** | **An already-written `actor` is tolerated, never rewritten — measured on two real corpora, read-only, neither written to.** Under the code shipped at `2.0.0-dirty.2`, `innoforce-ai-first` fails on two events naming `claude-20260828a` and `claude-20260828b`, session profiles that were later deleted: **2 problems across 15 tasks, and unfixable from inside that project**, since events are immutable and profiles are not. Under `2.0.0-dirty.3`, same bytes: **15 tasks validate, exit 0.** `KZ-IT-telegram-list` green in both. **Files changed in either project: 0** | both consumer projects, read-only | VERIFIED | [ac15_actor_tolerated.txt](ac15_actor_tolerated.txt) — before/after transcripts, both commands quoted |
| E65 | AC-15, census · budget · return-to-coordinator | The R4 pass's census, taken **before the first edit** at `fd85b7c`. Re-derives every TS measurement independently — all five reproduce exactly — and states the count **both ways**: 22 modified by owner ruling S32, **38 distinct paths touched**, so the declared method is under the limit of 30 and path-counting crosses it. Raises the crossing and the appearing group (four workflows became eight) before acting rather than after | source repo | VERIFIED | [census_r4.md](census_r4.md) |
| E66 | AC-15 items 3, 6, 10, 11 · DoF | Every R4 gate, one command per claim: **0** journal events touched with 28 byte-identical to `HEAD`; **0** retired terms in the adapter layer; **0** unresolved paths across 212 references in three reference forms; **20** templates read back against the rewritten naming rule with **0** contradicting; suite, build and all three `--check` subjects. Also records the second finding this pass made against itself — eight workflows still instructing agents to write the removed field, twelve sites, measured in the census beforehand and skipped | source repo | VERIFIED | [r4_gates.txt](r4_gates.txt) |
| E67 | AC-13 half two — **ruled met by review revision 3** | Recorded as a ruling, not as a claim. The second external report was filed verbatim and independently re-measured by the reviewer: a real project updated by an operator who is not the author, 0 files hand-carried, 0 framework files edited inside `.tfw/`. **E51 below stays DEFERRED**: an RF or EV asserting its own external check passed is the DoF pattern the ONB was warned about, so the executor records that the ruling exists and does not grant it | reviewer, rev3 | VERIFIED **as a recorded ruling** | [REVIEW rev3](../REVIEW__phase-aa__portable_delivery__rev3.md) §4, [FIELD-REPORT](../../FIELD-REPORT__TFW-60__second_external_update.md) |


## Verdict

**Evidence verdict: 65/67 VERIFIED, 1 DEFERRED, 0 BLOCKED, 1 N/A**

> 2026-08-28, after the phase was approved: E63 added. AC-13 half two's closing artifact arrived from a second external project, and E51 stays DEFERRED on purpose — the executor records the measurement and does not rule on its own declared outcome.

> Revision 2: 60 items became 62. E61 and E62 cover the revision's own work; no earlier row
> changed status, and none was re-run — three were corrected to say what their evidence
> actually shows.
>
> **Revision 3, 2026-08-29: 63 became 67.** E64–E67 index the R4 corrective pass, whose three
> evidence artifacts existed on disk and were named by nothing — the second half of review
> revision 3's first item, alongside the missing RF. No earlier row changed status. **E51 stays
> DEFERRED although rev3 ruled AC-13 half two met**: E67 records that the ruling exists, and
> the executor does not convert a reviewer's ruling about its own work into its own VERIFIED.

- **DEFERRED — E51, AC-13 half two.** The specific blocker: acceptance evidence requires a
  real external project updated by an operator who is not the author of this code. The
  executor's clone closes half one and nothing more. This is the phase's declared outcome and
  it is reported **unmet**.
- **N/A — E53**, the `v2.0.0-dirty.2` tag, by the coordinator's Q3 ruling (b): a release act,
  cut after review.

## Attachments

| File | Description |
|------|-------------|
| [`census.md`](census.md) | The census, measured before the first edit, with the command behind each group |
| [`fixture_run.txt`](fixture_run.txt) | Full transcript of the external fixture update, both the failing first pass and the re-run |
| [`fixture_report.md`](fixture_report.md) | What the fixture run found, including two findings no test here could have produced |
| [`fixture_manifest.md`](fixture_manifest.md) | The migration accounting the fixture produced — the F4 corpus, correctly classified |
| [`fixture_index.md`](fixture_index.md) | The fixture's generated index: `Unresolved inputs — 2`, no `Backlog` section |
| [`ac1_gate.txt`](ac1_gate.txt) | AC-1's gate grep with every hit outside `tasks/` classified |
| [`ac5_validator.txt`](ac5_validator.txt) | Validator output before and after, for all five keys |
| [`ac3_parser_untouched.txt`](ac3_parser_untouched.txt) | The row parser's code diffed across the move: one line, the locator |

---

*EV — TFW-60 / Phase AA: Portable Delivery | revision 3, 2026-08-29 | phase measurements pinned at `1079020`, the R4 pass at `b75bef1`*
