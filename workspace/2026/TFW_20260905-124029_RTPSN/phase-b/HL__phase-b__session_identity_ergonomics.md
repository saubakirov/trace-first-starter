# Phase HL — TFW_20260905-124029_RTPSN / Phase B: Session Identity Ergonomics

> **Date**: 2026-09-05
> **Author**: Codex (Coordinator)
> **Status**: 🧩 DERIVED — Phase TS awaiting approval
> **Master HL**: [Role, Task, and Phase Session Naming](../HL-TFW_20260905-124029_RTPSN.md)
> **Master Contract**: 🔒 FROZEN — owner verdicts applied at `7bc0f30`; this file adds execution context only
> **Research Basis**: [Iteration 1 RES](../research/iter1/RES.md) · [Iteration 2 RES](../research/iter2/RES.md)
> **Dependency Result**: [Phase A RF](../phase-a/RF__phase-a__command_entry_reliability.md) · [Phase A REVIEW](../phase-a/REVIEW__phase-a__command_entry_reliability.md)

---

## Parent Derivation

This phase implements only master HL §4 Phase B and inherits master DoD B1–B8, DoF 6–12, and §7/§7.1 without changing them. Its required result is one provider-neutral session identity contract applied at satisfiable checkpoints across every task-bound workflow, after authoritative task/phase resolution and before the first role-specific proposal, durable write, wait, or stop.

Vision, acceptance, failure conditions, and principles remain solely in the frozen master HL. The approved A1 stable-key suffix is included. The rejected A2 ASCII-separator fallback remains rejected. This phase creates no role, hierarchy, session owner, delegation channel, worktree rule, or command-entry architecture.

## Finished Phase View

```text
authoritative task/phase state
            |
            v
  one Session identity contract
            |
            +--> WORK: PLAN | RESEARCH | EXEC | REVIEW | RESUME | DOCS | INIT
            |             \--> LEAD only from an existing authoritative binding
            +--> TASK: unique approved abbreviation
            |             \--> full canonical ID / legacy TFW-## when needed
            +--> PHASE: bare canonical token only when known and unambiguous
            |
            v
      WORK · TASK [· PHASE]
            |
            +--> exact BASE collision + stable key --> · @shortest-unique-prefix
            +--> no capability/readback/key ---------> report once; continue
            +--> middle dot not preserved -----------> report once; no pipe fallback
```

The owner sees compact, consistent titles such as `PLAN · RTPSN · B`, `EXEC · RTPSN · B`, and `REVIEW · RTPSN · B`. The title is navigation metadata: it neither proves command/workflow compliance nor grants Role Lock or hierarchy authority.

## Starting Point

- Phase A is `DONE` and approved. Its 7/54 live prefix did not establish comparative entry-architecture superiority; AC-3 ended `BLOCKED` under the immutable ceiling and production retained the current thin proxy.
- No production skill, canonical workflow, manifest route, or Phase-B surface was changed by Phase A. A production skill/proxy change still requires a new approved TS and is outside this phase.
- Iteration 2 selected exactly `{WORK} · {TASK}[ · {PHASE}]`, the eight-token work vocabulary, unique approved abbreviation/full-ID fallback, bare canonical phase, and fail-soft host behavior.
- Master amendment A1 permits ` · @<short-stable-key>` only after a real BASE collision and verified host-key capability. A2 rejected every ASCII separator fallback; U+00B7 remains canonical.
- Current workflow coverage is incomplete and inconsistent: new-task Plan names only after creation; existing Plan, Research, Resume, Docs, and Init lack the selected semantics; Handoff and Review name too early from request wording and use the old role/pipe/full-ID form.
- `.tfw/glossary.md` still describes the old Handoff/Review/Plan arrangement. It must become a router, not a competing algorithm.
- The manifest still owns the 11-command/four-adapter copy topology. Seven routes are task-bound in at least one mode; Knowledge, Release, Update, and Config are project-wide and must not invent a task title.
- Baseline `83b31ff8d6cdb879fdf4f20578fa688b48863f8a` fixes the complete charged fixed-context graph, not only local file sizes:

| Affected route/profile | Baseline charged words; Candidate ceiling |
|---|---:|
| `/tfw-plan` | 24,725 (and the existing D75 constant remains 24,730) |
| `/tfw-research:focused` | 6,102 |
| `/tfw-research:deep` | 6,167 |
| `/tfw-handoff` and `/tfw-handoff:revise` | 6,366 each |
| `/tfw-review` | 24,954 |
| `/tfw-resume` | 3,264 |
| `/tfw-docs` | 15,278 |
| `/tfw-init` | 4,529 |
| Active charged `.tfw` runtime corpus | 33,749 |

## Decision Boundary

The existing `.tfw/conventions.md` receives one uniquely addressable `Session identity` section. It is the only semantic and fallback authority. The existing glossary entry points to that section without restating its grammar. Each affected canonical workflow owns only its local activation checkpoint and consumes the central contract after its existing Read Contract has resolved authoritative state.

This placement avoids a new always-read file or registry. Every affected workflow already reads `conventions.md`; Docs adds only the addressed identity range in its single-task modes. Canonical workflow copies remain copies enforced by the existing manifest/parity tests, not independent authorities.

Adding an addressed range is not permission to increase startup context. Every affected Candidate route/profile must remain at or below its own `83b31ff` charged-word total, and the active charged `.tfw` runtime corpus must remain at or below 33,749 words. The local 260-word central-range and 45-net-word checkpoint maxima are secondary caps only. Semantically equivalent compression may occur only inside the same seven canonical workflow paths, with their algorithms, ordered reads, gates, stops, and source-derived mutant coverage preserved. Existing D75/VBSA regressions and constants are protected, not recalibrated to the Candidate.

`LEAD` is not a synonym for Coordinator. It replaces `PLAN` or `RESUME` only when a governing task/delegation artifact already binds the current session as lead/main coordination. Otherwise the ordinary workflow cue remains. RTPSN does not define what lead coordination means.

## Canonical Contract Shape

```text
BASE := WORK " · " TASK [ " · " PHASE ]

WORK  := PLAN | RESEARCH | EXEC | REVIEW | RESUME | DOCS | INIT | LEAD
TASK  := unique-approved-abbreviation | full-canonical-task-id | legacy-TFW-##
PHASE := uppercase token obtained from the authoritative `phase-{token}` identity
```

- Current-grammar tasks use the approved abbreviation encoded in their canonical ID only when it is unique across configured accessible task roots. A collision, a historical grammar without an approved abbreviation, or an unprovable uniqueness check uses the full canonical ID.
- A phase segment is rendered only from selected phase state or another governing artifact in the loaded lineage. Research iteration numbers are not phases. Absent, conflicting, or multiple possible phases omit the whole segment.
- After an exact BASE collision survives every available authoritative phase/`LEAD` distinction, an exposed stable host key may contribute ` · @<prefix>`. The prefix starts at the first code point and expands until it is unique among the known colliding BASE sessions. If uniqueness or readback cannot be verified, no suffix is claimed.
- Rename failure, unavailable rename/readback, unresolved exact collision, or middle-dot corruption produces one explicit message in the current session containing the intended canonical title and reason; substantive work continues. No pipe, hyphen, emoji, guessed phase, invented ordinal, or silent success is allowed.

## Workflow Checkpoints

| Route / mode | Work cue | Identity checkpoint |
|---|---|---|
| `/tfw-plan`, existing | `PLAN`, or `LEAD` with authoritative binding | after selected task/phase state and lineage resolve; before Knowledge Gate or planning proposal |
| `/tfw-plan`, new | `PLAN`, or `LEAD` with authoritative binding | immediately after the approved canonical task ID is created; before status/event/HL writes |
| `/tfw-research` | `RESEARCH` | after task and iteration resolution; before research-folder/stage writes or waits; iteration never supplies phase |
| `/tfw-handoff` | `EXEC` | after Read Contract item 1 resolves task/phase; before ONB analysis/write/wait |
| `/tfw-review` | `REVIEW` | after Read Contract item 1 resolves task/phase; before Map/write/wait |
| `/tfw-resume` | `RESUME`, or `LEAD` with authoritative binding | after one task is selected; add phase only when the state/lineage selects exactly one |
| `/tfw-docs` auto/manual | `DOCS` | after Select/Triage resolves one task/phase; before proposing or applying documentation writes |
| `/tfw-docs --scan` | none | batch mode resolves multiple tasks; skip task-oriented rename |
| `/tfw-init` full init | `INIT` | after the approved first-task ID is created; before its status/event writes |
| `/tfw-init` attach/repair | none | no init task is created; skip task-oriented rename |
| `/tfw-knowledge`, `/tfw-release`, `/tfw-update`, `/tfw-config` | none | project-wide; no single authoritative task |

