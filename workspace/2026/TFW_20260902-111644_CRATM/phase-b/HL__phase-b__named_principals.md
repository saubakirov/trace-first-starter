# HL — Phase B: Named principals

> **Date**: 2026-09-05
> **Author**: Phase Coordinator (Codex)
> **Task**: [TFW_20260902-111644_CRATM](../HL-TFW_20260902-111644_CRATM.md) — Contextual Roles and Agent Team Mode
> **Phase**: B of five · 🔴 · **Requires:** Phase A ✅
> **Status**: 🟡 TS_DRAFT — planning complete; approval and execution blocked on the external validation retirement
> **Master contract**: 🔒 FROZEN — approved by saubakirov 2026-09-02

> **This file is derivation-only** (`conventions.md` §3 rules 20–21). It carries no §1, §5, §6,
> §7, or §12. Vision, acceptance, failure, principles, and amendments live only in the master HL.

---

## What this phase discharges, from the master

| Master item | Phase B's share |
|---|---|
| §3 items 3–7 | Profile context, accountable agent principals, writer identity, principal bindings, and grant/mentality separation |
| DoD 4 | Four-key profiles remain valid while organization/project roles become expressible |
| DoD 5–9 | `type: agent` becomes usable; principals name humans; events/bindings name principals; two stable names carry two grant levels |
| DoD 14, 16 | Permissions stay role-owned; the phase adds provider-neutral Markdown only |

Phase C owns who receives or rules a proposal. Phase D owns Role Assignment and team mode. This
phase supplies only the stable names and fields those later rules can consume.

## 2. Current State (As-Is) 🟢 FREE

The four-key profile admits `type: agent` but makes agents usable by nothing. Roles live in prose; the
binding selects only a human. Events name accountability (`on_behalf_of`) and tool (`via`), not the
writer; legacy `actor` remains tolerated. Research established that optional profile fields are
compatible, task scope is not a third role dimension, tool text drifts, and the filename token already
owns uniqueness. Phase A is `DONE`; D77 is the incoming canon.

At planning base `eef020bb5c00901c09f5def262b930e70975ae12`, the active validator rejects `writer`.
The frozen master excludes that script. Approval, Baseline selection, denominator freeze, and
`/tfw-handoff` therefore wait for its external retirement and a succeeding reader that accepts the
carrier.

## 3. Target State (To-Be) — derived from master §3 items 3–7

1. Optional `organization_role` and `project_role` are descriptive. Omitted means unknown;
   `not_applicable` means known not to apply.
2. An agent principal has `accountable_to: <human>` and Boolean `may_rule_amendments`. Provider,
   model, process, and session are not identity.
3. Optional `mentality` guides style only; it cannot alter grants, Role Locks, or permissions.
4. A grant change creates a new handle/profile; one stable principal exists per grant level.
5. Current `writer` names a principal; `on_behalf_of`, `via`, and token retain their separate jobs.
   Legacy `actor` remains history, untouched.
6. A per-machine binding selects a human or agent principal for attribution and grants nothing.

### 3.1 Result Visualization

```yaml
# existing human — the original four keys remain sufficient
handle: saubakirov
name: Sanzhar Aubakirov
type: human
since: 2025-09-08

# agent principal that may rule / one that may not
handle: method-ruler                 # second: method-worker
name: Method Ruler
type: agent
since: 2026-09-05
organization_role: not_applicable
project_role: phase coordinator
accountable_to: saubakirov
may_rule_amendments: true            # second: false
mentality: critical opponent         # optional, never authority
```

```yaml
# a new event after the external dependency lands
writer: method-ruler
on_behalf_of: saubakirov
via: tool-name

# per-machine selection; the project tree stores no local choice
bindings:
  C:\abs\path\to\project: method-ruler
```

The reader sees principal, accountable human, and fixed grant. Legacy `actor` stays unchanged.

### 3.2 Value Flow

`profile context → accountable principal → machine binding → event writer → durable attributable act`.
Mentality informs style beside this path; it never enters the authority path.

## 4. Deliverables, in order

