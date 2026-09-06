# Gather — «Чего мы ещё не знаем?»
> **Mindset:** Explorer. Картировать неизвестное, расширяя поле до выбора решения. Каждое предположение считать вопросом.
> **Test:** «Могу ли я назвать каждое измерение и его альтернативы, не заглядывая в источники?»
> Parent: [HL-TFW_20260906-190312_CRUE](../../HL-TFW_20260906-190312_CRUE.md)
> Goal: Выпуски TFW должны доходить до существующих проектов как целостные, безопасные и понятные улучшения, позволяя владельцу увидеть пользу, фактический результат, ограничения и следующий шаг без изучения внутреннего устройства TFW.

## Evidence Boundary

> **Coordinator correction, 2026-09-06.** The first Gather checkpoint incorrectly grouped the
> six-task repository-state test with independently reproduced delivery defects. D69 deliberately
> separates framework tests (`-k "not repository"`) from repository-state tests (`-k repository`),
> and the 2.2.0 migration names the full pytest command as a **maintainer** check while receivers run
> their approved project commands. The external full-suite run was optional and selected the wrong
> subject; the existence of the repository test is not a delivery defect. The rows and checkpoint
> below now preserve that distinction. A defect would require evidence that the required receiver
> route invokes the repository subset or fails to make the intended selection available; that
> evidence was not found.

- Текущее поведение исследовано как immutable release `v2.2.0` → `8e68ab37d300122ff110500ad58f354f76b6210f`; tag и commit совпали, `.tfw/VERSION` на этом объекте равен `2.2.0`. Более новый master не использовался как доказательство поведения релиза.
- Три field report — наблюдения агентов об отдельных обновлениях. Совпадение отчёта с tagged source повышает уверенность в наблюдаемом дефекте; само по себе объяснение автора отчёта не доказывает причину.
- Дословные реплики владельца считаются свидетельством его реакции в конкретном эпизоде. Формулировки агентов о «понятности», «бюрократии» или возможной реакции менее погружённого пользователя остаются интерпретациями.
- Внешние источники дают технические механизмы и контрпримеры. Они не доказывают, что конкретная форма TFW будет понятна или что перенос механизма в prompt-driven workflow сохранит свойства исходной системы.

## Dimensions

Все альтернативы ниже остаются открытыми до Challenge. Некоторые могут оказаться несовместимыми с frozen HL; Gather пока фиксирует пространство, а не выбирает решение.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| D1 · Идентичность release payload | moving checkout | operator-named tag | explicitly authorized commit | versioned bundle with digest/manifest |
| D2 · Носитель release-to-receiver контракта | duplicated prose in release/update/migration | canonical workflow + version guide references | immutable release envelope + referenced rules | generated views from typed source |
| D3 · Наблюдаемое состояние receiver | clean/uninstalled | release-identical installed | locally customized installed | unknown, mixed or partially applied |
| D4 · Классификация ownership | path/location | byte equality against baseline | explicit declaration | declaration + provenance + semantic role |
| D5 · Основание действия агента | fixed owner interview | stored value is sufficient | delta/conflict-triggered question | materiality + authority + consequence test |
| D6 · Application model | in-place per-file checklist | staged payload then bounded merge | resumable journaled steps | transactional snapshot/commit boundary |
| D7 · Поведение при повторе | stop on equal version | rerun every check | resume from durable checkpoint | reconcile observed state to desired state |
| D8 · Adapter transition | retain legacy root | cut over to canonical root | dual-read compatibility window | migrate command form (workflow → skill) |
| D9 · Verification verdict | one aggregate pass/fail | separate maintainer and receiver suites | layered payload/migration/project/behavior verdicts | scenario-specific proof bundle |
| D10 · Update record carrier | transient chat/checklist | project artifact in canonical new-write container | framework-local append-only journal | commit metadata plus linked report |
| D11 · Result status vocabulary | version differs / version equal | planned / applied / failed | staged / applied-unverified / verified / briefed | interrupted / refused / recoverable / complete |
| D12 · Owner-facing completion | four CHANGELOG-derived blocks | outcome-first summary + technical trace | distinct success/noncompletion forms | one state-aware schema with conditional sections |
| D13 · Legacy `.tfw/README.md` transition | three-way methodology merge + relocate additions | install current methodology + preserve legacy material in named project-purpose carrier | managed framework block + separate project blocks | explicit designation map plus deterministic transform |

