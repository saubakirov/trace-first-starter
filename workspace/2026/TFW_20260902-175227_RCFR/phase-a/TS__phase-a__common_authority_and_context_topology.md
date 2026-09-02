# TS — TFW_20260902-175227_RCFR / Phase A: Common Authority and Context Topology

> **Date**: 2026-09-02
> **Author**: Codex (Coordinator)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [Phase A derivation](HL__phase-a__common_authority_and_context_topology.md)
> **Master HL**: [Runtime Context Footprint Reduction](../HL-TFW_20260902-175227_RCFR.md)
> **Research**: [Iteration 2 RES](../research/iter2/RES.md) · [R01–R39](../research/iter2/3_extract.md)

---

## 1. Objective

Establish the common C9 context contract before role-specific compression: one selective read owner, compact shared rules and term routing, a retry-safe Knowledge Gate for timestamp task IDs, and independent semantic/word-count/receiver checks. Phase A removes the universal context tax where its common mechanism is owned, while making every later deletion and adapter change mechanically falsifiable.

## 2. Scope

### In Scope

- Apply research recommendations R01–R14, R20, and R25–R30.
- Establish one exact adapter copy/install mapping and repair R34–R39 only as needed for the common routing and clean-receiver contract.
- Replace the obsolete Knowledge Gate sequence cursor through full reconciliation; preserve Human-Only, deduplication, contradiction, verification, threshold, and WAIT semantics.
- Introduce paired decision fixtures and an ephemeral read audit whose output is evidence, never runtime authority.
- Record current and after word exposure with the same whitespace method and every instructed repeat counted.

### Out of Scope

- Compress the primary role algorithms in `research/base.md`, `handoff.md`, and `review.md`; Phase B owns them.
- Compress the remaining docs, resume, release, update, config, and init algorithms; Phase C owns their runtime paths. Phase A may modify their adapter-copy sections only.
- Rewrite task artifacts, historical tasks, the book, essays, CHANGELOG history, or migrations merely to reduce storage.
- Claim candidate semantic success from word counts or prose similarity.

## 3. Principles Check

| # | Principle (from master HL §7) | Enforced by | Gate |
|---|---|---|---|
| P1 | Context is a finite working resource | AC-6 | repeated mandatory word exposure is measured by checkpoint |
| P2 | One concept, one authority, one read | AC-1, AC-2 | authority and repeat classifications have one surviving owner |
| P3 | Task facts before framework history | AC-1 | status/journal precede triggered shared or historical reads |
| P4 | Progressive disclosure without semantic loss | AC-1, AC-5 | addressed reads and paired behavioral oracle |
| P5 | Subtraction before addition or relocation | AC-2 | every new mapping/test removes or replaces a named duplicate |
| P6 | Meaning fixed, representation open | AC-3, AC-5 | K0–K9 and decision/refusal/effect/citation/gate equality |
| P7 | Algorithms in steps, forms in templates, terms in glossary | AC-1–AC-3 | owner-specific checks reject duplicated mechanics |
| P8 | History remains discoverable, not resident | AC-2 | all redirects resolve and no deleted sole carrier is unmapped |
| P9 | Measurements resist gaming | AC-6 | whitespace words, repeats, transitive ranges, and raw output |
| P10 | The framework must pass its own path | AC-4–AC-6 | repository plus empty-receiver checks |

## 4. Affected Files

