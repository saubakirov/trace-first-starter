# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20261004-174815_LPF](../../HL-TFW_20261004-174815_LPF.md)
> Goal: A TFW project holds only the result and the selected trace: working material lives outside the project under the task ID and is gone when the task closes, and a comment carries value or is absent.
> Producer unit: `claude-code:agent:local_a7cf0ab7-482d-403e-b738-504d82bba898/lpf-researcher` (native agent `a2f09276b39617fd0`); mode focused, one pass. Repository state: HEAD `685af5b1`.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1 retention | nothing kept | D2 reader relies on | the original bytes | contradiction |
| D1 retention | fixed period, or until the next release | Git and DoF 4 | — | what is committed stays in history. A "30-day" window in a repository needs a history rewrite, which DoF 4 and the no-force-push rule forbid. CI can expire artifacts only because they live outside Git (C1) |
| D3 commit points | one per task, squashed at landing | G5 rules | Candidate, landing | squashing loses the Candidate and the landing commit |
| D5 home | a named place inside the record folder | C4 | — | only record files may sit in the record folder |
| D5 home | a project-wide products folder | C8 | — | no new root folder |
| Carrier | rules only in `conventions.md` (R-A) | the Read Contracts | — | no Read Contract reads a new section (Extract E4), so the rule reaches no role |
| Root line | a pointer to `conventions.md` | `Context Selection` | — | adapter roots "do not restate the workflow's algorithm or independently preload shared files" |
| C5 statement | without the list of kinds | D11 command 2 | — | the identifier and string check loses its anchor (C4) |

**Surviving configurations:**

| Group | Config | Notes |
|--------|------|-------|
| Retention | K1 and K2: nothing kept; the reader uses the row's values or a re-run at the commit | K4 remains only as the HL's DoF 1 route, with its home outside `evidence/` (C1) |
| Commit points | M2: outside this task | M6 recorded: governance acts drive the count |
| Daily products | P3 with the Coordinator's chooser rule | C5 adds two clauses, no mechanism |
| Rule carriers | R-C with both new subsections nested under §12 | C2, C3 |

**Unexpected survivors:**
- **Nesting under `Safety and Execution Honesty`.** Placing `Working material` and the comment
  statement as subsections of §12 makes the Executor read them before work and the Reviewer before
  its commit, with no word added to any Read Contract (C3).
- **The list of kinds.** Extract proposed to drop it from the C5 statement; it comes back, compact,
  because the loophole check depends on it (C4).
- **Leftover temporary folders under Daily on Windows.** The OS does not clean them by default, so a
  worker continuing a record removes the leftovers under that record's ID (C5).
- **A link clause.** Recursive removal can cross a link into the project; one clause in `Working
  material` closes it (C6).

## Findings

### C1: H3 — what would make "no retention by default" fail

- **Regulated work.**
  - AS 1215 keeps the audit record with the identification of examined items, and copies only of
    significant contracts (Gather G4).
  - EU AI Act Article 19 makes providers of high-risk systems keep the system's automatically
    generated logs for at least six months, enforceable from 2 August 2026. Those logs are product
    records of the receiver's system, held in its own record keeping.
  - TFW evidence is not that system. C2 forbids logs and attachments in `evidence/`, and C1 forbids
    keeping working material past the task. So a TS for regulated work names the retained class and
    its home: the project's own record system, or VALUE when the record is itself the product. No
    TFW rule text is needed for this.
- **A dispute after acceptance.** The row's command and commit allow a re-run. A live observation
  cannot be made again; its printed values are the record. The owner judged small screenshots
  useless (S2).
- **A long or one-off trial.** D7 items 1–3 cover it: why it cannot be repeated, the printed values
  and how they were captured, what the Reviewer checks instead. The claim rests on an attestation.
- **Cost on each side.**
  - Keeping: 298.7 MB of evidence, 91% of this repository's bytes (HL §2.1), and RWNR carrying
    TKL's dumps as an audit invariant.
  - Not keeping: one later use (PTTC), of values that summary-line rows carry.
- **Verdict.** K1 and K2 survive; K4 survives only as the DoF 1 route; K5 and K6 die (consistency
  check above).

### C2: Does update deliver the root line to existing receivers?

**Trial T1: a simulation of the written rule on temporary copies of this repository's
`CLAUDE.md`, `AGENTS.md` and templates.** The rule is update Step 4: "Apply exact copies or one
marker-bounded block; preserve unmarked/foreign neighbors … Reject … duplicate blocks or drift".

