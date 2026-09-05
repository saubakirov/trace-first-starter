# Phase HL — TFW_20260904-113200_VBSA / Phase A: Value-bearing budget contract and adoption

> **Date**: 2026-09-04
> **Author**: Codex (Coordinator)
> **Parent contract**: [HL-TFW_20260904-113200_VBSA](../HL-TFW_20260904-113200_VBSA.md), `🔒 FROZEN — approved by saubakirov 2026-09-04`
> **Phase**: A — Value-bearing budget contract and adoption
> **Status**: 🟡 TS_DRAFT — Awaiting owner approval
> **Authority boundary**: derivation-only; this file adds carrier, sequencing, and phase-local risk context and creates no independent Vision, DoD, DoF, or Principles
> **Project North Star**: inherited from the master HL: root `README.md` opening and `How It Works`; `.tfw/README.md` `NS1`–`NS3`

---

## Parent Contract and Derivation Boundary

Phase A is the only phase declared by the frozen master HL §4. It delivers the complete adoption of value-bearing scope accounting in one releasable unit: canonical semantics, role consumers, templates, project configuration, active adapter copies, structural assurance, and forward migration communication. Acceptance and failure remain exclusively those of master HL §§5–6; the twelve master principles remain exclusively master HL §7.

The phase does not reopen research. Iterations 1 and 2 are complete, iteration 2 is `SUFFICIENT`, and amendments A7–A10 are approved and applied. The phase implements those rulings without editing the frozen master HL, either RES, any RCFR trace, or legacy task history.

## Current Carrier Map

| Carrier | Current defect at `f5a96af07dcdc4230ecf31100bd155a3dca09604` | Phase result |
|---|---|---|
| `.tfw/conventions.md` + `.tfw/glossary.md` | Four repository-volume hard limits; `Scope Budget` still names files/new-files/LOC/modified-files | One value-bearing surface, four purpose classes, two measures, fixed-reference semantics, M1–M6, and one term-router to this authority |
| `.tfw/project_config.yaml` + template | Four `max_*` keys | `decomposition_trigger_files: 50`, `decomposition_trigger_loc: 5000`, `owner_escalation_multiplier: 2`; project-owned file/LOC values preserved by named mapping |
| `plan.md` + TS template | Old hard count/split rule and old Budget line; no prospective authority carrier | VALUE-only plan, immutable denominator, soft-trigger disposition, owner ceiling, M1–M6, and prospective ruling site |
| `handoff.md` + RF/EV templates | Executor counts undifferentiated new/modified/LOC; RF cannot bind one candidate; EV has no accounting row | Executor fixes Candidate before RF/EV, RF binds actual membership/result/decision, and exactly one EV accounting row replays the TS method |
| `review.md` + REVIEW template | Reviewer can verify claims but has no required same-contract budget replay | Independent replay of the same Baseline, Candidate, selector, metrics, command, and decision timing; missing or inconsistent authority is `BLOCKED` |
| `config.md`, `update.md`, `init.md`, `.tfw/CHANGELOG.md`, `RELEASE.md` | Old registry and generic preservation wording do not define the forward key migration or approval epoch | Explicit mapping, retirement disclosure, new-project defaults, version-agnostic update behavior, and a release gate that leaves the version decision to `/tfw-release` |
| `.agent/workflows/*`, `.claude/commands/*` | Exact active/compatibility copies inherit every changed canonical defect | Byte-identical copies for each of the six changed canonical workflows; manifest topology unchanged |
| `docs/scripts/test_runtime_context.py`, `docs/scripts/test_integration.py` | RCFR proves selective reads and parity but not VBSA classifications, invariance, migration, or authority timing | Source-derived semantic fixtures and clean-receiver parity/migration checks; tests remain `ASSURANCE`, not delivery budget |

## Finished Phase Preview

```yaml
tfw:
  scope_budgets:
    decomposition_trigger_files: 50
    decomposition_trigger_loc: 5000
    owner_escalation_multiplier: 2
```

```text
owner-approved Phase A plan: 29 VALUE files / 1,100 touched text LOC
                              │
fixed Baseline f5a96af ───────┼──► first immutable Executor Candidate
                              │          │
declared VALUE selector ──────┘          ├──► 29 logical files
                                         └──► touched LOC = additions + deletions

later RF / EV / REVIEW / journal ─────────────► result unchanged
VALUE revision ───────────────────────────────► new Candidate + recomputation

50 files / 5,000 LOC ── soft decomposition prompts only
≥58 files or ≥2,200 LOC ── Owner before added work (2× immutable plan)
```

The stakeholder receives one stable answer about delivered value and an equally visible, separate assurance trail. A stronger test suite or a longer honest RF cannot manufacture delivery growth.

## Exact Phase Surface and Ownership

