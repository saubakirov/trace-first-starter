# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-48](../../HL-TFW-48__value_first_methodology_rebaseline.md)
> Briefing: [Iteration 2 Briefing](1_briefing.md)
> Predecessor: [Iteration 1 RES](../iter1/RES.md)
> Goal: Re-derive TFW from its product purpose and production learning so that a proportionate method kernel preserves meaning, evidence, independent judgment, and portable knowledge across routine and high-risk work in multiple domains.
> Mode: Pipeline — Deep

## Corpus and Method

This Gather challenges Iteration 1's failure-selected baseline with successful routine or
low-execution-risk cases. It is a bounded multiple-case comparison, not a prevalence
estimate and not a controlled model-era study.

### Predeclared case criteria

The criteria below were frozen before case selection.

| Criterion | Operational rule |
|-----------|------------------|
| Success | A completed positive REVIEW, an explicit owner-approved closure ledger, or a completed RES whose recommendations were subsequently implemented and approved. A Task Board checkmark alone is insufficient. |
| Routine / low risk | The selected unit uses an established workflow, is reversible or additive, has bounded blast radius, and is not an emergency, destructive migration, live security cutover, or known incident investigation. For research/docs units, execution risk and decision impact are recorded separately. |
| Independence | One case represents one independently reviewable task or phase outcome. Multiple phases of one outcome count as one case; known predecessor/fix chains are not treated as independent confirmations. |
| Exclusion | Exclude Iteration 1 failure anchors, tasks without outcome evidence, high-risk production/security/migration work, unresolved REJECT/REVISE units, duplicate phases of one change, and cases selected only because their traces are easy to read. |
| Stop/expand | The initial target is two software cases per production project plus four non-code cases. Continue only while a new case changes a rule-locality, limit, learning, extension, review, or feasibility disposition; stop after project/domain coverage and semantic saturation, documenting shortfalls. |

