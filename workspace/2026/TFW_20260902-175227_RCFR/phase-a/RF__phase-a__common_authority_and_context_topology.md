# RF — TFW_20260902-175227_RCFR / Phase A: Common Authority and Context Topology

> **Date**: 2026-09-03
> **Author**: Codex (Executor, acting on behalf of `saubakirov`)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW_20260902-175227_RCFR](../HL-TFW_20260902-175227_RCFR.md)
> **Phase HL**: [HL Phase A](HL__phase-a__common_authority_and_context_topology.md)
> **TS**: [TS Phase A revision 2](TS__phase-a__common_authority_and_context_topology__rev2.md)
> **Approval baseline**: `2728dae78d55f6cb7daa39c82874ad5b43621f8a`

---

## 1. What Was Done

### New Files

| File | Description |
|------|-------------|
| `.tfw/adapters/manifest.yaml` | Tooling-only four-adapter, eleven-command copy/install contract. |
| `docs/scripts/test_runtime_context.py` | Independent semantic oracle, mutants, heading resolver, deletion ledger, and transient word/read audit. |
| `phase-a/evidence/EV__phase-a__common_authority_and_context_topology.md` | Structured evidence verdict for AC-1 through AC-6. |
| `phase-a/evidence/runtime-context-before-after.txt` | Reproducible baseline/candidate whitespace-word audit. |
| `phase-a/evidence/knowledge-gate-replay.txt` | K0–K9, migration, retry, reconciliation, and state-last replay. |
| `phase-a/evidence/semantic-fixtures.txt` | Behavioral records and one rejected mutant per fixture family. |
| `phase-a/evidence/clean-receiver-adapters.txt` | Exact command, role, vendor-root, and empty-receiver results. |

### Modified Files

| File | Changes |
|------|---------|
| `AGENTS.md` | Replaced universal foundation preload with compact command routing and workflow-owned reads. |
| `.tfw/conventions.md` | Added the unique-heading selective-read contract and compacted shared rules to operative clauses with durable history routes. |
| `.tfw/glossary.md` | Rebuilt operational entries as meaning/authority routers while retaining PV duties, RDP semantics, and retired-term lookup. |
| `.tfw/workflows/plan.md`, `.tfw/workflows/knowledge.md` | Added exact ordered read contracts and replaced sequence gating with digest reconciliation and state-last semantics. |
| `.tfw/workflows/init.md`, `.tfw/workflows/update.md`, `.tfw/workflows/config.md` | Replaced duplicated adapter-copy tables with validation and consumption of the single manifest. |
| `.claude/commands/tfw-plan.md`, `.claude/commands/tfw-knowledge.md`, `.claude/commands/tfw-init.md`, `.claude/commands/tfw-update.md`, `.claude/commands/tfw-config.md` | Synchronized the five changed canonical workflows into tracked Claude command copies. |
| `.agent/workflows/tfw-plan.md`, `.agent/workflows/tfw-knowledge.md`, `.agent/workflows/tfw-init.md`, `.agent/workflows/tfw-update.md`, `.agent/workflows/tfw-config.md` | Synchronized the same five canonical workflows into the tracked legacy Antigravity copies authorized by revision 2. |
| `.tfw/knowledge_state.yaml`, `.tfw/templates/knowledge_state.yaml` | Migrated the live and template schemas from sequence/task cursors to full task digest maps while preserving audit metadata and statistics. |
| `.tfw/scripts/gen_index.py`, `.tfw/scripts/test_gen_index.py` | Added deterministic selected-section hashing, pending/reconciliation JSON, gate arithmetic, refusal paths, and K0–K9 coverage. |
| `docs/scripts/test_integration.py` | Added exact manifest, path/role, installed-copy, mutation, and clean-receiver assertions. |
| `.tfw/adapters/README.md` | Documented the single non-runtime copy/install mapping. |
| `.tfw/adapters/codex/README.md`, `.tfw/adapters/claude-code/README.md`, `.tfw/adapters/antigravity/README.md` | Documented exact vendor discovery paths and complete command/role contracts. |
| `.tfw/adapters/codex/AGENTS.md.template`, `.tfw/adapters/claude-code/CLAUDE.md.template`, `.tfw/adapters/cursor/tfw.mdc.template`, `.tfw/adapters/antigravity/tfw-rules.md.template` | Installed compact persistent routers without common-file preload. |
| `CLAUDE.md`, `.agent/rules/agents.md`, `.agent/rules/tfw.md` | Synchronized the currently tracked persistent carriers named by the TS. |

