# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42 (`tfw.review.min_verify_ratio`)
> RF files claimed: 23 implementation paths + 8 work artifacts = 31
> Files to verify: ⌈31 × 0.42⌉ = 14 — **escalated to 31 (100%)** on discrepancy D1
> Method: `git diff 57a5147 ecfceee -- <path>` for every implementation file; every evidence file read in full; commands re-run in this session on the working tree at `ecfceee` (unrelated TFW-55 research files dirty, untouched)

## Verification Log

### V1: `.tfw/scripts/gen_index.py`
- **RF claim:** current grammar, whole-input dispatch, directory collision refusal, truthful malformed reporting, ReaderError key recovery, free-form `via` validation, retired-key checks
- **Actual:** `CURRENT_ID` added, `fullmatch`-ed first in `parse_identifier()`; `TASK_DIR` removed; `IdentifierCollisionError` raised from `_walk_containers()` naming identifier and both paths; `explain_yaml_error()` recovers the key from `exc.position` when no mark; `validate_event()` rejects empty/non-string `via`; `id_max_retries` and `review.default_mode` added to retired keys; unresolved reason now says "reported as malformed", no longer "rename it by hand"
- **Match:** ✅

### V2: `.tfw/scripts/migrate_board.py`
- **RF claim:** shared whole parsing replaces prefix extraction; duplicate refusal; exact partitions; computed pre-write guarantees; faithful prose; manifest disclosure
- **Actual:** `re.search(r"[A-Z][A-Z0-9]*-\d+")` gone; `_identifier_text()` unwraps link label / emphasis / strike then `parse_identifier()`; `reconcile()` raises `MigrationRefusal` on duplicate rows naming both lines; `computed_guarantees()` returns three partition equalities with arithmetic and missing/duplicate detail; `require_guarantees()` called in `plan()` and first thing in `render_manifest()`; `_plain()` strips `_` only at word boundaries; manifest has `## Malformed identifiers`, `## Guarantees checked` (arithmetic + HELD) and `## Guarantees not checked by this run`; `written` derives identifiers through the dispatcher instead of `split("__")[0]`; `main()` catches both refusals and prints `REFUSING … Nothing was changed`, exit 1
- **Match:** ⚠️ partial — see **D1**: line 750 prints `**Unaccounted: 0.**` as a string constant

### V3: `.tfw/scripts/test_gen_index.py` · V4: `.tfw/scripts/test_migrate_board.py`
- **RF claim:** current/dirty/legacy, malformed, collision, guarantee, prose, `via`, ReaderError and retired-key regressions incl. committed HELPDESK_SHAPE
- **Actual:** all present. HELPDESK_SHAPE carries exactly the five candidates the TS gate names. Duplicate-row test asserts manifest **not** created and both line numbers named. Unbalanced test removes `TFW-9` and asserts the guarantee name and identifier in the refusal
- **Match:** ✅ — with one note feeding D1: `test_migrate_board.py`:237 and :508 assert the literal `"Unaccounted: 0"`

### V5: `.tfw/conventions.md` · V6: `.tfw/glossary.md` · V7: `.tfw/project_config.yaml`
- **RF claim:** `PREFIX_stamp_ABBR` issued, both historical forms preserved, collision refusal defined, `via` free-form
- **Actual:** §4 Identifier rewritten as claimed; `id_max_retries` removed from config; `via` row and a new paragraph declare descriptive provenance. Glossary *Task Naming* names all three forms
- **Match:** ✅. Note for judge row 9: the §4 *Artifact file naming* table (`HL-{ID}.md` …) was not extended with a current-grammar example, and its prose addresses only clock and legacy tasks

