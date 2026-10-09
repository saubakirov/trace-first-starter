# Verify — "Do the material claims hold?"
> **Mindset:** Auditor. RF is a declaration, not a fact. Open files, run necessary checks, compare
> accepted claims with reality, and state the limits.
> **Test:** "Would the evidence establish this claim for this subject, revision and environment without RF?"
> Map: [map.md](map.md) at `94fd4e98735ce8a4dc7f13fe89e2a1631bc747ed`

Subject for every check unless stated: Candidate `0863d299d86a1ca1776ffb966d54a1b848e7c348` against
Baseline `6c9766fcb2de252e010a790b0fbe676f02058f7c`, Windows 11 Pro 10.0.26200, Git 2.42.0,
Python 3.13.5, PyYAML 6.0.3, pytest 9.0.2, MkDocs 1.6.1, GNU `wc` 8.32, run by this Reviewer in
Claude Code 2.1.286. Both trees were extracted blob by blob with `git cat-file --batch` into this
Reviewer's working material (`<temp>/tfw/TFW_20261004-174815_LPF/`); repository checks ran in the
shared checkout, whose VALUE paths equal the Candidate (V2).

## Selection Argument

| Claim IDs | Risk / criticality | Affected behavior / dependencies | Environment | Oracle / authority | Evidence gap / limit | Selected verification and why |
|---|---|---|---|---|---|---|
| C14, C15, C16 | mandatory floors | acceptance, budget authority, owner reservations | Git | TS §4, HL §4.1, conventions accounting/change-authority rules | none | full replay: accounting, name sets, ancestry, TS/HL diffs, reserved files and remote state |
| C1–C6, C8, C9 | high: shipped to every receiver at the next update; the owner approved exact words (S10) | every role's reads; install/update block handling | text | RES iter2 W1–W8 | none | every W "after" text matched once and every "before" text absent, whitespace-normalized; placement, word counts, copies |
| C7, C11 | high: DoF 3 hard constraint; shipped economics helper | four `--help` publishers, doctor, state, docs generator, config readers | Python toolchain above | Baseline behavior on identical input; option A | none | census at both revisions, my own line-by-line classification, every removed line screened, docstring/comment readers searched, AST and YAML equality, behavior replays |
| C10 | medium: a stale instruction elsewhere undermines the rule | other templates/workflows | `.tfw/` text | HL C1–C3 | judgment per hit | corpus search for attachment, old-column, inline-artifact and hand-over wording |
| C12, C13, C18 | safety/history floors; public repository | task folder, frozen roots | Git | DoF 4, DoF 6 | none | tree listing, sizes, type filter, leak greps (literal and broadened), frozen-root diff |
| C17 | DoD 9/10 explicit | location rule | research records | DoD 9, DoD 10 | POSIX/Cursor by documentation, by design | read RES iter1 trial matrix and addendum, TS ruling |

## Verification Log

### V1: C14 accounting replay
- **Accepted claim / authority:** 34-path selector; 32 changed; 258 + 411 = 669 ≤ 1,000; 32 ≤ 33.
- **Subject tuple:** Baseline→Candidate; Git 2.42.0; TS §4 at `397d396f`; immutable owner denominator 33 / 1,000.
- **Action or evidence:** both TS §4 NUL-safe commands with the 34 literal paths; whole non-workspace name set compared with the selector's changed set.
- **Observed:** 31 `M` + 1 `A`; numstat 32 rows, additions 258, deletions 411, touched 669, 0 binary rows; non-workspace changes equal the selector changes exactly; unchanged members `tools/README.md`, `.tfw/adapters/manifest.yaml`.
- **Limit:** none.
- **Result:** HOLDS

