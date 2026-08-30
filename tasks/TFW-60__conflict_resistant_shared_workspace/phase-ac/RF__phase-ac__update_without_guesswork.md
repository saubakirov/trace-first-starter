# RF — TFW-60 / Phase AC: Update Without Guesswork

> **Date**: 2026-08-30
> **Author**: Claude Code (Executor), `on_behalf_of: saubakirov`, `via: claude-code`
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-60](../HL-TFW-60__conflict_resistant_shared_workspace.md) at `56c3d70`, amendment A7 approved 2026-08-30
> **Phase HL**: [HL Phase AC](HL__phase-ac__update_without_guesswork.md)
> **TS**: [TS Phase AC](TS__phase-ac__update_without_guesswork.md) — revision 2 (after onboarding)
> **ONB**: [ONB Phase AC](ONB__phase-ac__update_without_guesswork.md) — two blocking questions, both ruled; nine recommendations, all ruled
> **Commits**: `d2e6bae` (ONB) · `4fe3b1d` (scripts and their tests) · `d047286` (workflow, canon, templates, adapters, release surface, integration tests) · this RF
> **Measured against**: `b9baec2` (TS approval). The working tree also carried other sessions' edits (`editions/`, `ASSISTED15`, TFW-55 research); none entered any commit of this phase.

---

## 1. What Was Done

Every place where the update path guessed or decided for the owner now either asks, derives, or refuses:

```text
BEFORE (v2.0.0-dirty.4)                           AFTER (this phase)

Step 0   source_head = HEAD                        Step −1  read the TARGET's update.md, follow it
         tag must equal HEAD → never on a          Step 0   operator names target_ref → source_head derived
         live source                                        from it → VERSION read from that commit = tag name
Step 3   "choose containers deliberately",         Step 3   🛑 three questions before the first durable write:
         handle from git user.name                          who acts · where tasks go · build.* — AG: one message
Step 5   cp -r payload → config overwritten        Step 5   copy loop with declared exclusions, prints "skipped:"
Step 6   7 rows, "managed CLAUDE.md content"       Step 6   Kind column: 5 copies (cmp) · 2 blocks (markers, §9 rule)
         allowlist: migration/changelog only                allowlist: text whose purpose is to retire the term
Step 7   {resolved-source}@{tag} → D:/… paths      Step 7   {upstream}@{verified-tag}; --check project reports a path
—                                                  Step 8a  briefing: Added·Changed·Fixed·Removed → four blocks
migrate  first [A-Z_]+ token → "DONE", no file     migrate  whole-or-UNDECLARED; own manifest heading; phases named
--check  "4 tasks validate" over 4 stateless       --check  failure on a live task; one informational line per
         phase dirs                                         terminal/stateless task
plan     ABBR = "UPD"                              plan     title first, then its initials, approved together
```

### New Files

| File | Description |
|------|------------|
| `.tfw/templates/briefing.md` | The update's last message: four blocks bound to `Added` / `Changed` / `Fixed` / `Removed`, absent section → *nothing in this release*, no free text (A7) |

### Modified Files — 26 counted, 6 copies (S32), measured `git diff b9baec2 d047286`: 943+ / 172− over the counted set

