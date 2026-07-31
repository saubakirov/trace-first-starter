# EV — TFW-49 / Phase B: Workflow and Adapter Consumption

> **Date**: 2026-07-31
> **Author**: Executor (Codex)
> **Task**: TFW-49
> **TS**: [Phase B TS](../TS__phase-b__workflow_and_adapter_consumption.md)

---

## Environment

| Field | Value |
|-------|-------|
| OS | Microsoft Windows NT 10.0.26200.0 |
| Language / Runtime | Python 3.13.5; standard-library production router |
| Git | 2.42.0.windows.1 |
| Test / render tools | pytest 9.0.2; MkDocs 1.6.1 |
| Deploy target | Local isolated Git fixtures and generated localhost site only; no remote target |
| CI / Pipeline | Local Executor run |

## Proof Record Index

| Proof Record | Claim / AC | Boundary and proof class | Method or observation | Actual result | Artifact / provenance | Actor / time _(when material)_ | Debt |
|--------------|------------|--------------------------|-----------------------|---------------|-----------------------|--------------------------------|------|
| PR-B1 | AC-1 — one router consumes the Phase A semantic owners | Local; Seam: Phase B router ↔ Phase A schema/state/module | Import/source scan; schema role/fixed-work mutations; owner-removal behavior through the unchanged Phase A suite | The production router imports `commit_identity`, resolves accepted role/work values from the loaded schema, and contains no accepted grammar pattern, registry, trailer vocabulary, Git execution, hook/configuration, or publication implementation. Owner mutations change or reject routing instead of activating a Python fallback | `.tfw/scripts/commit_identity_router.py`; `.tfw/scripts/test_commit_identity_router.py`; combined contract run `285 passed` | N/A — deterministic local ownership relation | None |
| PR-B2 | AC-1 — exact workflow map without action inflation | Local; Seam: router policy ↔ 11 canonical workflow authorities | Exhaustive 11-workflow × 4-surface resolution, unknown/role/work negative cases, schema normalization, and canonical source action query | All 11 approved workflow rows resolve with the TS role/task/work rules. Only handoff, docs, and release contain router action cues; the other eight remain mapping-only, and update's existing clone remains an auxiliary fetch | Router `describe` output; workflow/action tests in `.tfw/scripts/test_commit_identity_router.py` | N/A — deterministic local map | None |
| PR-B3 | AC-2 — truthful ordinary/reserved/replay operation routing | Local; Seam: router ↔ public Phase A parser/formatter ↔ temporary Git repositories | Positive and negative matrices for ordinary, merge, amend, fixup, squash, revert, and cherry-pick; every four-field mismatch; same/cross context; nested reserved source; actual temporary commits and Git-parsed trailers | Ordinary/merge use current context; amend retains identity only on exact equality and otherwise re-identifies; cross-context autosquash fails; cross-context replay returns `--no-commit`, inspection, and a current-operator subject; same-context generated replay remains truthful. Temporary-Git fixtures cover all seven same-context outcomes, all five context-sensitive cross branches, and schema-owned source/origin trailers | `.tfw/scripts/test_commit_identity_router.py`; Phase B router suite `149 passed` | N/A — isolated local Git seam | None |
| PR-B4 | AC-3 — explicit guarded context and secret-safe failure | Local; Seam: explicit inputs/staged paths ↔ Phase A validation/diagnostics | Guarded `task:none`, task-owned rejection, mixed/stale/unknown/missing input matrix, real staged-path fixture, CLI capture with message/path/environment/credential-shaped canaries | `task:none` requires declared non-task lifecycle work and staged-path inspection; task-scoped/mixed work stops; every context or operation field fails closed with stable correction; captured diagnostics omit rejected bodies, configured paths, environment values, hook material, credential-shaped sentinels, and tracebacks | `.tfw/scripts/test_commit_identity_router.py`; router CLI failure capture | N/A — local validation/non-disclosure is the complete claim | None |
| PR-B5 | AC-4 — point-of-action consumption and F26 separation | Local; Seam: router ↔ three canonical workflows ↔ exact installed copies | Source/action query plus rendered inspection of generated handoff, docs, and release pages | Handoff routes the local ONB/final commit and removes “Commit and push ONB”; docs uses `docs/coordinator`; release uses explicit task or guarded `none` with `release/coordinator`. All three separate local completion from push/publication, and TFW-49 `APPROVE PUSH` remains unavailable. Rendered pages show the cues, gate, and STOP without horizontal overflow (`1265/1265`) | `.tfw/workflows/{handoff,docs,release}.md`; generated `reference/workflows/{handoff,docs,release}/`; browser observation, 2026-07-31 | Executor, 2026-07-31 — local rendered QA | None |
| PR-B6 | AC-5 — registered adapter declarations and installed parity | Local; multi-source Seam: four templates ↔ three installed entry consumers ↔ workflow copies ↔ Codex skills | Exact surface/block query, managed-block comparison, byte comparisons, absent/live and legacy-path assertions | Each template declares only its registered surface and delegates all other authority to workflow/router context. Installed Antigravity/Claude/Codex entry behavior matches its owner; all 11 Antigravity and 11 Claude workflow copies are byte-exact; all 11 Codex skill pairs remain byte-exact; Cursor live path remains absent; both legacy `tfw-task.md` files remain unchanged | Four `.tfw/adapters/*` entry templates; installed consumers; parity tests in `.tfw/scripts/test_commit_identity_router.py` | N/A — deterministic source/interface relation | None |
| PR-B7 | AC-6 — regression, warning, exact-scope, protected-state, audit, and no-publication boundary | Local; Seam: Phase B tree ↔ Phase A regression/docs/render/Git state | Combined tests, docs pair, identical-input isolated MkDocs builds, normalized warning-record set comparison, exact allowlist, protected diff/hash/presence checks, `git diff --check`, exclusive-anchor audit, local ahead/ref/config hashes | Contract suites pass `285`; docs pass `68`; both MkDocs builds exit 0 with `294/294` warning records, `139/139` normalized distinct records, and `0 added / 0 removed`. Framework write set is exactly 28 (2 CREATE, 26 MODIFY); Phase A owners/config/template are unchanged; `.tfw/hooks` and live Cursor path are absent; local `core.hooksPath` is unset; protected global value is compared only by entry count/non-reversible hash. Pre-final-commit audit is valid for 12 exclusive descendants with `actor_authentication:false`; `origin/master` remains `b4c0a06dc9fbc104c5b8997865b6df3211bd5c0c` | Commands and results in RF §4; baseline `95f95c730e4365606cb5b1aafc796cdf1fd6ae21`; local tree; no remote operation | Executor, 2026-07-31 | None |
| PR-B8 | AC-7 — traceable local completion and explicit Phase C/review stop | Local; Seam: implementation ↔ EV/RF/Task Board ↔ local C1-R history | Structural trace scan, AC-to-PR mapping, Task Board row inspection, router-planned completion subject, final post-commit audit/protected-state rerun | ONB, EV, RF, implementation scope, and the single Task Board row form the Phase B Executor trace. The completion subject is routed as `[codex/TFW-49/phase-b/executor] ...`; the final commit remains local. Independent REVIEW, Phase C hook/client/platform proof, full TFW-49 closure, authentication, and publication are explicitly unclaimed. The final commit necessarily postdates its own RF and is audited immediately after creation, with that self-referential result reported to the Coordinator | This EV; `../RF__phase-b__workflow_and_adapter_consumption.md`; `README.md`; post-commit Coordinator report | Executor, 2026-07-31 | None |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Intended-environment observation is not triggered for local semantic ownership and deterministic workflow resolution; Local/Seam Proof is PR-B1/PR-B2 | Local schema/module/source fixtures | N/A | PR-B1, PR-B2 |
| E2 | AC-2 | Phase B claims a local operation plan and temporary-Git contract, not representative client/platform execution; the latter remains Phase C | Local temporary Git repositories | N/A | PR-B3 |
| E3 | AC-3 | Context rejection and diagnostic non-disclosure are complete local output properties; no real secret or external hook body was accessed | Synthetic canaries and local staged-path fixtures | N/A | PR-B4 |
| E4 | AC-4 | Workflow source/render behavior is locally inspectable; no remote publication event is intended or authorized in Phase B | Generated local MkDocs site | N/A | PR-B5 |
| E5 | AC-5 | Adapter and installed-copy parity is a deterministic source/interface relation; final representative cross-agent execution is explicitly Phase C | Approved local consumer set | N/A | PR-B6 |
| E6 | AC-6 | Regression, protected-state, Git-range, and warning comparisons are local proof; no hook-runtime, authentication, hosted, or remote-state outcome is claimed | Local repository and isolated local copies | N/A | PR-B7 |
| E7 | AC-7 | Trace integrity and local commit identity do not trigger intended-environment observation or independent acceptance | Local Executor traces/history | N/A | PR-B8 |

### Status Consequences

- Every Phase B Requirement Claim is deliberately local or a source/Git-fixture seam;
  none depends on an intended live environment.
- The rendered browser observation supports the local documentation-consumption seam
  only; it is not final cross-agent execution or publication evidence.
- Phase C remains responsible for hook installation/configuration and representative
  client/platform behavior. That future scope is not Value Debt because Phase B does
  not claim those outcomes.
- Evidence status does not authenticate an actor, approve the phase, or replace
  independent REVIEW.

## Verdict

Evidence verdict: 0/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 7 N/A

## Value Debt

No Value Debt.

## Attachments

No binary attachments.

---

*EV — TFW-49 / Phase B: Workflow and Adapter Consumption | 2026-07-31*
