# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20261004-174815_LPF](../../HL-TFW_20261004-174815_LPF.md)
> Goal: A TFW project holds only the result and the selected trace: working material lives outside the project under the task ID and is gone when the task closes, and a comment carries value or is absent.
> Producer unit: `claude-code:agent:local_a7cf0ab7-482d-403e-b738-504d82bba898/lpf-researcher` (native agent `a2f09276b39617fd0`); mode focused, one pass. Inputs: `2_gather.md` with its Claude Code addendum of 2026-10-04 and the Coordinator's ruling at the Gather stop.

## Configuration Space

Dimension names as in Gather. The seven dimensions form two independent groups: D1–D4 cover where
working material lives and what a verdict may rest on; D5–D7 cover the comment rule. Crossing the
two groups adds no constraint, so each group is crossed on its own.

### Working material and verdict basis (D1 × D2 × D3 × D4)

| Config | D1 Working-material root | D2 How a sandboxed role reaches it | D3 Removal | D4 Basis for an observation that cannot be repeated |
|---|---|---|---|---|
| K1 | TFW root (`~/.tfw/work/<ID>/`, or split by OS) | one-time per-tool setting | Closing step 6 | items the TS names as retained, read by the Reviewer |
| K2 | TFW root | per-action human approval | Closing step 6 | the EV row as attestation |
| K3 | TFW root | role runs without a sandbox | Closing step 6 | the EV row |
| K4 | system temporary directory | nothing needed | Closing step 6, earlier OS cleanup tolerated | the EV row |
| K5 ★ | system temporary directory, private to the role that created it | nothing needed | by the creating role before its return; Closing step 6 removes what is left in its own view | the EV row carries the printed output; nothing passes between roles |
| K6 | system temporary directory | nothing needed | after the Reviewer's verdict | the Executor's working material while it exists |
| K7 | ignored folder inside the project (the DoF 2 fallback) | nothing needed | Closing step 6 | the Executor's working material or the EV row |
| K8 ★ | the role's own disposable worktree under `<tfw-home>/worktrees/` | nothing needed: it is that role's workspace | with the worktree at Closing step 6 | the EV row |
| K9 ★ | K5 for scratch, plus the TFW root only for items a high-risk TS names as retained | temp: nothing; root: one-time setting | scratch before the return; retained items at Closing step 6 | retained items for that TS only, otherwise the EV row |

★ not proposed in the Briefing or the HL. Left out as contradicted: a TFW root with "nothing
needed" (E1: outcome (b) in Codex and Antigravity); removal at each role's return combined with a
Reviewer who reads the Executor's material.

### The comment rule (D5 × D6 × D7)

| Config | D5 Status of docstrings | D6 Reviewer's check | D7 "Historical" prose in `.tfw/` |
|---|---|---|---|
| M1 | a comment like any other: value or absent | listed command over the Candidate diff plus judgement of each listed line | hand to the agreed separate task |
| M2 | always allowed | listed command | separate task |
| M3 | allowed only when a program reads it | listed command | separate task |
| M4 | allowed when a program reads it or it documents a public interface | full read of every changed file | remove restatements now |
| M5 ★ | a comment like any other; a docstring a program publishes is output text, judged for the reader of that output | listed commands for comments, docstrings and channel words in identifiers of the VALUE diff | chatter removed only where its file changes anyway; restatements to the separate task |

Left out as contradicted: linter configuration in receivers (C6: no update rewrites receiver code;
C8: nothing new is added).

## Findings

### E1: H1 — every surface in one matrix

Classes as fixed in G1, plus the Coordinator's auto-mode rule. "Doc" means vendor documentation only.