## Execution Boundary

### Included

- Consolidate the exact grammar, source precedence, A1 collision suffix, A2 rejection, readback, report-once, and navigation-only semantics in one existing conventions authority.
- Replace the stale glossary statement with a pure router to that authority.
- Place one local checkpoint in the seven task-bound/conditionally task-bound canonical workflows and synchronize their tracked Claude and singular Antigravity compatibility copies exactly.
- Pay for the added addressed range/checkpoint within each affected route by semantically equivalent compression inside those same seven workflow paths; no route or active runtime-corpus growth is accepted.
- Derive the 7/4 workflow classification from the manifest and verify new/existing Plan, Research, Handoff, Review, Resume, Docs modes, Init modes, lead/unbound behavior, task/phase ambiguity, stable-key collisions, capability failure, and middle-dot preservation.
- Measure before/after canonical workflow, addressed-section, complete charged route graph, active runtime corpus, and copied-receiver word effects without using words or bytes as a substitute for human/behavioral evidence.
- Capture supported-host readback evidence for one newly created Codex task/session and one existing/resumed task/session, including exact title length, retrieval/search, and visible truncation limits.

### Excluded

- Any production change to the 22 Codex skill source/install paths, thin-proxy wording, root managed blocks, adapter manifest, or canonical command-entry sequence.
- ASCII separator fallback, emoji, invented collision ordinals, guessed task/phase/hierarchy, or a capability registry/wrapper/daemon/hook.
- A claim that static tests prove model compliance, human recognition speed/error, pixel behavior on an unobserved host, or cross-provider rename support.
- Any weakening, rebasing, renaming, or ceiling increase in the existing D75/VBSA context regressions, including `test_phase_c_every_changed_path_and_active_corpus_clear_thirty_percent`, `test_vbsa_plan_loads_three_unique_canonical_sections_with_d75_intact`, and `/tfw-plan <= 24,730`.
- CRATM role, lead/main semantics, delegation, channels, worktrees, session creation/ownership, landing policy, or other orchestration behavior.
- New research iteration, live model-comparison matrix, model/effort override, token-spend ceiling, or production skill migration.

## Required Sequence

1. Record `83b31ff8d6cdb879fdf4f20578fa688b48863f8a` as the immutable implementation baseline; reproduce the exact per-route/profile charged totals and 33,749-word active corpus above; prove the protected skill/manifest/CRATM selectors and existing D75/VBSA regression spans are clean.
2. Add the one conventions authority and reduce the glossary entry to a router; make its heading uniquely resolvable.
3. Move or add the seven workflow checkpoints at the table's exact resolution boundaries; remove the old pre-state Handoff/Review and create-only Plan semantics.
4. Synchronize only those seven canonical workflow bodies into both existing tracked full-copy receiver trees.
5. Compress only semantically equivalent prose inside the same seven workflow paths until every complete charged graph and the active corpus are non-growing; preserve all ordered algorithms/gates/stops with source-derived scenario/parity/negative assurance and output-changing mutants.
6. Measure local and complete-graph context/word deltas and capture supported-host new/resumed title evidence without treating either as comparative human-performance proof.
7. Run targeted and full tests, project/task checks, clean four-adapter receivers, exact copy parity, protected-path checks, and NUL-safe VALUE accounting; then fix the immutable Candidate before TRACE-only EV/RF writes.

## File Topology

