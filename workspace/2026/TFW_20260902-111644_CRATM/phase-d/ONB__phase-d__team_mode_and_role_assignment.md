# ONB — TFW_20260902-111644_CRATM / Phase D: Team mode and Role Assignment

> **Date**: 2026-09-06
> **Author**: Codex Executor (acting as `saubakirov`)
> **Status**: 🟠 ONB — Bound accepted; AG authorization active
> **Parent HL**: [HL-TFW_20260902-111644_CRATM](../HL-TFW_20260902-111644_CRATM.md)
> **Phase HL**: [HL Phase D](HL__phase-d__team_mode_and_role_assignment.md)
> **TS**: [TS Phase D](TS__phase-d__team_mode_and_role_assignment.md)

---

## 1. Understanding

Implement the owner-approved Phase D contract on top of Baseline `8e68ab37d300122ff110500ad58f354f76b6210f`: add provider-neutral AT declaration, frozen six-column Role Assignment semantics, seven direct return channels, and real Plan/Research/Handoff/Review receive-and-report checkpoints; add only the Codex profile proven by RES; synchronize the eight accepted workflow copies; and extend the two assurance owners with source-derived scenarios, negatives, output-changing mutants, census, route/corpus budgets, protected-path checks, and immutable VALUE accounting. This execution is authorized by the approved TS at `6a7ede0549dca272c149b0294a972c013d5cb291` plus the Coordinator's direct dispatch commit `1cf9d8c6871e4164ea281bf6e0b5788bdcb7273e`, not by the future AT convention, session title, identity metadata, or a not-yet-existing Role Assignment row.

The direct execution channel is Coordinator task `01a07697-f428-7582-ade4-50997a4a6d63` → Executor task `01a076b3-d919-7471-9306-c1020b80d43c`; scope is the approved Phase D TS; results return directly to that Coordinator. The acting human principal is `saubakirov`, resolved from the sole project profile; events use `on_behalf_of: saubakirov` and `via: codex`.

## 2. Entry Points

VALUE selector (literal, immutable; 16 files):

1. `.tfw/conventions.md`
2. `.tfw/templates/HL.md`
3. `.tfw/workflows/plan.md`
4. `.tfw/workflows/handoff.md`
5. `.tfw/workflows/review.md`
6. `.tfw/workflows/research/base.md`
7. `.tfw/adapters/codex/AGENTS.md.template`
8. `AGENTS.md`
9. `.agent/workflows/tfw-plan.md`
10. `.agent/workflows/tfw-handoff.md`
11. `.agent/workflows/tfw-review.md`
12. `.agent/workflows/tfw-research.md`
13. `.claude/commands/tfw-plan.md`
14. `.claude/commands/tfw-handoff.md`
15. `.claude/commands/tfw-review.md`
16. `.claude/commands/tfw-research.md`

ASSURANCE selector (2 files): `docs/scripts/test_runtime_context.py`, `docs/scripts/test_integration.py`.

Protected references include `.tfw/adapters/claude-code/CLAUDE.md.template`, `.tfw/VERSION`, `CHANGELOG.md`, project configuration, migrations, release artifacts, and Phases A–C/E. The existing Codex managed block is the only permitted root-bootstrap region; bytes outside its markers remain unchanged.

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions. The approved TS, immutable selector, dispatch, identity, and AG scope are complete.

## 4. Recommendations (suggestions, not blocking)

1. Keep the canonical AT wording complete but compact: the pre-write forecast reaches `/tfw-plan` 24,724/24,725, `/tfw-handoff` 6,363/6,366, `/tfw-review` 24,929/24,954, focused research 6,089/6,102, deep research 6,154/6,167, docs 15,278/15,278, and active corpus 33,367/33,749 without changing any cap literal.
2. Preserve the existing source-derived read-graph machinery and add Phase D semantic consumers beside it. A bare cross-reference was considered and rejected because it cannot execute declaration, same-unit activation, direct reporting, or the eight-gate profile admission algorithm required by F30 and D73–D75.
3. Adapt the pre-Phase-D protection assertion for root `AGENTS.md` to compare bytes outside the managed block, while retaining exact protection for every other historical/release path.

