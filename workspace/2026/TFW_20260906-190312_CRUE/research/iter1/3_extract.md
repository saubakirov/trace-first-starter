# Extract — «Чего мы не видим в разрозненных находках?»
> **Mindset:** Analyst. Из сырых наблюдений построить структуру и сделать видимыми сочетания, которых не было в Briefing.
> **Test:** «Показывает ли Configuration Space хотя бы одну комбинацию, которой никто не предлагал в Briefing?»
> Parent: [HL-TFW_20260906-190312_CRUE](../../HL-TFW_20260906-190312_CRUE.md)
> Goal: Выпуски TFW должны доходить до существующих проектов как целостные, безопасные и понятные улучшения, позволяя владельцу увидеть пользу, фактический результат, ограничения и следующий шаг без изучения внутреннего устройства TFW.

## Configuration Space

Сырой cross-product 13 Dimensions из Gather содержит десятки миллионов комбинаций, большинство из которых распадается из-за связности application/retry/result или прямо противоречит frozen HL. Поэтому таблица показывает шесть полных архитектурных семейств: в каждой строке заполнены все Dimensions, а очевидно противоречивые семейства перечислены отдельно. Ни одна строка не является рекомендацией до Challenge.

| Config | D1 · Идентичность release payload | D2 · Носитель release-to-receiver контракта | D3 · Наблюдаемое состояние receiver | D4 · Классификация ownership | D5 · Основание действия агента | D6 · Application model | D7 · Поведение при повторе | D8 · Adapter transition | D9 · Verification verdict | D10 · Update record carrier | D11 · Result status vocabulary | D12 · Owner-facing completion | D13 · Legacy `.tfw/README.md` transition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 · Preflight over current carriers | operator-named tag/commit | current distributed prose + release-time invariant tests | clean / identical / customized / unknown | baseline bytes + explicit protected paths | fixed interview with prefilled evidence | in-place exact checklist | equal version reruns completion checks | declared singular→plural path migration for current workflow form | maintainer/receiver suites kept separate | canonical project update report | planned / applied / failed / complete | four benefit blocks + run-result appendix | three-way merge, relocate project additions |
| C2 · Relation graph + update receipt | tag/commit + payload digest | canonical workflow and version guide own rules; checked relations connect existing carriers | all Gather states, including partial | declaration + provenance + semantic role | authority/applicability/materiality gate | stage payload, bounded semantic merges, version after verification | resume from receipt; reconcile evidence before replay | compatibility window for currently supported workflow path | layered payload / route / receiver / agent / owner verdicts | one bounded per-run receipt in declared project location | independent conditions + reason/evidence | one state-aware schema with conditional sections | explicit designation transform preserving project purpose |
| C3 · Immutable release envelope + observed state | versioned bundle with digest envelope | immutable release envelope; human views generated or referenced | desired target + observed receiver generation | typed declaration + provenance + semantic role | delta/conflict-triggered question | desired-state reconciliation from staged candidate | level-based reconcile until observed target matches | provider-version routes in envelope for already supported modes | envelope invariants + layered run evidence | per-run observed-status receipt | desired generation / observed generation / conditions | outcome-first rendering from release definition + run status | managed methodology region + separately owned project-purpose region |
| C4 · Isolated Git candidate | operator-named tag/commit | canonical workflow + version guide references | Git receiver with isolatable candidate | three-way Git diff + ownership declaration | delta/materiality gate | apply in temporary worktree/branch, verify candidate, land reviewed commit | discard/rebuild or resume candidate from commit | version-aware root transition inside candidate | candidate checks, receiver build, post-land verification | candidate commit + linked update report | prepared / verified / landed / briefed / cleanup-resolved | outcome-first summary linked to exact candidate | three-way merge in isolated candidate, preserve relocated text |
| C5 · Journaled in-place compensation | operator-named tag/commit | canonical workflow + explicit step/compensation contract | all Gather states | declaration + provenance | conflict/materiality gate | ordered sub-actions with durable checkpoints and compensations | resume next incomplete safe step or compensate | current supported route with explicit old/new root actions | per-step evidence + layered terminal verdict | append-only run journal/report | condition per obligation; no single version-equals-complete inference | success/refused/interrupted/failure forms | explicit transform with compensation before destructive replacement |
| C6 · Stateless reconcile + version-last receipt | tag/commit + immutable target digest | checked relations over current carriers | re-observed actual state on every run | content/provenance classification recomputed | materiality gate from current evidence | idempotent level-based operations; no durable step log | re-observe and converge; version marker written last | detect active current path, converge without duplicate command | recomputed layered checks before final marker | final receipt only; no progress registry | derived conditions during run; complete marker at end | state-aware summary; incomplete runs reconstruct next action | managed framework content plus preserved project-purpose extraction |