1. Extend the profile template with roles, accountability, grant, mentality, examples, and the
   two-grant-levels rule.
2. Add one canonical principal/profile contract to `conventions.md` §4; preserve Phase A.
3. Add current `writer` to the event template while preserving legacy `actor` and the other fields.
4. Let the binding template select a human or agent principal without gaining another job.
5. Prove post-retirement compatibility with unchanged four-key profiles and legacy events.

## What this phase must NOT do

No retiring validator/tests, adapters, workflows, glossary/changelog, routing, Role Assignment, team
mode, registry/liveness, or profile per session. Phase C–E and the retirement remain separate.

## 7.2 Knowledge Citations 🟢 FREE

| # | Source | Item | How it applies here |
|---|---|---|---|
| B1 | PV 0 — [NS2 principle 5](../../../../.tfw/README.md#ns2) | Human authority, bounded delegation | Agent principals require an accountable human and an explicit two-level grant before use |
| B2 | PV 1 — [Methodology values](../../../../.tfw/README.md#methodology-values) | Naming Creates Behavior; Portability | Stable provider-neutral handles carry the grant; no model/session becomes identity |
| B3 | PV 2 — [`philosophy.md` F37](../../../../knowledge/philosophy.md) | A mandate is a ceiling | `mentality` and profile roles cannot create permission |
| B4 | PV 3 — [`KNOWLEDGE.md` D59, D68, D76, D77](../../../../KNOWLEDGE.md) | Attribution ≠ authentication; opaque token; VALUE contract; Phase A result | Fields stay orthogonal, Baseline waits, and Phase A is preserved |
| B5 | PV 4 — [`conventions.md`](../../../../.tfw/conventions.md) `Task control files` and `Which handle a machine acts as` | Current identity and binding authority | The phase extends these exact owners once |
| B6 | PV 5 — [`convention.md` F19](../../../../knowledge/convention.md) | Naming consistency is design | New schema keys use one lower-snake-case vocabulary |
| B7 | PV 6 — [`process.md` F30, F38, F39](../../../../knowledge/process.md) | Reader, pre-act enforcement, search-derived delivery set | The succeeding reader is a pre-execution dependency |
| B8 | PV 7 — [`constraint.md` F12](../../../../knowledge/constraint.md) | Role obligations live in files | Principal and grant semantics live in canonical files, never tool memory |
| B9 | Task evidence — [FA15ES HL §11 S6](../../TFW_20260830-202031_FA15ES/HL-TFW_20260830-202031_FA15ES.md#11-strategic-insights-planning) | Organization/project roles are descriptive, not permissions | Supplies field evidence without merging Full and Assisted schemas |

## 8. Dependencies 🟢 FREE

| Dependency | Status |
|---|---|
| Master contract and research 1–3 | ✅ frozen; sufficient |
| Phase A RF/final REVIEW | ✅ `DONE`; D77 is the delivered result |
| External retirement of the validator that rejects `writer` | ⬜ **approval/execution blocker**; CRATM does not modify or inspect it |
| Immutable execution Baseline and VALUE denominator | ⬜ recompute only after the blocker lands |
| Phases C–E | ⬜ downstream; untouched here |

## 9. Risks — phase-local 🟢 FREE

| Risk | Mitigation |
|---|---|
| A live reader rejects `writer` | Block approval/execution until the succeeding path proves acceptance |
| A grant changes under an old signature | Grant change creates a new handle/profile |
| Mentality/roles become permission | Separate keys and negative AC checks |
| A session/provider is mistaken for a principal | Require stable handle plus accountable human; forbid provider/model/session identity |
| Scope leaks into routing or Role Assignment | Exact four-file VALUE selector; Phase C/D terms are exclusions |

## 10. RESEARCH Case

**Phase-local N/A.** Research is sufficient; the remaining item is a binary execution dependency.

## 11. Strategic Insights

No phase-local addition. The governing owner decisions are master S11–S12 and FA15ES S6.

---

*HL — Phase B: Named principals | TFW_20260902-111644_CRATM | 2026-09-05*
