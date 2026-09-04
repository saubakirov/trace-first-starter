# TS — TFW_20260902-175227_RCFR / Phase C: Closure, Secondary Paths, and Whole-System Proof

> **Date**: 2026-09-04
> **Author**: Codex (Coordinator)
> **Status**: ✅ APPROVED — saubakirov, 2026-09-04; execution authorized through the Phase C Coordinator task
> **Parent HL**: [Phase C derivation](HL__phase-c__closure_secondary_paths_and_whole_system_proof.md)
> **Master HL**: [Runtime Context Footprint Reduction](../HL-TFW_20260902-175227_RCFR.md)
> **Predecessor**: [Phase B RF](../phase-b/RF__phase-b__primary_role_paths.md) · [Phase B REVIEW rev2](../phase-b/REVIEW__phase-b__primary_role_paths__rev2.md)
> **Research**: [Iteration 2 RES](../research/iter2/RES.md) · [R04, R07, R19, R24–R34, R39](../research/iter2/3_extract.md)
> **Baseline**: `cf36dd6ac404b2335234cd9763bc4821409ca9fc`

---

## 1. Objective

Complete the frozen Runtime Context Footprint Reduction contract across status/journal writes,
lifecycle closure, and all seven secondary commands. The result must expose one current,
decision-purpose read graph for all eleven canonical commands, reduce real mandatory word exposure
without gaming the measure, preserve every decision/refusal/effect/gate/authority boundary, and pass
both self-hosted and clean-receiver proof.

## 2. Scope

### In Scope

- Make the seven secondary repository-local skills minimal command/role routers with no independent
  common-library preload.
- Give Resume, Docs, Knowledge, Release, Update, Config, and Init an ordered checkpoint Read Contract
  that loads task-local state first when a task exists and otherwise only exact decision inputs.
- Replace obsolete discovery, unbounded history reads, invalid config-registry targets, duplicated
  form/rule prose, and readerless active instructions with current single-owner behavior.
- Compact the status and journal-event form carriers while retaining every current schema,
  transition, immutability, attribution, compatibility, and refusal guarantee and placing every
  immutable bound before the write it governs.
- Extend the existing Phase A/B audit, source-derived semantic oracle, deletion ledger, integration
  harness, and four-vendor clean-receiver replay to the complete runtime system.
- Synchronize all changed skill/workflow copies and prove exact eleven-command routes and roles.

### Out of Scope

- Any amendment to frozen master HL §§1, 3–7, change to TFW meaning or algorithm, new role, lifecycle
  state, journal kind, artifact, persistent field, configuration key, or runtime authority.
- Any edit under `tasks/`, any prior RCFR phase artifact, the immutable RDP event, or unrelated/user
  work present after phase entry.
- Task-artifact content compression outside the two canonical state/event templates; essay, book,
  website, release/version/tag, migration execution, push, merge, publish, or deploy.
- Byte-size optimization, minification, formatting tricks, generated runtime packets, or moving text
  solely to improve the metric.

## 3. Principles Check

| # | Principle (master HL §7) | Enforced by | Gate |
|---|---|---|---|
| P1 | Context is a finite working resource | AC-1, AC-7 | every mandatory edge/repeat is word-counted |
| P2 | One concept, one authority, one read | AC-2–AC-4 | skill routes, workflow acts, template forms, shared range governs |
| P3 | Task facts before framework history | AC-2, AC-6 | selected status/journal and governing lineage precede global sources |
| P4 | Progressive disclosure without semantic loss | AC-2, AC-6, AC-7 | checkpoint reads plus baseline/candidate semantic records |
| P5 | Subtraction before addition or relocation | AC-3, AC-4, AC-7 | no new runtime file/key; net mandatory words decline |
| P6 | Meaning fixed, representation open | AC-2–AC-8 | source-derived decisions/refusals/effects/gates remain equal |
| P7 | Algorithms in steps, forms in templates, terms in glossary | AC-2–AC-4 | ownership and deliberate-duplicate audit |
| P8 | History remains discoverable, not resident | AC-3, AC-4 | deleted rationale maps to durable history and a live rule/test |
| P9 | Measurements resist gaming | AC-1, AC-7 | immutable ref, one `\S+` method, transitive/repeated/dynamic accounting |
| P10 | The framework must pass its own path | AC-5, AC-6, AC-8 | full lifecycle and four clean receivers |

## 4. Affected Files

