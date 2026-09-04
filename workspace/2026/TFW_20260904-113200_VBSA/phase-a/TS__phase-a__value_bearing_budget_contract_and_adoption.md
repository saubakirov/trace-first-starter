# TS — TFW_20260904-113200_VBSA / Phase A: Value-bearing budget contract and adoption

> **Date**: 2026-09-04
> **Author**: Codex (Coordinator)
> **Status**: 🟡 TS_DRAFT — Awaiting approval by saubakirov
> **Parent HL**: [HL-TFW_20260904-113200_VBSA](../HL-TFW_20260904-113200_VBSA.md) — `🔒 FROZEN`, including approved/applied A7–A10
> **Phase HL**: [HL__phase-a__value_bearing_budget_contract_and_adoption](HL__phase-a__value_bearing_budget_contract_and_adoption.md) — derivation-only
> **Accounting Baseline**: `f5a96af07dcdc4230ecf31100bd155a3dca09604`

---

## 1. Objective

Deliver the complete Phase A adoption of value-bearing scope accounting. Canonical rules, role workflows, templates, current and starter configuration, tracked adapter copies, migration communication, and structural assurance must agree on one declared `VALUE` surface measured from a fixed Baseline to a fixed Candidate, while `ASSURANCE`, `TRACE`, and non-value `DERIVED` work remain mandatory but do not spend the delivery budget.

## 2. Scope

### In Scope

- Define `VALUE`, `ASSURANCE`, `TRACE`, and `DERIVED` by semantic purpose, including accepted-output and necessary-constituent precedence, whole-fixed-diff treatment for inseparable roles, deterministic prospective sub-file selectors, and separate phase attribution.
- Replace the four-key `tfw.scope_budgets` schema with `decomposition_trigger_files`, `decomposition_trigger_loc`, and `owner_escalation_multiplier`; migrate project-owned file/LOC values explicitly and retire the two redundant dimensions.
- Make planning, execution, RF, one EV accounting row, and independent REVIEW use the same Baseline, Candidate, selector, metric definitions, reproduction method, trigger disposition, authority decision, and timing facts.
- Add the Saint-Exupéry Principle to this project's `.tfw/README.md` NS2 immediately after **Purpose before activity**, and add the compact universal Coordinator mental model to canonical `plan.md` plus its changed tracked copies.
- Preserve D75 selective workflow-owned reads, template-owned forms, strict-new/tolerant-legacy state behavior, the existing adapter manifest, and exact tracked-copy parity.
- Publish version-agnostic forward-migration and `[Unreleased]` communication. Leave the release number to `/tfw-release`, with a release gate requiring the version-named migration artifact if the selected bump crosses a major boundary.
- Add source-derived structural and clean-receiver tests covering semantic classification, stable accounting, migration, authority timing, and adapter behavior.

### Out of Scope

- Any rewrite, normalization, or correction of existing task history, approved TS files, recorded measurements, `tasks/**`, AFD, Helpdesk, or closed RCFR Phase A/B/C traces.
- A release number, VERSION change, tag, push, publish, or deployment; these remain `/tfw-release` and separately authorized external effects.
- A standalone accounting manifest, ledger, registry, production script, alternate-metric registry, fifth semantic class, shadow budget, or ONB accounting authority.
- Any change to `.tfw/adapters/manifest.yaml`, adapter topology, `.agents/skills/**`, root `README.md`, `README.ru.md`, `README.kk.md`, or another project's Project North Star. The allowed VALUE path `.tfw/README.md` is distinct.
- Mechanical deletion, LOC minimization, forced consolidation, or a `Subtraction Check`; simplification may not damage purpose, value, correctness, architecture, modularity, inspectability, or continuation.
- Delivery-specific quality metrics. Evidence, review, safety, compatibility, and proportionality continue under their existing gates.

## 3. Principles Check