### Obviously contradictory configurations excluded before Challenge

| Excluded | Contradiction |
|---|---|
| X1 · Ask nothing and preserve every local byte | Cannot install current TFW values into framework-owned `.tfw/README.md`; stored values can preserve obsolete semantics; violates frozen ownership/outcome. |
| X2 · Overwrite all `.tfw/` from payload | Erases project config/state/history and contradicts explicit ownership. |
| X3 · Version equality means complete | Fails interruption after version write but before verification/briefing/cleanup. |
| X4 · One mutable central receiver registry owns config, project state, update state and release definition | Creates competing authority and contradicts the target's no-duplicate-project-state boundary. |
| X5 · Replace update with a deterministic package manager/installer | Explicitly out of scope and does not settle prompt-agent ownership/materiality decisions. |
| X6 · Automatically replace Antigravity workflows with skills in this task | This is support expansion/new provider mode, not verification of the currently supported adapter path. It needs separate authority and evidence; current CRUE scope cannot approve it silently. |
| X7 · Treat full maintainer pytest as a required receiver gate | Crosses D69's intended `repository` / `not repository` subject split; the observed external failure came from an optional agent invocation. |

## Findings

### E1 · The hidden split is Release Definition versus Update Observation

Gather initially framed «contract» as a content-location problem. Cross-referencing D1, D2, D9, D10 and D11 reveals a more important separation:

```text
Release Definition (immutable, same for all receivers)
  target ref + commit/digest
  declared payload and adapter topology
  version routes and semantic migrations
  release benefits, reversals and limitations
  checks that the candidate itself must pass

Update Observation (one receiving project, one invocation/result)
  installed provenance and actual starting state
  preserved project intent/config/state
  material decisions and refusals
  actions actually applied
  checks actually run and their scope
  limitations, completion condition and continuation
```

SLSA's build provenance provides an external structural analogy: `buildDefinition` describes the input/template while `runDetails` describes a particular execution, and output subjects are separately identified. SLSA also warns that verifier burden grows with unchecked external parameters. This does not make TFW a supply-chain attestation system; it shows why release provenance cannot stand in for receiver outcome and why a per-run result need not become a second release definition. Source: [SLSA Build Provenance v1.2](https://slsa.dev/spec/v1.2/build-provenance).

This split keeps H2 compatible with «no new mutable registry» in three ways represented by C1/C2/C6:

- invariant tests can connect existing release carriers without a new definition file;
- an immutable release envelope can exist per version without receiving-project mutation (C3);
- a bounded update receipt can record observed run facts while config/state remain authoritative in their existing files.

The receipt is not allowed to redefine project configuration, ownership or release content. Its job is evidence and continuation for one update run.

### E2 · Relations that must be checked together

The following pairwise relations are independent of which C1–C6 family survives:

| Relation | Left | Right | Failure made visible |
|---|---|---|---|
| R1 · identifies | selected version/ref | immutable commit/digest + `.tfw/VERSION` | moving or mislabeled payload |
| R2 · contains | adapter manifest target/source | actual candidate tree and installed transition action | manifest/tree mismatch or orphaned route |
| R3 · routes | every supported installed state | one ordered applicable migration path | skipped versions, repeated or unsupported migration |
| R4 · supersedes | retired normative text | zero live uses + explicit receiver action | current 2.2.0 vocabulary contradiction |
| R5 · preserves | project-owned item and intent source | post-update bytes/meaning | state/config/purpose loss or stale workaround |
| R6 · applies | approved material decision | concrete candidate delta | mechanical checklist hiding a semantic action |
| R7 · observes | target generation/version | checks performed against that exact candidate | stale/equal-version success claim |
| R8 · proves | release/run claim | named evidence layer L1–L5 | project tests presented as release or comprehension proof |
| R9 · continues | nonterminal condition | safe next command/action and authority | interruption/refusal with no resumption path |
| R10 · renders | release facts + run facts | owner-facing status | invented benefit, hidden limitation or missing next action |

