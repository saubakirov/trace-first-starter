---
description: TFW Update — upgrade project's .tfw/ from upstream starter
---

# TFW Update — Framework Upgrade Workflow

> **Role:** Coordinator
> **Trigger:** Manually, when a new TFW version is available upstream
> **Source:** Upstream starter repository configured in `tfw.upstream`

## Prerequisites

1. Read project's `.tfw/project_config.yaml` → `tfw.version` (current) and `tfw.upstream` (source URL)
2. Fetch upstream into `.tfw/.upstream/` (see Step 0)
3. Read `.tfw/.upstream/.tfw/VERSION` → target version
4. Read `.tfw/.upstream/.tfw/CHANGELOG.md` → changes since current version

## Step 0: Fetch Upstream

Read `tfw.upstream` from `.tfw/project_config.yaml` — a clonable URL, **or a path to a local
working tree**. Both are valid sources.

**A local source must be clean at the tag you are taking.** Run `git status` in it and
confirm `.tfw/` carries no uncommitted change — a dirty `tasks/` is irrelevant, a dirty
`.tfw/` means the payload you are about to copy is not the payload that was released.

```bash
# local working tree as the source
git -C {tfw.upstream} status --porcelain -- .tfw/     # must print nothing
git -C {tfw.upstream} archive v{target} | tar -x -C .tfw/.upstream
```

For a URL source, clear the staging directory and clone fresh:

```bash
rm -rf .tfw/.upstream && git clone --depth 1 {tfw.upstream} .tfw/.upstream
# PowerShell: Remove-Item -Recurse -Force .tfw/.upstream ; git clone --depth 1 ...
```

> In CL mode, present the resolved command for the user to run.
> `.tfw/.upstream/` is gitignored.

## Step 1: Compare Versions

```
Current: {project tfw.version}
Target:  {.tfw/.upstream/.tfw/VERSION}
```

If current == target → already up to date. Stop.

## Step 2: Review CHANGELOG

List every change between current and target in `.tfw/.upstream/.tfw/CHANGELOG.md`.

## Step 3: Route a major update to its migration guide

**If the target crosses a major version, `.tfw/.upstream/.tfw/migrations/{major}.md` is the
procedure. Read it now, follow it instead of improvising, and come back here for Step 4.** A
major release without a migration guide is incomplete — the guide, not CHANGELOG prose, is
where the ordering constraints live.

## Step 3a: Diff every local `.tfw/` file against the pristine previous tag

Before merging anything, find out which local files were actually customized. Do not guess
which files differ — measure.

```bash
# In the SOURCE tree, not yours: the tag belongs to the framework, not to your project.
# The first external consumer had no TFW tags at all and still needed this check.
for f in $(git -C {source} ls-tree -r --name-only v{current} -- .tfw/); do
  git -C {source} show v{current}:"$f" | diff -q - "$f" >/dev/null || echo "CUSTOMIZED $f"
done
```

What it does *not* print is byte-identical to the release: overwrite it. On the first real
external update this turned three declared manual merges into **zero**, `conventions.md`
with its 212 changed lines included.

## Step 3b: Categorize Changes

Four categories, in the order that decides them: ⚫ project state, never overwritten
whatever Step 3a said · 🟢 identical to the release, overwrite · 🟡 customized, real diff ·
🔴 a decision or a break, read it.

### ⚫ Project state — NEVER overwrite:
- `.tfw/knowledge_state.yaml` — project knowledge consolidation tracking
- `knowledge/` — project-specific verified facts (NOT from upstream)
- `KNOWLEDGE.md` — project knowledge index (NOT from upstream)
- `TECH_DEBT.md` — project tech debt (NOT from upstream)

### 🟢 versus 🟡 is answered by Step 3a, not by a list

A list of files that *may* differ is a guess where Step 3a is a measurement.

