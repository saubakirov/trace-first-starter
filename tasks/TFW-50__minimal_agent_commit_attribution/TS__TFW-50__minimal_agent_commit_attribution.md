# TS — TFW-50: Minimal Agent Commit Attribution

> **Date**: 2026-08-05
> **Author**: Codex / Coordinator
> **Status**: ✅ TS — Revised from RES Iteration 1 and approved under delegated user authority
> **Parent HL**: [HL-TFW-50](HL-TFW-50__minimal_agent_commit_attribution.md)
> **Research**: [RES Iteration 1](research/iter1/RES.md)

## 1. Objective

Finish one portable Markdown-level Commit Attribution rule for every AI-authored local commit, regardless of whether the active TFW role is Coordinator, Researcher, Executor, or Reviewer. Refine the exact terms, preserve the already-correct handoff/release conflict fixes, verify the whole consumer corpus, and add neither enforcement runtime nor commit cadence.

## 2. Scope

### In Scope

- Refine the sole normative sentence and example in `.tfw/conventions.md`.
- Refine the concise `.tfw/glossary.md` definition without duplicating the grammar.
- Preserve and verify the corrected handoff text in canonical, Antigravity, and Claude files.
- Preserve and verify the corrected active release subject/push boundary.
- Verify universal applicability across all four roles, current workflows/adapters, and representative local history.
- Complete EV/RF and independent review locally.

### Out of Scope

- New commit requirements at stages, WAITs, STOPs, workflow completion, artifacts, files, or acceptance criteria.
- Edits to plan, research, review, docs, knowledge, canonical release, init, update, config, resume, Codex skills, or other adapter copies solely to repeat the rule.
- Hooks, scripts, schemas, registries, manifests, state/config keys, validators, trailers, Git history rewriting, actor authentication, or human/agent detection.
- Push, fetch, remote tag, deploy, publish, or notify.

## 3. Principles Check

| # | Principle (HL §7) | Enforced by | Gate |
|---|-------------------|-------------|------|
| P1 | Outcome over mechanism | AC-1, AC-6 | Searchable subjects; no runtime |
| P2 | Naming creates behavior | AC-1, AC-2 | Exact five-part terminology |
| P3 | Single source of truth | AC-1, AC-4 | One owner; other files only reconcile conflicts |
| P4 | Declared context, not identity proof | AC-2, AC-5 | Metadata/authentication boundary is explicit |
| P5 | Human publication authority | AC-4, AC-6 | Local commit and push remain separate |
| P6 | Proportional completeness | AC-3, AC-5 | All roles covered without role-specific duplication or cadence |
| P7 | Transparent boundaries | AC-4, AC-5, AC-6 | Exact six paths and verification-only corpus |

## 4. Affected Files

### Implementation allowlist

| File | Action | Description |
|------|--------|-------------|
| `.tfw/conventions.md` | MODIFY | Refine the sole normative rule and exact term derivation |
| `.tfw/glossary.md` | MODIFY | Refine the concise definition and Git metadata boundary |
| `.tfw/workflows/handoff.md` | PRESERVE + VERIFY | Keep corrected Step 4; no cadence addition |
| `.agent/workflows/tfw-handoff.md` | PRESERVE + VERIFY | Keep derived Step 4; preserve unrelated Evidence drift |
| `.claude/commands/tfw-handoff.md` | PRESERVE + VERIFY | Keep derived Step 4; preserve unrelated Evidence drift |
| `RELEASE.md` | PRESERVE + VERIFY | Keep attributed example and explicit push approval |

No new implementation file is allowed. The task's total implementation surface remains the six paths already changed in commit `389168a`; the corrective execution should change only conventions and glossary unless verification discovers a contradiction inside the four preserved paths.

### Verification-only corpus

- All canonical workflows: plan, research, handoff, review, resume, docs, knowledge, release, init, update, config.
- All `.agent`/`.claude` workflow copies and Codex source/installed skills.
- Root and adapter entry files that load conventions.
- `.tfw/adapters/codex/README.md` install/repair action.
- Actual local TFW-50 subjects and representative Reviewer history.

### Lifecycle traces

README, EV, RF, review stages, REVIEW, and later docs/knowledge markers follow their canonical workflow ownership; they are not extra implementation consumers.

## 5. Acceptance Criteria

### AC-1: Sole normative owner and grammar

- [ ] `.tfw/conventions.md` contains one Commit Attribution section, one normative sentence, and one example.
- [ ] Grammar is exactly `[agent/task/scope/role] summary`.
- [ ] No changed workflow, adapter, or glossary text becomes a second normative owner.

Gate: heading/exact-occurrence scan and full six-path diff review.
Evidence: N/A — repository text is the observed contract.

### AC-2: Exact terms and boundaries [depends: AC-1]

- [ ] `agent` is the lowercase AI product from explicit context, not a person, model, account, Git author, or committer.
- [ ] `task` is the canonical TFW task ID; `project` is allowed only when no task exists.
- [ ] `scope` is open normalized text from the explicit work-slice label, not a registry or inferred path.
- [ ] `role` comes from canonical TFW workflow ownership in conventions §15/Role Lock and is one of coordinator, researcher, executor, reviewer.
- [ ] `summary` is short and imperative with no numeric limit, body schema, or trailer.
- [ ] Commit Attribution is first-line subject trace context, separate from Git author/committer metadata and authentication; unmarked commits are not classified as human.

