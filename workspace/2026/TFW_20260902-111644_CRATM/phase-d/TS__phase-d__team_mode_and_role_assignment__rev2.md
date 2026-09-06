# TS — TFW_20260902-111644_CRATM / Phase D: Team mode and Role Assignment, revision 2

> **Date**: 2026-09-06
> **Author**: Codex (Phase D Coordinator, acting as `saubakirov`)
> **Status**: 🟡 TS_DRAFT — Awaiting exact Main approval
> **Parent HL**: [Master HL, owner-approved A7](../HL-TFW_20260902-111644_CRATM.md)
> **A7 freeze**: `2386bfb0994f6e0a1aed7b734e345cdb2a540ae1`
> **Review return**: [REVIEW revision 2](REVIEW__phase-d__team_mode_and_role_assignment__rev2.md)
> **Superseded execution order**: [original approved TS](TS__phase-d__team_mode_and_role_assignment.md) — immutable history, not authority for the replacement Candidate

---

## 1. Objective

Replace Phase D's rejected one-principal-per-role model with the owner-approved A7 contract: one
selected stable LEAD principal holds a bounded autonomous mandate, while distinct, directly
addressable Coordinator, Researcher, Executor and Reviewer working units operate beneath it without
personal profiles. Preserve actual unit parentage, work, and proposal origin independently from
shared principal attribution; keep separate review and human accountability; and resolve the supplied-
versus-additional provider-profile admission contradiction without inventing G8 evidence.

## 2. Scope

### Lineage and live-state reconciliation

- The original Phase D TS was approved at `6a7ede0549dca272c149b0294a972c013d5cb291`.
  Candidate `9edbebcf68872a72a9274765ad053e8d25fa66ac` was reviewed APPROVE, documented, and
  moved `KNW → DONE`; the closure and its outcome correction really occurred and remain immutable.
- REVIEW revision 2 at `fbed31b128cc0f21ac630d512a748041310d636c` later changed the current
  verdict to `REVISE` for a material admission contradiction. Owner-approved A7 then superseded the
  delivered delegation model and froze at `2386bfb0994f6e0a1aed7b734e345cdb2a540ae1`.
- The historical DONE event is not false history, but it no longer establishes completion of A7's
  prospective contract. Main therefore authorised one case-specific reconciliation: this revision is
  created, live Phase D state is aligned to `TS_DRAFT`, terminal-only `outcome` is removed, and one
  phase-local `amendment_escalated` event references this TS, REVIEW rev2, and the old DONE event.
- This is not a `DONE → TS_DRAFT` lifecycle transition. The current graph has no such edge. That
  general lifecycle-contract gap is recorded, not repaired: no invented `transition`, intermediate
  RF/REV, graph change, validator change, new event kind, or general reopen rule is permitted.

### In Scope

- Rewrite `conventions.md` HL Contract rule 8 and its AT section so a selected LEAD principal and an
  actual working unit are different facts. The human-rooted unit chain controls routing; principal
  attribution never collapses nodes or gives a child the LEAD's amendment grant.
- Preserve the originating `{principal, unit}` proposal through forwarding, transcription, restart,
  and continuation. A genuinely subordinate-origin proposal may be ruled by the selected LEAD's root
  Coordinator unit only when its immutable grant and mandate cover the claim. A LEAD-origin,
  owner-reserved, missing-origin, ambiguous-origin, or out-of-grant proposal returns to the human.
- Separate protected mandate selection from ordinary unit instantiation. After approved committed HL,
  the owner chooses manual work or AT; AT requires an existing stable `team/` LEAD, bounded scope,
  role coverage/reach, reservations, and autonomy boundary. Initial creation and continuation of
  working units inside that bound is dispatch/role trace, not a personal profile or amendment. An
  unavailable assigned role holder still returns through owner-approved §12 `SUPERSEDE` before any
  substitute is created. Widening the mandate,
  replacing the selected principal, removing a control, or crossing a reserved boundary keeps the
  applicable explicit ruling.
- Replace the HL template's one-table, one-profile-per-row form with two visibly different layers:
  a frozen selected-LEAD mandate and an append-only/dynamic working-unit assignment. Unit rows record
  workflow role, actual native address, parent unit, bounded scope, direct channel, `Autonomous from`,
  and dispatch reference. The full unit roster is not a pre-freeze prerequisite.
- Tighten the Phase B profile template only where A7 changes its consumption: a profile is a stable
  principal, never a working unit; `may_rule_amendments: true` makes only the selected LEAD/root ruling
  unit eligible inside the approved mandate, not every child sharing its attribution.
