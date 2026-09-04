# TS — TFW_20260902-175227_RCFR / Phase B: Primary Role Paths

> **Date**: 2026-09-04
> **Author**: Codex (Coordinator)
> **Status**: ✅ APPROVED — saubakirov, 2026-09-04; autonomous execution authorized through the Phase B Coordinator task
> **Parent HL**: [Phase B derivation](HL__phase-b__primary_role_paths.md)
> **Master HL**: [Runtime Context Footprint Reduction](../HL-TFW_20260902-175227_RCFR.md)
> **Predecessor**: [Phase A RF](../phase-a/RF__phase-a__common_authority_and_context_topology.md) · [Phase A REVIEW rev4](../phase-a/REVIEW__phase-a__common_authority_and_context_topology__rev4.md)
> **Research**: [Iteration 2 RES](../research/iter2/RES.md) · [R15–R18, R21–R23, R35–R39](../research/iter2/3_extract.md)

---

## 1. Objective

Deliver a single-pass authoritative read route for Coordinator, Researcher, Executor, and
Reviewer. Each fixed role path must fall at least 30% from the Phase B entry baseline while every
frozen decision, refusal, artifact effect, citation duty, gate, authority boundary, and hard stop
remains observable and adapter copies remain synchronized.

## 2. Scope

### In Scope

- Make the four repository-local role skills minimal bootstrap routers; none may require a second
  full preload over the canonical workflow.
- Give each primary workflow one ordered, checkpoint-specific Read Contract with task-local state
  first, exact task authority next, and shared/history/knowledge inputs only when triggered.
- Remove workflow prose that duplicates a form already owned by a template or a rule already owned
  by an addressed convention section, while retaining deliberate inline enforcement.
- Extend Phase A's runtime audit and source-derived semantic oracle to all four primary role paths,
  both research modes, revision return, and independent review judgments.
- Synchronize every changed canonical workflow and skill through the existing manifest topology and
  prove supported adapters in empty receivers.

### Out of Scope

- `/tfw-docs`, `/tfw-knowledge`, `/tfw-resume`, `/tfw-release`, `/tfw-update`, `/tfw-config`, and
  `/tfw-init` compression; Phase C owns those paths.
- Master HL amendments, new research, task-artifact shortening, historical rewrites, book/essay/site
  edits, release/version work, minification, or byte-size optimization.
- Any change under `tasks/`, including `TFW-36`, or repair of the immutable RDP `123>120` diagnostic.
- New runtime manifests, generated role packets, persistent fields, configuration keys, or adapter
  roots in this repository merely to make the metric smaller.

## 3. Principles Check

| # | Principle (master HL §7) | Enforced by | Gate |
|---|---|---|---|
| P1 | Context is a finite working resource | AC-1, AC-6 | fixed exposure and every repeat are measured |
| P2 | One concept, one authority, one read | AC-1–AC-5 | skill routes once; workflow owns algorithm; template owns form |
| P3 | Task facts before framework history | AC-1–AC-4 | status/journal are the first selected local inputs |
| P4 | Progressive disclosure without semantic loss | AC-2–AC-6 | triggered reads plus source-derived equivalence |
| P5 | Subtraction before addition or relocation | AC-5, AC-6 | no new runtime file/key; net runtime prose decreases |
| P6 | Meaning fixed, representation open | AC-2–AC-4, AC-6 | role semantic records and mutants gate every path |
| P7 | Algorithms in steps, forms in templates, terms in glossary | AC-2–AC-4 | owner classification and duplicate checks |
| P8 | History remains discoverable, not resident | AC-1, AC-6 | compatibility lookups are triggered and resolvable |
| P9 | Measurements resist gaming | AC-1, AC-6 | immutable baseline, transitive edges, symmetric exclusions |
| P10 | The framework must pass its own path | AC-5, AC-6 | self-hosted and empty-receiver verification |

## 4. Affected Files

