# EV — TFW-60 / Phase A: Task State & Coordination

> **Date**: 2026-08-26
> **Author**: Claude Code (Executor)
> **Task**: TFW-60 / Phase A
> **TS**: [TS Phase A](../TS__phase-a__task_state_and_coordination.md) — revision 2, approved 2026-08-26

---

## What "Evidence: N/A" means in this phase, and what it does not

**Every AC in the TS carries `Evidence: N/A`.** That is not an oversight and it is not coverage.
Amendment A3 moved every real-environment transport claim to TFW-61, and ruling S43 moved the
observation of a non-technical participant there too. What remains in Phase A is
transport-independent behaviour, and the honest verification for it is a deterministic fixture —
which is what the rows below record.

Two claims are therefore **explicitly not made anywhere in this phase**:

| Not claimed | Why | Who owns it |
|---|---|---|
| That a non-specialist can read or repair these carriers | Design intent only. No such participant was observed. NS3 forbids asserting untested comprehension | [TFW-61](../../../TFW-61__collaboration_transport_modes/PROPOSAL__TFW-61__collaboration_transport_modes.md) (S43) |
| That any file-sync or Git transport behaviour works | No provider, no client, no second machine was involved | TFW-61 (amendment A3) |

The concurrency evidence below is **two processes on one machine**. Cross-device behaviour is
not evidenced and is not claimed.

## Environment