| # | Principle (master HL §7) | Enforced by | Gate |
|---|---|---|---|
| P1 | Name the governed object before measuring it | AC-1, AC-8 | The declared VALUE selector is the only budget subject in TS, RF, EV, and REVIEW |
| P2 | Semantic role over location | AC-1, AC-7 | Cross-domain fixtures include a deliverable in a task folder and a source named like a TFW artifact |
| P3 | One measurement, one reference pair | AC-2, AC-5, AC-6, AC-8 | Baseline/Candidate/selector/method identity is source-derived and independently replayed |
| P4 | Trace integrity without trace taxation | AC-1, AC-7, AC-8 | Trace-only growth fixture leaves the Candidate result unchanged while traces remain required |
| P5 | Assurance is not product scope | AC-1, AC-7 | Ordinary assurance and test-as-product override fixtures produce different, justified membership |
| P6 | Structural enforcement | AC-4–AC-7 | Every writer/reader carrier and exact tracked copy is tested; prose-only agreement cannot pass |
| P7 | Domain-agnostic by construction | AC-1, AC-7 | Examples and fixtures cover code, prompts, documents, presentations, data, generated outputs, binaries, and tests |
| P8 | No shadow total | AC-1, AC-3 | Schema and census admit only two VALUE measures and no excluded-class numerical budget |
| P9 | History is evidence | AC-3, AC-7 | Old approved TS/history remain unchanged and tolerant; protected-path checks reject mutation |
| P10 | The Saint-Exupéry Principle | AC-4, AC-7 | Local quote placement and universal non-mechanical mindset are asserted; foreign North Stars remain unchanged |
| P11 | Decomposition signals, not size verdicts | AC-3, AC-4, AC-8 | 50/5000 are recorded with a terminal keep-whole disposition and never gate product quality |
| P12 | Bounded growth authority | AC-4, AC-8 | Immutable 29/1,100 denominator, prospective ruling order, and ≥58/≥2,200 Owner boundary are verified |

## 4. Affected Files

The rows below are the complete planned implementation selector. `Action` remains visible but is not a budget dimension. Every adapter copy in this table is `VALUE` because it is accepted shipped behavior, even when byte-identical to its canonical source.

