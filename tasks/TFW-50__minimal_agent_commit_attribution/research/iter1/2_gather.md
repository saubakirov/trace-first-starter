# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-50](../../HL-TFW-50__minimal_agent_commit_attribution.md)
> Goal: Determine the smallest complete Markdown-only commit-attribution design that covers every real TFW commit-producing role and workflow without implying authentication or publication authority.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: Normative ownership | Conventions only | Glossary only | Each role workflow | Each tool adapter |
| D2: Point-of-use cue placement | No cue beyond owner | Literal commit commands only | Every artifact-producing commit checkpoint | One cue in every role workflow header |
| D3: Adapter propagation | Canonical workflow only | Canonical + active installed workflow copies | Entry routers only | Every source, router, skill, and copy |
| D4: `scope` / work-slice semantics | Closed enumeration | Unnormalized explicit-context text | Normalized lowercase work-slice slug | Artifact path |
| D5: `role` derivation | Inline Role Lock | Canonical owner table | Session label | Tool account/actor |
| D6: Local/publication boundary | Commit and push together | Local commit by default; push needs approval | No push language in the rule | Per-workflow publication policy only |

## Findings

### G1: Exhaustive `rg` inventory, grouped by consumer class

The sweep covered the current framework and adapter corpus, not historical task artifacts: 16 files under `.tfw/workflows`, 19 under `.tfw/adapters`, 14 under `.agent`, 11 under `.agents`, and 12 under `.claude` (72 paths total), plus the root entry files and `RELEASE.md`. The inventory used `rg` for filenames, commit/push language, convention-loading references, and Role Lock/write actions. Deep inspection was limited to the 11 canonical writing workflows, the six-file implementation diff, the Codex install action, and grouped source/copy comparisons.

Representative inventory commands:

```text
rg -n -i --hidden --glob '*.md' --glob '*.yaml' --glob '!tasks/**' --glob '!.git/**' '(git\s+(add|commit|push)|\bcommit(s|ted|ting)?\b|\bpush(ed|ing)?\b)' .
rg -n -i -C 1 '(ROLE LOCK|\bwrite\b|\bcreate\b|\bupdate\b|\bcommit\b|\bpush\b|Task Board)' .tfw/workflows/...
rg -n --hidden --glob '!tasks/**' --glob '!.git/**' '(conventions\.md|\.tfw/conventions)' AGENTS.md CLAUDE.md .agent .agents .claude .tfw/adapters
```

| Consumer class | Exact current paths | Inventory result | Interpretation |
|----------------|---------------------|------------------|----------------|
| Canonical semantic owner | `.tfw/conventions.md` §4 | Contains the only full normative sentence and example | One semantic consumer and source of truth |
| Concise terminology reference | `.tfw/glossary.md` | Defines Commit Attribution and links to conventions | Discoverability/reference, not a second rule owner |
| Explicit canonical commit action | `.tfw/workflows/handoff.md:64` | Commits ONB using Commit Attribution; separates push approval | Real Executor point of use, but only one of several Executor commit checkpoints |
| Explicit canonical commit action without attribution cue | `.tfw/workflows/docs.md:55` | Says to commit knowledge changes with the task commit | Real Coordinator point of use; incomplete wording |
| Project-specific release action | `RELEASE.md:56-58` | Uses Commit Attribution, tags, then requires approval before push | Real current-project release point of use; not portable canonical coverage |
| Tool-adapter install action without attribution cue | `.tfw/adapters/codex/README.md:89-91` | Explicitly says to commit installed `tfw-*` skills with the project | Real Coordinator `init`/`update` commit point missed by the six-file implementation |
| Canonical artifact-producing workflows with no literal commit cue | `.tfw/workflows/plan.md`, `research/base.md`, `review.md`, `knowledge.md`, `release.md`, `init.md`, `update.md`, `config.md` | Each owns writes that become local commits; literal-string absence is not negative evidence | Must be evaluated by ownership and history, not `rg` alone |
| Indirect writing workflow | `.tfw/workflows/resume.md` | Writes Phase HL/TS only by invoking the plan flow | Consumer of plan's eventual commit checkpoint, not necessarily a separate commit action |
| Always-loaded references | `AGENTS.md`, `CLAUDE.md`, `.agent/rules/{agents.md,tfw.md}`, adapter entry templates, Codex skills | Load conventions before role work | Make canonical-only behavior plausible, but do not provide action-time recall |
| Derived installed workflow copies | `.agent/workflows/tfw-*.md`, `.claude/commands/tfw-*.md` | Full copies for Claude/Antigravity-style discovery | Mechanical consumers only when their canonical workflow gets a point-of-use cue |
| Codex router source + installed copies | `.tfw/adapters/codex/skills/tfw-*/SKILL.md`, `.agents/skills/tfw-*/SKILL.md` | All 11 source/installed pairs are byte-identical; each routes to its canonical workflow | Routers, not independent commit-action owners |
| Legacy meta-workflows | `.agent/workflows/tfw-task.md`, `.claude/commands/tfw-task.md` | Non-canonical plan+handoff orchestrators; tracked as stale in TD-123; absent from Codex by design | Exclude; their owned actions remain in plan/handoff |
| Non-consumer mentions | deploy history, changelog entries, `DO NOT COMMIT` personal-file warnings, historical tasks | Match words but do not instruct a TFW role to make an attributed local commit | Exclude from behavioral coverage |