### V8: `.tfw/workflows/plan.md` · V9: `.tfw/workflows/init.md`
- **RF claim:** owner approves ABBR before creation, one clock read, exact-path refusal, session naming with full ID
- **Actual:** plan.md Step 3.5 asks for the abbreviation in the batched exchange; Step 4.2 pseudocode reads clock once, `if dir exists: STOP; ask the owner to approve a different abbreviation`; retry loop and `id_max_retries` gone; init.md interview batch 1 asks for the abbreviation and step 6 creates `{PREFIX}_{stamp}_{ABBR}` with the same refusal
- **Match:** ✅

### V10: `.tfw/workflows/update.md`
- **RF claim:** 852 words; source/tag pins and recheck; installed-baseline provenance; reachable retired-term check; installed-adapter-only sync
- **Actual:** `wc -w` = 852. "Before Step 0" pins `source_head`, verifies `refs/tags/v${target}^{commit}` equals it; Step 5 rechecks both; Step 3 compares against `installed_from`; Step 6 requires zero hits **outside an allowlist**; Step 6 creates no target directory for uninstalled adapters
- **Match:** ⚠️ partial — see **D2**: Step 0 and Step 9 state that `.tfw/.upstream-source/` is gitignored; `.gitignore` lists only `.tfw/.upstream/`

### V11: `.tfw/migrations/2.0.0.md`
- **RF claim:** three grammars named, staging claim removed, malformed inputs non-actionable, split test commands
- **Actual:** all four present; "Commit whatever board changes are in flight … adding files to the Git index changes nothing the migration can see"; `-k "not repository"` before step 2, `-k repository` after the index exists
- **Match:** ✅

### V12: `.tfw/templates/project_config.yaml` · V13: `.tfw/templates/HL.md` · V14: `.tfw/templates/status.md`
- **RF claim:** issuance examples updated, HL abbreviation field, scope budgets marked project-owned
- **Actual:** `id_format: "{PREFIX}_{YYYYMMDD}-{HHMMSS}_{ABBR}"`, `scope_budgets: ← PROJECT`; HL header gains `> **Abbreviation**: {ABBR}`; status template `id: PREFIX_YYYYMMDD-HHMMSS_ABBR`, `authority: HL-PREFIX_YYYYMMDD-HHMMSS_ABBR.md`
- **Match:** ✅

### V15: `.tfw/compilable_contract.md` · V16: `docs/scripts/gen_docs.py` · V17: `docs/scripts/test_gen_docs.py`
- **RF claim:** references across all three grammars, underscore-safe boundaries, exact normalized directory matching
- **Actual:** `task_id_source` alternation of the three forms; `\b` replaced by `(?<![A-Za-z0-9_])` … `(?![A-Za-z0-9_/\]])`; `_task_glob()` matches directories through `gen_index.parse_identifier()` equality instead of a `{task_id}*` glob; three new tests incl. boundary rejection of `X{id}`, `{id}_TAIL`, `_BAD_ABBR`, `_lower`
- **Match:** ✅

### V18–V23: `.claude/commands/tfw-{plan,update,init}.md` · `.agent/workflows/tfw-{plan,update,init}.md`
- **RF claim:** six approved byte-identical copies
- **Actual:** `sha1sum` — each triplet identical (`35a116a2…`, `ad0be818…`, `b8f06a7f…`). All 11 `.agents/skills/tfw-*/SKILL.md` hash-equal to `.tfw/adapters/codex/skills/`
- **Match:** ✅

### V24: `phase-ab/status.md` · V25: `phase-ab/journal/20260829-165540__transition__d26e.md`
- **RF claim:** RF lifecycle and completion timestamp recorded; durable transition into execution
- **Actual:** `lifecycle: RF`, `updated: 20260829-173155`; event carries `on_behalf_of: saubakirov`, `via: codex`, two refs, summary within ceiling
- **Match:** ✅ — note: no event records execution → RF (the `updated` stamp at 17:31 has no journal entry). Low; carried to judge row 4

