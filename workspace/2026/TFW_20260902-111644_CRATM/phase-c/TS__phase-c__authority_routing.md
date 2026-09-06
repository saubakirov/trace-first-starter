# TS — TFW_20260902-111644_CRATM / Phase C: Authority routing

> **Date**: 2026-09-06
> **Author**: Phase Coordinator (Codex, acting as `saubakirov`)
> **Status**: ✅ APPROVED — Main Coordinator under the user's standing mandate, 2026-09-06; immutable denominator 12 VALUE files / 320 touched LOC (200 additions + 120 deletions)
> **Parent HL**: [HL-TFW_20260902-111644_CRATM](../HL-TFW_20260902-111644_CRATM.md) — `🔒 FROZEN`
> **Phase HL**: [HL__phase-c__authority_routing](HL__phase-c__authority_routing.md) — derivation-only
> **Planning and execution Baseline**: `fb08c120a91aca4c9ceaea859d46dd49c032afd0`

> **Approval boundary:** Main Coordinator approved planning content
> `95eb2ab510ed8d89205ed5fe498ccb061c112888`, this TS, the twelve literal VALUE paths, the cascade
> ruling, HC-C1/C2, and the 12/320 denominator before `/tfw-handoff`. The approval commit is recovered
> from Git path history after the act; its SHA is never typed into its own content. Planning now stops
> and routes exactly one separate Executor task.

---

## 1. Objective

Make Phase B's stable two-level principal grant operational for frozen-HL amendments. A proposal
travels upward through a human-rooted, child-only Coordinator chain to the nearest authorized
principal that is not its proposer, while owner-reserved claims, self-grant changes, Purpose Check
contract defects/not-fit results, and `❌ REJECT` remain human decisions. Every current owner-only
consumer changes coherently; no runtime, registry, new artifact class, or Phase D/E behavior appears.

## 2. Scope

### In Scope

- Define one canonical initiation-edge and ruler-resolution contract in `conventions.md` §3. The
  human root and terminal human ruler are the declared human `owner` in the governing task/phase
  `status.md`; a separate governing record proves that owner's authorization of the root Coordinator.
  `accountable_to` remains profile accountability and cannot grant or prove this prefix. A
  `dispatch` edge combines the initiating event `writer`, named destination, and referenced governing
  scope; it indexes existing role evidence and creates no transcript or registry.
- Admit a new edge only from a Coordinator already on one unambiguous human-rooted prefix to a child
  not on that prefix. Refuse Executor initiation, ancestor/back edges, ambiguous/missing parents, and
  chains that do not resolve to a human before work starts.
- Preserve the originating proposer principal through Coordinator transcription. Compare principal
  handles, not sessions: a fresh session holding the same handle cannot rule its own proposal.
- Resolve ordinary `EXTEND`/`SUPERSEDE` proposals to the first upward principal whose immutable grant
  is `true` and whose handle differs from the proposer; skip `false` and self; otherwise use the
  governing `status.md` owner. Never derive the human address from `accountable_to`.
- Keep human exceptions explicit: owner-reserved claim, agent self-grant/change-of-handle, Purpose
  Check contract defect/not-fit, `❌ REJECT`, budget authority, and malformed chain. Keep `RESTRICT`
  filing semantics and the existing direct owner-initiated amendment record only for a real explicit
  human decision, never an agent's `on_behalf_of`, human binding, or accountability link.
- Keep ordinary CL backward compatibility: no declared delegated chain means the existing direct
  owner-only route. Refuse when delegated authority is claimed but its prefix is unproved,
  ambiguous, or contradictory; do not classify absence of delegation as corruption.
- Rewrite the Rung-3 route, Plan iteration/revision gates, Handoff entry gate, and HL/RES template
  language to consume the canonical resolver without creating competing algorithms.
- Synchronize the six accepted singular `.agent` and `.claude` copies of the three changed workflows
  in the same Candidate. Adapt two existing repository-only assurance modules to derive the new
  authority outputs and reject contradiction mutants.
