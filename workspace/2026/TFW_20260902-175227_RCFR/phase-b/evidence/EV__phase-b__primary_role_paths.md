# EV — TFW_20260902-175227_RCFR / Phase B: Primary Role Paths

> **Date**: 2026-09-04
> **Author**: saubakirov (via Codex)
> **Task**: TFW_20260902-175227_RCFR
> **TS**: [TS Phase B](../TS__phase-b__primary_role_paths.md)

---

## Environment

| Field | Value |
|-------|-------|
| OS | Windows |
| Language / Runtime | Python 3.13.5; pytest 9.0.2 |
| Deploy target | Local isolated worktree and pytest temporary receivers |
| CI / Pipeline | Local |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | The source-derived audit resolves immutable commit `80382fbffd52b1f13cb3b38e8e450ecc0fef2fd5`, reproduces all five fixed baselines exactly, classifies charged/dynamic/repeated edges, and rejects route, heading, and duplicate-preload mutations. | Immutable Git tree plus candidate worktree | VERIFIED | [runtime-context-primary-roles.txt](runtime-context-primary-roles.txt) |
| E2 | AC-2 | Coordinator P1–P4 and Researcher R1–R3 produce the same six semantic fields as baseline; targeted high-risk mutants fail; both research modes have explicit read graphs; thin skills contain no independent full preload. | SourceTree fixtures over baseline and candidate | VERIFIED | [semantic-primary-roles.txt](semantic-primary-roles.txt) |
| E3 | AC-3 | Executor E1–E4 preserve onboarding, dependencies, build/evidence failure, and revision behavior; unsupported VERIFIED evidence and build-failure mutants are rejected; ONB/RF transitions and the hard stop remain asserted. | SourceTree initial/revision fixtures | VERIFIED | [semantic-primary-roles.txt](semantic-primary-roles.txt) |
| E4 | AC-4 | Reviewer V1–V4 and C1 preserve independent verification, Purpose Check, citation bar, disposition routing, and hard stop; 42% sampling and 100% discrepancy escalation remain asserted; deliberate PV/Purpose rereads are separately reported. | Independent Reviewer source fixtures | VERIFIED | [semantic-primary-roles.txt](semantic-primary-roles.txt); [runtime-context-primary-roles.txt](runtime-context-primary-roles.txt) |
| E5 | AC-5 | Four empty receivers expose all 11 commands with exact primary roles; repeated sync is byte-idempotent; drift is repaired; unmarked/related project content is preserved; canonical/installed primary copies are exact. | Four pytest temporary receivers | VERIFIED | [clean-receiver-primary-routes.txt](clean-receiver-primary-routes.txt) |
| E6 | AC-6 | Targeted and full test suites pass, all five paths exceed 30% reduction, combined reduction is 72.4%, project check passes, scope is 23 files/1,005 LOC, and the only task diagnostic is the immutable RDP `123>120` exception. | Candidate worktree and immutable baseline | VERIFIED | [verification-primary-roles.txt](verification-primary-roles.txt) |

## Verdict

Evidence verdict: 6/6 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

---

*EV — TFW_20260902-175227_RCFR / Phase B: Primary Role Paths | 2026-09-04*