### V26–V31: `RF`, `EV`, five evidence `.txt`
- Read in full; contents checked under Evidence Verification below.

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest .tfw/scripts/ docs/scripts/ -q -k "not repository"` | **281 passed, 3 deselected** (179 s) — matches RF |
| 2 | `python -m pytest .tfw/scripts/ docs/scripts/ -q -k repository` | **2 passed, 1 skipped, 281 deselected** — matches RF; 281 + 2 = 283 passed, 1 skipped = RF full-suite figure |
| 3 | `python .tfw/scripts/gen_index.py --check tasks` | 53 tasks validate; exit 0 |
| 4 | `python .tfw/scripts/gen_index.py --check project` | consistent with `2.0.0-dirty.3`; names what it did not check; exit 0 |
| 5 | `wc -w .tfw/workflows/update.md` | 852 |
| 6 | `sha1sum` on 3 workflow triplets; hash compare of 11 Codex skill pairs | all identical |
| 7 | `git diff --numstat 57a5147 ecfceee` excluding copies and work artifacts | 17 files, +712 −317 = **1029** — matches RF |
| 8 | Inline Python: `parse_board(HELPDESK_SHAPE)`, `_plain(...)`, `parse_identifier(...)` | `HD-30 legacy · HD-30b malformed · TFW-01_single_underscore malformed · 20260829-010832__dirty clock · TFW_20260829-010832_ABT current`; `_plain` keeps `normalize_text()` and `working_days`, removes `_emph_`, `**b**`, `~~s~~` — reproduces `parser_and_prose_before_after.txt` |
| 9 | `git log --format="%h %s" \| grep -E '^\S+ \[[^]]*/TFW-60/freeze/'` | five freeze commits; latest `810b1b8` = TS header baseline |
| 10 | `cat .gitignore` | contains `.tfw/.upstream/`; does **not** contain `.tfw/.upstream-source/` → D2 |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | "The collapse is the unanchored `re.search()` in `migrate_board.parse_board()`, before `LEGACY_ID` is consulted" | RF §2.1, ONB §1, TS AC-1 R2 | `git show 57a5147:.tfw/scripts/migrate_board.py` line 130: `identifier = re.search(r"[A-Z][A-Z0-9]*-\d+", cells[0])` — confirmed; `LEGACY_ID` is anchored `^…$` and never saw the cell | ✅ |
| C2 | "Every identifier parsed before Phase AB still parses to the same kind and normalized identifier at four pinned commits" — 53 / 2 / 15 / 30 | `four_corpora_compatibility.txt` | The framework count is checkable here: `--check tasks` reports **53 tasks** on this tree; the 53 listed identifiers are TFW-1…TFW-61 minus gaps, consistent with `tasks/`. The three external pins (`97dd429`, `58329e7`, `aec5f2d`) are at paths outside this repository and were not re-opened in this review; the method (pre-change regexes reimplemented inline vs. new dispatcher over `git ls-tree`) is stated and sound | ✅ for this corpus; external corpora accepted on stated method |
| C3 | "283 passed, 1 skipped" / "281 + 3 deselected" / "2 passed, 1 skipped" | RF §4 | Commands 1–2 | ✅ |
| C4 | "Scope: 23 physical, 17 counted, 0 new, 1029 counted-line churn" | RF §4, `verification_gates.txt` | Command 7 and `git show --stat ecfceee` (23 non-artifact paths) | ✅ |
| C5 | "TD-197's implementation decision is closed in this RF" | RF §2.5, §3 AC-7 | `conventions.md` §4 `via` row + paragraph; `validate_event()` non-empty check; tests. But `.tfw/templates/journal/event.md`:49 and :70 still define `via` as "provider family: claude, codex, gemini" — RF O4 admits this | ⚠️ closed at the TS gate (canon + validator); one definition site still disagrees |
| C6 | "All seven third-report §7 items are fixed or filed" | RF §3 AC-8, `verification_gates.txt` | Field report §7 lists exactly seven bullets: ReaderError key · profile.md contradiction · `scope_budgets` marker · `review.default_mode` · antigravity `{version}` · "commit, or at least stage" · unused adapters copied. Dispositions: 1 FIXED (test at `test_gen_index.py` ReaderError), 2 FILED (O2), 3 FIXED (template `← PROJECT`), 4 FIXED (`check_project` nested key), 5 FILED (O3), 6 FIXED (guide), 7 FIXED (`update.md` Step 6) | ✅ |
| C7 | "Both temporary directories are gitignored" | `update.md` Step 0 and Step 9 (new text) | `.gitignore` — only `.tfw/.upstream/` | ❌ → D2 |

## Discrepancies Found

**D1 — a guarantee printed as a constant.** `migrate_board.py`:750 emits `**Unaccounted: 0.** Every board row is classified exactly once; …` as a string literal, and `test_migrate_board.py`:237 and :508 assert that literal. The sentence is *entailed* — `require_guarantees()` at the top of `render_manifest()` raises before this line can run on an unbalanced corpus — but the line itself computes nothing and shows no arithmetic, and it is the very sentence the third report quoted over a table that listed `HD-30` twice. The computed form already exists eleven lines lower under `## Guarantees checked`. TS AC-2 bullet 1 gives exactly two acceptable states for an asserted invariant: computed under a heading naming the guarantee, or deleted — "not both left standing". This is both left standing. TS §7 DoF: *"A guarantee printed that the tool did not compute."* Small: delete the line and the two assertions, or print the count from `computed_guarantees()[0]`.