| Case | Result |
|---|---|
| Claude: line inside the managed block | delivered; project-owned text unchanged |
| Claude: line in the rule list outside the block | not delivered |
| Codex: line inside the managed block | delivered; project-owned text unchanged |
| A receiver that edited inside its block | drift: the written rule refuses, and the line arrives only after the drift is resolved |
| Cursor, Antigravity (`copy`) | the whole file is replaced, so the line arrives |

- **Init:** it says "Merge the managed TFW block into root `AGENTS.md`; never overwrite
  project-owned text". So the Claude rule list outside the block belongs to the project after
  installation and is never updated.
- **Reach:** the line reaches every new installation and every receiver that runs update without
  drift in its block. Receivers that never update get nothing, as they also never read the
  migration guide.
- **This repository's copies:**
  - the Claude and Codex blocks equal their templates;
  - the installed Antigravity rules file lags its template by one table row;
  - the Antigravity template itself has carried two Coordinator rows since ECON (`1fafca12`): one
    ends in `/tfw-init`, the other in `/tfw-economics`. A plain sync would copy the duplicate. DoD 6
    requires installed copies that match the manifest, so the Executor fixes the row first and then
    syncs. This is an existing defect outside this task's claims, found here.
- **Constraint:** `Context Selection` says "Skills and adapter roots dispatch commands and enforce
  only what must hold before a workflow can be opened. They do not restate the workflow's algorithm
  or independently preload shared files." The line must therefore be conduct, not procedure, and
  must state the rule itself; a pointer would contradict this rule.
- **Size:** Codex's default instruction limit is 32 KiB; the root files here are 4.5–6.2 KB, and a
  line of about 50 words adds about 0.35 KB.
- **Verdict:** R-C survives, with the line inside the block. The Claude "Mandatory Rules" list is
  not a carrier.

### C3: The second lever — which Read Contracts must name the source

A Read Contract addresses a heading as a range that includes its child headings.
`Anti-patterns (prohibited)` keeps all its content in `###` children, and `handoff.md` and
`research/base.md` read it by that one heading. So a `###` subsection under `## 12) Safety and
Execution Honesty` is read wherever §12 is read.

**Option N, nest both new subsections under §12:**

| Role that creates working material | When it reads the source | Words added to its workflow |
|---|---|---|
| Executor | Read Contract order 5, before implementation | 0; `handoff.md` stays at 1,118 of 1,400 |
| Reviewer | order 5, "Decide": after Verify, before its commit | 0. To read the source before Verify, +4 words at order 3, offset in `review.md` |
| Researcher | §12 is not in its Read Contract; it has the root line and the folded anti-pattern | 0. To read the source, +4 words at order 4, offset |
| Daily worker | reads no `conventions.md` heading; its skill states C4 and the temporary-folder clause inline | 0 |
| Coordinator | the rewritten `Evidence subfolder` sentence names working material; Closing step 6 already disposes of it | 0 |

`verify.md` has no Read Contract. Its new check line can name the subsection inside the line it
replaces: 0 net words.

**Option S, a separate subsection next to `Evidence subfolder`:**
- `handoff.md` +2 words ("`Working material`," at order 5). That makes 1,120 of 1,400, but DoD 3
  forbids growth, so the words are offset in the same file.
- `review.md` +2, offset; `review.md` then counts as a changed workflow.
- `research/base.md` +2.
- Daily skill +5 ("and `conventions.md` → `Working material`").
- In total about 11 words, each offset in its own file.

**Verdict:**
- Option N costs nothing and makes the Executor read the source before it creates working material.
- It fits §12's subject: what was run, and what counts as evidence.
- Neither heading name, `Working material` or a comment heading, is used anywhere in
  `conventions.md` or `glossary.md` today, so both stay unique.

### C4: The comment rule without the list of kinds

**Trial T2: the iteration-1 commands, rerun at HEAD.**
- **ECON diff `9e585cc1..1fafca12`, 416 added code and configuration lines:**
  - command 1, added comments: 7 lines, all of value — one docstring, two invariants, four
    setting explanations;
  - command 2, channel words as whole words: 0.
- **Deliverable-6 files, whole:**
  - command 3, the census: 403 lines, including the economics README's Markdown headings;
  - command 2: 46 lines, of which 34 lie outside comments.
  - The 34 are TFW vocabulary (the `TODO` status, the `legacy` identifier and event kinds),
    docstring and README prose, and one message the tool prints to its user. None is a note between
    agents.

**What the data shows.**
- **Command 1 needs no word list.** It lists every added comment, and the Reviewer judges each one
  against "value for the file's reader, or read by a program". Comments stay checkable without the
  list.
- **Command 2 needs the list.** It is the only listed check that shows explanations moved into names
  and strings, the loophole iteration 1 named. Its words (legacy, deprecated, todo, fixme, hack,
  workaround, compat, old, temp, tmp) are the kinds turned into search terms.