- Tighten the Phase B journal event template for `dispatch`: `writer` remains optional principal
  attribution, while the existing body/summary and refs preserve actual source and destination units,
  parent, workflow role/scope, and originating proposer or explicit `none`. No key or carrier is added.
- Update Plan, Handoff, Review, and Research checkpoints to resolve mandate and unit separately,
  restate both in the owning HL/ONB/REVIEW/Briefing/RES trace, preserve proposal origin, return directly,
  and re-evaluate status, gate, dispatch, parent, address and scope before starts and continuations.
- Synchronize the eight accepted `.agent`/`.claude` workflow copies and the Codex managed root block.
  The Codex profile selects one user-visible LEAD task and lets that LEAD create distinct directly
  addressable role tasks, with separate worktrees for mutating roles and the same Executor/Reviewer on
  returns. Forks, subagents, relays, hidden helpers and provider switches cannot hold long-lived units.
- Correct profile admission as one combined decision: the supplied initial Codex profile is admitted
  with disclosed G1–G7 mechanics and no G8 reliability claim; every additional provider profile must
  pass G1–G8 together in one native TFW trial; partial receipts never compose.
- Adapt only the two existing repository ASSURANCE modules. Prove source-derived principal/unit,
  mandate/instantiation, routing/origin, provider admission, accepted-copy, protected-history,
  candidate-epoch, VALUE, and A5 attention behavior with output-changing mutants.

### Out of Scope

- A new stable principal, per-role/session profile, binding, roster, liveness file, runtime, bridge,
  orchestrator, spawner, daemon, scheduler, lock, authentication claim, event key, artifact class,
  config key, branch policy, transport, permission model, or TFW worktree implementation.
- A Claude or mixed long-lived profile, new native provider trial, G8/reliability claim, or admission
  from documentation, translated operations, relay topology, separate partial receipts, or this task's
  operational history. Mixed fresh runs remain bounded helpers that return to the role holder.
- Rewriting Phase A–C RF/REVIEW/EV, the original D TS/REVIEW/Candidate, any old journal event, D82,
  master amendment history, release 2.2.0, VERSION, CHANGELOG, migrations, glossary, topic facts, or
  Phase E's eleven-site/F11/release sweep. Existing D ONB/RF/EV content is preserved cumulatively and
  may receive only the legal numbered revision-round append required by Handoff.
- General lifecycle reopening, `gen_index.py` repair, payment of the two terminal `not material — owed
  and forbidden to pay` observations, a new Reviewer, a new Executor, release, tag, push, or integration
  into saved-project master.

## 3. Principles Check

| # | Master HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Human authority, bounded delegation and accountability | AC-1, AC-2, HC-D1 | Explicit owner mode/LEAD choice; seven returns; human-rooted mandate |
| P2 | A mandate is a ceiling | AC-1, AC-3, HC-D2 | Instantiation stays inside approved coverage; widening returns before work |
| P3 | Every initiation edge starts at a Coordinator unit | AC-2, AC-4 | Parent/child records reject Executor sources, ancestors, cycles and competing parents |
| P4 | Every chain terminates at a human | AC-1, AC-2 | Selected LEAD resolves to accountable owner; missing root fails closed |
| P5 | Authority is carried by the principal name, not distributed by attribution | AC-2, AC-3 | Only selected LEAD/root ruling unit may consume the immutable grant |
| P6–P7 | Roles are context; permissions remain per Role Lock | AC-3, AC-4 | Working-unit rows and titles grant nothing; role checks remain unchanged |
| P8–P9 | Git owns mechanism; nothing executable | AC-4, HC-D3 | Provider operations remain adapter-local; only Markdown product changes |
| P10 | A session is not an independent person | AC-2, AC-5 | Unit addressability is operational evidence, never personal identity or reliability |
| P11 | Autonomy boundary is declared | AC-1, AC-3 | Selected mandate and each unit carry exact gate/boundary; state tokens alone grant nothing |
| P12 | Isolation is not a lock | AC-4, AC-6 | Worktrees, direct routing, mutation ownership and landing remain separate checks |

## 4. Affected Files and Value-Bearing Accounting

### Literal VALUE selector and cumulative Baseline forecast