- Preserve Phase A/B, RCFR D73–D75, VBSA D76, D77, D79, and D80; enforce unchanged attention/corpus
  ceilings at Candidate and after the coordinator's post-review `/tfw-docs` closure.

### Out of Scope

- Phase D Role Assignment, third mode, Autonomous-from field, provider routes/profiles, full dispatch
  semantic envelope, or delegation obligations; Phase E glossary, version, changelog, F11 correction,
  eleven-site TFW-54 sweep, and complete adapter resynchronization.
- A new executable carrier, resolver script, validator file, hook, daemon, scheduler, lock, registry,
  liveness state, config key, product file, artifact class, runtime permission, authentication claim,
  transport, or branch/merge policy.
- Any change to principal/profile/event/binding schema or meanings; grant levels; existing profiles,
  events, bindings, phase artifacts, master frozen claims, Assisted, sealed `tasks/`, or external state.
- Adding plural `.agents/workflows` files or repairing `.tfw/adapters/manifest.yaml`; the accepted
  singular-copy discrepancy stays visible for the Phase E audit.
- Silently raising, deleting, bypassing, or rebaselining `SESSION_ROUTE_CEILINGS`, active-corpus
  limits, per-workflow caps, Phase A/B tests, or the report-only RDP diagnostic. No cap change is
  currently planned or authorized; demonstrated minimum necessary growth must stop before the edit
  and return exact before/forecast/delta plus the rejected shorter form for a prospective A5 ruling.

## 3. Principles Check

| # | Master HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Human authority, bounded delegation | AC-2, AC-3, HC-C2 | Explicit grant, exceptions, stop conditions, accountability, and escalation precede any verdict |
| P2 | A mandate is a ceiling | AC-2, HC-C1 | Resolver never manufactures authority; self-grant and scope widening return to owner |
| P3 | Every initiation edge starts at a coordinator | AC-1 | Role and backward-edge fixtures refuse every other source |
| P4 | Every chain terminates at a human | AC-1, AC-2 | Governing status owner and separate root authorization resolve before dispatch/verdict application |
| P5 | Authority is carried by the name | AC-2 | Immutable grant belongs to stable principal; signature names the resolved ruler |
| P6 | A role is context, never permission | AC-1, AC-5 | Coordinator is an initiation precondition, not a profile-derived grant or Role Lock rewrite |
| P7 | Permissions are per role | AC-3, AC-5 | No participant changes workflow permissions; only the declared grant resolves one amendment act |
| P8 | Git owns mechanism, TFW protocol | AC-4, AC-6 | Exact-path commits/copies/Candidate remain Phase A protocol; no new mechanism |
| P9 | Nothing executable | AC-4, AC-5, HC-C1 | Markdown VALUE only; existing repository tests are ASSURANCE, never shipped runtime authority |
| P10 | Separate session is not independent person | AC-2 | Self-approval compares stable principal handle across session changes |
| P11 | Autonomy boundary is declared | N/A | Phase D; no mode, Role Assignment, or lifecycle switch here |
| P12 | Isolation is not a lock | AC-5 | Phase A worktrees remain index isolation only |

## 4. Affected Files and Value-Bearing Accounting

### Literal VALUE paths