**D2 — a false sentence in a shipped workflow.** `update.md` Step 0: *"Both temporary directories are gitignored."* Step 9: *"Both are gitignored; leaving them is harmless."* `.tfw/.upstream-source/` is not in this repository's `.gitignore`, and neither directory is ignored in any receiving project unless its owner adds them — the payload ships no `.gitignore`. The pre-change text made the narrower claim about `.tfw/.upstream/` only, which is true here. The rewrite widened a repository-local fact into a false one and shipped it in a phase whose subject is honest tool text. Fix: either add `.tfw/.upstream-source/` to `.gitignore` **and** reword to "add both to `.gitignore` if they are not already", or drop the claim.

**Not a discrepancy, recorded for the judge:** the AC-3 fixture named its HL `HL-TFW_20260829-172110_ABT__approved_fixture.md` — a title appended after the identifier — while the same commit's `templates/status.md` teaches `authority: HL-PREFIX_YYYYMMDD-HHMMSS_ABBR.md` and `conventions.md` §4 says `{ID}` "means the same thing everywhere … no title is appended" (stated for clock tasks; silent for the current grammar). The fixture is discarded and the AC-3 gate does not name artifact filenames, so this is not an AC failure; it is the artifact-naming section left unextended, and the executor's own fixture tripped on the gap. → judge row 9, tech debt.

Escalated to 100% verification: all 23 implementation paths and all 8 work artifacts opened.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | `evidence/parser_and_prose_before_after.txt` · `evidence/four_corpora_compatibility.txt` | ✅ | ✅ — before/after output reproduced by command 8; four-corpus method stated, this corpus's 53 confirmed |
| E2 | `evidence/runtime_guarantees.txt` | ✅ | ✅ — three HELD lines with arithmetic; deliberate failure names guarantee and `TFW-9`; matches `test_deliberately_unbalanced_result_names_failed_guarantee_and_identifier` |
| E3 | `evidence/current_id_end_to_end.txt` | ✅ | ⚠️ — creation, clock read, HL abbreviation, status title and index row are **observed** (index row quoted). The collision clause is a **transcription of the rule**, not an observed refusal: no second creation was attempted. The creation path is agent-executed prose, so nothing else could have run; the EV should have said "verified as text" for that clause. Also the HL filename appends a title (see Discrepancies, last paragraph) |
| E4 | `evidence/parser_and_prose_before_after.txt` | ✅ | ✅ — `plain= normalize_text() and working_days plus emphasis` |
| E5 | `evidence/verification_gates.txt` | ✅ | ✅ — both `-k` selections reproduced (commands 1–2); guide names both commands in order (V11) |
| E6 | `evidence/verification_gates.txt` | ✅ | ✅ — 852 words reproduced; missing-tag fixture shows `exit 128`, `fatal: Needed a single revision`; the workflow text carries every rule claimed (V10). D2 sits in the same file but outside E6's claim |
| E7 | `evidence/verification_gates.txt` | ✅ | ✅ — `test_via_accepts_unregistered_tool_text_and_is_optional_for_hand_edits` passes `local-tool/v7` |
| E8 | `evidence/verification_gates.txt` | ✅ | ✅ — seven dispositions each traced (C6) |
| E9 | TS AC-8 · ONB answer 2 | ✅ | ✅ — DEFERRED names its blocker (`/tfw-release` after review, §15); a legitimate DEFERRED |

