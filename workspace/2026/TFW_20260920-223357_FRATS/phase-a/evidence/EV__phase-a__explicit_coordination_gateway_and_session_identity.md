# EV — TFW_20260920-223357_FRATS / Phase A: Explicit Coordination, GATEWAY and Session Identity

> **Date**: 2026-09-21
> **Author**: saubakirov via `codex:thread:local:01a0c3a2-c742-7962-a981-369effb5ac83`
> **Task**: TFW_20260920-223357_FRATS
> **TS**: [TS Phase A](../TS__phase-a__explicit_coordination_gateway_and_session_identity.md)

---

## Environment

| Field | Value |
|---|---|
| OS | Windows 11 / Windows_NT x64 `10.0.26200` |
| Language / Runtime | Python 3.13.5; pytest 9.0.2; Git 2.42.0.windows.1 |
| Database | N/A |
| Deploy target | local repository and installed local adapter surfaces |
| CI / Pipeline | local configured suite; no remote CI or receiver mutation |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | One canonical coordination owner; glossary routing; workflows/adapters are local readers; retained terms dispositioned; current issuers zero | Candidate source census | VERIFIED | [copy-and-suite.txt](copy-and-suite.txt) `CURRENT-TERM CENSUS`; `.tfw/conventions.md` §7 |
| E2 | AC-2 | Five-field all-or-none current schema, legacy read/current-write refusal, invalid/partial/unresolved cases, and live post-Candidate migration | Python in-memory fixtures + live phase status | VERIFIED | [coordination-scenarios.md](coordination-scenarios.md) §1; migration commit `9e9513a` |
| E3 | AC-3 | Gates-only vertical edge matrix, exact iterative grant, separate GATEWAY, navigation, and prohibited edges | source inspection + bounded live Codex route | VERIFIED | [coordination-scenarios.md](coordination-scenarios.md) §§3–4; [provider-native.md](provider-native.md) Codex |
| E4 | AC-4 | Provision/activation/continuation separation, exact skill lineage, prompt/briefing/wrong-unit refusals, provenance and title rules | canonical/workflow inspection + live owner-direct activation | VERIFIED | [coordination-scenarios.md](coordination-scenarios.md) §2; current ONB and Codex ledger |
| E5 | AC-5 | Current `gate_answer`, mandatory refs, writer-owned ONB, self/cross-task/stale/missing/hidden-amendment refusal contract | event/status validator fixtures + template/source inspection | VERIFIED | [coordination-scenarios.md](coordination-scenarios.md) §5 |
| E6 | AC-6 | Briefing/RES, ONB/RF and REVIEW provenance; role ownership; independent review; no distrust-only repetition or peer correction | template/workflow matrix | VERIFIED | [coordination-scenarios.md](coordination-scenarios.md) §6 |
| E7 | AC-7 | Canonical/copy and managed-block parity, update migration boundary, syntax, configured suite, no new test, no selector escape | local Git/Python/pytest | VERIFIED | [copy-and-suite.txt](copy-and-suite.txt) `COPY PARITY` and `SYNTAX AND CONFIGURED SUITE` |
| E8 | AC-8 | Same bounded native sequence was attempted independently; authenticated Claude and the owner-authorized same-conversation `agy` readbacks preserve the prior authentication failure, initial contradiction and correction; P0–P4 are separated and never composed | native Codex task tools, Claude Code `2.1.278`, and `agy` `1.2.7` | VERIFIED | [provider-native.md](provider-native.md) |
| E9 | AC-9 | Twelve semantic outcomes, suite, exact-path boundary, no receiver/history/FRATS-D01 mutation | local repository | DEFERRED | [coordination-scenarios.md](coordination-scenarios.md) §7 and [copy-and-suite.txt](copy-and-suite.txt); RF and independent `/tfw-review` remain subsequent Role-Locked gates |
| E-accounting | AC-7, AC-9 | Approval `ad6042dad73aa04b9bbe9f13880c5a944e7e4f05`; Baseline `c80c0dd5e79a6e996fdc68a89ad01b26887c638e`; Candidate `1a9209530d7a939db1270e2f91dcef40a9f449e6`; literal 47-path VALUE selector; 47 MODIFY logical files; 826 + 520 = 1,346 touched text LOC; no binary/rename/deviation; below 50/5,000 triggers and 94/6,400 multipliers; prospective authority and owner approval preceded work; NUL-delimited rename-aware Git method reproduced exactly | local Git 2.42.0 | VERIFIED | [copy-and-suite.txt](copy-and-suite.txt) `NUL-SAFE BASELINE TO CANDIDATE ACCOUNTING` |

## Verdict

Evidence verdict: 8/9 VERIFIED, 1 DEFERRED, 0 BLOCKED, 0 N/A. Accounting is separately VERIFIED.

The single deferral is intentional Role Lock sequencing: RF and independent REVIEW cannot exist before
the Executor finishes EV/RF. It does not hide a missing implementation check or provider claim.

The post-Candidate continuation does not change the verdict counts. Authenticated Claude demonstrated
P2, and the single owner-authorized `agy` correction demonstrated P2 in the same conversation. Neither
provider demonstrated full P3, P4 or a reliability rate.

## Attachments

| File | Description |
|---|---|
| `coordination-scenarios.md` | Status, activation, routing, answer, ownership and six-edge cases. |
| `provider-native.md` | Independent Codex, Claude and Antigravity P0–P4 ledger and limits. |
| `copy-and-suite.txt` | Versions, commands, parity, census, configured suite and exact accounting. |

---

*EV — TFW_20260920-223357_FRATS / Phase A: Explicit Coordination, GATEWAY and Session Identity | 2026-09-21*