| File | Action | Class | Planned + | Planned − | Semantic reason / required result |
|---|---|---:|---:|---:|---|
| `.tfw/conventions.md` | MODIFY | `VALUE` | 70 | 20 | Rule 8, mandate granularity, AT entry/duties/returns/degradation, two-tier admission |
| `.tfw/templates/HL.md` | MODIFY | `VALUE` | 28 | 10 | Frozen selected-LEAD mandate separated from bounded unit instantiation |
| `.tfw/templates/team/profile.md` | MODIFY | `VALUE` | 8 | 4 | Principal is not a unit; child attribution does not inherit the LEAD grant |
| `.tfw/templates/journal/event.md` | MODIFY | `VALUE` | 8 | 2 | Dispatch body/refs preserve actual units, parent, scope/role and proposer origin |
| `.tfw/workflows/plan.md` | MODIFY | `VALUE` | 25 | 55 | Post-freeze mode/mandate choice, unit dispatch, rule-8 routing and refusal |
| `.tfw/workflows/handoff.md` | MODIFY | `VALUE` | 10 | 18 | Executor consumes principal plus actual unit/parent/scope without inherited grant |
| `.tfw/workflows/review.md` | MODIFY | `VALUE` | 10 | 12 | Independent Reviewer unit preserves origin and returns decisions directly |
| `.tfw/workflows/research/base.md` | MODIFY | `VALUE` | 10 | 52 | Researcher unit consumes bounded mandate and preserves proposal origin |
| `.tfw/adapters/codex/AGENTS.md.template` | MODIFY | `VALUE` | 8 | 9 | One selected LEAD creates direct role tasks; supplied G1–G7 limitation |
| `AGENTS.md` | MODIFY | `VALUE` | 8 | 9 | Exact managed-block receiver; project-local bytes outside markers preserved |
| `.agent/workflows/tfw-plan.md` | MODIFY | `VALUE` | 25 | 55 | Exact accepted Plan copy |
| `.agent/workflows/tfw-handoff.md` | MODIFY | `VALUE` | 10 | 18 | Exact accepted Handoff copy |
| `.agent/workflows/tfw-review.md` | MODIFY | `VALUE` | 10 | 12 | Exact accepted Review copy |
| `.agent/workflows/tfw-research.md` | MODIFY | `VALUE` | 10 | 52 | Exact accepted Research copy |
| `.claude/commands/tfw-plan.md` | MODIFY | `VALUE` | 25 | 55 | Exact accepted Plan copy, not a Claude team profile |
| `.claude/commands/tfw-handoff.md` | MODIFY | `VALUE` | 10 | 18 | Exact accepted Handoff copy, not a Claude team profile |
| `.claude/commands/tfw-review.md` | MODIFY | `VALUE` | 10 | 12 | Exact accepted Review copy, not a Claude team profile |
| `.claude/commands/tfw-research.md` | MODIFY | `VALUE` | 10 | 52 | Exact accepted Research copy, not a Claude team profile |
| **Total** | **18 MODIFY** | **`VALUE`** | **295** | **465** | **760 touched text LOC** |

The eight workflow copies are necessary constituents because this repository accepts them as live
receivers. The profile and event templates are necessary B carriers: leaving either unchanged makes
the same principal-level grant or writer field ambiguously stand for every working unit. The binding
template is not selected because it already says that a binding selects attribution, grants nothing,
and cannot make a session/workflow role/per-run profile into a principal.

### Declared excluded selectors