| File | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `.tfw/conventions.md` | MODIFY | `VALUE` | Sole authority algorithm, Rung-3 consumer, human exceptions, and Phase C prohibitions |
| `.tfw/workflows/plan.md` | MODIFY | `VALUE` | Preserve proposer, resolve/rout verdict, and stop at the resolved ruler |
| `.tfw/workflows/review.md` | MODIFY | `VALUE` | Keep Purpose/REJECT owner routes distinct while consuming shared Rung-3 authority |
| `.tfw/workflows/handoff.md` | MODIFY | `VALUE` | Refuse Rung-3 execution until the resolved ruler's terminal verdict exists |
| `.tfw/templates/HL.md` | MODIFY | `VALUE` | §12 records proposer origin, resolved ruler/signature, direct-owner act, and `RESTRICT` correctly |
| `.tfw/templates/RES.md` | MODIFY | `VALUE` | Researcher remains non-ruling; amendment proposals await the canonical route after transcription |
| `.agent/workflows/tfw-plan.md` | MODIFY | `VALUE` | Accepted byte-identical Plan copy |
| `.agent/workflows/tfw-review.md` | MODIFY | `VALUE` | Accepted byte-identical Review copy |
| `.agent/workflows/tfw-handoff.md` | MODIFY | `VALUE` | Accepted byte-identical Handoff copy |
| `.claude/commands/tfw-plan.md` | MODIFY | `VALUE` | Accepted byte-identical Plan copy |
| `.claude/commands/tfw-review.md` | MODIFY | `VALUE` | Accepted byte-identical Review copy |
| `.claude/commands/tfw-handoff.md` | MODIFY | `VALUE` | Accepted byte-identical Handoff copy |

### Declared excluded selectors

| File / selector | Action | Class | Treatment |
|---|---|---|---|
| `docs/scripts/test_runtime_context.py` | MODIFY | `ASSURANCE` | Replace affected P2/Rung-3 expected records; add source-derived authority matrix and contradiction mutants; no ceiling changes |
| `docs/scripts/test_integration.py` | MODIFY | `ASSURANCE` | Verify canonical/copy route parity and resolved-ruler hard stop; no product behavior |
| Exact Phase C HL/TS/status/journal plus later ONB/RF/REVIEW/evidence/review paths below `phase-c/` | CREATE/MODIFY | `TRACE` | Required lifecycle, decision, evidence, and review records; never spend delivery measures |
| Temporary in-memory authority payloads and command output | CREATE/DELETE | `DERIVED` | Fully reproduced in EV; never tracked or accepted independently |
| Post-review `KNOWLEDGE.md` §1–§3 documentation | MODIFY | `TRACE` | `/tfw-docs` decision/continuation record after APPROVE; does not move Candidate, but must keep final route/corpus caps green |

No VALUE row admits hunk subtraction. The whole Baseline→Candidate diff of every literal member is
VALUE; tests remain ASSURANCE only because the accepted product is the Markdown contract and copies.

### Prospective accounting contract — Main Coordinator approved

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | The twelve literal paths above, in that order; no glob and no narrower line selector |
| Baseline / selector source | `fb08c120a91aca4c9ceaea859d46dd49c032afd0`, read from Git on a clean detached worktree; selector is this TS at the later Git-created approval commit |
| Candidate rule | First tested Executor commit with all required VALUE and authorized ASSURANCE, before EV/RF/REVIEW/final transition; excluded-only later writes do not move it; later VALUE requires replacement and recomputation |
| Logical VALUE files | `12`; every row is an existing modified Markdown file; rename = one |
| Touched text LOC | `200` additions + `120` deletions = `320`; exact prospective comparison denominator, numeric numstat fields; binary/non-text N/A |
| Triggers / disposition | Configured prompts `50` files / `5,000` LOC. Keep one phase: the canonical algorithm, decision-site consumers, templates, and accepted copies are one inseparable authority path; a split ships contradictions. Two changed tests are assurance, not denominator members |
| Multiplier / authority | Immutable approved denominator `12/320`; owner threshold is `≥24` files or `≥640` touched LOC, or growth from planned zero. Main Coordinator approved this below-threshold technical bound under the user's standing task mandate; no ruling can change a frozen claim or HC-C1/C2 |
| Approval epoch / failure | `APPROVE — Main Coordinator`, 2026-09-06, explicitly approves unchanged planning content `95eb2ab510ed8d89205ed5fe498ccb061c112888`, cascade ruling, and denominator before handoff. Missing/mutable/mismatched/late = `BLOCKED`; metric-only N/A; unresolved phase attribution = `INVALID`; `DEFERRED` is non-terminal |

