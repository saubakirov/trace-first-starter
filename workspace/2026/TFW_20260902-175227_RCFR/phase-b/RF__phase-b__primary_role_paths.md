# RF — TFW_20260902-175227_RCFR / Phase B: Primary Role Paths

> **Date**: 2026-09-04
> **Author**: saubakirov (via Codex)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [Phase B HL](HL__phase-b__primary_role_paths.md)
> **TS**: [TS Phase B](TS__phase-b__primary_role_paths.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|------------|
| `evidence/EV__phase-b__primary_role_paths.md` | Structured AC-1–AC-6 evidence and verdict. |
| `evidence/runtime-context-primary-roles.txt` | Raw five-variant baseline/candidate read graph and word audit. |
| `evidence/semantic-primary-roles.txt` | Source-derived semantic records and mutant test result. |
| `evidence/clean-receiver-primary-routes.txt` | Four-vendor clean-receiver, idempotence, repair, and preservation replay. |
| `evidence/verification-primary-roles.txt` | Targeted/full gates, project/task diagnostics, reduction, parity, and scope counters. |

### Modified Files
| File | Changes |
|------|---------|
| `.tfw/workflows/{plan.md,research/base.md,handoff.md,review.md}` | Made each primary workflow the sole owner of one ordered checkpoint Read Contract while retaining role-specific gates and hard stops. |
| `.tfw/adapters/codex/skills/tfw-{plan,research,handoff,review}/SKILL.md` | Reduced source skills to command, role-lock, canonical-workflow, template-gate, and final-routing obligations. |
| `.agents/skills/tfw-{plan,research,handoff,review}/SKILL.md` | Synchronized exact installed Codex skill copies. |
| `.claude/commands/tfw-{plan,research,handoff,review}.md` | Synchronized exact canonical workflow copies. |
| `.agent/workflows/tfw-{plan,research,handoff,review}.md` | Synchronized exact legacy Antigravity workflow copies. |
| `.tfw/adapters/manifest.yaml` | Identified the existing four primary routes versus unchanged secondary routes without changing schema or runtime authority. |
| `docs/scripts/test_runtime_context.py` | Added the immutable Phase B baseline, five role variants, scoped/dynamic/repeated read graph, source-derived semantic preservation, and high-risk mutants. |
| `docs/scripts/test_integration.py` | Added exact primary copy/role assertions and four-vendor clean install, idempotence, drift repair, unmarked-root, and persistent-router tests. |

## 2. Key Decisions

1. The selected canonical workflow owns read ordering; skills route into it and do not independently preload root or common libraries. This eliminates the largest duplicated fixed packet without creating a second authority.
2. Dynamic task artifacts and relevant P5–P7 sources remain explicit graph edges with `charged: false` on both baseline and candidate. This exposes mandatory dynamic reads without inventing a fixed payload.
3. The Reviewer keeps separate Verify PV and Judge Purpose reads. Their repeated source classification is deliberate and charged, preserving independent acceptance judgment rather than optimizing it away.
4. The existing adapter manifest remains tooling-only. No runtime manifest, field, configuration key, generated packet, template, or secondary workflow was added or changed.

## 3. Acceptance Criteria

- [x] AC-1 — reproduced all five immutable baselines exactly and reported every scoped, dynamic, repeated, purpose, and authority edge; omission/duplicate/preload mutants fail.
- [x] AC-2 — Coordinator and both Researcher modes preserve source-derived decisions, effects, citations, gates, and hard stops through minimal skills and checkpoint reads.
- [x] AC-3 — Executor initial/REVISE, onboarding, dependency, build, evidence, RF, state, and stop behavior remains source-backed; unsupported evidence/build mutants fail.
- [x] AC-4 — Reviewer verification, 42%/100% escalation, Purpose Check, citation bar, disposition, verdict routing, KNW route, independent rereads, and hard stop remain source-backed.
- [x] AC-5 — four primary workflows/skills are byte-equal to tracked copies; four clean receivers expose all 11 commands with exact primary roles; replay is idempotent and repairs drift safely.
- [x] AC-6 — every primary path clears 30%, combined reduction is 72.4%, semantic families match baseline, full gates pass, and no unauthorized path changed.

## 4. Verification

- Targeted runtime tests (`python -m pytest docs/scripts/test_runtime_context.py -q`): PASS — 86 passed.
- Targeted runtime/integration gate (`python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q`): PASS — 143 passed.
- Collection (`python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only`): PASS — 437 tests collected.
- Full tests (`python -m pytest .tfw/scripts/ docs/scripts/ -q`): PASS — 436 passed, 1 skipped.
- Project check (`python .tfw/scripts/gen_index.py --check project`): PASS — exit 0.
- Task diagnostic (`python .tfw/scripts/gen_index.py --check tasks`): expected nonzero — only the immutable RDP `123>120` event-summary exception; no new problem.
- Scope: PASS — 23/23 implementation/test files, 1,005/3,500 changed LOC, 0 new runtime files.

## 5. Evidence

See [EV file](evidence/EV__phase-b__primary_role_paths.md) for evidence details.

Evidence verdict: 6/6 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `workspace/2026/TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md` | front matter `summary` | style | The committed immutable event summary remains 123 code points against the 120-code-point ceiling. The task diagnostic reports it as its only problem; Phase B was explicitly forbidden from repairing it. |

## 7. Fact Candidates

> fact-candidates: processed 2026-09-04

No fact candidates.

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

```mermaid
flowchart LR
    R[Active root] --> S[Thin role skill]
    S --> W[Canonical workflow]
    W --> T[Task-local state and authority]
    W --> A[Addressed shared ranges]
    W --> F[Template at artifact gate]
    M[Tooling-only manifest] -. copy/sync .-> S
    M -. copy/sync .-> W
```

---

## Revision 2 Return — Proof and Rung Routing Repair

> **Date**: 2026-09-04
> **Author**: saubakirov (via Codex)
> **Status**: 🟢 RF — Revision 2 complete
> **TS**: [TS Phase B revision 2](TS__phase-b__primary_role_paths__rev2.md)
> **Implementation candidate**: `8066284`

### 1. What Was Done

#### New Files

No new implementation, test, adapter, or evidence files. Revision 2 appends to the existing ONB,
RF, EV, and four raw evidence files as ordered.

#### Modified Files

| File | Changes |
|------|---------|
| `.tfw/conventions.md` | Established the single rung-1/rung-2/rung-3/mixed routing table and made status, Role Lock, and Hard Stop clauses delegate to it. |
| `.tfw/workflows/{plan,handoff,review}.md` | Made the Coordinator ruling, Executor acceptance, and Reviewer proposal paths consume the shared route without a universal TS-revision instruction. |
| `.claude/commands/tfw-{plan,handoff,review}.md` | Synchronized exact canonical workflow copies. |
| `.agent/workflows/tfw-{plan,handoff,review}.md` | Synchronized exact legacy canonical workflow copies. |
| `docs/scripts/test_runtime_context.py` | Completed both Researcher graphs, added independent stage omission failure, six output-changing semantic families, four route records, and four contradiction mutants. |
| `docs/scripts/test_integration.py` | Added shared-route/copy assertions and an executable universal-route contradiction detector. |

### 2. Key Decisions

1. `conventions.md` → `The 🔄 REVISE route` is the only recipient/artifact/state/hard-stop mapping.
   Workflows retain only role-specific actions needed to consume that mapping.
2. Rung 1 keeps the existing approved TS as its implementation order. The Coordinator records the
   acceptance bound in the live REVIEW, lifecycle remains `RF` until Executor acceptance, and no TS
   sibling is created.
3. Any rung 2, including mixed rung 1 + 2, produces one TS sibling for the complete round and uses
   `TS_DRAFT → ONB`; rung 3 blocks Executor dispatch until the owner verdict leaves an executable
   bound.
4. Semantic mutations alter non-probe source clauses and have explicit alternate derivations, so a
   complete record exists before the independent expected comparison rejects it.

### 3. Acceptance Criteria

- [x] AC-R1 — both Researcher modes enumerate all four stage templates in order under symmetric rules; an omitted Extract edge fails independently; corrected totals are 6,103/6,168.
- [x] AC-R2 — P/R/E/V/C/A each produce a changed named field before independent expected-record rejection; ordinary records and expected-data isolation still pass.
- [x] AC-R3 — isolated rung 1/2/3 and mixed 1+2 resolve exact recipient, ruling site, artifact, lifecycle, and hard stop from one table; four contradiction classes fail; consumers expose no universal route.
- [x] AC-R4 — copies/receivers remain exact, every reduction exceeds 30%, configured gates pass, round/cumulative budgets hold, exclusions are unchanged, and all cumulative artifacts append.

### 4. Verification

- Targeted runtime/integration (`python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q`): PASS — 156 passed.
- Collection (`python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only`): PASS — 450 tests collected.
- Full suite (`python -m pytest .tfw/scripts/ docs/scripts/ -q`): PASS — 449 passed, 1 skipped.
- Project check (`python .tfw/scripts/gen_index.py --check project`): PASS — exit 0.
- Task diagnostic (`python .tfw/scripts/gen_index.py --check tasks`): expected nonzero — only the approved immutable RDP `123>120` exception.
- Runtime totals: `50,851→25,085`, `29,992→6,103`, `30,057→6,168`, `55,885→6,366`, `74,537→25,537`; combined `241,322→69,259` (`71.3%`).
- Scope: PASS — revision 2 uses 12/12 files and 551 LOC; cumulative Phase B uses 24/24 distinct files and 1,556/3,500 LOC.

### 5. Evidence

See [EV file](evidence/EV__phase-b__primary_role_paths.md) for evidence details.

Revision 2 evidence verdict: 4/4 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

### 6. Observations (out-of-scope, not modified)

No new observations. The original immutable RDP `123>120` diagnostic remains the only task-check
problem and remains explicitly excluded from this round.

### 7. Fact Candidates

> fact-candidates: processed 2026-09-04

No fact candidates.

### 8. Strategic Insights (Execution)

No strategic insights.

### 9. Diagrams

```mermaid
flowchart LR
    V[Reviewer proposes and stops] --> C[Coordinator rules once]
    C -->|Rung 1: live REVIEW + existing TS| E1[Executor accepts RF → ONB]
    C -->|Rung 2 or mixed: one TS revision| E2[Executor accepts TS_DRAFT → ONB]
    C -->|Rung 3: HL §12 amendment| O[Owner verdict]
    O -->|Executable bound only| E3[Executor may be dispatched]
```

---

*RF — TFW_20260902-175227_RCFR / Phase B: Revision 2 return | 2026-09-04*
