# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20261004-174815_LPF](../../HL-TFW_20261004-174815_LPF.md)
> Goal: A TFW project holds only the result and the selected trace: working material lives outside the project under the task ID and is gone when the task closes, and a comment carries value or is absent.
> Producer unit: `claude-code:agent:local_a7cf0ab7-482d-403e-b738-504d82bba898/lpf-researcher` (native agent `a2f09276b39617fd0`); mode focused, one pass. Inputs: `2_gather.md` with its addendum, `3_extract.md`, and the Coordinator's ruling at the Extract stop.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|---|---|---|---|---|
| D1 root | TFW root | D2 reach | nothing needed | contradicted by trials: outcome (b) in Codex and Antigravity (G2) |
| D1 root | TFW root | D2 reach | one-time setting, for Codex on Windows `unelevated` | the setting makes Codex refuse every command (E2); a vendor defect, open |
| D1 root | system temp | D3 removal | survival guaranteed until Closing step 6 | tmpfs, Linux `/tmp` age cleanup, macOS `/tmp` and Windows Storage Sense can delete it earlier (G4) |
| D1 root | system temp | D4 basis | another role reads the Executor's material | the temp path differs between tools: Claude Code's sandbox rewrites `$TMPDIR` (E1) |
| D1 root | ignored folder in the project | C1 (frozen) | "outside the project tree" | allowed only as the DoF 2 failure route |
| D2 reach | per-action human approval | Q1 rule | unattended roles | a prompt nobody answers is a block: outcome (b), a DoF 2 risk |
| D3 removal | when the creating role ends | D4 basis | another role reads the Executor's material | the material is gone before the Reviewer starts |
| D4 basis | another role's working material | C3 (frozen) | "a verdict never depends on another role's working material" | direct contradiction |
| D5 docstrings | always allowed | C5's purpose | no correspondence in value files | `migrate_board.py` already carries a 31-line narrative module docstring (E5) |
| D6 check | linter configuration in receivers | C6, C8 (frozen) | no update rewrites receiver code; nothing new is added | direct contradiction |
| D7 prose | clean all of it in this task | scope ruling | the agreed separate task | Coordinator's ruling at the Extract stop |

**Surviving configurations:**

| Config | D1 | D2 | D3 | D4 | Notes |
|---|---|---|---|---|---|
| K5 | system temp, private to the creating role, under the ID | nothing needed | when the creating role's work ends; Closing step 6 removes what is left in its own view | the EV row, written when the observation is made | the default; refined in C2 and C3 |
| K9 | K5, plus a shared home only for items a TS names as retained | temp: nothing; shared home: decided per TS | scratch with the role; retained items at Closing step 6 | retained items, for that TS only | an exception path; on Windows Codex today only the ignored folder in the project can be that home, which is the DoF 2 route (C4) |
| K7 | ignored folder in the project | nothing needed | Closing step 6 | the EV row | DoF 2 fallback only, for receivers who turn temp writes off (C5) |
| M5 | docstring = comment, judged for the reader of a program's output | the refined listed commands (C8) | — | — | 2 chatter lines removed in this task; restatements go to the separate task |
| M5 with docstring option C | only program-read docstrings stay | same | — | — | the owner's strict alternative: drops IDE and `help()` documentation |
| M5 with docstring option D | program-read or "public interface" | same | — | — | survives, but "public interface" is undefined in script-heavy receivers |

Eliminated:
- K1 and K2: TFW root as the default, because of (b) and the Codex defect.
- K3: no sandbox. It fits the owner's own setup, but every receiver who keeps the default sandbox hits DoF 2.
- K4: K5 without role ownership, so orphans and cross-tool paths matter.
- K6: the Reviewer reads the Executor's material (C3).
- K8: the worktree folder works only for roles that have one, and it clutters that worktree's `git status`.
- M2: docstrings always allowed.
- M4: a full read of every changed file plus removing restatements now.

**Unexpected survivors:**
- **K5.** Not in the Briefing or the HL. It survives because each weakness of temp (lifetime, a path that differs per tool) matters only if material outlives its creator or passes to another role. C3 already forbids the second, and C2 below removes the need for the first.
- **The identifier check in M5.** Expected to be impractical. It is one `grep`. It found real reason-and-history comments in `tools/tfw_state.py` and stayed silent on a real 818-line Candidate diff (C8).

