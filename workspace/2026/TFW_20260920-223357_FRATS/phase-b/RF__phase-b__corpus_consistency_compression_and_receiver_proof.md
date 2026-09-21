# RF — TFW_20260920-223357_FRATS / Phase B: Corpus Consistency, Compression and Receiver Proof

> **Current filename**: `RF__phase-b__corpus_consistency_compression_and_receiver_proof.md`; later rounds append to this file.
> **Date**: 2026-09-21
> **Author**: `saubakirov`, via Codex Executor
> **Status**: 🟢 RF — Complete; independent review required
> **Parent HL**: [Master HL](../HL-TFW_20260920-223357_FRATS.md)
> **Phase HL**: [Phase B derivation](HL__phase-b__corpus_consistency_compression_and_receiver_proof.md)
> **TS**: [Approved Phase B TS](TS__phase-b__corpus_consistency_compression_and_receiver_proof.md)
> **Producer unit**: `codex:thread:local:01a0c415-c362-78b3-98e9-00d728c5ac18` (`EXEC · FRATS · B`)
> **Parent Coordinator**: `codex:thread:local:01a0bfdb-f0b7-7642-837c-8c47d0a284cf`
> **Activation / dispatch source**: owner-direct `/tfw-handoff frats phase b`
> **Coordination authority**: `../HL-TFW_20260920-223357_FRATS.md @ c80c0dd5e79a6e996fdc68a89ad01b26887c638e`
> **Originating proposer**: `none`

---

## 1. What Was Done

Phase B consolidated repeated activation, knowledge-return and template-handover rules into their
canonical owners; repaired contradictory Reviewer ownership, a dead glossary reference and stale
configuration wording; completed one deterministic filename issuance grammar; and regenerated all
twenty Claude/Antigravity workflow projections from the ten canonical workflows. Persistent entry
surfaces required no change and remain exact. No runtime, registry, restored audit or new permanent
test was added.

The behavioral result is smaller but not selected by size: ten-command reader exposure fell
114,221→113,405 (−816; −0.7144%) and unique active `.tfw` corpus fell 37,818→37,061
(−757; −2.0017%). The semantic result is the acceptance basis: all six protected edges retain a
positive and material-negative replay, current filename producers emit one path, and canonical/copy
parity is exact.

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `8c02d42375c3838ff62586bf5221b63f46d78446` |
| Baseline / Candidate | `1a9209530d7a939db1270e2f91dcef40a9f449e6` / `fd0655ce17f2c650d238622c1d6a57ec5dd9a204` |
| Candidate lineage | Initial tested implementation `aeb7c45af778f0541890c15a44d10e833ee3f5f9`; a final stale EV-template naming note was then corrected in VALUE, tests were rerun, and Candidate moved to descendant `fd0655ce17f2c650d238622c1d6a57ec5dd9a204`. The earlier commit is superseded, not separately nominated. |
| VALUE membership | Exactly the approved 47 paths, all class `VALUE`: 39 MODIFY and 8 ZERO-DIFF. Every path/action/owner/reader/semantic reason is in the [instruction ledger](evidence/instruction-disposition-ledger.md); exact per-path additions/deletions are in [adapter and suite evidence](evidence/adapter-and-suite.txt). |
| Arithmetic | 365 additions + 507 deletions = 872 touched text LOC; 47 logical files; 39 changed + 8 zero-diff; net −142 lines; binary/non-text N/A. |
| Membership deviations | None. No VALUE path outside the selector changed; no ASSURANCE path changed. |
| Trigger disposition | Actual 39 changed paths / 872 touched LOC stays below 50/5,000 prompts and 94/9,600 owner ceiling. The coupled owner→reader→projection product remains one phase; no prospective ruling was needed. |
| Authority and timing | Immutable 47-file / 4,800-LOC denominator approved prospectively at the TS approval ref. Actual result neither ratchets nor replaces it. |
| Reproduction | The TS's unchanged NUL-safe `git diff --name-status/--numstat --find-renames=50% -z Baseline Candidate -- $valuePaths` method; numeric fields only, `-` binary/N/A. |

