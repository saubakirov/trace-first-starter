# RES — TFW-15: Pipeline Formalization

> **Date**: 2026-04-01
> **Author**: Coordinator (AI)
> **Status**: ✅ RES — Complete
> **Parent HL**: [HL-TFW-15](HL-TFW-15__pipeline_status_rename.md)
> **Mode**: Pipeline

---

## Research Context
TFW-15 proposes decoupling process statuses from document types, adding a centralized status registry to PROJECT_CONFIG.yaml, formalizing a concept taxonomy in the glossary, and renumbering the Phase 3.5 hack in plan.md. This research validates design decisions, identifies hidden conflicts, and challenges assumptions before HL finalization.

## Briefing (4 turns)

### Research Plan
1. **Gather** — Audit all pipeline string locations, catalog status-document coupling
2. **Extract** — Analyze interactions between statuses and workflows/templates/adapters
3. **Challenge** — Test naming semantics, evaluate alternatives, question Document Status

### Scope Intent
- **In scope:** Pipeline strings, status registry, concept taxonomy, Phase 3.5 renumber, transition matrix, template status markers
- **Out of scope:** Adapter commands (.claude/, .agent/), archived tasks (TFW-{1..14}/)

### Briefing Decisions
- **Variant D selected** — 8 statuses (same count as now), rename `🔵 HL` → `📝 HL_DRAFT` and `🟡 TS` → `🟡 TS_DRAFT`
- **Naming pattern**: `{DOC}_DRAFT` = document in progress. Bare `{DOC}` not used as board status — approval implicit in transition
- **HL_READY rejected** — inconsistent (no TS_READY etc.), dead state
- **Document Status (DRAFT/APPROVED in file headers)** — deferred to end of research
- **Taxonomy** — keep as TODO, not a full section
- **Phase 3.5 renumber** — confirmed (→ Phase 4, current Phase 4 → Phase 5)

→ User direction: proceed to Gather

## Decisions
| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Variant D: 8 statuses, rename only | Minimal diff, AI-friendly descriptive names, proven count |
| D2 | HL_DRAFT + TS_DRAFT naming pattern | Consistent `_DRAFT` suffix, self-documenting for AI |
| D3 | No HL_READY / HL_DONE board status | Dead state — transition to next status = implicit approval |
| D4 | Status registry with `role` field, no `transitions` | Registry = single source of truth (TFW-12 precedent). Transitions deferred to future-work |
| D5 | REJECT = user decision point, not fixed path | User chooses: HL_DRAFT / RES / TS_DRAFT |
| D6 | Fix plan.md step numbering in-passing | Pre-existing tech debt, touching same file |
| D7 | Drop Document Status lifecycle from TFW-15 scope | No one reads DRAFT/APPROVED machine-readably. Headers still updated to match new status names |
| D8 | 📝 emoji for HL_DRAFT | Visually says "drafting", distinct from 🔵 |

## Open Questions
| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Status registry in PROJECT_CONFIG.yaml — needed? | ✅ Closed | Yes — for AI automation (D4) |
| Q2 | Document Status (DRAFT/APPROVED in headers) — in scope? | ✅ Closed | Out of scope (D7). Headers updated to match new status names only |
| Q3 | Concept Taxonomy — full glossary section or just TODO? | ✅ Closed | TODO — don't bloat docs |
| Q4 | ONB → TS refinement loop — formalize? | ✅ Closed | No — implicit convention, coordinator can refine TS during ONB |

---

## Stage: Gather — "What do we NOT know?"

### Pipeline string audit

Found the old pipeline string `⬜ TODO → 🔵 HL → 🔬 RES → 🟡 TS → ...` in these **live files** (need modification):

