# TS — TFW_20260902-111644_CRATM / Phase B: Named principals

> **Date**: 2026-09-05
> **Author**: Phase Coordinator (Codex)
> **Status**: 🟡 TS_DRAFT — approval gate not open; external validation retirement must land first
> **Parent HL**: [HL-TFW_20260902-111644_CRATM](../HL-TFW_20260902-111644_CRATM.md) — `🔒 FROZEN`
> **Phase HL**: [HL__phase-b__named_principals](HL__phase-b__named_principals.md) — derivation-only
> **Planning base**: `eef020bb5c00901c09f5def262b930e70975ae12` — not the execution Baseline

> **Executable boundary:** do not approve this TS, freeze its VALUE denominator, create an Executor,
> or start `/tfw-handoff` while the current validator rejects `writer`. After the external retirement
> lands, the Coordinator re-reads Phase B state, proves the succeeding validation path accepts the
> carrier, selects the immutable Baseline, recomputes the forecast, inserts the complete denominator,
> and asks the owner to approve the TS and denominator in one act.

---

## 1. Objective

Make a project able to name stable human and agent principals in profiles, bindings, and new journal
events while preserving human accountability and the immutable legacy event corpus. Organization and
project roles remain descriptive; optional mentality remains separate from the two-level amendment
grant. Phase C routing and Phase D team mode receive a compatible identity substrate, not rules from
their phases.

## 2. Scope

### In Scope

- Extend the Full profile template with optional `organization_role` and `project_role`, explicit
  absence semantics, agent `accountable_to`, Boolean `may_rule_amendments`, and optional `mentality`.
- Define a principal as a stable project handle, never a provider/model/process/session. An agent
  principal must name an existing human and one of exactly two grant levels.
- Make the grant-bearing identity durable: changing `may_rule_amendments` requires a new principal
  handle/profile; the old principal's grant is never redefined.
- Add optional `writer` to the current event schema. It names a declared principal; `on_behalf_of`
  remains the accountable human, `via` remains tool text, and the filename token remains uniqueness.
- Keep legacy `actor` readable and untouched. No legacy event or four-key profile is rewritten.
- Let the existing one-job, per-machine binding select a declared human or agent principal without
  granting authority or recording liveness.
- Update only the four canonical Markdown owners and prove them against the post-retirement
  validation path after the dependency lands.

### Out of Scope

- Editing, testing, replacing, or inspecting the retiring validator; adding any code, hook, daemon,
  lock, registry, config key, executable helper, or new artifact class.
- Authority routing, proposal recipients, initiation-chain traversal, amendment verdict format, or
  any Phase C rule.
- Team mode, Role Assignment, autonomous-from semantics, provider profiles/routes, or Phase D gates.
- Glossary, adapters, workflows, version, changelog, the complete TFW-54 sweep, or any Phase E work.
- Full↔Assisted schema convergence, provider/model/session fields, a profile per run, authentication,
  permissions, or a live roster.
- Changes to Phase A clauses, master lifecycle/HL, Phase C–E, another task, or external machine state.

## 3. Principles Check

| # | HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Human authority, bounded delegation | AC-2, AC-5 | Agent principal has accountable human and explicit grant; owner approves immutable denominator |
| P2 | A mandate is a ceiling | AC-2, HC-B1 | Mentality/roles grant nothing; exact path boundary cannot widen itself |
| P3 | Every initiation edge starts at a coordinator | N/A | Phase C; this TS creates no edge or routing rule |
| P4 | Every chain terminates at a human | AC-2 | Every agent principal must name an existing human profile |
| P5 | Authority is carried by the name | AC-2 | One stable principal per grant level; grant changes require a new name |
| P6 | A role is context, never permission | AC-1, AC-2 | Organization/project roles and mentality are explicitly non-authoritative |
| P7 | Permissions are per role | AC-2, AC-5 | Principal fields do not alter any workflow Role Lock |
| P8 | Git owns mechanism, TFW protocol | N/A | Phase A delivered it; Phase B preserves those clauses |
| P9 | Nothing executable | AC-5, HC-B1 | Four Markdown VALUE paths only; external validator is untouched |
| P10 | A separate session is not an independent person | AC-2, AC-4 | Session/provider cannot be a principal or binding inference |
| P11 | Autonomy boundary is declared | N/A | Phase D; no mode or lifecycle switch here |
| P12 | Isolation is not a lock | N/A | Phase A; no lock/liveness behavior added |

## 4. Affected Files and Value-Bearing Accounting