## 2. Key Decisions

1. The selected canonical workflow is the only owner of checkpoint reads. Root rules and adapter surfaces dispatch; they do not independently preload common files or restate algorithms.
2. Knowledge identity is `SHA-256(path NUL heading NUL normalized-body)` over sorted selected sections, with an explicit empty digest. The live map is written only after final source content exists and a complete, problem-free reconciliation is recomputed.
3. Adapter metadata is one tooling manifest, never a runtime authority. Clean receivers are the portability oracle; existing repository files cannot satisfy the test by accident.
4. Shared prose was removed only behind behavior/effect/citation/gate fixtures, unique-heading failure checks, history resolution, and an explicit R03–R14 deletion ledger.
5. Revision 2's ten derived copies were synchronized exactly; no additional adapter carrier or workflow algorithm was added to scope.

## 3. Acceptance Criteria

- [x] AC-1 — Root and workflows implement one selective, status/journal-first, unique-heading read contract with hard failure on an unresolved address.
- [x] AC-2 — Shared authority is compact, operational terms route to one owner, PV duties and RDP semantics survive, and removed history resolves durably.
- [x] AC-3 — The digest Knowledge Gate is deterministic, retry-safe, full-identity based, state-last, and covered by K0–K9 plus malformed/removed-task failures.
- [x] AC-4 — One exact manifest installs four vendor roots and 11/11 command/role routes into empty receivers; `/tfw-research` is Researcher.
- [x] AC-5 — Baseline and candidate records match across P/R/E/V/C/A families, every deliberate mutant fails, and the audit output is non-authoritative.
- [x] AC-6 — Both owned paths exceed the 30% reduction threshold, configured lint/test and project checks pass, and the unrelated task-state defect is only reported.

## 4. Verification

- Lint (`python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only`): **PASS — 405 tests collected**.
- Tests (`python -m pytest .tfw/scripts/ docs/scripts/ -q`): **PASS — 404 passed, 1 skipped in 159.98s**.
- Resolver (`python -m pytest .tfw/scripts/test_gen_index.py -q`): **PASS — 155 passed**.
- Runtime context (`python -m pytest docs/scripts/test_runtime_context.py -q`): **PASS — 64 passed**.
- Integration (`python -m pytest docs/scripts/test_integration.py -q`): **PASS — 47 passed**.
- Project consistency (`python .tfw/scripts/gen_index.py --check project`): **PASS**.
- Task-state diagnostic (`python .tfw/scripts/gen_index.py --check tasks`): **expected non-gating report — one pre-existing RDP journal summary is 123 code points against a 120 ceiling; not modified under this TS**.
- Context audit: **PASS — `/tfw-plan` 32,917 → 8,028 words (75.6% reduction); `/tfw-knowledge` 31,779 → 2,052 words (93.5% reduction)**.
- Scope: **34 modified implementation files + 2 new implementation/test files + 5 evidence files; mandatory lifecycle traces separate; within revision 2's 41-file and 4,600-LOC ceilings**.

## 5. Evidence

> **Cognitive mode:** Observational verification — evidence lives in the EV file, not inline.

See [EV file](evidence/EV__phase-a__common_authority_and_context_topology.md) for evidence details.

Evidence verdict: 6/6 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `workspace/2026/TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md` | 9 | style | Pre-existing journal summary is 123 code points, exceeding the configured 120-code-point ceiling; `--check tasks` reports it. AC-6 explicitly requires naming and not repairing unrelated task state. |

## 7. Fact Candidates

No fact candidates.

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

```text
root/adapter router
        |
        v
selected canonical workflow --unique heading--> shared rule or term authority
        |                                      (hard stop if 0 or >1 matches)
        +--> task status/journal first
        +--> checkpoint task artifacts/templates

current task traces --selected sections--> canonical SHA-256 map
        |                                      |
        | final source effects                 | problem-free full reconciliation
        +------------------------------------->+--> knowledge_state.yaml (state last)
```

