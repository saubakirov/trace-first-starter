# Extract — What do we not see?

> **Mindset:** Analyst. Combine Gather's choices, then locate the smallest source changes without claiming implementation.
> **Parent:** [HL-TFW_20260922-192606_PCUX](../../HL-TFW_20260922-192606_PCUX.md)
> **Goal:** Preserve strategic Coordinator planning while enabling command-only launches, live mandates, provider routes and complete documented closure.
> **Producer / route:** `codex:thread:local:01a0cb19-cbf2-7603-8775-c776f52660d4` → `codex:thread:local:01a0c980-4552-7ed3-b2aa-3c5cc46bc7bc`.
> **Evidence epoch:** governing HL/control `ff66d7ed5df678061d5689713fcf64c0e84ac744`; Gather `7c5aaf22909462183ceaa80921baf758644ad46e`; official Git object documentation opened 2026-09-23. No new owner browser source was selected.

## Configuration Space

The D1–D6 cross-product exceeds 30. These task-relevant connected cases vary at least one dimension and are not claims of admissibility or native reliability. Gather's letters retain their meanings; `B/C` records a contingent pair, not a new choice.

| Config | D1 — source of an effective launch grant | D2 — first trustworthy child identity | D3 — future or revoked operating selection | D4 — root-to-phase scope | D5 — same-unit continuation | D6 — legacy/default interpretation |
|---|---|---|---|---|---|---|
| C1 initial delegated root | C current status + frozen mandate | A receipt | B pending decision until gate | B phase-local state with exact ancestor source | B revalidate current state, preserve unit | A legacy read-only/new defaults |
| C2 delayed identity | C current status + frozen mandate | B first ordinary gate | B pending decision until gate | B phase-local | B same unit | A |
| C3 contingent readiness | C current status + frozen mandate | C one transport-only exchange if needed | B | B phase-local | B same unit | A |
| C4 owner switch to manual launch, native gates | C current status + owner decision | A receipt for a later owner-created role | B effective only at named gate | B phase-local | B existing Researcher returns as same unit | A |
| C5 explicit fully manual transfer | C current status + owner decision | A owner-created visible role receipt | B effective at named gate | B phase-local | B existing unit keeps identity | A |
| C6 root-live phase choice | C current status + owner decision | B first ordinary gate | B | A phase re-reads root choice live | B same unit | A |
| C7 new or already-live phase under scoped root choice | C current status + owner decision | A or B from actual launch | B | B phase-local projection of scoped root choice | B same unit where already active | C truthful one-time migration if old phase lacks spine |
| C8 separately approved phase choice | B later direct-owner decision | A role receipt | B | C separate phase decision | B same unit | A |
| C9 event-replay variant | B immutable decisions | B first ordinary gate | C every reader derives live mode from history | A phase reads root decision history | B same unit | C |

**Combination absent from the Briefing:** C7 makes a future root decision affect an already active phase only at its named gate, while that phase's current status remains locally authoritative and its running unit keeps its ID. It also covers a phase created later under a root choice whose recorded scope includes it; neither case needs a repeated owner approval merely because there is another phase. Whether one controlled ancestor reference or a local adoption record carries that projection is left for Challenge.

## Findings

### E1 — Current choice, immutable decision and baseline are three different facts

Iteration-1 S1 remains the smaller candidate if each field has one job: `coordination_authority` retains the governing frozen HL epoch and reservations; `activation` describes the **effective authority for new launches** (`owner-only` or `delegated:{exact immutable grant}`); `dialogue` and `owner_gateway` remain independent; one reporting value distinguishes required native vertical sends from the explicitly chosen owner-transfer exception; one exact current-selection reference points to the owner decision where a post-inception selection is in force. The first default owner-only/gates-only/native-reporting choice need not fabricate a decision event; TS must define its unambiguous baseline/no-later-decision representation. An initial delegated choice already has the frozen HL mandate cited by `activation` and `coordination_authority`. This is a candidate field interpretation, not implemented schema. Sources: iteration-1 RES D1/D3; HL §§3.4, 3.6, 4.1; `.tfw/templates/status.md`; `tools/tfw_state.py` closed keys/validation.