| Field | Value |
|-------|-------|
| OS | Windows 11 Pro 26200, NTFS |
| Language / Runtime | Python 3.13.5 |
| Test runner | pytest 9.0.2 |
| Shell | Git Bash, `PYTHONUTF8=1` |
| Repository state | baseline `80d6a16`; verified at `HEAD` of the Phase A executor commits |
| CI / Pipeline | local; the MkDocs build runs inside `test_integration.py` |
| Second machine | **none** — no cross-device claim is made |
| Sync provider | **none** — no provider claim is made |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | A fixture task driven `TODO → ONB → BLOCKED → RF → DONE → REJECTED`; path set diffed before and after — identical. No terminal state moved the directory | temp tree | VERIFIED | `fixture_transcript.txt` §AC-1 |
| E2 | AC-1 | A task created in December and updated the following March stays in the 2026 folder; the year is never recomputed | temp tree | VERIFIED | `fixture_transcript.txt` §AC-1 |
| E3 | AC-1 | Two different `task_containers` values over one tree resolve differently (`[workspace, tasks]` → 1 task; `[elsewhere]` → 0). Nothing hardcodes `tasks/` | temp tree | VERIFIED | `fixture_transcript.txt` §AC-1; `test_gen_index.py::test_container_key_is_configuration_not_a_literal` |
| E4 | AC-2 | Task creation succeeds with the container empty — no counter, no project-wide maximum, no other task read | temp tree | VERIFIED | `fixture_transcript.txt` §AC-2 |
| E5 | AC-2 | Frozen clock replayed a used identifier; the collision was **detected at identifier level** and resolved by taking a new actual timestamp. The existing directory was neither reused nor overwritten | frozen-clock fixture | VERIFIED | `fixture_transcript.txt` §AC-2 |
| E6 | AC-2 | A clock that never advances fails visibly after 5 attempts instead of looping — the backwards-stepping-clock case (ONB risk 3) | frozen-clock fixture | VERIFIED | `fixture_transcript.txt` §AC-2 |
| E7 | AC-2 | Both grammars resolve through one shared resolver: `20260826-120000` → clock, `TFW-60` → legacy | — | VERIFIED | `test_gen_index.py::test_parse_identifier` (7 cases) |
| E8 | AC-3 | Two threads appended events at the same timestamp: **two files, both bodies intact, nothing lost** | 2 threads, 1 machine | VERIFIED | `fixture_transcript.txt` §AC-3 |
| E9 | AC-3 | A 121-code-point summary was refused, and the refusal names the artifact route | temp tree | VERIFIED | `fixture_transcript.txt` §AC-3 |
| E10 | AC-3 | A correction was written as a new event; the original file's bytes are unchanged | temp tree | VERIFIED | `fixture_transcript.txt` §AC-3 |
| E11 | AC-3 | **The ceiling is 120 code points, and the measurement is recorded.** Populations: 272 commit summaries naming a task, 63 REVIEW state-change summaries. Medians 38 and 9; combined p95 83, p99 110. 120 refuses 3 of 335 real entries, and all three are shown | this repository | VERIFIED | `ceiling_measurement.txt` |
| E12 | AC-4 | All four resolution cases produce the specified behaviour: one profile → silent; several with no binding → one question; several with a binding → resolved; stale binding → one question, never a guess | temp tree + temp home | VERIFIED | `fixture_transcript.txt` §AC-4 |
| E13 | AC-4 | The binding file lives outside the project tree; the shared tree carries no binding and no private preferences | temp tree + temp home | VERIFIED | `fixture_transcript.txt` §AC-4 |
| E14 | AC-4 | Resolution reads only `team/` and the binding — no OS username, hostname or account string is consulted | temp tree | VERIFIED | `fixture_transcript.txt` §AC-4 |
| E15 | AC-4 | An automated principal carries its own profile (`type: agent`) and borrows no person's handle | temp tree | VERIFIED | `fixture_transcript.txt` §AC-4 |
| E16 | AC-4 | Readability of these carriers by a non-specialist | — | **DEFERRED** | **No non-technical participant was observed. Blocker: that participant appears in file-sync mode, which TFW-61 owns (S43). Asserted as design intent only** |
| E17 | AC-5 | Generated twice from identical input — byte-identical. Freshness is derived from the newest task `updated`, never from the wall clock, so two runs a minute apart agree | this repository + temp | VERIFIED | `fixture_transcript.txt` §AC-5; `test_gen_index.py::test_generation_is_byte_identical_across_runs` |
| E18 | AC-5 | The index declares that it is derived, its source count and its freshness; sorting is by a declared key, newest last | this repository | VERIFIED | `../../../../workspace/00-INDEX.md` header |
| E19 | AC-5 | Malformed and unresolved inputs are reported, not dropped — TFW-30 appears with a stable diagnostic naming its board-row class | this repository | VERIFIED | `workspace/00-INDEX.md` § Unresolved inputs |
| E20 | AC-5 | All four index conditions run: normal / absent / stale / malformed. Each detected; **task state byte-identical in all four** | temp tree | VERIFIED | `fixture_transcript.txt` §AC-5 |
| E21 | AC-6 | Migration ran as a dry run against a manifest before any project write; the manifest is a committed artifact | this repository | VERIFIED | `migration_accounting.md` |
| E22 | AC-6 | **61 board rows + 53 directories = 114 occurrences → 61 identities: 53 matched, 8 board-only, 0 directory-only.** Zero unexplained | this repository | VERIFIED | `migration_accounting.md` § Reconciliation |
| E23 | AC-6 | `git diff 80d6a16 HEAD -- tasks/` reports **14 additions and zero modifications**. Not one pre-existing task artifact was renamed, moved or byte-changed | this repository | VERIFIED | inline: `git diff --name-status 80d6a16 HEAD -- tasks/` → 14 × `A`, 0 × `M`/`R`/`D` |
| E24 | AC-6 | The migration opens no existing file in write mode and aborts rather than overwrite | temp tree | VERIFIED | `test_migrate_board.py::test_apply_leaves_every_pre_existing_file_byte_identical`, `::test_apply_refuses_to_overwrite` |
| E25 | AC-6 | No fact invented: `value: unrecorded` and `owner: unassigned` where the board carried nothing; every `authority` resolves to a file that exists | this repository + temp | VERIFIED | `test_migrate_board.py::test_facts_the_board_never_carried_are_marked_absent_not_guessed`, `::test_authority_points_at_a_file_that_exists` |
| E26 | AC-6 | Values outside the vocabulary carried verbatim, never normalized: `🟡 TS` (TFW-4) and `❄️ FROZEN` (TFW-45) both became `UNDECLARED` + `lifecycle_verbatim` | this repository | VERIFIED | `tasks/TFW-45__multi_agent_workflows/status.md`; `test_migrate_board.py::test_undeclared_values_are_carried_verbatim_never_normalized` |
| E27 | AC-6 | **All 61 rows captured verbatim** before removal — terminal, backlog and struck-through alike, including the 6 backlog rows with no directory | this repository | VERIFIED | `tasks/BOARD-SNAPSHOT.md` § Verbatim source |
| E28 | AC-7 | Corpus-wide relative-link check before and after. **Baseline 82 broken links → 64 now.** The failure set shrank by 18 | this repository, both trees | VERIFIED | inline, below |
| E29 | AC-7 | The 5 entries appearing "new" are the same template placeholder links renamed `{PREFIX}-{N}` → `{ID}`; each has a matching baseline entry under its old spelling | this repository | VERIFIED | inline, below |
| E30 | AC-7 | 278 commit subjects naming a task were resolved against the 53 directories. One identifier has no directory: **TFW-37**, which never had one and was already unresolvable at baseline | this repository | VERIFIED | inline: baseline carries the same single TFW-37 subject |
| E31 | AC-7 | `tasks/README.md` explains why a second container exists, with the measured reason for not renaming | this repository | VERIFIED | `../../../README.md` |
| E32 | AC-8 | `git grep -i "task board"` over `.tfw/`, `docs/`, `README.md`, `AGENTS.md`, `CLAUDE.md`, `RELEASE.md` returns only historical mentions | this repository | VERIFIED | inline, below |
| E33 | AC-8 | The board parser is gone from `gen_docs.py`; the tasks index reads `status.md` through the shared resolver | this repository | VERIFIED | `test_integration.py::test_generators_do_not_read_the_root_readme_for_task_state` |
| E34 | AC-8 | **A test fails if a board-shaped table regex is reintroduced into `docs/scripts/`.** It fired during this phase and caught a real leftover — an unused `SNAPSHOT_ROW` constant in `gen_index.py`, since removed | this repository | VERIFIED | `test_integration.py::test_no_board_shaped_regex_survives_in_the_generators` |
| E35 | AC-8 | `test_integration.py` line 159 was **rewritten, not deleted**: the vacuous assertion became three tests that fail if the board returns | this repository | VERIFIED | `test_integration.py` — `test_index_override_used` plus three new tests |
| E36 | AC-8 | The MkDocs site builds with the board absent | local build inside pytest | VERIFIED | `test_integration.py` — 22 integration tests pass, site generated |
| E37 | AC-9 | A task driven through `HL_DRAFT → TS_DRAFT → ONB → RF → REV → DONE` with **nothing but file writes** — no engine, no mutation interface, no required tool | temp tree | VERIFIED | `fixture_transcript.txt` §AC-9 |
| E38 | AC-9 | With **no index present at all**, the task stayed readable and reached `DONE`; `--check` reported the index stale rather than blocking | temp tree | VERIFIED | `fixture_transcript.txt` §AC-9 |
| E39 | AC-9 | Executable code in the release is exactly `gen_docs.py`, `gen_index.py`, `migrate_board.py`. Nothing requires a daemon, database, lock server, vendor API or MCP host | this repository | VERIFIED | `fixture_transcript.txt` §AC-9 |
| E40 | AC-10 | `.tfw/VERSION` is `2.0.0`; `tfw.version` matches | this repository | VERIFIED | `.tfw/VERSION`, `.tfw/project_config.yaml` |
| E41 | AC-10 | The CHANGELOG entry states the breaking change and the migration path, and presents the container as **one configuration value** taking a list — not two supported layouts | this repository | VERIFIED | `.tfw/CHANGELOG.md` § [2.0.0] |
| E42 | AC-10 | Quick Start, canonical rules, glossary, templates and adapter originals carry no residue of the board, a state engine or an identity subsystem | this repository | VERIFIED | E32 sweep; `git grep` for "state engine", "device registry" → 0 in `.tfw/` |
| E43 | AC-10 | TD-81 and TD-177 retired **by the code change plus the reintroduction test**. The `TECH_DEBT.md` registry edit is not the executor's under D37 and is handed to `/tfw-docs` | this repository | VERIFIED | E33, E34; handoff listed in RF §6 |
| E44 | AC-3, AC-5, AC-6 | Full suite green: **129 passed, 1 skipped**. The skip is `test_repository_accounting_balances`, which skips by design once the board is gone | local | VERIFIED | inline, below |

