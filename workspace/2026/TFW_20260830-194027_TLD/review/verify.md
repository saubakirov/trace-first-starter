# Verify — "Are the claims true?"

> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: **0.42** (`tfw.review.min_verify_ratio`)
> RF files claimed: **43** (41 modified · 1 created · 1 deleted). Measured in `dfba46f`: 42 M · 1 R · 6 A
> Files to verify: ⌈43 × 0.42⌉ = **19**
> **Actually verified: 43 of 43 — escalated to 100%** on the discrepancies in *Discrepancies Found* below

## Verification Log

### V1 — `tasks/DEBT-SNAPSHOT.md` · `TECH_DEBT.md`
- **RF claim:** moved by `git mv`, 160 lines = 28-line header + 132 sealed lines byte-identical to `c153895:TECH_DEBT.md`; 121 rows; root file gone; header states counts, revision and *sealed unexamined*, and characterizes nothing.
- **Actual:** `wc -l` = **160**. `diff <(git show c153895:TECH_DEBT.md) <(tail -n 132 tasks/DEBT-SNAPSHOT.md)` → **empty**. `grep -c '^| TD-'` → **121**. `test -e TECH_DEBT.md` → absent. Source `md5` = `0bd36979416174709d11c2a6c6779504`, as recorded. `git diff --name-status -M` reports `R098 TECH_DEBT.md → tasks/DEBT-SNAPSHOT.md` — a rename, so `--follow` history is real, not asserted. Header read end to end: counts (132 lines · 12 352 words), revision `c153895`, retirement date, the *sealed unexamined / age is not evidence of importance* sentence, and the note that the file's own footer is sealed with it. No row is quoted, summarized or characterized.
- **Match:** ✅

### V2 — `.tfw/workflows/review.md`
- **RF claim:** Step 5 rewritten to one write, three outcomes, the existence test, the literal search; Step 6 loses the append and gains the undisposed check; Step 7 loses `+ TECH_DEBT.md`; description, Output line, Trust-protocol row and two anti-patterns updated.
- **Actual:** read Steps 5–7 and the anti-pattern list in full. All present and correct: *"Debt is written **once**"*, the three outcomes with no fourth, *"A disposition names something that already exists when it is written"*, `→ backlog` named as not a disposition, `pending` named as a waiting state rather than a fourth outcome, *"`not material` is a first-class answer"*, and *"The task does not reach `DONE` while an item is undisposed."* Step 6 item 2 is the undisposed check; Step 7 item 4 gates `DONE` on §5. Frontmatter description reads *"…writes REVIEW, disposes of debt"*. Two anti-patterns added, one on skipped triage and one on closing with an undisposed item or a disposition naming nothing.
- **Match:** ✅ **content** — but see **D1** for how this file is delivered through the Claude Code adapter.

### V3 — the replacement search, executed
- **RF claim (AC-3):** the search is written out literally and **returns 243 rows** on this corpus.
- **Actual:** copied verbatim from `.tfw/workflows/review.md` and run from the project root. Output piped to `wc -l` → **243**. Exact match, and the operation is correct: it enumerates `REVIEW*.md` files carrying the §5 heading, prints each data row with its filename, and skips header and separator rows.
- **Match:** ✅

### V4 — `.tfw/templates/REVIEW.md`
- **RF claim:** §5 → *Tech Debt Collected and Disposed*; `Action` column → `Disposition`; checklist row 3 → debt disposed with its reason on its face; §6 gains an undisposed-row check.
- **Actual:** heading is *## 5. Tech Debt Collected and Disposed*, with an explicit note that the words *Tech Debt Collected* are kept because the search matches on them. Column header is `Disposition`; the example row reads `not material — {the ruling}`; the three forms are given as `paid — phase-{x}` · `promoted — {TASK-ID}` · `not material — {ruling}`, with `pending — owner` named as a waiting state and `→ backlog` named as not a disposition. §6 carries `- [ ] §5 — no row left undisposed`.
- **Match:** ✅

### V5 — `.tfw/templates/review/judge.md`
- **RF claim:** row 3 → **Debt disposed**, carrying the three outcomes, the existence test and the reason it is kept (consequence, not rate). One self-check line added.
- **Actual:** row 3 reads exactly that, with the parenthetical *"kept on consequence, not rate: the undisposed item is precisely what filled the registry retired at 2.1.0 — 77 of its 121 rows open, none consumed"*. Self-check gains *"Row 3: every §5 row disposed, and each disposition names something that exists today?"* No row was added — the count stays ten, satisfying `conventions.md` §14's firing-rate rule and ONB Recommendation 4.
- **Match:** ✅