## 5. Risks Found (edge cases, potential issues not in TS)

1. Root bootstrap has only two words of docs-route headroom; the Codex managed block must be exactly 161 words and identical to its template.
2. The repository already contains historical/provider examples outside adapters. The baseline census must be frozen and the Candidate must add zero new provider/API occurrences outside the two allowed Codex carriers; Phase D must not repair Phase E or historical text.
3. Declaration, row activation, and workflow permission are distinct. Tests must reject draft HL, unapproved exact TS, `—`, ambiguous/foreign same-unit evidence, relay/subagent/fork rows, self-grants, and metadata-derived authority.
4. The first tested implementation commit must remain the Candidate; EV, RF, status, journal, and assurance-only writes cannot silently move it.

## 6. Inconsistencies with Code (spec vs reality)

No blocking product inconsistency. The baseline correctly lacks AT and therefore requires the planned implementation. One assurance assumption is intentionally superseded by this approved phase: the RTPSN protected-path test currently compares all of root `AGENTS.md`; Phase D must instead protect its non-managed bytes while permitting the selected managed block. Pre-existing TFW-54/provider-history wording belongs to protected history or Phase E and is not repaired here.

Baseline verification before any durable Phase D write: clean detached HEAD aligned to dispatch `1cf9d8c6871e4164ea281bf6e0b5788bdcb7273e`; approval and Baseline are ancestors; all 18 selected paths exist; all eight workflow copies equal canon; `python -m pytest .tfw/scripts/ docs/scripts/ -q` → 646 passed, 1 skipped; cap literals unchanged. Planned VALUE denominator remains 16 files and 640 touched text LOC (420 additions + 220 deletions); neither 32-file nor 1,280-LOC owner-only multiplier threshold is forecast.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | PV0 — NS1 Purpose | ✅ | Applied | Direct human-rooted authority, visible rows, and resumable checkpoints remain inspectable. |
| 2 | PV0 — NS3 Non-goals | ✅ | Applied | No runtime, vendor lock, liveness promise, or untested provider profile is introduced. |
| 3 | PV1 — Methodology values | ✅ | Applied | Gates live in repository artifacts and canonical workflows, not transport metadata. |
| 4 | PV1 — Success Criteria | ✅ | Applied | Receive/report checkpoints and same-unit continuation are explicit and testable. |
| 5 | `philosophy.md` F37 | ✅ | Applied | A dispatch or row cannot create or widen its own mandate. |
| 6 | `philosophy.md` F38 | ✅ | Applied | `Autonomous from` is conservative; `—` returns every decision. |
| 7 | `KNOWLEDGE.md` D63 | ✅ | Applied | Each Role Assignment row is one frozen claim changed through §12. |
| 8 | `KNOWLEDGE.md` D73 | ✅ | Applied | Selective workflow read contracts remain authoritative; no preload or wrapper is added. |
| 9 | `KNOWLEDGE.md` D74 | ✅ | Applied | Primary workflow gates receive executable AT checks without losing prior authority. |
| 10 | `KNOWLEDGE.md` D75 | ✅ | Applied | Eight secondary workflow consumers will be exact canonical copies. |
| 11 | `KNOWLEDGE.md` D76 | ✅ | Applied | VALUE membership and arithmetic stay tied to immutable Baseline/Candidate refs. |
| 12 | `KNOWLEDGE.md` D77 | ✅ | Applied | The Codex profile requires separate worktrees for mutating rows. |
| 13 | `KNOWLEDGE.md` D79 | ✅ | Applied | Session title is navigation only and is never parsed as authority. |
| 14 | `KNOWLEDGE.md` D80 | ✅ | Applied | Participant remains a stable human-rooted principal, separate from role/provider/session. |
| 15 | `KNOWLEDGE.md` D81 | ✅ | Applied | Profile, binding, title, message, and event metadata grant no authority. |
| 16 | HL Contract | ✅ | Applied | Declaration facts and Role Assignment rows freeze with owner-approved HL. |
| 17 | §6 Scope Budgets | ✅ | Applied | Preflight uses unchanged caps and immutable multiplier thresholds; no ratchet. |
| 18 | §15 Role Lock | ✅ | Applied | AT activation never authorizes another workflow or combines Executor/Reviewer. |
| 19 | `convention.md` F4 | ✅ | Applied | Every reference is attached to a receive, validate, report, or admission action. |
| 20 | `convention.md` F5 | ✅ | Applied | Canonical workflow edits are propagated byte-for-byte to accepted copies. |
| 21 | `convention.md` F19 | ✅ | Applied | Existing identifiers, status, event, and artifact naming remain unchanged. |
| 22 | `process.md` F6/F7 | ✅ | Applied | Six-column assignments and direct channels survive coordinator/session changes. |
| 23 | `process.md` F30 | ✅ | Applied | Duties are placed at actual pre-work and return checkpoints, not stated as aspiration. |
| 24 | `process.md` F39 | ✅ | Applied | Source, route, provider, copy, and protected-path censuses precede edits. |
| 25 | `process.md` F40/F41 | ✅ | Applied | Context ceilings remain reachable and every compaction preserves its behavior. |
| 26 | `constraint.md` F2 | ✅ | Applied | Existing canonical prose is compacted where necessary to fund complete AT semantics. |
| 27 | `constraint.md` F12 | ✅ | Applied | Every role duty is persisted in shared files and verified from source. |
| 28 | `stakeholder.md` F6 | ✅ | Applied | Direct, bounded autonomy reduces interruptions without weakening owner returns. |
| 29 | `stakeholder.md` F7 | ✅ | Applied | The Role Assignment rendering precedes any autonomous spend. |
| 30 | `stakeholder.md` F14 | ✅ | Applied | Only the researched Codex visible-task chain receives a profile in this phase. |
| 31 | `environment.md` F6 | ✅ | Applied | Claude and mixed-provider admission remain excluded pending native evidence. |

