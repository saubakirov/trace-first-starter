# TFW Conventions

## 1) Purpose

TFW turns product work—strategy, research, operations, documents, design, education, and code—into a reproducible, value-first process:
- product purpose and applicable Project Values remain connected to the work,
- decisions and authority are traced,
- claims yield to appropriate proof and observed reality,
- independent judgment can challenge a shared mistake,
- selected learning receives a visible disposition,
- any human or agent can continue the project in a new session.

## 1.1) Method Kernel and Operational Contracts

### Semantic Ownership

TFW uses four canonical surfaces with non-competing responsibilities:

| Surface | Semantic responsibility | Must not become |
|---------|-------------------------|-----------------|
| Root `README.md` | Concise public product promise and entry path | A formal rules manual |
| `.tfw/README.md` | Philosophy, values, and success criteria | An artifact or workflow reference |
| `.tfw/conventions.md` | Operational obligations, contracts, and transitional controls | A second philosophy or glossary |
| `.tfw/glossary.md` | Concise canonical term definitions with links to operational owners | A duplicate workflow or contract |

A summary or point-of-use gate may reference an owned definition. It must not silently
redefine it. When wording conflicts, use the owner above and report the conflicting
consumer for correction in its approved phase.

### Method Kernel

Every TFW task MUST protect exactly five obligations:

| Protected Obligation | Operational requirement |
|----------------------|-------------------------|
| **Product purpose and applicable Project Values** | Discover and apply the product's purpose, owner decisions, and relevant project-owned values before choosing or judging work. Project-specific values remain outside the universal kernel. |
| **Lifecycle and role authority** | Make the current state and the authority to decide, act, challenge, override, or stop observable. A later or narrower context cannot silently weaken an authority boundary. |
| **Evidence precedence** | Treat observed reality as capable of refuting HL, TS, RF, prior knowledge, or participant agreement. Match proof to the claim rather than to convenient available output. |
| **Independent judgment** | Preserve a role or gate that can compare purpose, values, cited sources, delivered reality, and evidence instead of checking only artifact agreement. Challenges MUST cite the governing authority or observation. |
| **Visible learning disposition** | Give every selected durable or contradictory signal an explicit disposition and proportionate receipt; do not confuse capture volume with project learning. |

The Method Kernel requires discovery and protection of applicable Project Values; it
does not copy project-owned values or domain gates into the universal method.

### Composition and Proportionality

A valid TFW execution composes:

```text
one-or-more Rule Records
+ one-or-more Proof Records for every claim
+ event-triggered Learning Transactions
+ zero-or-more independent Registered Extensions
+ every applicable Numeric Control
```

The **Protected Obligation** is the unit of proportionality. No task-wide weight or
packaging mode may remove a kernel obligation. A task may package the same
obligations compactly, in stages, with risk-expanded detail, or in grouped artifacts.
More files do not prove stronger work; fewer files do not waive authority, proof,
judgment, or learning disposition.

Consumer status is explicit:

| Consumer group | Status |
|----------------|--------|
| Planning, comparative research, HL/RES synthesis, and research-stage templates | Phase B maps these consumers to the Method Kernel through the contracts below |
| Specification, execution, evidence, review, knowledge closure, lifecycle, extensions, adapters, migration, and release | Transitional until their approved consuming phases map, restore, or retire them |
| Configuration keys and exact values | Unchanged and transitional; a changed consumer does not silently recalibrate or delete its source value |

### Purpose-Led Planning and Insight Disposition

Planning MUST distinguish:

- product purpose, owner decisions, and applicable Project Values;
- the uncertainty whose answer can change a decision;
- the evidence needed to reduce that uncertainty; and
- a proposed solution, which remains a hypothesis until the applicable decision gate.

Every material human **Strategic Insight** records both a planning implication and a
resolvable TS disposition. Valid dispositions include an Acceptance Criterion, scope
boundary, Technical Guidance, Definition of Failure, decision or research direction,
explicit task-local/non-use reason, or named downstream destination. The Pre-TS Gate
checks that no material insight lacks a disposition; it MUST NOT force one insight into
one separate AC when another destination protects the consequence more accurately.
Project Values continue through the existing Knowledge Citation cascade rather than a
duplicate planning artifact.

### Comparative Decision Procedure

The **Comparative Decision Procedure** is TFW's current operational method for an
uncertainty that requires comparing material alternatives, relationships, or
configurations:

```text
Briefing → Gather → Extract → Challenge → RES
```

| Stage | Decision contribution |
|-------|-----------------------|
| Briefing | Names purpose, decision-changing uncertainty, material comparison/configuration question, and what result would change the approach |
| Gather | Establishes the declared evidence/corpus, exclusions, material decision factors, alternatives, and relevant relationships |
| Extract | Makes consequential option relationships or configurations visible without treating activity volume as coverage |
| Challenge | Attacks claims with counter-evidence, incompatibilities, edge/failure cases, and unresolved uncertainty |
| RES | Synthesizes the supported decision or explicit gap and routes applicable insights and selected learning |

Before stage execution, the Researcher MUST test procedure fit. Fit requires a real
comparison of alternatives, relationships, or configurations. Direct lookup, corpus
immersion, documentation mapping, diagnosis before causes are known, and open
exploration are not automatically suitable. On mismatch, record the unresolved
information need and return authority to the Coordinator/user. The fit gate MUST NOT
select, name, simulate, or load a substitute strategy.

The complete filesystem floor remains mandatory for every claimed completed procedure:
`1_briefing.md`, `2_gather.md`, `3_extract.md`, `4_challenge.md`, and `RES.md`.
Removing count authority does not permit a missing stage or bypass Coordinator closure
authority.

#### H4 Non-Claim

The claimed benefit of task-matched cognitive strategies remains
**unresolved/inconclusive**. The dated T0 desk protocol/owner package is the only
authorized H4 material. TFW-48 does not execute or imply name-only, operational,
token-matched, matched/mismatched, pilot, model/profile, scoring, or inferential
comparisons. It adds no strategy selector, catalog, registry, runtime choice, prompt
library, prestigious-method list, or strategy-extension mechanism. Future lookup,
immersion, diagnosis, case-study, or Yin-style work requires separately owner-gated
research; the procedure-fit gate only accepts or rejects the current procedure.

