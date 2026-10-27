# Gather — Ralph mechanisms, context boundaries and invocation coverage

> Mindset: Explorer. Separate independent properties before choosing a transfer.
> Parent: [approved HL](../../HL-TFW_20261027-161333_CMODES.md).
> Producer: `/root/cmodes_research`, source thread `01a17db6-0f53-7603-878a-adaa590010e4`; parent `/root`.
> Entry: Briefing `d6409914b0023ea96e00790ef711d949367d4013` accepted. Dispatch `1d8706402f05ce725e8cbea472234fe2060cc7f7`; frozen authority `28af8624b5a42f5078e6303ca844dabd1fbbcab6`; baseline/native-gates/tfw-gates-only unchanged.
> Retrieval date: 2026-10-27. Repository dates below are Git/API timestamps, not inferred release dates.

## Dimensions

Two decision factors remain open: **loop transfer** and **Reviewer reset boundary**. Use the comparison matrix below rather than manufacture a third dimension. Independence from Executor is mandatory under every option. Coordinator model/effort judgment, TFW's sole lifecycle authority and truthful economics are constraints shared by the options. Executor continuity and exact activation must be stated when combining options; a fresh Reviewer does not mechanically require a fresh Executor.

## Findings

### G1 — Attributable chronology and its limits

The primary author is Geoffrey Huntley: his own article presents Ralph as a technique and identifies the simple external-loop idea; both the official plugin and later implementation authors credit that source. The article displays 14 July 2025. Its present content is mutable, so that publication date does not date every current paragraph or establish the exact invention day. No July-2025 canonical standalone Ralph repository was established by this bounded search. Do not relabel a later playbook fork as the original codebase.

