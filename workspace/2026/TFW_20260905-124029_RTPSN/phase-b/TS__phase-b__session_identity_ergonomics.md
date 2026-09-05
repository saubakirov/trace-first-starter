# TS — TFW_20260905-124029_RTPSN / Phase B: Session Identity Ergonomics

> **Date**: 2026-09-05
> **Author**: Codex (Coordinator)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [Master HL](../HL-TFW_20260905-124029_RTPSN.md) · [Phase HL](HL__phase-b__session_identity_ergonomics.md)

---

## 1. Objective

Deliver one provider-neutral session identity contract and place it at the first satisfiable state-backed checkpoint of every task-bound TFW workflow. A user must be able to distinguish work, task, and unambiguous phase before substantive role work, while rename failure remains non-blocking and the current thin command-entry architecture, Role Locks, task state, and CRATM authority remain unchanged.

## 2. Scope

### In Scope

- One authoritative `{WORK} · {TASK}[ · {PHASE}]` grammar with the researched vocabulary, task/phase source precedence, A1 stable-key suffix, A2 rejection, rename/readback behavior, report-once fallback, and navigation-only semantics.
- Exact task-bound/mode classification and local identity checkpoints for Plan, Research, Handoff, Review, Resume, Docs, and Init; explicit non-task classification for Knowledge, Release, Update, and Config.
- Exact synchronization of the seven changed canonical workflows into existing tracked Claude and singular Antigravity compatibility copies; clean-receiver verification for all four manifest adapters.
- Source-derived semantic/negative tests, before/after context and word accounting, supported-host new/existing task-title evidence, and immutable VALUE accounting.

### Out of Scope

- Codex production skill or installed-skill edits, stronger/full/direct proxy migration, root managed-block changes, manifest changes, or a repeat of Phase-A model trials.
- New authority files, registries, wrappers, daemons, hooks, generated runtime inputs, or duplicated grammar/fallback algorithms in workflows or glossary.
- ASCII separator fallback, emoji/symbol alternatives, invented ordinals, guessed task/phase/hierarchy, or silent rename success.
- CRATM roles, lead/main definition, delegation, channels, worktrees, task/session creation ownership, or landing policy.
- Claims of comparative human recognition, universal pixel/search behavior, model compliance, or unobserved provider support.
- Any new external token-spend, run-count, model, or reasoning-effort budget.

## 3. Principles Check

| # | HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Causality before remedy | AC-3 / AC-6 | Preserve Phase-A baseline and protected paths; do not change proxy architecture. |
| P2 | One canonical algorithm | AC-1 / AC-3 | One conventions range owns semantics; workflows own checkpoints; glossary only routes. |
| P3 | Role Lock before task action | AC-2 | Identity executes only after the already-bound workflow role and state resolution, before role work. |
| P4 | Invocation, load, coverage, and compliance differ | AC-3 / AC-5 | Static/context/readback evidence is labelled at its actual level and never promoted. |
| P5 | Research before vocabulary | AC-1 | Implement Iteration-2 D1–D8 and owner amendment verdicts exactly; no new wording choice. |
| P6 | Resolve before naming | AC-1 / AC-2 / AC-4 | State-backed task/phase/lead resolution and omission/fallback scenarios are mandatory. |
| P7 | Recognition before formalism | AC-1 / AC-5 | Compact title is navigation metadata; full authority stays in state/artifacts/Role Lock. |
| P8 | Proportionate assurance | AC-3 / AC-6 | No new preload/file/model run; measure every fixed-context delta and use existing test surfaces. |
| P9 | Resume is a first-class entry | AC-2 / AC-5 | Existing Plan and Resume checkpoints plus current-host existing-task readback are explicit. |
| P10 | Capability honesty and bounded adjacency | AC-1 / AC-4 / AC-6 | Report once and continue; protect CRATM and unobserved-host claims. |

