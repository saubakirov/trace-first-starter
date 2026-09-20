# Gather — "What do we NOT know?"
> **Mindset:** Explorer. Map unknown territory; do not choose the design before the alternatives and evidence limits are visible.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260920-223357_FRATS](../../HL-TFW_20260920-223357_FRATS.md)
> Predecessor: [Iteration 1 RES](../iter1/RES.md)
> Goal: Refactor TFW from field evidence so its artifacts remain behaviorally complete while routine coordination moves from repeated dialogue to concise durable traces.
> Observation boundary: repository state at task HEAD `8d3f9f2`, native Codex observation and current official product/Git documentation inspected on 2026-09-20; no live Claude or eight-gate AT trial was run.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: traffic class | activation or dispatch | one bounded material question plus one gate answer | durable result/ruling return | iterative design dialogue |
| D2: durable carrier | live `status.md` or journal event | writer-owned role artifact | declared cross-role append to an existing artifact | new mandatory carrier |
| D3: identity layer | mutable human-facing title | task/unit address and workflow role | stable named principal | task-local mandate rooted in human authority |
| D4: capability boundary | prose instruction or declared mandate | provider permission mode | OS/sandbox/tool filtering | external IAM, credentials or service policy |
| D5: contended repository resource | one worktree/index | overlapping mutable paths | saved branch/candidate landing | release metadata, tag and deployment state |
| D6: lane mechanism | owner/LEAD activation rule | scan existing task state before activation | atomic repository-local claim/ref | maintained external scheduler or lock service |
| D7: native title surface | agent-callable title method | user slash command | GUI title edit | automatic provider title |
| D8: compression proof | raw byte/word reduction | reader-and-consequence census | negative-case semantic replay | controlled implementation or native observation |

## Findings

### G1: Existing carriers cover the ordinary lifecycle; one answer-ownership edge is ambiguous

The current workflow and templates already divide most material facts by lifecycle owner. A bounded
material question followed by one gate answer is control traffic under the Coordinator's Briefing
ruling; it is not automatically the iterative dialogue that the proposed architecture is meant to
remove.

| Fact or edge | Current owner/source | Current durable carrier | Observed limit |
|--------------|----------------------|-------------------------|----------------|
| live lifecycle, current role and gate | Coordinator | closed-schema `status.md` | intentionally unsuitable for arbitrary prose or answers |
| activation/delegation | Coordinator or selected LEAD | `dispatch` journal event plus target task prompt | prompt delivery is operational; journal preserves the durable edge |
| Research gate result | Researcher | current stage file, then `RES.md` | direct answer is presently recorded by the same Researcher in the next stage or `User Direction` |
| Executor onboarding blocker | Executor | `ONB.md` §3 Question/Answer | template says the Coordinator fills the answer, but Coordinator Role Lock forbids writing ONB |
| implementation result | Executor | `RF.md` plus evidence | no new result carrier is missing |
| review result and proposals | Reviewer | `REVIEW.md` | no new result carrier is missing |
| REVISE ruling | Reviewer proposes; Coordinator decides | explicit Coordinator ruling appended to the live `REVIEW.md` | this is a declared cross-role exception, not a general permission |
| frozen baseline change | accountable human/Coordinator | HL §12 amendment and revised TS as required | already has an authority-bearing route |
| close/archive decision | Reviewer proposal; Coordinator decision | `REVIEW.md` §6 and lifecycle transition | already has an authority-bearing route |

The exact fact that cannot currently travel with unambiguous authorship is an authoritative answer
to an Executor's blocking ONB question: the template assigns answer completion to the Coordinator,
while Coordinator Role Lock forbids ONB edits. The evidence leaves several designs open: a narrow
cross-role append exception, Executor transcription with explicit answer source and epoch, a TS/HL
change when the answer alters scope or authority, or a separate carrier. It does not establish that
routine happy-path returns require a new artifact class.