| File | Action | Class | Reason / required result |
|---|---|---|---|
| `.tfw/README.md` | MODIFY | `VALUE` | This project's accepted North Star gains the quoted Saint-Exupéry Principle in NS2 at the ruled position |
| `.tfw/conventions.md` | MODIFY | `VALUE` | Single canonical accounting, authority, forward-applicability, and M1–M6 contract |
| `.tfw/glossary.md` | MODIFY | `VALUE` | Replace the stale four-limit definition and provide stable term routing to conventions without duplicating authority |
| `.tfw/project_config.yaml` | MODIFY | `VALUE` | Migrate this project's values from four old keys to the three approved keys |
| `.tfw/workflows/plan.md` | MODIFY | `VALUE` | VALUE-only planning, trigger disposition, authority ceiling, and universal Saint-Exupéry mental model |
| `.tfw/workflows/handoff.md` | MODIFY | `VALUE` | Candidate fixation, same-selector execution accounting, prospective stop, and RF/EV binding |
| `.tfw/workflows/review.md` | MODIFY | `VALUE` | Independent same-contract replay, timing adjudication, and BLOCKED/N/A semantics |
| `.tfw/workflows/config.md` | MODIFY | `VALUE` | Three-key Config Sync Registry and explicit mapping/verification behavior |
| `.tfw/workflows/update.md` | MODIFY | `VALUE` | Preserve project-owned values through old→new mapping and approval-epoch semantics without history rewrite |
| `.tfw/workflows/init.md` | MODIFY | `VALUE` | New-project three-key setup and no injection of this project's North Star into a receiver's North Star |
| `.tfw/templates/TS.md` | MODIFY | `VALUE` | Prospective accounting contract, exact class/reason selector, denominator, triggers, constraints, and rulings |
| `.tfw/templates/RF.md` | MODIFY | `VALUE` | Actual Candidate, membership, result, deviation, and pre-work decision binding |
| `.tfw/templates/REVIEW.md` | MODIFY | `VALUE` | Independent accounting result and discrepancy/verdict carrier |
| `.tfw/templates/evidence/EV.md` | MODIFY | `VALUE` | Exactly one dedicated accounting row with method, arithmetic, timing, and result status |
| `.tfw/templates/project_config.yaml` | MODIFY | `VALUE` | Starter defaults 50/5000/2 and project-owned preservation annotation |
| `.tfw/CHANGELOG.md` | MODIFY | `VALUE` | Exact `[Unreleased]` behavior, mapping, compatibility, updating, and retired-wording communication |
| `RELEASE.md` | MODIFY | `VALUE` | Release-number ownership and mandatory version-named migration gate for a selected major boundary |
| `.agent/workflows/tfw-plan.md` | MODIFY | `VALUE` | Exact tracked copy of changed canonical plan workflow |
| `.agent/workflows/tfw-handoff.md` | MODIFY | `VALUE` | Exact tracked copy of changed canonical handoff workflow |
| `.agent/workflows/tfw-review.md` | MODIFY | `VALUE` | Exact tracked copy of changed canonical review workflow |
| `.agent/workflows/tfw-config.md` | MODIFY | `VALUE` | Exact tracked copy of changed canonical config workflow |
| `.agent/workflows/tfw-update.md` | MODIFY | `VALUE` | Exact tracked copy of changed canonical update workflow |
| `.agent/workflows/tfw-init.md` | MODIFY | `VALUE` | Exact tracked copy of changed canonical init workflow |
| `.claude/commands/tfw-plan.md` | MODIFY | `VALUE` | Exact tracked copy of changed canonical plan workflow |
| `.claude/commands/tfw-handoff.md` | MODIFY | `VALUE` | Exact tracked copy of changed canonical handoff workflow |
| `.claude/commands/tfw-review.md` | MODIFY | `VALUE` | Exact tracked copy of changed canonical review workflow |
| `.claude/commands/tfw-config.md` | MODIFY | `VALUE` | Exact tracked copy of changed canonical config workflow |
| `.claude/commands/tfw-update.md` | MODIFY | `VALUE` | Exact tracked copy of changed canonical update workflow |
| `.claude/commands/tfw-init.md` | MODIFY | `VALUE` | Exact tracked copy of changed canonical init workflow |
| `docs/scripts/test_runtime_context.py` | MODIFY | `ASSURANCE` | Source-derived semantic, accounting, trigger, authority, and failure-state tests |
| `docs/scripts/test_integration.py` | MODIFY | `ASSURANCE` | Clean-receiver migration, foreign-North-Star preservation, and exact adapter parity tests |

### Declared excluded selectors

| Selector | Class | Treatment |
|---|---|---|
| Exact Phase HL, governing `TS__phase-a__value_bearing_budget_contract_and_adoption*.md`, `status.md`, `journal/*.md`, `ONB__phase-a__value_bearing_budget_contract_and_adoption.md`, `RF__phase-a__value_bearing_budget_contract_and_adoption.md`, `REVIEW__phase-a__value_bearing_budget_contract_and_adoption*.md`, `evidence/EV__phase-a__value_bearing_budget_contract_and_adoption.md`, and `review/**`, all below `workspace/2026/TFW_20260904-113200_VBSA/phase-a/` | `TRACE` | Exact current and future phase-local lifecycle, evidence, and review surface; never in delivery measures |
| `workspace/2026/TFW_20260904-113200_VBSA/status.md` and `workspace/2026/TFW_20260904-113200_VBSA/journal/20260904-194559__transition__d7c8.md` | `TRACE` | Exact task-local Phase-A entry traces; never in delivery measures |
| Test execution caches and transient clean-receiver fixtures | non-value `DERIVED` | Reproducible and untracked; never persisted as delivery or a parallel ledger |