## 4. Affected Files and Value-Bearing Accounting

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `.tfw/conventions.md` | MODIFY | `VALUE` | Own the single addressable session-identity grammar, resolution, collision, transport, and fallback contract. |
| `.tfw/glossary.md` | MODIFY | `VALUE` | Replace the obsolete multi-authority Session Naming statement with a pure router. |
| `.tfw/workflows/plan.md` | MODIFY | `VALUE` | Cover existing and new task checkpoints and authoritative `LEAD` substitution. |
| `.tfw/workflows/research/base.md` | MODIFY | `VALUE` | Name after task/iteration resolution and before any research write/wait; iteration is not phase. |
| `.tfw/workflows/handoff.md` | MODIFY | `VALUE` | Replace pre-state legacy Step 0 with post-item-1 `EXEC` checkpoint. |
| `.tfw/workflows/review.md` | MODIFY | `VALUE` | Replace pre-state legacy Step 0 with post-item-1 `REVIEW` checkpoint. |
| `.tfw/workflows/resume.md` | MODIFY | `VALUE` | Name selected task and only a uniquely selected phase; preserve lead binding. |
| `.tfw/workflows/docs.md` | MODIFY | `VALUE` | Apply `DOCS` only in auto/manual single-task mode; skip batch. |
| `.tfw/workflows/init.md` | MODIFY | `VALUE` | Apply `INIT` after full-init task ID creation and before state writes; skip attach/repair. |
| `.claude/commands/tfw-{plan,research,handoff,review,resume,docs,init}.md` | MODIFY | `VALUE` | Seven byte-exact tracked full-copy receivers. |
| `.agent/workflows/tfw-{plan,research,handoff,review,resume,docs,init}.md` | MODIFY | `VALUE` | Seven byte-exact tracked compatibility receivers. |
| `docs/scripts/test_runtime_context.py` | MODIFY | `ASSURANCE` | Source-derived identity projections, context accounting, and output-changing mutants. |
| `docs/scripts/test_integration.py` | MODIFY | `ASSURANCE` | Manifest-derived 7/4 classification, exact copies, clean receivers, and protected-path checks. |
| `workspace/2026/TFW_20260905-124029_RTPSN/phase-b/**` | CREATE/MODIFY | `TRACE` | Phase state, decision, evidence, result, and review lineage; never runtime input. |

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | The 23 literal paths in `$valuePaths` below: two shared authorities, seven canonical workflows, seven Claude copies, seven singular Antigravity compatibility copies |
| Baseline / selector source | `83b31ff8d6cdb879fdf4f20578fa688b48863f8a`; this TS at its owner-approval commit |
| Candidate rule | First tested Executor commit with required VALUE+ASSURANCE, before EV/RF/REVIEW/final transition; excluded-only later writes do not move it; later VALUE requires a new Candidate and recomputation |
| Logical VALUE files | 23 planned maximum; rename = one |
| Touched text LOC | 360 additions + 240 deletions = 600 planned maximum; numeric numstat fields; binary/non-text = per-file N/A |
| Triggers / disposition | Configured soft prompts: 50 VALUE files or 5,000 touched text LOC. Cause is the frozen Phase-B contract; cost is bounded central prose plus seven synchronized checkpoint triplets; assurance uses two existing test files; split would break cross-workflow consistency; authority is the owner-approved master/TS; terminal verdict is ship only on all ACs; pre-work ref is this TS approval. |
| Multiplier / authority | Immutable denominators 23 files / 600 LOC; Coordinator may add only a necessary constituent below 46 files and 1,200 LOC while every protected boundary remains fixed; owner rules at/above either multiplier boundary or from planned zero |
| Approval epoch / failure | Prospective owner approval of this TS; missing/mutable/mismatched/late baseline or Candidate = BLOCKED; metric-only inapplicability = N/A; unresolved phase attribution = INVALID; DEFERRED is non-terminal |