The four exact rows are the complete planned product selector. All are `VALUE`: each is accepted
framework behavior or a necessary constituent of the named-principal schema.

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `.tfw/conventions.md` | MODIFY | `VALUE` | Canonical profile/principal, event-writer, and binding semantics in §4; Phase A clauses preserved |
| `.tfw/templates/team/profile.md` | MODIFY | `VALUE` | Compatible human/agent schema, accountability, grant, mentality, examples |
| `.tfw/templates/journal/event.md` | MODIFY | `VALUE` | Current optional `writer` and orthogonal legacy/accountability/tool/token meanings |
| `.tfw/templates/bindings.yaml` | MODIFY | `VALUE` | One project mapping may select any declared principal and still grants nothing |

### Declared excluded selectors

| Selector | Class | Treatment |
|---|---|---|
| Exact Phase B HL/TS/status/journal plus future ONB/RF/REVIEW/evidence/review paths below `phase-b/` | `TRACE` | Required lifecycle and evidence; never spends delivery measures |
| Temporary compatibility fixtures and command output | `DERIVED` | Reproducible, untracked, and removed after evidence capture |
| Existing repository tests/checks run without modification | `ASSURANCE` | Verification input only; no changed assurance path is planned |

No listed file admits hunk subtraction. If VALUE and another role become inseparable inside a listed
path, the whole fixed Baseline→Candidate file diff is VALUE.

### Prospective accounting contract — pending dependency readiness

| Fact | Current draft value / approval requirement |
|---|---|
| Subject / exact VALUE selector | The four literal paths above; fixed in this draft |
| Baseline / selector source | **UNSET by gate.** Select the first immutable main commit after the external retirement lands and its validation path accepts `writer`; `eef020b…` is planning evidence only |
| Candidate rule | First tested Executor commit with all required VALUE and any authorised ASSURANCE, before EV/RF/REVIEW/final transition; excluded-only later writes do not move it; later VALUE requires replacement and recomputation |
| Logical VALUE files | Working forecast `4`; recompute and freeze with the Baseline before approval |
| Touched text LOC | Working forecast `175` additions + `65` deletions = `240`; recompute from the post-dependency sources before approval; binary/non-text N/A |
| Triggers / disposition | Configured prompts are `50` files and `5,000` LOC. Expected disposition: keep one phase; four schema owners are one coherent capability and splitting them leaves an unusable identity path |
| Multiplier / authority | **No immutable denominator exists yet and therefore no growth authority exists.** After owner approval, owner ruling is required at ≥2× either approved measure, from planned zero, or for HC-B1 change; below it Coordinator authority remains prospective and bounded |
| Approval epoch / failure | Gate opens only after dependency proof + Baseline + recomputed denominator. Missing/mutable/mismatched/late facts = `BLOCKED`; metric-only N/A; unresolved phase attribution = `INVALID`; `DEFERRED` is non-terminal |

```powershell
$valuePaths = @(
  '.tfw/conventions.md',
  '.tfw/templates/team/profile.md',
  '.tfw/templates/journal/event.md',
  '.tfw/templates/bindings.yaml'
)
git diff --name-status --find-renames=50% -z $baselineSha $candidateSha -- $valuePaths
git diff --numstat --find-renames=50% -z $baselineSha $candidateSha -- $valuePaths
```

`$baselineSha` is set only by the readiness gate. `$candidateSha` is set only by the Candidate rule.
Neither is guessed, typed from planning base, or backfilled after evidence.

### Prospective scope rulings

The external retirement is a dependency, not Phase B scope. It gives no permission to edit its task
or carrier. No Phase B scope ruling exists at draft time. After approval, an additional VALUE path or
higher forecast requires a prospective ruling with cause, cost, assurance, split alternative,
Saint-Exupéry judgment, authority, verdict, timestamp, and reference; completed work is only a
deviation.

### Task-local hard constraint — HC-B1

| M1 consequence | M2 object/risk | M3 measure/selector | M4 pre-act check | M5 softer-control gap | M6 change authority |
|---|---|---|---|---|---|
| Phase B can silently revive a retiring executable, route authority early, mutate legacy history, or merge edition schemas | Every path outside the four VALUE rows and authorised Phase B TRACE; especially validator/tests, workflows, adapters, glossary, master/other phases/tasks, legacy events, and external binding state | Zero Baseline→Candidate changes outside the four VALUE paths; zero edits to existing team profiles/events | Compare full intended and actual path sets before every write and Candidate; verify dependency proof before Baseline selection; stop on first mismatch | File/LOC prompts cannot detect one small forbidden architecture/history mutation | Owner `saubakirov` prospectively; Coordinator multiplier authority cannot relax HC-B1 |

