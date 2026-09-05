# ONB — TFW_20260904-113200_VBSA / Phase A: Value-bearing budget contract and adoption

> **Date**: 2026-09-04
> **Author**: Codex (Executor)
> **Status**: 🟠 ONB — Bound accepted; no blockers
> **Parent HL**: [HL-TFW_20260904-113200_VBSA](../HL-TFW_20260904-113200_VBSA.md)
> **TS**: [TS Phase A](TS__phase-a__value_bearing_budget_contract_and_adoption.md)

---

## 1. Understanding

Phase A replaces ambiguous whole-diff scope limits with one prospective, semantic accounting contract over the 29 exact `VALUE` paths declared in the approved TS. The implementation must make conventions, planning, execution, evidence, review, configuration, initialization, update guidance, release guidance, templates, and tracked workflow copies agree while the two declared test files remain `ASSURANCE` and lifecycle artifacts remain `TRACE`. The fixed Baseline is `f5a96af07dcdc4230ecf31100bd155a3dca09604`; the immutable owner-approved denominator is 29 logical touched VALUE files and 1,100 touched text LOC (900 additions plus 200 deletions). The first tested implementation commit becomes Candidate before EV, RF, or the RF transition, and no release number, historical normalization, new accounting carrier, or protected HC-1 path is permitted.

## 2. Entry Points

- Semantic authority and term routing: `.tfw/conventions.md` §6 and `.tfw/glossary.md` `Scope Budget`.
- Project-owned values and starter defaults: `.tfw/project_config.yaml` and `.tfw/templates/project_config.yaml`.
- Active role consumers: `.tfw/workflows/plan.md`, `handoff.md`, `review.md`, `config.md`, `update.md`, and `init.md`.
- Writer and reader forms: `.tfw/templates/TS.md`, `RF.md`, `REVIEW.md`, and `.tfw/templates/evidence/EV.md`.
- Local North Star, forward communication, and release boundary: `.tfw/README.md`, `.tfw/CHANGELOG.md`, and `RELEASE.md`.
- Structural assurance: `docs/scripts/test_runtime_context.py` and `docs/scripts/test_integration.py`.
- Shipped adapters: the six corresponding `.agent/workflows/tfw-*.md` and six `.claude/commands/tfw-*.md` copies. All twelve are currently byte-identical to their canonical workflows; `.tfw/adapters/manifest.yaml` is byte-identical to Baseline and remains read-only.

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions. The approved TS, dispatch record, fixed Git references, exact selector, migration mapping, release boundary, HC-1 selector, trigger disposition, and authority ceiling form an executable bound.

## 4. Recommendations (suggestions, not blocking)

1. Keep the accounting semantics canonical in `conventions.md`; other carriers should contain only the role-specific facts needed at their checkpoint, preserving D75 selective reads and avoiding a second truth.
2. Add source-derived behavioral fixtures and output-changing mutants for classification, accounting, authority, and migration rather than assertion-only anchor checks.
3. Treat the migration as version-agnostic behavior now: preserve surviving receiver values, retire redundant keys, and require `/tfw-release` to choose the version and create any required major migration guide.

## 5. Risks Found (edge cases, potential issues not in TS)

1. The repository has no current `[Unreleased]` changelog section, so Phase A must add one without rewriting the released 2.1.0 record.
2. The exact NUL-safe Git output differs for ordinary paths, renames, and binary paths. Tests must exercise the produced membership and metric result, including one logical rename and per-file LOC `N/A`.
3. A receiving project may carry customized non-default old values. Mapping must preserve `max_files_per_phase` and `max_loc` numerically while ignoring retired `max_new_files` and `max_modified_files`, never inferring historical approval semantics from the new installed state.
4. Full-copy adapters are VALUE. Any canonical workflow edit that is not copied byte-for-byte to both tracked destinations would leave contradictory shipped behavior.
5. The RDP journal summary of 123 code points against the 120-code-point ceiling is an immutable baseline defect. Full-suite or repository checks may report it; it must be disclosed and never repaired, normalized, or used to raise the ceiling.
6. This repository's quoted Saint-Exupéry Principle is local North Star content. Init and update behavior must preserve a receiver's North Star byte-for-byte and must not inject the quote.
7. Candidate timing is part of the accounting result. EV, RF, final status, and final journal must be written only after the tested implementation commit is fixed.

## 6. Inconsistencies with Code (spec vs reality)

