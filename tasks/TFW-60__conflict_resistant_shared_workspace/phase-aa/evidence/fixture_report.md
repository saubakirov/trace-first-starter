# Fixture run — the development half of AC-13

> **What this is:** the executor's development fixture, run to build AC-2, AC-3, AC-4, AC-6
> and AC-8 against a real external corpus instead of against this repository.
> **What this is NOT:** acceptance evidence. AC-13 half two is the owner's own run on a real
> project, filed at task root as `FIELD-REPORT__TFW-60__second_external_update.md`. **This
> file does not close it, and the RF reports half two as unmet.**
> **Full transcript:** [fixture_run.txt](fixture_run.txt)

---

## The fixture

| Property | Value |
|---|---|
| Source corpus | `KZ-IT-telegram-list` at `c919640` — the commit before its own 2.0.0 update |
| Cloned to | the session scratch directory. **The live project was never written to** |
| TFW version | `1.3.0` |
| Payload source | this repository at `1079020`, by `git archive` — a commit SHA, not a tag |
| Update performed | `1.3.0 → 2.0.0-dirty.2`, following `update.md` and `.tfw/migrations/2.0.0.md` only |

Why this corpus and not a synthetic one: it carries **F3, F4 and F6 in one tree**.

- board at `tasks/README.md` under `## Board`, not the root README — F3
- `TFW-01_awesome_list_restructure` and `TFW-02_enhanced_validation` beside
  `TFW-3__tfw_init` and `TFW-4__showcase_reorg` — mixed identifier grammar, F4
- no `task_containers`, and `initial_seq: 3` — F6

## Outcome

| Check | Result |
|---|---|
| Update completed following only `update.md` and the guide | ✅ |
| Files hand-carried from outside the payload | **0** |
| Framework files edited inside `.tfw/` | **0** (see below) |
| `--check project` on the migrated fixture | `exit 0` |
| Board rows accounted for | 4 of 4, each named individually |
| Task directories accounted for | 4 of 4 — 2 matched, 2 reported unresolved |

The one file that differed from the payload was
`.tfw/scripts/__pycache__/gen_index.cpython-313.pyc` — Python bytecode written by running
the tool, not an edit. It produced a real finding, below.

## What each finding's fix did on a real corpus

### F3 — the board is found where the project keeps it

Run with defaults, the migration refused and named **relocation first**, with the exact flags
this fixture needed:

```
board source: git show HEAD:README.md -> 0 data rows
REFUSING: git show HEAD:README.md yielded zero rows under the heading '## Task Board'.
  Three causes, in the order they actually occur:
    1. the board is ELSEWHERE -- ...  --board tasks/README.md
    2. the heading differs            --board-heading '## Board'
    3. the board was REMOVED          --board-rev <commit-before-removal>
```

The shipped message offered only `--board-rev`, which sends a reader to diagnose a *removed*
board when the board is merely *elsewhere*. With the flags: `4 data rows`.

The row parser was not touched, and did not need to be.

### F4 — two directories stop being called ideas

The failing run reported *"2 task directories where 4 exist"* and rendered both
single-underscore directories under a heading reading *"They are ideas, not work in
progress"*, with `backlog idea, never started` in the manifest. Both hold completed HL, TS
and RF traces.

Now:

```
    2  matched       row and directory both exist
    0  board-only    a row with no directory at all
    2  unresolved    a row whose directory the grammar rejects
    0  unresolved    a rejected directory no row names
    0  directory-only  a directory with no row
```

`backlog idea, never started` appears nowhere in the manifest. The generated index has **no
`Backlog` section at all**, and both directories appear under `Unresolved inputs` with a
reason that talks about the name and asserts nothing about whether work happened:

> directory name matches neither identifier grammar … Board row `TFW-01` names it. Nothing
> further is asserted about it: rename it by hand to the recognized grammar to have it
> picked up

The manifest and the index agree, because both read one classification. Every identifier
still resolves by name:

| # | Identifier | Resolves to |
|---:|---|---|
| 1 | `TFW-01` | snapshot + directory whose name the grammar rejects + index (unresolved) |
| 2 | `TFW-02` | snapshot + directory whose name the grammar rejects + index (unresolved) |
| 3 | `TFW-3` | snapshot + task directory + index (unresolved or closed) |
| 4 | `TFW-4` | snapshot + task directory + `status.md` → index |

### F8 — the source is a committed revision

`board source: git show HEAD:tasks/README.md`, printed on every run. The working tree is
`--working-tree`, and it was not needed here.