| File | Changes |
|------|---------|
| `.tfw/workflows/update.md` | Rewritten at **1174 words** (was 840; ceiling 1200): Step −1; Step 0 pin from `target_ref`; Step 3 🛑 gate with the three questions and the AG rule; Step 5 copy loop with exclusions and `skipped:`; Step 6 `Kind` column, §9 pointer, allowlist wording; Step 7 `{upstream}@{verified-tag}`; Step 8a briefing |
| `.tfw/scripts/migrate_board.py` | `classify_status()` whole-or-refuse: one declared token, no second declared token, no `So` symbol after it; `U+FE0F`/`U+200D` skipped; result gains `signals`. `render_manifest()`: *Rows carrying more than one lifecycle signal*, *Phase directories* (via `iter_phase_dirs`), *Task state written* note rewritten |
| `.tfw/scripts/gen_index.py` | `check_tasks()`: stateless phase directories — failure on a live task, informational line per terminal / stateless / malformed task, summary count, nothing written. `check_project()`: `installed_from` machine-local report, never rewritten |
| `.tfw/scripts/test_migrate_board.py` | +11 tests: `AILAB-2` exact shape, second emoji alone, second token alone, `→ + = <` non-signals, bare variation selector, refused row receives state, manifest headings, phase listing |
| `.tfw/scripts/test_gen_index.py` | +12 tests: stateless phase under live / terminal / stateless / malformed task, one line per task, nothing written, repository census (six tasks), `installed_from` reported ×3 and accepted ×4 |
| `docs/scripts/test_integration.py` | Block sync helpers and tests (region equality, outside untouched, no-markers → None); root `CLAUDE.md` block checked with installed copies; no `{version}` in templates; project-owned payload files derived and required in Step 5; TD-198 row in `RETIRED_WORDINGS`; staging `update.md` path exempted |
| `.tfw/conventions.md` | §4 Identifier: acronym of the approved title, proposed with it, *never derived silently* said both ways; §4 Artifact file naming: current-grammar rows, no title appended; §9: the one marker rule (three cases) |
| `.tfw/glossary.md` · `.tfw/workflows/plan.md` · `.tfw/workflows/init.md` · `.tfw/templates/HL.md` | The same abbreviation rule in each carrier's words; worked examples title → initials; HL header **Title** then **Abbreviation** |
| `.tfw/adapters/claude-code/CLAUDE.md.template` | `<!-- TFW:CLAUDE:START/END -->` around the `## TFW` section; block brought current (`status.md` in context loading, `/tfw-knowledge`, `/tfw-config`, `Version: see .tfw/VERSION`) |
| `CLAUDE.md` (root) | Carries the block byte-identical to the template's; Conduct and Execution Modes follow it as project text |
| `.tfw/adapters/claude-code/README.md` | *The managed block* section; setup step says what is outside the block is the project's |
| `.tfw/adapters/codex/README.md` | Step 3: no markers → report and leave, pointer to §9 (was: append) |
| `.tfw/adapters/antigravity/tfw-rules.md.template` · `.agent/rules/tfw.md` | Template = rendered rule, byte for byte; `{version}` gone (TD-204) |
| `.tfw/adapters/cursor/tfw.mdc.template` | `{version}` ×3 gone; a whole copy (R2) |
| `.tfw/CHANGELOG.md` | `.3` entry: dated addendum quoting the retired sentence verbatim and what a project that went thin does (TD-198); `.2` entry: dated closing line on the `TD-11` paragraph (TD-191); `2.0.0-dirty` entry: `> **Superseded by** .tfw/migrations/2.0.0.md` above the migration fence (TD-190). No entry rewritten in substance; `[Unreleased]` untouched |
| `RELEASE.md` | §5: three checklist items — reach every earlier tag and open with Step −1; quote reversed wording verbatim; superseded-by line, entries append-only. §6 step 3 names them |
| `.tfw/templates/journal/event.md` | `via` free-form non-empty provider/tool text at `:49`, `:70`; "provider family is not a writer" reworded (TD-200) |
| `.tfw/templates/team/profile.md` | One file per person; role and context in `team/README.md`; `since` defined; `type: agent` admitted and unusable (TD-203) |
| `.tfw/templates/status.md` | The phase sentence, when to use which, who writes a phase file (by hand, never migration) |
| `.tfw/templates/project_config.yaml` | `installed_from` comment: the one form, never a machine path, `self` for the framework; marker stays `← PROJECT` |
| `.tfw/migrations/2.0.0.md` | Step 1 opens with the target's `update.md`; every command from the root (`cd .tfw` rewritten); `--working-tree` sentence; one manifest location `tasks/MIGRATION-2.0.0.md`; the two manifest sections to read; step 3a phase state by hand; multi-signal rows under `UNDECLARED`; three grammars unchanged |
| `.claude/commands/tfw-{update,plan,init}.md` · `.agent/workflows/tfw-{update,plan,init}.md` | Re-synced byte-identical in the same commit as their source (copies, not counted) |

### What a project on `2.0.0-dirty.2`, `.3` or `.4` must know (AC-11, for the `.5` entry and the briefing)

`/tfw-release` writes the entry; this is its updating section's required content, verified as a `.2` reader's
path in [`skipped_tag_read_through.txt`](evidence/skipped_tag_read_through.txt):