| File | Action | Description |
|---|---|---|
| `.tfw/workflows/plan.md` | MODIFY | minimal Coordinator checkpoints; preserve approval/freeze/amendment/research/Pre-TS/revision gates |
| `.tfw/workflows/research/base.md` | MODIFY | ordered Researcher reads and stage/resume/synthesis stops |
| `.tfw/workflows/handoff.md` | MODIFY | ordered Executor reads and onboarding/execution/evidence/RF/return stops |
| `.tfw/workflows/review.md` | MODIFY | stage-local Reviewer reads and independent PV/Purpose/citation/disposition/verdict routing |
| `.tfw/adapters/codex/skills/tfw-{plan,research,handoff,review}/SKILL.md` | MODIFY | source skills become minimal command/role/workflow routers |
| `.agents/skills/tfw-{plan,research,handoff,review}/SKILL.md` | MODIFY | exact installed copies of the four source skills |
| `.claude/commands/tfw-{plan,research,handoff,review}.md` | MODIFY | exact copies of changed canonical workflows |
| `.agent/workflows/tfw-{plan,research,handoff,review}.md` | MODIFY | exact legacy installed copies retained by this repository |
| `docs/scripts/test_runtime_context.py` | MODIFY | immutable Phase B baseline plus four-role read/semantic/mutant audit |
| `docs/scripts/test_integration.py` | MODIFY | manifest, installed-copy, exact role/path, and clean-receiver regression checks |
| `.tfw/adapters/manifest.yaml` | MODIFY | keep the exact four-primary-route source/role/copy contract mechanically consumable; no runtime authority |

**Budget:** 0 new runtime files, at most 23 modified implementation/test files, at most 3,500
changed LOC. Phase artifacts, ONB/RF/REVIEW, journals, and up to five evidence files remain within
the project limits of 50 files / 50 new / 5,000 LOC / 50 modified. No override is authorized.

## 5. Acceptance Criteria

### AC-1: Reproducible four-role baseline and read graph

The audit must resolve actual clean-master behavior from immutable commit
`80382fbffd52b1f13cb3b38e8e450ecc0fef2fd5`, including root, skill, workflow, template, addressed
section, PV, Purpose Check, transitive, and separately instructed repeated reads.

- [ ] It reproduces: Coordinator 50,851; Researcher focused 29,992; Researcher deep 30,057;
  Executor 55,885; Reviewer 74,537 fixed words.
- [ ] It classifies every edge by checkpoint purpose and authority, shows dynamic task/P5–P7 reads
  without charging either side, and rejects an unclassified full `conventions.md`, `glossary.md`, or
  `KNOWLEDGE.md` edge.
- [ ] Missing/duplicate addressed headings, omitted routes, and an injected duplicate skill/workflow
  preload fail independently of the generated report.

Gate: targeted runtime-audit tests plus CLI output generated against the immutable baseline and
candidate working tree.

Evidence: Environment: clean Git baseline and Phase B worktree. Action: resolve and count all five
primary variants with the same `\S+` implementation. Observable success: exact entry counts, complete
edge classifications, and the three injected failures are rejected.

### AC-2: Minimal Coordinator and Researcher paths [depends: AC-1]

Coordinator and Researcher must read each authority once at the checkpoint that needs it without
changing their decisions or stops.

- [ ] `/tfw-plan` preserves Knowledge Gate arithmetic, P0–P4 scanning, owner/title identity,
  HL approval and freeze, amendment classification/verdicts, hypothesis/research decisions,
  iteration minimum, Pre-TS dependency proof, budget/evidence requirements, post-review order, and
  the Coordinator hard stop.
- [ ] `/tfw-research` preserves iteration/resume detection, predecessor context, mode selection,
  stage templates and OODA checkpoints, external/counter-evidence rules, classified HL
  recommendations, RES completeness, and the Researcher hard stop.
- [ ] Their skills perform command recognition, Role Lock, canonical workflow routing, required
  template/evidence obligations, and final routing only; they do not load `AGENTS.md` or the three
  full common libraries again.

Gate: source-derived P1–P4 and R1–R3 semantic records, one deliberate Coordinator mutant and one
Researcher mutant, plus read-manifest assertions for both research modes.

Evidence: Environment: isolated role fixtures. Action: run new-task, later-phase, research-required,
research-sufficient, and returned-REVISE decisions. Observable success: baseline/candidate records
match on decision, refusal, artifact effects, citations, and gate while candidate reads contain no
duplicate full preload.

### AC-3: Minimal Executor path [depends: AC-1]

Executor must receive one governing order and retain every onboarding, execution, evidence, RF, and
stop condition.

- [ ] Initial and REVISE paths select status/journal, master and phase derivation, highest TS lineage,
  prior REVIEW only on return, referenced files, and relevant implementation files without rereading
  unchanged common/task authority.
