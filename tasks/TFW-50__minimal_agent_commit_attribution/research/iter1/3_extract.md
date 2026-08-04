# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-50](../../HL-TFW-50__minimal_agent_commit_attribution.md)
> Goal: Determine the smallest complete Markdown-only commit-attribution design that covers every real TFW commit-producing role and workflow without implying authentication or publication authority.

## Configuration Space

| Config | D1: Normative ownership | D2: Point-of-use cue placement | D3: Adapter propagation | D4: `scope` semantics | D5: `role` derivation | D6: Local/publication boundary |
|--------|-------------------------|--------------------------------|-------------------------|-----------------------|-----------------------|--------------------------------|
| C1 Canonical-only | Conventions only | No cue beyond owner | Canonical only | Normalized explicit work-slice text | Canonical workflow owner / Role Lock | Local commit; push needs approval |
| C2 Actual-action cues | Conventions only | Grouped commit checkpoints in every real producer | Canonical + installed workflow copies | Normalized explicit work-slice text | Canonical workflow owner / Role Lock | Local commit; push needs approval |
| C3 Four headline role workflows | Conventions only | One or more cues in plan/research/handoff/review | Canonical + their installed copies | Normalized explicit work-slice text | Canonical workflow owner / Role Lock | Local commit; push needs approval |
| C4 Literal-action-only | Conventions only | Existing literal commit commands only | Canonical + matching installed copies | Normalized explicit work-slice text | Canonical workflow owner / Role Lock | Local commit; push needs approval |
| C5 Source-complete / copy-stale | Conventions only | Grouped commit checkpoints in every real producer | Canonical sources only | Normalized explicit work-slice text | Canonical workflow owner / Role Lock | Local commit; push needs approval |
| C6 Broadcast-everywhere | Conventions plus repeated adapter prose | Cue in every workflow header and router | Every source, router, skill, and copy | Closed enumeration | Session/tool label | Per-file policy |

C4 is the combination not proposed in the Briefing: it is smaller than the four-role design but exposes why literal-string inventory alone is not a completeness test.

## Findings

### E1: Required configuration scoring separates semantic placement from copies

The full rule remains in exactly one place in every viable configuration. “Semantic placement” below counts a canonical owner, the glossary definition, and source files containing a short action cue; it does not mean the full rule is duplicated. “Mechanical installed copies” counts full-workflow copies that must mirror a changed canonical action but own no independent semantics.

| Configuration | Normative owners | Definition references | Point-of-use semantic cues | Total semantic placements | Mechanical installed copies | Canonical writing workflows covered | Ancillary actions covered |
|---------------|-------------------|-----------------------|----------------------------|---------------------------|-----------------------------|-------------------------------------|---------------------------|
| C1 Canonical-only | 1 | 1 | 0 | 2 | 0 | 0/10 at action time | 0/2 |
| C2 One owner + actual-action cues | 1 | 1 | 12 (10 workflows + Codex install + active release context) | 14 | 20 (10 `.agent` + 10 `.claude`) | 10/10 | 2/2 |
| C3 Cue in every headline role workflow | 1 | 1 | 4 | 6 | 8 | 4/10 | 0/2 |
| C4 Cue only at current literal commit instructions | 1 | 1 | 4 (handoff, docs, Codex install, active release context) | 6 | 4 (handoff + docs copies) | 2/10 | 2/2 |
| C5 Actual-action cues, canonical sources only | 1 | 1 | 12 | 14 | 0 | 10/10 in core; installed copies stale | 2/2 |

C2 is the smallest configuration that is complete across current canonical behavior and installed full-workflow consumers. Its apparent size is caused by 20 mechanical copies, not by 34 independent rules. C3 is smaller but does not cover the Coordinator lifecycle family. C1 relies entirely on early context loading and supplies no action-time prompt. C5 is source-complete but behaviorally incomplete for the installed `.agent` and `.claude` paths.

### E2: Exact terminology and the role-label drift

