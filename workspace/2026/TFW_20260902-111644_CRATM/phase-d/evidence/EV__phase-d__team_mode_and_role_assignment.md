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

## Round 3 — A7 principal/unit correction and root-only named LEAD

This cumulative round preserves the prior EV bytes and binds the corrected result to approved TS revision 3 and immutable Candidate `2363c3d315a855fc0bd6c6dbf683e16bfbaf1726`.

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| R3-E1 | AC-1 | AT remains an explicit owner choice after approved committed HL; one stable named agent principal receives a bounded mandate; declaration, activation, seven owner returns and safe degradation are independently parsed. Fourteen positive/negative mode cases matched. | Candidate source oracle; Python 3.13.5 | VERIFIED | `phase-d-round3-scenarios.json`; `phase-d-round3-mutants.json` |
| R3-E2 | AC-2 | Role Assignment now has a protected selected-LEAD mandate and a separate append-only working-unit trace. One principal may attribute distinct Coordinator/Researcher/Executor/Reviewer units; children do not inherit the root grant, and proposal origin remains `{principal, unit}`. | Candidate templates and canonical contract | VERIFIED | `phase-d-round3-scenarios.json`; `phase-d-round3-mutants.json` |
| R3-E3 | AC-3 | Plan, Handoff, Research and Review resolve actual source/destination/parent units, bounded role/scope, direct channel, dispatch refs and stable proposal origin. Replacement requires owner `SUPERSEDE` plus bounded dispatch; role locks and direct returns remain. | Candidate workflows and accepted-copy parity | VERIFIED | `phase-d-round3-scenarios.json`; `phase-d-round3-test-output.txt` |
| R3-E4 | AC-4 | The supplied Codex profile is admitted only as `ADMIT_SUPPLIED_LIMITED` with disclosed G1–G7/no-G8; each additional profile requires one native all-eight trial and partial receipts never compose. The adapter creates directly addressable role tasks, not per-role profiles. | Candidate adapter and source-derived admission matrix | VERIFIED | `phase-d-round3-scenarios.json`; `phase-d-round3-mutants.json` |
| R3-E5 | AC-5 | All canonical/accepted copies, managed receiver parity, protected history, provider boundaries, unaffected workflow cues, full configured suite and real strict MkDocs build passed. Build exit was 0; all 24 unique unresolved-reference tokens pre-exist Candidate and retain identical Markdown occurrence counts, so the 30 warning forms are inherited historical-link noise rather than new AT behavior. Post-Candidate cumulative EV/RF trace validation also passed 21 Phase D tests. | Windows local worktree; pytest; MkDocs | VERIFIED | `phase-d-round3-test-output.txt`; `phase-d-round3-mkdocs-baseline.json` |
| R3-E6 | AC-6 | Pre-approval 18 VALUE + 2 ASSURANCE WIP survived the trace/approval fast-forward with identical path/hash digest and zero overlap. Approval-to-Candidate lineage is legal. Baseline replay returns exactly 21 VALUE paths and 459 + 462 = 921 touched LOC; the old 18/760 forecast, observed 18/866 WIP, approved 21/932 forecast and actual 21/921 are separately disclosed. | Git 2.42.0.windows.1; approval epoch and Candidate objects | VERIFIED | `phase-d-round3-wip-preservation.txt`; `phase-d-round3-accounting.txt`; `phase-d-round3-a5.json` |
| R3-E7 | AC-7 | Only a valid selected agent principal acting in its exact root Coordinator unit renders `LEAD · {handle} · {TASK}[ · {PHASE}]` for Plan/Resume. Sixteen cases keep same-principal children, child Coordinators, human/different/unselected/stale/forwarded/wrong-role/missing/ambiguous inputs and Research on ordinary cues; readback failure reports once. All fourteen predicate/identity/consumer mutants were rejected. | Source-derived navigation oracle | VERIFIED | `phase-d-round3-scenarios.json`; `phase-d-round3-mutants.json` |

