# ONB — TFW_20260920-223357_FRATS / Phase A: Explicit Coordination, GATEWAY and Session Identity

> **Date**: 2026-09-21
> **Author**: `saubakirov`, via Codex Executor
> **Status**: 🟠 ONB — Accepted; no blocking questions
> **Parent HL**: [Master HL](../HL-TFW_20260920-223357_FRATS.md)
> **Phase HL**: [Phase A derivation](HL__phase-a__explicit_coordination_gateway_and_session_identity.md)
> **TS**: [Approved Phase A TS](TS__phase-a__explicit_coordination_gateway_and_session_identity.md)
> **Actual producer unit**: `codex:thread:local:01a0c3a2-c742-7962-a981-369effb5ac83` (`EXEC · FRATS · A`)
> **Parent Coordinator unit**: `codex:thread:local:01a0bfdb-f0b7-7642-837c-8c47d0a284cf` (`PLAN · FRATS`)
> **Activation source**: owner-direct `/tfw-handoff` request in this Executor unit; no dispatch event and no originating agent proposer
> **Coordinator route authority**: master HL §4.1 and §12 A3 until the Phase A Candidate validates and migrates the phase status

---

## 1. Understanding

Phase A replaces the current mode- and LEAD-centred control model with one provider-neutral
coordination contract. A task-bound unit must resolve five routing facts from its own `status.md`,
start material work only from an exact skill activation with reconstructable provenance, communicate
vertically with its own Coordinator under `tfw-gates-only`, and keep iterative dialogue behind a
separate GATEWAY and exact peer grant. The implementation must preserve legacy readability, role
ownership, independent review, immutable history and exact adapter parity while adding strict current
writes, authority-owned `gate_answer` events, producer provenance and bounded native evidence.

## 2. Entry Points

- Normative model and terminology: `.tfw/conventions.md`, `.tfw/glossary.md`.
- Current carrier contracts: `.tfw/templates/status.md`, `.tfw/templates/journal/event.md`,
  `tools/tfw_state.py`.
- Role-owned forms: `.tfw/templates/research/1_briefing.md`, `.tfw/templates/RES.md`,
  `.tfw/templates/ONB.md`, `.tfw/templates/RF.md`, `.tfw/templates/REVIEW.md`.
- Task activation and return algorithms: the nine canonical workflows in TS §4.
- Provider entry surfaces: the four persistent adapter sources plus installed Codex, Claude and
  Antigravity roots.
- Exact projections: eighteen Claude/Antigravity workflow copies generated from the nine canonical
  workflows; all are byte-identical at onboarding.
- Existing assurance reader: `docs/scripts/command_entry_eval.py`.
- Approval and accounting: TS approval commit
  `ad6042dad73aa04b9bbe9f13880c5a944e7e4f05`; Baseline
  `c80c0dd5e79a6e996fdc68a89ad01b26887c638e`; immutable denominator 47 VALUE files and 3,200
  touched text LOC.

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions.

The mandatory acting-principal gate was resolved before this write: the accountable author for this
owner-direct run is `saubakirov`; `robert` is not the author or authority of this activation. No
scope, acceptance, architecture, authority or denominator decision was changed by that answer.

## 4. Recommendations (suggestions, not blocking)

1. Implement the shared coordination vocabulary and carrier validators first, then change
   role-local workflows and adapter projections. This keeps every downstream reader subordinate to
   one semantic owner and avoids an interval where copies define competing behavior.
2. Add a strict new-write status validator beside the tolerant reader: complete pre-A3 absence stays
   readable, partial five-field sets fail, and every current write requires all five fields. This
   directly implements AC-2 without rewriting historical carriers.
3. Keep the current Phase A status in its legacy form through ONB and implementation. After the first
   tested Candidate proves the new schema, add the five routing fields as authorized TRACE before RF;
   do not fabricate a same-state transition.