### V6 — AC-2 census, re-run independently
- **RF claim:** `grep -ri 'TECH_DEBT'` over the canon returns **33 hits, every one historical**, classified per file and line.
- **Actual:** re-ran the exact command from TS AC-2. **33 hits.** Distribution: `.tfw/CHANGELOG.md` 26 · `.tfw/glossary.md` 1 · `.tfw/migrations/2.0.0.md` 3 · `KNOWLEDGE.md` 1 · `README.ru.md` 1 · `README.kk.md` 1. Every non-CHANGELOG hit read verbatim: the glossary's *Debt Registry (retired at 2.1.0)* entry, migration step 6's three lines (the retirement instruction and its rollback note), the `KNOWLEDGE.md` §3 Legacy row, and the two translated retirement notes. The CHANGELOG's 26 are the 2.1.0 retirement record plus 0.x–2.0.0 history. **Zero hits** in `README.md`, `RELEASE.md`, `CLAUDE.md`, `AGENTS.md`, all workflows, all templates, the contract, `docs/scripts/` and all three adapter sets — exactly as claimed.
- **Match:** ✅ — the RF's per-line classification is accurate line for line.

### V7 — AC-5 deferral scan, re-run
- **RF claim:** the post-change scan for the deferral shape returns only the three sentences that **prohibit** deferral.
- **Actual:** scanned `.tfw/workflows/` and `.tfw/templates/` for `record it as debt` · `instead of fixing/resolving` · `→ backlog` · `defer to backlog` · `if you can't/cannot`. Three hits, all prohibitions: `review.md:138`, `judge.md:17`, `REVIEW.md:70`. No instruction of the form *"if you cannot fix it, record it as debt"* survives anywhere.
- **Match:** ✅

### V8 — `.tfw/workflows/docs.md`
- **RF claim:** no debt step at all; prerequisite 2, Scope line, checklist row 4 (5→4, 6→5), the extraction bullet and the batch-mode line.
- **Actual:** diff confirms every one. Prerequisite 2 deleted, checklist row 4 deleted with 5–6 renumbered, `Observations → tech debt candidates` bullet deleted, batch line now reads *"…proposal for KNOWLEDGE.md"*. The only surviving occurrence of the word is the **Does NOT write to** line, which now states *"**debt of any kind** — it is captured and disposed of in the REVIEW that found it, and this workflow has no debt step"*. Frontmatter description updated.
- **Match:** ✅

### V9 — `.tfw/workflows/resume.md`
- **RF claim:** step 9 removed and 10–15 renumbered 9–14; the *Tech Debt Accumulated* report section removed; both anti-patterns replaced by their opposite.
- **Actual:** diff confirms all three. Step 9 gone, 10→9 … 15→14 with no gap and no duplicate. The report block's *Tech Debt Accumulated* section is deleted. Both anti-pattern lines (*Ignore TECH_DEBT.md items…*, *Ignore accumulated tech debt…*) are replaced by a single line prohibiting the opposite: treating a closed phase's §5 as a queue to inherit. Step 7's third bullet now reads *"Debt captured in REVIEW §5, and the disposition each item carries."*
- **Match:** ✅

### V10 — `.tfw/workflows/init.md`
- **RF claim:** no longer creates the file; Phase 4 items renumbered 4→3, 5→4, 6→5, 7→6.
- **Actual:** item 3 (`TECH_DEBT.md — empty or with initial entries if found`) deleted, remaining items renumbered exactly as claimed, no gap. The one surviving `tech debt` string at line 168 is a **research focus topic** for the init interview, not a registry instruction.
- **Match:** ✅

### V11 — `.tfw/workflows/update.md`
- **RF claim:** the never-overwrite list names *"any debt registry the project still keeps"* and states the obligation is withdrawn and nothing forbidden.
- **Actual:** line 75 reads exactly that. Correct posture — a receiving project's own file is project state and is never overwritten by an update.
- **Match:** ✅

### V12 — `.tfw/conventions.md`
- **RF claim:** §2 drops the required root artifact · §3 REVIEW definition · §8 workflow table ×2 · §10.4 uppercase list · §13 Trace Discipline gains the rule and the pointer · §14 one anti-pattern rewritten and three added · §15 Role Lock table.
- **Actual:** diff confirms all eight sites. §2's `TECH_DEBT.md` line deleted; §3's REVIEW definition now ends *"and a disposition on every debt item it captured"*; §8 rows for `review.md` and `docs.md` both updated; §10.4's uppercase reservation drops the filename; §13 gains a new paragraph naming the retirement and pointing at the snapshot; §14 rewrites the *Coordinator ignores executor Observations* line and adds three new anti-patterns (undisposed item / disposition naming nothing · registry reintroduced under another name · work left unfinished on the ground it can be logged); §15's Role Lock row for `docs.md` drops `TECH_DEBT.md`.
- **Match:** ✅

