# Extract — What do we not see?

> **Mindset:** Analyst. Cross the Gather dimensions to expose viable combinations and the smallest source seams.
> **Parent:** [HL-TFW_20260922-192606_PCUX](../../HL-TFW_20260922-192606_PCUX.md)
> **Goal:** Preserve strategic Coordinator planning while enabling command-only launches, live mandates, truthful provider routes, and complete documented closure.
> **Producer / route:** `codex:thread:local:01a0cb19-cbf2-7603-8775-c776f52660d4` → `codex:thread:local:01a0c980-4552-7ed3-b2aa-3c5cc46bc7bc`.
> **Evidence epoch:** HL freeze `5259851e6f07206a07d022db11ef1cbc91dca775`; Gather `168921d6f39a34ef1d3f60f19610a42d232835c2`; official product and Git documentation opened 2026-09-23. The later Claude browser addendum remains unselected.

## Configuration Space

The theoretical D1–D6 cross-product is larger than 30 combinations. The table retains task-relevant configurations with different launch, address, mode and role paths. `Existing trace` means the current RF/REVIEW/close carriers extended only for the approved task-specific obligations. These rows describe possible wiring, not proof of platform reliability or a final choice.

| Config | D1 — authorization at first command | D2 — first reliable child address | D3 — live operating selection | D4 — complete role topology | D5 — shared repository write control | D6 — close evidence and disposal |
|---|---|---|---|---|---|---|
| C1 Codex delegated | Frozen/current owner mandate + exact Coordinator-origin command | Native creation receipt | Status + immutable owner decision; gateway and dialogue separate | Visible Coordinator and role tasks | Separate mutation worktrees | Existing trace + exact dispositions |
| C2 Codex delayed address | Same mandate and command | First routed role gate | Same as C1 | Visible tasks | Separate mutation worktrees | Existing trace + exact dispositions |
| C3 owner-created, native reporting | Owner's exact command at the role gate | First routed role gate | Manual launch, required vertical native reports | Visible tasks/chats | Selected checkout, serialized writes | Existing trace + exact dispositions |
| C4 Claude click at ready gate | Owner clicks a card whose first prompt is only the exact role command | First normal gate supplies address/readiness, or one transport-only roll call if still needed | Manual/click-assisted launch, required vertical native reports | Visible full chats | One selected local workspace, serialized writes | Existing trace + archive dependency disposition |
| C5 Claude compact candidate | Valid delegated mandate + exact role command from Coordinator | Named subagent ID or first routed gate | Delegated launch; dialogue independent | Distinct role subagents | One selected local workspace, serialized writes | Existing trace + exact dispositions |
| C6 Antigravity manual full chats | Owner's exact command at the role gate | First routed role gate | Manual launch, required vertical native reports | Visible full chats | Selected workspace with one mutation owner | Existing trace + exact dispositions |
| C7 Antigravity compact candidate | Valid delegated mandate + exact role command from Coordinator | Named subagent ID or first routed gate | Delegated launch; dialogue independent | Distinct role subagents | Selected workspace with one mutation owner | Existing trace + exact dispositions |
| C8 explicit fully manual transfer | Owner's exact command at the role gate | Owner transfers the exact gate/return | Explicit manual-transfer selection, separately recorded | Visible roles | Selected workspace with one mutation owner | Existing trace + owner-transfer reference |

**Combination absent from the Briefing:** C4 allows the first ordinary role gate to supply readiness after a Claude role-gate click. A separate roll call is needed only if the receipt/gate lacks an address or workspace confirmation. This uses the already approved HL §3.5 condition and does not require a dormant chat or out-of-phase activation.

## Findings

### E1 — Minimal authority and operating-state carriers to test

The current five-field spine establishes route, topology, dialogue and either owner-only or delegated activation. It cannot express the explicit fully manual reporting exception, a conditional future selection, or the immutable owner decision that made a live selection authoritative. The existing `gate_answer` kind requires a blocked artifact and cannot carry an ordinary operating switch; `ownership_changed` changes who owns a unit, while `transition` is a lifecycle edge. A new task/phase-local owner-decision event kind is therefore a bounded schema candidate, with no new registry. Its body would record actual human source, prior/new launch and reporting selection, affected scope/roles, effective checkpoint, reservations, expiry and authority epoch; refs would point to the governing status and HL/TS within the owning task/phase. Sources: `.tfw/templates/status.md`, `.tfw/templates/journal/event.md`, `tools/tfw_state.py` `COORDINATION_KEYS`/`EVENT_KINDS`, `.tfw/conventions.md` → `Task control files`, `Workflow activation and routing`; HL §§3.4, 3.6.

