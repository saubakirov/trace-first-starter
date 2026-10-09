# RES — TFW_20261004-174815_LPF: Lean Project Footprint

> **Current filename**: fixed `research/iter2/RES.md` under the selected task.

> **Date**: 2026-10-05
> **Author**: Claude Code — Researcher (`lpf-researcher`)
> **Status**: 🔬 RES — iteration 2 complete
> **Parent HL**: [HL-TFW_20261004-174815_LPF](../../HL-TFW_20261004-174815_LPF.md)
> **Mode**: Pipeline, focused
> **Producer unit**: `claude-code:agent:local_a7cf0ab7-482d-403e-b738-504d82bba898/lpf-researcher` = native agent `a2f09276b39617fd0` in Claude Code session `bd8d3d9f-d605-429a-a889-2c6d2bd03aa5` (same unit as iteration 1)
> **Parent Coordinator**: `claude-code:session:local_a7cf0ab7-482d-403e-b738-504d82bba898`
> **Activation / dispatch source**: delegated; continuation `/tfw-research TFW_20261004-174815_LPF`; `journal/20261004-233709__dispatch__2d7e.md @ b2ebb255`
> **Coordination authority**: `HL-TFW_20261004-174815_LPF.md @ efc915a9fa3e4366a3567be800d028ee011c916f`
> **Originating proposer**: `none`

---

## Research Context

Iteration 1 chose where working material lives, how evidence becomes a registry, and how the
comment rule handles docstrings. Iteration 2 closes the remaining decision inputs:
- **H3:** whether raw material is ever needed after acceptance.
- **H4:** whether most commits are habit.
- **H6:** whether Daily loses products under the new rule.
- **Subtraction:** what in the proposal can go without losing purpose, proof, boundary or needed
  freedom.