### V13 — `.tfw/glossary.md`
- **RF claim:** REVIEW and the two role entries updated; the live entry replaced by **Debt Registry *(retired at 2.1.0)*** and a new **Disposition** entry, both on the `Task Board (retired at 2.0.0)` pattern.
- **Actual:** the `### TECH_DEBT.md` entry is gone. Two new `##`-level entries sit immediately above `## Task Board *(retired at 2.0.0)*`, in the same shape. Executor and Reviewer role entries both updated; the Reviewer entry now reads *"Triages executor Observations into REVIEW §5 and disposes of every one before the task closes."* The retirement carries its date in both new entries.
- **Match:** ✅

### V14 — `.tfw/compilable_contract.md`
- **RF claim:** manifest row 9 deleted, 10–14 renumbered 9–13; the optional-source row dropped; `TD-{N}` → `tasks/DEBT-SNAPSHOT.md`; the nav tree and the *where references appear* list.
- **Actual:** all five. Row 9 deleted, rows renumbered with no gap; the `TECH_DEBT.md | Optional | WARNING, skip page` row removed from the existence-rules table; `TD-{N}` now resolves to the snapshot with an explicit note that it carries no manifest row because the task-container glob (now row 10) already compiles it; the nav tree drops `Tech Debt`; *Where references appear* drops the registry line **and corrects `REVIEW.md §3` to `§5`** — a pre-existing error fixed in passing (map.md deviation 6).
- **Match:** ✅

### V15 — `docs/scripts/gen_docs.py`
- **RF claim:** `TECH_DEBT.md` out of `STATIC_SOURCES`; the `TD-{N}` resolver points at the snapshot; the nav entry removed; `TECH_DEBT` dropped from the backtick-path alternation; row anchors follow the snapshot.
- **Actual:** all five, and each is a deletion or a retarget with no new mechanism. `add_table_anchors` now fires on `tasks/DEBT-SNAPSHOT.md` instead of `reference/tech-debt.md`, so `#td-59`-style hand-written anchors keep working — matching RF §2 decision 6. The `_replace_td` fallback URL is `/tasks/DEBT-SNAPSHOT/`. A two-line comment explains why there is no manifest row.
- **Match:** ✅

### V16 — `docs/scripts/test_gen_docs.py` · `docs/scripts/test_integration.py`
- **RF claim:** three assertions follow the new target; `test_td_refs_resolved_in_output` follows and gains a docstring; the integration test was **not in the TS** and would have failed.
- **Actual:** confirmed. `test_td_ref_resolved` asserts `/tasks/DEBT-SNAPSHOT/`; two `validate_sources` fixtures drop the file; `test_td_anchor`'s fixture text is reworded away from *"Some tech debt"*. `test_integration.py` asserts the new path and carries a docstring naming what it protects. The RF's claim that the old assertion **would have failed** is correct on inspection: it searched the built site for `/reference/tech-debt/`, which no longer exists (`ls site/reference/tech-debt` → no such directory).
- **Match:** ✅

### V17 — `.tfw/migrations/2.0.0.md` step 6
- **RF claim:** new step 6, old 6 and 7 → 7 and 8; the *order* preamble and *If it goes wrong* corrected; the guide no longer claims blanket additivity; all eight AC-7 points and all six AC-8 points met; **no command, script or check**.
- **Actual:** read the step end to end. Heading order confirmed: `5. Remove the board` → `6. Retire the debt registry` → `7. Declare who is acting` → `8. Ask the project whether it is consistent`, so the consistency check is still last. Against AC-7's eight points: goal/value/problem stated before any instruction ✅ · three steps and no fourth (seal · warn · stop) ✅ · sits at step 6 ✅ · destination named as `tasks/` outright, never derived from `tfw.task_containers` ✅ · header states **lines and words**, with an explicit paragraph on why a row count is meaningless across shapes ✅ · one procedure regardless of size, *"a full registry does not have to be cleaned up first to earn its retirement"* ✅ · *"Your registry is not forbidden. The obligation to maintain one is withdrawn"* ✅ · rollback stated, and correctly qualified as the **second** non-additive step ✅. **No command anywhere:** *"Move it however your project moves files; nothing here tells you which tool to use."* Against AC-8's six points: one class only, with release gate / open defect / roadmap item / self-flagged row explicitly sealed ✅ · *"Recognition is at heading level and nothing below a heading is read"* ✅ · asks, and seals on silence or a no ✅ · on a yes, **one** task under the current grammar with the goal written ✅ · invisible where no such heading exists ✅ · no second route ✅.
- **Match:** ✅ — this is the strongest artifact in the delivery.