The 320 LOC is a comparison denominator, not a target. If the pre-work forecast grows but stays below
both multiplier limits, the Coordinator may authorize only a necessary constituent while Goal,
Value, outputs, AC, DoF, phase ownership, architecture, interfaces, data, security, trust, and
authority remain fixed. At or above either multiplier, from zero, or across HC-C1/C2, stop for owner.

```powershell
$valuePaths = @(
  '.tfw/conventions.md',
  '.tfw/workflows/plan.md',
  '.tfw/workflows/review.md',
  '.tfw/workflows/handoff.md',
  '.tfw/templates/HL.md',
  '.tfw/templates/RES.md',
  '.agent/workflows/tfw-plan.md',
  '.agent/workflows/tfw-review.md',
  '.agent/workflows/tfw-handoff.md',
  '.claude/commands/tfw-plan.md',
  '.claude/commands/tfw-review.md',
  '.claude/commands/tfw-handoff.md'
)
$baselineSha = 'fb08c120a91aca4c9ceaea859d46dd49c032afd0'
if ($candidateSha -notmatch '^[0-9a-f]{40}$') { throw 'Candidate must be the full immutable Executor SHA' }
git diff --name-status --find-renames=50% -z $baselineSha $candidateSha -- $valuePaths
git diff --numstat --find-renames=50% -z $baselineSha $candidateSha -- $valuePaths
```

`$candidateSha` is set only from Git by the Candidate rule. EV preserves these exact commands,
literal values, raw NUL-safe output decoding, arithmetic, and exit status.

### Prospective scope ruling — authority consumer cascade

The frozen master map names `conventions.md`, Plan, and Review, but later reviewed RCFR/RDP work left
live owner-only consumers in Handoff, HL/RES templates, accepted copies, and repository assurance.
They are necessary constituents under `HL Contract` rule 6: omitting any one leaves a contradictory
enforcement site and fails DoD 9–11/DoF 8. Cost is twelve VALUE modifications plus two ASSURANCE
modifications, forecast 320 VALUE LOC, no new path. Assurance is the full authority fixture/mutant
matrix, canonical/copy parity, prior suite, and exact attention accounting. Deferring copies to Phase
E, preserving old test literals, or placing the rule only in conventions were rejected because each
ships a false role route. Main Coordinator approved this below-multiplier refinement on 2026-09-06;
the ruling is terminal before work.

### Task-local hard constraints

| ID | M1 consequence | M2 object/risk | M3 measure / selector | M4 pre-act enforcement | M5 softer-control insufficiency | M6 change authority |
|---|---|---|---|---|---|---|
| HC-C1 | Phase C can smuggle Phase D/E, add a runtime, change identity semantics, or damage earlier reviewed contracts | Every path outside 12 VALUE + 2 ASSURANCE + authorized Phase C TRACE; master/Phase A/B; principal schema; D73–D80 semantic guarantees | Zero Candidate changes outside exact sets; zero changed forbidden heading/blob/key or prior semantic output; adapter copies equal canonical bytes | Compare intended path list before each write/commit; full status/cached-name inspection and `git commit --only`; semantic census before Candidate | File/LOC prompts cannot detect one tiny authority, runtime, identity, or phase-boundary breach | Owner `saubakirov`; Coordinator multiplier authority cannot relax HC-C1 |
| HC-C2 | A malformed chain or self-ruler can apply a frozen change irreversibly before anyone sees missing authority | Every §12 `EXTEND`/`SUPERSEDE` terminal verdict and every new initiation edge | Complete authority record must resolve governing `status.md.owner`, separate root authorization, proposer principal, child-only path, eligible non-proposer ruler, grant, reservation status, and signature; `accountable_to` is never root proof | Resolve and record authority before dispatch/verdict application/re-freeze; missing or competing claimed-chain fact = hard stop | Disclosure/review occurs after the frozen act and cannot undo a fabricated authority chain | Owner `saubakirov`; changing resolver semantics or an exception is a frozen-claim amendment |