| File | Action | Description |
|---|---|---|
| `.tfw/workflows/{resume,docs,knowledge,release,update,config,init}.md` | MODIFY | canonical secondary algorithms and ordered Read Contracts |
| `.tfw/adapters/codex/skills/tfw-{resume,docs,knowledge,release,update,config,init}/SKILL.md` | MODIFY | thin source command/role/workflow routers |
| `.agents/skills/tfw-{resume,docs,knowledge,release,update,config,init}/SKILL.md` | MODIFY | exact installed copies of source skills |
| `.claude/commands/tfw-{resume,docs,knowledge,release,update,config,init}.md` | MODIFY | exact copies of changed canonical workflows |
| `.agent/workflows/tfw-{resume,docs,knowledge,release,update,config,init}.md` | MODIFY | exact retained legacy self-hosting copies |
| `.tfw/templates/status.md` | MODIFY | compact task/phase state form and closed schema |
| `.tfw/templates/journal/event.md` | MODIFY | compact immutable event form, attribution and pre-write bounds |
| `.tfw/conventions.md` | MODIFY | lifecycle/shared authority only where duplicate or stale current prose remains |
| `.tfw/glossary.md` | MODIFY | current term routes only where the audit finds a stale or competing instruction |
| `.tfw/adapters/manifest.yaml` | MODIFY | remove Phase B-only commentary; retain one tooling-only 11-command map |
| `.tfw/scripts/gen_index.py` | MODIFY | lifecycle validation support only if required for pre-write/current-path enforcement |
| `.tfw/scripts/test_gen_index.py` | MODIFY | adverse status/journal/schema coverage for any validator change |
| `docs/scripts/test_runtime_context.py` | MODIFY | immutable all-command graph, corpus, semantic, mutant and ledger proof |
| `docs/scripts/test_integration.py` | MODIFY | secondary copy/route/registry/stale and clean-receiver proof |

**Budget:** 0 new runtime files, at most 44 modified implementation/test files, and at most 5,000
changed LOC. Mandatory phase artifacts and raw evidence are process traces. No budget override is
authorized.

## 5. Acceptance Criteria

### AC-1: Immutable complete runtime baseline and graph

The Phase A/B audit must derive the actual baseline at
`cf36dd6ac404b2335234cd9763bc4821409ca9fc` for all eleven canonical commands, both Researcher modes,
status/journal write checkpoints, revision return, and knowledge close.

- [ ] The unchanged primary graphs reproduce 24,730 Plan, 6,103 focused Research, 6,168 deep
  Research, 6,366 Handoff, and 25,182 Review words at phase entry.
- [ ] The secondary baseline is derived from source, not research forecasts, and the current seven
  skills/workflows plus two lifecycle templates reproduce the observed 9,873 carrier words before
  transitive/repeated edges are charged.
- [ ] Every edge names checkpoint, source/range, decision purpose, authority, observed words,
  repeat class, dynamic status, and charged status; full-file or transitive inputs cannot disappear
  merely because a candidate adds a Read Contract.
- [ ] Missing/duplicate headings, omitted command/status/template edges, unclassified full-library
  reads, and injected duplicate preloads fail independently of generated audit output.

Gate: targeted runtime-context tests and CLI audit against the immutable Git tree and candidate.

Evidence: Environment: clean Git baseline plus candidate worktree. Action: resolve every graph twice
with the same `\S+` counter and exercise omission/duplicate mutations. Observable success: exact
primary/carrier anchors, complete secondary totals and independently rejected graph defects.

### AC-2: Seven authoritative secondary command paths [depends: AC-1]

Each secondary skill must dispatch once into a complete canonical workflow; the workflow alone owns
ordered reads and the existing algorithm.

- [ ] Resume follows configured containers, selected task status/journal, each current phase's local
  state, and governing artifact lineage; derived indexes and obsolete `HL__Phase*`-style globs never
  determine state, and the user decision gate remains.
- [ ] Docs reads the selected status, REVIEW/RF, and `KNOWLEDGE.md` §§1–3 once; preserves significance
  triage, exact write ownership, markers, manual/batch approval, and never reads/writes §4, topics, or
  debt unless a separately named rule requires it.
- [ ] Knowledge preserves its digest transaction, problem/removed-ID hard stops, pending-only gather,
  Human-Only/dedup/contradiction/verification tests, two WAITs, processed markers, recomputation, and
  state-last retry convergence without skill-owned preloads.
- [ ] Release reads the exact release contract, VERSION, `[Unreleased]`, and authoritative DONE state
  since the last tag while preserving bump, checklist, changelog, version, project-step, verification,
  and no-tag/push/publish-without-authority gates; it does not load unrelated changelog history.
- [ ] Update uses the installed workflow only until a named target is pinned, then the pinned target
  workflow, only intervening changelog/migration ranges, and all current pin, three-question,
  classification, state-preservation, adapter, retired-vocabulary, verification, briefing, and cleanup
  refusals.