Two schema shapes remain for Challenge:

| Shape | Current status | Additional status values | Decision reference |
|---|---|---|---|
| S1, reuse current activation | `activation` reflects the current owner-only/delegated launch choice; `dialogue` and `owner_gateway` remain independent | `reporting: native\|owner-transfer` and `selection_ref` | New immutable owner-decision journal event; a future conditional event stays pending until the named gate, then status cites it |
| S2, explicit operating mode | Current `activation` keeps its existing delegation-ceiling meaning | `operating_mode: delegated-gates\|manual-gates\|fully-manual` and `selection_ref` | Same journal event and delayed activation rule |

S1 reuses one existing field but changes its accepted authority reference: a later owner grant for otherwise unchanged HL would need `delegated:{exact journal-decision ref}` as well as the frozen HL baseline. S2 retains a ceiling/current-choice distinction in separate fields but duplicates launch meaning. Both require validating the actual human decision and phase scope; neither may treat a mutable status value or a provider setting as authorization. The condition becomes effective at the named gate, not when a future instruction is first recorded. Revocation prevents new launches while an active unit returns to a safe checkpoint with the same identity and pending work.

Command-first provenance needs a separate ordering adjustment. The receiving unit can validate the exact command, task/phase, own unit identity when available, recorded `coordinator_route`, native source/owner action, current status and immutable owner mandate before material work. A parent's later `dispatch` records the actual destination address, source and receipt/gate ref at the time it becomes known; it never fabricates an earlier event time. If the native source cannot be matched to the recorded parent/owner, the delegated claim remains unresolved. This changes the current pre-work rule that requires a prior addressed dispatch, without removing direct addressing for any later send or return. It also preserves the launch-selection quality floor, model/effort comparison and native settings/fallback as launch metadata rather than prose in the first role message. Sources: `.tfw/conventions.md` → `HL Contract` rule 8, `Workflow activation and routing`, `Launch selection`; `.tfw/workflows/plan.md` Steps 1, 5, 7 and dispatch paragraph; HL §§3.3.2, 4.1.

### E2 — Topology and provider combinations

`owner_gateway` can already hold a gateway address while `dialogue` is gates-only. The instruction changes are therefore around title eligibility, Plan Step 5 and role/phase readers, plus the explicit GATEWAY-to-planning-Coordinator and GATEWAY-to-ready-phase-Coordinator route. A planning Coordinator returns the approved phase/dependency map; a separate phase Coordinator receives each phase's worker gates; only that Coordinator reports to GATEWAY. `GATEWAY` is a parent navigation/decision surface and never a role-workflow holder. Bounded peer dialogue remains a separate exact grant. Sources: `.tfw/conventions.md` → `Session identity`, `Workflow activation and routing`; `.tfw/workflows/plan.md` Steps 1 and 5; HL §§3.4–3.5.

The selected Claude Desktop report establishes that an empty pre-created full chat is unavailable through the tested mechanisms. C4 is the bounded role-gate route: show the exact command card, owner clicks local launch, then one ordinary gate or one transport-only readiness exchange binds the address and selected workspace. Creation remains owner-assisted; subsequent native addressed sends are a distinct capability. The parent cannot claim unattended future creation clicks. For one shared workspace, Researcher trace writes, Executor implementation writes, and later docs/knowledge/changelog writes must not overlap with another mutator. The Reviewer consumes a fixed commit while Executor mutation is stopped. This independence is about the Reviewer unit and the fixed reviewed subject, not a separate file copy. Sources: selected owner report observations in HL §2; `.tfw/conventions.md` → `Worktrees for concurrent mutation`; `.tfw/workflows/handoff.md` Steps 1–3; HL §3.5.

