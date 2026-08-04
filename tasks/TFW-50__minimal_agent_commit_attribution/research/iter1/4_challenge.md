# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW-50](../../HL-TFW-50__minimal_agent_commit_attribution.md)
> Goal: Determine the smallest complete Markdown-only commit-attribution design that covers every real TFW commit-producing role and workflow without implying authentication or publication authority.

## Consistency Check

### Added configuration C7

**C7 — Universal applicability + conflict reconciliation:** one universal conventions owner, one concise glossary definition, edits only where an existing instruction contradicts/overrides the subject rule or push boundary, and verification that actual commits from all four roles use the format. The universal quantifier covers roles; it does not prescribe when or how often they commit.

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1: Normative ownership | Conventions only | D2: Cue placement | Repeat the full rule in workflows/adapters | Creates multiple semantic owners and drift |
| D2: Cue placement | Every artifact-producing checkpoint MUST commit | TFW-50 scope | Format existing commits only | Adds a new cadence policy not authorized by the task |
| D2: Cue placement | Literal action strings define all consumers | D3: Coverage | All four roles | Literal absence does not negate universal applicability or real role commits |
| D3: Adapter propagation | Edit every installed copy | Canonical source | Source workflow is unchanged or canonical is loaded at runtime | Mechanical churn has no behavior delta |
| D4: `scope` semantics | Closed enumeration | Actual context | New explicit work-slice labels can occur | A registry would be incomplete by construction and add config-like enforcement |
| D5: `role` derivation | Hybrid/tool label | Canonical four-role ownership | `maintainer`, `Coordinator / Reviewer`, or actor values | Produces values outside the TFW role taxonomy |
| D6: Publication boundary | Commit and push together | Universal rule | Push only after explicit user approval | Local trace creation is not publication authority |

**Surviving configurations:**

| Config | D1 | D2 | D3 | Notes |
|--------|----|----|----|-------|
| C4 Literal-action-only | Conventions owner | Add cues to every current explicit positive commit instruction | Canonical + matching installed copies | Consistent, but adds reminders to non-conflicting docs/Codex install instructions |
| C7 Universal + conflicts | Conventions owner | Reconcile only contradictions/overrides; no cadence rule | Only copies containing the conflicting instruction | Complete under the actual context-loading contract and smaller than C4 |

**Unexpected survivors:**

- **C7:** The initially rejected “small” surface survives once applicability is separated from cadence. Universal scope plus mandatory context loading covers roles without role-specific cues.
- **C4:** It is behaviorally harmless, but survives only as a larger non-minimal alternative; its extra docs/install cues do not resolve a real conflict.

## Findings

### C1: Extract E3 incorrectly turned formatting into cadence

Two independent statements were conflated:

```text
Formatting rule: IF an AI-authored commit is made, its subject MUST use Commit Attribution.
Cadence rule: The workflow MUST make a commit at checkpoint X.
```

TFW-50 authorizes the first and does not authorize the second. Existing canonical semantics say that Executor makes incremental commits and explicitly commits ONB; they do not require commits after every Research or Review stage, every workflow STOP, or every artifact write. Research/base requires the stage file to exist before WAIT, not a Git commit. Review requires stage files and self-checks, not Git commits.

Therefore the E3 checkpoint table is **not** a TFW-50 implementation recommendation. It is retained only as an inventory of possible future cadence choices. Adding those cues now would change workflow frequency and lifecycle behavior, exactly the scope expansion C7 is meant to prevent.

This research session's Briefing/Gather/Extract commits demonstrate that Researcher-authored stage traces can use the rule. Their timing was explicitly requested in the delegation and cannot be cited as proof that canonical research semantics already mandates per-stage commits.

### C2: Re-score C1, C4, and C7 under the actual context contract

The four headline workflows all load conventions directly, and their Codex skills explicitly load conventions before the canonical workflow. Coordinator lifecycle skills do the same. Root Claude/Antigravity/Codex entry paths also make conventions part of startup context. Under that contract, a universal `Every AI-authored commit MUST...` sentence applies to Coordinator, Researcher, Executor, and Reviewer without one cue per role.