The ordinary owner decision needs one new task/phase-local journal kind because `gate_answer` requires an actually blocked role, `transition` changes lifecycle, and `ownership_changed` does not select operating mode. Its event records actual direct-human source, old/new launch and reporting selection, affected roles/scope, effect checkpoint, reservation/expiry and governing authority epoch. `on_behalf_of` alone is accountable-human attribution, **not** evidence that the owner personally made this selection; copied agent text or a title cannot supply it. A future conditional event stays pending: status still shows the old effective choice until the named Coordinator gate; the Coordinator then validates the condition/source and updates current status, citing that same immutable event. A revocation stops new delegated dispatch at once, while an active unit returns safely through its actual route. `selection_ref` and `activation` may cite the same event but answer different questions (why current choice is valid versus what kind of new launch is allowed); TS must reject contradictory combinations instead of letting readers choose precedence. Sources: HL §3.6; `.tfw/conventions.md` → `Task control files`, `HL Contract` rule 8 and `Workflow activation and routing`; `.tfw/templates/journal/event.md`.

The alternatives have costs that Challenge will test: a second `operating_mode` plus `activation` reproduces the launch choice; journal replay makes events the live state contrary to the current status contract; changing status when a future decision is merely recorded activates it early; status/provider-only flags lack the immutable human decision. [Git `cat-file`](https://git-scm.com/docs/git-cat-file) verifies that an object exists and can show its content/type; this is useful for an exact cited commit, but the object's existence does not attest that a human authorized the scope or that the event is currently effective. Those must be checked against the actual owner source and local state.

### E2 — Phase-local projection can preserve one owner choice without a second live state

The governing root choice can be used for a phase only if its immutable decision or frozen mandate actually covers that phase and role, the phase's own HL is a valid derivation, and the phase's **local** status records the choice effective for its workers. The task status must not mirror phase lifecycle or route, and a phase must not silently read root status as its current mode. A later root switch limited to Phase A must leave Phase B unchanged; a root choice including a future Phase B can be projected at its creation/checkpoint without a second owner decision. This follows `.tfw/conventions.md` → `A phase carries its own state` and the HL §3.6 scope/effect requirement, rather than importing a new phase-mode registry.

The exact cross-scope reference grammar remains a TS choice with two bounded options to challenge: (1) a phase status field cites the exact root decision path plus immutable epoch under an explicit, validated ancestor exception; or (2) a phase-local adoption event cites local authority and records the verified root decision identity in its body, while status points to that local event. The existing journal `refs` rule forbids escaping the owning task/phase, so a raw `../journal/...` in a phase event's `refs` is not valid today. Either option requires opening the actual root decision, checking its human source/scope/effect, and preserving the phase's local current status as authority. A free-form root path or copied decision prose is not equivalent. Sources: `.tfw/templates/journal/event.md` ref rules; `.tfw/templates/status.md`; `tools/tfw_state.py` `read_phase_status`; HL §§3.4, 3.6.

### E3 — Launch validity and continuation validity must not be collapsed

The command-first role can validate its exact `/tfw-*`, task/phase, lifecycle, current mandate and native origin before material work even if its parent has no child address yet. A creation receipt is one address source; if absent, the role's first normal gate can identify itself through a verifiable native sender/self-ID. The parent records a truthful addressed dispatch **after** observation; later addressed sends need that exact address. A contingent transport-only readiness exchange is permitted when the ordinary gate/receipt lacks necessary ID or workspace metadata, never as a universal pre-start handshake. If the provider cannot expose trustworthy origin or destination when required, the path stops or becomes explicitly owner-assisted. Sources: HL §§3.4–3.5; Gather G2; `.tfw/conventions.md` → `Workflow activation and routing`; `.tfw/workflows/plan.md` Step 7.

An operating switch does not create a new Researcher, Executor or Reviewer. The prior activation/dispatch remains evidence that the same unit validly began; **current** status controls new launches and the current route/reporting/dialogue; continuation verifies the old unit's identity, still-applicable scope and new decision's effect on ongoing work. A non-revoking switch to manual launch after research does not void an in-flight Researcher return; a revocation forbids new delegated acts and brings current work to a safe return, preserving artifacts. This needs a focused amendment to today's phrase “same immutable authority and routing spine,” which otherwise reads as if any valid mode change automatically invalidates the unit. It does not grant fresh work or bypass owner-reserved gates. Sources: HL §3.6; `.tfw/conventions.md` → `Workflow activation and routing`; `.tfw/workflows/plan.md` Step 1; iteration-1 RES D1–D3.

### E4 — Affected reader and copy surface

| Surface | Current assumption to change or verify | Minimum responsibility in TS |
|---|---|---|
| `.tfw/conventions.md` HL rule 8, Task control, Session identity, Workflow activation/routing, Launch selection | Early addressed dispatch, identical continuing spine, iterative-only GATEWAY title; model/effort rule already exists | Separate immutable grant/current choice/late address/continuation; retain model/effort and direct-parent gates. |
| `.tfw/templates/status.md`, `.tfw/templates/journal/event.md`, `tools/tfw_state.py` | Closed five-field spine, closed kinds, no reporting/selection ref; validator couples iterative dialogue to gateway | Define/validate current reporting, exact decision reference, event kind, scope/legacy behavior and independent topology/dialogue. |
| `.tfw/workflows/plan.md` | Coordination Selection, title, dispatch and existing-work routing assume older timing | Apply owner selection at named checkpoint, derive phase-local current state, record actual later address; preserve strategic planning and launch selection. |
| `.tfw/workflows/research/base.md`, `handoff.md`, `review.md`, `docs.md`, `knowledge.md` | Each task-bound entry rechecks spine/dispatch; same-unit correction/return paths vary | Read effective selection and prior valid launch separately; keep Role Lock, same-unit return and exact Coordinator route. |
| `.tfw/adapters/manifest.yaml`, provider persistent templates and installed roots | Copies repeat activation/spine or title mechanics; manifest owns install target | Update the canonical owner then verify installed/copy parity; profile mechanics cannot override core authority. |

This table identifies semantic readers, not an instruction to edit all files automatically. TS should distinguish an affected rule from an unaffected copy or an unrelated workflow. `init`/`update` installation must keep managed copies aligned with the manifest; neither a provider profile nor a title creates permission. H3/H4 remain implementation checks. No permanent test suite is proposed merely to meet a count.

## Checkpoint

| Found | Remaining for Challenge |
|---|---|
| C1–C9 connect the six Gather dimensions, including a scoped root-to-already-live phase switch absent from the Briefing. | Stress source mismatches, out-of-scope phase projection and ambiguous/late native ID. |
| S1 can keep current selection in status and human decision in an immutable event without a second mode registry; baseline/default and cross-scope grammar remain explicit TS choices. | Decide whether controlled ancestor status ref or local adoption event avoids hidden authority and unnecessary ceremony. |
| Prior activation evidence can survive a legitimate current-mode change while current status governs new launches and safe continuation. | Test revocation, pending gate, legacy read-only and same-unit return against every affected reader. |

**Sufficiency:**

- [x] External source used: official Git `cat-file` documentation opened 2026-09-23 to distinguish object verification from human grant/current effect.
- [x] Briefing gap closed for Extract: connected authority/reference/reader configurations and an unproposed active-phase case are mapped.
- [x] Configuration Space built from Gather D1–D6; alternatives remain labeled by evidence and await Challenge stress.

**Stage decision:** carry the status-current/immutable-decision candidate, delayed-ID variants and two bounded phase-reference forms into Challenge. Do not treat a pending decision, a historical grant or a Git object alone as a live selection.

## Material handover at this checkpoint

Producer is the Researcher unit above. Source/epoch: Gather `7c5aaf22909462183ceaa80921baf758644ad46e`, approved HL/control at `ff66d7ed5df678061d5689713fcf64c0e84ac744`, inspected state/event/validator/Plan/role/manifest readers, and official Git documentation opened 2026-09-23. Material: nine connected configurations, distinct baseline/current/pending reference roles, scoped phase projection alternatives, same-unit continuation semantics and an affected-reader map. Uncertainty: exact phase reference grammar, old/default migration and revocation failure handling need Challenge; no source implementation or provider full-cycle trial has occurred. Continuation: return Extract to the recorded Coordinator and wait for its gate before Challenge.

---
Stage complete: YES
→ User decision: no new owner choice requested; unresolved technical variants move to Challenge under the frozen HL.