| File / selector | Action | Class | Treatment |
|---|---|---|---|
| `docs/scripts/test_runtime_context.py` | MODIFY | `ASSURANCE` | Independent parsers, behavioral matrices, required cases and output-changing mutants; no product authority |
| `docs/scripts/test_integration.py` | MODIFY | `ASSURANCE` | Exact selector/copies/managed block, two-epoch history protection, provider census and closure-visible KNOWLEDGE check |
| Current derivative Phase HL, Phase D TS/status/journal and later ONB/EV/RF/REVIEW/review paths | CREATE/MODIFY | `TRACE` | Refresh A7 derivation before approval; then required reconciliation, approval, execution, evidence and review history; excluded from Candidate movement |
| `.tfw/templates/bindings.yaml` | NONE | `VALUE` protected/excluded | Existing attribution-only/no-grant/no-per-run semantics already satisfy A7; blob must match approval epoch |
| Master HL, A–C and old D artifacts/events, `KNOWLEDGE.md`, `knowledge/`, release and Phase E surfaces | NONE | `TRACE` or prior `VALUE` protected/excluded | Match the revised approval epoch; no retroactive rewrite or premature E work |
| In-memory fixtures and temporary reports | CREATE/DELETE | `DERIVED` | Untracked; EV stores reproducible inputs/outputs, not a new product carrier |

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | The eighteen literal VALUE paths above, in that order; no glob, line exclusion, or narrower selector |
| Baseline / selector source | Product Baseline `8e68ab37d300122ff110500ad58f354f76b6210f`; selector derived from A7 freeze `2386bfb0994f6e0a1aed7b734e345cdb2a540ae1`, REVIEW rev2, live source/copy census, Phase B carriers and Phase C rule-8 consumers; this TS at the later exact approval commit |
| Candidate rule | First tested Executor commit containing all required VALUE and authorised ASSURANCE, descendant of the exact revised-TS approval epoch, before EV/RF/REVIEW/final transition; excluded-only later writes do not move it; later VALUE requires replacement and recomputation |
| Logical VALUE files | `18`; all existing modified text paths; rename = one |
| Touched text LOC | `295` additions + `465` deletions = `760`; prospective cumulative Baseline→replacement-Candidate forecast; numeric numstat fields; binary/non-text N/A |
| Triggers / disposition | Configured prompts `50` files / `5,000` LOC. Keep one phase: rule 8, AT, role form, dispatch provenance, four consumers, accepted copies and one supplied provider profile are one authority path; splitting leaves an admitted mode whose origin or receiver contradicts it. Two test modules remain ASSURANCE |
| Multiplier / authority | Historical approved denominator `16/640` remains immutable. Revised forecast is `18/760`, a prospective `+2/+120` comparison, below the historical owner thresholds `32/1,280`; it does not ratchet those thresholds. Main must approve both new selector members and the complete revised plan before work. Later growth is ruled prospectively against `16/640`; at/above either threshold, from planned zero, or outside the selector returns to owner |
| Approval epoch / failure | `PENDING — Main Coordinator`: approve this exact TS revision content, 18-path selector, 295+465=760 forecast, HC-D1–HC-D4, A5 treatment, and lineage reconciliation at its Git planning commit. Missing/mutable/mismatched/late facts = `BLOCKED`; metric-only N/A; unresolved phase attribution = `INVALID`; `DEFERRED` is non-terminal |

The forecast is a comparison point, not a ceiling or consumption target. The old `16/640` plan and
actual `16/603` Candidate remain immutable historical facts. A replacement Candidate is always
recomputed from the same product Baseline, while implementation-only change control is additionally
checked from the exact revised-TS approval commit.

```powershell
$valuePaths = @(
  '.tfw/conventions.md',
  '.tfw/templates/HL.md',
  '.tfw/templates/team/profile.md',
  '.tfw/templates/journal/event.md',
  '.tfw/workflows/plan.md',
  '.tfw/workflows/handoff.md',
  '.tfw/workflows/review.md',
  '.tfw/workflows/research/base.md',
  '.tfw/adapters/codex/AGENTS.md.template',
  'AGENTS.md',
  '.agent/workflows/tfw-plan.md',
  '.agent/workflows/tfw-handoff.md',
  '.agent/workflows/tfw-review.md',
  '.agent/workflows/tfw-research.md',
  '.claude/commands/tfw-plan.md',
  '.claude/commands/tfw-handoff.md',
  '.claude/commands/tfw-review.md',
  '.claude/commands/tfw-research.md'
)
$baselineSha = '8e68ab37d300122ff110500ad58f354f76b6210f'
if ($candidateSha -notmatch '^[0-9a-f]{40}$') { throw 'Candidate must be the full immutable Executor SHA' }
git diff --name-status --find-renames=50% -z $baselineSha $candidateSha -- $valuePaths
git diff --numstat --find-renames=50% -z $baselineSha $candidateSha -- $valuePaths
```

### Prospective scope rulings

1. **A7 correction and two B carriers — pending exact Main approval.** Cause: the frozen owner model
   distinguishes one principal from subordinate units, while the delivered form equates every role
   row with a participant handle and current rule 8 routes by handles. Cost: two VALUE members beyond
   the historical selector and a cumulative 760-LOC forecast. Assurance: combined routing/admission
   matrices, two-epoch integration protection, copy parity and full suite. Split rejected: changing
   canon/workflows without profile/event semantics leaves grant inheritance or origin loss at the
   dispatch boundary. Saint-Exupéry check: binding changes, new fields, new artifacts, new profiles,
   generic reopen machinery and Phase E were removed. Authority: below `32/1,280`, but exact new
   members require prospective Main ruling before their first edit.