TUF's consistent-snapshot mechanism supports R1/R2/R7 as a design analogy: a client consumes one coherent target set and aborts/report failures before trusting it. It does not solve R5/R6/R10, which depend on project meaning and human authority. Source: [The Update Framework Specification](https://theupdateframework.github.io/specification/latest/).

### E3 · H1 configuration space: four decision policies

| Policy | Facts | Established choices | Changed semantics | Material unresolved alternatives | Expected question interface |
|---|---|---|---|---|---|
| P1 · Fixed interview | agent may prefill | always reconfirm selected keys | owner interprets | owner interprets | same technical questions every update |
| P2 · Stored-value continuation | reuse mechanically | reuse mechanically | preserve unless invalid syntax | ask only on hard parse conflict | few questions, high risk of preserving obsolete intent |
| P3 · Delta/conflict gate | derive without question | reuse if unchanged | ask whenever meaning changed | ask | question names detected delta |
| P4 · Authority/applicability/materiality gate | derive and cite | reuse when authoritative and still answers same question | compare original reason with new consequence | ask only when alternatives materially differ and no authority settles them | project consequence, evidence, recommendation, tradeoff |

P4 introduces a candidate decision procedure for later Challenge, not a final recommendation:

1. **Observe:** name the value/path/action and evidence source.
2. **Resolve authority:** identify whether a durable project decision already governs this exact meaning.
3. **Check applicability:** determine whether release semantics changed the question the prior decision answered.
4. **Check materiality:** compare effects on project behavior, data, purpose, risk, future authority and irreversible external action.
5. **Act or ask:** mechanical/equivalent alternatives can be handled and reported; unresolved material alternatives are asked with consequence, evidence, recommendation and tradeoff; a source defect that prevents safe application produces noncompletion, not a request to authorize a local framework fork.

The following cases separate policies:

| Case | P1 | P2 | P3 | P4 |
|---|---|---|---|---|
| unchanged `task_containers` with owner comment «new only in workspace; tasks archive» | asks | reuses | reuses | reuses and reports archive write boundary |
| old budget value whose semantics changed | asks technically | preserves | asks because schema changed | asks only if evidence shows original purpose may no longer apply; explains project effect |
| README byte-identical to old starter, no project designation | asks | preserves | asks | applies settled framework ownership while preserving any separately evidenced project purpose |
| README byte-identical but explicitly designated project purpose | asks | preserves stale methodology | asks | preserves designated purpose through transition while installing current methodology |
| source fails retired-wording gate | asks for workaround or stops | may copy | stops | returns source-defect noncompletion; project owner is not asked to redefine framework truth |
| push/tag/deploy after update | asks | may infer | asks on delta | separate external-effect authorization regardless of content decision |

Amershi et al.'s guidelines support the shape of P4—scope action under uncertainty, show relevant context, explain action, allow correction—but the study also found some uncertainty behavior hard to assess in a single session. Therefore P4 needs measured scenario runs; prose inspection cannot validate H1. Source: [Guidelines for Human-AI Interaction](https://doi.org/10.1145/3290605.3300233).

**H1 comparison measures for Challenge:** false-question count; hidden-material-decision count; questions requiring framework internals; correctness of cited prior authority; recovery cost after a wrong no-question action. Fewer questions alone is not success.

### E4 · Application/retry/result must be selected as a bundle

D6, D7, D10 and D11 cannot be chosen independently:

| Bundle | Apply | Progress/result | Retry | Known boundary |
|---|---|---|---|---|
| B1 · Version-last in-place | idempotent exact copies + bounded semantic merges | no step journal; target version written only after all checks | re-observe and replay safe operations | briefing delivery still needs a durable completion signal; semantic merges must prove idempotence |
| B2 · Staged candidate + receipt | build candidate separately, merge project-owned values once | receipt names desired source and independent conditions | resume/reconcile from observed conditions | staging cannot hide project changes indefinitely; receipt must not duplicate config/state |
| B3 · Isolated Git candidate | temporary worktree/branch and reviewed commit | commit + linked report | discard/rebuild or continue exact candidate | Git ref atomicity does not make earlier worktree edits or user communication atomic |
| B4 · Journaled compensation | ordered durable sub-actions | append-only step conditions and compensations | resume next safe action or compensate | most machinery and risk of stale procedure state |
| B5 · Pure level reconciliation | compute desired target and observed receiver each run | transient conditions + final receipt | converge regardless of missed intermediate steps | difficult for non-idempotent questions, merges, cleanup and message delivery |