4. Treat provider trials as bounded ledgers, not as reliability experiments. Codex can supply native
   title/readback and vertical return evidence in this unit; unavailable Claude or Antigravity
   operations must be recorded as exact limits rather than translated or composed.
5. Generate installed workflow copies mechanically from canonical sources and verify byte identity;
   do not hand-edit the eighteen projections.

## 5. Risks Found (edge cases, potential issues not in TS)

1. The repository contains unrelated untracked paths
   `PROPOSAL__serialized_landing_and_test_boundary.md` and
   `workspace/2026/TFW_20260909-231654_OTR/`. Exact-path staging is mandatory so neither enters a
   FRATS commit.
2. The active phase status intentionally lacks the new routing spine. Until the Candidate validates
   the new contract, master HL §4.1/A3 is the temporary route authority; treating the absence as a
   generic activation failure would make the phase unable to implement its own migration.
3. `gate_answer` combines immutable-event structure, answer ownership and amendment refusal. A
   shape-only validator cannot prove authority from filenames; the template and workflow must require
   status, blocked-artifact and governing-authority refs plus a body that names source, epoch and
   operational effect.
4. Native provider availability may differ on this host. A missing Claude or Antigravity surface is
   an evidence limitation, not permission to emulate it with Codex or a hidden helper.
5. The change spans 47 VALUE paths but one semantic contract. Copy drift or a single surviving current
   mode issuer can invalidate AC-1/AC-7 even when tests pass.

## 6. Inconsistencies with Code (spec vs reality)

1. `conventions.md` and `glossary.md` currently issue `CL`, `AG` and `AT`; TS AC-1 requires them to
   remain historical compatibility only.
2. `conventions.md`, the HL/profile/binding templates and role workflows currently centre authority
   and routing on a selected LEAD/AT mandate; A3 requires task-local routing facts and optional
   attribution that grants nothing.
3. `status.md` and `tools/tfw_state.py` know only lifecycle/owner/authority fields; TS AC-2 requires
   the all-or-none routing spine and strict current writes.
4. The journal contract has no `gate_answer` kind, while ONB currently says the Coordinator or human
   fills the answer directly in the Executor-owned file. This conflicts with Role Lock and TS AC-5.
5. Research, ONB/RF and REVIEW forms do not require the actual producer unit, parent and activation or
   dispatch source demanded by TS AC-6.
6. Canonical workflows still use mandatory Who Is Acting and Agent Team checkpoints, direct-return
   wording and CL/AG branches; TS AC-3/AC-4 require routing-spine consumption, minimal activation and
   explicit refusal before material work.
7. Persistent Codex and Claude instructions still describe AT or execution modes, and the smaller
   provider roots do not state the activation/routing boundary.
8. `docs/scripts/command_entry_eval.py` builds legacy statuses and prompts that do not carry the new
   routing/provenance contract.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|---|---|---|---|