### Research Intensity and Closure

**Research Intensity** changes qualitative breadth and challenge within the same
Comparative Decision Procedure:

| Intensity | Observable behavior |
|-----------|---------------------|
| Focused | Bounded decision, deliberately narrow declared evidence/corpus, proportionate countercheck, explicit exclusions, and low unresolved risk |
| Deep | Diverse independent evidence families, active counter-evidence, edge/failure cases, and explicit treatment of material unresolved uncertainty |

Intensity is not method fit, a strategy choice, or completion proof. No loop, source,
file, question, decision, turn, hypothesis, or configuration count can make an
insufficient claim pass or make a sufficient claim fail.

A stage or iteration closes only when its claim records:

1. the declared corpus or evidence families and material coverage;
2. exclusions and their possible effect on the decision;
3. counter-evidence or the justified scope of the countercheck;
4. the decision effect, supported disposition, or explicit unresolved result;
5. open gaps, blockers, and their owner or authority outcome; and
6. saturation: further available evidence is not changing a material disposition, or
   the remaining evidence cannot be obtained and the limitation is explicit.

An exhausted search may close as **insufficient/unresolved**; it MUST NOT fabricate a
conclusion. An additional iteration requires a named trigger: error correction,
unresolved material gap or hypothesis, counter-evidence need, changed decision, or
user-injected direction. The Coordinator/user decides whether to proceed, deepen,
defer, or accept the unresolved gap.

### Rule Record and Rule Deployment

Every operative rule has one **Rule Record**:

| Field | Requirement |
|-------|-------------|
| Protected consequence | Name the failure or invariant the rule protects |
| Semantic owner | Point to the one canonical definition or operational rule |
| Point-of-use cue or gate | Make discovery or enforcement occur where the rule matters |
| Observable enforcement | State what shows that the rule was loaded or applied |
| Authority and exception | Name who may override, strengthen, stop, or resolve conflict |
| Provenance and freshness | Record source/version and how stale derivatives are exposed |

**Rule Deployment** selects locality by protected consequence and observability:

| Consequence | Minimum valid deployment |
|-------------|--------------------------|
| Reversible misunderstanding or explanation | Canonical owner plus a discoverable reference or cue at the decision point |
| Lifecycle, navigation, or required-trace failure | Canonical owner plus an observable point-of-use gate |
| False claim, missing source, or crossed boundary | Canonical owner plus a claim-time proof gate that exposes the omission |
| Role, safety, destructive, or irreversible pre-action boundary | Complete local imperative before action plus a hard gate; a remote reference alone is invalid |

Task exposure, risk, or project policy MAY strengthen deployment. They MUST NOT weaken a
pre-action authority, safety, destructive, or irreversible boundary. A complete local
imperative remains enforcement, not a competing semantic definition, when it points to
the same owner and consequence.

Universal “repeat everything” and “reference everything” rules are prohibited. A
reference is effective only when an algorithmic step or observable gate makes the
consumer use it.

### Proof Records and Claim Boundaries

Every claimed deliverable MUST have one-or-more **Proof Records**. A Proof Record names
the claim, boundary, verification method or observation, result, artifact/provenance,
actor/time when material, and any unresolved debt.

| Proof obligation | Trigger | Minimum proof |
|------------------|---------|---------------|
| **Local Proof** | Every claimed deliverable | Verify the result within its owned boundary against the applicable requirement |
| **Seam Proof** | A claim crosses a component, source, role, package, phase, handoff, or other interface | Verify both sides and their relationship; one-sided success is insufficient |
| **Live Proof** | A claim depends on a stakeholder, user, environment, production condition, or irreversible external outcome | Observe the intended outcome at the earliest honest event and preserve its provenance |
| **Value Debt** | Required Seam or Live Proof cannot yet exist | Record owner, due event, evidence route, and explicit non-claim until the debt closes |

Proof packaging and proof obligation are independent. Compact, staged, risk-expanded,
and grouped packaging are all valid when every triggered proof remains visible.

**Verification**, **Evidence**, and **Proof Record** remain distinct:
- Verification is synthetic tool output such as lint, tests, build, or source checks.
- Evidence is real-world observation in the intended environment.
- A Proof Record connects a claim to the verification, evidence, source comparison, or
  other observation appropriate to that claim.

Neither a passing test nor an Evidence file proves an unobserved seam or live outcome
by implication.

### Learning Transactions and Learning Receipts

Learning is event-triggered. Start a **Learning Transaction** only when a signal is
durable, contradictory, or likely to change a future decision—for example a material
user correction, production surprise, failed assumption, or reusable discovered
pattern. Routine task detail and boilerplate absence do not require central routing.

Every selected signal receives a **Learning Receipt** proportionate to disposition:

| Disposition | Required receipt |
|-------------|------------------|
| Reject or retain task-local | State and reason |
| Promote, merge, or derive | Destination/backlink and responsible actor |
| Defer | Destination or due event and responsible actor |

Capture alone is not closure. A signal without a disposition is still open; a rejected
or task-local signal does not need a central knowledge entry.

#### Research Learning Receipts

At every research-stage checkpoint, run the selection test before creating a receipt.
Select only a durable or contradictory signal likely to change a future decision, such
as a material user correction, project/production surprise, failed assumption,
contradiction, or reusable pattern. Routine findings, boilerplate absence, and stage
completion do not trigger a Learning Transaction.

Each selected signal remains in its stage trace with a compact receipt:

| Field | Requirement |
|-------|-------------|
| Signal and trigger | Name what changed and why it passed the selection test |
| Disposition | Reject, task-local, promote, merge, derive, or defer |
| Required relation | Reject/task-local: state and reason. Promote/merge/derive: destination/backlink. Defer: destination or due event |
| Responsible actor | Required for promote/merge/derive/defer; record authority when material for reject/local |