**Actions (not budget dimensions):** 12 modified VALUE files, 2 modified ASSURANCE files, required
TRACE only. **Immutable approved denominator:** 12 VALUE files; 200 additions + 120
deletions = 320 touched text LOC; never ratchets.

## 5. Acceptance Criteria

### AC-1: Human-rooted child-only initiation chain

- [ ] The human root and terminal human ruler resolve only from the human `owner` in the governing
  task/phase `status.md`, plus a separate governing record authorizing the root Coordinator.
  `accountable_to` remains direct profile accountability and never proves authority or a dispatch root.
- [ ] One canonical rule defines a `dispatch` initiation edge from the event's stable `writer` to
  its named destination with references to governing scope/role evidence; it does not treat provider
  history, session title, binding, profile role, or a live roster as chain authority.
- [ ] Only a Coordinator already on one resolved human-rooted prefix may create a new child edge.
  Executor initiation, child→ancestor/task-Coordinator edge, repeated child, competing parent,
  missing provenance, and non-human termination are refused before work starts.
- [ ] Direct `accountable_to: <human>` remains Phase B identity/accountability; the initiation path
  does not create agent accountability chains, authentication, or participant-dependent Role Locks.
- [ ] A normal CL task with no declared delegated chain retains the direct owner-only route. A
  claimed delegated chain with no separate owner-authorized root is refused rather than derived from
  `accountable_to` or treated as CL.
- [ ] No runtime, registry, new event field, new file class, or Phase D Role Assignment is required.

Gate: extract the canonical rule and run full positive/negative chain fixtures. Required fixtures:
ordinary CL/no delegation→owner; root Coordinator→child; two-level child; Executor source; backward
ancestor; repeated/competing child; missing parent; unknown writer/destination; unassigned/non-human
status owner; profile names an `accountable_to` human but no separate owner-authorized prefix exists;
binding/title/provider/`accountable_to` substituted for provenance. Each fixture records status
owner, root authorization, all nodes, roles, stable handles, parent edges, and expected decision.

Evidence: EV contains the complete executable in-memory validator, every full fixture payload, exact
extraction/run command, raw output, exit status, and expected/actual parity. No reconstructed command
history or abbreviated payload is accepted.

### AC-2: Nearest authorized non-proposer resolves exactly once [depends: AC-1]

- [ ] The proposer is the principal that originated the frozen change. Coordinator transcription
  preserves that handle; `writer` of the transcription does not replace it.
- [ ] For ordinary `EXTEND`/`SUPERSEDE`, traversal skips `may_rule_amendments: false` and every node
  whose principal equals the proposer, selects the nearest remaining `true`, and otherwise selects
  the governing `status.md` owner. Principal equality survives session replacement or resumption;
  `accountable_to` is never a fallback ruler address.
- [ ] The §12 terminal verdict names the resolved ruler principal. Plan verifies chain, proposer,
  immutable grant, reservation, and signature before applying/re-freezing; unresolved authority
  stays `PROPOSED` and blocks execution.
- [ ] A grant change requires a new handle/profile exactly as Phase B states; neither routing nor a
  verdict mutates an existing grant.

Gate: full fixtures cover nearest true; false then higher true; no true→owner; proposer is nearest
true; proposer appears again in a fresh session; Coordinator transcribes a child proposal; unknown,
duplicate, or changed grant; mismatched verdict signer; two apparent roots. Mutants independently
alter proposer preservation, nearest order, grant polarity, handle equality, status-owner fallback,
and forbidden `accountable_to` fallback, and must change produced output before rejection.

Evidence: EV preserves the same complete validator/payloads plus selected ruler, refusal reason,
signature, and mutation results for every case.

### AC-3: Human exceptions and Role Locks stay distinct [depends: AC-2]

