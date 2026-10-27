# Extract — Minimal C2 adoption contract

> Mindset: Analyst. Separate required decisions from optional machinery.
> Parent: [approved HL](../../HL-TFW_20261027-161333_CMODES.md).
> Goal: Refine C2 into reviewable specification choices while preserving historical continuation and actual authority.
> Producer: `/root/cmodes_research`, native source `01a17db6-0f53-7603-878a-adaa590010e4`; parent `/root`.
> Inputs: Gather `6ff344568784f9bf8dfe04f4ed6add5a49149c27`, accepted by the Coordinator; continuing dispatch `4fb66e15f98f8f760a615e22f92f3bc44262e27c`; frozen HL authority `28af8624b5a42f5078e6303ca844dabd1fbbcab6`. Effective baseline/native-gates/tfw-gates-only and this Researcher's unit are unchanged.

## Configuration Space

Gather has two factors, so use a structured comparison rather than nine repetitive scenarios. W1/W2/W3 concern **Write boundary**; S1/S2/S3 concern **Selection checks**. All nine pairs are syntactically conceivable. Their shared consequences are separable: an S option does not fix a write-boundary problem, and a W option does not authenticate a human choice. The table maps those consequences for Challenge without selecting a final architecture.

| Family | Write boundary | Selection checks | Distinct value | Cost or necessary condition |
|---|---|---|---|---|
| M: minimal complete option | W2: new carrier or explicit adoption uses current format; ordinary historical continuation preserves its epoch | S1: immutable source plus meaningful agent verification of narrative authority | Uses current provenance and operating-choice records; no extra schema epoch, grammar or runtime | Must define issuance/adoption precisely and expose refusal/unknown outcomes; agent must actually inspect the source and current receiving context |
| T: stricter selection representation | W2 | S2 canonical body clauses, or S3 typed event fields | Can mechanize agreement of the declared mode/scope/effect with status for non-agent consumers | Needs a real consumer/value case; adds grammar/schema and readers, yet human assent and checkpoint satisfaction still require evidence |
| U: uniform migration | W1: any status mutation adopts current shape | Any S option | Uniform live shape after a write | Valid legacy continuation waits for sufficient adoption evidence; cannot silently synthesize mode or turn an ordinary return into a fictional owner choice |
| V: explicit format epoch | W3: discriminator controls format-specific reads/writes | Any S option | Directly labels the chosen schema for tooling | Adds field semantics and migration; unknown/downgraded labels still require provenance. It does not grant authority or eliminate human-source inspection |

T includes W2/S2 and W2/S3. U includes W1/S1–S3; V includes W3/S1–S3. M is W2/S1. Every pair is represented once, with shared requirements below. New combinations T/U/V add no independent permission or lifecycle controller. C1 from iteration 1 remains a fallback if explicit status mode is not accepted: the same authority/adoption checks then resolve mode from the immutable source at each use.

## Findings

### E1 — W2 distinguishes the operation, not just the resulting key set

The following is a proposed specification boundary for Challenge, not a change to the current writer. “Record” here must distinguish a status carrier from a new artifact or journal event. A new RF, research stage or current-grammar event under an already valid mandate does not by itself create a new task/phase status or select another mode.

| Operation | W2 treatment | Source and consequence |
|---|---|---|
| Read an existing complete historical carrier | Preserve its exact historical shape and applicable authority | Historical mode absence is not `manual`, `visible-agents` or `subagents`; use actual verified prior choice when needed |
| Advance lifecycle/update timestamp or return an artifact for the same governed scope, holder and authority | Ordinary continuation may preserve historical status grammar; new artifacts/events follow their own current templates | Requires valid existing activation and pending gate/transition authority. It cannot introduce a new mode, parent, holder, reporting choice or permission |
| Issue a new task or phase status, even if copied from an old file | New carrier: proposed complete current shape, including explicit mode and current upward spelling | Copying a five/seven-field carrier does not inherit legacy standing; new phase needs its own governing authority and actual routes |
| Explicitly adopt the current representation without changing the actual settled choice | Safe, deliberate format adoption; emit the complete current shape | Verify the actual existing choice, exact immutable source and observed unchanged recipient. Reuse that valid source; do not invent a `coordination_selected` event asserting a new human decision |
| Actually change mode, reporting, dialogue, holder/route or authority/activation scope | Treat as a semantic change, not ordinary continuation | Use the appropriate actual approval/selection/handoff under the frozen ceiling. Current issuance applies; preserve pending gates and valid units where the choice is non-revoking. A frozen change still needs its proper amendment |
| Merely append an unrelated TRACE commit or edit a free HL section | Does not change the frozen coordination epoch or mode | Do not advance `coordination_authority` to the latest HEAD for convenience |
| Remove mode from an already adopted current carrier | Not legacy continuation | Inspect its actual preimage/lineage; missing current field is a regression, not a route back to legacy permission |
| Repair a partial/mismatched carrier | No dependent activation until the actual existing or newly ruled values are resolved | Never complete missing mode/parent/source with defaults; historical readability is not live repair authority |

