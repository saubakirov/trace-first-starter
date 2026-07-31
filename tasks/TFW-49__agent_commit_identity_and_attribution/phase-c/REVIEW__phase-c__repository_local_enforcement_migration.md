# REVIEW — TFW-49 / Phase C: Repository-Local Enforcement, Migration, and Cross-Agent Proof

> **Date**: 2026-07-31
> **Author**: Reviewer (Codex)
> **Verdict**: 🔄 REVISE
> **Review Mode**: code
> **RF**: [RF Phase C](RF__phase-c__repository_local_enforcement_migration.md)
> **TS**: [TS Phase C](TS__phase-c__repository_local_enforcement_migration.md)
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> This file synthesizes stage findings; stage files retain the verification detail.

---

## 1. Map

Phase C adds the clean `1.1.0` project-state template, exact root-inclusive audit,
recognized two-hook runtime, private Git-common-dir lifecycle ledger, bounded local
carrier, and five canonical lifecycle integrations plus ten derived copies. The
baseline-to-RF scope is exactly 29 framework paths, three Executor trace paths, and one
Task Board transition; protected Phase A/B, config, knowledge, adapter, and remote
boundaries remain unchanged.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|------------------|--------|----------|
| 1 | Exact 29-path scope and RF measurements | PASS | 29/29; 6 create/23 modify; 7310→9944; +2768/−134 |
| 2 | Contract/state/template and both range modes | PASS | exact current 21-object audit plus topology fixtures |
| 3 | Current runtime, hashes, modes, config, private ledger | PASS for current tree | valid `1.1.0`, exact three-file inventory, relative-owned |
| 4 | Closed runtime recognition | **FAIL D1** | extra file, arbitrary non-empty entrypoint, and extra manifest key are accepted |
| 5 | Lifecycle idempotence and exact prior state | **FAIL D2** | prior `.tfw/hooks` → second rollback returns `E_RUNTIME_LEDGER_REQUIRED` |
| 6 | Router/carrier/seven operations/4×4/context/diagnostics | PASS | 345-suite reproduction and targeted source/runtime checks |
| 7 | Windows and Ubuntu WSL live hook boundary | PASS | exact declared Git/Python versions and actual hooks |
| 8 | Canonical/derived workflow parity and F26 | PASS | 10/10 byte-exact; publication remains separately authorized |
| 9 | Docs tests, pinned warnings, rendered links/anchors | PASS | 68; 317/317, 157/157, +0/−0; 10/10 pages |
| 10 | PR-C1–PR-C12 and all 12 EV dispositions | **FAIL D3** | PR-C3/4/10/12 and E3/E4/E10 overclaim D1/D2 coverage |
| 11 | Knowledge/phase citations | PASS | 28/28 resolve; no contradiction |
| 12 | Protected state and publication boundary | PASS | clean tree before traces; origin remains `b4c0a06...`; no remote action |

Raw verification log: [review/verify.md](review/verify.md).

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | FAIL | AC-3/4/10/11/12 do not close |
| 2 | Philosophy aligned | FAIL | failed AC mappings violate P1/P3/P5/P7–P12 |
| 3 | Tech debt documented | PASS | no new debt; D1/D2 are current correction work |
| 4 | Style and standards | FAIL | readable typed code, but owned runtime shape is fail-open |
| 5 | RF completeness | PASS | mandatory sections and explicit VD-C1 exist |
| 6 | Evidence completeness | FAIL | required negative cases absent; three VERIFIED rows overclaim |
| 7 | Code quality | FAIL | manifest/directory recognition is not closed |
| 8 | Test coverage | FAIL | 345 pass, but independently failing required edges are missing |
| 9 | Security | FAIL | unknown reserved-target material is trusted as recognized |
| 10 | Breaking/migration behavior | FAIL | exact-prior rollback/rollback is not stable |

Full judgment: [review/judge.md](review/judge.md).

## 4. Verdict

**🔄 REVISE**

The current installed runtime, exact DAG audit, platform executions, operation/context
semantics, parity, F26, documentation, and scope all reproduce. Approval is still
blocked because the lifecycle accepts unknown reserved runtime material and
non-canonical manifest shapes, and because rollback is not idempotent for the allowed
case where the exact prior local value already equals `.tfw/hooks`. These are direct
AC-3/AC-4 failures, not optional hardening.

### Items to fix

1. **D1 — runtime recognition:** reject unexpected runtime-directory entries,
   unexpected manifest/target fields, and non-canonical entrypoint values across
   install/verify/repair, with fail-closed tests and no external/global access.
2. **D2 — lifecycle state machine:** make the exact-prior `.tfw/hooks` case
   unambiguous and stable for repeated lifecycle actions while preserving exact
   rollback and secrecy.
3. **D3 — proof package:** extend the matrix, rerun both declared platforms and every
   regression/build/render/parity/scope/range gate, and correct PR-C3/4/10/12,
   E3/E4/E10, EV verdict, and RF wording. A corrective review must rerun the full
   Phase C result, not only the patch.

The Reviewer-owned local trace commit is still required and will independently
exercise the installed carrier. Its post-commit object/range result is reported to the
Coordinator; it closes the missing Reviewer operation observation but cannot convert
this REVISE verdict into acceptance.

## 5. Tech Debt Collected

No new TECH_DEBT item. RF §6 contains no qualifying observation, and D1–D3 are
acceptance-critical current-work defects returned to Executor.

## 6. Traces Updated

- [x] README Task Board — Phase C status `🔄 REVISE (C)` with REVIEW link
- [ ] HL status — unchanged; approved specification remains authoritative
- [ ] project_config.yaml — unchanged
- [x] Other project files — exact protected scope checked; no implementation write
- [ ] tfw-docs: Deferred — verdict is not APPROVE
- [ ] tfw-knowledge: Deferred — verdict is not APPROVE
- [ ] Remote push: NOT AUTHORIZED — process F26 remains absolute

## 7. Fact Candidates

No new Fact Candidates. The human publication-approval boundary is already recorded
as process F26; the defects above are reproducible implementation observations, not
human-only project knowledge.

---

*REVIEW — TFW-49 / Phase C: Repository-Local Enforcement, Migration, and Cross-Agent Proof | 2026-07-31*