- [ ] Config reads config, the one registry, and only registered target ranges; edit approval, verify
  reporting, missing/duplicate target refusal, and affected adapter sync remain, and every registry
  address resolves at phase close.
- [ ] Init detects full-init versus attach/repair before broad discovery, progressively reads project
  material, preserves interview/research/setup/status/event/adapter/verification/RF/close gates, and
  never resets configured state or guesses the selected adapter.

Gate: one source-derived baseline/candidate semantic record and one output-changing adverse mutant
for each of Resume, Docs, Knowledge, Release, Update, Config, and Init, plus ordered read manifests.

Evidence: Environment: isolated command fixtures, including configured and empty projects. Action:
exercise ordinary, refusal, WAIT, resume, and repair branches. Observable success: identical
decisions, refusals, artifact effects, citations and gates with no independent skill preload.

### AC-3: Compact status, journal, and closure writes [depends: AC-1]

The task/phase state and event paths must be complete at the write checkpoint with no resident
incident essay or post-write-only bound.

- [ ] `status.md` retains its closed keys, task versus phase fixed sentence, quoted prose rule,
  authoritative/local-state meaning, current lifecycle vocabulary, `UNDECLARED` behavior, terminal
  outcome, second-resolution timestamps, bounds, and named readers.
- [ ] Journal events retain timestamped opaque-token identity, closed kinds, `on_behalf_of`, optional
  `via`, paired transitions, refs, optional 120-code-point summary, legacy `actor` tolerance,
  immutability/correction behavior, phase-local location, and the rule that unmatched artifacts get
  no invented event.
- [ ] Every immutable-field bound is read and mechanically exercisable before the durable write;
  overlong summaries, undeclared actors, invalid kinds, malformed times, and illegal transition
  pairs fail before a new event is accepted.
- [ ] Form/schema lives once in the templates; convention/workflow copies remain only where a distinct
  enforcement site is named and a reference would arrive too late.

Gate: template/schema tests, lifecycle transition scenarios, pre-write adverse cases, and the
current task/project checker with the pre-existing RDP exception isolated.

Evidence: Environment: temporary task and phase directories. Action: create valid status/events and
each adverse variant before installing them. Observable success: valid forms pass, invalid writes
are refused, compatibility records remain readable, and no committed event requires editing.

### AC-4: No active stale, readerless, or competing instruction [depends: AC-2, AC-3]

Every current runtime clause in the eleven-command graph must have a reader and one authority; every
surviving duplicate must state a distinct enforcement purpose.

- [ ] The audit finds zero live obsolete phase globs, sequence/counter state, invalid registry
  targets, unbounded history preloads, wrong adapter roots/roles, universal REVISE-to-TS wording, or
  other pre-2.x/current-path instruction outside explicit compatibility/migration/history allowlists.
- [ ] Each deleted block maps to its surviving rule, executable test, and durable historical source,
  or to an evidenced finding that it has no current reader.
- [ ] Every surviving duplicate is classified with both enforcement sites and why a reference would
  fail; “important” is not a purpose.
- [ ] The generated ledger/report and adapter manifest remain evidence/copy metadata and are never
  inputs to a runtime role decision.

Gate: source census, unique-heading/target resolver, deletion/duplicate ledger tests, and deliberate
stale/readerless/second-authority mutations.

Evidence: Environment: baseline and final tracked sources. Action: enumerate all active graph text
and retired-vocabulary hits. Observable success: zero unexplained current hits and a resolvable
disposition for every deletion or deliberate duplicate.

### AC-5: Secondary adapter and clean-receiver parity [depends: AC-2]

Every changed secondary route must propagate through the existing tooling-only topology without
creating a second runtime authority.

- [ ] Seven canonical workflows equal tracked Claude and retained legacy Antigravity copies byte for
  byte; seven Codex source skills equal installed copies byte for byte.
- [ ] The manifest resolves exactly 11 commands, canonical sources, roles, vendor paths, and copy
  strategies, with Researcher owning only Research and the other declared roles unchanged.
- [ ] Four empty receivers expose all 11 commands at documented paths; a second install is a no-op,
  drift is repaired, and unrelated/owner content plus unmarked roots are preserved.
- [ ] Init, Update, and Config consume the same manifest mapping as tooling metadata and reject a
  missing command, wrong role, unresolved target, duplicate managed block, or extra TFW command.

Gate: exact byte/set/role/path checks plus clean install, idempotence, mutation-repair, and
preservation replay for Codex, Claude, Cursor, and Antigravity.

