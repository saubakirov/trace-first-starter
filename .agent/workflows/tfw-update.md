---
description: TFW Update — upgrade project's .tfw/ from upstream starter
---

# TFW Update — Framework Upgrade Workflow

> **Role:** Coordinator
> **Trigger:** Manually, when a new TFW version is available upstream
> **Source:** `tfw.upstream` in `.tfw/project_config.yaml`

## Step −1: follow the target's workflow, not this file

As soon as the payload is pinned (Step 0), open `.tfw/.upstream/.tfw/workflows/update.md` and
follow **it** from Step 1 on. The installed copy is what the update replaces; once, an installed
1.x workflow drove a major update by a minor procedure.

## Step 0: pin the source from the tag the operator names

Resolve `tfw.upstream` to a local Git checkout (clone a URL into `.tfw/.upstream-source/`; use a
local path as given). The operator names the target — a tag, or a commit when the owner
deliberately takes an untagged payload and says so in the checklist. Derive everything from it,
never from the source's `HEAD`: on a live source `HEAD` has moved past its release.

```bash
target_ref=v{target}                                              # named by the operator
source_head=$(git -C {source} rev-parse --verify "$target_ref^{commit}")
target=$(git -C {source} show "$source_head:.tfw/VERSION")
test "$target_ref" = "v$target"
```

If the tag is missing or `VERSION` at that commit disagrees with its name, stop: the tag must
identify the payload. For a local source,
`git -C {source} status --porcelain -- .tfw/` must print nothing; a dirty `tasks/` is irrelevant.
Record `target_ref`, `source_head`, target and source path in the update checklist.

Materialize the pinned payload into `.tfw/.upstream/` with `git -C {source} archive "$source_head"`;
never copy the live working tree. In CL mode, present the resolved command.

## Step 1: compare versions

Read the project's `tfw.version` and `.tfw/.upstream/.tfw/VERSION`. If equal, stop. Otherwise
list every intervening CHANGELOG entry; each entry's updating section names the earlier sections
a receiver on an older tag must also perform.

## Step 2: route major migrations

If the target crosses a major version, read and follow `.tfw/.upstream/.tfw/migrations/{major}.md`
before continuing. A major release without that guide is incomplete.

## Step 3: 🛑 ask the owner, then classify

**Before the first durable project write**, stop and ask exactly three questions. In AG mode
send the three as one message, continue through the read-only steps, and stop at the first write
until they are answered.

1. **Who is acting** — the handle for `team/{handle}.md` and `on_behalf_of`. Asked, never
   inferred from `git config user.name`, an OS username or the upstream's profiles
   (conventions §4).
2. **Where new tasks are created** — `tfw.task_containers`: `[tasks]` keeps one container;
   `[workspace, tasks]` creates in the first and resolves both.
3. **How the project verifies** — `build.*`, re-read because a preserved command may name a
   path the release removed.

Record the answers in the checklist. If `team/` is absent, create it with `team/{handle}.md`
from the profile template — one profile per person, never one per agent session; several
profiles need the per-machine binding the bindings template describes.

Then classify every local payload file against the version the project **installed**
(`tfw.installed_from` when it names a reachable tag; otherwise state the fallback baseline and
its uncertainty). A difference from the target is not a customization: text matching the
installed baseline, or merely older, is **provenance drift** and is overwritten; only a
divergence from the baseline is **customization** and is merged.

- **Project state, never overwrite:** `.tfw/knowledge_state.yaml`, `knowledge/`,
  `KNOWLEDGE.md`, and any debt registry the project still keeps — 2.1.0 withdraws the obligation to
  maintain one and forbids nothing.
- **Release-identical or provenance drift:** overwrite from the pinned payload.
- **Customized:** merge the measured local delta into the target.
- **Removed or structurally changed:** follow CHANGELOG and the migration guide.

`.tfw/project_config.yaml` is part project and part framework: preserve keys marked
`← PROJECT` — `build.*`, `scope_budgets`, the answers above — and update keys marked
`← FRAMEWORK`. Delete retired keys `initial_seq`, `id_max_retries` and `review.default_mode`;
`--check project` names them.