- **Without the kinds in the rule,** that check has no anchor, and a finding about an identifier
  cites nothing. The rule could not reveal that violation, so for names and strings it would be only
  advice.

**Verdict: reverse Extract E5.4 for the `conventions.md` statement.**
- Keep a compact list of about 12 words: notes to other agents, deferred work, history or legacy,
  excuses.
- Name the loophole: these do not move into names, strings or docstrings.
- The root line can keep the positive form plus "never a channel".
- Cost: about 20 words in `conventions.md`, which has no word ceiling; no workflow grows.
- False positives stay cheap: 34 identifier and string hits across all deliverable-6 code, each
  judged at a glance.

### C5: Daily over several turns

**The skill already runs records over several turns.**
- "Continue an existing record only when this request revises the same bounded deliverable."
- Economics snapshots come "before each orderly turn return".
- In this repository, one of five records ran over many turns: 16 dated or turn headings and 6
  snapshot mentions.

**Three failure paths while the temporary folder lives between turns:**

1. **Loss between turns.** macOS removes temporary files left unaccessed for 3 days; Linux after 10
   days or a reboot (iteration 1). A tool may also set its own temporary directory per session.
   - This is harmless if every output the person may accept is a product at its path, listed in the
     record at each turn return (C4 and P3).
   - What the person saw only in chat can be generated again.
2. **Leftovers.** Windows Storage Sense is off by default, and when on it deletes "temporary files
   that my apps aren't using". So an abandoned Daily leaves its folder in place indefinitely, and
   Daily has no Closing step 6.
   - The harm is disk space and privacy, outside the project.
   - Mitigation within D4's own wording: the worker that continues a record removes the leftovers
     it can see under that record's ID; the final turn removes the folder.
3. **Two agents sharing material.** This repository's only non-record Daily file is a 417-line
   Claude–Codex correspondence channel. Under D3 nothing passes between roles, and tools' temporary
   folders differ, so such a channel has no home. That is by design: agents exchange addressed
   messages, and the record keeps the selected outcome (NS2.4).