This reports the approved contract; it does not create a selector, move Candidate after TRACE-only
writes, ratchet the denominator or supply late authority.

### New Files

| File | Description |
|---|---|
| `evidence/current-corpus-and-exposure.txt` | Immutable historical replay and separate current successor selector/results. |
| `evidence/instruction-disposition-ledger.md` | Complete 47-path owner/reader/delivery/disposition ledger and filename fixtures. |
| `evidence/six-edge-replay.md` | Per-consolidation six-edge map, positive cases and material-negative mutants. |
| `evidence/adapter-and-suite.txt` | Copy/managed-surface parity, checks and exact accounting. |
| `evidence/receiver-replay.md` | One epoch-bound read-only replay across four receiver repositories. |
| `evidence/EV__phase-b__corpus_consistency_compression_and_receiver_proof.md` | Per-AC evidence index and verdict. |
| `RF__phase-b__corpus_consistency_compression_and_receiver_proof.md` | This Executor return. |

All are class `TRACE` and were created after Candidate selection.

### Modified Files

| Files | Changes |
|---|---|
| `.tfw/conventions.md`, `.tfw/glossary.md` | Canonical activation/routing and filename ownership; REVIEW, deferral and scope wording repairs. |
| Seven templates: `HL`, `TS`, `RES`, `ONB`, `RF`, `REVIEW`, `evidence/EV` | Exact current filenames and compact shared handover contract. |
| Ten `.tfw/workflows/*` command sources | Role-local bounded reads, exact producer paths, compact handover and Update/Init/Config consistency. |
| Ten `.claude/commands/*` and ten `.agents/workflows/*` targets | Regenerated byte-identical projections of canonical workflows. |

Eight approved paths are zero-diff: `.tfw/README.md`; Codex, Claude and Antigravity persistent
source/target pairs; and the Cursor persistent source. Their local bootstrap/recovery value remains
valid, so no cosmetic edit was made.

## 2. Key Decisions

1. Semantic preservation decided subtraction. Size was measured only after source→reader→delivery
   ownership and all six edge consequences were known.
2. Shared provider-neutral meaning lives in conventions; workflows keep algorithmic checkpoints;
   templates keep required fields; provider copies remain exact delivery projections.
3. Ordinary role workflows rely on the already-active root delivery and perform compact task-local
   spine checks. Update/Init load the canonical activation section only when repairing an adapter.
4. New primary artifact issuance has one topology-aware grammar. `research/iterN/RES.md` is the only
   current research-result path; root `RES__*` and other legacy variants remain readable history.
5. The historical RCFR measurement and current successor remain separate series. The old audit was
   loaded from immutable history for evidence, not restored as a maintained product reader.
6. Receiver evidence is bounded by repository and timestamp. Older versions, project dirt and RYC's
   unmarked `AGENTS.md` prevent a universal migration claim.

### D75 correction package — for `/tfw-docs` after review

The Executor did not edit `KNOWLEDGE.md`. Its current D75 impact cell says
`310,485→112,536 (−63.8%)`, while the terminal Phase C RF records
`310,485 → 112,206 (63.9% lower)` and `66,436 → 32,088 (51.7% lower)` at
`workspace/2026/TFW_20260902-175227_RCFR/phase-c/RF__phase-c__closure_secondary_paths_and_whole_system_proof.md:185`.
The Phase C EV records the same 63.9%/51.7% result in E7, and final REVIEW rev3 independently says
fresh audit reproduces both reductions. Fresh immutable replay in this phase reproduces the exact
112,206/32,088 pair.

If the independent Reviewer accepts the correction, `/tfw-docs` should replace only D75's impact
cell with this exact text:

```text
Trajectory 310,485→112,206 (−63.9%); active `.tfw` 66,436→32,088 (−51.7%); changed paths ≥30%, no primary regression, four receivers/11 routes, suite 520/1
```

The D75 decision text and citations remain unchanged. The later documentation commit must receive
the same independent Reviewer's bounded follow-up before `DONE`; otherwise the initial verdict must
remain explicitly conditional.

## 3. Acceptance Criteria

- [x] AC-1 — reproduced the historical immutable measurement and recorded a reproducible, separate ten-command successor with exact bridge/limits.
- [x] AC-2 — closed a 47-path instruction ledger and one current filename grammar with historical-read compatibility.
- [x] AC-3 — passed positive/material-negative replay for activation, authority, evidence, recovery, continuation and exception.
- [x] AC-4 — established canonical ownership and justified every preserved repetition; no percentage quota or replacement runtime.
- [x] AC-5 — proved ten canonical workflows, twenty generated copies and three installed persistent surfaces exact; bounded Cursor/provider claims.
- [x] AC-6 — captured stable start/end epochs for Helpdesk, KazNPU, AFD and RYC without writes.
- [x] AC-7 — passed configured checks, command-entry dry-run, diff/scope/copy checks and exact immutable accounting; no new tests.
- [x] AC-8 — this RF gives one owner-readable comparison and the exact sourced D75 correction route without editing knowledge.
- [ ] AC-9 — Executor Candidate/EV/RF complete; independent REVIEW, accepted docs follow-up and terminal Coordinator lineage are downstream and intentionally not self-approved.

## 4. Verification

- Lint (`python -m pytest tools/tests/ docs/scripts/ -q --collect-only`): 14 tests collected; exit 0.
- Tests (`python -m pytest tools/tests/ docs/scripts/ -q`): 14 passed in 3.97s; exit 0.
- Command-entry evaluation (`python docs/scripts/command_entry_eval.py dry-run --repetitions 1`): `errors=[]`, `valid=true`, denominator 18; exit 0.
- Canonical projections: 20/20 Claude/Antigravity copies have the canonical Git blob; persistent managed/full-copy surfaces pass.
- `git diff --check`: clean.
- Receiver replay: all four start/end HEAD/branch/status tuples equal; no receiver mutation.
- Historical replay: exit 0, 569 audit lines, exact accepted 112,206/32,088 terminal values.

Preserved costs and limits: accepted evidence remains Codex P2 with partial P3, authenticated Claude
P2, and Antigravity P2 with partial P3, with no full P3/P4 or reliability rate; dynamic task inputs
remain visible but uncharged; root/provider bootstrap text remains locally available; the old
harness has unresolved Phase-A-era anchors and is not claimed for those cases; no receiver upgrade,
release, push, publication or deployment was tested or authorized.

## 5. Evidence

See [EV](evidence/EV__phase-b__corpus_consistency_compression_and_receiver_proof.md) for the evidence index.

Evidence verdict: 9/10 VERIFIED, 1 DEFERRED, 0 BLOCKED, 0 N/A.

The deferred item is only the independent-review and terminal-closure remainder of AC-9.

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|---|---|---|---|
| 1 | `KNOWLEDGE.md` | 128 | todo | D75 says 112,536/−63.8%; terminal Phase C artifacts and fresh replay resolve 112,206/−63.9%. Exact replacement and owning `/tfw-docs` route are in §2. |
| 2 | Four receiver repositories | epoch in receiver evidence | todo | KazNPU/AFD run older TFW releases, and RYC has an unmarked project-owned `AGENTS.md`; future updates require separate owner action and preservation checks. |

## 7. Fact Candidates

No fact candidates. All execution findings are agent-readable repository or command evidence; no new
human-sourced fact was introduced.

## 8. Strategic Insights (Execution)

No strategic insights. The implementation applied the approved HL/TS and created no new human-sourced
domain implication.

## 9. Diagrams

No diagrams.

### Material handover at this return