If no signal passes, write **“No selected signal.”** Do not invent a row to fill the
checkpoint. Counter-evidence may reopen the decision and change a prior disposition.

RES `## Fact Candidates` contains only promote/merge/derive signals that need durable
project verification, with source, destination/backlink, and responsible actor.
Reject/task-local receipts remain in stage traces; deferred receipts remain in the
stage trace or an existing open-thread/decision field unless a later owner explicitly
promotes them. Phase D still owns promotion, knowledge closure, and downstream
`/tfw-knowledge` compatibility; Phase B does not claim those consumers are migrated.

### Project Extensions and Registered Extensions

A **Project Extension** adapts TFW to a project without redefining the universal
kernel. It is independent from a Learning Transaction: learning may occur without an
extension, and an extension may be deliberately configured without a new learning
event.

A **Registered Extension** MUST expose:

| Field | Requirement |
|-------|-------------|
| Semantic owner | Project-owned authority for the extension |
| Source and version | Resolvable origin or configuration version |
| Precedence and conflict | Behavior when project and universal rules disagree |
| Consumers | Workflows, templates, adapters, roles, or tools that load it |
| Freshness evidence | Observable load, sync, hash/version, or stale-state result |
| Unsupported/migration behavior | What happens across incompatible versions or upgrades |

Passive metadata is not registration. At least one consumer MUST produce an observable
load, sync, or conflict result. Direct edits that silently fork upstream core and a
central registry through which every artifact must pass are not framework defaults.

### Numeric Controls

A **Numeric Control** receives meaning before a value. Select one **Numeric Control
Type**:

| Type | Semantic use | Required validation |
|------|--------------|---------------------|
| Structural existence gate | Require a necessary construct to exist | Show that the construct is necessary and the existence check detects it |
| Tunable boundary or threshold | Limit exposure or loss | Owner, loss function, count, enforcement, breach response, override, and outcome/cost calibration |
| Escalation trigger | Increase verification or authority when crossed | Evidence that crossing the trigger should change the response |
| Attention warning | Prompt explain/split/reassess without automatic failure | Useful signal and proportionate response |
| Sampling default | Set an initial coverage expectation | Coverage/saturation rationale, exclusions, and justified expansion or shortfall |
| Normative target | Express a desired measured outcome | Owner, measure, response, and recalibration |
| Descriptive measurement | Report observed inventory or change | Provenance and counting consistency; no breach or override |

Every normative Numeric Control lifecycle MUST name: semantic owner, protected failure
or intended outcome, observed consumer/enforcement, counting rule, breach response,
override authority, provenance/freshness, and monitoring/recalibration or retirement.
Descriptive measurements require provenance and consistent counting, but have no breach
or override semantics.

#### Transitional Restore-Owner-or-Retire Ledger

Phase A changes no exact value or consumer. The values below retain current behavior
only as transitional controls; neither breach nor non-breach validates them.

| Object | Current value | Provisional semantic state | Consumer or gap | Next owner decision |
|--------|---------------|----------------------------|-----------------|---------------------|
| `research.max_passes` | `3` | Intended policy; boundary/default type unresolved | Declared in config and research limits, while OODA consumes `loops_per_stage` | Define alias vs independent ceiling with count/response/override, or retire |
| `research.min_iterations` | `2` | Active tunable boundary/sampling floor; universal value unvalidated | Plan and iteration gate consume it; sync registry ownership is incomplete | Register owner/derivatives, define override evidence, then calibrate or retire the universal default |
| `knowledge.max_index_lines` | `200` | Intended target/warning; type unresolved | Config declares it; no active counting or breach path | Restore count/response/override and navigation outcome, or retire normativity |
| `knowledge.max_index_facts_lines` | `30` | Obsolete/dead candidate | Originating index topology and consumer no longer exist | Confirm retirement and remove derivatives in an approved consuming phase |
| `knowledge.max_facts_per_topic` | `50` | Active intent with incomplete warning/threshold semantics | Knowledge workflow checks it without a defined breach response | Define split/warn/explain/override behavior before calibration |
| `knowledge.max_topic_files` | `8` | Active intent with incomplete warning/threshold semantics | Knowledge workflow checks it without a taxonomy-quality response | Define coherent taxonomy response and override before calibration |
| Workflow instruction length | `≤1200` words | Intended normative target/attention control; exact type unresolved | Conventions declare it; word-count unit and breach response are absent | Define unit and response with owner, or retire normativity |
| Adapter content length | `≤35` lines | Intended maintainability target; unit/enforcement unresolved | Adapter guidance declares it; file/skill/whole-adapter unit is ambiguous | Define architecture-neutral unit and response, or retire normativity |

#### Phase B Research Numeric Disposition Ledger

Phase B changes workflow authority without changing `.tfw/project_config.yaml`, its
template, or any exact stored value. Former expressions remain listed so retirement is
traceable; none is replaced by a larger or hidden quota.

