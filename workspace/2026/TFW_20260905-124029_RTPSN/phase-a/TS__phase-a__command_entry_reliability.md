# TS — TFW_20260905-124029_RTPSN / Phase A: Command Entry Reliability

> **Date**: 2026-09-05
> **Author**: Codex (Coordinator)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [Phase A derivation](HL__phase-a__command_entry_reliability.md)
> **Master HL**: [Role, Task, and Phase Session Naming](../HL-TFW_20260905-124029_RTPSN.md)
> **Research**: [Iteration 1 RES](../research/iter1/RES.md) · [Iteration 2 RES](../research/iter2/RES.md)

---

## 1. Objective

Deliver a reproducible, bounded command-entry contract for all 11 TFW commands and four declared adapter classes. Phase A must add real Codex behavioural evidence to the existing structural proof, retain the current thin proxy as the production default, and permit only an evidence-qualified bounded strengthening without claiming that RCFR or any architecture caused the known incidents.

## 2. Scope

### In Scope

- Reproduce the source/receiver/runtime census and current-versus-pre-RCFR entry measurements from immutable Git revisions.
- Define six distinct evidence levels: source presence, receiver parity, command invocation, complete canonical load, later conformance, and controlled comparative effect.
- Add an explicit, non-default evaluation harness and deterministic tests for its fixtures, arm generation, graders, statistics, budgets, redaction, and evidence output.
- Run the fixed 54-run Codex matrix over three entry arms and six representative Coordinator/Researcher/Executor/Reviewer fixtures.
- State one universal pre-action sequence without introducing a second command algorithm or a universal read.
- Keep the current proxy unless the strengthened proxy alone clears every deployment threshold; synchronize all 11 source/installed Codex skill pairs only on that result.
- Revalidate all 11 commands, four manifest adapters, installed copies, absent receiver classes, clean receivers, Role Locks, Read Contracts, and startup word/token estimates.

### Out of Scope

- Phase B title grammar, rename checkpoints, `LEAD`, phase cues, U+00B7 rendering, collision handling, or stable-key suffix implementation.
- Production full-copy or direct-single-authority Codex migration; a winning result for either requires a new approved TS.
- Changes to canonical workflow steps, gates, roles, manifest routes/roles, persistent root preload, task identity, or CRATM orchestration.
- Human recognition, sidebar truncation/search, or non-Codex live-host claims.
- A registry, service, daemon, hook, generated runtime dependency, or default networked test.
- Reclassification of the CRATM/RTPSN incidents or an architecture-causality claim beyond the frozen research findings.

## 3. Principles Check

| # | Master HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Causality before remedy | AC-1, AC-6 | incident class and architecture estimate remain separate fields |
| P2 | One canonical algorithm | AC-2, AC-5 | proxies route; canonical workflows alone own steps/gates |
| P3 | Role Lock before task action | AC-3, AC-5 | invocation/load/order graders and negative skill mutants |
| P4 | Invocation, load, coverage, and compliance differ | AC-1, AC-3, AC-6 | six independent evidence levels; no aggregate replaces them |
| P5 | Research before vocabulary | N/A | naming vocabulary belongs only to Phase B and is excluded |
| P6 | Resolve before naming | N/A | no naming action is implemented in Phase A |
| P7 | Recognition before formalism | N/A | human title recognition is not a Phase-A claim |
| P8 | Proportionate assurance | AC-2–AC-4 | fixed 54-run and usage/time ceilings; bounded deployment delta |
| P9 | Resume is a first-class entry | AC-3 | one Coordinator fixture is an existing-task resume path |
| P10 | Capability honesty and bounded adjacency | AC-1, AC-4–AC-6 | live/installed/declared states and ineligible architectures stay explicit |

