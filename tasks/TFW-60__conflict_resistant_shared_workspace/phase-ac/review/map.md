# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase AC](../RF__phase-ac__update_without_guesswork.md)
> TS: [TS Phase AC](../TS__phase-ac__update_without_guesswork.md) — revision 2, amendment A7 approved
> Reviewer: Claude Code, `on_behalf_of: saubakirov` (one profile in `team/`, used silently), `via: claude-code`
> Contract baseline: master HL at `e8690c7` — the A7 re-freeze (`git log --format="%h %s" | grep -E '^\S+ \[[^]]*/TFW-60/freeze/'`); `56c3d70` is the A6 baseline the phase HL and TS name, and `56c3d70..e8690c7` is exactly A7 (deliverable 6 gains `Changed`; §12 gains row A7). `e8690c7..HEAD` on the HL: empty.

## Understanding

The update path had five places where it guessed or decided for the owner, each measured on a real project in the fourth and fifth field reports. The executor rewrote `update.md` (840 → 1174 words) so that the pin is derived from the tag the operator names, the update stops before its first durable write with exactly three questions (handle, containers, `build.*`), the payload copy excludes the two project-owned files and prints what it skipped, every Step 6 row is declared a `cmp` copy or a marker-bounded block, `installed_from` has one form, and the update ends with a briefing rendered from a new template out of four CHANGELOG sections. Two scripts changed in one function each: `migrate_board.classify_status()` now refuses a status cell that carries a second declared token or a second Unicode-`So` symbol (`UNDECLARED`, verbatim, never terminal, own manifest heading, phase directories named), and `gen_index.check_tasks()` names phase directories without `status.md` — a failure under a live task, one informational line per terminal/stateless/malformed task. `check_project()` reports a machine-local `installed_from`. Around the two scripts, twenty text carriers were brought into agreement: the abbreviation rule (initials of the approved title, proposed with it) in five files, the one marker rule in conventions §9 with the Claude template gaining markers and this repository's root `CLAUDE.md` carrying the block, `{version}` removed from three adapter templates, TD-190/191/198/200/201/203/204 closed in the CHANGELOG, RELEASE.md, three templates and the migration guide.

