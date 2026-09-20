# Extract — "What do we NOT see?"
> **Mindset:** Analyst. Build structure from the gathered evidence; expose combinations without selecting a winner.
> **Test:** "Does the configuration space reveal at least one combination that the Briefing did not propose?"
> Parent: [HL-TFW_20260920-223357_FRATS](../../HL-TFW_20260920-223357_FRATS.md)
> Predecessor: [Iteration 2 Gather](2_gather.md)
> Goal: Refactor TFW from field evidence so its artifacts remain behaviorally complete while routine coordination moves from repeated dialogue to concise durable traces.
> Boundary: task HEAD `8d3f9f2`; no live Claude/eight-gate AT trial, provider reliability claim, framework/receiver mutation, architecture selection, commit, push or release.

## Configuration Space

The eight Gather dimensions yield more than 30 combinations. The table lists coherent configuration
families that expose distinct carrier, identity, enforcement and repository-lane boundaries.

| Config | D1: traffic class | D2: durable carrier | D3: identity layer | D4: capability boundary | D5: contended repository resource | D6: lane mechanism | D7: native title surface | D8: compression proof |
|--------|-------------------|---------------------|--------------------|-------------------------|-----------------------------------|--------------------|--------------------------|-----------------------|
| C1 | activation/dispatch | journal plus target prompt | task/unit address and role | prose/mandate | one worktree/index | owner/LEAD activation rule | agent-callable method | reader-and-consequence census |
| C2 | bounded material question/answer | same writer-owned role artifact | task/unit address and role | provider permission mode | overlapping mutable paths | scan task state before activation | user slash command | negative-case semantic replay |
| C3 | bounded material question/answer | declared cross-role append | stable named principal | prose/mandate | overlapping mutable paths | atomic repository-local claim/ref | GUI title edit | controlled native observation |
| C4 | bounded material question/answer | new mandatory carrier | task-local mandate | OS/sandbox/tool filtering | saved branch/candidate landing | maintained external scheduler | automatic provider title | reader-and-consequence census |
| C5 | durable result/ruling return | writer-owned role artifact | task/unit address and role | prose/mandate | one worktree/index | owner/LEAD activation rule | agent-callable method | negative-case semantic replay |
| C6 | durable result/ruling return | declared cross-role append | task-local mandate | external IAM/credentials | release metadata/tag | external scheduler/lock service | GUI title edit | controlled implementation/native observation |
| C7 | iterative design dialogue | new mandatory carrier | stable named principal | provider permission mode | overlapping mutable paths | atomic repository-local claim/ref | user slash command | raw byte/word reduction |
| C8 | activation plus durable return; no routine dialogue | journal for activation; role artifact for result | stable principal only at selected LEAD, unit address for children | mandate plus actual provider/OS enforcement | saved branch/candidate landing | landing-owner activation; worktrees continue independently | agent-callable LEAD title; task titles for units | six-edge negative-case replay |
| C9 | one bounded question/answer | Executor records answer/source in ONB; scope-changing answer routes to Coordinator-owned TS/HL revision | no named operational principal | declared mandate, separately enforced if available | overlapping mutable paths | path/scope admission before mutation | task title already set | six-edge negative-case replay |
| C10 | activation plus result return | journal, RF and REVIEW; Coordinator appends only the declared REVIEW ruling | LEAD principal plus task-local mandate | external IAM/credentials | release metadata/tag only | serialize release; allow non-release work | provider/user title surface | controlled native observation plus semantic replay |
| C11 | activation plus result return | existing role artifacts | owner human plus task/unit; no persistent agent name | OS/sandbox/tool filtering | all repository mutation | one active repository lane | automatic title | reader-and-consequence census |
| C12 | activation plus result return | existing role artifacts | reusable LEAD principal and separate task mandate | provider permission mode | independent paths parallel; saved branch landing serialized | pre-activation overlap check plus landing owner | GUI or user command | six-edge replay plus current-baseline integration evidence |