### V18 — `.tfw/CHANGELOG.md` 2.1.0 entry
- **RF claim:** why, changed, removed, **13 retired wordings verbatim**, the condensed updating procedure, verification, known open.
- **Actual:** all seven sections present. Counted the *Retired wording, verbatim* list: **13 bullets**, several carrying two strings. Spot-checked three against the baseline: `` Append to project-level `TECH_DEBT.md` `` (`c153895:.tfw/workflows/review.md`), `` | 4 | New tech debt discovered? | `TECH_DEBT.md` | _(append)_ | `` (`docs.md`), and `| 9 | `TECH_DEBT.md` | `reference/tech-debt.md` | Copy + frontmatter |` (`compilable_contract.md`) — all three are literal, not paraphrased, which is what makes `update.md` Step 6's allowlist machinery able to fire (ONB Recommendation 3). The *Updating from 2.0.0* section carries the whole three-step procedure, the safety exception, the rollback and *"Nothing to run"* — followable without opening the migration guide, which is AC-7's fourth bullet.
- **Match:** ✅

### V19 — the three READMEs, `RELEASE.md`, `templates/RELEASE.md`
- **RF claim:** the root-artifact row removed from all three READMEs; English gains the snapshot in *where things live* with its date and mechanism; RU and KK gain a retirement note in each language carrying the date, the three outcomes and *nothing is forbidden*; both release checklists stop reading the registry.
- **Actual:** confirmed in all five files. The English README's new row carries `2026-09-02` and the mechanism. The RU and KK notes each carry the date, the three outcomes and the *nothing is forbidden* clause — checked semantically, not only structurally; the three languages agree. `RELEASE.md` and `.tfw/templates/RELEASE.md` both lose `- [ ] TECH_DEBT.md reviewed — no critical items blocking release`.
- **Match:** ✅

### V20 — `CLAUDE.md` and `.tfw/adapters/claude-code/CLAUDE.md.template`
- **RF claim:** the `/tfw-docs` row in both; nothing outside the `TFW:CLAUDE` markers; the template was **found in ONB, absent from the TS**.
- **Actual:** both files change exactly one table cell — *Update KNOWLEDGE.md and TECH_DEBT.md after REVIEW* → *Update KNOWLEDGE.md after REVIEW*. The `CLAUDE.md` diff touches nothing outside the block. This is the highest-value catch in the task and it is verified: without the template edit, the next `/tfw-update` would re-copy the retired wording back, which is DoF 4 with a delay fuse.
- **Match:** ✅

### V21 — `AGENTS.md` and `.tfw/adapters/codex/AGENTS.md.template`
- **RF claim (§2 decision 8):** not edited; neither ever named the registry, so AC-10's `TFW:CODEX` clause is satisfied by a no-op, stated rather than manufactured.
- **Actual:** `grep -i 'TECH_DEBT' AGENTS.md` → zero hits; neither file appears in `dfba46f`. The claim is true and the posture is right: manufacturing an edit to tick a checkbox is what the coordinator's ONB ruling 2 forbade.
- **Match:** ✅

### V22 — all 33 adapter copies, `cmp` against source
- **RF claim:** *"24 adapter copies `cmp`-verified byte-identical — 12 Claude commands, 12 Antigravity workflows and 11 Codex skills, of which exactly the 12 predicted changed."*
- **Actual:** I swept **every** copy, not a sample. `.claude/commands/` holds 12 files, `.agent/workflows/` 12, `.agents/skills/` 11. `tfw-task.md` has no `.tfw/workflows/` source in either set (it is a meta-workflow), leaving **33 comparable copies**. All 33 `cmp` byte-identical to their sources; **zero drift**. `git status` shows exactly the 12 predicted files modified. The `.agents/skills/tfw-review/SKILL.md` is a **pointer**, not a copy — it instructs the agent to read `.tfw/workflows/review.md` directly — so the Codex path carries no stale review text.
- **Match:** ✅ on substance, ⚠️ on arithmetic — see **D3**. The verified position is *stronger* than the RF claims: 33 copies checked, not 24.