0. Read the **target's** `.tfw/workflows/update.md` from the pinned payload and follow it (Step −1); pin from the tag you name, never from the source's `HEAD`.
1. On `.2`: also perform the `.3` section — re-sync `.claude/commands/tfw-*.md`, add `tfw.installed_from`, delete per-session agent profiles; read the `.3` entry's addendum on the retired sentence *"Commands never duplicate workflow content — they reference it"* and `grep` your own rule files for it.
2. On `.2` or `.3`: also perform the `.4` section — remove `tfw.id_max_retries` and `review.default_mode`; rename nothing.
3. Answer the three questions the update asks before its first write: who acts, where tasks go, `build.*`.
4. `installed_from` is `{upstream}@{verified-tag}`; `--check project` reports a machine path — record the upstream reference. All three local consumers carry a `D:/` path today and will be told so.
5. `CLAUDE.md`: insert the `<!-- TFW:CLAUDE:START/END -->` block once, from the template; until then Step 6 reports the file and leaves it.
6. `--check tasks` names a phase directory without `status.md`; under a live task that is a failure — author the file from the template's phase paragraph.
7. The abbreviation of a new task is the initials of its approved title, proposed and approved with it.
8. Read the briefing the update delivers last — four blocks, in your `content_language`.

The briefing for this repository's own `.3 → .5` delta is rendered in [`briefing_dirty3_to_dirty5.md`](evidence/briefing_dirty3_to_dirty5.md); its `.5` bullets are re-derived from the cut entry.

## 2. Key Decisions

