# EV — TFW-50: Minimal Agent Commit Attribution

> **Date**: 2026-08-05
> **Author**: Codex / Executor
> **Task**: TFW-50
> **TS**: [TS TFW-50](../TS__TFW-50__minimal_agent_commit_attribution.md)

---

## Environment

| Field | Value |
|-------|-------|
| OS | Microsoft Windows NT 10.0.26200.0 |
| Shell | Windows PowerShell 5.1.26100.8655 |
| Language / Runtime | Python 3.13.5; pytest 9.0.2 |
| Git | 2.42.0.windows.1 |
| Deploy target | Local repository only; no deployment or publication authorized |
| CI / Pipeline | Local docs unit and MkDocs integration suites |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Sole normative owner, exact grammar, one section, one example, and no second owner | Repository source inspection | N/A | Verification Record V1 |
| E2 | AC-2 | Exact term derivation plus Git author/committer, authentication, unmarked-human, body-schema, trailer, and numeric-limit boundaries | Repository source inspection | N/A | Verification Record V2 |
| E3 | AC-3 | Universal Coordinator/Researcher/Executor/Reviewer applicability and absence of newly added commit cadence | Full active corpus and corrective diff | N/A | Verification Record V3 |
| E4 | AC-4 | Four preserve-and-verify files remain byte-identical to their `389168a` blobs; push reconciliation remains explicit | Git blob comparison | N/A | Verification Record V4 |
| E5 | AC-5 | Total implementation surface is exactly six existing paths; corrective execution changed only two; wider corpus has no subject/push conflict | Git diff and grouped corpus scan | N/A | Verification Record V5 |
| E6 | AC-6 | Executor-observable history, regression tests, generated-path cleanup, and no-publication state passed; the current-task Reviewer commit and independent inspection remain pending `/tfw-review` | Local Git history and docs build | DEFERRED | Verification Record V6 |

## Verification Record

### V1 — Sole owner and grammar

- `Commit Attribution` normative owner hits across the six implementation paths: `1`, in `.tfw/conventions.md`.
- Grammar: `[agent/task/scope/role] summary`.
- Conventions contain one normative sentence and one example.
- Glossary links to conventions §4 and does not repeat the grammar.

### V2 — Exact terminology and boundaries

- `agent`: lowercase AI product name from explicit context.
- `task`: canonical TFW task ID; `project` only when none exists.
- `scope`: established lowercase work-slice slug or lowercase hyphenation of its explicit label; no registry.
- `role`: lowercase canonical workflow owner from conventions §15/Role Lock.
- `summary`: short and imperative; no numeric limit, trailer, or body schema.
- Glossary states that the prefix is first-line subject text, separate from Git author/committer metadata, not actor authentication, and not a classifier for unmarked commits.

### V3 — Universal roles without cadence

- Canonical Role Locks inspected: Coordinator (`plan.md`), Researcher (`research/base.md`), Executor (`handoff.md`), Reviewer (`review.md`).
- The sole rule begins with “Every AI-authored commit”; no role-specific grammar was added.
- Corrective added-text scan found `0` occurrences of per-stage, per-WAIT, per-STOP, per-workflow, per-artifact, per-file, or per-AC commit requirements.
- Full active workflow/adapter/skill scan: `12` commit-family hits, `6` push-family hits, `0` automatic-push conflicts, `0` conflicting subject instructions, and `0` hybrid/maintainer subject roles.

### V4 — Preserve-file byte stability

| Path | `389168a` blob = final blob | Blob hash |
|------|-----------------------------|-----------|
| `.tfw/workflows/handoff.md` | yes | `00baa9b2c9df93cc989d9b0841df22bfb8a06ea1` |
| `.agent/workflows/tfw-handoff.md` | yes | `44fea1c0da8665a5c948764f8d4e1a9bd5bea4c4` |
| `.claude/commands/tfw-handoff.md` | yes | `44fea1c0da8665a5c948764f8d4e1a9bd5bea4c4` |
| `RELEASE.md` | yes | `3ff41c298a5d4fbcc985f2c2850f8a766fce2aae` |

The installed handoff Evidence drift is therefore unchanged in full, not merely visually equivalent.

### V5 — Allowlist and protected state

- Total implementation diff from `bc6779e`: exactly six existing paths, all in the TS allowlist; unexpected `0`, missing `0`.
- Corrective diff `c7a0055..420fdbe`: only `.tfw/conventions.md` and `.tfw/glossary.md`.
- New framework/runtime/config/state files: `0`.
- `git diff --check`: PASS.
- Local and global `core.hooksPath`: unset; `.git/hooks/prepare-commit-msg`: absent.
- No hooks, scripts, schemas, registries, manifests, config/state, validators, runtime enforcement, or history rewrite were introduced.

### V6 — History, regression, cleanup, and publication boundary

Current range captured immediately before the EV/RF trace commit:

- `git log --format='%H%x09%s' bc6779e..HEAD`: `14` subjects inspected; regex-invalid subjects: `0`.
- Coordinator representative: `021f039` — `[codex/TFW-50/task/coordinator] approve all-role attribution revision`.
- Researcher representative: `c768748` — `[codex/TFW-50/iter1/researcher] synthesize commit-attribution research`.
- Executor representative: `420fdbe` — `[codex/TFW-50/task/executor] refine universal attribution terms`.
- Current-task Reviewer representative and independent range inspection: **DEFERRED — pending `/tfw-review`**.
- Prior Reviewer compatibility example: `3935c53` — `[codex/TFW-49/phase-c/reviewer] approve corrected repository-local enforcement`.

The history demonstrates grammar expressibility and searchability only. Explicit delegation prompts required attribution during TFW-50, and the prior Reviewer examples were produced while rejected TFW-49 machinery existed; these are confounders. No causal compliance, authentication, or guaranteed actor-identification claim is made.

Regression and cleanup:

- `python -m pytest docs/scripts/test_gen_docs.py -q`: `55 passed in 1.45s`.
- `python -m pytest docs/scripts/test_integration.py -q`: `13 passed in 91.22s`.
- Test-generated `.pytest_cache/`, `docs/scripts/__pycache__/`, and `site/` were removed.
- Pre-existing ignored user paths remained exactly: `entities.json`, `mempalace.yaml`, `tasks/TFW-36__content_marketing_blog_series/`.
- `origin/master` remained `bc6779e365b01118030ec577a47e6339f0fabf1c`; pre-EV/RF local state was ahead `14`, behind `0`.
- No push, fetch, tag, deploy, publish, or notify action was performed.

The EV/RF trace commit necessarily follows this snapshot; its attributed subject is reported in the Executor final handoff and must be included in the independent Reviewer range inspection.

## Verdict

Evidence verdict: 0/6 VERIFIED, 1 DEFERRED, 0 BLOCKED, 5 N/A

---

*EV — TFW-50: Minimal Agent Commit Attribution | 2026-08-05*
