# RES — TFW_20261004-174815_LPF: Lean Project Footprint

> **Current filename**: fixed `research/iter1/RES.md` under the selected task.

> **Date**: 2026-10-04
> **Author**: Claude Code — Researcher (`lpf-researcher`)
> **Status**: 🔬 RES — iteration 1 complete
> **Parent HL**: [HL-TFW_20261004-174815_LPF](../../HL-TFW_20261004-174815_LPF.md)
> **Mode**: Pipeline, focused
> **Producer unit**: `claude-code:agent:local_a7cf0ab7-482d-403e-b738-504d82bba898/lpf-researcher` = native agent `a2f09276b39617fd0` in Claude Code session `bd8d3d9f-d605-429a-a889-2c6d2bd03aa5`
> **Parent Coordinator**: `claude-code:session:local_a7cf0ab7-482d-403e-b738-504d82bba898`
> **Activation / dispatch source**: delegated; command-first `/tfw-research TFW_20261004-174815_LPF`; `journal/20261004-193543__dispatch__71eb.md @ 72b88163`
> **Coordination authority**: `HL-TFW_20261004-174815_LPF.md @ efc915a9fa3e4366a3567be800d028ee011c916f`
> **Originating proposer**: `none`

---

## Research Context

The HL wants a TFW project to hold only its result and its selected trace. Working material goes
outside the project under the task ID and disappears at close; evidence becomes a registry the
Reviewer checks by repetition; a comment carries value or is absent. Iteration 1 supplies the
decision inputs for claims C1, C3 and C5:
- **H1:** where working material can live under ordinary agent sandboxes.
- **H2:** whether reviewers have ever needed an Executor's raw files.
- **H5:** whether the comment rule holds against docstrings and other loopholes, and can be checked
  without code.
- **H7:** how much of the "historical" wording in `.tfw/` is rule and how much is chatter.

Without these, the location would have been chosen by taste, the removal point without knowing what
reviewers use, and the comment rule with an open loophole.

## Briefing

[`1_briefing.md`](1_briefing.md) (commit `b847402e`), answered by the Coordinator.

Stage files:
- [`2_gather.md`](2_gather.md) (`96ab30da`), with a dated Claude Code addendum (`b6cd3a18`);
- [`3_extract.md`](3_extract.md) (`b6cd3a18`);
- [`4_challenge.md`](4_challenge.md) (`3d03f9ba`).