| File | Action | Description |
|---|---|---|
| `AGENTS.md` | MODIFY | keep conduct/command routing; remove the universal four-file preload from the managed block |
| `.tfw/conventions.md` | MODIFY | selective-read contract; compact operative shared rules; history redirects; query-only compatibility |
| `.tfw/glossary.md` | MODIFY | one-sentence term router; addressed PV exception; historical lookup entries |
| `.tfw/workflows/plan.md` | MODIFY | exact Phase-A read contract and digest-based Knowledge Gate |
| `.tfw/workflows/knowledge.md` | MODIFY | pending-task digest transaction, reconciliation, recomputation, state-last write |
| `.tfw/workflows/{init,update,config}.md` | MODIFY | consume and validate one adapter copy/install mapping; do not duplicate it in prose |
| `.tfw/knowledge_state.yaml` | MODIFY | migrate sequence cursor to task-to-section SHA-256 map |
| `.tfw/templates/knowledge_state.yaml` | MODIFY | canonical digest-map state schema |
| `.tfw/scripts/gen_index.py` | MODIFY | read-only pending-task/digest resolver and stable JSON output |
| `.tfw/scripts/test_gen_index.py` | MODIFY | K0–K9, migration, ambiguity, removal, and deterministic ordering tests |
| `docs/scripts/test_integration.py` | MODIFY | adapter mapping, history-link, installed-copy, and receiver integration checks |
| `docs/scripts/test_runtime_context.py` | CREATE | independent semantic fixtures and ephemeral transitive read/word audit |
| `.tfw/adapters/README.md` | MODIFY | document the single copy-mapping contract without becoming role authority |
| `.tfw/adapters/{codex,claude-code,antigravity}/README.md` | MODIFY | document the exact vendor discovery path and complete command/role contract |
| `.tfw/adapters/{codex/AGENTS.md.template,claude-code/CLAUDE.md.template,cursor/tfw.mdc.template,antigravity/tfw-rules.md.template}` | MODIFY | compact common router and vendor-correct persistent rule contract |
| `CLAUDE.md`, `.agent/rules/agents.md`, `.agent/rules/tfw.md` | MODIFY | synchronize currently installed persistent rule carriers without touching unrelated content |
| `.tfw/adapters/manifest.yaml` | CREATE | one tooling-only map of vendor targets, 11 commands, roles, sources, and copy/check strategy |

**Budget:** 2 new implementation/test files and 24 modified files; up to 5 phase evidence files. Maximum 31 affected files and an estimated 3,800 changed LOC, within 50 files / 50 new / 5,000 LOC / 50 modified. Brace groups above are counted by their concrete members. Net text is expected to shrink despite changed-line count.

## 5. Acceptance Criteria

### AC-1: One selective read contract

The managed root block routes commands, the selected workflow owns checkpoint reads, and shared ranges are loaded only by unique heading when a decision requires them.

- [ ] Root instructions do not order a universal reload of `AGENTS.md`, full `conventions.md`, full `glossary.md`, or full `KNOWLEDGE.md`.
- [ ] `conventions.md` defines status/journal-first selection, unique-heading resolution, and a hard stop for missing or duplicate addressed headings.
- [ ] `plan.md` and `knowledge.md` contain one ordered prerequisite/read list each; no skill or adapter root becomes a second algorithm owner.
- [ ] Every retained full-file or repeated edge has a named checkpoint purpose and authority classification.

Gate: `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q` plus read-audit output containing no unclassified full-library edge.

Evidence: Environment: current repository and empty temporary receiver. Action: resolve `/tfw-plan` and `/tfw-knowledge` from root rule to checkpoint inputs. Observable success: identical required task/PV inputs, no duplicate common preload, and hard failure after injecting a missing or duplicate heading.

### AC-2: Compact shared authority with durable history

Shared rules remain executable while terminology and historical explanation stop owning algorithms.

- [ ] Each operational glossary heading has one discriminating sentence and one normative authority link; steps, field lists, and refusal algorithms live only at their owners.
- [ ] The P0–P7 table and independent Coordinator/Reviewer P0–P4 duties remain addressable and unchanged in meaning.
- [ ] Debt Registry, Task Board, and §14.1 remain available only through explicit historical/compatibility lookup routes.
- [ ] Every removed R03–R14/G4 block maps to a surviving condition/action/authority, structural test, and durable history source or an explicit no-current-reader finding.
- [ ] Any surviving inline duplicate names the local enforcement act that makes a pointer insufficient.

Gate: history-link resolver, glossary owner assertions, G4 deletion-ledger coverage, and deliberate-duplicate tests in `docs/scripts/test_runtime_context.py`.

Evidence: Environment: clean-context fixture corpus. Action: resolve representative current and retired terms, a frozen amendment, a revision, and a PV decision. Observable success: baseline and candidate cite the same authority/history and take the same required action or refusal.

### AC-3: Computable and retry-safe Knowledge Gate

The Knowledge Gate uses full task identity plus canonical candidate/insight-section content, not sequence or timestamp ordering.