Evidence: Environment: repository and four empty temporary receivers. Action: install, rerun, mutate
one managed copy, and enumerate routes. Observable success: exact parity, repair, no second-run diff,
and no unrelated receiver change.

### AC-6: Source-derived whole-lifecycle semantic proof [depends: AC-2, AC-3, AC-5]

The independent Phase A/B oracle must prove the complete task lifecycle and secondary decisions,
not prose similarity or self-consistency.

- [ ] Existing P/R/E/V/C/A records remain source-derived and green; new secondary/lifecycle records
  derive produced fields from baseline and candidate sources before independent expected comparison.
- [ ] Expected records cannot feed production, minimal anchor-only input fails, and at least one
  deliberate mutant per primary, secondary, lifecycle/closure, and adapter family changes a named
  output before rejection.
- [ ] A clean-context scenario covers Plan → Research → Handoff → Review → Docs → Knowledge → DONE,
  plus a REVISE return and task/phase resume, with exact role locks, state/event effects, citations,
  owner WAITs, refusal conditions, and hard stops.
- [ ] Separate scenarios cover Release authorization, pinned Update provenance/state preservation,
  Config approval/registry completeness, and Init full versus repair routing.

Gate: targeted semantic and integration tests that compare immutable baseline/candidate records and
reject output-changing source mutants.

Evidence: Environment: clean-context temporary projects and separate role sessions. Action: execute
the current-path decision scenarios without prior chat state. Observable success: identical records
and effects, complete lifecycle closure, and independent rejection of every mutant family.

### AC-7: Per-path and whole-corpus word reduction [depends: AC-1, AC-4, AC-6]

The final report must use one reproducible whitespace-word method and show the real runtime effect at
the immutable baseline and final candidate.

- [ ] Report exact before/after words and reduction for every canonical command/checkpoint, both
  Researcher modes, lifecycle write/close paths, the summed canonical trajectory, and the unique
  `.tfw` active-runtime corpus; repeated instructed reads are charged each time and section reads
  count only the resolved section.
- [ ] Every changed secondary/lifecycle path is at least 30% below its baseline, the combined active
  runtime corpus is at least 30% below baseline, and no primary entry path exceeds 24,730 / 6,103 /
  6,168 / 6,366 / 25,182 respectively.
- [ ] Dynamic task artifacts and relevance-triggered P5–P7 inputs are present but uncharged on both
  sides; no mandatory transitive edge or deliberate independent reread is excluded.
- [ ] Reduction comes only from deletion, consolidation, selective loading, or simpler ownership;
  no bytes, minification, relocation, generated formatting, or storage-only figure is used.

Gate: reproducible CLI report and arithmetic assertions against the named baseline and candidate.

Evidence: Environment: immutable Git baseline and final candidate. Action: capture raw graph rows and
summary arithmetic immediately before RF. Observable success: exact path/corpus tables, every bound
green, and independent recomputation matches.

### AC-8: Full verification, scope, and exclusion gate [depends: AC-5, AC-6, AC-7]

The phase must finish with all configured checks green and with every frozen/user boundary intact.

- [ ] Targeted runtime, gen-index, and integration suites pass; collection succeeds; the full
  `.tfw/scripts/` + `docs/scripts/` suite passes; project consistency exits zero.
- [ ] Task diagnostics report only the already-ruled immutable RDP `123>120` event unless a genuinely
  new external problem is surfaced and stopped on; Phase C does not normalize it.
- [ ] Diff inspection proves at most 44 authorized implementation/test files, at most 5,000 changed
  LOC, no new runtime file/key/artifact, no `tasks/` change, no prior-phase trace edit, and no
  unrelated/user change absorbed.
- [ ] RF names every modification/deletion and supplies exact path/corpus counts, tests,
  clean-receiver results, deviations, observations, residual risks, and the exact candidate commit;
  no merge or push occurs.

Gate: `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q`,
`python -m pytest .tfw/scripts/test_gen_index.py -q`,
`python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only`,
`python -m pytest .tfw/scripts/ docs/scripts/ -q`,
`python .tfw/scripts/gen_index.py --check project`, task diagnostic, and Git diff/blob checks.

