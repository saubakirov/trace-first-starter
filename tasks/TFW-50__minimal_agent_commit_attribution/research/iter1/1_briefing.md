# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW-50](../../HL-TFW-50__minimal_agent_commit_attribution.md)
> Goal: Determine the smallest complete Markdown-only commit-attribution design that covers every real TFW commit-producing role and workflow without implying authentication or publication authority.

## Research Plan

### Gather

- Use `rg` to inventory explicit and implicit local commit instructions across canonical workflows, coordinator-owned lifecycle workflows, adapters, installed workflow copies, and Codex skills; group results before selectively reading actual consumers.
- Inspect relevant local Git history and the already completed six-path implementation to separate demonstrated commit behavior from prescribed behavior and to identify what can be preserved, what is insufficient, and what is extraneous.
- Consult only the minimum official Git documentation needed to distinguish TFW Commit Attribution from Git author/committer metadata and actor authentication.

### Extract

- Classify every relevant file as canonical semantic owner, point-of-use commit action, always-loaded reference, derived/installed copy, or non-consumer; do not flatten these categories into an equal-weight file list.
- Define and challenge `Commit Attribution`, `agent`, `task`, `scope`/work slice, `role`, and `summary`, including boundaries against Git author, committer, and authenticated actor concepts.
- Compare three configurations: canonical-only; one canonical owner plus cues at actual commit actions; and a cue in every role workflow. Evaluate completeness, prompt visibility, duplication, drift, and adapter obligations.

### Challenge

- Attempt to falsify the preferred configuration against Coordinator planning and docs/knowledge/release/init/update/config/resume, Researcher stage/RES commits, Executor handoff commits, Reviewer review/REVIEW commits, and active tool-specific copies.
- Test the six-path implementation for omissions, unnecessary files, semantic duplication, push-policy consistency, and preservation of unrelated adapter drift.
- Produce a future-TS inventory with explicit include/exclude reasons and state the limits of prompt compliance without proposing runtime, hook, schema, manifest, or config enforcement.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | One canonical owner plus cues only at actual commit actions is sufficient across all roles. | open |
| H2 | `[agent/task/scope/role] summary` uses the smallest precise term set for the user's searches. | open |
| H3 | Role workflows, lifecycle workflows, and installed adapter copies form distinct consumer classes and should not be treated as one flat sync list. | open |
| H4 | Prompt compliance is sufficient for readable declared context when authentication and automated enforcement are explicitly out of scope. | bounded; needs cross-role evidence |

## Scope Intent

- **In scope:** Current tracked TFW corpus; canonical and coordinator-owned workflows; Researcher, Executor, and Reviewer commit points; active adapters, installed copies, and skills; relevant local Git history; the prior six-path implementation; minimal official Git terminology.
- **Out of scope:** Any implementation change; HL, TS, ONB, RF, REVIEW, README, code, runtime, hooks, Python, schemas, manifests, project/state configuration, releases, tags, pushes, fetches, deployments, notifications, and history rewrites.

## Guiding Questions

1. Which tracked files are genuine commit-action consumers, and which are only the semantic owner, always-loaded references, derived copies, or non-consumers? **Recommended default:** include every explicit local commit action in the inventory, but place the full rule only in the canonical owner and short cues only at actual actions.
2. What exact meanings make the five subject components precise without implying Git identity or authentication? **Recommended default:** treat the prefix as declared TFW context, use the acting product name, canonical task ID, explicit current work slice, active Role Lock, and a short imperative summary.
3. Which topology is the smallest complete one across all roles and adapters? **Recommended default:** prefer one canonical owner plus point-of-use cues, synchronizing only active derived copies of those changed commit actions; accept canonical-only or every-role cues only if corpus evidence disproves that default.

## User Direction

- Run exactly one focused iteration (`iterations.yaml` sets `min_iterations: 1`, `max_iterations: 1`).
- The local corpus is primary; external checking is limited to official Git terminology.
- Researcher commits its own stage and RES traces using the current `[agent/task/scope/role] summary` rule.
- Do not redirect the guiding questions to the end user. Apply the stated defaults unless corpus evidence requires escalation to the Coordinator.
- No implementation and no remote-changing action.

---
Stage complete: YES