The literal action inventory is therefore not the consumer inventory. It finds four current positive action families (handoff, docs, project release, Codex install), while ownership adds the other artifact-producing workflows.

### G2: Exact commit-producing role/workflow matrix

`git log --all` confirms that the subject convention is already used by every TFW role: 18 marked Coordinator commits, 1 Researcher commit, 13 Executor commits, and 5 Reviewer commits. TFW-50 itself contains Coordinator (`9aaf1f9`, `056378a`), Executor (`c204f8a`, `46fe8b1`, `389168a`), and Researcher (`8a190d5`) local commits; the Reviewer evidence comes from TFW-49. Coordinator subworkflow evidence includes `docs` (`cdc75a6`, `5fabe2e`, `40d1b31`) and `knowledge` (`8e9e330`). These counts are evidence of real behavior, not a proposed enforcement mechanism.

| Workflow / action | Effective TFW role | Files it creates or updates | Current commit instruction | History / ownership evidence | Consumer conclusion |
|-------------------|--------------------|-----------------------------|----------------------------|------------------------------|--------------------|
| `/tfw-plan` | Coordinator | Task folder, HL, TS, Task Board, `iterations.yaml`, research-applied HL updates | None | TFW-50 Coordinator commits changed HL/TS and research control | Direct commit producer; needs an action cue at completed planning traces |
| `/tfw-research` | Researcher | `1_briefing.md` through `4_challenge.md`, then `RES.md` | None | `8a190d5` commits the Briefing at its mandatory WAIT; current protocol writes before every WAIT | Direct commit producer; stage and RES checkpoints must be covered |
| `/tfw-handoff` | Executor | ONB, implementation, evidence, RF, Task Board | ONB only uses Commit Attribution; glossary/conventions separately say incremental commits | Three TFW-50 Executor commits cover ONB, execution transition, and implementation | Direct producer; preserve ONB cue but cover incremental/final traces too |
| `/tfw-review` | Reviewer | `review/{map,verify,judge}.md`, REVIEW, TECH_DEBT, Task Board | None | Five marked Reviewer commits in TFW-49 | Direct producer; review stage/final checkpoints must be covered |
| `/tfw-resume` | Coordinator | Status matrix; Phase HL/TS only through `plan.md` Phase 4 flow | None | Canonical step 12 explicitly delegates writing to plan | Indirect producer; a plan cue can cover it without a duplicate resume cue |
| `/tfw-docs` | Coordinator per conventions §15 | KNOWLEDGE §1-§3, TECH_DEBT, REVIEW marker | “Commit knowledge changes with the task commit” | Three marked `docs/coordinator` commits | Direct explicit producer; replace/extend the existing cue. `docs.md`'s inline “Coordinator / Reviewer” label is role-owner drift |
| `/tfw-knowledge` | Coordinator | Topic files, KNOWLEDGE §4, knowledge state, candidate markers | None | `8e9e330` is a marked `knowledge/coordinator` commit | Direct producer; needs a cue after approved final writes |
| `/tfw-release` + active `RELEASE.md` | Coordinator per conventions §15 | CHANGELOG, VERSION, project config; release commit/tag and optional publication | Canonical workflow has no commit cue; current `RELEASE.md` does | Workflow delegates extra Git steps to active release context | Direct producer; keep current project cue and add portable canonical action coverage |
| `/tfw-init` | Coordinator | Project config/state, task tree, root docs, adapters, init RF, Task Board | Only a negative personal-file warning | Canonical owner writes a complete tracked TFW installation | Direct producer; needs a final local-commit cue. Codex install has an additional explicit action in its README |
| Codex Install or Repair | Coordinator through init/update | Root routing block and `.agents/skills/tfw-*` installed copies | “Commit ... with the project,” no attribution reference | Exact point of use in `.tfw/adapters/codex/README.md` | Direct adapter commit action; needs a short cue, while the skill files themselves do not |
| `/tfw-update` | Coordinator | Framework files, config version marker, adapter copies | None | Workflow executes a tracked framework upgrade and adapter resync | Direct producer; needs a final local-commit cue after verification |
| `/tfw-config` | Coordinator | Project config, inline workflow/convention values, adapter copies | None | Workflow explicitly performs an approved batch write and sync | Direct producer; needs a cue after verification |