2. **A5 attention treatment — pending exact Main approval.** At A7, active runtime is
   `32,946/33,749`; central range `33/260`; routes are Plan `24,724/24,725`, Research focused
   `6,080/6,102`, Research deep `6,145/6,167`, Handoff `6,363/6,366`, Review `24,934/24,954`,
   Resume `3,196/3,264`, Docs `15,266/15,278`, Init `4,515/4,529`. Canonical words are conventions
   `11,714`, HL `2,176`, profile `371`, event `353`, Plan `1,894`, Handoff `2,014`, Review `2,094`,
   Research `1,150`, Codex adapter `161`. Meaning and addressed enforcement sites cannot fit in Plan's
   one-word or Handoff's three-word headroom by a bare pointer. Rejected shorter form: renaming old
   participant rows to units without separate mandate/provenance/admission decisions; it preserves the
   contradiction. Executor must use substitution and local compaction first, but A5 permits the
   minimum necessary growth. Do not silently raise old cap literals or delete semantics to turn a
   diagnostic green; EV records exact before/after, any crossing, necessity and the smallest rejected
   form. Assurance may replace an obsolete hard-pass expectation only with that explicit measured A5
   record; the historical RTPSN result and literals remain preserved.

### Task-local hard constraints

| ID / M1 consequence | M2 object/risk | M3 measure/selector | M4 pre-act check | M5 softer-control gap | M6 change authority |
|---|---|---|---|---|---|
| HC-D1 — Child can rule LEAD-origin work | Proposal origin laundering | `{principal, unit}`, parent path, signer, reservation | Resolve from dispatch and role traces before verdict | Shared `writer` cannot distinguish units | Owner/A7; no local widening |
| HC-D2 — Mode activates from a roster or token | Mandate/instantiation collapse | Two HL layers plus exact gate/dispatch | Owner choice, committed HL, scope/reach and gate all resolve | Prose-only role list can look authorised | Main within A7; owner if boundary widens |
| HC-D3 — Supplied profile is rejected or G8 invented | Admission contradiction | Combined supplied/additional decision matrix | Evaluate canon and adapter together | Separate string checks both pass | Main within A7; provider expansion to owner |
| HC-D4 — Current trace rewrites history | Case-specific state reconciliation | Exact old DONE event plus new non-transition event | Validate status/event current forms before write | Ordinary transition graph has no reopen edge | Main's explicit reconciliation only |

**Actions (not budget dimensions):** 18 VALUE modifications; 2 ASSURANCE modifications; one Phase HL
refresh, one new TS, one status correction, one phase event and later ordinary ONB/EV/RF/REVIEW TRACE; zero new product,
runtime, state, config, event-key, provider-profile or Phase E paths.
**Immutable owner-approved denominator:** historical `16` VALUE files / `640` touched LOC; never ratchets.

## 5. Acceptance Criteria

### AC-1: AT entry and the selected mandate are explicit

- [ ] Canon defines AT only after an owner-approved committed HL plus an explicit human selection of
  one existing stable agent principal as LEAD and a bounded mandate covering scope, roles/reach,
  reservations, direct reporting and `Autonomous from`. A draft roster, profile, binding, title,
  status token, `writer`, or provider grants nothing.
- [ ] The owner may choose manual work or AT after HL approval, normally after research. No choice
  preserves CL and separately explicit AG. A full named unit roster is neither an HL-freeze condition
  nor a substitute for the owner act.
- [ ] The Coordinator/LEAD owes scope, Role Locks, direct routes, durable state, same-role continuity,
  unit provenance and seven exact owner returns. Every unit owes its assigned role/scope, gate checks,
  direct reports and no cross-workflow execution. Human accountability remains ultimate.
- [ ] Degradation is observable stop/wait or already-authorised non-AT work. No relay, hidden helper,
  silent replacement, provider switch, weakened trace or fabricated profile is used.

Gate: source-derived contract parser and scenario matrix cover manual, ordinary AG, incomplete AT,
post-HL selected AT, missing principal/mandate/approval, roster-only, boundary/gate failure, seven
returns and degradation; each declaration/duty/return mutant changes output before rejection.

Evidence: EV preserves exact source spans, inputs, expected/actual decisions, seven channels and exits.

### AC-2: Principal, working unit and proposal origin remain distinct [depends: AC-1]

- [ ] One selected LEAD principal may attribute several distinct units, but every dispatch records one
  actual source, destination and parent unit, role/scope, direct address/channel and governing refs.
  Identical principal `writer` values never merge those nodes.
- [ ] Every child has one validated human-rooted parent; only Coordinator units create children.
  Executor sources, ancestors, task-Coordinator targets, cycles, repeated/competing parents, foreign
  scope, missing address and unresolved roots refuse before work.
- [ ] Proposal origin is the original principal and unit. Forwarding, transcription, restart,
  continuation, new writer or same LEAD attribution cannot replace it.
