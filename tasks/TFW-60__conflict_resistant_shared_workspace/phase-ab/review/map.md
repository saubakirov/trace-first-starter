# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase AB](../RF__phase-ab__honest_migration.md) — commit `ecfceee`
> TS: [TS Phase AB, revision 2](../TS__phase-ab__honest_migration.md) — approved by owner 2026-08-29
> Master HL at contract baseline: `810b1b8` (`[claude-code/TFW-60/freeze/coordinator] add the phase that makes migration honest`), recovered per `conventions.md` §3 rule 15
> Reviewer: Claude Code, `on_behalf_of: saubakirov`, `via: claude-code`. One profile in `team/` — used without asking

## Understanding

The third external update (`helpdesk`, `0.8.7 → 2.0.0-dirty.3`) showed `migrate_board.py` reading `HD-30b` as `HD-30`, writing `lifecycle: TODO` onto a shipped task, and printing "accounted for exactly once. Unaccounted: 0" over a table that listed one identifier twice. Phase AB, added by amendment A5, makes the tools tell the truth and lands one identifier grammar for new tasks.

The executor (Codex, one commit `ecfceee`, 23 implementation paths, 17 budget-counted, 0 new files, 1029 counted lines of churn) did four things. **Parsing:** removed the unanchored `re.search(r"[A-Z][A-Z0-9]*-\d+")` in `parse_board()` that reached the identifier before the anchored grammar could refuse it; every candidate now goes whole through one dispatcher in `gen_index.parse_identifier()` returning `current | clock | legacy | None`, and a third pattern `CURRENT_ID = ^PREFIX_YYYYMMDD-HHMMSS_ABBR$` was added. Two board rows or two directories normalizing to one identifier raise before any write. **Guarantees:** `computed_guarantees()` produces three partition equalities with their arithmetic; `require_guarantees()` runs in `plan()` and again at the top of `render_manifest()`, so the manifest file is never opened on an unbalanced corpus; the manifest prints each guarantee as `HELD` with its arithmetic and lists what it did not check. **Prose:** `_plain()` strips `_` only at word boundaries, so `normalize_text()` survives. **Grammar carriers:** `conventions.md`, `glossary.md`, both `project_config.yaml`, `templates/HL.md` (new `Abbreviation` header field), `templates/status.md`, `compilable_contract.md`, `plan.md`, `init.md` and `gen_docs.py` now issue or resolve the current grammar; `id_max_retries` is retired and `--check project` names it. Alongside: `update.md` cut from 1380 to 852 words while gaining source-pin, tag-check, provenance-drift and allowlist rules; `via` declared free-form and validated as non-empty; the migration guide names the `-k "not repository"` / `-k repository` split.

Release work (VERSION, CHANGELOG, tag) is deliberately not done — ONB answer 2 and TS revision 2 moved it to `/tfw-release` after review, correcting Phase AA's ruling against `conventions.md` §15.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 parsed whole or refused; three named forms; malformed visible; duplicate rows **and** directories hard-stop; four corpora compared | §3 AC-1 ✅ — dispatcher, collision refusal, `four_corpora_compatibility.txt` | ✅ |
| AC-2 every printed guarantee computed; invariant evaluated at run time; failing invariant stops before the manifest is opened; checked vs not-checked distinguished | §3 AC-2 ✅ — `runtime_guarantees.txt`, deliberate `TFW-9` failure | ✅ claim; see verify.md D1 for the one residual literal |
| AC-3 `{PREFIX}_{stamp}_{ABBR}`; owner approves ABBR; no `_` in fields; HL header records ABBR; collision → refuse, never suffix; session name uses new ID; canon states all three forms | §3 AC-3 ✅ — disposable `ABT` fixture, `current_id_end_to_end.txt` | ✅ |
| AC-4 markup stripped, identifier characters kept | §3 AC-4 ✅ | ✅ |
| AC-5 repo-state tests separable; guide names both commands | §3 AC-5 ✅ | ✅ |
| AC-6 source quiescence; provenance drift; reachable retired-term condition; `update.md` < 1200; "commit, or at least stage" corrected | §3 AC-6 ✅ — 852 words, missing-tag fixture exit 128 | ✅ claim; see verify.md D2 for a false sentence the rewrite introduced |
| AC-7 `via` free-form, stated where defined, validated; TD-197 closes | §3 AC-7 ✅ | ⚠️ canon + validator agree; the event template (`templates/journal/event.md`:49, :70) still says "provider family" — filed by the RF as O4 |
| AC-8 executor: seven §7 items fixed or filed; dirty-era consumer notes in RF | §3 AC-8 executor ✅ | ✅ |
| AC-8 release: `/tfw-release` after review | §3 AC-8 release ⬜ DEFERRED | ✅ — correct per §15 and TS R2 |
| §4 budget 30/15/30/3000, no overrun; measured 25/19 incl. release files | §4 Scope: 23 physical, 17 counted, 0 new, 1029 lines | ✅ (25 − 2 deferred release files = 23) |
| §6 "Trace before fixing AC-1 … report the mechanism in the RF" | §2 decision 1 and `parser_and_prose_before_after.txt` | ✅ |
| §6 "Do not fix `HD-30b`" | HELPDESK_SHAPE fixture; no consumer written | ✅ |
| §6 preserve empty-board refusal, per-identifier accounting, printed root, `--check tasks`, `--working-tree` logging | code diff touches none of them; `--check tasks` passes on 53 tasks | ✅ |

## Deviations from TS

- **Not in TS, done:** nothing. Every changed path is in TS §4 or its R2 addition. The six adapter copies are re-synced as the owner's copies ruling requires; `.agents/skills/` was verified, not rewritten (D54).
- **In TS, filed rather than done:** the event template's `via` wording (RF O4) and `templates/team/profile.md` (RF O2) — both outside the 25-path census; the executor filed rather than widened, as §4 instructs.
- **In TS, deferred by design:** AC-8 release acts → `/tfw-release`.
- **RF authorship header:** `Author: saubakirov` — accountable human named, tool (`codex`) visible only in the commit subject and the journal event. Consistent with the two-field model; not a defect.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy? Pain before mechanism; task locality; one writer per file; stable paths; local truth, derived views; filesystem first, Git preserved; coordinator logs management; consolidation is a boundary; no trace deletion; every phase pays for its release surface.
- [x] Read ONB — were blocking questions resolved? Three questions, all answered in the file with options weighed; four of nine inconsistencies acknowledged as the coordinator's own and corrected in TS R2.

Stage complete: YES