## Findings

### G1 · Tagged release path is pinned, but its contract is distributed

The happy path of `v2.2.0` is explicit:

```text
operator target
  → resolve tag/commit and .tfw/VERSION
  → git archive immutable object into .tfw/.upstream/
  → switch to target update.md
  → route through CHANGELOG + version migration
  → mandatory owner gate
  → classify + exact per-file checklist approval
  → in-place payload/config application
  → adapter/vocabulary gates
  → write version/provenance
  → project + adapter + vocabulary + build checks
  → four-block briefing
  → cleanup
```

Strong points are independently visible in the tagged source: source pinning, installed provenance, explicit config/state skips, key-by-key config merge, target-workflow handoff, version-route table, retired-wording search strings and truthful limits printed by `--check project`.

The behavioral contract is nevertheless spread across root `RELEASE.md`, `.tfw/workflows/release.md`, `.tfw/CHANGELOG.md`, `.tfw/migrations/2.2.0.md`, `.tfw/workflows/update.md`, `.tfw/adapters/manifest.yaml` and `.tfw/templates/briefing.md`. Some repetition is purposeful: changelog history must remain immutable, a version guide carries route-specific action, and the live workflow owns execution. Therefore «put everything in one file» is not yet a supported conclusion. H2 is about one owner for each truth plus checked relations, not necessarily one physical document.

### G2 · Classification ledger: observation is not cause

| Observation | Direct evidence | Current classification | Confidence and boundary |
|---|---|---|---|
| Manifest targets Antigravity `.agents/`, while the same tag installs its own Antigravity copies in `.agent/`; v2.1.0 also declared and installed `.agent/` | tagged manifest/tree and v2.1.0 workflow/tree; all three reports encountered the transition | **delivery-coherence defect**: root transition is undeclared and self-install does not satisfy its manifest | High for inconsistency. Not evidence that plural is wrong: current Google docs make `.agents/` canonical and keep backward support for `.agent/rules`. |
| `A writer is not named yet` is both retired and live in handoff/research/review | tagged CHANGELOG plus three tagged workflow hits; reproduced by all reports | **delivery defect** | High. Direct tagged-source contradiction; practical severity is separate from existence. |
| repository-state test asserts six starter task names; one receiver ran the full suite and saw it fail | tagged `test_gen_index.py`; D69's explicit `-k` split; migration's maintainer/receiver distinction; kaznpu report | **wrong optional invocation by the agent**; possible instruction-discoverability question, not a proven delivery defect | High that the test is intentionally repository-scoped and the receiver run selected it. No evidence that the required receiver route invokes it. |
| owner gate always asks handle, task containers and `build.*`, even when stored evidence is unchanged | tagged `update.md`; reports show repeat questions and one direct confused response | **missing decision semantics** plus **observed communication friction** | High that fixed questioning exists; medium for causal UX generalization. A stored value can be stale or semantically changed. |
| exact checklist can reach 150 mechanical items and obscure a write into archive | tagged rule requires one checkbox per file; kaznpu report records 150 and owner objection to `tasks/` | **missing materiality/presentation semantics**; archive write itself was an **agent deviation** | High for rule and episode. The checklist remains useful as trace; evidence does not justify removing detailed audit data. |
| `.tfw/README.md` is preserved solely because it exists, even when byte-identical to old starter | tagged `update.md`; two reports measured starter equality and needed owner input | **missing ownership-transition semantics** | High. Byte equality is evidence of provenance, not proof of owner intent; the frozen HL now settles that current TFW values must update while project purpose survives. |
| large budget values may encode a workaround whose reason disappears under new semantics | helpdesk owner quote plus tagged migration that preserves numbers | **missing intent/applicability semantics** | High for this project, unproven as population claim. Numeric outlier alone cannot identify motive. |
| update record was first written into `tasks/` | kaznpu direct report and owner correction | **local agent deviation**; absence of a canonical record carrier is **missing semantics** | High for distinction. `task_containers` describes task creation/resolution, not blanket authorization for update records. |
| agent first justified `.agent/` using a nonexistent collision with Codex paths | helpdesk report explicitly retracts its own rationale | **agent error** | High. A release omission may increase inference pressure, but does not make the false reason a source fact. |
| agents locally replaced retired wording or retained a red gate | reports | **agent responses to a source defect**, not release architecture | High. Local corrective merge is evidence of coping behavior, not a validated solution. |
| final briefing lacks a next-action/actual-outcome/limitation slot | template permits only four CHANGELOG categories; migration demands verified project outcome and pilot continuation | **source-level communication-contract contradiction** | High for structural conflict. No evidence that every recipient needs the same fifth block. |
| briefings were delivered | all three reports | **observed delivery only** | High for delivery; no positive comprehension claim follows. The reports explicitly say the owner did not report reading or usefulness in at least one case. |

