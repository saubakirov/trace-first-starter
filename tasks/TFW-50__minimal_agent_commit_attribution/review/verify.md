# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: spec
> Min verify ratio: 0.42
> RF files claimed: 10 distinct paths in RF §1 (2 new, 4 modified, 4 preserved)
> Files to verify: ⌈10 × 0.42⌉ = 5; actual verification: 10/10 plus the complete active workflow/adapter/skill corpus

## Verification Log

### V1: baseline, original plan/implementation, correction, and revised execution chain
- **RF claim:** TFW-50 starts from the published/restored `bc6779e` baseline, retains the original six-path implementation, then applies a user-driven all-role research correction before revised execution.
- **Actual:** `origin/master` and the declared baseline both resolve to `bc6779e365b01118030ec577a47e6339f0fabf1c`. Its tree `066795d7aff38a2b5528865e8e36bfd0a82fa94c` equals the restored `v0.9.0` source commit `5aef936b` tree. `bc6779e..ace895b` is a linear 15-commit range with zero merges: original HL/TS → original ONB/approval → `389168a` implementation → research reopen → four stages + RES → revised HL/TS → revised ONB/approval → two-file correction → EV/RF. The original and revised artifact versions and the complete RES iteration were read, not only the final patch.
- **Match:** ✅

### V2: `.tfw/conventions.md` and `.tfw/glossary.md`
- **RF claim:** Conventions are the sole normative owner; the glossary is a concise reference; all five subject terms and Git metadata/authentication boundaries are exact.
- **Actual:** The six implementation paths contain exactly one `Every AI-authored commit MUST use` sentence, one `[agent/task/scope/role] summary` grammar occurrence, and one `### Commit Attribution` normative section, all in `.tfw/conventions.md:153-157`. The sentence derives `agent` from the lowercase AI product in explicit context, `task` from the canonical task ID with only the no-task `project` fallback, `scope` from an established or explicitly normalized lowercase work-slice label, `role` from the canonical §15/Role Lock owner, and `summary` as short and imperative. `.tfw/glossary.md:82-84` defines first-line subject trace context, links to conventions §4, separates it from author/committer metadata and authentication, and does not repeat the grammar.
- **Match:** ✅

### V3: four preserve-and-verify paths
- **RF claim:** Canonical handoff, both installed handoff copies, and `RELEASE.md` are byte-stable to `389168a` and retain the corrected subject/push semantics.
- **Actual:** All four `389168a:path` blobs equal their current `HEAD:path` blobs: canonical handoff `00baa9b2…`, both installed copies `44fea1c0…`, and `RELEASE.md` `3ff41c29…`. Handoff Step 4 says to commit ONB using Commit Attribution and permits push only after explicit user approval. `RELEASE.md` uses `[codex/project/release/coordinator] release vX.Y.Z` and separately requires explicit approval before pushing commit and tag. Full-blob equality also proves the unrelated canonical/installed Evidence drift was not altered after the original implementation.
- **Match:** ✅

### V4: exact six-path implementation boundary and prohibited machinery
- **RF claim:** Total implementation scope is exactly six existing paths; corrective execution changes only conventions/glossary; no runtime, hook, script, schema, registry, manifest, config/state, validator, or new framework file appears.
- **Actual:** `git diff-tree -r 389168a` lists exactly the six TS allowlist paths. `git diff c7a0055..420fdbe` lists only `.tfw/conventions.md` and `.tfw/glossary.md`. Classifying `bc6779e..HEAD` after excluding explicit TFW-50 lifecycle traces and `README.md` yields exactly the same six existing paths, with zero unexpected and zero missing. No implementation path has a code/config/schema extension; `git diff --check bc6779e..HEAD` passes. Local/global `core.hooksPath` are unset and `.git/hooks/prepare-commit-msg` is absent.
- **Match:** ✅

