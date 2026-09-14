# TS — TFW_20260913-151442_RWNR / Phase A: Rehome continuation responsibilities

> **Date**: 2026-09-13
> **Author**: robert, Coordinator unit `01a09a92-18fb-7da1-a639-6a86844bf147`
> **Status**: ✅ APPROVED — `saubakirov`, 2026-09-13; exact TS proposal and `3 VALUE files / 900 touched text LOC` authorized
> **Parent HL**: [Phase A derivation](HL__phase-a__continuation_responsibilities.md)
> **Master HL**: [Resume Workflow Necessity and Retirement](../HL-TFW_20260913-151442_RWNR.md)
> **Research**: [Iteration 2 RES](../research/iter2/RES.md) · [Extract E1–E5](../research/iter2/3_extract.md) · [Challenge C1–C6](../research/iter2/4_challenge.md)
> **G1**: owner-approved C2 constraints in [dispatch 4ded](../journal/20260913-190312__dispatch__4ded.md)

---

## 1. Objective

Make `/tfw-plan <exact task-or-phase>` a pure, total returning-work inspector/router while preserving every lifecycle owner and keeping Resume unchanged. The accepted Candidate must re-resolve continuation identity every time, stay at or below 1,200 Plan words, reduce the complete retained instruction surface below 2,737 words, and supply executable no-mutation, migration, and history gates for safe Phase B retirement. Any miss selects C1 and keeps Resume.

## 2. Scope

### In Scope

- Add one existing-reference pre-route to Plan after its ordered context/identity inputs resolve and before the Knowledge Gate or any Plan write.
- Cover exact active/historical selection, phase-local state, the full lifecycle matrix, approval/review lineage, direct close/recovery address, and report/ask/stop cases without invoking another workflow.
- On every continuation, re-resolve AT, selected/acting principal, mandate root, current unit and direct dispatch; reapply the exact root or ordinary Plan title and read it back.
- Deduplicate Plan in place and reference central conventions/templates rather than copying their contracts.
- Synchronize the two tracked full-copy Plan receivers exactly.
- Add source-derived and temporary-repository assurance for routing, identity, no mutation, migration preflight, history preservation, word accounting, and failure mutants.

### Out of Scope

- Any Resume deletion or edit; manifest/config/skill/receiver/docs/migration-guide retirement; Phase B work; or release-version selection.
- A new command, alias, redirect, tombstone, helper workflow, registry, hidden dispatcher, or adapter-owned route logic.
- Plan-owned lifecycle effects, phase selection, close/repair, approval, implementation, review, knowledge consolidation, release, or TKL mutation.
- Historical trace rewriting or inference from chat, visible title, OS/provider identity, or derived indexes.

## 3. Principles Check

| # | Master HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Delete surface, preserve semantics | AC-2, AC-5 | total route and preservation oracles pass before Phase B |
| P2 | One user job, one obvious entry | AC-2 | exact Plan entry yields one route/wait/terminal result |
| P3 | Role boundaries outrank convenience | AC-2, AC-4 | Plan never invokes or performs another owner's effect |
| P4 | Evidence before retirement | AC-2–AC-6 | source-derived scenarios, temporary trees, mutants and immutable Candidate |
| P5 | Net simplification | AC-1 | Plan ≤1,200 and complete `C < 2,737` |
| P6 | Canonical first, adapters thin | AC-1, AC-6 | one canonical edit; two exact copies; thin skill unchanged |
| P7 | History remains true | AC-5 | 179 exact tree entries and three monotone aggregates |
| P8 | No substitute ceremony | AC-1, AC-4 | no helper, alias, tombstone, registry or hidden route |