```powershell
$valuePaths = @(
  '.tfw/conventions.md',
  '.tfw/glossary.md',
  '.tfw/workflows/plan.md',
  '.tfw/workflows/research/base.md',
  '.tfw/workflows/handoff.md',
  '.tfw/workflows/review.md',
  '.tfw/workflows/resume.md',
  '.tfw/workflows/docs.md',
  '.tfw/workflows/init.md',
  '.claude/commands/tfw-plan.md',
  '.claude/commands/tfw-research.md',
  '.claude/commands/tfw-handoff.md',
  '.claude/commands/tfw-review.md',
  '.claude/commands/tfw-resume.md',
  '.claude/commands/tfw-docs.md',
  '.claude/commands/tfw-init.md',
  '.agent/workflows/tfw-plan.md',
  '.agent/workflows/tfw-research.md',
  '.agent/workflows/tfw-handoff.md',
  '.agent/workflows/tfw-review.md',
  '.agent/workflows/tfw-resume.md',
  '.agent/workflows/tfw-docs.md',
  '.agent/workflows/tfw-init.md'
)
$candidateSha = git rev-parse HEAD # immutable Candidate checked out before TRACE-only writes
git diff --name-status --find-renames=50% -z 83b31ff8d6cdb879fdf4f20578fa688b48863f8a $candidateSha -- $valuePaths
git diff --numstat --find-renames=50% -z 83b31ff8d6cdb879fdf4f20578fa688b48863f8a $candidateSha -- $valuePaths
```

### Prospective scope rulings

1. **A1 approved:** implement ` · @<short-stable-key>` only after exact BASE collision, only from an exposed stable host key, and only with shortest-unique-prefix plus readback evidence. Without verified uniqueness/capability, report once and continue without suffix.
2. **A2 rejected:** U+00B7 with one surrounding space is the only separator. A rename/readback mismatch is reported once; no pipe or other alternate render is emitted.
3. **Entry architecture fixed:** the current thin proxy and all 22 Codex skill source/install paths stay byte-identical to baseline. No Phase-A partial rate authorizes a production change.
4. **Workflow classification fixed:** Plan, Research, Handoff, Review, Resume, Docs, and Init are task-bound in the stated modes; Knowledge, Release, Update, and Config remain project-wide. No manual list may replace the manifest-derived verification.
5. **No new VALUE path** may hold duplicated semantics or evidence. Use the one conventions range, the seven checkpoints, the two existing assurance files, and phase TRACE.

### Task-local hard constraints (when material)

No additional M1–M6 hard constraint is declared. The grammar, protected architecture, no-guessing, A2 rejection, and CRATM boundary are acceptance/failure conditions, not an artificial operational ceiling.

**Actions (not budget dimensions):** VALUE = 23 MODIFY; ASSURANCE = 2 MODIFY; TRACE = phase state/journal/HL/TS/ONB/evidence/RF/review writes. DELETE = 0; RENAME = 0.
**Immutable owner-approved denominator:** 23 VALUE files and 600 touched text LOC; never ratchets.

## 5. Acceptance Criteria

Each synthetic gate proves only source/semantic/structural behavior. Supported-host observations prove only the named host and task metadata. Neither substitutes for model compliance or comparative human performance.

### AC-1: One exact identity authority

The selected research grammar and owner verdicts exist once and resolve deterministically.

- [ ] One uniquely addressed `.tfw/conventions.md` `Session identity` section owns `BASE := WORK " · " TASK [ " · " PHASE ]`, exactly `PLAN|RESEARCH|EXEC|REVIEW|RESUME|DOCS|INIT|LEAD`, and the navigation-only/no-authority rule.
- [ ] Modern current-grammar tasks use their owner-approved ID abbreviation only after uniqueness across configured accessible task roots is established; collision, historical grammar without an approved abbreviation, or unprovable uniqueness uses the full canonical ID; legacy `TFW-##` is preserved.
- [ ] Phase comes only from selected governing phase state/lineage, renders the uppercase bare `phase-{token}` token, and is omitted when absent, conflicting, or ambiguous; a research iteration never supplies phase.
- [ ] `LEAD` replaces `PLAN`/`RESUME` only when an already-governing binding explicitly establishes lead/main coordination; absence or ambiguity keeps the ordinary cue and creates no hierarchy.
- [ ] After an exact BASE collision, A1 uses the exposed stable key's shortest leading prefix unique among known colliding BASE sessions, then verifies readback; unavailable uniqueness/key/readback reports once and claims no suffix.
- [ ] Rename/readback failure or middle-dot corruption reports the intended canonical title and reason once, never blocks substantive work, and never emits the rejected pipe/ASCII fallback, emoji, guessed segment, or invented ordinal.
- [ ] `.tfw/glossary.md` `Session Naming` remains a `Meaning`/`Authority` router to the conventions range and contains no duplicate grammar, workflow matrix, or fallback algorithm.