Proposed current C2 shape is the existing seven routing/selection fields plus `coordination_mode`, with `upstream_route` and exactly one upward name. Recognized historical complete forms remain the five-field `owner_gateway` spine, that spine with the selection pair, and pre-mode seven-field `upstream_route` carriers. A new mode field combined with a partial spine, missing selection pair or historical upward spelling is not a fourth implicit migration state.

W2 needs the writer to inspect the actual selected path and prior carrier/authority, not just infer “old” from absent mode. Existing task-local Git provenance and dispatch/source refs can supply that context. An allowed-key reader remains useful but cannot distinguish a forged copy from genuine history by key count alone. No automatic repository scan, hidden migration queue or parallel schema registry follows from this proposal. If provenance is unavailable, preserve historical evidence and stop the dependent new issuance/adoption claim.

### E2 — S1 is a complete bounded authority check

Full machine verification of human consent is not the objective. S1 uses the current immutable baseline/event, the actual human answer source retained there, the role's receiving context and an accountable agent's semantic judgment. It can be complete without adding a typed human-consent parser.

At the actual activation/adoption checkpoint, the consuming agent must resolve:

1. **Carrier and source:** exact task/phase path, complete applicable shape, current status selection, immutable artifact/path/full commit, and actual initial choice for `baseline` or actual subsequent owner choice for the selected event.
2. **Meaning and scope:** whether the choice really states the proposed mode and reporting/dialogue/topology, covers this phase and role, preserves the frozen ceiling, and agrees with the previous values/continuation or revocation consequences. Attributed `on_behalf_of` is insufficient by itself.
3. **Effect and route:** whether the named checkpoint has occurred, the choice is applicable rather than stale/contradictory, actual holder/parent/owner identities agree, and any required recipient acknowledgement or revocation delivery is observed. Current status remains the live selection; a later unadopted event is not replayed as live state.
4. **Result:** proceed only for the supported bounded act; otherwise return the exact missing/contradictory fact to the authorized Coordinator. Record material grounds in the existing owned dispatch/stage/artifact, not a second permission ledger.

Mechanical validation still checks closed shape/enums, contextual parent identities, resolvable source and event envelope. Those checks narrow mistakes; they do not replace the four semantic questions. The implementation must label the distinction honestly instead of claiming that a zero-error parser result validates authority. S1 is not permission to accept vague prose: a missing or ambiguous mode/scope/effect is an unresolved authority fact.

S2/S3 could be useful if a named static consumer must compare explicit declared fields without an agent. Neither the current research mandate nor the inspected current consumers establishes a need for an autonomous adoption engine. Adding checkpoint evaluation, event replay, ownership inference or automatic status switching would create a new runtime outside the required value. Challenge should require a concrete benefit before retaining T or V over M; schema convenience alone is not evidence of that benefit.

### E3 — Same-holder phases still have independent permission

Under C2, a direct phase may name owner H upward only when its actual local holder C equals the governing task Coordinator, human owner and exact authority lineage agree, and the effective phase selection covers this topology. A foreign X with the same human owner fails. A distinct delegated phase retains its actual local P and upward C. These facts do not follow from `coordination_mode` alone; the field selects an operating mode, not a bypass of authority checks.

For dependent A and B, an exact ancestor event covering both may serve as their source, but each phase adopts locally at its actual checkpoint. A's completion is recorded locally by C; no C-to-C phase-ready message is needed. B's predecessor readiness and approved phase scope/TS remain separate from mode adoption. Workers read their local `coordinator_route` for all gates and returns; only C uses the owner upward route for owner-reserved decisions.

Holder replacement is not a lifecycle/timestamp update. Existing successor rules require saved authority, state and pending gates; actual successor identity; bounded dispatch; acknowledgement; and an authorized route switch. Until that is established the old route remains effective or the dependent action is explicitly pending. Root holder replacement cannot silently rewrite active phase recipients or create a worker-to-owner escape. Challenge must consider mixed checkpoints and unavailable notification, including the current parent-consistency reader's refusal while a transition is unresolved.

### E4 — Correction identity does not grant another phase