No planned path is a narrower mixed-role selection. If implementation makes VALUE and an excluded role inseparable in one listed file, the whole file's fixed Baseline→Candidate diff is VALUE. A narrower exclusion is valid only if this TS records a deterministic selector before that work; freehand hunk subtraction is prohibited.

### Value-bearing accounting contract

| Fact | Approved Phase A value |
|---|---|
| Subject | Only changed paths in the 29 exact `VALUE` rows above |
| Baseline | Immutable commit `f5a96af07dcdc4230ecf31100bd155a3dca09604` |
| Candidate rule | The first immutable Executor commit containing every required VALUE change and its ASSURANCE changes after tests pass, created before EV/RF/REVIEW or the RF transition. RF and EV bind its full SHA. Excluded-only later writes do not advance it; any later VALUE change requires a new Candidate and recomputation |
| Selector source | This TS at its owner-approval commit, resolved through phase state/journal and Git; missing or mutable approval lineage is `BLOCKED` |
| Logical touched VALUE files | Count changed selector members; a rename is one logical file; planned denominator **29** |
| Touched text LOC | Sum numeric additions plus deletions from NUL-safe `git diff --numstat --find-renames`; report additions and deletions separately; binary/non-text is per-file `N/A`, never zero; planned denominator **1,100 = 900 additions + 200 deletions** |
| Configured decomposition triggers | `50` logical files and `5,000` touched text LOC from the pre-migration project-owned values |
| Trigger disposition | **Keep one phase.** Planned 29/1,100 is below both triggers, and separating rules, live consumers, templates, copies, and migration would ship contradictory behavior. Triggers are disclosure/decomposition prompts, not quality vetoes |
| Owner escalation multiplier | `2`; Owner is required before work forecast at **≥58 logical files** or **≥2,200 touched text LOC**. Growth from an applicable planned zero would also require Owner; neither measure is zero here |
| Denominator rule | The owner-approved 29/1,100 plan never ratchets after a Coordinator ruling or actual result |
| Missing/late facts | Missing, mutable, mismatched, or retroactively supplied Baseline/Candidate/selector/method/decision facts make the accounting AC `BLOCKED`; `N/A` is only for an inapplicable metric |

**Reproduction method.** Resolve the approved TS text from its approval commit, extract the 29 rows whose Class is exactly `VALUE` into a literal path array, and run both commands from repository root against the same two full SHAs:

```powershell
git diff --name-status --find-renames=50% -z <BASELINE_SHA> <CANDIDATE_SHA> -- $valuePaths
git diff --numstat --find-renames=50% -z <BASELINE_SHA> <CANDIDATE_SHA> -- $valuePaths
```

The first output determines logical membership/action and treats one rename record as one file. The second supplies additions and deletions for text paths; `-` fields mark binary/non-text `N/A`. The EV accounting row records the resolved approval ref, the two SHAs, selector membership, raw arithmetic, trigger disposition, authority/timing result, and command. Executor and Reviewer use this method unchanged.

### Prospective scope rulings

None at approval. If discovery proposes another VALUE path or greater work, the Executor stops before touching it. The Coordinator may append a ruling here before work only when the path is a necessary constituent of the unchanged accepted result; Goal, Value, accepted outputs, AC, DoF, phase ownership/boundary, frozen architecture/target, public interfaces, persisted data, and security/trust/authority boundaries all remain unchanged; every applicable forecast stays below 2× the immutable 29/1,100 denominator; and the ruling records cause, cost, assurance effect, split alternative, Saint-Exupéry judgment, authority, verdict, and timestamp/reference. Performed work is a deviation, never retroactive approval.

### Task-local hard constraint — HC-1 (M1–M6)

