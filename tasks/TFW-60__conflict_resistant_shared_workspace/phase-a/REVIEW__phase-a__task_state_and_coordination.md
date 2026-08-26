# REVIEW — TFW-60 / Phase A: Task State & Coordination

> **Date**: 2026-08-26
> **Author**: Codex
> **Verdict**: ❌ REJECT
> **RF**: [RF Phase A](RF__phase-a__task_state_and_coordination.md)
> **TS**: [TS Phase A](TS__phase-a__task_state_and_coordination.md)
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> This file is a synthesis of stage findings. Stage files contain the raw audit trail.

---

## 1. Map

Phase A replaces the root Task Board as live authority with task-local status, immutable event files, participant profiles, and a derived portfolio index; it also migrates the legacy corpus and publishes the model as TFW `2.0.0`. The direction is aligned with the master contract and North Star. Because the first evidence discrepancy invalidated the planned sample, verification escalated from 31 files to every one of the 103 baseline-to-HEAD changed paths.

The owner directed the reviewer to add `team/codex.md` and register it in `team/README.md` after the new attribution rules left the Codex review without a valid actor. That reviewer-added profile is an explicit role-lock exception and is excluded from judgment of the executor's result.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|------------------|--------|----------|
| 1 | Full changed surface: 73 claimed authored product files, 24 installed adapter paths, 6 RF/evidence traces | ❌ | All 103 changed paths inspected; `review/verify.md` V1–V12 |
| 2 | Build/test/index commands | ✅ command results | `129 passed, 1 skipped`; 130 collected; current dirty-tree index reports up to date |
| 3 | Mutually offline task-ID uniqueness and bounded retry | ❌ | Seconds-only grammar can collide offline; released workflows contain no retry algorithm; F1–F2 |
| 4 | Concurrent event append | ❌ | Equal second + equal kind produces the same filename; E8 used different kinds; F3 |
| 5 | Participant/binding resolution | ❌ | Resolution exists only in a non-shipped harness and conflicts with the live private-preference file; F4–F5 |
| 6 | Status/index/docs consumers | ❌ | Partial state validation; legacy-only docs resolver; year grouping bug; clean clone differs; F6–F8 |
| 7 | Migration and accounting | ❌ | 10 tracked states, broken committed TFW-54 authority, overwritten accounting artifact, hardcoded migration paths/date; F8–F9 |
| 8 | Release consistency | ❌ | Live `{PREFIX}-1`/`initial_seq` residue, template version `0.8.4`, contradictory TS path-depth clause; F10–F11 |
| 9 | Evidence sufficiency | ❌ | 44 items audited: 22 match, 10 partial, 12 contradicted; no attachments missing |
| 10 | Knowledge citations | ❌ partial | 34/34 resolve; 31 applications are relevant, 3 ONB applications are irrelevant |
| 11 | Safety and unrelated work | ❌ | Broad staging swept TFW-54/TFW-55 work; later repair preserved the user's working-tree files; F14 / TD-144 |
| 12 | Derived-index behavior after a normal task transition | ❌ | `RF → REV` changed only task-local state; `gen_index.py --check` and `test_committed_index_is_current` then failed until the shared index would be rewritten; F15 |

Raw verification log: [review/verify.md](review/verify.md).

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ❌ | AC-2/3/4/5/6/7/10 fail; only AC-1/8/9 substantially hold |
| 2 | Purpose Check + design soundness | ❌ | `not fit for purpose`: the mandatory current-index test forces every transition back into one shared aggregate, directly breaching the master contract; collision and consumer designs are also unsound |
| 3 | Tech debt documented | ✅ | RF §6 is concrete; surviving items triaged below without duplicating existing rows |
| 4 | Style & standards | ❌ | Canonical workflows/templates and copies retain mutually inconsistent live instructions |
| 5 | Observations collected | ✅ | Eleven observations plus an explicit staging failure; harmless duplication filtered out |
| 6 | RF completeness (§7–§9 present) | ✅ | Fact Candidates, Strategic Insights, and rendered before/after diagrams are present and substantive |
| 7 | Evidence completeness — does it exist? | ✅ | 44 numbered items and four attachments exist; E16 is honestly deferred |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | 12 claims contradicted and 10 only partially supported |
| 9 | Backward compatibility | ❌ | New IDs/layout fail in `gen_docs`; a clean clone loses one state and one authority; legacy allocation residue remains |
| 10 | Safety | ❌ | Migration depended on unrelated untracked state and broad staging recurred |

Detailed reasoning: [review/judge.md](review/judge.md).

## 4. Verdict

**❌ REJECT**

The product direction is correct, and the passing suite is real. The result is nevertheless not releasable because the failures are structural rather than cosmetic:

1. The approved TS fixes task IDs to second-resolution timestamps while also requiring mutually offline uniqueness. Those clauses cannot both be satisfied; the fixture avoids the required equal-second case.
2. The event filename also collides for equal second + equal kind; the concurrency fixture proves only that different kinds have different names.
3. The release does not integrate identity resolution into durable-write workflows, does not validate the full status contract, and does not migrate the documentation consumer to clock IDs/year nesting.
4. The committed migration is incomplete: 10 states ship instead of 11, TFW-54's authority depends on an untracked file, and the required 61/53 accounting artifact was overwritten.
5. The `2.0.0` surface still teaches removed `{PREFIX}-1`/`initial_seq` behavior and ships a `0.8.4` project-config template.
6. The evidence layer exists but overstates what it establishes: 22/44 items match, while 10 are partial and 12 are contradicted.
7. A normal task-local transition makes the required current-index test fail until `workspace/00-INDEX.md` is rewritten. This directly contradicts master HL §3.1 (“without being edited by every workflow transition”) and §3.2 (“Different tasks synchronize without a common edit”): the original shared-write bottleneck returns as a generated file.