| Configuration | Normative owner | Glossary | Conflict semantic surfaces | Mechanical copies | Role applicability | Cadence expansion | Result |
|---------------|------------------|----------|----------------------------|-------------------|-------------------|-------------------|--------|
| C1 Canonical-only from the pre-TFW-50 baseline | 1 | 1 | 0 | 0 | All four roles load it | None | **Eliminate:** old handoff still coupled commit+push and old `RELEASE.md` prescribed `release: vX.Y.Z`, so explicit local instructions overrode/contradicted the rule |
| C4 Cue at every literal positive commit instruction | 1 | 1 | 4: handoff, docs, Codex install, active release | 4: handoff + docs installed copies | All four roles load it | None | **Eliminate as dominated:** complete, but docs and Codex install never prescribe a conflicting subject or push; their extra cues add no distinct behavior |
| C7 Universal + conflict reconciliation | 1 | 1 | 2: handoff, active release | 2: handoff installed copies | All four roles load it | None | **Survive:** resolves every actual conflict with 4 semantic placements + 2 mechanical copies |

Evaluated against the **current** tree, C1 is no longer independent: keeping the already reconciled handoff/release text makes it C7. The relevant comparison is therefore baseline C1 versus current C7, not “delete the current reconciliation and call it canonical-only.”

The earlier C2 actual-checkpoint configuration is eliminated: 14 semantic placements, 20 copies, and a three-phase plan buy cadence changes that TFW-50 neither requested nor needs. C3 is incomplete if interpreted as four headline workflows and redundant if expanded to every writing workflow. C5 leaves active full-copy conflicts stale. C6 duplicates semantics everywhere.

### C3: Actual lifecycle commits prove applicability, not causality

Marked local/all-ref history currently contains 18 Coordinator, 3 Researcher, 13 Executor, and 5 Reviewer subjects in the format. TFW-50 itself contains Coordinator (`9aaf1f9`, `056378a`), Executor (`c204f8a`, `46fe8b1`, `389168a`), and Researcher (`8a190d5`, `ad16b1a`, `5035ab3`) examples. TFW-49 supplies Reviewer examples.

This proves four things:

1. Every role can express `agent/task/scope/role` with the same grammar.
2. Real Coordinator scopes already include `task`, `master`, `research`, `docs`, and `knowledge`; Researcher uses `iter1`; phase roles use `phase-a` etc. This supports open normalized work-slice text rather than a registry.
3. The format is searchable in `git log` and coexists with separate Git author/committer fields.
4. No role-specific workflow wording is technically required to form a valid subject.

It does **not** prove that the conventions sentence alone caused compliance. Coordinator/Executor/Researcher received explicit delegation text, and the Reviewer examples come from the rejected TFW-49 mechanism/history. Stronger current models and mandatory context loading make C7 plausible, but prompt compliance remains a bounded behavioral claim, not causal evidence or authentication.