| # | File | Line(s) | What | Notes |
|---|------|---------|------|-------|
| 1 | `.tfw/conventions.md` | 98, 103 | Pipeline diagram + skip path | Also status table at L107-117 |
| 2 | `.tfw/glossary.md` | 48, 53 | Status Flow section | Also count "8 statuses" at L57 |
| 3 | `.tfw/README.md` | 127-128 | Task Lifecycle diagram | Also "8-status lifecycle" at L280 |
| 4 | `.tfw/workflows/plan.md` | 60, 143, 148 | Phase step + Status Transitions | L60: "add task with status `🔵 HL`" |
| 5 | `.tfw/workflows/research.md` | 278, 280 | Status Transitions section | Pipeline/Standalone/Skip paths |
| 6 | `README.md` (root) | 90, 128 | Key Concepts + Task Board legend | |
| 7 | `.tfw/templates/HL.md` | 5 | `🔵 HL — Ожидает ревью` | → `📝 HL_DRAFT — Ожидает ревью` |
| 8 | `.tfw/templates/TS.md` | 5 | `🟡 TS — Ожидает апрува` | → `🟡 TS_DRAFT — Ожидает апрува` |
| 9 | `.tfw/workflows/handoff.md` | 58, 62 | `🟠 ONB` and `🟢 RF` status refs | These don't change (ONB/RF stay) |

**Not affected:**
- `.tfw/workflows/review.md` — no emoji status refs
- `.tfw/workflows/resume.md` — no emoji status refs
- `.tfw/adapters/` — only mention "status" in README.md directory listing, no pipeline strings
- `tasks/TFW-{1..14}/` — archived, not touched

**CHANGELOG note:** `.tfw/CHANGELOG.md` mentions "Phase 3.5" 3 times (L15, L21, L72) — these are historical entries, should NOT be changed.

### New pipeline string (Variant D)

```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE
                          (skip: 📝 HL_DRAFT ··· 🟡 TS_DRAFT)
```

### Checkpoint: Gather
| Found | Remaining |
|-------|-----------|
| 9 files need changes (7 pipeline strings, 2 templates) | Status registry design for PROJECT_CONFIG.yaml |
| CHANGELOG Phase 3.5 refs = historical, don't touch | Exact transition matrix wording |
| handoff.md refs ONB/RF statuses — unchanged | TS_DRAFT implications for current task board entries |
| Adapters unaffected | |

**Agent assessment:** Gather is complete — all affected locations cataloged. No surprises found. The scope is clean.
**Recommendation:** close Gather, proceed to Extract.
**Stage Handoff:** For Extract I plan to analyze: (1) how TS_DRAFT interacts with the existing handoff and ONB flow, (2) whether the status table in conventions.md needs semantic updates beyond the pipeline string, (3) what the status registry YAML should look like. Any additions?

→ User decision: ___

## Stage: Extract — "What do we NOT see?"

### Finding E1: TS_DRAFT + Handoff interaction — clean

`handoff.md` says "Input: Approved HL + TS files". Executor starts AFTER user approves TS. Board shows `🟠 ONB` at that point. So:
- `🟡 TS_DRAFT` on board = "coordinator wrote TS, user reviewing"
- Transition `TS_DRAFT → ONB` = user approved TS, executor started
- Handoff workflow doesn't reference TS status emoji — no code change needed there

Same pattern as HL_DRAFT: approval is implicit in the transition to next status.

### Finding E2: Status table descriptions — semantic shifts

Current conventions.md L107-117:

| Current | New | Change |
|---|---|---|
| `🔵 HL` → "HL written, awaiting review/approval" | `📝 HL_DRAFT` → "HL in draft, awaiting review/approval" | "written" → "in draft" (more accurate for _DRAFT) |
| `🟡 TS` → "TS written, awaiting approval for execution" | `🟡 TS_DRAFT` → "TS written, awaiting approval for execution" | Same meaning, only label changes |
| `🔬 RES` → "Research in progress (optional — user can skip to TS)" | → "...can skip to TS_DRAFT" | Update skip path ref |

Minor changes. No semantic surprises.

### Finding E3: plan.md step numbering — already broken

Step numbers in plan.md: 1, 2, 3, 4 (Phase 1) → 5, 6, 7 (Phase 2) → **9**, 10, 11 (Phase 3 — step 8 missing) → Phase 3.5 uses internal 1, 2, 3 → 12a/12b, 13a/13b, 14a/14b (Phase 4).

If we renumber Phase 3.5 → Phase 4 and Phase 4 → Phase 5, should we also fix the step numbering gap? This is pre-existing tech debt, not TFW-15 scope, but touching the same file.

**Recommendation:** fix step numbering as cleanup-in-passing if it's ≤5 lines of change. Otherwise, TECH_DEBT.

### Finding E4: Review verdict paths + new names