The journal does not currently offer a generic gate-answer event kind. Its closed kinds are
`created`, `dispatch`, `handoff`, `transition`, `ownership_changed` and
`amendment_escalated`; body/refs preserve details of those edges. Treating every answer as a new
journal kind would therefore be a design change rather than use of an existing generic channel.

Sources: `.tfw/workflows/{plan,research/base,handoff,review}.md`,
`.tfw/templates/{status,ONB,TS,RES,RF,REVIEW}.md`, `.tfw/templates/journal/event.md`, and
`.tfw/conventions.md` at `8d3f9f2`.

### G2: Native provider surfaces narrow H1/H9 but do not prove reliable checkpoint compliance

| Provider/surface | Current documented capability | Bounded observation | Evidence not obtained |
|------------------|-------------------------------|---------------------|-----------------------|
| Codex App Server | `thread/name/set` updates a user-facing name; `thread/name/updated` reports it; thread list/read/resume hydrate `thread.name`; thread start/resume/fork return instruction sources | this task accepted exact title `RESEARCH · FRATS`, and the task list returned the same title once | population reliability, causal reason for earlier misses, and an eight-gate trial |
| Claude Code CLI | `/rename [name]` renames a session; `/resume [session]` accepts ID or name; current documented names are bounded and duplicate live names receive variants | documentation only | whether an agent can self-invoke the slash command at the required checkpoint and obtain exact programmatic readback in the owner's installed version |
| Claude Desktop Code sessions | a user can edit a title; desktop sessions can list/read/message/rename/archive other Desktop Code sessions; messages identify the sending session/title | documentation only | cross-surface equivalence with CLI/cloud/VS Code and a native owner-machine observation |
| Provider permission systems | Codex permission profiles and Claude permission rules/modes can enforce tool/filesystem boundaries outside prose | current Codex task reports an unrestricted/disabled filesystem permission profile | a technically restricted TFW run matching a declared task-local mandate |