| Object or former expression | Phase B disposition | Replacement authority | Phase E handoff |
|-----------------------------|---------------------|-----------------------|-----------------|
| `max_web_queries_per_stage: 5` | Loses universal cap/default normativity | Declared evidence families, exclusions, claim risk, and saturation | Restore an owned sampling default with validation or remove the key |
| `max_files_per_stage: 15` | Loses universal cap/default normativity | Approved corpus, coverage, exclusions, and whether newly available files change a disposition | Restore an owned sampling default with validation or remove the key |
| `max_questions_per_turn: 3` | Loses universal hard-cap normativity | Ask only decision-changing questions; prioritize and split when the user cannot answer safely or coherently in one turn | Restore a protected communication boundary or remove the key |
| `max_passes: 3` | Confirmed unconsumed residue | No replacement; stage/iteration closure follows the claim conditions above | Define an independent consumer and response or remove the key |
| `min_iterations: 2` | Loses universal hard-floor/closure authority; may remain compatibility metadata | One complete filesystem-traced procedure; more iterations require a named trigger and Coordinator/user authority | Restore an owned floor with evidence or remove/redefine the key |
| `iterations.yaml max_iterations: 5` | Loses soft-ceiling/closure authority; field may remain compatibility metadata | Named trigger, material risk/gap, and Coordinator/user authority | Restore an owned attention/escalation control or remove/redefine the field |
| `loops_per_stage: 1/3` | Loses completion-authority status | Focused/deep qualitative intensity plus evidence-based stage closure | Restore an owned iteration/escalation control or remove/redefine the keys |
| Fixed decisions, turns, cross-checks, or hypotheses in intensity files | Retired | Observable evidence breadth, counter-evidence, edge/failure coverage, exclusions, and unresolved risk | No config migration unless Phase E deliberately introduces an owned control |
| Planning/Briefing `2–4` hypotheses, `3–5` bullets, and `≤3` questions | Retired | Decision-changing hypotheses/plan content and prioritized/split questions | No replacement number |
| Minimum `3` dimensions | Retired | Materially independent decision factors; use a legible comparison when a configuration representation adds no value | No replacement number |
| Minimum `3` alternatives per dimension | Retired | Materially distinct realistic alternatives without invented filler | No replacement number |
| Configuration sampling after `>30` combinations | Retired | State the inclusion/exclusion rule and prove omitted classes cannot change the disposition | No replacement number |

## 2) Required Artifacts (project root)

- `README.md` — human explanation: why/what/how. Contains Task Board.
- `AGENTS.md` — AI agent behavior rules for the project.
- `TECH_DEBT.md` — accumulated tech debt from reviews (observations → triage → registry).
- `KNOWLEDGE.md` _(optional)_ — project knowledge index: architecture, decisions, legacy. Template: `.tfw/templates/KNOWLEDGE.md`.
- `RELEASE.md` _(optional)_ — project release strategy and context. Template: `.tfw/templates/RELEASE.md`.
- `.tfw/README.md` — TFW philosophy, lifecycle, values.
- `.tfw/conventions.md` — project conventions (this file).
- `.tfw/glossary.md` — project glossary.
- `.tfw/templates/HL.md` — canonical HL template.
- `.tfw/templates/TS.md` — canonical TS template.
- `.tfw/templates/RF.md` — canonical RF template.
- `.tfw/templates/ONB.md` — canonical Onboarding Report template.
- `.tfw/templates/RES.md` — canonical Research Report template.
- `.tfw/templates/REVIEW.md` — canonical Review template.
- `.tfw/workflows/init.md` — canonical initialization workflow.
- `.tfw/workflows/plan.md` — canonical planning workflow.
- `.tfw/workflows/research/base.md` — canonical research workflow (entry point).
- `.tfw/workflows/handoff.md` — canonical execution workflow.
- `.tfw/workflows/review.md` — canonical review workflow.
- `.tfw/workflows/resume.md` — canonical resume workflow.
- `.tfw/workflows/docs.md` — canonical knowledge update workflow.
- `.tfw/workflows/release.md` — canonical release workflow.
- `.tfw/workflows/update.md` — canonical upstream update workflow.
- `.tfw/workflows/config.md` — interactive config change workflow.
- `.tfw/VERSION` — current framework version (semver, single line).
- `.tfw/CHANGELOG.md` — version history (Keep a Changelog format).
- `.tfw/project_config.yaml` — project configuration (stack, build commands, task prefix, execution engine).
- `.tfw/compilable_contract.md` — build-time compilation specification (Source Manifest, Reference Format, Output Structure).

## 3) Artifact Types (canonical)

> See also: [glossary.md](glossary.md) for terminology, [README.md](README.md) for philosophy.

### HL (High Level)
Context/frame. Not a task — a "map of meaning".
Format: strictly follows `.tfw/templates/HL.md`.

### RES (Research Report)
Structured investigation artifact. Produced via Briefing → Gather → Extract → Challenge stages in `research/` subfolder.
RES file = synthesis (Decisions, Hypotheses, HL Recommendations, Conclusion). Stage files = raw investigation.
Created between HL and TS (pipeline) or standalone for any research.
Format: strictly follows `.tfw/templates/RES.md`.

### TS (Task Spec)
Task definition. Always self-contained: inputs/outputs/constraints/DoD.
Format: strictly follows `.tfw/templates/TS.md`.

### RF (Result File)
Results/facts/data/final text. RF has priority as source of truth.
Contains mandatory Observations table (structured, typed).
Format: strictly follows `.tfw/templates/RF.md`.

### ONB (Onboarding Report)
Structured executor report before starting: understanding, questions, risks, inconsistencies.
Coordinator/human answers directly in the file (Q&A format).
Format: strictly follows `.tfw/templates/ONB.md`.

### REVIEW (Review Report)
Formal coordinator report after reviewing RF: checklist, verdict, tech debt.
Format: strictly follows `.tfw/templates/REVIEW.md`.

### Fact Candidates (section in RF, REVIEW, RES)
Raw observations about the project recorded during work. Cognitive mode: pure reporting — record factual without interpretation. NOT verified facts — they become facts after `/tfw-knowledge` consolidation. Each artifact has a Fact Candidates section with a structured table (Category, Candidate, Source, Confidence). Quality filter: "Would the next agent decide differently knowing this?"

### Visual Sections (per-template)

> **Decision criterion:** "Does the cognitive mode CHANGE between templates?" If yes → per-template naming. If no → unified.
> Visual sections trigger different cognitive modes per template context (empirically validated: RES3 D22, RES4 Exp1+Exp2).

| Template | Section | Cognitive Mode | What it produces |
|----------|---------|---------------|-----------------|
| HL | §3.1 Result Visualization | Narrative / Outcome | Outcome preview — Working Backwards style ("imagine it's done") |
| HL | §3.2 Value Flow | Strategic / Value-oriented | Value streams, INPUT→PROCESSING→OUTCOME, transformation tables |
| RF | §9 Diagrams | Technical / Engineering | Architecture, ERD, sequence diagrams, component diagrams |
| RES | Findings Map | Analytical / Research | Root cause analysis, hypothesis trees, priority matrices |
| REVIEW | — | — | No visual section (checklist artifact, not result) |