| 1 | K1 — root `README.md` preamble and `How It Works` | ✅ | Applied | Preserve inspectable state, bounded human authority and durable continuation rather than provider memory. |
| 2 | K2 — `.tfw/README.md` NS1 | ✅ | Applied | Reject routing changes that obscure purpose, authority, inspectability or continuation. |
| 3 | K3 — `.tfw/README.md` NS2.2/2.4/2.5/2.7 | ✅ | Applied | Prefer the smallest complete carrier set, selected traces, bounded delegation and proportional evidence. |
| 4 | K4 — `.tfw/README.md` NS3 | ✅ | Applied | No transcript store, authority replacement, artifact factory or provider-bound runtime is introduced. |
| 5 | K5 — methodology values | ✅ | Applied | Structural carrier validation, exact terminology and provider-independent core files guide the design. |
| 6 | K6 — success criteria | ✅ | Applied | Preserve resumability, material decision trace, qualified knowledge boundaries and acceptance-ready results. |
| 7 | K7 — philosophy F3/F4/F32/F37/F38/F40/F43/F45 | ✅ | Applied | Use critical opposition, structural gates, mandate ceilings, finite Coordinator attention, exact terms, architecture over patches and subtraction. |
| 8 | K8 — D23/D28/D31/D59/D73–D75 | ✅ | Applied | Keep selective ordered reads, filesystem state, capability boundaries and source-owned adapter topology while changing coordination semantics. |
| 9 | K9 — D79/D81/D83/D84 | ✅ | Applied with successor boundary | Preserve navigation-only titles, human-rooted authority, unit/principal separation and optional `writer`; A3 supersedes new AT/LEAD issuance. |
| 10 | K10 — D85/D86 | ✅ | Applied | Keep receiver-safe update provenance and finite role-owned closure; update migration must never guess routes. |
| 11 | K11 — HL Contract, Design Rules, Role Lock, anti-patterns | ✅ | Applied | Do not change frozen HL/TS or cross roles; keep workflows algorithmic and adapter-safe. |
| 12 | K12 — convention F1/F5/F19 | ✅ | Applied | Canonical workflows own exact generated copies and naming remains one rule per file type. |
| 13 | K13 — process F3–F5/F27/F30/F35/F37–F40/F43/F45/F47–F49 | ✅ | Applied | Use precise vocabulary, ordered gates, file-first returns, external/native evidence, reproducible counts and conservative autonomy. |
| 14 | K14 — constraint F2/F11/F12/F14 | ✅ | Applied | Minimize reader load, keep provider claims native, store obligations in files and preserve the necessary second coordination act. |
| 15 | K15 — environment F5/F6 | ✅ | Applied | Do not translate Codex behavior into Claude claims; report each installed surface independently. |
| 16 | K16 — stakeholder F6–F8/F10–F11/F14–F18 | ✅ | Applied | Minimize interruptions without weakening authority, keep signals quiet, preserve visible rounds and distinguish task units from stable attribution. |
| 17 | K17 — risk F1 | ✅ | Applied | Use full exact pathspecs and `git commit --only`; preserve sibling dirt and stop on inseparable hunks. |
| 18 | K18 — TKL-20260913-01 | ✅ | Applied | Reuse role/stage handovers and independent records; create no global coordination inventory. |
| 19 | K19 — FRATS iteration-1 RES D1–D10 | ✅ | Applied | Preserve exact measurement epochs, historical readability, conditional identity and the filename/copy reader findings. |
| 20 | K20 — FRATS iteration-2 RES D11–D21 | ✅ | Applied with A3 successor | Use four traffic classes, optional principal value, provider evidence levels and six-edge preservation; A3 replaces the proposed same-writer answer with authority-owned `gate_answer`. |

No additional applicable Project Value or qualified record was found beyond the Coordinator's §7.2
set and its cited incoming relations.

### Material handover at this return

Actual producer: Executor unit `codex:thread:local:01a0c3a2-c742-7962-a981-369effb5ac83`, acting as
`saubakirov` via Codex from an owner-direct activation, returning vertically to Coordinator unit
`codex:thread:local:01a0bfdb-f0b7-7642-837c-8c47d0a284cf`. Inspected context: phase status/journal,
master and phase HL, approved TS at `ad6042dad73aa04b9bbe9f13880c5a944e7e4f05`, both RES iterations,
all twenty HL §7.2 sources, configured scope budgets, governing convention ranges, all canonical
VALUE sources, installed projections and the existing evaluator. Source epoch: repository HEAD
`ad6042dad73aa04b9bbe9f13880c5a944e7e4f05` plus the disclosed unrelated untracked paths. Material
return: no blocker; eight code/spec inconsistencies, five implementation recommendations and five
execution risks. Uncertainty retained: native Claude and Antigravity capabilities on this host and
their attainable P-levels. Continuation: commit this ONB alone, transition the phase to `ONB`, then
execute the approved AC dependency order and return EV/RF to the same Coordinator.

---

*ONB — TFW_20260920-223357_FRATS / Phase A: Explicit Coordination, GATEWAY and Session Identity | 2026-09-21*