The Codex capability is documented by the official [App Server thread API](https://learn.chatgpt.com/docs/app-server),
and its enforcement surfaces by [Codex permissions](https://learn.chatgpt.com/docs/permissions).
Claude capability is documented by the official [interactive commands](https://code.claude.com/docs/en/commands),
[Desktop sessions](https://code.claude.com/docs/en/desktop),
[environment variables](https://code.claude.com/docs/en/env-vars) and
[permissions](https://code.claude.com/docs/en/permissions) pages. These pages were fetched on
2026-09-20.

Both current Codex and documented Claude Desktop provide direct task/session messaging, so
conversation is an easy provider implementation. Availability does not show that repeated dialogue
is architecturally required. Conversely, one successful Codex title mutation and public Claude
documentation do not establish reliability. H1/H9 therefore cannot be explained by absolute native
capability absence, but placement, instruction-source loading/conflict and exact checkpoint
compliance remain unmeasured causal alternatives. Missing native Claude evidence is an explicit
limit; Codex behavior is not translated into a Claude result.

### G3: Title, task, principal, mandate, capability and approval preserve different facts

| Layer | Fact preserved | Fact not established |
|-------|----------------|----------------------|
| title/name | human-facing addressability and navigation; potentially continuity across resumptions | stable identity, authority, approval or access control |
| task/unit | actual task/thread address, parent, role, scope, channel and dispatch edge | a reusable cross-session person-like identity |
| principal | stable project-local profile attribution | authentication, current mandate or owner authority |
| task-local mandate | delegated scope, autonomy ceiling and reserved decisions rooted in a human principal | actual provider/OS capability restriction unless separately enforced |
| permission/IAM boundary | tools, paths, domains or services the run can actually access | legitimacy of a decision within TFW |
| commit/blob | exact bytes, parents, epoch and Git author/committer metadata | architecture approval or mandate by metadata alone |
| HL/TS/ruling | accountable-human decision, approved baseline and scoped authority | identity of every runtime process that later reads it |

The current FRATS history records Git Author and Committer as
`Sanzhar <sanzhar.aubakirov@innoforce.kz>` and reports no signature for the inspected commits. The
freeze commit `04184dd…` pins HL blob `336271…`; that is strong byte/epoch provenance, while its
authority still comes from the task's owner decision and frozen artifacts rather than the author
field. This is direct evidence for keeping H17's distinctions separate.

A persistent named LEAD may add a stable human-facing address on a shared office host or across
repeated sessions. A task title already adds task-specific addressability, and a unit record adds
parent/role/scope. The unique value of a stable named principal is therefore still only a candidate:
reusable attribution or continuity that must survive beyond one task/unit. It neither grants
authority nor replaces the task-local mandate. An owner-launched non-AT operational Researcher such
as this session can remain accountable through human owner, task state, role, gate recipient and
actual `via` without inventing a named agent principal. A shared device with several humans still
requires the human requester to be resolved separately from any leader name.

Sources: current `team/README.md`, `team/saubakirov.md`, `team/robert.md`, conventions
identity/AT/commit sections, FRATS task state and
`git log --format='%H %an <%ae> %cn <%ce> %G? %s'` scoped to this task. The participant files
declare attribution rather than authentication or authority; no claim here depends on a
repository-local principal registry or a machine binding.

### G4: Worktrees isolate checkouts; they do not serialize shared repository outcomes

Current TFW rules already separate genuinely read-only work from mutating worktrees, require
exact-path staging and preserve producer-attributed candidates. Git's own model gives each worktree
its own `HEAD` and index while sharing refs and repository objects. `git worktree lock` protects a
worktree from administrative prune/move/delete; it is not a repository mutation or landing mutex.
Git merge handles divergent histories and can stop on conflicts, but it does not decide which task
may land or release first.

The current repository listed 14 worktrees during this stage. That proves concurrent isolated
checkouts exist, not that all are active or that any two currently overlap. The root worktree also
contains unrelated untracked owner/task paths; they were inspected only as state and were not
modified. No current overlapping-path conflict was established.

| Boundary | What current rules provide | Open alternatives |
|----------|----------------------------|-------------------|
| worktree mutation | separate working tree/index and task-attributed candidate | parallel independent paths; one mutator for the repository; resource-scoped exclusion |
| overlapping paths | merge/rebase conflict detection after divergence | pre-activation scope check; atomic claim; accept-and-reconcile |
| landing to saved branch | candidate reachability and exact-path hygiene | per-branch landing owner; queued landing; opportunistic landing after current-baseline replay |
| release metadata/tag | project-defined release workflow | same lane as landing; separately serialized release lane; external release system |
| abandoned/stale work | recoverable candidate/receipt history | expiry/lease; explicit cancel/release; coordinator reconciliation |

The historical TFW-52 evidence is a counterexample to treating a shared-file lease as sufficient:
offline or unsynchronized writers can bypass it, while recoverability came from immutable
candidates, run evidence and reconciliation. A repository-local reservation would introduce shared
state and would need atomic acquisition, stale-owner recovery and an authority rule. Scanning
existing task-local `status.md` files avoids a new carrier but races unless activation itself is
serialized. An external scheduler can arbitrate atomically but adds maintained runtime
infrastructure.

An unrelated untracked proposal in the current checkout describes another alternative: keep
worktree work parallel and serialize only saved-branch/release landing through one Landing Owner,
with current-baseline replay and a bounded integration pass. It is non-normative, unapproved and not
used as authority here; it demonstrates that “one active mutator” and “no repository lane” are not
the only choices. Gather leaves all three broad scopes open: serialize all mutation, serialize only
overlapping mutable resources, or serialize landing/release while allowing isolated worktree
mutation.

Sources: `.tfw/conventions.md`, current `git worktree list --porcelain`, accepted TFW-52 iteration-2
and iteration-3 research, current owner HL §17, and official Git
[worktree](https://git-scm.com/docs/git-worktree) and [merge](https://git-scm.com/docs/git-merge)
documentation inspected on 2026-09-20.

### G5: A semantic-edge inventory can test compression; no reduced implementation exists yet

The current canonical surface repeats direct routing in four workflows plus conventions:

- Plan: questions/proposals/results return directly.
- Research: every WAIT and final RES return directly.
- Handoff: questions and RF return directly.
- Review: questions, verdict and proposals return directly.
- Conventions: AT units report questions, gates and results directly.

Research, Handoff and Review also repeat session identity logic that has a shared conventions owner.
The repetitions can be classified by consequence instead of by text similarity:

| Semantic edge | Minimum preservation question |
|---------------|-------------------------------|
| activation | does the intended role receive a scoped, addressable start event? |
| authority | can the reader tell who may decide, amend or only propose? |
| evidence | is the result durably bound to sources, epoch and writer? |
| recovery | can a resumed role find current state and unfinished work without chat history? |
| continuation | is the next role/task and trigger unambiguous? |
| exception | can a material blocker, REVISE ruling, freeze change or unavailable holder be resolved without concealed authorship? |

This matrix is a candidate preservation oracle for H3/H8. Replacing ambiguous “return directly”
paragraphs with explicit terms such as activation, bounded control traffic, durable return and
dialogue could reduce repeated prose, but no modified instruction set or controlled behavior
observation exists in this iteration. The iteration-1 current bridge also showed that corpus size
and runtime trajectory can move differently; raw reduction alone cannot prove preserved behavior.

No new counterevidence to iteration 1's H10 result was found. Current canonical rules still expose
one `TYPE__{ID}` single-phase grammar; the remaining issue is whether every producer emits it at the
right topology-aware checkpoint. H10 remains challenge-only rather than a new Gather branch.

### G6: Evidence limits to carry into Extract

- No live Claude, native eight-gate AT, alternate-provider reliability or prompt-placement trial was
  run.
- Current Codex title success is one capability/readback observation, not a compliance rate.
- The 14-worktree count is existence evidence, not a conflict or throughput measurement.
- Current task state contains no global reservation/scheduler mechanism and no observed active
  collision; concurrency costs are source- and owner-report-bound.
- The ONB answer edge is a real writer-contract inconsistency; whether it warrants a narrow rule,
  revised template or new carrier is not decided in Gather.
- Stable LEAD/principal value has a plausible shared-host/cross-session use, but no evidence yet
  shows that the distinction must be mandatory for every operational session.
- Compression has a source-derived semantic-edge oracle but no reduced candidate to measure.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Existing state and role-owned artifacts cover the ordinary happy path and named lifecycle exceptions. | Resolve the ONB material-answer writer/provenance ambiguity without assuming a new carrier. |
| A bounded material question plus one answer is control traffic; iterative dialogue is a separate class. | Test whether every negative case still closes through an owned artifact and explicit activation. |
| Title, task/unit, principal, mandate, capability enforcement, commit provenance and approval are distinct. | Identify the smallest configuration in which a persistent named LEAD/principal preserves a unique durable fact. |
| Native Codex title capability was documented and observed once; Claude title/session capability is documented only. | Keep causal reliability claims unresolved and state the missing Claude/self-invocation/readback evidence. |
| Worktrees isolate checkout/index state but do not lock shared refs, landing or releases. | Compare all-mutation, overlapping-resource and landing/release-only serialization, including stale recovery. |
| A six-edge preservation matrix can test instruction compression. | Extract a concrete current contract and carry it into negative-case Challenge; do not claim behavioral proof. |
| H10 has no new counterevidence. | Retain its iteration-1 result and challenge only if later evidence conflicts. |

**Sufficiency:**
- [x] External source used? — current canonical/task/history sources plus official OpenAI, Anthropic and Git documentation.
- [x] Briefing gap closed? — all H1–H3 and H6–H17 are represented; H10 remains challenge-only and iteration-1 epochs/dispositions are preserved.
- [x] Dimensions identified? — eight independent dimensions with at least three alternatives each.

Stage complete: YES
→ User decision: pending Coordinator gate