## 4. Affected Files and Value-Bearing Accounting

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `.tfw/conventions.md` heading `Tool Adapter Pattern` | MODIFY | `VALUE` | own the universal entry sequence and evidence-claim boundary without owning workflow algorithms |
| `.tfw/adapters/README.md` | MODIFY | `VALUE` | expose the four-adapter entry contract and declared/installed/live distinction |
| `.tfw/adapters/codex/README.md` | MODIFY | `VALUE` | document the thin baseline, live smoke/eval boundary, and conditional strengthening rule |
| `.tfw/adapters/codex/skills/tfw-*/SKILL.md` (exact 11 manifest commands) | MODIFY iff AC-4 selects strengthened | `VALUE` | source entry contracts gain only the tested pre-action boundary; no workflow logic |
| `.agents/skills/tfw-*/SKILL.md` (same exact 11) | MODIFY iff AC-4 selects strengthened | `VALUE` | installed active copies remain byte-exact with their sources |
| `docs/scripts/command_entry_eval.py` | CREATE | `ASSURANCE` | reproducible explicit live trial runner, graders, statistics, budgets, and evidence writer |
| `docs/scripts/test_command_entry_eval.py` | CREATE | `ASSURANCE` | offline fake-runner, fixture, grader, mutant, budget, redaction, and summary tests |
| `docs/scripts/test_runtime_context.py` | MODIFY | `ASSURANCE` | source-derived entry sequence/evidence-level projection and independent negative mutations |
| `docs/scripts/test_integration.py` | MODIFY | `ASSURANCE` | exact 11×4 manifest/receiver/Role-Lock/skill-contract parity and clean-receiver gates |
| `workspace/2026/TFW_20260905-124029_RTPSN/phase-a/evidence/**` | CREATE | `TRACE` | raw live trials, summary, counts, test output, and required EV |
| `workspace/2026/TFW_20260905-124029_RTPSN/phase-a/{ONB,RF}__phase-a__command_entry_reliability.md` | CREATE | `TRACE` | Executor understanding and cumulative result trace |
| task/phase `status.md` and `journal/**` | MODIFY / CREATE | `TRACE` | authoritative lifecycle and immutable events |

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | `.tfw/conventions.md`; `.tfw/adapters/README.md`; `.tfw/adapters/codex/README.md`; and, only if AC-4 selects strengthened, the exact 11 paths under each of `.tfw/adapters/codex/skills/tfw-*/SKILL.md` and `.agents/skills/tfw-*/SKILL.md` resolved from `.tfw/adapters/manifest.yaml` |
| Baseline / selector source | `7bc0f30736ff1456c5d9dd74286a4e3a94c63361`; this TS at its owner-approval commit |
| Candidate rule | First tested Executor commit with required VALUE+ASSURANCE, before EV/RF/REVIEW/final transition; excluded-only later writes do not move it; later VALUE requires a new Candidate and recomputation |
| Logical VALUE files | 25 planned maximum: 3 unconditional + 22 conditional; rename = one |
| Touched text LOC | 500 additions + 300 deletions = 800 planned maximum; numeric numstat fields; binary/non-text = per-file N/A |
| Triggers / disposition | Configured soft prompts: 50 VALUE files or 5,000 touched text LOC. Record cause, cost, assurance, split, authority, terminal verdict, and pre-work ref before any growth. The conditional branch does not ratchet the plan. |
| Multiplier / authority | Immutable denominators 25 files / 800 LOC; Coordinator may add only necessary constituents below 50 files and 1,600 LOC while all protected boundaries remain fixed; owner rules at/above either multiplier boundary or from planned zero |
| Approval epoch / failure | Prospective owner approval of this TS; missing/mutable/mismatched/late baseline or Candidate = BLOCKED; metric-only inapplicability = N/A; unresolved phase attribution = INVALID; DEFERRED is non-terminal |

```powershell
$valuePaths = @(
  '.tfw/conventions.md',
  '.tfw/adapters/README.md',
  '.tfw/adapters/codex/README.md',
  '.tfw/adapters/codex/skills/tfw-*/SKILL.md',
  '.agents/skills/tfw-*/SKILL.md'
)
$candidateSha = git rev-parse HEAD # run while the immutable Candidate is checked out, before TRACE-only writes
git diff --name-status --find-renames=50% -z 7bc0f30736ff1456c5d9dd74286a4e3a94c63361 $candidateSha -- $valuePaths
git diff --numstat --find-renames=50% -z 7bc0f30736ff1456c5d9dd74286a4e3a94c63361 $candidateSha -- $valuePaths
```

### Prospective scope rulings

1. **Current baseline wins or result is inconclusive:** change only the three unconditional VALUE files; production skills remain byte-identical to baseline.
2. **Strengthened proxy clears AC-4:** the exact 22 conditional VALUE paths enter Candidate together; partial command coverage is forbidden.
3. **Direct/full-copy materially wins:** make no production receiver edit, mark production selection `BLOCKED`, preserve evidence, and return to the Coordinator for a new TS covering generation, portability, and migration.
4. **No new VALUE path** may be added merely to store measurements or prose: use phase evidence (`TRACE`) or the existing two assurance test surfaces.