Claude Code documentation describes custom subagent skill loading, named ID-based continuation and `SendMessage`, but also notes version-dependent foreground/background tool and permission behavior. Antigravity documentation distinguishes an IDE full Agent conversation from CLI/2.0 subagents with their own IDs, tool/skill lists and workspace options. Thus C5/C7 require a surface-specific check of exact `/tfw-*` invocation, unit identity, direct Coordinator return, same-unit continuation, full tool set, and Reviewer independence before they can be offered as a complete compact cycle. The browser result promised in the later Claude report remains unselected. The valid design boundary is a genuinely small one-phase task with bounded Coordinator context and an explicit visible-role route whenever a required link is absent. [Claude Code — Custom subagents](https://code.claude.com/docs/en/sub-agents), [Antigravity — Custom subagents](https://www.antigravity.google/docs/subagents/); HL §§3.5, 10.

### E3 — Close ordering and source ownership

The existing Executor Candidate and EV/RF, independent Reviewer, docs and human-knowledge workflows, and Coordinator close state/event form a usable chain. The missing task-specific effect is an attributable `.tfw/CHANGELOG.md` entry under `Unreleased`, after an accepted change is known and before final-effect acceptance; the repository's `/tfw-release` route remains a separate trigger for versioning, tagging and publication. The actual changelog source currently has an empty `Unreleased` section, and `.tfw/workflows/release.md` does not authorize a task close to tag or publish. The approved HL §3.7 supplies this task's changelog requirement; TS must give it an owner and review timing. Sources: `.tfw/CHANGELOG.md` opening; `.tfw/workflows/release.md` Steps 1–4; `.tfw/conventions.md` → `Closing and record recovery`; HL §3.7.

A close-compatible ownership chain is: Executor records task-owned work resources and Candidate in ONB/EV/RF; Coordinator records actual child addresses and any owned setup in dispatch, then routes docs/knowledge effects and exact changelog change; the same independent Reviewer checks changed final claims; Coordinator verifies exact result reachability, integration and no live dependency before disposing of its own children and resources; parent archives the completed Coordinator only after durable return. Every resource is removed, intentionally retained with a specific restoration/shared-use reason, or pending with actor/action. Git distinguishes the existence of a commit object from its reachability through a ref; exact SHA verification and retained reachability must both be checked before removing the last worktree/branch that protects a Candidate. [Git — git-rev-parse](https://git-scm.com/docs/git-rev-parse), [Git — git-worktree](https://git-scm.com/docs/git-worktree). Sources: `.tfw/conventions.md` → `Landing a deliverable across sessions`, `Closing and record recovery`; `.tfw/workflows/handoff.md` Step 2; HL §3.7.

## Checkpoint

| Found | Remaining for Challenge |
|---|---|
| Eight connected C1–C8 configurations expose a receipt-less Claude readiness path and manual launch with mandatory native returns. | Exercise address race, owner-switch timing, no-peer/no-GATEWAY worker traffic and provider failure cases. |
| Two small live-state schema shapes and one owner-decision event shape reuse task-local status/journal. | Test whether S1 or S2 preserves existing activation authority without ambiguous or duplicated meaning. |
| Existing Candidate/review/docs/knowledge mechanics can anchor the approved close, with a task changelog effect and exact resource dispositions. | Challenge dirty/shared resources, archive restoration dependency and final claim changes before reporting fully cleaned closure. |

**Sufficiency:**

- [x] External source used: opened current official Claude Code and Git documentation for subagent continuation/tool limits and commit/worktree identity on 2026-09-23.
- [x] Briefing gap closed for Extract: candidate carrier, topology and close configurations are mapped without treating them as proven.
- [x] Configuration Space built from Gather D1–D6, with a combination absent from the Briefing.

**Stage decision:** carry C1–C8 and S1/S2 into Challenge; test against approved HL scenarios and preserve all unproved provider links as conditional.

## Material handover at this checkpoint

Producer is the named Researcher unit above. Inspected scope is Gather's six dimensions, the selected current status/event/workflow/close sources, the task HL, and the opened primary Claude/Git documentation. Material: a task-local owner-decision event plus a small status extension can represent live selection; command-first work requires later truthful address binding; the existing Candidate and final-effect chain can carry most close obligations. Uncertainty: S1 versus S2 still needs adversarial testing, and provider docs do not establish an end-to-end compact route on the owner's Desktop/IDE surfaces. Continuation: Challenge tests the configurations after this stage gate returns through the recorded Coordinator route.

---
Stage complete: YES
→ User decision: no new owner choice at Extract; unresolved technical branches move to Challenge.