Kubernetes API conventions distinguish desired `spec` from observed `status`, attach `observedGeneration`, and prefer level-based convergence over dependence on every intermediate edge. They also caution that a single phase enum is hard to evolve and use independent conditions with reason/message. This is useful for separating installed target from verified/briefed conditions; TFW need not adopt Kubernetes schema or controller machinery. Source: [Kubernetes API Conventions — Spec and Status](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-architecture/api-conventions.md#spec-and-status).

The original Saga paper supplies B4's compensating-action model for long-lived operations, but a Markdown agent cannot inherit database guarantees merely by naming steps. Each compensation must declare what it can safely reverse and what history it must not erase. Source: [Garcia-Molina & Salem, “Sagas”](https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf).

Git exposes transactional updates for refs, with compare-against-old-value and start/prepare/commit/abort, but its documentation notes that concurrent readers may still see a subset of multiple ref modifications. More importantly, TFW's worktree edits occur before ref landing. C4 therefore needs isolation and post-land verification; «one Git commit» is not by itself an end-to-end transaction. Source: [git-update-ref documentation](https://git-scm.com/docs/git-update-ref.html).

RFC 9110's retry condition remains the narrow guard: replay only if semantics are idempotent or application can be detected. This excludes «copy loop is repeatable, therefore update is repeatable» as a valid inference. Source: [RFC 9110 §9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2).

### E5 · Candidate result model: independent conditions, not version equality

The minimum obligations exposed by Gather are orthogonal:

| Condition | Evidence | Example nonterminal reason | Safe continuation must name |
|---|---|---|---|
| SourcePinned | ref, commit/digest, version | SourceUnverified | how to repin or stop without receiver writes |
| RouteResolved | installed provenance → migration path | UnsupportedStartingState | project-specific plan authority |
| DecisionsResolved | cited prior choices + new verdicts | OwnerDecisionRequired / SourceDefect | exact material consequence or upstream correction |
| PayloadApplied | source/target inventory and hashes | PartialApplication | replay/restore boundary |
| ProjectStatePreserved | protected bytes/semantic comparisons | PreservationConflict | affected project-owned meaning |
| AdaptersAligned | active provider roots/routes + parity | AdapterTransitionConflict | current supported path; no implicit new provider mode |
| ReceiverVerified | named L1–L3 checks and candidate identity | VerificationFailed | failed subject and whether project changed |
| OwnerBriefed | delivered rendering derived from evidence | BriefingPending | the result that still must be communicated |
| CleanupResolved | removed or disclosed retained staging | CleanupDeferred | exact retained path and safe later cleanup |
| Complete | all required conditions true for same target/run | RequiredConditionUnknown | first unmet condition, not equal version |

This table is a semantic candidate, not a demand for ten mutable fields. C1 can render the same obligations as a checklist; C2/C5 can persist conditions; C6 can recompute most and persist only a final receipt. Challenge must compare cost and stale-state risk.

### E6 · Adapter compatibility and provider expansion are separate configurations

The current TFW release declares Antigravity workflows as an installed adapter. CRUE must therefore test the supported workflow route across actual legacy/canonical roots without losing project neighbors. Current Google documentation establishes `.agents/` as the canonical workspace root and retains some `.agent/rules` compatibility; it also announces a workflow→skills migration. These facts produce two distinct questions:

1. **Current compatibility:** for the already supported workflow form, determine active roots, migrate singular/plural safely, reject duplicate route ambiguity and prove second-run stability.
2. **Support expansion:** add Antigravity skills, migrate workflow command semantics or claim a new provider/version mode.

Only the first is within the current approved delivery outcome. The second remains a prospective dependency/amendment/scope decision; none of C1–C6 assumes it is approved. Sources: [Google workspace rules](https://antigravity.google/docs/rules-workflows), [workspace workflow paths](https://codelabs.developers.google.com/getting-started-agy-ide), [workflow-to-skill migration](https://antigravity.google/docs/migration/workflows-to-skills).

### E7 · H2 alternative representations

| Representation | Canonical truth ownership | Derived/repeated content | Receiver mutation | Maintenance/agent-reading exposure |
|---|---|---|---|---|
| R-A · Current carriers + manual discipline | workflow, migration, manifest, changelog each own a truth | tables repeated by hand | config + files + ad hoc checklist | lowest new machinery; observed drift remains possible without relation checks |
| R-B · Existing carriers + invariant graph | same owners; release checks encode R1–R10 | human summaries may repeat; contradictions fail pre-tag | bounded receipt only | moderate test surface; agent still reads selected prose |
| R-C · Immutable release envelope | envelope identifies target/routes/relations; referenced prose owns explanation | human views generated or linked | receipt only | clearer machine-verifiable candidate; new schema and migration cost |
| R-D · Fully generated carriers | typed source generates workflow/changelog/migration/manifest views | almost all views derived | receipt only | largest architecture change; risk that generated form becomes unreadable to reasoning agents |

The new combination not proposed in Briefing is R-B + B5/C6: keep existing human-readable carriers, add release-time relation checks, recompute observed receiver state on every invocation, write the version marker last, and persist only a final bounded receipt. It avoids both a central mutable registry and a full step journal, but its feasibility depends on proving every replayed operation and final communication condition.

**H2 verdict at Extract:** at least three structurally coherent representations avoid a mutable receiver registry (R-B, R-C and C6's final receipt). H2 is not yet proven because Challenge must show one survives stale evidence, partial application and agent misinterpretation at acceptable cost.

### E8 · H3 communication configurations and specimens

| Form | Release benefits | Actual outcome | Limitations/deferred | Next action | Trace depth |
|---|---|---|---|---|---|
| M1 · Four CHANGELOG blocks | complete by category | absent except free-text violation | absent | absent | low |
| M2 · Outcome-first + benefit blocks | only applicable, cited release facts | explicit state and checks | explicit material items | required/recommended/none | linked technical receipt |
| M3 · Separate terminal forms | state-specific subset | success / source defect / project failure / refusal / interruption | form-specific | form-specific | linked receipt |
| M4 · One conditional schema | applicable benefits if evidence permits | independent conditions rendered | required whenever present | always rendered | expandable detail |

State specimens for later behavioral tests:

```text
SUCCESS
Status: the prospective fixture `receiver-clean` is fully updated to immutable `candidate-A`;
payload, migration, active-adapter and project checks passed against the same candidate.
Gained: the fixture can use selective context and VALUE-only accounting declared by the release.
Changed/preserved: framework instructions changed; receiver configuration, knowledge and history did not.
Limitations: no material limitation was observed in this declared scenario.
Next: no action is required to complete the update; one ordinary task is the recommended pilot.
Details: the `receiver-clean` update receipt names the commands and resulting digests.
```

```text
SOURCE DEFECT BEFORE PROJECT WRITES
Status: update not applied; TFW `v2.2.0` at `8e68ab37` failed its live retired-wording gate.
Project impact: receiver project files were not changed.
Why: the release retires `A writer is not named yet`, but three live workflows still contain it;
this is a framework source condition, not a project decision.
Next: retry after a corrected immutable payload; no receiver-project repair is requested.
Details: the report lists the target commit and the three tagged-source hits.
```

```text
INTERRUPTED / APPLIED BUT UNVERIFIED
Status: update incomplete; target payload and version `2.2.0` are present, but receiver verification,
owner briefing and cleanup were not observed.
Project impact: framework files may have changed; protected config/state hashes still require comparison.
Recovery: re-pin `8e68ab37`, re-observe the candidate and continue from the first unmet condition;
restore the recorded pre-update snapshot only if no post-update task write occurred.
Next: resume the same target and verify conditions; do not infer completion from equal version.
```

```text
MATERIAL OWNER DECISION
Effect: helpdesk values `420` files and `60000` lines would become decomposition prompts under the
new contract, not the old limits that originally caused counting disputes.
Evidence: the migration preserves numbers, while the owner's recorded reason says they were raised
to bypass the behavior this release changes; the old choice therefore does not settle new meaning.
Recommendation: use the owner's proposed `42` files and `6000` lines so decomposition remains useful.
Tradeoff: lower triggers ask for decomposition earlier; preserving the larger values avoids that prompt
but carries an obsolete workaround into the new semantics.
Technical trace: helpdesk field report §2.5 and the pre/post config comparison remain available.
```

These specimens are test inputs, not claims that users understand them. M2–M4 can all satisfy the information contract syntactically; later live observation must measure whether recipients can correctly state completion, material change and next action.

**H3 verdict at Extract:** one communication can combine release facts and run facts if they remain separately sourced and conditionally rendered. A single fixed happy-path paragraph cannot represent refusal/interruption/source defect without hiding state; multiple renderings may still share one schema.

### E9 · Common scenario/evidence matrix for Challenge

| Scenario | Required decision evidence | Required technical evidence | Required owner-facing evidence |
|---|---|---|---|
| unchanged 2.1 receiver | no new material choice; cite applicable prior settings | pin, route, invariant checks, receiver build | complete + applicable benefit + no required action |
| customized README/project purpose | designation and purpose carrier | pre/post semantic preservation + current methodology install | what moved/preserved, no values-adoption question |
| changed-semantics budget workaround | original reason or unresolved applicability | old/new schema and preserved history | consequence, recommendation, tradeoff |
| singular Antigravity with project neighbors | no provider expansion authority inferred | active path, project-neighbor hashes, no duplicate command, second run | material path change only if it affects use |
| source retired-wording failure | no project owner workaround verdict | pre-tag L1 failure; zero receiver writes | framework defect, noncompletion, retry route |
| interruption after version write equivalent | none unless a material merge is unresolved | observed conditions distinguish incomplete from complete | incomplete state + safe continuation |
| optional full pytest on receiver | agent must select intended test subject | D69 `-k` split and required receiver route | optional failure is classified, not presented as project/update failure |
| completed second run | reuse prior authority if still applicable | recompute completion or validate receipt/target; zero unintended diff | already complete, checks/status current, no repeated interview |
| refused material decision | explicit refusal | preserved pre-action state and evidence | refusal, unchanged/changed scope, later continuation |

### E10 · Structural decisions made in Extract

These decisions shape the research space; they do not select a winner:

1. Compare six complete C1–C6 families and exclude only configurations that visibly contradict frozen scope/ownership/evidence boundaries.
2. Couple apply/retry/record/status as bundles B1–B5; do not evaluate an «idempotent copy» independently of semantic merge, verification and briefing.
3. Separate immutable Release Definition from per-receiver Update Observation; neither may become authority for the other's facts.
4. Preserve the Coordinator correction: repository-state test selection is an agent/instruction-subject issue unless the required receiver route is proven wrong.
5. Treat current Antigravity workflow compatibility as in scope and workflow→skills support as an unapproved expansion.
6. Test H1 by false questions and hidden decisions, H2 by relation integrity and resumption, and H3 by state recognition/continuation—not by artifact presence or fluent prose.

## Checkpoint

| Found | Remaining |
|---|---|
| Six internally expressible whole configurations cover all 13 Gather Dimensions without presupposing a winner. | Challenge must attack each against the same scenario matrix and cost boundaries. |
| Release Definition and Update Observation are distinct truths; provenance does not prove receiver outcome. | Decide whether existing carriers + invariants, an immutable envelope or another family is the smallest complete representation. |
| H1 has four comparable policies and measurable failure modes. | Run counterexamples against P3/P4, especially stale authority and false materiality. |
| Application, retry, record and result form five coupled bundles. | Determine whether stateless reconciliation can really cover semantic merges and briefing, and whether persisted conditions become stale machinery. |
| H2 has at least three no-mutable-registry candidates. | Pairwise consistency and maintenance/agent-reading costs remain to be challenged. |
| Current adapter compatibility is separated from provider-mode expansion. | Define the supported version matrix; do not absorb workflow→skills without authority. |
| H3 has four forms and state specimens that keep release/run evidence separate. | Seek examples where one schema overloads the owner or hides a material limitation; later live comprehension evidence remains required. |

**Sufficiency:**

- [x] External source used? SLSA, Kubernetes API conventions, Git ref transactions, Saga, TUF, RFC 9110, Google Antigravity and the HAI primary study were used with explicit transfer limits.
- [x] Briefing gap closed? Comparable whole designs, authority/ownership, interruption/retry, checks and communication specimens are represented.
- [x] Configuration Space built from Gather dimensions? All 13 Dimensions appear in each C1–C6 row; obviously contradictory combinations are named separately.
- [x] At least one HL hypothesis tested? H1–H3 each have alternative configurations, measures and provisional verdicts.
- [x] Counter-evidence sought? Atomic-ref limits, stale condition risk, deterministic-framework mismatch, optional test boundary and unapproved provider expansion are explicit.
- [x] Deep-mode minimum decisions met? Six structural decisions are recorded in E10.
- [x] Metacognitive check completed? Yes. New combinations beyond Briefing: Release Definition versus Update Observation; relation-graph + stateless reconcile + version-last final receipt; and independent completion conditions instead of one phase/version flag.

Stage complete: YES
→ User decision: Close Extract and proceed to Challenge; alternatively name one configuration family that needs a bounded additional comparison.