- [ ] Positive case: an eligible selected LEAD/root Coordinator rules a genuinely subordinate-origin,
  non-reserved proposal inside its immutable grant and mandate. Negative cases: the same LEAD cannot
  rule its own/root-unit proposal; a child cannot consume the LEAD's grant; owner-reserved,
  missing/ambiguous-origin and out-of-grant proposals return to the human or remain blocked.

Gate: compose the revised rule-8 source with profile, journal, Plan and Review consumers into an
authority matrix. Output-changing mutants collapse writer into unit identity, inherit the grant,
change origin on forwarding/restart, erase parent, turn a child into signer, or make a LEAD-origin
proposal appear subordinate; every mutant is independently rejected.

Evidence: EV stores full principal/unit/proposal/signer records and every route/refusal decision.

### AC-3: Role Assignment separates mandate from instantiation [depends: AC-1] [depends: AC-2]

- [ ] The HL template places one Role Assignment before Phase Dependencies and renders two layers:
  selected-LEAD mandate commitments and actual working-unit assignments. Their fields and mutation
  rules are unambiguous; sample content uses one principal across distinct units.
- [ ] Mandate selection is a protected human act. Widened scope/role coverage/reach/autonomy, principal
  replacement, removed control/reservation, or unavailable LEAD uses the applicable explicit ruling;
  dropping a control is never `RESTRICT`.
- [ ] Initial creation and continuation of a directly addressable unit inside the approved mandate is
  append-only/dynamic instantiation and dispatch, not a new principal/profile or HL amendment. An
  unavailable selected LEAD or assigned role holder returns through §12 `SUPERSEDE` to the owner and
  waits; a Coordinator's same-principal/same-scope replacement dispatch is not owner approval.
- [ ] Composed negative case: unavailable assigned holder + same principal + same scope + replacement
  dispatch alone yields `WAIT_FOR_OWNER`. Only an actual owner-approved `SUPERSEDE` followed by a
  bounded replacement dispatch may yield `PROCEED_REPLACEMENT`.
- [ ] Each unit row carries workflow role, actual unit, parent, bounded scope, direct channel,
  `Autonomous from`, and dispatch ref. Lifecycle state is resolved non-ordinally against the same
  task/phase path and exact gate; `—`, missing approval, foreign/ambiguous history or wrong unit waits.
- [ ] Profile and event templates preserve the split with no new key. Bindings remain byte-identical
  to the approval epoch because their existing no-grant/no-unit semantics are already correct.

Gate: parse/render both tables and execute mandate-versus-instantiation cases for initial selection,
in-bound child creation/continuation, unavailable-holder replacement with and without owner-approved
`SUPERSEDE`, widening, removed control, earlier/later boundary, `—`, foreign unit and missing gate.
Mutants merge the layers, demand per-role profiles, pre-freeze the roster, inherit grants, treat a
replacement dispatch as approval, omit event provenance or call widening ordinary instantiation.

Evidence: EV records rendered tables, event projection, cases and independent mutant rejections.

### AC-4: Four workflows, copies and Codex operations enforce the same model [depends: AC-3]

- [ ] Plan asks manual/AT after approved committed HL, validates the selected mandate, creates only
  bounded child units, records dispatch provenance, applies revised rule 8, and never executes another
  workflow. Handoff, Research and Review resolve their actual unit before first work and continuation.
- [ ] ONB/Briefing/RES/REVIEW restate selected principal, actual unit, parent, role/scope, direct
  channel, boundary, dispatch source and proposal origin where present. Questions, gates, RF, RES,
  verdict and proposals return directly. The same Executor and independent Reviewer are reused.
- [ ] All eight workflow copies are byte-identical to canon. The Codex managed receiver matches its
  template and preserves every byte outside markers.
- [ ] Codex uses one user-visible selected LEAD task which creates distinct user-visible directly
  addressable role tasks; mutating units use separate worktrees and direct create/send/wait operations.
  No subagent, fork, relay, hidden helper, provider switch or new task/profile is substituted on return.
- [ ] Provider/API terms remain adapter-local; Role Locks, selective reads, REVISE authority, Purpose
  routing, Candidate timing, worktree isolation, exact-path landing and human returns do not weaken.

Gate: source-derived workflow/adapter records, exact byte parity and managed-block comparison; cases
cover start, continuation, return and correction. Mutants move checks after work, drop parent/origin,
relay a return, replace a role unit, weaken a Role Lock or substitute a disallowed holder.

Evidence: EV records exact existing Phase D task IDs/worktrees/direct receipts and role continuity as
mechanics evidence only; product authority comes from A7 and the approved TS.