### Inline output

**E28 / E29 — link-failure set, before and after**

```
baseline 80d6a16 : TOTAL 82 broken relative links
HEAD             : TOTAL 64 broken relative links
                   NEW 5   FIXED 23

each NEW entry has a matching baseline entry under the old placeholder:
  YES  .tfw/templates/RF.md -> evidence/EV__{ID}__{title}.md
  YES  .tfw/templates/research/1_briefing.md -> ../../HL-{ID}__{title}.md
  YES  .tfw/templates/research/2_gather.md -> ../../HL-{ID}__{title}.md
  YES  .tfw/templates/research/3_extract.md -> ../../HL-{ID}__{title}.md
  YES  .tfw/templates/research/4_challenge.md -> ../../HL-{ID}__{title}.md
```

The gate is "the failure set must not grow." It shrank by 18.

**E32 — the board sweep**

```
$ grep -rin "task board" .tfw/ docs/ README.md AGENTS.md CLAUDE.md RELEASE.md \
    | grep -viE "retired|removed|snapshot|CHANGELOG"
(no output)
```

Remaining mentions are all historical and permitted: the `.tfw/CHANGELOG.md` entry recording the
removal, the `glossary.md` entry marked *(retired at 2.0.0)*, the `gen_docs.py` docstring
explaining what TD-81 was, and `migrate_board.py`, whose job is to read the board once.

