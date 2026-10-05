# Map — "What must be true?"
> **Mindset:** Experienced newcomer. Understand the accepted result before judging it.
> **Test:** "Can I name the material claims, harms, boundaries, evidence identities and limits?"
> RF: [RF__TFW_20261004-174815_LPF.md](../RF__TFW_20261004-174815_LPF.md) at `e19b8a522f2e83cdd842c561091d96a22f597eff`, wording corrected at `b38f4db26d9c265e664e8372ecc95f1b1bd32b0b` (lifecycle `RF`)
> TS: [TS__TFW_20261004-174815_LPF.md](../TS__TFW_20261004-174815_LPF.md), approved by the owner at `9216218d87cc4ab1091062d7900260e09491e814`; prospective scope ruling 1 and correction 1 at `397d396f237557578c899cb357c51c03795f4a72`; unchanged since
> HL: [HL-TFW_20261004-174815_LPF.md](../HL-TFW_20261004-174815_LPF.md), frozen at `efc915a9fa3e4366a3567be800d028ee011c916f`; later edits only in free sections and in the Phase A deliverable list (HL Contract rule 6)
> Accepted subject: Candidate `0863d299d86a1ca1776ffb966d54a1b848e7c348` (parent `397d396f`), Baseline `6c9766fcb2de252e010a790b0fbe676f02058f7c`
> Reviewer unit: `claude-code:agent:local_a7cf0ab7-482d-403e-b738-504d82bba898/lpf-reviewer` = native agent `af28db4ba2fb54c91` in Claude Code session `bd8d3d9f-d605-429a-a889-2c6d2bd03aa5`; activated by [dispatch 15bd](../journal/20261005-093558__dispatch__15bd.md) at `8d6f0d31f4facd0f740023ebfcc967e19935b317`; first message exactly `/tfw-review TFW_20261004-174815_LPF`; return route `claude-code:session:local_a7cf0ab7-482d-403e-b738-504d82bba898`; originating proposer `none`

## Bootstrap record

- **Spine.** `status.md` carries `coordinator_route`, `upstream_route: owner:saubakirov` (matches
  `owner`), `dialogue: tfw-gates-only`, `activation` and `coordination_authority` (both
  `HL-TFW_20261004-174815_LPF.md @ efc915a9…`), `reporting: native-gates`, `selection_ref: baseline`.
  Lifecycle `RF` is the Reviewer gate.
- **Mandate.** HL §4.1 lets the Task Coordinator launch one independent Reviewer as a named
  in-session agent for this task only. Dispatch 15bd is that act: it names this unit, the first
  message, the fixed Candidate, the governing TS/ruling/HL refs and the return route; no owner,
  Executor or peer route.
- **Independence.** This unit was created for the review and carries no Researcher or Executor
  context. It reads no other unit's transcript and does not look for the Executor's removed working
  folder; the Executor is held (dispatch 15bd).
- **Lineage.** `6c9766fc..HEAD` holds nine commits. The Candidate holds exactly 32 VALUE paths and
  nothing else; `e19b8a52`, `b38f4db2` and `8d6f0d31` touch only this task's folder.
- **Session identity.** `REVIEW · LPF` would be the title; an in-session agent has no title surface
  of its own, so title write/readback is unavailable and is disclosed, not claimed.
- **Economics binding** (`.tfw/economics/README.md`, Claude Code JSONL recipe): namespace
  `claude.code-jsonl`; source ID `bd8d3d9f-d605-429a-a889-2c6d2bd03aa5/af28db4ba2fb54c91`; file
  `<session>/subagents/agent-af28db4ba2fb54c91.jsonl`, whose metadata reads back the name
  `lpf-reviewer`; source version `2.1.286`; range start index 0, the line
  `/tfw-review TFW_20261004-174815_LPF` at 2026-10-05T04:36:41.355Z (09:36:41 +05:00); timezone
  `+05:00`; project `my-project`; owner `saubakirov`; role `reviewer`; revision 1. No other unit's
  file is read.
- **Working material.** `<temp>/tfw/TFW_20261004-174815_LPF/` inside this session's scratchpad in
  the system temporary directory; removed before the return.

## Understanding