This is a fundamental specification-and-implementation failure and includes the named finding **`not fit for purpose`**, so it routes to the owner; a corrective executor pass under the current TS is insufficient. Under `conventions.md` §5, a review `REJECT` is not the terminal task status `REJECTED`; the owner must choose whether to return the task to `HL_DRAFT`, `RES`, or `TS_DRAFT`. The narrowest viable route is **`TS_DRAFT`**: preserve the master purpose, rewrite the contradictory collision/path/index clauses, then execute and review Phase A again.

### Fundamental issues requiring TS/implementation rework

1. Replace the seconds-only uniqueness design with an offline collision-resistant identifier grammar or explicitly narrow the guarantee; add an equal-second/mutually-offline gate.
2. Make event filenames unique for same-second, same-kind concurrent writers without a shared counter; add an atomic no-clobber gate.
3. Define and integrate participant resolution before every durable workflow write, including a valid path for a new agent profile and the relationship to `.user_preferences.md`.
4. Make one shared consumer resolver support both grammars, every configured container, year nesting, phase paths, and docs index grouping.
5. Enforce every required/conditional status key, declared lifecycle, terminal outcome, dates/types, and directory-ID agreement; malformed state must remain visible and non-actionable.
6. Re-run migration from a clean tracked input: ship all intended states, point authority only at committed artifacts, preserve the pre-removal accounting, and remove repository/date/container hardcodes from the reusable script.
7. Reconcile AC-1 year nesting with AC-7's equal-depth clause.
8. Sweep every canonical workflow/template/adapter original and propagated copy, set the template version to `2.0.0`, and rebuild evidence from reproducible current commands.
9. Remove the always-current shared-index build requirement from normal task transitions; validate staleness visibility without forcing unrelated tasks to rewrite the aggregate, and rebuild it only at the declared consolidation boundary.

## 5. Tech Debt Collected

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| 1 | RF §6 obs. 1–3 | Med | `KNOWLEDGE.md`, `knowledge/convention.md` | D66/D65/F22 still describe the retired root board or old carrier count | Added as TD-181; do not run `/tfw-docs` on a rejected result |
| 2 | RF §6 obs. 4 | Med | `TECH_DEBT.md` TD-81, TD-177 | Executor claims their mechanism is retired, but the phase is rejected | Existing rows remain open; no duplicate and no closure |
| 3 | RF §6 obs. 5 | High | `editions/02-assisted/AGENTS.md` | A shipped edition changes state by moving task folders, contradicting stable-path P4/DoF 3 | Added as TD-182 |
| 4 | RF §6 obs. 6 | High | `tasks/TFW-36__content_marketing_blog_series/.gitignore` | `*` hides the entire task and makes the generated index non-reproducible from a clone | Added as TD-183 |
| 5 | RF §6 obs. 7 | ⚪ N/A | `README.md` | North Star wording changed mechanism, not purpose | Reviewer ruled aligned; no debt |
| 6 | RF §6 obs. 8, 9, 11 | Med | migrated `status.md` files | UNDECLARED lifecycle values and unrecorded owners/values need deliberate owner classification | Added as TD-184 |
| 7 | RF §6 obs. 10 | ⚪ filtered | `docs/scripts/gen_docs.py` | Duplicate config read is harmless at current scale | Rejected as filler |
| 8 | RF process failure | High | shared Git index / staging procedure | Broad staging captured unrelated task work again | Existing TD-144 already describes and prioritizes this exact defect |

## 6. Traces Updated

- [x] Review stage files and this REVIEW created.
- [x] Owner-directed reviewer identity created as `team/codex.md` and registered in `team/README.md`; recorded as an explicit role-lock exception, not executor output.
- [x] Task state routed to `REV` with a Codex-authored transition event; it remains there pending the owner's required REJECT route choice.
- [x] Derived index deliberately not rewritten by the reviewer. Its resulting staleness and failing current-index test are purpose finding F15, not a missing trace update.
- [x] HL status — N/A; reviewer role lock forbids changing it and REJECT requires the owner/coordinator to choose the re-entry state.
- [x] `project_config.yaml` allocation state — checked; `initial_seq` is removed from live config but remains stale in release instructions.
- [x] Other project files — 100% changed-surface audit completed; stale information is listed in §4.
- [x] tfw-docs: **N/A — verdict is REJECT; rejected work is not consolidated.**
- [x] tfw-knowledge: **N/A — verdict is REJECT; Fact Candidates remain unpromoted.**

## 7. Fact Candidates

No new Fact Candidates. The review produced implementation findings reproducible from files and commands, not human-only project facts. The owner's instruction to add the Codex participant profile is recorded in §1/§6 as a direct decision and does not need knowledge promotion.

---

*REVIEW — TFW-60 / Phase A: Task State & Coordination | 2026-08-26*
