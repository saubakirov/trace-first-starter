# TS — TFW_20260922-123250_CMTR / Phase C: Minimal Core Integration and Live Pilot

> **Current filename**: `TS__phase-c__minimal_core_integration_and_live_pilot.md`
> **Date**: 2026-09-22
> **Author**: robert
> **Status**: 🟢 TS_APPROVED
> **Parent HL**: [HL-TFW_20260922-123250_CMTR](../HL-TFW_20260922-123250_CMTR.md)

---

## 1. Objective

Replace the rejected Phase A tier/profile/self-calibration residue with a concise provider-neutral
rule applied at each real role launch. Preserve the required quality floor, expose when a minimum is
not proved and avoid unnecessary model, token and session spend.

## 2. Scope

### In Scope

- Replace the obsolete section in `.tfw/conventions.md` with `Launch selection`.
- Replace the tier/profile instructions in Plan Step 5 and enforce the rule at every dispatch.
- Remove the decorative execution-profile column/field from the HL and TS templates.
- Prove the change with the live Executor/Reviewer launches, focused inspection and existing tests.

### Out of Scope

- Provider adapters, glossary, configuration, model rosters, pricing tables or a new artifact type.
- Effective-backend-setting, minimum-cost, savings or unpiloted-provider claims.
- New permanent tests, release/version/changelog work, push or other external effects.
- Rewriting Phase A history or research artifacts.

## 3. Principles Check

| # | HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Quality floor before economy | AC-1, AC-2 | prerequisites and quality floor precede model/effort choice |
| P2 | Exact launch, not role taxonomy | AC-1, AC-2 | tiers and profiles are absent; every dispatch applies the rule |
| P3 | Model and reasoning are separate | AC-1, AC-2 | separate selection is explicit |
| P4 | Live provider truth | AC-1, AC-4 | no static names; native inspection or bounded unavailability |
| P5 | Honest evidence boundaries | AC-1, AC-5 | requested/effective/delivery/outcome/rework remain distinct |
| P6 | Saint-Exupéry / proportional assurance | AC-3, AC-4, AC-5 | four files, no new entity or permanent test |

## 4. Affected Files and Value-Bearing Accounting

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `.tfw/conventions.md` | MODIFY | `VALUE` | Own the concise provider-neutral rule and evidence boundary. |
| `.tfw/workflows/plan.md` | MODIFY | `VALUE` | Apply selection at actual Coordinator dispatch; remain ≤1,400 words. |
| `.tfw/templates/HL.md` | MODIFY | `VALUE` | Remove the execution-profile column without replacement. |
| `.tfw/templates/TS.md` | MODIFY | `VALUE` | Remove the recommended execution-profile field without replacement. |

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | The four literal paths above; no directory or pattern expansion. |
| Baseline / selector source | `e819908`; accepted owner rendering and this TS are recoverable through task journal and Git. |
| Candidate rule | First tested Executor commit containing all four VALUE changes and required evidence, before RF/REVIEW/final transition. |
| Logical VALUE files | 4 planned maximum; all MODIFY; rename counts once. |
| Touched text LOC | 150 additions + 150 deletions = 300 planned maximum; actual numeric numstat fields govern. |
| Triggers / disposition | 4 files / 300 LOC are below project prompts 50/5,000; metrics bound scope and are never quality evidence. |
| Multiplier / authority | Immutable 4-path / 300-LOC maximum. Coordinator may subtract; another path or excess LOC requires owner approval. |
| Approval epoch / failure | Owner acceptance at `journal/20260922-171921__gate_answer__3d91.md`; missing/mismatched/late authority is BLOCKED. |

```powershell
$valuePaths = @(
  '.tfw/conventions.md',
  '.tfw/workflows/plan.md',
  '.tfw/templates/HL.md',
  '.tfw/templates/TS.md'
)
git diff --name-status --find-renames=50% -z e819908 <CANDIDATE_SHA> -- $valuePaths
git diff --numstat --find-renames=50% -z e819908 <CANDIDATE_SHA> -- $valuePaths
```

### Prospective scope rulings

The owner accepted the four-file delivery set and concise rendering. No scope exception exists.

### Task-local hard constraints

| M1 consequence | M2 object/risk | M3 measure/selector | M4 pre-act check | M5 softer-control gap | M6 change authority |
|---|---|---|---|---|---|
| Decorative policy or provider overclaim returns to core | four literal VALUE paths | exact path diff and active-text search | inspect baseline and accepted rendering | prose review alone can miss stale fields | owner for any added path or denominator excess |

**Actions (not budget dimensions):** 4 VALUE modifications; no VALUE create/delete/rename.
**Immutable owner-approved denominator:** 4 literal VALUE files and at most 300 touched text LOC; never ratchets.

## 5. Acceptance Criteria

### AC-1: Concise provider-neutral launch rule

`.tfw/conventions.md` contains one `Launch selection` section that:

- checks context, tools, native availability, authority, addressable unit and exact return route;
- sets a quality floor from uncertainty, dependencies, assurance timing/strength and consequence/reversibility;
- selects model and reasoning effort separately from current native options;
- names a lower-resource option and its material risk or `not compared`;
- uses the two-line `Launch` / `Why` output when native authorized creation is unavailable;
- separates requested, effective when observable, delivery, outcome and material rework; and
- keeps provider rosters and controls out of the core rule.

Gate: inspect the replacement section against owner acceptance and iteration-4 D15–D21.
Evidence: exact active-core diff in `evidence/EV__phase-c__minimal_core_integration_and_live_pilot.md`.

### AC-2: Enforcement at actual dispatch

Plan Step 5 preserves all coordination fields and applies launch selection to each role launch.
The post-approval dispatch instruction explicitly requires this selection and rejects a profile as a
substitute. Native authorized launches pass parameters; other launches use the two-line output.

Gate: inspect both Plan locations; confirm no role/phase tier decides model or effort.
Evidence: this Phase C Executor dispatch plus the later Reviewer dispatch and returned outcomes.

### AC-3: Decorative profile removal

The HL Coordination Selection table ends at `Immutable epoch`. The TS header has no execution-profile
field. No replacement field, launch-profile artifact or glossary entity is introduced.

Gate: inspect both templates and search the four VALUE files for legacy profile text.
Evidence: focused `rg` output recorded in EV.

### AC-4: Naming, length and exact delivery boundary

The core heading is `Launch selection`; research labels, tier names, static model examples and
self-calibration are absent from active text. Plan remains at or below 1,400 words. Candidate changes
exactly the four literal VALUE paths and stays within 300 touched text LOC.

Gate: word count, exact path diff and `git diff --check`.
Evidence: command outputs and accounting in EV/RF.

### AC-5: Purpose assurance without proxy tests

Existing documentation/integration and blob-boundary tests pass. No permanent test is added.
Independent REVIEW checks the frozen Goal/Value and North Star, not artifact count or commit presence.
Claims remain bounded to observed requested parameters, delivery, outcome and material rework; no
effective-setting, global-minimum, savings or foreign-provider working claim is introduced.

Gate: existing test suite and independent `/tfw-review`.
Evidence: test outputs, Executor RF and Reviewer verdict.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-c__minimal_core_integration_and_live_pilot.md` | Per-AC evidence, live-launch observations, accounting and test results. |

## 6. Binding Rendering and Technical Guidance

The owner accepted this semantic rendering. Line wrapping may change; concepts, names and evidence
ceilings may not expand.

```md
### Launch selection

Before creating a separate role unit, the Coordinator:

1. **Checks prerequisites:** required context, tools, native availability, authority, an addressable unit and an exact return route. If one is missing, do not launch; name it.
2. **Sets the quality floor** from uncertainty, dependency breadth, assurance timing and strength, and consequence/reversibility.
3. **Selects model and reasoning effort separately** from current native options. Choose the least-resource option justified to meet the floor. Name one plausible lower-resource option and either the material failure it risks or `not compared`; do not call the choice minimum without comparison.
4. **Applies the choice at launch.** When native and authorized, pass the parameters and record dispatch. Otherwise output exactly:
   `Launch: <command> · <model> · <effort>`
   `Why: <reason>; lower: <option> — <risk | not compared>.`
5. **Keeps evidence separate:** requested settings, effective settings when observable, delivery, outcome, and material rework. Correct the next launch by the failure cause, not by role name, provider analogy, or completion alone.

Provider-specific rosters and controls belong to the owning adapter or current native inspection, never this core rule.
```

Plan Step 5 uses the accepted compact wording and adds after the approval/dispatch instructions:

```md
Every dispatch applies this launch selection; profiles never substitute.
```

Template changes are deletion-only for the execution-profile column/field. Executor may improve
English grammar only when meaning, two-line output, names and length bounds remain unchanged.

## 7. Definition of Failure

- ❌ Any tier, role name or phase name selects the model/effort.
- ❌ Static model names, a permanent roster, self-calibration or a replacement profile enters core.
- ❌ The choice is called minimum without a bounded comparison.
- ❌ Requested parameters are reported as effective settings or sufficient by delivery alone.
- ❌ Another VALUE file, more than 300 touched LOC, a permanent test or an adapter claim is added.
- ❌ Plan exceeds 1,400 words or owner-facing output exceeds the two accepted lines.
- ❌ Review checks only TS/process conformance and not frozen purpose/value.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Compact text loses an authority or return prerequisite | AC-1 exact checklist and independent review. |
| Lower-option clause becomes another decorative metric | Require material risk or `not compared`; never score it. |
| Word-budget compliance drives semantic deletion | Preserve the binding checklist; compress only repetition. |
| Successful Codex launch is overclaimed as an optimum | Keep requested/effective/delivery/outcome/rework separate. |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| Four VALUE files in §4 | Phase A rejected Candidate | Forward-correct current master; preserve Phase A history. |

---

*TS — TFW_20260922-123250_CMTR / Phase C: Minimal Core Integration and Live Pilot | 2026-09-22*
