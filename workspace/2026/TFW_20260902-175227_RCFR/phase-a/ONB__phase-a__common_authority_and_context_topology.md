# ONB — TFW_20260902-175227_RCFR / Phase A: Common Authority and Context Topology

> **Date**: 2026-09-03
> **Author**: Codex (Executor, acting on behalf of `saubakirov`)
> **Status**: ✅ ONB — All Coordinator answers recorded; revision 2 execution authorized
> **Parent HL**: [HL-TFW_20260902-175227_RCFR](../HL-TFW_20260902-175227_RCFR.md)
> **Phase HL**: [HL Phase A](HL__phase-a__common_authority_and_context_topology.md)
> **TS**: [TS Phase A revision 2](TS__phase-a__common_authority_and_context_topology__rev2.md)
> **Approval baseline**: `2728dae78d55f6cb7daa39c82874ad5b43621f8a`

---

## 1. Understanding

Phase A must replace duplicated common preload and shared decision prose with a selective, heading-addressed authority topology; replace the sequence-based Knowledge Gate with a full-task-identity digest reconciliation; and make all four adapters expose the same exact 11-command/role contract from one tooling manifest. The change is test-first: the independent semantic fixture and its family-specific mutants, the Knowledge Gate transition matrix, and the empty-receiver adapter contract must fail against the old behavior before governed prose or adapter deletion occurs. The execution is limited to the approved Phase A TS: no Phase B role-workflow compression, no Phase C closure or secondary-workflow work, and no edits to the frozen master HL, Phase HL, or approved TS. The current executor worktree is clean and detached at the exact approval baseline; the candidate branch remains checked out in the separate Coordinator worktree. This ONB is the only executor change before the Coordinator clears the gate.

The semantic boundary includes the already committed RDP corrections in `.tfw/glossary.md`: named authority links for Evidence Collection, Execution Loop, and Pre-RF Gate; the deliberate exclusion of `plan.md` from the Session Naming Step 0 rule; and the paid-disposition requirement that a ruling name the phase and order payment in the same act with a cited condition. The planned query-router form must retain those meanings verbatim or equivalently; any discovered semantic conflict is a hard stop.

## 2. Entry Points