### V23 — `.tfw/VERSION` · `.tfw/project_config.yaml` (AC-9)
- **RF claim:** 2.0.0 → 2.1.0; **no key added** — one value changed; `.tfw/scripts/` gained no script and no flag; maintained root artifacts 8 → 7.
- **Actual:** `cat .tfw/VERSION` → `2.1.0`. The config diff is a **single line**: `version: "2.0.0"` → `"2.1.0"`, comment unchanged. `git diff --name-only c153895..HEAD -- .tfw/scripts/` → **0 files**. Added files across the whole range: the snapshot (a rename, so net zero new content) plus this task's own trace artifacts. Root artifact census: `README.md`, `README.ru.md`, `README.kk.md`, `AGENTS.md`, `CLAUDE.md`, `KNOWLEDGE.md`, `RELEASE.md` — 7 maintained, down from 8. **Net −1 confirmed.**
- **Match:** ✅

### V24 — `KNOWLEDGE.md`
- **RF claim:** §1 Architecture Map gains a **Debt** component; §3 Legacy & Deprecation gains the retirement row.
- **Actual:** both present. The §1 row names the mechanism, the three outcomes, the existence test and the discovery search with its 243 measurement, and points at the four canonical sites plus the snapshot. The §3 row enumerates every retired surface individually, carries `2026-09-02 · TFW 2.1.0`, and links the RF. Well above the minimum the AC asks for.
- **Match:** ✅

### V25 — `workspace/00-INDEX.md`, `status.md`, journal
- **RF claim:** index regenerated (derived); `status.md` `TS_DRAFT → ONB → RF` with times read from the clock.
- **Actual:** `status.md` reads `lifecycle: RF`, `updated: 20260902-073517`. Journal holds five events in the `{stamp}__{kind}__{token}.md` grammar, ordered and consistent with the transitions. Index regenerates with unresolved inputs unchanged at 2.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | **315 passed, 1 skipped** in 219.4 s — identical to the RF's claim and to the ONB's pre-change baseline |
| 2 | `python .tfw/scripts/gen_index.py --check tasks` | **56 tasks validate**; 17 stateless phase directories, informational. Exit clean |
| 3 | `python .tfw/scripts/gen_index.py --check project` | *"project is consistent with the release it declares"*, framework version **2.1.0** |
| 4 | the `review.md` Step 5 search, verbatim | **243 rows** |
| 5 | `diff <(git show c153895:TECH_DEBT.md) <(tail -n 132 tasks/DEBT-SNAPSHOT.md)` | empty — byte-identical |
| 6 | `grep -rni 'TECH_DEBT'` over the AC-2 surface | **33 hits**, all historical |
| 7 | `cmp` across 33 adapter copies | **33/33 byte-identical** |
| 8 | `git diff --name-status -M c153895..HEAD` / `git show --numstat dfba46f` | 42 M · 1 R · 6 A; **702** changed lines excluding trace artifacts |
| 9 | `grep -rl 'DEBT-SNAPSHOT/">TD-' site --include=index.html \| wc -l` | **220** pages (RF says 219) |
| 10 | `ls site/reference/tech-debt` | no such directory — the old page is gone |
| 11 | `wc -lw` on three sibling registries; `grep -n '^#'` on each | matches the dry run exactly; no sibling file modified |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | *"the search returns **243 rows** on this corpus"* | RF §3 AC-3; `review.md` Step 5; CHANGELOG | Ran verbatim → 243 | ✅ |
| C2 | *"`diff` … is **empty**; `md5` matched before the header (`0bd3697…`)"* | RF §3 AC-1; EV E1 | `diff` empty; `git show c153895:TECH_DEBT.md \| md5sum` = `0bd36979416174709d11c2a6c6779504` | ✅ |
| C3 | *"33 hits, every one historical"* with a per-line table | RF §3 AC-2 | Re-run; 33 hits; every non-CHANGELOG hit read and classified correctly | ✅ |
| C4 | *"315 passed, 1 skipped — identical to the pre-change baseline"* | RF §4 | Re-ran the suite: 315 passed, 1 skipped. Baseline confirmed in ONB §2 | ✅ |
| C5 | *"`TD-209` disposed to `→ Phase B`, and amendment A8 dropped Phase B five days later"* — the gate's one real finding | RF §4; `disposition_walk.md` | `tasks/TFW-60…/phase-ac/REVIEW…` row TD-209 reads `→ Phase B`; no `phase-b/` directory exists under TFW-60; HL A8 dropped Phases B and C on 2026-08-30 (cited in this task's own HL Origin note) | ✅ |
| C6 | *"`--check project` … names adapter copies as something it does **not** verify"* | EV E10 | Ran it: *"not checked: … adapter copies against their sources …"* | ✅ |
| C7 | *"a `TD-N` citation opens `tasks/DEBT-SNAPSHOT.md` in a browser"* | RF §3 AC-6; EV E6; CHANGELOG | `site/tasks/DEBT-SNAPSHOT/index.html` exists; 220 built pages link to it; the screenshot shows the rendered snapshot page with its header text | ✅ |
| C8 | *"No file in any project other than this one was created, modified, moved or deleted"* (DoF 3) | RF; EV E12; `dry_run_receiving_projects.md` | All three sibling `TECH_DEBT.md` files present, mtimes 2026-04-25 / 2026-05-26 / 2026-08-04 — none touched. No `tasks/DEBT-SNAPSHOT.md` exists in any sibling | ✅ |
| C9 | *"the one project in the 25 carrying `## 🔴 Safety Rules (from incidents)`"* | RF §3 AC-8; EV E8 | `grep -n '^#' research-yandex-cloud/TECH_DEBT.md` → line 57 carries that exact heading | ✅ |
| C10 | *"24 adapter copies `cmp`-verified — 12 Claude commands, 12 Antigravity workflows and 11 Codex skills"* | RF §3 AC-10; EV E10 | 12 + 12 + 11 = 35 files, 33 with a source. The enumeration and the number **24** do not agree | ❌ arithmetic — see **D3**. Substance verified independently and is stronger |

