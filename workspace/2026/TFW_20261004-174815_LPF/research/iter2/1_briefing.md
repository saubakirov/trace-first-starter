# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW_20261004-174815_LPF](../../HL-TFW_20261004-174815_LPF.md)
> Goal: A TFW project holds only the result and the selected trace: working material lives outside the project under the task ID and is gone when the task closes, and a comment carries value or is absent.
> Producer unit: `claude-code:agent:local_a7cf0ab7-482d-403e-b738-504d82bba898/lpf-researcher` = native agent `a2f09276b39617fd0` in Claude Code session `bd8d3d9f-d605-429a-a889-2c6d2bd03aa5` (same unit as iteration 1)
> Parent Coordinator: `claude-code:session:local_a7cf0ab7-482d-403e-b738-504d82bba898`
> Activation / dispatch source: delegated; continuation `/tfw-research TFW_20261004-174815_LPF`; `journal/20261004-233709__dispatch__2d7e.md @ b2ebb255`
> Coordination authority: `HL-TFW_20261004-174815_LPF.md @ efc915a9fa3e4366a3567be800d028ee011c916f`, §4.1
> Originating proposer: `none`

Iteration 2 of `research/iterations.yaml`, the first pending entry at `b2ebb255`; no `iter2/` existed
at resolution. Mode: focused. The session title `RESEARCH · LPF` is unavailable for an in-session
agent. The model is claude-opus-5-5 as dispatched; effort is unavailable.

**Economics source binding** (`.tfw/economics/README.md`, Claude Code JSONL recipe):
- Provider `claude-code`; source ID `bd8d3d9f-d605-429a-a889-2c6d2bd03aa5/a2f09276b39617fd0`; file
  `<session>/subagents/agent-a2f09276b39617fd0.jsonl`; source version 2.1.286.
- Range start at line 970 (2026-10-04T18:34:57.441Z), disjoint from revision 1 (lines 1–969). It
  opens with iteration 1's uncovered tail (lines 970–992) and then this dispatch (line 993,
  23:40:47 +05:00).
- Timezone +05:00; task `TFW_20261004-174815_LPF`, no phase; owner `saubakirov`; role `researcher`.
- The finite end and cutoff are set at the RES return.

**Inherited from iteration 1** ([RES](../iter1/RES.md) at `57159eac`, accepted and applied at `b2ebb255`):
- **D1–D4:** working material lives in the system temporary directory under `tfw/<ID>/`, private to
  the role that created it, and is removed when the role's work ends. H6 tests this against Daily.
- **D5–D7:** the EV row is written when an observation is made; "observed" carries the deciding
  values; the TS says five things for an unrepeatable claim. H3 decides whether item 5, retention,
  is ever needed.
- **D12 and R8:** the two chatter passages are removed in this task.
- **Open threads 1–4:** H3, H4, H6 and the full subtraction challenge, which is this iteration.

## Research Plan

### Gather — observe, count, collect sources

- **H3, later use of closed tasks' raw evidence.**
  - Find every citation of a non-EV `evidence/` file in a file outside the cited task's folder:
    later tasks, reviews, Daily records, `knowledge/` and `.tfw/`. Find every copy of another task's
    material inside a later task's `evidence/` (for example, TKL's `sources/<commit>/…` tree).
  - Read each hit in context and record what the later reader needed.
  - External anchor: retention defaults for build artifacts and logs in common CI platforms,
    against record-retention rules in regulated audit.
- **H4, commits per role return.**
  - For CMTR, PCUX, RWNR, PTW and LFD, count commits by the role and work tokens in the subject
    (`[provider/TASK/work/role]`), and place each commit at a role return or between returns.
  - Inventory every `.tfw/` rule and recovery path that requires a separate or ordered commit: ONB
    committed alone; the Candidate before traces; an event committed before its SHA enters status;
    the freeze commit before research; landing a dead run's commits; exact-path staging.
  - External anchor: Git guidance on commit granularity and recovery.
- **H6, Daily products.**
  - Inventory this repository's `daily/` (5 records, 12 files) and the Daily skill and record
    template: what products exist, where they live, whether the record links them, and what the
    skill calls an "orderly return".
  - Add the HL's size-only receiver figures (R3: PNG, webm, PDF, scripts, fonts, docx) as product
    kinds.
  - External anchor: platform guidance on binaries in repositories (size limits, large-file storage).
- **Subtraction, inputs only.** For each of D1–D12 and each Phase A deliverable (1–8), read the
  target text it would change:
  - `conventions.md` sections `Evidence subfolder`, `Safety and Execution Honesty`, `Semantic
    value-bearing classification`, `Closing and record recovery`, `Anti-patterns` and `Design
    Rules`;
  - the EV and `verify.md` templates, `handoff.md` steps 8–11 and `review.md` Verify;
  - the Daily skill and its template, the adapter root templates and the migration-guide pattern.
  - Record which existing sentence already carries part of each decision's meaning.

Candidate decision dimensions:
- **H3:** citing context, bytes versus statement, whether the EV row would have sufficed.
- **H4:** commit kind (rule-required, recovery, habit), position (at a return, between returns),
  harm if merged.
- **H6:** product kind, ordinary path exists, linked from the record, survives the orderly return.
- **Subtraction:** purpose, proof, boundary, needed freedom, the text that already carries it.

### Extract — map configurations

- **H3:** a table of cross-task citations, each marked "the EV row would have sufficed" or "bytes
  needed", leading to a decision on TS-named retention.
- **H4:** a commit taxonomy per task: the rule-required minimum, a projected count under "commit at
  role returns", and which rules or recovery paths would break.
- **H6:** product kind × ordinary path × link × orderly return, leading to a decision on whether C4
  needs a product list or a named home for one-off products, and how D4's "when the role's work
  ends" maps onto Daily turns.
