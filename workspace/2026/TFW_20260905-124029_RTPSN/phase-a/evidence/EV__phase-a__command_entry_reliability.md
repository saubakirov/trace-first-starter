# EV — TFW_20260905-124029_RTPSN / Phase A: Command Entry Reliability

> **Date**: 2026-09-05
> **Author**: saubakirov (Executor, via Codex)
> **Task**: TFW_20260905-124029_RTPSN
> **TS**: [TS Phase A](../TS__phase-a__command_entry_reliability.md)

---

## Environment

| Field | Value |
|---|---|
| OS | Microsoft Windows 11 Pro 10.0.26200 |
| Language / Runtime | Python 3.13.5; pytest 9.0.2; Codex CLI 0.151.0-alpha.7.2 |
| Database | N/A — no database is in Phase-A scope |
| Deploy target | Local repository Candidate `0636bc80da74ed686a01bdbe514c6a9921997d52`; production skill baseline retained |
| CI / Pipeline | Local; live attempts pinned to `gpt-5.6-sol` / `medium` |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | Exact 11-command × 4-adapter census records canonical source, role, target, source, parity, installed, clean-receiver, and live state separately; revision-pinned and normalized entry counts preserve CRATM/RTPSN classification, H3 refutation, and the six-level claim boundary. | Candidate Git tree plus frozen research traces; only Codex has any live observation | VERIFIED | `command-entry-topology.txt` |
| E2 | AC-2 | Explicit non-default harness builds six hashed disposable fixtures, three validated arms, an exact 54-run schedule, event/diff graders, fail-closed budgets, redaction, retained invalid attempts, Wilson/Newcombe statistics, independent summary, and safe cleanup. Fake-runner/mutant unit suite passes 31 tests; dry-run leaves no residue. | Python 3.13.5; local fake runner for tests; Codex invocation only behind `run` | VERIFIED | `test-output.txt`; `command-entry-summary.json`; Candidate `docs/scripts/command_entry_eval.py` and `docs/scripts/test_command_entry_eval.py` |
| E3 | AC-3 | The approved command and denominator were preserved, but 54 valid runs could not complete under the approved ceiling. First two valid runs reported 162,311 tokens, projecting 4,382,397 for 54; seven completed before delivered STOP, reporting 702,852 total tokens, and one interrupted attempt has explicitly unreported telemetry. No partial denominator or substituted run was accepted. | Codex CLI 0.151.0-alpha.7.2; `gpt-5.6-sol` / `medium`; local ephemeral Git fixtures | BLOCKED | `command-entry-trials.jsonl` run IDs and `run_end`; `command-entry-summary.json` (`valid_runs=7`, `valid_denominator=54`, `ac3_status=BLOCKED`); `test-output.txt` |
| E4 | AC-4 | Independent recomputation applies the safe terminal branch exactly once: `BASELINE RETAINED`; comparative rule is not applied, production skill edits are unauthorized, and no superiority claim is made. Both production skill trees are byte-identical to Baseline. | Raw partial JSONL plus Candidate Git diff | VERIFIED | `command-entry-summary.json` decision object; `command-entry-counts.txt` Candidate/skill diff |
| E5 | AC-5 | Conventions own one six-step pre-action contract and six evidence levels; adapter docs distinguish declared/tracked/installed/clean/live states; Codex remains a thin router, full-copy receivers remain canonical copies, manifest remains tooling-only, and independent route/load/role/order/stop/parity/generated-input mutants pass. No workflow, manifest, root preload, title grammar, or production skill changed. | Immutable Candidate | VERIFIED | `test-output.txt`; Candidate `.tfw/conventions.md`, `.tfw/adapters/README.md`, `.tfw/adapters/codex/README.md`, `docs/scripts/test_runtime_context.py`, `docs/scripts/test_integration.py` |
| E6 | AC-6 | Exact four-by-eleven topology, current source/copy parity, four clean receivers, all-command context counts, four-design scorecard, targeted 282-test suite, full 612-pass/1-skip suite, project consistency, Candidate scope, and NUL-safe accounting pass. | Immutable Candidate; Python/pytest/Git versions above | VERIFIED | `command-entry-counts.txt`; `test-output.txt`; `command-entry-topology.txt` |
| E7 | AC-7 | All Phase-A evidence links resolve inside the phase folder; every runtime/effect claim is bounded by revision, evidence level, host/model/effort, and known limits. RF inputs state H3 remains refuted and H4 remains inconclusive. Phase-B naming, owner verdict A1, rejected A2, and CRATM authority remain untouched. | Phase-A TRACE set and Candidate diff | VERIFIED | This EV plus `command-entry-topology.txt`, `command-entry-counts.txt`, `command-entry-trials.jsonl`, `command-entry-summary.json`, and `test-output.txt` |
| E-accounting | AC-6 | Approval `8866090960cb403e5254bf017bb2423b8171b0f2`; Baseline `7bc0f30736ff1456c5d9dd74286a4e3a94c63361`; Candidate `0636bc80da74ed686a01bdbe514c6a9921997d52`; approved NUL-safe selector yields only `M .tfw/conventions.md` (universal contract/evidence ladder), `M .tfw/adapters/README.md` (four-adapter/claim-state docs), and `M .tfw/adapters/codex/README.md` (thin baseline/live boundary), all Phase-A VALUE; conditional 22 skills absent; 3 logical files; 81 additions + 0 deletions = 81 touched text LOC; binary/non-text N/A; triggers not reached (3<50, 81<5,000); immutable 25-file/800-LOC denominator approved prospectively and unchanged; no unresolved/INVALID attribution. | Baseline/Candidate Git objects; Candidate checked out before TRACE writes | VERIFIED | `command-entry-counts.txt` exact commands, NUL-rendered output, membership, authority/timing, trigger disposition, and Candidate scope |

`E-accounting` reproduces the approved TS selector. It does not redefine the selector, move
Candidate, ratchet the denominator, or use late authority.

## Verdict

Evidence verdict: 7/8 VERIFIED, 0 DEFERRED, 1 BLOCKED, 0 N/A

AC-3 is terminally blocked for this approved matrix. The production result remains
`BASELINE RETAINED`; this resolves safe Phase-A implementation without converting the partial
sample into behavioral or architectural superiority.

## Attachments

| File | Description |
|---|---|
| `command-entry-topology.txt` | Exact 11×4 census, revision comparison, evidence ladder, and incident/hypothesis boundary |
| `command-entry-trials.jsonl` | Redacted raw seven completed live attempts plus explicit Coordinator STOP record |
| `command-entry-summary.json` | Independent rates, intervals, usage, limitations, AC-3 status, and terminal decision |
| `command-entry-counts.txt` | Per-command/design context estimates and exact VALUE/Candidate accounting |
| `test-output.txt` | Environment, exact dry-run schedule, input hashes, raw STOP math, tests, consistency, parity, and cleanup output |

---

*EV — TFW_20260905-124029_RTPSN / Phase A: Command Entry Reliability | 2026-09-05*
