# HL — TFW-50: Prompt-First Session and Commit Identity

> **Date**: 2026-07-31
> **Author**: Coordinator (Codex) + User
> **Status**: ✅ HL — Approved by user on 2026-08-01
> **Owner correction**: The user rejected TFW-49 as a complete product-fit failure and
> explicitly selected a prompt-only replacement with no required Python or Git hooks.
> **Publication boundary**: Local work only. No push, remote tag, deploy, publish,
> notify, or host escalation is authorized.

---

## 1. Vision

Every TFW agent understands why session and commit names matter and writes them in one
small, readable format from the explicit current task context. The method remains a
prompt-and-agent discipline: no validator service, schema registry, router, runtime,
hook installation lifecycle, or audit subsystem is needed to obtain searchable Git
history.

**Impact:** Humans and agents can recognize task, work slice, role, and agent surface
at a glance, while TFW becomes smaller and easier to understand instead of turning a
naming convention into software.

> “It only needed one precise sentence in the prompts: give agents the format and
> explain its purpose.”

## 2. Current State (As-Is)

TFW-49 selected a useful subject format but implemented the wrong product:

| Current result | Observed cost | Product-fit verdict |
|----------------|--------------:|---------------------|
| Schema, tracked state, state template | 199 lines | Rejected: unnecessary owner layers |
| Three Python production programs | 2,879 lines | Rejected: methodology became software |
| Three Python test programs | 2,801 lines | Rejected: proof volume protects unwanted machinery |
| Manifest and two repository hooks | 31 lines | Rejected: local enforcement is not required |
| **Runtime-only total** | **12 files / 5,910 lines** | **Delete completely** |

The current clone also has repository-local `core.hooksPath=.tfw/hooks` and a private
runtime ledger. The user-global `core.hooksPath` has already been unset without reading
or disclosing external hook contents. TFW-49 phases and commits remain as the trace of
the failed decision; no history rewrite is required.

## 3. Target State (To-Be)

One concise semantic owner explains the two related names:

```text
Session: <Role> | <Task-ID> | <work>
Commit:  [<surface>/<task>/<work>/<role>] <summary>
```

The accompanying meaning is equally small: use explicit current workflow context so
the task history is searchable and the next agent can recognize ownership; never guess
missing values. This is declared provenance, not actor authentication or publication
authority.

### 3.1 Result Visualization

```text
BEFORE
  prompt → router → schema/state → Python runtime → hooks → ledger → commit

AFTER
  explicit task context → one precise prompt → readable session + commit names
```

Example:

```text
Session: Executor | TFW-50 | implementation
Commit:  [codex/TFW-50/implementation/executor] remove rejected commit runtime
```

### 3.2 Value Flow

```text
PURPOSE + EXPLICIT TASK/WORK/ROLE/SURFACE
                  ↓
       PRECISE POINT-OF-USE PROMPT
                  ↓
      READABLE SESSION AND COMMIT NAME
                  ↓
     SEARCHABLE HISTORY + FAST RESUME
```

## 4. Delivery

TFW-50 is one corrective value slice. Splitting deletion from prompt replacement would
leave broken references or two competing systems.

### Single Phase: Remove Machinery, Keep the Meaning 🔴

1. Delete all 12 TFW-49 runtime/schema/state/hook files and local generated cache.
2. Remove the repository-local hook override and private runtime ledger; do not inspect
   or mutate system Git configuration or external hook contents.
3. Replace the long Commit Identity contract with one concise conventions owner and a
   concise glossary reference.
4. Put the session/commit format, purpose, and “do not guess” boundary in the four
   adapter templates and the installed Codex, Claude, and Antigravity entry prompts.
5. Remove dead runtime/router/hook/audit instructions from the six affected canonical
   workflows and keep their twelve installed Claude/Antigravity copies exact.
6. Preserve old TFW-49 task artifacts and commits as failure evidence; later
   `/tfw-docs` supersedes D58–D60 and the obsolete architecture index without erasing
   provenance.
7. Prove the prompt-first behavior with actual Executor and independent Reviewer
   session/commit naming, source inspection, adapter parity, and existing docs tests —
   not with a replacement validator.

### Exact Framework Scope

**Delete — 12 files:**

- `.tfw/commit_identity.schema.json`
- `.tfw/commit_identity_state.json`
- `.tfw/templates/commit_identity_state.json`
- `.tfw/scripts/commit_identity.py`
- `.tfw/scripts/commit_identity_router.py`
- `.tfw/scripts/commit_identity_hooks.py`
- `.tfw/scripts/test_commit_identity.py`
- `.tfw/scripts/test_commit_identity_router.py`
- `.tfw/scripts/test_commit_identity_hooks.py`
- `.tfw/hooks/runtime.json`
- `.tfw/hooks/prepare-commit-msg`
- `.tfw/hooks/commit-msg`

**Modify — 27 files:**