Within an existing phase/correction scope, the current Handoff and Review workflows require the same Executor and independent Reviewer, subject to the actual ruling and continued valid authority. That is a continuity requirement for that bounded work. It does not answer whether those native units may receive phase B after phase A.

Cross-phase reuse therefore remains a receiving-context specification question: would a proposed B dispatch be a new scoped activation of a still-independent role unit, and do the selected authority and phase-local records explicitly permit it? What artifacts are carried, which scope is closed/pending, and what evidence demonstrates that R has not become Executor, peer or consolidator for the reviewed result? If those questions are not resolved, capacity planning cannot assume a reusable pair. Fresh distinct phase units are also bounded by actual capacity; a slot limit does not grant reuse, replacement or silent mode switching.

The evidence packages in Gather remain intact. Any future native acceptance run must return full reachable fixed Candidate, actual Reviewer identity/context origin, approved TS/RF/EV, actual checkout/base, verdict and correction return. Later VALUE moves Candidate and requires review of the new value; later TRACE alone does not silently redefine the reviewed product. Source-based examples here provide no substitute for that run.

### E5 — Immutable Git evidence supports S1 without becoming authority

External source used: [Git revisions reference](https://git-scm.com/docs/gitrevisions), retrieved 2026-10-27, revision/path syntax. A revision plus path addresses the blob/tree at that revision, providing a stable way to inspect the exact supplied artifact instead of a moving branch file. An immutable object establishes inspected content, not its author's human consent, permission scope or the truth of an asserted native result.

This source supports M's use of existing immutable references. The missing step is semantic verification against the actual governing/receiving context, which is already required by the common workflow. No new machine-readable consent grammar is necessary merely to inspect exact content. Current reader/schema behavior remains as Gather established; no product code was altered or new parser behavior executed in Extract.

### E6 — Keep specification decisions, native proofs and ECFIX separate

| Work remaining | Owner / admissible next action |
|---|---|
| W2 operation boundary, S1 semantic obligations, direct-phase route/completion and holder-change behavior | CMODES common specification; Challenge can assess source-based adverse cases |
| Cross-phase receiving-context policy for E/R reuse | CMODES specification/authorized Coordinator ruling; do not derive it from correction continuity or arithmetic |
| Actual independent review/correction, two-phase cycle, interruption/restart, replacement, retained idle capacity and named cross-surface behavior | Future approved implementation/native evidence; this Researcher cannot launch those roles here |
| Accepted lineage-to-economics interface | ECFIX durable return through Coordinator; H3 stays pending |
| Own Researcher contribution | Same exact source; final validated covering successor to revision 1 or attributable failure/gap |

## Checkpoint

| Found | Remaining for Challenge |
|---|---|
| M = W2/S1 is a complete minimal option using existing provenance and meaningful authority judgment | Attack ordinary-continuation disguises, new copied carriers, downgrade and ambiguous source cases |
| Additional format/grammar combinations have grouped, explicit costs and conditional value | Determine whether any demonstrated consumer justifies them |
| Two dependent phases separate scope, adoption, readiness and actual holder | Challenge mixed/current/legacy checkpoints and unavailable successor acknowledgement |
| Correction reuse and cross-phase reuse have different authority questions | Preserve an explicit receiving-context decision and realistic capacity limit |
| Product/native proof and ECFIX gaps remain separate from design coherence | Do not promote design analysis to implemented acceptance or H3 support |

OODA: observed the accepted Gather matrix and current continuation/successor contracts; oriented them against the Coordinator's direction; decided to treat W2/S1 as a full option with grouped incremental variants; acted by specifying operation and semantic-check boundaries for Challenge. One focused pass, no new units, implementation, permanent tests or economics experiments.

Knowledge handover: producer and epochs above; inspected current status/selection/successor rules, status template, Handoff/Review continuity clauses and the official Git revision reference. Material is the explicit issuance/adoption distinction and complete S1 semantic contract, with cross-phase receiving context retained as unresolved. These are research proposals, not new operational authority or promoted architecture. Return only to `/root`.

**Sufficiency:**
- [x] External source used.
- [x] Briefing gap closed enough to challenge the remaining options.
- [x] Gather's two factors mapped through grouped configuration families.

Stage complete: YES

Recommend closing Extract. Question: accept M and the grouped alternatives for Challenge, retaining cross-phase E/R receiving context and H3 as explicit open boundaries?

→ Coordinator decision: accepted by `/root` after `b7517e489bea72d8383bd09af50e3442a87b840e`. Challenge M and actual refusal cases; retain added grammar/epoch only for demonstrated consumer value. Turn cross-phase E/R reuse into a TS-ready bounded recommendation or identify its exact contradiction. No close-agent/slot-release assumption; H3 remains pending.