### AC-5: Supplied and additional profile admission compose correctly [depends: AC-1] [depends: AC-4]

- [ ] All eight provider-neutral gates remain defined. The initial supplied Codex profile is admitted
  only as the explicit first-release exception with G1–G7 mechanics disclosed and no G8 reliability
  rate or cross-provider claim.
- [ ] Every additional provider profile is rejected unless one provider-native TFW unit passes all
  G1–G8 in one trial. Missing any gate, documentation, a translated test, Helpdesk relay, separate
  demonstrations or partial receipts cannot compose into admission.
- [ ] Assurance evaluates the combined canon plus adapter result. Positive case:
  `ADMIT_SUPPLIED_LIMITED`. Negative case: additional profile without native G8 (or any gate) is
  `REJECT_NO_NATIVE_ALL_EIGHT`. A complete native additional run is the only additional-admit case.
- [ ] The universal-gate mutant changes the supplied positive result and is rejected. The forbidden
  partial-receipt-composition mutant changes the additional negative result and is rejected. Heading
  presence or separate limitation checks alone are insufficient.

Gate: one independent admission oracle consumes source-derived canon and adapter projections, runs
the three cases plus each missing gate, and proves both required mutants change output before reject.

Evidence: EV stores full admission inputs/outputs, native-evidence provenance and mutation results.

### AC-6: Replacement Candidate, history and attention are reproducible [depends: AC-2] [depends: AC-3] [depends: AC-4] [depends: AC-5]

- [ ] Exact Main approval fixes this TS content and 18/760 prospective plan before handoff. Candidate
  is the first tested Executor commit after that epoch; NUL-safe replay from immutable Baseline returns
  exactly 18 VALUE members and numeric additions/deletions. Any variance is reported and ruled before
  further VALUE work; no result ratchets 16/640.
- [ ] A second approval-epoch diff admits only the 18 VALUE paths, two ASSURANCE paths and legal Phase
  D continuation TRACE. Blob-for-blob protection applies to `KNOWLEDGE.md`, master A7, A–C, original
  D TS/REVIEW and review stages, every pre-approval journal event, release 2.2.0, bindings, the refreshed
  Phase HL, approved TS rev2 and REVIEW rev2, and Phase E surfaces. The closure-visible KNOWLEDGE
  assertion is checked at this epoch, not incorrectly against the pre-D product Baseline.
- [ ] ONB, RF and EV are cumulative exceptions: their complete approval-epoch content remains present
  and only a numbered revision-round section is appended at Handoff's legal stage; no prior answer,
  claim or evidence row is edited or deleted. A new REVIEW uses its required revision sibling rather
  than altering REVIEW rev2.
- [ ] Original approval/DONE/correction history remains readable. Before approval, the live TS may
  receive only its legitimate approval record; the refreshed Phase HL and Coordinator-ruled REVIEW
  rev2 are then frozen as execution inputs. Live reconciliation uses only the authorised status
  correction and one non-transition `amendment_escalated` event.
- [ ] Exact before/after document, route, central-range and active-corpus counts are recorded. A5 uses
  minimum substitution/compaction without semantic loss. Any old comparator crossing is explicit and
  evidenced; cap literals are not silently raised and a historical test is not weakened to an
  unmeasured pass.
- [ ] Targeted current-form, Phase B/C/D, copy/provider, protected-history, scenario and mutant checks;
  `git diff --check`; configured full suite; and real MkDocs build pass. Git status is clean after each
  exact-path commit. Candidate stays reachable. No push, release, tag or saved-master integration.

Gate: literal PowerShell selector; independent numstat parser; Baseline and approval-epoch membership
queries; object/blob comparisons; status/event validation; word/route reports; tests and build.