### Knowledge Capture Sections (unified naming)

| Section | Name | Templates | Cognitive Mode |
|---------|------|-----------|---------------|
| §7 | Fact Candidates | RF, RES, REVIEW | Pure reporting: record without interpretation |
| §8/§11 | Strategic Insights + qualifier | HL (Planning), RF (Execution), RES (Research) | Deep analytical synthesis: capture + add implications |

### Knowledge Input Sections (unified naming)

| Section | Name | Templates | Cognitive Mode |
|---------|------|-----------|----------------|
| §7.2 | Knowledge Citations | HL | Input tracing: cite what was read from PV Index with links |
| §7 | Knowledge Citations | ONB | Input tracing: confirm read of HL §7.2 citations, add new items |
| _(section)_ | Knowledge Citations Verified | review/verify.md | Verification: check that citation links resolve to real items |

> **Unified naming rationale (D43/D28/D39):** cognitive mode is the same across all three — "report what you read and how it applies." Same mode = same name. Scan scope differs by role: Coordinator + Reviewer do full PV scan, Executor references coordinator's citations. See glossary.md → Project Values (PV).

### Evidence Sections (per-template)

> Evidence = real-world verification of completed work in its intended environment.
> Separate from Verification (RF §4 — synthetic tool output: lint, test, build).
> Status vocabulary: VERIFIED / DEFERRED / BLOCKED / N/A.
> Role pipeline: Coordinator designs (TS) → Executor collects (EV file) → Reviewer audits (REVIEW).
>
> **Mandatory folder:** Every task directory MUST contain an `evidence/` subfolder with a structured EV file.
> The EV file captures environment metadata, per-AC verification results, and a verdict summary.
> RF §5 is a pointer to the EV file — not a duplicate of the evidence table.
> Template: `.tfw/templates/evidence/EV.md`.

| Template | Section | Cognitive Mode | What it produces |
|----------|---------|---------------|------------------|
| TS | Evidence field (in §5 AC items) | Prescriptive / Planning | What to verify in real environment, suggested tools |
| EV file | `evidence/EV__{...}.md` | Observational / Verification | Environment header, per-AC evidence table, verdict, attachments |
| RF | §5 Evidence (pointer) | Summary / Reference | One-line pointer to EV file + verdict summary |
| review/verify.md | Evidence Verification | Audit / Trust-but-verify | Artifact existence checks, claim-vs-reality |
| review/judge.md | Check #7 Evidence completeness | Judicial / Completeness | All TS Evidence fields covered in EV file? |

## 4) Task Numbering

ID format is defined in `.tfw/project_config.yaml` (field `tfw.task_prefix`).

File naming:

| Artifact | Format | Example |
|----------|--------|---------|
| Master HL | `HL-{PREFIX}-{N}__{title}.md` | `HL-PROJ-3__tfw-setup.md` |
| Single-phase RES | `RES__{PREFIX}-{N}__{title}.md` | `RES__PROJ-3__tfw-setup.md` |
| Single-phase TS | `TS__{PREFIX}-{N}__{title}.md` | `TS__PROJ-3__tfw-setup.md` |
| Single-phase RF | `RF__{PREFIX}-{N}__{title}.md` | `RF__PROJ-3__tfw-setup.md` |
| Single-phase ONB | `ONB__{PREFIX}-{N}__{title}.md` | `ONB__PROJ-3__tfw-setup.md` |
| Single-phase REVIEW | `REVIEW__{PREFIX}-{N}__{title}.md` | `REVIEW__PROJ-3__tfw-setup.md` |
| Phase RES | `RES__phase-{x}__{title}.md` | `RES__phase-a__conventions.md` |
| Phase TS | `TS__phase-{x}__{title}.md` | `TS__phase-a__conventions.md` |
| Phase RF | `RF__phase-{x}__{title}.md` | `RF__phase-a__conventions.md` |
| Phase ONB | `ONB__phase-{x}__{title}.md` | `ONB__phase-a__conventions.md` |
| Phase REVIEW | `REVIEW__phase-{x}__{title}.md` | `REVIEW__phase-a__conventions.md` |
| Single-phase EV | `EV__{PREFIX}-{N}__{title}.md` | `EV__PROJ-3__tfw-setup.md` |
| Phase EV | `EV__phase-{x}__{title}.md` | `EV__phase-a__conventions.md` |

> **Rule:** ALL artifact filenames MUST include the task ID (`{PREFIX}-{N}`) or Phase identifier. A filename without either is an error.

Task folder: `tasks/{PREFIX}-{N}__{title}/`

### Research subfolder

Research artifacts live in a single `research/` container at task root. Each iteration gets its own numbered subfolder:

```
tasks/{ID}/research/
  iterations.yaml              ← control file
  iter1/
    1_briefing.md              ← numbered stage files
    2_gather.md
    3_extract.md
    4_challenge.md
    RES.md                     ← synthesis co-located with stages
  iter2/
    1_briefing.md
    2_gather.md
    3_extract.md
    4_challenge.md
    RES.md
```

File existence = stage completion. Stage file format: see `.tfw/templates/research/` (`1_briefing.md`, `2_gather.md`, `3_extract.md`, `4_challenge.md`).

#### Multi-iteration research

When research spans multiple iterations, each iteration gets its own subfolder and RES:

| Iteration | Stage files folder | RES file |
|-----------|-------------------|----------|
| 1 | `research/iter1/` | `research/iter1/RES.md` |
| 2 | `research/iter2/` | `research/iter2/RES.md` |
| N | `research/iterN/` | `research/iterN/RES.md` |

**Trace rule:** Iteration folders accumulate — never delete or overwrite previous iteration's files. Each `research/iterN/` folder is a trace. Deleting them = deleting reasoning.

**Control file:** `research/iterations.yaml` tracks iteration state. Created by coordinator in `plan.md` Step 6 before launching research. Format:

```yaml
task_id: PROJ-N
title: research focus description
min_iterations: 2       # from tfw.research.min_iterations or coordinator override
max_iterations: 5       # soft ceiling
iterations:
  - number: 1
    focus: "initial investigation of H1-H3"
    hypotheses: [H1, H2, H3]
    status: complete     # pending | in_progress | complete
    res_file: research/iter1/RES.md
    # agent: antigravity           # optional — which tool/agent ran this iteration
    # sources: [external, codebase] # optional — what sources were consulted
  - number: 2
    focus: "deepen findings from iter 1, test H4"
    hypotheses: [H4]
    status: pending
    res_file: research/iter2/RES.md
```

The `agent` field records which tool or agent conducted the iteration — for traceability, not dispatch. The `sources` field records what source categories were consulted. Both fields are optional; simple single-agent tasks can omit them.

Coordinator updates `research/iterations.yaml` after each iteration (marks status, adds next iteration if needed). Researcher reads it at start to understand predecessor context and assigned hypotheses.


### Review subfolder

Review stage files (`review/map.md`, `review/verify.md`, `review/judge.md`) — intermediate review traces written during the review process. Created in task phase directory. Parallels research stage files (`research/iterN/1_briefing.md`, etc.). The REVIEW artifact synthesizes these files. Stage file format: see `.tfw/templates/review/` (map.md, verify.md, judge.md).

### Evidence subfolder

Every task directory (or phase directory for multi-phase tasks) MUST contain an `evidence/` subfolder. The subfolder always contains at least one structured EV file (`EV__{PREFIX}-{N}__{title}.md` or `EV__phase-{x}__{title}.md`). Additional binary artifacts (screenshots, API responses, logs) go into the same `evidence/` folder and are indexed in the EV file's Attachments section. Template: `.tfw/templates/evidence/EV.md`.

### Multi-phase folder structure

For multi-phase tasks, master artifacts (HL, RES) stay at task root. Each phase gets a subfolder:

```
tasks/PROJ-5__query_redesign/
  HL-PROJ-5__query_redesign.md        ← Master HL
  research/                           ← Master research (if any)
  phase-a/
    HL__phase-a__data_model.md
    TS__phase-a__data_model.md
    ONB__phase-a__data_model.md
    RF__phase-a__data_model.md
    REVIEW__phase-a__data_model.md
    evidence/                         ← Mandatory evidence folder
      EV__phase-a__data_model.md      ← Structured evidence file
  phase-b/
    HL__phase-b__api_layer.md
    ...
```

## 5) Task Statuses

```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → 📚 KNW → ✅ DONE
                                                                              │
                                                                    ┌─────────┴─────────┐
                                                                    🔄 REVISE          ❌ REJECT
                                                                 (back to dev)    (user decides)
                    (skip: 📝 HL_DRAFT ··· 🟡 TS_DRAFT)        ↓
                                                           ❌ BLOCKED
```

| Status | Meaning |
|--------|---------|
| ⬜ TODO | Task planned, HL not started |
| 📝 HL_DRAFT | HL being drafted, awaiting review/approval |
| 🔬 RES | Research in progress (optional — user can skip to TS_DRAFT) |
| 🟡 TS_DRAFT | TS written, awaiting approval for execution |
| 🟠 ONB | Onboarding: executor studying the task |
| 🟢 RF | Execution complete, RF written |
| 🔍 REV | Review: reviewer checking RF |
| 📚 KNW | Knowledge capture: tfw-docs + tfw-knowledge applied (optional — reviewer can pre-close with N/A) |
| ✅ DONE | Task closed, traces updated |
| ❌ BLOCKED | Blocked by dependency |

Task Board format — ID column must be a relative link to the task folder:
```
| [PROJ-1](tasks/PROJ-1__title/) | Description | Status | ... |
```

Review verdicts:
- ✅ **APPROVE** — all ok → 📚 KNW (run tfw-docs + tfw-knowledge), then ✅ DONE
- 🔄 **REVISE** — specific issues → back to execution (same task)
- ❌ **REJECT** → 🛑 User decides: (a) 📝 HL_DRAFT (rework HL), (b) 🔬 RES (new research), (c) 🟡 TS_DRAFT (rewrite TS)

## 6) Scope Budgets (per Phase)

> Configured in `.tfw/project_config.yaml` (`tfw.scope_budgets`).
> Values below are defaults. Override in project_config.yaml for your project.

| Parameter | Default | Rationale | Config key |
|-----------|---------|-----------|------------|
| Files per phase | 14 | Agent maintains full context of changed files | `max_files_per_phase` |
| New files per phase | 8 | Limits blast radius of new abstractions | `max_new_files` |
| LOC per phase | 1200 | Keeps changes reviewable in one pass | `max_loc` |
| Modified files | 12 | Prevents scattered, hard-to-review diffs | `max_modified_files` |

## 7) Execution Modes

### CL (Chat Loop) — default
- AI proposes steps, human approves/executes.
- AI does NOT execute external actions without approval.

### AG (Autonomous) — explicit request only
- AI works independently within approved TS scope.
- Makes incremental commits.
- Stops when encountering issues not covered by TS.

## 8) Workflows

TFW defines the following canonical workflows in `.tfw/workflows/`:

| Workflow | Role | Purpose |
|----------|------|---------|
| [init.md](workflows/init.md) | Coordinator | Discover project → interview → knowledge → setup → verify |
| [plan.md](workflows/plan.md) | Coordinator | Research → HL → RESEARCH gate → scope decision → TS |
| [research/base.md](workflows/research/base.md) | Researcher | Structured investigation → RES artifact (pipeline or standalone) |
| [handoff.md](workflows/handoff.md) | Executor | Context load → ONB → execute → RF |
| [review.md](workflows/review.md) | Reviewer | Read RF → checklist → verdict → tech debt → traces |
| [resume.md](workflows/resume.md) | Coordinator | Locate task → status matrix → decide next phase |
| [docs.md](workflows/docs.md) | Coordinator | Update KNOWLEDGE.md and TECH_DEBT.md after task completion |
| [knowledge.md](workflows/knowledge.md) | Coordinator | Consolidate fact candidates into verified project knowledge (Orient → Gather → Consolidate → Prune) |
| [release.md](workflows/release.md) | Coordinator | Read RELEASE.md → scope release → version bump → CHANGELOG → tag |
| [update.md](workflows/update.md) | Coordinator | Fetch upstream → compare versions → categorize changes → update checklist → re-sync adapters |
| [config.md](workflows/config.md) | Coordinator | Interactive config change → propagate to all inline values |