Total evidence items: 9 · verified: 8 · partial: 1 (E3, collision clause) · missing: 0.

## Knowledge Citations Verified

PV scan performed: priority 0 (`README.md` opening, § How It Works — heading exists at line 135; `.tfw/README.md` NS1–NS3 at anchors `ns1`/`ns2`/`ns3`), priority 1 (`methodology-values`, `success-criteria`, `where-truth-belongs` anchors exist), priority 2 (`knowledge/philosophy.md`), priority 3 (`KNOWLEDGE.md` §1), priority 4 (`conventions.md` §3, §11, §14) in full; 5–7 by relevance (`convention.md`, `process.md`, `risk.md`, `constraint.md` rows cited).

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | HL §7.2 #1 / ONB #1 | PV 0 — `README.md` opening and § How It Works | ✅ | ✅ | ✅ — "another authorized person or agent can understand … inspect its material grounds" | ✅ — a manifest that computes what it prints is inspectable grounds; an uncomputed one is not |
| 2 | HL #2 / ONB #2 | PV 0 — `.tfw/README.md` NS1, NS2 principles 3 and 5 | ✅ | ✅ | ✅ — "Selected Trace, not transcript"; "Continuation over isolated output" | ✅ — refusing malformed input and reporting it is selected trace; guessing is fabricated continuity |
| 3 | HL #3 / ONB #3 | PV 1 — Methodology values: Structural Enforcement | ✅ | ✅ | ✅ — "a rule that cannot reveal its own violation is only advice" | ✅ — pre-write gates over manifest prose; also the ground of TD-197 |
| 4 | HL #4 / ONB #4 | PV 1 — Methodology values + § Where truth belongs | ✅ | ✅ | ✅ — one authoritative owner per truth type | ✅ — migration reports and exits; D37 keeps `KNOWLEDGE.md` with `/tfw-docs` |
| 5 | HL #5 / ONB #5 | PV 1 — Portability + § Success Criteria | ✅ | ✅ | ✅ | ✅ — grammar carriers must agree in a receiving project (the ten-path R2 addition is this item applied) |
| 6–10 | HL #6–#10 / ONB #6–#10 | PV 2 — `philosophy.md` F4, F11, F27, F34, F38 | ✅ | ✅ all five rows present | ✅ — structural gates; no extra entities; observable progress; vague → usable; coordinator attention finite | ✅ — F11 is the ground for one dispatcher rather than a per-consumer regex; F27 for arithmetic printed with each guarantee |
| 11–15 | HL #11–#15 / ONB #11–#15 | PV 3 — D31, D50, D37, D43, D55, D59, D65 | ✅ | ✅ all rows present | ✅ | ✅ — D43 is the functional reason `gen_docs.py` entered scope; D59 (declaration ≠ authentication) is the reason `via` is free-form; D65 — no trace renamed |
| 16–17 | HL #16–#17 / ONB #16–#17 | PV 4 — `conventions.md` §§3–5, §13–14 | ✅ | ✅ | ✅ | ✅ — §15 role lock decided AC-8's owner; §14 anti-pattern "status normalized into vocabulary" governs malformed handling |
| 18 | HL #18 / ONB #18 | PV 5 — `convention.md` F22 | ✅ | ✅ | ✅ — board is a process artifact | ✅ — the retired board is migration input, not product authority |
| 19 | HL #19 / ONB #19 | PV 6 — `process.md` F7, F30 | ✅ | ✅ | ✅ — cross-session loss; capture without enforcement site | ✅ — rules moved into `update.md` steps and manifest arithmetic, not into a session |
| 20 | HL #20 / ONB #20 | PV 7 — `risk.md` F1 | ✅ | ✅ | ✅ — shared index, verbal directive survival 0/1 | ✅ — external corpora read at pinned commits, never staged; TFW-55 dirty files excluded from the commit (verified: `ecfceee` touches no TFW-55 path) |
| 21 | HL #21 / ONB #21 | PV 7 — `constraint.md` F1, F3 | ✅ | ✅ | ✅ | ✅ — no personal state in tree; template edits limited to the abbreviation field |
| 22–28 | HL #22–#28 / ONB #22–#28 | RES 1 external — YAML 1.2.2, RFC 8259, Git docs, Drive/OneDrive/Dropbox, five agent frameworks | not re-fetched this review (external; unchanged since the baseline; RES-1 inputs) | — | — | ✅ — ONB marks 22, 23, 25–28 **N/A** with a stated boundary (schema, journal carrier and transport untouched; TFW-61 owns sync) and 24 Applied (pinned commits isolate dirty corpora). The N/A reasoning is correct: Phase AB changes no carrier these items governed |
| 29 | HL #29 / ONB #29 | RES 2 — git-interpret-trailers, git-log, git-merge-base | not re-fetched | — | — | ✅ — "Applied in part": reachability of pinned commits; landing derivation unchanged |
| N1 | ONB new | `conventions.md` §15 · `release.md` | ✅ | ✅ | ✅ — `release.md` → Coordinator, "version bump → CHANGELOG → tag" | ✅ — decided Q2 |
| N2 | ONB new | `glossary.md` Task Naming · `compilable_contract.md` §2 | ✅ | ✅ | ✅ | ✅ — decided Q1's census |
| N3 | ONB new | `conventions.md` §10.3 | ✅ | ✅ | ✅ — templates and contract are upstream-owned payload | ✅ — why the live config alone does not deliver AC-3 |