## 4. Affected Files and Value-Bearing Accounting

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `.tfw/workflows/plan.md` | MODIFY | `VALUE` | sole canonical continuation behavior; compact pure router plus existing planning gates |
| `.agents/workflows/tfw-plan.md` | MODIFY | `VALUE` | installed Antigravity full-copy receiver; exact canonical bytes after parity |
| `.claude/commands/tfw-plan.md` | MODIFY | `VALUE` | installed Claude full-copy receiver; exact canonical bytes after parity |
| `docs/scripts/test_runtime_context.py` | MODIFY | `ASSURANCE` | source-derived lifecycle/identity cases, precedence and semantic mutants |
| `docs/scripts/test_repository_contracts.py` | MODIFY | `ASSURANCE` | temporary-tree no-mutation, receiver, history, accounting, parity and scope oracles |
| `workspace/TFW_20260913-151442_RWNR/phase-a/{status.md,journal/**,ONB__*,RF__*,REVIEW__*,evidence/**}` | CREATE/MODIFY | `TRACE` | phase lifecycle, evidence and delivery/review records; never runtime input |

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | `.tfw/workflows/plan.md`; `.agents/workflows/tfw-plan.md`; `.claude/commands/tfw-plan.md` |
| Baseline / selector source | `f6e85aa898061779c6b37bba34dc97e28c76f01f`; owner-approved TS proposal at `413945ca0a4f34065ff22b8b24f47bf694d72710:workspace/TFW_20260913-151442_RWNR/phase-a/TS__phase-a__continuation_responsibilities.md` (blob `d15c5dc8b25c2751ed289a418f937226608333dc`); approval act recorded in [dispatch f58c](journal/20260913-194049__dispatch__f58c.md) |
| Candidate rule | First tested immutable Executor commit with all required VALUE+ASSURANCE, before EV/RF/REVIEW/final transition; excluded-only later writes do not move it; later VALUE requires a new Candidate and recomputation |
| Logical VALUE files | `3`; rename = one and no rename is planned |
| Touched text LOC | at most `360 additions + 540 deletions = 900`; numeric numstat fields across the three literal VALUE paths |
| Triggers / disposition | Forecast is below `50 files / 5,000 LOC`; one canonical rewrite plus two exact receivers avoids a split, and tests/evidence protect the high-risk router. No pre-work trigger fires |
| Multiplier / authority | Immutable plan `3/900`; at or above `6 VALUE files` or `1,800 LOC` returns to owner. Any new instruction/helper path changes the approved architecture and also returns to owner. Below both multipliers, Coordinator may approve only necessary growth inside the same three paths with Goal, outputs, ACs, DoF, roles and authority fixed |
| Approval epoch / failure | Owner `saubakirov` approved the exact proposal at commit `413945ca0a4f34065ff22b8b24f47bf694d72710`, blob `d15c5dc8b25c2751ed289a418f937226608333dc`, with immutable `3/900`; missing/mutable/mismatched/late = `BLOCKED`; metric-only N/A; unresolved phase = `INVALID`; `DEFERRED` is non-terminal |

```powershell
$valuePaths = @('.tfw/workflows/plan.md','.agents/workflows/tfw-plan.md','.claude/commands/tfw-plan.md')
git diff --name-status --find-renames=50% -z f6e85aa898061779c6b37bba34dc97e28c76f01f <CANDIDATE_SHA> -- $valuePaths
git diff --numstat --find-renames=50% -z f6e85aa898061779c6b37bba34dc97e28c76f01f <CANDIDATE_SHA> -- $valuePaths
```

### Prospective scope rulings

Only the three literal VALUE paths may change. The two receiver paths change all-or-none with canonical Plan and must be byte-identical; tests and TRACE never enlarge VALUE. A new canonical instruction source, behavior-bearing adapter/helper, or Resume mutation is an architecture change and returns to the owner before work. No Phase A split is useful because canonical Plan and its copies form one atomic delivery.

### Task-local hard constraints

| M1 consequence | M2 object/risk | M3 measure/selector | M4 pre-act check | M5 softer-control gap | M6 change authority |
|---|---|---|---|---|---|
| Prevent a bloated Plan, hidden replacement command, lost continuation guard, overwritten history, or foreign receiver mutation | candidate Plan; all changed surviving instruction sources; pre-route repository bytes; 179 task traces; three aggregates; receiver connected group | strict-UTF-8 Unicode `\S+`; baseline→Candidate zero-context/no-renames added-line selector from Extract E5; exact path/blob/subsequence and before/after byte maps | Before Candidate creation, run Plan cap, complete `C`, route/no-mutation, receiver preflight/idempotence, split-history and unclassified-path checks | Later disclosure/review cannot restore overwritten bytes, make incomparable counts valid, or undo a shipped authority leak | Any miss immediately selects C1 and keeps Resume. Executor cannot waive. Changed VALUE selector/helper or ≥2× returns to owner; only necessary same-path growth below 2× may receive prospective Coordinator ruling |