### V5: universal roles, wider corpus, and cadence separation
- **RF claim:** One universal owner covers Coordinator, Researcher, Executor, and Reviewer; the wider corpus has no conflicting subject or automatic-push rule; no new commit cadence or duplicated grammar was added.
- **Actual:** Canonical plan/research/handoff/review role paths load conventions and resolve to §15 owners `coordinator`, `researcher`, `executor`, and `reviewer`. The complete active inventory contains 16 `.tfw/workflows` files, 19 `.tfw/adapters` files, 14 `.agent` files, 11 `.agents` skills, and 12 `.claude` files. Independent grouped scans reduce positive commit actions to handoff, docs grouping, active release, and Codex-skill inclusion. Only handoff/release formerly overrode subject/push semantics, and both are reconciled. Docs says changes share the task commit; Codex install says skills are included with the project; neither sets a subject or authorizes push. No non-task file repeats the full grammar, no automatic-push/conflicting-subject pattern exists, and added implementation text introduces no per-stage, WAIT, STOP, workflow, artifact, file, or AC commit requirement. All 11 Codex source/installed skill pairs are SHA-256 equal.
- **Match:** ✅

### V6: task traces, evidence claims, and final all-role history
- **RF claim:** Revised HL/TS/ONB, bounded RES Iteration 1, EV, and RF accurately preserve the all-role/no-cadence correction; existing history is compatibility/searchability evidence only.
- **Actual:** `research/iterations.yaml` explicitly sets one focused iteration (`min_iterations: 1`, `max_iterations: 1`), permitted by the task override, and all four numbered stages plus RES exist and are complete. Challenge explicitly rejects Extract's cadence expansion and selects C7. Reviewer commit `6c4e321ab2d2b0fa15cbf3265d5b678885417bff` contains only `review/map.md` and `review/verify.md` and uses `[codex/TFW-50/task/reviewer] record independent verification trace`. The subsequent final audit found 16/16 valid subjects in `bc6779e..HEAD`: Coordinator 3, Researcher 5, Executor 7, Reviewer 1, with zero TFW-49 subjects in the current-task range. Scopes and role owners match the traced work; Git author and committer remain separate `Sanzhar` metadata. RF/EV name prompts and rejected TFW-49 machinery only as confounders and do not use TFW-49 as TFW-50 completion.
- **Match:** ✅

### V7: tests, rendered documentation build, cleanup, and publication boundary
- **RF claim:** Docs tests pass, the integration suite performs a real MkDocs build, generated debris is removed without touching ignored user files, and the remote remains unpublished.
- **Actual:** Independent reruns produced `55 passed in 1.01s` and `13 passed in 95.08s`; after final REVIEW/README writes, the final-state rerun produced `55 passed in 1.12s` and `13 passed in 90.55s`. The integration fixture invokes `python -m mkdocs build --config-file docs/mkdocs.yml` against the real project. Each dry-run cleanup identified only `.pytest_cache/`, `docs/scripts/__pycache__/`, and `site/`; exact-target cleanup removed those three paths. The ignored user-file manifest SHA-256 remained `D13E09EA…A2BE8` before and after, and the only remaining ignored roots are `entities.json`, `mempalace.yaml`, and `tasks/TFW-36__content_marketing_blog_series/`. `origin/master` remains `bc6779e`; this Reviewer performed no push, fetch, tag, deploy, publish, or notify action.
- **Match:** ✅