Key decisions the executor took inside its grant: the second-signal class is Unicode `So`, not category S (ruled at onboarding on a four-corpus measurement); the exclusion list carries both project-owned files and the payload keeps shipping them, with the root cause filed as O11; Step 5's copy is a POSIX `find | while read` loop that prints `skipped:`; the `TFW:CLAUDE` block bounds the `## TFW` section and was brought current before being bounded; the briefing reads four sections and nothing else. Three commits (`d2e6bae`, `4fe3b1d`, `d047286`) plus the RF/EV commit `af1a695`; 26 counted paths, 1 new, 943+/172− measured by the reviewer over the same set.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 pin derived from the tag, `VERSION` compared, Step 5 recheck against the derived commit, porcelain rule kept | RF §3 AC-1, four boxes; gate: live-source PASS, fabricated tag STOP | ✅ |
| AC-2 updating section reaches every earlier tag; RELEASE.md §5/§6 rules; TD-198 quote; TD-191 closed; TD-190 superseded-by; Step −1 in `update.md`, the guide and the `.5` section | RF §3 AC-2, six boxes; `.5` section content in RF §1 | ✅ |
| AC-3 allowlist admits retirement text; zero outside on this repository and one consumer | RF §3 AC-3, two boxes; 0 / 0 | ✅ |
| AC-4 markers in the Claude template; Step 6 `Kind` per row; one marker rule in §9 (R2); block brought current (R2); root `CLAUDE.md` (R2); Cursor (R2); Antigravity; Claude README | RF §3 AC-4, eight boxes | ✅ |
| AC-5 `installed_from` = `{upstream}@{verified-tag}`; `--check project` reports a machine path; `self` valid | RF §3 AC-5, three boxes | ✅ |
| AC-6 🛑 three questions before the first write, AG one message; answers in checklist; Step 8a briefing from the template, four blocks (A7), absent → *nothing in this release*; last message; < 1200 words | RF §3 AC-6, five boxes; 1174 words | ✅ |
| AC-7 exclusions named; copy prints skipped; executor decision recorded; payload test covers the list; R2 decision | RF §3 AC-7, four boxes | ✅ |
| AC-8 whole-or-refuse on the status cell (`So`, R2); `UNDECLARED` never terminal/skipped; manifest heading; phase directories named; `--check tasks` failure/informational (one line per task, R2); `templates/status.md` phase paragraph; guide; `AILAB-2` fixture failing before | RF §3 AC-8, eight boxes; 22 of 28 fail before, 28 pass after; 8 class changes over 114 rows | ✅ |
| AC-9 abbreviation rule in conventions §4, `plan.md`, `init.md`, glossary, HL template; artifact naming rows (TD-201) | RF §3 AC-9, four boxes | ✅ |
| AC-10 `via` in `event.md` (TD-200); `profile.md` (TD-203); guide: one manifest location, `--working-tree`, root commands; grep clean | RF §3 AC-10, four boxes | ✅ |
| AC-11 executor items: `.2/.3/.4` must-know; every §6 item and defect 7 fixed or filed; `2.0.0` unclaimed. Release and field items after review | RF §3 AC-11: three executor boxes ticked, two release/field boxes open and marked as not the executor's act | ✅ — the open boxes are the TS's own assignment |
| §4 census 26 counted, 1 new, inside `50/50/5000/50` | RF header: 26 counted, 6 copies (S32), 943+/172− | ✅ |
| §7 DoF — no pin from `HEAD`; no two-signal cell classified; no skipped row unprinted; no unnamed stateless phase; no `status.md` written into another task; no overwriting copy; no inferred handle; abbreviation rule unambiguous; < 1200 words; no CHANGELOG rewrite; no identifier reclassified; no budget crossed; no check reported that did not run | RF §2, §3, §4 address each; the four-corpus comparison names 8 class changes, all multi-signal | ✅ |

## Deviations from TS

- **Cursor template and root `CLAUDE.md`** were not in TS revision 1's census; both were admitted at onboarding (Q2 ruled A; rec. 3 returned) and the TS carries them as R2. Not a deviation from the governing revision.
- **`RETIRED_WORDINGS` gains a TD-198 row** in `test_integration.py` — ONB rec. 4, accepted; inside the Tests group, no new path.
- **`check_project()` in `gen_index.py`** changed for AC-5; the TS §4 table lists `gen_index.py` for `check_tasks()`/`read_phase_status()` only. The file was in the census; the function was not named. AC-5's second bullet requires exactly this behaviour, so the path and the work are both in scope.
- **TS AC-1 names a commit target** ("or a commit when the owner deliberately takes an untagged payload") and `update.md` Step 0 repeats it in prose, but the shell block tests `"$target_ref" = "v$target"` unconditionally, which cannot pass for a commit. Not a TS item missed — the TS states no check for that path either — recorded for Verify and Judge.
- No RF work outside the TS scope was found. `[Unreleased]` untouched; no `.5` entry written; no `status.md` written into any other task; the four consumer projects untouched (read-only, confirmed by `git status` on three of them at review).

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy? Pain before mechanism; one normal writer per mutable file; stable paths over status moves; local truth, derived views; filesystem first, Git preserved; no trace deletion during simplification; every phase pays for its release surface. Phase AC applies P1 (every fix is a measured field shape), P4/P5 (`UNDECLARED` is a value a person resolves; the gate names what it did not write), P9 (CHANGELOG appended, never rewritten) and P10 (workflow, canon, templates, adapters, guide, tests and release surface in one phase).
- [x] Read ONB — were blocking questions resolved? Two questions, both ruled by the coordinator in ONB §8 and carried into TS R2; A7 filed and approved the same day; nothing open at execution start.

Stage complete: YES