- [ ] The resolver enumerates every resolvable current and legacy task, excludes phases as tasks, and hashes sorted `path NUL heading NUL body` tuples after LF normalization; an explicit empty tuple represents no selected section.
- [ ] `processed_task_digests` stores one 64-lowercase-hex digest per full task ID; `last_consolidation_date` is audit metadata and `last_consolidation_seq` is removed after successful reconciliation.
- [ ] Missing/changed IDs are pending; a previously recorded missing task, ambiguous/duplicate identity, malformed path, or unresolved trace hard-stops.
- [ ] `off`, `soft`, and `hard` preserve their configured behavior; hard routes to `/tfw-knowledge` exactly at `delta >= interval`, including no-candidate tasks.
- [ ] `/tfw-knowledge` preserves Human-Only, deduplication, contradiction, verification, and both WAIT gates; approved facts/markers precede post-marker digest recomputation and the state-last write.
- [ ] First migration performs full reconciliation and never uses old sequence/date state to skip a source.

Gate: `python -m pytest .tfw/scripts/test_gen_index.py -q`; K0–K9 all pass, including no-op, below/exact threshold, retry, migration, equal timestamp, candidate/no-candidate, late edit, and removed task.

Evidence: Environment: temporary repository seeded with K0–K9 and a copy of current task topology. Action: run pending JSON, simulate a partial knowledge write, retry, and reconcile an absent map. Observable success: stable pending IDs/digests, no duplicate fact effect, detected removal, and state written only after source effects.

### AC-4: Exact adapter copy and receiving-project contract

Adapter installation uses one tooling mapping and each supported vendor receives its documented root and 11-command/role contract without making the mapping a runtime authority.

- [ ] The mapping names Codex, Claude, Cursor, and Antigravity persistent rule target, all 11 command targets, canonical source, canonical role, and copy/check strategy.
- [ ] Init, update, and config reference the one mapping instead of maintaining divergent command tables.
- [ ] Empty-receiver installation resolves 11/11 commands for each adapter at the vendor-documented path; `/tfw-research` resolves to Researcher.
- [ ] Persistent root templates contain the compact router and no mandatory full-foundation preload.
- [ ] Codex remains 11/11; the measured Claude 10/11, Cursor 0/11, and Antigravity obsolete-path defects fail the old fixture and pass only after candidate installation.

Gate: adapter manifest schema, exact-set/role/path assertions, installed-copy drift checks, and empty-receiver integration test.

Evidence: Environment: four empty temporary receiver directories. Action: execute the candidate installation mapping and enumerate vendor discovery paths. Observable success: exact 11-command set and roles for every adapter, correct persistent rule path, and no reliance on files pre-existing in this repository.

### AC-5: Independent semantic and audit surface

Behavioral equivalence is judged independently from candidate wording and generated read reports.

- [ ] Fixture families P1–P4, R1–R3, E1–E4, V1–V4, C1–C3, and A1 encode input plus expected `{decision, refusal, artifact effects, citations, gate}`.
- [ ] Current baseline and C9 candidate pass the same oracle; at least one deliberate mutant per family fails.
- [ ] The read audit emits command, checkpoint, source heading, reason, observed words, repeat classification, and authority to stdout or a temporary test path only.
- [ ] No role workflow, skill, adapter root, or task artifact reads generated audit output.
- [ ] An omitted edge and missing/duplicate heading are caught independently of the audit generator's own output.

Gate: `python -m pytest docs/scripts/test_runtime_context.py -q` with baseline/candidate/mutant results and no committed generated report.

Evidence: Environment: fresh fixture directories with only contract-declared inputs. Action: run paired current/candidate scenarios and mutants. Observable success: semantic records match for valid pairs, every mutant family fails, and prose differences do not affect the verdict.

### AC-6: Honest Phase-A reduction and regression gate  [depends: AC-1, AC-2, AC-3, AC-4, AC-5]

Phase A records what it actually changes and leaves later role reductions to their declared phases.

- [ ] Before counts are rerun at execution start so concurrent carrier changes cannot be hidden behind the research snapshot.
- [ ] `/tfw-plan` and `/tfw-knowledge` each reduce fixed instructed exposure by at least 30% under the same transitive/repeated-read method; the research targets 25,620 and 11,840 words are reported as comparisons, not substituted for observation.
- [ ] No measured canonical role/checkpoint regresses; unfinished Phase-B/C paths remain explicitly marked pending rather than reported as complete savings.
- [ ] The full C9 projection remains reproducible from declared ranges, while phase evidence separates observed Phase-A results from future estimates.
- [ ] Project lint/test commands pass; any unrelated pre-existing task-state validation problem is named and not repaired under this TS.