Evidence: one EV accounting row plus raw decoded records reproduces membership, arithmetic, ancestry,
timing, history protection, A5 disposition, commands and exits.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-d__team_mode_and_role_assignment.md` | Revised per-AC evidence, matrices/mutants, native receipts, two-epoch history checks, A5 and VALUE accounting |

## 6. Technical Guidance

- Treat `{principal, unit}` as the minimum authority identity. A principal provides durable
  attribution/accountability; a unit provides operational role, address, parent and proposal origin.
  Never derive either half from the other.
- Keep Role Assignment in the existing HL section, with two tables or equally explicit sub-blocks.
  Protected mandate mutations and dynamic in-bound unit rows must have visibly different instructions.
- Use the existing dispatch event body and refs for unit details. Do not add frontmatter keys. Use
  compact labeled lines if the 120-code-point summary cannot carry the record.
- Replace obsolete participant-row wording rather than adding a parallel explanation. Keep canonical
  workflow actions self-contained; a reference may add precision but not hide the action/refusal.
- Derive copy targets from the live manifest and accepted topology, but modify only the eight literal
  receivers in the selector. Do not start the broader Phase E sweep.
- Implement admission as a decision over evidence class plus profile class. The supplied exception is
  narrow and named; it does not weaken the all-eight rule for later profiles.

## 7. Definition of Failure

- ❌ A LEAD principal and one of its working units are treated as the same dispatch node, or identical
  `writer` values erase actual source/destination, parent, work or proposer origin.
- ❌ A child inherits `may_rule_amendments`, a LEAD rules its own proposal after forwarding/restart, an
  origin is guessed, or a genuinely subordinate proposal cannot reach an otherwise eligible LEAD.
- ❌ AT begins from a profile, roster, draft, state token or table alone; the full unit roster is
  required before HL freeze; or ordinary in-bound instantiation silently widens mandate/control.
- ❌ A per-role/session profile, runtime, roster, key, carrier, provider trial, bridge, relay, hidden
  helper or Phase E/release change is added.
- ❌ Canon rejects the supplied limited profile, admits an incomplete additional profile, composes
  partial evidence, or claims G8/reliability that was not observed.
- ❌ Any old TS/RF/REVIEW/EV/status snapshot/journal/release is rewritten, or the case-specific live
  reconciliation is presented as a legal `DONE → TS_DRAFT` transition or a general new rule.
- ❌ The selector, immutable Baseline, historical 16/640 denominator, revised 18/760 plan, approval
  epoch or Candidate is missing/mutable/late; a new member or deviation is approved retrospectively.
- ❌ An old attention cap is silently raised, an assertion is deleted for convenience, or required
  meaning is cut to fit a diagnostic comparator.

**On failure:** stop before the violating act. Technical/selector gaps return to this Phase
Coordinator; mandate/principal/reservation, provider expansion, owner-threshold or lifecycle-policy
changes return through Main to the human owner. Do not repair with silent widening or replacement.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Shared principal attribution launders proposal origin | Source-derived `{principal, unit}` records plus forwarding/restart mutants |
| Dynamic units make frozen mandate porous | Separate tables and explicit widening-versus-instantiation matrix |
| Two B templates turn Phase D into a retroactive rewrite | Change only forward consumption; protect old artifacts and binding blob at approval epoch |
| Admission exception becomes a universal waiver | Combined oracle names exactly one supplied limited class; every additional class keeps all-eight |
| Historical DONE obscures the new live contract | Explicit lineage, non-transition reconciliation event and two-epoch checks |
| Correct enforcement exceeds legacy attention comparators | A5 minimum-growth record with exact counts; no silent cap edit or semantic deletion |
| Closure-visible KNOWLEDGE causes a false integration failure | Protect it from revised approval epoch while VALUE still measures from product Baseline |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| `.tfw/conventions.md` | A–C, future E | Revise C rule 8 and D AT prospectively; preserve historical RF/REVIEW and defer only the real E sweep |
| `.tfw/templates/team/profile.md` | B | Clarify grant consumption without changing the compatible schema or old profiles |
| `.tfw/templates/journal/event.md` | B | Clarify dispatch body/ref semantics; no key change and no event rewrite |
| Current derivative Phase HL and `.tfw/templates/HL.md` | C/D | Refresh live A7/TS derivation before approval; then protect it while replacing only the product template's obsolete Role Assignment model |
| Four canonical workflows and eight copies | A/C/D, future E | Make principal/unit/origin checks coherent while preserving Role Locks and exact receiver parity |
| Codex adapter/root managed block | D, future E | Supply one-LEAD/direct-unit operations and limited admission; no new profile or Phase E sweep |
| `docs/scripts/test_{runtime_context,integration}.py` | RCFR, RDP, VBSA, RTPSN, A–C/D | Extend independent assurance; distinguish product Baseline from revised approval/history epoch |
| `KNOWLEDGE.md` §§1–3 | A–D docs history | Protected during Candidate; `/tfw-docs` may update only after new APPROVE |

> References use compilable-contract patterns (`D31`, `D43`, `D54`, `D59`, `D63`, `D72–D82`,
> `knowledge/process.md` F30/F39–F41, `knowledge/stakeholder.md` F6/F7/F14,
> `knowledge/environment.md` F6, A7).

---

*TS — TFW_20260902-111644_CRATM / Phase D: Team mode and Role Assignment, revision 2 | 2026-09-06*
