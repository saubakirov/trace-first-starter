---
description: TFW Handoff — executor onboarding, implementation, RF
---

# TFW Handoff — Task Execution by New Agent

> **Roles:** Coordinator (hands off) → Executor (receives, questions, implements)
> **Input:** Approved HL + TS files
> **Output:** RF file with implementation results

> **🔒 ROLE LOCK: EXECUTOR**
> Permitted writes: ONB, approved implementation outputs, the existing EV evidence
> artifact, RF, and the task's Task Board trace—only inside approved TS scope.
> Forbidden actions: writing or modifying HL, TS, RES, or REVIEW; changing scope;
> editing an unapproved consumer; or starting independent review.
> If an acceptance-critical mismatch, scope change, destructive/irreversible authority
> gap, or protected-boundary conflict is found: record it in ONB or RF as appropriate,
> return to the Coordinator/user, and **STOP**. Do not silently reinterpret approval.

## Step 0: Name This Session

**Name this session:** `Executor | {TASK-ID} | Phase {X}`
Set this as the session/conversation name before doing anything else.

## Context Loading (Executor)

When starting as executor, load in order:
1. `AGENTS.md` — agent instructions
2. `.tfw/conventions.md` — project conventions
3. `.tfw/glossary.md` — terminology
4. `KNOWLEDGE.md` — architecture, decisions, legacy (if exists)
5. **Master HL** for the task — understand vision, design philosophy, architecture decisions
6. **Phase HL** (if multi-phase) — phase-specific scope and context
7. **TS file** for the task — exact scope, DoD, constraints
8. Approved predecessor facts, cited knowledge, and related HL/TS/RES/RF/REVIEW
   artifacts referenced by the task
9. Every affected implementation/source/output file listed in TS

## Phase 1: Executor Onboarding

1. **Read all context** — complete the ordered load above before proposing action.
2. **Open the canonical ONB template** — use
   [`.tfw/templates/ONB.md`](../templates/ONB.md) as the output owner. Do not recreate
   its section/form contract in this workflow.
3. **Challenge the specification against reality** — inspect the actual project and
   cited sources for:
   - acceptance-critical identifiers, paths, APIs, and public contracts;
   - cited authority availability, freshness, and the required comparison relation;
   - required checks and the claim/failure each protects;
   - Local/Seam/Live proof feasibility and the earliest honest observation event;
   - product cohesion, hidden seams, unrelated work, and actual scope measurements;
   - requirement-versus-adaptable-guidance ambiguity.
4. **Write ONB completely** — fill Understanding, Entry Points and its reality check,
   Questions, Recommendations, Risks, Inconsistencies, and Knowledge Citations. Confirm
   each HL §7.2 citation and add newly relevant Project Value items. A non-triggered
   check may be `N/A` with reason; omission is not a result.
5. **Apply the mismatch gate**:
   - acceptance-critical mismatch, changed approved scope, unavailable required source,
     missing required proof route, or fragmented product outcome → blocking Question
     and **STOP**;
   - adaptable-guidance substitution → MAY recommend it, but later RF must disclose
     source, rationale, claim/proof effect, and authority.
6. **Create the routed repository-local ONB commit** — update the Task Board to
   `🟠 ONB`, verify the recognized runtime, then use the adapter-declared surface plus
   the current task/work and `executor` Role Lock through the router/carrier:

   ```text
   python .tfw/scripts/commit_identity_hooks.py verify --repo .
   python .tfw/scripts/commit_identity_hooks.py commit --workflow handoff --surface {adapter-surface} --task {TASK-ID} --work {master|phase-*} --role executor --operation ordinary --summary "{concise ONB result}" --repo .
   python .tfw/scripts/commit_identity.py audit-range --repo .
   ```

   The carrier consumes the Phase B router plan, supplies complete expected context
   only to the local Git child, and returns the new object ID. Record the post-commit
   state-owned exact-range result and `actor_authentication:false` in the Coordinator
   handoff. Do not infer identity from branch, prior subject, staged prose, model, or
   session. Missing runtime, invalid range, local dirt, or an unpublished current
   commit blocks the authority transition. File or commit presence proves trace
   presence only.
7. **Apply the separate publication gate** — a local commit, task/phase completion,
   approval, RF, or REVIEW does not authorize push. Push only after separate explicit
   human publication authority. For TFW-49, process F26 keeps publication unavailable
   until every phase closes and the user later says `APPROVE PUSH`.
8. **Mandatory approval gate** — do NOT implement until the Coordinator/user explicitly
   replies `APPROVE`. `REVISE` returns to ONB. Unanswered blocking questions prohibit
   approval.

   > **Coordinator ONB answer protocol:** If an answer is not explicit in approved
   > authority, present 2–3 options with tradeoffs; do not decide for the stakeholder.

## Phase 2: Execution

9. **Update the Task Board** — after explicit approval, change status to `🟢 RF`
   (execution in progress).
10. **Execute by Requirement Claim**:
   - Preserve every approved obligation and acceptance-critical boundary.
   - Produce complete, usable output with no placeholders for code, documents, research
     outputs, designs, operational actions, and decisions alike.
   - Use CL/AG authority exactly as configured; do not infer permission for external,
     destructive, irreversible, or scope-changing action.
   - Apply `[depends: AC-X]` as an execution loop: verify each prerequisite AC Gate
     before beginning a dependent AC. Independent ACs may proceed in any safe order.
