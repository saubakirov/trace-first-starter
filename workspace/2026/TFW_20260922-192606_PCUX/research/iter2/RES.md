# RES — TFW_20260922-192606_PCUX: Provider-specific coordinator UX and autonomy guidance

> **Date:** 2026-09-23
> **Author:** Codex Researcher
> **Status:** 🔬 RES — iteration 2 complete; Coordinator assessment pending
> **Parent HL:** [HL-TFW_20260922-192606_PCUX](../../HL-TFW_20260922-192606_PCUX.md)
> **Mode:** Pipeline, focused
> **Producer unit:** `codex:thread:local:01a0cb19-cbf2-7603-8775-c776f52660d4`
> **Parent Coordinator:** `codex:thread:local:01a0c980-4552-7ed3-b2aa-3c5cc46bc7bc`
> **Activation / dispatch source:** continuation command `/tfw-research TFW_20260922-192606_PCUX` and `journal/20260923-032812__dispatch__d5e4.md @ ff66d7ed5df678061d5689713fcf64c0e84ac744`; approved HL §4.1 mandate at `5259851e6f07206a07d022db11ef1cbc91dca775`
> **Coordination authority:** `HL-TFW_20260922-192606_PCUX.md @ 5259851e6f07206a07d022db11ef1cbc91dca775`
> **Originating proposer:** `none` for the continuation dispatch; owner `saubakirov` approved the governing mandate

---

## Research Context

The Coordinator accepted [iteration-1 RES](../iter1/RES.md) D1–D3 but prepared a second focused pass because exact authority/reference and reader semantics remained open. This iteration tested H5/H6/H7: command-first launch before the child's address is known; a pending or revoked owner choice; root-to-phase scope; same-unit continuation; and old/default state. The [Briefing](1_briefing.md) framed those questions, [Gather](2_gather.md) separated six dimensions, [Extract](3_extract.md) compared nine connected configurations, and the corrected [Challenge](4_challenge.md) screened all dimension pairs and failure cases. No schema, workflow, provider profile, HL or task-control implementation was changed by this Researcher.

## Decisions