## Discrepancies Found

> Escalated to **100% verification** on D1. All 43 file entries opened or diffed.

### D1 — the replacement search is corrupted when `review.md` is delivered through the Claude Code adapter *(new in this task)*

`.tfw/workflows/review.md:152` and its copy `.claude/commands/tfw-review.md:152` contain the awk field
reference `$0`, twice:

```awk
s && /^\| / && $0 !~ /^\| *(#|-)/ {print FILENAME": "$0}
```

`$0` is also Claude Code's slash-command argument placeholder. When `/tfw-review <path>` is invoked, the
harness substitutes it **before** the workflow text reaches the agent. In this review session, invoked as
`/tfw-review workspace\2026\TFW_20260830-194027_TLD\RF__TFW_20260830-194027_TLD.md`, the block arrived as:

```awk
s && /^\| / && workspace2026TFW_20260830-194027_TLDRF__TFW_20260830-194027_TLD.md !~ /^\| *(#|-)/ {print FILENAME": "workspace2026TFW_20260830-194027_TLDRF__TFW_20260830-194027_TLD.md}
```

Both occurrences replaced by the argument with its separators stripped. The result is not runnable, and it
fails silently in the sense that matters: it *looks* like a shell command. Invoked with no argument, `$0`
resolves empty and the awk program is a syntax error. Either way, **every** Claude Code invocation of
`/tfw-review` delivers a broken search.

- **New in this task.** `git show c153895:.tfw/workflows/review.md | grep -c '$[0-9]'` → **0**, and no
  workflow at the baseline carried a numeric `$N`. The pre-existing shell snippets in `config.md` and
  `update.md` use named variables (`$b`, `$rel`, `$f`), which the placeholder mechanism does not touch.
  `.claude/commands/tfw-task.md` uses `$ARGUMENTS` deliberately, which confirms the mechanism is live here.
- **Scope.** `.claude/commands/tfw-review.md` (confirmed, first-hand) and `.agent/workflows/tfw-review.md`
  (same string; the Antigravity substitution rules were not tested). The Codex path is unaffected — its
  skill is a pointer that sends the agent to read `.tfw/workflows/review.md` directly.
- **Why it matters.** AC-3 requires the search *"written out literally, so a reader can run it without
  inventing it"*, and HL DoF 5 fails the task if *"the canon states no operation by which open items can be
  listed"*. The canon states it correctly; the project's primary adapter mangles it on every delivery.
  This is the release's load-bearing deliverable failing at the point of use — and it failed here, in the
  first review conducted under the new rule.
- **Not the executor's process failure.** `cmp` fidelity is perfect and AC-10 is met as written: the copy
  *is* byte-identical. Nothing in the canon warns that `$N` collides with an adapter's placeholder syntax.
  The defect is real all the same, and it is in a file this task wrote.

### D2 — `+247%` is attributed to 17 days in the HL and 19 days in the CHANGELOG

HL §2.6 states *"+247% in 17 days"* over a table running 2026-08-13 (3 562 words) → 2026-08-31 (12 352).
The CHANGELOG's 2.1.0 entry states *"+247% in 19 days"*. The interval is 18 days to 2026-08-31 and 19 to
the CHANGELOG's own measurement date of 2026-09-01, so the shipped figure is defensible and the HL's is the
one that is off. Both are compiled to the published site. Not the executor's error — HL §2 is the
coordinator's free section — and the percentage itself is right in both.