**Actions (not budget dimensions):** VALUE = 3 MODIFY; ASSURANCE = 2 MODIFY; TRACE = phase lifecycle/evidence/delivery records.
**Immutable owner-approved denominator:** `3 VALUE files / 900 touched text LOC`; never ratchets.

## 5. Acceptance Criteria

### AC-1: Minimal canonical change and immutable surface arithmetic

- [ ] Only the three literal VALUE paths change; canonical Plan is the sole behavior source and both receivers equal it byte-for-byte.
- [ ] Strict UTF-8 Unicode `\S+` reports `W(candidate Plan) ≤ 1,200`.
- [ ] Reproduce `B = 2,021 + 716 = 2,737` from the named baseline blobs. Compute `C` as complete Candidate Plan plus candidate-side added-line tokens in every other changed surviving instruction source from Extract E5; generated copies count once after parity. Require `C < 2,737`.
- [ ] No new instruction/helper path, copied central contract, unclassified moved instruction, public/internal resume substitute, or Phase A Resume edit exists.

Gate: targeted `rwnr` tests; strict counter and zero-context diff over immutable Baseline/Candidate; exact path/copy comparison.

Evidence: Full — `evidence/phase-a-accounting.json` records SHAs, blobs, paths, counts, added-line classification and terminal verdict.

### AC-2: Total routing-only continuation matrix

- [ ] With no existing reference, return `NEW` into existing Plan inception. Exact zero matches, collisions, historical-only scope and invalid carriers report the resolved defect and stop before Knowledge Gate or writes.
- [ ] For one active task, read task state/journal/authority; for a selected phase use only phase-local carriers. Unselected `PHASES` renders the phase matrix, asks which phase, and stops; nested `PHASES` is invalid.
- [ ] Route `TODO`, `HL_DRAFT`, unapproved `TS_DRAFT`, and valid REVISE to existing Plan gates; `RES` to Research; approved `TS_DRAFT`/`ONB` to Handoff; `RF`/incomplete `REV` to Review; APPROVE-carrier mismatch/`KNW` to Coordinator control.
- [ ] `BLOCKED` waits on its recorded dependency; `DONE`/`REJECTED` are terminal; `UNDECLARED`/unknown preserve the verbatim value and wait for the owner. No state is compared ordinally or normalized.
- [ ] All 28 Extract/Challenge fixtures match the expected result. For every fixture, including those that later continue Plan, the pre-route evaluator preserves the complete repository path set and bytes.

Gate: source-derived scenario table plus temporary Git-repository before/after hashes; precedence mutants for collision, history, phase, approval, terminal and unknown branches must fail.

Evidence: Full — `evidence/phase-a-routing.json` names each fixture, state/lineage input, result, route, mutation hash and mutant outcome.

### AC-3: Continuation identity is re-resolved and reapplied

- [ ] Every existing-task continuation resolves AT applicability, selected stable agent, acting principal, mandate root, current actual unit, parent/scope/channel and direct dispatch from authoritative task/phase state and ordered lineage before questions, routing or writes.
- [ ] Non-AT ordinary continuation yields `PLAN · {TASK}[ · {PHASE}]`. A valid named AT root yields exact `LEAD · {handle} · {TASK}[ · {PHASE}]`. A same-principal child, including a Coordinator child, remains ordinary `PLAN` with no handle.
- [ ] When AT continuation is indicated, absent, ambiguous, stale, foreign or wrong-root mandate/identity facts name the defect, ask or report through the direct channel, and stop with identical repository bytes and no claimed LEAD title.
- [ ] Each continuation attempts exact title reapplication and exact readback; transport failure follows the central report-once/continue-unclaimed rule and never becomes authority.
- [ ] Tests reject chat/title/OS/provider inference, forwarded selection, principal-only grant, child inheritance, skipped re-resolution, missing readback, and altered title acceptance.

