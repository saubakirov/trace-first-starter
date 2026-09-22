# Challenge — What do we not expect?

> **Mindset:** Critic. Try to make a historical grant look current, an unknown address look known, or a root choice silently become a phase choice.
> **Parent:** [HL-TFW_20260922-192606_PCUX](../../HL-TFW_20260922-192606_PCUX.md)
> **Goal:** Preserve strategic Coordinator planning while enabling command-only launches, live mandates, provider routes and complete documented closure.
> **Producer / route:** `codex:thread:local:01a0cb19-cbf2-7603-8775-c776f52660d4` → `codex:thread:local:01a0c980-4552-7ed3-b2aa-3c5cc46bc7bc`.
> **Evidence epoch:** approved HL/control `ff66d7ed5df678061d5689713fcf64c0e84ac744`; Gather `7c5aaf22909462183ceaa80921baf758644ad46e`; Extract `ceb69657cb3b38b5c2a0c130527d5542ade59fac`; official OWASP guidance opened 2026-09-23. This is source-level stress, not an implemented schema or provider full-cycle trial.

## Consistency Check

All 15 dimension pairs from Gather D1–D6 were screened against the frozen HL and current source contracts. The table records material incompatibilities; an unlisted pair is not automatically authorized and still needs the case's actual source/scope/identity checks.

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|---|---|---|---|---|
| D1 effective grant | Mutable status/provider setting alone | D3 selection timing | Any delegated or future choice | A mutable value supplies no direct-owner decision or frozen mandate; this would be self-granted authority. |
| D1 effective grant | Frozen HL mandate only | D3 selection timing | Later explicit owner switch | The stable ceiling does not say which current launch/reporting choice is in effect after a switch. |
| D1 effective grant | Later decision alone | D4 phase scope | Phase without checked frozen/derived authority | The new event cannot widen §4.1 or replace the governing phase HL. |
| D2 child identity | Preallocated dormant address | D3 selection timing | Activation only at named future gate | The role could be activated out of phase or require a waiting prompt, contrary to command-only gate timing. |
| D2 child identity | First ordinary gate | D1 effective grant | Prior addressed dispatch required before any work | A truthful addressed event cannot precede the first observation of the child ID. |
| D2 child identity | Missing/ambiguous sender and self-ID | D5 continuation | Exact same-unit return | Neither a parent nor Reviewer can attribute a return or safely address the same unit from an invented ID. |
| D3 selection timing | Change current status when conditional instruction is merely recorded | D5 continuation | Same-unit revalidation | A role may take the future selection as immediately effective before the owner's named checkpoint. |
| D3 selection timing | Replay journal decisions for live mode | D4 phase scope | Local phase status as sole live authority | Event-derived/root-live state becomes a second competing current phase choice. |
| D3 selection timing | Chat/provider-only choice | D6 legacy/default | Read-only missing spine | Neither source can authorize a current role from a missing or incomplete task-local carrier. |
| D4 phase scope | Phase reads root status live | D5 continuation | Local phase route and role identity | A root mode change could silently alter Phase B or bypass Phase A's own current status/route. |
| D4 phase scope | Copied root decision prose without exact source/scope | D1 effective grant | Current phase choice | A paraphrase cannot prove the owner decision covers that phase, role and checkpoint. |
| D5 continuation | Reuse initial grant while ignoring current selection | D3 selection timing | Immediate revocation | The stale launch grant would authorize further delegated actions after revocation. |
| D5 continuation | New unit on every switch | D3 selection timing | Switch with pending gate/accepted work | Recreating a role loses the same-unit correction/return chain the HL explicitly preserves. |
| D6 legacy/default | Synthesize delegation or owner transfer from absent fields | D1 effective grant | Immutable mandate/decision required | The absent fields cannot imply a delegated launch or suppress native reporting. |
| D6 legacy/default | Treat partial/unknown state as permissive manual mode | D2 child identity | Later address binding | The child could begin despite invalid scope/route and later launder that start through a real address. |

**Surviving configurations:** “survives” means compatible with the approved design after focused reader/schema changes; it is not an assertion that the current validator accepts it or a platform trial passed.