The Candidate ships the owner-approved Lean Project Footprint rules word for word from RES
iteration 2 W1–W8: working material lives in the system temporary directory under `tfw/<ID>/` and
is removed by its creator; `evidence/` is a registry of *verified · how · observed · result*; a Daily
record lists every product and keeps its folder clean; a comment in a value file carries reader
value or is program-read; every adapter root states both rules in one line; receivers get the 3.9.0
guide with an optional cleanup offer. It then cleans this repository's live code and configuration
under docstring option A (census 277 → 93) and deletes one TS-template row by ruling 1. The purpose
is a repository that holds only result and selected trace (HL §1, NS2.4) without losing
inspectability (NS1).

## Accepted Claims and Boundaries

| ID | Layer | Accepted claim / authority boundary | Risk or concrete harm | Affected behavior / dependencies | Relevant environment | Oracle / authority | Evidence identity (`subject@revision`, source) | Required? |
|---|---|---|---|---|---|---|---|---|
| C1 | VALUE | `conventions.md` carries W2.1–W2.6 once each in their named places; no other line changed (AC-1, DoD 1) | receivers inherit a rule the owner did not approve (S10) or a second, conflicting statement | every role reading §4, §6, §12, §14 | rule text | RES iter2 W2; HL C1, C2, C5; DoD 1 | `.tfw/conventions.md@0863d299` vs `@6c9766fc` | yes |
| C2 | VALUE | EV template is a registry: W3 columns, attested sentence, no Attachments; Environment, accounting row, append rule, Verdict kept (AC-2, DoD 2) | evidence still invites bytes, or the accounting row breaks | every Executor's EV | template text | W3; C2; DoD 2 | `.tfw/templates/evidence/EV.md@0863d299` | yes |
| C3 | VALUE | `handoff.md` steps 8/10/11 carry W4 and its copy is identical; `verify.md` carries W5; no growth (AC-3, DoD 3, DoF 5) | Executor keeps attaching or hands working material on; Reviewer lacks the two checks | Executor Step 2, Reviewer Verify | workflow text | W4, W5; C3; DoD 3 | `.tfw/workflows/handoff.md`, `.claude/commands/tfw-handoff.md`, `.tfw/templates/review/verify.md` `@0863d299` | yes |
| C4 | VALUE | Daily skill §2/§4 and record template §4 carry W6; skill ≤ 1,400 words; entries and installed skills unchanged (AC-4, DoD 4) | Daily keeps piling unlinked outputs or loses products | every Daily turn | extension text | W6; C4; DoD 4 | `.tfw/extensions/daily-task/**@0863d299` | yes |
| C5 | VALUE | W1 appears once in each of four templates (inside `TFW:CLAUDE`/`TFW:CODEX`, fourth Rules bullet in Cursor/Antigravity); duplicate Coordinator row merged; `CLAUDE.md`/`AGENTS.md` changed only inside the blocks; `.agents/rules/tfw.md` equals its template; markers intact (AC-5, DoD 6, DoF 3) | the rule never reaches sessions, or install/update loses its block | install, update, every session | root instructions | W1; C5, C6; DoD 6; manifest | four templates, `CLAUDE.md`, `AGENTS.md`, `.agents/rules/tfw.md` `@0863d299` | yes |
| C6 | VALUE | `.tfw/migrations/3.9.0.md` has the seven W8 parts with the harm in the owner's terms, three answers and the exact receipt row; `[Unreleased]` carries the W8 entry (AC-6, DoD 5) | receivers are cleaned silently, asked wrongly, or not told | next receiver update | guide text vs update workflow and receipt template | W8; C6; DoD 5; `update.md`, `templates/update_receipt.md` | `.tfw/migrations/3.9.0.md`, `.tfw/CHANGELOG.md` `@0863d299` | yes |
| C7 | VALUE | Over the 14 deliverable-6 files every remaining comment/docstring line is program-read or carries reader value; no program-read line removed; behavior unchanged (AC-7, DoD 7, DoF 3, C7) | a shipped script, install or update breaks; correspondence stays | `tfw_economics.py` (shipped), doctor, state, docs generator, config readers | Python 3.13, PyYAML, pytest, MkDocs on this machine | W2.3 option A; correction 1; DoD 7; DoF 3 | 14 paths `@0863d299` vs `@6c9766fc` | yes |
| C8 | VALUE | W7: both chatter passages removed, governing sentences kept, copy identical, words decrease (AC-8) | a governing sentence or link target lost | Knowledge Gate readers, Antigravity Coordinator | rule text | W7 | `.tfw/workflows/knowledge.md`, `.claude/commands/tfw-knowledge.md`, `.tfw/adapters/antigravity/coordinator.md` `@0863d299` | yes |
| C9 | VALUE | `.tfw/templates/TS.md` loses exactly the `evidence/{file}` row (ruling 1) | template keeps contradicting C2, or more changes ride along | every future TS | template text | ruling 1 | `.tfw/templates/TS.md@0863d299` | yes |
| C10 | VALUE | The shipped corpus states C1–C3 without leaving an instruction elsewhere that still invites attachments, the old EV columns or hand-over of working material | receivers' agents follow the stale instruction; the rule is undermined | roles reading other templates/workflows | `.tfw/` text | HL C1–C3, C8; NS1 | `git grep` over `.tfw/@0863d299` | selected (risk) |
| C11 | ASSURANCE | Retained tests, `--help`, doctor outputs, economics `validate` and the MkDocs build show no behavior change (RF §4, E10) | a regression ships unseen | scripts above | this machine | Baseline vs Candidate same-input outputs | rerun on extracted Baseline/Candidate trees | yes |
| C12 | TRACE | This task's trace obeys the rule: `evidence/` holds only EV; removal recorded; no archive/binary/image/file > 1 MiB; no machine path or address (AC-9, DoD 8, DoF 6) | the shipping task contradicts its own rule; a public leak | task folder | Git tree | C2, C7; DoF 6 | `workspace/2026/TFW_20261004-174815_LPF/**@HEAD` | yes (safety floor) |
| C13 | TRACE | No change under `workspace/`, `tasks/`, `daily/`, `tools/migrations/` outside this task (AC-10, DoF 4) | history rewritten | frozen records | Git | DoF 4; hard constraint 2 | `git diff --stat 6c9766fc 0863d299` | yes |
| C14 | TRACE | One `E-accounting` row reproduces the contract: 34-path selector, 32 changed, 258 + 411 = 669 ≤ 1,000, 32 ≤ 33 (AC-11) | budget authority misreported | accounting contract | Git 2.42 | TS §4; conventions `Value-bearing accounting contract` | NUL-safe `git diff` at the two SHAs | yes |
| C15 | TRACE | Accepted-result identity: Candidate is the first tested Executor VALUE commit, reachable, exact-path; VALUE at HEAD equals the Candidate | review judges a different result than the one accepted | landing, acceptance | Git | conventions `Exact-path staging`, accounting contract | commit name sets, ancestry, `git diff 0863d299 HEAD -- <VALUE>` | yes (mandatory) |
| C16 | TRACE | Human authority: owner approved TS, denominator and option A; ruling 1 is prospective and inside Coordinator authority; reserved acts (release, `VERSION`, tag, push) untouched; frozen HL claims unchanged | an unauthorized scope change or release act | owner reservations HL §4.1 | Git, task records | HL §4.1; HL Contract rules 5–6; `Decomposition, constraints, and change authority`; handoff Step 2 | TS@9216218d/397d396f, HL@efc915a9 vs HEAD, Candidate name set | yes (mandatory) |
| C17 | VALUE / TRACE | DoD 9: location rests on RES trials (Claude Code and Codex on this machine, documentation otherwise), EV cites RES; DoD 10: docstring decision recorded in TS | location unproven; owner ruling missing | Working-material rule | RES records | DoD 9, DoD 10 | `research/iter1/RES.md@57159eac`, TS@9216218d | yes |
| C18 | TRACE / VALUE | Safety: no secret, machine path, private name or personal address in task artifacts or shipped text; removal follows no link | public leak; destructive cleanup | public repository; receivers | text | DoF 6; W2.2 | task folder and Candidate diff | yes (safety floor) |