Actual producer: Executor unit `codex:thread:local:01a0c415-c362-78b3-98e9-00d728c5ac18`, acting as
`saubakirov` via Codex from the owner-direct `/tfw-handoff frats phase b` activation. Authorized
recipient: Coordinator unit `codex:thread:local:01a0bfdb-f0b7-7642-837c-8c47d0a284cf`.

Source epoch: TS approval `8c02d42375c3838ff62586bf5221b63f46d78446`, Baseline
`1a9209530d7a939db1270e2f91dcef40a9f449e6`, tested Candidate
`fd0655ce17f2c650d238622c1d6a57ec5dd9a204`, and receiver verification epoch
2026-09-21T14:06:17.5456556Z–14:06:19.3562146Z. Inspected scope: all 47 VALUE paths, ten canonical
workflow graphs and twenty generated copies, persistent adapter surfaces, configured checks, both
metric series, historical semantic oracle where its anchors resolve, current six-edge replays, D75
source lineage, and four receiver repositories read-only.

Material return: tested Candidate, six bounded evidence attachments, EV, this RF, exact 39/8 and
365+507 accounting, exact copy/receiver immutability results, and the D75 correction package.
Uncertainty retained: old-oracle cases whose retired anchors no longer resolve, provider behavior
beyond the accepted Codex/Claude/Antigravity bounds stated above, and receiver-specific future update
results. Unresolved decision: the independent
Reviewer must judge AC-1–AC-9 and the D75 correction. Continuation: transition Phase B to `RF`,
return only to the recorded Coordinator, then start a separate independent `/tfw-review`; if it
accepts the D75 correction, route `/tfw-docs` and obtain the same Reviewer's bounded follow-up before
terminal closure. No release or receiver mutation is implied.

---

*RF — TFW_20260920-223357_FRATS / Phase B: Corpus Consistency, Compression and Receiver Proof | 2026-09-21*

---

## Return Round 1 — R1–R3 Replacement Result

> **Date**: 2026-09-21
> **Status**: 🟢 RF — Rung-1 return complete; independent re-review required
> **Activation**: delegated same-Executor continuation under
> `HL-TFW_20260920-223357_FRATS.md @ 35fba767abd768413237bf6416102e189f1d91e6`
> **Ruled REVIEW**: `44f9a6135293a3a68af7a537a4875d722f25d5bf`, §8 R1–R3
> **Producer**: `codex:thread:local:01a0c415-c362-78b3-98e9-00d728c5ac18`
> **Coordinator**: `codex:thread:local:01a0bfdb-f0b7-7642-837c-8c47d0a284cf`

This numbered return section supersedes the original RF's Candidate/accounting/metric, validator-path
and provider-limit statements where different. The original rejected round remains openable above
and at its immutable commit.

### 1. What Was Done

R1 consolidated Plan, Handoff, Review and Update to 923/937/998/988 `\S+` words from the Reviewer's
1,433/2,101/2,136/2,630 observations while preserving activation, authority, evidence, recovery,
continuation and exception carriers. All ten canonical workflows are now ≤1,200 words. The eight
affected Claude/Antigravity copies were regenerated; all 20 generated copies exactly match their ten
canonical sources.

R2 corrects the validator source to `tools/tfw_state.py` and adds an exact Candidate-object command
plus positive/material-negative output in `evidence/rung1-semantic-replay.txt`. R3 restores the
accepted Phase A limits: Codex P2 with partial P3, authenticated Claude P2, Antigravity/`agy` P2 with
partial P3, and no full P3/P4 or reliability rate. These bounds are sourced by
[Phase A RF](../phase-a/RF__phase-a__explicit_coordination_gateway_and_session_identity.md) §2.5 and
[Phase A REVIEW](../phase-a/REVIEW__phase-a__explicit_coordination_gateway_and_session_identity.md) §1.

#### Actual Value-Bearing Accounting

