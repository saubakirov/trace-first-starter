# Extract — Bounded progress and phase review context

> Mindset: Analyst. Separate useful policy from machinery already supplied by TFW.
> Parent: [approved HL](../../HL-TFW_20261027-161333_CMODES.md).
> Goal: Make manual, visible-agent and single-Coordinator subagent operation coherent for single-phase and multi-phase Full work.
> Producer: native `/root/cmodes_research`; exact source thread `01a17db6-0f53-7603-878a-adaa590010e4`; Coordinator `/root`, `codex:thread:local:01a17d06-be29-7a31-afe4-bbd67c5cc3b7`.
> Authority: HL at `28af8624b5a42f5078e6303ca844dabd1fbbcab6`; dispatch `journal/20261027-231212__dispatch__5fb7.md @ 1d8706402f05ce725e8cbea472234fe2060cc7f7`.
> Selection: baseline, delegated, native-gates, tfw-gates-only; iteration 3, no governed phase token; originating proposer none.
> Input: [Gather](2_gather.md) at `c96e496fe457bd36a4383a1fe106d00242dd6e8d`, accepted by the Coordinator with direction to compare L1/R1, resolve default/exception authority and minimize consumers.

## Configuration Space

Gather has two independent factors. The matrix exposes all nine pairings without repeating shared properties. These are alternatives for specification, not currently authorized runtime operations or an architecture verdict.

| Loop transfer / Reviewer reset boundary | R1: fresh per phase, same for corrections | R2: fresh every corrective round | R3: conditional reuse across phases |
|---|---|---|---|
| L1: existing TFW mechanisms plus bounded guidance | M11: main comparison baseline; phase freshness and correction continuity | M12: no external loop, but repeated review resets require changing current continuity policy | M13: economical continuity without a new loop; receiving-context checks remain necessary |
| L2: bounded fresh-invocation Executor loop | M21: fresh E invocations and phase-fresh R are separate reset boundaries | M22: both working and checking context repeatedly reset; largest reconstruction exposure | M23: fresh E invocations paired with retained R context; freshness is intentionally asymmetric |
| L3: same-session stop-hook retries | M31: E context persists while R starts fresh at the phase boundary | M32: E context persists while R resets each round; neither reset entails the other | M33: maximum conversation continuity, subject to all hook and cross-phase authority constraints |

M21/M23 make the previously implicit asymmetric combination visible: Executor reset does not require Reviewer reset, and fresh Reviewer does not require fresh Executor. L2 means an approved invocation mechanism inside a bounded Executor responsibility; it cannot silently replace the formal holder, turn fresh processes into authorized roles or fabricate source continuity. R2 would need an explicit policy change before use. No pairing can override Role Lock, independent fixed-Candidate review, existing owner gates or C2/W2/S1.

## Findings

### E1 — The incremental value of L1 is a decision boundary, not another loop

TFW already supplies durable scope, an independent oracle, bounded findings, Coordinator rulings, knowledge handover and exact continuation routes. Importing a second PRD, progress log, loop state or completion token would duplicate those consumers. The useful transfer is to make meaningful continuation and non-success termination explicit at the existing return/ruling site.

| Existing consumer | Already supplied | Concrete addition worth specifying | Unnecessary addition |
|---|---|---|---|
| Executor ONB/RF/EV and ordinary execution | Approved TS, work/evidence, return and pending conditions | On an actual impediment, preserve the observed failure, attempted remedy, changed evidence or next discriminating action; preserve a partial result before an orderly stop | A progress record for every edit/tool call, a parallel task list or new status |
| Live REVIEW and Coordinator ruling | Complete material finding, authority rung, completion condition, Candidate effect | When the same failure recurs without a changed basis, do not blindly repeat the same dispatch; diagnose whether evidence, specification, capability or authority is missing and choose the existing route | Fixed three-round budget, a new approval per retry or mandatory model escalation |
| Role return / phase acceptance | Durable artifacts, independent verdict and owner acceptance where required | State that process exit, cap exhaustion, cancellation and assistant completion text are execution outcomes, never substitutes for acceptance | Hook-generated approval or automatic phase advancement |
| New-phase Reviewer selection | Independence and receiving authority | Explicit R1 default and a narrow authorized exception, distinct from ordinary same-phase correction | A new context-selection form or owner gate for every correction |