No governing contradiction found. The live four-key configuration, hard-limit wording, non-accounting RF/EV/REVIEW forms, and absent `[Unreleased]` section are the planned Baseline defects named by the TS, not divergent implementation facts. The approved TS lineage resolves at `36e50e4a362d474550f26e58defe56132b5417be`, its Baseline is an ancestor, and its 29/1,100 denominator agrees with the dispatch journal.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | Project North Star, NS1 — Purpose | ✅ | Applied | Budget membership follows purposeful accepted delivery; mandatory trace remains visible without becoming delivered value. |
| 2 | Project North Star, NS2.1/NS2.3/NS2.6 | ✅ | Applied | Goal and Value select VALUE; selected trace and risk-proportional assurance remain mandatory outside delivery arithmetic. |
| 3 | Project North Star, NS3 — Non-goals | ✅ | Applied | No artifact-count success measure, shadow process budget, or documentation-factory mechanism is introduced. |
| 4 | Methodology values — Structural Enforcement | ✅ | Applied | The same contract is carried through TS, Candidate, RF, one EV row, REVIEW, and source-derived tests. |
| 5 | Success Criteria #4 — ready for acceptance | ✅ | Applied | VALUE is the complete, usable, inspectable accepted result rather than every operational file needed to produce it. |
| 6 | `knowledge/philosophy.md` F13/F42/F43/F45 | ✅ | Applied | Wording and examples stay domain-agnostic; gates require material consequences; carrier design favors coherent architecture and justified subtraction. |
| 7 | `KNOWLEDGE.md` D16/D24/D49/D52/D72 | ✅ | Applied | Project config remains the value source, enforcement-critical defaults stay inline, requirements and evidence keep their gates, and review routing remains conventions-owned. |
| 8 | `conventions.md` — Scope Budgets (per Phase) | ✅ | Applied | The four Baseline limits are replaced in the canonical section by the approved two VALUE triggers and one authority multiplier. |
| 9 | `conventions.md` — Design Rules | ✅ | Applied | Role checkpoints keep necessary defaults inline while templates own forms and no positional adapter-unsafe commands are added. |
| 10 | `knowledge/convention.md` F22 | ✅ | Applied | The historical Task Board exception is generalized by semantic class without rewriting its record; shipped adapter copies remain VALUE. |
| 11 | `knowledge/process.md` F32/F37/F38/F40 | ✅ | Applied | Counts will be re-derived immediately from fixed refs; pre-act checks enforce immutable boundaries; the known 123/120 journal defect is reported, not repaired. |
| 12 | `knowledge/constraint.md` F7 | ✅ | Applied | Classification examples and evidence cover non-code delivery and do not assume software-only value. |
| 13 | Git `git-diff` documentation | ✅ | Applied | `--numstat` additions/deletions, binary `-` fields, rename-aware name status, and `-z` path termination ground the reproduction method. |
| 14 | NASA SWE-093 and NASA software-size guidance | ✅ | Applied | Measurement needs declared analysis context; SLOC is useful but language- and purpose-sensitive, so text LOC is not treated as universal for binaries or non-code forms. |
| 15 | Scrum Guide and Kanban Guide | ✅ | Applied | Preserve the accepted goal while scope learns; expose policies, flow, and trade-offs rather than equating a threshold with quality. |
| 16 | DORA small batches and Google Small CLs | ✅ | Applied | Decomposition stays a strong feedback prompt, but coherent, independently useful delivery and reviewer judgment outrank a universal hard line count. |
| 17 | PeerJ controlled experiment and Empirical Software Engineering review-evolution study | ✅ | Applied | Change decomposition affects review behavior and review changes evolve with size/context; neither source supplies TFW's universal numeric cutoff. |
| 18 | Library of Congress sustainability factors | ✅ | Applied | Significant characteristics differ by genre and form, supporting semantic VALUE membership plus metric applicability instead of cross-format LOC equivalence. |
| 19 | NASA Systems Engineering Handbook | ✅ | Applied | Proposed change, justification, authorized disposition, implementation, and verification remain ordered acts; prospective authority cannot be supplied after work. |
| 20 | NIST SP 800-53 CM-3 | ✅ | Applied | Configuration-controlled changes are reviewed and approved before implementation, recorded, tested, and monitored; TFW imports the ordering, not NIST machinery. |
| 21 | Semantic Versioning 2.0.0 | ✅ | Applied | Released contents remain immutable and incompatible public-contract changes require version classification, while the actual version choice stays with `/tfw-release`. |

Additional applicable items found during the prescribed read: `KNOWLEDGE.md` D73–D75. They require workflow-owned selective reads, one existing adapter manifest, source-derived mutants, exact copy parity, strict new writes, and tolerant historical reads; all are applied as compatibility constraints.

## 8. Round 1 Return — Accepted Bound

### 8.1 Understanding and authority