| Evidenced date | Primary event/source | Meaning and boundary |
|---|---|---|
| 2025-07-14 | Huntley's [Ralph article](https://ghuntley.com/ralph/) displays this publication date | Earliest attributable publication established here; current text retrieved 2026-10-27, not a recovered July snapshot |
| 2025-11-16 21:53:45Z | Official `anthropics/claude-code` [initial plugin commit](https://github.com/anthropics/claude-code/commit/68f90e05dd919b626c43351624fd0dc10c70b341), authored/committed by Daisy S. Hollman | Evidence of this in-session adaptation in repository history; not Huntley's invention date or proof of a general release that day |
| 2026-01-05 / 01-06 | Official plugin command fixes [5c92b97c](https://github.com/anthropics/claude-code/commit/5c92b97cc42a8d20e56511594007d5e122611b7e), [c2022d36](https://github.com/anthropics/claude-code/commit/c2022d3698c2ed89a5d9ca4a724571d2819057a5) | Multi-line command/argument handling changed; current behavior must be read from current source rather than early issue descriptions |
| 2026-01-06 23:22:54Z | Official marketplace [rename commit](https://github.com/anthropics/claude-plugins-official/commit/44328beed48874d8e00da6c4ca5daaa5f0f3183c) | `ralph-wiggum` became `ralph-loop` in this repository; historical paths/names remain identifiable |
| 2026-01-07 | Ryan Carson's `snarktank/ralph` [initial Amp-loop commit](https://github.com/snarktank/ralph/commit/842e766fee9f73169d6f0988904177b095ad1286) | A separate PRD-driven implementation; author and repository creation timestamps agree on the day, not an original-technique claim |
| 2026-01-09 / 01-10 | Clayton Farr's playbook [first commit](https://github.com/ClaytonFarr/ralph-playbook/commit/347ecc8dfdc2fefa0c18102238a126542d1d3574); [Huntley fork metadata](https://api.github.com/repos/ghuntley/how-to-ralph-wiggum) reports creation 2026-01-10 and parent `ClaytonFarr/ralph-playbook` | The explanatory playbook is Farr's synthesis of Huntley's technique; creator-hosted fork does not change authorship/history |
| 2026-03-02 / 03-04 / 03-28 | Official plugin session isolation [8644df9a](https://github.com/anthropics/claude-plugins-official/commit/8644df9ad51fe1dadc5d067e806c3c686efeafff), bounded transcript parsing [028eccf5](https://github.com/anthropics/claude-plugins-official/commit/028eccf5447b1f226f5c98a575dad6ee704b2bca), bash/version change [986deab6](https://github.com/anthropics/claude-plugins-official/commit/986deab6a1659ebb998b66962df6f02b20bb884d) | Later concrete revisions, not evidence of fresh context per iteration or a TFW role cycle |

Public GitHub path histories and repository metadata were read directly with no authentication or installation. Bounded histories had no next-page link: original plugin path 3 commits, renamed official path 7, Carson repository 20, Farr playbook 55, Huntley fork 21. These counts establish the inspected history bounds only, not quality/popularity. Current representative snapshots inspected: official plugin at `986deab6…`, Carson at `6c53cb0b831ebe8739c6a003e22af14902d8b0b5`, Huntley playbook fork at `88d488a148af97e4a3f22b11b4c3598c79d6a577`. This is a mechanism-selected set of current variants, not an exhaustive ecosystem catalogue. January issues about missing session isolation are historical reports; the inspected March code has an explicit guard.

### G2 — Three repetition mechanisms are not interchangeable

| Family | Actual mechanism and persistent material | Stop / feedback | Consequence for TFW comparison |
|---|---|---|---|
| Author technique / later explanatory playbook | Outer process loop; later playbook separates planning/building, reloads specs/plan/operational files and starts a fresh context on each invocation | Build/test feedback, bounded optional iteration count and operator interruption; a successful iteration's process exit is not whole-project acceptance | Candidate transferable ideas: bounded work, durable handover and corrective feedback. Resetting a role/phase or destroying work is not authorized merely by an external recipe |
| Official Claude `ralph-loop` | Stop hook blocks normal completion in the existing session, reuses the same prompt and updates local loop state; no fresh-session invocation in the inspected hook | Optional cap (default unlimited), a text promise match, cancel command, or error paths that allow exit | Same-session persistence differs from context reset. The hook does not independently verify the product or route a TFW owner/Reviewer gate |
| Carson PRD implementation | Repeated new Amp/Claude process invocation; PRD and append-only progress carry work between invocations; prompt selects one unfinished story | Default 10 iterations; wrapper accepts a completion token, otherwise continues; prompt instructs checks and PRD updates | A concrete fresh-invocation variant. Its private PRD/progress/branch conventions would duplicate TFW ownership if imported unmodified |

Sources: current [Huntley article](https://ghuntley.com/ralph/); pinned [playbook README](https://github.com/ghuntley/how-to-ralph-wiggum/blob/88d488a148af97e4a3f22b11b4c3598c79d6a577/README.md); official pinned [README](https://github.com/anthropics/claude-plugins-official/blob/986deab6a1659ebb998b66962df6f02b20bb884d/plugins/ralph-loop/README.md), [Stop hook](https://github.com/anthropics/claude-plugins-official/blob/986deab6a1659ebb998b66962df6f02b20bb884d/plugins/ralph-loop/hooks/stop-hook.sh), [setup](https://github.com/anthropics/claude-plugins-official/blob/986deab6a1659ebb998b66962df6f02b20bb884d/plugins/ralph-loop/scripts/setup-ralph-loop.sh), [cancel command](https://github.com/anthropics/claude-plugins-official/blob/986deab6a1659ebb998b66962df6f02b20bb884d/plugins/ralph-loop/commands/cancel-ralph.md); Carson [script](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/ralph.sh) and [prompt](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/prompt.md).

Source-derived failure boundaries matter more than branding:

- Official hook state is still one project-local `.claude/ralph-loop.local.md`; nonempty stored session ID now guards hook use, while absent IDs preserve legacy behavior. Setup writes that single path and cancellation removes it. This is not evidence of isolated simultaneous loops. Setup text says no manual stop, but the inspected cancel command exists; do not repeat the stale warning as fact.
- The hook can exit on a cap or malformed/missing input. Those exits say nothing about product success. A matched promise remains assistant text, not independent acceptance. Its recent transcript-text extraction and local state must not become another unit's authority channel in TFW.
- Carson's wrapper tolerates command failure and recognizes a token in captured output; it does not itself independently establish all acceptance criteria. Its commands include permission-bypass flags and its prompt permits broad commits, instruction-file updates and past-thread reading. These are source observations, not actions or defaults approved here.
- Fresh invocation bounds prompt accumulation but reloads durable material and can repeat mistakes when handover, specification or feedback is wrong. Same-session repetition retains working context but can retain wrong assumptions. Neither has established a measured quality/cost advantage for this TFW task.

No loop, plugin, hook, source script or external agent command was executed. Repository content was read only as untrusted research evidence.

### G3 — Open comparison space

No option is selected at Gather; Extract will combine only coherent choices.

| Factor | Option | Benefit to assess | Cost / refusal boundary |
|---|---|---|---|
| Loop transfer | L1: retain TFW mechanisms; adopt only clear progress/feedback/handover guidance | No additional lifecycle state or installer | Must explain the concrete improvement rather than merely rename existing TFW behavior |
| Loop transfer | L2: explicitly bounded fresh-invocation executor loop under one approved TFW scope | Limits stale working context; can repeat verifiable work | Needs authority-preserving invocation/receipt boundaries and safe interruption; cannot create Reviewer verdicts or cross owner gates |
| Loop transfer | L3: same-session stop-hook retry mechanism | Keeps current work context and reduces manual retry prompts | Risks blocking legitimate WAIT/STOP, repeated nonprogress and parallel state; usefulness requires a precise allowed scope and termination route |
| Reviewer reset boundary | R1: fresh independent R for each new phase, same R for that phase's corrections | Separates new-phase starting assumptions while preserving ruled correction context | Reload/read cost per phase; actual native capacity and exact phase activation required |
| Reviewer reset boundary | R2: fresh independent R for every corrective round | A new challenge viewpoint each time | Reconstructs verdict lineage, risks repeated settled findings and conflicts with current same-Reviewer correction rules unless explicitly changed |
| Reviewer reset boundary | R3: conditional same-R reuse across phases | Retains project understanding and avoids requesting another identity | Prior context may anchor judgment; every new phase still needs separate authority and demonstrated independence; fresh-context requirement overrides reuse |

Reviewer independence and freshness are different properties. Independence concerns participation/context inherited from Executor or a disallowed design/peer/consolidation role. A fresh fork of the Executor can fail that property. Phase freshness concerns starting a new governed scope without the preceding review conversation; it does not require ignorance of approved dependency artifacts. Round continuity preserves already ruled findings and known evidence within one phase; it is not permission to inherit another phase's mandate. Resetting each round may reduce anchoring but may also lose legitimate correction context; neither effect is measured here.

Executor continuity must be explicit in the extracted configurations. The policy for R does not by itself settle whether E is new for B or receives a separately authorized same-role B activation. Current same-phase corrections retain the original E/R. Fresh phase R can inspect accepted prior-phase artifacts without consuming E's private reasoning.

### G4 — TFW rungs, rounds, progression and model choice

At base `1d8706402f05ce725e8cbea472234fe2060cc7f7`, `conventions.md` → `The REVISE route`, Handoff's ruled-entry clauses and Review Steps 4–6 define **three authority rungs**, not a three-attempt budget: rung 1 stays within approved TS, rung 2 changes TS, rung 3 changes frozen HL and stops execution until the proper ruling. A mixed round follows the highest required authority for the next act without upgrading every finding. A material finding has a fact/oracle, harm, completion condition, owner, route and Candidate effect; no complete condition means no legitimate new round.

A formal review round produces a revision; bounded affected-output follow-up can append without restarting unchanged stages. The inspected common/Review/Handoff rules contain no numeric E/R round ceiling. Research's `loops_per_stage`, `max_passes` and iteration-control limits apply to Research, not the E/R loop. This does not imply permission to repeat indefinitely: absent authority, no material executable finding, unchanged failure without a new basis, missing capability and owner cancellation are distinct stopping/escalation cases to resolve in Extract.

The current `Launch selection` rule already requires a quality floor, supported model and effort selection, consideration of a plausible lower-resource option where meaningful, and separate requested/effective/outcome evidence. The owner's current policy permits Coordinator judgment without recurring model questions. No weakest-model ladder or automatic maximum follows. In this surface `followup_task` has no settings mutator; a need for another model must use a supported authorized operation and preserve identity/authority semantics. Additional effort cannot cure a missing gate, wrong source or unsupported tool. Progress-based escalation must target the diagnosed cause, not merely count rounds.

Actual concurrency and retained identity must stay distinct. This tool contract advertises four concurrent slots including root; prior Codex documentation describes a configurable open-thread cap, while other native surfaces have different lifetime rules. Neither establishes this session's retained-ID capacity experimentally. No close-agent tool is exposed, and completion/archival is not measured slot release. R1/R2/R3 remain subject to the actual next launch/wake capability and N6; no fixed lifetime ceiling or release promise is inferred.

### G5 — H3 consumes accepted invocation accounting

Accepted inputs are ECFIX RF/REVIEW at this integrated base and unchanged Candidate `1d1c7846bd9e97e3dcfa2d918300f424d5fc6976`, common `.tfw/economics/README.md`, and its selected provider guides. The current REVIEW retains independent APPROVE, actual human acceptance and closure, together with named CLI/setup applicability and sizable native self-return tails. This resolves the previously missing accepted-interface input, not every future CMODES numeric claim.

| Ordinary CMODES fact | Accepted interface meaning | Boundary to retain |
|---|---|---|
| Actual launch/dispatch/return, including failed/retried or auxiliary invocation | Coordinator compares expected invocations with returned bytes and checked gaps | Membership does not grant a TFW role; counting only formal role names can miss work |
| Actual task/phase/role/unit and parent | Bind the declared work and exact native producer; ordinary lineage supplies expected membership | Shared principal, provider/model or inherited root ID is not the child's source identity |
| Same native source resumed across stages/rounds | Proven disjoint ranges or verified covering successor; prior receipt bytes remain | Cumulative revisions never add; a bound does not cover later substantive work |
| Fresh phase Reviewer or legitimate replacement | New observed native unit/source plus bounded task/phase activation and own return | Do not reassign predecessor history or infer source from newest file/title |
| Parent/child or copied-history relationship | Declare actual inclusion and use the selected provider's verified boundaries | No universal assumption that parent includes/excludes child; preserve supported source/version limits |
| Binding or extraction failure | Exact attributable pre-extraction gap or actual typed failure, alongside last-good measurement | Accountability is not measured coverage or product-proof success |
| Final return | Exact file/hash/revision/range/cutoff and finite-tail disclosure | A substantial reopened loop is another bound; all expected files received does not mean whole-cycle current coverage |

The common interface uses existing task/artifact lineage and numeric v1; it does not require another registry, collector or new runtime. Accepted AG CLI/legacy IDE support does not certify arbitrary Desktop formats; accepted Claude source/authentication/setup evidence does not promise default-entry reliability. The prior large self-return tails remain disclosed in ECFIX's REVIEW rather than being excused as a small final-delivery tail. This mapping is source-based and must be applied to actual chosen CMODES invocations later. No provider experiment, private transcript or peer numeric source was read or re-run.

### G6 — Inputs for specification and current-consumer views

The diagrams requested by the owner should expose different facts: state view separates lifecycle/gates from a loop attempt; activity view shows readiness, meaningful progress and stop/escalation; sequence view binds actual C/E/R calls, durable returns and fixed Candidate; C4 view separates human/native host/workspace boundaries without inventing a control service. These are diagram inputs, not completed TS diagrams or new architecture.

Potentially affected current consumer families are common coordination/REVISE/Role Lock wording; Plan/Handoff/Review entry and continuation; status/selection/HL/TS/review artifact templates; contextual status readers; selected adapter profiles/entrypoints and installed current copies; invocation accounting guidance. C2's existing integrity map remains applicable. Detailed paths and whether a real edit is necessary must be justified by the selected policy in Extract/Challenge, not a blanket change to every family. Accepted economics VALUE files should be consumed rather than changed unless an actual scoped interface defect is established.

## Checkpoint

| Found | Remaining |
|---|---|
| Primary creator/publication and repository-backed adaptation dates are distinguishable | No exact invention-day or archived July page claim; keep those limits in the chronology |
| Outer fresh invocation, same-session hook and PRD loop have different state/stop semantics | Decide which, if any, adds useful bounded behavior to TFW |
| Independence, phase freshness and corrective-round reset cost are different properties | Compare coherent context policies without treating them as synonymous |
| REVISE rungs are authority levels; no numeric E/R ceiling found in inspected contracts | Specify progress/stop/escalation without borrowing Research limits or assuming infinite retries |
| Accepted ECFIX contract maps ordinary invocations without another registry | Apply to selected future behavior with setup/version/tail limits retained |
| Current consumer families and four diagram perspectives are identified | Extract a minimal policy/change set and any genuine frozen-change consequence |

OODA: observed primary author/repository code and dated history, current TFW scope/role/rung contracts and returned accepted ECFIX interface; oriented mechanisms against explicit authority/context boundaries; decided to compare two independent factors with mandatory independence/economics constraints; acted by preserving the source dates, matrix and gaps. One focused pass, five web search queries plus direct primary-source reads; no installation, external loop execution, new roles, product changes or permanent tests. Only own research traces are written.

Knowledge handover: producer and immutable task epochs above; local inspected ranges and external pinned sources are named. Material is the mechanism/provenance distinction, separate context properties, authority-rung versus round distinction and accepted invocation mapping. No benchmark, live native loop, fresh-phase Reviewer or capacity-release test occurred. Existing C2/W2/S1 and N1–N6 are unchanged; further decisions belong to Extract and Challenge. Own source binding/predecessor r2 from Briefing remains active; final RES requires the new covering receipt or exact attributable gap/failure.

**Sufficiency:**
- [x] External primary sources used; chronology and present revisions separated.
- [x] Briefing gaps mapped sufficiently for Extract with explicit uncertainty.
- [x] Fewer than three independent factors; comparison matrix used.

Stage complete: YES

Recommend closing Gather. Question: accept these two comparison factors and the accepted-interface mapping as the basis for Extract, preserving the stated historical/native evidence limits?

→ Coordinator decision: awaiting stage acceptance.