This is a small clarification of when to continue, stop or route a change. It does not add a numeric retry ceiling. A bounded transient retry within the approved execution scope remains ordinary Executor work; a review correction remains one ruled round. If no complete material condition can be stated, apply the current approve/dispose or BLOCKED route rather than inventing a finding. Cancellation stops the requested work; missing authority stops the dependent act; a capability failure is neither rejection of the Candidate nor permission to bypass its gate.

Model/effort choice stays with the authorized Coordinator under the existing quality-floor and Lean selection rule. A stronger model is one possible response to a diagnosed reasoning limitation, not a response to every failed command or round number. Unsupported settings changes, identity replacement and costs cannot be hidden inside continuation. No new model-choice form is needed.

### E2 — L2/L3 require concrete benefit beyond L1

L2 can bound accumulated working context, but reconstructs approved scope, path/base and prior evidence on each invocation. It needs an actual supported invocation/resume boundary, cancellation behavior, attributable source and preservation of the formal role holder. These are additional obligations before any measured benefit exists here. A narrow future repetitive workload with an objective oracle might justify it; this research has not established that workload or benefit.

L3 can keep retrying in the same context but must distinguish legitimate TFW WAIT/STOP from unfinished execution, preserve cancellation and avoid competing local state. Gather's pinned official hook exits for several reasons unrelated to product quality. Current [Claude Code hook documentation](https://code.claude.com/docs/en/hooks#stop), retrieved 2026-10-27, says Stop runs after a normal response, not a user interrupt; its continuation input warns about unresolved blocking conditions. The current page also documents a consecutive continuation safeguard whose counter resets on tool calls. This is a present documentation statement, not proof of behavior in Gather's historical commits, a total-work budget or a TFW acceptance rule. No hook or loop was run here.

The distinction strengthens L1's explicit termination/acceptance boundary. It does not establish that L2/L3 are impossible; it identifies the extra machinery and proof a concrete consumer would have to justify. Challenge should attack the minimal M11 policy first, then ask whether an actual failure needs either additional mechanism.

### E3 — Default, exception and hard freshness are different authority cases

Proposed R1 policy: a new governed phase normally starts a distinct independent Reviewer without the previous phase's review conversation. That Reviewer may read approved dependency artifacts and applicable review history needed to judge the new scope; freshness is not ignorance. Within the same phase, ordinary authorized corrections retain that Reviewer and the same Executor, including a new fixed Candidate when VALUE changes. A TS revision or a correction round does not by itself create a new phase.

| Receiving situation | Who decides / valid source | Required disposition |
|---|---|---|
| New phase under the accepted R1 default | Actual Coordinator responsible for that phase, within its mandate | Select a fresh independent R using the ordinary dispatch/activation route; no extra owner question |
| Proposed cross-phase R reuse under an accepted policy that explicitly permits exceptions | The same phase-responsible Coordinator, only if its governing authority includes that discretion and the phase TS/owner selection do not reserve or prohibit it | Record the concrete benefit, independence and receiving bound in the existing phase planning/dispatch artifact; exercise the granted exception, not a new approval workflow |
| Freshness is mandatory in the scoped frozen HL, approved TS or explicit owner choice; or exception discretion is absent/unclear | The authority that can change that actual constraint | No local waiver. Resolve the missing choice or change through the existing planning/approval route; a TS change uses its approval route, a frozen-HL change uses its resolved amendment ruler |
| Same-phase ordinary corrective round | Existing Coordinator ruling under the approved TS/live REVIEW | Retain E/R, review the affected return; do not reapply the new-phase default or seek a fresh owner gate |
| Independence is breached, identity/context is unavailable, or the actual platform cannot supply the required holder | Existing Coordinator diagnoses and routes a bounded replacement or exact blocked condition | Never describe contaminated reuse as an exception to independence, or unavailable capacity as a freshness waiver |

“Phase-responsible Coordinator” means the actual task Coordinator governing that phase in single-Coordinator mode, or its properly delegated phase Coordinator in a topology with separate phase Coordinators. A parent grant limited to coordination does not implicitly grant waiver of a child phase's constraints. Reviewer may report a mismatch and refuse; it cannot authorize its own exception. Executor cannot select or approve its Reviewer. This research proposes the policy; it does not itself grant reuse permission now.