- [ ] Owner-reserved claim and an agent principal's own grant/change-of-handle route to the owner,
  never to a delegated ruler.
- [ ] `RESTRICT` continues to apply on filing with no synthetic verdict; an owner-initiated amendment
  remains the existing direct human act on one row only when a real explicit owner decision exists.
  `on_behalf_of`, a human binding, or `accountable_to` grants no human self-ruling exception.
- [ ] Review retains literal owner routing for Purpose Check `not fit for purpose`, contract defect,
  and `❌ REJECT`; only Rung-3 amendment authority changes.
- [ ] Reviewer still proposes and stops; Coordinator still accepts dispositions; Executor never
  initiates, resolves authority, rules, edits HL/TS, or accepts a pending amendment.
- [ ] Budget multiplier/zero, unavailable participant, reserved claim, and malformed-chain returns
  remain explicit; none is silently recast as delegated amendment authority.

Gate: parse source-derived records for each exception and role. Negative mutants replace Purpose or
REJECT owner routing, apply `RESTRICT` through a ruler, allow same-principal session laundering, or
let Executor resolve/dispatch; each must fail independently.

Evidence: EV records exact extracted clauses, full exception payloads, produced routes, mutations,
and exit status.

### AC-4: Every real consumer agrees with one authority [depends: AC-2] [depends: AC-3]

- [ ] A live-source census classifies every old owner-only occurrence as replaced amendment route,
  preserved human exception, historical changelog/knowledge, or unrelated budget/approval rule. No
  unclassified current enforcement site remains.
- [ ] Plan iteration/revision gates, Handoff Rung-3 entry, HL §12, and RES recommendation wording use
  the canonical resolved-ruler semantics without duplicating a different traversal algorithm.
- [ ] Review consumes the shared Rung table and preserves its human exceptions. `research/base.md`
  remains unchanged because the updated RES template is its already-declared output form.
- [ ] Each of six accepted tracked copies is byte-identical to its canonical Plan/Review/Handoff
  workflow at Candidate; no manifest, plural target, Codex wrapper, or Phase E copy is added/edited.
- [ ] Existing ASSURANCE derives authority matrix and Rung-3 output from canonical sources. Expected
  records cannot read their oracle; output-changing contradiction mutants are rejected.

Gate: repository census excluding historical task traces, canonical/copy blob and SHA-256 parity,
targeted authority tests, copy-consumer integration tests, and `git diff --check` on exact selectors.

Evidence: EV stores census command/raw classified output, parity hashes, targeted commands/results,
and the complete source-derived validator rather than only pass totals.

### AC-5: Frozen boundary, compatibility, and attention contract hold [depends: AC-1] [depends: AC-4]

- [ ] Candidate changes only 12 VALUE, 2 ASSURANCE, and Phase C TRACE paths. Phase A worktree/staging/
  landing, Phase B principal/writer/binding, RCFR D73–D75, VBSA D76, D77, D79, and D80 invariants pass
  their existing source-derived and full-suite checks.
- [ ] No Role Assignment/team mode/provider profile or route/autonomy field, Phase E sweep/glossary/
  release, runtime/config/artifact, Assisted/sealed-task edit, new file, or unruled cap change lands.
- [ ] Exact before/after word counts exist for all six canonical VALUE owners. `RES.md` remains at or
  below ~1200; inherited over-limit sources grow only by minimum necessary wording. The rejected
  shorter forms are rule-only-in-conventions, unsynchronized adapters, and unchanged false test text;
  each loses an enforcement or accepted consumer.
- [ ] The default bound leaves fixed route ceilings unchanged: Plan 24,725; Research focused 6,102; Research deep 6,167; Handoff
  6,366; Review 24,954; Resume 3,264; Docs 15,278; Init 4,529; active corpus 33,749. Candidate is at or
  below each without editing ceilings. Post-review `/tfw-docs` is also at or below Docs 15,278 and
  corpus 33,749; the Baseline values 15,264 and 33,228 leave only 14/521 words, so required D81/
  artifact documentation must use minimal substitution/compaction without dropping D73–D80 meaning.
