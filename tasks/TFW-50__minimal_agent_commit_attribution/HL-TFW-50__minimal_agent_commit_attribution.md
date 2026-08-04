# HL — TFW-50: Minimal Agent Commit Attribution

> **Date**: 2026-08-04
> **Author**: Codex / Coordinator
> **Status**: ✅ HL — Revised and approved from RES Iteration 1

## 1. Vision

Every AI-authored commit is understandable directly in `git log`: who acted, for which task and scope, under which TFW role, and what changed. One precise Markdown rule achieves this without enforcement software.

**Impact:** Humans and agents can find task, phase, and role history without reconstructing session context.

> “Keep the readable result, remove the machinery.”

## 2. Current State (As-Is)

| Area | Current state |
|------|---------------|
| Baseline | Commit `bc6779e` restores and publishes the exact `v0.9.0` tracked tree; TFW-48/49 remain history only |
| Hooks | Local/global `core.hooksPath` are unset. A legacy default `.git/hooks/prepare-commit-msg` was discovered when it prefixed the first local plan commit; the hook was removed and the unpushed commit was amended |
| Rule | Conventions contain no agent commit-subject rule |
| Reach | Every supported agent entry path already loads conventions |
| Conflict | Handoff Step 4 couples “Commit and push ONB” |
| Release conflict | Active `RELEASE.md` still prescribes the un-attributed subject `release: vX.Y.Z` and unconditional push |
| Existing adapter drift | Canonical handoff and its Antigravity/Claude copies already differ in the Evidence block; TFW-50 will disclose and preserve that unrelated drift, not absorb it |
| Useful result | `[codex/TFW-49/phase-c/reviewer] ...` was readable; its Python/schema/hook/runtime system was rejected |
| Planning gap | The first TFW-50 TS treated Executor/handoff as the main commit path, although Coordinator, Researcher, Reviewer, and Coordinator-owned lifecycle workflows also create commits |

## 3. Target State (To-Be)

**Commit Attribution** means declared context in an AI-authored commit subject. It improves trace readability; it does not authenticate the actor.

The complete rule is one sentence:

> Every AI-authored commit MUST use `[agent/task/scope/role] summary`: set `agent` to the lowercase AI product name from explicit context, `task` to the canonical TFW task ID (`project` only when none exists), `scope` to the established lowercase work-slice slug or a lowercase hyphenated form of its explicit label, and `role` to the lowercase canonical TFW workflow owner from §15/Role Lock; keep `summary` short and imperative, commit locally, and push only after explicit user approval.

```text
[codex/TFW-50/task/coordinator] define minimal commit attribution
```

#### Terminology Contract

| Term | Exact meaning |
|------|---------------|
| **Commit Attribution** | Declared structured prefix in the first-line subject of an AI-authored commit; separate from Git author/committer metadata and never authentication |
| `agent` | Lowercase AI product name from explicit context, such as `codex` or `claude`; not a person, model, account, Git author, or Git committer |
| `task` | Canonical TFW task ID; `project` only when no task exists |
| `scope` | Established lowercase explicit work-slice slug, or a lowercase hyphenated form of its explicit label; open normalized text, not a registry |
| `role` | Lowercase canonical TFW workflow owner from conventions §15, confirmed by Role Lock where present: `coordinator`, `researcher`, `executor`, or `reviewer` |
| `summary` | Short imperative description of the change; no numeric length target |

Values are separated by `/`, enclosed once in `[]`, followed by one space and the summary. Unmarked commits are not assumed to be human-authored.

Terms intentionally not used: **Commit Identity** or **actor** (authentication implication), **surface** (adapter channel rather than the user-visible agent), and model/session/account/trailer fields (no value for the requested search).

The rule governs subjects of commits that occur. It does not require a commit at every stage, WAIT, STOP, workflow, artifact, or file.

### 3.1 Result Visualization

| Before | After |
|--------|-------|
| `update files` | `[codex/TFW-50/phase-a/executor] add commit attribution rule` |
| Context must be reconstructed | Agent, task, scope, role, and change are searchable |
| Local completion can imply push | Publication requires explicit user approval |

### 3.2 Value Flow

`explicit context → compact subject → readable history → faster handoff and audit`

### 3.3 Exact Change Surface

#### Final implementation/verification surface: six existing files, zero new framework files