| Config | Launch and address | Effective selection and scope | Continuation / legacy boundary | Verdict |
|---|---|---|---|---|
| C1 initial delegated root | Exact command and frozen mandate; receipt supplies ID | Current root status and covered phase-local status | Same unit checks current effect; missing legacy spine is read-only | Survives. |
| C2 delayed identity | Exact command and verifiable origin; first normal gate binds ID | Same as C1 | No invented earlier addressed event | Survives conditionally on native sender/self-ID proof. |
| C3 contingent readiness | Exact command; one transport-only check only if receipt/gate misses needed metadata | Same as C1 | Same unit and exact route | Survives as provider-scoped fallback, not universal handshake. |
| C4 owner switch to manual launch/native gates | Later owner creates next role; receipt/first gate binds ID | Pending event becomes current only at named gate | Current Researcher returns on its existing ID; native reports remain required | Survives. |
| C5 explicit fully manual transfer | Owner launches visible roles | Immutable owner choice selects transfer explicitly in local status | Same units/artifacts; exact owner-carried gate, no unsolicited agent send | Survives only with that explicit decision. |
| C6 root-live phase choice | Child ID may be sound | Root status silently overrides phase-local current mode | Same unit may see two conflicting choices | Eliminated: violates phase-state authority. |
| C7 scoped root decision projected to phase | Receipt or first gate supplies actual ID | Phase-local current status cites checked root decision and local phase authority | Existing unit continues or safely returns; old phase migrated truthfully if needed | Survives; one controlled ancestor decision reference is the smaller candidate. |
| C8 separate phase owner choice | Exact role address | Distinct direct-owner event valid for that phase | Same-unit return | Survives only when the owner actually makes that separate choice; not a required ceremony per phase. |
| C9 event replay | Actual child address possible | Journal/root history computes live phase mode | Local status loses its sole-current-authority role | Eliminated under existing TFW state contract. |

**Unexpected survivors:**

- C2: the parent need not know a new role's address for that role to start when actual command origin and mandate are verifiable; the first normal gate may supply the parent's later exact destination.
- C4: a switch to manual launches does not erase the currently active Researcher or remove its duty to return through the recorded native route.
- C7: one root owner decision can cover a later-created or already-live phase without a second owner approval, but only after scope/effect verification and an explicit phase-local current-status projection.

## Findings

### C1 — Late address, duplicate sender and false dispatch history

Stress sequence: an authorized Coordinator issues only `/tfw-research <task>` at `RES`; the child validates the task/phase, current mandate, lifecycle, actual launcher/native origin and parent route before material work. Its parent initially lacks a destination ID. The child's first normal gate reports through `coordinator_route` and exposes a native sender/self-ID; only then does the parent write an addressed `dispatch` with the actual observation source/time and later use that ID for addressed continuation. An already available creation receipt shortens this path; a missing origin or unverifiable sender does not. A second gate with the **same** ID and dispatch tuple is the same logical unit, not another child. A conflicting ID, foreign parent, repeated parent claim or different scope cannot overwrite the first dispatch or be reconciled by title; stop the affected path and report the discrepancy to the Coordinator. This preserves HL §3.3/§4.1 provenance without a ticket or backdated event. Current `.tfw/conventions.md` and `plan.md` early-address prose must be corrected together with role-entry readers; a `dispatch` event written only after observation is not a missing pre-work permission. Sources: HL §§3.4, 4.1; Gather G2; Extract E3.

### C2 — Pending decision, root-to-phase scope and one current status

Stress sequence: the owner states “after research, use manual launches” while Researcher is active. The Coordinator records the direct-human decision and named effect gate in a new immutable owner-decision event, but current task/phase status remains on the existing choice until Researcher returns. At that gate the Coordinator verifies the event's actual source, previous/new selection, scope, frozen §4.1 ceiling and reservations, then changes the selected current status and exact decision reference. The Researcher does not self-apply the event. A new role follows the now-effective choice; no completed research is replayed and no second approval is asked merely because the phase is ready. If the condition never occurs, the event remains pending history, not current authority.

For a scoped root decision, a phase's **own** status must carry the effective choice for its workers; root status is not their live mode. The smaller candidate is a controlled ancestor decision reference in the new phase-status selection field: exact task-root event path/immutable epoch, validated owner source and phase/role/effect coverage, plus the phase's separate local `coordination_authority`. This is a narrow exception that TS must define for the new status field; it does **not** relax the existing phase-journal `refs` containment rule. If such a constrained status reference cannot be validated by the implementation, the alternative is an explicit phase-local adoption record that points to the checked ancestor through a valid local authority path, not copied prose pretending to be a second owner grant. C6's live root lookup fails because a decision limited to Phase A could silently change Phase B. C8 remains available when the owner actually selects a different phase choice, not as routine per-phase confirmation. Sources: HL §3.6; `.tfw/conventions.md` → `A phase carries its own state`; `.tfw/templates/journal/event.md`; Extract E2.

### C3 — Revocation, same-unit return and legacy/default failure

Stress sequence: while Executor is active, the owner immediately revokes delegation. The Coordinator records the exact owner act and updates effective status at once, stopping **new** delegated dispatch. It addresses the active unit if that exact channel is available; the unit rechecks at its next safe gate, stops newly delegated actions, preserves current artifacts and returns actual state through its own Coordinator. If delivery or the unit's next checkpoint is unavailable, record the exact open action rather than claiming instant remote halt. The previous launch remains evidence that the unit began validly; it is not authority for new work. A non-revoking switch instead lets the same unit finish its already authorized in-scope return/correction under the updated route/reporting rule. Its ID, pending gates and independent Reviewer identity survive. Neither case permits a fresh task outside the old/new common scope or an owner-reserved verdict.