| Surface | Phase-B purpose | Authority boundary |
|---|---|---|
| `.tfw/conventions.md` `Session identity` | sole grammar/resolution/fallback authority | title is navigation metadata; no role or lifecycle authority |
| `.tfw/glossary.md` `Session Naming` | term router | no duplicated grammar or algorithm |
| seven canonical workflows | local authoritative resolution/activation checkpoint | consume the shared contract; no copied fallback logic |
| seven `.claude/commands/` copies | tracked full-copy receiver surface | byte-exact canonical copies |
| seven `.agent/workflows/` copies | tracked compatibility receiver surface | byte-exact canonical copies; not plural manifest authority |
| `docs/scripts/test_runtime_context.py` | source-derived semantics, immutable per-route/corpus accounting, mutants | assurance only; existing D75/VBSA constants/tests stay unchanged and expected outputs remain independent of produced records |
| `docs/scripts/test_integration.py` | 11-route classification, copies, clean receivers, protected surfaces | assurance only; manifest remains tooling metadata |
| Phase `evidence/` | title readback, word/context effects, tests, accounting, EV | TRACE only; never runtime input |

## Knowledge Applications

| PV priority | Exact item | Phase-B application |
|---|---|---|
| P0 | `README.md` How It Works: inspectable context, checkpoint resume, human/agent responsibilities; `.tfw/README.md` NS1 continuity and NS3 vendor/runtime non-goals | The identity checkpoint must aid continuation while artifacts and humans retain authority; no host becomes the source of task truth. |
| P1 | `.tfw/README.md` Methodology values: Structural Enforcement, Naming Creates Behavior, Portability; Success Criteria 1, 2, and 4 | Put identity in observable workflow steps, keep semantics provider-neutral, and never present a label as proof or acceptance. |
| P2 | `knowledge/philosophy.md` F3, F4, F13, F21, F24, F28, F32, F43 | Prefer precise cross-domain terms, addressed structural checkpoints and explicit N/A/reporting; preserve architecture rather than patching one title. |
| P3 | `KNOWLEDGE.md` D15, D28, D54, D68–D70, D73–D78 | Keep one workflow-owned selective-read system, current task identity grammar/state authority, four-adapter manifest, thin proxy baseline, immutable accounting, and worktree attribution. |
| P4 | `conventions.md` HL Contract rules 5–6 and 20–21; Design Rules; Anti-patterns; Role Lock Protocol | Derive rather than amend the master; centralize semantics; keep workflow steps self-contained and adapter-safe; do no code in planning. |
| P5 | `knowledge/convention.md` F4 and F19 | Make the reference an executable checkpoint and use one casing/delimiter vocabulary without exceptions. |
| P6 | `knowledge/process.md` F3, F4, F7, F27, F30, and F43 | Exact naming and numbered gates must survive session loss; capture needs an enforcement site; explain intentional omission where readers encounter it. |
| P7 | N/A after scan | No additional domain/constraint/stakeholder topic adds a Phase-B rule beyond the frozen master and cited architecture/process items. |

## Cross-Phase Handoff

Phase A and B share `.tfw/conventions.md` and the two assurance files. The Phase-A reviewed baseline is already on `master`; Phase B changes only the new session-identity range and Phase-B tests. Phase-A R0–R5 evidence remains intact and the 22 production skill paths remain byte-identical to `83b31ff8d6cdb879fdf4f20578fa688b48863f8a`.

## Phase-Local Risks

| Risk | Control |
|---|---|
| A shared contract passes local caps but grows the charged graph | Enforce the exact per-route/profile ceilings and 33,749 active-corpus ceiling from `83b31ff`; treat 260/45 only as extra caps. |
| Workflow checkpoints drift from the central grammar | Keep only timing/WORK binding locally; source-derived tests reject copied semantic clauses and missing/misordered routes. |
| Net-zero editing removes a gate or silently rebases D75 | Compress only the same seven workflow paths; preserve algorithms with semantic mutants and keep named tests/constants unchanged. |
| A compact cue loses unique task identity | Check modern abbreviation uniqueness across configured roots; otherwise use full canonical ID. |
| Phase or `LEAD` is guessed | Require governing phase state/lineage or binding; omit the phase/use ordinary work cue on ambiguity. |
| Host inability becomes a workflow blocker | Report intended title and exact limitation once, then continue; never claim verified rename. |
| Supported-host evidence is mistaken for portability or human performance | Bound claims to exact current-host readback/retrieval/visible observation; list unobserved hosts and metrics. |
| Copied receivers or sibling work enter Candidate | Sync exact seven paths, stage explicit selectors, recheck branch status and protected diffs before Candidate. |

---

*Phase HL — TFW_20260905-124029_RTPSN / Phase B | 2026-09-05*