| Surface and default mode | System temp | `~/.tfw/work/<ID>` | `%LOCALAPPDATA%\tfw\work\<ID>` | Basis |
|---|---|---|---|---|
| Codex CLI 0.152.1, `exec --sandbox workspace-write`, Windows sandbox `unelevated` | (a) | (b) | (b) | trial (G2) |
| Codex app and interactive CLI ("Auto": workspace write, on-request approvals) | (a) | (b) | (b) | doc: same native sandbox; the app was not driven |
| Codex on macOS/Linux | (a): `/tmp` and `$TMPDIR` are writable roots | (b) | — | doc |
| Antigravity `agy` 1.2.12, `request-review`, file tools | (a) | (b) | (b) | trial (G2); its terminal tool needs approval everywhere, workspace included |
| Claude Code 2.1.289, `auto` (interactive default) | (a)\* | (a)\* | (a)\* | trial (addendum) |
| Claude Code 2.1.289, `default` = Manual (headless default) | (b) | (b) | (b) | trial (addendum); every write needs a human, workspace included |
| Claude Code with its sandbox on (macOS/Linux/WSL2; off by default) | (a): its per-user temp, published as `$TMPDIR` | (b) | — | doc |
| Cursor, Auto-review, terminal sandbox (macOS/Linux; not installed here) | (a) unless `disableTmpWrite` | (b): External-File Protection | (b) | doc |
| The owner's own settings: Codex `danger-full-access`, Claude Code `bypassPermissions` | writable | writable | writable | G2 |

\* automatic check, nondeterministic.

Pattern: wherever any location outside the workspace is (a), the temporary directory is one of them.
The TFW roots are never better than temp, and they are worse in Codex, Antigravity and Cursor.
Claude Code is the only surface that treats them the same. Claude Code's sandbox allows only its own
per-user directory, which it publishes as `$TMPDIR`. So a temp location must be resolved through
the variable (`$TMPDIR`, else `/tmp`; `%TEMP%` on Windows), not written as a literal `/tmp`.

### E2: Settings that remove outcome (b)

| Tool | Setting | Tried here | Result |
|---|---|---|---|
| Codex | `[sandbox_workspace_write] writable_roots = […]` in `~/.codex/config.toml`, described as "Additional writable roots when `sandbox_mode = "workspace-write"`" in the config reference; or `--add-dir <DIR>` per run | yes, Windows `unelevated`, three runs: the config key with workspace and root on different drives; `--add-dir`; the config key with both on one drive | **every command refused, the workspace control included**: `UnsupportedOperation("windows unelevated restricted-token sandbox cannot enforce split writable root sets directly; refusing to run unsandboxed")`. The vendor's tracker reports the same error, including in the Windows desktop app (openai/codex #34970, open when read; also #32168, #35864, #30712). `elevated` was not tried: its setup creates sandbox users and changes firewall and local policy. macOS/Linux: documented only |
| Antigravity | allow rule `write_file(<path>)` under `permissions.allow` in `settings.json`, named in the tool's own denial message and on its permissions page; `--add-dir` per run | `--add-dir` only | no effect: the write into the added folder was still denied in headless `request-review`. The allow rule was not tried because it changes the owner's persistent settings |
| Claude Code | `permissions.additionalDirectories`, `--add-dir`, `/add-dir` | `--add-dir` in Manual | works: a read in the added folder ran without approval, a read outside it was denied, and a write in it still needed approval exactly as in the workspace. Per the vendor page, additional directories follow the working directory's rules, so edits there are approved in `auto` without the classifier |
| Cursor | `additionalReadwritePaths` in `~/.cursor/sandbox.json` (all workspaces) or `<workspace>/.cursor/sandbox.json` (sandbox reference) | not installed | documented only |

Consequence: today no setting makes a TFW root writable for Codex on Windows while its sandbox is on.
Choosing a TFW root would leave Codex receivers on Windows at outcome (b), which is DoF 2 for anyone
who keeps the default sandbox. All remedy trials used throwaway folders beside the TFW roots, never
the roots themselves.

### E3: Which location works everywhere

| Criterion | TFW root `~/.tfw/work` | TFW root split by OS | System temp | Ignored folder in the project |
|---|---|---|---|---|
| Writable in default modes (E1) | (b) in Codex, Antigravity, Cursor | same | (a) wherever any outside location is | (a): it is the workspace |
| Setting that removes (b) (E2) | none works in Codex on Windows; untried in Antigravity | same | none needed | none needed |
| Survives to Closing step 6 | yes | yes | not guaranteed: tmpfs is emptied at reboot, Linux `/tmp` is cleaned after 10 days, macOS `/tmp` after 3 days unaccessed, Windows Storage Sense when it switches itself on (G4) | yes |
| One path for every role and tool | yes | yes, per OS | no: Claude Code's sandbox rewrites `$TMPDIR`; the macOS per-user `$TMPDIR` differs from `/tmp` | within one checkout only |
| Reference form | `<tfw-home>/work/<ID>/…` | same | `<temp>/tfw/work/<ID>/…` | project-relative |
| Existing TFW roots (G5) | matches `rates`; differs from Windows `bindings` and `worktrees` | matches `bindings` and `worktrees`; differs from `rates` | adds no TFW root, so the Windows split does not spread | contradicts C1 "outside the project tree" |
| Who can remove it at Closing step 6 | the Coordinator, if allowed to write there | same | reliably only a role of the same tool and OS user | anyone |