### Task-local hard constraints (when material)

No additional M1–M6 hard constraint is declared. The Phase B and architecture-migration boundaries are enforced as scope, conditional Candidate rules, and Definitions of Failure rather than as an artificial pre-act limit.

**Actions (not budget dimensions):** VALUE = 3 unconditional MODIFY + 22 conditional MODIFY; ASSURANCE = 2 CREATE + 2 MODIFY; TRACE = phase evidence/lifecycle/ONB/RF writes.
**Immutable owner-approved denominator:** 25 VALUE files and 800 touched text LOC; never ratchets.

## 5. Acceptance Criteria

Each AC is independently verifiable. Synthetic gates never substitute for live evidence, and live evidence never grants authority to change the TS.

### AC-1: Reproducible census and causal boundary

The phase reproduces the entry topology and names the strongest claim supported at every boundary.

- [ ] Enumerate the exact 11 manifest commands and four adapters; for every route record canonical source, role, declared target, source presence, tracked-copy presence/parity, installed state, clean-receiver result, and live-host observation separately.
- [ ] Compare `7bc0f30736ff1456c5d9dd74286a4e3a94c63361`, pre-change `db757a5910187e17fec4af86cd4faebd8c312942`, RCFR change `aa0466b74295d53abcfb9c4a0fb0e3c134fa37a2`, and the final Candidate for entry wording, runtime read words/estimated tokens, canonical authority count, copied receiver count, and observed behavior.
- [ ] Preserve the research classification: CRATM = uncovered path; RTPSN = post-load noncompliance; H3 refuted as stated; H4 inconclusive before this phase's trial.
- [ ] Report source presence → receiver parity → invocation → complete load → later conformance → controlled comparative effect as six non-substitutable levels.
- [ ] State untested live hosts and absent installed receivers without promoting clean-receiver success to live behavior.

Gate: `python -m pytest docs/scripts/test_integration.py docs/scripts/test_runtime_context.py docs/scripts/test_command_entry_eval.py -q` plus a baseline census generated from the immutable SHAs.

Evidence: Full — `evidence/command-entry-topology.txt` records commands, adapters, revisions, receiver states, counts, and incident classifications; deliberate source/parity/role/load/conformance mutants fail at their own level.

### AC-2: Safe and independently tested live-evaluation harness

The harness is an explicit assurance tool, not a runtime input, and its graders observe behavior rather than candidate wording.

- [ ] Materialize one disposable Git fixture per run with the same root instructions, canonical workflows, task traces, and non-arm files; hash every graded input.
- [ ] Implement three arm builders: exact current proxy; research-defined strengthened proxy with only pre-action/load/order/Role-Lock/stop language; schema-valid direct prototype derived from the same canonical workflow in the temporary receiver.
- [ ] Keep byte-identical full-copy receivers in the structural/context comparison without double-counting their canonical body as a fourth Codex live arm.
- [ ] Invoke Codex with `--ephemeral`, `--ignore-user-config`, fixture-limited `workspace-write`, JSONL output, explicit `gpt-5.6-sol`, and `medium` reasoning; never print auth material or inherited secrets.
- [ ] Grade tool/event traces and final Git diff for invocation, complete canonical load, Read Contract order, permitted/forbidden artifact effects, gate/stop, and final route. Model self-report is not evidence.
- [ ] Enforce total-run, valid-denominator, token, time, timeout, invalid-run retention, and redaction rules before a live call starts.
- [ ] Unit tests use a fake runner and independently constructed traces; at least one mutant per grader, arm, budget, and summary family changes output before rejection.

Gate: `python -m pytest docs/scripts/test_command_entry_eval.py -q`; `python docs/scripts/command_entry_eval.py --help`; a `--dry-run` emits the exact 54-run schedule without network/model execution or fixture residue.

Evidence: Full — unit-test output plus the dry-run schedule and input hashes are stored in `evidence/test-output.txt` and `evidence/command-entry-summary.json`.

### AC-3: Fixed cross-role behavioural trial

The approved matrix completes before any production skill edit.