1. **A second status signal is a character of Unicode category `So`, not any category S** — the ONB's blocking question, ruled by the coordinator on the measurement: over 114 rows on four pinned corpora, category S entire refused three single-signal rows on a plus sign or an arrow (`TFW-52`, `HD-30`, live `HD-31`); `So` refuses exactly the eight rows carrying a second emoji or a second declared token. `U+FE0F` and `U+200D` are skipped explicitly. A declared token in outcome prose *is* a signal (`HD-19` `✅ DONE (KNW deferred …)`): the conservative direction, ruled and kept.
2. **The old classifier stripped every symbol from the cell before matching; the new one keeps prose punctuation in the outcome.** Three already-migrated rows would read `+1 UX` and `→ TD-126` instead of `1 UX` and `TD-126` if re-migrated; existing state files are not rewritten (immutable by rule), so nothing changes for them. Recorded so the reviewer does not read the three text-only differences as classification drift.
3. **`classify_status()` returns a `signals` list** — empty for a clean cell — and the manifest prints it. A refusal that names what it saw is what lets a person resolve the row with one `transition` event instead of re-reading the board.
4. **AC-7: the exclusion list carries both project-owned files; the payload keeps carrying them** (ONB rec. 1, accepted). A root `.gitattributes export-ignore` would govern `git archive` alone and add a root file outside the census; the loop in Step 5 covers every materialization and the payload test derives the excluded set from the payload itself (every root `.yaml` with a template counterpart), so a new project-owned file fails the test until it is excluded. The root cause — the payload carries this repository's own `project_config.yaml` and `knowledge_state.yaml`, which conventions §10.3 says are never sourced from upstream — is §6 O11 for the payload boundary.
5. **Step 5's copy is an executable `find | while read` loop in POSIX sh**, not `rsync` or `cp --parents`: it runs in Git Bash on Windows, where three consumers were updated, and it prints `skipped:` for each exclusion. A copy printing nothing skipped on a project that has both files is declared a failed step.
6. **The `TFW:CLAUDE` block bounds the `## TFW` section** — context loading, commands, key references — and was brought current before being bounded (coordinator's widening of rec. 2): `status.md` in the context-loading order, `/tfw-knowledge` and `/tfw-config` in the table, `Version: see .tfw/VERSION`. Project identity, mandatory rules, execution mode and code standards stay outside. Root `CLAUDE.md` was reordered so the block is contiguous; its Conduct and Execution Modes text is unchanged and follows the block.
7. **One marker rule, in conventions §9, for every block row: markers present → replace between them; file absent → create from the template; no markers → report and leave.** The Codex README's *append the complete block* became the pointer. Appending to a file that already carries an unmarked hand-written TFW section would produce two sections — the fourth report's `CLAUDE.md`.
8. **Cursor admitted to the census (Q2, ruled A)**: `{version}` ×3 removed, the template is a whole copy, the Step 6 table has no footnote.
9. **`--check tasks`: a stateless phase directory is a failure only when the task's own `status.md` is live**; terminal, absent or malformed task state makes it an informational line that says which — one line per task, a summary count, exit code unaffected (R2). On this repository: six lines, 17 directories, exit 0.
10. **`--check project` on `installed_from`: a drive letter, a leading `/` or a backslash is machine-local and a problem (exit 1); `self`, `unrecorded` and a URL pass; nothing is rewritten.** The three local consumers will be told at their next update — the intended effect.
11. **The briefing reads four sections (A7) and nothing else**: `Why this release exists`, `Verification`, `Known open`, `Canon` explain the release to its authors. An absent section yields *nothing in this release*; a bullet with no CHANGELOG bullet behind it is forbidden by the template. The positive framing the owner asked for is the block order, not adjectives.
12. **TD-198 is now a registry row**: *"Commands never duplicate workflow content"* in `RETIRED_WORDINGS`, scanned over the installed adapter surface — where the fourth report found the stale principle. The CHANGELOG quotes it (excluded from the scan by rule) and `.tfw/adapters/claude-code/README.md` keeps its blockquote (outside both scans).
13. **Word ceiling met by removing duplication first**: Step 3's `team/` paragraph folded into the gate; Step 5's two-line recheck became one line against the derived commit; Step 8's list stopped repeating Step 6; Step −1 kept to three lines. 1174 of 1200.
14. **Evidence at pins, never `HEAD`**: the fabricated tag and the dry-run payload live in a scratch clone; the four corpora were read with `git show {pin}:tasks/BOARD-SNAPSHOT.md`; the consumers were read with `grep`, `git show` and `sha256sum` only.
15. **`[Unreleased]` is untouched.** The `.5` entry is `/tfw-release`'s act after review (AC-11); its required updating section is §1 above. Additions to `.2`, `.3` and the `2.0.0-dirty` entry are appended and dated.
16. **`templates/project_config.yaml` keeps `← PROJECT` on `installed_from`** (ONB inc. 6, accepted): the key is framework-shipped, the value is project-written by each update; the marker names who writes the value.

## 3. Acceptance Criteria

### AC-1 — the pin is derived from the tag
- [x] `target_ref` named by the operator; `source_head=$(git rev-parse --verify "$target_ref^{commit}")`, never `HEAD` — `update.md` Step 0
- [x] `VERSION` read from that commit and compared with the tag's name; a mismatch stops — Step 0; `pin_on_live_source.txt` Run 2
- [x] Step 5 recheck against the derived commit: a source that moved elsewhere is not reported; a moved tag is — `pin_on_live_source.txt` last section
- [x] `status --porcelain -- .tfw/` rule as written
- Gate: on a clone 29 commits ahead of `v2.0.0-dirty.4`, PASS; fabricated tag, STOP — both runs verbatim in the gates file

### AC-2 — a receiver on any earlier tag finds its path
- [x] Updating section names every intervening section; RELEASE.md §6 makes it a step — §5/§6, `skipped_tag_read_through.txt`
- [x] RELEASE.md §5: reversed statement quoted verbatim; `.3` entry gains the quote and what a project that went thin does (TD-198)
- [x] `.2` entry's `TD-11` paragraph closed, dated (TD-191)
- [x] `2.0.0-dirty` migration fence carries `> **Superseded by**`; RELEASE.md names the form (TD-190)
- [x] `update.md` opens with Step −1; the guide's step 1 repeats it first; **R2** the `.5` updating section opens with it (§1 above)
- [x] No entry rewritten in substance; additions appended, dated
- Gate: the `.2` reader's path recorded step by step

### AC-3 — the gate can be literally green
- [x] Allowlist admits *text whose purpose is to retire the term*, one sentence — Step 6
- [x] The six known hits fall inside; a live use is not admitted — `gates_and_word_count.txt`: 0 outside here, 0 outside on `innoforce-ai-first`

### AC-4 — every Step 6 row is executable the same way
- [x] `TFW:CLAUDE` markers in the template, Codex pattern
- [x] Step 6 table states copy / block per row; Claude rules and Codex routing are blocks, five rows copies
- [x] **R2** one marker rule in conventions §9, three cases; Step 6 and both READMEs point to it; Codex `:104` is the pointer
- [x] **R2** the block brought current with the canon
- [x] **R2** root `CLAUDE.md` carries the block byte-identical; the installed-copies test checks it
- [x] **R2** Cursor template: `{version}` ×3 gone, a whole copy
- [x] Antigravity template reads `.tfw/VERSION` as the rendered rule does; identical (TD-204)
- [x] Claude adapter README describes the block and the first-run rule
- Gate: fixture `CLAUDE.md` with text above and below — region equals the template's after sync, outside bytes unchanged (`cmp` both)

### AC-5 — `installed_from` has one form
- [x] `{upstream}@{verified-tag}` in Step 7 and the config template; local checkout named symbolically, path in the checklist
- [x] `--check project` reports drive letter / leading `/` / backslash as machine-local; nothing rewritten
- [x] `self` valid — this repository's `--check project` is consistent
- Gate: `D:/…@v2.0.0-dirty.4` → 1 problem; `steps-framework@v2.0.0-dirty.4` → consistent

### AC-6 — the owner is asked, not guessed
- [x] Step 3 🛑 gate before the first durable write, exactly three questions; handle asked, never inferred; AG: one message, read-only steps continue, stop at the write
- [x] Answers recorded in the checklist
- [x] Step 8a briefing from `templates/briefing.md`; **R2** absent section → *nothing in this release*; **A7** `Changed` as a fourth block
- [x] The briefing is the last message; the checklist records delivery
- [x] `update.md` under 1200 words: **1174**
- Gate: AG dry run against a fixture consumer stops with the three questions, fingerprint identical before/after, `git user.name` present and unused; the `.3 → .5` briefing rendered

### AC-7 — the copy cannot overwrite project-owned files
- [x] Step 5 names the exclusions; config merged key by key; state never touched
- [x] The copy prints what it skipped; nothing-skipped on a project with both files is a failed step
- [x] Executor decision recorded: exclusion list, payload keeps both (§2 item 4); **R2** root cause in §6 O11
- [x] Payload test covers the exclusion list: the project-owned set is derived from the payload and required in Step 5
- Gate: fixture — both files byte-identical, both printed as skipped

### AC-8 — the status cell parsed whole or refused; no phase left without a named state
- [x] One declared token + free text with no further declared token and no further status symbol; **R2** a symbol is category `So`; `U+FE0F`/`U+200D` skipped; fixture tests each signal alone, `→` and `+` as non-signals, a bare variation selector
- [x] An `UNDECLARED` row is never terminal, never skipped by `plan()`; receives `status.md` at `UNDECLARED`
- [x] Manifest heading *Rows carrying more than one lifecycle signal*; the *Task state written* note no longer implies skipped rows are terminal
- [x] Manifest names every `phase-*` directory of every matched task and says phase state is not written by migration; author by hand
- [x] `--check tasks` reports stateless phase directories: failure on a live task, informational otherwise; **R2** one line per task, malformed task state → informational with the reason; on this repository six lines over 17 directories, exit 0; writes nothing
- [x] `templates/status.md` carries the phase sentence and says when to use which
- [x] The migration guide says all of it in the order met
- [x] The `AILAB-2` shape is a committed fixture: 22 of 28 new tests fail before, 28 pass after
- Gate: fixture; `--check tasks` on a fixture and on this repository; four pinned corpora — 8 class changes, all multi-signal; 3 text-only differences (`+`/`→` kept); 103 identical

### AC-9 — the abbreviation is the initials of the approved title
- [x] Conventions §4 Identifier: acronym of the approved full title, proposed **together with the title**, approved with it; *never derived silently* said both ways (never apart from a title, never without approval)
- [x] `plan.md` 3.5 and 4.2, `init.md` Batch 1 and Mini-Setup 6, glossary: the same rule, worked examples title → initials (`CRSW`, `ASSISTED15`)
- [x] HL template header: **Title** then **Abbreviation**, adjacent
- [x] Artifact file naming: current-grammar rows with `HL-TFW_20260829-172110_ABT.md`, `RES__TFW_20260829-172110_ABT.md`; no title appended, the reason stated (TD-201)
- Gate: five excerpts side by side in `carriers.txt`; `gen_docs.py`'s `task_id_source` resolves both examples

### AC-10 — carriers agree with the canon and each other
- [x] `event.md` `:49`, `:70`: `via` free-form non-empty text (TD-200)
- [x] `profile.md`: one file per person; role and context in `team/README.md`; no fifth key (TD-203)
- [x] Guide: one manifest location (`tasks/MIGRATION-2.0.0.md`, beside the snapshot); the `--working-tree` sentence; `cd .tfw && …` rewritten from the root
- [x] `grep` for the four retired wordings over the templates and the guide: nothing
- Gate: the grep; the guide's retired-files command run from the root as written

### AC-11 — the release describes what shipped
- [x] **executor:** what a project on `.2`, `.3`, `.4` must know — §1 above
- [x] **executor:** every fifth-report §6 item and fourth-report defect 7 — fixed here or in §6:
  - manifest location → **fixed** (guide names `tasks/MIGRATION-2.0.0.md`, beside the snapshot)
  - role location → **fixed** (profile template: `team/README.md`)
  - `since` semantics → **fixed** (profile template: the date the participant joined the project — one line)
  - README route template → §6 O2 · stale index in a non-first container → §6 O3 · `created` seconds provenance → §6 O4 · `--check project` green before migration → §6 O5 · fourth-report defect 7 → §6 O6
- [ ] **`/tfw-release`, after review:** version bump, CHANGELOG entry and tag as one act; the entry's updating section per §1 — *not the executor's act*
- [ ] **field:** one consumer on the line updates to the new tag from Step −1 — *after the tag exists*
- [x] `2.0.0` not claimed: `VERSION` reads `2.0.0-dirty.4`

## 4. Verification

- Lint (`python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only`): collects — every test file imports
- Tests (`python -m pytest .tfw/scripts/ docs/scripts/ -q`): **315 passed, 1 skipped** (baseline at `b9baec2`: 283 passed, 1 skipped; +32 tests, no test removed or weakened)
- Verify (`python .tfw/scripts/gen_index.py --check tasks`): **54 tasks validate**, 6 informational lines over 17 stateless phase directories, exit 0
- `--check project`: consistent with the release it declares
- `--check index`: **stale** — `workspace/00-INDEX.md` lags this phase's `status.md` and other sessions' task changes; a derived view with one writer, left for the coordinator to rebuild deliberately (§6 O12)
- Adapter copies: `update.md`, `plan.md`, `init.md` byte-identical in `.claude/commands/` and `.agent/workflows/`; `.agent/rules/tfw.md` identical to its template; root `CLAUDE.md` block identical to the template's
- Word count: `update.md` 1174

## 5. Evidence

> **Cognitive mode:** Observational verification — evidence lives in the EV file, not inline.

See [EV file](evidence/EV__phase-ac__update_without_guesswork.md) for evidence details — 37 rows, eight artifacts indexed.

Evidence verdict: **34/37 VERIFIED, 3 DEFERRED, 0 BLOCKED, 0 N/A** — the deferred three are the `.5` entry, the tag and the consumer run, assigned by the TS to `/tfw-release` and the field.

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| O1 | `tasks/TFW-55__canonization_program/` | — | ux | The board snapshot reads `DONE`; the working tree carries live research (`research/iter2/` uncommitted, `iterations.yaml` modified) and no `status.md` at task or phase level. Its two stateless phases are *informational* by the rule — correct, but the rule's premise (a terminal task is history) is not true here. Seen by the coordinator; the owner authors the state |
| O2 | `README.md` route section (every consumer) | — | duplication | Fifth report §6: *add a permanent route* has no template, so each project writes its own paragraph and rewrites it in three places on a container change. A `templates/readme_route.md` with `{container}` is a new payload path — outside this census |
| O3 | `.tfw/scripts/gen_index.py` `build()` | ~1140 | ux | Fifth report §6: after the first container changes, the old `{old}/00-INDEX.md` stays on disk as a stale copy and nothing names it. A line *stale index at {old}: delete it* when `00-INDEX.md` is seen in a non-first container. Phase B touches `gen_index` |
| O4 | `.tfw/scripts/migrate_board.py` `build_status()` | ~520 | ux | Fifth report §6: `created` is taken from the directory's first commit (second-accurate) while the board carried a day; the provenance comment does not say where the seconds came from, and the status template promises a declared zero time for day-only sources. One sentence in the comment |
| O5 | `.tfw/scripts/gen_index.py` `check_project()` | ~1290 | ux | Fifth report §6: with the board still in the README and no `status.md` yet, `--check project` answers *consistent*. One line — *board still present at {path}: migration pending* — when a `## Task Board` heading is found in the root README |
| O6 | `.tfw/scripts/gen_index.py` `check_project()` | ~1250 | missing-test | Fourth report defect 7: `--check project` reads `team/` whole but not who references it; a deleted human profile leaves `on_behalf_of` dangling and only `--check tasks` goes red. Filed in the TS as an observation; `--check tasks` already catches it |
| O7 | `team/README.md` (this repository) | 3–4 | style | Says *humans and agents alike — that is why this container is not called `people/`* — the contradiction TD-203 removed from the template stands in the project's own README, which the template now names as where a role goes. Project text, outside the census |
| O8 | `docs/scripts/gen_docs.py` | 766 | style | Imports `mkdocs_gen_files` at module load, so the module cannot be imported outside a docs build (`mkdocs.yml` must exist) — an executor checking `resolve_references()` from the repository root gets a `ConfigurationError`. Guarding the import behind the build entry point would let the resolver be unit-checked |
| O9 | consumers' migrated `status.md` (`HD-30`, `HD-31`, `TFW-52`) | `outcome` | naming | The old classifier stripped every symbol before matching, so three already-written outcomes read `1 UX TD-271`, `fieldworker role  directed assignment`, `blocked TD-126`. Immutable by rule; a person may correct with a `transition` event if the text matters |
| O10 | `.tfw/adapters/codex/README.md` | 96–110 | style | Step 3 still says *if root `AGENTS.md` is absent, create it with project guidance plus the block* — consistent with §9 case 2; not changed. Noted because the Claude README now says the same in different words; a future pass may make the two paragraphs one pointer each |
| O11 | payload boundary (`.tfw/project_config.yaml`, `.tfw/knowledge_state.yaml`) | — | security | **Root cause behind AC-7, recorded on the coordinator's ruling:** the payload carries this repository's own two state files, which conventions §10.3 says are never sourced from upstream. The exclusion list makes the copy obey the rule; the payload still ships them. A Phase AA-surface question for a later ruling — `.gitattributes export-ignore`, or a payload that is `.tfw/` minus two files |
| O12 | `workspace/00-INDEX.md` | — | ux | Stale after this phase's transitions and other sessions' task work. Derived and non-blocking by design; the coordinator rebuilds it deliberately with `python .tfw/scripts/gen_index.py` — one writer, not the executor mid-phase |

## 7. Fact Candidates

> fact-candidates: processed 2026-08-30

> Human-sourced only; the coordinator's rulings and the owner's words are the source.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | stakeholder | The owner wants change presented positively and in this order — what is now possible, what changes in how you work, what was repaired, what you no longer have to do — "because people do not like change"; the structure is the framing, not adjectives | fifth field report, owner quote; HL §12 A7 | High |
| 2 | philosophy | *The framework is its own first consumer or the mechanism is untested where it lives*: a rule this repository does not obey is advice. Applied: root `CLAUDE.md` carries the marker block and a test checks it like every installed copy | ONB §8, coordinator ruling on rec. 3 | High |
| 3 | convention | Boards carry status markers beyond the declared glyph set — `🔄` for a live phase, `🟢` in outcome prose — so *declared glyphs only* is the wrong rule for a second signal; Unicode `So` is what a person reads as a marker, and `Sm` (`+ → =`) is prose | ONB §8, coordinator ruling on Q1, on the executor's four-corpus measurement | High |
| 4 | process | Two adapters with two first-run rules is the drift class this phase closes elsewhere; fixing one and filing the other "would be the scar tissue TFW-57 measures" — a rule is stated once and pointed to, never restated per adapter | ONB §8, coordinator ruling on inc. 1 | Medium |
| 5 | process | The coordinator does not read around frozen text even when the reading is obviously right: the briefing's `Changed` input went through §12 as A7 and was approved the same day rather than being assumed | ONB §8, risk 5; HL §12 A7 | High |

## 8. Strategic Insights (Execution)

> fact-candidates: processed 2026-08-30

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | **Mechanizing a copy of stale content makes the mechanism precise about the wrong text.** The coordinator widened the marker deliverable with an obligation: bring the block current with the canon (context loading order, command table) *before* bounding it. Implication: every future "make this sync mechanical" deliverable carries a content audit of the thing being synced as its first step, or the sync will faithfully propagate a contradiction to every consumer | philosophy | Coordinator, ONB §8 ruling on rec. 2 |
| S2 | **The least structured CHANGELOG section carries the most consequential news.** Reversals (`Copies are the model`) and grammar changes live under `Changed`; a briefing built only from `Added` / `Fixed` / `Removed` would have printed *nothing in this release* over the two largest changes of the line. Implication for `RELEASE.md`: a reversal belongs under `Changed` with the retired wording quoted, and the briefing block *what you now do differently* is the reader's contract that the section will be read to them | process | Coordinator, A7 evidence column; owner approval 2026-08-30 |
| S3 | **A refusal earns trust only when the operator agrees the refused thing was ambiguous.** The owner-side test of the status rule was not "does it catch `AILAB-2`" but "does it refuse `A+B`": a gate that refuses plainly single-signal rows teaches operators to override refusals, and then the real refusal is overridden too. Implication: every whole-or-refuse rule this framework adds is measured on real corpora for false refusals before it is fixed in a fixture — the order this phase followed | philosophy | Coordinator, ONB §8 ruling on Q1 |

## 9. Diagrams

The status cell, whole or refused — one rule, applied after the identifier's:

```text
cell ──► strip leading marker run (any S, U+FE0F, U+200D, spaces)
     ──► first [A-Z_]+ token
            │ not declared ──────────────────────────────► UNDECLARED, verbatim, signals=[]
            │ declared
            ▼
        trailing text (U+FE0F/U+200D removed)
            │ any [A-Z_]+ word ∈ declared ─┐
            │ any char with category So ───┴► UNDECLARED, verbatim, signals=[what was seen]
            │ neither                                       (manifest: "Rows carrying more than one lifecycle signal")
            ▼
        lifecycle = token · outcome = trailing, dashes trimmed
        Sm/Sc/Sk (+ → = < $) and prose pass through untouched
```

`--check tasks`, the phase-directory decision:

```text
for each task dir ── for each phase-* without status.md
     task status.md ── absent ───────────► note (informational): "carries no status.md of its own"
                    ── malformed ────────► note (informational): "malformed, reported above"   (the malformed state is the failure)
                    ── lifecycle ∈ {DONE, REJECTED} ► note (informational): "the task is DONE"
                    ── live ─────────────► FAILURE: "{task}: N phase directories carry no status.md while the task is {lifecycle}: …"
one informational line per task · summary count · exit code from failures only · nothing written
```

The update, where it stops and what it derives:

```text
operator ──target_ref──► Step 0: source_head = rev-parse target_ref^{commit}; VERSION(source_head) == tag name? ── no ──► STOP
                              │ yes: archive source_head → .tfw/.upstream (staging)
                              ▼
                         Step −1: follow .tfw/.upstream/.tfw/workflows/update.md
                              ▼
                         Steps 1–2 (read-only) ──► Step 3 🛑 who · where · build.*  ── unanswered ──► STOP before the first durable write
                              │ answered → checklist
                              ▼
                         Step 5 copy: every payload file except project_config.yaml, knowledge_state.yaml → "skipped: …" ×2
                         Step 6 copies (cmp) · blocks (region between markers; no markers → report, leave)
                         Step 7 installed_from = {upstream}@{verified-tag}
                         Step 8 --check project ──► Step 8a briefing (Added·Changed·Fixed·Removed) = last message
```

---

*RF — TFW-60 / Phase AC: Update Without Guesswork | 2026-08-30*
