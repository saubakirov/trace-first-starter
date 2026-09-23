---
description: TFW Handoff — executor onboarding, implementation, RF
---

# TFW Handoff — Task Execution by Executor

> 🔒 **ROLE LOCK: EXECUTOR.** Write ONB, implementation, evidence and RF only. Never write or modify
> HL, TS, RES or REVIEW, rule scope, or review your result. A scope defect is recorded in ONB and
> stops execution.

## Read Contract

Root instructions are active. Read this workflow, then inputs in order; shared ranges use unique
headings.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | selected phase/task `status.md` and `journal/` | current state, authority, lineage | task-local |
| 2 | master/phase HL and highest approved TS | frozen purpose and one governing order | governing artifacts |
| 3 | live REVIEW only on REVISE; then TS-referenced artifacts | ruled return and declared inputs | governing artifacts |
| 4 | `.tfw/project_config.yaml` → `tfw.scope_budgets` | VALUE triggers and authority ceiling | config |
| 5 | `.tfw/conventions.md` headings `Task control files`, `Session identity`, `Artifact file naming`, `Task Statuses`, `Safety and Execution Honesty`, `Anti-patterns (prohibited)` | state, identity, lifecycle, evidence, prohibitions | shared rule |
| 6 | HL §7.2 citations and TS-named implementation files | inherited decisions and facts | named source |
| 7 | `.tfw/templates/ONB.md`, `.tfw/templates/evidence/EV.md`, `.tfw/templates/RF.md` | forms, each only at its gate | template |

Never reload root or full common libraries. On REVISE, add only highest TS, live REVIEW and changed
lineage; do not reread unchanged authority in the same session. Missing/duplicate headings stop.

## Identity, activation, and returned work

After state resolves, apply `Session identity` with `WORK=EXEC`. Apply root activation/routing before
analysis. Current work requires a complete matching spine and approved Executor/TS gate. Verify cited
delegation/dispatch; owner-direct work invents no principal. Record provenance in ONB/RF and return
only to `coordinator_route`. Never write or self-answer `gate_answer`.

Resolve current `reporting`/`selection_ref` with the existing five-field compatibility rule.
Only effective owner-transfer changes return transport; manual creation does not. On a
non-revoking switch keep this same Executor, its valid activation and pending gates. A new role's
first message is only the exact command; its address may be learned from receipt or first normal
gate. Current Codex mutation uses a separate worktree; an explicitly selected shared-local provider
route serializes one mutation owner and holds Executor writes during fixed-Candidate review.

For REVISE, accept exactly one ruled case:

- **Rung 1:** lifecycle `RF`; unchanged approved TS plus the Coordinator's closed bound appended to
  live REVIEW. No TS sibling.
- **Any rung 2:** lifecycle `TS_DRAFT`; highest approved `TS…__rev{N}.md` governs the whole round.
- **Rung 3:** only a valid resolved owner verdict under `HL Contract` rule 8 may leave an executable
  bound; otherwise stop.

Read cited findings/rulings. State, recipient and artifacts must match the case. Pending Coordinator
items, rung 2 without revised TS, or unresolved rung 3 stop. Do not redo accepted work or unaffected
evidence. Append numbered round sections to ONB/RF; TS/REVIEW use revision siblings.

At use/return gates apply `Current knowledge use` and `Knowledge handover`: preserve source/epoch,
producer unit, inspected scope, material or justified-none, uncertainty, recipient and continuation.

## Step 1 — ONB

1. Read the governing artifacts and relevant implementation.
2. Analyze blockers, recommendations, risks, spec/code inconsistencies and missing facts. Verify each
   HL §7.2 citation in ONB §7 and add only genuinely relevant missed PV sources.
3. Open the ONB template. Emit `ONB__{ID}.md` or
   `ONB__phase-{x}__{phase_slug}.md`; on return append the numbered touched sections.
4. Commit ONB alone. Before every commit apply `Exact-path staging`: inspect full status and cached
   names, stage explicit full paths, and use `git commit --only -- <paths>`. Never use broad staging
   or commit foreign dirt.
5. A blocker requires an authority-owned `gate_answer`; cite its operational effect. With no blocker,
   valid activation and approved TS suffice—do not invent second permission. Report the state change
   to `coordinator_route`.
6. Set lifecycle `ONB` from `TS_DRAFT`, or from `RF` for rung 1, and append a phase/task-local
   `handoff` event using one clock reading and a drawn four-hex token. No path outside this task/phase
   changes.

## Step 2 — Implement and prove

Before each implementation write, compare the path with the approved VALUE selector and protected
boundaries. Only forecast VALUE logical files/touched text LOC count toward decomposition; TRACE,
ASSURANCE and non-value DERIVED do not. The owner-approved plan is immutable. Stop before an added
VALUE path, protected-boundary change, growth from applicable planned zero, or forecast at/above the
owner multiplier. Below it, only a prospective Coordinator ruling inside unchanged boundaries may
admit a necessary constituent.

7. Implement every authorized local action with production-ready content. For dependent ACs, pass
   the prerequisite first. Stop through `coordinator_route` if required work exceeds authority.
8. Run TS-required targeted/full checks. Reuse evidence only when inputs/output, oracle/authority and
   environment assumptions still apply; rerun changed or uncertain dependencies.
9. Pass the configured build/compile gate. Fix failures before RF.
10. After all VALUE/ASSURANCE work and checks pass, commit the first tested implementation descendant;
    its full SHA is Candidate. Confirm all changed paths are approved VALUE+ASSURANCE or authorized
    task-local TRACE. Later TRACE/ASSURANCE/non-value DERIVED does not move Candidate; later VALUE
    does and requires recomputation. Keep Candidate reachable through review/landing.
    Record requested/effective launch settings, delivery and material rework separately; unobserved
    effective settings stay unknown. Identify exact task-owned temporary resources and their current
    owner/disposition for the Coordinator's later safe close.
11. Open the EV template and emit `evidence/EV__{ID}.md` or
    `evidence/EV__phase-{x}__{phase_slug}.md`; append on return. Use only VERIFIED, DEFERRED, BLOCKED,
    N/A; each VERIFIED row resolves to evidence and every other row explains the gap. Add exactly one
    accounting row: TS approval, full Baseline/Candidate, literal membership/actions/classes/reasons,
    numeric additions/deletions/touched LOC, binary N/A, deviations, trigger disposition,
    immutable-denominator authority/timing and the unchanged NUL-safe command. Missing/mutable/late
    contract facts are BLOCKED; N/A means truly inapplicable. Summarize verdict counts.

## Step 3 — RF and stop

12. Open the RF template and read every heading.
13. Emit `RF__{ID}.md` or `RF__phase-{x}__{phase_slug}.md`; append numbered touched sections on
    return. Fill all mandatory sections, bind Candidate/approval/accounting/authority, point §5 to EV
    with verdict counts, and write explicit empty §7–§9 declarations. Observations include only
    consequential unmodified issues and an allowed type.
14. Set lifecycle `RF` and append a valid `transition` event with one clock reading. Return the exact
    Candidate, evidence and limitations to `coordinator_route`.

**STOP.** Tell the user: “RF is complete. Start `/tfw-review` to review the results.” Never write
REVIEW or continue into another role.