| Materiality fact | Bound |
|---|---|
| M1 — consequence | Mutating historical traces, another project's North Star, or adapter topology would corrupt evidence or expand architecture outside the approved result |
| M2 — protected object/risk | `tasks/**`; every `workspace/**` path outside the current VBSA phase/root TRACE selectors above; the frozen master HL and RES files; `.tfw/adapters/manifest.yaml`; `.agents/**`; root `README.md`, `README.ru.md`, and `README.kk.md`; `.tfw/VERSION`; existing `.tfw/migrations/**` |
| M3 — direct measure + selector | Zero Baseline→Candidate changed paths in the protected selector; the Candidate name-only set must be contained by the 31 exact VALUE+ASSURANCE paths plus the declared current-task TRACE selectors |
| M4 — pre-act enforcement | Before any out-of-table write and before Candidate creation, compare the intended/actual path set to this selector and stop on the first mismatch |
| M5 — why softer control is insufficient | File/LOC triggers cannot distinguish one small unauthorized history/topology mutation from legitimate delivery growth |
| M6 — change authority | Only owner `saubakirov`, prospectively. Coordinator authority under the multiplier cannot relax this boundary |

**Action summary (not budget dimensions):** 0 new and 29 modified planned VALUE files; 0 new and 2 modified ASSURANCE files; lifecycle TRACE files are created/appended as required. **Budget result:** 29 logical VALUE files; 1,100 planned touched text LOC (900 additions, 200 deletions).

## 5. Acceptance Criteria

### AC-1: One semantic budget subject

The framework names the declared value-bearing surface as the only budget subject and classifies every planned or actual changed path by purpose rather than location or extension.

- [ ] `VALUE`, `ASSURANCE`, `TRACE`, and `DERIVED` have non-overlapping defaults, accepted-output/necessary-constituent precedence, whole-fixed-diff ambiguity treatment, and no fifth class.
- [ ] Examples cover code, prompts, documents, presentations, data, generated final outputs, ordinary tests, test-as-product, deliverables inside task folders, and TFW-looking product sources.
- [ ] Exclusion from budget explicitly does not mean out of implementation scope, optional, untested, unevidenced, unreviewed, unsafe, or exempt from proportionality.
- [ ] Exactly two delivery measures exist: logical touched VALUE files and touched text LOC, with additions/deletions separate, rename identity, and binary/non-text `N/A`; no shadow excluded-class budget or alternate-metric registry exists.

Gate: `python -m pytest docs/scripts/test_runtime_context.py -q -k vbsa`
Evidence: In the local repository, replay semantic fixtures from their declared inputs and record the source clauses plus produced class/metric output in the phase EV.

### AC-2: Fixed and phase-correct measurement contract [depends: AC-1]

Planning, execution, evidence, and review must carry the same fixed accounting identity and refuse to reconstruct missing authority.

- [ ] The contract names immutable Baseline and Candidate, selector/class/reason, metric definitions, and one NUL-safe reproduction method; later excluded-only trace/assurance/non-value-derived changes leave Candidate and result unchanged.
- [ ] Any later VALUE change creates a new Candidate. Missing, mutable, mismatched, or late facts yield `BLOCKED`; metric-only `N/A` is never a substitute for missing authority.
- [ ] Inseparable mixed roles count the whole fixed file diff unless a deterministic narrower selector existed before work; freehand line subtraction is forbidden.
- [ ] Phase attribution is separate: distinct immutable phase Candidates, one whole-delta phase owner with dependency, or `INVALID`; never double count or invent an “other phase” class.

Gate: `python -m pytest docs/scripts/test_runtime_context.py -q -k "vbsa and (accounting or candidate or attribution)"`
Evidence: Run the exact TS reproduction method against the bound Baseline/Candidate and record the resolved refs, selector, membership, additions, deletions, total, and status in exactly one EV accounting row.

### AC-3: Three-key configuration and forward migration [depends: AC-1]

Current and starter configuration, Config Sync, init, update, changelog, and release guidance must preserve project-owned intent while changing the schema and prospective semantics explicitly.