Gate: source-derived parser resolves the conventions/glossary headings exactly once; independent scenario projections and semantic mutants cover every bullet.

Evidence: Full — `evidence/session-identity-contract.txt` records the resolved authority hash, grammar/vocabulary, source precedence, collision traces, failure messages, and mutant results.

### AC-2: Correct checkpoint and complete 11-route classification

Every task-bound mode applies the contract after authoritative resolution and before the first role-specific proposal, durable write, wait, or stop.

- [ ] New Plan names after the approved ID is created and before status/event/HL writes; existing Plan names after task/phase lineage resolution and before Knowledge Gate or planning proposals.
- [ ] Research names after task/iteration resolution and before folder/stage writes or waits; iteration remains excluded from phase.
- [ ] Handoff and Review remove their legacy pre-state role/pipe/full-ID Step 0 and name after Read Contract item 1, before ONB or Map activity.
- [ ] Resume names after one task resolves and includes a phase only when exactly one is selected; authoritative lead binding selects `LEAD`, otherwise `RESUME`.
- [ ] Docs names only after auto/manual Select/Triage resolves one task/phase and skips `--scan`; Init names only after full-init task-ID creation and skips attach/repair.
- [ ] Manifest-derived census classifies all 11 routes exactly once: the seven routes above with their conditional modes, and Knowledge/Release/Update/Config as project-wide with no task-oriented rename.
- [ ] Every workflow consumes the one conventions authority; local prose contains only its state-backed checkpoint, work-cue binding, and exact stop-before boundary.

Gate: targeted integration/runtime-context tests parse all 11 manifest rows, local checkpoints and ordering anchors; deletion/reorder/work-token/mode/phase/lead mutants fail at their own boundary.

Evidence: Full — `evidence/session-identity-coverage.txt` records the manifest-derived matrix, source locations, ordered anchors, produced title/skip result, and negative cases.

### AC-3: Single authority, copy parity, and measured context

The implementation adds no second algorithm, universal preload, or production entry migration.

- [ ] The central identity range is at most 260 words and each canonical workflow's local checkpoint adds at most 45 net words; exact before/after words and estimated tokens are reported for the addressed range, seven canonical workflows, seven Codex skill+workflow routes, and both tracked full-copy receiver sets.
- [ ] No root rule, skill, adapter manifest, task/project state, or project-wide workflow adds a Session identity read; only the seven task-bound/conditional routes load the addressed range in the applicable mode.
- [ ] The seven changed Claude copies and seven changed singular Antigravity compatibility copies are byte-identical to canonical workflows; all unchanged routes remain byte-identical too.
- [ ] Clean receivers generated for Codex, Claude, Cursor, and plural Antigravity contain the exact 11 routes, one Role Lock each, and the same seven/conditional identity semantics without reading tooling manifest or evidence at runtime.
- [ ] All 22 Codex skill source/install paths, `.tfw/adapters/manifest.yaml`, AGENTS/CLAUDE managed blocks, and Phase-A entry contract remain byte-identical to baseline.
- [ ] Static parity/context evidence is labelled R0/R1-style structural evidence only and makes no R2–R5, human-performance, or provider-liveness claim.

Gate: `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q`; exact byte/hash and word reports from immutable Baseline→Candidate.

Evidence: Full — `evidence/session-identity-context.txt` records per-route and aggregate word/token deltas, copy hashes, clean-receiver results, protected-selector hashes, and claim-level labels.

### AC-4: Resolution and fail-soft scenario assurance

Source-derived cases produce exact titles or explicit skip/report outcomes without relying on hand-copied expected text.

