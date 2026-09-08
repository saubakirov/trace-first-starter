# Phase HL — TFW_20260907-133942_PTTC / A: Proportionate repository verification

> **Date**: 2026-09-08
> **Author**: robert, Coordinator unit `01a08196-9e95-7ef3-8a4f-a5d6b4a424a9`
> **Status**: Planning derivation; exact TS and verification cost await owner approval
> **Parent**: [Master HL](../HL-TFW_20260907-133942_PTTC.md), Phase A
> **Governing master contract**: frozen by saubakirov on 2026-09-08; A2 freeze `5c151d57f66df3ea321fe145170fe3db07c3eb6a`
> **Planning source**: `099d37d21ddfada2ca72c576055f0a26029c7205`
> **Dispatch**: [root f6e1](../journal/20260908-201815__dispatch__f6e1.md)

This is a derivation of the master contract. Vision, DoD, DoF and Principles exist only in master HL §§1, 5, 6 and 7. The phase adds source selection, sequencing and implementation context; it proposes no frozen amendment. Its accepting owner remains `saubakirov`.

## 2. Current State

At the planning source, `docs/scripts/test_integration.py` has 3,156 physical lines, 106 effective test functions before parametrization, and one module-scoped automatic MkDocs fixture. Static AST inspection identifies 15 direct `site/` consumers and 91 other effective tests. The latter use source files, Git objects and temporary trees; this classification remains to be independently checked against direct and helper dependencies during implementation.

Seven earlier same-name definitions are shadowed; two surviving historical names only call already-collected predicates. The knowledge check at lines 2715–2789 compares complete D82/D83/D84 rows with historical rows, although it also carries useful cardinality, phase-lineage and immutable-reference checks. The current CRUE repair already separates historical 3.0.0 package replay from current release metadata and removes the global doctor-clean test. That removal needs no replacement work here.

Two live references in `test_runtime_context.py`, `LEDGER_SPECS` R10/R14, point to source predicates to be moved. All current callers of `resolve_deletion_ledger` use the current source tree. Historical selector constants in the integration tests identify old deliverables and must keep their old paths.

The canonical Knowledge Gate on this intake reports 67 tasks, no problems, no removed IDs, and three pending IDs: `TFW_20260906-190312_CRUE`, `TFW_20260907-020729_SLC`, `TFW_20260907-133942_PTTC`. Hard mode permits continuation at 3/5. Counts are philosophy 47, convention 23, process 51, constraint 16, stakeholder 19, domain 5, environment 6, risk 1, context 1: 169 facts, all nine categories. An initial disposable calculation omitted the legacy `§` numbering prefix; correcting normalization naturally reproduced the stored TFW-31/TFW-41 digests. No knowledge/configuration/state repair followed.

## 3. Phase A Result — derived from master §§3 and 4

| Accepted result | Visible difference for the maintainer | Required protection |
|---|---|---|
| A source/Git test family independent of the website | A knowledge or source check runs without MkDocs or existing `site/` | Output consumers retain one shared build; missed consumers cannot pass on stale output |
| Fewer redundant predicates | Superseded bodies and two duplicate wrappers leave the active source | Current predicates, the narrow retired-board-parser guard and historical Git evidence remain |
| Knowledge checks bound to their actual claim | Harmless explanations and approved successors can be accepted without editing knowledge to satisfy an old snapshot | Missing/duplicate decisions, false lineage, fabricated references and material authority distortion are rejected by the relevant check or independent review |
| A usable verification route in the existing maintainer guide | The maintainer can name the affected risk, command and reusable evidence | Broad-risk changes and changed oracles do not inherit a stale PASS |

### 3.1 Result preview

Illustrative acceptance view, not a report of completed work:

```text
Knowledge explanation clarified
  identity, lineage and relevant sources    preserved
  current source/Git check                  PASS
  MkDocs starts for the knowledge selection 0
  semantic explanation                     independently assessed

Generated page is broken
  stale valid site/ already exists
  selected output check rebuilds           observed
  real rendering defect                    FAIL

Value: routine source work loses an unrelated build;
       a genuine integration failure remains visible.
```

### 3.2 Value flow

```text
Change + governing claim
  -> relevant inputs / oracle / environment
  -> reuse applicable evidence OR run the affected selection
  -> shared build only for output consumers
  -> independent review of result and evidence applicability
  -> reviewed Phase A result for Phase B
```

## 4. Execution context and sequence

The [TS](TS__phase-a__proportionate_repository_verification.md) proposes four VALUE paths and five acceptance criteria. Keep `test_integration.py` as the output module; move proved pure tests/helpers into `test_repository_contracts.py`. This is a dependency split, with no selector service, cache, registry or extra test-runner framework.

The parent chain is human owner `saubakirov` → root Coordinator/LEAD `robert`, unit `01a07050-9d35-7080-a5f6-afd14334e68d` → this Phase A Coordinator, unit `01a08196-9e95-7ef3-8a4f-a5d6b4a424a9`. Native direct messages, host `local`, carry questions and results. Proposal origin for this TS is this phase Coordinator; the initial scope/mandate dispatch originated from the root unit. Shared principal attribution grants no child amendment authority.

