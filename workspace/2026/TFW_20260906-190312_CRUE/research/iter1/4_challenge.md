# Challenge — «Чего мы НЕ ожидаем?»
> **Mindset:** Critic. Построенные конфигурации атакуются одинаковыми сценариями; выживание требует доказуемой границы, а не убедительного названия.
> **Test:** «Сохраняется ли вывод, если другой исследователь прервёт операцию в худшей точке, изменит одно основание и потребует показать источник каждого статуса?»
> Parent: [HL-TFW_20260906-190312_CRUE](../../HL-TFW_20260906-190312_CRUE.md)
> Goal: Выпуски TFW должны доходить до существующих проектов как целостные, безопасные и понятные улучшения, позволяя владельцу увидеть пользу, фактический результат, ограничения и следующий шаг без изучения внутреннего устройства TFW.

## Attack Protocol and Evidence Boundary

Challenge проверяет логическую жизнеспособность H1–H3, а не объявляет ещё не проведённое поведенческое испытание успешным. Для каждого кандидата применены одни и те же атаки:

1. прерывание до и после изменения версии, проверки, записи результата, сообщения и cleanup;
2. повторный запуск при старой, равной и смешанной версии файлов;
3. один дефект внутри связанного release-набора и один независимый receiver failure;
4. устаревшее решение владельца, существующее значение без основания и действительно новая материальная альтернатива;
5. singular/plural Antigravity roots, соседние project-owned файлы и неоднозначный duplicate command;
6. попытка использовать запись результата как источник текущего состояния;
7. попытка выдать логическую проверяемость, зелёный fixture или наличие сообщения за наблюдаемое поведение агента либо понимание владельца.

Внешние аналоги использованы только в их доказуемых границах:

- TUF прекращает update cycle при несогласованной или недоверенной metadata и связывает target с согласованным snapshot. Это поддерживает остановку связанного набора, но не переносит в TFW подписи, deterministic client или package manager. Source: [The Update Framework Specification](https://theupdateframework.github.io/specification/latest/).
- Kubernetes `Condition` связывает наблюдение с `observedGeneration`, `reason` и `message`; устаревшее наблюдение видно по несовпадающему поколению. Для TFW это аргумент в пользу переоценки условий, но не в пользу постоянного status-объекта. Source: [Kubernetes Condition type](https://github.com/kubernetes/apimachinery/blob/master/pkg/apis/meta/v1/types.go#L1496-L1571).
- Git может проверить old OID и сгруппировать ref updates, но документация прямо ограничивает наблюдаемую атомарность нескольких refs; worktree-файлы, сообщение владельцу и cleanup вообще находятся вне ref transaction. Source: [git-update-ref documentation](https://git-scm.com/docs/git-update-ref.html).
- Актуальный Google codelab отдельно описывает `.agents/workflows/` как slash-command workflows и `.agents/skills/` как skills. Это подтверждает текущий plural path, но не разрешает TFW молча заменить уже поддерживаемый workflow mode новым skill mode. Source: [Google Antigravity workflows and skills](https://codelabs.developers.google.com/autonomous-ai-developer-pipelines-antigravity).

## Consistency Check

### Coverage of all dimension pairs

Ниже проверены все 78 пар D1–D13. `C` означает, что как минимум одна альтернатива пары совместима без специального межосевого условия; `Gx` указывает на обязательный guard из следующей таблицы. Такая отметка не утверждает, что любые две альтернативы совместимы.

| From | Pair results with every later Dimension |
|---|---|
| D1 | D2=`G1`; D3=`C`; D4=`C`; D5=`C`; D6=`C`; D7=`G2`; D8=`C`; D9=`G3`; D10=`C`; D11=`C`; D12=`C`; D13=`C` |
| D2 | D3=`C`; D4=`C`; D5=`C`; D6=`C`; D7=`C`; D8=`G4`; D9=`C`; D10=`G5`; D11=`C`; D12=`G6`; D13=`C` |
| D3 | D4=`C`; D5=`C`; D6=`G7`; D7=`G8`; D8=`C`; D9=`C`; D10=`C`; D11=`G9`; D12=`C`; D13=`C` |
| D4 | D5=`C`; D6=`C`; D7=`C`; D8=`C`; D9=`C`; D10=`C`; D11=`C`; D12=`C`; D13=`G10` |
| D5 | D6=`G12`; D7=`C`; D8=`C`; D9=`C`; D10=`C`; D11=`C`; D12=`C`; D13=`G11` |
| D6 | D7=`G13`; D8=`C`; D9=`C`; D10=`G14`; D11=`G15`; D12=`C`; D13=`C` |
| D7 | D8=`C`; D9=`C`; D10=`G16`; D11=`C`; D12=`C`; D13=`C` |
| D8 | D9=`G17`; D10=`C`; D11=`G18`; D12=`C`; D13=`C` |
| D9 | D10=`C`; D11=`C`; D12=`G19`; D13=`C` |
| D10 | D11=`G20`; D12=`G21`; D13=`C` |
| D11 | D12=`G22`; D13=`C` |
| D12 | D13=`C` |

### Incompatible pairs and required guards

| Guard | Dimension A · Alternative | Dimension B · Alternative | Why incompatible / required guard |
|---|---|---|---|
| G1 | D1 · moving checkout | D2 · any pinned contract | A contract read from a different moving state is not the contract for the applied payload; pin tag/authorized commit and bind all reads to its digest first. |
| G2 | D1 · immutable source | D7 · retry | Retry must repin the same object or explicitly select another target; live `HEAD` silently changes the desired state. |
| G3 | D1 · target digest | D9 · verification | Every verdict must name the same candidate identity; unbound green output proves another tree at best. |
| G4 | D2 · current workflow contract | D8 · workflow→skill | A skill is a distinct command-loading form, not a path-only copy of the supported workflow; it requires separate support authority and evidence. |
| G5 | D2 · release definition | D10 · receiver receipt | Receipt may reference immutable release facts but cannot redefine migration, manifest or release meaning. |
| G6 | D2 · release facts | D12 · owner message | Message combines selected release facts with run observations; copying either into another normative registry creates drift. |
| G7 | D3 · mixed/partial receiver | D6 · replay | Continue only when application is detectable and the operation is idempotent; otherwise stop at the connected semantic group. |
| G8 | D3 · partial receiver with equal version | D7 · stop on equality | Equal version is compatible with three incomplete interruption points; state must be re-observed. |
| G9 | D3 · mixed state | D11 · complete | Complete requires fresh evidence for the same source and receiver state, not the most favourable persisted bit. |
| G10 | D4 · path or byte equality only | D13 · project-purpose README | Identical bytes do not settle semantic ownership; an explicit project-purpose designation must survive the methodology transition. |
| G11 | D5 · stored value alone | D13 · changed ownership/meaning | A prior value is reusable only when authority, subject and applicability still match; changed meaning can require one material decision. |
| G12 | D5 · no new authority | D6 · semantic merge/external effect | Mechanical current-policy application needs no extra approval; a new project meaning or separately authorized effect does. |
| G13 | D6 · semantic merge | D7 · blind replay | Repetition is unsafe unless the old/new/application state is detectable; otherwise stop or use an approved restore boundary. |
| G14 | D6 · in-progress application | D10 · final receipt | A terminal receipt is written after observation of the attempt, not updated as a step journal; abrupt interruption is reconstructed next time. |
| G15 | D6 · version-last | D11 · complete | Version-last narrows one ambiguity but does not prove receipt creation, message emission or safe cleanup. |
| G16 | D7 · recovery | D10 · transient chat or stale receipt | Chat alone is not a portable trace; a receipt is history, so retry still recomputes current conditions. |
| G17 | D8 · root transition | D9 · adapter verdict | Verdict needs active-route uniqueness, neighbour preservation and second-run stability; byte-copy equality alone is insufficient. |
| G18 | D8 · unresolved duplicate/unsupported route | D11 · complete | An ambiguous active command prevents completion of the whole adapter group. |
| G19 | D9 · aggregate pass/fail | D12 · truthful noncompletion | The message must distinguish source, route, receiver and behavioural subjects; one red/green bit misattributes cause. |
| G20 | D10 · historical receipt | D11 · current status | Receipt records an attempt and never outranks current files, config, source or checks. |
| G21 | D10 · message-ready receipt | D12 · delivery/understanding | A renderable message supports safe re-delivery; receipt cannot prove the channel delivered it or that the owner understood it. |
| G22 | D11 · interrupted/refused/source-defect | D12 · four CHANGELOG blocks only | Release categories cannot express actual noncompletion, limitation and continuation without violating the current template. |

### Surviving configurations

| Config | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 | D13 | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 · C2/C6 bounded reconciler | named tag/commit + digest | existing carriers + release-time relation checks | recomputed clean/identical/custom/mixed state | declaration + provenance + semantic role | authority/applicability/materiality policy | staged exact changes; bounded detectable semantic transforms | re-observe same target; replay only safe operations | current workflow compatibility, singular→plural with collision stop | layered source/route/receiver; later agent/owner evidence separate | append-only attempt receipt at one exact project-owned path | technical conditions + communication state; no equality shortcut | short state-specific rendering from receipt | install current methodology; relocate/preserve evidenced project purpose | Only full in-scope survivor after guards; combines C2's boundary with C6's re-observation, but rejects C6's «final marker proves all» implication. |
| S2 · C4 as optional transport under S1 | same immutable target | same relation contract | Git receiver where isolation is safe and authorized | same as S1 | same as S1 | prepare/verify isolated candidate; land only the connected accepted set | discard/rebuild or resume exact candidate, then re-observe | same current workflow boundary | candidate and post-land checks, then S1 verdicts | same receipt as S1, not commit metadata alone | prepared/landed remain nonterminal until S1 guards hold | same rendering | same transition | Survives only as an execution aid. It is not the contract for non-Git receivers, dirty/shared checkouts or message delivery. |

### Logically viable but not a current survivor

| Config | Logical result | Why it is not selected for current CRUE recommendation |
|---|---|---|
| C3 · immutable release envelope | Can model a coherent release and observable receiver generations without a mutable receiver registry. | Introduces a typed schema, generation/migration rules and new readers across every adapter. No present evidence shows this architecture is required to close the two reproduced source defects and missing update semantics. Provider-version routes could also smuggle in Antigravity skill-mode expansion. Preserve as a future alternative if relation checks over existing carriers prove insufficient. |

### Eliminated configurations

| Config | Elimination reason |
|---|---|
| C1 · preflight over current carriers | Fixed repeat interview contradicts H1's purpose; «canonical project update report» has no exact carrier; equal-version rerun plus four benefit blocks still cannot distinguish interruption, noncompletion and message state. Its release-time invariant tests are retained inside S1. |
| C5 · journaled in-place compensation | Current TFW journal kinds are closed and contain no update-step kind; `status.md` is also closed. Inventing step events would violate current conventions, and durable per-step conditions would become a second stale procedure-state system unless every fact were rechecked. Compensation cannot safely undo later project work. |
| C6 · stateless reconcile + version-last receipt, unmodified | Stateless observation is valuable, but semantic decisions, message emission and cleanup are not reducible to idempotent file convergence. Version-last plus one final marker still admits a crash between marker, receipt and response. Only its re-observation principle survives in S1. |

### Unexpected survivors

- **C4 as a subordinate transport:** isolation remains useful even though it cannot provide end-to-end transactionality. The unexpected result is not «Git solves update», but «Git can reduce exposure while the semantic/result contract remains independent».
- **C3 as a future fallback:** the envelope is not logically refuted; it loses on current necessity and unmeasured maintenance/reading cost, not on coherence. This preserves H2's alternative if the smaller invariant graph later fails.

## Findings

### C1 · Completion has three different proof boundaries

The Extract condition `OwnerBriefed` was too coarse. Challenge separates:

| Boundary | What can establish it now | What cannot establish it |
|---|---|---|
| Technical convergence | current target identity; file/config/adapter comparisons; required receiver checks; cleanup removed or exact retained path disclosed | version equality, old receipt, source test alone |
| Message prepared/emitted | a receipt contains the state-specific rendering; the current interaction emits it; a later run can emit it again | version-last, receipt existence alone, claim that a response was read |
| Owner comprehension | future declared behavioural observation where the person identifies outcome, material change and next action | fluent prose, message delivery, three advisory field reports |

Therefore the recoverable guarantee is **at-least-once truthful rendering**, not exactly-once communication. A crash after technical convergence but before the response leaves a valid receipt that a later run can render again. A crash before receipt creation leaves no terminal state: the next run re-observes. No durable field claims that the owner read or understood the message.

### C2 · The minimum receipt needs one concrete carrier and one write boundary

S1 uses this prospective carrier:

```text
.tfw/update_receipts/receipt_20260906_190312_2_3_0_8e68ab37_a1b2.md
```

The directory is declared **project-owned append-only update history**. Payload copying, adapter sync and cleanup never overwrite or delete it. It is outside task lifecycle, so it does not add keys to closed `status.md`, invent a journal kind or reinterpret the second `task_containers` entry as writable. Its lower-snake filename encodes attempt time, target version, source-short identity and a collision token; the content carries the full immutable source identity.

Minimum content is bounded by evidence needs, not by file count:

| Field group | Required content |
|---|---|
| Attempt | schema version; attempt identifier; acting attribution; time |
| Desired source | upstream; tag or authorized commit; full commit/digest; target TFW version |
| Observed receiver | starting installed provenance; route selected; pre-write / applied / mixed observation |
| Decisions | reused authority references; new material verdict references; unresolved/refused item, if any |
| Application | connected groups applied; project-owned meaning preserved; deviations and affected paths |
| Verification | separate source, route and receiver verdicts with commands/artifacts and candidate identity |
| Outcome | `complete`, `source_blocked`, `receiver_blocked`, `refused` or `recovery_required`; first unmet condition |
| Cleanup | resolved, or exact retained path and reason |
| Continuation | one safe next action and the target identity to reuse or replace |
| Owner rendering | benefit facts that actually apply; actual outcome; preserved data/limitation; next action in project language |

**Write boundary:** after the attempt's current files and checks have been re-observed and cleanup is resolved or explicitly retained, but before the final owner-facing response. The receipt is written once and never edited. The response is rendered from that receipt. If response emission is uncertain, a later invocation may safely render it again. A normal source defect before receiver writes still gets a receipt; an abrupt process death cannot, and is recovered by observation rather than invented history.

This is a new carrier and therefore has an implementation/migration/read-contract cost. It survives Challenge because the cost is explicit and it replaces the ad hoc `workspace/UPDATE-2.2.0.md`; it does not silently overload a task artifact or create current-state authority.

### C3 · A connected semantic group stops together

The relation graph is a set of release-time and update-time checks over existing authoritative carriers, not a serialized central registry. Nodes remain owned where they already live: workflow rule, migration action, manifest path, payload file, release claim, verification subject and owner-facing benefit. Edges are assertions tested from those sources.

The stopping rule is stronger than «continue with an independent-looking file»:

- if a changelog claim, migration step, canonical workflow, adapter source/target and retired-term rule describe one feature transition, any missing or contradictory member blocks that whole connected group;
- if the group changes a shared vocabulary, ownership rule or command route consumed by several adapters, the update cannot declare the remaining copies independently complete;
- if a project-owned semantic merge is unresolved, no dependent version/provenance or completion receipt is written;
- a genuinely independent receiver build failure does not retroactively make the immutable source invalid, but it leaves the receiver outcome `receiver_blocked` or `applied-unverified`; it does not become `complete`;
- partial ordinary-file application is reported as partial. Automatic rollback is allowed only within a predeclared safe boundary and before later project writes; otherwise recovery preserves history and re-observes.

TUF is counterevidence against permissive partial continuation: its client workflow aborts on a mismatch in the metadata chain rather than selecting a convenient remaining file. Conversely, TUF is also counterevidence against overbuilding: TFW does not need its signed metadata system to express a checked dependency component.

### C4 · Conditions are reevaluable questions, not stored truth

S1 may name conditions such as `SourcePinned`, `PayloadApplied`, `ProjectStatePreserved`, `AdaptersAligned`, `ReceiverVerified`, `CleanupResolved` and `OwnerMessagePrepared`, but their authoritative form is a check definition plus current evidence. They are not added as mutable fields to `status.md` or a receipt that later sessions trust without reading the receiver.

For each condition, the check binds four elements:

1. subject identity — source digest and receiver candidate;
2. observation — exact file relation, command result or authority reference;
3. freshness — observation from the current invocation or explicitly named immutable artifact;
4. reason/continuation — why false/unknown and the safe next check or action.

Kubernetes `observedGeneration` demonstrates why freshness must be explicit: a well-formed old condition may describe an earlier desired state. TFW's simpler response is to recompute conditions from files and selected sources and use the receipt only as historical evidence and a recovery hint.

### C5 · H1 survives only with an applicability test

The facts / established choices / new decisions distinction survives the counterexamples under this policy:

| Input | Agent action | Stop/question condition |
|---|---|---|
| Direct current fact | Read and report it; do not ask the owner to transcribe YAML or paths. | Stop if sources conflict or the fact cannot be observed safely. |
| Established choice | Reuse only when the cited human authority, decision subject and present semantics still match. | Ask when changed meaning or revoked/ambiguous authority makes applicability material. |
| Framework-owned current rule | Apply from the pinned target when it is in scope; `.tfw/README.md` current TFW values need no values-adoption question. | A source contradiction blocks as a framework defect; do not ask the project owner to legalize a local fork. |
| New project decision | Explain affected project behaviour, evidence, recommendation and consequence in plain project language. | Ask one bounded question before the affected write. |
| External effect | Route through its own authorization even when file content is settled. | No push/tag/deploy inference from update approval. |

Counterexample results:

- A stored budget number whose original purpose was to evade old semantics is not automatically an established choice for the new semantics.
- A byte-identical README explicitly designated as project purpose is not framework-owned merely because bytes match an old starter.
- An unchanged, documented `workspace`-write / `tasks`-archive rule is not a new decision and must not trigger another technical interview.
- Unknown identity still needs the one attribution question required by TFW; reducing routine questions does not permit guessing it.

H1 is logically supported on the declared scenarios. It remains behaviourally unverified until fresh agents run those cases and the trace counts false questions, hidden material decisions and wrong authority citations. No reduction percentage or time saving is claimed.

### C6 · Current Antigravity compatibility is narrower than provider expansion

The surviving scope is explicit:

- support the TFW command form already declared by v2.2.0: workflow files;
- treat project-local `.agents/workflows/` as the current canonical target shown by Google;
- detect an installed singular `.agent/workflows/` as a TFW legacy state to migrate, not as proof that Google guarantees singular-workflow compatibility;
- preserve unrelated files under both `.agent/` and `.agents/`;
- if both roots expose divergent copies of the same TFW command, stop the whole Antigravity command group and report the collision;
- prove source/target existence, active-route uniqueness, exact command inventory, neighbour preservation and second-run stability for the workflow route.

Not included without a separate provider-mode decision and evidence:

- creating `.agents/skills/tfw-*` packages;
- translating slash-command workflows into auto-triggered skills;
- claiming compatibility with Antigravity CLI/global skill directories;
- deleting project-owned skill/workflow neighbours;
- using a current skills codelab as proof that the existing TFW workflow mode was behaviourally tested.

Logical path correctness can be checked from the candidate tree. Actual discovery/triggering by a fresh Antigravity agent is future L4 evidence and cannot be inferred here.

### C7 · H3 survives as one information contract with state-specific renderings

One fixed happy-path paragraph fails, but one contract can generate short variants. The owner-facing order is:

1. actual outcome in the first sentence;
2. concrete project benefit only when the selected release and receiver evidence support it;
3. what project data/behaviour was preserved and any material limitation;
4. the next action, including «ничего для завершения не требуется» when true;
5. one receipt link for technical detail.

Prospective failure specimen in plain project language:

```text
Обновление не завершено: файлы TFW уже изменены, но проверка команд вашего проекта ещё не дала
подтверждённого результата. Ваши задачи, настройки и история не перезаписывались. Следующий шаг —
повторно проверить тот же выпуск; новое решение от вас сейчас не требуется. Технические детали и
точка продолжения записаны в отчёте обновления.
```

Prospective source-defect specimen:

```text
Обновление не началось: в выбранном выпуске TFW обнаружено внутреннее противоречие. Файлы проекта
не менялись, исправлять проект не нужно. После исправления выпуска можно повторить обновление;
причина и проверка записаны в отчёте.
```

These specimens test information presence and attribution only. Future behavioural evidence must ask the recipient to identify the update outcome, one material effect and the next action; it must record observed mistakes and environment. Message existence is not comprehension evidence, and no numerical improvement is claimed before measurement.

### C8 · Stress-test outcomes

| Scenario | S1 result | S2 transport contribution | Required future evidence |
|---|---|---|---|
| clean supported receiver | converge, verify, append receipt, render success | candidate can reduce exposure before landing | fresh-agent completion without maintainer correction |
| equal version after crash before receipt | do not stop; recompute all conditions and create recovery/success receipt | post-land state still rechecked | injected interruption replay |
| crash after receipt before response | receipt remains historical/message-ready; render again | none | provider/session delivery behaviour |
| partial semantic README transform | detect old/new/ambiguous meaning; stop group when application cannot be proved | candidate diff can make ambiguity visible | legacy-purpose fixtures and post-land preservation |
| source retired-wording defect | block connected release group before receiver writes; source-blocked receipt | candidate must not bypass source gate | pre-tag gate fixture |
| receiver build failure after application | preserve source verdict; report receiver-blocked/applied-unverified | candidate may remain inspectable | representative receiver command fixture |
| both Antigravity roots contain divergent TFW command | block entire Antigravity group; no implicit preferred winner | compare in candidate only | actual workflow discovery test |
| owner refuses material merge | preserve pre-action state for affected group; receipt records refusal and continuation | candidate can be discarded if isolated | authority/refusal scenario trace |
| non-Git receiver | S1 remains applicable | S2 is N/A, not failure | ordinary-filesystem recovery fixture |
| later owner comprehension | no technical state changes | none | live/task-based L5 observation; do not infer from artifact |

### C9 · Decisions made in Challenge

1. Eliminate pure C1, C5 and C6; retain C2/C6 only as guarded S1, with C4 as an optional transport.
2. Keep C3 as a logically viable future alternative, not a current implementation recommendation.
3. Use release-time relation checks over existing carriers; do not serialize a second mutable release or receiver registry.
4. Stop an entire connected semantic group on contradiction, unresolved merge or adapter-route ambiguity.
5. Use the concrete `.tfw/update_receipts/receipt_20260906_190312_2_3_0_8e68ab37_a1b2.md` naming form for the prospective append-only carrier; do not extend `status.md` or journal kinds.
6. Write a receipt only after current-state re-observation and cleanup resolution/disclosure, then render the owner response from it; treat communication as safely repeatable rather than exactly-once.
7. Replace `OwnerBriefed` as one durable condition with technical convergence, message preparation/emission and future comprehension evidence.
8. Preserve P4's authority/applicability/materiality policy for H1 and require later scenario measurement before claiming interaction improvement.
9. Restrict Antigravity work to current workflow compatibility and singular→plural legacy transition; provider skill mode remains out of scope.
10. Use one H3 information contract with state-specific plain-language renderings; never use message delivery as proof of comprehension.

## Checkpoint

| Found | Remaining |
|---|---|
| One guarded in-scope configuration S1 survives all pairwise and scenario attacks; Git isolation is a conditional subordinate transport. | TS must turn relation guards, receipt schema and connected-group stops into exact acceptance criteria without expanding scope. |
| A concrete append-only project-owned receipt path and write boundary avoid both ad hoc task-container writes and closed `status.md`/journal expansion. | Coordinator must decide whether the new `.tfw/update_receipts/` artifact is accepted or should be replaced by another equally concrete non-authoritative carrier. |
| H1 is logically supported by authority + subject + applicability + material consequence, not by a three-label taxonomy alone. | Fresh-agent cases must measure false questions, hidden decisions and authority errors; no benefit magnitude is established yet. |
| H2 is logically supported by checks over existing carriers plus per-attempt historical receipts; C3 remains a fallback. | Behavioural agent-reading cost and long-term maintenance cost are not measured in this research pass. |
| H3 is logically supported by one information contract with state-specific renderings and safe re-delivery. | Actual delivery semantics and owner comprehension require later provider/user observation. |
| Current Antigravity workflow compatibility has an explicit singular→plural boundary. | Actual Antigravity discovery/triggering remains an L4 evidence task; workflow→skill support is not authorized. |

**Sufficiency:**

- [x] External source used? TUF, Kubernetes Condition, Git ref transaction limits and current Google Antigravity workflow/skill documentation were used with transfer limits.
- [x] Briefing gap closed? Each whole configuration was attacked for repeat/interruption, ownership/authority, connected failure, adapter transition, record location and communication.
- [x] Pairwise incompatibility checked? All 78 Dimension pairs are accounted for; 22 guards identify the incompatibilities material to the survivors.
- [x] Surviving configurations listed? S1 and conditional S2 are fully listed; C3 is preserved separately as logically viable but not selected now.
- [x] At least one HL hypothesis tested? H1–H3 each received counterexamples and a bounded logical verdict.
- [x] Counter-evidence sought? Pure stateless reconcile, durable step journal, end-to-end Git atomicity, four-block communication and implicit Antigravity skill migration were actively rejected or narrowed.
- [x] Deep-mode minimum decisions met? Ten structural decisions are recorded in C9.
- [x] Metacognitive check completed? Yes. New findings are the append-only non-task receipt boundary, connected semantic-group stop rule and split between message preparation/emission/comprehension; these were not merely confirmations of Extract.

Stage complete: YES
→ User decision: Close Challenge and authorize RES synthesis; alternatively reject or replace the proposed `.tfw/update_receipts/` carrier before synthesis.
