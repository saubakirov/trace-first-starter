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

Preserved costs and limits: provider-native reliability remains Codex P2/Claude P0; dynamic task
inputs remain visible but uncharged; root/provider bootstrap text remains locally available; the old
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
beyond P2/P0, and receiver-specific future update results. Unresolved decision: the independent
Reviewer must judge AC-1–AC-9 and the D75 correction. Continuation: transition Phase B to `RF`,
return only to the recorded Coordinator, then start a separate independent `/tfw-review`; if it
accepts the D75 correction, route `/tfw-docs` and obtain the same Reviewer's bounded follow-up before
terminal closure. No release or receiver mutation is implied.

---

*RF — TFW_20260920-223357_FRATS / Phase B: Corpus Consistency, Compression and Receiver Proof | 2026-09-21*