The root first checks this plan, lands its separate producer commit in the saved project and presents exact TS scope/cost to the owner. Only a subsequent addressed dispatch based on that approval permits creation of one Executor and one independent Reviewer, each a separate native Codex task with its own worktree. Reuse those holders on returns. No Executor/Reviewer exists for this phase yet. The supplied profile establishes only disclosed G1–G7 mechanics, not G8 reliability.

Phase A precedes B. B receives A's reviewed RF and deviations. Closing-rule implementation, terminal-record recovery and the synthetic receiver belong to B; this phase makes no closure or receiver-wide reliability claim.

## Knowledge citations — application of master §7.2

P0–P4 were independently scanned; relevant P5–P7 items below were read. Paths resolve from this phase directory.

| Priority | Source and exact item | Application |
|---|---|---|
| P0 | [North Star](../../../../.tfw/README.md#ns1), NS1; NS2.2/4/5/7; NS3 | Remove needless coupling and duplicate protection while preserving purpose, authority and inspectability; do not build another control product |
| P1 | [Methodology values](../../../../.tfw/README.md#methodology-values), Candor, Structural Enforcement, Portability; Success Criteria 1–4 | Observe the dependency boundary and preserve readable grounds for acceptance; do not label a modeled behavior native proof |
| P2 | [Philosophy](../../../../knowledge/philosophy.md), F32, F36, F40–F43, F45 | Judge the complete result and protected consequence; avoid a test that freezes harmless prose or a plan that adds artifacts instead of removing the cause |
| P3 | [Architecture Decisions](../../../../KNOWLEDGE.md#architecture-decisions), D52–D53, D59, D61, D63–D64, D71, D76–D77, D81–D85 | Use existing EV/RF and independent review; retain meaningful rendering defects and immutable history; account for tests as this phase's product and sequence crossings |
| P4 | [Conventions](../../../../.tfw/conventions.md#hl-contract), HL Contract rules 3/6/8/17–21; Design Rules; Anti-patterns | Derive from the approved master; specify outcomes rather than implementation code; preserve role boundaries and require a cited material return |
| P5 | [Convention](../../../../knowledge/convention.md), F21/F23 | Cite project purpose separately from method practice; write canonical artifacts in English and explain the result in Russian |
| P6 | [Process](../../../../knowledge/process.md), F39/F46/F48/F51 | Locate live reference consumers before moving tests; coordinate SLC; bound cost prospectively and keep incomplete evidence honest |
| P7 | [Constraint](../../../../knowledge/constraint.md), F16 | Repository tooling is an upstream maintainer concern; Full receivers acquire no pytest/MkDocs/Python/Git-corpus obligation |

## 8. Dependencies

| Dependency | Resolved boundary |
|---|---|
| Research | [main iter1 RES](../research/iter1/RES.md) and [main iter2 RES](../research/iter2/RES.md), especially iter2 D2–D5/D8–D9; both complete. Independent audit remains `0ebf0b107cee9589e709746c836b989628230041:workspace/2026/TFW_20260907-133942_PTTC/research/iter1/RES.md`; it does not overwrite the main iter1 |
| SLC | Root directly relayed SLC's confirmation: no new functional overlap in the four selected VALUE paths; R10/R14 do not overlap its task-container/config extraction. SLC is still at HL without implementation. Keep the landing test output-backed and leave `task_containers`/`iter_task_dirs` unchanged. If PTTC lands first, root supplies its SHA and moved-helper addresses so SLC uses the actual new structure. Supported single `tasks` containers and historical URLs remain supported |
| CRUE | Current release repair already present. Preserve controlled package/doctor checks and historical package commits; no release-policy change |
| Other Knowledge Gate work / possible second PTTC team | Outside this phase. Root owns coordination; no competing implementation follows from this planning task |
| Immutable acceptance | Initial TS scope/cost, frozen changes, Phase B and publication are owner-reserved. A plan commit is no execution approval |

## 9. Phase-local risks

| Risk | Response in the TS |
|---|---|
| Pure classification misses a helper's HTML dependency | Inventory effective functions and reachable helpers; retain unresolved consumers under the build; absent/stale-output observations |
| Moving tests breaks source references or makes the board guard scan itself | Two explicit current ledger targets; preserve historical literals; narrow self-exclusion and retained adverse protection |
| Field checks become another snapshot or a claim to understand all prose | Separate structural checks, immutable historical regressions and explicit semantic judgment; test bounded positive and negative cases |
| Broad move appears artificially cheap or prompts unnecessary phases | Count the whole four-path diff as VALUE; disclose the soft LOC trigger before owner approval |
| Measurement or review repeats costly work | One controlled comparison and one final full suite; shared observations and targeted independent challenge inside the prospective ceiling |

## 10. Research disposition

Main iter2 resolves the design questions for planning. No new research iteration is warranted. Empirical obligations remain in TS AC-1 through AC-5: boundary, local cost, knowledge variants, applicability/permission behavior and integration protection. Earlier reports supply historical observations, not measured Phase A savings.

## 11. Strategic Insights

No new human-sourced strategic insights. The root dispatch operationalizes the owner's already-recorded Saint-Exupery and exact scope/cost approval requirements; it creates no new owner ruling.

## 12. Amendment route

No amendments proposed. Any change to a frozen master claim returns through master §12 and its resolved ruler; this phase carries no substitute amendment authority.
