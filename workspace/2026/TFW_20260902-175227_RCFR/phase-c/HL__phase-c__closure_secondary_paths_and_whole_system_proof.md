# Phase HL — TFW_20260902-175227_RCFR / Phase C: Closure, Secondary Paths, and Whole-System Proof

> **Date**: 2026-09-04
> **Author**: Codex (Coordinator)
> **Status**: 🧩 DERIVED — Phase TS approved
> **Master HL**: [Runtime Context Footprint Reduction](../HL-TFW_20260902-175227_RCFR.md)
> **Master Contract**: 🔒 FROZEN — this file adds execution context only
> **Research Basis**: [Iteration 2 RES](../research/iter2/RES.md) · [R04, R07, R19, R24–R34, R39](../research/iter2/3_extract.md)
> **Predecessor**: [Phase B RF](../phase-b/RF__phase-b__primary_role_paths.md) · [Phase B REVIEW rev2](../phase-b/REVIEW__phase-b__primary_role_paths__rev2.md)

---

## Parent Derivation

This phase implements master HL §4 Phase C. It compacts lifecycle closure, status/journal use,
and the seven secondary commands; removes the remaining active stale or readerless instruction;
and proves the complete eleven-command runtime graph without changing the master contract's
meaning, algorithms, guarantees, authority boundaries, refusal conditions, or 30% threshold.

Vision, acceptance, failure conditions, and principles remain solely in the frozen master HL.
The human essay and book remain outside every agent dependency.

## Pre-TS Gate

The dependency chain is factually complete:

- `phase-a/status.md` and `phase-b/status.md` are both `DONE`.
- Phase A REVIEW revision 4 and Phase B REVIEW revision 2 are both `✅ APPROVE`; neither leaves a
  cited acceptance failure or pending disposition.
- Phase B delivered the one-workflow read owner, all four primary role paths, the shared REVISE
  route, source-derived semantic records, and four-vendor clean-receiver proof.
- Current `master` and this worktree's entry `HEAD` are the same commit,
  `cf36dd6ac404b2335234cd9763bc4821409ca9fc`, and the entry worktree was clean.
- The hard Knowledge Gate reports `1/5` pending task IDs, with no problem or removed-task IDs;
  consolidation is not due.
- Research iteration 2 marked the design sufficient and gives exact Phase C recommendations.
  No new hypothesis or contract question remains, so new research would repeat settled work.

The immutable legacy RDP `123>120` journal diagnostic remains a reported external condition. Phase
C may make future pre-write behavior enforceable but may not edit that event or any file under
`tasks/`.

## Phase-Entry Baseline

Whitespace words (`\S+`) remain the unit. The immutable baseline for every Phase C comparison is
`cf36dd6ac404b2335234cd9763bc4821409ca9fc`; dynamic task artifacts and relevance-triggered facts
must be shown on both sides and excluded symmetrically from fixed arithmetic.

The current audit already reproduces the five completed primary variants at this commit:

| Existing primary path | Phase-C entry words |
|---|---:|
| Coordinator `/tfw-plan` | 24,730 |
| Researcher `/tfw-research`, focused | 6,103 |
| Researcher `/tfw-research`, deep | 6,168 |
| Executor `/tfw-handoff` | 6,366 |
| Reviewer `/tfw-review` | 25,182 |

The still-uncompacted secondary carriers and the two lifecycle form carriers contain 9,873 words
before their transitive preloads and repeated reads are charged:

| Surface | Skill words | Workflow words |
|---|---:|---:|
| `/tfw-resume` | 176 | 755 |
| `/tfw-docs` | 149 | 438 |
| `/tfw-knowledge` | 162 | 1,021 |
| `/tfw-release` | 157 | 513 |
| `/tfw-update` | 173 | 1,165 |
| `/tfw-config` | 160 | 788 |
| `/tfw-init` | 192 | 1,973 |
| `status.md` + journal-event templates | — | 2,051 |

These carrier counts are diagnostic, not the success metric. AC-1 extends the Phase A/B audit to
derive the exact transitive baseline for all seven commands, lifecycle writes, repeated reads, and
the unique active `.tfw` corpus before any reduction claim is accepted.

## Result Preview

```text
BEFORE — secondary and close paths at cf36dd6

/tfw-secondary
  └─ skill reloads broad common files
      └─ workflow repeats or scans a broad source
          ├─ resume follows obsolete HL__Phase* globs
          ├─ docs reads all KNOWLEDGE for §§1–3 work
          ├─ release/update load unbounded history
          ├─ config registry names missing headings
          └─ status/event forms carry incident essays

AFTER — one complete current runtime system

root route
  └─ thin command/role skill
      └─ one canonical checkpoint Read Contract
          ├─ selected status + journal first
          ├─ exact governing artifact or uniquely named range
          ├─ form template only at the write gate
          └─ history/knowledge only when a decision triggers it

11 commands + focused/deep research + revision + knowledge close
  └─ every edge has a decision, word cost, authority and repeat class
      └─ ≥30% whole-system reduction, no primary-path regression
          └─ same decisions, refusals, effects, gates and clean receivers
```

The stakeholder receives one report with exact before/after counts per path and across the full
runtime corpus, not a claim inferred from smaller files or fewer bytes.

## Selected Architecture

The canonical workflow remains the sole algorithm and ordered-read owner. A repository-local skill
recognizes the command, enforces its role boundary before dispatch, opens the workflow, and does not
preload its inputs again. Templates own output form and schema; uniquely addressed convention
ranges own shared invariants; the glossary routes terms and PV; task-local state and artifact
lineage outrank derived views and filename guesses. Generated audit output and the adapter manifest
remain evidence/copy metadata, never runtime authority.