- [ ] If measured minimum necessary wording or closure cannot meet a ceiling without semantic loss,
  execution stops before any ceiling edit and reports exact before/forecast/minimum delta, affected
  route/corpus, and the rejected shorter reference/substitution/cut to Main Coordinator. Only a
  prospective recorded A5 ruling can revise that technical bound; silent cap edits, test removal,
  semantic deletion, and retrospective rebaseline fail.
- [ ] Configured lint/tests, project structure, MkDocs build, Phase A/B authority/identity/accounting
  regressions, and adapter parity pass. The inherited RDP 123/120 report remains report-only,
  unchanged, and absent from user-facing closure.

Gate: run the source-derived runtime-context payload and compare every literal ceiling; inspect full
diff/cap constants; run targeted then full configured commands only after the verified surface changes;
repeat route/corpus accounting after `/tfw-docs` before `DONE`.

Evidence: EV records exact commands, raw per-route before/after/ceiling JSON, active-corpus totals,
per-file counts, test/build output, changed cap-line blobs, and shorter-form judgment.

### AC-6: Immutable accounting and lineage replay [depends: AC-5]

- [ ] Before handoff, Phase B actual RF/final REVIEW, full Baseline, literal selector, immutable 12/320
  denominator, Main approval, HC-C1/C2, and the prospective cascade ruling are present and consistent.
- [ ] Executor bootstraps on the exact Git-produced approval ref, confirms clean/correct HEAD, and
  fixes the first fully tested VALUE+ASSURANCE commit as Candidate before EV/RF/REVIEW/RF state.
- [ ] NUL-safe commands reproduce twelve VALUE members, numeric additions/deletions/touched LOC,
  trigger/split/authority decision, and timing in one EV row. Tests do not spend the denominator.
- [ ] Candidate remains immutable through evidence/review. Any later VALUE creates a replacement
  Candidate and full recomputation; missing/mismatched/late facts are `BLOCKED`, never reconstructed.
- [ ] The independent Reviewer replays accounting and ancestry from Git without receiving totals as
  authority. Exact-path staging and producer/role attribution remain visible in commit history.

Gate: compare approval ancestry before work; at Candidate run both §4 commands with full SHAs and
literal array; verify Candidate→tip VALUE diff/history, exact commit membership/subject, and independent
REVIEW replay.