**Actions (not budget dimensions):** 4 modified VALUE files, 0 planned ASSURANCE files, required TRACE
only. **Immutable owner-approved denominator:** not yet established; execution remains blocked.

## 5. Acceptance Criteria

### AC-1: Compatible role context

- [ ] `organization_role` and `project_role` are optional for both profile types and accept a
  non-empty description or exact `not_applicable`.
- [ ] Omitted means unknown/not supplied; it does not assert that the role is absent.
- [ ] Every existing four-key profile remains valid without edit, and roles are explicitly context,
  never authentication, permission, task scope, or workflow role.

Gate: compare the canonical schema/table/examples; run the succeeding validation path over the
unchanged `team/saubakirov.md` and temporary human profiles covering omitted and `not_applicable`.
Evidence: EV captures the post-retirement command, fixture inputs, and results.

### AC-2: Accountable agent principal and two stable grant levels [depends: AC-1]

- [ ] `type: agent` requires `accountable_to` naming an existing `type: human` profile and Boolean
  `may_rule_amendments` equal to `true` or `false`.
- [ ] Provider, model, executable, process, session, and workflow role cannot define principal identity.
- [ ] `mentality` is optional non-empty descriptive guidance and cannot imply authority, change a
  Role Lock, or alter participant permissions.
- [ ] Two agent profiles demonstrate one principal per grant level. Changing the grant requires a
  new handle/profile; an already used principal is never redefined.
- [ ] No routing or verdict-recipient algorithm is introduced.

Gate: inspect canonical rules and run temporary profile fixtures for valid ruler/non-ruler, missing
human, agent-accountable-to-agent, invalid grant, and mentality-without-authority cases.
Evidence: EV records exact fixtures/results and a static search proving no workflow permission depends
on profile fields.

### AC-3: New writer composes with immutable legacy events [depends: AC-2]

- [ ] A current event may carry `writer`, which names a declared human handle or a valid agent
  principal; `on_behalf_of` remains a declared human and `via` remains non-empty free-form tool text.
- [ ] `writer` is not derived from `via`, OS/account identity, hostname, model, session, folder, or
  filename token. The token retains uniqueness alone.
- [ ] Legacy `actor` is accepted exactly as already written and is never required, issued, validated
  under the new principal rules, removed, or rewritten.
- [ ] The post-retirement validation path accepts a synthetic current `writer` event and the existing
  legacy corpus together; no old event changes and no check fails because of this phase.

Gate: after dependency readiness, validate one current human-writer event, one agent-writer event,
one actor-only legacy event, and the unchanged project corpus; search the Candidate for legacy-event
modifications.
Evidence: EV captures command/output, fixture payloads, legacy corpus result, and zero modified legacy
paths. Any live rejection is `BLOCKED`, never `DEFERRED`.

### AC-4: Binding selects a principal and grants nothing [depends: AC-2]

- [ ] One project-root mapping may select a declared human or valid agent principal.
- [ ] One profile still resolves silently; several still use the per-machine file; invalid/missing/
  copied/shared binding still triggers exactly one short identity question.
- [ ] Binding contents remain one mapping per project and nothing else. No authority, mentality,
  fallback, default, liveness, device identifier, provider data, or project-local copy appears.
- [ ] Identity is never inferred, and no real external binding is created or overwritten by evidence.

Gate: inspect canonical example and use a temporary external-path fixture against the succeeding
reader; verify the real `%LOCALAPPDATA%`/POSIX locations are untouched.
Evidence: EV records fixture location, mappings/results, cleanup, and no real external mutation.

### AC-5: Boundaries, compatibility, and attention contract hold [depends: AC-1] [depends: AC-3] [depends: AC-4]

- [ ] Candidate changes only the four VALUE paths and Phase B TRACE; Phase A worktree/staging/landing
  clauses remain semantically intact.
- [ ] No code/config/test modification, runtime, registry, provider-specific identity, Role Assignment,
  authority routing, team mode, glossary/version sweep, Assisted convergence, or legacy rewrite lands.
- [ ] Phase B removes stale future-TFW-54 wording only where the four owned passages must explain the
  shipped principal; Phase E retains the complete remaining sweep/audit.
