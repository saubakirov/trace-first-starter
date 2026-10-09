# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20261004-174815_LPF](../../HL-TFW_20261004-174815_LPF.md)
> Goal: A TFW project holds only the result and the selected trace: working material lives outside the project under the task ID and is gone when the task closes, and a comment carries value or is absent.
> Producer unit: `claude-code:agent:local_a7cf0ab7-482d-403e-b738-504d82bba898/lpf-researcher` (native agent `a2f09276b39617fd0`); mode focused, one pass. Repository state: HEAD `a5ff6efb`.

## Configuration Space

Gather's dimensions D1–D7 form three groups below. D8 is applied item by item in E6. A fourth
group, rule carriers, appeared in this stage (E4).

### Retention after acceptance (D1 × D2)

| Config | D1 Raw material after acceptance | D2 What a later reader relies on |
|--------|-----------------|-----------------|
| K1 | nothing kept | the values the EV row printed |
| K2 | nothing kept | a re-run at the cited commit |
| K3 | nothing kept | RF and REVIEW statements |
| K4 | items the TS names are kept | bytes for the named items, the row for every other claim |
| K5 | kept for a fixed period (30–90 days) | bytes inside the period, the row after it |
| K6 | kept until the next release | bytes until the release, the row after it |

"Nothing kept" with "the original bytes" contradicts itself and is left out.

### Commit points (D3 × D4)

