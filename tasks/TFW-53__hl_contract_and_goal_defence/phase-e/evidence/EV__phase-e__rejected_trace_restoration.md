# EV — TFW-53 / Phase E: Rejected-Task Trace Restoration

> **Date**: 2026-08-18
> **Author**: Executor (Claude Code)
> **Task**: TFW-53
> **TS**: [TS Phase E](../TS__phase-e__rejected_trace_restoration.md)

---

## Environment

| Field | Value |
|-------|-------|
| OS | Windows 11 Pro 10.0.26200 |
| Language / Runtime | Python 3.13 (`docs/scripts/` test suite, PyYAML parse check) |
| Shell | Git Bash (POSIX) on win32 |
| Repository state | branch `master`, HEAD `eb95146` at collection time |
| Deploy target | N/A — the deliverable is framework text and two Markdown files; there is nothing to deploy |
| CI / Pipeline | local |

**Why a documentation phase still has real evidence.** Every AC of this phase is a claim about file
content, git history or a status vocabulary. All three are directly observable, so nothing here is
DEFERRED for want of an environment. The two things that could not be observed are named as such in
their rows.

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | `❌ REJECTED` present in all five carriers. `grep -rn "REJECTED" .tfw/ README.md` → **12 hits**, each classified in the table below. Six of the twelve are the five carriers (`conventions.md` supplies two — the diagram and the table row, both required by AC-1's first bullet); `README.md` supplies three of its own, the legend plus the two board rows AC-3 creates | Git Bash, ripgrep-free `grep -rn` | **VERIFIED** _(corrected 2026-08-18 — see the correction note below)_ | Hit classification table below; `conventions.md`:327 and :342, `project_config.yaml`:108, `templates/project_config.yaml`:112, `glossary.md`:130, `README.md`:298, :299 and :310 |
| E2 | AC-1 | The status is terminal in the §5 diagram — drawn as a side node, `from any status ──→ ❌ REJECTED     terminal · no edge leads out · the trace is kept`, with no outbound edge and no path to `📚 KNW` or `✅ DONE` | Read `conventions.md` §5 | **VERIFIED** | `.tfw/conventions.md`:327; quoted in RF §1 |
| E3 | AC-1 | The REVISE/REJECT branch is byte-unchanged. `git diff -U0 .tfw/conventions.md` shows **6 added lines, 0 deleted** across the whole file, so no pre-existing diagram line was touched | `git diff --numstat` → `6 0 .tfw/conventions.md` | **VERIFIED** | inline output above |
| E4 | AC-1 | Both `project_config.yaml` files parse as YAML after the insertion, and the new entry sits **after** `BLOCKED` with the same key shape and no spurious `role` key | PyYAML 3.13: both files → *parsed OK, 11 statuses, order ['BLOCKED','REJECTED'], emoji U+274C, role key present: False* | **VERIFIED** | inline output, RF §4 |
| E5 | AC-1 | The `glossary.md` count sentence ships the ONB R6 wording: the pipeline is still counted at 9, the two off-pipeline states follow with their boundary in the same sentence | Read `glossary.md`:130 | **VERIFIED** | `.tfw/glossary.md`:130 |
| E6 | AC-1 | The three-way collision is stated at **both** ends: the `conventions.md` §5 row and the `glossary.md` status article name all three tokens; the `glossary.md` `### Amendment Log` article gains exactly one clause and nothing else | Read all three sites; `git diff .tfw/glossary.md` → 2 changed lines, both single-line replacements | **VERIFIED** | `.tfw/conventions.md`:342, `.tfw/glossary.md`:130 and :57 |
| E7 | AC-1 | `templates/HL.md` is **not** touched — the Phase A file where the amendment verdict lives | `git status --short .tfw/templates/HL.md` → no output | **VERIFIED** | inline output |
| E8 | AC-2 | `conventions.md` §13 gains the trace rule as a third sentence; the two existing sentences are unchanged | `git diff -U0 .tfw/conventions.md` — additions only, 0 deleted lines | **VERIFIED** | `.tfw/conventions.md` §13 |
| E9 | AC-2 | §14 gains **one** bullet, appended after the last existing entry; no other phase's entry is edited. Bullet count 38 → 39 | `git diff` shows one `+` bullet in §14 and no `-` line | **VERIFIED** | `.tfw/conventions.md` §14, last bullet before `### 14.1` |
| E10 | AC-2 | The §13 rule and the §14 bullet name **no task and no repository** — checked by searching both added passages for `TFW-4`, `TFW-5` and `this project` | `grep -n "TFW-4\|TFW-5" ` over the §13 and §14 additions → no match | **VERIFIED** | the two added passages, quoted in RF §1 |
| E11 | AC-3 | Both board rows sit between TFW-47 and TFW-50, each with `❌ REJECTED` and a link to its task folder; each description cell is one line | Read `README.md`:298–299 | **VERIFIED** | `README.md`:298 (TFW-48), :299 (TFW-49) |
| E12 | AC-3 | TFW-48's status is **assigned**, not restored, and the row says so. Pre-restore comparison: `git show 5b17786:README.md \| sed -n '294,295p'` → line 294 status cell `🟡 TS (D)`, line 295 status cell `❌ REJECTED — complete product-fit failure; superseded by TFW-50` | Git Bash | **VERIFIED** | inline output; the difference is stated in both the row and the post-mortem header |
| E13 | AC-3 | TFW-49's status cell is a **literal restoration** — byte-compared against `5b17786:README.md`:295 | `diff` of the extracted status cell → identical | **VERIFIED** | `README.md`:299 |
| E14 | AC-4 | Every git reference in both post-mortems re-executed at collection time: `721ca15` → **75** files · `bc6779e` → **149 files changed, 798 insertions(+), 27103 deletions(-)** · `5b17786:README.md`:294–295 → both status cells as quoted · `ad0696e` → `[codex/TFW-50/master/coordinator] reject TFW-49 and draft prompt-first replacement` · `9e19a4f` → `[master]: TFW-49: approve agent commit identity research`, 2026-07-30 | Git Bash, all six commands | **VERIFIED** | inline outputs, reproduced in RF §4 |
| E15 | AC-4 | The TFW-49 owner verdict is **byte-identical** to its source, whole and unelided — the seven-line block extracted from `ad0696e` and `diff`ed against the post-mortem copy | `diff` → no output, `IDENTICAL` | **VERIFIED** | `POSTMORTEM__TFW-49.md` § The owner's verdict |
| E16 | AC-4 | The `bc6779e` verdict sentence is byte-identical in **both** post-mortems — extracted, newline-normalised, compared against `git log -1 --format=%B bc6779e` | `diff` per file → `IDENTICAL` twice | **VERIFIED** | both files, § The owner's verdict |
| E17 | AC-4 | `9e19a4f` is described as *the commit that recorded the approval of TFW-49's research* and explicitly **not** as a contract baseline, with the reason stated | Read `POSTMORTEM__TFW-49.md` recovery table | **VERIFIED** | `POSTMORTEM__TFW-49.md` § Recovering the full artifacts, row 2 |
| E18 | AC-4 | Length: `wc -w` → TFW-48 **544 words**, TFW-49 **727 words**. Both single-page. TFW-49 is longer by the seven-line verdict block the coordinator approved at ONB R1 plus two extra recovery rows | `wc -w` | **VERIFIED** | inline output |
| E19 | AC-4 | Both files carry the same five sections in the same order: *What the task attempted · The owner's verdict · The failure mechanism · Recovering the full artifacts · What replaced it* | `grep -n "^## "` on both files → identical heading sequence | **VERIFIED** | both files |
| E20 | AC-4 | TFW-48's successor line reads *"Nothing replaced it. No successor task has been chartered."* and TFW-55 is not named anywhere in either file | `grep -c "TFW-55"` on both → 0 | **VERIFIED** | `POSTMORTEM__TFW-48.md` § What replaced it |
| E21 | AC-4, AC-3 | Every relative link in both post-mortems and both board rows resolves to an existing path — 3 post-mortem links, 4 board links, 7 of 7 | filesystem existence check per link | **VERIFIED** | inline output, RF §4 |
| E22 | AC-5 | `find tasks/TFW-48__* tasks/TFW-49__* -type f \| wc -l` → **2**. Exactly one file per folder, both `POSTMORTEM__*.md`. No `phase-*/`, no `research/`, no HL, no RF | Git Bash | **VERIFIED** | inline output |
| E23 | AC-5 | No artifact file from `721ca15` re-entered the working tree — `git status --short` lists only the two post-mortems as new under `tasks/TFW-48*`/`tasks/TFW-49*`, against 75 files that stay in history | `git status --short` | **VERIFIED** | inline output, RF §3 |
| E24 | AC-6 | `[Unreleased]` no longer says *"Nothing pending."* — it carries one `### Added` block naming the status, the §13 rule and the §14 anti-pattern. `git diff .tfw/CHANGELOG.md` → **1 hunk**, 4 insertions, 1 deletion (the *"Nothing pending."* line it replaces) | `git diff --numstat` → `4 1 .tfw/CHANGELOG.md` | **VERIFIED** | `.tfw/CHANGELOG.md`:6–11 |
| E25 | AC-6 | The `[1.2.0]` entry is untouched, and `VERSION` / `tfw.version` are untouched | `git diff .tfw/CHANGELOG.md \| grep "1\.2\.0"` → no match · `git diff .tfw/VERSION` → no output · `git diff .tfw/project_config.yaml \| grep version` → no match | **VERIFIED** | inline output |
| E26 | AC-1..AC-6 | Regression: the project's only executable gate still passes. `python -m pytest docs/scripts/` → **68 passed** in 61.85s, against the Phase D baseline of 68 passed | local Python 3.13 | **VERIFIED** | inline output, RF §4 |
| E27 | AC-3 | **Board rows: recorded DEFERRED at collection time, discharged since.** At collection `README.md` was in the working tree and unstaged — held by a concurrent TFW-55 session, so per TS §9 and the ONB Q2 answer (b) the executor left it unstaged and the coordinator landed it. **Discharged 2026-08-18:** the rows are committed. `git log --oneline -1 -- README.md` → `8d9432b`, which carries `README.md \| 9 +-`. `grep -n "REJECTED" README.md` → 298, 299, 310 in the committed tree | Git Bash, both at collection time and at re-execution | **VERIFIED** _(was DEFERRED at collection; the blocker cleared, and both states are recorded rather than the first being overwritten)_ | `README.md`:298–299, committed in `8d9432b`. Note: that commit's subject names TFW-58, not TFW-53 — filed as TD-178, and not a defect of this phase's own work |

### The twelve `REJECTED` hits, classified

> **Correction, 2026-08-18 — REVIEW Phase E finding D1a.** This table first reported **ten** hits and a
> legend at line 307. Both numbers came from a `README.md` that already carried the edited legend but
> **not yet** the two board rows — a mid-execution snapshot recorded as the final state. Nine `.tfw/`
> hits plus that one README hit is exactly the ten first reported. The count is **twelve**, and the two
> that were missing are `README.md`:298 and :299 — the board rows AC-3 exists to create, which are
> carriers of the new status in the most load-bearing sense in this phase. The command is re-executed
> below against the committed tree. The original figures are stated here rather than silently replaced,
> because this file is the phase's permanent record and a corrected number that hides its correction is
> the same defect one layer in.

The TS gate predicted seven. The actual count is **twelve**, and every hit beyond the seven is a site the
amended TS itself requires — so the arithmetic is reported here rather than left for the reviewer to
reconcile.

| Hit | Site | Which of the three meanings | New? |
|-----|------|-----------------------------|------|
| 1 | `.tfw/conventions.md`:327 | **task status** — the §5 diagram side node | new (AC-1) |
| 2 | `.tfw/conventions.md`:342 | **task status** — the §5 table row, which also names the other two | new (AC-1) |
| 3 | `.tfw/project_config.yaml`:108 | **task status** — `tfw.statuses` entry | new (AC-1) |
| 4 | `.tfw/templates/project_config.yaml`:112 | **task status** — the same entry, so a new project is born with it | new (AC-1) |
| 5 | `.tfw/glossary.md`:130 | **task status** — `## Status Flow`, and names the other two | new (AC-1) |
| 6 | `README.md`:310 | **task status** — the board legend | new (AC-1) |
| 7 | `README.md`:298 | **task status** — the TFW-48 board row, status **assigned** now | **new (AC-3)** — missing from the first count |
| 8 | `README.md`:299 | **task status** — the TFW-49 board row, status restored byte-identical from `5b17786` | **new (AC-3)** — missing from the first count |
| 9 | `.tfw/CHANGELOG.md`:9 | **task status** — the `[Unreleased]` announcement | new (AC-6) |
| 10 | `.tfw/glossary.md`:57 | **amendment verdict** — the `### Amendment Log` article's one appended clause, pointing at the task status | new (AC-1, second bullet — the other end of the collision) |
| 11 | `.tfw/templates/HL.md`:246 | **amendment verdict** — HL §12 verdict vocabulary | pre-existing, Phase A, untouched |
| 12 | `.tfw/templates/HL.md`:248 | **amendment verdict** — the `WITHDRAWN` rationale referring to it | pre-existing, Phase A, untouched |

**Reconciling 7 against 12.** The TS gate counted *five carriers = five hits, plus two pre-existing*.
Four things it did not count:

1. `conventions.md` carries the status **twice** — AC-1's own first bullet demands both the table and the
   ASCII diagram, so one carrier is two hits.
2. `README.md` carries the status **three times, not once** — the legend under AC-1 plus the two board
   rows under AC-3. The gate line treated the README as a single legend carrier, which is what the first
   count reproduced.
3. The `glossary.md` `### Amendment Log` clause is required by AC-1's second bullet — the other end of
   the three-way collision.
4. The `[Unreleased]` block is required by AC-6, which was added to the TS after the gate line was
   written.

**Final split: task status 9 sites · amendment verdict 3 sites · review verdict `❌ REJECT` 0 new,
untouched.** 9 + 3 = 12, matching both the table above and the re-executed command.

**Re-execution, against the committed tree:**

```
$ grep -rn "REJECTED" .tfw/ README.md | wc -l
12
$ grep -rn "REJECTED" .tfw/ README.md | sed 's/:.*//' | sort | uniq -c
      1 .tfw/CHANGELOG.md
      2 .tfw/conventions.md
      2 .tfw/glossary.md
      1 .tfw/project_config.yaml
      2 .tfw/templates/HL.md
      1 .tfw/templates/project_config.yaml
      3 README.md
$ grep -n "REJECTED" README.md | cut -d: -f1
298
299
310
$ grep -n "^> Statuses:" README.md
310:> Statuses: ⬜ TODO → … → ✅ DONE | ❌ BLOCKED (waiting) | ❌ REJECTED (closed unsuccessfully, trace kept)
```

**Why the legend moved 307 → 310.** Three lines were inserted above it: this phase's two board rows, and
one TFW-58 proposal row added by the same coordinator commit that landed the board (`8d9432b`). Only two
of the three displaced lines are this phase's.

## Verdict

Evidence verdict: **27/27 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A**

_At first collection: 26/27 VERIFIED, 1 DEFERRED — E27, the board rows, which existed and were read but
were not yet committed because `README.md` was concurrently held. The coordinator landed them in
`8d9432b`, so the blocker cleared and E27 is now VERIFIED. Both states are recorded on the row rather
than the first being overwritten._

> **Corrections applied 2026-08-18 after REVIEW Phase E (🔄 REVISE, one finding).** Two numbers in this
> file did not reproduce, both from one cause — a mid-execution snapshot recorded as the final state:
> the `REJECTED` census (**10 → 12**, the two board rows were missing) and the README legend line number
> (**307 → 310**). Every command behind the corrected figures is re-executed above with its output
> quoted. Discharging E27 was not among the review's five items; it is corrected here because leaving it
> DEFERRED while the RF reports the rows as committed would have created a fresh contradiction between
> the two files of the same phase. No product file was touched by this corrective pass.

## Attachments

No binary artifacts. Every observation in this phase is text in a tracked file or output from a git
command, and each row above names the file, the line or the command that produces it.

---

*EV — TFW-53 / Phase E: Rejected-Task Trace Restoration | 2026-08-18*
