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

**A local source must be clean at the tag you are taking** — a dirty `.tfw/` there means the
payload is not the one that was released. A dirty `tasks/` is irrelevant.

```bash
rm -rf .tfw/.upstream && mkdir -p .tfw/.upstream          # PowerShell: Remove-Item -Recurse -Force
# local tree:
git -C {tfw.upstream} status --porcelain -- .tfw/         # must print nothing
git -C {tfw.upstream} archive v{target} | tar -x -C .tfw/.upstream
# URL:
git clone --depth 1 {tfw.upstream} .tfw/.upstream
```

> In CL mode, present the resolved command. `.tfw/.upstream/` is gitignored.

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
procedure. Read it now, follow it, and come back for Step 4.** A major release without a
migration guide is incomplete.

## Step 3a: Diff every local `.tfw/` file against the pristine previous tag

Find out which local files were actually customized. Measure, do not guess.

```bash
# In the SOURCE tree, not yours: the tag belongs to the framework, not to your project.
# The first external consumer had no TFW tags at all and still needed this check.
for f in $(git -C {source} ls-tree -r --name-only v{current} -- .tfw/); do
  git -C {source} show v{current}:"$f" | diff -q - "$f" >/dev/null || echo "CUSTOMIZED $f"
done
```

What it does *not* print is byte-identical to the release: overwrite it. On two real external
updates this turned every declared manual merge into zero but the config.

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

`.tfw/project_config.yaml` always needs attention, being structurally part-yours. **It marks
its own keys** — every line carries `← PROJECT` (preserve) or `← FRAMEWORK` (update), so merge
by the markers in the file rather than by a list here that can disagree with them.

**Preserved does not mean correct.** `build.*` is yours and never overwritten, so a release
that moved a tool leaves your command naming a path that is gone. Re-read it by hand; Step 8's
`--check project` reports it.

### Two keys that are decisions, not values to preserve (🔴):

- **`tfw.task_containers` — a decision, and it does not exist before 2.0.0.** There is
  nothing to preserve; you are choosing it now, and it decides where new tasks are created
  and whether existing paths still resolve. Two real options:

  | Choice | When |
  |---|---|
  | `[tasks]` — one container | Your existing directory keeps its name and its tasks. The simple case |
  | `[workspace, tasks]` — new container first, old one second | You want new tasks somewhere new **and** every existing path to keep resolving. Creation uses the first; resolution searches both |

  Choose deliberately. Left silent, it is set by whoever ran the update.

- **`initial_seq` — delete the key.** Retired at 2.0.0: identifiers come from the clock, so
  nothing reads a counter.

### Create `team/` if the project has none (🔴)

Copy `.tfw/templates/team/profile.md` to `team/{handle}.md` and fill the four keys —
**before the first durable write**, this update's own commit included. Create the directory
together with that profile, never empty: without a profile, no journal event has a valid
`on_behalf_of`.

One profile per **person** — not one per agent session; `team/` holds people.

**When a second profile appears, write the binding too**: copy `.tfw/templates/bindings.yaml`
to the per-machine path it documents. Seven workflows tell a session to read it once a project
declares more than one participant.

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
| **Claude Code commands** | `.tfw/workflows/*.md` | **`.claude/commands/tfw-*.md`** |
| Antigravity workflows | `.tfw/workflows/*.md` | `.agent/workflows/tfw-*.md` |
| Claude Code rules | `.tfw/adapters/claude-code/` | `CLAUDE.md` |
| Antigravity rules | `.tfw/adapters/antigravity/` | `.agent/rules/` |
| Cursor | `.tfw/adapters/cursor/` | `.cursor/rules/` |
| Codex skills | `.tfw/adapters/codex/skills/tfw-*/SKILL.md` | `.agents/skills/tfw-*/SKILL.md` |
| Codex routing | `.tfw/adapters/codex/AGENTS.md.template` managed block | Root `AGENTS.md` managed block |

Row 1 was missing until `2.0.0-dirty.3` and its absence reached two projects out of two: both
adapters are byte copies of the same workflows, only one was listed, and the unlisted one
rotted.

Only re-sync adapters the project uses. **Re-copy only the `tfw-*` entries the payload
provides and touch nothing else** — a project's own commands (`kz-release.md`) sit beside them
and are not ours.

For Codex, follow `.tfw/adapters/codex/README.md` Install or Repair. Two bounds it states
and this step repeats: copy only the `tfw-*` directories that exist under
`.tfw/adapters/codex/skills/`, and touch only the marker-bounded block in root `AGENTS.md`.

### Then check the layer you just wrote

```bash
# One line per term the CHANGELOG's `### Changed` section retires. Nothing may print.
grep -rlF -e "<retired term>" .claude .agent .agents AGENTS.md CLAUDE.md
```

Zero, every time: a stale copy is a second set of instructions that no gate reads. The terms
are release-specific, so they are taken from the CHANGELOG rather than written here — an
instruction that inlines the term it searches for becomes a hit on itself the moment it is
copied into the layer being checked.

## Step 7: Update Version Marker

Update `tfw.version` in `.tfw/project_config.yaml` to the target version, and record where
the payload actually came from beside it:

```yaml
tfw:
  version: "2.0.0-dirty.3"
  installed_from: "D:/projects/research/steps-framework@v2.0.0-dirty.3"
```

`tfw.upstream` is where updates are fetched from; `installed_from` is what this project
actually runs. A local unpushed tag is unreachable from a remote URL, so without this the next
update clones the remote, finds an older payload and reports all is well.

## Step 8: Verify

**Ask the project itself first:**

```bash
python .tfw/scripts/gen_index.py --check project
```

One command for *is this project consistent with this release*: payload, `team/`, containers,
retired keys, version marker, carrier validity. It reports and exits. Its output names what it
did **not** check — and this list is that:

- Adapter copies match their sources — **`.claude/commands/tfw-*` and
  `.agent/workflows/tfw-*` both**, plus `.agents/skills/tfw-*` and the single marker-bounded
  TFW block in root `AGENTS.md`
- the adapter-layer grep above prints nothing, for every term the CHANGELOG retires
- `installed_from` names the source and tag this payload actually came from
- A literal `/tfw-*` routes to the matching local workflow (`$tfw-*` and `/skills` are
  fallbacks, not required syntax)
- Your own additions survived in `conventions.md` and `glossary.md`
- Build, lint and test still pass

## Step 9: Cleanup

`rm -rf .tfw/.upstream` (PowerShell: `Remove-Item -Recurse -Force`). Optional — it is
gitignored, so leaving it is harmless.