- [ ] Run exactly six fixtures × three arms × three repetitions = 54 valid runs, interleaved deterministically by fixture, repetition, and arm.
- [ ] Fixtures are: Coordinator new-task question/approval stop; Coordinator existing-task resume; Coordinator ambiguous/uncertain task hard stop; Researcher first-stage write/STOP; Executor approved-TS ONB/WAIT with no implementation; Reviewer RF Map/STOP with no verdict.
- [ ] Each fixture declares allowed reads/writes, forbidden paths/artifacts, required gate/stop, and final route before execution; the same expectation is used for all arms.
- [ ] A run's aggregate adherence is pass only when every applicable independent grader passes; publish every boundary rate, aggregate rate, role rate, and failure trace.
- [ ] Publish per-arm proportions with 95% Wilson intervals and pairwise Newcombe difference intervals; do not infer a smaller effect from an interval that includes zero.
- [ ] Record actual input/output tokens and elapsed time when emitted by the CLI. If a field is unavailable, retain raw output and mark only that metric `N/A`; use separately labelled word-based estimates.
- [ ] Stop at 750,000 reported total tokens or 180 minutes. If either ceiling arrives before 54 valid runs, the AC is `BLOCKED`; no partial denominator or substituted run is accepted.

Gate: `python docs/scripts/command_entry_eval.py run --model gpt-5.6-sol --reasoning medium --repetitions 3 --max-runs 54 --max-tokens 750000 --max-minutes 180 --output workspace/2026/TFW_20260905-124029_RTPSN/phase-a/evidence/command-entry-trials.jsonl` followed by the independent summary/check command over the raw JSONL.

Evidence: Full — `evidence/command-entry-trials.jsonl` and `evidence/command-entry-summary.json`; each summary claim resolves to run IDs and raw events.

### AC-4: One predeclared production decision [depends: AC-1, AC-2, AC-3]

The decision rule is applied once and cannot be relaxed after results are visible.

- [ ] Current proxy remains production unless a challenger improves aggregate adherence by at least 10 percentage points, its 95% difference interval excludes zero, and no role loses more than 5 points.
- [ ] The strengthened proxy is deployable only if it meets the behavioural rule, adds no more than 15 words/~20 estimated tokens to any skill route, adds no runtime preload or algorithm statement, and all AC-5/AC-6 gates pass.
- [ ] On strengthened selection, all exact 11 source skills and all exact 11 installed copies change in one Candidate; every pair is byte-identical and every command keeps its manifest role and canonical workflow.
- [ ] A direct or full-copy material win is recorded but not deployed. Production selection becomes `BLOCKED` and returns to Coordinator for a new approved TS; no generated/copy topology is invented by the Executor.
- [ ] Inconclusive, tied, mixed-role, missing-telemetry, or below-threshold evidence is reported as such and retains the current baseline without a superiority claim.
- [ ] RF records the rule inputs and exactly one result: `BASELINE RETAINED`, `STRENGTHENED SELECTED`, or `BLOCKED — NEW TS REQUIRED`.

Gate: independent recomputation from raw JSONL plus a decision-function unit test covering every terminal branch and threshold edge.

Evidence: Full — the decision object in `evidence/command-entry-summary.json` names rates, intervals, role deltas, context cost, test state, and selected terminal result.

### AC-5: Universal entry contract without a second algorithm [depends: AC-4]

The framework describes and tests one satisfiable pre-action sequence for every command/adapter class.

- [ ] `conventions.md` Tool Adapter Pattern owns this sequence: discover the command receiver; reach the canonical workflow; bind its declared Role Lock before task action; execute its Read Contract in order; obey its gates/stops; name the next `/tfw-*` route.
- [ ] Full-copy adapter receivers satisfy the sequence by beginning with byte-identical canonical workflow content. Codex skills remain thin routers and name complete canonical load; neither form introduces adapter-specific workflow logic.
- [ ] Adapter documentation distinguishes source, parity, invocation, load, conformance, and comparative evidence, and states that a higher level cannot be inferred from a lower one.
- [ ] Manifest remains tooling-only copy/check metadata; no runtime role reads it for authority and no route/role changes.
- [ ] Static tests reject a missing workflow route, incomplete-load instruction, missing/competing Role Lock, reordered ownership, injected common preload, missing stop, source/copy drift, and a generated evidence read.
- [ ] No canonical workflow, persistent root rule, session-title instruction, or Phase B naming grammar changes under this AC.

Gate: targeted mutant tests in `docs/scripts/test_runtime_context.py` and `docs/scripts/test_integration.py`, plus exact `git diff --name-only` scope check.

