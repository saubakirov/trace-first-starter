# Verify — "Are the claims true?" (revision 2)
> **Mindset:** Auditor. The RF is a declaration, not a fact.
> Min verify ratio: 0.42 · Files changed in `4846f27`: 10 · Verified: **10 of 10** — the round is small enough to read whole, and a corrective pass is where a stale sentence hides
> Method: `git diff ecfceee 4846f27`; commands re-run on the working tree at `4846f27` (unrelated TFW-55 files dirty, untouched; my own uncommitted rev1 review files present)

## Verification Log

### V1: `.tfw/scripts/migrate_board.py`
- **RF claim:** the redundant `Unaccounted: 0` sentence deleted; `Guarantees checked` is the only guarantee rendering
- **Actual:** four lines removed at :750–:753; `grep Unaccounted` over `migrate_board.py` and `test_migrate_board.py` returns nothing; `require_guarantees()` still runs at the head of `render_manifest()` and in `plan()`
- **Match:** ✅

### V2: `.tfw/scripts/test_migrate_board.py`
- **RF claim:** the two assertions that enshrined the literal deleted
- **Actual:** `:237` and `:508` assertions gone; the remaining assertions in both tests still check the malformed row, the directory and every identifier by name
- **Match:** ✅

### V3: `.tfw/workflows/update.md` · V4–V5: `.claude/commands/tfw-update.md`, `.agent/workflows/tfw-update.md`
- **RF claim:** both gitignore claims removed; 840 words; copies re-synced
- **Actual:** Step 0 ends at "present the resolved command."; Step 9 is one sentence with no claim; `grep -i gitignore` returns nothing; `wc -w` = 840; sha1 of the triplet collapses to one value. Every rule AC-6 requires (source pin, tag check, Step 5 recheck, provenance drift, allowlist, installed-adapter-only sync) is still present — the deletion removed only the two sentences
- **Match:** ✅

### V6: `RF__phase-ab__honest_migration.md`
- **RF claim:** revision 2 header; correction table; §4 refreshed
- **Actual:** as claimed. **One stale cell:** §1 modified-files row for `update.md` still reads "Reduced to 852 words" while §1's correction table and §4 say 840. A first-round figure left in a table that was otherwise not touched; harmless, noted for judge row 4
- **Match:** ⚠️ cosmetic

### V7: `evidence/EV__phase-ab__honest_migration.md`
- **RF claim:** E2 and E6 reference the correction; E3 wording explicit
- **Actual:** E3 now reads "The creation-workflow collision rule was verified as text; duplicate normalized directories are exercised as an actual refusal under E1" — the exact distinction rev1 asked for. E2 and E6 name the post-correction state. Verdict line unchanged: 8/9 VERIFIED, 1 DEFERRED
- **Match:** ✅

### V8: `evidence/verification_gates.txt`
- **RF claim:** correction-round section with gates re-run
- **Actual:** dated section appended, first-round section left as a record (its "852" is history, not a current claim); residual-text scan, targeted and full test runs, both checks, scope 707 + 320 = 1027
- **Match:** ✅

### V9: `journal/20260830-103847__transition__6544.md`
- **RF claim:** clock-read REVIEW correction event that also records the prior missing handoff without back-dating
- **Actual:** `time: 2026-08-30T10:38:47+05:00`, `kind: transition`, `on_behalf_of: saubakirov`, `via: codex`, `from: RF`, `to: RF`, three refs, summary 109 code points. Filename stamp equals `status.md` `updated`. Written after the fact and says so — the correct shape under §4 ("a correction is a new event that references the one it corrects")
- **Match:** ✅