- semantic owners: `.tfw/conventions.md`, `.tfw/glossary.md`;
- adapter templates: `.tfw/adapters/codex/AGENTS.md.template`,
  `.tfw/adapters/claude-code/CLAUDE.md.template`,
  `.tfw/adapters/antigravity/tfw-rules.md.template`,
  `.tfw/adapters/cursor/tfw.mdc.template`;
- installed entry prompts: `AGENTS.md`, `CLAUDE.md`, `.agent/rules/tfw.md`;
- canonical workflows: `.tfw/workflows/docs.md`, `.tfw/workflows/handoff.md`,
  `.tfw/workflows/init.md`, `.tfw/workflows/release.md`,
  `.tfw/workflows/review.md`, `.tfw/workflows/update.md`;
- Antigravity copies: `.agent/workflows/tfw-docs.md`,
  `.agent/workflows/tfw-handoff.md`, `.agent/workflows/tfw-init.md`,
  `.agent/workflows/tfw-release.md`, `.agent/workflows/tfw-review.md`,
  `.agent/workflows/tfw-update.md`;
- Claude copies: `.claude/commands/tfw-docs.md`,
  `.claude/commands/tfw-handoff.md`, `.claude/commands/tfw-init.md`,
  `.claude/commands/tfw-release.md`, `.claude/commands/tfw-review.md`,
  `.claude/commands/tfw-update.md`.

Lifecycle artifacts and the README row are outside the framework count. KNOWLEDGE and
topic/state files remain post-review `/tfw-docs` or `/tfw-knowledge` territory.

## 5. Definition of Done (DoD)

- ✅ 1. Session and commit naming have one concise canonical meaning, one valid
  example, and an explicit purpose tied to searchable/resumable traces.
- ✅ 2. All four adapter templates and three installed adapter entries give agents the
  correct surface and the same point-of-use naming instruction without script calls.
- ✅ 3. All 12 rejected runtime/schema/state/hook files are absent; no replacement
  executable, schema, registry, manifest, state, hook, ledger, or validator is added.
- ✅ 4. Repository-local `core.hooksPath` and the private TFW runtime ledger are absent;
  user-global `core.hooksPath` remains absent and no external hook material is read.
- ✅ 5. The six canonical workflow owners and twelve derived copies contain no dead
  runtime/router/range-audit references and preserve exact copy parity.
- ✅ 6. Actual TFW-50 Executor and Reviewer sessions/commits use the documented formats
  from prompt context alone; review judges meaning and discoverability, not mechanical
  authentication.
- ✅ 7. Existing documentation generation/integration tests and rendered references
  pass after the net-negative change.
- ✅ 8. TFW-49 remains visibly rejected, its history is preserved, and post-review
  docs record TFW-50 as the prompt-first supersession of D58–D60.

## 6. Definition of Failure (DoF)

- ❌ 1. Any Python commit-identity program, test, hook, schema, tracked activation
  state, runtime manifest, private ledger, or `core.hooksPath` dependency remains.
- ❌ 2. A new executable, validator, registry, audit layer, generated prompt system, or
  hook lifecycle replaces the deleted mechanism.
- ❌ 3. The same complete naming contract is repeated across workflows instead of one
  owner plus short point-of-use prompt cues.
- ❌ 4. An agent must infer task, work, role, or surface from branch/history/path rather
  than use explicit current workflow context.
- ❌ 5. Session/commit naming is presented as authentication, proof, acceptance, or
  authorization to publish.
- ❌ 6. TFW-49 commits are rewritten/deleted, or any local work is pushed without the
  user’s later explicit approval.
- ❌ 7. Compression removes the purpose of the format or leaves a supported adapter
  unable to discover the instruction.

**On failure:** stop, remove the newly introduced mechanism or duplication, and return
to the prompt-first target. Do not recover reliability by rebuilding TFW-49 under a
different name.

## 7. Principles

1. **Methodology, not software** — agent behavior starts with meaning and prompts.
2. **Delete before adding** — remove rejected ownership and machinery completely.
3. **Naming creates behavior** — precise terms and one example replace explanations.
4. **One semantic owner** — adapters carry short cues, not copied contracts.
5. **Purpose before enforcement** — searchable provenance is the value; blocking Git
   is not the product.
6. **Agents use explicit context** — missing context is resolved, never inferred.
7. **Failure remains a trace** — preserve TFW-49 history and record its supersession.
8. **Independent judgment remains** — Reviewer checks whether the simpler prompt
   actually produced understandable traces.

### 7.1 Quality Contract

- The final framework diff is net-negative by construction: 12 files and 5,910 lines
  of runtime machinery disappear, no framework file is created, and modified prompt
  consumers must not offset the deletion with new procedural prose.
- The format and one sentence of purpose are sufficient. Edge-case catalogues,
  registries, lifecycle matrices, activation anchors, and cross-platform runtime
  claims are prohibited.
- Full local imperatives remain only for role, destructive, irreversible, and
  publication boundaries; commit naming itself is a reversible convention.

### 7.2 Knowledge Citations