| Fact | Replacement result |
|---|---|
| TS / ruled return | TS approval `8c02d42375c3838ff62586bf5221b63f46d78446`; REVIEW ruling `44f9a6135293a3a68af7a537a4875d722f25d5bf` |
| Baseline / Candidate | `1a9209530d7a939db1270e2f91dcef40a9f449e6` / `50ed7fb8c09cfc32e67623848b0551f9ada881da` |
| Candidate lineage | Replacement Candidate is the first tested descendant containing the R1 VALUE repairs; rejected `fd0655ce…` remains history and is not nominated. |
| VALUE membership | Same approved 47 paths: 39 MODIFY, 8 ZERO-DIFF; class/reason ledger unchanged except explicit F12–F15 dispositions. |
| Arithmetic | 1,283 additions + 2,823 deletions = 4,106 touched text LOC; net −1,540; all text; no rename/binary. |
| Deviations | None. Other Baseline→Candidate paths are governing/TRACE history, not added VALUE. |
| Trigger/authority | 39 changed / 4,106 touched is below 50/5,000 prompts and 94/9,600 ceiling. Immutable 47/4,800 denominator and boundaries remain owner-approved; no prospective ruling needed. |
| Reproduction | Unchanged TS NUL-safe literal-selector commands; full final table in `evidence/adapter-and-suite.txt`. |

New TRACE file: `evidence/rung1-semantic-replay.txt`. Modified VALUE: four canonical workflows and
their eight generated projections. Modified TRACE: the affected evidence attachments, EV and RF only.

### 2. Key Decisions

1. Delete repeated explanation, not gates: exact state, refusal, artifact, evidence, return and
   exception behavior remains local to each workflow.
2. Preserve live cross-reference anchors such as Review `Step 2: Verify`; metric discovery and Config
   registry resolution pass on the replacement Candidate.
3. Treat provider levels as inherited accepted evidence, not a new native test or reliability claim.

### 3. Acceptance Criteria

- [x] AC-1 — identical successor selector now measures 114,221→107,850 exposure and 37,818→31,813 active corpus; historical series remains separate.
- [x] AC-2 — F12–F15 explicitly close all four word-bound contradictions; filename census remains valid.
- [x] AC-3 — exact Candidate-source replay passes all six positive/material-negative cases; validator path exists and self-resolves.
- [x] AC-4 — every canonical workflow is ≤1,200 words with canonical ownership and no replacement runtime.
- [x] AC-5 — 20/20 copies exact; provider claims match accepted Phase A limits and do not exceed P3/P4 evidence.
- [x] AC-6 — original read-only receiver epoch remains applicable; R5 ruled no receiver mutation or new epoch is owed.
- [x] AC-7 — configured checks, dry-run, copy parity and final immutable accounting pass.
- [x] AC-8 — owner-readable result and verified D75 correction route remain unchanged.
- [ ] AC-9 — replacement Candidate/EV/RF complete; same independent Reviewer judgment and later accepted docs/terminal lineage remain downstream.

### 4. Verification

- Word bound: all ten canonical workflows pass; maximum is Init at 1,197.
- Lint: 14 tests collected; exit 0.
- Tests: 14 passed in 3.95s; exit 0.
- Command-entry dry-run: `errors=[]`, `valid=true`, denominator 18.
- Generated copies: 20/20 canonical blob matches.
- Successor metric: trajectory 107,850 (−6,371; −5.5778% from Baseline); unique corpus 31,813
  (−6,005; −15.8787%).
- Six-edge replay: six positives pass; six material negatives reject, including real validator
  diagnostics for missing authority and illegal same-state transition.
- `git diff --check`: clean.

### 5. Evidence

See [EV](evidence/EV__phase-b__corpus_consistency_compression_and_receiver_proof.md) and its Return
Round 1 rows. Replacement evidence verdict: 9/10 VERIFIED, 1 DEFERRED, 0 BLOCKED, 0 N/A. The deferred
portion is only independent acceptance/docs follow-up/terminal lineage in AC-9.