## TS ↔ RF Alignment

| TS requirement | RF claim | Claim IDs | Aligned? |
|---|---|---|---|
| AC-1 | §1 Modified files; §3 AC-1; E1 | C1 | ✅ |
| AC-2 | §1; §3 AC-2; E2 | C2 | ✅ |
| AC-3 | §1; §3 AC-3; E3 | C3 | ✅ |
| AC-4 | §1; §3 AC-4; E4, E5 (live effect DEFERRED by the TS) | C4 | ✅ |
| AC-5 | §1; §3 AC-5; E6 | C5 | ✅ |
| AC-6 | §1 New files; §3 AC-6; E7, E8 (receiver exercise DEFERRED by the TS) | C6 | ✅ |
| AC-7 | §1; §2 decisions 1–4; §3 AC-7; §4; E9, E10 | C7, C11 | ✅ |
| AC-8 | §1; §3 AC-8; E11 | C8 | ✅ |
| AC-9 | §3 AC-9; §5; E12 — the literal leak grep is not empty (three self-referencing TS lines) | C12, C18 | ⚠️ partial — verify the three hits |
| AC-10 | §3 AC-10; E13 | C13 | ✅ |
| AC-11 | §1 accounting table; E-accounting | C14 | ✅ |
| Ruling 1 / correction 1 | §1 accounting; Modified files `TS.md`; §2 decision 1 | C9, C16 | ✅ |
| TS §7 DoF | §3 baseline obligations; §4 | C1–C18 | ✅ |
| HL DoD 9, DoD 10 | E12 (RES citation); TS docstring ruling | C17 | ✅ |