C8, C9 and C12 expose combinations not stated in the Briefing. In particular, C9 splits one answer
by consequence: the Executor remains the sole ONB writer for a bounded factual answer, while a
scope/authority change moves to an already Coordinator-owned TS/HL revision. C12 separates
worktree/path admission from saved-branch landing instead of treating all mutation as one resource.
These are configuration families, not selected designs.

## Findings

### E1: The no-dialogue architecture needs four traffic classes, not one routing slogan

| Class | Definition | Durability requirement | Examples in current TFW |
|-------|------------|------------------------|-------------------------|
| activation | a bounded instruction that starts or resumes one addressable unit | dispatch edge and target scope must be recoverable | Coordinator dispatch, next-role trigger, return after a gate |
| control exchange | one material question plus one authoritative answer needed to continue | the role that owns the affected artifact records the answer, source, epoch and consequence; authority-changing answers must reach their authority owner | Research gate answer, ONB blocker, approval/rejection |
| durable return | a writer-owned result that another role can consume without reconstructing chat | named artifact, writer/source epoch, state/verdict and next trigger | RES, RF/evidence, REVIEW, revised TS |
| iterative dialogue | open-ended co-development in which meaning accumulates across turns | requires a deliberate collaborative channel or later consolidation | design workshop, repeated clarification, unbounded relay |

This classification explains H2's structural mechanism. Current native products make direct
messages easy, and current workflows repeat “return directly,” so the lowest-friction
implementation can become conversational even when RES/RF/REVIEW already carry the result. It does
not follow that every question is prohibited dialogue: the Coordinator's ruling classifies one
bounded material question and gate answer as control traffic.

H3's candidate compression is therefore semantic rather than lexical. “Activate the unit,” “record
one control answer in the affected owned trace,” and “return the durable result” carry different
consequences. Replacing all three with “message directly,” or replacing them all with “do not
dialogue,” loses information. Whether these four terms improve behavior remains untested.

### E2: The ONB answer edge is a configuration problem with four internally coherent forms

| Form | ONB writer | Authoritative answer location | Scope/authority-changing answer | New ownership or carrier cost | Unresolved risk |
|------|------------|-------------------------------|---------------------------------|-------------------------------|-----------------|
| A: declared append | Executor creates ONB; Coordinator may append only the answer field | ONB §3 with distinct writer attribution | Coordinator also revises TS/HL when required | one narrow cross-role exception | exception may generalize or obscure who owns the resulting ONB |
| B: sourced transcription | Executor writes question and records the received answer, source, timestamp/epoch and effect | ONB §3 | answer is not treated as authority until Coordinator changes TS/HL | no new carrier; one transcription rule | transcription error or stale answer unless exact source/epoch is preserved |
| C: authority-first revision | Executor records only blocker/question | Coordinator-owned TS revision or HL amendment; Executor resumes against it | same artifact is the authoritative change | no cross-role ONB write; potentially heavier revision | minor factual questions may trigger disproportionate baseline churn |
| D: separate answer record | Executor owns ONB; Coordinator owns a new ruling/answer artifact linked from ONB | new linked carrier | same carrier or TS/HL depending consequence | new artifact class, reader and lifecycle | duplicates existing ruling patterns and expands runtime surface |

All four can close the exact current contradiction between `ONB.md`'s “Coordinator fills in” text
and Coordinator Role Lock. None is selected in Extract. The consequence split matters in every
form: a factual unblock may be recorded without silently amending authority, while a scope,
acceptance or architecture change must move through an existing human/Coordinator-owned baseline
route. That distinction is stronger than choosing a writer by convenience.

The same-role stage pattern already used by Research supplies a comparison: the Coordinator sends a
gate answer, and the Researcher records the direction in its own next stage. That is evidence that
sourced transcription is compatible with role ownership, not proof that ONB must use it.

### E3: A persistent named LEAD contributes one unique candidate fact—reusable attribution continuity

The current layers can be reduced to two questions:

1. **Which unit may act now?** Task address, parent, workflow role, scope, channel, dispatch and
   task-local mandate answer this.
2. **Which reusable participant identity spans units or resumed sessions?** A stable principal can
   answer this when the project deliberately needs the continuity.

The second fact is the only durable distinction found that task/unit address, role, accountable
human, current state and `via` do not already supply. A persistent named LEAD can let a human refer
to the same declared agent participant across a root session, resumptions and delegated-unit
history. `team/robert.md` is an example of a stable declared agent profile; `team/README.md`
explicitly says such a profile is attribution, not authentication, and must not be shared merely
because two sessions use one provider.

| Scenario | Reusable attribution continuity material? | Minimum other facts still required |
|----------|-------------------------------------------|------------------------------------|
| owner-launched non-AT Researcher/Executor/Reviewer | not shown; owner, unit, role, gate and actual `via` already resolve accountability | accountable human, task/unit, role, source epoch |
| selected LEAD resumed across sessions | potentially yes: the stable participant name links separate root sessions beyond mutable task titles | explicit owner selection, task-local mandate, current unit address |
| shared host with one human and several agent sessions | potentially yes for human-facing addressability, but only if sessions are deliberately assigned that principal | session-to-principal binding plus actual capability boundary |
| shared device or several human principals | agent name cannot resolve which human acts or approves | human requester/accountable owner must be resolved separately |
| AT child unit | shared LEAD attribution may explain delegation lineage, but cannot merge child role/unit identity | exact child address, parent, role, scope, channel and dispatch |

This analysis narrows H7/H11/H12/H13/H16. A LEAD can replace a mechanical relay only as a bounded
activated root unit; its stable name can preserve cross-session attribution continuity. The name
does not carry mandate, architecture authority, approval provenance or least privilege. Ordinary
operational units need not invent that principal when the reusable continuity is not requested.

### E4: Mandate and capability require a two-layer contract

| Layer | Required content | Verification surface | Failure if omitted |
|-------|------------------|----------------------|--------------------|
| semantic mandate | exact task scope, role, allowed autonomy, reserved human decisions, parent and expiry/return condition | frozen task artifacts, dispatch and role-owned traces | a technically capable unit may act outside delegated authority |
| technical exposure | actual writable roots, tools, network domains, credentials/IAM and provider permission mode | native provider/session configuration plus OS/service controls | a prose-only “read-only” or “no release” promise remains unenforced |

The current task demonstrates the mismatch directly: its workflow mandate prohibits framework,
receiver and lifecycle mutation, while the session's reported filesystem permission profile is
unrestricted. Compliance is currently procedural. Official Codex and Claude documentation both
separate provider-enforced permission controls from prompt text. H16 therefore has a measurable
contract—declared mandate and actual exposure can be compared field by field—without treating a
principal name as a security boundary.

### E5: Repository lanes have at least three separable resource scopes

| Lane family | Serialized resource | Parallel work admitted | Admission evidence | Completion/transfer | Stale or abandoned state |
|-------------|---------------------|-------------------------|--------------------|---------------------|--------------------------|
| L1: repository mutation lane | any mutable repository operation | read-only work only | one active owner/LEAD activation decision | mutator returns candidate and releases lane | Coordinator/owner revokes or reassigns; unfinished candidate remains recoverable |
| L2: overlapping-resource lane | declared path/resource set | read-only plus disjoint mutating sets | pre-activation scope comparison or atomic resource claim | release exact resource set after evidence | stale claim needs epoch/owner/expiry and recovery rule |
| L3: landing/release lane | saved branch integration, release metadata/tag and deployment effect | worktree mutation continues; independent read-only always continues | landing owner accepts a candidate against current baseline | integrate, replay bounded checks, record result, then release | candidate remains immutable; next landing reconciles or rejects stale base |
| L4: external scheduler | scheduler-defined resource keys | whatever policy admits | service transaction/lease | service records release and next holder | service-specific expiry, fencing and recovery |