### 6. Observations (out-of-scope, not modified)

No new observations. Original D75 and receiver observations retain their ruled R4/R5 dispositions;
R4 is a post-APPROVE `/tfw-docs` effect and R5 is terminal not-owed.

### 7. Fact Candidates

No fact candidates. The delegated mandate and rulings are already durable governing artifacts, not
new human-only project knowledge.

### 8. Strategic Insights (Execution)

No strategic insights. This round implements the closed Reviewer/Coordinator bound only.

### 9. Diagrams

No diagrams.

### Material handover at this return

Producer: same Executor unit `codex:thread:local:01a0c415-c362-78b3-98e9-00d728c5ac18`, acting as
`saubakirov` via Codex. Recipient: Coordinator unit
`codex:thread:local:01a0bfdb-f0b7-7642-837c-8c47d0a284cf`. Source epoch: mandate `35fba767…`, ruled
REVIEW `44f9a613…`, approved TS `8c02d423…`, Baseline `1a920953…`, replacement Candidate
`50ed7fb8…`. Inspected scope: R1–R3, four canonical workflows/eight projections, all ten word
counts/copy blobs, affected metrics/tests, Candidate validator source, Phase A provider RF/REVIEW and
affected evidence/RF/EV. Material return: R1–R3 complete with no scope deviation. Uncertainty remains
only at the accepted provider evidence limits and downstream independent acceptance.
Continuation: transition to `RF`, return only to the Coordinator, and route the same independent
Reviewer through `/tfw-review`; no docs effect, receiver write, release or close occurs in this unit.

---

## Return Round 2 — Revision 2 and Transcript-Isolation Result

> **Date**: 2026-09-22
> **Status**: 🟢 RF — revision 2 and necessary constituent complete; independent review required
> **Producer unit**: `codex:thread:local:01a0c415-c362-78b3-98e9-00d728c5ac18`
> **Parent Coordinator**: `codex:thread:local:01a0bfdb-f0b7-7642-837c-8c47d0a284cf`
> **Activation / dispatch source**: delegated continuation under mandate
> `HL-TFW_20260920-223357_FRATS.md @ 35fba767abd768413237bf6416102e189f1d91e6`
> **Governing order**: revision-2 approval `116a324bb38d5ca21094bf6c5d528620d4ec4121`
> plus prospective necessary-constituent ruling `68d85cc20b285e2dce083d23519d3394056033f4`
> **Originating proposer**: owner `saubakirov` through the recorded Coordinator unit

This numbered section supersedes earlier Candidate, metric, workflow-bound, provider-entry,
receiver-epoch and accounting claims where different. Rejected and replaced epochs remain readable
above and at their immutable commits.

### 1. What Was Done

Revision 2 restores the Coordinator's exact Strategic Architect identity and nine-step planning
behavior, preserves the post-approval dispatch paragraph under the resolved gate answer, installs one
Phase/Step/Stage/Gate vocabulary and ≤1,400-word ceiling, normalizes active workflow headings/links,
and makes provider coordination entry disclose four capabilities honestly. REVIEW §10 then closes
the remaining passive-observation loophole: another active role's transcript, reasoning, tool output,
terminal and unreturned working tree are not coordination or evidence surfaces. Bounded wait/status,
one addressed status request and named artifacts/commits after durable return remain permitted.

#### Actual Value-Bearing Accounting