The same Executor accepts the rung-1-only return ruled in the live REVIEW at
5ab04d0e666ad38960229013a7ac649e693f3ca8. The unchanged approved TS at
36e50e4a362d474550f26e58defe56132b5417be remains the governing order. The round is limited to:

1. make the plan read graph load the uniquely addressed canonical classification, accounting, and
   authority sections, with missing/meaning-reversing route mutants rejected and D75 ceilings preserved;
2. make controlled clean-receiver preservation executable or behavior-derived from init/update, with a
   preserve→overwrite mutant rejected and both receiver North-Star byte surfaces unchanged;
3. keep EV Result status vocabulary exactly VERIFIED / DEFERRED / BLOCKED / N/A, while retaining
   phase-attribution INVALID only as accounting detail.

### 8.2 Entry points and selector

Implementation may modify only already-approved paths among canonical plan/init/update workflows and
their exact .agent/.claude copies, .tfw/templates/evidence/EV.md, and the two ASSURANCE test files.
The outer approved selector remains 29 VALUE plus 2 ASSURANCE paths. No new carrier, manifest path,
migration, script, ledger, REVIEW, TS, HL, RES, unrelated task, or historical file is authorized.

### 8.3 Questions

No blocking questions. REVIEW §8 supplies a closed implementation bound, same-Executor assignment,
observable completion, debt ruling, unchanged 29/1,100 denominator, and new-Candidate requirement.

### 8.4 Risks and checks

1. Loading all three canonical plan sections can exceed D75 unless the graph deduplicates contained
   addressed ranges and the carrier remains concise; the immutable ceiling test is a mandatory gate.
2. A receiver test is invalid if expected bytes are merely asserted without executing semantics derived
   from a workflow carrier; the mutant must change produced behavior before rejection.
3. INVALID must remain an attribution outcome without becoming a fifth EV Result status.
4. The historical RDP 123/120 defect is owed but forbidden to pay in this phase; reproduce only.
5. Required VALUE changes supersede the prior Candidate only after all round tests pass and a new
   immutable Candidate is committed. EV/RF/status/event updates follow that commit.

### 8.5 Prior work and citations

All prior accepted implementation, evidence, and original ONB answers remain in force and are not redone.
D73/D75 govern canonical selective routing and mutation-sensitive structural assurance; D74 governs
executable adapter/receiver behavior and byte preservation; D52 keeps the four Evidence statuses. The
round introduces no new knowledge citation or strategic fact.

## 9. Round 2 Return — Accepted Bound

### 9.1 Understanding and authority

The same Executor accepts the pass-2 rung-1 return ruled in live REVIEW §16 at
baa0b7c8c6938d9131bcf5bb78efd6edfc3653bb. The approved TS at
36e50e4a362d474550f26e58defe56132b5417be and immutable 29/1,100 denominator remain unchanged.
Only R2-D1 is active: restore every named approved classification, ambiguity, selector, and complete
Saint-Exupéry boundary rule inside the three already-loaded canonical plan ranges.

### 9.2 Entry points and selector

The permitted implementation surface is the existing approved conventions/plan carriers, their two
tracked plan copies when canonical plan changes, and the two approved ASSURANCE files. No new path,
authority, carrier, manifest entry, ledger, script, migration, or HC-1 change is permitted. Pass-1
receiver and EV-status carriers remain unchanged and must stay green.

### 9.3 Questions

No blocking questions. REVIEW §16 enumerates every required example/rule, the source-derived adverse
mutants, D75 ceiling, adapter parity, Candidate replacement, accounting, and stop condition.

### 9.4 Risks and checks

1. The current planner graph is 24,729 against a 24,730 ceiling. Restored semantics must be paid for by
   removing only duplicated prose or excess selected config comments, never another rule.
2. A hard-coded expected phrase is insufficient: the projection must derive examples, ambiguity policy,
   selector properties, and Saint boundary from the live canonical ranges.
3. The proven freehand-permission mutant and removal of each required example/rule must change produced
   output before independent rejection.
4. RDP 123/120 remains terminally ruled and forbidden to repair.
5. VALUE changes require a new tested Candidate before round EV/RF/status/event writes.

### 9.5 Prior work and citations

Pass-1 routing, receiver behavior, EV vocabulary, accounting, and evidence remain accepted and are not
redone except by regression. D73/D75 require the live-source projection and adverse guards; the frozen
HL/TS contract supplies the domain examples, selector ambiguity rule, and complete non-damage boundary.
No new fact candidate or strategic insight arose.

---

*ONB — TFW_20260904-113200_VBSA / Phase A: Value-bearing budget contract and adoption | 2026-09-04*
