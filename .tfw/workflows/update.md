---
description: TFW Update — upgrade project's .tfw/ from upstream starter
---

# TFW Update — Framework Upgrade Workflow

> **Role:** Coordinator
> **Trigger:** Manually, when a new TFW version is available upstream
> **Source:** `tfw.upstream` in `.tfw/project_config.yaml`

## Before Step 0: pin the source

Resolve `tfw.upstream` to a local Git checkout (clone a URL into `.tfw/.upstream-source/`;
use a local path as given). Before reading its payload, record:

```bash
source_head=$(git -C {source} rev-parse HEAD)
target=$(git -C {source} show "$source_head:.tfw/VERSION")
tag_commit=$(git -C {source} rev-parse --verify "refs/tags/v${target}^{commit}")
test "$tag_commit" = "$source_head"
```

If the tag is missing or does not point at the pinned commit, stop: `VERSION` is not trusted
until the corresponding tag exists and identifies the payload. For a local source,
`git -C {source} status --porcelain -- .tfw/` must also print nothing. A dirty `tasks/` is
irrelevant. Record `source_head`, target, tag commit and source path in the update checklist.

## Step 0: materialize the pinned payload

Create `.tfw/.upstream/` from `git -C {source} archive "$source_head"`; do not copy the live
working tree. In CL mode, present the resolved command.

## Step 1: compare versions

Read the project's `tfw.version` and the pinned `.tfw/.upstream/.tfw/VERSION`. If equal, stop.
Otherwise list every intervening entry from the pinned CHANGELOG.

## Step 2: route major migrations

If the target crosses a major version, read and follow
`.tfw/.upstream/.tfw/migrations/{major}.md` before continuing. A major release without that
guide is incomplete.

## Step 3: classify every local payload file

Compare the project with the version it actually installed, not automatically with
`v{current}`. When `tfw.installed_from` names a reachable tag or commit, use that as the
baseline. Otherwise state the fallback baseline and its uncertainty.

A difference from the target is not by itself a customization. If local wording matches the
installed baseline, or is simply older than the target, it is **provenance drift** and is
overwritten. Only a local divergence from the installed baseline is **customization** and
needs a merge. This prevents an update from reporting upstream-line drift as hand edits.

Classify in this order:

- **Project state, never overwrite:** `.tfw/knowledge_state.yaml`, `knowledge/`,
  `KNOWLEDGE.md`, `TECH_DEBT.md`.
- **Release-identical or provenance drift:** overwrite from the pinned payload.
- **Customized:** merge the measured local delta into the target.
- **Removed or structurally changed:** follow CHANGELOG and the migration guide.

`.tfw/project_config.yaml` is part project and part framework. Preserve keys marked
`← PROJECT`, including `build.*` and `scope_budgets`; update keys marked `← FRAMEWORK`.
Re-read preserved build commands because they may name a path the release removed.

For 2.0.0, choose `tfw.task_containers` deliberately: `[tasks]` retains one container;
`[workspace, tasks]` creates in the first and resolves both. Delete retired keys
`initial_seq`, `id_max_retries`, and `review.default_mode`; `--check project` names them.

If `team/` is absent, create it together with `team/{handle}.md` from the profile template
before the update's first durable project write. One profile represents one person. With
multiple profiles, create the per-machine binding described by the bindings template.

## Step 4: produce the checklist

Write one checkbox per source/target file, grouped by the four classifications. Include every
file named under CHANGELOG `Removed` or `Changed` and every template structural change.

## Step 5: execute the checklist

Per item: apply, verify that measured project customization survived, and tick it. Then repeat
the source checks:

```bash
test "$(git -C {source} rev-parse HEAD)" = "$source_head"
test "$(git -C {source} rev-parse --verify "refs/tags/v${target}^{commit}")" = "$source_head"
```

If either differs, stop before adapter sync. The copied bytes remain pinned and inspectable;
do not mix them with the moved source. Reconcile or restart from a newly approved pin.

## Step 6: re-sync only installed adapters

The payload may contain adapter sources for tools the project does not use. Do not create
their target directories. For each adapter already installed or explicitly selected by the
owner, re-copy only TFW-managed entries:

| Adapter | Source | Target |
|---|---|---|
| Claude commands | `.tfw/workflows/*.md` | `.claude/commands/tfw-*.md` |
| Antigravity workflows | `.tfw/workflows/*.md` | `.agent/workflows/tfw-*.md` |
| Claude rules | `.tfw/adapters/claude-code/` | managed `CLAUDE.md` content |
| Antigravity rules | `.tfw/adapters/antigravity/` | `.agent/rules/` |
| Cursor | `.tfw/adapters/cursor/` | `.cursor/rules/` |
| Codex skills | `.tfw/adapters/codex/skills/tfw-*/SKILL.md` | `.agents/skills/tfw-*/SKILL.md` |
| Codex routing | `.tfw/adapters/codex/AGENTS.md.template` | marker-bounded root `AGENTS.md` block |

Never touch adjacent project-owned commands or rules. For Codex, follow its adapter README.

Build an explicit allowlist for each vocabulary item retired by CHANGELOG: canonical migration
or changelog text and byte-identical copies may name it in order to retire it. Search the
payload and installed adapter layers and require **zero hits outside that allowlist**. This is
reachable; an unconditional “nothing may print” is not, because retirement instructions must
name the term they retire.

## Step 7: record version and provenance

Set `tfw.version` to the target and `tfw.installed_from` to
`{resolved-source}@{verified-tag-or-commit}`. `tfw.upstream` says where to fetch; this field says
which verified bytes the project runs.

## Step 8: verify

Run `python .tfw/scripts/gen_index.py --check project`, then verify installed adapter copies,
the retired-vocabulary allowlist, literal `/tfw-*` routing, preserved local conventions, and
all configured build/lint/test commands. The project check writes nothing and reports what it
does not check.

## Step 9: cleanup

Remove `.tfw/.upstream/` and a temporary `.tfw/.upstream-source/` if desired.
