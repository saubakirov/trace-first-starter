# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20261004-174815_LPF](../../HL-TFW_20261004-174815_LPF.md)
> Goal: A TFW project holds only the result and the selected trace: working material lives outside the project under the task ID and is gone when the task closes, and a comment carries value or is absent.
> Producer unit: `claude-code:agent:local_a7cf0ab7-482d-403e-b738-504d82bba898/lpf-researcher` (native agent `a2f09276b39617fd0`); mode focused, one pass. Repository state: HEAD `588386e7`.

## Dimensions

No alternative is recommended at this stage.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1 Raw material after acceptance (H3) | nothing kept; the EV row is the record | kept only for items the TS names | kept for a fixed period, as CI does (30–90 days) | kept until the next release |
| D2 What a later reader relies on for a closed task's claim (H3) | the values the EV row printed | a re-run at the cited commit | the original bytes | statements in RF and REVIEW |
| D3 Commit points inside a task (H4) | after every step | at role returns, plus the ordered commits a rule requires there | one commit per role per round | one per task, squashed at landing |
| D4 Where the commit count is settled (H4) | a rule sentence in this task | outside this task (H4's consequence) | the agreed separate cleanup task | nowhere: the count follows governance acts |
| D5 Home of a one-off Daily product (H6) | an ordinary project path the worker picks | a named product place inside the record folder | working material, gone at the return | a project-wide products folder |
| D6 What the Daily record says about products (H6) | links every product it leaves | links the result only, as the template asks today | an explicit product list | nothing beyond the result section |
| D7 When Daily working material goes (H6, C4) | before each orderly turn return | at the record's close | at the start of the next Daily | left to the OS temp cleaner |
| D8 Fate of each D1–D12 item and Phase A deliverable (subtraction) | kept as planned | folded into an existing sentence | removed | amendment proposal for a frozen item |

## Findings

### G1: H3 method and corpus

A script read every tracked text file at HEAD; `site/`, a derived copy, was skipped. It found
497,188 path tokens containing `evidence/` in 992 files. Each token got:
- a cited task: the task ID in the path, or the folder of the file it resolved against;
- a kind: the EV file, the folder itself, or any other file (non-EV).

A citation is cross-task when the cited task differs from the citing file's task, or when the citing
file lies outside every task folder. Byte copies were found by blob identity in `git ls-tree -r HEAD`.
A prose pass read every line outside evidence folders that names another task next to "evidence"
and a raw-material word: 73 lines.

The corpus at HEAD holds 1,581 files in 110 task evidence folders: 57 EV files and 1,523 others
(299 MB). The others are 590 JSON, 359 TXT, 214 non-EV Markdown notes, 104 RAW, 59 Python and 58 ZIP
files, 24 PNG and smaller groups.

### G2: H3 narrative citations of another task's raw evidence

Outside evidence folders, 11 lines in 6 files cite a non-EV evidence file of another task. Two
`.tfw` update receipts are left out here; they hold snapshot copies (G3). The lines form five
clusters:

| # | Later file | Material of the closed task | What the reader took from it | In the closed task's own trace too? |
|---|---|---|---|---|
| 1 | `KNOWLEDGE.md`, a decision row | CRUE field analysis, a Markdown note in `evidence/` | the analysis, as provenance | yes: CRUE EV and `verify.md` cite it |
| 2 | `KNOWLEDGE.md`, a task row | CRATM phase E release-package note | a provenance link | yes: CRATM RF, EV, `verify.md` |
| 3 | PTTC HL, proposal and research Gather | CRATM phase E raw test transcript | run counts and durations: 529 collected in 0.39 s; 15 passed in 279.97 s; 528 passed and 1 skipped in 768.55 s; an earlier run with 2 failures in 721.91 s and its cause; six late runs summed to 1,962.73 s | no: the values exist only in the transcript |
| 4 | RWNR phase B dispatch event | five TKL archives and one raw diff (18.7–57.2 MB each) | path, blob and size, as a landing invariant: keep exactly these five large blobs, add no sixth | identity only, no content |
| 5 | PCUX HL | FRATS phase A provider note | the result "only partial Codex P3" | yes: FRATS RF, REVIEW, `verify.md`, phase B EV |

- No REVIEW, `verify.md`, Daily record, `knowledge/` record or `.tfw/` rule cites another task's raw
  evidence.
- Cluster 3 is the only case where a later task used values that only raw bytes held. PTTC used them
  as the motivation of its HL; its own words are "No fresh benchmark was run for this HL". Every figure
  is a pytest summary line, the form the HL §3.1 row shows ("474 passed in 12.3s"). The failed run's
  cause came from the output text. The suite can be re-run at the CRATM commit.
- Three clusters (1, 2, 5) cite Markdown notes kept in `evidence/` next to the EV. Their statements
  also stand in RF, REVIEW or EV. C2 leaves such notes no place in `evidence/`.
- Cluster 4 shows the cost side: a later task had to carry a closed task's dumps as an audit
  constraint.

### G3: H3 mechanical mentions and byte copies

- **Tool output:** 86 evidence files in five tasks mention other tasks' evidence paths 33,524
  times. They are TKL 56, SLC 13, PTTC 11, RWNR 5 and CRATM 1, all tool output: MkDocs warnings, tree
  inventories, censuses, diffs. No reader stands behind these mentions.
- **Update receipts:** two `.tfw/update_receipts/` files hold snapshot copies with 66 mentions.
- **Byte copies:** 198 non-EV evidence files (1.4 MB) are byte-identical to a file owned by another
  task. 169 of them are 200 bytes or less (empty or generic output). The other 29:
  - 21 TKL files copy SLC files: six trace documents (status, a transition event, HL, TS, RF,
    REVIEW) and three evidence outputs. TKL printed them as input for a trial that reused "an actual
    accepted SLC effect", partly as captured command output and partly as a tree copy under a 40-hex
    commit folder (14 files, the 225-character path of HL §2.1);
  - 3 SLC evidence outputs on the other side of those pairs;
  - 5 identical MkDocs outputs in SLC and PTTC: the same build, not a copy.
- **Reading at a commit:** TKL's own research took the other road. It read SLC files "with `git show
  <full-sha>:<path>`", and they were "intentionally not copied". D8's practice is already in use.
- **Bytes without a method:** the prose pass found one substantive case. RVAG Extract judged FRATS's
  kept semantic-replay output unusable: the "output exists but lacks executable predicates and
  command", so the claim stayed unestablished. The later reader needed the method; the bytes did
  not help.

### G4: H3 external anchor

- CI platforms delete build output by default:
  - GitHub Actions keeps artifacts and logs for 90 days (1–400 configurable). From 2026-10-01 the same
    retention covers checks, workflow runs and statuses.
  - GitLab expires job artifacts after 30 days by default and keeps those of the latest pipeline.
- Regulated audit keeps the documentation, not every item examined. PCAOB AS 1215:
  - audit documentation is retained for seven years and assembled within 14 days under the amended
    standard;
  - for inspected documents it asks for identification of the items, for example check numbers;
  - abstracts or copies are required only for significant contracts or agreements.
- The common pattern: the record of what was done, and on what, is kept; copies are kept only for a
  named class.

### G5: H4 rules that name a commit or read one

| Commit kind | Current `.tfw/` text | Order |
|---|---|---|
| Freeze | `conventions.md` HL rules 13–14: the approved HL is committed before the first research iteration; `freeze` scope for the first freeze and every re-freeze | before research |
| Status binding | HL rule 16: no header names its own commit; `coordination_selected`: "Commit the event before its SHA enters an effective status `selection_ref`"; journal event template | after the freeze or event it cites |
| Dispatch | the ONB, RF, RES, REVIEW and Briefing headers require an "immutable dispatch ref" | before the unit's first artifact |
| ONB | `handoff.md` step 4: "Commit ONB alone" | before implementation |
| Candidate | `handoff.md` step 10; TS, REVIEW and `verify.md` templates; `Value-bearing accounting contract`: the first tested VALUE+ASSURANCE commit "before EV/RF/REVIEW/final transition" | before traces |
| Review map | `review.md` Step 1: "complete the self-check, commit exact paths, and stop when required" | before Verify |
| Landing | `Landing a deliverable across sessions`: a separate commit naming the producer's task and phase; the Candidate stays reachable | after review |
| Durable return | `Transcript isolation`: after a durable return "only the named artifacts and commits become inputs" | at each return |

Recovery paths:
- `Worktrees for concurrent mutation`, dead run: "Read its tree and land its commits before removal".
  It reads the tree and the commits.
- `Repair only the record` reads the status/event pair as files, not commits.
- Closing step 4 confirms that the Candidate is still reachable.

No rule names a commit for a research stage file, a `verify.md` or `judge.md` file, a separate
status/event write, a gate ruling or an economics receipt.

### G6: H4 census

**Corpus.** Three sources, all refs:
- commits whose subject names the task ID;
- commits that touch the task folder, under its old and new paths;
- commits whose subject names only the abbreviation. These were reviewed and two foreign ones
  dropped.

**Classification.**
- **At a return:** the next task commit is by another role, or the commit is a researcher stage commit.
- **Rule kinds** (as in G5) are read from scope tokens and changed paths.
- **Status binding** is detected by a status or `iterations.yaml` diff that prints an earlier
  commit's SHA.

| Task | All refs | Unique patches (merges excluded) | On master | Unit commits: at return / rule-named between returns / habit | Coordinating commits: rule-named / other | Keep returns and rule-named | Strict: coordinators keep rule-named only |
|---|---:|---:|---:|---|---|---:|---:|
| CMTR | 73 | 54 | 54 | 41: 25 / 4 / 12 | 32: 11 / 21 | 51 (1.43×) | 40 (1.82×) |
| PCUX | 124 | 113 | 124 | 44: 29 / 6 / 9 | 80: 35 / 45 | 93 (1.33×) | 70 (1.77×) |
| RWNR | 92 | 85 | 57 | 41: 17 / 13 / 11 | 51: 40 / 11 | 77 (1.19×) | 70 (1.31×) |
| PTW | 95 | 68 | 88 | 52: 18 / 15 / 19 | 43: 20 / 23 | 57 (1.67×) | 53 (1.79×) |
| LFD | 67 | 66 | 67 | 30: 15 / 6 / 9 | 37: 17 / 20 | 49 (1.37×) | 38 (1.76×) |
| **All** | **451** | **386** | **390** | **208: 104 / 44 / 60** | **243: 123 / 120** | **327 (1.38×)** | **271 (1.66×)** |

Unit commits are the Researcher's, Executor's and Reviewer's. Coordinating commits are the
Coordinator's and the historical LEAD's.

Rules name 172 of the 451 commits: dispatch 58, landing 27, freeze 24, status binding 21, ONB 18,
Candidate 14, review map 10.

- **Habit is a minority:** 124 to 180 of 451 commits (27–40%). The largest habit groups:
  - the Reviewer's `verify.md`, `judge.md` and REVIEW commits before its final status commit;
  - the Executor's status/event commits split from ONB or RF;
  - the Coordinator's gate-ruling events after every research stage (LFD, PCUX);
  - HL and TS edits.
- **Rule-named volume follows governance acts:**
  - PCUX committed 11 freezes of its HL (the first and ten re-freezes) with 11 status bindings
    between 00:41 and 02:46;
  - RWNR recorded 28 dispatches across its LEAD and Coordinator units.
- **Side refs hold copies:**
  - RWNR has 35 commits that are not on master, from producer branches landed again on a fresh
    base;
  - PTW has 95 commits but 68 unique patches.
- **The HL §2.1 counts missed unattributed commits.** Its figures (≈62/107/92/76/67) counted subject
  IDs only and missed, for example, PCUX's Executor rounds, CMTR's phase A and PTW's reviews.
- **Position by role change is generous.** An unrelated commit by another role marks a return.
  Corrected by hand for LFD, its strict count moves from 38 to 37.

### G7: H4 external anchor

Git's SubmittingPatches asks to "Make separate commits for logically separate changes". It measures
granularity by logical change, not by count or by session step. In TFW terms:
- the rule-named commits mark boundaries that carry identity (freeze, Candidate, landing);
- the habit commits split one return into process steps.

### G8: H6 this repository's Daily and the Daily form

- **Records:** 5 records, 12 files.
  - Four records hold only `task.md`.
  - One holds `task.md`, an economics leaf (4 JSONL), two economics reports and a 417-line file that
    two agents used as a shared Claude–Codex correspondence channel.
- **Products:** all five records link their products at ordinary project paths (`.tfw/`, `.claude/`,
  `workspace/`, release branches). No binary or one-off product exists.
- **The Daily skill (1,288 words)** says:
  - "Keep products at their ordinary project paths";
  - honour the receiver's established form, "including a three-file task/brief/messages split";
  - economics bytes go into the record's "economics leaf", and "the actually used quote basis" is
    copied into the record root;
  - "Update the selected local record with result paths";
  - its return point is "each orderly turn return".
- **The record template** says: "Link the current product result at its ordinary path."
- **Missing:** neither the skill nor the template mentions temporary files, cleanup before a return,
  or what else may sit in the record folder.

### G9: H6 receiver R3, aggregate numbers only

Counted on the owner's machine on 2026-10-05 under the Coordinator's permission. R3 was identified
as the HL §2.1 receiver by its record count: 35 now, 32 at the HL measurement. No file name, path,
quote or content enters this trace.

- **Size:** 35 records, 1,663 files, 268.5 MiB.
- **Form:** every record uses the three-file form the skill names. None has an economics leaf or a
  quote file.
- **Files per record:** min 3, median 17, max 797. One record holds only its three record files.
  Files that are not the record: 1,558, or 94%.
- **By type (files, MiB):**
  - PNG 855 / 97.5; PDF 59 / 97.3; GIF 19 / 21.3;
  - JSONL 39 / 5.5; HTML 41 / 4.0; JPG 9 / 3.2; WEBM 18 / 2.8;
  - Markdown outside the record files 151 / 1.5; JSON 161 / 0.8; Python 63 / 0.5;
  - SVG 45, WEBP 24, TXT 20, XLSX 10.
- **Records containing each type outside the record files:** Markdown 32, PNG 19, Python 18, HTML 18,
  JSON 15, PDF 13, SVG 7, ZIP 5, TXT 5, DOCX 4, WEBP 4, compiled Python cache 3, JPG 3, PowerShell 3,
  JavaScript modules 3 and 2.
- **Fact (b), files that are not the record next to it:** 34 of 35 records.
- **Fact (a), a link to an existing project file at an ordinary path** (outside `daily/` and the agent
  instruction folders):
  - anywhere in the record: 35 of 35, an upper bound, since links to inputs count too;
  - inside the record's result or closing section: 6 of 35, a lower bound, since only some records
    have such a section.
- **Crossing the lower bound with fact (b):**
  - 29 records hold other files and link no product at an ordinary path from their result or closing
    section;
  - 5 do both;
  - 1 links and holds nothing else.
- **Outside the records:** one file lies under `daily/` outside any record.

The HL §2.1 figures (32 records, 1,495 files, 243 MB, 797 tracked) and the owner's S6 remain the
second basis.

### G10: H6 external anchor

- GitHub warns above 50 MiB per file and refuses above 100 MiB.
- It recommends repositories ideally under 1 GB and strongly under 5 GB, with Git LFS for large
  binaries.
- R3's Daily alone holds 268.5 MiB, mostly PNG and PDF.

### G11: Subtraction inputs: text that already carries part of each item

| Item | Existing text that already carries part of it | Where |
|---|---|---|
| C2, D6, deliverable 2 | "VERIFIED status requires an artifact reference (file path or inline output)"; the EV Artifact cell "{path or inline output}"; "Give VERIFIED a resolving artifact"; "In the existing row or its resolving attachment"; the Attachments section; `Evidence subfolder` sentence 3, which invites binaries | `conventions.md` §12; EV template; `Evidence subfolder` |
| C1 "no class" (the classification sentence in deliverable 1) | TRACE is "Lifecycle, decision, review, evidence, and log records"; "Location/name never decide" | `Semantic value-bearing classification` |
| D5 | anti-pattern "Evidence is reconstructed after the fact"; `handoff.md` step 8 runs the checks, step 11 emits EV | `conventions.md` §14; `handoff.md` |
| C3 | anti-pattern "A Reviewer approves without opening the delivered output and checking RF/evidence claims against reality"; Verify "rerun changed, missing or uncertain dependencies and every TS-required check. Audit EV against RF §5"; the `verify.md` column "Artifact exists?" | `conventions.md` §14; `review.md`; `verify.md` |
| D3, D4 | Closing step 6 disposes of "temporary files whose accepted work and source returns are preserved" and records "completed, retained or pending cleanup truthfully; DONE never asserts deletion succeeded"; step 4: "pending cleanup names its actor/action"; `handoff.md` step 10: "Identify exact task-owned temporary resources and their current owner/disposition for the Coordinator's later safe close" | `Closing and record recovery`; `handoff.md` |
| Anti-pattern "working material committed into the project" | "A per-user file is stored in the shared tree."; exact-path staging reads the full `git status` before every commit | `conventions.md` §14; `Exact-path staging` |
| D8 | "Incidental traces … do not become … a second copy of the result"; TKL research's `git show <sha>:<path>` practice | `Trace boundary and selected siblings`; TKL Gather |
| C5, D9–D11, anti-pattern "a comment used as a channel" | no comment rule anywhere in `.tfw/`; the nearest is "A journal event … copies artifact/chat bodies instead of referencing them" | `conventions.md` §14 |
| C4, deliverable 4 | "Keep products at their ordinary project paths"; "Update the selected local record with result paths"; template "Link the current product result at its ordinary path" | Daily skill and template |
| C6, deliverable 5 | update receipt row "Material questions": "`<none, or question → answer/route>`" | `templates/update_receipt.md` |
| DoD 6 | the Codex and Claude roots install as `managed_block`, Cursor and Antigravity as `copy`; update applies "one marker-bounded block; preserve unmarked/foreign neighbors"; the Claude template's rule list sits outside its managed block; the Codex template has no rule list | `adapters/manifest.yaml`; `update.md`; root templates |
| DoD 3, Design Rule | "workflow instructions ≤1400 words. A ceiling is not a target or permission to remove meaning" | `Design Rules` |

Word baselines at `588386e7`:
- **workflows and templates:** `handoff.md` 1,118; `review.md` 1,562, already above 1,400 (DoD 3 asks
  only that it does not grow); `verify.md` 1,064; EV template 323; Daily `SKILL.md` 1,288; Daily
  record template 477;
- **`conventions.md` sections:** `Evidence subfolder` 56; `Semantic value-bearing classification`
  204; `Safety and Execution Honesty` 61; `Anti-patterns` 495; `Closing and record recovery` 1,620;
  `Design Rules` 157;
- **adapter root templates:** Codex 627, Claude 787, Cursor 512, Antigravity 623;
- **migration guide** 3.8.1: 1,162.

### G12: Queries and files

**Web:** 7 calls, 6 searches and 1 refused fetch (HTTP 403). The soft limit of 5 was exceeded, as
allowed.
- H3: GitHub Actions retention; GitLab artifact expiry; PCAOB AS 1215 retention; AS 1215
  identification of items tested; the AS 1215 page (refused).
- H4: Git SubmittingPatches.
- H6: GitHub large-file limits.

**Project files opened beyond scripted counts:**
- **H3:**
  - `KNOWLEDGE.md` (two rows); the PTTC HL, proposal and research Gather (one line each);
  - the RWNR phase B dispatch event (lines 70–110); the PCUX HL (one line);
  - CRATM iteration 3 RES, `knowledge/constraint.md`, RDP `judge.md`, RVAG Extract and the SLC REVIEW
    (one line each);
  - TKL RF, REVIEW and EV lines by grep; CRATM, FRATS and CRUE files by grep.
- **H4:**
  - `conventions.md`: `Commit Attribution`, `Worktrees for concurrent mutation`, `Exact-path
    staging`, `Landing a deliverable across sessions`, the coordination selection paragraph,
    `Closing and record recovery`, `Value-bearing accounting contract`, `Transcript isolation`;
  - `handoff.md` steps 1–15; `review.md` Steps 1–4; the selection and freeze steps of `plan.md`;
  - role template headers by grep; `git log` and `git diff-tree` for the five tasks.
- **H6:** the 12 Daily files (the heads of three); the Daily `SKILL.md` in full and the record
  template §4–§5; R3 by script, counts only.
- **Subtraction:**
  - the `conventions.md` sections listed in G11; the EV template; `verify.md` lines by grep;
  - the four adapter root templates (headings and rule lines); `adapters/manifest.yaml`;
  - `update.md` lines 154–167; the headings of `migrations/3.8.1.md`; the update receipt template by
    grep; the head of `CHANGELOG.md`.

**Working material:** the census scripts and their JSON output sit in the system temporary
directory under this task's ID. They are removed at the end of this iteration.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| H3: five cross-task clusters. Only one used values that only raw bytes held (PTTC, from CRATM's test transcript), and they are pytest summary lines. No review, Daily or knowledge record relied on raw files. For one later reader, kept bytes without the method were useless (RVAG). | Extract: whether TS-named retention (D7 item 5) is ever needed. Challenge: regulated work and disputes after acceptance |
| H4: 451 commits; rules name 172; habit is 27–40%; projected cut 1.38–1.66×, not several-fold | Extract: a decision per commit kind; which habit kinds merge without harm. Challenge: crash recovery, a shared working tree |
| H6: in R3, 94% of Daily files are not the record (34 of 35 records), and result sections rarely link a product at an ordinary path (at least 6 of 35). This repository is clean except for one correspondence file | Extract: product kind × home × link; whether C4 needs a product list or a named home |
| Subtraction: existing text found for every item except C5 | Extract: the matrix and the minimal deliverable set |

**Sufficiency:**
- [x] External source used? 6 searches; 1 fetch refused
- [x] Briefing gap closed? All four inputs gathered; R3 fact (a) has only an upper and a lower bound
- [x] Dimensions identified? Eight

**Knowledge handover.**
- **Material:** G1–G11.
- **Inspected scope:** G12.
- **Uncertainty:**
  - R3 fact (a) is bounded, not exact;
  - return points are approximated by role change;
  - rule kinds are detected from subjects and paths;
  - the H3 census covers HEAD only, so deleted files are not seen;
  - the knowledge inputs named in the Briefing (D52, D53, F23, F29) were not reopened here.
- **Knowledge publication:** none.
- **Continuation:** on the Coordinator's answer, Extract.

Stage complete: YES
→ User decision: ___
