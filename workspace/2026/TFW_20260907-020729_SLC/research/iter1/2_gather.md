# Gather — What do we know?
> **Mindset:** Scout. Separate observed behavior from design choices.
> **Test:** Every proposed simplification has an identified reader and preservation consequence.
> Parent: [HL SLC](../../HL-TFW_20260907-020729_SLC.md)
> Goal: One workspace default with compatible historical access.

## Dimensions

| Dimension | A | B | C |
|---|---|---|---|
| Representation | Active list plus optional historical-path list | Replace path strings with per-container role objects | Retain mixed list plus an exclusion list |
| Digest treatment | Remove only verified historical IDs during migration | Retain old IDs and filter them through historical lookup on each gate | Add a second persisted historical digest map |
| Recovery | Reuse update preparation, preservation attachments, present-state re-entry and receipt | Introduce a persistent migration journal/lock/controller | Require an external Git transaction or manual restore |

All alternatives are observations of possible designs, not recommendations. The exact optional field name is undecided. Adoption is governed by frozen HL §3 rather than another dimension: fresh, preserved single/custom, mixed empty, established history, unresolved/live.

## Findings

### G1: Current scope has multiple jobs
At source `49ddad02f97dfb46919bdd19292902b9082d696f`, `tools/tfw_state.py:task_containers` feeds ordinary discovery and the optional Knowledge Gate oracle. Its walker already accepts an explicit container list. `docs/scripts/gen_docs.py` uses that same default for source globs, task output mapping, generated landings and exact identifier resolution. The compiler's `tasks/` URL prefix is separate from source location. Changing the default alone cannot preserve every reader.

### G2: Fresh installation already has a clean route
README new/existing-project prompts clone an upstream source into a temporary location and copy `.tfw/` into the receiving project. Quickstart and Full init Mini-Setup derive receiver config/state from templates and create the first configured container. The shipped template and helper fallback still say `[tasks]`; the owner's separate root edit says `[workspace]`. Copying the upstream project's own config or task corpus is not the supported clean installation. A full framework checkout contains genuine history and must not be automatically wiped to make it look new.

### G3: The helpdesk report is independently corroborated
Read-only receiver: `D:/projects/research/helpdesk`. Commit `31baa3444cfe98b35bda03688b5b4eafdc2d43a4`, authored `2026-09-08T19:05:08+05:00`, narrows `[workspace, tasks]` to `[workspace]`. Both sides contain the same knowledge-state blob `3c0eb3d63a06fe394f00305834b7c4fbc1090bf6`. Thirty legacy task directories and thirty remembered IDs remain: HD-1 through HD-28, HD-30 and HD-31; HD-29 is absent. The retained config comment explicitly records the owner's 2026-09-03 historical-only decision, including no continuation. This is stronger evidence of disposition than the folder's age or a legacy ID.

### G4: Receipt and committed state disagree
The commit's `.tfw/update_receipts/UPDATE__20260908-184145__abdd.md` says the owner chose to preserve `[workspace, tasks]` and that it was preserved and verified. The committed config contradicts this. The receipt says no commit was made by that update attempt, so the available evidence does not identify when or by whom the later narrowing happened. Its pinned source is v3.1.0 at `a767b17072733dc856d4c73fa6a72277e1538ba5`; its template was still `[tasks]`, and the owner's uncommitted upstream edit was excluded by `git archive`. Do not attribute this failure to copying the workspace template. The receiver working config was already restored to the mixed list when inspected; this research did not repair it. The reported conditional 4/5 count remains unverified.

### G5: State preservation needs an explicit migration exception
Canonical `knowledge.md` compares all remembered whole IDs against current discovery; absence means indeterminate input. `update.md` preserves project state as payload, merges project config by ownership, supports prescribed version-addressed compatible migration, and re-observes interrupted/equal-version updates. These rules provide a route, but do not yet specify SLC's exact digest exception, write order or recovery evidence. “Connected group” alone is not a multi-file atomic-write mechanism.

### G6: External checks constrain interpretation
[YAML 1.2.2 §6.6](https://yaml.org/spec/1.2.2/#66-comments) treats comments as presentation information; a parser does not implement an archive policy from prose. Here the comment is evidence of an owner decision, which migration must express in machine-readable configuration. [Debian configuration policy §10.7.3](https://www.debian.org/doc/debian-policy/ch-files.html#configuration-files) is a useful external comparison for preserving local changes and repeatable upgrades; it does not govern TFW. Neither source proves native agent behavior.

## Checkpoint

| Found | Remaining |
|---|---|
| Three independent design dimensions; real receiver scope/state mismatch; clean init path; exact consumer roles | Compare all 27 configurations; establish interrupted-write behavior; quantify necessary change surfaces |

**Sufficiency:** external source used: YES; Briefing gap closed for Gather: YES; dimensions identified: YES. The configured 15-file soft read budget was exceeded for the bounded cross-repository receiver verification and consumer map; no broad historical task-body preload was used.

Stage complete: YES
Decision: close Gather and proceed to Extract under the owner's authorization to complete research; no new owner choice is required at this checkpoint.