Evidence: Environment: final candidate with clean tracked entry baseline. Action: record raw targeted,
full, project/task, diff, scope and exclusion outputs. Observable success: all authorized gates pass,
only the known immutable diagnostic remains, and the branch is ready for independent review.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-c__closure_secondary_paths_and_whole_system_proof.md` | required structured per-AC evidence and verdict |
| `evidence/runtime-context-whole-system.txt` | raw baseline/candidate graph, word and corpus audit |
| `evidence/semantic-and-lifecycle-whole-system.txt` | source-derived records, full lifecycle and rejected mutants |
| `evidence/stale-duplicate-ledger.txt` | active census plus deletion and deliberate-duplicate dispositions |
| `evidence/clean-receiver-secondary-routes.txt` | four-vendor exact route, idempotence, repair and preservation replay |
| `evidence/verification-whole-system.txt` | targeted/full tests, project/task diagnostics, scope and exclusion checks |

## 6. Technical Guidance

- Extend `docs/scripts/test_runtime_context.py`, `docs/scripts/test_integration.py`, and existing
  `gen_index` validation rather than creating a parallel audit, oracle, registry, or validator.
- Research iteration 2 R04, R07, R19, R24–R34 and R39 are the implementation catalogue. Forecast
  counts are context only; AC-1's source-derived `cf36dd6` baseline governs.
- Preserve the Phase A source-independence rule and Phase B rung route. A semantic test passes only
  when a source change alters the produced record before the expected oracle rejects it.
- Keep dynamic inputs explicit. A temporary audit or receiver is evidence; no generated report may
  become a role dependency or source of truth.
- Treat `.agent/workflows/` as retained self-hosting copies in this repository and plural
  `.agents/workflows/` as the manifest-declared Antigravity receiving path; neither substitutes for
  the other's proof.

## 7. Definition of Failure

- ❌ Any frozen meaning, algorithm, gate, authority boundary, refusal condition, lifecycle state,
  event kind, compatibility guarantee, or 30% threshold changes.
- ❌ Any command skill and workflow both own the same preload/algorithm, or any role must read the
  whole conventions, glossary, knowledge index, or changelog without a checkpoint-specific reason.
- ❌ A state/event rule is removed without a surviving authority and test, or an immutable bound has
  no pre-write reader.
- ❌ Resume trusts a derived index or obsolete glob; Config retains an unresolved registry target;
  Release/Update load unrelated history; Init resets configured project state.
- ❌ A generated audit, ledger, manifest, packet, or index becomes runtime authority or a second
  source of truth.
- ❌ Semantic proof compares anchors/prose only, lets expected data feed production, or uses a mutant
  that fails before changing the produced output.
- ❌ Any changed secondary/lifecycle path misses 30%, the combined active corpus misses 30%, a
  primary path regresses, or a mandatory/repeated/dynamic edge is hidden to improve arithmetic.
- ❌ A changed canonical behavior is not synchronized and proven in all tracked/clean-receiver
  adapter surfaces in this phase.
- ❌ `tasks/`, prior phase traces, the RDP event, release/tag/version state, unrelated/user work, or
  any file outside the authorized surface changes.
- ❌ Scope exceeds 44 modified implementation/test files or 5,000 changed LOC, or adds any runtime
  file/key/artifact without an owner-approved amendment.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| rare secondary branch is lost under compact prose | source-derived ordinary/refusal/WAIT scenario and mutant per command |
| status/event template trimming removes the only rule | pre-write schema fixtures and deletion ledger with rule/test/history targets |
| secondary baseline is biased by the candidate Read Contract | resolve baseline from immutable Git source with legacy and current parsers |
| whole-corpus sum double-counts or hides repeats | report both instructed exposure and unique `.tfw` union with explicit edge classes |
| shared convention cleanup breaks primary routes | reproduce the five phase-entry counts and semantic families after every shared edit |
| adapter parity passes only in self-hosting layout | four empty receivers and distinct singular/plural Antigravity assertions |
| final proof is captured before the final trace effect | re-run counts, quotations, and state checks immediately before RF and name the commit |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| `.tfw/workflows/knowledge.md` | Phase A | preserve digest identity, pending/problem gates, WAITs and state-last transaction |
| `.tfw/workflows/{init,update,config}.md` | Phase A | preserve manifest-driven four-adapter behavior and clean-receiver guarantees |
| `.tfw/conventions.md`, `.tfw/glossary.md` | Phases A and B | retain unique-heading addresses, PV routing, lifecycle and REVISE authority |
| `.tfw/adapters/manifest.yaml` | Phases A and B | tooling-only exact 11-command map; never runtime authority |
| `.tfw/scripts/{gen_index.py,test_gen_index.py}` | Phase A | preserve digest reconciliation, discovery and all K0–K9 behavior |
| `docs/scripts/{test_runtime_context.py,test_integration.py}` | Phases A and B | extend the same oracle/audit/receiver harness; preserve all accepted cases |
| tracked skill/workflow copies | Phases A and B | retain exact byte/role parity while synchronizing Phase C sources |

---

*TS — TFW_20260902-175227_RCFR / Phase C | 2026-09-04*