| Fact | Final result |
|---|---|
| TS approval ref | `116a324bb38d5ca21094bf6c5d528620d4ec4121` |
| Necessary-constituent authority | REVIEW §10 at `68d85cc20b285e2dce083d23519d3394056033f4`, committed before its eight VALUE writes |
| Baseline / Candidate | `1a9209530d7a939db1270e2f91dcef40a9f449e6` / `93186cea9ac8209cade30a49e76f3b8a32ae6227` |
| Candidate lineage | Tested descendant of prior input `627182ab5292454a00d37bb2062547a67d203387`; later TRACE writes do not move it. |
| VALUE membership | Exact approved 47 paths, all MODIFY-or-zero-diff VALUE: 46 modified and `.tfw/README.md` zero-diff. Per-path actions and cumulative semantic reasons are in the disposition ledger; exact arithmetic table is in `evidence/adapter-and-suite.txt`. |
| Arithmetic | 1,675 additions + 2,982 deletions = 4,657 touched text LOC; net −1,307; 47 logical files; binary/non-text N/A; no rename. |
| Membership deviations | None. Paths outside the selector are governing/TRACE history, not added VALUE. |
| Trigger disposition | 46/4,657 remains below the 50-file/5,000-LOC prompts and 94-file/9,600-LOC owner ceiling. REVIEW §10 prospectively admitted only the necessary constituent inside unchanged boundaries; no split or added assurance was required. |
| Authority and timing | Owner approved immutable 47/4,800 denominator in revision 2 before implementation; it never ratchets. REVIEW §10 predates Candidate `93186cea…`. |
| Reproduction | The TS's exact literal selector and NUL-safe `name-status`/`numstat` commands are unchanged; numeric fields are text LOC and `-` is binary/N/A. |

This reports the approved contract; it does not create a selector, move Candidate, ratchet the
denominator or supply late authority.

#### New TRACE File

| File | Description |
|---|---|
| `evidence/rung2-semantic-replay.txt` | Exact-object replay for AC-10–AC-12 and transcript isolation; no role transcript input. |

#### Modified Implementation Families

| Files | Changes |
|---|---|
| `.tfw/workflows/*.md` plus 20 projections | Exact AC-10 Plan behavior, AC-11 heading normalization, preserved six-edge carriers and ≤1,400 words; every projection equals its canonical source. |
| `.tfw/glossary.md`, `.tfw/conventions.md` | Exact four-term vocabulary, Design Rules, active anchor repair and one exact transcript-isolation owner rule. |
| Four adapter templates; `AGENTS.md`, `CLAUDE.md`, `.agents/rules/tfw.md` | Honest four-capability disclosure and shortest provider-specific transcript-isolation mapping with managed/full-copy parity. |
| Templates named by the 47-path selector | Cumulative Phase B naming and handover repairs retained; no new artifact class. |

### 2. Key Decisions

1. Exact owner text is semantic authority, not a compression target: Plan remains 1,370 words, below
   the approved 1,400 ceiling, with the gate-answered dispatch paragraph intact.
2. Vocabulary normalization changes ordered-action headings only; true task phases, cognitive stages,
   Config modes and historical artifacts remain unchanged.
3. Transcript isolation owns the policy once in Coordination; adapters contain only executable
   surface mappings. A suspected stall yields bounded wait/status or one addressed request, never
   hidden inspection or reconstructed reasoning.
4. Candidate evidence comes from named artifacts, commits and local checks. No agent transcript,
   session output or unreturned working tree is an evidence source.

### 3. Acceptance Criteria

- [x] AC-1 — identical successor measurement yields 114,221→110,512 trajectory and 37,818→33,220 active corpus; historical series remains separate.
- [x] AC-2 — F1–F19 disposition ledger closes the cumulative active-source census.
- [x] AC-3 — exact-source positive/material-negative entry, continuation, provider and isolation cases pass while prohibited inspection refuses.
- [x] AC-4 — canonical ownership remains singular; all workflows are ≤1,400 without filler or new runtime/control surface.
- [x] AC-5 — 20/20 projections and all installed managed/full adapter targets match sources; provider evidence bounds are unchanged.
- [x] AC-6 — four receiver repositories match start/end at the declared final epoch and were not mutated.
- [x] AC-7 — configured checks, 54-schedule dry-run, links, headings, parity and exact final accounting pass.
- [x] AC-8 — owner-readable final metrics/accounting/limits and the exact D75 post-APPROVE route are present; `KNOWLEDGE.md` is untouched.
- [ ] AC-9 — Candidate, EV and RF are complete; independent verdict, accepted docs effect/follow-up and terminal Coordinator lineage are downstream.
- [x] AC-10 — exact Strategic Architect mindset/nine planning steps, Coordination read, state route and retained dispatch behavior resolve; Plan is 1,370 words.
- [x] AC-11 — exact vocabulary/Design Rules, heading map, active anchors and ≤1,400 ceiling resolve; 84/84 checked links pass.
- [x] AC-12 — provider-honest capability entry and transcript-isolation mappings produce the same explicit owner boundary without false orchestration.