| Config | D3 Commit points | D4 Where the count is settled |
|--------|-----------------|-----------------|
| M1 | after every step | nowhere (today's practice) |
| M2 | at role returns, plus the ordered commits a rule requires there | outside this task (H4's consequence) |
| M3 | as M2 | a rule sentence in this task |
| M4 | one per role per round | the agreed separate cleanup task |
| M5 | one per task, squashed at landing | outside this task |
| M6 | as today | fewer governance acts (re-freezes, dispatches); no commit rule at all |

- M5 contradicts G5: squashing loses the Candidate and the landing commit.
- M6 was not in the Briefing.

### Daily products (D5 × D6 × D7)

| Config | D5 Home of an output with no ordinary path | D6 What the record says | D7 When working material goes |
|--------|-----------------|-----------------|-----------------|
| P1 | an ordinary path the worker picks | the result only (today's template) | before each orderly turn return |
| P2 | an ordinary path the worker picks | every product it leaves | before each orderly turn return |
| P3 | an existing place the project chooses, or none: then it is working material | every product it leaves, each with its path | the record folder is clean before each turn return; the temporary folder goes when the Daily work ends |
| P4 | a named place inside the record folder | an explicit product list | before each orderly turn return |
| P5 | not kept: everything beyond the result is working material | the result section only | at the record's close |
| P6 | a project-wide products folder | an explicit product list | at the record's close |

- P4 contradicts C4: only record files may sit in the record folder.
- P6 contradicts C8: no new root folder.
- P3 was not in the Briefing. It separates C4's "record folder clean before each return" from D4's
  "temporary folder removed when the work ends".

### Rule carriers (new in this stage, E4)

| Config | Where each new rule sentence lives |
|--------|-----------------|
| R-A | in `conventions.md` sections only, as deliverable 1 plans |
| R-B | in `conventions.md` and inline in every workflow that acts on it |
| R-C | in `conventions.md` as the authority, plus the root line every session loads, plus the template each role opens |

R-C was not proposed for C1: the root line planned for C5 (DoD 6) can carry C1 as well.

## Findings

### E1: H3 — every cross-task case judged

| Case (G2, G3) | Verdict | Reason |
|---|---|---|
| CRUE field analysis cited from `KNOWLEDGE.md` | the row sufficed | the statement stands in CRUE's EV and `verify.md`; the note itself is analysis that C2 sends to RF or to EV rows |
| CRATM release-package note cited from `KNOWLEDGE.md` | the row sufficed | in CRATM's RF, EV and `verify.md` |
| PTTC took durations and counts from CRATM's raw test transcript | a timely row would have sufficed | every figure is a pytest summary line; a row per run, written at the time (D5) with its deciding values (D6), prints it. The failed run's cause is rework, which RF records. The suite re-runs at the CRATM commit |
| RWNR carried five TKL blobs as a landing invariant | nothing was needed | identity only, a burden that disappears under C2 |
| PCUX cited the FRATS provider note | the row sufficed | in FRATS's RF, REVIEW, `verify.md` and phase B EV |
| TKL printed SLC files as trial input | nothing from evidence was needed | the trial needed "an accepted effect". 15 of the 21 copies were SLC trace documents, which stay under C2 |
| RVAG on FRATS's kept replay output | the bytes failed | without the command and predicates the output proved nothing. The "how" of a row is what makes it checkable |

**Decision.**
- **H3 holds.** No case needed bytes that a row written at the time, or a re-run at the cited
  commit, would not give.
- **D7 item 5 leaves the rule text.** TS-named retention is not needed by default. Retention stays
  available only as the HL's DoF 1 failure route, which the frozen HL already states.
- **External pattern (G4).** CI deletes build output after 30–90 days. Audit keeps the record, with
  the identification of what was examined, and copies only for a named class. TFW's data never needed
  such a class; the TS of a regulated task can still name one under DoF 1.

### E2: H4 — commit kinds, harm if merged, decision

| Kind | Commits in 5 tasks | Named by | What it protects | Harm if merged into the return commit | Disposition |
|---|---:|---|---|---|---|
| Dispatch | 58 | role headers: "immutable dispatch ref" | the unit cites a fixed source | none, if other Coordinator writes at that point ride in it; the commit must exist before the unit starts | required at the hand-off |
| Landing | 27 | `Landing a deliverable across sessions` | producer attribution; Candidate reachability | attribution lost | required, separate |
| Freeze | 24 | HL rules 13–14 | a verifiable baseline | the baseline cannot be checked | required |
| Status binding | 21 | HL rule 16; `coordination_selected`; event template | a status can cite only an existing SHA | impossible: a commit cannot cite itself | required, after the cited commit |
| ONB alone | 18 | `handoff.md` step 4 | ONB visibly precedes implementation | the order cannot be checked | required; falls between returns when no blocker stops the Executor |
| Candidate | 14 | `handoff.md` step 10; TS, REVIEW and `verify.md` templates | the identity of the accepted result | identity lost | required, before traces |
| Review map | 10 | `review.md` Step 1 | the selection is fixed before results | selection after results becomes possible | required; falls between returns when the Reviewer does not stop |

Habit commits, 180 in the strict count of G6:

| Habit group | Commits |
|---|---:|
| Coordinator HL and TS edits between freezes | 35 |
| Coordinator event-only commits (gate rulings, records) | 31 |
| Reviewer `verify.md`, `judge.md` and REVIEW commits before its final status commit | 30 |
| Executor status, event or trace commits split from ONB, Candidate or RF | 26 |
| Coordinator REVIEW-side records (acceptance, capture, cleanup notes) | 25 |
| Coordinator status or `iterations.yaml` updates | 13 |
| Coordinator product, changelog or knowledge writes | 12 |
| Executor extra VALUE commits, economics receipts, other | 8 |

- No rule or recovery path reads any habit group.
- The dead-run path reads the tree as well as the commits. An intermediate commit therefore protects
  a dead run only when its tree is lost; Challenge tests that case.

**Decision.**
- **H4 is false in its strong form.** Habit is a minority (27–40%). Committing at returns would cut
  commits 1.38–1.66×, not several-fold.
- **H4's false case holds for two kinds.** ONB alone and the review map are rule-named commits that
  fall between returns when no stop follows.
- **Governance acts drive the count** (58 dispatches, 24 freezes, 27 landings), not commit habit
  (M6).
- **By the HL, commit reduction leaves this task.** The habit groups above are the input if the
  agreed separate task or a later one takes it up.

### E3: H6 — product kinds, homes, links and returns

**R3 narrowed (fact c), counted 2026-10-05.**
- 19 of 35 records link a project file that changed in Git after the record was created; 14 of 35
  within 24 hours.
- Crossed with fact (b):
  - 16 records (any time) or 21 (within 24 hours) hold files other than the record and link no
    project file changed after the record began;
  - 18 records do both (any time);
  - 1 links such a file and holds nothing else.
- So 16 to 21 records keep their outputs only beside the record, or link none.

**R4, counts only, same rules.** Its record form is a single `task.md`.
- **Size:** 4 records, 1,339 files, 48.8 MiB. Files per record range from 19 to 1,148 (median 86);
  1,335 files are not the record.
- **By type:** JSON 864 (43.1 MiB), Markdown 218 (2.6), Python 125 (1.0), TXT 50, JSONL 40 (1.1),
  compiled Python cache 14, PowerShell 13, YAML 6, RSC 2, XML 2, JPG 2, PNG 2, PUB 1.
- **Facts:**
  - fact (b): 4 of 4;
  - fact (a): 3 of 4 link a project file at an ordinary path, all three from the result or closing
    section;
  - fact (c): 3 of 4 any time, 2 of 4 within 24 hours.
- One record holds other files and links no changed project file.

Output kinds beside the record (number of records containing each kind):

| Kind | R3 | R4 | An ordinary place for it in a typical project? |
|---|---|---|---|
| Images: PNG 19, SVG 7, WEBP 4, JPG 3, GIF 1 | up to 19 | 2 | sometimes (documentation assets); often a one-off view |
| Documents: PDF 13, DOCX 4, XLSX 2, XLS 1, ICS 1, CSV 1 | up to 13 | — | sometimes, in a place the project owns |
| HTML previews and small web builds: HTML 18, JS 2, MJS 3, CJS 2, CSS 1, fonts 2; nested Git control files in 2 | up to 18 | — | rarely; a few records hold a whole small project |
| Video: WEBM 1 (18 files), MP4 1 | 1–2 | — | rarely |
| Scripts: Python 18, PowerShell 3 | 18 | 3 | yes, when reusable (tools); otherwise working material |
| Data exports: JSON 15, TXT 5, JSONL 1 | 15 | 4 | yes, when the data is the product; otherwise working material |
| Archives: ZIP 5 | 5 | — | rarely; usually a copy |
| Compiled cache (PYC) | 3 | 1 | never: pure working material |
| Notes beyond the record files (Markdown) | 32 | 3 | sometimes |

**Decision.**
- **H6 is false as stated.** Outputs without a link to an ordinary path sit beside the record in
  16–21 of R3's 35 records and in 1 of R4's 4. They are one-off charts, previews, documents, videos,
  exports and small builds, as H6's false case foresaw. Whether a given file is a product or working
  material cannot be told without its content, which this research did not open.
- **The HL's consequence applies, in a form that adds nothing new** (config P3):
  - the record lists every product it leaves, each with its path. The template line "Link the
    current product result" becomes "every product";
  - an output the project has no place for gets an existing place the project chooses, or it is
    working material and goes. TFW names no folder (C8), so TFW defines no "named home";
  - the record folder holds only the record files before each orderly turn return (C4).
- **D4 on Daily:** the temporary folder may live across turns and goes when the Daily work ends.
  Daily has no Closing step 6. The OS temp cleaner is the outer backstop, harmless because the
  folder lies outside the project.

### E4: Where each rule must live to be read

| Reader | Loads besides its own workflow |
|---|---|
| Every session | root instructions. Claude Code loads `CLAUDE.md` "at the start of every conversation"; Codex reads `AGENTS.md` "before doing any work", with a combined default limit of 32 KiB |
| Coordinator (`plan.md`) | `Evidence subfolder`, `Semantic value-bearing classification`, `Closing and record recovery`, `Value-bearing accounting contract` |
| Executor (`handoff.md`) | `Anti-patterns (prohibited)`, `Exact-path staging`, `Safety and Execution Honesty`; the EV template at step 11 |
| Reviewer (`review.md`) | `Exact-path staging`, `Safety and Execution Honesty`, `Trace Discipline`; the Verify template |
| Researcher (`research/base.md`) | `Anti-patterns (prohibited)`, `Commit Attribution` |
| Daily worker | no `conventions.md` heading; its skill, its template and the root |

- **The new `Working material` subsection would be read by no Read Contract.** DoD 1 needs it as the
  authority, but its reach comes from four carriers:
  - the root line (every role);
  - the folded anti-pattern (Executor, Researcher);
  - `handoff.md` step 10 (Executor);
  - the Daily skill (Daily worker).
- **`Evidence subfolder` reaches only the Coordinator.**
  - Executors learn C2 from the EV template; Reviewers learn it from `verify.md`.
  - `Safety and Execution Honesty` is the one section both read. Its sentence "VERIFIED status
    requires an artifact reference (file path or inline output)" is where C2 and D6 meet both roles.
  - Rewritten as "the observation in the EV row", it costs no extra words.
- **C5 reaches writers only through the root line and the folded anti-pattern**, and the Reviewer
  through the `verify.md` check.
- **So the root line (DoD 6) is the main carrier, and it can carry C1 as well as C5** (config R-C).
  Root files here are 4.5–6.2 KB, far below Codex's limit.

### E5: The four findings that touch delivery

**1. `handoff.md` step 10 hands temporary files to the Coordinator, against D3–D4.**
- **Already in the rules:**
  - Closing step 4: "every task-owned resource's exact ownership, use and safe disposition";
    "pending cleanup names its actor/action";
  - Closing step 6: disposal of "temporary files whose accepted work and source returns are
    preserved"; "Record completed, retained or pending cleanup truthfully; DONE never asserts
    deletion succeeded";
  - `Worktrees for concurrent mutation`: the Coordinator removes a tree only after landing;
  - `Transcript isolation`: another unit's tool output and unreturned working tree are not evidence
    surfaces.
- **The conflict:** step 10's sentence, "Identify exact task-owned temporary resources and their
  current owner/disposition for the Coordinator's later safe close", lets working material outlive
  its creator and change hands. Those are the two conditions under which D3 found the temporary
  directory unsafe.
- **Removable from the proposal:**
  - D4's clause "removes what it sees and reports what it cannot", which step 6 already says;
  - any new cleanup step;
  - all but one clause of the lifetime text in `Working material`.
- **The fix is a same-length rewrite of that sentence:** the Executor removes its own working
  material when its work ends and names the other task-owned resources (worktree, processes,
  containers) for the Coordinator's close.

**2. Root templates and DoD 6.**
- **Already in the rules and files:**
  - the manifest installs the Codex and Claude roots as `managed_block`, Cursor and Antigravity as
    `copy`;
  - update applies "one marker-bounded block; preserve unmarked/foreign neighbors";
  - the Claude template lists five rules outside its block, so receivers never get later changes to
    them;
  - the Codex template has no rule list;
  - Cursor and Antigravity keep three Conduct rules inside copied files;
  - this repository installs the Codex, Claude and Antigravity copies, not Cursor, and keeps its own
    Conduct outside the blocks.
- **The effect:** a line added to the Claude list reaches new installs only; a Codex "Conduct" line
  would need a new heading.
- **Removable from the proposal:**
  - the "Conduct" heading. The line goes inside each managed block (Codex, Claude) and into the Rules
    list (Cursor, Antigravity), with no new heading;
  - the pointer form. `conventions.md` is not preloaded, so a pointer sends the agent to a file the
    root tells it not to preload. One line that states the rule itself, and names its heading,
    replaces the pointer.
- **The same line can carry C1 (E4)**, which keeps the `Working material` subsection short.
- **DoD 6 holds as written:** one line in all four templates, and installed copies follow the
  manifest. No amendment.

**3. `review.md` is above 1,400 words; DoD 3 forbids growth.**
- **Already in the rules and files:**
  - `Design Rules`: "workflow instructions ≤1400 words. A ceiling is not a target or permission to
    remove meaning";
  - DoD 3 forbids growth for every changed workflow and holds `handoff.md` within 1,400 words;
  - `review.md` Verify already says "Reuse adequate evidence; rerun changed, missing or uncertain
    dependencies and every TS-required check. Audit EV against RF §5", and Step 2 opens the Verify
    template;
  - `verify.md`: "RF is a declaration, not a fact. Open files, run necessary checks"; its test asks
    "Would the evidence establish this claim … without RF?".
- **Removable from the proposal:** `review.md` leaves deliverable 3.
  - Its text already carries verification by repetition.
  - The two Reviewer checks go into `verify.md`, which the Reviewer opens at Step 2.
  - `review.md` stays untouched at 1,562 words, and DoD 3's "review.md … carry deliverable 3" is met
    by existing text. No amendment.
  - If the TS still wants a `review.md` sentence, the same file must lose as many words.
- **In `verify.md`**, the column "Artifact exists?" becomes "Repeated or opened?" at the same
  length.

**4. `.tfw/` has no anchor for the comment rule.**
- **Partial anchors already in the rules:**
  - "No placeholders" in all four root templates: a TODO is a placeholder;
  - the anti-pattern "Work is left unfinished because it can be called debt" covers deferred-work
    notes;
  - `Trace Discipline`: the RF carries "results, decisions and observations", the home of the reason;
  - the anti-pattern "A journal event … copies artifact/chat bodies instead of referencing them":
    correspondence is referenced in the trace, not copied;
  - NS2.4 (selected trace, not transcript) and NS3 (not a raw chat archive);
  - outside TFW, PEP 8: "Comments that contradict the code are worse than no comments". This is the
    owner's first harm, staleness.
- **Removable from the proposal:**
  - the list of forbidden kinds in the rule text (messages to agents, excuses, deferred work, legacy
    chatter, jokes, notifications). The positive form "value for the file's reader, or read by a
    program" excludes them, and "No placeholders" plus the debt anti-pattern already forbid deferred
    work;
  - the separate anti-pattern bullet. "A comment used as a channel" folds into the existing debt or
    journal bullet, which Executors and Researchers already read;
  - "kept byte for byte" in D9. The program-read exception and DoF 3 protect those lines.
- **What stays:**
  - one C5 statement with the exception list (DoD 1);
  - the root line (DoD 6);
  - the `verify.md` check (C8);
  - the migration guide (C6).

### E6: Subtraction matrix

| Item | Serves | What breaks if it goes | Text already carrying part | Verdict | Minimal carrier |
|---|---|---|---|---|---|
| D1 temp location | C1, DoD 1 | DoD 1 unmet | `Worktrees` location pattern | keep, one phrase per OS family | `Working material`; root line |
| D2 not a TFW root | rationale | nothing | — | remove from rule text | RES and TS only |
| D3 private to its creator | C1, C3 | lost or handed-over material (DoF 1) | `Transcript isolation`; C3 | fold to one clause; fix step 10 | `Working material`; `handoff.md` step 10 |
| D4 removed when the work ends | C1 | orphaned material, no actor | Closing steps 4 and 6 | fold: only "the creating role removes it when its work ends" is new | `Working material`; step 10; Daily §4 |
| D5 row written when observed | C2 | an unrepeatable observation is lost (HL §9) | anti-pattern "Evidence is reconstructed after the fact" | fold: the EV template opens at step 8 instead of 11 | `handoff.md` steps 8 and 11 |
| D6 deciding values | C2 | the EV becomes the dump (the 358 KB case) | "file path or inline output" (Safety, EV) | fold into the column header and the Safety sentence | EV template; Safety |
| D7 unrepeatable claims | the limit of C3 | attested claims go unlabeled | `verify.md` explicit limits; NS2.7; DoF 1 | shrink to one sentence keeping items 1–3 and the attestation label; drop the owner's proportionality call (NS2.7 and the TS carry it) and item 5 (E1) | EV template |
| D8 commit, not tree copy | MAX_PATH; no copies | a long path fails at once in temp, visibly | C2's "how … commit"; "a second copy of the result" | remove as a rule; the HL §9 risk row stays | none |
| D9 exception list | C5 | DoF 3 | none | keep, short; drop "byte for byte" | C5 statement |
| D10 docstrings | owner reserve, DoD 10 | DoD 10 | — | keep as owner input | TS |
| D11 Reviewer check | C8, DoD 7 | the comment channel goes unchecked | `verify.md` self-check | fold to one check line; the commands go to the TS | `verify.md`; TS |
| D12 chatter removal | C7, S9 | — (it removes words) | — | keep | deliverable 8 |
| Del. 1 `Evidence subfolder` | C2 | binaries stay invited | its sentence 3 | replace sentence 3 | `conventions.md` |
| Del. 1 `Working material` | C1, DoD 1 | DoD 1 | Closing; `Worktrees` | keep, short: location, creator, lifetime, step 6 | `conventions.md` |
| Del. 1 classification sentence | C1 | — | the TRACE row; "Location/name never decide" | remove; clarify the TRACE row's "log records" instead | `conventions.md` |
| Del. 1 C5 statement | C5, DoD 1 | no anchor at all | partial (E5.4) | keep: positive form plus exceptions | `conventions.md` |
| Del. 1 two anti-patterns | DoD 1 | Executors and Researchers lose them | "A per-user file is stored in the shared tree"; the debt and journal bullets | fold into existing bullets | `conventions.md` §14 |
| Del. 2 EV template | C2, DoD 2 | — | Artifact column; Environment table | keep: rename columns, delete Attachments, move the per-row Environment into "How" | EV template |
| Del. 3 `handoff.md` | C2, D5, D3 | — | step order; step 10 | keep: two same-length edits | `handoff.md` |
| Del. 3 `review.md` | C3 | nothing: already carried | the Verify bullets | remove from the deliverable | — |
| Del. 3 `verify.md` | C3, C8 | the two checks | Evidence Verification table; self-check | keep: column rename plus two checks, offset in the same file | `verify.md` |
| Del. 4 Daily | C4, DoD 4 | unlinked outputs (E3) | "Keep products at their ordinary project paths"; "Link the current product result" | keep: one sentence in §4; template line "every product" | Daily skill, template |
| Del. 5 migration guide, changelog | C6, DoD 5 | C6 | receipt row "Material questions" | keep; a short guide | `migrations/`, `CHANGELOG.md` |
| Del. 5 root line ×4 | forward C5 (S4), DoD 6 | ad-hoc writes never see C5 | managed blocks | keep: inside the blocks, self-contained, carrying C1 too | four templates; three installed copies |
| Del. 6 cleanup | C7, DoD 7 | the shipped rule fails at home | — | keep | live code and configuration |
| Del. 7 own trace | C7, DoD 8 | — | — | keep | this task's folder |
| Del. 8 chatter | C7 | — | — | keep | two live files |

Frozen items tested; none is proposed for amendment:

| Frozen item | Test | Why not an amendment |
|---|---|---|
| DoD 1 "the two anti-patterns once each" | could they go? | folded into existing bullets they are still stated once, and they are the only carrier besides the root for Executors and Researchers |
| DoD 3 | `review.md` above the ceiling | untouched, it does not grow and already carries repetition |
| DoD 6 | placement; pointer | inside the blocks and self-contained, the line meets "one line in all four templates" |
| C2 "no copies, however small" | still needed? | G3's copies show why it stays |
| C1 "referenced … only by its ID-relative name" | against D3 | D3 is stricter and compatible (iteration 1) |
| DoF 1 retention route | needed as rule text? | it stays in the frozen HL as a failure response; no rule text |

**Minimal deliverable set:**
- **`conventions.md`:**
  - sentence 3 of `Evidence subfolder` replaced;
  - a short `Working material` subsection;
  - the Safety sentence edited and the TRACE row clarified;
  - one C5 statement;
  - two folds into existing anti-patterns.
- **EV template:** columns renamed, Attachments deleted, one sentence for unrepeatable claims; no
  growth.
- **`handoff.md`:** two same-length edits, at steps 8/11 and step 10.
- **`verify.md`:** one column renamed and two checks added, offset in the same file.
- **`review.md`:** untouched.
- **Daily:** one sentence in §4 of the skill, offset in the same file; one line in the template.
- **Root instructions:** four templates and three installed copies get one self-contained line
  carrying C1 and C5.
- **Release text:** the migration guide and the changelog entry.
- **Deliverables 6–8:** unchanged.

### E7: Queries and files

**Web:** 5 calls, all for E4–E5: 2 searches (PEP 8 on comments; root instruction loading in Claude
Code and Codex) and 3 fetches (the Claude Code memory page; the Codex AGENTS.md page, which
redirected once).

**Project files:** the Read Contract lines of ten workflows, by grep; sizes and block contents of
`AGENTS.md`, `CLAUDE.md` and `.agents/rules/tfw.md`, by grep. All other inputs come from G11.

**Receivers:** R3 and R4 by script, counts only. R4 was identified by the record count seen during
Gather; nothing else there was inspected.

**Working material:** scripts and JSON output in the system temporary directory under this task's
ID, removed at the end of this iteration.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| H3 holds: no case needed bytes that a timely row or a re-run would not give. TS-named retention leaves the rule text | Challenge: regulated work, disputes after acceptance, long trials |
| H4 is false in its strong form. Two rule-named kinds fall between returns (ONB alone, review map). Commit reduction leaves this task | Challenge: a dead run whose tree is lost; a shared working tree |
| H6 is false as stated: 16–21 of R3's 35 records and 1 of R4's 4 keep unlinked outputs. P3: every product listed, the project chooses a place, the rest is working material | Challenge: whether P3 collides with C1, C4 or C8; whether Daily cleanup can drop an unlinked product |
| Rule carriers: only the root line reaches every role; no Read Contract reads `Working material` | Challenge: is one root line enough, and what if a receiver edits its root |
| Subtraction: D2 and D8 go; D3–D7 and D11 fold; `review.md` leaves deliverable 3; no amendment | Challenge: which failure returns if a removal is wrong (NS2.2) |

**Sufficiency:**
- [x] External source used? 2 searches, 3 fetches
- [x] Briefing gap closed? H3, H4 and H6 decided at Extract level; the subtraction matrix is built; the four delivery findings are answered
- [x] Configuration Space built from Gather dimensions? D1–D7 in three groups, D8 in E6; one new carrier dimension

**Knowledge handover.**
- **Material:** E1–E6.
- **Inspected scope:** E7, plus G12.
- **Uncertainty:**
  - Fact (c) counts any later change, so unrelated edits inflate it. The 24-hour count is the
    tighter bound.
  - Whether an output is a product or working material is not decided without content.
  - The habit groups rest on path classes.
- **Knowledge publication:** none.
- **Continuation:** on the Coordinator's answer, Challenge.

Stage complete: YES
→ User decision: Coordinator's ruling (addressed message, 2026-10-05): Extract closed; go to Challenge.
1. **Main carrier to test.** One root line states both rules itself (working material and
   comments). It sits inside the updated block for Codex and Claude and in the Rules list for
   Cursor and Antigravity; a short `conventions.md` subsection is the source. Second lever: which
   Read Contract lines in `handoff.md`, `verify.md` and the Daily skill must name that subsection so
   that roles creating working material read the source, and what it costs against `handoff.md`'s
   1,400-word limit.
2. **A Daily product with no place in the project.** The worker picks an existing project place and
   records the path in the record. One question goes to the person only when no suitable place
   exists at all, and the answer may be "working material, do not keep". No new mechanism: the skill
   already has one consequential question with a hold.
3. **Test beyond the plan:**
   - whether update delivers the root line to existing receivers through the updated block, given
     that the Claude rule list sits outside it;
   - whether the comment rule loses checkability without the list of forbidden kinds, which
     supplies the words for the Reviewer's commands (D11); a rule that cannot reveal its violation is
     only advice;
   - whether the Daily rule holds over several turns while the temporary folder lives between turns.