Gate: source-derived identity cases and semantic mutants in `docs/scripts/test_runtime_context.py`, with before/after repository hashes for every stop case.

Evidence: Full — identity rows live in `evidence/phase-a-routing.json`, including intended title, readback, claim state, direct return and mutation result.

### AC-4: Exact lifecycle owners and close/recovery boundary

- [ ] Plan outputs a route but never invokes or executes Research, Handoff, Review, Docs, Knowledge, close/repair, phase choice, approval, transition or implementation.
- [ ] For `KNW`, selected close/repair, and reconstructable APPROVE/carrier mismatch, Plan prints the fixed Extract E2 `Coordinator control` address to `.tfw/conventions.md` → `Closing and record recovery` and stops.
- [ ] That central heading remains the sole close/repair effect owner; session title, principal attribution, adapter copy and route output grant no authority.
- [ ] Existing Role Lock permitted/forbidden artifacts remain semantically unchanged and every declared state has exactly one named owner, wait, or terminal result.

Gate: contract projection and mutants that make Plan write, choose, invoke, close, repair, approve or branch inside an adapter must fail.

Evidence: Full — route/owner assertions and failing mutants are recorded in `evidence/phase-a-tests.txt` and cross-referenced from EV.

### AC-5: Retirement preconditions preserve receivers and history [depends: AC-1, AC-2, AC-4]

- [ ] Phase A changes none of the Resume workflow/skill/manifest/config/receiver/doc/migration paths and makes no deletion claim.
- [ ] An executable assurance model covers `ABSENT`, `OWNED_EXACT`/`OWNED_BLOCK`, `TARGET_CURRENT`, and `FOREIGN_OR_DRIFTED`; it preflights the connected retirement group before writes, preserves foreign/outer bytes, accepts absent Cursor, verifies ten unique commands across four clean adapters, and produces an empty second-run diff.
- [ ] Regenerate the 179-entry baseline task-tree manifest at `a2363fd07253ca92410db149b4301432de79be3b` and require SHA-256 `ed52c4c26845e90c14a569f867ec2200b18da44374f7df2fd897bf7fb58bef96`; path, mode and blob IDs stay exact.
- [ ] For `.tfw/CHANGELOG.md`, `KNOWLEDGE.md`, and `knowledge/stakeholder.md`, verify the named baseline blobs remain exact ordered raw-line subsequences; additions may pass, but delete/edit/reorder/re-encode/line-ending mutants fail.
- [ ] Any receiver, history, route, identity, no-mutation or arithmetic miss rejects Phase A acceptance, preserves Resume and records C1; no partial retirement or optimistic Phase B route follows.

Gate: real temporary receiver trees, connected-group mutants, repeat-run diff, Git-object history oracle and aggregate byte-line mutants in `docs/scripts/test_repository_contracts.py`.

Evidence: Full — `evidence/phase-a-receiver-migration.json` and `evidence/phase-a-history.json` record fixtures, identities, mutations and verdicts.

### AC-6: Reproducible evidence and regression package [depends: AC-1, AC-2, AC-3, AC-4, AC-5]

- [ ] Targeted routing, identity, migration, history, accounting and parity tests pass and each required mutant changes the projection before rejection.
- [ ] The configured maintainer collect-only and test commands over `tools/tests/` and `docs/scripts/` pass from the immutable Candidate; pre-existing unrelated failures are separated and cannot support a green claim.
- [ ] EV includes one row per AC using only `VERIFIED`, `DEFERRED`, `BLOCKED`, or justified `N/A`; every claim resolves to raw phase evidence and immutable Baseline/Candidate SHAs.
- [ ] Exact Candidate diff contains only the approved VALUE/ASSURANCE paths before TRACE-only evidence/RF writes. No evidence file becomes a runtime reader.

Gate: `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_repository_contracts.py -q`; configured lint `python -m pytest tools/tests/ docs/scripts/ -q --collect-only`; configured test `python -m pytest tools/tests/ docs/scripts/ -q`; exact NUL-safe scope/accounting commands.

