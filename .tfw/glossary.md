# TFW Glossary

Terms route to their one normative owner. Procedures, field schemas, refusal algorithms,
and incident histories live at the linked authority or durable history source.

## Execution Modes

### CL (Chat Loop Mode)
**Meaning:** The default mode in which AI proposes and the human performs or approves external actions. **Authority:** [conventions.md](conventions.md#7-execution-modes), `CL (Chat Loop)`.

### AG (Autonomous Mode)
**Meaning:** Explicitly authorized execution within a bounded approved scope, with safe failure on missing context. **Authority:** [conventions.md](conventions.md#7-execution-modes), `AG (Autonomous)`.

### AT (Agent Team)
**Meaning:** Provider-neutral team execution mode. **Authority:** [conventions.md](conventions.md#at-agent-team--explicit-declaration-only), `AT (Agent Team)`.

## Artifact Types

### HL (High Level)
**Meaning:** The task's meaning, outcome, boundaries, and approved contract baseline. **Authority:** [conventions.md](conventions.md#hl-high-level), `HL (High Level)`, and `.tfw/templates/HL.md`.

### RES (Research Report)
**Meaning:** The cumulative structured investigation record produced by the Researcher. **Authority:** [conventions.md](conventions.md#res-research-report), `RES (Research Report)`, and `.tfw/templates/RES.md`.

### TS (Task Spec)
**Meaning:** The self-contained executable order for one task or phase. **Authority:** [conventions.md](conventions.md#ts-task-spec), `TS (Task Spec)`, and `.tfw/templates/TS.md`.

### RF (Result File)
**Meaning:** The Executor's authoritative record of delivered results, verification, evidence, and observations. **Authority:** [conventions.md](conventions.md#rf-result-file), `RF (Result File)`, and `.tfw/templates/RF.md`.

### ONB (Onboarding Report)
**Meaning:** The Executor's pre-work record of understanding, questions, recommendations, risks, and inconsistencies. **Authority:** [conventions.md](conventions.md#onb-onboarding-report), `ONB (Onboarding Report)`, and `.tfw/templates/ONB.md`.

### REVIEW (Review Report)
**Meaning:** The Reviewer-locked verdict and disposition record produced after independent verification. **Authority:** [conventions.md](conventions.md#review-review-report), `REVIEW (Review Report)`, and `.tfw/templates/REVIEW.md`.

### KNOWLEDGE.md
**Meaning:** The project index for architecture, key artifacts, legacy, and verified topic facts. **Authority:** [conventions.md](conventions.md#102-knowledge-infrastructure), `Knowledge Infrastructure`.

### RELEASE.md
**Meaning:** Project-specific release context and checks used by the release workflow. **Authority:** [.tfw/workflows/release.md](workflows/release.md), `TFW Release`.

## Contract and Purpose Defence

### HL Contract
**Meaning:** Owner approval freezes HL §§1, 3–7 while leaving only the declared free sections editable. **Authority:** [conventions.md](conventions.md#hl-high-level), `HL Contract`.

### Contract Baseline
**Meaning:** The approved HL revision against which later purpose and amendment decisions are judged. **Authority:** [conventions.md](conventions.md#hl-high-level), `Contract Baseline`.

### Frozen Section
**Meaning:** An approved declarative HL claim that no role may change outside the amendment protocol. **Authority:** [conventions.md](conventions.md#hl-high-level), `HL Contract` rules 3–5.

### Amendment
**Meaning:** An evidence-, cost-, and impact-backed proposal for an owner ruling on a frozen claim. **Authority:** [conventions.md](conventions.md#hl-high-level), `HL Contract` rules 10–12.

### Amendment Log
**Meaning:** HL §12's append-only record of amendment proposals, owner verdicts, and resulting state. **Authority:** `.tfw/templates/HL.md` §12.

### Project North Star
**Meaning:** The highest-priority statement of what the project builds, why, and what it deliberately does not build. **Authority:** [conventions.md](conventions.md#project-north-star), `Project North Star`.

### Purpose Check
**Meaning:** The Reviewer's independent comparison of the delivered result with the North Star and frozen contract baseline. **Authority:** `.tfw/templates/review/judge.md`, `Purpose Check`.

### not fit for purpose
**Meaning:** A Purpose Check result stating that green local criteria still fail the approved intended outcome. **Authority:** `.tfw/templates/review/judge.md`, `Purpose Check`.

### Deferral confession
**Meaning:** An explicit statement that the contract remains unmet when a material gap is deliberately deferred. **Authority:** [conventions.md](conventions.md#hl-high-level), `HL Contract` rule 22.

## Knowledge Terms

### Fact Candidate
**Meaning:** An unverified observation whose value depends on human knowledge and may be promoted only through consolidation. **Authority:** [.tfw/workflows/knowledge.md](workflows/knowledge.md#phase-2-gather), `Gather`.

### Strategic Insight
**Meaning:** Human-sourced domain knowledge captured with implications during planning, research, or execution. **Authority:** `.tfw/templates/{HL,RES,RF}.md`, each `Strategic Insights` section.

### Value Flow
**Meaning:** HL §3.2's input-to-transformation-to-outcome view of how the proposed result creates value. **Authority:** `.tfw/templates/HL.md` §3.2.

### Result Visualization
**Meaning:** HL §3.1's concrete preview of the completed result. **Authority:** `.tfw/templates/HL.md` §3.1.

### Findings Map
**Meaning:** RES's analytical visualization of relationships among findings, causes, or alternatives. **Authority:** `.tfw/templates/RES.md`, `Findings Map`.

### Per-template Naming
**Meaning:** One cognitive mode keeps one section name, while distinct modes use distinct names. **Authority:** [conventions.md](conventions.md#3-artifact-types-canonical), `Knowledge Capture Sections`.

## Evidence Terms

### Evidence
**Meaning:** Observation of completed work in its intended environment, distinct from synthetic verification output. **Authority:** [conventions.md](conventions.md#evidence-sections-per-template), `Evidence Sections`.

### Evidence Plan
**Meaning:** The TS per-criterion prescription of environment, action, and observable success. **Authority:** `.tfw/templates/TS.md` §5.

### Evidence Collection
**Meaning:** The Executor activity after the build gate and before the Pre-RF Gate that records each AC using the evidence vocabulary. **Authority:** [.tfw/workflows/handoff.md](workflows/handoff.md#phase-2-execution), **Collect evidence**.

### Evidence Audit
**Meaning:** The Reviewer's independent check that EV claims resolve and agree with the delivered result. **Authority:** `.tfw/templates/review/verify.md`, `Evidence Verification`.

### Evidence Status Vocabulary
**Meaning:** The closed EV result set `VERIFIED`, `DEFERRED`, `BLOCKED`, and `N/A`. **Authority:** `.tfw/templates/evidence/EV.md`, `Evidence Table`.

## Commit Attribution

**Meaning:** The structured first-line prefix that makes an AI-authored commit searchable without classifying unmarked commits. **Authority:** [conventions.md](conventions.md#commit-attribution), `Commit Attribution`.

## Task Naming

**Meaning:** A current task uses the full approved `{PREFIX}_{YYYYMMDD-HHMMSS}_{ABBR}` directory name as its identifier. **Authority:** [conventions.md](conventions.md#identifier), `Identifier`, and `tfw.task_prefix`.

## Status Flow

**Meaning:** The closed task/phase lifecycle from TODO through execution, review, optional knowledge
capture, and a terminal outcome. **Authority:** [conventions.md](conventions.md#5-task-statuses),
`Task Statuses`, and `.tfw/templates/status.md`.

### UNDECLARED
**Meaning:** A non-selectable migration value preserving a legacy status outside the closed vocabulary until an owner resolves it by a two-act transition. **Authority:** [conventions.md](conventions.md#5-task-statuses), `Task Statuses`.

### KNW (Knowledge Capture)
**Meaning:** Optional post-review documentation and knowledge consolidation before closure. **Authority:** [conventions.md](conventions.md#5-task-statuses), `Task Statuses`.

### Revision
**Meaning:** A repair round whose rung selects either the existing approved TS plus ruled live REVIEW
or the highest approved TS sibling, while ONB/RF/EV append. **Authority:** [conventions.md](conventions.md#5-task-statuses),
`The 🔄 REVISE route`, and `Artifact file naming`.

### Citation bar
**Meaning:** A review round may order only work that cites the failed approved TS criterion or frozen HL claim. **Authority:** [conventions.md](conventions.md#5-task-statuses), `REVISE`, and `.tfw/templates/REVIEW.md` §5.

### Rung
**Meaning:** A review finding's payment owner: Executor, Coordinator, or task owner. **Authority:** [conventions.md](conventions.md#15-role-lock-protocol), `Role Lock Protocol`.

## Concept Taxonomy

| Level | Question | Owner |
|---|---|---|
| Purpose | Why and for whom? | Project North Star / HL |
| Architecture | Which durable structure? | HL / KNOWLEDGE decisions |
| Convention | Which shared rule? | `conventions.md` |
| Implementation | How in this scope? | TS / code / RF |

## Roles

### User (Human)
**Meaning:** The accountable stakeholder who approves scope, frozen claims, and human-only decisions. **Authority:** [conventions.md](conventions.md#15-role-lock-protocol), `Role Lock Protocol`.

### Coordinator (AI)
**Meaning:** The planning role that writes HL/TS and rules review dispositions without implementing. **Authority:** [.tfw/workflows/plan.md](workflows/plan.md), `ROLE LOCK: COORDINATOR`.

### Researcher (AI)
**Meaning:** The investigation role that writes RES and research stage files without changing the contract. **Authority:** [.tfw/workflows/research/base.md](workflows/research/base.md), `ROLE LOCK: RESEARCHER`.

### Executor (AI)
**Meaning:** The delivery role that writes ONB, implementation, evidence, and RF only inside an approved TS. **Authority:** [.tfw/workflows/handoff.md](workflows/handoff.md), `ROLE LOCK: EXECUTOR`.

### Reviewer (AI — coordinator under the reviewer Role Lock)
**Meaning:** The independent verification role that writes review artifacts and never implementation or governing HL/TS. **Authority:** [.tfw/workflows/review.md](workflows/review.md), `ROLE LOCK: REVIEWER`.

### Principal

**Meaning:** Stable project-local participant attribution. **Authority:** [conventions.md](conventions.md#declared-participants-and-principals), `Declared participants and principals`.

### Initiation Chain

**Meaning:** Human-rooted working-unit delegation path. **Authority:** [conventions.md](conventions.md#hl-contract), `HL Contract` rule 8.

## Execution Gates

### Acceptance Criteria (TS)
**Meaning:** Observable conditions that define whether the scoped result is acceptable. **Authority:** `.tfw/templates/TS.md` §5.

### Technical Guidance (TS)
**Meaning:** Non-normative implementation advice subordinate to acceptance criteria. **Authority:** `.tfw/templates/TS.md` §6.

### Definition of Failure (TS)
**Meaning:** Explicit outcomes that invalidate delivery even if individual checks appear green. **Authority:** `.tfw/templates/TS.md` §7.

### Principles Check
**Meaning:** The TS mapping from each frozen design principle to an enforcement site and gate. **Authority:** `.tfw/templates/TS.md` §3.

### AC Dependency Annotation
**Meaning:** `[depends: AC-X]` forbids starting a dependent criterion until its prerequisite is verified. **Authority:** `.tfw/templates/TS.md` §5 and `handoff.md` **Implement**.

### Execution Loop
**Meaning:** The Executor implements and verifies each prerequisite AC before any annotated dependent AC proceeds. **Authority:** [.tfw/workflows/handoff.md](workflows/handoff.md#phase-2-execution), **Implement**.

### Pre-TS Gate
**Meaning:** Planning must inspect the latest dependency RF before specifying a later phase. **Authority:** [.tfw/workflows/plan.md](workflows/plan.md), **Pre-TS Gate**.

### Pre-RF Gate
**Meaning:** Before writing RF, the Executor opens `.tfw/templates/RF.md` and reads every section heading. **Authority:** [.tfw/workflows/handoff.md](workflows/handoff.md#phase-3-write-rf), **Pre-RF Gate**.

### Session Naming
**Meaning:** A state-backed, fail-soft navigation title for task-bound work; `plan.md` binds it after creation by design because the task identifier must first exist. **Authority:** `conventions.md` → `Session identity`; workflows only bind their local cue and checkpoint.

### Phase Dependencies
**Meaning:** HL §4's graph and table state predecessor, shared-file, and parallel-execution relationships. **Authority:** `.tfw/templates/HL.md` §4.

## RESEARCH

**Meaning:** The optional Researcher-locked investigation stage between HL framing and executable TS. **Authority:** [.tfw/workflows/research/base.md](workflows/research/base.md), `Core Algorithm`.

## Stage (Research)

**Meaning:** One ordered research activity with its own template, trace file, and completion gate. **Authority:** `research/base.md`, `Stage Execution`.

## Pass (Research)

**Meaning:** A bounded analytical lens inside a stage; passes do not create separate lifecycle state. **Authority:** `.tfw/templates/research/*.md`.

## Iteration (Research)

**Meaning:** One complete Briefing→Gather→Extract→Challenge→RES cycle preserved in its own directory. **Authority:** `research/base.md`, `Resume & Iteration Detection`.

## iterations.yaml

**Meaning:** Research-local state declaring iteration bounds and completion without owning task lifecycle. **Authority:** `.tfw/workflows/research/base.md`, `Resume & Iteration Detection`.

## min_iterations

**Meaning:** The minimum completed research cycles required before the Researcher may close. **Authority:** `tfw.research.min_iterations` in `.tfw/project_config.yaml`.

## Read-only AG

**Meaning:** Autonomous research permission to inspect and write research traces while all project artifacts remain read-only. **Authority:** `research/base.md`, `Execution mode`.

## Research — Dimensional Analysis

**Meaning:** Deep-mode method that maps design dimensions and rejects inconsistent configurations before selecting one. **Authority:** `.tfw/workflows/research/deep.md`, `Dimensional Analysis`.

### Dimension (Research)
**Meaning:** An independent design axis with explicit alternatives. **Authority:** `.tfw/workflows/research/deep.md`, `Dimensional Analysis`.

### Alternative (Research)
**Meaning:** One candidate value for a research dimension. **Authority:** `.tfw/workflows/research/deep.md`, `Dimensional Analysis`.

### Configuration Space (Research)
**Meaning:** The combinations induced by selected alternatives across dimensions. **Authority:** `.tfw/workflows/research/deep.md`, `Dimensional Analysis`.

### Consistency Check (Research)
**Meaning:** The explicit test that removes configurations whose alternatives conflict. **Authority:** `.tfw/workflows/research/deep.md`, `Dimensional Analysis`.

### Surviving Configuration (Research)
**Meaning:** The configuration remaining after consistency and evidence challenge. **Authority:** `.tfw/workflows/research/deep.md`, `Dimensional Analysis`.

## Phase

**Meaning:** A scope-bounded unit of a multi-phase task with its own HL→TS→ONB→RF→REVIEW path and local state. **Authority:** [conventions.md](conventions.md#multi-phase-folder-structure), `Multi-phase folder structure`.

## Multi-phase Handoff

**Meaning:** The Coordinator dispatches each approved phase to a separate Executor and reviews its RF before dependent planning. **Authority:** `plan.md` **Pre-TS Gate** and `handoff.md` **Multi-Phase Task Flow**.

## Worktree Protocol

**Meaning:** Concurrent-mutation isolation contract. **Authority:** [conventions.md](conventions.md#worktrees-for-concurrent-mutation), `Worktrees for concurrent mutation`.

## Landing Commit

**Meaning:** Cross-session deliverable-attribution commit. **Authority:** [conventions.md](conventions.md#landing-a-deliverable-across-sessions), `Landing a deliverable across sessions`.

## Scope Budget

**Meaning:** The two-measure report over a phase's declared **value-bearing surface**: logical touched `VALUE` files and touched text LOC. `VALUE`, `ASSURANCE`, `TRACE`, and `DERIVED` are purpose classes; accepted-output and necessary-constituent precedence, fixed Baseline/Candidate rules, trigger disposition, and authority are defined only in the canonical section. The configured file/LOC values are soft decomposition prompts, while `owner_escalation_multiplier` bounds prospective Coordinator authority against the immutable owner-approved plan. **Authority:** [conventions.md](conventions.md#6-scope-budgets-per-phase), `Scope Budgets (per Phase)`.

## Topic File

**Meaning:** A `knowledge/{category}.md` store of verified project facts for one category. **Authority:** [conventions.md](conventions.md#102-knowledge-infrastructure), `Knowledge Infrastructure`.

## Knowledge Gate

**Meaning:** The off/soft/hard threshold over distinct pending full-task digests that routes overdue work to consolidation. **Authority:** [.tfw/workflows/plan.md](workflows/plan.md#step-2-knowledge-gate) and [.tfw/workflows/knowledge.md](workflows/knowledge.md#phase-1-orient).

## Consolidation

**Meaning:** Human-gated promotion, merge, rejection, and marking of pending task knowledge, with post-marker digest state written last. **Authority:** [.tfw/workflows/knowledge.md](workflows/knowledge.md), Phases 2–4.

## Project Values (PV)

PV is the ordered decision context below. Coordinator and Reviewer independently scan P0–P4;
P5–P7 are relevance-triggered.

### PV Index (scan order)

| Priority | Source | What it contains |
|---|---|---|
| 0 | **Project North Star** — designated README sections; otherwise master HL §1 at its contract baseline | What the project builds, why, and deliberately does not build |
| 1 | `.tfw/README.md` `Methodology values` and `Success Criteria` | How TFW work is practiced and what observable success means |
| 2 | `knowledge/philosophy.md` | Validated principles and design rationale |
| 3 | `KNOWLEDGE.md` §1 | Architecture Decisions |
| 4 | `conventions.md` `HL (High Level)`, `Design Rules`, and `Anti-patterns (prohibited)` | Contract, design, naming, and prohibitions |
| 5 | `knowledge/convention.md` | Agreed standards and patterns |
| 6 | `knowledge/process.md` | Process facts and workflow patterns |
| 7 | Other `knowledge/*.md` | Domain, constraint, stakeholder, environment, and risk facts |

Priorities 0 and 1 remain distinct semantic items even when one file contains both.

- **Coordinator:** scan P0–P4 and relevant P5–P7; write HL §7.2 with the exact item, link, and application.
- **Reviewer:** independently scan P0–P4 and relevant P5–P7; verify resolution, existence, semantic match, and relevance in `verify.md`.
- **Executor:** read HL §7.2 citations; confirm their use and add newly relevant items in ONB §7.
- **Researcher:** read HL §7.2 citations and cross-reference relevant findings in RES.

**Authority:** [conventions.md](conventions.md#project-north-star), `.tfw/workflows/{plan,review}.md`, and `.tfw/templates/ONB.md` §7.

## Config Sync Registry

**Meaning:** The config workflow's closed map from each project setting to exact inline readers and generated adapter copies. **Authority:** [.tfw/workflows/config.md](workflows/config.md), `Config Sync Registry`.

## Tool Adapter

**Meaning:** A vendor discovery root plus exact `/tfw-*` command copies that route to the tool-agnostic core. Antigravity uses `.agents/rules/tfw.md` for its persistent rule and `.agents/workflows/tfw-{command}.md` for commands. **Authority:** [.tfw/adapters/manifest.yaml](adapters/manifest.yaml) for copy/check metadata and [conventions.md](conventions.md#9-tool-adapter-pattern) for runtime behavior.

## status.md

**Meaning:** The only authority for one task or phase's current lifecycle and owner. **Authority:** [conventions.md](conventions.md#task-control-files), `Task control files`, and `.tfw/templates/status.md`.

## journal/

**Meaning:** A task-local append-only set of immutable coordination events whose timestamped filenames are their identities. **Authority:** [conventions.md](conventions.md#task-control-files), `Task control files`, and `.tfw/templates/journal/event.md`.

## Task discovery

**Meaning:** Direct resolution of a selected whole task identifier through configured containers
to its task-local state and artifacts. Optional read-only projections are disposable and never
gate a transition. **Authority:** [conventions.md](conventions.md#discovery), `Discovery`.

## team/

**Meaning:** Human attribution profiles; machine-to-handle bindings remain outside project state. **Authority:** [conventions.md](conventions.md#which-handle-a-machine-acts-as), `Which handle a machine acts as`.

## Historical Lookup

Debt Registry — retired; see `tasks/DEBT-SNAPSHOT.md` and D61.

Task Board — retired; see `tasks/BOARD-SNAPSHOT.md` and D68.

Portfolio index — retired; current Full keeps no shared task cache or freshness duty. See D69,
D73, D75, and D76.

Compatibility origin details are maintainer-only at `conventions.md` `Terminology Origin` and
are not ordinary role inputs.

## Disposition

**Meaning:** A review item becomes **paid** by a named phase, **promoted** to an existing task, or ruled **not material**; if payment is future, the same act must order that phase in a round with the item's cited condition, or `paid` is deferral. **Authority:** `.tfw/templates/REVIEW.md` §5 and [conventions.md](conventions.md#15-role-lock-protocol), `Role Lock Protocol`.

## project_config.yaml

**Meaning:** Project-owned TFW configuration for identifiers, containers, commands, templates, budgets, and knowledge behavior. **Authority:** `.tfw/project_config.yaml` and `.tfw/templates/project_config.yaml`.

## VERSION

**Meaning:** The installed framework semantic version. **Authority:** `.tfw/VERSION`.

## CHANGELOG.md

**Meaning:** The versioned history of framework additions, changes, fixes, and removals. **Authority:** `.tfw/CHANGELOG.md`.

## Compilable Contract

**Meaning:** The deterministic build-time specification for compiling TFW artifacts. **Authority:** [compilable_contract.md](compilable_contract.md).

## Reference Format

**Meaning:** Standard cross-artifact citations resolved into links by the build. **Authority:** [compilable_contract.md](compilable_contract.md#2-reference-format), `Reference Format`.

## Source Manifest

**Meaning:** The ordered project-file inputs used by compilation utilities. **Authority:** [compilable_contract.md](compilable_contract.md#1-source-manifest), `Source Manifest`.

---

## Project-Specific Terms

A receiving project may replace this section with local terms; no canonical workflow requires it.