| # | Path | Exact intended change |
|---|------|-----------------------|
| 1 | `.tfw/conventions.md` | **Refine** the existing sole normative sentence and example with exact `agent`, `task`, `scope`, `role`, and metadata boundaries |
| 2 | `.tfw/glossary.md` | **Refine minimally**: concise definition, owner link, and separation from Git author/committer metadata; no second rule |
| 3 | `.tfw/workflows/handoff.md` | **Preserve + verify** the corrected Step 4 attribution and separate push approval; add no cadence rule |
| 4 | `.agent/workflows/tfw-handoff.md` | **Preserve + verify** the same Step 4 correction; preserve unrelated pre-existing Evidence drift |
| 5 | `.claude/commands/tfw-handoff.md` | **Preserve + verify** the same Step 4 correction; preserve unrelated pre-existing Evidence drift |
| 6 | `RELEASE.md` | **Preserve + verify** the attributed release example and explicit push approval |

#### Workflow traces, not implementation scope

TFW-50 will also create or update its normal task traces: `README.md` Task Board, TS, ONB, EV, RF, review stage files, and REVIEW. `KNOWLEDGE.md` or `TECH_DEBT.md` may change only after approved review through their own explicit triage; they are not pre-approved implementation files.

#### Explicit no-write boundary

No changes to Git hooks/config/history, Python or other scripts, schemas, manifests, state/config files, adapter entry prompts, Codex skills, unrelated workflows, historical task artifacts, or version files.

#### Verified consumer model

RES Iteration 1 inventoried 72 workflow/adapter paths plus root entry files and history. Coordinator, Researcher, Executor, and Reviewer all produce commits, but all load conventions. Therefore universal applicability covers every role without copying the rule into every workflow. Additional edits are required only where existing text contradicts the subject rule or push boundary; handoff and active release guidance were the only such conflicts.

## 4. Phases

### Phase A: Universal Rule and Conflict Reconciliation 🔴

- Refine the sentence and example in `.tfw/conventions.md` as the sole owner.
- Refine only the concise term definition in `.tfw/glossary.md`.
- Preserve and verify the already-correct handoff and release conflict reconciliations.
- Verify all-role applicability across canonical workflows, adapters, and actual TFW-50 subjects without adding workflow cues or commit cadence.

## 5. Definition of Done (DoD)

- ✅ 1. Conventions solely own the exact `[agent/task/scope/role] summary` rule.
- ✅ 2. Glossary defines the term concisely and links to the owner without duplicating the rule.
- ✅ 3. The universal rule applies to Coordinator, Researcher, Executor, and Reviewer without role-specific duplication or new commit cadence.
- ✅ 4. The canonical and installed handoff Step 4 wording is semantically identical and no longer treats ONB completion as push authority.
- ✅ 5. Pre-existing non-commit handoff drift is measured and remains byte-for-byte unchanged outside Step 4.
- ✅ 6. `RELEASE.md` uses the format and makes push conditional on explicit user approval.
- ✅ 7. No Python, hook, executable, schema, registry, manifest, state, config, trailer protocol, validator, or cadence policy is added.
- ✅ 8. Representative Coordinator, Researcher, Executor, and Reviewer commits conform by direct `git log` inspection; causality and authentication are not claimed; existing docs tests pass.

## 6. Definition of Failure (DoF)

- ❌ 1. Any runtime enforcement or new framework file is introduced.
- ❌ 2. The full rule is duplicated in adapters or workflows.
- ❌ 3. Attribution is presented as actor authentication or human/agent detection.
- ❌ 4. Local completion is presented as permission to push.
- ❌ 5. Model, account, session, branch, trailers, or other fields expand the format.
- ❌ 6. Unrelated handoff Evidence drift is silently synchronized or otherwise changed.
- ❌ 7. History is rewritten, or implementation exceeds the six named files without explicit approval.
- ❌ 8. A per-stage, per-STOP, per-workflow, per-artifact, or per-file commit cadence is introduced.

**On failure:** remove the added mechanism or duplication and return to this HL.

## 7. Principles

1. **Outcome over mechanism** — retain readable subjects, not the rejected system.
2. **Naming creates behavior** — four exact labels replace explanatory prompt volume.
3. **Single source of truth** — one owner, one short action cue.
4. **Declared context, not identity proof** — the subject is a trace supplied by the agent.
5. **Human publication authority** — commit and push are separate decisions.
6. **Proportional completeness** — keep the runtime instruction compact, but let planning traces be as complete as the decision requires; document length is not a quality target.
7. **Transparent boundaries** — name every intended file, known inconsistency, and non-claim before execution.

### 7.2 Knowledge Citations