Conventions.md L124-127:
```
- ✅ APPROVE → ✅ DONE
- 🔄 REVISE → back to execution (same task)
- ❌ REJECT → new task with HL/TS
```

With rename: REJECT path should say "back to HL_DRAFT" (not "new task with HL/TS" — HL_DRAFT is the status they return to). Currently `REJECT` says "new task with HL/TS" — but the transition matrix in HL-15 says `REV → 📋 PLAN` (back to planning). In Variant D, this should be `REV → 📝 HL_DRAFT`.

**Subtle:** REJECT could mean (a) fix the current task's HL or (b) create a whole new task. Current wording implies (b). Need to clarify.

### Finding E5: `(develop)` in pipeline string — phantom status

The pipeline string contains `🟠 ONB → (develop) → 🟢 RF`. The `(develop)` is not a real status — it's an annotation showing "work happens here". But it takes space in the diagram and is inconsistent — no other transition has an inline annotation.

Options:
- Keep `(develop)` — it's useful context
- Remove it — `🟠 ONB → 🟢 RF`
- This is not a TFW-15 concern but worth noting

### Finding E6: Status registry design

Proposed `tfw.statuses` structure for PROJECT_CONFIG.yaml:

```yaml
tfw:
  statuses:
    - id: TODO
      emoji: "⬜"
      description: "Task registered, work not started"
    - id: HL_DRAFT
      emoji: "📝"
      description: "HL being drafted or discussed"
      role: coordinator
    - id: RES
      emoji: "🔬"
      description: "Research in progress (optional)"
      role: coordinator
    - id: TS_DRAFT
      emoji: "🟡"
      description: "TS written, awaiting approval"
      role: coordinator
    - id: ONB
      emoji: "🟠"
      description: "Executor onboarding"
      role: executor
    - id: RF
      emoji: "🟢"
      description: "Execution complete, RF written"
      role: executor
    - id: REV
      emoji: "🔍"
      description: "Review in progress"
      role: reviewer
    - id: DONE
      emoji: "✅"
      description: "Task closed"
    - id: BLOCKED
      emoji: "❌"
      description: "Blocked by dependency"
```