**The chooser rule (Coordinator's ruling).** The worker picks an existing place and records its
path. One question goes to the person only when no place exists, and the answer may be "working
material". It uses the skill's existing consequential question with a hold, so it adds no mechanism
and stays inside C4 and C8.

**Verdict:** P3 holds over several turns with two clauses and no new mechanism:
- products are listed at each turn return;
- a continuing worker removes leftovers under the record's ID.

### C6: Removal can cross a link into the project

- Codex issue #49995 (Windows): automatic worktree cleanup crossed a directory junction and deleted
  another repository's `.git`, `.gitignore` and `.gitattributes`.
- The same mechanism applies when a role removes its temporary folder. If working material contains
  a junction or symlink into the project, an easy way to "cite instead of copy", a recursive delete
  can reach project files. The harm is DoF 4's: deleted records.
- **Verdict:** `Working material` needs one clause: working material links to nothing in the
  project, and its removal does not follow links. This is D8's useful remainder in a new form; D8's
  MAX_PATH reason stays dropped.

### C7: H4 — does anything in this task depend on fewer commits?

- No deliverable changes a commit rule, and no DoD or DoF item counts commits.
- **Crash recovery does not need role-made intermediate commits:**
  - Codex keeps its 15 most recent managed worktrees and saves a snapshot of the work, including
    uncommitted changes, before deleting one. Such "Codex worktree snapshot" commits appear in PTW's
    history.
  - Git removes only clean worktrees unless forced: "Only clean worktrees … can be removed".
- **A shared working tree** is protected by exact-path staging, not by commit frequency.
- **Verdict:** M2 survives. Commit reduction leaves this task; nothing here assumes it.

### C8: Subtraction — what returns if each removal is wrong (NS2.2)

| Removal or fold | Failure that would return | What would show it | Verdict |
|---|---|---|---|
| D2 out of rule text | none | — | stays out |
| D8 as a MAX_PATH rule | a long path fails at once in temp | the failing command | stays out; C6 keeps the link clause |
| D5 folded into `handoff.md` steps 8 and 11 | an unrepeatable observation lost if the reorder is missed | the anti-pattern "Evidence is reconstructed after the fact"; the Reviewer at Verify | stays folded |
| D6 into the EV column header | the EV turns into a dump | `verify.md`: the Reviewer sees size and content | stays folded |
| D7 items 4 and 5 dropped | proportionality or retention unstated | NS2.7; the HL's DoF 1 route | stays dropped |
| `review.md` out of deliverable 3 | a Reviewer relies on raw files | Verify already asks to rerun; the column "Repeated or opened?" | stays out |
| The list of kinds dropped (E5.4) | the names-and-strings check loses its anchor | C4 | **reversed: keep a compact list** |
| The root line as a pointer | it contradicts `Context Selection` | C2 | stays dropped |
| The "Conduct" heading | none | — | stays dropped |
| The classification sentence | "log records" read as run logs | the clarified TRACE row | stays dropped; clarify the row |
| Separate anti-pattern bullets | Executors and Researchers lose the line | the folded bullets in their Read Contracts | stays folded |

Inspectability and continuation keep their carriers:
- the registry row still says what was verified, how, what was observed and the result;
- products stay at their paths, listed in the record;
- no removal touches either carrier.

### C9: Queries, files and trials

**Web:** 4 calls.
- Searches: Windows Storage Sense; EU AI Act Article 19; Codex app worktrees.
- Fetch: the git-worktree documentation.

**Trials** (working material in the system temporary directory under this task's ID):
- T1: the update rule simulated on temporary copies of this repository's root files and templates;
- T2: the iteration-1 commands on the ECON diff and the deliverable-6 files;
- T3: turn markers and commits in this repository's five Daily records.

**Files:**
- the Read Contract tables of `review.md`, `handoff.md`, `research/base.md` and `plan.md`;
- `conventions.md`: `Context Selection` and the heading levels of `Anti-patterns (prohibited)`;
- update Step 4; `init.md` lines 156–185, by grep;
- block parity of the installed copies, by script;
- the history of the Antigravity template and its installed copy.

No receiver file was opened in this stage.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| H3: no retention by default survives regulated work, disputes and long trials. A regulated class is named by its TS and lives in the project's own record system | — |
| Carrier: update delivers a line inside the managed block and never one outside it; a receiver with drift gets it after resolving the drift. The Antigravity template has a duplicate row to fix before syncing | RES: classify the duplicate row (existing defect) |
| Second lever: nesting both subsections under §12 costs 0 words; naming them separately costs about 11 words, each offset | — |
| Comment rule: comments stay checkable without the list; names and strings do not. Keep a compact list and name the loophole (E5.4 reversed) | — |
| Daily over several turns holds with two clauses: products listed at each turn return; a continuing worker removes leftovers | — |
| Removal must not follow links (Codex #49995) | — |
| H4: nothing in this task depends on fewer commits | — |

**Sufficiency:**
- [x] External source used? 3 searches, 1 fetch
- [x] Briefing gap closed? H3, H4, H6 and the subtraction challenge are tested; the Coordinator's three tests are answered
- [x] Pairwise incompatibility checked? Surviving configurations listed? Yes, above

**Knowledge handover.**
- **Material:** C1–C8.
- **Inspected scope:** C9.
- **Uncertainty:**
  - T1 simulates the written update rule, not a native update run;
  - receivers' blocks were not inspected, so their drift is unknown;
  - the heading-range reading of `Context Selection` is inferred from `Anti-patterns (prohibited)`,
    not stated in the rule;
  - Codex issue #49995 is a vendor report.
- **Knowledge publication:** none.
- **Continuation:** on the Coordinator's answer, the RES.

Stage complete: YES
→ User decision: Coordinator's ruling (addressed message, 2026-10-05): Challenge closed; go to RES.
1. **The duplicate Coordinator row in the Antigravity template** is fixed in this task under
   deliverable 5: the template and the installed copies change anyway, and the row is a defect. Only
   this row changes in that file. RES records it as a refinement of the deliverable list (free under
   rule 6), not as an amendment.
2. **The Reviewer reads the working-material rule at Decide**, with no change to `review.md`. The two
   checks stand in `verify.md`, which it opens during Verify; that is enough.
3. **Accepted:**
   - the short list of forbidden kinds returns: checkability rests on it, and it forbids moving
     into names, strings and docstrings;
   - working material links to nothing in the project, and its removal follows no link;
   - a Daily worker continuing a record removes visible leftovers under the record's ID;
   - both subsections sit inside `Safety and Execution Honesty`.
4. **RES adds a separate section of proposed wordings:** the exact text and place of every rule
   change.
   - The places: the root line (one per adapter, inside the updated block), the two `conventions.md`
     subsections, the `Evidence subfolder` sentence, the classification line, the prohibition item
     and the EV template columns.
   - Also: `handoff.md` steps 8, 10 and 11 with word counts, the two `verify.md` lines, the Daily
     skill sentences and record template, and the migration-guide plan with the three answers and
     the receipt entry.
   - The owner wants these words and places at the TS stop; the section is TS input, not an HL
     amendment.
5. **Before returning,** validate and attach the economics for the new range (revision or disjoint
   contribution, file, hash, cutoff). Stop after RES.