| # | Source | Item | Application |
|---|--------|------|-------------|
| 1 | `.tfw/README.md` | Traces Over Code | Make Git history a useful trace |
| 2 | `.tfw/README.md` | Naming Creates Behavior | Let field names carry the instruction |
| 3 | `.tfw/README.md` | Single Source of Truth; Portability | One Markdown owner, no runtime |
| 4 | `KNOWLEDGE.md` §1 | D15, D23 | Keep adapters thin and remove repeated prose |
| 5 | `KNOWLEDGE.md` §1 | D24, D28 | Keep a short action cue; use precise terminology |
| 6 | `knowledge/philosophy.md` | F22 | Do not bloat prompt or template surfaces |
| 7 | `knowledge/process.md` | F3, F4 | Exact naming plus an action step beats an info dump |
| 8 | `knowledge/process.md` | F6, F22 | Prevent coordinator scope explosion and generic overhead |
| 9 | `.tfw/conventions.md` §11 | Token density; Progressive Disclosure | Minimize context cost |
| 10 | `knowledge/convention.md` | F5 | Canonical workflows own adapter behavior; derived drift must be explicit |

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| Exact `v0.9.0` tracked tree restored and pushed | ✅ `bc6779e` |
| Local/global `core.hooksPath` absent | ✅ |
| Agent entry paths already load conventions | ✅ |
| Knowledge Gate: task 50 − consolidation 46 = 4, below interval 5 | ✅ |

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Agent overlooks the canonical sentence | Medium | Medium | Mandatory conventions loading plus representative all-role subject audit; do not overclaim causality |
| `scope` varies | Medium | Low | Use the current named phase or workflow slice; provide one example |
| Existing handoff drift gets mistaken for TFW-50 work | Medium | Medium | Snapshot it; change only Step 4; report it separately |
| Design expands again | Low | High | Exact six-file implementation scope and no-infrastructure DoF |

## 10. RESEARCH Case

### Research Result

RES Iteration 1 completed a bounded inventory after the first audit treated Executor/handoff as representative. It found that all four roles commit, but universal conventions loading covers applicability. The decisive correction was to separate commit formatting from commit cadence.

### Hypotheses

| # | Hypothesis | Status |
|---|------------|--------|
| H1 | One canonical owner plus edits only for contradictory instructions is sufficient across all roles | refined and supported |
| H2 | `[agent/task/scope/role] summary` uses the smallest precise term set for the user's searches | supported with exact term refinement |
| H3 | Semantic owner, conflict point, always-loaded reference, and derived copy require different treatment | supported |
| H4 | Prompt compliance is sufficient for readable declared context when authentication and automated enforcement are out of scope | bounded support; current prompted history is non-causal |

### Risks of Not Researching

Closed by RES: the six-file surface is complete because the rule is universal, not because Executor represents other roles. The remaining risk is overstating observed prompted compliance as causal proof.

### Proposed RESEARCH Focus

**Decision: research complete and sufficient.** Selected C7: one conventions owner, one glossary reference, and reconciliation only where existing text conflicts. No second iteration, new mechanism, workflow-wide cue broadcast, or cadence policy.

### Why Not Just...?

- Keep TFW-49? — readable outcome, rejected mechanism.
- Use hooks or a validator? — unnecessary lifecycle and portability cost.
- Repeat the rule in adapters? — conventions are already loaded; repetition adds drift.
- Add Conventional Commits or trailers? — they solve a different problem and add context.

## 11. Strategic Insights (Planning)

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | Codex handled TFW-48 and TFW-49 badly: it expanded the mechanism, optimized workflow artifacts, and lost the user's original cleanup goal. Both tasks are rejected attempts whose history is retained as a warning | process | User, rollback decision and explicit correction |
| S2 | The four-part readable prefix was useful; its software enforcement was not | convention | User, TFW-50 direction |
| S3 | Old Git hooks are unnecessary and must not be restored | constraint | User, cleanup direction |
| S4 | Push is a separate explicit user decision | process | User, publication correction |
| S5 | This task must demonstrate precise terms, short wording, linear behavior, and no hidden branches | philosophy | User, TFW-50 direction |
| S6 | TFW has no HL length limit. Brevity is not a universal objective: instructions should be concise where precision permits, while HL and other traces should remain proportionate and complete | philosophy | User, correction after TFW-50 HL draft |
| S7 | Precision includes an exact file inventory and explicit terminology before approval; unknowns should trigger bounded research rather than hidden assumptions | philosophy | User, request to complete TFW-50 HL |
| S8 | Commit Attribution must cover every commit-producing TFW role, including Researcher, not only Executor/handoff; minimality must be measured against complete behavior rather than file count alone | process | User correction after initial TFW-50 execution began |

---

*HL — TFW-50: Minimal Agent Commit Attribution | 2026-08-04*