Gate: `python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only`, `python -m pytest .tfw/scripts/ docs/scripts/ -q`, `python .tfw/scripts/gen_index.py --check project`, and the Phase-A context audit using one whitespace-word implementation.

Evidence: Environment: repository checkout after candidate changes plus clean receiver. Action: capture raw before/after audit output and full test output. Observable success: at least 30% observed reduction for both Phase-A-owned command paths, zero checkpoint regressions, exact separation of observed/projected rows, and resolvable evidence files.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-a__common_authority_and_context_topology.md` | required structured per-AC evidence and verdict |
| `evidence/runtime-context-before-after.txt` | raw command/checkpoint/range/repeat word report |
| `evidence/knowledge-gate-replay.txt` | K0–K9, migration, retry, and state-last output |
| `evidence/semantic-fixtures.txt` | baseline/candidate/mutant semantic records |
| `evidence/clean-receiver-adapters.txt` | four-adapter empty-install command/role/path results |

## 6. Technical Guidance

- Treat [iteration 2 Gather](../research/iter2/2_gather.md) G1–G5 and [Extract](../research/iter2/3_extract.md) R01–R39 as reference material; the acceptance criteria above govern.
- The selected digest algorithm is fully specified in Gather G2. Hashes detect source changes, not truth; human knowledge gates remain unchanged.
- Use unique headings as runtime addresses. Research line numbers are evidence for the current snapshot and must not become the contract.
- The G4 ledger is exhaustive for the proposed common deletions. Add a row before removing any additional narrative block.
- Keep adapter mapping as copy/install metadata. Role algorithms remain in canonical workflows; installed command bodies remain derived copies.
- Preserve unrelated dirty work. `.tfw/glossary.md` is an identified overlap at planning time; if its current diff cannot be reconciled without changing another task's intent, stop before editing it.

## 7. Definition of Failure

- ❌ A universal common-file preload remains in a Phase-A-owned bootstrap or prerequisite path without a distinct named decision.
- ❌ A glossary/history deletion lacks a surviving authority, test, and history/compatibility route where one is required.
- ❌ The digest excludes no-candidate tasks, orders by timestamp, hides a removed task, uses a pre-marker hash, or writes state before approved source effects.
- ❌ Adapter installation passes by checking only files that happened to exist; any vendor resolves fewer or more than the exact 11 commands or the wrong role/path.
- ❌ A generated manifest/report becomes a role input or validates itself without an independent semantic oracle.
- ❌ Counts omit repeated/transitive reads, use bytes/minification, claim projected Phase-B/C savings as observed, or miss the 30% Phase-A command threshold.
- ❌ Existing user changes in `.tfw/glossary.md` or any other overlapping file are overwritten or committed without reconciliation.
- ❌ Any frozen lifecycle, role, freeze, research, evidence, review, task-state, or knowledge guarantee changes.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| concurrent glossary work invalidates the research line map | rebaseline by heading and compare the dirty diff before edits; stop on semantic conflict |
| a digest map grows with every task | accept linear state now because only checker/knowledge read it; measure serialized size and retain partitioning as a future option only if operationally needed |
| exact adapter paths change upstream | source vendor paths in tests and make path mismatch explicit rather than silently falling back |
| deterministic fixtures overfit candidate text | oracle records behavior/effects/citations/gates; deliberate mutants prove independence |
| Phase A changes secondary workflow copy sections early | restrict edits to mapping/read contracts and list the files as cross-phase surfaces |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md` | Phases B and C | Phase-A owners/addresses and fixtures must remain stable |
| `.tfw/workflows/knowledge.md` | Phase C | preserve the digest transaction while compressing the remaining closure prose |
| `.tfw/workflows/{init,update,config}.md` | Phase C | Phase A changes mapping/read sections only; later edits reuse them |
| `.tfw/adapters/manifest.yaml` and root templates | Phases B and C | synchronize command bodies as each role workflow changes; mapping remains non-normative |
| `docs/scripts/test_runtime_context.py`, `docs/scripts/test_integration.py` | Phases B and C | extend the same oracle and receiver matrix; do not create parallel test authorities |
| `.tfw/scripts/gen_index.py`, `.tfw/scripts/test_gen_index.py` | Phase C | later discovery changes must preserve K0–K9 and stable JSON |

---

*TS — TFW_20260902-175227_RCFR / Phase A: Common Authority and Context Topology | 2026-09-02*