## 9) Tool Adapter Pattern

`.tfw/` is the tool-agnostic core — one copy per project. Each development tool reads its own entry point, which references `.tfw/`:

```
CLAUDE.md ──→ "Read .tfw/README.md, follow .tfw/conventions.md"
.cursor/rules ──→ "Read .tfw/README.md, follow .tfw/conventions.md"
.agent/rules ──→ "Read .tfw/README.md, follow .tfw/conventions.md"
AGENTS.md + .agents/skills/tfw-*/SKILL.md ──→ Codex `/tfw-*` command routing
```

Adapters are chosen at project init. See `.tfw/quickstart.md` for setup.

For Codex, `/tfw-*` is the primary human-facing command contract. Root `AGENTS.md`
provides always-on recognition and fallback routing; repository-local skills provide
discoverability and progressive workflow loading. Skills are implementation, not a
separate wrapper users must learn. Adapter source lives in `.tfw/adapters/codex/` and
installed copies live in `.agents/skills/tfw-*/`.

## 10) Context Loading Order (new session, strict)

1. `AGENTS.md`
2. `.tfw/conventions.md`, `.tfw/glossary.md`
3. `KNOWLEDGE.md` (if exists)
4. Relevant HL/TS/RF for the current task

## 10.1) Fact Categories

> Universal categories for Fact Candidates. Open list — agents can use custom categories when none fit.

| Category | Scope | Examples |
|----------|-------|----------|
| `environment` | Where the work lives | servers, tools, platforms, classrooms, labs, hosting |
| `process` | How work gets done, business processes | schedules, approvals, reporting cadence, grading cycles |
| `stakeholder` | Who needs what | priorities, pain points, expectations, quotes, key decisions |
| `constraint` | What limits exist | contractual obligations, regulatory deadlines, resource caps, technical limits |
| `convention` | Agreed standards | naming, style, format, language, tone |
| `domain` | Subject matter knowledge | revenue patterns, client segments, market metrics, business rules, curriculum |
| `context` | Background that shapes decisions | market conditions, competitive landscape, regulatory changes, prior decisions |
| `risk` | Known dangers | client concentration, market dependency, knowledge silos, fragile dependencies |
| `philosophy` | Values, principles, vision | design rationale, methodology beliefs, north star decisions, "why we do it this way" |

## 10.2) Knowledge Infrastructure

| File | Purpose |
|------|---------|
| `knowledge/` | Project root folder for topic files (per-category verified facts) |
| `knowledge/{category}.md` | Topic file — verified facts for a category. Template: `.tfw/templates/topic_file.md` |
| `.tfw/knowledge_state.yaml` | Consolidation tracking: last seq, date, statistics |
| `.tfw/workflows/knowledge.md` | 4-phase consolidation workflow (Orient → Gather → Consolidate → Prune) |
| `tfw.knowledge` in project_config.yaml | Configurable limits: interval, gate_mode, max_index_lines, max_facts_per_topic, max_topic_files |

## 10.3) File Classification in `.tfw/`

`.tfw/` contains three categories of files with different lifecycle rules:

| Category | Files | Init | Update | Owner |
|----------|-------|------|--------|-------|
| **Framework** | workflows/, templates/, conventions.md, glossary.md, README.md, CHANGELOG.md, VERSION, compilable_contract.md, quickstart.md, adapters/ | Copy from upstream | Overwrite/merge from upstream | Upstream repo |
| **State** | knowledge_state.yaml | Create from template | **NEVER** overwrite | Project (tfw-knowledge) |
| **Config** | project_config.yaml | Create from template → fill project values | Merge: framework sections update, project sections preserve | Project + upstream |

**Templates** for state and config files: `.tfw/templates/knowledge_state.yaml`, `.tfw/templates/project_config.yaml`.

**Rule:** `init.md` and `update.md` MUST respect these categories. State files are NEVER sourced from upstream — only from templates.

## 10.4) YAML File Naming Convention

All YAML configuration and state files in `.tfw/` use `lower_snake_case` naming:
- `project_config.yaml` (not `PROJECT_CONFIG.yaml`)
- `knowledge_state.yaml` (not `KNOWLEDGE_STATE.yaml`)

Markdown templates in `.tfw/templates/` also follow `lower_snake_case`:
- `topic_file.md` (not `TOPIC_FILE.md`)

Uppercase names are reserved for project-root documents (`KNOWLEDGE.md`, `TECH_DEBT.md`, `AGENTS.md`) and `.tfw/` framework docs (`CHANGELOG.md`, `VERSION`).

## 11) Quality Standard (no compromises)

- No placeholders.
- Results must be usable without manual edits.
- If a result is wrong — fix the prompt/context and retry until quality is met.
- Tasks are atomic and human-verifiable.
- **Content Language:** Template structure (headings, labels, field names) is always English.
  Artifact content is filled in the language specified by `tfw.content_language` in project_config.yaml.
  Default: `en`. Agent MUST check this value before writing artifacts.

### Design Rules