- [ ] Blocking ONB questions stop execution; answered/non-blocking onboarding, attributed commit,
  state/event handoff, AC dependency order, test/build failure, evidence statuses/artifacts, Pre-RF
  template gate, mandatory RF sections, RF transition, and Executor hard stop retain meaning.
- [ ] The skill remains an Executor lock/router and does not repeat the canonical read list.

Gate: E1–E4 source-derived records, initial/REVISE read manifests, unsupported-VERIFIED and
build-failure mutants, and artifact/state assertions.

Evidence: Environment: isolated initial and revision fixtures. Action: exercise unresolved ONB,
dependent AC, failed build, evidence collection, RF creation, and highest-revision return. Observable
success: identical baseline/candidate decisions and effects with no unchanged authority reread.

### AC-4: Minimal independent Reviewer path [depends: AC-1]

Reviewer must remain independent and preserve stage cognition and acceptance authority boundaries.

- [ ] Bootstrap reads state and governing artifacts once; Map reads mapping inputs; Verify reads
  files/evidence and independently scans P0–P4; Judge deliberately rereads the contract baseline and
  Project North Star for Purpose Check; Decide reads stage outputs and routing rules.
- [ ] Verification ratio/escalation, Claim & Source checks, evidence audit, semantic citation audit,
  ten-row Judge, Purpose Check outcomes, citation bar, three-rung route, reviewer-proposed versus
  Coordinator-ruled dispositions, APPROVE/REVISE/REJECT transitions, KNW routing, and Reviewer hard
  stop retain meaning.
- [ ] The review skill does not preload common libraries and cannot collapse the two deliberate
  independent PV/Purpose reads.

Gate: V1–V4 and C1 source-derived records, 42%/100% verification scenarios, purpose/citation/rung
mutants, and read-manifest assertions naming every deliberate repeat.

Evidence: Environment: separate Reviewer fixture with no Executor session history. Action: review a
green RF, a discrepancy, a purpose failure, a citation-less proposed revision, and a rung-2 item.
Observable success: identical verdict/routing/effects and independent citations; each mutant fails.

### AC-5: Adapter and copy parity [depends: AC-2, AC-3, AC-4]

Every changed primary route must propagate through the existing tooling-only manifest without
creating another runtime authority.

- [ ] Four canonical workflows equal their tracked Claude and legacy Antigravity copies byte for
  byte; four Codex source skills equal their installed copies byte for byte.
- [ ] The manifest still resolves exact route, canonical source, role, destination, and copy strategy
  for Coordinator, Researcher, Executor, and Reviewer and remains unread by runtime roles.
- [ ] Empty receivers expose all 11 commands at each supported vendor's documented path, with the
  four primary roles exact; installing twice is a no-op and one altered managed copy is repaired
  without touching unrelated content.
- [ ] Existing persistent roots remain compact routers and do not regain a common preload.

Gate: integration exact-set/role/path checks, byte comparisons, clean-receiver install/update replay,
and a missing-command/wrong-role mutation.

Evidence: Environment: repository plus four empty temporary receivers. Action: install and re-run the
manifest mapping, mutate one managed copy, and enumerate paths/roles. Observable success: exact
parity, idempotence, repair, and preservation of unrelated content.

### AC-6: Semantic preservation, reduction, and regression gate [depends: AC-2, AC-3, AC-4, AC-5]

All primary role paths must pass the Phase A independent oracle and reduce fixed words by at least
30% individually, with no checkpoint regression.

- [ ] P1–P4, R1–R3, E1–E4, V1–V4, C1–C3, and A1 derive every produced field from baseline and
  candidate sources before comparison with independent expected records; expected data cannot feed
  production.
- [ ] Baseline and candidate match on `{decision, refusal, artifact effects, citations, gate}`; at
  least one deliberate mutant per P/R/E/V/C/A family changes produced output before rejection.
- [ ] Each of Coordinator, Researcher focused, Researcher deep, Executor, and Reviewer is at least
  30% below AC-1; the combined five-path trajectory is at least 30% below 241,322 words.
- [ ] Reduction comes from deleted duplication, selective reads, and simpler ownership—not omitted
  mandatory inputs, minification, relocation, or generated formatting.
