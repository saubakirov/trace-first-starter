# Phase HL — TFW_20260902-175227_RCFR / Phase B: Primary Role Paths

> **Date**: 2026-09-04
> **Author**: Codex (Coordinator)
> **Status**: 🧩 DERIVED — Phase TS approved
> **Master HL**: [Runtime Context Footprint Reduction](../HL-TFW_20260902-175227_RCFR.md)
> **Master Contract**: 🔒 FROZEN — this file adds execution context only
> **Research Basis**: [Iteration 2 RES](../research/iter2/RES.md) · [R15–R18, R21–R23, R35–R39](../research/iter2/3_extract.md)
> **Predecessor**: [Phase A RF](../phase-a/RF__phase-a__common_authority_and_context_topology.md) · [Phase A REVIEW rev4](../phase-a/REVIEW__phase-a__common_authority_and_context_topology__rev4.md)

---

## Parent Derivation

This phase implements master HL §4 Phase B. It delivers minimal Coordinator, Researcher,
Executor, and Reviewer runtime paths while preserving the master contract's approval, freeze,
amendment, research, onboarding, execution, evidence, RF, independent review, Purpose Check,
citation-bar, disposition, verdict-routing, and hard-stop guarantees.

Vision, acceptance, failure conditions, and principles remain solely in the frozen master HL.

## Pre-TS Gate

Phase A is actually delivered, not merely planned:

- `phase-a/status.md` is `DONE`.
- Phase A RF records workflow-owned selective reads, unique-heading refusal, the task-digest
  Knowledge Gate, one adapter manifest, and a source-derived semantic oracle.
- Phase A REVIEW revision 4 is `✅ APPROVE`; no cited Phase A failure remains.
- Phase A is present in master at `80382fbffd52b1f13cb3b38e8e450ecc0fef2fd5`.
- The immutable legacy RDP `123>120` journal diagnostic remains outside this phase.

The clean-worktree Knowledge Gate reports zero pending task IDs, zero removed IDs, and zero
problems. The separately observed machine-local `TFW-36` case is therefore a local diagnostic,
not a reason to invent or alter that legacy task.

## Phase-Entry Baseline

Measurement is whitespace words (`\S+`) over the fixed transitive read graph at Phase A's closing
commit. Dynamic task artifacts and relevance-triggered P5–P7 facts are excluded on both sides;
every separately instructed repeat is counted. Coordinator includes the independent P0–P4 scan;
Reviewer includes the same scan plus the Purpose Check's deliberate North-Star reread.

| Primary path | Phase-entry fixed words | Phase-B ceiling | Conservative candidate forecast | Forecast reduction |
|---|---:|---:|---:|---:|
| Coordinator `/tfw-plan` | 50,851 | 35,596 | ≤25,620 | ≥49.6% |
| Researcher `focused` | 29,992 | 20,994 | ≤6,051 | ≥79.8% |
| Researcher `deep` | 30,057 | 21,040 | ≤6,084 | ≥79.8% |
| Executor `/tfw-handoff` | 55,885 | 39,119 | ≤7,220 | ≥87.1% |
| Reviewer `/tfw-review` | 74,537 | 52,176 | ≤26,881 | ≥63.9% |
| **Plan + focused + deep + handoff + review** | **241,322** | **168,925** | **≤71,856** | **≥70.2%** |

The accepted Phase A audit separately reproduces `/tfw-plan` at `64,229 → 35,380` and
`/tfw-knowledge` at `78,587 → 41,659`. The first number above adds the still-required independent
P0–P4 decision scan to the 35,380-word Phase B entry path rather than hiding it.

## Selected Architecture

```text
active root
   └─ primary role skill: identify command + role + canonical workflow + hard stop
          └─ canonical workflow: one ordered, checkpoint-specific Read Contract
                 ├─ task status/journal first
                 ├─ exact governing task artifacts
                 ├─ addressed shared rules only when a decision needs them
                 ├─ template only at its write/review gate
                 └─ history and P5–P7 knowledge only when triggered

generated audit/manifest ── evidence and copy metadata only ── never a role input
```

The skills become minimal bootstrap routers. The four canonical workflows remain the sole
algorithm owners and select each checkpoint's inputs. Templates continue to own forms. The
Reviewer deliberately retains independent PV and Purpose Check reads; the Executor and Researcher
consume the Coordinator's citations rather than repeating that scan.

## Execution Boundary

### Included

- R15–R18: all four primary Codex skills lose their second full common-library preload while
  retaining command recognition, Role Lock, workflow routing, template/evidence obligations, and
  hard stop.
- R21–R23 plus the existing Phase A `plan.md` contract: the four canonical workflows acquire or
  refine checkpoint-specific ordered reads and remove duplicated form/rule prose.
- R35–R39 as touched: canonical workflow copies, Codex skill sources and installed copies, and the
  manifest-driven clean-receiver route stay exact across supported adapters.
- The existing semantic oracle and runtime audit expand from Phase A's two commands to all four
  primary roles, including focused/deep research and deliberate repeated Review judgments.

### Excluded

- Phase C closure and secondary commands except regression checks proving they did not break.
- New research, frozen master-HL changes, task-artifact compression, book/essay/site work,
  minification, and storage-size optimization.
- Changes under `tasks/`, including `TFW-36` and the immutable RDP journal.
- New runtime manifests, compiled role packets, configuration keys, or persistent state.

## Exact Change Surface

| Surface | Files | Purpose |
|---|---:|---|
| canonical primary workflows | 4 | one algorithm owner and ordered checkpoint reads |
| Codex role-skill sources + installed copies | 8 | minimal bootstrap/router with no second full preload |
| installed Claude + legacy Antigravity workflow copies | 8 | byte-synchronized changed canonical behavior |
| shared Phase A validation | 2 | four-role read graph, semantic mutants, clean receiver |
| adapter manifest | 1 | exact route/source/role/copy contract; non-runtime |
| **maximum implementation surface** | **23 existing files** | no new runtime file |

Primary artifact templates are verified as form authorities and remain outside the mutation
surface. If a preserved gate cannot be represented without changing one, execution stops for a TS
revision rather than silently widening scope.

## Cross-Phase Handoff

Phase C receives four compact primary role paths plus the extended audit/oracle. It may compact
closure and secondary workflows, but it must not reintroduce skill-owned preloads or weaken the
Phase B semantic records. Any later edit to `plan.md`, the manifest, or shared validators is a
cross-phase modification and must preserve both Phase A and Phase B gates.

## Phase-Local Risks

| Risk | Control |
|---|---|
| shortening a skill removes a command-level refusal | retain the role lock, canonical pointer, template/evidence obligations, and hard-stop assertion |
| a workflow read contract hides a required repeat | every repeat has checkpoint purpose; Reviewer PV/Purpose independence is explicitly tested |
| a shorter workflow moves form back into prose | templates remain the form authority; duplicate structure is deleted from workflows |
| audit proves its own model | source-derived semantic records and deliberate mutants remain independent of generated read output |
| derived adapter copies drift | manifest exact-set/role/path checks plus byte equality for installed copies |
| a 30% pass comes from omitting a dynamic input | dynamic reads are shown in the manifest and excluded symmetrically from word arithmetic |

---

*Phase HL — TFW_20260902-175227_RCFR / Phase B | 2026-09-04*
