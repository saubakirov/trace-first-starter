# Gather — Current writes, phase adoption and evidence obligations

> Mindset: Explorer. Map the unresolved choices within C2; keep evidence types separate.
> Parent: [approved HL](../../HL-TFW_20261027-161333_CMODES.md).
> Goal: Refine coherent three-mode coordination without claiming an implemented full cycle.
> Producer: `/root/cmodes_research`, native source `01a17db6-0f53-7603-878a-adaa590010e4`; return only to `/root`.
> Entry: Briefing `3faf1ef2245b1dce4ec9f477ce330146cb35a052` accepted by the Coordinator; dispatch `20261027-195312__dispatch__82a7.md @ 4fb66e15f98f8f760a615e22f92f3bc44262e27c`; frozen authority unchanged at `28af8624b5a42f5078e6303ca844dabd1fbbcab6`.

## Dimensions

Two independent specification choices remain inside the working C2 design: **when current issuance requires the new mode field**, and **how much selection-content consistency is mechanically checkable**. Use the comparison matrix below. Historical preservation, phase-local permission, distinct Reviewer identity and truthful evidence are requirements rather than optional dimensions. Scheduling and recovery are bounded operation/evidence questions, not new product modes. C1 remains the fallback from iteration 1 rather than another full search.

## Findings

### G1 — Read compatibility does not define a write boundary

At repository epoch `4fb66e15f98f8f760a615e22f92f3bc44262e27c`, `tools/tfw_state.py:260–406` has separate `validate_status` and `validate_new_status`. The first accepts a complete historical spine with `owner_gateway`, rejects a partial selection pair and requires the pair with `upstream_route`. It rejects unknown keys, so proposed `coordination_mode` is currently invalid. The second additionally requires the current upward name and selection pair, and forbids issuing `owner_gateway`.

The common rules say both that new writers emit the current shape and that complete historical carriers are not silently rewritten/reparented. A lifecycle update under unchanged valid historical authority must therefore not accidentally become an owner mode-selection event. The future specification needs to define whether “new write” means new carrier/current adoption or every mutation; the existing function names alone do not settle this. Within the searched `tools/` and `.tfw/` Python files, `validate_new_status` has no caller beyond its definition. This bounded observation is not a repository-wide claim about every integration, and changing the function alone would not prove writer enforcement.

| Choice factor | Alternative | Benefit | Cost / unresolved consequence |
|---|---|---|---|
| Write boundary | W1: every status mutation emits the new complete current shape | A single format after any mutation | Historical continuation may require an adoption decision before an otherwise valid return; cannot silently fill mode or fabricate consent. |
| Write boundary | W2: new carriers and explicit adoption emit current shape; unchanged historical carriers retain their epoch on routine updates | Preserves continuation without forced reparenting or inferred mode | Writer needs explicit operation context and must prevent a new carrier from masquerading as legacy. Define which changes cross the adoption boundary. |
| Write boundary | W3: add an explicit schema epoch/discriminator and validate writes by epoch | Distinguishes format directly in the carrier | Adds a separate field and migration rules; an epoch still cannot authenticate consent or permit a mode change. |
| Selection checks | S1: retain narrative selection body with agent verification of all semantics | Smallest schema change; existing human-source detail remains expressive | Parser can check source/envelope but cannot reliably detect mode/scope/effect contradictions; workflow must reject ambiguity. |
| Selection checks | S2: canonical named clauses in the existing event body, with bounded extraction and comparison | Potential machine agreement checks for selected mode, scope and effect without a parallel state file | Requires exact clause grammar and failure behavior; original human answer and authority interpretation still need inspection. |
| Selection checks | S3: add typed event fields for mode/scope/effect and compare them against current status | Explicit typed contract for static consumers | Widens the closed event schema and its writers/readers; field agreement still does not prove human source or checkpoint satisfaction. |

None is selected at Gather. Extract will map compatibility and implementation burden; Challenge will eliminate combinations that violate frozen requirements. W3/S3 are schema options, not permission to add another authority registry.

### G2 — Exact source inspection is only one layer of adoption

`verify_baseline_source` (`tools/tfw_state.py:410–429`) resolves the cited immutable object/path and checks an HL prefix. `verify_selection_source` (`432–476`) resolves the commit, compares event bytes after line-ending normalization, validates the current event envelope and matches its human attribution to status owner. It does not parse mode, prior state, phase/role scope, effect checkpoint or actual human assent from the body. `validate_new_event` checks selection refs include local status and governing HL (`781–787`). These are useful source-integrity checks, not complete authorization checks.

Some contextual checks occur only when `task_dir` is supplied. A shape-only `validate_status(data)` call cannot establish the actual phase parent or inspect the immutable source. Any proposed acceptance evidence must name the invoked contextual entry point rather than claim validation from a successful shape check.