- [ ] `tfw.scope_budgets` contains only `decomposition_trigger_files: 50`, `decomposition_trigger_loc: 5000`, and `owner_escalation_multiplier: 2` in this project and the template; no old key remains live.
- [ ] Migration maps a receiver's non-default `max_files_per_phase` to `decomposition_trigger_files` and `max_loc` to `decomposition_trigger_loc` without changing the numbers; it explicitly retires `max_new_files` and `max_modified_files` and adds multiplier default 2.
- [ ] Old approved TS files and historical results keep recorded meaning. New behavior applies prospectively by introducing release plus TS approval epoch; current installation state never reinterprets history.
- [ ] `[Unreleased]`, config/update/init wording, and update briefing source state what changes, what is preserved/removed, and what a user now does differently.
- [ ] Phase A assigns no version. `RELEASE.md` blocks release until `/tfw-release` classifies the bump and creates the required `.tfw/migrations/{major}.0.0.md` if a major boundary is selected.

Gate: `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q -k "vbsa and (config or migration or release or update or init)"`
Evidence: Exercise a clean receiver fixture with customized old values and record the resulting exact three-key block plus unchanged historical task bytes in the phase EV.

### AC-4: Prospective authority and Saint-Exupéry judgment [depends: AC-2] [depends: AC-3]

The Coordinator receives bounded prospective authority, never authority to revise its own grant, ratchet the plan, approve retrospectively, or trade architecture for a smaller patch.

- [ ] Plan and TS carriers distinguish soft trigger disposition, M1–M6 task-local hard constraints, Coordinator-preservable boundaries, and Owner escalation at `>= owner_escalation_multiplier` or growth from applicable zero.
- [ ] The immutable owner-approved planned result is the denominator after every ruling; a Coordinator can act only before added work and below the ceiling inside the unchanged accepted result and protected boundaries.
- [ ] `.tfw/README.md` NS2 places the owner's exact quotation immediately after **Purpose before activity** and states the non-damage boundary.
- [ ] Canonical `plan.md` has a compact universal mental model analogous to Working Backwards, without `Subtraction Check` or mechanical minimization; its tracked copies are exact.
- [ ] Init/update receiver tests prove another project's North Star is not overwritten or injected with this project's quoted wording.

Gate: `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q -k "vbsa and (authority or saint or north_star)"`
Evidence: Record source-location checks and a clean-receiver before/after North Star byte comparison in the phase EV.

### AC-5: Executor, RF, and EV binding [depends: AC-2] [depends: AC-4]

The Executor must consume the approved contract, stop before unauthorized growth, bind one Candidate before trace completion, and attest to the actual result without becoming an accounting authority.

- [ ] Handoff compares only VALUE measures, records trigger/ceiling decisions prospectively, and never treats ASSURANCE/TRACE/non-value DERIVED volume as a delivery overrun.
- [ ] RF binds full Candidate SHA, actual VALUE membership/class/reason, additions, deletions, touched LOC, trigger disposition, deviations, and the pre-work decision reference.
- [ ] EV requires exactly one dedicated accounting row using the TS method and status vocabulary; it does not become a selector, manifest, ledger, or second total.
- [ ] ONB can raise a blocking question but is not an accounting authority. Candidate precedes EV/RF/final state, and later excluded-only writes do not move it.

Gate: `python -m pytest docs/scripts/test_runtime_context.py -q -k "vbsa and (handoff or rf or ev)"`
Evidence: At the Candidate, run the Executor-side accounting row and record test result, commit ordering, and RF/EV agreement.

### AC-6: Independent Reviewer adjudication [depends: AC-5]

The Reviewer independently reruns the exact approved contract and can detect classification, arithmetic, reference, timing, and authority disagreement without inventing a replacement total or retroactive permission.