### 4. Verification

- Canonical word counts: Plan 1,370; Research 1,014; Handoff 937; Review 1,005; Docs 739;
  Knowledge 1,042; Release 726; Update 1,003; Config 749; Init 1,209 — all ≤1,400.
- Generated copies: 20/20 byte-identical; Codex/Claude managed blocks and Antigravity full target
  match their sources.
- Tests: `python -m pytest tools/tests/ docs/scripts/ -q` → 14 passed in 4.00s, exit 0.
- Command-entry dry-run: `--repetitions 3` → `errors=[]`, `valid=true`, denominator 54, exit 0.
- Candidate diff check: no output, exit 0.
- Relative links: 42 changed VALUE Markdown blobs, 84 checked links, 0 missing.
- Active headings: no operational `Phase N`, `Plan gates`, `## N.` or colon-form `Step N:`.
- Semantic replay: all exact-text, entry/continuation/GATEWAY/provider and isolation cases PASS.
- Receiver replay: all four start/end boundaries equal; no write or transcript/session inspection.

### 5. Evidence

See [EV](evidence/EV__phase-b__corpus_consistency_compression_and_receiver_proof.md) Return Round 2.
Final-Candidate evidence verdict: 12/13 VERIFIED, 1 DEFERRED, 0 BLOCKED, 0 N/A. The deferred row is
only AC-9's independent acceptance, ruled docs/follow-up and terminal lineage.

### 6. Observations (out-of-scope, not modified)

No new observations. The original D75 discrepancy remains independently verified and routed by R4
to `/tfw-docs` only after APPROVE; receiver upgrades/customization changes remain not owed by Phase B.

### 7. Fact Candidates

No fact candidates. The owner decisions are already durable in the approved TS, gate answer and
REVIEW §10 ruling; implementation facts are repository-readable.

### 8. Strategic Insights (Execution)

No strategic insights. This return implements the exact owner-approved and prospectively ruled
bounds without adding an Executor-authored project strategy.

### 9. Diagrams

No diagrams.

### Material handover at this return

Producer: same Executor unit `codex:thread:local:01a0c415-c362-78b3-98e9-00d728c5ac18`, acting as
`saubakirov` via Codex. Recipient: recorded Coordinator unit
`codex:thread:local:01a0bfdb-f0b7-7642-837c-8c47d0a284cf`. Source epoch: mandate `35fba767…`,
revision-2 approval `116a324b…`, resolved gate answer `6a43c85d…`, prospective transcript-isolation
ruling `68d85cc…`, Baseline `1a920953…` and final Candidate `93186cea…`. Inspected scope: the literal
47-path selector, AC-1–AC-12, exact owner text, F1–F19 ledger, ten workflows/20 projections, seven
provider source/target paths, configured checks, metric graphs, four receivers read-only and all
affected evidence attachments. Material return: one tested descendant Candidate with no scope or
membership deviation. Uncertainty remains only in independent judgment and downstream D75
publication/closure. Continuation: transition Phase B to `RF`, return only to this Coordinator, and
start the same independent `/tfw-review`; after APPROVE, route only the already-ruled docs/follow-up
and terminal sequence. No peer dialogue, transcript inspection, receiver mutation, release or push.