Evidence: Full — source-derived contract projection and mutant results in `evidence/test-output.txt`; live evidence remains separately referenced from AC-3.

### AC-6: Exact topology, context, and regression proof [depends: AC-5]

The selected Candidate preserves the current command system and measures every modified active entry.

- [ ] Manifest still resolves exactly 11 commands, four adapters, one role and one canonical workflow per command, with no extra/missing route.
- [ ] Installed current-repository copies match their source; four empty receivers get their exact declared roots and 11-command role set; absent Cursor/plural Antigravity remain labelled clean-fixture-only, not live.
- [ ] Before/after word and estimated token counts cover every modified source and active installed copy, include proxy-plus-canonical double reads, and use the same whitespace/`ceil(words × 4/3)` method.
- [ ] Full-copy, current, strengthened, and direct designs receive separate runtime-context, distribution/drift, portability, maintenance, observability, and behavioural-evidence rows.
- [ ] Existing runtime-context and semantic projections remain green; no modified proxy increases authority count or changes task effects.
- [ ] Targeted and full repository tests, project trace checks, NUL-safe VALUE accounting, and candidate-scope checks pass from the immutable Candidate.

Gate: `python -m pytest docs/scripts/test_command_entry_eval.py docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q`; `python -m pytest .tfw/scripts/ docs/scripts/ -q`; `python .tfw/scripts/gen_index.py --check project`; exact manifest clean-receiver and source/copy commands; TS accounting commands against Candidate SHA.

Evidence: Full — `evidence/command-entry-counts.txt` and `evidence/test-output.txt` contain raw commands/output; EV points to the immutable Baseline and Candidate.

### AC-7: Claim-bounded evidence package [depends: AC-1, AC-3, AC-4, AC-6]

The result can be reviewed without reconstructing the planning conversation.

- [ ] EV has at least one row per AC and distinguishes `VERIFIED`, `BLOCKED`, `DEFERRED`, and justified `N/A` exactly as the evidence template requires.
- [ ] Every statement of causality, advantage, runtime behavior, context cost, or adapter availability cites its evidence level, revision, host, model/effort when relevant, and known limit.
- [ ] RF states H3 remains refuted, H4's new status follows only the fixed trial, and baseline retention is not called architectural superiority.
- [ ] Raw JSONL, topology, counts, summary, tests, and Candidate refs resolve inside the phase evidence folder; no generated artifact is read by a workflow or skill.
- [ ] Phase B naming grammar and owner verdict A1 remain untouched; rejected A2 is not revived; CRATM authority remains outside RTPSN.

Gate: evidence-link audit, generated-input census, phase diff review, and independent recomputation of every RF numeric/quoted claim immediately before RF.