`.tfw/project_config.yaml` always needs attention, being structurally part-yours:
  **Project sections** (preserve): `project.*`, `tfw.task_prefix`,
  `tfw.content_language`, `build.*`, `stack.*`, `tfw.user_preferences`
  **Framework sections** (update): `tfw.version`, `tfw.templates`, `tfw.workflows`,
  `tfw.statuses`, `tfw.scope_budgets`, `tfw.research`, `tfw.review`, `tfw.knowledge`
  **Preserved does not mean correct.** `build.*` is yours and is never overwritten — so if
  this release moved a tool, your command still names the old path. Re-read it by hand, and
  let Step 8's `--check project` confirm it.

### Two keys that are decisions, not values to preserve (🔴):

- **`tfw.task_containers` — a decision, and it does not exist before 2.0.0.** There is
  nothing to preserve; you are choosing it now, and it decides where new tasks are created
  and whether existing paths still resolve. Two real options:

  | Choice | When |
  |---|---|
  | `[tasks]` — one container | Your existing directory keeps its name and its tasks. The simple case |
  | `[workspace, tasks]` — new container first, old one second | You want new tasks somewhere new **and** every existing path to keep resolving. Creation uses the first; resolution searches both |

  Choose deliberately and be able to say why. Left silent, it is set by whoever ran the
  update.

- **`initial_seq` — delete the key.** Retired at 2.0.0: identifiers come from the clock, so
  nothing reads a counter.

### Create `team/` if the project has none (🔴)

Copy `.tfw/templates/team/profile.md` to `team/{handle}.md` and fill the four keys —
**before the first durable write**, this update's own commit included. Create the directory
together with that profile, never empty: without a profile, no journal event has a valid
`actor` or `on_behalf_of`.

### Files to check for breaking changes (🔴):
- Any file listed under `### Removed` or `### Changed` in CHANGELOG
- Template structural changes (new required sections, renamed fields)

## Step 4: Generate Update Checklist

One checkbox per file, grouped by the three categories, naming the source and the target.
Step 3a decides which group each file lands in.

## Step 5: Execute Update

Per item: apply, confirm no project customization was lost, tick it off.

## Step 6: Re-sync Adapters

Update tool-specific adapter copies from `.tfw/`:

| Adapter | Source | Target |
|---------|--------|--------|
| Antigravity workflows | `.tfw/workflows/*.md` | `.agent/workflows/tfw-*.md` |
| Antigravity rules | `.tfw/adapters/antigravity/` | `.agent/rules/` |
| Claude Code | `.tfw/adapters/claude-code/` | `CLAUDE.md` |
| Cursor | `.tfw/adapters/cursor/` | `.cursor/rules/` |
| Codex skills | `.tfw/adapters/codex/skills/tfw-*/SKILL.md` | `.agents/skills/tfw-*/SKILL.md` |
| Codex routing | `.tfw/adapters/codex/AGENTS.md.template` managed block | Root `AGENTS.md` managed block |

Only re-sync adapters that the project uses.

For Codex, follow `.tfw/adapters/codex/README.md` Install or Repair. Two bounds it states
and this step repeats: copy only the `tfw-*` directories that exist under
`.tfw/adapters/codex/skills/`, and touch only the marker-bounded block in root `AGENTS.md`.

## Step 7: Update Version Marker

Update `tfw.version` in `.tfw/project_config.yaml` to the target version.

## Step 8: Verify

**Ask the project itself first:**

```bash
python .tfw/scripts/gen_index.py --check project
```

One command for *is this project consistent with this release* — the payload, `team/`, the
container configuration, retired keys, version marker, carrier validity. It reports and
exits: it repairs nothing, writes nothing, and is authority over nothing. Its output names
what it did **not** check, and this list is that:

- Adapter copies match their sources, including `.agents/skills/tfw-*` and the single
  marker-bounded TFW block in root `AGENTS.md`
- A literal `/tfw-*` routes to the matching local workflow (`$tfw-*` and `/skills` are
  fallbacks, not required syntax)
- Your own additions survived in `conventions.md` and `glossary.md`
- Build, lint and test still pass

## Step 9: Cleanup

`rm -rf .tfw/.upstream` (PowerShell: `Remove-Item -Recurse -Force`). Optional — it is
gitignored, so leaving it is harmless.