Evidence: Full — `evidence/phase-a-tests.txt`, all four structured JSON receipts below, and `evidence/EV__phase-a__continuation_responsibilities.md`.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-a__continuation_responsibilities.md` | required per-AC evidence and terminal verdict |
| `evidence/phase-a-routing.json` | 28 route fixtures plus identity/reapply/readback/no-mutation cases and mutants |
| `evidence/phase-a-receiver-migration.json` | four-class preflight, connected-group refusal, four-adapter convergence and repeat receipt |
| `evidence/phase-a-history.json` | 179 task entries, three aggregate before-images, byte-line oracles and mutants |
| `evidence/phase-a-accounting.json` | Baseline/Candidate identity, VALUE numstat, Plan/C counts and instruction classification |
| `evidence/phase-a-tests.txt` | exact targeted/full/project/parity/scope commands and raw output |

## 6. Technical Guidance

- Use RES Extract E1–E5 as the exact route/oracle design and Challenge C1–C5 as its negative-case set; the ACs above govern delivery.
- Keep the pre-route as a compact table or decision sequence in Plan and link unique central headings for discovery, state, identity, AT, close/recovery and Role Locks.
- Extend existing source-tree/session-identity/test helpers instead of adding a runtime helper or parallel authority table.
- The migration model is Phase A assurance for Phase B's later version-addressed guide; it authorizes no current removal and invents no G2 version.
- Use strict UTF-8 reads, NUL-safe Git output, temporary directories, and exact before/after byte maps. Keep default tests offline.
- Commit implementation with `git commit --only` over the five approved VALUE/ASSURANCE paths, after full status inspection.

## 7. Definition of Failure

- ❌ Plan exceeds 1,200 words, `C ≥ 2,737`, the baseline/counter differs, or any moved/new instruction is unclassified.
- ❌ Plan performs another workflow's effect, chooses a phase, mutates during pre-route, or gains close/recovery authority.
- ❌ A non-root child claims LEAD, a valid root loses it, non-AT is blocked, or invalid/stale/ambiguous AT facts proceed instead of stopping.
- ❌ Any continuation skips authoritative identity re-resolution, title reapplication, exact readback, or direct-report failure behavior.
- ❌ A Resume/live-retirement path changes, a substitute continuation surface appears, or Phase B/G2 work begins.
- ❌ Foreign receiver or historical bytes are overwritten, `TARGET_CURRENT` is omitted, repeat creates a diff, or history mutants pass.
- ❌ Tests assert wording without changing observable route/mutation results, evidence cannot reproduce Candidate claims, or C1 is not selected on a miss.
- ❌ VALUE exceeds `3/900` without the required prospective ruling, or any unapproved path enters Candidate.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Plan compression drops an existing gate | source-derived anchors, route matrix, full suites and deletion mutants |
| Identity failure is confused with ordinary non-AT | fixtures distinguish no mandate from indicated-but-invalid AT and assert stop behavior |
| Visible title is treated as authority | authoritative re-resolution precedes rename; exact readback is navigation evidence only |
| Assurance accidentally implements Phase B | exact diff allowlist and unchanged Resume/live-retirement paths |
| Synthetic receiver model overclaims native migration | label it Phase A precondition assurance; Phase B still requires real pinned guide/receiver evidence |
| Large test modules hide false greens | independent mutants, raw fixture receipts and Reviewer recomputation |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| `.tfw/workflows/plan.md` and its two full-copy receivers | Phase B consumes; modification only if its approved TS proves necessity | Preserve the accepted router, cap and identity behavior; retirement must not re-expand Plan |
| `docs/scripts/test_runtime_context.py` | Phase B removes Resume-specific expectations | Extend the same source-derived table; keep Phase A route/identity cases green |
| `docs/scripts/test_repository_contracts.py` | Phase B implements command absence and real update receivers | Reuse the four-class/history/accounting oracles; do not replace their immutable baselines |

---

*TS — TFW_20260913-151442_RWNR / Phase A: Rehome continuation responsibilities | 2026-09-13*
