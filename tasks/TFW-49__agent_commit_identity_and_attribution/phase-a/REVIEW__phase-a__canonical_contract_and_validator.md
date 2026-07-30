# REVIEW — TFW-49 / Phase A: Canonical Commit Identity Contract and Validator

> **Date**: 2026-07-30
> **Author**: Reviewer (Codex)
> **Verdict**: 🔄 REVISE
> **Review Mode**: code
> **RF**: [RF Phase A](RF__phase-a__canonical_contract_and_validator.md)
> **TS**: [TS Phase A](TS__phase-a__canonical_contract_and_validator.md)
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> This file is a synthesis of stage findings. Reference stage files for raw evidence.

---

## 1. Map

Phase A introduces a prospective six-consumer C1-R contract: universal schema,
project activation state, standard-library formatter/parser/message validator/range
auditor, tests, and canonical conventions/glossary references. It intentionally stops
before Phase B commit routing and Phase C hook/config installation, and it represents
identity only as declared structural provenance.

The implementation is cohesive and most behavior reproduces, but review found two
acceptance-critical contract gaps and one false RF measurement after independently
checking all ten AC, ten Principles, ten Evidence rows, the entire implementation
surface, generated pages, and protected state.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|------------------|--------|----------|
| 1 | Exact implementation scope and protected state | ✅ | Six approved framework paths plus EV/RF/README only; no hook/config/workflow/adapter/knowledge spill |
| 2 | Contract and docs suites | ✅ | `46 passed`; isolated final docs pair `68 passed` |
| 3 | Schema/state ownership and mutation | ❌ | Production data is correct, but missing `truth_boundary` and invalid `identity_template` pass schema/state validation |
| 4 | C1-R parser, normalization, origins, `task:none`, diagnostics | ✅ | Independent source/runtime matrix reproduced claimed behavior |
| 5 | Reserved/generated same-context rule | ❌ | Stale supplied context fails; absent expected context returns valid for public `validate-subject` |
| 6 | Exact anchored Git DAG behavior | ✅ | Linear/merge/root/unborn/shallow/missing/non-ancestor coverage and current range reproduce |
| 7 | Authority, non-authentication, Phase B/C, C2-R boundaries | ✅ | Six-consumer semantic scan found no overclaim or later-phase implementation |
| 8 | Rendered documentation | ✅ | Exact anchors, three owner links per section, visible content/table, and `1265/1265` no-overflow layout reproduced |
| 9 | TD-125 warning attribution | ❌ | Identical pinned builds yield `283/283`, `131/131`, and zero set delta, not RF V3's reported measurements |
| 10 | Evidence and citations | ❌ partial | 22/22 citations resolve; all Evidence rows exist; PR-1/PR-4 and RF V3 overstate reality |

Raw verification log: [review/verify.md](review/verify.md).

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ❌ | AC-1, AC-4, AC-6, and AC-10 fail; Judge AC table |
| 2 | Philosophy aligned | ❌ | P1/P3/P5/P6 are not fully enforced |
| 3 | Tech debt documented | ✅ | No new debt; current defects must be corrected rather than deferred |
| 4 | Style & standards | ✅ | Cohesive standard-library design, precise names, canonical docs, and protected scope |
| 5 | Observations collected | ✅ | No separate out-of-scope observation warrants TECH_DEBT |
| 6 | RF completeness (§7–9 present) | ✅ | Sections present; no omitted Human-Only Fact Candidate |
| 7 | Evidence completeness | ❌ | PR-1/PR-4 false in material part; RF V3 not reproducible |
| 8 | Code quality | ❌ | Schema loader leaves downstream-consumed semantic fields unchecked |
| 9 | Test coverage | ❌ | Missing negative cases allow both contract gaps to remain green |
| 10 | Security | ✅ | No secret/path/body/hook/environment disclosure or protected-state mutation |
| 11 | Breaking changes | ✅ | Prospective C1-R only; C2-R rejected; no prior operational owner removed |

Full judgment: [review/judge.md](review/judge.md).

## 4. Verdict

**🔄 REVISE**

The central C1-R parser/auditor is largely sound, the exact Git DAG semantics pass,
scope is disciplined, documentation renders correctly, and no authentication or
later-phase architecture is claimed. Approval is nevertheless blocked because the
binding semantic-owner and same-context gates do not fully enforce their TS/RF
claims, and the RF contains a non-reproducible quantitative verification statement.

### Items to fix

1. **Close schema semantic-shape validation.** Validate every required downstream
   owner field at contract load—at minimum `truth_boundary` shape/content and
   `grammar.identity_template` placeholders/compatibility—and add negative fixtures.
   Missing or semantically unusable owner data must fail immediately with stable
   field-specific `E_SCHEMA_SHAPE`, not later `E_SUBJECT_FORMAT`/generic operation
   behavior.
2. **Enforce the supplied-context rule for public reserved-form validation.** A
   `fixup!`, `squash!`, `amend!`, or supported generated revert passed to contextual
   validation without all four expected fields must fail with a stable actionable
   context-required diagnostic. Preserve an explicit structural-only internal path
   for the independent range audit; stale supplied context must continue to fail.
3. **Correct and reproduce RF/EV attestations.** Update PR-1/PR-4 and RF AC/V rows to
   the corrected behavior after implementation. Replace RF V3's warning counts and
   set attribution with a reproducible identical-input baseline/final comparison.
   The current independent result is baseline/final `283/283` warning lines,
   `131/131` normalized distinct warnings, and `0 added / 0 removed`.

After correction, rerun the full 46-test contract matrix plus new negative fixtures,
68 docs tests, exact baseline/final MkDocs comparison, rendered anchors, exact scope,
and pre/post-C1-R range audit before requesting another independent review.

## 5. Tech Debt Collected

No new TECH_DEBT item. D1–D3 are current Phase A closure defects and must not be
converted into deferred debt. TD-125/TD-126 remain unchanged.

## 6. Traces Updated

- [x] README Task Board — `🔄 REVISE (A)` with Phase A REVIEW link
- [ ] HL status — unchanged; phase is not approved
- [ ] project_config.yaml — unchanged; no sequence allocation
- [x] Other project files — protected scope checked; no stale implementation write made
- [ ] tfw-docs: Deferred — verdict is REVISE
- [ ] tfw-knowledge: Deferred — verdict is REVISE

## 7. Fact Candidates

No Fact Candidates. The review found reproducible technical behavior and current
closure defects, not new Human-Only project knowledge. The Coordinator's LOC
disposition is already retained as RF S1 and is not duplicated here.

---

*REVIEW — TFW-49 / Phase A: Canonical Commit Identity Contract and Validator | 2026-07-30*
