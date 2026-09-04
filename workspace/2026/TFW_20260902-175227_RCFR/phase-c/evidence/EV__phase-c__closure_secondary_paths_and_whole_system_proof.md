# EV — TFW_20260902-175227_RCFR / Phase C: Closure, Secondary Paths, and Whole-System Proof

> **Date**: 2026-09-04
> **Author**: saubakirov (via Codex)
> **Task**: TFW_20260902-175227_RCFR
> **TS**: [TS Phase C](../TS__phase-c__closure_secondary_paths_and_whole_system_proof.md)

---

## Environment

| Field | Value |
|-------|-------|
| OS | Microsoft Windows NT 10.0.26200.0 |
| Language / Runtime | Python 3.13.5 |
| CI / Pipeline | local Executor worktree at immutable baseline `cf36dd6ac404b2335234cd9763bc4821409ca9fc` |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | The source-derived graph reproduced all five primary entry totals and the 9,873-word secondary carrier anchor; every emitted row includes checkpoint, source/range, purpose, authority, words, repeat, dynamic, and charged fields, while omission/address/preload mutants fail independently. | immutable Git baseline plus candidate tree | VERIFIED | [runtime-context-whole-system.txt](runtime-context-whole-system.txt) |
| E2 | AC-2 | Resume, Docs, Knowledge, Release, Update, Config, and Init each dispatch once through a thin skill into one complete workflow-owned Read Contract; ordinary, refusal, WAIT, provenance, approval, and repair semantics match baseline, and one output-changing mutant per command is rejected. | source-derived baseline/candidate oracle | VERIFIED | [semantic-and-lifecycle-whole-system.txt](semantic-and-lifecycle-whole-system.txt) |
| E3 | AC-3 | Status and journal templates retain every required field, bound, reader, transition rule, compatibility rule, and pre-write checkpoint; overlong summary, undeclared human, invalid kind, malformed time, terminal/illegal/missing transition pairs, and malformed token/stamp are refused before installation. | temporary status/event fixtures and real validator | VERIFIED | [verification-whole-system.txt](verification-whole-system.txt) |
| E4 | AC-4 | Active secondary surfaces contain no unexplained obsolete glob, unbounded history preload, role-from-manifest rule, invalid registry address, or competing Read Contract; every deletion/consolidation and every surviving duplicate has an authority, test, and history disposition. | baseline/current source census with deliberate mutations | VERIFIED | [stale-duplicate-ledger.txt](stale-duplicate-ledger.txt) |
| E5 | AC-5 | Seven canonical secondary workflows equal Claude and retained singular Antigravity copies byte-for-byte; seven Codex source skills equal installed copies; the exact 4×11 manifest topology installs, reruns without byte changes, repairs secondary drift, and preserves unrelated/unmarked content. | four empty temporary receivers | VERIFIED | [clean-receiver-secondary-routes.txt](clean-receiver-secondary-routes.txt) |
| E6 | AC-6 | Existing P/R/E/V/C/A records remain source-derived; added secondary, lifecycle/closure, and adapter records independently match immutable baseline expectations. Minimal-anchor input fails, expected data cannot feed production, and every family mutant changes a named produced field before rejection. | clean-context source trees and isolated mutations | VERIFIED | [semantic-and-lifecycle-whole-system.txt](semantic-and-lifecycle-whole-system.txt) |
| E7 | AC-7 | All changed secondary/lifecycle paths exceed or meet the 30% reduction floor, primary paths stay at or below their entry ceilings, canonical trajectory falls 63.9%, and the unique active `.tfw` corpus falls 51.7%; dynamic and relevance-selected inputs remain explicit and uncharged. | identical `\S+` method on baseline and candidate | VERIFIED | [runtime-context-whole-system.txt](runtime-context-whole-system.txt) |
| E8 | AC-8 | 492 tests collected; full suite is 491 passed and 1 skipped; project consistency exits zero; task diagnostics contain only the ruled immutable RDP 123>120 event; 41 implementation/test files and 4,109 changed LOC stay within scope, with zero new runtime files or excluded changes. | final local candidate before RF | VERIFIED | [verification-whole-system.txt](verification-whole-system.txt) |

## Verdict

Evidence verdict: 8/8 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

---

*EV — TFW_20260902-175227_RCFR / Phase C: Closure, Secondary Paths, and Whole-System Proof | 2026-09-04*

---

## Return Round 1 — REVIEW `b33d534` / Coordinator ruling `7bded93`

This revision supplements the original evidence without rewriting it. E9–E11 directly close the
three Rung-1 findings in the live REVIEW; all other acceptance surfaces remain unchanged.

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E9 | AC-6 | All 11 Phase C cases produce each of six semantic fields from separately resolved baseline/candidate source clauses before comparison. The expected map is poisoned before production without affecting output; each of 11 source mutants changes its named field and fails the independent expected comparison. | immutable `cf36dd6` plus candidate tree and in-memory source mutants | VERIFIED | [semantic-and-lifecycle-whole-system.txt](semantic-and-lifecycle-whole-system.txt) |
| E10 | AC-3 | The live current-event pre-write gate rejects 4 impossible calendar/time/offset values, 4 absolute refs, 2 task-escaping refs, and 4 non-string/multiline/over-ceiling summaries; it accepts 3 normalized relative refs. Two adverse immutable legacy events remain readable through `read_journal`, with the historical ceiling diagnostic retained. | actual validator plus temporary journals | VERIFIED | [verification-whole-system.txt](verification-whole-system.txt) |
| E11 | AC-2, AC-4, AC-5 | Docs and Release now express the single baseline role `Coordinator`. A census derived from 11 baseline/current manifest rows reconciles workflow locks/headings, 22 canonical/installed skills, and 22 tracked workflow copies with zero errors; 8 omission/duplicate/stale/conflict/parity mutants fail. Affected file hashes match. | candidate source graph, immutable baseline, and four-vendor integration tests | VERIFIED | [stale-duplicate-ledger.txt](stale-duplicate-ledger.txt), [clean-receiver-secondary-routes.txt](clean-receiver-secondary-routes.txt) |

### Return Verification

- Targeted ruled-item set: 43 passed, 266 deselected.
- Full affected modules: 370 passed.
- Full configured suite: 509 collected; 508 passed, 1 skipped.
- Project check: exit 0. Task check: the one ruled immutable RDP `123>120` diagnostic only.
- Scope: 41 implementation/test files and 4,480 changed LOC from `cf36dd6`; ceilings 44/5,000;
  zero new runtime, `tasks/`, prior-phase, or release/version files.
- Runtime results remain above every frozen threshold: 63.9% trajectory reduction and 51.7%
  active-corpus reduction.

Return evidence verdict: 3/3 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A. The current cumulative
evidence now supports AC-1 through AC-8; the immutable RDP diagnostic remains a ruled exclusion.

---

*EV Return Round 1 — TFW_20260902-175227_RCFR / Phase C | 2026-09-04*