| Class | Planned membership | Counted by delivery budget | Purpose |
|---|---:|---:|---|
| `VALUE` | 29 exact text paths | Yes: logical files and touched text LOC | Framework behavior, shipped role surfaces, terminology, migration communication |
| `ASSURANCE` | 2 exact test paths | No | Semantic mutation tests, invariance fixtures, adapter/receiver checks |
| `TRACE` | phase/root state and journals; Phase HL/TS; later ONB/RF/EV/REVIEW/review stages | No | Authority, decisions, evidence, and continuation |
| non-value `DERIVED` | None planned | No | No generated output is needed as a maintained phase result |

All tracked `.agent/workflows/tfw-*` and `.claude/commands/tfw-*` copies changed by this phase are `VALUE`: they are accepted shipped behavior, not transient install/check output. The two Python test files are `ASSURANCE` even though they are required for acceptance.

The phase-level planned result is 29 logical touched VALUE files and 1,100 touched text LOC, reported as 900 additions plus 200 deletions. It is below the current project-owned decomposition triggers of 50 files and 5,000 LOC. The phase remains whole because splitting canonical rules, consumers, templates, adapter copies, and migration communication would temporarily ship contradictory behavior.

## Release and Migration Boundary

Phase A does not choose or write a release number. The implementation supplies the complete old-key→new-key mapping in the target `update/config/init` behavior and an exact `[Unreleased]` updating section. `RELEASE.md` must block a future release until `/tfw-release` has classified the change and, if that decision crosses a major boundary, created the required `.tfw/migrations/{major}.0.0.md` from the already complete migration contract. This is a version-assignment gate, not a deferred behavioral phase.

The mapping preserves the two project-owned values that retain a job:

| Old key | New key | Treatment |
|---|---|---|
| `max_files_per_phase` | `decomposition_trigger_files` | Preserve the configured number; semantics are prospective for TS approved under the introducing release |
| `max_loc` | `decomposition_trigger_loc` | Preserve the configured number; semantics are prospective for TS approved under the introducing release |
| `max_new_files` | — | Retire explicitly as redundant; never reinterpret as total files |
| `max_modified_files` | — | Retire explicitly as redundant; never reinterpret as total files |
| — | `owner_escalation_multiplier` | Add default `2`; its only job is the delegated-authority ceiling |

Old approved TS files and historical results remain readable under their recorded semantics. No update normalizes task artifacts or infers a past approval epoch from current installation state.

## Dependencies and Read Context

| Dependency | Status and application |
|---|---|
| Frozen VBSA master HL | ✅ A7–A10 are applied; this phase derives only from the resulting claims |
| Research iterations 1–2 | ✅ `SUFFICIENT`; no Researcher or third iteration is justified |
| RCFR D75 | ✅ Selective workflow-owned reads, strict-new/tolerant-legacy state, template-owned forms, source-derived tests, and the existing manifest are preserved |
| Knowledge Gate | ✅ `hard`, `problems=[]`, `removed_task_ids=[]`, actual pending `1/5`; below threshold |
| Release number | ⏳ Deliberately reserved for `/tfw-release`; Phase A supplies an exact non-versioned migration contract and release gate |
| Executor / Reviewer | ⏳ Exactly one fresh Executor after owner TS approval, then exactly one fresh independent Reviewer after RF |

Inherited decision context is master HL §7.2, especially P0 NS1/NS2/NS3; P1 Structural Enforcement and Success Criterion 4; P2 F13/F42/F43/F45; P3 D16/D24/D43/D52/D63/D72–D75; P4 HL Contract, Design Rules, Scope Budgets, and prohibited anti-patterns; P5 F5/F22; P6 F32/F36–F40; P7 F7.

## Phase-Local Risks

| Risk | Mitigation |
|---|---|
| A new number is treated as a hard quality veto | Name file/LOC values only as decomposition/disclosure triggers; reserve hard local constraints for a complete M1–M6 tuple |
| Project-owned configuration is silently lost or reinterpreted | Test non-default old values through the explicit mapping and bind semantics to the introducing release plus TS approval epoch |
| Candidate moves when traces are written | Require an implementation Candidate before EV/RF and structural tests proving excluded-only later growth leaves it unchanged |
| Full-copy adapters are misclassified as non-value generated output | Keep every changed tracked adapter copy in the exact VALUE selector and require byte parity |
| The local Saint-Exupéry wording leaks into another project's North Star | Modify only this repository's `.tfw/README.md`; verify init/update receiver fixtures preserve the receiving North Star |
| Release number is decided inside planning | Keep the changelog section `[Unreleased]`; release gate owns version classification and any version-named migration file |
| A concise patch leaves a second obsolete reader | Census old keys and old hard-limit language across canonical and installed adapter surfaces; unexplained live hits fail acceptance |

## Research Closure and Continuation

All five research hypotheses are closed; H4 was refuted and replaced by soft triggers plus explicit authority and material-hard-bound controls. No conflict with the frozen HL or D75 was found.

Owner approval of the adjacent Phase TS freezes the 29-file / 1,100-LOC denominator. After approval, start `/tfw-handoff` in exactly one fresh Executor session. This Coordinator authors no implementation, ONB, RF, EV, or REVIEW.

---

*Phase HL — TFW_20260904-113200_VBSA / Phase A: Value-bearing budget contract and adoption | 2026-09-04*