- [ ] Cases cover unique/colliding current abbreviations; legacy and dirty-clock IDs; known/absent/ambiguous/complex phases; research iteration; bound/unbound `LEAD`; exact BASE collisions with diverging stable-key prefixes; no key; no rename; no readback; and corrupted middle dot.
- [ ] Workflow-mode cases cover new/existing Plan, Research, Handoff, Review, ambiguous/single-phase Resume, Docs auto/manual/batch, Init full/attach, and all four project-wide routes.
- [ ] Produced records contain task source, phase source/omission reason, work source, BASE, suffix decision, intended title, rename/readback result, report-once result, checkpoint, and claim level.
- [ ] At least one output-changing mutant per work/task/phase/collision/transport/checkpoint/authority family changes the produced record before an independent expected projection rejects it.
- [ ] No test reads generated Phase-B evidence, the TS, or hand-authored expected records as runtime authority.

Gate: targeted semantic projection and mutant commands exposed by the existing runtime-context assurance file; normal and mutated outputs archived.

Evidence: Full — `evidence/session-identity-scenarios.json` and `evidence/session-identity-mutants.json` preserve produced records and independent rejection results.

### AC-5: Supported-host new and resumed evidence

The current Codex host demonstrates the selected grammar without expanding the claim to other hosts or to comparative human performance.

- [ ] Record exact task/thread IDs and readback for one newly created task/session title and one existing/resumed task/session title; one is `EXEC · RTPSN · B` and the existing Coordinator case is `PLAN · RTPSN · B` unless a governing binding truthfully requires `LEAD`.
- [ ] Record Unicode code points, character/word count, intended versus read-back equality, and comparison with the previous full role/ID/phase rendering.
- [ ] Retrieve/filter the task list by the literal work cue, `RTPSN`, and `B`, recording whether the full stored title remains searchable even if the visible sidebar truncates it.
- [ ] Inspect the available sidebar/title surface and record visible full/truncated/unknown honestly; no pixel width or human timing/error is inferred when the host does not expose it.
- [ ] A rename, readback, search, or visibility capability that is absent is reported once and marked `N/A`/`BLOCKED` at the affected metric without blocking valid workflow work or fabricating evidence.
- [ ] Unobserved Claude, Cursor, and Antigravity hosts are named as unobserved; current-host success is not portability proof.

Gate: current Codex task metadata/list/readback plus available UI observation; exact raw responses or bounded captures are stored in phase evidence.

Evidence: Full where exposed, otherwise explicit per-metric N/A/BLOCKED — `evidence/session-title-readback.json` and `evidence/session-title-visibility.txt` record the two cases and limits.

### AC-6: Integrated verification and immutable accounting

The final Candidate is reproducible, scoped, and green before EV/RF.

- [ ] Targeted identity, runtime-context, integration, and adapter-copy tests pass; the full `.tfw/scripts/` + `docs/scripts/` suite passes apart from a precisely attributed pre-existing failure.
- [ ] `python .tfw/scripts/gen_index.py --check project` passes. `--check tasks` reports no RTPSN defect; the known immutable RDP 123-code-point event may remain only as an attributed pre-existing result.
- [ ] All 23 VALUE paths are the only Baseline→Candidate VALUE members, fit the immutable 23-file/600-LOC denominator, and are attributed wholly to Phase B; ASSURANCE and TRACE do not move Candidate.
- [ ] Protected diffs are empty for all Codex skill source/install paths, manifest, root managed blocks, CRATM, Phase A, and the four project-wide canonical workflows.
- [ ] NUL-safe `--name-status`/`--numstat` replay records full Baseline, Candidate, membership, rename identity, numeric additions/deletions, binary N/A, trigger disposition, and approval timing.
- [ ] No placeholder, unruled deviation, duplicate authority, source/copy drift, undisposed observation, or post-Candidate VALUE remains.

Gate: targeted and full pytest; project/task checks; exact parity/protected diffs; TS §4 NUL-safe accounting commands.