One agent/one task is insufficient as a repository safety rule because separate tasks can still
target the same paths, branch or release state. Conversely, the observed 14 worktrees do not prove
a current collision, throughput problem or need to serialize all mutation. Worktree count supplies
only coexistence evidence.

The current TFW contract already supplies parts of each state machine: isolated worktrees,
task-attributed candidates, exact-path staging and current-baseline verification. It does not supply
an atomic repository-wide claimant, conflict fence or landing queue. Existing task-local
`status.md` files can inform a pre-activation scan, but they are not themselves a global mutex.
`git worktree lock` protects worktree administration, not shared refs or landing.

The lane choice therefore turns on the resource whose concurrent change can invalidate another
unit: working copy/index, overlapping content, target branch, or release effect. Challenge must test
each scope against disjoint edits, stale candidates, abandoned holders and emergency human action.

### E6: Provider evidence belongs on a ladder, not in a binary capability claim

| Level | Evidence | Codex in this iteration | Claude in this iteration |
|-------|----------|-------------------------|--------------------------|
| P0: documented surface | official current product docs name the operation | title set/update events, hydrated thread names, instruction-source returns and permissions documented | `/rename`, `/resume`, Desktop rename/message/session surfaces and permissions documented |
| P1: one native operation | operation succeeds in the relevant surface | exact `RESEARCH · FRATS` title set succeeded | absent |
| P2: exact native readback | independent native list/read returns the exact value | exact task list readback observed once | absent |
| P3: bounded checkpoint series | operation/readback repeated at predefined workflow checkpoints | absent | absent |
| P4: end-to-end reliability | full native TFW trial covers all required gates and failure recovery | absent | absent |

H1/H9 remain causal hypotheses because P0–P2 show only that Codex capability existed in one case,
and P0 shows a Claude user/product surface. They do not measure instruction placement, conflicting
loaded sources, model compliance or reliability. Claude documentation cannot be translated into a
claim that a Claude agent can self-invoke `/rename` at the checkpoint or programmatically verify
exact readback. No partial receipts compose into the missing all-gate evidence.

### E7: The six semantic edges form an explicit preservation contract

Any compressed/current workflow candidate must preserve all six edges. An edge is preserved only if
its source, destination, authority, durable carrier and recovery consequence remain unambiguous.

| Edge | Required fields/behavior | Current principal carriers | Negative case the candidate must survive | Preservation test |
|------|--------------------------|----------------------------|-------------------------------------------|-------------------|
| activation | target unit/address, parent, role, exact scope, input refs, mode/channel, sender and start/return condition | dispatch journal event plus target prompt/task | target unavailable, duplicate activation, resumed session | a fresh or resumed unit can prove why it may start and what it must not do without chat reconstruction |
| authority | accountable human, delegated decision ceiling, amendment owner and reserved decisions | owner in task state, HL/TS, mandate/ruling | child claims parent authority; agent name treated as approval | every decision resolves to an authorized human-rooted path and cannot be widened by attribution alone |
| evidence | writer, source/ref, epoch, method, result and limitations | stage/RES, ONB/RF/EV, REVIEW, receipts | stale source, failed check, unsupported provider extrapolation | another role can reproduce or bound the claim and distinguish observation from inference |
| recovery | current lifecycle/gate, immutable accepted lineage, unfinished owner and next valid action | status, iterations, journal, Git candidates and role artifacts | crash, abandoned holder, stale reservation, moved HEAD | a new session can resume from durable state without relying on hidden conversation |
| continuation | next role/unit, trigger, required inputs, gate result and return route | workflow checkpoint plus durable result and dispatch/transition | unavailable next holder, REVISE loop, missing return | the workflow has exactly one valid next activation or an explicit bounded escalation |
| exception | blocker question, answer source/epoch, consequence, proposal versus ruling, frozen-change route | writer-owned stage/ONB/RF/REVIEW plus declared Coordinator ruling and HL/TS amendment | clarification changes scope; failed evidence; frozen baseline change; record dispute | exception closes without concealed cross-role authorship or silent authority change |