## Findings

### C1: Was the H1 Codex result an artefact of my setup?

In every Codex trial in Gather, the workspace sat inside the temp folder (or temp was redirected).
An ordinary receiver has its project on one drive and temp on another. Rerun with the workspace at
C: outside `%TEMP%`, temp on E:, `exec --sandbox workspace-write`, Windows `unelevated`, no extra
roots:

| Block | Outcome |
|---|---|
| workspace (control) | ok |
| `%TEMP%\tfw\work\<ID>` | ok |
| `~/.tfw/work/<ID>` | denied, `UnauthorizedAccessException` |

The result holds. Gather's run with `%TEMP%` redirected to C: also had workspace and temp on
separate drives, and it worked too. The split-roots defect fires only when roots are added (E2).

### C2: K5 under interruption and resume with a different temp path

| Resume situation | Temp path in the new session | Working material | Registry (EV in the project) |
|---|---|---|---|
| same tool, same OS user, new session (Codex thread, new Claude Code session) | same: `%TEMP%` and macOS `$TMPDIR` are per user, Linux `/tmp` is per machine; none changes between sessions | found | complete |
| Claude Code with its sandbox on | same: the sandbox gives each user one temp directory and publishes it as `$TMPDIR` (Claude Code sandboxing page) | found | complete |
| Claude Code Desktop's harness scratchpad used instead | different: the harness gives each session its own scratchpad (this session's own environment says so) | not found | complete if rows were written when observed |
| reboot on tmpfs, or OS cleanup in between | same path, contents gone | lost | complete if rows were written when observed |
| the role re-dispatched as a new unit in another tool | different | orphaned in the old view | complete if rows were written when observed |

