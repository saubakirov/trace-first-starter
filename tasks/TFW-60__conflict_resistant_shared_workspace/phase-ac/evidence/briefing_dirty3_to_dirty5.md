# What changed for you — TFW 2.0.0-dirty.3 → 2.0.0-dirty.5

> **Project**: steps-framework (the framework's own repository, as its own consumer) · **Date**: 2026-08-30 · **Written in**: `en` (`tfw.content_language`)
> **Derived from**: the `2.0.0-dirty.4` CHANGELOG entry (released 2026-08-30) and the `2.0.0-dirty.5` entry **as this phase's RF §1 proposes it** — the `.5` entry itself is written by `/tfw-release` after review, so its bullets below are re-derived from the cut entry at that point. Every bullet is bound to a CHANGELOG bullet; nothing here has no bullet behind it.
> **Rendered from**: `.tfw/templates/briefing.md`

## What is now possible

<!-- `Added` — .4 carries no Added section; .5 (proposed) -->
- *`.4`: nothing in this release.*
- `.5`: when a `/tfw-update` runs, you are asked three things before it writes anything to your project — who is acting, where new tasks go, how the project verifies — and it ends with a message like this one, in your project's language.
- `.5`: a migration manifest now names every phase directory of every task it touched and says plainly that phase state is yours to write.
- `.5`: `--check tasks` tells you which phase directories have no state file, and whether that matters — a failure only when the task is live.
- `.5`: `--check project` tells you when `installed_from` carries a path from one machine that means nothing on another.

## What you now do differently

<!-- `Changed` — one bullet per item -->
- `.4`: a new task's directory is `PREFIX_YYYYMMDD-HHMMSS_ABBR` — the prefix from your config, the clock read once, and an abbreviation you approve during planning. Existing tasks keep their names forever; only new ones use it.
- `.5`: that abbreviation is the initials of the task's full title — *Conflict Resistant Shared Workspace* → `CRSW` — proposed to you together with the title, approved together, both in the HL header. No more opaque codes.
- `.5`: an update pins the source from the **tag you name**, not from wherever the source repository happens to stand. A source that has moved on past its release is still a valid source.
- `.5`: a `/tfw-update` opens the **target's** `update.md` and follows it — the installed copy is what the update replaces.
- `.5`: the Claude Code rules in `CLAUDE.md` live between `<!-- TFW:CLAUDE:START/END -->` markers, like the Codex block in `AGENTS.md`. A file without markers is reported, never edited; you insert the block once.

## What stopped breaking

<!-- `Fixed` — one bullet per item -->
- `.4`: a task identifier is read whole or refused — `HD-30b` is no longer read as `HD-30`. Nothing gets state it was not given.
- `.4`: two board rows or two directories that resolve to one identifier stop the migration before it writes.
- `.4`: every guarantee the migration manifest prints is computed from the tree in front of it; the literal "Unaccounted: 0" is gone.
- `.4`: migrated prose keeps identifier underscores intact.
- `.4`: you can run the framework's tests in your project without inheriting checks about the framework's own repository (`-k "not repository"`).
- `.4`: `/tfw-update` verifies the source tag before trusting its version, and again before installing; provenance drift is told apart from your own customizations.
- `.4`: documentation links resolve the new identifier grammar too.
- `.4`: `via` on a journal event is free-form tool text; there is no provider list to be wrong about.
- `.4`: Phase AA's corrective pass has its RF — no gap in the trace.
- `.5`: a board status cell like `✅ DONE (A/V/B/C) · 🔄 Phase D` is no longer read as `DONE` by its first token: it is refused, carried verbatim, and your live task gets a state file instead of silence.
- `.5`: the payload copy can no longer overwrite your `project_config.yaml` or `knowledge_state.yaml`; the copy step prints what it skipped.
- `.5`: the retired-vocabulary gate is literally green on a correct project — text whose purpose is to retire a term is allowed to name it.
- `.5`: a receiver that skipped a tag finds its path: each release's updating section points at the earlier sections it must also perform.
- `.5`: the Antigravity and Cursor rule templates no longer ask for a version substitution nobody remembers.
- `.5`: the event, profile and status templates say what the conventions say — `via` free-form, one profile per person with roles in `team/README.md`, a phase paragraph for phase state.

## What no longer has to be done

<!-- `Removed` — .4 carries no Removed section; .5 (proposed) -->
- *`.4`: nothing in this release.*
- `.5`: you no longer hand-merge `update.md` against your own `CLAUDE.md`, reading both — the block between the markers is compared and replaced mechanically.
- `.5`: you no longer reconcile a pin that "cannot pass" on a live source by hand — the tag you name is the pin.
- `.5`: you no longer back up `project_config.yaml` and `knowledge_state.yaml` "just in case" before copying the payload.

---

*Rendered 2026-08-30 for this repository's `.3 → .5` delta. When `/tfw-release` cuts the `.5` entry, the `.5` bullets are re-derived from it; the `.4` bullets are final.*