Round 3 evidence verdict: 7/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A.

Round 3 attachments: `phase-d-round3-scenarios.json`, `phase-d-round3-mutants.json`, `phase-d-round3-accounting.txt`, `phase-d-round3-wip-preservation.txt`, `phase-d-round3-a5.json`, `phase-d-round3-test-output.txt`, `phase-d-round3-mkdocs-baseline.json`.

## Round 4 — rendered-LEAD collision and finite continuation repair

This cumulative Rung-1 round preserves all prior EV bytes and binds the ruled repair to replacement Candidate `fac67ef443c5cb50a766cc6c6c639ea60a259437` under unchanged approved TS rev3.

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| R4-E1 | AC-7 | Canon now defines `RENDERED:=BASE|LEAD_BASE`, so collision, shortest stable-key prefix, exact readback and fail-soft behavior apply to both forms. Qualified roots keyed `ab7`/`ac9` render `LEAD · cratm-main · CRATM · D · @ab` and exact readback claims it. Missing key and altered readback each report once and continue unclaimed. Root Plan/Resume, same-principal child and child-Coordinator results remain unchanged. | Candidate source-derived oracle; Python 3.13.5 | VERIFIED | `phase-d-round4-scenarios.json`; `phase-d-round4-mutants.json` |
| R4-E2 | AC-6 | The continuation guard uses a finite exact set for cumulative ONB/RF/EV, rev3/rev4 REVIEW and three stages each, seven exact attachment names per round, status, and a closed phase-journal filename grammar. The committed rev3 ruling tip and complete anticipated Round-4 Executor→Reviewer sequence pass; arbitrary review/evidence, unsuffixed attachments, product/assurance and malformed/unrelated TRACE fail. A post-Candidate run with all seven Round-4 attachments staged passed 22 Phase D tests, proving the complete Executor TRACE surface is admitted. | Candidate Git/source integration oracle | VERIFIED | `phase-d-round4-scenarios.json`; `phase-d-round4-mutants.json`; `phase-d-round4-test-output.txt` |
| R4-E3 | AC-5, AC-7 | All 19 navigation cases and 23 output-changing mutants passed, as did 22 Phase D tests, the complete configured suite (`668 passed, 1 skipped`), strict MkDocs (exit 0), copy/protected-history checks and `git diff --check`. The accepted warning claim stays bounded to 24 pre-existing tokens with unchanged occurrence counts. | Windows local worktree; pytest; MkDocs; Git | VERIFIED | `phase-d-round4-test-output.txt`; `phase-d-round4-mkdocs-baseline.json` |
| R4-E-accounting | AC-6 | Approval `b755de9128f2b0442615a4ca8b787761f937bbcd`; ruling `61c7364fac7e377a7e3b76c09d376dcd26475c98`; Baseline `8e68ab37d300122ff110500ad58f354f76b6210f`; replacement Candidate `fac67ef443c5cb50a766cc6c6c639ea60a259437`. Candidate changes exactly the ruled one VALUE plus two ASSURANCE paths. Baseline replay remains exactly 21 MODIFY/VALUE files and 463 + 464 = 927 touched text LOC, 5 below approved 21/932; binary/non-text N/A. Historical 16/640 remains immutable; 21 < 32 and 927 < 1,280, so `KEEP_ONE_PHASE`, no ratchet or new authority. The exact approved NUL-safe selector is unchanged. | Git 2.42.0.windows.1; immutable objects | VERIFIED | `phase-d-round4-accounting.txt`; `phase-d-round4-wip-preservation.txt`; `phase-d-round4-a5.json` |

Round 4 evidence verdict: 4/4 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A.

Round 4 attachments: `phase-d-round4-scenarios.json`, `phase-d-round4-mutants.json`, `phase-d-round4-accounting.txt`, `phase-d-round4-wip-preservation.txt`, `phase-d-round4-a5.json`, `phase-d-round4-test-output.txt`, `phase-d-round4-mkdocs-baseline.json`.
