# PROPOSAL — Retire the task meta-workflow

> **Date**: 2026-09-02
> **Author**: Claude Code (Coordinator)
> **Status**: ⬜ TODO — proposal only. No HL, no TS. Entry point: **`/tfw-config`**, not `/tfw-plan`.
> **Origin**: owner ruling 2026-09-02, promoted from
> [`TFW_20260902-112841_RDP`](../TFW_20260902-112841_RDP/REVIEW__TFW_20260902-112841_RDP.md) §5 row 1

---

## The finding

`/tfw-task` has **two installed copies that differ from each other** and **no source** in
`.tfw/workflows/`. `cmp` reports them different at line 1; there is no `.tfw/workflows/task.md` for
either to be a copy of; `.agents/skills/` has no counterpart at all.

**Why it cannot self-correct.** Every drift instrument the project owns compares a copy against its
source. With no source, `update.md`'s re-sync and every `cmp` sweep are *structurally unable* to see
the divergence or repair it — so a project on the Codex adapter and one on Claude Code receive
different lifecycle instructions from the same command, and the gap widens with each release.

`conventions.md` §9 says an adapter installs *"whole copies or marker-bounded blocks, and nothing of a
third kind."* This is a third kind.

## The owner's ruling, 2026-09-02

> *«tfw-task надо удалить вообще, устаревшее, забыли про неё.»*

Deleted, not sourced. The command is obsolete.

## Measured footprint

Measured 2026-09-02, before the ruling was recorded. **2 deletions, 9 reference sites in 6 files.**

| Site | What is there |
|---|---|
| `.claude/commands/tfw-task.md` | **DELETE** — 1 625 bytes |
| `.agent/workflows/tfw-task.md` | **DELETE** — 1 430 bytes, differs from the above |
| `.tfw/workflows/config.md:123` | the *"not copied, and why"* table row |
| `.tfw/workflows/config.md:134` | `[ "$b" = "tfw-task" ] && continue` — the drift check **skips it by name** |
| `.claude/commands/tfw-config.md:123,134` | installed copy of both |
| `.agent/workflows/tfw-config.md:123,134` | installed copy of both |
| `.tfw/adapters/claude-code/README.md:16,86` | the file tree, and the command table |
| `.tfw/adapters/codex/README.md:51` | *"`/tfw-task` is intentionally absent"* — a decision that becomes odd once the command exists nowhere. Judgement call: history, or stale? |
| `CLAUDE.md:29` | the command table row, inside the `TFW:CLAUDE` marker block |

**Never edited:** `.tfw/CHANGELOG.md:1156` records the TFW-53/D sync that named `tfw-task` as
adapter-only. That is history.

## Why `/tfw-config` and not `/tfw-plan`

The work is a removal and a re-sync. `conventions.md` §15 grants `config.md`'s Coordinator exactly
`project_config.yaml`, workflow files, convention files and adapter copies — every file above. Opening
an HL, a TS, an ONB, an RF and a REVIEW to delete a forgotten command is the
*"maximum-documentation bureaucracy"* `NS3` names as a non-goal.

**What the run must not skip:** the drift check in `config.md` currently skips `tfw-task` **by name**.
Deleting the files without deleting that line leaves a check that silently excludes a file that no
longer exists — a dead exception, and the next person to read it learns the wrong rule.

## Definition of done, informally

The term `tfw-task` returns nothing outside `tasks/`, `workspace/` and the CHANGELOG's historical
entry; `config.md`'s drift check runs with no by-name exception; both adapter READMEs and `CLAUDE.md`'s
table no longer offer a command that does not exist; and the retirement is named in the CHANGELOG the
way the Task Board's and the debt registry's were.


---

## Owner rulings, 2026-09-02 15:53

`/tfw-plan` was invoked on this task. The coordinator declined to write an HL over a proposal
that names `/tfw-config` as the entry point, and asked instead. Three rulings came back.

**1. The entry point holds.** `/tfw-config`, not `/tfw-plan`. No HL, no TS, no ONB, no RF, no
REVIEW. The routing line at the top of this document stands as written.

**2. The knowledge gate is skipped.** Recorded in `status.md` as
`knowledge-gate: skipped (reason: removal of a forgotten command; the task produces no new
architectural facts)`. At the gate: `interval` 5, `gate_mode` hard, `last_consolidation_seq` 60
dated 2026-08-30, six tasks opened since.

**3. Adjacent staleness is folded into the same run.** The two blocks in
`.tfw/adapters/claude-code/README.md` that this removal must edit anyway are stale beyond
`tfw-task`, and the run repairs both:

| Block | Stale how | What the run does |
|---|---|---|
| file tree, line 16 | lists 9 commands; `tfw-config`, `tfw-init`, `tfw-knowledge` missing | drop the `tfw-task` line, add the three missing ones |
| command table, line 86 | same three commands missing | drop the `/tfw-task` row, add the three missing rows |

## Footprint, re-measured 2026-09-02 15:53

The table above says nine reference sites. Measuring again gives **ten**, in the same six
tracked files. The tenth is `.tfw/adapters/codex/README.md:51` — the line this document itself
hedged over as possibly history; it appears not to have been counted. Ruling: it is **not**
history. It documents a deliberate absence from one adapter, and once the command exists in no
adapter the sentence asserts a distinction that no longer exists. Remove it.

Confirmed unchanged from the original measurement:

- both deletions exist, and differ from each other — 1 625 B and 1 430 B
- `.tfw/workflows/task.md` does not exist; there is no source
- `.agents/skills/` holds 11 skills and `.tfw/adapters/codex/skills/` holds 11; `tfw-task` is in
  neither, so the Codex adapter needs no skill removal
- `.tfw/CHANGELOG.md:1156` is history and is never edited
- `site/` is gitignored with zero tracked files; its twenty-odd hits regenerate on the next build
  and are never edited by hand

---

*PROPOSAL — Retire the task meta-workflow | 2026-09-02*