**Design choices:**
- `role` field connects statuses to roles (user's request)
- No `label` field — `id` IS the label (KISS)
- No `transitions` list — deferred (automation future-work). Transitions stay in conventions.md prose
- TODO/DONE/BLOCKED have no `role` — they're boundary states

### Finding E7: glossary.md Phase definition — implicit status reference

Glossary L69: "Each phase has its own HL → TS → ONB → RF → REVIEW cycle." This uses bare document names, not status names. With rename, should this be `HL_DRAFT → TS_DRAFT → ONB → RF → REVIEW`?

**No.** This sentence describes the artifact cycle, not the status cycle. HL, TS, ONB, RF, REVIEW are **document types** here, not statuses. This is exactly the decoupling TFW-15 achieves — document type names ≠ status names. This sentence stays as-is.

### Checkpoint: Extract
| Found | Remaining |
|-------|-----------|
| E1: TS_DRAFT + handoff = clean, no code change in handoff.md | |
| E2: Status descriptions — minor text updates | |
| E3: plan.md step numbering already broken (pre-existing) | Decide: fix or TECH_DEBT |
| E4: REJECT verdict wording needs clarification | Decide: fix or leave |
| E5: `(develop)` phantom annotation — cosmetic | Decide: keep or drop |
| E6: Registry design with `role` field, no transitions | User approval needed |
| E7: Glossary Phase definition stays as-is (document types ≠ statuses) | |

**Agent assessment:** Extract revealed useful hidden patterns. E3 (step numbering) and E4 (REJECT wording) are the most actionable. E6 (registry design) needs user input on `role` field. E7 confirms the design is correct — document types and statuses are properly decoupled.
**Recommendation:** close Extract, proceed to Challenge.
**Stage Handoff:** For Challenge I plan to test: (1) what if we DON'T add `tfw.statuses` to config and just update prose? (2) is `📝` the right emoji for HL_DRAFT? (3) does `_DRAFT` suffix create confusion with Document Status (DRAFT/APPROVED in headers)?

→ User decision: ___

## Stage: Challenge — "What do we NOT expect?"

### Challenge C1: What if we skip the registry and just rename in prose?

**Alternative:** Don't add `tfw.statuses` to PROJECT_CONFIG.yaml. Just rename the pipeline strings in existing docs.

- **Pro:** Fewer changes (7 files instead of 8). No YAML maintenance.
- **Con:** User explicitly said they want AI not to get confused with automation. Prose can drift — we already proved this in TFW-12 (D16: "Drift proven across TFW-5/8/9/11 — each new template/workflow caused multi-file desyncs").
- **Verdict:** Registry needed. Single source of truth principle. The `role` field is bonus value for automation.

### Challenge C2: `_DRAFT` suffix vs Document Status — naming collision risk

If the board status is `HL_DRAFT` and the file header says `📋 DRAFT — Ожидает ревью`, is that confusing?

**No.** They answer different questions:
- Board status `📝 HL_DRAFT` = "where is the TASK in the pipeline?"
- File header `DRAFT` = "what is the STATE of THIS DOCUMENT?"

A task at status `🔬 RES` can have an HL file with header `DRAFT` (not yet finalized). After research, coordinator updates HL and changes header to `APPROVED`. The board status at that point transitions to `🟡 TS_DRAFT`.

**But:** the word "DRAFT" appears in both. AI models might parse `HL_DRAFT` as "HL whose Document Status = DRAFT". This is technically correct — but it's a coincidence, not a design link.

**Mitigation:** if we keep Document Status in scope, use different words. File header: `📋 DRAFT` vs `🔵 APPROVED`. Board status: `HL_DRAFT`. Or — simplest — drop Document Status from TFW-15 scope entirely. The user already leaned this way.

### Challenge C3: `📝` emoji — is it right?

`📝` = "memo" — represents a document being written. Fits `HL_DRAFT`.

Alternatives:
- `🔵` (keep current, just change label) — minimal visual disruption but loses the semantic shift
- `📋` (clipboard) — was PLAN in HL-15, might cause confusion with rejected variant
- `✏️` (pencil) — too generic

**Recommendation:** `📝` is good. It visually says "drafting" which is exactly the semantics.

Note: `🟡` stays for TS_DRAFT (same emoji as current TS). Two _DRAFT statuses with different emojis is fine — emoji = identity, not pattern.

### Challenge C4: What if we just keep `🔵 HL` and `🟡 TS`?

**The "do nothing" option.** Add the registry, add roles, fix Phase 3.5 — but don't rename statuses.

- **Pro:** Minimum disruption. Everyone already knows `🔵 HL`.
- **Con:** Doesn't solve the original problem (HL §1.1): `🔵 HL` means both "writing HL" and "HL on review". The ambiguity stays. With automation, this matters — agent at `🔵 HL` doesn't know: "should I write HL or is HL done?"
- **Counter-argument:** Agent can check if HL file exists. If yes → HL is written. If no → need to write it.
- **Counter-counter:** What if HL exists but is being revised after REJECT? Same status, different action needed.

**Verdict:** Rename to `HL_DRAFT` makes the status self-documenting. The ambiguity is worth fixing. The cost is low (text replace in 8 files).

### Challenge C5: Board width with `HL_DRAFT` / `TS_DRAFT`

Board line comparison:
```
Current:  | TFW-15 | Pipeline formalization | 🔵 HL |
Proposed: | TFW-15 | Pipeline formalization | 📝 HL_DRAFT |
```

`HL_DRAFT` is 8 chars vs `HL`'s 2. Status column gets wider. For AI — irrelevant (reads strings). For human glancing — emojis do the work, text is secondary.

**Verdict:** Non-issue. Board readability depends on emoji, not text width.

### Challenge C6: REJECT path — user's clarification

User said: "REJECT возвращает нас к юзеру, надо у него спрашивать вариант: начинать с research или с постановки TS."

This means REJECT is NOT a fixed transition. It's a decision point:
```
🔍 REV → ❌ REJECT → 🛑 User decision:
                         (a) → 📝 HL_DRAFT (rework HL from scratch)
                         (b) → 🔬 RES (new research needed)
                         (c) → 🟡 TS_DRAFT (HL is fine, rewrite TS)
```

This is more nuanced than a fixed `REV → HL_DRAFT` transition. The transition matrix should show this as a branching point, not a single arrow.

### Checkpoint: Challenge
| Found | Remaining |
|-------|-----------|
| C1: Registry needed — single source of truth | — |
| C2: _DRAFT vs Document Status — no collision, but drop Doc Status from scope | — |
| C3: 📝 is the right emoji | — |
| C4: "Do nothing" rejected — ambiguity is worth fixing | — |
| C5: Board width — non-issue | — |
| C6: REJECT = branching decision point, not fixed path | Need to reflect in transition matrix |

**Agent assessment:** All challenges answered. No showstoppers found. The design is sound. Key refinement: REJECT path is a user decision point (C6), not a fixed transition. Document Status should drop from TFW-15 scope (C2).
**Recommendation:** close Challenge, proceed to Final Checkpoint.

→ User decision: ___

---
## Final Checkpoint

| Stage | Status | Key Findings |
|-------|--------|-------------|
| Gather | ✅ | 9 files need changes. Adapters unaffected. CHANGELOG historical — don't touch. |
| Extract | ✅ | TS_DRAFT+handoff clean. Step numbering broken (fix). REJECT=branching. Registry design with `role`. Document types ≠ statuses confirmed. |
| Challenge | ✅ | Registry needed (C1). 📝 emoji right (C3). Do-nothing rejected (C4). Document Status deferred (C2). REJECT=user choice (C6). |

### Sufficiency Check
**Question:** Sufficient for HL finalization? Can we confidently define phases, approach, and dependencies?
**Self-check:**
- Are there unclosed Open Questions in RES? **No — all 4 closed.**
- Did all stages produce substantive findings or were any perfunctory? **All substantive: Gather=audit, Extract=7 findings, Challenge=6 tests.**
- Is the solution proportionate to the problem scale? **Yes — 8-file rename + 1 config addition. No over-engineering.**
- Are phases, boundaries and dependencies clear enough to finalize HL? **Yes — single-phase task, file list complete, design validated.**
**Agent assessment:** Research is sufficient. The design is validated, scope is clear, all questions answered. HL needs update to reflect Variant D (not original 10-status PLAN+HL proposal). Ready for HL finalization.
→ User decision: ___

**Verdict:** Sufficient for HL finalization

## Closure

### HL Update Recommendations

| # | What to update in HL | Source |
|---|---------------------|--------|
| 1 | **Pipeline:** replace `PLAN → RES → HL → TS` with `HL_DRAFT → RES → TS_DRAFT` (Variant D, 8 statuses) | D1, D2 |
| 2 | **Status Registry:** update YAML example — rename ids, add `role` field, remove `label` field | D4, E6 |
| 3 | **Transition Matrix:** update status names + REJECT as branching user decision point | D5, C6 |
| 4 | **Concept Taxonomy §2.1:** keep but simplify — Document Status row removed (out of scope) | D7 |
| 5 | **File list §3:** add `TS.md` template (missed). Total: 9 files, not 8 | Gather |
| 6 | **Phase 3.5:** confirm renumber + fix step numbering in plan.md | D6, E3 |
| 7 | **Emoji:** `📝` for HL_DRAFT, `🟡` stays for TS_DRAFT | D8, C3 |
| 8 | **DoD:** update pipeline string, remove grep for `🔵 HL →` (new target: `🔵 HL`), add grep for old pipeline | Gather |
| 9 | **REJECT verdict in conventions.md:** update to branching decision point | C6 |

### Next Step
Coordinator updates HL with these 9 recommendations → presents updated HL to user → user confirms → proceed to TS.

→ User decision: ___

## Conclusion

Researched TFW-15 pipeline formalization across 4 briefing turns, 3 stages, 1 pass. Key contribution: rejected the original 10-status PLAN+HL proposal in favor of Variant D — 8 statuses with descriptive `_DRAFT` suffix (`HL_DRAFT`, `TS_DRAFT`). This preserves the proven status count while solving the ambiguity problem. Research uncovered: TS template was missing from the file list (+1 file), plan.md step numbering was already broken (fix in-passing), REJECT verdict needs user branching (not fixed path), and Document Status lifecycle should be deferred. Registry design includes `role` field for future automation. Self-critique: the Briefing phase took 4 turns to converge on naming — could have proposed Variant D earlier instead of presenting abstract role-group options first.

---

*RES — TFW-15: Pipeline Formalization | 2026-04-01*