---

*RF — TFW_20260902-175227_RCFR / Phase A: Common Authority and Context Topology | 2026-09-03*

## 10. Revision 3 return — review round 1 result

R1–R3 are complete. Both active root carriers now delegate selection without a universal
common-library preload. The audit discovers actual root, skill, workflow, full-file, addressed,
transitive, and repeated reads: `/tfw-plan` is 64,229→35,068 words (45.4% reduction) and
`/tfw-knowledge` is 78,587→41,347 (47.4%).

The semantic gate reads the clean Git baseline and working-tree candidate, resolves governing
source anchors, compares all 19 P/R/E/V/C/A results, rejects six source mutants, and separately
rejects an absent source root, omitted route, and missing/duplicate headings. R03–R14 resolve
their research condition/action plus real authority, test, and history targets. Antigravity's
conventions, glossary, manifest, and clean receiver agree on plural `.agents/{rules,workflows}`;
each independent singular mutation fails.

Verification: 412 collected; 411 passed, 1 skipped; project consistency PASS; expected unrelated
RDP task-state diagnostic remains the single 123>120 failure and was not modified. No deviation
from revision 3 scope. Implementation commit: `037be0d`.

Final cumulative scope is 3,224 additions + 1,239 deletions = 4,463 changed LOC across 57 files, within the 4,600 ceiling.

## 11. Revision 6 return — final R4 repair

### 11.1 What Was Done

`docs/scripts/test_runtime_context.py` now derives every normalized semantic field from a clause
read through the executing baseline or candidate `SourceTree`. Each record carries field-level
path, heading, and clause provenance. The rev5 compaction experiment was discarded; its other
three paths match `f5cc3f1` exactly.

### 11.2 Key Decisions

1. `EXPECTED_RECORDS` is a comparison-only oracle. `Scenario` contains source addresses, while
   `DERIVATIONS` maps observed clauses to normalized values without reading expected data.
2. A field resolves exactly one clause variant or execution fails. This makes missing semantic
   content observable while allowing baseline and candidate wording to normalize identically.
3. The E3 adverse variant is deliberately resolvable: changing the build-failure rule changes
   the produced decision, refusal, and gate before the independent expected comparison rejects it.

### 11.3 Acceptance Criteria

- [x] All 19 P/R/E/V/C/A records derive all six fields independently from both source trees.
- [x] Expected mutation cannot feed production; minimal anchor-only input fails.
- [x] Preserved-address semantic substitution completes, changes output, and fails comparison.
- [x] Existing Knowledge Gate, integration, audit, structural, receiver, and ledger gates remain green.
- [x] Both rev6 counters remain inside their separately approved ceilings.

### 11.4 Verification

- Runtime context: **73 passed**.
- Gen-index: **155 passed**.
- Combined runtime/integration: **121 passed**.
- Configured lint: **415 tests collected**.
- Configured tests: **414 passed, 1 skipped**.
- Project consistency: **PASS**.
- Context audit: **45.4% plan reduction; 47.4% knowledge reduction**.
- Task diagnostic: the immutable RDP summary remains the sole expected `123>120` report.
- Rejected compaction paths: exact equality with `f5cc3f1` for gen-index implementation/tests and integration tests.
- Final counters: **41 implementation/test/evidence paths; 2,559 additions + 1,236 deletions = 3,795 LOC. Whole candidate: 69 paths; 4,278 additions + 1,239 deletions = 5,517 LOC.**

### 11.5 Evidence

See [EV file](evidence/EV__phase-a__common_authority_and_context_topology.md) and
[`semantic-fixtures.txt`](evidence/semantic-fixtures.txt). Revision 6 evidence verdict:
4/4 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A.

### 11.6 Observations

The existing RDP journal summary remains 123 code points against the configured 120 ceiling. It is
immutable, out of scope, and unchanged, as ruled in REVIEW revision 2.

### 11.7 Fact Candidates

No fact candidates.

### 11.8 Strategic Insights

No strategic insights.

### 11.9 Diagrams

```text
baseline SourceTree ---\
                       clause resolver -> produced record -> independent expected comparison
candidate SourceTree --/                    | field/path/heading/clause provenance
```

Implementation commit: `13853b0`.