### D3 — the RF and EV say *24* adapter copies where their own enumeration gives 35

*"24 adapter copies `cmp`-verified byte-identical — 12 Claude commands, 12 Antigravity workflows and 11
Codex skills"* does not add up. I swept all of them: **33 comparable copies** (35 files less the two
`tfw-task.md`, which have no `.tfw/workflows/` source), **all byte-identical, zero drift**. The claim is
understated, not overstated — the verified position is better than the reported one — but a number that
contradicts its own enumeration in a released artifact is a discrepancy and is recorded as one.

### D4 — `219` built pages carrying a resolved `TD-N` link, measured as `220`

RF §3 AC-6 and EV E6 say 219; the same grep on the current `site/` returns 220. One page. The site was
rebuilt between the RF and this review, and the snapshot's own page now carries such links. Immaterial to
the claim, which is that the citations resolve — and they do.

### D5 — the RF's file count is 41 modified where git records 42

The RF's own §1 table enumerates 42 rows and its budget line says 41. Well inside every ceiling (50 files /
50 modified) either way, so no stop-and-report was owed and none was skipped. Arithmetic only.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | AC-1 seal, inline transcript + header verbatim | ✅ inline in EV | ✅ — `diff` empty and `md5` reproduced independently; the header quoted in EV is the header in the file |
| E2 | AC-2 census → RF §3 table | ✅ RF §3 | ✅ — re-run: 33 hits, per-line classification accurate. TS assigns N/A here; the status was not chosen by the executor |
| E3 | AC-3 search, inline transcript | ✅ inline | ✅ — re-run verbatim, 243 rows |
| E4 | AC-4 → `evidence/disposition_walk.md` | ✅ 7 140 B | ✅ — ten items, each with the existence test applied; the `TD-209` finding independently confirmed (C5); the ceremony verdict is given in **both** directions with the uncomfortable number (6 of 10 `not material`) stated first rather than explained away |
| E5 | AC-5 reading pass → RF §3 | ✅ RF §3 | ✅ — post-change scan re-run; only the three prohibitions remain. TS assigns N/A |
| E6 | AC-6 → `td_citation_resolves_to_snapshot.png` + inline | ✅ 66 827 B | ✅ — opened the image: the snapshot page rendered, header text *"The rows were sealed unexamined…"* visible. It also visibly shows the frontmatter leak the RF records as O1, which corroborates that observation |
| E7 | AC-7 → `evidence/dry_run_receiving_projects.md` | ✅ 9 177 B | ✅ — read-only declaration is explicit and per-project; the measured shapes (129 L/3 509 W · 13 L/75 W · 75 L) match what I measured myself |
| E8 | AC-8 → same file §3 | ✅ | ✅ — the `## 🔴 Safety Rules (from incidents)` heading confirmed at line 57 of the named project's registry |
| E9 | AC-9 → the diff | ✅ | ✅ — config diff is one value; `.tfw/scripts/` untouched; root census 8 → 7. TS assigns N/A |
| E10 | AC-10 → inline `cmp` transcript + `--check project` | ✅ inline | ⚠️ — the **claim holds and is understated**: 33 copies verified, not 24 (D3). `--check project` output reproduced verbatim, including its *not checked* line |
| E11 | AC-11 → inline transcripts | ✅ inline | ✅ — all three commands re-run, all three match |
| E12 | DoF 3 → `dry_run_receiving_projects.md` read-only declaration | ✅ | ✅ — independently confirmed: three sibling registries present and untouched, mtimes months old, no snapshot created anywhere |