No additional knowledge item was needed beyond the Phase HL citations.

---

*ONB — TFW_20260902-111644_CRATM / Phase D: Team mode and Role Assignment | 2026-09-06*

## 8. Revision Round 2 — A7 single-LEAD and profile-admission correction

### 8.1 Governing bound and understanding

This mixed rung-2 round replaces only the prospective Phase D product contract while preserving the
original Candidate, EV, RF, reviews, closure, journal and released 2.2.0 history. The governing order
is owner-approved A7 plus
[`TS__phase-d__team_mode_and_role_assignment__rev2.md`](TS__phase-d__team_mode_and_role_assignment__rev2.md),
fixed unchanged from reviewed content at approval epoch
`25930c5238036b3d96ee5ae50d195a9dc340f394`. Direct dispatch
`journal/20260906-210453__dispatch__5a4c.md` reuses this Executor task and reports to Phase D
Coordinator task `01a07697-f428-7582-ade4-50997a4a6d63`; it creates no new task, principal, profile
or role holder.

The correction separates the one owner-selected stable LEAD principal from the actual addressable
working units it creates. Shared principal attribution does not merge unit nodes, parentage, work or
proposal origin and does not distribute the LEAD's amendment grant. Role Assignment must distinguish
the protected mandate from ordinary in-bound unit instantiation. An unavailable assigned holder
still waits for an owner-approved §12 `SUPERSEDE`; a replacement dispatch alone is insufficient.
The supplied Codex profile is admitted only as the named G1–G7/no-G8 first-release exception, while
every additional profile still requires one native all-eight trial.

### 8.2 Entry points and immutable accounting

The literal VALUE selector contains 18 existing files: `.tfw/conventions.md`,
`.tfw/templates/{HL.md,team/profile.md,journal/event.md}`, four canonical workflows, the Codex adapter
template and root managed receiver, and the eight accepted workflow copies. The two ASSURANCE paths
remain `docs/scripts/test_runtime_context.py` and `docs/scripts/test_integration.py`. Product Baseline
is `8e68ab37d300122ff110500ad58f354f76b6210f`; the cumulative forecast is 295 additions + 465
deletions = 760 touched text LOC. The historical approved denominator remains immutable at 16/640;
18/760 is a prospectively approved comparison, not a ceiling or ratchet. All later VALUE arithmetic
will be replayed from the product Baseline and all approval-epoch history protection from
`25930c5238036b3d96ee5ae50d195a9dc340f394`.

