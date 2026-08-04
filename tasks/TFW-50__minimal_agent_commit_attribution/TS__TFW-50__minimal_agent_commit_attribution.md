# TS — TFW-50: Minimal Agent Commit Attribution

> **Date**: 2026-08-05
> **Author**: Codex / Coordinator
> **Status**: ⚠️ TS — Execution paused; consumer scope requires revision after research
> **Parent HL**: [HL-TFW-50](HL-TFW-50__minimal_agent_commit_attribution.md)

> This TS records the first six-file configuration. It is not current execution authority after the user identified missing Coordinator, Researcher, and Reviewer commit paths. A Coordinator must revise and re-approve it from the bounded research result before execution resumes.

## 1. Objective

Add a portable, prompt-level Commit Attribution convention that makes AI-authored Git history searchable by agent, task, scope, and TFW role. Correct the two active commit instructions that conflict with it, while adding no enforcement runtime and changing no unrelated methodology.

## 2. Scope

### In Scope

- One canonical normative sentence and one example in conventions.
- One concise glossary definition pointing to the canonical owner.
- One point-of-use handoff correction in the canonical workflow and two installed copies.
- One active release-example correction and explicit user approval before push.
- Static verification, current-repository commit inspection, docs tests, EV, and RF.

### Out of Scope

- Hooks, scripts, schemas, registries, manifests, state/config keys, validators, trailers, or Git history rewriting.
- Actor authentication, human/agent detection, model/account/session tracking, or hosted enforcement.
- Adapter entry prompts, Codex skills, unrelated workflows, version files, historical task artifacts, and existing non-commit handoff drift.
- Push, remote mutation, tag, deploy, publish, or notify.

## 3. Principles Check

| # | Principle (HL §7) | Enforced by | Gate |
|---|-------------------|-------------|------|
| P1 | Outcome over mechanism | AC-1, AC-5 | Readable subject contract exists; runtime inventory remains absent |
| P2 | Naming creates behavior | AC-1, AC-2 | Terms and four labels have one exact meaning |
| P3 | Single source of truth | AC-1, AC-3 | One normative owner; other consumers only point or instantiate |
| P4 | Declared context, not identity proof | AC-2, AC-5 | Non-authentication boundary present; prohibited claims absent |
| P5 | Human publication authority | AC-3, AC-4 | Handoff/release require explicit user approval before push |
| P6 | Proportional completeness | AC-1, AC-5 | Rule stays one sentence; no arbitrary document limit or added machinery |
| P7 | Transparent boundaries | AC-3, AC-5, AC-6 | Exact files, preserved drift, exclusions, and actual commit range are verified |

## 4. Affected Files

### Implementation files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/conventions.md` | MODIFY | Sole normative Commit Attribution owner under §4 |
| `.tfw/glossary.md` | MODIFY | Concise term definition and owner reference |
| `.tfw/workflows/handoff.md` | MODIFY | Step 4 reference; remove automatic push authority |
| `.agent/workflows/tfw-handoff.md` | MODIFY | Same Step 4 semantic correction only |
| `.claude/commands/tfw-handoff.md` | MODIFY | Same Step 4 semantic correction only |
| `RELEASE.md` | MODIFY | Attributed release example and explicit push approval |

### Lifecycle traces

| File | Action | Description |
|------|--------|-------------|
| `README.md` | MODIFY | TFW-50 Task Board state and artifact links only |
| `tasks/TFW-50__minimal_agent_commit_attribution/ONB__TFW-50__minimal_agent_commit_attribution.md` | CREATE | Executor onboarding |
| `tasks/TFW-50__minimal_agent_commit_attribution/evidence/EV__TFW-50__minimal_agent_commit_attribution.md` | CREATE | Claim/evidence trace |
| `tasks/TFW-50__minimal_agent_commit_attribution/RF__TFW-50__minimal_agent_commit_attribution.md` | CREATE | Executor result |

Reviewer-owned stage/REVIEW traces and later docs/knowledge triage are created only by their canonical workflows.

**Budget observation:** 0 new framework files, 6 framework/project modifications. Configured scope values are not completion targets.

## 5. Acceptance Criteria

### AC-1: Canonical term and owner

Conventions solely own the normative rule; glossary names the concept without creating a second rule.

- [ ] Conventions contain one `Commit Attribution` section under §4, one normative sentence, and one example.
- [ ] Glossary defines Commit Attribution as declared context, links to conventions §4, and states that it is not authentication.
- [ ] No other changed file repeats the complete normative sentence.

Gate: exact-text occurrence scan, heading/link check, and changed-file review.
Evidence: N/A — documentation ownership is fully observable in repository sources.

### AC-2: Exact subject semantics [depends: AC-1]

The rule expresses one stable grammar without hidden registries or numeric limits.

- [ ] Subject grammar is exactly `[agent/task/scope/role] summary`.
- [ ] `agent`, `scope`, and `role` are lowercase contextual labels; `task` is the canonical TFW ID or `project` only when no task exists.
- [ ] `summary` is short and imperative without a numeric length target.
- [ ] Unmarked commits are not classified as human, and attribution is not actor authentication.