Evidence: `evidence/EV__phase-c__authority_routing.md` records the complete immutable chain, raw NUL
decoding, arithmetic, command text/output, ancestry, membership, and no-later-VALUE proof.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-c__authority_routing.md` | Complete executable authority validator with all payloads; per-AC evidence; census/parity; route/corpus counts; test/build results; immutable accounting replay |

No detached evidence file is permitted merely to shorten EV. Large raw suite output may be indexed as
an attachment only if EV preserves the exact runnable command, exit status, decisive lines, attachment
hash, and every authority fixture/payload needed for independent replay.

## 6. Technical Guidance

- Keep one compact resolver contract in `HL Contract`; other sites should state their decision-edge
  inputs/outputs and refer to the sole owner rather than restate traversal.
- Treat profile accountability, root authorization, and child dispatch as three different facts.
  Governing `status.md.owner` supplies the human address, a separate record authorizes the root
  Coordinator, and only that Coordinator extends the child chain. “Coordinator-only” or
  `accountable_to` without child/ancestor provenance is insufficient.
- Preserve proposal origin as a stable principal handle. `writer` declares who transcribed an event;
  D59 forbids treating that attribution as proof/authentication, and it does not identify who
  proposed the frozen change by itself.
- Prefer substitutions and removal of superseded owner-only sentences over additive parallel rules.
  Do not delete a human exception to buy word budget.
- Modify repository-only tests only to verify the approved semantic change. Never add a runtime
  validator or make expected test data an authority source.
- Before the Candidate commit, inspect full status and cached names, stage/commit exact paths only,
  and obtain the commit SHA from Git. Preserve all full payloads and commands contemporaneously in EV.

## 7. Definition of Failure

- ❌ A chain can be initiated by a non-Coordinator, points to an ancestor, has competing/missing
  provenance, lacks a human governing owner or separate root authorization, derives authority from
  `accountable_to`, fails to terminate at the owner, or proceeds by fallback instead of refusal.
- ❌ An agent rules its own proposal through transcription or a new session, widens/changes its own
  grant, or a profile role/binding/title/provider grants permission.
- ❌ Owner-reserved/self-grant/Purpose/REJECT/budget/malformed-chain routes become ordinary delegated
  amendments, or the owner-initiated direct act is generalized into agent self-approval.
- ❌ Any current owner-only enforcement consumer survives unclassified, or one canonical/copy route
  contradicts another.
- ❌ A cap is raised/bypassed/rebased without a prospective recorded A5 ruling; RCFR/VBSA/Phase
  A/B/D79/D80 semantics or tests regress; evidence omits
  validator bytes, payloads, runnable commands, raw result, or honest history limits.
- ❌ Candidate touches an unapproved path, enters Phase D/E, adds executable/runtime/config/artifact
  surface, modifies external state, or lacks immutable approval/Baseline/Candidate/accounting lineage.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Frozen “cycles impossible” wording is implemented as role-only advice | AC-1 requires child-only prefix construction and backward/missing/ambiguous refusal fixtures |
| Proposer identity is overwritten by transcriber or session | Stable-handle origin and same-principal-two-session fixtures in AC-2 |
| Generic “authorized ruler” silently captures human-only decisions | Exhaustive AC-3 exception records retain exact governing-owner routes |
| Profile accountability is mistaken for human authority | AC-1 fixture has valid `accountable_to` but absent owner-authorized prefix and must refuse |
| Later RCFR/RDP consumers are omitted from the master-era map | Prospective cascade ruling plus live census and copy parity in AC-4 |
| Tests are preserved as a false oracle or become product runtime | Source-derived outputs/mutants in two existing ASSURANCE files; no new carrier |
| Post-review docs push the 14-word Docs slack over the current signal | AC-5 tries meaning-preserving substitution first, then stops before change with exact evidence for a prospective A5 ruling |
| Executor starts from saved checkout instead of approved planning line | Bootstrap exact HEAD/clean check and safe alignment to Git-produced approval ref before any write |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| `.tfw/conventions.md` | A, B, D | Preserve A worktrees/staging/landing and B principal semantics; C owns authority algorithm; D later adds mode/freeze granularity only |
| `.tfw/workflows/plan.md` | RCFR, D | Preserve ordered reads/Knowledge Gate; C changes amendment routing; D later declares Role Assignment before freeze |
| `.tfw/workflows/review.md` | A, RCFR/RDP, D | Preserve exact-path review, Purpose/REJECT owner routes, citation bar, and shared Rung authority; D later adds team reporting |
| `.tfw/workflows/handoff.md` | A, VBSA, D | Preserve exact-path Candidate/accounting; C changes only Rung-3 authority precondition; D later adds delegate obligations |
| `.tfw/templates/HL.md` | D | C owns §12 authority text; D later adds Role Assignment outside §12 |
| `.tfw/templates/RES.md` | RCFR | Preserve researcher Role Lock and classification; C changes only who receives a transcribed proposal |
| Six tracked workflow copies | A, E | Phase C syncs only changed accepted singular copies; Phase E retains complete adapter audit |
| Two assurance modules | RCFR, RDP, VBSA, RTPSN | Extend source-derived records without weakening prior oracle separation, mutations, or ceilings |

---

*TS — TFW_20260902-111644_CRATM / Phase C: Authority routing | 2026-09-06*