- [ ] Configured full tests and project checks pass. The immutable RDP journal diagnostic is reported
  separately; `TFW-36` is neither created nor modified.

Gate: `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q`,
`python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only`,
`python -m pytest .tfw/scripts/ docs/scripts/ -q`, and
`python .tfw/scripts/gen_index.py --check project`; `--check tasks` is a diagnostic with the known
immutable RDP exception.

Evidence: Environment: Phase B candidate, immutable baseline, and clean receivers. Action: record raw
role audit, semantic/mutant results, adapter replay, full tests, project/task diagnostics, and diff
budget. Observable success: all semantic and structural gates pass, every path clears 30%, no hidden
regression or unauthorized file change exists.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-b__primary_role_paths.md` | required structured per-AC evidence and verdict |
| `evidence/runtime-context-primary-roles.txt` | raw baseline/candidate edge and word audit |
| `evidence/semantic-primary-roles.txt` | source-derived records and rejected mutants |
| `evidence/clean-receiver-primary-routes.txt` | adapter command/role/path/idempotence replay |
| `evidence/verification-primary-roles.txt` | targeted/full tests, project checks, diagnostics, and scope counters |

## 6. Technical Guidance

- Use Phase A's `docs/scripts/test_runtime_context.py` and `docs/scripts/test_integration.py` as the
  single proof surfaces; do not create parallel audit or oracle modules.
- R15–R18 and R21–R23 in research iteration 2 are the design reference. Their candidate numbers are
  conservative forecasts; AC-1 and the observed result govern.
- Keep role algorithms in workflows, form/schema in existing templates, and shared invariants at
  unique convention headings. A short skill may repeat only enforcement required before its
  workflow can be opened.
- Preserve source-derived oracle independence established by Phase A revision 6/8. Wording may vary;
  decisions, refusals, effects, citations, and gates may not.
- The repository is self-hosting only for selected adapters. Empty receivers and the manifest decide
  portability; absent `.cursor/commands` or plural `.agents/workflows` in this checkout is not by
  itself a defect.

## 7. Definition of Failure

- ❌ Any primary path misses 30%, hides a repeated/transitive edge, or omits a required dynamic read
  from the manifest to improve the count.
- ❌ A skill and workflow both own the same preload or algorithm, or a generated audit/manifest
  becomes a role instruction source.
- ❌ Any approval, freeze, amendment, iteration, research, onboarding, execution, evidence, RF,
  independent review, Purpose Check, citation-bar, disposition, verdict-routing, or hard-stop
  behavior changes.
- ❌ Reviewer independence is weakened by reusing Executor conclusions or by collapsing the
  deliberate PV/Purpose reads.
- ❌ A changed canonical workflow or skill is not synchronized to every tracked/receiver adapter
  surface in the same phase.
- ❌ Templates, secondary workflows, master frozen claims, `tasks/`, `TFW-36`, the RDP journal,
  runtime state/schema, or configuration keys change without a Coordinator-issued TS revision.
- ❌ Tests pass only because expected oracle data feeds production, mutants do not change produced
  records, or self-hosting files substitute for a clean receiver.
- ❌ Scope exceeds 23 modified implementation/test files, 3,500 changed LOC, or any project budget.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| thin skills lose a command-level guard | assert role, workflow, template/evidence duties, and hard stop before copy sync |
| workflow compression deletes the only edge-case carrier | require a source-derived fixture or retain the local enforcement clause |
| audit counts selected config/PV ranges inconsistently | one immutable baseline, one word function, explicit repeated edges |
| Reviewer savings come from lost independence | verify isolated review scenarios and name deliberate rereads in the manifest |
| canonical and adapter copies drift during repair | byte-compare every changed installed copy and clean-install all vendors |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| `.tfw/workflows/plan.md` | Phase A | preserve Phase A Knowledge Gate and unique-heading contract |
| `.tfw/adapters/manifest.yaml` | Phases A and C | remains tooling metadata; no role may read it as authority |
| `docs/scripts/test_runtime_context.py`, `docs/scripts/test_integration.py` | Phases A and C | extend the same oracle/audit; preserve Phase A cases |
| primary workflow copies | Phase C adapter verification | later sync must retain Phase B byte/role parity |

---

*TS — TFW_20260902-175227_RCFR / Phase B: Primary Role Paths | 2026-09-04*
