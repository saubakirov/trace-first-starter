# EV — TFW_20260905-124029_RTPSN / Phase B: Session Identity Ergonomics

> **Date**: 2026-09-06
> **Author**: codex/TFW_20260905-124029_RTPSN/phase-b/executor
> **Task**: TFW_20260905-124029_RTPSN
> **TS**: [TS Phase B](../TS__phase-b__session_identity_ergonomics.md)

---

## Environment

| Field | Value |
|---|---|
| OS | Microsoft Windows 11 Pro 10.0.26200, build 26200 |
| Language / Runtime | Python 3.13.5; pytest 9.0.2; MkDocs 1.6.1; Git 2.42.0.windows.1 |
| Database | N/A — documentation/workflow repository |
| Deploy target | N/A — local Candidate and clean temporary receivers |
| CI / Pipeline | Local isolated Git worktree on `codex/rtpsn-phase-b-exec` |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | One 33-word authority, exact WORK vocabulary, state precedence, A1 suffix, fail-soft transport, glossary-only router, and seven changing/rejected mutant families | Candidate source parser | VERIFIED | [contract](session-identity-contract.txt), [scenarios](session-identity-scenarios.json), [mutants](session-identity-mutants.json) |
| E2 | AC-2 | Manifest-derived 7 task/conditional + 4 project-wide census, exact checkpoints/modes, deletion/reorder rejection, and four clean receivers | Candidate + temporary receivers | VERIFIED | [coverage](session-identity-coverage.txt) |
| E3 | AC-3 | Nine charged profiles, active corpus, 260/45 local caps, estimated tokens, copy hashes, protected spans/selectors, and semantic-preserving compression | Baseline/Candidate Git + Python graph oracle | VERIFIED | [context](session-identity-context.txt) |
| E4 | AC-4 | 15 title/fallback scenarios, 16 workflow-mode records, complete record fields, and work/task/phase/collision/transport/checkpoint/authority mutants | SourceTree projections; no TS/evidence runtime input | VERIFIED | [scenarios](session-identity-scenarios.json), [mutants](session-identity-mutants.json) |
| E5 | AC-5 | Exact local Codex readback for new Executor and resumed Coordinator titles, code points/counts, direct-ID retrieval, and honest N/A for unavailable literal search/visible truncation and unobserved hosts | Codex desktop metadata API | VERIFIED | [readback](session-title-readback.json), [visibility](session-title-visibility.txt) |
| E6 | AC-6 | 268-test gate and 629-test full suite green; project check green; task check has only the named pre-existing RDP defect; Candidate clean and protected | Local Candidate worktree | VERIFIED | [test output](test-output.txt), [context](session-identity-context.txt) |
| E-accounting | AC-6 | Approval `f904af8`; full Baseline/Candidate; 23 explicit VALUE members, all M and Phase B; 360 + 240 = 600; binary 0/N/A; triggers below 50/5000; prospective authority; NUL-safe replay | Git 2.42 / local worktree | VERIFIED | [accounting](session-identity-accounting.txt) |

## Verdict

Evidence verdict: 7/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A.

AC-5 contains expected N/A submetrics for a non-exposed literal-search API and unavailable text-turn
screen observation. Those limitations are themselves recorded and do not broaden the host claim.

## Attachments

| File | Description |
|---|---|
| `session-identity-contract.txt` | Authority, grammar, precedence, fallback, hashes, and ruling. |
| `session-identity-coverage.txt` | Eleven-route matrix, modes, ordering, receivers, and negative cases. |
| `session-identity-context.txt` | Graph/corpus/local words, token estimates, compression, parity, and protection. |
| `session-identity-scenarios.json` | Source-derived normal and workflow-mode records. |
| `session-identity-mutants.json` | Seven output-changing independently rejected source mutants. |
| `session-title-readback.json` | Bounded local Codex title metadata and exact readback. |
| `session-title-visibility.txt` | Retrieval, visibility, N/A, and cross-host limits. |
| `session-identity-accounting.txt` | Immutable NUL-safe Baseline→Candidate VALUE accounting. |
| `test-output.txt` | Candidate environment, tests, receivers, checks, and known external defect. |

---

*EV — TFW_20260905-124029_RTPSN / Phase B: Session Identity Ergonomics | 2026-09-06*
