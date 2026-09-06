# EV — TFW_20260902-111644_CRATM / Phase D: Team mode and Role Assignment

> **Date**: 2026-09-06
> **Author**: saubakirov (Codex Executor)
> **Task**: TFW_20260902-111644_CRATM
> **TS**: [TS Phase D](../TS__phase-d__team_mode_and_role_assignment.md)

---

## Environment

| Field | Value |
|---|---|
| OS | Microsoft Windows 10.0.26200.9278 |
| Language / Runtime | Python 3.13.5; Git 2.42.0.windows.1; MkDocs 1.6.1 |
| Database | N/A |
| Deploy target | Local repository worktree; documentation build only |
| CI / Pipeline | Local Executor run: `python -m pytest .tfw/scripts/ docs/scripts/ -q` |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | The source-derived contract contains all three declaration facts, separate declaration/activation state, Coordinator and delegate duties, exactly seven owner-return trigger/channel records, degradation behavior, and all eight provider-neutral admission gates. Seventeen positive and negative scenarios matched independent expected decisions; 45 output-changing mutants across 11 families were independently rejected. | Candidate `9edbebcf68872a72a9274765ad053e8d25fa66ac`; Python 3.13.5 | VERIFIED | `phase-d-scenarios.json`; `phase-d-mutants.json` |
| E2 | AC-2 | The live HL template renders `### 4.1 Role Assignment 🔒 FROZEN` before approval/freeze instructions with the six required columns. The row-state matrix covers before/after boundary, approvals, subordinate `—`, wrong unit, missing/ambiguous transitions, role extension, participant/boundary supersession, deletion, and invalid `RESTRICT`; decisions use the active same-unit journal path rather than ordinal comparison. | Candidate product sources parsed by Phase D assurance | VERIFIED | `phase-d-scenarios.json`; `phase-d-mutants.json` |
| E3 | AC-3 | Source-derived records for Plan, Handoff, Research, and Review preserve their Role Locks and implement declared-versus-active checks, gate re-evaluation, direct Coordinator returns, and same-role return routing. The dispatch fixture records Coordinator writer, bounded destination/scope, Role Assignment reference, and TS reference using existing event fields. All eight workflow receivers are byte-identical to their canonical source. | Candidate product sources and copied receivers; Python 3.13.5 | VERIFIED | `phase-d-scenarios.json`; `phase-d-mutants.json`; `phase-d-byte-parity.json` |
| E4 | AC-4 | The Codex profile uses fresh visible independently addressable tasks, separate mutating worktrees, direct `create_thread`/`send_message_to_thread`/`wait_threads`, and same-role reuse; it rejects forks, subagents, relays, hidden helpers, and provider switches as row holders. Operational trace identifies Coordinator `01a07697-f428-7582-ade4-50997a4a6d63` at `C:\Users\c0rpa\.codex\worktrees\12e6\steps-framework` and Executor `01a076b3-d919-7471-9306-c1020b80d43c` at `C:\Users\c0rpa\.codex\worktrees\f8b5\steps-framework`, sharing `D:/projects/research/steps-framework/.git`; direct send/wait receipts preserve role continuity. The trace proves mechanics only, not authority or G8 reliability. The receiver block equals the template and provider/API terms have no positive product leak outside the allowed adapter paths. | Live Codex task chain plus Candidate census/parity checks | VERIFIED | `phase-d-native-profile.json`; `phase-d-census.json`; `phase-d-byte-parity.json`; `phase-d-protected.json` |
| E5 | AC-5 | Candidate changes exactly the approved sixteen VALUE paths plus the two ASSURANCE paths. Canonical/copy hashes and the managed adapter block match; 109 protected Baseline blobs have zero mismatches, Phase E is absent, and the root file outside the managed block is byte-identical. The live-source census classifies 178 occurrences with zero positive provider product leaks. The configured suite, including the real MkDocs build, completed with `655 passed, 1 skipped`; targeted Phase D assurance completed with `5 passed, 179 deselected`; `git diff --check` was clean. | Candidate checkout; pytest; real `python -m mkdocs build --config-file docs/mkdocs.yml` | VERIFIED | `phase-d-test-output.txt`; `phase-d-byte-parity.json`; `phase-d-protected.json`; `phase-d-census.json` |
| E6 | AC-6 | Candidate is the first tested Executor implementation commit and directly follows the ONB state commit; Baseline, approval, dispatch, and Candidate ancestry are recorded. Per-document word counts and every route/corpus payload remain within the existing byte-identical caps: active corpus `32946/33749`, Docs `15278/15278`, and every workflow route/local delta passes. Candidate preceded EV/RF/final state, and no push, release, tag, cap edit, or Phase E work occurred. | Git object database; Candidate context replay | VERIFIED | `phase-d-accounting.json`; `phase-d-context.json`; `phase-d-protected.json`; `phase-d-test-output.txt` |
| E-accounting | AC-6 | Approval `6a7ede0549dca272c149b0294a972c013d5cb291`; immutable Baseline `8e68ab37d300122ff110500ad58f354f76b6210f`; Candidate `9edbebcf68872a72a9274765ad053e8d25fa66ac`. The approved literal sixteen-path selector and the actual membership are identical; every row records path/action/class/reason. Result: 16 logical text files, 180 additions + 423 deletions = 603 touched LOC; binary/non-text is N/A. The immutable approved denominator remains 16 files / 640 touched LOC (420 additions + 220 deletions). Disposition is `KEEP_ONE_PHASE`: `16 < 32`, `603 <= 640`, and `603 < 1280`, so neither growth nor multiplier/zero-growth authority was triggered and no prospective ruling was required. Replay used raw bytes from `git diff --name-only -z` and `git diff --numstat -z`, split independently on NUL, and reproduced 16 names, 16 numstat rows, identical membership, and `180 + 423 = 603`; actual results did not ratchet the denominator or move Candidate. | Repository Git 2.42.0.windows.1; independent Python subprocess byte parser | VERIFIED | `phase-d-accounting.json` |

## Verdict

Evidence verdict: 7/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

## Attachments

| File | Description |
|---|---|
| `phase-d-accounting.json` | Immutable selector, per-path VALUE accounting, NUL-safe replay, lineage, thresholds, and document counts |
| `phase-d-byte-parity.json` | Canonical/copy and managed-block SHA-256 parity |
| `phase-d-census.json` | Classified live-source occurrence and provider-leak census |
| `phase-d-context.json` | Corpus, route, central-range, and workflow-local context measurements |
| `phase-d-mutants.json` | Forty-five output-changing independently rejected mutants across eleven families |
| `phase-d-native-profile.json` | Coordinator/Executor identities, worktrees, direct channel receipts, mechanics, and evidence limit |
| `phase-d-protected.json` | Baseline comparison for 109 protected paths, Phase E absence, and root outside-block parity |
| `phase-d-scenarios.json` | Extracted contract, assignment, workflow, adapter records, fixtures, and seventeen expected/actual cases |
| `phase-d-test-output.txt` | Commands, exits, full-suite result, targeted result, MkDocs execution note, and diff check |

---

*EV — TFW_20260902-111644_CRATM / Phase D: Team mode and Role Assignment | 2026-09-06*