The official [`git-commit`](https://git-scm.com/docs/git-commit) manual reinforces the boundary: the first line is commit title/subject; author and committer are separate inputs; their names themselves do not authenticate. C7 changes only subject text.

### C4: Only two pre-existing instruction families actually conflicted

The exhaustive literal inventory has four positive action families. Applying the inclusion test — “Would current text contradict, override, or ambiguously derive the universal rule?” — yields:

| Existing instruction | Baseline behavior | Conflict test | C7 disposition |
|----------------------|-------------------|---------------|----------------|
| Canonical handoff + `.agent`/`.claude` copies | `Commit and push ONB` | Contradicts separate push authority; point-of-use text must change | Include all three; current correction is necessary |
| Active `RELEASE.md` | `Git commit: release: vX.Y.Z`; unconditional push | Overrides subject grammar and publication boundary | Include; current correction is necessary |
| Canonical docs + copies | “Commit knowledge changes with the task commit (not separately)” | Sets grouping only; no subject or push override. Universal rule applies | Verification-only; no TFW-50 edit |
| Codex adapter README | Commit installed skills with the project | Sets repository inclusion only; no subject or push override. Universal rule applies | Verification-only; no TFW-50 edit |

This recovers the logic of the six-file implementation without pretending that the three handoff files are three semantic decisions: they are one conflict plus two runtime copies.

### C5: Role precision does not require a broad role-label cleanup

The role definition must be made authoritative in the normative sentence:

> `role` is the lowercase canonical TFW workflow owner from conventions §15, confirmed by the workflow Role Lock where present.

Exact candidate sentence for the future TS:

> Every AI-authored commit MUST use `[agent/task/scope/role] summary`: set `agent` to the normalized lowercase AI product name from explicit context, `task` to the canonical TFW task ID (`project` only when none exists), `scope` to the established lowercase explicit work-slice slug or otherwise a lowercase hyphenated form of its explicit label, and `role` to the lowercase canonical TFW workflow owner from §15/Role Lock; keep `summary` short and imperative, commit locally, and push only after explicit user approval.

That precedence gives `/tfw-docs` and `/tfw-release` the value `coordinator`. It does not admit `maintainer` or a hybrid `coordinator-reviewer` value.

Current drift remains real:

- `docs.md` says `Coordinator / Reviewer` while conventions §15 owns docs as Coordinator.
- `release.md` says `Coordinator / Maintainer` while conventions §15 owns release as Coordinator.

It does not have to be fixed inside TFW-50 because the refined canonical rule resolves the derivation, the current release example already uses `coordinator`, and actual marked docs commits use `docs/coordinator`. Editing both canonical labels and four installed copies would turn a two-line terminology inconsistency into a six-file role-cleanup branch with no observed subject error. Treat those files as verification-only: a future docs/release AI commit using `reviewer` or `maintainer` fails TFW-50 verification. Label normalization may be a separate consistency cleanup if that failure or user demand occurs.

### C6: Installed copies follow changed runtime text, not file-count symmetry

The 20-copy plan fails the value test. A copy is mandatory only when:

1. its canonical source is changed by TFW-50; and
2. the tool executes the copy rather than loading that canonical source; and
3. leaving it unchanged preserves a contradiction.

Only `.agent/workflows/tfw-handoff.md` and `.claude/commands/tfw-handoff.md` meet all three conditions. They contained the same auto-push conflict as canonical handoff. The other installed workflows need no edit because their canonical workflow text is not changed and the universal conventions rule is already in tool context. Codex skills load the canonical workflow and conventions, so no skill source/copy changes are required.

C7 therefore needs no phase split. The six-file surface is under both current file budgets and is safer to review as one bounded change. Mechanical symmetry is not a reason to create phases.

### C7: Exact smallest complete future-TS inventory

#### Minimum normative core

| Path | Disposition | Exact treatment |
|------|-------------|-----------------|
| `.tfw/conventions.md` | **MODIFY within existing section** | Preserve the sole grammar/example/push rule; make `agent`, `task`, normalized explicit work-slice `scope`, canonical-owner/Role-Lock `role`, and imperative `summary` derivation exact in the one normative sentence |
| `.tfw/glossary.md` | **MODIFY minimally** | Keep one concise definition/link; state explicitly that subject attribution is separate from Git author/committer metadata and authentication. Do not duplicate grammar |

#### Minimum conflict-reconciliation surface already implemented

| Path | Disposition | Exact treatment |
|------|-------------|-----------------|
| `.tfw/workflows/handoff.md` | **PRESERVE + VERIFY** | Keep corrected ONB Commit Attribution cue and explicit push approval; add no new checkpoint/cadence instruction |
| `.agent/workflows/tfw-handoff.md` | **PRESERVE + VERIFY derived copy** | Keep only the same corrected Step 4; preserve unrelated Evidence drift |
| `.claude/commands/tfw-handoff.md` | **PRESERVE + VERIFY derived copy** | Keep only the same corrected Step 4; preserve unrelated Evidence drift |
| `RELEASE.md` | **PRESERVE + VERIFY** | Keep compliant release example and explicit push approval |

**ADD:** no implementation files, hooks, scripts, schemas, registries, manifests, tests for runtime enforcement, config values, or workflow cadence rules.

The final TFW-50 implementation allowlist is the same six paths as commit `389168a`. Future execution should modify only the two normative-core files if the exact terminology checks require it; the four reconciled files are in-scope verification targets and should remain byte-stable unless a discovered contradiction demands correction.

#### Verification-only consumers — no edits

| Consumer group | Verification |
|----------------|--------------|
| `.tfw/workflows/plan.md`, `research/base.md`, `review.md`, `resume.md`, `docs.md`, `knowledge.md`, `release.md`, `init.md`, `update.md`, `config.md` | Confirm no subject format or automatic-push text contradicts conventions; when a commit exists, applicability is universal |
| `.agent/workflows/*` and `.claude/commands/*` other than handoff | Confirm no independent conflicting subject/push instruction; do not sync for symmetry |
| `.tfw/adapters/codex/README.md` | Confirm “commit skills with project” does not prescribe a conflicting subject/push |
| `.tfw/adapters/codex/skills/tfw-*/SKILL.md` and `.agents/skills/tfw-*/SKILL.md` | Confirm conventions + canonical workflow loading and exact source/installed equality |
| `AGENTS.md`, `CLAUDE.md`, `.agent/rules/*`, adapter entry templates | Confirm conventions are always loaded; no added wording |
| Canonical docs/release labels | Verify expected AI role is `coordinator` by conventions §15; do not accept `maintainer` or a hybrid role in a subject |
| `git log` | Verify representative Coordinator, Researcher, Executor, and Reviewer subjects; report explicit-prompt/runtime confounders rather than claiming causality |

#### Explicit exclusions

- All per-stage/per-STOP/per-artifact commit requirements proposed in Extract E3.
- All 20 broad installed-copy edits and the three-phase packaging derived from them.
- `.tfw/workflows/docs.md`, `.tfw/workflows/release.md`, and their copies as role-label implementation changes.
- `.tfw/workflows/resume.md` and stale `tfw-task` meta-workflows.
- Codex skill sources/installed copies, other adapter entrypoints, templates, project/state config, hooks, scripts, validators, manifests, schema, runtime, version files, and historical task artifacts.

#### Optional future cadence improvements outside TFW-50

If the project later wants commit frequency as methodology, plan it separately with evidence and explicit approval. Candidate questions include Researcher stage-vs-iteration commits, Reviewer stage-vs-final commits, Coordinator workflow closure commits, Executor coherent-slice grouping, and whether docs/knowledge should share or separate commits. None is decided by Commit Attribution.

### C8: Hypothesis impact

| Hypothesis | Challenge verdict | Reason |
|------------|-------------------|--------|
| H1: one owner + cues only at actual commit actions | **Refined** | One owner is sufficient for applicability; cues are required only to reconcile an actual contradictory instruction, not every place a commit may happen |
| H2: field set is minimal and precise | **Supported with term refinement** | Five subject components remain sufficient; `scope` must be normalized open work-slice text and `role` must come from canonical TFW ownership |
| H3: consumer classes differ | **Supported** | Semantic owner, conflict point, always-loaded reference, and derived runtime copy have different obligations |
| H4: prompt compliance is sufficient without enforcement | **Boundedly supported, not causally proven** | Current all-role history is compatible with the rule, but delegation prompts and rejected prior mechanisms confound attribution of success |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C7 survives hard attack; cadence expansion removed; C1/C4/C7 re-scored under actual context; six-file allowlist restored; only two normative files may need wording refinement; other consumers are verification-only; 20-copy/three-phase plan rejected | Coordinator must approve Challenge before RES synthesis; final RES must preserve the causal limitation and exact include/exclude inventory |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked? Surviving configurations listed?

Stage complete: YES
→ User decision: Pending Coordinator checkpoint approval