### 8.3 Questions and authorization

No blocking questions. Main approved the exact TS rev2 content, both added VALUE members, the complete
18/760 plan, A5 treatment and case-specific lineage reconciliation before work. The explicit AG
execution grant and direct dispatch release the implementation HOLD for this bound only. The current
operational chain has no newly selected product LEAD/profile; authority comes from the owner's standing
Main mandate and exact TS approval, never from the product behavior being implemented.

### 8.4 Recommendations, risks and consistency

1. Replace obsolete roster/handle-as-node wording rather than layer a second explanation over it; use
   substitution and local compaction before invoking A5 growth.
2. Keep `{principal, originating unit}` explicit through forwarding, restart and continuation. Test
   both a truly subordinate proposal reaching an eligible LEAD and a LEAD-origin proposal remaining
   owner-routed after laundering attempts.
3. Treat replacement as a two-act gate: owner-approved `SUPERSEDE`, then bounded dispatch. Same
   principal and scope do not make a silent substitute legal.
4. Evaluate profile admission as one combined canon-plus-adapter decision. Separate gate and evidence
   strings are insufficient because they allowed the original contradiction.
5. Preserve the approval-epoch blobs, old cap literals, bindings, master/phase planning inputs and all
   A–C/original-D/Phase-E/release history exactly; the known generic lifecycle reopen gap and
   `gen_index.py` mismatch remain explicitly out of scope.

No blocking spec/code inconsistency remains. The delivered product intentionally contradicts A7 and
the supplied-profile exception; that is the approved correction subject, not an ambiguity. The only
execution risk is accidental collapse of principal, unit or proposer identity while shortening the
four over-limit workflows; source-derived matrices and output-changing mutants are the required gate.

### 8.5 Knowledge citation delta

All refreshed Phase HL §7.2 citations were read. NS1–NS3 and methodology values require human-rooted,
inspectable delegation without vendor runtime; F37/F38 prevent mandate self-extension and price owner
attention; D63/D72–D82 preserve frozen claims, REVISE lineage, VALUE accounting, worktree isolation,
principal/unit separation and routing; F30/F39–F41 require executable enforcement sites and
source-derived delivery; stakeholder F6/F7/F14 and master S28–S29 require one named LEAD, fewer owner
turns and human accountability for the whole chain. No new PV item or fact candidate is needed.

---

*ONB Revision Round 2 — TFW_20260902-111644_CRATM / Phase D | 2026-09-06*

## 9. Revision Round 3 — root-only named LEAD navigation

### 9.1 Governing order, unit and preserved entry state

The governing order is
[`TS__phase-d__team_mode_and_role_assignment__rev3.md`](TS__phase-d__team_mode_and_role_assignment__rev3.md),
approved unchanged from reviewed draft `73d711808a6b6fe1b1e15589e7c3c9d479a9e8a5` at epoch
`b755de9128f2b0442615a4ca8b787761f937bbcd`. Direct dispatch
`journal/20260906-215342__dispatch__ee40.md` reuses this Executor unit
`01a076b3-d919-7471-9306-c1020b80d43c`, whose actual parent is Phase D Coordinator unit
`01a07697-f428-7582-ade4-50997a4a6d63`. No product LEAD principal is selected by this operational
trace; the acting principal remains human `saubakirov`, proposal origins remain A from Main's A7
consumer finding and B from the owner's named-LEAD request, and metadata grants nothing.

Before fast-forward, HEAD was `c1809cd4a9c85c8dbc83e5c31fc6daa797debd29`, with exactly 20 dirty
paths, zero cached/untracked paths and sorted-map digest
`ff36d393785fd6450ac0717603e47ad668e695026ed818454992dc4262be1719`. Incoming TRACE changed five
non-overlapping phase paths. After `git merge --ff-only 89ed24bd6a983ec33f3b67fe9dac5c8c604fadf6`,
the exact path set, every `git hash-object` value, digest and cached/untracked counts were identical.
The preserved 18 VALUE + 2 ASSURANCE WIP therefore remains uncommitted and is not a Candidate.