| # | Research decision | Rationale and evidence limit |
|---|---|---|
| D1 | Keep one task/phase-local **current** `status.md` selection with a checked immutable owner-decision source; retain the frozen HL epoch as governing ceiling. Reuse current `activation` for effective **new-launch** authority and add only the reporting and exact current-selection reference needed by the approved mode choices. | Extract E1 and Challenge C2 eliminate status-only permission, duplicate operating-mode precedence and journal replay as a second live authority. A pending conditional event remains historical until its named gate. Exact field names, baseline representation and event grammar belong in TS. |
| D2 | Permit the authorized exact command to start before the parent knows the child's address when actual launcher/native origin, mandate, lifecycle and parent route are verifiable. Bind and record the real child ID from a creation receipt or first normal gate; use one transport-only readiness exchange only when the active surface needs it. | A pre-addressed dispatch cannot truthfully precede the first observed ID. Missing/foreign/ambiguous IDs refuse later directed operations; a duplicate exact tuple is not a second unit. This is source-level compatibility, not proof of every provider's native identity/readback reliability. Gather G2; Challenge C1. |
| D3 | Keep each phase's status as its workers' sole live choice. A root decision can cover a phase only after checking its exact source, frozen ceiling, phase/role scope and effect checkpoint and projecting the current choice locally. Prefer one constrained exact ancestor-decision reference in the new phase-status field; retain a phase-local adoption record only if that reference cannot be safely validated. | Root-live lookup can silently change an unrelated phase; copied prose can masquerade as a second grant. The preferred status-field exception does not relax phase-journal `refs` containment. TS selects its exact syntax/validation. Extract E2; Challenge C2. |
| D4 | Separate evidence of a unit's valid prior activation from the **current** permission to launch new units. A non-revoking switch preserves the same Researcher/Executor/Reviewer, pending gates and required returns; revocation stops new delegated dispatch and brings an active unit to a safe, reported boundary. | Treating any changed spine as retroactive invalidation loses work; ignoring the new choice allows stale delegation. Unavailable delivery/checkpoint is an explicit open action, not a claim of instant halt. Extract E3; Challenge C3; HL §3.6. |
| D5 | Use explicit baseline/default and migration rules: total absence of the original spine is read-only, partial/contradictory old/new spine refuses, and a valid old complete five-field status never gains delegation, iterative dialogue or fully manual transfer from absent new fields. | `plan.md` already offers owner-only/gates-only/owner gateway by default, with native vertical reporting; new positive grants/transfer require an actual owner source. A truthful complete migration precedes new semantics without re-asking settled approval. Exact validator compatibility is TS work. Gather G3; Challenge C3. |
| D6 | Correct both directions of the current dialogue/GATEWAY coupling in the target readers: GATEWAY may be gates-only, and owner-approved bounded peer dialogue must not require selecting a GATEWAY topology. Keep exact peer/purpose/boundary/consolidator/output/stop grant, vertical returns and independent Reviewer. | The validator currently accepts one combination and rejects the other, while Session identity/Plan and core peer prose impose older coupling. Frozen HL §§3 and 3.4/A5 make the selections independent; dialogue alone grants no launch, execution or widened send edge. The current PCUX mandate remains gates-only. Corrected Challenge C4. |
| D7 | Treat current conventions, status/event templates, `tools/tfw_state.py`, Plan and task-bound role readers as one semantic change surface; verify relevant manifest-owned installed copies and preserve the full model/reasoning-effort launch algorithm and strategic Plan passages. | A prose-only fix leaves validator rejection; a validator-only fix leaves early-address/continuation refusal. H3/H4 and active-provider reliability remain implementation checks, not new research gates. Extract E4; Challenge C4; HL A12. |