The matrix disproves the earlier handoff-centered model. Executor is only one of four committing roles, and Coordinator is a family of commit-producing workflows rather than a single planning action.

### G3: Canonical, always-loaded, and derived consumers are not equal

For all 11 workflow mappings, the `.agent` and `.claude` installed copies are byte-identical to each other. Seven mappings also equal canonical byte-for-byte. Four already contain unrelated drift from canonical: `handoff` (Evidence block), `knowledge` (RF section number), `init` (Codex attach/repair additions absent), and `update` (Codex resync additions absent). Any future cue propagation into these copies must therefore be surgical; a bulk overwrite would absorb unrelated TFW-50-external changes.

Codex has a different topology: each repository-local skill is a thin router that loads conventions and reads the canonical workflow completely. All 11 installed/source skill pairs currently match. Adding full rule text or workflow cues to both skill layers would make routers semantic duplicates and create 22 unnecessary edits.

Root/entry adapters already load conventions. This establishes visibility of the semantic owner, but not reliable recall at a later commit checkpoint. The distinction is:

```text
conventions.md       = semantic owner
workflow action      = point-of-use reminder
AGENTS/CLAUDE/rules  = always-loaded path to owner
Codex skills         = routers to owner + canonical workflow
.agent/.claude copy  = derived executable copy of a canonical workflow
```

### G4: Disposition of the current six-file implementation

Commit `389168a` changed exactly six files (15 insertions, 5 deletions).

| Current file | Preserve | Insufficient | Extraneous |
|--------------|----------|--------------|------------|
| `.tfw/conventions.md` | Preserve one normative owner, one grammar sentence, and one example | `scope` normalization and role derivation still need exact terminology challenge | No runtime or duplicated workflow body was added |
| `.tfw/glossary.md` | Preserve the concise definition and link | Must remain explicit that the prefix is subject text, not author/committer or authentication | Not an action consumer, but useful as the terminology index |
| `.tfw/workflows/handoff.md` | Preserve the corrected ONB cue and push boundary | Covers only ONB, not incremental implementation or final RF/evidence traces, and not other roles | None |
| `.agent/workflows/tfw-handoff.md` | Preserve the same surgical Step 4 change | Inherits handoff's partial coverage | Not an independent semantic consumer; count it only as a derived installed copy |
| `.claude/commands/tfw-handoff.md` | Preserve the same surgical Step 4 change | Inherits handoff's partial coverage | Not an independent semantic consumer; count it only as a derived installed copy |
| `RELEASE.md` | Preserve the current project release example and explicit push approval | Does not cover the portable canonical release workflow or other Coordinator workflows | Project-specific rather than canonical, but it is an active point of use, so not removable as “extra” |