### 9.2 Understanding and acceptance boundary

All revision-2 mandate/unit, proposal-origin, replacement, admission and direct-route requirements
stand. Revision 3 adds one exact navigation conjunction: only `PLAN` or `RESUME` may attempt LEAD,
and only when authoritative lineage selects one valid agent principal, the acting principal equals
that selected handle, and the current actual unit equals the mandate's exact root Coordinator unit.
The qualified title is `LEAD · {handle} · {TASK}[ · {PHASE}]`, using the stable profile handle.

A same-principal child remains ordinary `PLAN` or `RESUME`, even if bounded or itself a Coordinator.
A human, different/unselected agent, stale handle, forwarded selection, wrong role, missing or
ambiguous root/current unit also keeps ordinary WORK and emits no guessed handle. The title remains
navigation-only: it cannot establish principal, unit, mandate, grant, dispatch or authority. Existing
TASK/PHASE, collision, exact-readback and report-once/fail-soft behavior remains unchanged, as do all
Research/Handoff/Review/Docs/Init cues.

### 9.3 Selector, accounting and implementation route

The approved literal selector is 21 VALUE paths: the preserved 18 plus only
`.tfw/workflows/resume.md`, `.agent/workflows/tfw-resume.md` and
`.claude/commands/tfw-resume.md`. The same two ASSURANCE modules remain selected. Product Baseline is
`8e68ab37d300122ff110500ad58f354f76b6210f`; historical denominator `16/640`, rev2 forecast
`18/760`, observed held WIP `18/866`, and approved combined forecast `21/932` are distinct facts.
The forecast is not actual and does not ratchet the `32/1,280` owner thresholds.

Implementation will compact the central Session identity predicate, point Plan and Resume to the
same facts/checkpoint, synchronize their accepted copies, and extend the existing source-derived
oracle and two-epoch integration checks. It will not create or rename a live task, profile, principal,
binding, carrier, runtime or config key; will not edit glossary or unrelated cues; and will not absorb
RTBO, restore retired index/runtime files, or touch saved-project master.

### 9.4 Questions, risks and authorization

No blocking question remains. Main approved the exact 21-path/932-LOC plan before this round and the
direct dispatch releases only that implementation bound. The principal risk is reducing the LEAD
predicate to shared attribution, a generic bound or Coordinator role; root/child and stale/forwarded
mutants must reject each collapse. A5 requires minimum substitution and exact before/after document,
route, central-range and active-corpus measures without changing cap literals or deleting semantics.

Before Candidate, the complete root PLAN/RESUME, child/human/different/missing/ambiguous/stale/
forwarded cases, required mutants, copy/history checks, full suite, build, diff check and literal
21-path numstat must pass. Candidate is the first tested immutable 21 VALUE + 2 ASSURANCE commit after
the approval epoch. EV/RF and lifecycle trace remain later cumulative TRACE only.

---

*ONB Revision Round 3 — TFW_20260902-111644_CRATM / Phase D | 2026-09-06*

## 10. Revision Round 4 — rendered-LEAD collision and finite continuation repair

### 10.1 Governing order and returned unit

This is a Rung-1-only return while lifecycle is `RF`. The implementation order remains approved
[`TS__phase-d__team_mode_and_role_assignment__rev3.md`](TS__phase-d__team_mode_and_role_assignment__rev3.md)
at approval epoch `b755de9128f2b0442615a4ca8b787761f937bbcd`; the closed repair bound is REVIEW rev3 §8 at ruling
tip `61c7364fac7e377a7e3b76c09d376dcd26475c98`. No TS sibling, HL amendment, profile, principal or
new role holder is permitted.