**No location meets every criterion.**
- **Temp:** wins on writability, loses on survival and on a shared path. Both losses matter only
  when material must outlive the creating role's return or pass to another role or tool. C3 already
  forbids a verdict that depends on another role's working material.
- **K5:** if each role keeps its material private and removes it before returning, temp's weak
  points stop mattering, nothing new is added, and the Windows root split does not spread. K5 reads
  the §3.2 picture's "Executor and Reviewer look at it while it matters" as each role looking at its
  own material. If the owner meant shared material, K5 conflicts with that picture, though not with
  C1–C8.
- **A durable shared home** is then needed only when a high-risk TS names retained items (K9, the
  HL's DoF 1 route). That home has no working setting in Codex on Windows today (E2). Such a task
  falls back to the ignored folder in the project (K7) or retains nothing (E4).
- **K8** works only for roles that have their own worktree. It also leaves untracked files in that
  worktree's `git status`, which is the signal C8 relies on, so it is weaker than K5.
- **If a TFW root is chosen anyway** (K1, K9), the Windows convention matching both existing
  Windows uses (`bindings`, `worktrees`) is `%LOCALAPPDATA%\tfw\work\<ID>\`; `rates` is the
  outlier.

### E4: H2 — the three verdicts that rested on executor data

| Case | What the verdict used | Can it be repeated? | What a registry row must carry | What is lost without the bytes |
|---|---|---|---|---|
| RTPSN `phase-a/review/verify.md` V7–V8: live model trials | `command-entry-trials.jsonl`: 9 records, 162,705 bytes (7 attempts × 27 fields with events, hashes and grader results), recomputed with `summary --check` | no: nondeterministic, ≈0.7 M tokens | per attempt: arm, outcome, grader result and usage; the totals and stop arithmetic; the harness command and commit | the check that the summary matches the raw events. The Reviewer can re-check the row's arithmetic, the harness at the Candidate and a bounded re-run, not the original attempts |
| FA15ES `review/verify.md` V8, E12–E13: renders | two committed PNGs, opened at original resolution | yes: the builder is in the Candidate | the render command and commit; what was seen | nothing: the Reviewer renders and opens its own output |
| TKL `REVIEW__TFW_20260909-231654_TKL.md` O1: a 600-second bound | timestamps in a 1,596-byte raw seal file (`deadline`, `entry_completed_at`, `raw_result_sealed_at`, `observed_at`) | no: the timing of a past run | the printed timestamps themselves, not "within bound" | nothing, if the row carries them: the 40-second overrun is then visible in the row |

Inputs for the decisions:
- **C3.** "Repeat or open" covers renders, builds, tests and counts. When an observation cannot be
  repeated, the Reviewer can establish the method, the harness at the Candidate and the row's own
  arithmetic. The observed values remain the Executor's attestation (F30: evidence → attestation →
  proof). C3's second clause still holds, because the row is trace, not working material.
  - The TS must add how such a claim is labelled and when it may be accepted.
  - In Gather's census, 2 of 343 review documents had such a claim (RTPSN, TKL).
- **C2, through F32.** What protects the verdict is the form of the row's "observed" column: the
  printed output (values, timestamps, counts), not a conclusion. The only defect found solely in raw
  data (TKL O1, ruled not material) would have been visible in a row of that form.
- **C1.** If the row has that form, none of the three cases needs working material after the
  creating role returns. Retention is needed only when the TS wants the original attempts
  re-examined (RTPSN type). Retained items then need a home that survives and that both roles can
  reach, and temp is neither (E3).

### E5: H5 — comment forms, exception list, a check without code

Forms by reader. Receivers' stacks, per the Coordinator: Python (FastAPI, scripts), some JS/TS,
Markdown-only projects, YAML everywhere.

| Form | Example | Reader | Under C5 |
|---|---|---|---|
| Interpreter or encoding line | `#!/usr/bin/env python3`; `# -*- coding: utf-8 -*-` | OS, interpreter | kept byte for byte |
| Tool directive | `# noqa: E402`; `# pragma: no cover`; `// eslint-disable-next-line`; `// @ts-expect-error`; `/// <reference …/>`; `# yamllint disable-line`; `# yaml-language-server: $schema=…`; `<!-- markdownlint-disable -->` | linter, type checker, coverage tool, editor | kept byte for byte |
| License header | `SPDX-License-Identifier: …` | scanners, people | kept |
| TFW managed-block marker | `<!-- TFW:CODEX:START -->` / `END` | install and update | kept byte for byte (DoF 3) |
| Docstring a program publishes | module docstring as `--help` (`description=__doc__`, five scripts here); FastAPI endpoint → OpenAPI; FastMCP tool → the description the model reads; Typer command help; doctest examples | the reader of that output: a CLI user, an API client, the model choosing a tool; the doctest runner | kept while it says what that reader needs; narrative inside it is correspondence |
| Configuration comment that explains a setting | `task_prefix: TFW  # project prefix for current and legacy identifiers` | whoever edits the file | kept (C5) |
| Instruction comment in a template or prompt | HTML comments in `.tfw/templates/` | the agent filling the template | kept: value for that file's reader |
| Restatement of the code | `def load(path):  # read the file` | nobody | absent |
| Reason, history, migration note, restated shared rule | `# Legacy: kept for v2 clients` | a future agent | absent: the reason lives in the trace |
| Deferred work, excuse, message, joke, notification | `# TODO: remove after migration` | another agent | absent |

Exception list, draft wording for the TS (Coordinator's and owner's decision):

> A comment stays only when a program reads it (interpreter or encoding line, tool directive,
> license header, TFW managed-block marker), kept byte for byte, or when it tells that file's reader
> what the file cannot: what a setting means and which values it takes, the instruction a template
> gives the agent who fills it, or, in a docstring a program publishes, what the reader of that
> output needs. Reasons, history, restated rules or code, deferred work and messages to other agents
> are absent; the reason lives in the trace.

Boundary cases for the configuration exception, from deliverable-6 files:
- `.tfw/project_config.yaml:14–15`: says what a change of disposition does and which migration guide
  holds the procedure. Borderline.
- `.tfw/templates/bindings.yaml:30–31`: restates a rule about profile files, not about this file's
  settings. Fails "explains a setting".
- `.tfw/templates/project_config.yaml:23–24`: says why a fresh project has no historical setting.
  Passes.

Docstring options for the owner's ruling, which HL §4.1 reserves:

| Option | For | Against |
|---|---|---|
| A — a comment like any other | one rule; the five `--help` docstrings stay because a program prints them | needs the clarification that a program-read docstring is judged by the reader of its output |
| B — always allowed | nothing to judge | the HL's loophole: `tools/migrations/2.0.0/migrate_board.py` already carries a 31-line narrative module docstring that `--help` prints |
| C — only when a program reads it | mechanical | removes documentation that IDE hovers and `help()` show to people |
| D — program-read or public interface | keeps library documentation | "public interface" is undefined in script-heavy receivers |

M5 is option A with that clarification.

The Reviewer's check without code. The commands are listed; the judgement stays with the Reviewer.
1. Added comment and docstring lines in the Candidate's VALUE diff; each listed line is judged
   against the exception list:
   `git diff -U0 <Baseline> <Candidate> -- <VALUE paths> | grep -E '^\+[^+]' | grep -E '^\+\s*(#|//|/\*|\*|<!--)|\s(#|//)\s|"""'`
2. Channel words in added identifiers and strings:
   `git diff -U0 <Baseline> <Candidate> -- <VALUE paths> | grep -E '^\+[^+]' | grep -i -o -E '\w*(legacy|deprecated|todo|fixme|hack|workaround|compat|old|temp|tmp)\w*' | sort | uniq -c`
3. The DoD 7 census over whole deliverable-6 files after cleanup:
   `git grep -n -E '(^|\s)(#|//)|"""|<!--' -- <deliverable-6 paths>`. Every remaining line must be
   program-read or a value configuration comment, classified in the EV row. Size today: 162
   full-line and 10 inline Python comments, 110 docstring delimiter lines and 97 configuration
   comment lines. That is a reading task, not a tool.

Commit messages are trace, not value files, so C5 does not reach them. A deferred-work note in a
commit body means work left undone, which the Reviewer's existing TS check finds. No extra check is
needed.

**H5 status.** The first false case holds: the Executor of this task needs docstrings for a tool
(five `argparse` scripts, one of them shipped to receivers). The second does not: the check is two
`grep` pipelines and a census. The HL's consequence applies: docstrings are admitted where a program
reads them, judged for the reader of the output.

**Scope note for the TS.** Deliverable 6 names `tools/`, which contains
`tools/migrations/2.0.0/migrate_board.py`, the maintainer copy of a 2.0.0 migration tool removed from
the payload in 3.0.0 (`migrations/3.0.0.md`). It is not pinned by hash in `.tfw/`. Whether it counts
as a historical folder under C7 is a scope question for the TS.

### E6: H7 — all 169 lines classified

Criteria as fixed in G10. "Restatement" means an operative rule stated in full elsewhere in live
`.tfw/`, checked with `git grep` for each cluster. "False match" means the word does not refer to a
retired form or an old receiver.

| Group | Lines | Protective rule | Restatement | Chatter | False match |
|---|---|---|---|---|---|
| `conventions.md` | 41 | 37 | 3 | 0 | 1 |
| `workflows/` (10 files) | 48 | 30 | 14 | 1 | 3 |
| `glossary.md` | 10 | 5 | 4 | 0 | 1 |
| `templates/` (12 files) | 32 | 17 | 12 | 0 | 3 |
| `adapters/` (8 files) | 10 | 3 | 5 | 1 | 1 |
| other: `README.md`, `quickstart.md`, `compilable_contract.md`, `economics/`, `extensions/`, `project_config.yaml` | 28 | 17 | 3 | 0 | 8 |
| **Total** | **169** | **109** | **41** | **2** | **17** |

Of the 152 lines in scope, 150 are rules (98.7%) and 2 are chatter, so H7 holds under this
classifier.

The two chatter lines:
- `workflows/knowledge.md:122`: "Before TKL, this section defined the global pending/digest gate".
  The next two lines, which the pattern does not match, continue the history. The paragraph's last
  clause is operative ("this legacy link reinstates no task sweep…").
- `adapters/antigravity/coordinator.md:55`: a note about one past task (PCUX). The rule it points to
  lives in the shared coordination contract.

Five rules account for 33 of the 41 restatements:
1. **Absent routing fields.** "Total absence of the routing fields is legacy read-only and cannot
   activate new work." Stated at `conventions.md:637`; repeated 7 times: `:657`, `:959`,
   `templates/status.md:97`, and word for word in four workflows (`docs.md:34`, `knowledge.md:36`,
   `release.md:35`, `research/base.md:50`).
2. **GATEWAY/LEAD.** "Historical GATEWAY/LEAD carriers remain readable." Stated at
   `conventions.md:352` and `:1158`; repeated in all four adapter root templates, which every
   receiver loads at every session start.
3. **Role-lock prohibitions.** Copied from the `conventions.md` role table: `docs.md:13`,
   `knowledge.md:14`, and line 14 of the Codex `tfw-docs` skill.
4. **Knowledge-lifecycle preservation.** Legacy rows are not converted, `knowledge_state.yaml` stays
   inert, and legacy targets are cited as `conventions.md:1361` prescribes. Repeated 14 times across
   `knowledge.md`, `docs.md`, `update.md`, the knowledge templates, the glossary, `quickstart.md`
   and `conventions.md:1382`.
5. **`actor` and `may_rule_amendments`.** "Readable, never issued." Stated at
   `conventions.md:301–302` and `:309`; repeated in `templates/journal/event.md` (twice),
   `templates/team/profile.md` (twice) and `templates/bindings.yaml:30`.

The other 8 restatements are single repeats of other rules.

The 17 false matches break down as follows:
- 12 use "historical" for past prices, valuations or recollection, in economics text and program
  messages.
- 3 refer to "historical red-before-green" in review guidance.
- 1 is a "historical defect count".
- 1 is Claude Code's own "legacy slash-command" feature.

Inputs for the decisions:
- **C5.** The wording in `.tfw/` is rule, not correspondence, and C5 holds going forward without
  cleaning it. The owner's impression (S9) is better explained by repetition and density than by
  notes between agents: one rule stated eight times, and the same legacy line in every adapter root
  template.
- **Chatter scope.** The two chatter lines are trivially small, but neither file is in the
  deliverable list. Deliverable 5 changes the adapter root templates, not
  `antigravity/coordinator.md`.
- **Restatement scope.** The 41 restatements are the larger subtraction, but many are point-of-use
  copies under selective reading. Each workflow's Read Contract loads only some `conventions.md`
  headings, and the adapter root templates are what a session reads first. Removing one needs a
  check against every Read Contract that reaches it; that is the agreed separate task. Four of the
  41 sit in adapter root templates that deliverable 5 changes anyway.

### E7: Queries, files, trials and side effects

**Web queries (5, within the soft limit):** the Codex config reference; a Cursor `sandbox.json`
search and the sandbox reference page; a search for the Codex split-roots error; openai/codex issue
#34970.

**Project files opened** (soft limit exceeded, each file named):
- Stage and task inputs: `research/base.md`, the HL, `1_briefing.md`, `iterations.yaml`,
  `status.md`, `templates/research/3_extract.md`.
- H7 context: `conventions.md`, `workflows/knowledge.md`, `release.md`, `init.md`, `economics.md`,
  `review.md`, `adapters/antigravity/coordinator.md`, `compilable_contract.md`,
  `extensions/daily-task/SKILL.md`, `project_config.yaml`, `templates/project_config.yaml`,
  `templates/bindings.yaml`, `templates/status.md`, `templates/review/verify.md`,
  `templates/update_receipt.md`, `templates/team/profile.md`, `templates/knowledge/topic.md`.
- H2: the RTPSN trials file and the TKL seal file, size and field names only.
- H5: `migrations/2.0.0.md` and `3.0.0.md`, by grep.

**Trials in this stage:** Codex ×3, Antigravity ×1 and Claude Code ×1, using two throwaway folders
beside the TFW roots and throwaway workspaces. The Claude Code trials for H1 itself are in Gather's
addendum.

**Side effects:**
- All trial folders were removed.
- `icacls` output for `%LOCALAPPDATA%` and the profile root matches a fingerprint taken before the
  trials.
- Antigravity keeps one more headless conversation in its local history.
- Codex ran with `--ephemeral` and Claude Code with `--no-session-persistence`.

**Correction to Gather.** In the Antigravity trials (G2), a quoting slip created a folder literally
named `work$ID` instead of `work\<ID>` under each root. The root, and therefore the class, is
unchanged; the Codex trials used the correct path.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| H1: system temp is (a) wherever any outside location is; the TFW roots are (b) in Codex, Antigravity and Cursor; Claude Code treats both the same (auto (a)\*, Manual (b)) | macOS/Linux and the Codex app rest on documentation; Codex `elevated` untried |
| H1: no setting makes a TFW root writable for Codex on Windows with its sandbox on (a known vendor defect); Antigravity `--add-dir` does not help; Claude Code `--add-dir` works | Antigravity allow rule untried (persistent setting) |
| C1 input: temp works only as role-private scratch (K5); a durable shared home is needed only for TS-named retained items (K9) | Challenge: temp cleanup mid-role; Executor and Reviewer on different tools; K5 against the owner's reading of §3.2 |
| H2/C3: in Gather's census, 2 of 343 reviews rested on unrepeatable executor data and 1 on repeatable renders; the row's "observed" must be the printed output | Challenge: what makes a row insufficient (RTPSN type) |
| H5: docstrings are program-read in five scripts here, so they are admitted with the output-reader test; the check is two greps and a census | Owner's docstring ruling at the TS; `migrate_board.py` scope |
| H7: 150 of 152 in-scope lines are rules, 2 are chatter; 41 restatements, 33 of them in five rules | Challenge: a stricter classifier; which restatements are point-of-use copies |

**Sufficiency:**
- [x] External source used? 5 queries and fetches (vendor references, the Codex issue tracker)
- [x] Briefing gap closed? Yes, Claude Code included (Gather addendum)
- [x] Configuration Space built from Gather dimensions? Yes: K1–K9 and M1–M5; K5, K8, K9 and M5 were not proposed

**Knowledge handover:**
- **Material:** as above.
- **Uncertainty:** Claude Code's auto results are nondeterministic by nature; the Codex Windows
  defect may be fixed in a later version; POSIX and the Codex app are documented only.
- **Publication:** no knowledge publication.
- **Continuation:** on the Coordinator's answer, Challenge.

Stage complete: YES
→ User decision: ___