The Coordinator then asked for the exact words and places of every rule change, because the owner
wants to see them at the TS stop (HL §11 S10). That section, [Proposed wordings](#proposed-wordings--ts-input),
is the main output of this RES and the basis of the TS.

## Briefing

[`1_briefing.md`](1_briefing.md) (commit `588386e7`), answered by the Coordinator.

Stage files:
- [`2_gather.md`](2_gather.md) (`a5ff6efb`);
- [`3_extract.md`](3_extract.md) (`685af5b1`);
- [`4_challenge.md`](4_challenge.md) (`a1cfac43`).

Every stage gate carries the Coordinator's written ruling. The Challenge ruling is recorded in the
same commit as this RES.

## Decisions

Numbering continues from iteration 1 (D1–D12).

| # | Decision | Rationale |
|---|----------|-----------|
| D13 | **No raw material is kept after acceptance by default.** D7 item 5 (retention) leaves the rule text. A regulated class is named by its TS and kept in the project's own record system, or in VALUE when the record is the product. The HL's DoF 1 route stays the only retention path. | Five cross-task clusters. Only one used values that only raw bytes held: PTTC took them from CRATM's test transcript, and they were pytest summary lines that a row written at the time prints. For RVAG, kept bytes without their method proved nothing. CI deletes build output after 30–90 days. AS 1215 keeps the identification of the items examined, with copies only for significant contracts. The EU AI Act Article 19 logs belong to the system's own records (Gather G2–G4; Extract E1; Challenge C1) |
| D14 | **Commit reduction leaves this task** (M2). | 451 commits in five tasks; rules name 172; habit is 27–40%. Committing only at returns would cut the count 1.38–1.66×, not several-fold. Two rule-named kinds, ONB alone and the review map, fall between returns. Governance acts drive the count: 58 dispatches, 24 freezes, 27 landings. Crash recovery reads trees, and Codex snapshots a worktree before deleting it. Git refuses to remove a dirty worktree without force (Gather G5–G7; Extract E2; Challenge C7) |
| D15 | **Daily: the record lists every product with its project path, and the record folder holds only record and economics files before each orderly turn return.** An output with no evident place goes to an existing one the worker chooses. When none suits, the worker asks one consequential question, and "working material" is a valid answer. Working material lives under the system temporary `tfw/<folder ID>/` across turns. A worker continuing the record removes the leftovers it sees there, and the final turn removes the folder. No named home, no new folder, no product-list form. | Outputs without a link to an ordinary path sit beside the record in 16–21 of R3's 35 records and in 1 of R4's 4. A named home inside the record folder contradicts C4; a project-wide folder contradicts C8. Windows Storage Sense is off by default, so leftovers stay. The question reuses the skill's existing consequential-question hold (Extract E3; Challenge C5; Coordinator's Extract ruling) |
| D16 | **One self-contained root line carries C1 and C5 in every adapter root.** It goes inside the managed block for Codex and Claude and into the Rules list for Cursor and Antigravity. No new "Conduct" heading. The line states the rules and names their source headings; it does not point instead of stating. | Only the root reaches every role, Daily and ad-hoc sessions (Extract E4). Trial T1: update delivers a line inside the block and never one outside it; Claude's "Mandatory Rules" sit outside. `Context Selection` forbids adapter roots to preload shared files (Challenge C2) |
| D17 | **`Working material` and `Comments` are `###` subsections of `## 12) Safety and Execution Honesty`.** The Executor reads them before implementation (handoff Read Contract order 5), the Reviewer at Decide (review order 5). No Read Contract changes; `review.md` stays untouched. | A heading range includes its child headings, as `Anti-patterns (prohibited)` shows. This costs 0 words, against about 11 for separate subsections. Coordinator's Challenge ruling 2 (Challenge C3) |
| D18 | **The comment statement keeps C5's list of kinds and closes the loophole into names, strings and docstrings.** The root line keeps the positive form and a short "never as …" clause. `verify.md` lists added comments, docstrings and channel words. This reverses Extract E5.4. | Trial T2 on ECON's 416 added code and configuration lines: the comment listing needs no word list (7 lines, all of value). The names-and-strings listing does need it: its search words are the kinds, and a finding about an identifier must cite them. 34 such hits across all deliverable-6 code are TFW vocabulary or prose (Challenge C4) |
| D19 | **Working material holds no link into the project, and its removal follows no link.** D8's MAX_PATH rule stays dropped. | Codex issue #49995: on Windows, automatic worktree cleanup crossed a directory junction and deleted another repository's `.git` (Challenge C6) |
| D20 | **Subtraction result:** D2 and D8 leave the rule text. D3–D6, D7 items 1–3 with the attestation label, and D11 fold into existing sentences. The classification sentence becomes a clause in the TRACE row. The two anti-patterns fold into existing bullets. `review.md` leaves deliverable 3. `handoff.md` step 10's hand-over sentence is rewritten. The EV's per-row Environment column moves into "How". | Every item tested against purpose, proof, boundary and freedom; D2 and D8 protect nothing in rule text. Step 10 let working material outlive its creator and change hands. On simulated copies: `handoff.md` 1,118 → 1,116 words, `verify.md` 1,064 → 1,063, EV template 323 → 323 (Extract E5–E6; Challenge C8; [W4–W5](#w4-handoffmd-steps-8-10-and-11)) |
| D21 | **The duplicate Coordinator row is merged into one row of the eight Coordinator commands** in the Antigravity template (Coordinator's ruling). The Cursor template has the same duplicate since the same commit, ECON `1fafca12`; it is proposed for the same fix (Q13). This repository's installed Antigravity copy then follows the fixed template. | The manifest names eight Coordinator commands. Both templates list them in two rows, one ending in `/tfw-init`, the other in `/tfw-economics`. A plain sync would copy the duplicate (Challenge C2; this RES) |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q9 | Which docstring option? | open | Owner, at the TS stop (HL §4.1 reserve). W2.3 carries option A's clause until then |
| Q10 | Is `tools/migrations/2.0.0/` a historical folder under C7? | open | TS scope. Its script holds 102 of the 379 census lines in code and configuration ([W9](#w9-ts-only-content-not-rule-text)) |
| Q11 | Are attested claims acceptable for a given task? | open | Per TS, the owner's proportionality call |
| Q12 | Do `verify.md`, the EV template and the Daily skill count as "changed workflows" under DoD 3 and DoF 5? | open, Coordinator at TS | The wordings keep `handoff.md`, `verify.md` and the EV template at or below their baselines. The Daily skill grows 1,288 → 1,355, within DoD 4's 1,400. Recommendation: DoD 4 governs the skill, since a ceiling of its own would mean nothing if no growth were allowed. The TS names the counted files |
| Q13 | Does the Cursor template's duplicate row get the same fix as Antigravity's? | open, Coordinator | Recommendation: yes. The file changes anyway for the root line, and the fix only removes words. No Cursor copy is installed here |
| Q14 | Migration guide filename | open, TS | `migrations/<next version>.md` needs the release version, an owner reserve. A topic-named guide (`migrations/economics-core.md` and `knowledge-lifecycle.md` are precedents) avoids deciding the version inside this task |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H3 | After acceptance, raw material adds nothing a registry row cannot carry | open | ✅ holds | No cross-task case needed bytes that a row written at the time, or a re-run at the cited commit, would not give. One case shows bytes failing without their method (D13) |
| H4 | Most commits per task are habit; committing at role returns cuts them several-fold without harm | open | ❌ in its strong form | Habit is 27–40% of 451 commits; the projected cut is 1.38–1.66×. Two rule-named kinds fall between returns. By the HL's consequence, commit reduction leaves this task (D14) |
| H6 | The rule suffices for Daily without losing results | open | ❌ as stated; consequence applied without a named home | 16–21 of R3's 35 records and 1 of R4's 4 keep unlinked outputs beside the record. Every product is listed, an existing place is chosen or one question is asked, and the rest is working material (D15) |
| H1, H2, H5, H7 | — | iteration 1 | unchanged | iteration 1 RES |

## HL Update Recommendations

> **The researcher classifies, never applies or rules.** Each recommendation names its HL section.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R9 | §10 Hypotheses | H3 ✅, H4 ❌ in its strong form, H6 ❌ as stated with the consequence applied without a named home, with the evidence in the table above | this RES |
| R10 | §10 Blind Spots | Mark H3, H4 and H6 resolved. Remaining: receivers' configuration comments are uninspected; whether a given Daily output is a product or working material cannot be told without its content | Gather G9; Extract E3 |
| R11 | §2.1 Where the weight is | Add R3 at 2026-10-05: 35 records, 1,663 files, 268.5 MiB, of which 1,558 files (94%) are not the record, in 34 of 35 records. Add R4: 4 records, 1,339 files, 48.8 MiB. Replace the approximate commit counts with the census, noting that subject IDs missed unattributed commits: all refs 73/124/92/95/67 and unique patches 54/113/85/68/66 for CMTR/PCUX/RWNR/PTW/LFD | Gather G6, G9; Extract E3 |
| R12 | §2.2 What the rules say today | Add five facts. (a) `handoff.md` step 10 hands temporary resources to the Coordinator. (b) `review.md` has 1,562 words, above the 1,400 ceiling; DoD 3 forbids only growth. (c) The 3.8.1 guide already sends "requested PDF exports and temporary analysis scripts … outside the repository to OS temp". (d) The Cursor and Antigravity templates carry a duplicate Coordinator row since ECON `1fafca12`, and this repository's installed Antigravity copy lags its template. (e) Claude's "Mandatory Rules" sit outside its managed block, so update never changes them | Extract E5; Challenge C2; `migrations/3.8.1.md` §3 |
| R13 | §4 Phase A deliverables (free under HL Contract rule 6) | Deliverable 1: both subsections nested under §12; the classification sentence becomes a TRACE-row clause; the two anti-patterns fold into existing bullets; the Safety sentence is edited. Deliverable 3: `review.md` leaves it (ruling); `handoff.md` steps 8, 10 and 11. Deliverable 4: Daily skill §2 and §4, template §4. Deliverable 5: one line stating C1 and C5 inside the managed blocks and Rules lists, no Conduct heading; the duplicate Coordinator row merged in the Antigravity template (ruled) and, on Q13, the Cursor template; installed copies follow. Exact words: [Proposed wordings](#proposed-wordings--ts-input) | D16–D21 |
| R14 | §9 Risks | Update three rows. "Daily cleanup discards a product nobody linked": mitigation D15. "A reviewer needs raw material that was removed": add H3's evidence. "Agents move explanations into docstrings, long names …": mitigation D18 and the `verify.md` listing. Add three rows: removal of working material follows a link into the project, Low/High, D19; Daily temp leftovers stay on Windows, Medium/Low, D15; a receiver whose managed block has local edits gets no line until it resolves the drift, Medium/Medium, named in the migration guide. MAX_PATH row: the mitigation becomes "fails at once and visibly; no rule (D20)" | Challenge C2, C5, C6, C8 |
| R15 | §7.2 Knowledge Citations | Add a RES row citing `research/iter2/RES.md` (D13–D21 and the proposed wordings) as the ground of the TS | this RES |
| R16 | §8 Dependencies | Add: "Research iteration 2 (H3, H4, H6, subtraction)" ✅ | this RES |

### Amendment Proposals — frozen sections, resolved-ruler verdict required

**No amendment proposals.** Considered and not proposed:

| Considered | Why not |
|---|---|
| DoD 6 "the one-line Conduct pointer" | The line is a conduct rule that states C1 and C5 and names their headings, one line in all four templates; installed copies match the manifest after sync. Satisfied as written |
| DoD 3 and `review.md` (1,562 words) | Left untouched, it does not grow and already carries verification by repetition |
| DoD 1 "the two anti-patterns once each" | Folded into existing bullets, each is still stated once |
| C2 "no copies, however small" | Stays: Gather G3 found 198 byte copies across task evidence |
| DoF 1 retention route | Stays in the HL as a failure response; no rule text |
| C1 "referenced … only by its ID-relative name" | "A trace names at most `<temp>/tfw/<ID>/`" is compatible and stricter |
| DoF 5 against the Daily skill's growth | A TS classification (Q12), not a frozen change |

## Proposed wordings — TS input

> **Classification:** TS input, not an HL amendment (Coordinator's Challenge ruling). The owner sees
> these words and places at the TS stop (HL §11 S10).
>
> **Method:** every "before" text below was matched exactly once at `a1cfac43`, and every "after"
> text was applied to temporary copies of the files. Word counts are `wc -w` of those copies, the
> DoD 3 measure; passage counts are whitespace-separated tokens. The Executor may rewrap lines.

### W1. Root line: one per adapter, inside the updated block

The same text in all four templates (68 words, 432 bytes):

```text
**Working material and comments.** Keep raw output, logs, exports, screenshots and scratch
scripts in the system temporary directory under `tfw/<task or record ID>/`, never in the project,
and remove them when your work ends. A comment exists only when it carries value for its file's
reader or a program reads it, never as a note to agents, deferred work, history or an excuse
(`conventions.md` → `Working material`, `Comments`).
```

| Adapter | File | Place | Form | Words before → after |
|---|---|---|---|---|
| Claude Code | `.tfw/adapters/claude-code/CLAUDE.md.template` | inside `TFW:CLAUDE`, a new paragraph after "Version: see `.tfw/VERSION`." and before `### Command Routing` | paragraph | 787 → 855 |
| Codex | `.tfw/adapters/codex/AGENTS.md.template` | inside `TFW:CODEX`, a new paragraph after its first paragraph ("… The command must work without a wrapper.") and before the command table | paragraph | 627 → 695 |
| Cursor | `.tfw/adapters/cursor/tfw.mdc.template` | `## Rules`, a fourth bullet after "**Language.**" (continuation lines indented two spaces) | bullet | 512 → 571, with the row fix |
| Antigravity | `.tfw/adapters/antigravity/tfw-rules.md.template` | `## Rules`, a fourth bullet after "**Language.**" | bullet | 623 → 682, with the row fix |

The duplicate-row fix, in the Antigravity template (ruled) and the Cursor template (Q13):

```text
BEFORE
| `/tfw-plan`, `/tfw-docs`, `/tfw-knowledge`, `/tfw-release`, `/tfw-update`, `/tfw-config`, `/tfw-init` | Coordinator |
| `/tfw-plan`, `/tfw-docs`, `/tfw-knowledge`, `/tfw-release`, `/tfw-update`, `/tfw-config`, `/tfw-economics` | Coordinator |
AFTER
| `/tfw-plan`, `/tfw-docs`, `/tfw-knowledge`, `/tfw-release`, `/tfw-update`, `/tfw-config`, `/tfw-init`, `/tfw-economics` | Coordinator |
```

**This repository's installed copies after the sync:**
- `CLAUDE.md`: 825 → 893 words (6,052 → 6,486 bytes), project-owned text unchanged;
- `AGENTS.md`: 854 → 922 words (6,248 → 6,682 bytes), project-owned text unchanged;
- `.agents/rules/tfw.md`: 612 → 682, equal to the fixed template;
- no Cursor copy is installed.

Codex's default instruction limit is 32 KiB.

### W2. `conventions.md`

**W2.1 — `## 12) Safety and Execution Honesty`, bullet 3, second sentence** (11 → 11 words):

```text
BEFORE  VERIFIED status requires an artifact reference (file path or inline output).
AFTER   VERIFIED status requires the observed deciding values in the EV row.
```

**W2.2 — new `### Working material`**, nested under §12 after its bullets and before
`## 13) Trace Discipline` (130 words with the heading):

```text
### Working material

Working material is what a role makes for its own work and is neither result nor selected trace:
raw output, logs, exports, screenshots, archives, copies and helper scripts. The role that needs it
creates it in the system temporary directory of its own environment (`$TMPDIR`, else `/tmp`, on
POSIX; `%TEMP%` on Windows) under `tfw/<task or Daily record ID>/`, never in the project. It stays
private to that role: no other role relies on it, a trace names at most `<temp>/tfw/<ID>/`, it holds
no link into the project, and its removal follows no link. The creating role removes it when its
work ends, or names at its return what it keeps and why; `Closing and record recovery` step 6
removes what remains and records what it could not.
```

DoD 1 asks this subsection to name four things, which it does:
- the location for POSIX and Windows;
- the creator;
- the lifetime;
- `Closing and record recovery` step 6 as the removal point.

Each clause maps to an accepted decision: D1, D3, D4, D19 and C1.

**W2.3 — new `### Comments`**, after `Working material` (108 words with the heading):

```text
### Comments

In a value file — code, tests, configuration, prompts, templates — a comment exists only when it
carries value for that file's reader or a program reads it. Program-read comments are interpreter
and encoding lines, tool directives, license headers and TFW managed-block markers. Reader value
includes what a setting means, the instruction a template gives and, in a docstring a program
publishes, what the reader of that output needs. Comments are not a channel: no messages to other
agents, excuses, deferred-work notes, legacy chatter, jokes or notifications, and none of these
moves into names, strings or docstrings. The reason for a decision lives in the trace.
```

The docstring clause ("in a docstring a program publishes, what the reader of that output needs")
is option A. The owner's ruling (Q9) replaces it. The list of kinds is C5's own (D18).

**W2.4 — `### Evidence subfolder`, sentence 3** (22 → 38 words):

```text
BEFORE  Additional binary artifacts (screenshots, API responses, logs) go into the same `evidence/`
        folder and are indexed in the EV file's Attachments section.
AFTER   It holds nothing else — no attachments, binaries, logs, archives or copies, however small:
        each EV row carries what was verified, how (command or action and the Candidate commit or
        live target), what was observed and the result.
```

**W2.5 — `### Semantic value-bearing classification`, TRACE row** (+10 words):

```text
BEFORE  | `TRACE` | Lifecycle, decision, review, evidence, and log records | Never |
AFTER   | `TRACE` | Lifecycle, decision, review, evidence, and log records; raw run logs are working material, never in the repository | Never |
```

**W2.6 — `## 14) Anti-patterns (prohibited)`, two existing bullets extended** (+3 and +7 words):

```text
State and trace
BEFORE  - A per-user file is stored in the shared tree.
AFTER   - A per-user file or working material is stored in the shared tree.

Value and assurance
BEFORE  - Work is left unfinished because it can be called debt, or a parallel project/task debt
          registry is introduced.
AFTER   - Work is left unfinished because it can be called debt, a comment is used as a channel, or a
          parallel project/task debt registry is introduced.
```

`conventions.md` total: 15,764 → 16,038 words; no ceiling applies.

**Readers:**
- the Coordinator meets C2 and the TRACE clause in `plan.md`'s reads;
- the Executor and the Reviewer read both subsections inside §12;
- the Executor and the Researcher read the two folded bullets;
- every role, including Daily and ad-hoc work, reads the root line.

### W3. EV template (`.tfw/templates/evidence/EV.md`), 323 → 323 words

```text
Evidence section, first paragraph
BEFORE  Use only VERIFIED / DEFERRED / BLOCKED / N/A. Give VERIFIED a resolving artifact and explain
        every other result. Combine ACs only when one check resolves them.
AFTER   Use only VERIFIED / DEFERRED / BLOCKED / N/A, and explain every result other than VERIFIED.
        Combine ACs only when one check resolves them. A claim that cannot be repeated is attested:
        its row says why, how its values were captured and what the Reviewer checks instead.

Evidence section, second paragraph, opening
BEFORE  In the existing row or its resolving attachment, identify the claim's relevant input/output, …
AFTER   In the row, identify the claim's relevant input/output, …

Registry table: header and example row
BEFORE  | # | AC | What was verified | Environment | Result | Artifact |
        | E1 | AC-{N} | {observed result} | {specific environment} | {VERIFIED/DEFERRED/BLOCKED/N/A} | {path or inline output} |
AFTER   | # | AC | Verified | How | Observed | Result |
        | E1 | AC-{N} | {claim checked} | {command or action; Candidate or target; environment} | {deciding values, not raw output} | {VERIFIED/DEFERRED/BLOCKED/N/A} |

Accounting row: its description cell is unchanged; the last three cells are re-mapped
BEFORE  … exact NUL-safe method | {repo/Git/runtime} | {VERIFIED/DEFERRED/BLOCKED/N/A} | {command and result} |
AFTER   … exact NUL-safe method | {command; repo/Git/runtime} | {numbers} | {VERIFIED/DEFERRED/BLOCKED/N/A} |

Attachments section: deleted (heading, table and example row)
```

**What stays, and where each decision lands:**
- The Environment table at the top, the accounting row, the append-round rule ("later rounds
  append to this file"; "Preserve earlier rows; append later final-output observations …") and the
  Verdict section all stay, as DoD 2 requires.
- D6 lives in the "Observed" cell; D7 items 1–3 with the attestation label live in one sentence.
- D5, writing a row when its observation is made, lives in `handoff.md` step 8.

### W4. `handoff.md` steps 8, 10 and 11

| Step | Before | After | Words |
|---|---|---|---|
| 8 | `8. Run TS-required targeted/full checks. Reuse evidence only when inputs/output, oracle/authority and environment assumptions still apply; rerun changed or uncertain dependencies.` | `8. Emit the EV from its template. Run TS-required targeted/full checks, raw output in working material, each observation in its row when made. Reuse evidence only when inputs/output, oracle/authority and environment assumptions still apply; rerun changed or uncertain dependencies.` | 21 → 39 (+18) |
| 10, last sentence | `Identify exact task-owned temporary resources and their current owner/disposition for the Coordinator's later safe close.` | `Identify task-owned resources and owner/disposition for the Coordinator's safe close; remove your working material before returning, or name what you keep and why.` | 15 → 23 (+8) |
| 11, opening | `` 11. Open the EV template and emit `evidence/EV__{ID}.md` or `evidence/EV__phase-{x}__{phase_slug}.md`; append on return. Use only VERIFIED, DEFERRED, BLOCKED, N/A; each VERIFIED row resolves to evidence and every other row explains the gap. Add exactly one accounting row: `` | `11. Add Candidate to each EV row and exactly one accounting row:` | 37 → 12 (−25) |
| 11, closing | `… contract facts are BLOCKED; N/A means truly inapplicable. Summarize verdict counts.` | `… contract facts are BLOCKED; N/A means truly inapplicable.` | 11 → 8 (−3) |

**Whole file:** 1,118 → 1,116 words, within the 1,400 Design Rule; DoD 3 holds.

**Offsets.** The words removed from step 11 repeat the EV template, which the Executor now opens at
step 8:
- its status rule ("Use only VERIFIED / DEFERRED / BLOCKED / N/A … explain every result other than
  VERIFIED");
- "later rounds append to this file";
- its Verdict section.

The file names stay in the template's "Current filename" line and in `Evidence subfolder`
sentence 2.

**Fit with the Candidate:**
- Rows written at step 8 record the deciding values on the tree that step 10 commits.
- Step 11 adds the Candidate to each row and the accounting row.
- The EV is committed after the Candidate, as the accounting contract requires.

### W5. `verify.md`: the two check lines, 1,064 → 1,063 words

```text
Check 1 — `## Evidence Verification`, replacing its opening paragraph
BEFORE  Evidence applies to `{accepted subject, revision/Candidate, relevant environment,
        oracle/authority, dependency state}`. Changed dependencies or insufficient proof require an
        affected check; an enclosing SHA or unrelated record change does not invalidate adequate
        evidence.
AFTER   `evidence/` holds only EV files; no verdict rests on working material.

Check 2 — `## Commands Executed`, appended to its paragraph after "… this is not PASS."
AFTER   List comments, docstrings and channel words (`todo`, `legacy`, `old`, `temp`) the
        Candidate's VALUE diff adds; each must meet `conventions.md` → `Comments`.

Evidence Verification table: two header cells and one example cell
BEFORE  | # | RF evidence ref | Subject tuple | Artifact exists? | Establishes the claim? | Limit |
        | E1 | {evidence/file or inline ref} | …
AFTER   | # | EV row | Subject tuple | Repeated or opened? | Establishes the claim? | Limit |
        | E1 | {EV row ID} | …
```

**Offset.** The replaced paragraph repeats rules stated elsewhere:
- `review.md` Verify, which the Reviewer reads completely: "Evidence applies only to its
  `{accepted subject, revision/Candidate, relevant environment, oracle/authority, dependency
  state}`. Reuse adequate evidence; rerun changed, missing or uncertain dependencies …";
- the enclosing-SHA rule in `Closing and record recovery` step 2 and in the EV template.

The subject tuple also stays in this file's Verification Log and table. The Reviewer reads
`Working material` and `Comments` at Decide (ruling); the checks need no other read.

### W6. Daily skill and record template

```text
.tfw/extensions/daily-task/SKILL.md, section 2
BEFORE  Keep products at their ordinary project paths.
AFTER   Keep products at their ordinary project paths, giving an output with no evident place an
        existing one; ask only when none suits, and 'working material' is a valid answer.

.tfw/extensions/daily-task/SKILL.md, section 4, a new paragraph before the record update
AFTER   Before each orderly turn return, the record folder holds only record and economics files and
        the record lists every product with its project path. Working material stays under the
        system temporary `tfw/<folder ID>/`; a continuing worker removes leftovers it sees there,
        and the final turn removes it.
and in the next sentence
BEFORE  Update the selected local record with result paths, material decisions/revisions, …
AFTER   Update the selected local record with material decisions/revisions, …

.tfw/extensions/daily-task/templates/task.md, section 4, first sentence
BEFORE  Link the current product result at its ordinary path.
AFTER   Link every product at its ordinary project path.
```

**Counts:** the skill grows 1,288 → 1,355 words, within DoD 4's 1,400 (Q12); the template goes
477 → 476.

**Why these files count as the record:** "record and economics files" covers the three-file
task/brief/messages form the skill honours, the economics leaf and the copied quote basis. The
question reuses section 3's "Ask only for a missing consequential fact/choice/authority and hold
only its dependent action"; no new mechanism.

### W7. Deliverable 8 (decided in iteration 1: D12, R8)

```text
.tfw/workflows/knowledge.md, `## Canonical Knowledge Gate algorithm` (57 → 39 words)
BEFORE  **Retired historical destination.** Before TKL, this section defined the global pending/digest
        gate. Its original wording remains in Git object
        `ec91c56007c20cda79f740fec15c85e4af74d17c:.tfw/workflows/knowledge.md`, under this same
        heading. It no longer governs planning or qualification. Current work follows the selected
        handover, source, authority and incoming-relation checks above; this legacy link reinstates
        no task sweep, count, digest, processed marker or state write.
AFTER   **Retired historical destination.** This heading no longer governs planning or
        qualification. Current work follows the selected handover, source, authority and
        incoming-relation checks above; a link to this heading reinstates no task sweep, count,
        digest, processed marker or state write.

.tfw/adapters/antigravity/coordinator.md, the last paragraph (line 55) removed (−25 words)
BEFORE  Historical PCUX observations do not select a current task's topology, grant dialogue or
        change reporting; the current owner mandate and shared coordination contract govern them.
```

**Effect:**
- `knowledge.md` goes 1,120 → 1,102 words; the Antigravity profile goes 800 → 775.
- The heading stays as the target of old links.
- "this legacy link" pointed at the removed Git object; it becomes "a link to this heading".

### W8. Migration guide plan, the three answers and the receipt entry

**File:** `.tfw/migrations/<next version>.md`, or a topic name (Q14). It follows the 3.8.1 pattern.

**Plan of the guide:**
1. **Pin the source and follow the complete route.** Standard.
2. **What changes for new work,** adopted at the next authorized activation; frozen HL/TS and
   existing routes stay. The guide gives a "retired wording → successor" table:
   - the `Evidence subfolder` invitation to binaries becomes the registry and working material in
     temp;
   - the EV columns and Attachments section become "Verified · How · Observed · Result";
   - no comment rule becomes `Comments`;
   - Daily's product sentence gains the product listing and the clean record folder.
3. **Why comment correspondence harms,** in the owner's terms (C6):
   - it goes stale and starts contradicting the code;
   - it grows into a wall and a slow conversation between agents;
   - it lets an agent leave a note instead of finishing;
   - every later reader pays for it in tokens.
4. **The cleanup offer.** Update asks one material question, under update's rule to "ask one short
   material question only when evidence cannot settle … consequential choice": "Open a separate
   TFW task to remove comment correspondence from existing code?"
   - **Now:** after the update completes, the owner starts `/tfw-plan` for the cleanup task.
     Update itself edits no code (its Role Lock).
   - **Later:** recorded; the owner may start the task at any time. Nothing else is tracked: no
     registry (C8).
   - **Not at all:** recorded.
   - Whatever the answer, new agent writes follow `Working material` and `Comments`.
5. **What update never does.** It rewrites no receiver code, comment or history, and it moves or
   deletes no existing `evidence/` file, attachment, Daily record or leftover (DoF 4). A task in
   flight keeps what it has committed; its new rows follow the registry form.
6. **Root instructions.**
   - The line arrives inside the managed blocks (Codex, Claude) and with the copied rule files
     (Cursor, Antigravity).
   - A block with local edits is drift, and update refuses it (Step 4). Once the receiver resolves
     the drift, the line arrives.
   - A project's own rules outside the block, such as Claude's "Mandatory Rules", are never touched.
7. **Verify.**
   - Each selected adapter carries the line.
   - Block parity holds.
   - The receipt row is filled.

**The receipt entry.** It goes in `templates/update_receipt.md`, the §2 table, row
`Material questions`, whose form is `<none, or question → answer/route>`:

```text
| Material questions | Open a separate TFW task to remove comment correspondence from existing code (migrations/<file>.md §4)? → now: owner starts /tfw-plan cleanup task after this update / later / not at all — <answering human>, <time>; new agent writes follow Working material and Comments regardless |
```

**The `[Unreleased]` changelog entry (draft):**

```text
### Changed
- Working material — raw output, logs, exports, screenshots and scratch scripts — lives in the
  system temporary directory under `tfw/<ID>/`, private to the role that made it and removed when
  its work ends. `evidence/` holds only EV registry rows (verified · how · observed · result); the
  Attachments section is gone.
- A comment in a value file carries value for its reader or is read by a program; comments are not
  a channel between agents. Every adapter root states both rules in one line.
- Daily records list every product with its project path; the record folder holds only record and
  economics files before each orderly turn return.

### Fixed
- The Cursor and Antigravity rule templates list the Coordinator commands in one row.

See the migration guide for the optional comment cleanup.
```

### W9. TS-only content (not rule text)

**The Reviewer's listings for this task's Candidate** (D11, refined in iteration 1 C8 and here in C4).
First, the added comments in code and configuration:

```text
git diff -U0 <Baseline> <Candidate> -- <VALUE *.py *.js *.ts *.sh *.yaml *.yml *.toml> \
  | grep -E '^\+[^+]' | grep -E '^\+\s*(#|//|/\*|\*\s)|\s(#|//)\s|"""'
```

Second, Markdown: `<!--` only. Third, channel words as whole words in added lines:

```text
git diff -U0 <Baseline> <Candidate> -- <VALUE paths> | grep -E '^\+[^+]' \
  | grep -i -w -E '(legacy|deprecated|todo|fixme|hack|workaround|compat|old|temp|tmp)'
```

**DoD 7 census.** It runs over the deliverable-6 paths as written, split by type as in iteration 1:
`git grep -n -E '(^|\s)(#|//)|"""'` over the 14 code and configuration files, and `<!--` over the 2
Markdown files.
- Lines at `a1cfac43`: 379 in code and configuration (233 full-line comments, 110 docstring
  delimiter lines, the rest inline comments) and 0 in Markdown.
- `tools/migrations/2.0.0/migrate_board.py` holds 102 of the 379 (Q10).
- Challenge T2's 403 counted the whole `.tfw/economics/` folder; deliverable 6 names only
  `.tfw/economics/*.py`.

**The DoD 8 EV note:** "Working material: `<temp>/tfw/TFW_20261004-174815_LPF/`; removed at
<return>, or pending with its actor." It names no machine path.

**Docstrings (Q9):** option A (W2.3), C or D, in iteration 1's form; B is eliminated.

### Contact with frozen claims

| Wording | Frozen claim touched | How |
|---|---|---|
| W1 root line | C1, C5, DoD 6 | within: one conduct line in all four templates, stating the rules and naming their headings |
| W2.2 `Working material` | C1, DoD 1 | within: research selected temp (iteration 1); duties as C1 states them |
| W2.3 `Comments` | C5, DoD 1, DoD 10 | within: C5's own exceptions and kinds; the docstring clause awaits the owner |
| W2.4, W3 | C2, DoD 2 | within: registry columns; no Attachments; accounting row and append rule kept |
| W2.5, W2.6 | DoD 1 | within: anti-patterns stated once each, folded |
| W4 | C3, DoD 3 | within: 1,118 → 1,116 words |
| W5 | C3, C8, DoD 3 | within: the "two Reviewer checks in `verify.md`"; 1,064 → 1,063 words |
| W6 | C4, DoD 4 | within: 1,355 ≤ 1,400; DoF 5 reading in Q12 |
| W7 | C7, DoF 4 | within: live files, words decrease |
| W8 | C6, DoD 5 | within: three answers, receipt row named, new writes follow regardless |

## Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|

No fact candidates. No human input reached this iteration; every ruling came from the Coordinator,
and the counted facts are reproducible by command.

## Strategic Insights (Research)

No strategic insights. No human interaction occurred in this iteration's briefings.

## Findings Map

```
H3  did a later task need a closed task's raw bytes?
 ├─ 5 cross-task clusters; 1 used values only bytes held (PTTC <- CRATM pytest lines)
 ├─ RVAG: kept bytes without the method proved nothing
 └─ CI 30–90 days; AS 1215 keeps identification, copies only for a named class
       └──► D13  nothing kept by default; a regulated class is named by its TS
H4  are most commits habit?
 ├─ 451 commits; rules name 172; habit 27–40%; returns-only cut 1.38–1.66×
 ├─ ONB alone and review map: rule-named, between returns
 └─ recovery reads trees; Codex snapshots; Git refuses a dirty removal
       └──► D14  commit reduction leaves this task
H6  does Daily keep its products?
 ├─ R3: 94% of files are not the record; 16–21 of 35 records keep unlinked outputs; R4: 1 of 4
 ├─ a named home contradicts C4 (record folder) or C8 (new root)
 └─ Windows temp is not cleaned by default
       └──► D15  list every product; existing place, else one question; continuing worker cleans
Carriers and wording
 ├─ only the root reaches every role; update delivers inside the block only ──► D16
 ├─ §12 is read by Executor and Reviewer; child headings ride along ──────────► D17
 ├─ the names-and-strings listing needs the kinds as its anchor ──────────────► D18
 ├─ a cleanup crossed a junction (Codex #49995) ──────────────────────────────► D19
 └─ subtraction: 2 removed, 6 folded, review.md out; counts on copies ────────► D20, W1–W9
Defect found: duplicate Coordinator row (Cursor, Antigravity; ECON) ──────────► D21
```

## Iteration Status

- **Iteration:** 2 of 2 (min) / 3 (max)
- **Hypotheses tested:** H3 (✅), H4 (❌ in its strong form), H6 (❌ as stated, consequence applied)
- **Hypotheses deferred:** None
- **Gaps discovered:**
  - Trial T1 simulates update's written rule, not a native update run; receivers' blocks were not
    inspected, so their drift is unknown.
  - The heading-range reading of `Context Selection` is inferred from `Anti-patterns (prohibited)`,
    not stated in the rule.
  - Whether a given Daily output is a product or working material cannot be told without content.
  - Codex issue #49995 is a vendor report.
- **Superseded decisions:**
  - D7 item 5 by D13; D7 item 4 leaves the rule text and stays a TS matter; items 1–3 fold into W3.
  - D8 by D19 and D20.
  - Extract E5.4 by D18.
  - HL deliverable 1's classification sentence and separate anti-pattern items by W2.5 and W2.6.
  - HL deliverable 3's `review.md` part by D17 (ruling).
  - HL deliverable 5's "Conduct line pointing at C5" by D16.

### Open Threads (for next iteration)

No open threads. Q9–Q14 are TS decisions, not research.

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [ ] **MORE NEEDED** — {specify what and why}
- [ ] **BLOCKED** — {specify blocker}

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 2 tested retention, commit habit and Daily products, and put the whole proposal to the
subtraction test.

**What it settled.**
- **Retention:** raw material is not needed after acceptance.
- **Commits:** the count follows governance acts more than habit, so it leaves this task.
- **Daily:** it needs only two things: every product listed and the record folder clean. No new
  home.
- **Subtraction:** two decisions leave the rule text and six fold into existing sentences. One
  planned file, `review.md`, drops out.

**What research added beyond the plan:**
- a plain update would never deliver a root rule placed outside the managed block;
- the comment rule needs its list of kinds to stay checkable for names and strings;
- recursive cleanup can cross a link into the project;
- Windows keeps abandoned temp folders;
- two templates carry a duplicate row.

The proposed wordings were matched against the files and counted on copies. The owner can read
the exact words, and the DoD word limits are already checked.

**Self-critique.**
- I proposed dropping the list of kinds at Extract; the Challenge trial reversed that.
- My first census of deliverable 6 included the whole `.tfw/economics/` folder. W9 corrects it to
  the paths as written.
- The Daily skill grows by 67 words. I found no honest offset there without removing meaning, so
  the reading of DoF 5 goes to the TS (Q12) instead of being forced.
- H4's return points rest on role changes and path classes, an approximation.

### Material handover at this return

- **Producer / unit:** the Researcher named in the header; activation and dispatch as in the header.
- **Source / epoch:**
  - this repository from `b2ebb255` (dispatch) to the RES commit;
  - vendor and public pages read 2026-10-04 and 2026-10-05: GitHub Actions and GitLab retention,
    PCAOB AS 1215, EU AI Act Article 19, Git SubmittingPatches and git-worktree, GitHub large-file
    limits, Windows Storage Sense, Codex worktrees and issue #49995, the Claude Code and Codex
    instruction pages, PEP 8;
  - receivers R3 and R4 by aggregate counts only, under the Coordinator's permission.
- **Inspected scope:** as listed in each stage file (G12, E7, C9). For this RES, the exact
  target passages of W1–W8 and the economics contract and helper.
- **Material:** D13–D21; the proposed wordings W1–W9 with counts; the census numbers.
- **Uncertainty:** as under Gaps discovered.
- **Unresolved owner decisions:** the docstring ruling (Q9); the release version behind the guide's
  filename (Q14); per task, the acceptance of attested claims (Q11).
- **Knowledge publication:** none.
- **Working material of this iteration:**
  - census scripts with their JSON output, the update simulation and the wording simulation;
  - they sat in this session's temporary directory (Claude Code's session scratchpad inside the
    system temporary directory) under `tfw/TFW_20261004-174815_LPF/`;
  - removed at this return; nothing in the project points into it.
- **Continuation:** the Coordinator reviews this iteration through `/tfw-plan` and writes the TS
  from the proposed wordings.

**Economics contribution** (under `.tfw/economics/README.md`, Claude Code JSONL recipe):
- **File:** [`economics/researcher-iter2-20261005.jsonl`](../../economics/researcher-iter2-20261005.jsonl),
  2,699 bytes, SHA-256 `54c69fe259d78df18a6f2b527dbaef6e31126d421e7eb5cb32181db43c46d56e`.
  - It holds one manifest row and two daily usage rows, and passes `validate` together with
    revision 1.
- **Kind:** a disjoint contribution, revision 2, with no predecessor; it adds to revision 1 and does
  not replace it.
  - Revision 1 covers helper indices `[1, 969)`, this file `[969, 2083)`. The helper's indices are
    zero-based and end-exclusive: physical lines 970–2083.
  - The ranges touch without overlapping, and the binding was accepted as disjoint at the Briefing.
- **Source:** ID `bd8d3d9f-d605-429a-a889-2c6d2bd03aa5/a2f09276b39617fd0`; file
  `<session>/subagents/agent-a2f09276b39617fd0.jsonl`; version 2.1.286.
  - All 1,114 lines in the range belong to this unit.
  - Bound prefix: 8,522,971 bytes, SHA-256 `83e6309bf1b2a2df1612ffb903c0cb3085f5e0e3618ed59741e4b71fb4a2686b`.
- **Cutoff:** `2026-10-04T20:09:56.887992+00:00` (2026-10-05 01:09:56 +05:00); `complete: false`.
- **Measured:** model `claude-opus-5-5`, 216 native responses (59 on 2026-10-04 and 157 on
  2026-10-05, +05:00).
  - Input: 57,810,065 tokens, of which 56,472,380 were cache reads, 440 fresh input and 1,337,245
    five-minute cache writes.
  - Output: 478,185 tokens, of which reasoning was 321,215, a diagnostic subset not added twice.
  - Effort and native duration are unavailable in this source.
- **Tail after the cutoff:** this edit, the removal of working material, the RES commit and the
  return message. Disclosed once; it does not trigger recapture.

---

*RES — TFW_20261004-174815_LPF: Lean Project Footprint | 2026-10-05*