Dispatch `journal/20260906-233320__dispatch__98b7.md` reuses this exact Executor unit
`01a076b3-d919-7471-9306-c1020b80d43c`, with Phase D Coordinator parent
`01a07697-f428-7582-ade4-50997a4a6d63`, direct Codex task channel, Executor role and Round-4 scope.
The originating proposer remains principal `saubakirov` in Main Coordinator unit
`01a07050-9d35-7080-a5f6-afd14334e68d`; forwarding does not replace that origin. The acting human
principal is `saubakirov`, resolved from the sole project profile. Shared attribution grants this
child no LEAD or amendment authority.

### 10.2 Understanding and acceptance boundary

Two accepted defects are mandatory. First, the central Session identity contract must apply its
collision, exact-readback, report-once and fail-soft behavior to both ordinary `BASE` and rendered
`LEAD_BASE`. Two qualified roots with stable keys `ab7` and `ac9` must choose the shortest unique
leading prefix and render `LEAD · cratm-main · CRATM · D · @ab`; exact readback claims it, while a
missing stable key or altered readback reports once and continues unclaimed. Source-derived cases
and independent output-changing mutants must cover each branch without changing root-only
qualification, ordinary titles or Plan/Resume continuity.

Second, the Phase-D continuation assurance must admit a finite exact set: cumulative ONB/RF/EV,
status and valid phase-local journal events, REVIEW rev3/rev4 plus exactly their three stage files,
and the seven explicitly named attachments for each of rounds 3 and 4. It must reject arbitrary
`review/**`, `evidence/**`, unsuffixed pre-approval attachments, product/assurance paths and unrelated
TRACE. Matching must be exact path membership or structurally exact journal validation, never a
substring-only round test. Positive fixtures cover the committed rev3 tip and the complete expected
Round-4 Executor-to-Reviewer sequence; foreign-path negatives remain closed.

### 10.3 Entry points, scope and immutable history

VALUE/ASSURANCE writes are limited to exactly `.tfw/conventions.md`,
`docs/scripts/test_runtime_context.py` and `docs/scripts/test_integration.py`. The first is the only
VALUE path; the tests are the only ASSURANCE paths. Every other member of the approved 21+2 selector
is read/protected only. If mechanical evidence required another path, execution would stop and
report rather than widen scope.

Historical Candidate `2363c3d315a855fc0bd6c6dbf683e16bfbaf1726`, all prior ONB/RF/EV/REVIEW
bytes and approval history remain openable. A new replacement Candidate will be the first fully
tested implementation commit after this acceptance and before new EV/RF/state TRACE. Product
Baseline replay must still return the exact 21-path VALUE membership, with actual numstat and A5
figures recomputed. No later VALUE is allowed.

### 10.4 Questions, recommendations, risks and authorization

No blocking questions. The Coordinator ruling and exact dispatch resolve the complete return bound;
the standing approved AG execution grant authorizes implementation only inside it.

Recommendations: express collision eligibility once as `duplicate(rendered-title)` where the
rendered title is either BASE or qualified LEAD_BASE; keep collision keys outside authority and
qualification inputs. Model the continuation allowlist as explicit finite constants plus a strict
phase-journal recognizer so reviewer-stage growth cannot silently broaden it.

Risks: a BASE-only collision predicate would repeat the accepted defect; treating identical handles
as identical units would collapse two roots; readback mismatch must not claim ownership; a glob or
substring allowlist would legalize foreign evidence/review content. Each risk has an output-changing
mutant or positive/negative path fixture in the required assurance.

### 10.5 Knowledge citation delta

The prior 31 HL §7.2 citations remain read and applied; no unchanged acceptance area is re-done.
D72 governs this Rung-1 return and cumulative artifacts; D79–D82 keep navigation non-authoritative
and principal/unit/dispatch facts separate; F30 requires enforcement at the real collision and
continuation consumers; F39–F41 require exact source-derived delivery and context measurement; F4,
F5 and F19 preserve executable references, canonical ownership and naming; Role Lock prohibits this
Executor from changing TS/HL/REVIEW. No new PV item or fact candidate was found.

---

*ONB Revision Round 4 — TFW_20260902-111644_CRATM / Phase D | 2026-09-06*