- **Instruction attention (transitional)**: workflow instructions currently retain the
  `≤1200`-word control. Phase A neither validates nor removes it; use the
  [Numeric Control ledger](#transitional-restore-owner-or-retire-ledger) until its owner
  defines the counting unit and response or retires normativity.
- **Rule Deployment**: choose locality from the protected consequence and observable
  gate in [§1.1](#rule-record-and-rule-deployment). Complete local imperatives remain
  mandatory before role, safety, destructive, and irreversible actions.
- **Ref-inside-step**: a step is self-contained about the action and observable gate;
  its canonical reference supplies definition or precision. A bare recommendation or
  remote link is not enforcement.
- **Progressive Disclosure**: load only the contracts and reference material required
  at the current decision point. Do not turn deferred libraries or modes into universal
  startup context.

## 12) Safety and Execution Honesty

- In CL mode, never claim something was "run" or "tested" outside the session.
- Never request secrets in plain text. Use environment variables.
- Evidence requires real-environment observation — deploying, opening, running, or viewing completed work in conditions beyond the build/test toolchain. VERIFIED status requires an artifact reference (file path or inline output).

## 13) Trace Discipline

Every task produces an **RF file** with results, decisions, and observations. The **Task Board** in README.md tracks all task statuses. Together, these form the project's memory across sessions.

## 14) Anti-patterns (prohibited)

- Executor starts coding before all blocking questions resolved
- Executor skips reading HL and goes straight to code
- Coordinator skips review and closes without REVIEW file
- RF file doesn't mention test results or observations
- TS is written without an approved HL
- Executor modifies Master HL without coordinator approval
- Executor makes architectural decisions not in HL
- Executor modifies files outside TS scope (even "obvious fixes")
- Executor does "bonus fixes" without documenting in RF deviations
- Executor writes RF before build/lint passes
- Executor sees tech debt / dead code but doesn't report in Observations
- Coordinator ignores executor Observations — must triage to TECH_DEBT.md
- Coordinator writes ONB, RF, or implements code → **Role Lock violation**
- Executor writes HL, TS, or changes scope → **Role Lock violation**
- Executor writes REVIEW file → **Role Lock violation**
- Reviewer approves without opening any files — Step 2 (Verify) requires spot-checking RF claims against actual artifacts
- Executor omits RF §7-9 (Fact Candidates, Strategic Insights, Diagrams) — sections are mandatory; empty content ("No X.") is valid, absent section is not
- Researcher omits Findings Map in RES — section is mandatory; "No findings map." is valid if genuinely no visualization relevant
- Coordinator reads KNOWLEDGE.md in context loading but never cites relevant items in HL §4 — "read but don't use" pattern breaks cross-task knowledge flow
- TS contains ready-made implementation — TS §5 must contain acceptance criteria (WHAT), not code or steps (HOW); implementation belongs to executor
- Coordinator reads own TS instead of RF when planning next phase — before writing TS for Phase N, read RF of the latest completed phase; plan ≠ fact
- Executor writes RF without opening template — RF template must be opened before writing; writing from memory drifts from required structure
- Coordinator answers ONB questions without source — when uncertain, present options and context, not decisions on behalf of the stakeholder
- Executor marks evidence VERIFIED without artifact reference in `evidence/` folder — assertion without evidence
- Executor marks evidence N/A without justification from TS Evidence field or documented reason
- Executor writes RF §5 Evidence before actually collecting evidence — evidence must be contemporaneous, not reconstructed
- Reviewer approves RF without checking that evidence artifact references resolve to real files or inline output
- Executor marks evidence DEFERRED without naming the specific blocker (missing environment, unavailable device, pending deployment)

### 14.1 Terminology Origin (maintainer reference)

The following terms used in research stage templates are TFW-native and intentionally avoid methodology names:

| TFW Term | Meaning | Origin |
|----------|---------|--------|
| Dimension | An independent decision factor (degree of freedom) in the problem | Zwicky's GMA: "parameter" |
| Alternative | One valid value for a Dimension | Zwicky's GMA: "parameter value" |
| Configuration Space | The full cross-product of all Dimension alternatives | Zwicky's GMA: "morphological box" |
| Consistency Check | Pairwise incompatibility analysis eliminating invalid combinations | Zwicky's GMA: "cross-consistency assessment (CCA)" |
| Surviving Configuration | A configuration that passed all pairwise checks | Zwicky's GMA: "compatible solution" |

> **Scope:** This note is for framework maintainers only. The terms "Zwicky", "GMA", "General Morphological Analysis", "morphological box", and "cross-consistency assessment" MUST NOT appear in any researcher-facing template or workflow instruction.

## 15) Role Lock Protocol

Each workflow declares a **🔒 ROLE LOCK** at the top. The agent MUST refuse any action outside the locked role.

| Workflow | Role Lock | Permitted Artifacts | Forbidden Artifacts |
|----------|-----------|---------------------|---------------------|
| `init.md` | Coordinator | RES, RF, project config files | HL, TS, code |
| `plan.md` | Coordinator | HL, TS | ONB, RF, RES, REVIEW, code |
| `research/base.md` | Researcher | RES, research/ stage files | HL, TS, ONB, RF, REVIEW, code |
| `handoff.md` | Executor | ONB, RF, code | HL, TS, RES, REVIEW |
| `review.md` | Reviewer | review stage files (map.md, verify.md, judge.md), REVIEW | ONB, RF, HL, TS, code |
| `resume.md` | Coordinator | Status matrix, Phase HL, Phase TS | ONB, RF, RES, REVIEW, code |
| `docs.md` | Coordinator | KNOWLEDGE.md, TECH_DEBT.md | code |
| `release.md` | Coordinator | VERSION, CHANGELOG.md | code |
| `update.md` | Coordinator | `.tfw/` files, adapter copies | code |
| `config.md` | Coordinator | project_config.yaml, workflow files, convention files, adapter copies | code |

### Hard Stop Rule

When a Coordinator reaches the end of planning (TS approved), the correct action is:
1. Inform the user that planning is complete
2. Instruct: "Start `/tfw-handoff` to begin execution"
3. **Do NOT continue into execution**

When an Executor finishes RF, the correct action is:
1. Inform the user that execution is complete
2. Instruct: "Start `/tfw-review` to review the results"
3. **Do NOT write a REVIEW file**

When a Researcher finishes RES, the correct action is:
1. Inform the user that research is complete
2. Instruct: "Continue with `/tfw-plan` to apply research findings"
3. **Do NOT write HL or TS**

## 16) Compilable Contract

> Build-time specification for deterministic compilation of TFW artifacts into documentation.
> Defines the Source Manifest, Reference Format, and Output Structure.
> Full contract: [compilable_contract.md](compilable_contract.md)