No file in the six-file diff is runtime overreach. The error is incompleteness and flat counting: three handoff paths are one canonical action plus two derived copies, while Researcher, Reviewer, most Coordinator workflows, and the Codex install action remain uncued.

### G5: Minimum official Git terminology

Only the official Git manuals were consulted:

- [`git-commit`](https://git-scm.com/docs/git-commit) defines a commit as recording the staged/indexed changes in a new commit with a log message. TFW Commit Attribution occupies the commit subject/log-message text.
- The same manual's **Commit Information** section defines separate author and committer name/email/date inputs and explicitly states that those names do not authenticate anyone; authentication uses credentials separately.
- [`git`](https://git-scm.com/docs/git) lists `GIT_AUTHOR_*` and `GIT_COMMITTER_*` as distinct commit-object identity inputs.

Exact boundary:

| Term | Meaning for TFW-50 | Explicitly not |
|------|--------------------|----------------|
| Commit Attribution | Declared structured context in the first line of an AI-authored Git log message | Git author/committer metadata, a signature, credential, or authenticated actor claim |
| `agent` | Stable lowercase product/tool name of the acting AI from explicit session context (`codex`, `claude`) | Person, model version, account, Git author, Git committer, or hosting-service actor |
| `task` | Canonical TFW task ID; `project` only when no task exists | Branch, ticket URL, or free-form title |
| `scope` / work slice | One normalized lowercase label for the explicit current work slice, such as `task`, `phase-a`, `iter1`, `docs`, `knowledge`, `release`, `init`, `update`, or `config` | Filesystem path, hidden inference, or second task identifier |
| `role` | Lowercase TFW owner of the current workflow: `coordinator`, `researcher`, `executor`, or `reviewer` | Git role, maintainer account, model persona, or generic actor |
| `summary` | Short imperative remainder of the commit subject after one space | Full body, numeric-length protocol, or machine-validated trailer |

Local history demonstrates the separation: TFW-50 commits have Git author and committer `Sanzhar`, while their subjects declare `codex` as the acting agent. The prefix adds searchable context without replacing or authenticating Git metadata.

### G6: Gaps carried into Extract

1. `role` cannot be defined only as “inline active Role Lock”: `docs.md` says “Coordinator / Reviewer,” `release.md` says “Coordinator / Maintainer,” and some coordinator workflows use a `Role:` label rather than a lock. Conventions §15 supplies the canonical four-role owner table.
2. The existing `scope` examples omit real current values (`iter1`, `research`, `config`, `resume`, review stages). A normalized work-slice definition is more complete than a closed list.
3. “Cue only where the literal words `git commit` already appear” is not complete: it would still omit plan, research, review, knowledge, init, update, and config despite their writes and actual role history.
4. “Cue in every role workflow” is also ambiguous: four headline role workflows do not cover Coordinator-owned docs/knowledge/release/init/update/config, while cueing resume separately may duplicate plan's delegated action.
5. The current release cue and Codex install instruction are genuine project/adapter points of use, not new semantic owners.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Exhaustive grouped consumer inventory; all-role/workflow matrix; actual all-role history; six-file disposition; minimal official Git terminology | Build and score the three required configurations; determine exact cue checkpoints and a provisional include/exclude inventory; challenge the preferred configuration against omissions and copy drift |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?

Stage complete: YES
→ User decision: Pending Coordinator checkpoint approval