- [ ] Review workflow and REVIEW template reuse the same Baseline, Candidate, selector, metrics, and method; discrepancies name the accounting AC and affect the verdict through existing routes.
- [ ] `BLOCKED`, metric-only `N/A`, `INVALID` phase attribution, and non-terminal `DEFERRED` behavior are distinct and explicit.
- [ ] Reviewer verifies prospective decision timing and immutable denominator, but cannot supply missing Coordinator/Owner authority after work.
- [ ] RF/REVIEW appends do not move Candidate or invalidate a correct result.

Gate: `python -m pytest docs/scripts/test_runtime_context.py -q -k "vbsa and review"`
Evidence: Independently rerun the exact accounting command at the bound Candidate and record agreement/discrepancy in the phase EV and REVIEW §2.

### AC-7: Structural proof and adapter parity [depends: AC-3] [depends: AC-4] [depends: AC-5] [depends: AC-6]

Source-derived tests must prove behavior, mutation sensitivity, historical tolerance, clean-receiver preservation, and exact installed copy parity without changing the adapter manifest.

- [ ] Fixtures cover trace-only growth, assurance-only growth, test-as-product, a deliverable inside a task folder, a generated final deliverable, a true VALUE overrun, mixed-role whole-file treatment, rename identity, and binary/non-text LOC `N/A`.
- [ ] A deliberate semantic mutant in each classification/accounting/authority/migration family changes produced output before independent comparison rejects it; expected records cannot feed production execution.
- [ ] All six changed canonical workflows exactly match their twelve tracked `.agent`/`.claude` copies; clean receivers consume the same rules; `.tfw/adapters/manifest.yaml` is byte-identical to Baseline.
- [ ] Old approved TS examples remain readable, while new template/config writes are strict under the new schema; no historical task is modified.
- [ ] Targeted tests, the full configured suite, and `gen_index.py --check project` pass.

Gate: `python -m pytest .tfw/scripts/ docs/scripts/ -q` and `python .tfw/scripts/gen_index.py --check project`
Evidence: Record targeted/full-suite exit status, adapter parity, manifest Baseline equality, protected-path census, and project check in the phase EV.

### AC-8: Phase A publishes and obeys its own accounting [depends: AC-7]

This phase must be the first complete consumer of the new contract, not merely prose describing it.

- [ ] RF publishes actual changed VALUE membership against the exact 29-row planned selector and explains every membership deviation.
- [ ] RF and the single EV accounting row bind Baseline `f5a96af07dcdc4230ecf31100bd155a3dca09604`, the first valid Executor Candidate, logical files, additions, deletions, touched text LOC, the 50/5000 trigger disposition, and the 2× authority result.
- [ ] The owner-approved 29-file/1,100-LOC denominator stays unchanged; any prospective ruling is timestamped before work and any performed unapproved change is reported only as a deviation.
- [ ] Candidate contains no protected HC-1 change. Later RF/EV/REVIEW/status/journal additions are TRACE and do not change the reported delivery result.