The registry stays complete on one condition: an observation enters the EV row when it is made.
Repeatable checks can be re-run after a loss, which `handoff.md` step 8 already permits ("Reuse
evidence only when…"). An observation that cannot be repeated, lost before its row exists, is gone
for good.

Today `handoff.md` runs checks at step 8 and emits the EV only at step 11, after the Candidate. In
the gap the output lives in working material. So TS deliverable 3 must put "an observation that
cannot be repeated enters its row when made" into step 8 or 11. DoD 3 forbids growth, so the words
must come out of the same file. ISO/IEC 17025:2017 7.5.1 asks the same of laboratories (via
summaries at 17025store.com and IAS): original observations recorded when they are made,
identifiable with the task.

Two refinements K5 needs:
1. **Removal point.** "Remove before its return" is ambiguous. A role stops at intermediate gates
   (ONB, questions, REVISE rounds) and continues as the same unit, so deleting scratch at every stop
   destroys continuity. The removal point is the end of the role's work (its final return), and C1's
   "no later than Closing step 6" remains the backstop. For Daily, C4 governs only the record folder
   at each orderly return, so scratch may persist across Daily turns, as C4 already says.
2. **Orphans and C1's deadline.** A folder orphaned in another tool's or another session's view
   cannot be seen by the replacement unit or by the Coordinator at Closing step 6. C1's "removed no
   later than Closing step 6" therefore cannot be guaranteed in that case. The OS temp cleanup is
   the real backstop.
   - Within C1: each unit removes its own folder; a replacement unit and Closing step 6 remove
     `<temp>/tfw/<ID>/` in every view they can reach and disclose any view they cannot. That is a
     disclosure duty, not a new mechanism.
   - Accepting OS cleanup outright would weaken the frozen claim and would need a §12 amendment. I
     do not recommend it, because the case is rare.

### C3: Subtraction — must the rule name a path at all?

The Coordinator's minimal form is "outside the project, in a temporary place the role owns, never
passed between roles and never referenced by path". It meets two frozen limits:
- **C1** requires the material to live "under the task or Daily record ID" in TFW's root or the
  system temporary directory.
- **DoD 1** requires the `Working material` subsection to name "the research-selected location for
  POSIX and Windows, the creator, the lifetime and Closing step 6".

So the rule cannot drop the location. It can drop everything else:

| Keep | Drop |
|---|---|
| the location class per OS, through the variable: `$TMPDIR`, else `/tmp`; `%TEMP%` | any fixed root (`~/.tfw`, `%LOCALAPPDATA%\tfw`), so the Windows root inconsistency does not spread |
| the ID as the folder name: resume and Closing step 6 find it, parallel tasks do not collide | the `work/` level; `tfw/<ID>/` groups TFW leftovers in one place |
| the creator, never passed to another role, removed when the role's work ends, Closing step 6 as the backstop | per-tool settings for reaching a TFW root (E2) |
| "nothing in the trace points into it" (stricter than C1's "ID-relative name", and C1 does not require a reference) | the reference-form clause. DoD 8's one EV mention of the location used stays in the form `<temp>/tfw/<ID>/` |

Illustrative minimal wording (about 70 words). The exact words belong to the TS, which S10 brings
to the owner:

> **Working material** (raw output, logs, exports, screenshots, copies, helper scripts) belongs to
> no class and never enters the project. The role that needs it keeps it under `tfw/<ID>/` in the
> temporary directory its environment provides (`$TMPDIR`, else `/tmp`; `%TEMP%`), passes none of it
> to another role, points nothing in the trace into it, and removes it when its work ends; Closing
> step 6 removes what remains in its view. An observation enters its EV row when it is made.

"The environment provides" is deliberate. Inside Claude Code's sandbox the variable already points
at the one temp directory that sandbox allows, so the same words work in every observed surface.

### C4: Would "temp is the only default location" survive a vendor fix of the Codex defect?

Yes. The conclusion rests on vendor design, not on the defect:
- Codex: "workspace … and temporary directories like `/tmp`".
- Antigravity: "workspace and system temp directories".
- Cursor: temp writable unless `disableTmpWrite`.
- Claude Code's sandbox: a per-user temp directory.

The defect does not touch the default layout (C1). Its root cause, per the issue, is a blanket
equality check that rejects an added split root set (openai/codex #35864, open, no maintainer
response when read; still present in the installed 0.152.1).

A fix would change two things, neither of them the default:
1. A TFW root would move from "no working setting" to "(b) with a one-time setting" for Codex on
   Windows, as on macOS/Linux. It would still not be (a).
2. K9's shared home for TS-named retained items would get a working option in Codex. Every receiver
   would still need that setting in every tool, and Antigravity's allow rule is untried.

The vendor-preferred `elevated` sandbox may not have the defect at all. Untested, by ruling.

### C5: Non-default settings that break temp

- **Codex:** `[sandbox_workspace_write] exclude_tmpdir_env_var` and `exclude_slash_tmp` (config
  reference). In read-only mode, which is the default for folders not under version control,
  nothing is writable at all.
- **Cursor:** `disableTmpWrite: true`.

A receiver with these settings has no writable location outside the project. For them the HL's DoF
2 route, the ignored folder in the project (K7), is the only home. The owner's own setup (no
sandbox) is unaffected. Stating the fallback in the rule would add words and a `.gitignore` entry
for a rare case; by subtraction it stays in the HL's failure route.

### C6: Windows path length

| Prefix on this machine (5-letter user name) | Characters |
|---|---|
| default Windows temp + `tfw\work\<ID>\` | 67 |
| `%LOCALAPPDATA%\tfw\work\<ID>\` | 62 |
| `~\.tfw\work\<ID>\` | 49 |
| this checkout | 37 |

MAX_PATH is 260. Long paths need both the `LongPathsEnabled` registry value and a long-path-aware
application, and Windows does not enable them by default (Microsoft Learn, "Maximum Path Length
Limitation"). This machine has them on, and Git `core.longpaths` is true here.

The repository's longest tracked path is 225 characters, so copying the repository tree into working
material passes 260 at every candidate location. The risk does not depend on the location; it comes
from copying the repository: the 225-character path was itself a repository copy inside `evidence/`
(HL §2.1). TS input: working material cites the commit instead of copying the tree.

### C7: Where printed output is not enough, and what the TS must be able to say

A different researcher's strongest attack on C2 and C3 is that some observations cannot be
repeated, and the row is written by the party being checked. Six cases:

| Case | Example in this repository | Why printing fails |
|---|---|---|
| volume | RTPSN: 162,705 bytes of trial records; receivers: 309 MB of run logs | too much to print |
| not text | a screen or rendering whose live target is gone | a description, not the thing |
| nondeterministic or costly | model trials (≈0.7 M tokens), load tests | a re-run gives other values |
| time-bound or one-shot | TKL's 600-second timing; a live system at one moment; sending, migrating real data | the moment is gone |
| private | output with secrets, personal data or private names (DoF 6) | must be redacted |
| bound to an environment | Windows-only behaviour reviewed from another OS; a device; credentials | the Reviewer cannot reach it |

The warning case: `workspace/2026/TFW_20260902-111644_CRATM/phase-c/evidence/EV__phase-c__authority_routing.md`.
- Size: 358,257 bytes, 25,918 words, 10,282 lines. The median of this repository's 58 EV files is
  13,521 bytes.
- Contents: 345,982 bytes (97%) sit inside fenced blocks, mostly pasted raw validator output plus
  an inline validator script; the registry rows are 6,127 bytes.

"Observed = printed output" without a bound moves the dump into the registry. The row's "observed"
must be the values that decide the claim, not the raw output.

For each claim that rests on such an observation, the TS must be able to say:
1. **Which claim, and why it cannot be repeated:** one of the six cases.
2. **What the row prints, captured by command when made:** the deciding values (per-attempt outcome
   and usage, start and end timestamps, totals), the redaction rule if any, and how (command or
   harness, commit, environment, time). Never a conclusion such as "within bound" (F32, TKL O1).
3. **What the Reviewer does instead of repeating:** checks the method and inputs at the Candidate,
   the row's own arithmetic and consistency, a bounded re-run where affordable (one attempt, one
   sample), and plausibility.
4. **What that supports:** the claim stands as the Executor's attestation with the method checked,
   not as the Reviewer's own observation (F30; PCAOB AS 1105.08: direct evidence is more reliable),
   and whether that is enough to accept this claim. That is a proportionality decision (NS2.7), the
   owner's for material claims.
5. **Retention:** none by default; otherwise which raw items, where (a home both roles reach that
   outlives the creating role, which temp is not), until when (the verdict at the latest) and who
   reads them.

None of this needs a new status or column. Items 1 and 2 live in the TS acceptance criteria and in
the row's "how" and "observed" cells; item 4 lives in the Reviewer's `verify.md` judgement. The
cost is a sentence in the TS for each affected claim. Most tasks have none: 2 of 343 review
documents in Gather's census.

### C8: H5 — is the check practical without code?

**Tried on a real Candidate diff:** ECON `1fafca12`, 37 files and 818 added lines outside task
folders.
- Extract's command 1 listed 36 lines; 30 were Markdown headings and bold text. Split by file type
  it lists 6:
  - 1 docstring;
  - 1 comment stating a non-obvious invariant ("never unlink a held lock");
  - 4 configuration comments that explain settings (2 unique, each in the config and its template).
  - Commands as refined:
    - code and configuration (`*.py *.js *.ts *.sh *.yaml *.yml *.toml`):
      `grep -E '^\+\s*(#|//|/\*|\*\s)|\s(#|//)\s|"""'` on added lines;
    - Markdown: `<!--` only.
- Command 2, narrowed to whole words, listed 0 lines in the diff. The first form matched "template",
  "attempt", "holds" and "folder".
- Command 2 over all deliverable-6 Python listed 55 lines. Among them:
  - the real reason-and-history comments at `tools/tfw_state.py:862`, `883` and `894` ("The old check
    existed because…");
  - the TFW term `LEGACY_ID`, a definition and not correspondence.

So the commands list and the Reviewer judges. No test in the repository depends on help text.

The Executor of this task must keep the five `description=__doc__` docstrings, or turn them into
literals, which changes nothing for the reader. Option A with the output-reader test avoids that
churn. H5's verdict from Extract stands: the false case holds for the first half (a tool reads
docstrings); the check is practical.

### C9: H7 under a second, independent pattern

The first pattern searched for retired-form words. A second searched for history narration that
avoids them:
- case-insensitive: "previously", "formerly", "no longer", "used to", "originally", "was
  replaced/renamed/removed/retired", "in the past", "earlier/older versions", "prior to";
- case-sensitive: "before/until/since/after" followed by a version or an upper-case task code.

It found 11 lines:
- 8 lifecycle words (REVIEW, DONE, APPROVE);
- 1 program error message;
- 2 from the `knowledge.md` paragraph already classed as chatter (lines 122 and 125).

No new chatter, so H7 holds. A stricter reading would treat every rule that only protects old
artifacts as unwanted. That conflates protection with correspondence. Gathering such rules into one
compatibility section is a design question for the agreed separate task.

### C10: Carried rulings and untested items, for RES

- Removed in this task under C7: `workflows/knowledge.md:122` and
  `adapters/antigravity/coordinator.md:55`.
  - In `knowledge.md` the unit is the two narrative sentences on lines 122–124 ("Before TKL, this
    section defined…", "Its original wording remains in Git object…"); line 122 alone cuts a sentence.
  - Lines 125–127 are operative and stay ("It no longer governs planning or qualification. Current
    work follows… reinstates no task sweep…").
  - Line 55 of the Antigravity profile is a paragraph of its own.
- Not touched: the four GATEWAY/LEAD repeats in the adapter root templates, which go to the agreed
  separate task on repetition and the word limit, together with the other 37 restatements.
- Untested, by ruling: Codex's `elevated` sandbox and Antigravity's `write_file(<path>)` allow rule.
  Both change the system or the owner's settings and matter only if a TFW root were chosen.
- Still open:
  - the docstring ruling (owner, at the TS);
  - whether `tools/migrations/2.0.0/` counts as a historical folder under C7 (TS scope);
  - H3, H4 and H6 (iteration 2).

### C11: Queries, files, trials and side effects

**Web queries (5, within the soft limit):**
- openai/codex #35864;
- the Claude Code environment-variables page (truncated) and a search for its per-user sandbox temp
  directory;
- ISO/IEC 17025:2017 7.5.1 (summaries);
- Microsoft Learn, "Maximum Path Length Limitation".

**Project files opened:**
- `templates/research/4_challenge.md`, `templates/evidence/EV.md`;
- `workflows/handoff.md`, steps 8–11;
- the CRATM phase-C EV, structure and sizes only;
- grep and diff over the ECON Candidate, deliverable-6 code and the tests.

**Trial:** one Codex run with an ordinary layout. **Side effects:** the throwaway workspace, the
probe folders and the scratch files are removed; Codex ran with `--ephemeral`.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| The H1 Codex result is not a setup artefact: temp is writable and the TFW root denied with workspace and temp on separate drives | none |
| K5 keeps the registry complete through any resume if an observation enters its row when made; removal at the end of the role's work, not at every gate; orphans need a disclosure duty to stay inside C1 | TS: the step-8/11 ordering in `handoff.md` within DoD 3 |
| The rule must name the location class and the ID (C1, DoD 1); fixed roots, `work/`, tool settings and the reference clause can go; a ~70-word form is possible | exact wording at the TS stop (S10) |
| A vendor fix would not change the default; it would only give K9 a Codex option | `elevated` untested, by ruling |
| Printed output fails in six cases; the TS must say five things per affected claim; the 358 KB EV shows that "observed" needs a bound | owner's proportionality call for material attested claims |
| The H5 commands are practical once split by file type (6 lines on a real diff); docstrings stay for five scripts | owner's docstring ruling |
| H7 survives a second pattern | none |

**Sufficiency:**
- [x] External source used? 5 (vendor tracker, vendor docs, ISO/IEC 17025 summaries, Microsoft Learn)
- [x] Briefing gap closed? Yes: every planned Challenge item plus the Coordinator's four
- [x] Pairwise incompatibility checked? Surviving configurations listed? Yes: K5, K9, K7, M5 with docstring options A, C, D

**Knowledge handover:**
- **Material:** as above.
- **Uncertainty:**
  - Claude Code's auto results are nondeterministic;
  - POSIX and the Codex app rest on documentation;
  - the Codex defect's future is unknown;
  - per-session temp paths were observed only in this harness.
- **Publication:** none.
- **Continuation:** on the Coordinator's answer, Synthesis (RES) for iteration 1. H3, H4 and H6
  remain for iteration 2 (`min_iterations: 2`).

Stage complete: YES
→ User decision: ___