### V8: source attribution and Project Values citations
- **RF claim:** The Git terminology boundary and HL/ONB knowledge citations are traceable to real sources.
- **Actual:** Official Git primary documentation confirms that commit-message text up to the first blank line is the title used as an email Subject, while author/committer information is stored separately and names do not authenticate anyone: [git-commit documentation](https://git-scm.com/docs/git-commit). All 10 HL §7.2 rows resolve; all 12 ONB §7 rows resolve, including the two additions. The cited README values, KNOWLEDGE D15/D23/D24/D28, philosophy F22, process F3/F4/F6/F22, convention F3/F5, conventions §11, and RES D1/D2/D4/D8 all exist and support the stated applications.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `git rev-parse HEAD origin/master bc6779e`; `git merge-base --is-ancestor bc6779e HEAD`; range/parent inspection | remote = baseline; baseline is ancestor; 15 commits; 0 merges |
| 2 | tree comparison for `bc6779e` and `5aef936b` | both `066795d7aff38a2b5528865e8e36bfd0a82fa94c` |
| 3 | `git diff-tree --no-commit-id --name-status -r 389168a`; `git diff c7a0055..420fdbe` | exactly six original implementation paths; exactly two corrective paths |
| 4 | `git rev-parse 389168a:path` vs `HEAD:path` for four preserve files | 4/4 byte-identical |
| 5 | grouped `rg` scans over workflows/adapters/skills/root entries | one normative owner; four action families; 0 subject/automatic-push conflicts; 0 cadence additions |
| 6 | strict regex parse of `git log --format=... bc6779e..HEAD` before and after Reviewer trace | final: 16/16 valid; 3 Coordinator, 5 Researcher, 7 Executor, 1 Reviewer; 0 TFW-49 range hits |
| 7 | `python -m pytest docs/scripts/test_gen_docs.py -q` | final state: 55 passed in 1.12s |
| 8 | `python -m pytest docs/scripts/test_integration.py -q` | final state: 13 passed in 90.55s; real MkDocs build |
| 9 | `git clean -ndX -- .pytest_cache docs/scripts/__pycache__ site`, then exact cleanup | only 3 generated roots targeted and removed; ignored-user manifest unchanged |
| 10 | hook/config/status/ref inspections | hooksPath unset; legacy hook absent; remote baseline preserved; only Reviewer traces untracked |

## Discrepancies Found

No discrepancies. RF's Reviewer item was an explicit deferral to this independent workflow, not a false claim; Reviewer commit `6c4e321` and the subsequent 16-subject final range audit now resolve it.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | `evidence/EV__TFW-50__minimal_agent_commit_attribution.md` / V1 | ✅ | ✅ — sole owner and grammar independently confirmed |
| E2 | EV V2 | ✅ | ✅ — exact terms and metadata/authentication boundaries confirmed |
| E3 | EV V3 | ✅ | ✅ — all roles are semantically covered; no cadence addition found |
| E4 | EV V4 | ✅ | ✅ — four preserve blobs independently matched `389168a` |
| E5 | EV V5 | ✅ | ✅ — exact six-path boundary and protected state confirmed |
| E6 | EV V6 | ✅ | ✅ — tests/cleanup/no-publication confirmed; current-task Reviewer commit and final all-role range audit completed independently |

## Knowledge Citations Verified

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 #1-3 | `.tfw/README.md` values: Traces Over Code, Naming Creates Behavior, Single Source of Truth, Portability | ✅ | ✅ |
| 2 | HL §7.2 #4-5 | `KNOWLEDGE.md` D15, D23, D24, D28 | ✅ | ✅ |
| 3 | HL §7.2 #6 | `knowledge/philosophy.md` F22 | ✅ | ✅ |
| 4 | HL §7.2 #7-8 | `knowledge/process.md` F3, F4, F6, F22 | ✅ | ✅ |
| 5 | HL §7.2 #9 | `.tfw/conventions.md` §11 | ✅ | ✅ |
| 6 | HL §7.2 #10 | `knowledge/convention.md` F5 | ✅ | ✅ |
| 7 | ONB §7 #1-10 | all inherited HL citations | ✅ | ✅ |
| 8 | ONB §7 #11 | `knowledge/convention.md` F3 | ✅ | ✅ |
| 9 | ONB §7 #12 | RES Iteration 1 D1, D2, D4, D8 | ✅ | ✅ |

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈10 × 0.42⌉ files and recorded findings? (10/10 plus full corpus)
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citation rows: 22 across HL/ONB, verified: 22, hallucinations: 0
- [x] Evidence artifacts from RF §5 verified (files exist, claims match)?
  - Total evidence items: 6, verified: 6, pending: 0, missing: 0

Stage complete: YES