### V2: C15 accepted-result identity and staging
- **Accepted claim / authority:** the Candidate is the first tested Executor VALUE commit, reachable, exact-path; later commits are TRACE.
- **Subject tuple:** `6c9766fc..HEAD` on `master`.
- **Action or evidence:** per-commit name sets; `git merge-base --is-ancestor`; `git diff 0863d299 HEAD` and `git diff HEAD` over the 34 paths; parent; untracked foreign folder.
- **Observed:** the Candidate holds exactly the 32 VALUE paths and nothing else; parent `397d396f` (ruling 1); reachable from `HEAD`; VALUE diff Candidate→HEAD and HEAD→working tree empty; `e19b8a52`, `b38f4db2`, `8d6f0d31` touch only the task folder; the untracked `workspace/2026/TFW_20260909-231654_OTR/` rode in no commit.
- **Limit:** the staging commands themselves are attested by RF; their observable result (exact name sets) is verified.
- **Result:** HOLDS

### V3: C16 human authority and frozen contract
- **Accepted claim / authority:** owner approval of TS, denominator and option A; ruling 1 inside Coordinator authority; reserved acts untouched; frozen HL claims unchanged.
- **Subject tuple:** TS at `18e426f7`→`9216218d`→`397d396f`→HEAD; HL at `efc915a9`→HEAD; `.tfw/VERSION`; remote state.
- **Action or evidence:** TS diffs; section-by-section HL comparison; `handoff.md` Step 2 and `Decomposition, constraints, and change authority` at Baseline; `git status -sb`; `git branch -r --contains`.
- **Observed:** approval header and owner quote in `9216218d` (also journal 34fa, HL S11); `397d396f` adds only ruling 1 and correction 1; TS unchanged since. HL frozen sections §1, §3, §3.1, §3.2, §4.1, §5, §6, §7 are byte-identical to the freeze; the only frozen-section edit is the Phase A deliverable list (rule 6 refinement), acceptable under DoD/DoF as they stand. Ruling 1 is prospective (Candidate's parent), below the multiplier (34 / 669 vs 66 / 2,000), names cause/cost/assurance/authority/verdict, and matches handoff Step 2 ("Below it, only a prospective Coordinator ruling inside unchanged boundaries may admit a necessary constituent"); "planned zero" in the convention refers to a planned measure of zero, not to each path outside a non-zero plan, so the TS's phrase "planned-zero rule: no VALUE path outside the selector" (read by the Executor's ONB as an owner route) does not apply. `VERSION` 3.8.1 unchanged; no tag; `master` ahead of `origin/master` by 27; no remote branch contains the Candidate.
- **Limit:** none.
- **Result:** HOLDS

### V4: C1–C6, C8, C9 exact wordings, places and counts
- **Accepted claim / authority:** W1–W8 verbatim in their named places; no meaning change; no growth in no-growth files.
- **Subject tuple:** Candidate files vs RES iter2 W texts; GNU `wc -w`.
- **Action or evidence:** a 61-check script: every W "after" text must occur exactly once and every "before" text zero times in the Candidate (whitespace-normalized); `git diff -U1` of every rule file; marker/heading line numbers; managed-block equality with templates and outside-block equality with Baseline; `cmp` of all manifest copies.
- **Observed:** 61 of 61 checks pass. Placement: Claude template START 15 · root line 21 (after "Version", before `### Command Routing`) · END 94; Codex START 1 · 6 · END 73; `CLAUDE.md` 3 · 9 · 82; `AGENTS.md` 28 · 33 · 100; Cursor/Antigravity/installed copy: fourth `## Rules` bullet after **Language.**; conventions §12 at 1436, `### Working material` 1442, `### Comments` 1453, §13 1463, both headings unique. Both installed managed blocks equal their template blocks; text outside the blocks unchanged; `.agents/rules/tfw.md` equals its template; all 22 manifest copies (11 Claude commands, 11 skills) equal their sources; Daily entries and installed skills unchanged; `review.md` unchanged. Words: conventions 15,764→16,038; EV 323→323; handoff and copy 1,118→1,116; verify 1,064→1,063; Daily skill 1,288→1,355 (≤ 1,400); record template 477→476; knowledge and copy 1,120→1,102; Antigravity profile 800→775; templates 787→855, 627→695, 512→571, 623→682; installed 825→893, 854→922, 612→682; `TS.md` 546→538, one deleted line. Cursor and Antigravity rule files are always applied (`alwaysApply: true`, `trigger: always_on`).
- **Limit:** none.
- **Result:** HOLDS

### V5: C6 migration guide and changelog
- **Accepted claim / authority:** seven W8 parts; harm in the owner's terms; three answers; exact receipt row; accurate claims about update.
- **Subject tuple:** `.tfw/migrations/3.9.0.md@0863d299` vs W8, C6, `update.md`, `templates/update_receipt.md`, `migrations/3.8.1.md`.
- **Action or evidence:** whole-file read; AC-6 gate commands; cross-check of every behavioral claim.
- **Observed:** sections 1–7 at lines 10, 32, 52, 66, 87, 93, 107; the four harms match C6 (stale, wall and slow conversation, note instead of finishing, tokens); now/later/not at all with "new agent writes follow ... regardless"; receipt row named `Material questions` exactly as the template spells it; "ask only when evidence cannot settle a consequential choice" matches `update.md` Step 1; drift refusal matches `update.md` Step 4; route table follows 3.8.1 and every linked guide exists; gate: 5 matching lines, `Material questions` at 79, 84, 112. `[Unreleased]` equals the W8 draft (Changed × 3, Fixed × 1, guide sentence, no link; only `migrations/economics-core.md` is published by the site generator).
- **Limit:** a receiver exercise is DEFERRED by the TS.
- **Result:** HOLDS

### V6: C7 comment cleanup and program-read safety
- **Accepted claim / authority:** remaining lines program-read or reader value; nothing program-read removed; no behavior change.
- **Subject tuple:** the 13 code/configuration files and `tools/README.md`; option A; W2.3.
- **Action or evidence:** census `git grep -n -E '(^|\s)(#|//)|"""'` at both revisions; `<!--` in the README; tokenizer listing of every removed comment and AST listing of every removed docstring; screen of removed lines for interpreter/encoding/directive/license/marker forms; search for `__doc__`, `getdoc`, `inspect.`, doctest, pytest config and docstring-rendering MkDocs plugins; AST equality after stripping docstrings; `yaml.safe_load` equality; ownership-marker count; who reads YAML comments; line-ending/BOM/final-newline comparison.
- **Observed:** census 277 → 93 (economics 15→3, project config 18→15, bindings 36→30, config template 42→36, `tfw_state.py` 144→0, others as RF); README `<!--` 0 at both. My classification of all 93 lines agrees with the EV table: interpreter lines (2), `# noqa: E402` (1), delimiters/one-liner of the four published module docstrings (7), one `#` inside a string literal (1), setting meanings in `.tfw/project_config.yaml` (15) and the manifest (1), template instructions and setting meanings in the two templates (66). Removed: 103 comments and 44 docstrings in Python, 18 YAML lines; none program-read; the only programs that read docstrings are the four `ArgumentParser(description=__doc__)` calls, whose module docstrings are byte-identical; no doctest or docstring renderer exists. All nine Python ASTs equal Baseline after docstring removal (two emptied class bodies became `pass`; two inline comments left their code lines intact); all four YAML files parse to identical values; 17 `←` ownership markers kept; `update.md` preserves `build.*` by key, not by comment; managed-block marker lines 10 → 10. Line endings, BOM and final newline unchanged in every changed file.
- **Limit:** none.
- **Result:** HOLDS

### V7: C11 behavior replays
- **Accepted claim / authority:** scripts behave as before; retained surface passes.
- **Subject tuple:** extracted Baseline and Candidate scripts on one tree; working tree = Candidate for VALUE.
- **Action or evidence:** `--help` of the four publishers and `tfw_state.py`, plus all nine economics subcommand helps; doctor `status`, `check tasks` (text, JSON), `check project`, `knowledge-pending`, two subcommand helps; economics `validate`; retained pytest surface, AC-7 gate, `build.lint`; MkDocs build into working material; `git status --porcelain --ignored` and a newer-file scan before/after.
- **Observed:** `--help` byte-identical — 409, 905, 713, 1,076 and 0 bytes, SHA-256 prefixes 6bf17747, 4bd824e5, d2926ef8, 34c00f2e; nine economics subcommand helps identical; doctor outputs identical with exits 1, 2, 2, 0, 0 and 63 status lines; `validate` exit 0 over the three received role files (rows 1, 2, 1, hashes equal to file names), identical output with the Baseline script; "14 passed in 4.08s"; AC-7 gate "12 passed"; lint "14 tests collected"; MkDocs exit 0 with 32 warnings, all on unchanged lines (changelog links to unpublished guides, `index.md`, philosophy, one conventions link at line 220, one glossary link); no project file written.
- **Limit:** pytest 9.0.2 against the `<9` pin in `tools/requirements.txt`, as RF records.
- **Result:** HOLDS

### V8: C10 coherence of the shipped corpus
- **Accepted claim / authority:** no remaining instruction invites attachments, the old EV columns or hand-over of working material.
- **Subject tuple:** `.tfw/**@0863d299` except historical guides and changelog.
- **Action or evidence:** `git grep -i` for attachment, artifact reference, inline output, resolving artifact, `evidence/{`, artifact exists, RF evidence ref, temporary resources, binary artifact, screenshot, raw output, scratch, helper script; each hit read.
- **Observed:** remaining "attachment" hits are update/init preservation attachments (content-addressed receiver preservation), a different object; `templates/ONB.md`, `templates/RF.md` §5 and `templates/REVIEW.md` ask to name task-owned temporary resources and their disposition, consistent with W2.2 and handoff step 10; the update receipt asks for "command and its result, or an evidence path", a separate record. The only contradiction, the TS template's `evidence/{file}` row, is removed by ruling 1. No tool parses EV columns (one evaluation fixture keeps an old-form EV as simulated receiver data).
- **Limit:** judgment per hit.
- **Result:** HOLDS

### V9: C12, C13, C18 trace, history and leak floors
- **Accepted claim / authority:** `evidence/` holds only EV; no archive/binary/image/oversize file; no leak; frozen roots untouched; removal follows no link.
- **Subject tuple:** task folder at HEAD; Baseline→Candidate frozen roots; Candidate added lines.
- **Action or evidence:** `ls -1A evidence/`; `git ls-files` type filter; `git ls-tree -r -l HEAD`; numstat binary rows; the literal case-sensitive TS M3 grep (the Windows application-data folder name) and broadened greps (drive-letter paths, profile paths, e-mail addresses, the machine user and organization names, private project names) over the task folder including JSONL; the same over the Candidate's added lines; `git diff --stat` over `workspace tasks daily tools/migrations`.
- **Observed:** `evidence/` = `EV__TFW_20261004-174815_LPF.md` only; 0 typed binaries; largest blob 53,379 bytes (HL); 0 binary numstat rows. The literal grep returns exactly TS lines 195, 283, 349, the TS's own description of the check; broadened greps find only the Windows local application-data environment-variable notation in HL and research and the public owner handle; economics `source_label` fields are bare file names. Candidate added lines carry no path, address or secret ("tokens" appears only as LLM tokens). Frozen roots: "7 files changed, 632 insertions(+), 8 deletions(-)", all in this task's folder. When this Reviewer started, the session scratchpad held no `tfw/` folder, consistent with E12's removal record.
- **Limit:** the Executor's 368-file listing is an attestation of names and counts; nothing depends on it (C3).
- **Result:** HOLDS

### V10: C17 location research and docstring decision
- **Accepted claim / authority:** DoD 9 and DoD 10.
- **Subject tuple:** `research/iter1/2_gather.md` G1–G2 and addendum, `RES.md` D1–D4; TS@9216218d.
- **Action or evidence:** read the trial protocol, matrix and addendum; read the TS ruling and journal 34fa.
- **Observed:** write/read/delete trials on this machine with Codex CLI 0.152.1 (temp outcome (a), TFW roots (b)), Antigravity 1.2.12 (same) and Claude Code 2.1.289 after the owner's sign-in (`auto` passes everywhere, Manual blocks everywhere); Cursor and POSIX by vendor documentation; EV E12 cites RES iter1 D1–D4 and the H1 matrix. This Reviewer's own create/write/read under `<temp>/tfw/TFW_20261004-174815_LPF/` in a Claude Code in-session agent adds one observation. TS §4 records "owner ruling 2026-10-05 — option A", quoted in journal 34fa and HL S11.
- **Limit:** POSIX, Cursor and the Codex desktop app rest on documentation, as DoD 9 allows.
- **Result:** HOLDS

## Commands Executed

| # | Command | Claim IDs | Result |
|---|---|---|---|
| 1 | `git diff --name-status --find-renames=50% -z 6c9766fc… 0863d299… -- $valuePaths` (34 paths) | C14 | 31 M, 1 A |
| 2 | `git diff --numstat --find-renames=50% -z 6c9766fc… 0863d299… -- $valuePaths` | C14 | 32 rows, 258 + 411 = 669, 0 binary |
| 3 | `git show --name-status` per commit; `git merge-base --is-ancestor 0863d299 HEAD`; `git diff --stat 0863d299 HEAD -- $valuePaths` | C15 | exact name sets; reachable; empty |
| 4 | `git diff 9216218d 397d396f -- TS`; HL section comparison `efc915a9`→HEAD; `git status -sb`; `git branch -r --contains 0863d299` | C16 | ruling-only TS edit; frozen sections identical except rule-6 list; not pushed |
| 5 | `python wcheck.py` (61 W checks) | C1–C6, C8 | 61/61 |
| 6 | `wc -w` before/after over 19 files; `cmp` copies; block-equality script | C1–C5, C8, C9 | counts as V4; copies equal |
| 7 | census `git grep -n -E '(^|\s)(#|//)|"""'` at both SHAs over the 13 files; `grep -c '<!--' tools/README.md` | C7 | 277 → 93; 0 |
| 8 | `python astcheck.py`; `python removed.py`; YAML `safe_load` comparison | C7 | ASTs equal; 0 program-read removals; YAML equal |
| 9 | `python <base|cand>/<script> --help` ×5 and economics subcommand helps ×9 | C7, C11 | all byte-identical |
| 10 | `python <base|cand>/tools/tfw_doctor.py --root . …` ×7; economics `validate` | C11 | identical; exit 0 |
| 11 | `python -m pytest -p no:cacheprovider docs/scripts/test_gen_docs.py docs/scripts/test_integration.py tools/tests/test_git_blob_sizes.py -q` (site in working material) | C11 | 14 passed |
| 12 | `python -m pytest -p no:cacheprovider tools/tests/test_git_blob_sizes.py docs/scripts/test_gen_docs.py -q`; `… tools/tests/ docs/scripts/ -q --collect-only` | C7, C11 | 12 passed; 14 collected |
| 13 | `python -m mkdocs build --config-file docs/mkdocs.yml --site-dir <temp>/…` | C11 | exit 0; 32 pre-existing warnings |
| 14 | W9 listings 1–3 over the Candidate VALUE diff | C7 | 3 trimmed remains; 0; 5 rule-vocabulary lines |
| 15 | leak greps over the task folder and added lines; `git ls-tree -r -l HEAD`; `git diff --stat … -- workspace tasks daily tools/migrations` | C12, C13, C18 | as V9 |

Comments, docstrings and channel words the Candidate's VALUE diff adds (`verify.md` check 2): no
docstring and no Markdown comment is added; listing 1 shows three lines — `# Upstream maintainer and
documentation tests.`, `# when its profile names an existing accountable human.`, `# display
string.` — each the unchanged head of an existing setting-meaning or template-instruction comment
whose tail was deleted, so each meets `Comments`; listing 3's five lines are rule vocabulary
(`$TMPDIR`, `/tmp`, `%TEMP%`, `<temp>`, "legacy chatter", the channel-word list), no channel use.

## Claim and Source Checks

| # | Claim / citation | Where | Primary artifact / source | Holds? |
|---|---|---|---|---|
| S1 | "15,764 → 16,038 words", headings 1436/1442/1453/1463 | RF §1, E1 | Candidate file, `wc -w`, `grep -n` | ✅ |
| S2 | managed-block START/line/END numbers | E6 | Candidate files | ✅ |
| S3 | census 277 → 93 with every line classified | RF §1, E9 | census at both SHAs; my classification | ✅ |
| S4 | `--help` sizes and hash prefixes | E10 | rerun | ✅ |
| S5 | "14 passed", "12 passed", "14 tests collected" | RF §4, E10 | rerun (4.08 s) | ✅ |
| S6 | "7 files changed, 632 insertions(+), 8 deletions(-)" | E13 | rerun | ✅ |
| S7 | leak grep hits only TS 195, 283, 349 | RF AC-9, E12 | rerun, case-sensitive | ✅ |
| S8 | 32 MkDocs warnings, none on a changed page | RF §4 | rerun | ✅ — none on a changed line |
| S9 | handoff step 10 hand-over superseded by approved W4 | RF §3 | TS approval `9216218d`; W4 | ✅ |
| S10 | sandbox trials for Claude Code and Codex | DoD 9, E12 | RES iter1 G1–G2, addendum | ✅ |

## Guard and Check Admission

| # | Kind | Protected behavior / invariant | Failure consequence | Counterfactual detection | Admission |
|---|---|---|---|---|---|
| G1 | positive control | docs generator behavior, rendered site, 5 MiB blob boundary | a regression in retained surfaces | existing suite; passes before and after; not designed to detect comment removal | labelled control |
| G2 | temporary diagnostic | published module docstrings (`--help`) | a published docstring changed or lost | any byte change in a published docstring changes `--help` bytes | temporary |
| G3 | temporary diagnostic | no code change beyond docstring removal | behavior drift hidden in a cleanup | any non-docstring edit changes the AST dump | temporary |
| G4 | temporary diagnostic | doctor and economics outputs | maintainer/shipped helper regression | Baseline vs Candidate scripts on one input | temporary |
| G5 | governance assertion | W9 listings, census, `verify.md` checks | correspondence re-enters value files | lists lines for human judgment; no automated verdict | governance only |

No permanent guard is added or claimed.

## Candidate Findings

| ID | Class | Subject | Affected claim / authority | Observed fact + oracle | Concrete harm | Material consequence or named absence | Owner | Observable completion | Route / rung | Candidate effect | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| O1 | TRACE | AC-9 literal gate | C12 | the gate "returns nothing" cannot pass: the TS's own lines 195, 283, 349 contain the searched word; no leak exists (V9) | none | none — the protected object is intact | Coordinator | none required | observation | unchanged | observation |
| O2 | VALUE | `### Working material`, one folder per task | C1 (W2.2) | the path `tfw/<task or Daily record ID>/` is shared by every role of a task on one machine; the Executor removed the whole folder and its `tfw/` parent (E12). A role that removes the folder rather than only its own material can delete another role's retained or in-flight material | lost working material and rework for the other role | none for acceptance: material is non-authoritative, no claim may rest on it (C3) and observations enter EV when made; the wording is owner-approved (S10) | owner, at a later rule task if wanted | none required for this task | observation | unchanged | observation |
| O3 | TRACE | Coordinator's own helper files | C7, Closing step 6 | four `lpf_*.py` helper files sit in the session scratchpad root (system temp, outside the project) rather than under `tfw/<ID>/`; names only were seen | none (outside the project) | none; Closing step 6 removes them | Coordinator | removal recorded at close | Closing step 6 | unchanged | observation |
| O4 | TRACE | glossary `Evidence Status Vocabulary` | out of scope | it cites heading `Evidence Table`, which the EV template has never had (`## Evidence` at Baseline and Candidate) | a reader resolving the authority meets a missing heading | none for this task; pre-existing | Coordinator | none required here | observation for routing | unchanged | observation |

No material finding. RF §6 observations 1 (broken changelog links to unpublished guides) and 2
(the retained MkDocs test builds `site/` inside the project unless `TFW_ASSURANCE_SITE_DIR` is set)
are confirmed and remain out of scope.

## Evidence Verification

`evidence/` holds only EV files; no verdict rests on working material.

| # | EV row | Subject tuple | Repeated or opened? | Establishes the claim? | Limit |
|---|---|---|---|---|---|
| E1 | E1 | conventions@Candidate | ✅ | ✅ | none |
| E2 | E2 | EV template@Candidate | ✅ | ✅ | none |
| E3 | E3 | handoff, copy, verify@Candidate | ✅ | ✅ | row-writing order is attested, not repeatable; TRACE only |
| E4 | E4 | Daily skill/template, entries@Candidate | ✅ | ✅ | none |
| E5 | E5 | live Daily record | ❌ DEFERRED by TS | ⚠️ deferred, actor named | next Daily turn after release |
| E6 | E6 | templates, installed copies@Candidate | ✅ | ✅ | none |
| E7 | E7 | guide, changelog@Candidate | ✅ | ✅ | none |
| E8 | E8 | receiver update | ❌ DEFERRED by TS | ⚠️ deferred, actor named | next receiver update |
| E9 | E9 | 13 files + README@Candidate | ✅ | ✅ | none |
| E10 | E10 | scripts, tests@Candidate, this machine | ✅ | ✅ | pytest pin |
| E11 | E11 | knowledge, profile@Candidate | ✅ | ✅ | none |
| E12 | E12 | task folder@Candidate/HEAD; working folder | ✅ | ✅ | removal listing attested |
| E13 | E13 | frozen roots Baseline→Candidate | ✅ | ✅ | none |
| E14 | E-accounting | Baseline/Candidate, 34 paths | ✅ | ✅ | none |

## Knowledge Citations Verified

PV scan: P0 NS1–NS3 and P1 `Methodology values`/`Success Criteria` read separately; P2
`knowledge/philosophy.md`, P3 `KNOWLEDGE.md` §1, P4 `HL (High Level)`, `Design Rules`, `Anti-patterns`
scanned fully; P5–P7 searched for comment, docstring, evidence and attachment facts — only F43
(ONB §7 row 29) bears on the change, and no P7 file does.

| # | Artifact | Priority + exact citation | Resolves? | Item exists? | Meaning matches? | Relevant? |
|---|---|---|---|---|---|---|
| 1 | HL §7.2 | P0 NS1 "inspect its material grounds … without rebuilding the original conversation" | ✅ | ✅ | ✅ quote present | ✅ registry keeps grounds inspectable |
| 2 | HL §7.2 | P0 NS2.2 "Subtraction is not improvement when it damages … inspectability, or continuation" | ✅ | ✅ | ✅ | ✅ bounds the cleanup |
| 3 | HL §7.2 | P0 NS2.4 "do not archive everything" | ✅ | ✅ | ✅ | ✅ |
| 4 | HL §7.2 | P0 NS2.7 "subtract ceremony that does not protect the purpose" | ✅ | ✅ | ✅ | ✅ |
| 5 | HL §7.2 | P0 NS3 raw chat archive; documentation factory | ✅ | ✅ | ✅ (elided "a prompt collection", as ONB notes) | ✅ |
| 6 | HL §7.2 | P1 Structural Enforcement | ✅ | ✅ | ✅ | ✅ `git status`, EV shape, verify checks |
| 7 | HL §7.2 | P1 Portability | ✅ | ✅ | ✅ | ✅ no machine path in trace |
| 8 | HL §7.2 | P1 Success Criteria 2 | ✅ | ✅ | ✅ | ✅ |
| 9 | HL §7.2 | P2 F22 «Не захламляй шаблон» | ✅ | ✅ | ✅ | ✅ EV loses Attachments |
| 10 | HL §7.2 | P2 F40 missing term | ✅ | ✅ | ✅ | ✅ *working material* named |
| 11 | HL §7.2 | P2 F41 framework satisfies its own rule | ✅ | ✅ | ✅ | ✅ C7 |
| 12 | HL §7.2 | P2 F30 evidence → attestation → proof | ✅ | ✅ | ✅ | ✅ C3 |
| 13 | HL §7.2 | P3 D52, D53 ("Optional = never happens"; owner's folder quote) | ✅ | ✅ | ✅ case differs only | ✅ folder stays mandatory |
| 14 | HL §7.2 | P3 D31 | ✅ | ✅ | ✅ | ✅ |
| 15 | HL §7.2 | P3 D82 | ✅ | ✅ | ✅ | ✅ no code added |
| 16 | HL §7.2 | P4 `Evidence subfolder` | ✅ | ✅ | ✅ rewritten as intended | ✅ |
| 17 | HL §7.2 | P4 `Safety and Execution Honesty` "file path or inline output" | ✅ | ✅ at Baseline; replaced by W2.1 | ✅ | ✅ |
| 18 | HL §7.2 | P4 `Design Rules` ≤1,400; ceiling not permission | ✅ | ✅ | ✅ | ✅ DoD 3/4 |
| 19 | HL §7.2 | P4 `Anti-patterns` | ✅ | ✅ | ✅ two folded, none weakened | ✅ |
| 20 | HL §7.2 | P4 `Semantic value-bearing classification` | ✅ | ✅ | ✅ | ✅ W2.5 |
| 21 | HL §7.2 | P5 F9 | ✅ | ✅ | ✅ | ✅ |
| 22 | HL §7.2 | P6 F23, F29, F32, F37, F50 | ✅ | ✅ | ✅ | ✅ |
| 23 | HL §7.2 | RES iter2 D13–D21, W1–W9; RES iter1 D1–D12 | ✅ | ✅ | ✅ | ✅ ground of the TS |
| 24 | ONB §7 | rows 1–28 restate the HL citations with applications | ✅ | ✅ | ✅ | ✅ |
| 25 | ONB §7 | row 29 P6 F43 "The reason has to live at the point of confusion" | ✅ | ✅ | ✅ | ✅ tension with C5, held for the knowledge route |

## Accounting Replay

| Approval / authority | Baseline | Candidate | Literal VALUE membership / actions / classes / reasons | Adds | Deletes | Touched LOC | Binary | Trigger disposition | Exact NUL-safe command | Verdict |
|---|---|---|---|---:|---:|---:|---|---|---|---|
| owner at `9216218d`; ruling 1 at `397d396f` before the Candidate | `6c9766fcb2de252e010a790b0fbe676f02058f7c` | `0863d299d86a1ca1776ffb966d54a1b848e7c348` | 34 literal TS §4 `VALUE` paths; 31 M + 1 A changed, 2 unchanged, 0 renames/deletes; no path outside the selector; `tools/migrations/2.0.0/**` untouched | 258 | 411 | 669 | N/A — no binary row | 32 / 669 below triggers 50 / 5,000 and multiplier 66 / 2,000; no split | TS §4 commands, unchanged | VERIFIED |

## Selected Knowledge Evidence

| Source / epoch | Producer / unit | Scope | Authority | Applicability |
|---|---|---|---|---|
| RES iter1 @`57159eac` | `lpf-researcher` (dispatch 71eb) | H1, H2, H5, H7; D1–D12 | Coordinator rulings at each stage | location, row form, comment draft, docstring options |
| RES iter2 @`9313bd8a` | `lpf-researcher` (dispatch 2d7e) | H3, H4, H6, subtraction; W1–W9 | Coordinator rulings; owner saw W at TS stop | exact rule text |
| ONB @`be8fb05d`; RF @`e19b8a52`/`b38f4db2`; EV | `lpf-executor` (dispatch 34fa) | Candidate and its evidence | TS approval and ruling 1 | verified above |
| Ruling 1 @`397d396f` | Task Coordinator | one VALUE path, AC-7 list | handoff Step 2; change-authority rule | prospective, held |
| HL §11 S1–S11 | owner quotes via Coordinator | purpose, value, approvals | owner | owner-sourced inputs for knowledge at close |
| RES iter1 FC1 | Coordinator's answer from field reports | receiver stacks | not human-direct | not admissible alone for qualification |
| economics roles ×3 | Researcher ×2, Executor | numeric TRACE | own sources | validated, hashes match names |

## Checkpoint

**Self-check:**
- [x] Replayed the Map selection and verified all mandatory safety/security, authority and identity floors?
- [x] Established evidence applicability and ran every TS-required or dependency-affected check?
- [x] Recorded explicit limits instead of substituting file, discrepancy, test, commit or artifact counts?
- [x] Classified guards and controls by protected behavior, consequence and counterfactual detection?
- [x] Recorded every candidate finding with the complete item contract and material consequence test?
- [x] Verified RF AC claims, evidence references, citations and immutable accounting against actual artifacts?

Stage complete: YES