Gate: semantic assertions against conventions and glossary; absence scan for prohibited claims/fields.
Evidence: N/A — semantics are repository text.

### AC-3: Handoff action boundary [depends: AC-1]

All three active handoff consumers point to Commit Attribution at the commit action and require separate explicit approval for push.

- [ ] Step 4 in canonical, Antigravity, and Claude handoff files has the same commit/push meaning.
- [ ] None of the three says or implies that ONB completion authorizes push.
- [ ] Outside the Step 4 change, the pre-existing canonical-vs-installed Evidence drift is unchanged.

Gate: three-file Step 4 comparison plus baseline/final diff restricted outside that line.
Evidence: N/A — action contract is repository text; live push is prohibited.

### AC-4: Release action boundary [depends: AC-1]

The active project release instructions use Commit Attribution and separate local release preparation from publication.

- [ ] The release commit example conforms to `[agent/task/scope/role] summary` using `project/release/coordinator` where no task exists.
- [ ] Push requires explicit user approval.

Gate: inspect `RELEASE.md` release steps and scan for the superseded `release: vX.Y.Z` subject.
Evidence: N/A — no release or publication is authorized.

### AC-5: Minimal intervention and protected boundaries [depends: AC-2]

The result remains a Markdown convention, not an identity system.

- [ ] Exactly the six approved implementation files change; no new framework file exists.
- [ ] No hook/script/schema/registry/manifest/state/config/trailer/validator is added.
- [ ] Adapter entry prompts, skills, unrelated workflows, historical tasks, version files, Git config, and history remain unchanged.
- [ ] No model/session/account/branch field or authentication claim appears.

Gate: exact allowlist diff, prohibited-path/text scan, Git-config snapshot, and `git diff --check`.
Evidence: N/A — protected-state comparison is repository-local verification.

### AC-6: Real commit readability and regression [depends: AC-3] [depends: AC-4] [depends: AC-5]

TFW-50 demonstrates the convention in its own local lifecycle without publishing it.

- [ ] Every AI-authored commit in `bc6779e..HEAD` conforms to the approved grammar and accurately names its role/scope.
- [ ] Executor and independent Reviewer each inspect the actual current-repository range.
- [ ] Existing docs tests pass and generated outputs/caches are removed after verification.
- [ ] Remote remains unchanged and no push/tag/deploy/publish/notify occurs.

Gate: `git log --format=%H%x09%s bc6779e..HEAD`, independent review, docs test pair, status/remote comparison.
Evidence: Observe the actual local Git range and record hashes/subjects plus local-vs-remote state in EV.

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__TFW-50__minimal_agent_commit_attribution.md` | Required structured evidence, including actual local commit subjects and no-publication state |

## 6. Technical Guidance

- Exact normative sentence and terminology contract are in HL §3; do not expand them.
- The new conventions section belongs under §4 Task Numbering because it defines task-linked Git naming.
- The glossary entry belongs beside Task Naming and should reference conventions rather than restate the full rule.
- Baseline handoff drift is limited to the Evidence/RF §5 block: canonical uses EV-file enforcement while installed copies retain inline Evidence. It is intentionally out of scope; only Step 4 changes in all three.
- All supported agent entry paths already load conventions; no entry-prompt change is needed.
- `RELEASE.md` is the only active non-task commit example found by the bounded scan. Historical task examples are traces and remain untouched.
- A legacy default `.git/hooks/prepare-commit-msg` added `[master]:` to the first local plan commit despite unset `core.hooksPath`; it was removed and the unpushed commit was amended. Executors must not restore or replace it.

## 7. Definition of Failure

- ❌ Any implementation path outside the six-file allowlist changes without Coordinator return.
- ❌ Any new framework/runtime/config/state file is created.
- ❌ The complete normative sentence is duplicated outside conventions.
- ❌ Existing handoff Evidence drift changes, whether by partial or full sync.
- ❌ Attribution is claimed to authenticate an actor or identify unmarked commits as human.
- ❌ Extra subject fields, fixed length limits, operation matrices, or trailer protocols appear.
- ❌ Handoff or release still authorizes push without explicit user approval.
- ❌ Any remote action, Git history rewrite, or old-hook restoration occurs.
- ❌ Any AI-authored `bc6779e..HEAD` commit fails the format or misstates context.
- ❌ Required tests or repository checks fail when RF is written.

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Executor “cleans up” existing handoff drift | Exact line-only boundary and failure clause |
| Glossary becomes a competing owner | Definition plus owner reference only; exact duplication scan |
| Subject values become a registry | Use explicit current context and examples, not enumerated runtime data |
| Testing creates ignored build/cache debris | Audit and remove only generated paths after tests |
| Agent attempts to publish completed work | Hard no-push scope and local/remote comparison in EV/REVIEW |

---

*TS — TFW-50: Minimal Agent Commit Attribution | 2026-08-05*