Every stage gate carries the Coordinator's written ruling.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | **Working material lives in the system temporary directory**, under `tfw/<ID>/`, resolved through the role's own environment: `$TMPDIR`, else `/tmp`, on POSIX; `%TEMP%` on Windows. | In every observed default mode, temp is writable wherever any place outside the workspace is. Trials: Codex 0.152.1, Antigravity 1.2.12, Claude Code 2.1.289. Documentation: Cursor, POSIX. Inside Claude Code's sandbox the variable already names the only temp it allows (Gather G2 and addendum; Extract E1; Challenge C1) |
| D2 | **Not a TFW root** (`~/.tfw/work`, `%LOCALAPPDATA%\tfw\work`) | Needs an approval the workspace does not, in Codex, Antigravity and Cursor. No working setting in Codex on Windows today: `writable_roots` and `--add-dir` make the `unelevated` sandbox refuse every command, a vendor defect. A new root would also spread the existing Windows split (Extract E2, E3; Challenge C4) |
| D3 | **The material is private to the role that created it.** Nothing passes to another role; nothing in the trace points into it. DoD 8's EV note names only the location `<temp>/tfw/<ID>/`. | Temp's weak points (it can be wiped early; its path differs between tools) harm only material that outlives its creator or changes hands. C3 already forbids the second (Extract K5; Challenge C2, C3) |
| D4 | **Removed by the creating role when its work ends**, not at every gate stop. Closing step 6 is the backstop. Whoever cleans removes what it can see and reports what it cannot; the closing rule already records completed, left and pending cleanup. | ONB, questions and REVISE rounds continue the same unit. A folder orphaned in another tool's view cannot be seen. Coordinator's ruling: a refinement of the closing rule, within C1 (Challenge C2) |
| D5 | **An observation enters its EV row when it is made.** | Across any interruption the registry stays complete only this way. `handoff.md` runs checks at step 8 but emits EV at step 11, so output waits in working material; an unrepeatable observation lost there is lost for good. ISO/IEC 17025 7.5.1 makes the same demand of laboratories (Challenge C2) |
| D6 | **The "observed" cell carries the values that decide the claim**, captured by command. Not a conclusion, not raw output. | TKL O1: a 40-second overrun visible only in raw timestamps would show in a row that prints them. CRATM phase C: an EV of 358,257 bytes, 97% pasted raw output, shows the dump moving into the registry (Extract E4; Challenge C7) |
| D7 | **For a claim resting on an observation that cannot be repeated, the TS says five things:** (1) which claim and why it cannot be repeated; (2) which values the row prints and how they were captured; (3) what the Reviewer checks instead (method at the Candidate, the row's arithmetic, a bounded re-run); (4) that this supports an attestation with the method checked, and whether that is enough to accept the claim, the owner's proportionality call; (5) retention, none by default. | Six cases where printing fails: volume, not text, nondeterministic or costly, time-bound or one-shot, private, bound to an environment. In this repository, 2 of 343 review documents had such a claim (Extract E4; Challenge C7) |
| D8 | **Working material cites a commit instead of copying the repository tree.** | The longest tracked path (225 characters) plus any location prefix (49–67 characters) exceeds Windows MAX_PATH (260). Long paths are off by default (Challenge C6) |
| D9 | **Comment-exception draft** for the TS (Extract E5). A comment stays when a program reads it, kept byte for byte: interpreter or encoding line, tool directive, license header, TFW managed-block marker. It also stays when it tells the file's reader what the file cannot: what a setting means, the instruction a template gives, or, in a docstring a program publishes, what the reader of that output needs. Everything else is absent. | Receivers' stacks (Python/FastAPI, JS/TS, YAML) read docstrings in FastAPI, FastMCP, Typer, doctest and argparse; directives live in ruff, coverage, ESLint, TypeScript, yamllint, yaml-language-server and markdownlint (Gather G8) |
| D10 | **Docstrings:** option A recommended, a comment like any other, with a program-published docstring judged by the reader of that output. Options C and D survive; B is eliminated. Owner's ruling at the TS. | Five scripts here print their docstring as `--help`, one of them shipped. `tools/migrations/2.0.0/migrate_board.py` shows B's loophole: a 31-line narrative docstring (Extract E5; Challenge C8) |
| D11 | **Reviewer check without code:** two listed commands over the VALUE diff, split by file type, plus a channel-word `grep`; one census for DoD 7. The Reviewer judges each listed line. | On the real ECON Candidate (818 added lines) the commands list 6 lines. Unsplit, Markdown headings had given 30 false hits. Over all deliverable-6 code, the `grep` finds real reason-and-history comments (Challenge C8) |
| D12 | **"Historical" prose in `.tfw/` is rule:** 150 of 152 in-scope lines. The two chatter passages are removed in this task (C7). The 41 restatements, including the four GATEWAY/LEAD lines in the adapter root templates, go to the agreed separate task on repetition and the word limit. | Every line classified; a second independent pattern found no further chatter. Coordinator's ruling at the Extract stop (Extract E6; Challenge C9, C10) |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Which outcome qualifies a location? | answered | Only (a), in the tool's default mode; (b) is a DoF 2 risk reported with the setting that removes it (Coordinator) |
| Q2 | Which surfaces does the owner use? | answered | Codex desktop app and CLI; Claude Code via the Claude Desktop Code tab; Antigravity; Cursor not installed; Windows 11 (Coordinator, from repository files) |
| Q3 | Which stacks do receivers use? | answered | Mainly Python (FastAPI services, scripts), some JS/TS, Markdown-only projects, YAML everywhere (Coordinator, from field reports) |
| Q4 | Claude Code trial | answered | The owner signed in; trial run 2026-10-04 (Gather addendum) |
| Q5 | Is the role-private folder the owner's call? | answered | No: the Coordinator's, within C1 and C3; §3.2 is a value flow; the owner sees it at the TS stop |
| Q6 | Chatter and repeats: this task or the separate one? | answered | 2 chatter passages here; the GATEWAY/LEAD repeats to the separate task |
| Q7 | Run Codex `elevated` and the Antigravity allow rule? | answered | Skipped: both change the system or the owner's settings and matter only for a TFW root. Untested |
| Q8 | Orphaned folders: amendment or refinement? | answered | Refinement of the closing rule, within C1 |
| Q9 | Which docstring option? | open | Owner, at the TS stop (HL §4.1 reserve) |
| Q10 | Is `tools/migrations/2.0.0/` a historical folder under C7? | open | TS scope; it is the maintainer copy of a tool removed from the payload in 3.0.0, not pinned by hash in `.tfw/` |
| Q11 | Are attested claims acceptable for a given task? | open | Per TS, the owner's proportionality call (D7 item 4) |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | TFW's machine-local root is writable under ordinary sandbox settings; temp is the fallback | open | ❌ for the TFW root · ✅ for temp, which becomes the location, not the fallback | Codex: root (b), temp (a), also with workspace and temp on separate drives. Antigravity: root (b), temp (a). Claude Code: `auto` (a) everywhere (automatic check, nondeterministic), Manual (b) everywhere, same for root and temp. Cursor and POSIX: documented (a) for temp, (b) outside. No setting removes (b) for Codex on Windows today |
| H2 | Reviewers establish claims by repetition, not by reading raw files | open | 🟡 holds with one exception | 26 of 343 review documents cite raw executor files, most to audit them while the Reviewer repeated the check. 2 verdicts rested on unrepeatable executor data (RTPSN, TKL), 1 on repeatable renders (FA15ES). The false case occurred once and was not material: TKL O1. The fix is the row's form (D6), not retention until the verdict |
| H5 | The comment rule holds against its loopholes and can be checked without code | open | 🟡 first half false, second half true | A tool does read docstrings: five `argparse` scripts here, and FastAPI, FastMCP, Typer and doctest in receivers' stacks. So docstrings are admitted where a program publishes them, judged for that output's reader. The check is practical: 6 lines to judge on a real diff |
| H7 | The "historical" prose is mostly rule; chatter is small | open | ✅ | 169 matches: 17 false, 109 protective rules, 41 restatements, 2 chatter. A second pattern found none more |
| H3, H4, H6 | — | open | deferred | Iteration 2 by plan |

## HL Update Recommendations

> **The researcher classifies, never applies or rules.** Each recommendation names its HL section.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §10 Hypotheses | Statuses and evidence for H1, H2, H5 and H7 as in the table above; H3, H4 and H6 remain open for iteration 2 | this RES |
| R2 | §10 Blind Spots | Mark as resolved: sandbox writes (H1), raw-file reviews (H2), docstring consumers (H5), historical prose (H7). Remaining: receivers' configuration comments are still uninspected | Gather, Extract |
| R3 | §2.4 Assumptions and unknowns | Replace "untested (H1)" and "unknown (H2)" with the results. Add that macOS/Linux and the Codex app rest on vendor documentation | Gather G2–G4 and addendum; Extract E1 |
| R4 | §2.2 What the rules say today | Add that TFW's machine-local roots lie outside every observed default sandbox, while the system temp lies inside | Extract E1, E2 |
| R5 | §8 Dependencies | "Research on sandbox writes (H1) before TS binds the location" → ✅, bound to the system temp; note the documentation-only limits | Extract E3 |
| R6 | §9 Risks | Update and add rows, as listed below | Challenge C2, C5–C7; Extract E2 |
| R7 | §7.2 Knowledge Citations | Add a row citing `research/iter1/RES.md` (H1 matrix, D1–D8) as the ground for the location and the registry rules; DoD 9 requires the EV to cite the RES | DoD 9 |
| R8 | §4 Phase A deliverables (free under HL Contract rule 6) | Add the removal of the two chatter passages: `workflows/knowledge.md` lines 122–124 (two sentences; lines 125–127 stay) and `adapters/antigravity/coordinator.md:55`. Acceptable under §5 and §6 as they stand: live files, not historical records (DoF 4), and words decrease (DoD 3, DoF 5) | Challenge C10; Coordinator ruling |

R6, the risk rows for §9:
- "An agent sandbox cannot write outside the project": probability Low for temp. The residual case is
  receivers who disable temp writes (Codex `exclude_tmpdir_env_var` / `exclude_slash_tmp` and
  read-only mode, Cursor `disableTmpWrite`); for them the DoF 2 route applies.
- "Windows root inconsistency spreads": retire it. No new root is added.
- New: **orphaned temp folders** after an interrupted session. Mitigation: D4.
- New: **the EV becomes the new dump.** Mitigation: D6.
- New: **an unrepeatable observation is lost between `handoff.md` steps 8 and 11.** Mitigation: D5.
- New: **repository copies exceed MAX_PATH.** Mitigation: D8.
- New: **Claude Code `auto` writes outside the working directory depend on a classifier.** Shown for
  information only.

### Amendment Proposals — frozen sections, resolved-ruler verdict required

**No amendment proposals.** Considered and not proposed:

| Considered | Why not |
|---|---|
| C1: orphaned folders cannot always be removed by Closing step 6 | Ruled a refinement of the existing closing rule, which records left and pending cleanup and forbids claiming removal in DONE (D4) |
| C3: observations that cannot be repeated | C3 holds as written: the EV row is trace, not working material, so no verdict depends on another role's material. Such claims are recorded as attested, and the TS names them (D7). Retention for the Reviewer would be the HL's DoF 1 failure route, not a normal path |
| §3.1/§3.2: the notation `<tfw-home>/work/<ID>/` and "Executor and Reviewer look at it" | C1 lets research select the system temp; the notation shows one of C1's two options; the Coordinator ruled §3.2 a value flow. The TS states the exact location; an owner round would change no commitment |
| C1's reference form ("ID-relative name") | D3's "nothing points into it" is stricter and compatible; C1 does not require a reference |
| DoD 1 location naming | Satisfied by naming the variable per OS family (D1) |

### TS inputs and their contact with frozen claims

| TS input | Frozen claim touched | How |
|---|---|---|
| Location: system temp, role-private, removal when the role's work ends (D1–D4) | C1, DoD 1, DoD 8 | within: C1 lets research select temp; the duties stay |
| Row entered when the observation is made (D5) | none | wording in `handoff.md` steps 8 and 11 must stay inside DoD 3 (no word growth) |
| Five things for unrepeatable observations (D7) | C3, DoF 1 | within: C3's second clause holds because the row is trace; item 5 (retention) is the DoF 1 route, never a default |
| "Observed" bound to deciding values (D6) | C2 | within: refines "what was observed"; EV template (deliverable 2) |
| Commit reference instead of a tree copy (D8) | none | a sentence in the `Working material` subsection |
| Comment-exception draft (D9) | C5 | within: C5 delegates "docstrings and other candidate exceptions" to research and the TS; its own list is unchanged |
| Docstring options (D10) | C5, HL §4.1 owner reserve | owner's ruling at the TS stop |
| Closing refinement: remove what you see, report what you cannot (D4) | C1 | within (Coordinator's ruling) |
| Two chatter passages removed (D12, R8) | C7, §4 deliverable list | free under HL Contract rule 6 |
| Reviewer's listed commands (D11) | C8 | within: the "two Reviewer checks in `verify.md`"; no code, no new command |

## Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | environment | Receiving projects are mainly Python (FastAPI services and scripts), with some JavaScript/TypeScript for the web and some Markdown-only projects; YAML configuration is everywhere | Coordinator's answer to the Briefing, 2026-10-04, from field reports and size-only observations | ★★☆ |

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | convention | Because receivers run FastAPI services, docstrings there are often API documentation that a program publishes (OpenAPI), and FastMCP docstrings are what a model reads to choose a tool. Implication: the docstring rule matters most in receivers, not here. Option A's output-reader test keeps these docstrings honest without banning them. | FC1 relayed by the Coordinator; implication by research | ★★☆ |

## Findings Map

```
H1  where can working material live?
 ├─ trials on Windows: Codex, Claude Code, Antigravity; docs: Cursor, macOS/Linux
 ├─ system temp: writable by default wherever any outside place is ─────┐
 ├─ TFW root: approval needed in Codex, Antigravity, Cursor;            │
 │  the Codex setting that would allow it breaks the sandbox            │
 └─ temp's weak points: wiped early, path differs per tool              │
       harmless if material never outlives or leaves its role ─────────┤
                                                                        ▼
                         D1–D4  temp, private to the role, under the ID;
                                removed when the role's work ends;
                                Closing step 6 cleans what it sees, reports the rest
H2  do reviewers need raw files?
 ├─ 26 of 343 reviews cite them; most repeated the check anyway
 ├─ 2 verdicts rested on unrepeatable data, 1 on repeatable renders
 └─ the only raw-only defect would show in a row that prints values
       ├──► D5  the row is written when the observation is made
       ├──► D6  "observed" = the deciding values, not output, not verdict
       └──► D7  five things the TS says for an unrepeatable claim
H5  does the comment rule hold?
 ├─ programs read docstrings (5 scripts here; FastAPI, FastMCP in receivers)
 │     └──► D9, D10  exception draft; docstring option A
 └─ two greps list 6 lines on a real diff ──► D11  Reviewer check, no code
H7  is the "historical" prose chatter?
 └─ 150 of 152 lines are rules; 2 chatter ──► D12  remove 2 here; 41 repeats → separate task
```

## Iteration Status

- **Iteration:** 1 of 2 (min) / 3 (max)
- **Hypotheses tested:** H1 (❌ TFW root, ✅ temp), H2 (🟡 holds with one non-material exception),
  H5 (🟡 docstrings are program-read; check practical), H7 (✅)
- **Hypotheses deferred:** H3, H4 and H6, to iteration 2 by plan
- **Gaps discovered:**
  - macOS/Linux and the Codex desktop app rest on vendor documentation;
  - Codex `elevated` and the Antigravity allow rule untested, by ruling;
  - Cursor not installed;
  - Claude Code `auto` outcomes are nondeterministic by nature;
  - receivers' configuration comments remain uninspected.
- **Superseded decisions:** HL §10's "the system temporary directory is the fallback" is superseded
  by D1: temp is the location (H1 result).

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | H3: did any later task need bytes from a closed task's evidence? | decides whether TS-named retention is ever needed (D7 item 5) | search later tasks for citations into closed tasks' `evidence/` |
| 2 | H4: commit count per task | the HL's commit-reduction claim | count commits per role return in recent tasks; check recovery paths that rely on intermediate commits |
| 3 | H6: Daily products with no ordinary path | C4 could lose one-off charts or videos | inventory Daily products; check D1–D4 against C4's "each orderly return" |
| 4 | The full subtraction challenge | the planned iteration-2 test of what in the proposal can go | apply it to D1–D12 and to the deliverables |

### Recommendation
- [ ] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [x] **MORE NEEDED** — iteration 2 for H3, H4, H6 and the subtraction challenge (`min_iterations: 2`); iteration 1's inputs for C1, C3 and C5 are complete
- [ ] **BLOCKED** — {specify blocker}

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 1 tested where working material can live, whether reviewers need raw files, whether the
comment rule holds and how much historical wording is chatter.

**What it settled.** The HL's own first choice, TFW's machine-local root, fails in the default
sandboxes of Codex, Antigravity and Cursor. In Codex on Windows it cannot even be enabled. The system
temporary directory works everywhere, provided working material stays private to the role that
created it. That condition turns temp's two weaknesses into non-issues and adds no mechanism.
Research also found what the plan had missed:
- the gap between `handoff.md` steps 8 and 11, where an unrepeatable observation can be lost;
- a 358 KB EV showing that "observed = printed output" needs a bound;
- the five things a TS must say when repetition is impossible;
- that this repository's own scripts depend on docstrings.

**Self-critique.**
- A layout confound in the Codex trials was caught only in Challenge. It did not change the result.
- Quoting slips put a literal `$ID` folder name into the Antigravity trials, and stale files spoiled
  the first Manual run. Both are disclosed and corrected.
- The line between a protective rule and a restatement in H7 is a judgement, checked by `git grep`
  for each cluster but still a judgement.
- POSIX conclusions rest on vendor documentation.

### Material handover at this return

- **Producer / unit:** the Researcher named in the header; activation and dispatch as in the header.
- **Source / epoch:**
  - this repository from `72b88163` (dispatch) to the RES commit;
  - vendor pages read 2026-10-04: OpenAI Codex, Claude Code, Antigravity, Cursor;
  - openai/codex issues #34970 and #35864;
  - Microsoft Learn;
  - summaries of ISO/IEC 17025 and PCAOB AS 1105;
  - trials on this Windows 11 machine with Codex 0.152.1, Claude Code 2.1.289 and Antigravity 1.2.12.
- **Inspected scope:** as listed in each stage file (G11, E7, C11).
- **Material:** D1–D12; the H1 matrix; the H7 classification; the comment-exception draft; the
  listed commands.
- **Uncertainty:** as under Gaps discovered.
- **Unresolved owner decisions:** the docstring ruling; per task, the acceptance of attested claims.
- **Knowledge publication:** none.
- **Working material of this iteration:** trial workspaces, probe files and scratch outputs, all in
  the system temp. Removed; no file remains in any probed location.
- **Continuation:** the Coordinator reviews this iteration through `/tfw-plan` and prepares the
  iteration-2 entry in `iterations.yaml`.

**Economics contribution** (under `.tfw/economics/README.md`, Claude Code JSONL recipe):
- **File:** [`economics/researcher-iter1-20261004.jsonl`](../../economics/researcher-iter1-20261004.jsonl),
  revision 1, SHA-256 `5adaf3d29dc4648d28ae236208f806b5591ad9003c37b1439163a10edd94f430`, 1,928
  bytes. It holds one manifest row and one usage row and passes `validate`.
- **Source:** ID `bd8d3d9f-d605-429a-a889-2c6d2bd03aa5/a2f09276b39617fd0`; file
  `<session>/subagents/agent-a2f09276b39617fd0.jsonl` (all 969 lines belong to this unit); source
  version 2.1.286.
- **Range and cutoff:** lines 1–969; cutoff `2026-10-04T18:34:56.581828+00:00` (23:34:56 +05:00);
  `complete: false`.
- **Measured:** model `claude-opus-5-5`.
  - Input: 57,024,926 tokens, of which 55,241,071 were cache reads, 400 fresh input and 1,783,455
    five-minute cache writes.
  - Output: 455,939 tokens, of which reasoning was 320,207, a diagnostic subset not added twice.
  - Effort and native duration are unavailable in this source.
- **Tail after the cutoff:** this edit, the RES commit and the return message. Disclosed once; it
  does not trigger recapture.

---

*RES — TFW_20261004-174815_LPF: Lean Project Footprint | 2026-10-04*