## Verification Selection

| Claim IDs | Planned check or reusable evidence | Why this depth | Known gap or limit |
|---|---|---|---|
| C14, C15, C16 | rerun both NUL-safe commands with the 34 literal paths; commit name sets and ancestry; `git diff 0863d299 HEAD` over VALUE; TS diffs `9216218d→397d396f→HEAD`; HL frozen sections `efc915a9→HEAD`; `VERSION` and tags untouched | mandatory floors; the accounting must be rerun, not trusted | none |
| C1–C6, C8, C9 | whitespace-normalized match of every W "after" text in the Candidate files and absence of every "before" text; hunk positions; `wc -w`; `cmp` of copies; marker line numbers | the owner approved these exact words (S10); TS DoF forbids meaning change | none |
| C7 | census at both revisions; my own line-by-line classification of every remaining line; every removed line checked for program-read forms; search for `__doc__`, `getdoc`, `inspect`, doctest and YAML-comment readers; AST and parsed-YAML comparison | DoF 3 is a hard constraint and option A is a judgment line | none |
| C11 | rerun the retained pytest surface, the four `--help` outputs and doctor/economics on extracted Baseline and Candidate trees | cheap to repeat; C3 asks for repetition, not reuse | pytest 9.0.2 against the `<9` pin, as the RF records |
| C10 | `git grep` over shipped `.tfw/` for residual attachment, old-column, inline-artifact and hand-over wording, then read each hit | coherence of a shipped rule is its purpose; a stale instruction elsewhere defeats it | judgment per hit |
| C12, C13, C18 | `ls`, `git ls-tree -r -l`, extension filter and leak grep over the task folder (including JSONL); read the three TS hits; `git diff --stat` over frozen roots; read removal/link clauses | safety and history floors | none |
| C17 | open RES iter1 H1 matrix and D1–D4; TS docstring ruling text | DoD 9 and DoD 10 are explicit | macOS/Linux, Cursor and the Codex desktop app rest on vendor documentation by design (DoD 9) |
| PV / citations | PV priorities 0–4 fully, 5–7 by relevance; every HL §7.2 and ONB §7 citation for link, existence, semantic match, currentness and relevance | workflow requirement | none |

Out of reach by design: the live effect of AC-4 (next Daily turn) and AC-6 (next receiver update),
both DEFERRED by the approved TS; a native update run on a receiver.

## Deviations from TS

- Selector 34 paths, not 33: `.tfw/templates/TS.md` added by prospective ruling 1 at `397d396f`,
  the Candidate's parent.
- AC-7's `--help` list corrected to four scripts (correction 1, same commit).
- AC-9's literal leak grep returns three lines of the TS's own description of the check.
- The census runs over 13 code/configuration files plus `<!--` over `tools/README.md` (W9's split),
  where the TS gate says "the 14 files".
- The Executor's working folder sat in the session scratchpad inside the system temporary directory;
  TS §6 (non-binding) names `%TEMP%\tfw\<ID>\`.
- `docs/scripts/test_integration.py` ran (MkDocs is installed), as the TS allows.

None is a finding until Verify establishes fact, harm and material consequence.

## Checkpoint

**Self-check:**
- [x] Read RF §§1–5, governing TS AC/DoF, HL purpose/principles, ONB and referenced predecessors?
- [x] Mapped every material accepted claim and the mandatory safety/security, authority and result-identity boundaries?
- [x] Bound each claim to affected behavior/dependencies, environment, oracle/authority and exact evidence identity?
- [x] Recorded a replayable verification selection and every known gap or limit?
- [x] Avoided classifying by filename, discrepancy count or artifact volume?

Stage complete: YES