11. **Run every applicable Gate and proof obligation**:
    - Use the TS Gate to choose applicable source, structure, lint, test, build, render,
      interface, stakeholder, operational, or live checks.
    - A code test/build is not universal. Mark a check `N/A` only when its claim is not
      triggered and record the reason.
    - A failing applicable gate must be fixed, or the affected outcome must remain an
      explicit blocked/non-claim before RF. Passing local output does not close a
      crossed or live boundary.
12. **Record Material Deviations** — before acting on a deviation, classify it:
    - acceptance-critical precision or scope mismatch → return to authority and
      **STOP**;
    - adaptable Technical Guidance substitution → record source
      requirement/guidance, actual choice, rationale, affected claim/proof, and
      authority for RF. Silent changes are prohibited.
13. **Collect claim-triggered proof and Evidence**:
    1. Open [`.tfw/templates/evidence/EV.md`](../templates/evidence/EV.md) and use its
       existing task/phase EV path; create the `evidence/` folder only when absent.
    2. Fill the actual Environment and create stable `PR-*` records for every claimed
       deliverable. Each record resolves claim, boundary/proof class, method or
       observation, result, artifact/provenance, material actor/time, and debt.
    3. Local Proof is mandatory. Add Seam Proof for each crossed source/interface/role/
       package/phase boundary and Live Proof for each stakeholder/environment/
       irreversible outcome.
    4. Keep the existing per-AC Evidence rows and the four statuses
       `VERIFIED / DEFERRED / BLOCKED / N/A`. Status scopes only the observation row.
    5. Unavailable triggered Seam/Live Proof requires complete Value Debt: affected
       claim, owner, due event, evidence route, impact, and explicit non-claim.
       `BLOCKED` cannot close; unjustified `N/A` cannot waive proof.
    6. Shared observations and grouped records are valid when every claim and boundary
       remains resolvable. Do not force one row/file per mechanism.
    7. Record the Evidence verdict counts and index only material binary attachments.
       Proactively use claim-applicable tools; do not fabricate unavailable observation.

## Phase 3: Write RF

14. **Pre-RF Gate** — open the current
    [RF template](../templates/RF.md) and
    [EV template](../templates/evidence/EV.md). Read every heading and field before
    writing RF. Verify the EV contains every triggered proof/debt relation and the
    Evidence verdict; do not reconstruct Evidence after attestation.
15. **Create RF from its canonical template**:
    - attest only to supported claims and cite their `PR-*` records;
    - disclose limitations, blocked conditions, Value Debt, and every Material
      Deviation with authority and claim/proof effect;
    - report reproducible applicable verification methods and actual results;
    - keep RF §5 a concise EV pointer plus Evidence verdict, not a duplicated proof
      table;
    - include every mandatory §1–§9 section. In §6 report only out-of-scope issues that
      would bite the next developer. Before §7–§8, review human-sourced conversation
      history; use explicit `No ...` dispositions when no content qualifies.
16. **Completeness gate** — resolve every TS AC, every claimed deliverable, every
   applicable Gate, every `PR-*` reference, every limitation/deviation, and the exact
   write set. File/checkmark presence is trace presence only. The RF is Executor
   Attestation; independent REVIEW retains acceptance/rejection authority.
17. **Create the routed repository-local completion commit** — verify runtime, then
    run the same handoff carrier with the adapter-declared surface, current task/work,
    `executor`, `ordinary`, a concise result summary, and `--repo .`. The carrier
    obtains and validates the Phase B router plan before invoking Git. Use it for the
    exact implementation/EV/RF/Task Board write set. Re-run lifecycle verify and the
    state-owned exact range after the commit; RF contains the reproducible pre-commit
    result and the post-commit result is reported to the Coordinator because a commit
    cannot contain its own object ID. Re-run protected-state checks and keep
    publication behind the separate gate in Step 7.

## 🛑 Executor STOP

> **Your work is done.** Do NOT proceed to review.
> Inform the user: "RF is complete. Start `/tfw-review` to review the results."
> Writing a REVIEW file as executor is a **🔒 Role Lock violation**.

## Multi-Phase Task Flow

For large tasks broken into phases:

```
Coordinator: Master HL (approved)
    │
    ├── Phase A: Coordinator writes TS__phase-a
    │   └── Executor Agent: reads → ONB → executes → RF__phase-a
    │   └── After RF, run /tfw-review for review
    │
    ├── Phase B: Coordinator writes TS__phase-b
    │   └── Executor Agent: reads → ONB → executes → RF__phase-b
    │   └── After RF, run /tfw-review for review
    │
    └── ... repeat per Phase
```

Each Phase Agent starts with full context loading.
Coordinator maintains the Master HL for continuity.

## Anti-patterns

> Full generic list → conventions.md §14. Role-specific items below:

- Executor continues past Phase 3 — must STOP after RF
- Executor writes REVIEW file — **🔒 Role Lock violation**
- **🔒 Executor MUST NOT write HL, TS, REVIEW, or change scope** — Role Lock violation