The official [`git-commit`](https://git-scm.com/docs/git-commit) manual treats text through the first blank line as the commit title/subject and defines author/committer information separately. It also states that author/committer names do not authenticate anyone. TFW therefore needs no actor, identity, credential, signature, or Git-metadata field.

| Component | Exact extracted meaning |
|-----------|-------------------------|
| Commit Attribution | A declared structured prefix in the first line of an AI-authored commit message. It is trace context only and does not modify or authenticate Git author/committer metadata |
| `agent` | Stable lowercase AI product/tool name from explicit session context; not a person, account, model version, Git author, Git committer, or hosting actor |
| `task` | Canonical TFW task ID; use `project` only when the current workflow genuinely has no task |
| `scope` / work slice | Normalized lowercase text derived from the explicit current work-slice label. It is open text, not a registry; spaces and separators normalize to a readable slug such as `phase-a` or `iter1` |
| `role` | One of the four lowercase TFW roles, derived from the canonical workflow owner in conventions §15 and confirmed by an inline Role Lock where present: `coordinator`, `researcher`, `executor`, or `reviewer` |
| `summary` | Short imperative remainder of the one-line subject after one space; no numeric length protocol, body schema, or trailer |

Current label drift must be fixed or explicitly overridden at the same source point; it must not create new values:

- `.tfw/workflows/docs.md` says `Coordinator / Reviewer`, but conventions §15 owns `/tfw-docs` as Coordinator. An AI crossing from review into docs changes to the Coordinator workflow owner; `reviewer` remains valid only inside `/tfw-review`.
- `.tfw/workflows/release.md` says `Coordinator / Maintainer`, but `maintainer` is not a TFW role. An AI running `/tfw-release` uses `coordinator`; a human maintainer is outside the AI-authored rule.
- `update.md` already says Coordinator. `plan`, `research`, `handoff`, `review`, `resume`, `knowledge`, `init`, and `config` have unambiguous canonical ownership.

The extracted rule should therefore refine the existing conventions sentence, not add a role registry or adapter-specific interpretation: `scope` comes from normalized explicit work-slice text; `role` comes from canonical TFW workflow ownership/Role Lock.

### E3: Exact grouped commit checkpoints

A commit checkpoint is a durable workflow boundary: role handoff, mandatory WAIT/STOP after a completed trace, or a coherent verified implementation slice. It groups all accumulated in-scope changes owned by that workflow since the prior checkpoint. It does **not** require one commit per file, artifact, acceptance criterion, or edit.

| Included canonical workflow | Exact checkpoint(s) | Changes grouped into the checkpoint | Explicit non-checkpoints |
|-----------------------------|---------------------|-------------------------------------|--------------------------|
| `.tfw/workflows/plan.md` | (1) Immediately before each STOP that hands approved planning/research-control traces to `/tfw-research`; (2) after TS approval and before the final STOP/handoff to `/tfw-handoff` | Task Board, HL, TS, `iterations.yaml`, and other Coordinator-owned planning traces accumulated since the previous boundary | Do not commit after each HL revision, question, YAML field, or phase table edit |
| `.tfw/workflows/research/base.md` | After completed Briefing and after each Gather, Extract, and Challenge stage file, before its mandatory WAIT; then after `RES.md` synthesis before the final STOP | One completed stage trace per stage checkpoint; final RES at iteration closure | Do not commit template copy-on-enter, partial OODA writes, or every source note |
| `.tfw/workflows/handoff.md` | (1) Existing ONB checkpoint before approval WAIT; (2) incremental commits only for coherent verified implementation work slices; (3) one final checkpoint after EV/RF/Task Board traces are complete and before Executor STOP | ONB; cohesive implementation slices; remaining evidence/result traces at closure | Do not commit each changed file, AC row, test run, or evidence attachment separately |
| `.tfw/workflows/review.md` | After each Map, Verify, and Judge stage passes its self-check; then one final checkpoint after REVIEW, tech-debt triage, and Reviewer-owned Task Board updates, before transition to Coordinator-owned docs/knowledge | One completed review stage at each stage boundary; all final Reviewer traces together | Do not commit each checklist row, verification command, or observation separately |
| `.tfw/workflows/docs.md` | Once, after approved KNOWLEDGE/TECH_DEBT changes and the `tfw-docs` marker are complete | All docs-workflow changes for the task | Do not commit KNOWLEDGE sections separately; do not merge this into the prior Reviewer-role commit |
| `.tfw/workflows/knowledge.md` | Once, after final approval and all topic/index/state/processed-marker writes are complete | All consolidation changes | Do not commit each fact or category file separately |
| `.tfw/workflows/release.md` | Once, after CHANGELOG/VERSION/config updates and before any tag or publication action | One local release commit | Tagging is not another commit; no push without explicit approval |
| `.tfw/workflows/init.md` | Attach/repair branch: once after adapter verification and before report/STOP. Full-init branch: once after Phase 5 verification, init RF, and Task Board closure | All tracked initialization or repair changes; ignored personal preferences remain excluded | Do not commit each copied adapter/workflow/skill separately |
| `.tfw/workflows/update.md` | Once, after Step 8 verification and cleanup, before the final report | All verified framework/config/adapter update changes | Do not commit each copied framework category or adapter separately |
| `.tfw/workflows/config.md` | Edit mode only: once after approved batch update, adapter sync, and successful verification. Verify mode: no commit | One coherent config propagation batch | No commit for read-only verification; no commit after each inline value |

Ancillary point-of-use files must point to these same checkpoints, not create extra ones:

- `.tfw/adapters/codex/README.md`: installed skills are included in the surrounding `init` or `update` checkpoint using Commit Attribution; “commit the skills” must not imply a separate per-adapter commit.
- `RELEASE.md`: retain the current subject example and explicit push boundary, but identify its commit step as the single canonical release checkpoint rather than a second release commit.

### E4: Smallest complete future-TS inventory

#### Semantic source surfaces

| Path | Disposition | Exact future-TS treatment |
|------|-------------|---------------------------|
| `.tfw/conventions.md` | **MODIFY; preserve owner** | Keep the sole rule and example; refine only `scope` as normalized explicit work-slice text and `role` as canonical TFW workflow owner/Role Lock |
| `.tfw/glossary.md` | **PRESERVE; no edit required** | Keep the concise definition/link and non-authentication boundary; do not add the full grammar again |
| `.tfw/workflows/plan.md` | **MODIFY — add grouped cues** | Add the two planning handoff checkpoints from E3 |
| `.tfw/workflows/research/base.md` | **MODIFY — add grouped cues** | Add completed stage-before-WAIT and final RES-before-STOP commits |
| `.tfw/workflows/handoff.md` | **MODIFY; preserve existing cue** | Keep ONB wording; add coherent incremental and final EV/RF trace checkpoints |
| `.tfw/workflows/review.md` | **MODIFY — add grouped cues** | Add Map/Verify/Judge stage commits and final Reviewer trace commit |
| `.tfw/workflows/docs.md` | **MODIFY existing action + label** | Replace the unattributed task-commit line with one docs checkpoint and align the AI workflow label to canonical Coordinator ownership |
| `.tfw/workflows/knowledge.md` | **MODIFY — add grouped cue** | Add one post-approval final consolidation checkpoint |
| `.tfw/workflows/release.md` | **MODIFY — add grouped cue + label** | Add one local release commit before tag/publication and align the AI workflow label to canonical Coordinator ownership |
| `.tfw/workflows/init.md` | **MODIFY — add branch-final cues** | Add one attach/repair closure checkpoint and one full-init closure checkpoint |
| `.tfw/workflows/update.md` | **MODIFY — add grouped cue** | Add one verified final update checkpoint |
| `.tfw/workflows/config.md` | **MODIFY — add edit-only cue** | Add one post-sync verified edit checkpoint; explicitly no commit in verify mode |
| `.tfw/adapters/codex/README.md` | **MODIFY existing action** | Make installed skills part of the surrounding init/update attributed commit, not a separate semantic rule or commit |
| `RELEASE.md` | **MODIFY; preserve current example/boundary** | Keep the compliant example and explicit push approval; clarify that it is the single canonical release checkpoint |

There are **no new implementation files**. The semantic design has 14 placements, but only 13 existing semantic files require further edits because `.tfw/glossary.md` is preserved as-is.

#### Mechanically required installed copies

Each file below is **MODIFY — surgical sync of only the corresponding canonical role label/checkpoint cue; preserve all unrelated drift**.

`.agent` installed workflows (10):

```text
.agent/workflows/tfw-plan.md
.agent/workflows/tfw-research.md
.agent/workflows/tfw-handoff.md
.agent/workflows/tfw-review.md
.agent/workflows/tfw-docs.md
.agent/workflows/tfw-knowledge.md
.agent/workflows/tfw-release.md
.agent/workflows/tfw-init.md
.agent/workflows/tfw-update.md
.agent/workflows/tfw-config.md
```

`.claude` installed commands (10):

```text
.claude/commands/tfw-plan.md
.claude/commands/tfw-research.md
.claude/commands/tfw-handoff.md
.claude/commands/tfw-review.md
.claude/commands/tfw-docs.md
.claude/commands/tfw-knowledge.md
.claude/commands/tfw-release.md
.claude/commands/tfw-init.md
.claude/commands/tfw-update.md
.claude/commands/tfw-config.md
```

Known canonical/copy drift in handoff, knowledge, init, and update must remain byte-for-byte unchanged outside the exact TFW-50 cue/role-label lines. The 20 files are mechanical propagation, not 20 additional design decisions.

#### Explicit exclusions

| Path/group | Disposition | Reason |
|------------|-------------|--------|
| `.tfw/workflows/resume.md`, `.agent/workflows/tfw-resume.md`, `.claude/commands/tfw-resume.md` | **EXCLUDE** | Resume's write path explicitly delegates to plan; a second cue would duplicate the same checkpoint |
| `.agent/workflows/tfw-task.md`, `.claude/commands/tfw-task.md` | **EXCLUDE** | Non-canonical stale meta-workflows (TD-123); owned actions remain in plan/handoff |
| `.tfw/adapters/codex/skills/tfw-*/SKILL.md`, `.agents/skills/tfw-*/SKILL.md` | **EXCLUDE** | Thin routers already load conventions and canonical workflows; source/installed pairs are exact copies |
| `AGENTS.md`, `CLAUDE.md`, `.agent/rules/*`, `.tfw/adapters/*` entry templates other than the Codex README action | **EXCLUDE** | Always-loaded references, not commit checkpoints; no need to duplicate rule or cue |
| `.tfw/templates/RELEASE.md` and all artifact/stage templates | **EXCLUDE** | Formats outputs; canonical workflow owns action timing. The generic release template does not require Git |
| `.tfw/project_config.yaml`, `.tfw/knowledge_state.yaml`, schemas, manifests, registries | **EXCLUDE** | No runtime/config enforcement and no closed scope/role registry |
| Hooks, Git config, Python or other scripts, validators, tests for runtime recognition | **EXCLUDE** | Explicit no-runtime boundary |
| README, KNOWLEDGE, TECH_DEBT, VERSION, CHANGELOG and historical task artifacts as implementation files | **EXCLUDE** | Not point-of-use consumers for this change; normal future workflow traces are separate from implementation scope |

#### Scope-budget packaging for `/tfw-plan`

The complete 33-file edit surface exceeds a single phase's 12-modified-file budget even though 20 files are mechanical copies. The smallest budget-compliant packaging is:

1. **Phase A — canonical owner and workflow actions (11 files):** `.tfw/conventions.md` plus the 10 included canonical workflows.
2. **Phase B — ancillary actions + Antigravity copies (12 files):** `.tfw/adapters/codex/README.md`, `RELEASE.md`, and the 10 `.agent` workflows.
3. **Phase C — Claude copies (10 files):** the 10 `.claude` commands.

`.tfw/glossary.md` remains a verification target but not a changed file. This phase split measures semantic sources separately from mechanical propagation and does not pretend that a smaller incomplete file list is “minimal.”

### E5: Provisional configuration decision

C2 (one owner plus grouped cues at actual commit checkpoints) is the provisional smallest complete configuration for Challenge:

- one full normative rule, not one per role;
- action-time cues for all four roles and the Coordinator workflow family;
- exact Researcher and Reviewer stage/final trace commits;
- open normalized work-slice text, not a registry;
- canonical TFW role ownership, with docs/release drift corrected rather than legitimized;
- 20 installed copies treated as mechanical sync;
- no cue for read-only/delegating resume, no per-artifact commits, and no runtime.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Scored configuration space; precise role/scope terms; exact grouped checkpoints for 10 canonical workflows; exact 33-file complete surface; preserve/modify/exclude dispositions; budget-compliant three-phase packaging | Falsify C2 through pairwise consistency checks: duplicate/double-commit risk, role-transition correctness, adapter drift preservation, release/init edge cases, and whether any included or excluded file changes completeness |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?

Stage complete: YES
→ User decision: Pending Coordinator checkpoint approval