The unchanged `conventions.md` status/selection contract and `templates/journal/event.md` require the answer source, previous/selected values, exact phase/role scope, reservations, effect time and revocation/continuation consequences. They also require commit-before-adoption and phase-local effective state. This yields the following decision cases for Extract; these are obligations, not executed tests:

| Case | Mechanical evidence available or needed | Separate authority / state evidence |
|---|---|---|
| New C2 carrier | Closed complete shape; mode enum; one upward name; referenced object/path | Initial human mode choice under exact frozen ceiling, actual unit and bounded role mandate |
| Historical complete five/seven-field carrier | Recognized full historical shape; no partial additions | Its actual original choices and valid continuation; missing mode is not a default enum |
| Total coordination absence or partial carrier | Distinguish total legacy absence from incomplete spine/selection/mode extension | Total absence is read-only; partial/mismatched carrier cannot activate dependent work |
| Mode differs from source | Exact status/source value comparison if a selected grammar supports it | No “latest wins” repair, inferred mode or silent conversion; authorized correction/adoption needed |
| Selection object exists but is future-effective | Immutable event/path and declared checkpoint can be inspected | Checkpoint must actually occur; pending event cannot update current phase permission |
| Stale or contradictory selection | Previous values, scope and immutable reference can be compared with current carrier | Resolve the actual applicable owner choice and delivered revocation; do not replay a global event history into a second live state |
| Same-holder direct phase | Exact local Coordinator equals actual root Coordinator; owner and authority lineage agree | Only that Coordinator may use owner upward; worker returns still use local Coordinator; completion is local, without self-send |
| Distinct delegated phase | Actual local Coordinator differs; upward exactly names its governing task Coordinator | Exact delegated scope and parent lineage; no owner shortcut or permission from shared principal/title |

### G3 — Two dependent phases need two adoption decisions, not two physical Coordinators

For a source-based scenario with root C, phases A and B, and B dependent on A, an ancestor event may explicitly cover both phases and roles. That single immutable source does not make both current automatically. A must adopt at its own eligible checkpoint; B must separately adopt at its eligible checkpoint. B's readiness also requires its actual predecessor condition and approved scope/TS, independently of the mode selection. If only A is covered, B cannot reuse A's permission. A root change is neither a phase status write nor a launch grant.

The same-holder form must check C against the actual root holder, not merely a matching human owner. Its local phase completion avoids C sending to itself; a distinct phase Coordinator still uses the vertical phase-return edge. Phase A and B retain their own lifecycle, authority, pending gates and evidence. A non-revoking choice preserves valid active units and gates; revocation requires actual delivered notice/safe return evidence and cannot be reported as remote halt merely because an event exists.

Open specification questions for Extract are the exact W2 adoption boundary if W2 survives, mode/source comparison grammar, and how a holder change is validated against already active phase authority. These are common coordination questions, not ECFIX accounting questions.

### G4 — Native evidence package and scheduling constraints

Primary sources were refreshed on 2026-10-27, limited to the unresolved operation boundaries:

- [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), fetched through OpenAI Developer Docs: `agents.max_concurrent_threads_per_session` limits concurrently open spawned threads, excluding the primary. This does not establish that an idle completed unit releases a slot or that this session exposes a closing operation.
- [Claude subagent resume](https://code.claude.com/docs/en/sub-agents#resume-subagents): resume retains the same ID/history, while a new invocation creates another instance; built-in Explore/Plan are one-shot. Exact IDs matter because a reused name may resolve elsewhere. Documented user cancellation differs from tool-stopped continuation, and a non-parent resumer can redirect return recipient. These are documented capabilities/risks, not executions here.
- [Claude worktrees](https://code.claude.com/docs/en/worktrees#choose-the-base-branch): initial default base can differ from current work. Its resume/troubleshooting sections document continuing outside isolation when a worktree is gone and some interactive verification failures. Therefore identity resumption and actual checkout/base verification are separate checks.

The active tool contract here declares four concurrency slots including root. It exposes `followup_task`, `send_message`, `wait_agent` and `interrupt_agent`, but no close-agent operation. `followup_task` can resume the idle existing unit; `send_message` alone does not start an idle turn. The limit wording differs from the Codex configuration reference; neither proves the other's slot-lifetime behavior. No roster, peer transcript or capacity experiment was requested or performed.

An arithmetic planning case root + retained Researcher + Executor + Reviewer uses four identities. It is not an observed slot reservation or successful launch sequence. Reusing the same E/R pair across phase scopes might fit that bound only if each new phase activation is independently authorized and Reviewer independence is retained. It cannot be assumed from the instruction to reuse a unit for corrections. An additional phase-specific pair or a replacement could exceed an open-thread limit even if workers are idle. The next action must be a supported, authorized lifecycle operation or an explicit capacity blocker; hidden helpers, disposal assumptions or silent mode switches do not resolve it.

| Proof obligation | Minimum evidence to return | Possible within this research mandate? |
|---|---|---|
| Same Researcher continuation | Exact current ID, accepted prior return, addressed next-stage continuation, actual workdir and authority | Yes, observed for this unit only; this Gather is another continuation, not restart proof |
| Independent fixed-Candidate Review | Distinct fresh Reviewer identity/context origin, approved TS/RF/EV, full reachable Candidate SHA, actual reviewed checkout/object, bounded verdict returned to C | No new roles authorized; future approved implementation/review run |
| Correction by the same E/R | Original E and R IDs, authorized correction scope, new VALUE Candidate if changed, independent re-review by original R, exact return | Future approved role cycle; source-based scenario now |
| Two dependent phase operation | Separate effective A/B states and source checks; A's actual predecessor result; B's authorized activation; local completion with no self-send | Future approved C2 implementation; current reader rejects the form |
| Resume and interruption | Exact native ID, stop cause, permitted resume source, received continuation, actual path/base/authority and correct return recipient | Current same-unit follow-up observed; interruption, host restart and cancellation recovery unexecuted |
| Replacement | Authorized successor and reason, original stopped/pending state, new actual ID/parent, fixed inherited artifacts, path/base/authority checks, distinct source lineage | Future approved recovery; new launch forbidden here |
| Retained idle capacity | Actual limit and occupied-unit semantics at relevant checkpoint, supported lifecycle action, identity retention on correction, success or exact refusal | Unexecuted; documentation and arithmetic are insufficient |
| Cross-surface guarantee | Per claimed surface/version, same bounded native-cycle and failure evidence | Not supplied; Claude findings remain source-based |

### G5 — H3 and own accountability remain separate

H3 stays pending: the Coordinator has not returned an accepted ECFIX interface. The possible mapping input remains ordinary task/phase/role/actual unit/parent/source/return lineage. Extract may list those facts but cannot assert their acceptance or prescribe ECFIX numeric categories, splitting or reconciliation. Absence is neither positive evidence nor authorization to repeat adjacent work.

Own numeric accountability continues the exact source binding and revision-1 predecessor in Briefing. No new numeric receipt is claimed at this stage; the final RES return will contain a validated successor or attributable failure/gap. Researcher continuation does not change contributor identity or imply phase attribution.

## Checkpoint

| Found | Remaining |
|---|---|
| Two independent specification choices support a bounded matrix | Compare W/S combinations without reopening all C1–C6 options |
| Current structural/source checks are narrower than activation semantics | Specify exact mode/source/parent/effect acceptance boundaries |
| A/B adoption and predecessor readiness are distinct obligations | Challenge concrete stale/partial/mixed-epoch and holder-change cases |
| Fixed-Candidate, correction and recovery have explicit proof packages | Native implementation evidence remains unexecuted and must be retained in RES |
| Capacity needs lifetime evidence, not only an advertised count | Supported lifecycle or exact blocker at the future launch checkpoint |
| ECFIX dependency remains explicit | Exact accepted interface must arrive through Coordinator before dependent acceptance |

OODA: observed bounded source/consumer ranges; oriented them against the accepted Briefing; decided to compare two specification factors rather than invent dimensions; acted by preserving the matrix and evidence obligations. One focused pass. No source-discovery rerun, new role launch, product mutation or permanent test was performed.

Knowledge handover: this Researcher inspected the current reader, status/selection contracts, journal/status templates, role-cycle clauses and inherited iteration-1 analysis at the stated epoch, plus the named current primary documentation. Material is the write-boundary ambiguity, limited parser assurance and bounded evidence matrix above. It is source-based analysis, not a promoted product fact or architecture verdict. Exact native proof and ECFIX uncertainty remain. Continue only through the parent Coordinator's Extract checkpoint.

**Sufficiency:**
- [x] External source used.
- [x] Briefing unknowns mapped sufficiently for Extract; pending dependencies are identified rather than declared solved.
- [x] Fewer than three independent specification factors; comparison matrix used.

Stage complete: YES

Recommend closing Gather. Question: accept this two-factor matrix and explicit evidence backlog for Extract, with H3 still pending?

→ Coordinator decision: accepted by `/root` after `6ff344568784f9bf8dfe04f4ed6add5a49149c27`. Continue Extract using grouped properties; assess W2/S1 as a complete minimal option; require concrete value for additional fields/grammar; do not infer cross-phase E/R reuse from correction continuity. H3 remains pending.