### F1 — the depth was load-bearing, and this is the only test that shows it

`parents[2]` resolves correctly from `.tfw/scripts/` **by coincidence**, so a source-only
move would have passed every test in this repository. The observable test is the tools copied
to a different depth *inside* a project:

| Placed at | `parents[2]` would give | The tool resolved |
|---|---|---|
| `tools/` | `…/fixture` — **wrong, outside the project** | `…/fixture/consumer` ✅ |
| `tools/tfw/` | `…/fixture/consumer` — right, by luck | `…/fixture/consumer` ✅ |
| `a/b/c/d/` | `…/consumer/a/b` — **wrong** | `…/fixture/consumer` ✅ |

Depth arithmetic would have been wrong in two of three placements. It was also *silently*
wrong: `tools/` resolves to a directory outside the project, where a run would have written
an index for a tree nobody asked about.

### AC-10 — the pristine-tag diff, and whose tag it is

The fixture has **no TFW version tags of its own**; the tag lives in the source. Run against
the source's `v1.3.0`:

```
CUSTOMIZED .tfw/knowledge_state.yaml
CUSTOMIZED .tfw/project_config.yaml
customized files: 2
```

Two files out of ~38, and both are the ones that are *supposed* to be project-owned. Every
other `.tfw/` file was byte-identical to the release and could simply be overwritten. This is
the check that turned three declared manual merges into zero on the first real update.

### F6 — the two decisions arrived as decisions

`task_containers` was chosen (`[tasks]` — the existing directory keeps its name and its
tasks) and `initial_seq: 3` was deleted, both because `update.md` named them rather than
leaving them to inference.

## Two findings the fixture produced that no test here could have

### 1. The first command the guide gives died on a Windows console · **was a blocker**

```
File "…/encodings/cp1252.py", line 19, in encode
UnicodeEncodeError: 'charmap' codec can't encode character '✅' in position 1679
```

`migrate_board.py` without `--manifest` prints the manifest to stdout, and the manifest
quotes the board **verbatim** — so it carries whatever characters the project's board
carried. On a console whose codepage is cp1252, `print()` raises and the run dies before
printing anything useful.

Runtime *messages* are ASCII by rule here, and a test enforces it. **Content is not, and
cannot be** — the whole value of the verbatim block is that it is exact. Fixed by making both
entry points' streams tolerant (`errors="replace"`) while files keep `encoding="utf-8"` and
stay byte-exact. Two tests added: one drives the tool as a subprocess with
`PYTHONIOENCODING=cp1252`, one asserts the written snapshot keeps every row's exact bytes.

Not findable by inspection here: this repository's own board is gone, so nothing in its test
corpus prints a real board to a real console.

### 2. Copying a payload adds and overwrites, but never removes · **medium**

```
RETIRED: .tfw/templates/topic_file.md
```

The template moved to `templates/knowledge/topic.md`. The old path stayed in the fixture's
`.tfw/` because copying a payload over an existing one cannot delete anything. A second copy
of a template is a second thing that can be edited by mistake.

The guide now carries the command that finds them.

### 3. `__pycache__` dirties a receiving project's tree · **low**

Running a shipped Python tool writes `.tfw/scripts/__pycache__/`. This repository's
`.gitignore` covers it; a project whose ignore rules never needed a Python entry will see the
payload dirty its own tree on first use. One line added to the guide.

## What was confusing, not only what worked

- **`update.md` Step 3a's loop reads from the source, not from the receiving project**, and
  the first attempt got that backwards. The step now says whose tag; it needed saying twice
  before it stuck.
- **The `--board` and `--board-heading` flags are two decisions that arrive as one.** The
  refusal names both, which is why the second attempt worked — but a reader who fixes only
  the path gets zero rows again and has to read the refusal a second time.
- **Nothing tells the operator to delete retired framework files** until the guide says so,
  and there is no check that reports one. `--check project` could grow that; it is filed as
  an observation rather than added, because a payload-completeness check that also asserts
  payload *minimality* is a different claim.

## What is deliberately not closed

**AC-13 half two.** This is a clone in a scratch directory, driven by the same agent that
wrote the code. It is a development fixture and it is not acceptance evidence — the point of
DoD 19 is a project whose operator is not the author. The live `KZ-IT-telegram-list` was
never written to: it belongs to its owner, and a second agent writing into it is the defect
this task exists to end.

---

*Fixture run for TFW-60 Phase AA · 2026-08-27 · payload at `1079020`*