### G3 · Adapter root is a transition problem, not a spelling contest

At the tag, the new manifest uses `.agents/rules` and `.agents/workflows`; the repository's installed Antigravity copies remain in singular `.agent/`. The preceding release's update workflow explicitly targeted singular `.agent/`. Current official Google material says workspace rules default to `.agents/rules`, retains backward support for `.agent/rules`, and places workspace workflows in `.agents/workflows`. A current migration guide additionally says legacy workflows are being replaced by `.agents/skills/<name>/SKILL.md` and are scheduled for retirement on 2026-11-01.

This counterevidence changes the question. Reverting the manifest to singular would align with the tagged tree but move away from the vendor's current canonical route. Blind cutover to plural can orphan project-owned files or leave duplicate commands. The unresolved design space must cover at least:

- installed singular only, plural only, both roots, and neither root;
- project-owned neighbors in either root;
- current active-path detection versus declared desired path;
- exact command parity, duplicate slash commands and second-run diff;
- version-aware workflow-to-skill transition, without claiming current TFW supports a provider mode it has not tested.

Primary sources: [Google Antigravity Rules](https://antigravity.google/docs/rules-workflows), [Google Codelab workspace paths](https://codelabs.developers.google.com/getting-started-agy-ide), [Google workflows-to-skills migration](https://antigravity.google/docs/migration/workflows-to-skills). These pages describe the current product on the research date; they do not establish what every historical Antigravity build loaded.

### G4 · H1 needs four evidence properties, not only three labels

The proposed `facts / established choices / new decisions` distinction is directionally supported but under-specified.

1. **Observation:** what is actually present — tag, bytes, config value, prior event, installed adapter root.
2. **Authority:** who or what was allowed to settle the meaning — immutable source, project config, approved artifact, owner statement.
3. **Applicability:** whether the old choice still answers the same question under the new release semantics.
4. **Materiality/ambiguity:** whether plausible alternatives change project purpose, data, behavior, risk or future authority.

Counterexamples show why no one label is sufficient:

- A config value is a fact and may be an established choice, but changed semantics can invalidate the reason that produced it (`420/60000` budget workaround).
- Byte identity to a starter makes framework provenance likely, but an owner may deliberately have adopted the text as project purpose; equality alone does not grant destructive authority.
- `[workspace, tasks]` is an established resolution setting, but does not decide where an update report may be written.
- A provider's supported legacy path is a technical fact, while removal of project-owned commands from that path is a separate project decision.
- The existing human handle is discoverable, but acting `on_behalf_of` remains an authority claim, not an OS/Git inference.

The primary HAI study by Amershi et al. offers supporting design heuristics: show contextually relevant information, scope service when uncertain, support correction, explain why the system acted, remember recent interaction and communicate consequences. It also reports that uncertainty-scoping was hard to assess in one session for some products. This supports scenario-based evaluation, not a proof that fewer questions are safer. Source: [Amershi et al., CHI 2019](https://doi.org/10.1145/3290605.3300233).

**H1 verdict at Gather:** plausible only if the model includes evidence source, authority, applicability and materiality. The current fixed interview disproves neither H1 nor its alternative; it demonstrates that unchanged facts and unresolved authority are not distinguished today.

### G5 · H2 can be a checked relation graph without a mutable receiver registry

The Update Framework (TUF) is not a drop-in architecture for TFW, but its primary specification supplies a useful separation:

- immutable target content is identified by trusted metadata before application;
- snapshot metadata prevents mix-and-match among independently changing metadata;
- a client aborts and reports verification/rollback failures rather than exposing unverified target files;
- consistent snapshots let a client finish against one coherent version while another is being published.

Source: [The Update Framework Specification](https://theupdateframework.github.io/specification/latest/).

TFW already has part of this shape through named tag → commit → `git archive`, distinct manifest/migration/changelog roles and installed provenance. The missing property is a tested relation across carriers: release claims, migration actions, adapter topology, live instructions, shipped tests and receiver-facing claims can disagree while the tag remains internally valid as a Git object.

Candidate relation types for Extract, without choosing a carrier:

- `declares`: release entry declares feature, removal or limitation;
- `routes`: each supported installed state resolves to applicable migration actions;
- `contains`: immutable candidate contains every declared target/source;
- `supersedes`: old live instruction has one explicit successor/action;
- `verifies`: each user-facing claim names an evidence layer that can actually prove it;
- `preserves`: project-owned value has a source and postcondition;
- `continues`: each nonterminal result has a safe next invocation.

**Counterevidence:** TUF solves an adversarial package-distribution problem with deterministic clients and signed metadata. Importing its complete metadata machinery would violate scope and would not make a language-model agent interpret ownership or materiality correctly. H2 remains open: coherence may be achieved by release-time invariant tests over existing carriers rather than a new registry.

### G6 · Interrupted and repeated update states are not representable in v2.2.0

The tagged workflow says «if installed and target versions match, stop». Later, the same workflow writes `tfw.version` and `installed_from` before running final verification, briefing and cleanup. This creates an observable ambiguity:

| Interruption point | Existing evidence after interruption | Next invocation under v2.2.0 | Unresolved risk |
|---|---|---|---|
| before owner-approved writes | pinned staging may exist; installed version unchanged | reroutes from installed version | cleanup and prior checklist location are unspecified |
| during payload/config application | mixed files; installed version usually old | reclassifies and may replay writes | semantic merges and completed steps have no durable checkpoint contract |
| after adapter changes, before version write | new payload/adapters, old version | treats new bytes as local difference against old baseline | customization versus partial application can be misclassified |
| after version/provenance write, before verification | version equals target | stops immediately | incomplete update can look complete |
| after verification, before briefing | version equals target | stops immediately | owner never receives result/limitations/continuation |
| after briefing, before cleanup | version equals target; staging remains | stops immediately | retained staging is not reported or reconciled |
| completed update, intentional second run | version equals target | stops | no distinction from the three incomplete equal-version states above |
| owner refuses material change | no standardized durable status | future run reconstructs context | refusal and safe continuation are not part of the result model |

RFC 9110 provides a narrow but applicable retry rule: automatic repetition is safe when semantics are idempotent or the client can detect whether the original action was applied; it specifically uses a version-control client checking revisions as an example. Source: [RFC 9110 §9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2). Exact byte copies may be idempotent, but the whole TFW update includes merges, project decisions, version mutation, verification, briefing and cleanup. Therefore file-copy repeatability does not prove workflow repeatability.

The migration guide permits rollback of framework/config/adapter snapshot before new post-update task writes, and requires manual assessment afterward. It does not define an observable marker for «new post-update task writes», nor a canonical update transaction/checkpoint record. No `UPDATE-*` carrier or location is named in the tagged update workflow, migration or briefing template.

### G7 · Verification must preserve separate subjects and verdicts

Observed and declared proof subjects are distinct:

| Layer | Question it can answer | Candidate checks | What it cannot prove |
|---|---|---|---|
| L1 · immutable payload | Is the selected release self-consistent? | tag/commit/version; manifest source/target existence; live retired-wording zero; changelog↔migration relations; explicit split between framework and repository-state test subjects | that a particular receiver can migrate |
| L2 · route/migration | Is this starting state supported and resumable? | route table coverage; old/new/mixed config; README ownership transition; adapter-root transitions; interruption checkpoints; second run | receiver build correctness or user understanding |
| L3 · receiver preservation | Did this project keep its data and established intent? | pre/post hashes for protected files; semantic config diff; archive immutability; active adapter parity; project build commands | generalized behavior of another agent/project |
| L4 · agent behavior | Can a fresh agent follow shipped instructions without maintainer correction? | predeclared scenario runs; action/question/reason trace; injected source defect; interrupted/repeat paths | human comprehension |
| L5 · owner outcome | Does the recipient understand material result and continuation? | live observation/interview/task-based check with declared sample | universal comprehension or provider capability |

`gen_index.py --check project` is commendably explicit that it checks structure, not adapter copies, Git state or artifact contents. The wider update workflow requires additional gates, so Extract must compare how their reproducible receiver route is made available. This does not turn the intentionally separate repository-state pytest subset into a receiver gate. A green L3 project build likewise does not repair L1 payload contradictions.

### G8 · H3 requires run evidence in addition to release benefits

The four-block template binds positive claims to CHANGELOG `Added/Changed/Fixed/Removed`, limiting invented benefits. It cannot, by construction, include:

- selected source and actual receiver route;
- applied versus refused/partial/interrupted status;
- actual project checks and their scope;
- preserved project decisions/data;
- local deviations or material limitations;
- next useful action and whether it is required.

The migration simultaneously requires the actual verified outcome and recommends a pilot continuation. Thus the current source carries two incompatible completion contracts: «NO FREE TEXT; four CHANGELOG blocks only» and «state receiver outcome/continuation». Reports show agents solved this by adding information outside the template or omitting it.

The HAI primary study includes separate guidance to make capability and limits clear, show relevant context, explain system behavior, communicate consequences and notify users about changes. These are compatible with a result that combines release facts and run facts, but do not determine its exact structure. A user saying «не понимаю последний вопрос» or objecting to an archive write is direct evidence of confusion in that moment; delivery of a briefing is not evidence of later understanding.

**H3 verdict at Gather:** the existing four-block form does not satisfy H3 for non-happy paths. The broader hypothesis — one clear communication can combine grounded benefits, outcome and continuation — remains open for Extract and requires state-specific specimens plus later live observation.

### G9 · Scenario inventory for later comparison

Any coherent alternative should be evaluated against the same cases:

1. 2.1.0 release-identical receiver; unchanged config; no real decisions.
2. 2.1.0 with project-owned config and README additions; current TFW values must still update.
3. `.tfw/README.md` byte-identical to an earlier starter but explicitly designated as project purpose.
4. old-only budget block with ordinary values; old-only block with an owner-confirmed workaround; mixed old/new block.
5. Antigravity singular-only with project neighbors; plural-only; both roots; workflow-to-skill-capable installation.
6. archive container listed for resolution but forbidden for new writes.
7. source payload fails its own retired-wording or manifest parity gate before receiver writes.
8. interruption at each row of G6, followed by the same command in a fresh agent session.
9. second run after a proven complete update.
10. owner refuses one material semantic change while accepting mechanical payload changes.
11. receiver build fails although payload gates pass; payload gate fails while receiver build passes.
12. successful update with no required owner action; successful update with recommended pilot; partial/noncompleted update with a recovery route.

### G10 · Primary-source map and counterevidence

| Source | Mechanism used | Counterevidence / limit |
|---|---|---|
| [tagged TFW 2.2.0](https://github.com/saubakirov/trace-first-starter/tree/8e68ab37d300122ff110500ad58f354f76b6210f) | actual shipped contract and tree | release source can agree with itself incompletely; later master is irrelevant |
| [ai-first-devices report](../../../../../docs/feedback/updates/2.2.0/FIELD-REPORT__ai-first-devices__claude-code-opus-5__20260906-171558.md) | one Claude update, direct quotes and measured comparisons | same session also performed earlier 0.9→2.1 leg; explanations are not independent review |
| [helpdesk report](../../../../../docs/feedback/updates/2.2.0/FIELD-REPORT__helpdesk__claude-code-opus-5__20260906-172507.md) | one Claude update, project tests and owner budget rationale | contains a self-identified agent reasoning error; one owner/project |
| [kaznpu report](../../../../../docs/feedback/updates/2.2.0/FIELD-REPORT__kaznpu-ai-lab__codex__20260906-172421.md) | one Codex update, archive objection and extra test failure | no user statement that full checklist or briefing was understood |
| [Google Antigravity docs](https://antigravity.google/docs/rules-workflows) | current canonical/legacy rules roots | current docs do not prove historical versions or project-specific activation |
| [Google workflow migration](https://antigravity.google/docs/migration/workflows-to-skills) | current workflow→skill transition and retirement date | prospective external change may require separate version support in TFW |
| [TUF specification](https://theupdateframework.github.io/specification/latest/) | immutable trusted targets, consistent snapshots, abort/report on verification failure | deterministic security framework; not evidence for prompt comprehension or need for full TUF machinery |
| [RFC 9110 §9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) | retry only with idempotent semantics or detectable application | HTTP semantics are an analogy; TFW multi-file/decision workflow must define its own equivalence |
| [Amershi et al. 2019](https://doi.org/10.1145/3290605.3300233) | uncertainty scoping, correction, explanation, change notification | validated guidelines across 20 products by 49 practitioners, not a TFW user study or a guarantee of comprehension |

### G11 · Decisions made within the Researcher role

1. Treat retired wording and self-tree/manifest disagreement as reproducible delivery defects because each contradicts the frozen tagged source's own declared gate/topology; do not derive their causes only from reports.
2. Treat the six-task pytest failure as an agent's wrong optional invocation: D69 and the migration separate repository-state maintainer checks from receiver checks. Keep instruction discoverability as a question unless the required route is shown to select the wrong subset.
3. Treat repeated questions, checklist overload and budget-intent loss as missing semantics or observed interaction friction, not as proven universal usability failures.
4. Treat the archive write and false path-collision rationale as local agent errors, while separately retaining the source gaps that made those errors easier to commit.
5. Reject briefing delivery as a proxy for user understanding; only direct reactions are observations of understanding/confusion, scoped to their episodes.
6. Keep all Dimensions open. The initial axes were expanded and revised by evidence; no three field-report patches are being treated as architecture.

## Checkpoint

| Found | Remaining |
|---|---|
| The tag/payload identity is proven and the full release→update→result path is mapped. | Exact coherent configurations and their pairwise consistency are Extract work. |
| Two source-level defects are reproducible independently of report explanations: retired wording and self-tree/manifest disagreement. | Severity and chosen correction mechanism remain open. The six-task test is excluded from this count. |
| The external six-task failure came from an optional full-suite invocation that crossed D69's intended test-subject boundary. | Whether the receiver-facing instructions make the intended selection sufficiently discoverable remains a question, not a proven required-route defect. |
| H1 requires observation, authority, applicability and materiality; three labels alone are insufficient. | Define comparable decision policies and test false-question/hidden-decision rates on declared cases. |
| H2 can be framed as checked relations among existing authoritative carriers, not necessarily a new registry. | Compare canonical-prose, release-envelope and generated-view variants with maintenance/agent-reading cost. |
| Equal version is ambiguous after interruption because version is written before verification/briefing/cleanup. | Choose and test a progress/result model, recovery boundary and durable carrier. |
| Official Antigravity sources make plural canonical while keeping some legacy support and moving workflows toward skills. | Determine supported version matrix and non-destructive transition policy. |
| H3 fails in the current four-block form for non-happy paths; delivery is not comprehension. | Compare state-aware communication structures and predeclare live observation measures. |
| Five proof layers are distinct. | Specify minimum evidence per scenario without turning the workflow into maximum-documentation bureaucracy. |

**Sufficiency:**

- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?
- [x] At least one HL hypothesis tested? H1–H3 received provisional, evidence-bounded verdicts.
- [x] Counter-evidence sought? Official Antigravity compatibility, TUF/RFC applicability limits, byte-equality and checklist counterexamples, and HAI study limits are recorded.
- [x] Deep-mode minimum decisions met? Six explicit classification/scope decisions are recorded in G11, including the Coordinator correction.
- [x] Metacognitive check completed? Yes. New findings beyond confirmation: the equal-version interruption ambiguity; the vendor-supported status of both Antigravity rule roots and impending workflow→skill transition; and the need for applicability/materiality in addition to the original three decision labels.

Stage complete: YES
→ User decision: Close Gather and proceed to Extract; alternatively name a specific evidence gap for one more bounded Gather pass.