### V10: `phase-ab/status.md`
- **RF claim:** `updated` bumped
- **Actual:** `lifecycle: RF`, `updated: 20260830-103847`
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest .tfw/scripts/ docs/scripts/ -q -k "not repository"` | **281 passed, 3 deselected** (118 s) |
| 2 | `python -m pytest .tfw/scripts/ docs/scripts/ -q -k repository` | **2 passed, 1 skipped, 281 deselected** — 283 passed, 1 skipped in total, matches RF |
| 3 | `python .tfw/scripts/gen_index.py --check project` | consistent with `2.0.0-dirty.3`; exit 0 |
| 4 | `wc -w .tfw/workflows/update.md` | 840 |
| 5 | `sha1sum` on the three workflow triplets | one hash each |
| 6 | `grep -n Unaccounted` / `grep -in gitignore` over the five corrected files | no matches |
| 7 | `git diff --numstat 57a5147 4846f27` excluding copies and work artifacts | 17 files, +707 −320 = **1027** — matches RF |
| 8 | Inline Python: `plan()` + `render_manifest()` on the `BOARD` fixture | `"Unaccounted" in manifest` → False; `**HELD**` × 3; `## Guarantees not checked by this run` present |
| 9 | `cat .gitignore` | unchanged — `.tfw/.upstream/` only; consistent with the workflow now making no claim |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | "The computed `Guarantees checked` section is now the only guarantee rendering" | RF §1 correction table | command 8: one `HELD` table, no other guarantee sentence in the rendered manifest | ✅ |
| C2 | "`update.md` remains under its ceiling at 840 words" | RF §1, §4; EV E6 | command 4 | ✅ |
| C3 | "1027 counted-line churn" | RF §4 | command 7 | ✅ |
| C4 | "283 passed, 1 skipped" | RF §4 | commands 1–2 | ✅ |
| C5 | "also records the prior missing execution-to-RF handoff without back-dating" | journal event summary; RF §1 | event time 10:38:47 = filename stamp = `status.md` `updated`; the first-round `updated: 173155` still has no event of its own, and the new event says so rather than inventing one | ✅ |
| C6 | "TD-200 and TD-201 remain reviewer-filed follow-up work" | RF §3 | `templates/journal/event.md`:49, :70 still say "provider family"; `conventions.md` §4 artifact table unchanged; TS has no revision 3 | ✅ — consistent |

## Discrepancies Found

No discrepancies. One cosmetic stale figure (RF §1 row for `update.md`: "852" where the current count is 840) — recorded, not escalated: the same RF states 840 twice and the evidence file dates both figures.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E2 | `runtime_guarantees.txt` · `verification_gates.txt` | ✅ | ✅ — literal absent (command 8), arithmetic HELD ×3 |
| E3 | `current_id_end_to_end.txt` · `parser_and_prose_before_after.txt` · `verification_gates.txt` | ✅ | ✅ — collision rule now labelled "verified as text"; directory-side refusal is a real run (`test_two_directories_resolving_to_one_identifier_stop_and_name_both`) |
| E6 | `verification_gates.txt` | ✅ | ✅ — 840 words, no gitignore claim |
| E1, E4, E5, E7, E8, E9 | unchanged since rev1 | ✅ | ✅ — carried; code paths untouched by `4846f27` |

Total: 9 · verified: 8 · DEFERRED with named blocker: 1 (E9, `/tfw-release`) · partial: 0 · missing: 0.

## Knowledge Citations Verified

Unchanged reference set: HL §7.2 (29) and ONB §7 (N1–N3) were verified in full at revision 1 — 32 resolved, 32 semantically verified, 0 irrelevant, 0 hallucinated. `4846f27` adds no citation and edits no cited file. Carried, not repeated.

## Checkpoint

- [x] Opened ≥ ⌈N × ratio⌉ files? — 10 of 10
- [x] Ran build/test commands? — 9
- [x] Claim & Source Checks filled — C1–C6, all hold
- [x] Each RF §3 checkmark verified? — AC-2 and AC-6 re-verified against the corrected files; others carried from rev1 with untouched code
- [x] KNOWLEDGE.md checked? — no change; D68 and §3 Legacy remain TD-202, routed to `/tfw-docs`
- [x] Knowledge Citations verified? — carried from rev1: 32 / 32 / 32 / 0 / 0
- [x] Evidence artifacts verified? — 9 items, 8 verified, 1 DEFERRED, 0 missing

Stage complete: YES