## Step 4: produce the checklist

One checkbox per source/target file, grouped by the four classifications, plus every file named
under CHANGELOG `Removed` or `Changed` and every template structural change.

## Step 5: execute the checklist — copy with declared exclusions

The copy **never overwrites** `.tfw/project_config.yaml` (merged key by key, Step 3) or
`.tfw/knowledge_state.yaml` (never touched). The step that copies **prints what it skipped**:

```bash
src=.tfw/.upstream/.tfw
find "$src" -type f | while read -r f; do rel=${f#"$src"/}
  case "$rel" in project_config.yaml|knowledge_state.yaml) echo "skipped: .tfw/$rel (project-owned)" ;;
  *) mkdir -p ".tfw/$(dirname "$rel")" && cp "$f" ".tfw/$rel" ;; esac; done
```

A copy that reports nothing skipped on a project that has both files is a failed step. Per
checklist item: apply, verify that measured customization survived, tick it. Then recheck the
source — `test "$(git -C {source} rev-parse --verify "$target_ref^{commit}")" = "$source_head"`.
If it differs, stop before adapter sync; the copied bytes stay pinned and inspectable.

## Step 6: re-sync only installed adapters

Do not create directories for tools the project does not use. For each installed or
owner-selected adapter, re-copy only TFW-managed entries. A **copy** is verified by `cmp`; a
**block** on the region between its markers, under the marker rule in `conventions.md` §9:
markers present — replace between them; file absent — create it from the template; no
markers — report and leave it; the operator inserts the block once.

| Adapter | Source | Target | Kind |
|---|---|---|---|
| Claude commands | `.tfw/workflows/*.md` | `.claude/commands/tfw-*.md` | copy |
| Antigravity workflows | `.tfw/workflows/*.md` | `.agent/workflows/tfw-*.md` | copy |
| Claude rules | `.tfw/adapters/claude-code/CLAUDE.md.template` | `TFW:CLAUDE` block in `CLAUDE.md` | block |
| Antigravity rules | `.tfw/adapters/antigravity/` | `.agent/rules/` | copy |
| Cursor | `.tfw/adapters/cursor/` | `.cursor/rules/` | copy |
| Codex skills | `.tfw/adapters/codex/skills/tfw-*/SKILL.md` | `.agents/skills/tfw-*/SKILL.md` | copy |
| Codex routing | `.tfw/adapters/codex/AGENTS.md.template` | `TFW:CODEX` block in `AGENTS.md` | block |

Never touch adjacent project-owned commands or rules.

Build an allowlist for each vocabulary item the CHANGELOG retires: **text whose purpose is to
retire the term** — a deletion instruction, a migration step, a changelog line, their
byte-identical copies — may name it; a live use never is. Search the payload and installed
adapter layers and require **zero hits outside that allowlist**.

## Step 7: record version and provenance

Set `tfw.version` to the target and `tfw.installed_from` to `{upstream}@{verified-tag}`, where
`{upstream}` is `tfw.upstream` as configured — a URL or a symbolic name, **never a machine-local
path**. For a local checkout, name it symbolically and record the path in the checklist.
`--check project` reports a path here and rewrites nothing.

## Step 8: verify

Run `python .tfw/scripts/gen_index.py --check project`, then verify adapter copies and blocks,
the retired-vocabulary allowlist, literal `/tfw-*` routing, preserved local conventions and
every configured build/lint/test command. The check writes nothing and names what it skipped.

## Step 8a: brief the owner

Write the briefing from `.tfw/templates/briefing.md` in `content_language`: four blocks from the
intervening entries' `Added`, `Changed`, `Fixed` and `Removed` sections — *what is now
possible*, *what you now do differently*, *what stopped breaking*, *what no longer has to be
done*. Each block is bound to the entries' own bullets; an absent section reads *nothing in this
release*; no free text. The briefing is the update's **last message**, and the checklist records
that it was delivered.

## Step 9: cleanup

Remove `.tfw/.upstream/` and a temporary `.tfw/.upstream-source/` if desired.