The contract makes H8 testable beyond word count. A smaller surface passes only if a source-derived
reader can still execute the happy path and each negative case above. Raw corpus/trajectory change
remains supporting cost evidence, not a semantic verdict. The contract also supplies the later H3
behavior test: activation, control exchange, durable return and iterative dialogue must lead to the
right carrier and authority behavior, not merely shorter prose.

### E8: Extract disposition map before Challenge

| Hypothesis | Extract state | Evidence boundary to attack next |
|------------|---------------|----------------------------------|
| H1 | unresolved, capability-absence branch narrowed | Codex P2 and Claude P0 do not establish gate placement or reliability causes |
| H2 | structurally supported | direct messaging is easy and “return directly” is repeated, but negative cases may still need bounded control exchanges |
| H3 | plausible and now operationalized | four traffic classes and six semantic edges exist; no behavioral trial proves the terminology works |
| H6 | conditionally supported | ordinary lifecycle uses existing carriers; ONB answer ownership must resolve without hidden authority mutation |
| H7 | plausible under a selected root mandate | LEAD can activate/route, but availability, reserved human decisions and independent review remain constraints |
| H8 | open but measurable | six-edge contract supplies oracle; no reduced candidate has passed it |
| H9 | unresolved | instruction-source and checkpoint alternatives remain unmeasured; raw length alone is not isolated |
| H10 | supported from iteration 1; challenge-only | no new competing current grammar or counterevidence found |
| H11 | conditionally supported | owner-launched non-AT unit needs no invented stable principal; shared-human cases still require resolution |
| H12 | narrowed | reusable cross-unit/session attribution continuity is the only unique durable principal fact found |
| H13 | plausible, ergonomic only | persistent name may aid shared-host addressability; authority and human attribution remain separate |
| H14 | unresolved as stated | one lane has safety value, but scope may be all mutation, overlap, landing or release |
| H15 | supported in resource model | task identity cannot itself fence shared paths/branch/release; scheduler-free mechanism still unresolved |
| H16 | supported as a two-layer requirement | mandate and actual exposure are distinct; current run demonstrates procedural-only restriction |
| H17 | supported | commit pins bytes/epoch; current unsigned human Git metadata does not prove architecture authority |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Four traffic classes separate activation, bounded control exchange, durable return and iterative dialogue. | Attack the classification with failed evidence, unavailable holder, amendment and recovery cases. |
| The ONB contradiction has four coherent configurations; consequence determines whether TS/HL authority must change. | Reject configurations that introduce hidden cross-role writing, stale transcription, unnecessary churn or an unjustified carrier. |
| A persistent principal's unique candidate fact is reusable attribution continuity across units/resumed sessions. | Test whether task history plus unit addresses already preserve enough continuity and whether shared-host naming creates misattribution. |
| Mandate and actual capability exposure form separate semantic and technical layers. | Test provider/OS enforcement gaps without inferring them from a name or prompt. |
| Mutation, overlapping resources, landing and release are distinct lane scopes; worktree count is not collision evidence. | Challenge each lane against independent edits, stale candidates, abandoned work and human override. |
| Codex is at P2 for one title; Claude is at P0 documentation only. | Preserve the missing P3/P4 evidence and avoid provider translation. |
| Six semantic edges now form a source-derived preservation contract. | Run the happy path and negative cases conceptually against the configuration families in Challenge. |

**Sufficiency:**
- [x] External source used? — Gather's current repository/task/history observations and official OpenAI, Anthropic and Git documentation remain source-bound by evidence level.
- [x] Briefing gap closed? — carrier, identity, LEAD, capability, lane, provider and compression structures are explicit for Challenge.
- [x] Configuration Space built from Gather dimensions? — twelve coherent families use all eight Gather dimension names and expose new mixed configurations.

Stage complete: YES
→ User decision: pending Coordinator gate