An exception needs all receiving-context conditions from iteration 2, applied to R independently of E: unchanged role and actual native identity; exact B authority/approved TS and phase-local route; no simultaneous conflicting A/B act; explicit A completion or suspended state and treatment of retained A corrections; actual B workspace/path/base; independent access to the fixed reachable B Candidate while mutation is stopped; source/range and return binding. If A later needs correction while B is active, serialize and revalidate the affected activation or route a valid replacement; no silent switch back. A claimed fresh-context requirement cannot be satisfied by relabeling a retained conversation, clearing a title or forking Executor history.

The default can therefore coexist with a useful exception without making it discretionary everywhere. The accepted policy grants a bounded choice; a harder scoped requirement removes that choice. If no accepted exception policy exists, use fresh R or obtain the actual missing decision. This preserves owner control without making every correction owner-mediated.

### E4 — Independence, phase freshness and round reset have different costs

| Policy | Independence from E | New-phase freshness | Correction-context consequence |
|---|---|---|---|
| R1 | Mandatory; separate holder and permitted evidence | Default yes, with the explicit exception semantics above | Retains ruled findings and evidence; avoids compulsory reconstruction each round |
| R2 | Still mandatory; a fresh identity alone is insufficient | Yes if correctly provisioned | Reconstructs findings, dispositions and Candidate lineage each round; may expose anchoring but can repeat settled work |
| R3 | Still mandatory and must be rechecked for B | No previous-conversation reset | Retains project context and may save reconstruction; can carry prior assumptions and requires separately authorized B activation |

These costs and benefits are structural inferences, not measured performance rankings. Freshness does not prove better judgment; independence is a non-waivable acceptance property. R2 is coherent only after changing current same-Reviewer correction rules and justifying that cost; a real independence failure already has a replacement route without adopting universal R2. R3 remains a possible authorized exception rather than an implicit fallback when R1 is inconvenient.

Executor policy is separate: retain E for same-phase corrections. For phase B, a new E or a separately authorized sequential activation of the same unchanged E may be appropriate under the receiving conditions; a fresh B Reviewer does not force a fresh E. Reusing E does not grant R reuse, and retaining R does not grant E reuse. Different evidence obligations apply to each actual source/holder. No exposed close-agent mechanism proves slot release; neither completion nor archival establishes retained-ID capacity. N6 remains an execution obligation, not an invented four-ID lifetime ceiling.

### E5 — Minimal live consumers and specification inputs

The following is the incremental H4/H5 policy surface, not a replacement for iteration 1/2's C2/W2/S1 integrity map. Exact implementation selectors and denominator belong to the Coordinator's TS. Do not broaden the change set merely because a file mentions roles.

| Current path / addressed consumer | Necessary effect if M11 is adopted | Reuse / exclusion |
|---|---|---|
| `.tfw/conventions.md` → coordination/role continuity and `The 🔄 REVISE route` | Scope same-holder continuity to corrections; state phase-fresh R default, authorized exception and nonprogress routing/exit-versus-acceptance boundary | Reuse finding grammar, authority rungs, Launch selection and Knowledge handover; do not duplicate them |
| `.tfw/workflows/plan.md` → TS/dispatch and REVISE return | Coordinator applies the actual phase policy, checks permitted exception authority and records meaningful choice in existing planning/dispatch context | Existing HL/TS approval and live REVIEW ruling suffice |
| `.tfw/workflows/review.md` → Identity, activation, and trust | Distinguish new-phase entry from same-phase continuation; independently reject mismatched freshness/independence/Candidate scope | Ordered review and affected-return checks remain |
| `.tfw/workflows/handoff.md` → activation/REVISE/return | Clarify separate E phase activation and same-phase correction continuity where existing text could be read as cross-phase permission | Existing ONB/RF/EV sections can carry partial progress and failure; no new loop artifact |
| `.tfw/adapters/codex/AGENTS.md.template` and installed root `AGENTS.md` continuity sentence | Scope its unqualified “reuse the same Executor and independent Reviewer” consistently with the selected common rule | Follow established adapter/copy integrity route; no rewrite of every provider guide |
| `.tfw/templates/TS.md`, `.tfw/templates/RF.md`, `.tfw/templates/REVIEW.md` | Existing scope/AC, evidence and handover sections can express the selected policy and outcome | No new fields or template edit justified by H4/H5 alone |