**Evidence verdict as declared:** 8/12 VERIFIED · 0 DEFERRED · 0 BLOCKED · 4 N/A. Every N/A is the status
**the TS itself assigns** to that AC (AC-2, AC-5, AC-9, and E5's synthetic reading pass) — checked against
the TS text; none was chosen by the executor to avoid work. This is the correct handling of the
*"Evidence: N/A"* challenge row in the Trust Protocol.

## Knowledge Citations Verified

> HL §7.2 carries 19 items. All 19 were checked for link resolution, item existence, semantic match and
> relevance. Priorities 0–4 were scanned in full; 5–7 by relevance, and all three were relevant.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | HL §7.2 #1 | PV 0 — `README.md` opening · § How It Works: inspectable continuity, not volume of record | ✅ | ✅ | ✅ — the README's own framing | ✅ — AC-6 keeps 1 659 citations resolving; the REVIEW stays the durable record |
| 2 | HL §7.2 #2 | PV 0 — `NS1 — Purpose`: *"not the production of more text or more process"* | ✅ `.tfw/README.md` L72–73, anchor `ns1` present | ✅ | ✅ | ✅ — AC-9's net −1 is the operative form |
| 3 | HL §7.2 #3 | PV 0 — `NS3 — Non-goals`: *"maximum-documentation bureaucracy… measures success by artifact count"* | ✅ L103–104, anchor `ns3` | ✅ | ✅ | ✅ — 77 unactioned rows are that non-goal, measured |
| 4 | HL §7.2 #4 | PV 1 — § Methodology values → **Structural Enforcement** | ✅ L91–92, anchor `methodology-values` | ✅ | ✅ | ✅ — and it is the citation that produced the highest-value catch: the adapter **template**, not the installed copy |
| 5 | HL §7.2 #5 | PV 1 — same → **Portability** | ✅ | ✅ | ✅ | ✅ — ordinary Markdown, and the search needs no tool |
| 6 | HL §7.2 #6 | PV 1 — `NS2 — Principles` 6, proportional assurance | ✅ L79–80, anchor `ns2` | ✅ | ✅ | ✅ — no row added to `judge.md`; row 3 rewritten |
| 7–10 | HL §7.2 #7–10 | PV 2 — `knowledge/philosophy.md` F45 (L52), F11 (L18), F40 (L47), F7 (L14) | ✅ | ✅ all four located by row | ✅ — F45 subtraction/artifact budget · F11 markdown *is* the graph · F40 bloat as terminology failure · F7 MVP closure | ✅ — F45 → the design target; F11 → no per-task debt file; F40 → *disposition* is the missing word; F7 → staging stayed out |
| 11–13 | HL §7.2 #11–13 | PV 3 — `KNOWLEDGE.md` D65 (L100), D53 (L88), D37 (L72) | ✅ | ✅ all three located | ✅ — D65 trace never reverted · D53 optional store used 0/38 → mandatory · D37 docs/knowledge write split | ✅ — D65 → rows preserved · D53 → the mirror case, cited exactly as a mirror and not as a precedent · D37 → `docs.md` loses its row without touching the split |
| 14–16 | HL §7.2 #14–16 | PV 4 — `conventions.md` §2 (L15), §14 firing-rate rule, §4 Discovery board pattern | ✅ | ✅ | ✅ | ✅ — §2 was the enforcement site and the line is gone; §14's rule is honoured by rewriting a row rather than adding one; the board pattern is followed down to the no-manifest-row shape |
| 17 | HL §7.2 #17 | PV 5 — `knowledge/convention.md` F1 (L8): adapter files are exact byte-copies, `cp` is the sync method | ✅ | ✅ | ✅ | ✅ — 33 copies `cmp`-verified, none hand-edited |
| 18 | HL §7.2 #18 | PV 6 — `knowledge/process.md` F30 (L37): capture without an enforcement site does not change behaviour | ✅ | ✅ | ✅ | ✅ — the disposition gate **is** the enforcement site the registry never had. The single most load-bearing citation in the HL, and it is exact |
| 19 | HL §7.2 #19 | PV 7 — `knowledge/constraint.md` F3 (L10): agents generate filler tech debt because template sections exist; quality filters mandatory | ✅ | ✅ | ✅ | ✅ — the filter existed and the file grew eightfold with it in force, which is why the section was removed rather than filtered harder |

**ONB §7** re-verifies the same 19 and adds three uncited items, each of which I checked: `update.md` Step 6's
allowlist machinery exists and keys on literal strings (which is why V18 matters); `judge.md`'s *Deferral
confession* test exists at the Purpose Check; `tasks/BOARD-SNAPSHOT.md`'s header carries the
*"In a shape no strict row parser matches: 9"* line that set the precedent for stating shape without
characterizing content. All three resolve and all three are relevant.

**No dangling citation. No semantic mismatch. No irrelevant application. Zero hallucinated references.**

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈43 × 0.42⌉ = 19 files and recorded findings? — **43 of 43, escalated to 100% on D1**
- [x] Ran at least 1 build/test command? — eleven, listed above, including the full suite
- [x] Claim & Source Checks filled — ten claims spot-checked, every citation traced, data claims checked against primary sources (`git show` at the baseline revision, the sibling trees, the built site)
- [x] Each RF §3 (AC) checkmark verified against actual file? — all eleven ACs
- [x] KNOWLEDGE.md checked — contradictions with changes documented? — none; §1 and §3 were updated by this task and agree with the delivery
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: **19** (+3 ONB additions), resolved: **22**, semantically verified: **22**, irrelevant: **0**, hallucinated: **0**
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: **12**, verified: **12** (one with an arithmetic caveat, D3), missing: **0**

Stage complete: **YES**