- **Subtraction:** a matrix of D1–D12 and deliverables 1–8 × (purpose, proof, boundary, freedom) ×
  existing text, marking each item removable, mergeable or kept, then the minimal deliverable set.

### Challenge — test survivors

- **H3:** what would make "no retention by default" fail: regulated work, a dispute after
  acceptance, a long trial someone wants to re-examine. Weigh the cost of a later need against the
  cost of keeping.
- **H4:** whether fewer commits harm crash recovery (landing a dead run), Candidate identity,
  attribution carried in commit subjects, or several sessions sharing one working tree.
- **H6:** whether a named home for one-off products collides with C1, C4 or C8 (no new root folder);
  whether Daily cleanup can drop an unlinked product.
- **Subtraction:** for each surviving item, which failure (DoF) comes back if it goes. Apply NS2.2:
  subtraction must not damage inspectability or continuation.

Budget: Gather and Challenge will exceed the soft limit of 15 project files, because the subtraction
challenge reads every target text. Each query and opened file is listed in its stage file with the
hypothesis or check it serves. Web queries stay around 3–5 per stage.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H3 | After acceptance, raw material adds nothing a registry row cannot carry. False case: a later task needed bytes from a closed task's evidence. Consequence: TS of high-risk tasks may name retained items explicitly. | open |
| H4 | Most commits per task are habit, not rule; committing at role returns cuts them several-fold without harming continuation or review. False case: a rule or recovery path depends on intermediate commits. Consequence: commit reduction leaves this task. | open |
| H6 | "Working material outside the project; only the record in the record folder; products at ordinary paths" suffices for Daily without losing results. False case: a Daily product has no ordinary path (a one-off chart, a demo video). Consequence: the record gets an explicit product list and a named home for one-off products. | open |

Plus the subtraction challenge over D1–D12 and deliverables 1–8, which iteration 1 deferred here.

## Scope Intent

- **In scope:**
  - H3 over this repository's tasks, reviews, Daily records, `knowledge/` and `.tfw/`;
  - H4 over CMTR, PCUX, RWNR, PTW and LFD and the `.tfw/` commit rules;
  - H6 over this repository's `daily/`, the Daily form and the HL's size-only receiver figures;
  - subtraction over D1–D12 and deliverables 1–8, returning refinements or amendment proposals
    with evidence, cost and the alternative considered.
- **Out of scope:**
  - receivers' content, unless Q1 permits a type-and-count listing;
  - rule wording, the TS and HL edits (Coordinator);
  - any change to code, prose or configuration;
  - re-opening H1, H2, H5 or H7, except where subtraction re-examines their decisions;
  - the agreed separate task (restatements, the word limit);
  - new tool trials (none planned).

## Guiding Questions

1. **H6 evidence base.** This repository's `daily/` holds 5 records with 12 files (8 Markdown, 4
   JSONL) and no product files; the heavy case is receiver R3, measured by size only. May I list one
   receiver's Daily file types and counts per record (no names, no content), or does H6 rest on this
   repository's records, the owner's S6 and the HL's size figures?
2. **H4 oracle, fixed before counting.** I propose to count a commit as required when a current
   `.tfw/` rule names it (ONB alone, the Candidate before traces, an event committed before its SHA
   enters status, the freeze commit) or a recovery path reads it (landing a dead run's commits).
   Everything else is habit. "Committing at role returns" would allow, at each gate stop or final
   return, the ordered commits a rule requires at that point. Under this oracle H4's false case
   ("a rule depends on intermediate commits") is decided per commit kind, not by the mere existence
   of ordered commits at a return. Confirm or set another rule.
3. **Subtraction reach.** Should the challenge also test frozen items (for example, DoD 6's four
   adapter pointers or DoD 3's word rule) and return amendment proposals where evidence supports
   them, or stay within the free deliverable list (HL Contract rule 6)?

## User Direction

Coordinator's ruling at the mode gate (addressed message, 2026-10-04): mode **focused**. The soft
limits are as in iteration 1: they may be exceeded when every file and query is named in the stage
file with the hypothesis or check it serves. The hard limit of 3 questions per turn stays. The
economics range from line 970 is accepted as a disjoint contribution.

## Sources and knowledge handover

**Inspected at this checkpoint:**
- `status.md` (complete routing spine, matching the dispatch);
- the journal dispatch event `20261004-233709__dispatch__2d7e.md`;
- the HL at `b2ebb255`: the diff from `efc915a9` touches only free sections and adds deliverable 8
  under rule 6;
- `research/iterations.yaml` at `b2ebb255`;
- `research/iter1/RES.md` (own);
- `research/base.md` and `focused.md`, reread on resume;
- `conventions.md` heading `Session identity`;
- this template.

**Feasibility observations, counts only:**
- commits naming each task: CMTR 62, PCUX 107, RWNR 92, PTW 76, LFD 67 (FRATS 70, a spare);
- `daily/`: 5 records, 12 files;
- files citing a non-EV `evidence/` path in full: 188, cross-task share unknown.

**Knowledge inputs for the stages:**
- H3: KNOWLEDGE D52 and D53, `knowledge/process.md` F23 and F29.
- H4: `conventions.md` `Exact-path staging`, `Commit Attribution` and `Closing and record recovery`.
- H6: the Daily skill and record template, HL S6.
- Subtraction: README NS2.2, `knowledge/philosophy.md` F22, F40 and F41, `conventions.md` `Design
  Rules`.

No knowledge publication.

**Material handover:** no finding yet; H3, H4 and H6 open. **Continuation:** on a valid answer to
this Briefing, copy `2_gather.md` and run Gather.

---
Stage complete: YES