Priorities 0 and 1 are recorded as distinct items (HL #1–#2 vs #3–#5) and checked separately: 0 against purpose/principle clauses (NS1, NS2.3, NS2.5), 1 against methodology-value clauses (Structural Enforcement, Portability, one owner per truth). No citation resolves to an absent, wrong or irrelevant item. **Total: 32 (29 + N1–N3) · resolved: 32 (24 opened locally, 8 external accepted as unchanged RES inputs) · semantically verified: 32 · irrelevant: 0 · hallucinated: 0.**

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings? — 31 of 31 (100%, escalated on D1)
- [x] Ran at least 1 build/test command (or documented why not)? — 10 commands
- [x] Claim & Source Checks filled — C1–C7; one ❌ (C7), one ⚠️ (C5)
- [x] Each RF §3 (AC) checkmark verified against actual file? — yes; AC-2 and AC-6 carry D1 and D2
- [x] KNOWLEDGE.md checked — contradictions with changes documented? — D68 and §3 Legacy row 2 still declare `YYYYMMDD-HHMMSS__slug` current and the event suffix an actor (RF O1); routed to `/tfw-docs` per D37. KNOWLEDGE.md:22 `docs/scripts/gen_index.py` path is TD-186, pre-existing
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified — Total: 32, resolved: 32, semantically verified: 32, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified — Total evidence items: 9, verified: 8, partial: 1 (E3 collision clause is text, not a run), missing: 0

Stage complete: YES