Evidence: Full — the complete phase evidence set below and immutable Candidate SHA.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-a__command_entry_reliability.md` | required structured per-AC evidence and verdict |
| `evidence/command-entry-topology.txt` | immutable revision, 11×4 source/receiver/live census, incident classification |
| `evidence/command-entry-trials.jsonl` | raw 54-run schedule, events, diffs, grader results, usage, timing, and retained invalid attempts |
| `evidence/command-entry-summary.json` | independently reproducible rates, intervals, role deltas, context costs, and decision object |
| `evidence/command-entry-counts.txt` | before/after words, estimated tokens, VALUE name-status/numstat, authority/copy counts |
| `evidence/test-output.txt` | dry run, targeted/full tests, mutant checks, project check, parity and clean-receiver output |

## 6. Technical Guidance

- Treat Iteration 1 RES D1–D8, Extract E1–E6, Challenge C3–C6, and the exact 151-word plan specimen as evidence and reference design. The ACs above govern implementation.
- Extend the existing `SourceTree`, manifest, clean-receiver, role-census, and runtime-context helpers where they remain the natural owner; do not fork parallel truth tables.
- Keep live execution behind an explicit `run` subcommand. Test collection and default pytest must perform no network/model calls.
- Derive command names, workflow paths, and roles from the manifest for fixture generation, but grade runtime authority against canonical workflow contents and Role Locks, not against manifest prose.
- Store full raw CLI JSONL in phase evidence; redact only credential-bearing environment fields and record the redaction schema. Never request or serialize plain-text secrets.
- Build Wilson/Newcombe calculations with standard-library math or an already-declared dependency; do not add a package solely for confidence intervals.
- Use disposable directories created by the platform temp API, verify their resolved path before cleanup, and never delete the workspace/task root.
- If the strengthened arm wins, apply one consistent contract skeleton while retaining command-specific permitted/forbidden artifacts and template gates. The proxy must remain a router, not a summarized workflow.
- Use `git status` whole and `git commit --only` with the explicit Phase-A path list; never stage broad unrelated changes.

## 7. Definition of Failure

- ❌ RCFR or proxy thinning is named as the cause of CRATM/RTPSN, or the two incidents are presented as non-invocation/non-load evidence.
- ❌ Static text, parity, clean-receiver installation, or a successful title is presented as behavioural compliance or comparative effect.
- ❌ The live denominator is reduced below 54 valid runs, altered after outcomes appear, or completed after the token/time ceiling without a `BLOCKED` result.
- ❌ A grader relies on model self-report, candidate-specific wording, generated expected output, or a sandbox that makes forbidden writes unobservable.
- ❌ A challenger is called materially better without the aggregate, interval, and per-role thresholds; an inconclusive result is converted into a winner.
- ❌ Strengthened skills ship without AC-4 qualification, partial 11-command synchronization ships, or any route gains more than the bounded context cost.
- ❌ Full-copy/direct architecture, a new generator/symlink topology, or a second algorithm ships under this TS.
- ❌ A proxy duplicates workflow steps, templates, gates, or role logic; a manifest or generated report becomes runtime authority.
- ❌ Any canonical workflow, manifest route/role, persistent root preload, or Phase B naming/session-title behavior changes.
- ❌ Clean-receiver evidence is described as a live Cursor/Antigravity/Claude observation, or missing telemetry is estimated and relabelled actual.
- ❌ Evidence omits raw run IDs/revisions, cannot reproduce a numeric claim, leaks secrets, or becomes an input to runtime roles.
- ❌ The phase modifies CRATM roles, delegation, channels, worktrees, session ownership, or coordinator-of-coordinators semantics.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| sample is too small to resolve a 10-point effect | fixed intervals and baseline-default rule; inconclusive is a valid result, not permission to guess |
| live CLI output schema changes | capture version/raw JSONL; parser fails closed and fake-schema mutants cover missing fields |
| runs consume more usage/time than expected | pre-act cumulative ceiling, per-run timeout, retained invalid attempts, `BLOCKED` rather than denominator shrinkage |
| fixture task content leaks an arm cue | identical hashed non-arm fixture and prompt; arm label excluded from the model-visible task |
| direct arm is not portable or maintainable | evidence-only eligibility; new approved TS required for any production design |
| strengthened wording improves entry salience but not later obedience | grade R2/R3/R4 and aggregate separately; deployment requires the full conformance threshold |
| existing tests encode current words rather than semantics | source-derived projection plus deliberate mutants; no candidate-generated expected oracle |
| conditional skill edits complicate VALUE accounting | immutable maximum selector/count and one all-or-none 22-file branch |
| shared Git index includes neighbouring work | explicit paths, full status before commit, `git commit --only`, inspect committed diff afterward |

## 9. Cross-Phase Modifications (multi-phase only)

| File | Also modified in | Coordination note |
|---|---|---|
| `.tfw/conventions.md` Tool Adapter Pattern | Phase B may consume it | Phase B must preserve the evidence ladder and single-algorithm boundary while adding no title authority here. |
| `.tfw/adapters/README.md`, `.tfw/adapters/codex/README.md` | Phase B adapter documentation | Extend the same adapter claims; do not overwrite Phase-A measured limits. |
| `.tfw/adapters/codex/skills/tfw-*/SKILL.md`, `.agents/skills/tfw-*/SKILL.md` | Phase B only if its canonical workflow route requires copy sync | Preserve the Phase-A selected entry form; naming logic belongs in workflows, not skills. |
| `docs/scripts/command_entry_eval.py`, `docs/scripts/test_command_entry_eval.py` | Phase B may add naming acceptance fixtures | Keep Phase-A raw runs immutable and create a separate Phase-B evidence run/output. |
| `docs/scripts/test_runtime_context.py`, `docs/scripts/test_integration.py` | Phase B regression surface | Extend the existing source-derived manifest/read graph; no parallel test authority. |

---

*TS — TFW_20260905-124029_RTPSN / Phase A: Command Entry Reliability | 2026-09-05*