`KNOWLEDGE.md`, `knowledge/convention.md` and `TECH_DEBT.md` are **outside this sweep by ruling**
(ONB Q3): they have other owners under D37 and are handed to `/tfw-docs` and `/tfw-knowledge`
through RF §6. They still contain board statements. That is a known, recorded, assigned gap — not
a silent one.

**E44 — build gate**

```
$ python -m pytest docs/scripts/ -q
129 passed, 1 skipped in 33.84s
```

Baseline was 68 passing. 61 tests were added; 1 skips by design once the board is gone.

**E23 — corpus integrity**

```
$ git diff --name-status 80d6a16 HEAD -- tasks/ | awk '{print $1}' | sort | uniq -c
     14 A
```

No `M`, no `R`, no `D`. Every change to the legacy corpus is an addition.

## Verdict

**Evidence verdict: 43/44 VERIFIED, 1 DEFERRED, 0 BLOCKED, 0 N/A.**

The single DEFERRED item is E16 — readability by a non-technical participant — deferred with a
named blocker: no such participant exists in a transport-independent fixture, and observing one
belongs to TFW-61 under S43. Phase A asserts that readability as design intent and does not claim
it as observed.

**Two limits on what this evidence supports**, stated so no reader has to infer them:

1. **Concurrency was demonstrated between two processes on one machine.** Behaviour across two
   machines, or through any synchronization provider, is neither tested nor claimed.
2. **Determinism holds given identical inputs.** One task directory in this repository,
   `tasks/TFW-36__content_marketing_blog_series/`, carries a `.gitignore` containing `*` and is
   therefore invisible to Git entirely. Its `status.md` exists on disk and the index reads it, but
   a fresh clone has different inputs and will produce a different index. That condition
   pre-existed this phase and was not created by it; it is reported in RF §6 rather than
   overridden.

## Attachments

| File | Description |
|------|-------------|
| `census.md` | The measured baseline the owner's overrun ruling stands on, landed before any other write |
| `migration_accounting.md` | Row-by-row reconciliation of 61 board rows against 53 directories, regenerable |
| `fixture_transcript.txt` | Full output of the acceptance fixtures — 30 checks across AC-1, 2, 3, 4, 5 and 9, all passing |
| `ceiling_measurement.txt` | The two populations behind the 120-code-point journal ceiling, the percentile table, and the three real entries it refuses |

> The fixture harness that produced `fixture_transcript.txt` is **not** a deliverable and does not
> ship. AC-9 limits release code to index generation and migration accounting; the harness performs
> the same ordinary file writes a lifecycle skill performs, so the guarantees can be observed
> rather than asserted.

---

*EV — TFW-60 / Phase A: Task State & Coordination | 2026-08-26*