Evidence: Full — `evidence/test-output.txt` and `evidence/session-identity-accounting.txt`; EV has one row per AC plus one accounting row.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-b__session_identity_ergonomics.md` | Per-AC evidence, accounting row, verdict, and attachment index (required). |
| `evidence/session-identity-contract.txt` | Resolved authority, grammar/fallback cases, hashes, and semantic mutants. |
| `evidence/session-identity-coverage.txt` | Manifest-derived workflow/mode/checkpoint matrix and negative cases. |
| `evidence/session-identity-context.txt` | Before/after words/tokens, route edges, copy hashes, protected surfaces, and claim labels. |
| `evidence/session-identity-scenarios.json` | Source-derived normal scenario records. |
| `evidence/session-identity-mutants.json` | Output-changing mutant records and independent expected rejection. |
| `evidence/session-title-readback.json` | Supported-host new/existing title metadata and exact readback. |
| `evidence/session-title-visibility.txt` | Retrieval/search/visible truncation observations and explicit limits. |
| `evidence/session-identity-accounting.txt` | Immutable Baseline/Candidate VALUE membership and NUL-safe numstat replay. |
| `evidence/test-output.txt` | Environment, targeted/full tests, task/project checks, and clean-receiver results. |

## 6. Technical Guidance

- Prefer a compact conventions-owned table/state machine and local ref-inside-step checkpoints. Workflow prose may bind `WORK` and timing, but should not restate task/phase/collision/transport rules.
- Derive classification from `.tfw/adapters/manifest.yaml` in assurance only; runtime roles must not read that tooling manifest.
- Reuse the existing unique-heading resolver, SourceTree/scenario/mutant patterns, copy installers, and word-accounting helpers where they provide independent source sensitivity.
- Capture app metadata as bounded raw evidence with stable task/thread identifiers; redact unrelated titles/content and do not convert app state into durable task authority.
- Sync full-copy receivers from canonical workflow bytes, then verify all 11 routes rather than editing copies independently.

## 7. Definition of Failure

- ❌ More than one file owns the grammar/fallback algorithm, or the glossary/workflows duplicate it.
- ❌ A workflow names before authoritative state resolution, after a role-specific proposal/write/wait/stop, or omits a required new/existing/conditional path.
- ❌ A research iteration becomes phase; an ambiguous phase is guessed; `LEAD` appears without governing authority; an abbreviation collision remains undisambiguated.
- ❌ A pipe/ASCII/emoji fallback or invented ordinal ships, or host failure blocks valid work/succeeds silently.
- ❌ Codex skills, manifest, root managed blocks, command-entry architecture, CRATM, Phase A, or project-wide workflows change beyond the approved selector.
- ❌ Fixed-context growth is unmeasured, exceeds the approved per-range/checkpoint bounds, adds a universal edge, or is justified by the inconclusive 7/54 Phase-A prefix.
- ❌ Static/parity/readback evidence is presented as model compliance, human recognition improvement, or cross-host support.
- ❌ Adapter copies drift, a clean receiver loses an 11-route/Role-Lock contract, or generated evidence becomes a runtime input.
- ❌ Candidate/accounting authority is missing, late, mutable, mismatched, over 23 VALUE files/600 touched LOC, or includes sibling work.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Central semantics add repeated fixed context to seven routes | Address one ≤260-word range, keep checkpoints ≤45 net words, measure exact per-route and aggregate deltas. |
| Prose assurance passes while semantics drift | Produce source-derived scenario records and output-changing mutants with independent expected projections. |
| App tools expose storage but not sidebar pixels/search | Record exact readback/retrieval, visible observation when available, and explicit N/A/BLOCKED limits without widening claims. |
| Stable keys or colliding-session census are unavailable | Keep BASE, report unresolved collision once, continue, and never invent a suffix. |
| Existing full-copy receivers are edited independently | Modify canonical workflows first, copy exact bytes, verify all 11 current and clean receiver routes. |
| Concurrent master/shared changes land during execution | Executor works in one isolated task worktree; Coordinator merges reviewed lines and refreshes master before knowledge gates. |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| `.tfw/conventions.md` | Phase A | Append/modify only the Phase-B Session identity range; preserve the reviewed entry sequence and R0–R5 ladder. |
| `docs/scripts/test_runtime_context.py` | Phase A | Extend existing source-derived semantics/context tests; preserve all Phase-A entry claims and mutants. |
| `docs/scripts/test_integration.py` | Phase A | Extend the manifest/copy/clean-receiver checks; do not weaken Phase-A 11×4 gates. |

---

*TS — TFW_20260905-124029_RTPSN / Phase B: Session Identity Ergonomics | 2026-09-05*