| # | Source | Item | How it applies |
|---|--------|------|----------------|
| 1 | [.tfw/README.md](../../.tfw/README.md#naming-creates-behavior) | Naming Creates Behavior | A precise format and purpose should replace machinery and long explanation. |
| 2 | [.tfw/README.md](../../.tfw/README.md#single-source-of-truth) | Single Source of Truth | Keep one semantic owner and short adapter cues. |
| 3 | [knowledge/philosophy.md](../../knowledge/philosophy.md) | F11 | Do not proliferate a second entity when the Markdown relation already carries the value. |
| 4 | [knowledge/philosophy.md](../../knowledge/philosophy.md) | F14 | TFW is a methodology, not installable software. |
| 5 | [knowledge/process.md](../../knowledge/process.md) | F3 | Small prompt plus precise terms directs agents better than long explanation. |
| 6 | [knowledge/process.md](../../knowledge/process.md) | F6 | Coordinator must veto scope explosion that loses the original value. |
| 7 | [knowledge/process.md](../../knowledge/process.md) | F22 | Over-engineering a finding into framework machinery is an anti-pattern. |
| 8 | [KNOWLEDGE.md](../../KNOWLEDGE.md) | D28 | Naming is the operational prompt. |
| 9 | [KNOWLEDGE.md](../../KNOWLEDGE.md) | D55 | Rule locality follows consequence; this reversible naming convention needs a cue, not a hard gate. |
| 10 | [knowledge/process.md](../../knowledge/process.md) | F26 | Local completion never authorizes publication. |

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| User rejection of TFW-49 mechanism and selection of prompt-only target | ✅ Authoritative |
| Exact runtime and prompt-consumer inventory | ✅ Reproduced |
| Global user `core.hooksPath` disabled without reading external material | ✅ Complete |
| TFW-49 history retained as failure trace | ✅ Required |
| Explicit approval of this HL before TS/execution | ✅ Approved by user, 2026-08-01 |

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Deletion leaves a dead reference | Medium | High | Exact reference scan plus canonical/derived parity check. |
| Prompt becomes another long contract | Medium | High | One owner, one example, short adapter cue, hard no-new-mechanism DoF. |
| Agents sometimes mistype the convention | Medium | Low | Explain purpose, review actual history, correct prompts when behavior fails. |
| Removing local hooks restores an unknown global hook | Low | Medium | User-global `core.hooksPath` is already absent; local unset is verified without reading external material. |
| Cleanup erases provenance | Low | High | Delete implementation files only; preserve commits and TFW-49 task artifacts. |

## 10. RESEARCH Case

### Decision

No new research. Existing TFW-49 research remains useful only for the readable
four-field format and the non-authentication boundary. The owner has now supplied the
decision-changing fact the prior research failed to prioritize: TFW’s product value
is prompt-directed agent behavior, and hard Git enforcement is unwanted complexity.
This is a direct bounded refactor, not an unresolved comparison.

### Hypotheses

| # | Hypothesis | Status |
|---|------------|--------|
| H1 | The four-field format makes history easier to recognize and filter | retained from TFW-49 |
| H2 | Precise prompt placement is sufficient for current agents | owner-confirmed; validate through actual Executor/Reviewer use |
| H3 | Python/hooks are required for useful commit provenance | refuted by product authority; machinery is the failure |

### Why Not Just...?

- Why not repair TFW-49? — Its architecture is the rejected product; incremental
  repair would preserve the wrong owners and obscure the clean correction.
- Why not erase TFW-49 commits? — Failure is a valuable trace, and published history
  would require destructive rewriting. TFW-50 can remove the result without deleting
  the reasoning record.
- Why not keep hooks as optional? — Optional runtime still creates owners, lifecycle,
  documentation, and maintenance for a value the user did not request.

## 11. Strategic Insights (Planning)

| # | Insight | Planning implication | TS disposition / destination | Category | Source |
|---|---------|----------------------|------------------------------|----------|--------|
| S1 | The strength of TFW is prompts and agents; its philosophy is to remove unnecessary things | Make deletion and no-new-mechanism hard acceptance boundaries | AC: full runtime removal; DoF: replacement machinery | philosophy | User correction, 2026-07-31 |
| S2 | The requested result was only a commit/session format placed in several prompts | Limit the final product to one owner, adapter cues, and cleanup of dead references | Scope and prompt-discoverability AC | convention | User correction, 2026-07-31 |
| S3 | Hooks are unnecessary; agents should understand the purpose and write names themselves | Remove local runtime/hooks and rely on explicit context plus independent review | Runtime removal and actual-use proof AC | process | User correction, 2026-07-31 |
| S4 | TFW-49 is a complete failure and should not be presented as successful | Preserve A–C traces but mark the task rejected and superseded | TFW-49 status; TFW-50 docs closure | process | User decision, 2026-07-31 |
| S5 | Rewriting or deleting the failed history is less valuable than admitting the failure and starting correctly | No history rewrite; remove the resulting files in TFW-50 | Scope boundary and DoF 6 | philosophy | User decision, 2026-07-31 |

---

*HL — TFW-50: Prompt-First Session and Commit Identity | 2026-07-31*