Gate: semantic assertions against conventions/glossary and prohibited-term scan.
Evidence: N/A — repository text is the observed contract.

### AC-3: Universal role applicability without cadence [depends: AC-1] [depends: AC-2]

- [ ] The rule says every AI-authored commit, so it applies equally to Coordinator, Researcher, Executor, and Reviewer.
- [ ] No role-specific grammar or duplicated full rule is added.
- [ ] No new requirement says to commit per stage, WAIT, STOP, workflow, artifact, file, or AC.
- [ ] Current docs/release label drift cannot create `maintainer` or a hybrid role because canonical §15/Role Lock owns the role value; no broad label-cleanup branch is added.

Gate: complete verification-only corpus scan plus comparison to RES D1/D2/D6.
Evidence: N/A — this verifies methodology text and absence of cadence expansion.

### AC-4: Existing conflict reconciliation remains correct [depends: AC-1]

- [ ] Canonical and installed handoff Step 4 use Commit Attribution and require separate explicit approval before push.
- [ ] `RELEASE.md` uses a compliant project/release/coordinator example and requires approval before pushing commit/tag.
- [ ] The four preserve-and-verify files remain byte-stable during corrective execution unless a concrete contradiction is found.
- [ ] Unrelated canonical-vs-installed handoff Evidence drift remains unchanged.

Gate: baseline/current hashes and line-scoped diffs for the four files.
Evidence: N/A — no publication is authorized.

### AC-5: Minimal complete consumer treatment [depends: AC-3] [depends: AC-4]

- [ ] The total implementation allowlist remains exactly six existing paths; no new implementation file or phase is created.
- [ ] Other workflows/adapters/skills are audited as verification-only and contain no conflicting subject or automatic-push instruction.
- [ ] Docs grouping and Codex install inclusion wording are not mistaken for competing subject rules.
- [ ] No hook, script, schema, config/state, validator, runtime, operation matrix, or broad adapter sync appears.

Gate: exact total-task allowlist diff from plan baseline, grouped `rg` scan, protected-path audit, and `git diff --check`.
Evidence: N/A — repository-local source comparison.

### AC-6: Cross-role readability, regression, and no publication [depends: AC-5]

- [ ] Representative local subjects exist for Coordinator, Researcher, Executor, and — by final independent review — Reviewer using the same grammar.
- [ ] Subjects accurately reflect explicit task, work slice, and canonical TFW role.
- [ ] History is reported as compatibility/searchability evidence only; explicit prompts and prior TFW-49 machinery are named confounders, so no causal compliance or authentication claim is made.
- [ ] Existing docs tests pass; generated outputs/caches from verification are removed without touching ignored user files.
- [ ] Remote remains at `bc6779e`; no push/fetch/tag/deploy/publish/notify occurs.

Gate: `git log --format=%H%x09%s bc6779e..HEAD`, independent review's own attributed commit, docs tests, status/remote comparison.
Evidence: Record actual representative hashes/subjects and local-vs-remote state in EV. Executor may record Reviewer completion as pending independent review rather than claim it early.

### Evidence Artifact

| File | Description |
|------|-------------|
| `evidence/EV__TFW-50__minimal_agent_commit_attribution.md` | Exact terminology/source checks, six-path preservation, all-role subjects available at execution time, regression results, and no-publication state |

## 6. Technical Guidance

- Apply RES Iteration 1 C7, not Extract's rejected 33-file cadence configuration.
- Keep one normative sentence; a short glossary definition may clarify metadata without restating the grammar.
- Preserve the four already-correct reconciliation files unless a concrete contradiction is reproduced.
- Use conventions §15 as role authority. `/tfw-docs` and `/tfw-release` AI work therefore uses `coordinator`; do not create `maintainer` or hybrid roles.
- Audit the wider corpus read-only. Universal applicability is the intended mechanism; absence of a local cue is not itself a defect.
- Existing TFW-50 Coordinator/Executor/Researcher commits and earlier Reviewer commits show expressibility, but their prompts/mechanisms confound causality.

## 7. Definition of Failure

- ❌ Any implementation path outside the six-file total-task allowlist changes without Coordinator return.
- ❌ Any new framework/runtime/config/state file or phase is created.
- ❌ The full rule is duplicated outside conventions.
- ❌ A new commit cadence or checkpoint policy is introduced.
- ❌ Existing handoff Evidence drift changes.
- ❌ Attribution is claimed to authenticate an actor or identify unmarked commits as human.
- ❌ Extra fields, fixed length limits, operation matrices, or trailers appear.
- ❌ Any current handoff/release text authorizes push without explicit user approval.
- ❌ Any remote action, history rewrite, or old-hook restoration occurs.
- ❌ Tests/checks fail when RF is written, or generated debris is left behind.

## 8. Risks

| Risk | Mitigation |
|------|------------|
| Universal rule is mistaken for Executor-only because handoff has a local cue | AC-3 all-role semantics plus representative all-role history |
| Precision wording becomes an unreadable mini-spec | One sentence, one example, one concise glossary definition; no registry |
| Research cadence proposal leaks into implementation | Explicit AC-3 and Definition of Failure |
| Verification-only files are edited for symmetry | Six-path allowlist and preserve-vs-modify dispositions |
| Prompted history is overclaimed as causal evidence | AC-6 requires explicit confounder disclosure |

---

*TS — TFW-50: Minimal Agent Commit Attribution | Revised 2026-08-05*