The exact legacy split is: total absence of the original five-field spine is read-only; a partial or mismatched old/new spine refuses; a valid complete old five-field status can be interpreted at its documented native-reporting baseline only for compatibility, then migrated truthfully to the new complete schema before a current write/launch needs new semantics. No missing field implies delegation, iterative dialogue or fully manual transfer. An initial new task defaults to owner-only, gates-only, owner gateway and required native gate reporting; positive delegation or transfer requires its own source. This preserves `.tfw/conventions.md` → `Task Statuses`, `Workflow activation and routing` and `plan.md` Step 5 while avoiding a needless re-approval of already valid unchanged tasks. The exact old/new validator transition is TS work, with focused negative checks, not a permanent test-count target. [OWASP's authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) independently recommends denying by default and validating each request; that is a safety analogy for refusing ambiguous current grants, not a substitute for TFW's own owner/mandate rules.

### C4 — Reader coherence and the dialogue/GATEWAY asymmetry

The surviving path requires `.tfw/conventions.md` authority/session/launch text, status and event templates, `tools/tfw_state.py`, `plan.md`, role-entry/continuation readers, and only their relevant manifest-owned installed copies to agree on current choice, historical launch evidence and later ID binding. A prose-only change would leave the closed validator rejecting new fields/event kind; a validator-only change would leave role readers demanding a pre-addressed dispatch. Phase status must remain local, and the Coordinator alone reads `owner_gateway`; role gates always go to `coordinator_route`. A GATEWAY title/readback remains navigation only. H3/H4 and actual platform reliability are separate verification, not a reason to postpone the compatible conditional profile language.

One asymmetry needs precise TS treatment: `gateway:{address}` with `tfw-gates-only` is already structurally accepted by `tfw_state.py` but discouraged by current Session identity/Plan prose, so the chosen gates-only GATEWAY needs those readers corrected. The reverse validator implication (`iterative` requires `gateway:{address}`) is not itself proof that dialogue grants execution or that a gateway may join peer talk; every peer dialogue still needs its exact immutable grant and separate GATEWAY under current root routing. Do not loosen that guard solely to make fields look mathematically symmetric. The HL separates **selection authority** and **communication permission**; the chosen route's essential fix is that GATEWAY does not imply iterative traffic. Sources: `tools/tfw_state.py` `validate_status`; `.tfw/conventions.md` → `Session identity`, `Workflow activation and routing`; HL §§3.4, 3.6.

## Checkpoint

| Found | Remaining |
|---|---|
| C1–C5/C7 survive as contract-compatible source designs; C6 root-live and C9 event-replay are eliminated. C8 survives only on an actual separate owner choice. | TS must choose exact status/event grammar and controlled ancestor-reference validation, then verify all affected readers/copies. |
| Delayed native address is compatible with command-first activation when origin is verifiable; duplicate/conflicting child IDs have distinct outcomes. | Real provider receipt/gate/continuation reliability remains an active-surface check, not a claim made by static research. |
| Pending switches, immediate revocation and same-unit returns can coexist when current selection governs new actions and prior dispatch remains historical launch evidence. | Implementation must demonstrate transition ordering, legacy interpretation and safe-stop reports on actual cases. |

**Sufficiency:**

- [x] External source used: official OWASP Authorization Cheat Sheet opened 2026-09-23 for a bounded deny-by-default/per-action-check analogy, not a replacement for TFW authority.
- [x] Briefing gap closed for Challenge: H5/H6/H7 address race, phase scope, conditional selection, same-unit continuation, revocation, legacy/default and reader/copy failure cases were stressed.
- [x] All 15 dimension pairs screened; material incompatibilities and surviving configurations are listed with their limits.

**Stage decision:** close focused Challenge. Recommend one live-current status plus immutable owner-decision provenance (Extract S1), truthful later child-address binding, a constrained root-to-phase decision reference with phase-local effective state, and separate new-launch versus same-unit-continuation checks. Leave exact syntax/validator migration to TS; do not require another owner mandate for an unchanged scoped choice, remove existing model/effort selection, or describe untested provider mechanics as proven.

## Material handover at this checkpoint

Producer is the Researcher unit above. Inspected source/epoch: approved HL/control at `ff66d7ed5df678061d5689713fcf64c0e84ac744`, Gather `7c5aaf22909462183ceaa80921baf758644ad46e`, Extract `ceb69657cb3b38b5c2a0c130527d5542ade59fac`, selected current status/event/validator/Plan/role readers, and official OWASP guidance opened 2026-09-23. Material: incompatible pairs, surviving/conditional configurations, exact failure sequences and minimum reader coherence requirements. Uncertainty: TS still must settle reference grammar, migration and source checks; platform-native completion remains unproved. Continuation: return this Challenge to the recorded Coordinator and await acceptance before RES synthesis; no HL, TS, code or control file was edited.

---
Stage complete: YES
→ User decision: no owner choice requested at this technical checkpoint; frozen §4.1 authority and owner reservations remain unchanged.