External source checks were bounded comparisons: [Microsoft's event-sourcing pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing) distinguishes event-authoritative replay from this project's status-authoritative contract; [Git revision verification](https://git-scm.com/docs/git-rev-parse) and [object inspection](https://git-scm.com/docs/git-cat-file) verify objects but not owner permission/current effect; [OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) supports explicit denial of ambiguous permission. The governing TFW/HL rules, not these external pages, authorize this task.

## Open Questions

| # | Question | Status | Answer / next owner |
|---|---|---|---|
| Q1 | What exact field/event grammar and reference validation implements D1/D3/D5 without ambiguity? | Design narrowed; TS/implementation owed | Specify baseline/no-later-decision form, event kind/content, effective checkpoint, constrained root decision reference, phase scope, old/new schema reading and negative cases. Coordinator/TS owns the choice. |
| Q2 | Can each active provider actually supply verifiable origin, later child ID and addressed same-unit return for a selected route? | Native reliability unproved | Check on that provider/surface at the matching launch/gate. A missing required mechanism yields an explicit owner-assisted/visible route; static design cannot substitute for this check. |
| Q3 | Is the later Claude browser addendum available as a completed owner-selected source? | Not selected in this epoch | The owner may later select its exact epoch/digest. It is relevant to tool-dependent compact eligibility, not a prerequisite to this authority-reader TS or conditional compact wording. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL status at this epoch | RES status | Evidence |
|---|---|---|---|---|
| H5 | Task-local authority/trace can support command-only launch with later child address. | Iter1 design-supported; provenance/reader interactions open | Design-supported for receipt/first-gate paths; native verification and reader implementation owed | Gather G2; Extract E3; Challenge C1/C2. |
| H6 | Gateway, dialogue and phase routes can express gates-only GATEWAY and separate phase Coordinators. | Iter1 design-supported; phase/reader compatibility open | Design-supported; target requires independent dialogue/topology in both directions | Gather G3/G4; Extract E2/E4; corrected Challenge C4; frozen HL §§3, 3.4. |
| H7 | Status plus immutable owner decision can express defaults, manual/delegated/transfer and safe switches. | Iter1 S1 design-supported; exact refs/legacy/continuation open | Design-supported with scoped phase-local projection and prior-launch/current-choice separation; exact grammar/implementation owed | Extract E1–E3; Challenge C2/C3. |

H1/H2/H8 remain iteration-1 conditional provider evidence limits, H3/H4 remain implementation checks, and H9 remains iteration-1 design-supported close work. None was retested or silently declared native-proven here.

## HL Update Recommendations

The Researcher classifies but does not apply or rule. Current implementation conflicts concern source readers and validator behavior, not a newly discovered need to change the frozen owner-approved result.

### Refinements — free sections, Coordinator applies

| # | § | What to update | Source |
|---|---|---|---|
| R1 | §2 | Make the as-is/target distinction exact: current validator/title/peer prose couple iterative dialogue and GATEWAY; current five-field status/event kinds do not carry reporting/current selection; early-address readers conflict with approved command-first timing. | Gather G1–G4; corrected Challenge C4. |
| R2 | §7.2 | Cite iteration-2 source findings for status/event/phase-local authority, reader/copy surfaces and bounded external object/authorization comparisons, without presenting them as implemented rules or provider trials. | Gather G1–G4; Extract E4; Challenge C1–C4. |
| R3 | §8 | Mark H5/H6/H7 research design as sufficient for TS while retaining exact field/reference grammar, validator/reader parity and native provider reliability as implementation/real-use obligations; keep the browser addendum unselected. | Decisions D1–D7; Challenge Checkpoint. |
| R4 | §9 | Add precise failure paths for conflicting late child IDs, premature conditional effect, out-of-scope root-to-phase projection, stale grant after revocation, partial legacy state and one-sided dialogue/GATEWAY repair. | Challenge C1–C4. |
| R5 | §10 | Record H5/H6/H7 as design-supported with their bounded remaining TS/native checks; note that H6's approved independence works both ways. Keep H1/H2/H8 conditional and H3/H4 outside research. | Hypothesis table above; corrected Challenge C4. |

### Amendment Proposals — frozen sections, resolved-ruler verdict required

No amendment proposals. Frozen HL §§1 and 3–7 already require command-first/later address, phase-local routing, live owner switches, independent GATEWAY/dialogue selections and preserved role/model obligations. Implementing those claims needs source changes, not a new frozen claim or self-issued verdict.

## Fact Candidates

The visible conversation history for this Researcher was reviewed. This continuation supplied Coordinator mode/stage gates and a correction interpreting the existing frozen HL, not a new direct human project observation. The current code/readers and external documentation are agent-discoverable and fail the Human-Only Test. No new fact candidates; iteration-1 owner-report candidates remain in [RES iter1](../iter1/RES.md#fact-candidates) for later `/tfw-knowledge` qualification.

## Strategic Insights (Research)

No strategic insights. No new human strategic briefing occurred in this Researcher unit; the owner's relevant values and choices remain in the governing HL §11 and are not re-authored from Coordinator messages.

## Findings Map

```text
initial approved baseline ──────────────────────────────┐
actual later owner choice ──> immutable scoped decision   │
                                   │ named checkpoint + source/scope check
                                   ▼                     ▼
                         task or phase status = current choice
                              │
                  ┌───────────┴────────────┐
                  ▼                        ▼
        next launch checks grant     same unit checks prior launch,
        and exact native origin      current effect and return route
                  │                        │
                  └──────> truthful ID/dispatch after observation
```

The frozen HL bounds every arrow; the journal does not independently compute live status. A revoked new-launch edge stops immediately, while an already running unit returns safely with its evidence.

## Iteration Status

- **Iteration:** 2 of 2 (min) / 5 (max)
- **Hypotheses tested:** H5, H6 and H7 — source-design supported, not implemented or provider-native proven.
- **Hypotheses deferred:** None within the prepared iteration-2 scope. H1/H2/H8's complete provider trials and the unselected browser addendum remain separately bounded from iteration 1.
- **Gaps discovered:** Exact `selection_ref`/event grammar and constrained phase-ancestor resolution; validation of owner-origin versus `on_behalf_of`; old five-field migration; identical-unit versus current-choice reader logic; both directions of dialogue/GATEWAY decoupling; later native ID reliability.
- **Superseded decisions:** Challenge C4's initial suggestion to retain `iterative → GATEWAY` as a target constraint was corrected at `cd1136a3d5a73d413abfc2aee9faa227ec0fe66b` after the Coordinator cited frozen HL §§3/3.4/A5. C6 root-live phase and C9 journal-replay configurations are eliminated; no owner/frozen decision was superseded.

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|---|---|---|
| 1 | Exact status/event/ref and legacy migration grammar | Implementers need one non-contradictory current authority and phase scope rule | Route into TS with focused negative cases, rather than a third research iteration absent a material new conflict. |
| 2 | Active-surface command/origin/ID/continuation checks | Static source analysis cannot prove native full-cycle reliability | Verify at each actual provider gate and report exact unavailable links; do not block conditional route documentation. |
| 3 | Owner-unselected Claude browser addendum | Could narrow tool-dependent compact eligibility | Consume only if owner returns a complete selected epoch; otherwise retain as an open bounded input. |

### Recommendation

- [x] **SUFFICIENT** — two configured minimum iterations are complete in research substance. Proceed to `/tfw-plan` to assess both RES returns, apply/rule HL recommendations and prepare the scoped TS; implementation/native checks remain explicit obligations, not fabricated research proof.
- [ ] **MORE NEEDED** — no third iteration is justified by the present source record alone.
- [ ] **BLOCKED** — no blocker for this research synthesis; owner-reserved TS/mental-model verdicts remain future gates.

## Conclusion

Iteration 2 located the reader and reference seams that iteration 1 left open: effective launch selection, immutable human decision, pending future effect, phase-local projection and historical valid activation are different facts. The smallest source-compatible design keeps one current task/phase status, a checked owner-decision event, later truthful child-ID recording and same-unit continuation through switches and revocation. It also requires both dialogue/GATEWAY dependencies to be removed in the target while preserving a narrow peer grant and independent review. The work remains source-level research: exact schema syntax, implementation parity and native provider reliability have not been demonstrated here, and the unselected browser addendum was not used.

### Material handover at this return

Producer/unit: the Researcher named above. Source/epoch: approved HL/control `ff66d7ed5df678061d5689713fcf64c0e84ac744` with frozen mandate `5259851e6f07206a07d022db11ef1cbc91dca775`; accepted iteration-1 RES `a2c3c717311cf5e02dcd8018284b7e8613de2326`; iteration-2 Briefing `73ca536b536d09f2f8e0454e76c42aee5168ea21`, Gather `7c5aaf22909462183ceaa80921baf758644ad46e`, Extract `ceb69657cb3b38b5c2a0c130527d5542ade59fac` and corrected Challenge `cd1136a3d5a73d413abfc2aee9faa227ec0fe66b`; official Microsoft/Git/OWASP pages opened 2026-09-23. Inspected scope: H5/H6/H7, task/phase status and event contracts, validator, Plan/role readers and adapter-copy inventory; no other unit's transcript or unfinished work. Material: D1–D7 and classified free-section refinements; no frozen amendment proposal or new human Fact Candidate. Uncertainty: exact TS grammar, active-surface identity/continuation and owner-unselected browser input. Continuation: return this RES to the recorded Coordinator; it decides whether to advance through `/tfw-plan`, and this Researcher edits no HL, TS, code, status or iteration control.

---

*RES — TFW_20260922-192606_PCUX: Provider-specific coordinator UX and autonomy guidance | 2026-09-23*