Status and journal instructions are treated as live write paths rather than passive documentation:
their forms must stay complete and compact, and every immutable bound must have a reader before the
write it governs. Compatibility history remains discoverable through named durable traces, not
resident in every template read.

## Execution Boundary

### Included

- R19: remove independent full preloads from all seven secondary Codex skills while retaining each
  command's role/refusal boundary and canonical route.
- R24, R25, R31–R34: add or refine ordered Read Contracts and current algorithms for Docs,
  Knowledge, Resume, Release, Update, Config, and Init.
- R04/R07 and the Phase C deliverable: compact status/journal form and lifecycle reads while
  preserving every closed field/kind, transition, immutability, attribution, compatibility, and
  refusal rule.
- Extend the existing audit, semantic oracle, stale/duplicate ledger, and clean-receiver harness;
  do not create parallel proof machinery.
- Synchronize each changed behavior through the existing manifest topology and retained tracked
  self-hosting copies.

### Excluded

- Any frozen Master HL change, new research, new methodology behavior, new lifecycle state, new
  journal kind, new persistent field, new config key, or new runtime authority.
- Changes under `tasks/`, edits to prior phase traces, repair of the immutable RDP event, or edits to
  user work outside the authorized surface.
- Essay, book, website, release/version/tag, migration execution, push, merge, publish, or deploy.
- Minification, formatting tricks, storage-size optimization, or moving prose solely to improve a
  count.

## Exact Change Surface

| Surface | Existing files permitted | Purpose |
|---|---:|---|
| seven canonical secondary workflows | 7 | one algorithm/read owner per command |
| Codex skill sources + installed copies | 14 | thin command/role dispatch with byte parity |
| tracked Claude + legacy Antigravity workflow copies | 14 | synchronize every changed canonical workflow |
| status and journal-event templates | 2 | compact, complete form/schema authority at the write gate |
| shared convention/glossary and manifest | 3 | remove surviving duplicate/stale routes without a new authority |
| existing validation scripts/tests | 4 | full graph, lifecycle, semantic, stale, and receiver proof |
| **maximum implementation/test surface** | **44 existing files** | no new runtime file |

The implementation ceiling is 44 modified files and 5,000 changed LOC, within configured project
budgets. Mandatory phase traces and evidence artifacts are process records, not new runtime
surfaces. If the guarantee cannot fit this boundary, execution stops for Coordinator ruling rather
than widening itself.

## Knowledge Basis

| Priority | Exact item | Application |
|---|---|---|
| P0 | `.tfw/README.md` NS1 and NS3; root README `How It Works` | Smaller context is valid only if purposeful continuation and task-local authority remain inspectable; artifact-count bureaucracy is a non-goal. |
| P1 | `.tfw/README.md` `Methodology values` and `Success Criteria` | Gates remain structural, provider-independent, and resumable; reduced prose cannot replace observable acceptance. |
| P2 | `knowledge/philosophy.md` F22, F40, F43, F45 | Keep templates minimal, replace paragraphs with precise terms, prefer architecture over local patches, and subtract before adding. |
| P3 | `KNOWLEDGE.md` D23, D25, D61, D68, D72, D73, D74 | Preserve progressive disclosure, task-local state, finite review routing, workflow-owned reads, semantic proof, and the accepted primary paths. |
| P4 | `conventions.md` `HL (High Level)`, `Design Rules`, `Anti-patterns (prohibited)` | Phase HL is derivation-only; refs sit inside steps; role locks, adapter safety, trace immutability, and current state authority remain enforced. |
| P5 | `knowledge/convention.md` F4, F8, F14 | Each reference has an algorithmic step, lists have one owner, and templates carry only their own form instructions. |
| P6 | `knowledge/process.md` F3, F4, F22, F30, F32, F35, F37–F40, F43 | Write against files, use step/gate algorithms, delete tautology, measure at a named revision, verify externally, and put immutable bounds before writes. |
| P7 | Other topic files | No additional applicable constraint after the required scan; the task is methodology-runtime work already bounded by P0–P6. |

## Closure Handoff

Phase C is the final implementation phase. After an APPROVE verdict, the Coordinator must run
`/tfw-docs`, then `/tfw-knowledge` when the gate/candidates require it, reconcile the phase and
master lifecycle without a task-level phase rollup, and close only when all documentation and
knowledge markers are current. Release, tag, push, and merge remain separate owner-authorized acts.

## Phase-Local Risks

| Risk | Control |
|---|---|
| secondary compression drops a rare refusal or WAIT | one source-derived scenario and output-changing mutant per command family |
| lifecycle prose is deleted with its only edge case | schema/transition fixtures plus a deletion ledger naming surviving authority, test and history |
| status/event bounds are learned after an immutable write | require a pre-write reader and adverse fixture for every immutable bound |
| whole-system totals hide repeated or dynamic reads | same transitive graph algorithm, repeat classification and symmetric dynamic exclusions |
| shared cleanup regresses approved primary paths | freeze `cf36dd6`, reproduce five entry counts, and require no per-path increase |
| self-hosting masks adapter drift | four empty receivers, exact 11-command roles, idempotence, repair and unrelated-content preservation |
| cleanup expands into historical or user-owned files | exact 44-file ceiling, `tasks/` blob check, clean-entry diff audit and Coordinator stop |

---

*Phase HL — TFW_20260902-175227_RCFR / Phase C | 2026-09-04*