This follows the distinction between a planning target and an evidence-based stopping
decision. A recent synthesis on
[information power and saturation](https://academic.oup.com/eurjcn/advance-article/doi/10.1093/eurjcn/zvag046/8487364)
warns against treating suggested sample counts as cutoffs and recommends explicit
depth/breadth and limitation reporting. The transfer is methodological: these traces
are cases, not interview participants.

### Source boundaries

- Read-only production roots remained Atamat (`D:\projects\research\atamat`),
  Helpdesk (`D:\projects\research\helpdesk`), and AFD
  (`D:\projects\research\ai-first-devices`).
- Existing safe-memory authorization remained available for discovery, but no personal
  memory was needed to select or verify the routine cases.
- No production file, predecessor trace, coordinator-owned file, implementation, or H4
  comparison task/model was changed or executed.
- External sources were used for sampling adequacy, measurement validity, provenance,
  crossover validity, and dated model-cost inputs.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1 — Rule consequence | Reversible explanation/reference | Observable lifecycle or navigation error | False evidence/value judgment | Pre-action role, safety, destructive, or irreversible breach |
| D2 — Rule locality | Canonical reference only | Canonical owner + short local cue | Canonical owner + local observable gate | Full local imperative + hard gate |
| D3 — Task exposure | Routine and local | Reversible cross-seam | External-source or stakeholder-facing | High-risk/irreversible |
| D4 — Numeric semantics | Boundary | Escalation trigger | Attention warning / sampling default | Target / descriptive measurement |
| D5 — Numeric owner | Framework invariant | Workflow default | Project calibration | Task-specific override |
| D6 — Learning entry | Every completed artifact | Event-triggered durable/contradictory signal | Coordinator-selected batch | Remain task-local / reject |
| D7 — Learning receipt | None | One-line disposition and reason | Source↔destination backlink | Central lifecycle registry |
| D8 — Project extension form | Inline root instruction | Project config block | Registered/versioned extension | Direct upstream-core fork |
| D9 — Value proof | Local artifact verification | Interface/seam proof | Stakeholder/end-to-end validation | Explicit value debt with due validation |
| D10 — Review packaging | One compact review | Staged logs + synthesis | Risk-triggered expansion | Grouped cross-phase value/seam review |
| D11 — H4 evidence scope | Protocol feasibility only | Small protocol rehearsal | Variance calibration pilot | Inferential matched-strategy trial |
| D12 — H4 resource surface | Codex credits | API-token equivalent | Human scoring/reconciliation | Researcher case construction/analysis |

## Findings

### G1. Candidate pool, selections, and exclusions

The initial pool was derived from Task Boards before opening detailed case artifacts.
The table exposes both selected and excluded candidates so the final set is not presented
as if it were inevitable.

| Project/domain | Candidate | Disposition | Reason |
|----------------|-----------|-------------|--------|
| Atamat software | TFW-2.127 City & Language Propagation | Selected | Additive bounded fix; APPROVED; tests and targeted source checks recorded |
| Atamat software | TFW-15 Follow-Up Buttons UX | Selected | Reversible UI change; 10/10 AC; APPROVED; no fixups |
| Atamat software | TFW-2.121 Security Hardening | Excluded | Security boundary, not low-risk |
| Atamat software | TFW-5 Yandex Cloud Migration | Excluded | Irreversible infrastructure/migration exposure |
| Atamat software | TFW-2.100 Backend Refactoring Audit | Excluded | Iteration 1 failure anchor |
| Helpdesk software | HD-7 Phase A Frontend i18n | Selected | Additive frontend infrastructure; APPROVE; build and source checks |
| Helpdesk software | HD-8 Phase D Numbering + Deep Linking | Selected | Bounded additive cross-layer feature; APPROVE; 10/10 files checked |
| Helpdesk software | HD-10 Production Release | Excluded | Production deployment exposure |
| Helpdesk software | HD-26 / HD-30 | Excluded | Iteration 1 failure anchors |
| AFD software | AFD-25 Maven Publish | Selected | Three-file build-tool change; local publish proof; APPROVE |
| AFD software | AFD-32 Bus Display ID Flag | Selected | Default-off additive flag; ~80 LOC; APPROVE; deferred field proof explicitly bounded |
| AFD software | AFD-36 / AFD-38 / AFD-49 | Excluded | Resilience, security, or field-release risk |
| Non-code design | TFW-27 Phase A Brand Identity | Selected | Reversible branding/docs/config unit; owner-approved deviation; APPROVE |
| Non-code documentation | HD-24 Phase A+B Documentation Package | Selected as one case | Docs-mode APPROVE; code/source fidelity verified; two phases implement one package |
| Non-code research | TFW-46 Iteration 2 Evidence Layer | Selected | Research execution is reversible; RES fed a completed, approved implementation; decision impact remains high |
| Non-code operational coordination | AFD-51 Phase A YC Contract & Boundary | Selected | Docs-only, scope-locked coordination package; 100% source review; APPROVE |
| Non-code content | TFW-36 Phase A Content Strategy | Excluded from routine set; retained as counter-case | Final output approved, but three data-integrity incidents make it a failure-bearing source-verification case |
| Non-code operational decision | AFD-31 Industrial Deploy closure | Excluded from routine set; retained as contrast | Incident-driven/high-impact; explicit owner closure but no independent REVIEW |
| Non-code knowledge | AFD-30 Knowledge Actualization | Excluded | Task says DONE but has no REVIEW artifact |

The selected set is six independent software cases and four non-code cases. The final
two cases added new examples—inline review packaging and source-to-contract
traceability—but no new dimension or mechanism class. Gather therefore reached
semantic saturation for the registered focus at the approved initial coverage target.
This does not estimate how often any mechanism succeeds or fails.

### G2. Routine software cases expose proportionality, not absence of controls

| Case | Success evidence | Control that carried the value | Observed overhead or gap | Hypotheses |
|------|------------------|--------------------------------|--------------------------|------------|
| Atamat TFW-2.127 | APPROVED; targeted inspection; 545 pass, 9 disclosed pre-existing fail, 4 skip | Direct source checks for the language/city chain plus regression tests | One 51-line REVIEW; no staged review or learning receipt; six observations routed informally | H1, H3 |
| Atamat TFW-15 | APPROVED; 10/10 AC; build passes | Compact AC/source review plus ONB recommendations | One 56-line REVIEW. Implementation estimate grew from ~130 to ~165 LOC for useful accessibility/catch-all additions and was accepted | H1, H2, K3 |
| Helpdesk HD-7/A | APPROVE; 16/~22 files (73%); typecheck/build; locale source checks | Cross-file source sampling, build, terminology/source verification | 308 review lines across four artifacts. Missing RF §5–§8 did not block a correct result; reviewer created two FCs afterward | H1, H3, K3 |
| Helpdesk HD-8/D | APPROVE; 10/10 files; 11/11 AC; security checks | Full cross-layer source verification and coordinator-approved deviations | 276 review lines. No new tests accepted as non-blocking. A local `<50 LOC and adds integrity` scope heuristic was promoted as a candidate, not validated universally | H1, H2, H3 |
| AFD-25 | APPROVE; 3/3 files; build + local publication + negative-scope checks | Executable build/publish evidence exactly at the changed seam | One 139-line REVIEW. Existing Docker-related failure was disclosed and excluded; one environment FC routed | H1, H3, K3 |
| AFD-32 | APPROVE; 10/10 files; 5/7 evidence verified, 1 deferred, 1 unchecked | End-to-end source path, migration tests, default-off compatibility, explicit evidence statuses | ~80 implementation LOC produced 294 review lines across four artifacts. One FC was explicitly rejected as duplicate—a useful receipt | H1, H2, H3, K3 |

The cases challenge two possible overreactions:

1. **“Routine success needs no kernel.”** False. Every case depended on at least one
   value-carrying control: source checks, executable evidence, explicit deviation
   authority, or independent review.
2. **“Every kernel obligation needs a full artifact stack.”** Also false. The two
   successful Atamat cases used compact single reviews. Later staged reviews produced
   stronger traceability, but 276–308 review lines for bounded work show a real
   proportionality cost.

The correct unit to test in Extract is therefore the obligation and its evidence, not
the presence of a particular section or number of stage files.

### G3. Non-code work changes which seam must be reviewed

| Case | Decisive truth seam | Review/value behavior | Learning behavior | Hypotheses |
|------|---------------------|-----------------------|-------------------|------------|
| TFW-27/A Brand Identity | HL concept ↔ generated assets/config ↔ owner judgment | 8/8 AC; owner-approved PNG-for-SVG deviation; user refinements accepted as refinements rather than hidden scope | Two candidates; knowledge/docs deferred to task completion | H1, H3, K3 |
| HD-24/A+B Documentation | TS/doc claims ↔ actual code and source facts | 4/6 deliverables inspected (67%); 3 TS/code and 6 additional reality corrections; missing generic RF sections did not block docs quality | Seven candidates deferred to batch; no compact per-item disposition receipt | H1, H3, K3 |
| TFW-46 Iteration 2 Research | Research claim ↔ external/tool evidence ↔ later approved implementation | Five investigated areas; 1,073 lines across briefing, stages, and RES; evidence proportionality explicitly allowed N/A | Research decisions became D52/D53 after implementation/review, but the closure is visible only by following later task artifacts | H3, K3 |
| AFD-51/A Operational Contract | Delivered cross-project handoff ↔ source code ↔ durable responsibility contract | Four docs read 100%; code claims checked; live infrastructure explicitly DEFERRED. Owner chose one 86-line inline REVIEW and no map/verify/judge files to avoid artifact proliferation | Gaps have one owner; two process candidates deferred to task close with stated route | H1, H3, K3 |

TFW-36 is decisive counter-evidence against “routine non-code review can reuse code
checks.” A content deliverable reached approval only after three claim-integrity
incidents were repaired, including fabricated or misattributed external claims that
traversed multiple roles. The missing control was not more generic review text; it was a
source-audit seam appropriate to public claims.

The non-code cases support **claim-typed review**:

- design may require owner/stakeholder judgment;
- documentation requires source-to-document fidelity;
- research requires evidence and rival-explanation discipline;
- operational coordination requires authority, ownership, and delivered-contract
  fidelity;
- public content requires external-claim verification.

They do not support one universal visible-demo requirement or one universal review
package.

### G4. Rule locality: observable gates outperform both extremes

#### Current deployment patterns

| Rule class | Canonical owner | Local form observed | Observable enforcement | Routine-case signal |
|------------|-----------------|---------------------|------------------------|---------------------|
| Role authority | `conventions.md` §14 plus workflow ownership | Full `ROLE LOCK` imperative in eight canonical workflows; the Codex skill repeats the allowed/forbidden artifact boundary | Attempted write is permitted/refused before action | No routine case justifies weakening this pre-action boundary |
| Evidence honesty | `conventions.md` §12 and Evidence vocabulary | TS Evidence field, handoff collection step, review evidence audit | Command/source/artifact/environment can be inspected | AFD-25/32 show narrow executable evidence; reference-only would be weaker |
| Lifecycle WAIT/STOP | Research/review workflows | Short point-of-use gate and required stage artifact/status | File/state transition is visible | This Iteration 2 briefing gate worked without restating all research rationale |
| Source fidelity | Domain artifact or cited authority | Local citation/source check in docs/research/content review | Source and derived claim can be compared | HD-24/AFD-51 succeeded; TFW-36 failed before this seam was made explicit |
| Configured attention policy | `project_config.yaml` plus inline value | Literal value repeated through Pattern A and Config Sync Registry | Count can be observed, then split/override | The exact number often lacked a defined response or current evidence |
| Project-specific policy | Root instructions, config comments, project knowledge | Loaded before/with framework; no registered extension record | Depends on agent discovery and manual precedence | AFD uses project overrides and custom config successfully, but ownership is comment-based |

The current framework provides a live maintenance counterexample to unqualified Pattern
A repetition:

- Config Sync Registry omits `research.min_iterations`,
  `knowledge.max_index_lines`, and `knowledge.max_index_facts_lines`.
- The registry says knowledge values appear in a `knowledge.md` **Limits** section, but
  the current workflow has no such section.
- `research.max_passes: 3` is displayed, but the OODA algorithm actually uses
  per-mode `loops_per_stage`; no step consumes `max_passes`.

This does not falsify local cues. It shows that literal local derivatives need visible
source version/freshness or an executable sync check. The five-field rule record from
Iteration 1 remains plausible, with an important refinement: a local copy and a local
gate are different things.

### G5. Complete active numeric ledger

Type is recorded before any threshold judgment. “Source sufficiency” distinguishes
evidence for the protected mechanism from evidence for the exact numeric value.

#### Config-backed values

| Value | Type first | Owner / consumer | Protected failure or invariant | Counting rule and breach response | Override authority | Observed behavior | Source sufficiency for exact value |
|-------|------------|------------------|--------------------------------|-----------------------------------|--------------------|-------------------|------------------------------------|
| `max_files_per_phase: 14` | Attention warning | Project config → plan Step 7 | Too many changed surfaces for one coherent phase/review | Count planned files; split or document override | Coordinator + owner/project config | Defaults vary Atamat/TFW 14, Helpdesk 35, AFD 75 | None; rationale supports measurement, not 14 |
| `max_new_files: 8` | Attention warning | Project config → plan Step 7 | New-abstraction blast radius | Count planned new files; split or justify | Coordinator + owner/project config | Values vary 8/18/50 across the three project eras | None for 8 |
| `max_loc: 1200` | Attention warning | Project config → plan Step 7 | Review/context overload | Estimate changed LOC; split or justify | Coordinator + owner/project config | Values vary 1200/3500/4500; Iteration 1 found proxy/reclassification behavior | Evidence of proxy risk; none for 1200 |
| `max_modified_files: 12` | Attention warning | Project config → plan Step 7 | Scattered diff | Count modified files; split or justify | Coordinator + owner/project config | Values vary 12/26/75 | None for 12 |
| `max_web_queries_per_stage: 5` | Sampling default | Researcher / base Limits table | Uncontrolled search cost and widening | Count search queries per stage; declared Soft; no canonical breach action | Researcher with recorded reason | This Gather used 10 across four evidence families rather than omit one family | Mechanism/cost rationale only |
| `max_files_per_stage: 15` | Sampling default | Researcher / base Limits table | Context/search sprawl | Count project files opened per stage; Soft; no canonical breach action | Researcher with recorded reason | This Gather exceeded 15 to cover ten cases plus config/protocol sources | Mechanism rationale only |
| `max_questions_per_turn: 3` | Interaction boundary | Researcher / base hard rule | Coordinator/user overload and fragmented answers | Count questions in one turn; hard stop at 3 | No explicit workflow override; coordinator can answer/redirect | Current Briefing used exactly 3; no failure evidence at 2/4 | Coordination rationale only |
| `max_passes: 3` | Declared sampling default, currently unconsumed | Config and base table | Endless OODA looping | No current algorithm consumes it; mode `loops_per_stage` controls loops | Undefined | Duplicates mode-loop concept and has no breach path | None; inactive derivative |
| `min_iterations: 2` | Structural floor with task calibration | Coordinator / plan iteration gate | Premature research closure/confirmation | Count completed iterations; below floor MUST continue | Coordinator may override with justification | TFW-48 Iteration 2 corrected failure-selection bias; TFW-42 and TFW-43 show approved `min=1` exceptions | Mechanism supported; universal default 2 not calibrated |
| focused `loops_per_stage: 1` | Sampling default | Focused mode / OODA | Unnecessary repeated search on bounded questions | Up to one loop; exit on sufficiency | Mode selection and project config | No selected case isolates one loop | None for 1 |
| deep `loops_per_stage: 3` | Sampling ceiling | Deep mode / OODA | Shallow closure on complex uncertainty | Up to three loops; may stop earlier on sufficiency | Mode selection and project config | This Gather used distinct local, external, and counter-evidence passes | Supports multiple loops; not exact 3 |
| `min_verify_ratio: 0.42` then `1.0` on discrepancy | Escalation floor | Reviewer / review Step 3 and mode files | Author claims accepted without independent inspection | Round up `files × .42`; any discrepancy escalates to all files | Project config; no per-review override defined | Selected reviews chose 67%, 73%, or 100%; small/high-seam tasks naturally reached 100%. `0.42` originated as a post-approval user preference replacing “2–3 files” | Independent sampling and escalation supported; 0.42/100% exact values unvalidated |
| `knowledge.interval: 5` | Escalation trigger | Plan knowledge gate | Knowledge backlog grows stale | `current_seq - last_consolidation_seq`; hard stop/reminder/off by gate mode | Project config; skip with justification | Helpdesk/AFD cases often batch at task close, a lifecycle event rather than fifth task | Trigger mechanism supported; 5 was a design preference |
| `max_index_lines: 200` | Target, currently unconsumed | Config only; no current workflow consumer | Root index becomes an unscannable knowledge dump | Intended line count; no current breach response | Undefined/project config | TFW 186, Helpdesk 284, AFD 388 lines; two mature projects exceed it while remaining active | Threshold falsified as a hard boundary; target effect unmeasured |
| `max_index_facts_lines: 30` | Legacy target, currently unconsumed | Config only; prior design referenced removed §5 | Fact index crowds out navigation | No current section/counting/breach path | Undefined | Current KNOWLEDGE topology no longer matches the originating §5 design | No current construct to calibrate |
| `max_facts_per_topic: 50` | Attention warning | Knowledge workflow says “check” | Topic retrieval degrades | Count active fact rows; no defined breach response | Project config/user during consolidation | Helpdesk process = 50; AFD convention = 54 while config remains 50 | Shows boundary is not enforced; no evidence for 50 |
| `max_topic_files: 8` | Attention warning | Knowledge workflow says “check” | Category fragmentation and discovery cost | Count topic files; no defined breach response | Project config/user during consolidation | Helpdesk and AFD both have 8; open taxonomy may require a ninth rather than misclassification | No evidence for 8; possible category-pressure risk |

#### Direct hard-looking numbers consumed by the tested mechanisms

| Value | Type first | Protected mechanism | Breach/override | Gather evidence |
|-------|------------|---------------------|-----------------|-----------------|
| Workflow instructions `≤1200` words | Maintainability/attention target | Keep role runtime instructions scannable | No canonical breach response; current HL records init and handoff above it | Instruction pressure is real; exact ceiling and word counting are unvalidated |
| Adapter content `≤35` lines | Maintainability target | Prevent adapter fork/duplication | No breach response; Codex now uses skill directories rather than one small file | The unit changed; line target is not architecture-neutral |
| Plan questions `max 3–5` | Interaction sampling default | Batch clarification | No relation defined to research hard 3 | Range conflicts with the apparent universal hard 3 |
| Briefing `3–5` bullets per stage | Format target | Force a usable but bounded investigation plan | Template compliance only | No protected failure or evidence for the endpoints |
| Dimension `≥3` alternatives; `<3` dimensions switches method | Structural trigger | Make configuration space possible | Switch to comparison matrix | Mechanism is logically connected to later Extract; exact alternative count is methodological, not empirical |
| Deep stage `min 2` decisions | Output target | Prevent a stage that only summarizes | No exception semantics | This Gather exceeds it naturally; exact 2 not validated |
| Deep stage `min 1` hypothesis | Structural coverage target | Keep deep work tied to HL uncertainty | Stage cannot close without one | Strong traceability mechanism; count 1 is a minimum coverage rule |
| Promoted fact `≥2` independent sources | Corroboration boundary | Prevent weak claims becoming trusted knowledge | One source goes to user confirmation or skip | Iteration 1 already found one authoritative source or explicit owner decision can suffice; universal 2 is over-broad |
| Fact staleness `>20` tasks | Escalation warning | Surface possibly obsolete knowledge | Flag only; user decides; no deletion | No current threshold evidence; task cadence varies |
| Research `max_iterations: 5` | Soft cost ceiling | Prevent endless full iterations | Coordinator-owned control file; no fixed breach algorithm | No evidence for 5; TFW-48 registry uses it as a planning cap |
| Evidence folder `≥1` structured EV | Structural existence gate | Make live evidence discoverable and non-optional | Current handoff/review should reject missing evidence structure | Older successful cases predate it; current evidence-layer decisions support the structural gate, not an output-count target |

#### Numeric conclusions that Gather can and cannot support

- The corpus supports **typing, ownership, observable breach response, and override
  recording** before a number governs behavior.
- It supports scope counts, search caps, review ratios, and knowledge sizes as useful
  signals or planning defaults.
- It does not validate a single current numeric value as a universal performance optimum.
- Some values need no calibration because their construct has disappeared
  (`max_index_facts_lines`) or their consumer is missing (`max_passes`,
  `max_index_lines`).
- Absence of a recorded incident was never treated as validation or invalidation.

NIST's
[AI RMF Measure guidance](https://airc.nist.gov/airmf-resources/playbook/measure/)
independently requires metric selection to follow purpose/context, acceptable limits to
include course-correction behavior, unused metrics to be documented, and measurement
effectiveness to be reassessed. It supports the ledger fields, not any TFW threshold.

### G6. K3 overhead: semantics survive, uniform packaging does not

The selected cases provide a rough trace-cost observation:

| Case | Review artifact count | Review/stage lines | Work scale signal |
|------|-----------------------|--------------------|-------------------|
| Atamat TFW-2.127 | 1 | 51 | Targeted fix, tests and spot checks |
| Atamat TFW-15 | 1 | 56 | ~165 LOC UI change |
| Helpdesk HD-7/A | 4 | 308 | ~22 implementation files |
| Helpdesk HD-8/D | 4 | 276 | 10 implementation files |
| AFD-25 | 1 | 139 | 3 implementation files |
| AFD-32 | 4 | 294 | ~80 implementation LOC / 10 files |
| TFW-27/A | 1 | 57 | Branding/docs/config output |
| HD-24/A+B | 4 | 291 | Six documentation deliverables |
| AFD-51/A | 1 | 86 | Four operational contract docs; staged logs intentionally omitted |
| TFW-46 Iteration 2 | 5 research artifacts | 1,073 | High-impact methodology research, low execution irreversibility |

These line counts are descriptive, not direct cost or quality measures. They still
falsify “more trace files are free.” AFD-32 is the clearest routine overhead case:
review traces are several times the implementation LOC. AFD-51 is the useful
counter-configuration: it retained map/verify/judge distinctions inline, read 100% of
four docs, and explicitly skipped separate stage files under an owner “do not
proliferate artifacts” decision.

K3's candidate obligations remain visible in successful cases:

1. product purpose or governing principles were checked when material;
2. lifecycle/authority was explicit;
3. evidence or source reality could overrule document agreement;
4. a distinct reviewer or owner judgment occurred;
5. reusable observations had some disposition.

What does **not** survive as an automatic routine obligation is a full set of staged
files, a generic diagram/insight section, or a multi-item learning transaction when the
entry predicate finds no durable signal.

### G7. Learning receipts and project extensions

#### Receipt observations

| Case | Signal disposition observed | Receipt quality |
|------|-----------------------------|-----------------|
| AFD-32 | One FC rejected as duplicate of an existing philosophy fact | Strong: state, reason, and existing owner are visible in one paragraph |
| HD-8/D | Three FCs plus one review FC deferred; file also says `fact-candidates: processed` | Ambiguous: “processed” and “deferred” can be read as conflicting states |
| HD-24/A+B | Seven candidates deferred to batch; trace-update boxes remain unchecked | Weak: no per-item destination, owner, or due event |
| AFD-51/A | Two process candidates deferred to task close with reason and target workflow | Stronger: entry event and route are explicit, though no backlink exists yet |
| TFW-36/A counter-case | Some candidates applied, others pending, source contamination corrected | Partial but auditable: per-item state matters more than one artifact-level marker |

The minimum useful receipt observed is not a new document. It is a relation:

`source signal → disposition → destination or reason → responsible actor/due event`.

The [W3C PROV-O Recommendation](https://www.w3.org/TR/prov-o/) supplies an external
minimum vocabulary—entity, activity, agent, derivation, generation, attribution—that
can express that relation without requiring a full RDF implementation. For TFW, the
value is the distinction among the source entity, routing activity, resulting entity,
and responsible role.

#### Extension observations

- AFD 0.9.0 marks its scope budgets as a project override and uses
  `75/50/4500/75`, while Helpdesk uses `35/18/3500/26` and Atamat retains
  `14/8/1200/12`. This is effective project calibration but not a controlled model-era
  result.
- AFD also places a project-owned `dispatch.retention_days: 30` block inside
  `tfw:`. Ownership and runtime meaning live in comments, not a registered schema.
- Root `AGENTS.md`/`CLAUDE.md` files carry project behavior and load before framework
  references, but conflict precedence is not declared by a machine-readable extension.
- Current Codex installed `tfw-research` and `tfw-plan` skills hash-match their adapter
  sources. That is a positive parity observation, but no manifest exposes source
  version, last sync, or stale state to a Researcher.
- The current Config Sync Registry is itself incomplete, proving that a registry needs
  a completeness consumer rather than trust in manual registration.

The extension problem is therefore not “where can text be placed?” Projects already
have several locations. The missing behavior is registered discovery, precedence,
version/freshness, consumer coverage, and visible failure when an extension cannot be
loaded or migrated.

### G8. Value/seam review can be narrow and scheduled

| Seam type | Cases | Sufficient local proof | Deferred/grouped proof |
|-----------|-------|------------------------|------------------------|
| Single-surface UI/design | Atamat TFW-15; TFW-27/A | AC/source inspection, build, owner visual judgment | None when the delivered surface itself is the value |
| Cross-layer software | HD-8/D; AFD-32 | Both sides of the data/route/flag contract checked | AFD-32 on-device proof explicitly deferred; due event must remain findable |
| Build/package boundary | AFD-25 | Build + `publishToMavenLocal` + negative-scope checks | Remote publishing was intentionally env-gated, not represented as done |
| Source-to-document | HD-24/A+B | Code/source claims checked against docs | Batch knowledge closure can follow after task completion |
| Cross-project operational contract | AFD-51/A | Delivered handoff + source code + one-owner gaps | Live YC validation deferred to the execution phase that owns the environment |
| Public factual content | TFW-36/A counter-case | Source audit per material claim | Generic artifact conformance is insufficient |

This supports three separable obligations:

1. local verification of the phase output;
2. seam proof when another component/source/authority is part of the claim;
3. stakeholder or live end-to-end validation at the earliest honest due event.

Grouping (2) or (3) can reduce repetition, but the owner and due event must be explicit.
NIST Measure guidance similarly ties evaluation to purpose, operational context, and
independent assessors rather than to one universal inspection percentage.

### G9. H4 feasibility inputs and dated cost envelope

No H4 cell was created, dispatched, forked, or executed. The following is a planning
model only.

#### Protocol basis carried from Iteration 1

- Two inquiry families: evidence adjudication (`F-E`) and dependency decomposition
  (`F-D`).
- Two profile packages, treated as surface+model+system+tool bundles rather than pure
  capability levels.
- Focal calibration conditions: `B0`, `O-M`, `O-X`, and `L`.
- Main design conditions: `B0`, `BT`, `C`, `N`, `O-M`, `O-X`, and `L`.
- Strategy-neutral outcome items, family-typed hard failures, condition-masked scoring,
  and four confirmatory contrasts.
- Fresh isolated contexts are required because exposure to one operational strategy can
  carry into later outputs. As a design analogy, FDA-hosted
  [ICH E9](https://www.fda.gov/media/71336/download) notes that crossover efficiency is
  invalidated by carryover unless reversibility conditions are established in advance.
  For H4, isolation—not a conversational “washout”—is the control.

#### Dated rate assumptions — 2026-07-29

The current
[OpenAI Codex rate card](https://help.openai.com/en/articles/20001106-codex-rate-card)
prices token use per million tokens:

| Profile assumption | Input | Cached input | Output |
|--------------------|-------|--------------|--------|
| P1 — GPT-5.6 Sol | 125 credits | 12.5 credits | 750 credits |
| P2 — GPT-5.6 Terra | 62.5 credits | 6.25 credits | 375 credits |
| Equal P1/P2 average used below | 93.75 credits | 9.375 credits | 562.5 credits |

For an API-equivalent currency sensitivity—not a quote for Sol/Terra—the official
[GPT-5.4 API page](https://developers.openai.com/api/docs/models/gpt-5.4) lists
USD 2.50 input, USD 0.25 cached input, and USD 15 output per million tokens. GPT-5.4
prompts above 272k input receive higher rates; the per-run assumptions below remain
well below that threshold.

Per-run planning assumptions carried from Iteration 1:

- input-equivalent tokens: 15k–30k;
- output tokens: 2k–6k;
- isolated-run wall time: 10–25 minutes;
- protocol-failure rerun reserve: 10% of model/run budget;
- no rerun for refusal, weak reasoning, missed evidence, tool misuse, or bad verdict;
- cache sensitivity: 0%, 50%, and 80% of input, because fresh isolation does not imply
  that the platform will or will not cache a stable source prefix.

Formulas:

```text
input_M  = outputs × input_tokens_per_run / 1,000,000
output_M = outputs × output_tokens_per_run / 1,000,000
rate_in  = (1-cache_share) × uncached_rate + cache_share × cached_rate
model_cost = input_M × rate_in + output_M × output_rate
rerun_reserve = base model/run cost × 10%
```

#### Model/credit sensitivity before the 10% rerun reserve

| Design | Base input/output | Cache share | Codex credits, P1/P2 average | GPT-5.4 API-reference USD |
|--------|-------------------|-------------|-------------------------------|---------------------------|
| 40-output rehearsal | 0.60–1.20M / 0.08–0.24M | 0% | 101.3–247.5 | 2.70–6.60 |
| 40-output rehearsal | same | 50% | 75.9–196.9 | 2.03–5.25 |
| 40-output rehearsal | same | 80% | 60.8–166.5 | 1.62–4.44 |
| 112-output pilot | 1.68–3.36M / 0.224–0.672M | 0% | 283.5–693.0 | 7.56–18.48 |
| 112-output pilot | same | 50% | 212.6–551.3 | 5.67–14.70 |
| 112-output pilot | same | 80% | 170.1–466.2 | 4.54–12.43 |
| 220-output illustration | 3.30–6.60M / 0.44–1.32M | 0% | 556.9–1,361.3 | 14.85–36.30 |
| 220-output illustration | same | 50% | 417.7–1,082.8 | 11.14–28.88 |
| 220-output illustration | same | 80% | 334.1–915.8 | 8.91–24.42 |

Add 10% to the selected row for the protocol-failure reserve. Missing cost-stopped
blocks remain missing; the reserve is a budget, not permission to replace bad outputs.

#### Human and elapsed-time sensitivity

Planning assumptions requiring owner validation:

- two condition-masked scorers at 6–10 minutes per output;
- reconciliation = 20% of independent scoring time;
- case construction/source pack/outcome key/hash = 3–6 researcher hours per independent
  case;
- treatment tokenization/profile packaging = 4–8 hours per design;
- analysis/simulation/reporting = 8–16 hours for the rehearsal and 16–32 hours for the
  112/220 designs.

| Design | Case-pack assumption | Serial run hours | Serial hours +10% reserve | Scoring + reconciliation | Researcher time | Total human time |
|--------|----------------------|------------------|---------------------------|--------------------------|-----------------|------------------|
| 40-output rehearsal | 4 cases (2/family), 2 profiles, 4 focal conditions, 8 focal repeats | 6.7–16.7 | 7.3–18.3 | 9.6–16.0 h | 24–48 h | 33.6–64.0 h |
| 112-output pilot | 12 cases, 2 profiles, 4 focal conditions, 16 focal repeats | 18.7–46.7 | 20.5–51.3 | 26.9–44.8 h | 56–112 h | 82.9–156.8 h |
| 220-output illustration | 12 main + 2 pilot case packs assumed from 168 primary + 28 pilot outputs; 24 repeats | 36.7–91.7 | 40.3–100.8 | 52.8–88.0 h | 62–124 h | 114.8–212.0 h |

Parallel execution can reduce elapsed time but not credits, run-minutes, scoring, or case
construction. Human/process cost dominates the published API-reference charge.

#### Lower-cost claim boundary

The 40-output option preserves:

- both inquiry families;
- both profile packages;
- matched versus mismatched operational strategies;
- baseline and length/structure control;
- repeated-run mechanics on a small subset.

It does **not** preserve the Iteration 1 inference standard. Two cases per family cannot
establish the required interval coverage/power or support the four-condition
multiplicity-controlled H4 claim. Its valid output is a protocol-operability,
scoring-agreement, token/runtime, and case-construction estimate. It cannot support or
reject matched-strategy effectiveness.

### G10. Hypothesis status after Gather

| Hypothesis | Gather evidence | Counter-evidence | Provisional stage status |
|------------|-----------------|------------------|--------------------------|
| H1 | Successful cases repeatedly use owned rules plus local source/evidence checks; role/irreversible boundaries remain full local imperatives | Compact Atamat reviews show full staged machinery is unnecessary; Config Sync Registry drift shows literal copies are not gates | Still conditionally supported; locality must be rule/risk typed |
| H2 | Mature projects use different scope calibrations; several values are unconsumed/exceeded; routine cases self-select 67–100% review rather than bind at 42% | Every successful case still used counts, targets, or explicit scope/evidence boundaries; fixed structural floors can prevent premature closure | Mechanism strongly supported; no exact current threshold validated |
| H3 | Selected cases show ambiguous deferred candidates, useful duplicate rejection, event-based closure, and missing backlinks; existing destinations were sufficient | TFW-36 needed a new source-audit control, showing capture/verification moments can still be domain-specific | Supported as dominant, not exclusive; minimum receipt/entry predicate required |
| H4 | Protocol and resource assumptions can now be costed; crossover isolation and scorer controls are clear | No fresh output exists; cheaper option narrows to feasibility; current Deep baseline remains treatment-contaminated | Unresolved/inconclusive by authorization boundary |

## Gather Decisions

These decisions govern evidence handling in Extract; they are not final TFW
recommendations.

1. **G-D1 — Sample sufficiency:** close the routine-case sample at six software and
   four non-code cases. Treat the count as achieved coverage plus semantic saturation,
   not a prevalence threshold.
2. **G-D2 — Numeric disposition:** separate threshold calibration from dead-consumer
   repair. A number with no active construct or breach path cannot be “tuned”; it first
   needs retire/restore/assign-owner analysis.
3. **G-D3 — K3 proportionality:** carry K3 as semantic obligations activated by risk,
   seam, and learning-entry predicates. Do not equate K3 with a mandatory number of
   files/sections.
4. **G-D4 — H4 feasibility:** carry three owner options—40-output protocol rehearsal,
   112-output variance pilot, and illustrative 220-output design—with explicit claim
   boundaries. None is authorized for execution.

## Metacognitive Check

- **What was new rather than confirmatory?** Several active values are not merely weakly
  evidenced: `max_passes`, `max_index_lines`, and `max_index_facts_lines` lack active
  consumers; mature knowledge bases exceed 200/50; the Config Sync Registry points to a
  missing knowledge Limits section.
- **What changed K3?** The kernel candidate survives semantically, but uniform artifact
  packaging does not. AFD-32's 294 review lines for ~80 implementation LOC and AFD-51's
  compact inline review expose a real proportionality axis.
- **What changed H3?** A one-line rejection/local/defer receipt can be enough when it
  names state, reason, destination/owner, and due event. A central lifecycle registry is
  not automatically justified.
- **What challenged the routine sample?** TFW-36 shows that “successful final state”
  can contain serious process failure and must not be mislabeled routine. AFD-31 shows
  that honest closure-without-execution is valuable but belongs to a higher-risk
  contrast, not the low-risk pool.
- **What remains unknowable?** Causal model/profile effects; the prevalence of each
  failure; the optimal numeric values; whether 42% sampling has a defensible detection
  probability; and H4 effect size. Observational traces cannot answer those alone.
- **External-search override:** 10 queries exceeded the soft default of 5. The override
  separated four source families—sampling/measurement, provenance, trial validity, and
  current pricing—rather than dropping a registered Briefing gap. Search count was not
  treated as evidence strength.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Six routine software and four non-code cases met the predeclared frame; exclusions expose the failure/high-risk/no-review pool; the final cases reached semantic saturation. | Extract must convert the dimensions into configurations without claiming prevalence. |
| H1 survives as criticality- and observability-selected locality; full staged packaging does not. | Build the locality decision function and constrained-profile fallback. |
| All active config numbers and directly consumed hard-looking numbers are typed; several have no consumer or breach response; no exact current value is validated. | Produce per-number dispositions and separate dead construct, mechanism, and threshold decisions. |
| K3 obligations appear in successful work, but trace packaging ranges from 51 to 1,073 lines and can dominate small tasks. | Derive entry predicates and minimum evidence/receipt forms. |
| Project calibration and custom policy already work through config/root files, but registration, precedence, freshness, and migration are implicit. | Define and compare minimum extension contracts. |
| Value proof decomposes into local, seam, and due end-to-end obligations across software and non-code claims. | Compare review configurations and due-event ownership. |
| H4 now has dated token/credit/API-reference/human-time formulas for 40, 112, and 220 outputs. | Extract must produce owner decision options and preserve the no-run boundary. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?
- [x] At least one HL hypothesis tested?
- [x] Counter-evidence sought?
- [x] Metacognitive check completed?
- [x] Deep exit: at least two Gather decisions?
- [x] Deep exit: at least one hypothesis tested?

**Recommendation:** Close Gather and proceed to Extract. Additional routine cases are
unlikely to add a new mechanism class; retain the exposed exclusions as Challenge
counter-cases.

**Questions for Coordinator:**

1. Approve closing Gather at the achieved six-software/four-non-code coverage plus
   semantic-saturation rule, or identify a missing domain/project class that should be
   added before Extract.
2. Approve treating unconsumed/orphaned numbers as a separate
   restore-owner-or-retire decision before any threshold calibration.
3. Approve carrying the 40-output option only as a protocol rehearsal with a narrowed
   feasibility claim, never as an H4 effect test.

Stage complete: YES
→ User decision: APPROVED A-C by Coordinator. Close at six independent software
  cases plus four non-code cases under the documented coverage-and-semantic-saturation
  rule; this supports mechanism/configuration analysis, not prevalence or model-era
  causal claims. Preserve excluded failure, security, migration, incident, and
  no-review cases for Challenge. Classify every unconsumed/orphaned number before
  calibration as (1) obsolete/dead policy, (2) intended policy with missing or broken
  consumer/breach path, (3) active consumer with missing registry/ownership
  documentation, or (4) descriptive/config residue. Do not recommend an exact value
  without a semantic owner, observed consumer/enforcement, counting rule, breach
  response, and override authority. Carry the 40-output option only as an
  operability/scoring/cost rehearsal incapable of confirming or refuting H4; the
  112- and 220-output options also remain unapproved. Preserve the
  no-run/no-fork/no-dispatch boundary in Extract.