Research/knowledge workflow rewrites, a new registry, schema epoch, parser fields for every exception and a maintained retry counter have no demonstrated consumer. Status readers should keep validating the adopted C2 structural contract; meaningful authority/freshness judgment remains S1 at receipt. C2-related adapter/profile and installed-copy changes still require their prior integrity coverage; the H4/H5 increment does not grant permission to skip them or add every file speculatively.

The accepted economics VALUE paths remain unchanged: `.tfw/economics/README.md`, `claude-code.md`, `antigravity.md`, `tfw_economics.py`. No actual interface defect was found. Expected invocations derive from ordinary actual dispatch/launch/return, including failures, retries and auxiliary work; counting an invocation grants no role authority. Same-source work needs disjoint ranges or a verified covering successor; new source/holder needs its own binding. A return cutoff excludes later substantive work, and prior covering revisions are preserved but not added. Source/version/setup and tail limits from accepted ECFIX remain material. H3's accepted interface is sufficient for this mapping; actual future receipts still need their own verification.

| Requested TS view | Decision input, without a new runtime |
|---|---|
| State | Existing lifecycle, gate and phase readiness; loop attempts do not become lifecycle states |
| Activity | Execute within scope → inspect result → ordinary retry or durable return; Coordinator diagnoses a recurring unchanged failure and takes the existing route |
| Sequence | Actual phase C, E and fresh R; fixed Candidate; same E/R correction; explicit branch only for a permitted B reuse or replacement |
| C4 | Human owner, native execution surface, actual role units and shared durable workspace; no invented controller service or slot disposer |

## Checkpoint

| Found | Remaining for Challenge |
|---|---|
| All two-factor combinations exposed; asymmetric E/R reset is explicit | Try to break M11 without introducing L2/L3 machinery pre-emptively |
| L1 adds nonprogress and technical-exit interpretation at existing consumers | Attack false success, unchanged failure, cancellation and blocked authority |
| Fresh-phase default, permitted exception and hard freshness have distinct rulers | Contradictory authority, unavailable capacity, A correction during B and contaminated R cases |
| E continuity is independent of R freshness; no per-correction new gate | Verify the separation survives changed Candidate and new-phase activation cases |
| H3 maps to accepted invocation accounting with no economics VALUE edit | Verify failed/retried/new/reused invocation dispositions without repeating ECFIX experiments |

OODA: observed the accepted Gather, addressed current TFW consumers and present primary hook documentation; oriented repetition/context mechanisms against existing consumers; decided on the complete two-factor space and a concrete default/exception contract for challenge; acted by writing this stage. One focused pass; direct primary-source documentation read, no new search queries, installations, loops, agents, product edits or permanent tests. The current web page is not historical behavior evidence.

Knowledge handover: source epoch is the immutable Gather/base above; local rules inspected at their named consumers. Material is the default/exception authority distinction, asymmetric E/R reset and minimal incremental consumers. These are source-based specification candidates, not a tested product cycle or measured quality/cost result. C2/W2/S1 and N1–N6 remain; N4 applies when reuse is selected, N3 still requires actual independent fixed-Candidate review. Own exact source binding and predecessor r2 remain as recorded in Briefing; final synthesis requires the successor receipt or an honest attributable gap/failure. HL/TS/control and economics VALUE paths are untouched.

**Sufficiency:**
- [x] External primary source used with current-versus-historical distinction.
- [x] Briefing gaps converted into concrete policy choices and challenge obligations.
- [x] Configuration space built from Gather's two factors, with shared properties grouped.

Stage complete: YES

Recommend closing Extract. Question: accept M11's default/exception contract and minimal consumer map as the main Challenge target, retaining L2/L3 and R2/R3 as alternatives requiring concrete added value?

→ Coordinator decision: accepted Extract at `6ee2ae6d5fd61f0c668be607635c161587c2d572`; authorized Challenge of M11, explicit exception discretion and the genuine unavailable fresh-context case. Minimal consumers accepted; economics VALUE unchanged; RES waits for the Challenge checkpoint.