Gate: Apply the exact §4 reproduction method and HC-1 selector to the bound Candidate; independently repeat in `/tfw-review`.
Evidence: Exactly one EV accounting row with resolving Git refs, selector source, arithmetic, trigger/authority disposition, timing check, and `VERIFIED` only on exact agreement; otherwise `BLOCKED`.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-a__value_bearing_budget_contract_and_adoption.md` | Required structured evidence with per-AC rows and exactly one dedicated VBSA accounting row |

No additional maintained evidence file is planned. Command output may be recorded inline in EV; transient logs/fixtures remain non-value `DERIVED` and untracked.

## 6. Technical Guidance

- Governing decisions: master HL §§3–7 and amendments A7–A10; research iter2 D15–D21 and carrier-removal result D18; D73–D75 for selective reads, source-derived tests, and manifest topology.
- Preserve the current workflow Read Contracts. Any newly required runtime read must state a named checkpoint purpose and must not create another source of truth.
- `.tfw/conventions.md` remains the semantic authority; `.tfw/glossary.md` is a term router, configuration carries project-owned values, templates own forms, and `.tfw/adapters/manifest.yaml` remains tooling-only copy/check metadata.
- The release-number choice remains `/tfw-release`. The Phase A result may describe a selected major-boundary gate but must keep changelog content under `[Unreleased]` and leave VERSION unchanged.
- Apply P2 F43 and the Saint-Exupéry Principle to every carrier: retain each site only for its distinct writer/reader job, while never deleting a site whose removal breaks purpose, architecture, inspectability, or continuation.
- Process facts F32/F37/F38 require contemporary command output, fixed reference revisions, and pre-act enforcement; do not type final counts from an earlier working-tree run.
- Canonical workflows are sources. After modifying one of the six declared workflows, update only its corresponding tracked `.agent` and `.claude` copies and prove byte equality; do not edit the manifest without a topology change.

## 7. Definition of Failure

- ❌ Any required TFW trace, ordinary assurance artifact, or non-value derived output spends the delivery budget or changes an already correct fixed-Candidate result.
- ❌ Any path/class/extension shortcut hides necessary VALUE, or a freehand hunk subtraction, double-counted phase path, fifth class, alternate-metric registry, shadow budget, or competing total appears.
- ❌ Config keeps an old key live, loses a receiver's project-owned file/LOC values, silently reinterprets an approved TS/history, or assigns a release number outside `/tfw-release`.
- ❌ A decomposition trigger becomes a quality veto; a local hard constraint lacks any M1–M6 fact; the Coordinator ratchets the denominator, crosses `>=2x`, changes a protected boundary, or approves after work.
- ❌ RF, EV, and REVIEW use different refs/selectors/metrics/commands, accept a missing/mutable/mismatched/late fact, or misuse `N/A`/`DEFERRED`/`INVALID`.
- ❌ The Saint-Exupéry Principle becomes deletion/LOC minimization/forced consolidation, or init/update injects this project's North Star wording into another project's North Star.
- ❌ A canonical workflow and tracked copy differ, D75 selective-read architecture regresses, `.tfw/adapters/manifest.yaml` changes without topology evidence, or an extra accounting carrier/script is created.
- ❌ Any HC-1 protected path changes, including closed RCFR traces, another historical task, master HL/RES, `.agents/**`, root/localized README, VERSION, or existing migration history.

**On failure:** stop before the affected work, record the exact failed criterion and state, and return to the Coordinator or Owner according to the existing authority boundary. Do not repair a semantic failure by raising a number.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Old hard-limit language survives in an unscanned live carrier | Add a live-surface census plus deliberate mutant; allow occurrences only in history, migration explanation, and old immutable tasks |
| Parsing a NUL-safe Git rename record is implemented inconsistently | Canonical metric definition plus source-derived rename/binary fixtures; Executor and Reviewer reuse the same raw method |
| Approval epoch becomes mutable install-state inference | Resolve the approved TS lineage and introducing release; never decide old semantics from current config alone |
| Version-agnostic migration is mistaken for permission to skip a versioned major guide | RELEASE gate blocks any selected major release until the corresponding `.tfw/migrations/{major}.0.0.md` exists and carries the complete mapping |
| Soft triggers become ceremony | TS, RF, EV, REVIEW each carry the same terminal decomposition disposition and tests fail on omission or `DEFERRED` |
| Planned LOC estimate is gamed as a target | Treat 1,100 only as immutable authority denominator; acceptance is semantic/structural, not proximity to estimate |
| Self-hosted fixtures pass while foreign project behavior fails | Clean-receiver tests preserve customized old values and a foreign North Star byte-for-byte |

## 9. Cross-Phase Modifications

No cross-phase modifications. The frozen master HL defines only Phase A and requires all canonical, workflow, template, adapter, verification, and update implications to ship together.

---

*TS — TFW_20260904-113200_VBSA / Phase A: Value-bearing budget contract and adoption | 2026-09-04*