- Shared authority and router: `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, and `.tfw/workflows/plan.md`.
- Knowledge Gate: `.tfw/workflows/knowledge.md`, `.tfw/knowledge_state.yaml`, `.tfw/templates/knowledge_state.yaml`, `.tfw/scripts/gen_index.py`, and `.tfw/scripts/test_gen_index.py`.
- Semantic oracle: new `docs/scripts/test_runtime_context.py`, plus the Phase A fixture/mutant evidence generated from it.
- Adapter contract: `.tfw/adapters/manifest.yaml`, `.tfw/workflows/{init,update,config}.md`, adapter READMEs/templates, installed `CLAUDE.md`, and installed `.agent/rules/{agents,tfw}.md` carriers named by the TS.
- Repository verification: `docs/scripts/test_integration.py`, `python .tfw/scripts/gen_index.py --check`, configured lint/test commands, exact adapter-set checks, and the independent semantic oracle.
- Evidence and result: at most five Phase A evidence files, the mandatory EV record, and `RF__phase-a__common_authority_and_context_topology.md`, only after implementation and verification.

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | The approval baseline contains the RDP-added `last_consolidation_task` field and compatibility comment, while TS AC3 explicitly removes `last_consolidation_seq` but does not state the disposition of `last_consolidation_task`. May the successful full reconciliation remove `last_consolidation_task` as a superseded cursor while preserving its provenance in Git/evidence and preserving the current date/statistics, or must it remain as explicitly non-authoritative audit metadata? Removing it keeps one semantic state and avoids a readerless cursor; retaining it most literally preserves the post-research RDP change. Coordinator ruling is required before the state migration. | **Coordinator:** Remove both `last_consolidation_seq` and `last_consolidation_task` only after successful full reconciliation. The latter is a compatibility/audit bridge, not an operational cursor; it becomes readerless and cannot honestly describe batch reconciliation once `processed_task_digests` is authoritative. Preserve its provenance in Git and RF/EV migration evidence, retain the current date and statistics, and include RDP under its own digest entry. If reconciliation is incomplete, a trace is removed/ambiguous/malformed, or post-marker recomputation is incomplete, leave the old live state unchanged and stop. |
| 2 | Confirm that the TS maximum of 31 affected files is the explicitly enumerated implementation/test/evidence budget (24 modified + 2 new + up to 5 evidence), while mandatory TFW lifecycle traces (`ONB`, `RF`, phase `status.md`, and journal events) are tracked separately. If those mandatory traces count toward 31, the approved TS is arithmetically infeasible without a Coordinator-authored TS revision because the enumerated set already consumes all 31 slots. | **Coordinator:** Confirmed. The 31-file limit applies to the enumerated implementation/test/evidence set: 24 modified, 2 new, and up to 5 evidence files. Mandatory lifecycle traces are listed and counted separately. No additional implementation surface or sixth evidence file is authorized without a scope stop. |
| 3 | Execution changed the five TS-listed canonical workflows `plan.md`, `knowledge.md`, `init.md`, `update.md`, and `config.md`. This necessarily makes ten tracked installed copies stale: the corresponding five `.claude/commands/tfw-*.md` files and five legacy `.agent/workflows/tfw-*.md` files. Synchronizing them satisfies the existing installed-copy drift gate and AC4 but raises the implementation set from 24 to 34 modified files (41 total with 2 new + 5 evidence); omitting them leaves the current valid Claude commands and tracked Antigravity copies running different instructions and fails `test_installed_adapter_copies_match_their_sources`. The confirmed Q2 ruling excludes only lifecycle traces. Please issue the governing scope/budget ruling or a TS revision before these ten paths are touched. | **Coordinator / owner:** Approved in governing `TS__phase-a__common_authority_and_context_topology__rev2.md`. Synchronize exactly the ten named derived copies. The revised budget is 34 modified + 2 new + up to 5 evidence = 41 total, with a 4,600 changed-LOC estimate. Acceptance criteria, frozen HL claims, Phase B/C boundaries, and all prior completed work remain unchanged; any other path or overrun is a new scope stop. |

## 4. Recommendations (suggestions, not blocking)

1. Treat `2728dae78d55f6cb7daa39c82874ad5b43621f8a` as both the implementation and measurement baseline. Research measurements remain historical observations or projections; every Phase A reduction claim should be remeasured from this commit and label observed versus projected counts explicitly.
2. Build the semantic oracle, mutants, digest fixtures, and adapter exact-set fixtures before changing governed prose. This supplies the deletion gate required by G4 and prevents a shorter document from being mistaken for a correct contract.
3. Make `.tfw/adapters/manifest.yaml` tooling input only. Generated/installed vendor files remain the runtime discovery surfaces; no adapter should need to read the manifest at command invocation.
4. Reconcile every resolvable current and legacy task before the first digest-state write. Write source markers and approved knowledge first, recompute post-marker digests, then write `.tfw/knowledge_state.yaml` last.
5. Keep executor commits local and incremental by verification slice, using the required subject prefix. Report every commit SHA to the Coordinator; do not move or update the Coordinator's candidate branch from this worktree.

## 5. Risks Found (edge cases, potential issues not in TS)

1. The research snapshot predates the final RDP rounds and knowledge consolidation. The approval baseline changes `.tfw/glossary.md`, `.tfw/knowledge_state.yaml`, and the read-only `KNOWLEDGE.md` input relative to that snapshot; an implementation derived mechanically from research text would overwrite current semantics or report stale baselines.
2. The live knowledge state now records `TFW_20260902-112841_RDP`, 153 total facts, 67 verified, 86 unverified, 310 rejected, 533 processed candidates, and 183 scanned sources. Full reconciliation must start from this state and must not silently restore the older research-era values.
3. G4 deletion is order-sensitive. A prose deletion before an independently asserted semantic record and family-specific mutant failure would make the compact contract unauditable even if the final tests happen to pass.
4. Adapter byte equality is insufficient: the known failures are discovery path, missing command, wrong role, and incomplete source mapping. The gate must assert the literal 11-command set, roles, canonical sources, vendor paths, and idempotent copy/check behavior.
5. The executor is on a detached HEAD by design. A commit is isolated from the candidate branch until the Coordinator deliberately integrates its SHA; each SHA must therefore be recorded at the handoff boundary.
6. The 31-file implementation/test/evidence allowance is fully allocated. Any additional implementation path, generated persistent carrier, or sixth evidence file requires a scope ruling rather than a convenient edit.

## 6. Inconsistencies with Code (spec vs reality)

1. The approved TS header and the owner's dispatch authorize Phase A, while the phase-local `status.md` still says `TS_DRAFT` and “awaiting owner approval.” Per `handoff.md`, the Executor will not change lifecycle state or append the handoff event until this ONB is answered and approved; the transition to `ONB` belongs immediately after that gate.
2. Research iter2 measured an earlier repository state. At the approval baseline, a direct UTF-8 `\S+` observation gives 5,199 words for `.tfw/glossary.md` and 14,052 for `KNOWLEDGE.md`, rather than the research snapshot's 5,174 and 13,989. The implementation must establish one reproducible counter and report baseline, candidate, and projection under matching labels.
3. The current Knowledge Gate still derives pending work from `current_seq - last_consolidation_seq`; current clock-derived task IDs do not allocate a sequence. The RDP compatibility field `last_consolidation_task` narrows the human interpretation but does not implement the TS digest algorithm.
4. The repository's installed Antigravity copies remain under obsolete singular `.agent/*`, while the researched vendor discovery contract is plural `.agents/rules` and `.agents/workflows`. Phase A must test a clean receiver at the vendor path while preserving unrelated content in the currently installed singular carriers explicitly listed by the TS.
5. Current adapter documentation and templates do not expose one uniform contract: Codex has 11/11, Claude omits `/tfw-research` and mislabels its role in metadata, Cursor has no command surface, and Antigravity uses the obsolete path and an incomplete list. Equality checks over existing files cannot detect all four failure shapes.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | K1 — NS1 | ✅ | Applied | Reduction is subordinate to purposeful continuation, inspectability, and authority; semantic records and gates decide whether deletion is acceptable. |
| 2 | K2 — NS3 | ✅ | Applied | Full-library preload and duplicated adapter instructions are treated as removable bureaucracy only after their necessary decision edges are identified. |
| 3 | K3 — Structural Enforcement; Naming Creates Behavior; Portability | ✅ | Applied | Phase A uses named headings, executable gates, and empty-receiver adapter fixtures rather than prose assurances. |
| 4 | K4 — philosophy F22, F40, F43, F45 | ✅ | Applied | The planned design moves format to templates, introduces exact terms for repeated decisions, fixes common authority centrally, and prefers subtraction. |
| 5 | K5 — D23, D25, D61 | ✅ | Applied | The design follows prior template/progressive-disclosure reductions and retains semantic acceptance axes instead of optimizing word count alone. |
| 6 | K6 — D63, D68, D72 | ✅ | Applied | Frozen-contract authority, task-local state, and the review citation/disposition loop are explicit protected semantics in fixtures and deletion review. |
| 7 | K7 — conventions §11 and §14 | ✅ | Applied | References are placed in the step that consumes them; role locks and structural gates constrain both router wording and tests. |
| 8 | K8 — convention F4, F8, F14 | ✅ | Applied | The router owns an algorithmic read edge, each mapping has one owner, and adapter templates stop duplicating full shared prerequisites. |
| 9 | K9 — process F3, F4, F22, F30 | ✅ | Applied | Named, numbered algorithms and executable checks replace tautological guidance and unenforced duplicate prose. |
| 10 | K10 — PV priorities 7 | ✅ | N/A confirmed | The remaining topic files add no Phase A-specific constraint beyond the cited project values and current owner direction. |
| 11 | New — D54 | ✅ | Applied | The existing decision for all 11 TFW commands supplies the exact public command-set baseline that every adapter must expose. |
| 12 | New — D69 | ✅ | Applied | Full identifier parsing and refusal on malformed or ambiguous identity constrain digest enumeration and collision behavior. |
| 13 | New — glossary: Evidence Collection, Execution Loop, Pre-RF Gate, Session Naming, Disposition | ✅ | Applied | These RDP-corrected entries form explicit preservation assertions for authority links, the plan-session exception, and same-act paid disposition. |

---

*ONB — TFW_20260902-175227_RCFR / Phase A: Common Authority and Context Topology | 2026-09-03*

---

## 8. Revision 3 Return — Review Round 1

### 8.1 Understanding and order

The governing order is `TS__phase-a__common_authority_and_context_topology__rev3.md`, approved by `saubakirov` on 2026-09-03 and returned by REVIEW round 1. This round repairs only R1–R3: active-root preload and real graph measurement; source-derived semantic/adversarial fixtures and resolving R03–R14 targets; and one plural Antigravity authority across conventions, glossary, manifest, and a clean receiver. The accepted digest algorithm, K0–K9, 61-task state, exact four-by-eleven adapter contract, and ten derived workflow copies are regression inputs, not work to redo.

### 8.2 Questions (blocking)

No new blocking questions. Revision 3 names the exact files, observable results, evidence order, cumulative budget, and hard-stop conditions. The Coordinator's dispatch explicitly authorizes the same Executor task to continue through RF.

### 8.3 Execution constraints

1. Add source-sensitive failing tests before changing any R1–R3 implementation input and preserve both red and green results in the existing raw evidence files.
2. Modify only `AGENTS.md`, `.agent/rules/agents.md`, `docs/scripts/test_runtime_context.py`, `.tfw/conventions.md`, `.tfw/glossary.md`, `.tfw/adapters/manifest.yaml`, and `docs/scripts/test_integration.py`, plus cumulative ONB/RF/EV/evidence/state traces.
3. Treat a nonexistent baseline/candidate source root, a real omitted graph edge, missing/duplicate addressed heading, unresolved deletion-ledger target, or singular Antigravity surface as a test failure rather than a report row.
4. Keep the implementation/test/evidence surface at the same 41 files and cumulative changed LOC at or below 4,600; stop before 5,000, a 42nd file, or a sixth evidence artifact.
5. Leave `.tfw/knowledge_state.yaml` untouched until the final RF/EV selected sections exist; then reconcile all tasks, require no problems/removals, write state once, and replay to zero pending.

### 8.4 Knowledge citations and prior decisions

All 13 knowledge applications recorded in §7 remain applicable and are not reopened. In particular, K1/K2/K4/K8/K9 require the audit and semantic oracle to derive from active sources rather than assertions, while K3/K6/K7 preserve structural gates, history lookup, and role boundaries. ONB Q1–Q3 remain answered. REVIEW §5's RDP observation is `not material — owed and forbidden to pay` and will not be modified.

### 8.5 New risks and inconsistencies

1. A baseline read graph cannot be inferred from the candidate parser because the baseline syntax differs; the fixture must load and execute each source tree under its own root, then compare normalized behavioral output.
2. A source-level mutant must change an authority-bearing source and be observed through the same resolver/executor; mutating the already-produced record would repeat REVIEW D2.
3. Legacy singular `.agent/workflows/*` files remain tracked compatibility artifacts. The repair must stop advertising them as Antigravity runtime discovery without editing the accepted derived copies.

No inconsistency prevents execution. The active root preload, fixed oracle, and singular Antigravity route are the three expected failing starting conditions ordered by revision 3.

---

*ONB revision 3 return — TFW_20260902-175227_RCFR / Phase A | 2026-09-03*

## 9. Revision 3 completion note

R1–R3 were executed without reopening accepted Phase A work. The budget stop at 4,672
changed LOC was obeyed before RF: deletion-led compaction reduced the pre-trace tree to 4,297,
then the complete configured gate passed. Implementation commit: `037be0d`. No blocking
question, scope addition, sixth evidence artifact, or unrelated RDP repair was introduced.

## 10. Revision 4 Return — Review Round 2

### 10.1 Understanding and order

The governing order is `TS__phase-a__common_authority_and_context_topology__rev4.md`,
approved by `saubakirov` on 2026-09-03 and returned by REVIEW revision 2. This round repairs
only R4 in `docs/scripts/test_runtime_context.py`: the expected oracle becomes comparison-only,
while baseline and candidate executions independently derive all six semantic fields from their
own `SourceTree`. The accepted graph, digest, ledger, adapter, source-family mutant, and scope
gates remain regression inputs.

### 10.2 Questions (blocking)

No new blocking questions. Revision 4 fixes the executable path, append-only evidence targets,
ceiling, red-first order, and state-last close. The Coordinator's dispatch explicitly authorizes
the same Executor task to continue through RF.

### 10.3 Execution constraints

1. First add failing guards for oracle separation, rejection of a minimal anchor-only source,
   and a semantic candidate substitution that preserves resolution while changing derived output.
2. Keep expected values outside execution. Every baseline and candidate field must carry a
   trace to a clause read from that execution's own source tree.
3. Modify no implementation path except `docs/scripts/test_runtime_context.py`; append only the
   existing semantic evidence and cumulative ONB/RF/EV, then reconcile state and lifecycle last.
4. Keep the implementation/test/evidence surface at 41 paths and cumulative changed LOC at or
   below 4,600; stop instead of adding a path or broadening the round.

### 10.4 Knowledge citations and prior decisions

All 13 applications in §7 remain in force. In particular, K1/K3/K4/K8/K9 require an independently
observable semantic effect rather than a self-confirming tuple, while K6/K7 preserve the accepted
authority, role, and gate boundaries. The REVIEW revision 2 RDP observation remains
`not material — owed and forbidden to pay` and is not modified.

No inconsistency prevents execution. The shared `OUTCOMES`-fed result path is the intentional red
starting condition named by revision 4.

---

*ONB revision 4 return — TFW_20260902-175227_RCFR / Phase A | 2026-09-03*

## 11. Revision 5 Return — Budget-Safe Round 2

The governing order is approved `TS__phase-a__common_authority_and_context_topology__rev5.md`.
It retains R4 as the sole semantic change and permits readable, behavior-preserving compaction
only in the four named code/test files so the whole-tree metric includes every trace.

No blocking question remains. The rev4 budget STOP preserved committed red guards and prevented
an implementation, RF, evidence, or state commit. Its unstaged sketch was discarded before rev5
was applied. Current state remains `ONB`; authority is rev5.

Execution will preserve pre/post CLI, schema, collection, mutation, adapter, audit, and K0–K9
parity; dense representations and weakened gates are forbidden. The pre-review hard stop is
4,300 whole-tree changed LOC relative to `2728dae…`, with no new path.

---

*ONB revision 5 return — TFW_20260902-175227_RCFR / Phase A | 2026-09-03*

## 12. Revision 6 Return — Owner Budget Override

The governing order is approved `TS__phase-a__common_authority_and_context_topology__rev6.md`.
The owner authorizes a phase-local whole-tree ceiling of 6,000 changed LOC while retaining the
41-path, 4,600-LOC implementation/test/evidence bound. R4 remains the sole semantic change and
`docs/scripts/test_runtime_context.py` is the only implementation path permitted this round.

No blocking question remains. The rejected rev5 compaction experiment was discarded exactly from
its four paths before rev6 was applied; committed red guards and all earlier traces remain intact.
Execution will derive all six fields from each executing `SourceTree`, keep expected values
comparison-only, require minimal-source failure, and require a resolvable E3 substitution to change
produced output before the independent comparison rejects it.

---

*ONB revision 6 return — TFW_20260902-175227_RCFR / Phase A | 2026-09-04*