- [ ] Exact before/after word counts exist for all four VALUE files. The three templates remain below
  ~1200 words; any `conventions.md` growth from 10,179 words is the minimum necessary because one
  canonical profile/principal contract must be visible to the identity checkpoint, and a template-only
  copy would leave binding/event semantics without shared authority.
- [ ] Existing repository checks and the post-retirement validation path pass without modifying an
  excluded assurance path.

Gate: inspect full Candidate path/diff, run diff check and repository checks, compare Phase A clauses,
search changed lines for prohibited concepts, and record exact word deltas/shorter-form judgment.
Evidence: EV records path set, checks, semantic comparison, counts, and exclusions.

### AC-6: Value-bearing accounting is reproducible [depends: AC-5]

- [ ] Before approval, the dependency result, full Baseline SHA, TS approval commit, literal selector,
  and immutable planned file/LOC denominator are present and consistent.
- [ ] Candidate is the first tested Executor VALUE commit and precedes EV, RF, REVIEW, and RF state.
- [ ] NUL-safe commands reproduce membership, additions, deletions, touched LOC, trigger disposition,
  authority, and timing in one EV row; later VALUE creates a replacement Candidate and recomputation.
- [ ] Missing dependency proof, Baseline, denominator, approval, immutable Candidate, or matching replay
  yields `BLOCKED` and no handoff/review progression.

Gate: run both §4 commands with full SHAs and literal array; compare one EV accounting row and later
independent REVIEW replay.
Evidence: `evidence/EV__phase-b__named_principals.md` records the complete immutable chain.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-b__named_principals.md` | Per-AC compatibility fixtures, dependency proof, word counts, changed-path boundary, and accounting replay |

## 6. Technical Guidance

- Prefer one concise `conventions.md` subsection for the complete principal/profile semantics and
  short template-specific instructions. Do not duplicate the whole rule in three templates.
- Use `writer`, not `actor`, for current events. The separate word pays for unambiguous semantics:
  six immutable legacy events already use `actor`, including tool values. Keep `actor` historical.
- Treat the grant as Boolean data on an immutable principal identity: `true` and `false` are the two
  levels; a grant change creates a new handle. Phase C may consume that fact but owns all routing.
- Keep role values descriptive strings plus `not_applicable`; omitted remains unknown. Do not import
  Assisted labels or its binding schema.
- Use temporary fixtures outside tracked paths and never modify the real per-machine binding.

## 7. Definition of Failure

- ❌ The external retirement is not landed/verified, yet Baseline, denominator, approval, or Executor exists.
- ❌ An existing four-key profile or legacy event needs an edit, or a new writer fails the succeeding validation path.
- ❌ An agent principal lacks an existing accountable human, or provider/model/session becomes identity.
- ❌ Mentality/role implies authority, the grant has more than two levels, or an old principal's grant changes.
- ❌ Binding grants authority, records liveness, gains another key kind, moves into the project, or is inferred.
- ❌ Candidate touches outside the four VALUE paths/TRACE or enters Phase C–E, Assisted, code, tests, runtime, or registry scope.
- ❌ Accounting lacks immutable dependency/Baseline/approval/Candidate facts or cannot be reproduced.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Planning base is mistaken for execution Baseline | Header and AC-6 keep Baseline unset until dependency proof |
| `writer` is accepted in prose but rejected in practice | Binary pre-execution fixture; rejection is BLOCKED |
| Mutable profile rewrites authority history | One grant per stable principal; changed grant creates a new handle |
| Optional mentality becomes a permission backdoor | Separate field and negative AC; no workflow permission consumer |
| Phase B absorbs routing/team/sweep work | Four literal VALUE paths plus HC-B1 and AC-5 searches |
| Conventions grows unnecessarily | One canonical body, exact counts, rejected shorter form, A5 minimum-necessity evidence |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| `.tfw/conventions.md` | Phases A, C, D | Preserve Phase A §4; Phase B owns identity/profile/binding semantics; C/D add separate routing/mode rules |
| `.tfw/templates/team/profile.md` | Phase E audit | Phase B owns the schema; Phase E may sweep stale references but not redefine it |
| `.tfw/templates/journal/event.md` | Phase D, E audit | Phase B owns `writer`; Phase D may specify `dispatch` usage without changing identity meanings |
| `.tfw/templates/bindings.yaml` | Phase E audit | Phase B owns principal selection; no later phase may turn it into authority or runtime state |

---

*TS — TFW_20260902-111644_CRATM / Phase B: Named principals | 2026-09-05*
