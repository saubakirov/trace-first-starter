# EV — TFW-60 / Phase A: Task State & Coordination

> **Date**: 2026-08-27
> **Author**: Claude Code (Executor), acting for `saubakirov`
> **Task**: TFW-60 / Phase A — third corrective pass
> **TS**: [TS Phase A](../TS__phase-a__task_state_and_coordination.md) — revision 5, approved
> **Reviews**: [rev 3](../REVIEW__phase-a__task_state_and_coordination__rev3.md) 🔄 · [rev 2](../REVIEW__phase-a__task_state_and_coordination__rev2.md) 🔄 · [first](../REVIEW__phase-a__task_state_and_coordination.md) ❌
>
> ## 📌 PINNED SNAPSHOT: `afd24f5`
>
> **Every number in this file is measured at `afd24f5`, and at nothing else.** Not at HEAD.
> The commit carrying this file is deliberately *not* the commit these numbers describe.
>
> Three rounds produced contradicted evidence from three honest attempts, and the cause was
> structural rather than careless: the executor counts the tree, then commits a report
> containing those counts, and that commit changes the tree that was counted. **A measurement
> cannot include the act of recording it.** `conventions.md` §3 rule 16 settled the same
> problem for freeze baselines — a commit's SHA cannot appear in its own content.
>
> Re-run any command in [`measurement_log.txt`](measurement_log.txt) against `afd24f5` and
> you get this file. One population per quantity; no `baseline-to-HEAD` counts anywhere.

---

## What "Evidence: N/A" means here, and what it does not

Every AC in the TS carries `Evidence: N/A`. That is not coverage. Amendment A3 moved
real-environment transport claims to TFW-61, and S43 moved the non-technical-participant
observation there. What remains is transport-independent behaviour, verified by deterministic
fixture and by shipped tests.

**Three claims are explicitly not made anywhere in this phase:**

| Not claimed | Why | Who owns it |
|---|---|---|
| That a non-specialist can read or repair these carriers | Design intent only; no such participant was observed. NS3 forbids asserting untested comprehension | TFW-61 (S43) |
| That any file-sync or Git transport behaviour works | No provider, no client, no second machine | TFW-61 (A3) |
| That concurrency holds across machines | The evidence is two threads and two processes on **one** machine | TFW-61 |

## Environment

| Field | Value |
|-------|-------|
| OS | Windows 11 Pro 26200, NTFS |
| Runtime | Python 3.13.5, pytest 9.0.2 |
| Shell | Git Bash, `PYTHONUTF8=1` |
| Pinned snapshot | **`afd24f5`** — every figure measured here |
| Baseline for deltas | `80d6a16` |
| Board source | `git show b094943:README.md` — the last commit that still held the board |
| Second machine | **none** |
| Sync provider | **none** |

## The clock reads, shown

AC-3 and AC-12 require every time value to be read from the system clock rather than
composed. The rejected pass shipped an event stamped `23:20:00` — round seconds, dated after
the review that consumed it. Each read this pass was printed at the moment of writing:

```
ownership_changed event   datetime.now().astimezone() -> 2026-08-26T22:46:47+05:00
                          derived stamp               -> 20260826-224647
                          filename                    -> 20260826-224647__ownership_changed__saubakirov.md

phase-a/status.md         clock read for phase state  -> 2026-08-26T23:15:29+05:00 -> 20260826-231529

migration re-run          clock read: 20260826-231927
                          board source: git show b094943:README.md -> 61 data rows
```

No value in this pass was typed. The seconds are `47`, `29`, `27` — not round.

## Evidence

| # | AC | What was verified | Result | Artifact |
|---|----|--------------------|--------|----------|
| E1 | AC-1 | Fixture task driven `TODO → ONB → BLOCKED → RF → DONE → REJECTED`; path set diffed before and after — identical | VERIFIED | `fixture_transcript.txt` §AC-1 |
| E2 | AC-1 | A December task updated the following March stays in the 2026 folder | VERIFIED | `fixture_transcript.txt` §AC-1 |
| E3 | AC-1 | Two container values over one tree resolve differently; nothing hardcodes `tasks/` | VERIFIED | `fixture_transcript.txt` §AC-1; `test_container_key_is_configuration_not_a_literal` |
| E4 | AC-2 | **The identifier is the whole directory name.** A bare `YYYYMMDD-HHMMSS` is refused by the resolver as ambiguous | VERIFIED | `test_a_bare_timestamp_is_never_accepted_as_an_identifier` |
| E5 | AC-2 | **The case revision 2 could not express**: two mutually offline participants creating in the *same second* with different slugs produce two identifiers and do not collide | VERIFIED | `fixture_transcript.txt` §AC-2; `test_same_second_different_slug_are_two_distinct_identifiers` |
| E6 | AC-2 | Same second **and** same slug is one task — surfaced as such, not duplicated | VERIFIED | `fixture_transcript.txt` §AC-2; `test_same_second_same_slug_is_the_same_identifier` |
| E7 | AC-2 | Creation reads no counter and no other task's contents | VERIFIED | `fixture_transcript.txt` §AC-2 |
| E8 | AC-2 | A clock that will not advance fails visibly after 5 attempts instead of looping | VERIFIED | `fixture_transcript.txt` §AC-2 |
| E9 | AC-2 | **The creation algorithm is in the shipped workflow**, not only a fixture — container, clock, create-or-retry, the bound, the visible failure | VERIFIED | `.tfw/workflows/plan.md` step 2 |
| E10 | AC-3 | **The case revision 2 lost**: same second, **same kind**, two actors → two files, both bodies intact | VERIFIED | `fixture_transcript.txt` §AC-3; `test_same_second_same_kind_two_actors_produce_two_files` |
| E11 | AC-3 | One actor writing twice in a second **takes another reading of the clock**. The earlier implementation added a second arithmetically — a number somebody allocated, which its own docstring forbade — and at `23:59:59` it wrapped the time while keeping yesterday's date. Now every candidate is a reading, proven by a controllable clock that records what it was asked for | VERIFIED | `test_every_candidate_comes_from_a_clock_reading`, `test_the_clock_is_read_again_between_attempts`, `test_midnight_does_not_reverse_the_date` |
| E12 | AC-3 | An event without `on_behalf_of` is refused | VERIFIED | `fixture_transcript.txt` §AC-3; `test_an_event_without_on_behalf_of_is_refused` |
| E13 | AC-3 | A provider name is rejected as an actor **even when filename and body agree**. The earlier test only proved a mismatch was caught, so `actor: claude` stated consistently in both places passed. An actor must now also resolve to a declared `team/` handle | VERIFIED | `test_a_provider_name_is_not_an_actor_even_when_filename_and_body_agree`, `test_no_provider_family_may_be_an_actor` (5 cases), `test_an_actor_must_be_a_declared_team_handle` |
| E14 | AC-3 | Over-ceiling summary refused, artifact route named | VERIFIED | `fixture_transcript.txt` §AC-3 |
| E15 | AC-3 | A correction is a new event; the original's bytes are unchanged | VERIFIED | `fixture_transcript.txt` §AC-3 |
| E16 | AC-3 | **Ceiling 120 code points, population pinned at `afd24f5`**: **296** commit subjects + **65** REVIEW verdicts = **361**; medians 38 and 9; combined p95 81, p99 110; **3 of 361** refused, all three quoted in full. It read 292, then 294, then 295 for the same quantity because each run read the live tree; both populations are now taken with `git log afd24f5` and `git show afd24f5:<file>` | VERIFIED | `ceiling_measurement.txt`, pinned |
| E17 | AC-3 | Six pre-2.0.0 events are reported as **legacy**, not corrected — the journal is immutable, so a later rule describes old entries and never rewrites them | VERIFIED | `workspace/00-INDEX.md` § Unresolved inputs; `test_legacy_events_are_reported_as_legacy_not_as_defects` |
| E18 | AC-4 | All four resolution cases behave as specified: one profile silent; several with no binding → one question; binding → resolved; stale binding → one question | VERIFIED | `fixture_transcript.txt` §AC-4 |
| E19 | AC-4 | **Resolution is in the shipped workflows**, and the Windows binding location is the literal `%LOCALAPPDATA%\tfw\bindings.yaml`. It had shipped with a TAB and a BACKSPACE where the two backslash escapes were interpreted, in 6 canonical files and 12 adapter copies — every agent sent to a path that cannot exist | VERIFIED | `control_char_gate.txt` step 4; `test_the_windows_binding_path_is_the_literal_one` |
| E20 | AC-4 | **No agent profile ships.** `team/claude-code.md` and `team/codex.md` deleted; the schema still admits `type: agent` so TFW-54 fills the slot | VERIFIED | `fixture_transcript.txt` §AC-4; `team/` holds `README.md` + `saubakirov.md` |
| E21 | AC-4 | The withdrawal is recorded as a **new event**, not an edit — three prior events keep `actor: claude-code` / `codex` bytes untouched | VERIFIED | `journal/20260826-224647__ownership_changed__saubakirov.md` |
| E22 | AC-4 | Identity is never inferred from OS username, hostname or account string | VERIFIED | `fixture_transcript.txt` §AC-4 |
| E23 | AC-4 | Readability by a non-specialist | **DEFERRED** | **No such participant exists in a transport-independent fixture. Blocker named: the observation belongs to TFW-61 under S43** |
| E24 | AC-5 | Byte-identical across two runs; freshness derived from inputs, never the wall clock | VERIFIED | `test_generation_is_byte_identical_across_runs`, `test_freshness_comes_from_inputs_not_the_clock` |
| E25 | AC-5 | Declares derived, source count, freshness; explicit sort by a declared key | VERIFIED | `workspace/00-INDEX.md` header |
| E26 | AC-5 | Malformed and unresolved inputs reported with stable diagnostics, never dropped | VERIFIED | `fixture_transcript.txt` §AC-5 |
| E27 | AC-5 | Normal / absent / stale / malformed all detected; **task state byte-identical in all four** | VERIFIED | `fixture_transcript.txt` §AC-5 |
| E28 | **AC-5 / F15** | **A normal transition touches exactly one file, and it is the task's own.** The index is then stale, and that is the correct state | VERIFIED | `fixture_transcript.txt` §AC-5; `test_a_task_transition_does_not_touch_anything_shared` |
| E29 | **AC-5 / F15** | The forcing test is **gone**. `build.verify` is now `gen_index.py --validate`, which reads task-local truth and is unaffected by index freshness | VERIFIED | `.tfw/project_config.yaml`; `test_a_stale_index_is_visible_but_never_blocking` |
| E30 | **AC-6** | **The board source is explicit, and a zero-row read is REFUSED.** This is the defect that deleted the trace | VERIFIED | inline, below; `test_an_empty_board_source_is_refused` |
| E31 | **AC-6** | **Snapshot verified BY COUNT against the pre-removal commit: 61 = 61.** Not by a sentence | VERIFIED | inline, below |
| E32 | **AC-6** | All 61 identifiers **named individually** in the accounting; `Unaccounted: 0` | VERIFIED | `migration_accounting.md` § Every board identifier |
| E33 | **AC-6** | The eight identifiers lost in the rejected pass named, with where each lands | VERIFIED | `census.md` §2 |
| E34 | AC-6 | Reconciliation: 61 rows + 53 directories → 53 matched, 8 board-only, 0 directory-only | VERIFIED | `migration_accounting.md` § Reconciliation |
| E35 | AC-6 | **The migration changed no pre-existing task artifact.** `80d6a16..afd24f5` over `tasks/` is **48 additions and 4 modifications** — a pinned range, not "baseline-to-HEAD", which invalidates itself the moment the RF lands. All four modifications are coordinator artifacts of live tasks, each attributed to its commit. No executor commit modified a file the phase did not create, except the reverted broad-staging error | VERIFIED | `measurement_log.txt` §3 |
| E36 | AC-6 | Nothing invented: `value: unrecorded`, `owner: unassigned` where the board was silent | VERIFIED | `test_facts_the_board_never_carried_are_marked_absent_not_guessed` |
| E37 | AC-6 | Out-of-vocabulary values carried verbatim: `🟡 TS` and `❄️ FROZEN` → `UNDECLARED` + `lifecycle_verbatim` | VERIFIED | `tasks/TFW-45__multi_agent_workflows/status.md` |
| E38 | AC-7 | Link-failure set did not grow — **re-run now, not quoted**: baseline 82 → HEAD 64, 5 new and 23 fixed, and all 5 "new" are the same template placeholder links under their renamed spelling, each with a matching baseline entry | VERIFIED | `measurement_log.txt` §E38 |
| E39 | AC-7 | The equal-depth clause is deleted by R3 — nothing to execute | N/A | TS §AC-7 |
| E40 | AC-8 | The board sweep, **run with no filtering**, returns 19 lines: the CHANGELOG entry recording the removal, the glossary term marked *(retired)*, the README snapshot row, a `gen_docs.py` docstring, the migration script itself, and the guard tests. The earlier EV claimed "no output", which came from a filtered form of the command that was not the form shown | VERIFIED | `measurement_log.txt` §E40 |
| E41 | AC-8 | A test fails if a board-shaped regex returns; it fired once and caught a real leftover | VERIFIED | `test_no_board_shaped_regex_survives_in_the_generators` |
| E42 | **AC-11 / F6** | **The status reader enforces the whole closed schema** — required keys, vocabulary, conditional keys *both ways*, stamps, directory↔id agreement | VERIFIED | 12 tests; `gen_index.validate_status` |
| E43 | **AC-11 / F7** | `gen_docs.py` resolves both grammars, every configured container, year nesting and phase paths; the year is no longer read as a task | VERIFIED | 10 tests in `test_gen_docs.py` |
| E44 | **AC-11 / F8** | **11 task state files tracked, not 10.** TFW-54's authority now names a committed artifact | VERIFIED | inline, below |
| E45 | **AC-11 / F9** | Accounting preserved and re-runnable after removal; repository, date and container hardcodes gone from the script | VERIFIED | `migrate_board.py` — `--board-rev`, `--now`, container-derived paths |
| E46 | **AC-11 / F10** | Template config reads `2.0.0`; `initial_seq` and `{PREFIX}-1` gone from six files and every propagated copy | VERIFIED | inline, below |
| E47 | **AC-11 / F13** | Coverage of every named failure, **and** of the production path itself: identity with `team/` absent, empty, agent-only and human, driven through `gen_index.py --validate`. Plus clock-read provenance, midnight, provider actors, control characters as a class, and canonical naming. Suite 68 → **220** | VERIFIED | `measurement_log.txt` §1 |
| E48 | **AC-11 / F14** | Per-commit file lists are **persisted**, not asserted, and the table now runs to `afd24f5` — the product commit these numbers describe. Every executor commit after the reverted error names only this phase's paths | VERIFIED | `measurement_log.txt` §8 |
| E49 | **AC-11 / F5** | Transferred to TFW-61 by R3 — a file-sync concern | N/A | TS §AC-11 |
| E50 | **AC-12** | Two phases under two owners write two different files; the task's own file is untouched | VERIFIED | `fixture_transcript.txt` §AC-12 |
| E51 | **AC-12** | The task-level lifecycle never summarizes phase state; no phase name leaks into the task file | VERIFIED | `fixture_transcript.txt` §AC-12 |
| E52 | **AC-12** | The index renders phase rows beneath their task, in order | VERIFIED | `fixture_transcript.txt` §AC-12; `workspace/00-INDEX.md` |
| E53 | **AC-12** | `created`/`updated` carry second resolution; a day-resolution stamp is a schema breach | VERIFIED | `fixture_transcript.txt` §AC-12; `test_stamps_must_be_second_resolution_or_unrecorded` |
| E54 | **AC-12** | **Migration created phase state for no legacy task** — 1 phase file in the whole corpus, TFW-60's own | VERIFIED | `census.md` §4; `fixture_transcript.txt` §AC-12 |
| E55 | **AC-12** | One lifecycle id added — `🧩 PHASES` — and propagated through config, conventions, glossary, template, quickstart and every adapter copy | VERIFIED | inline, below |
| E56 | AC-9 | A full lifecycle driven with ordinary file writes; with no index present the task stayed readable and reached `DONE` | VERIFIED | `fixture_transcript.txt` §AC-9 |
| E57 | AC-9 | Executable code is exactly `gen_docs.py`, `gen_index.py`, `migrate_board.py` | VERIFIED | `fixture_transcript.txt` §AC-9 |
| E58 | AC-10 | `VERSION` `2.0.0`; CHANGELOG states the breaking change, the migration path and the container as one setting | VERIFIED | `.tfw/CHANGELOG.md` |
| E59 | AC-10 | TD-81 and TD-177 retired by the code change and the reintroduction test; the registry edit is `/tfw-docs`' under D37 | VERIFIED | RF §6 |

### Inline output

Every command below was run against `afd24f5`. Full transcript:
[`measurement_log.txt`](measurement_log.txt).

**Identity fails closed — the production path, not an injected set**

```
gen_index.py --validate over a scratch project, team/ varied:
  team/ ABSENT              -> exit 1  REFUSED
  team/ EMPTY               -> exit 1  REFUSED
  team/ with an AGENT only  -> exit 1  REFUSED   accountability is not a tool
  team/ with a HUMAN        -> exit 0  accepted
```

The defect was one expression: `actors = team_handles(root) or None`. An empty `team/`
became `None`, and both checks were guarded by `is not None` — so *nobody declared* meant
*everybody passes*, and the rule was unenforced in exactly the case it exists for. The
earlier tests passed because they called the validator directly with a non-empty set: the
one path on which the defect cannot appear.

**Naming — `{ID}` now has one meaning**

```
before:  {container}/{YYYY}/{ID}__tfw_init/
         -> 20260827-054300__tfw_init__tfw_init      doubled slug, rejected by the contract

after:   {container}/{YYYY}/{ID}/
         -> workspace/2026/20260827-054300__tfw_init/
         -> parse_identifier -> ('clock', '20260827-054300__tfw_init')     LEGAL
```

Detectors over the 43-file shipped canonical surface: **0** bare identifiers used as names,
**0** doubled slugs, **0** actorless event examples. Each detector is proven to fire on a
known-bad string before its passing result is believed — and that self-check earned its
keep: it caught the actorless pattern wrongly flagging a *correct* three-segment name,
because `[a-z_]+` had swallowed the actor.

**Control characters**

```
files scanned : 927
control chars : 0
```

The scan is Python, not a shell pipeline: `grep -P` aborts here with a locale error and
**exits without output**, which is indistinguishable from a clean result.

**Migration, re-read at the pin**

```
$ git show b094943:README.md | awk '/^## Task Board/,0' | grep -c '^|'
63                                       61 data rows + header + separator

$ git show afd24f5:tasks/BOARD-SNAPSHOT.md | grep 'Rows captured'
| Rows captured | 61 |

$ git show afd24f5:tasks/BOARD-SNAPSHOT.md | grep -oE 'TFW-[0-9]+' | sort -u | wc -l
61                                       distinct identifiers
```

**61 = 61.** Three different counts of that same file are all correct and answer different
questions — 122 lines contain `TFW-`, 678 occurrences, 61 distinct identifiers. AC-6 closes
on the third.

**Corpus integrity, pinned range**

```
$ git diff --name-status 80d6a16 afd24f5 -- tasks/ | awk '{print $1}' | sort | uniq -c
     48 A
      4 M
```

All four modifications are coordinator artifacts of live tasks — two proposals, the master
HL, and this TS — each attributed to its commit in the log. The migration changed no
pre-existing task artifact.

**Gates**

```
$ python -m pytest docs/scripts/ -q
220 passed, 1 skipped in 124.78s          baseline 68; 152 added across three passes

$ python docs/scripts/gen_index.py --validate
53 tasks validate against the closed schema
```

**Census, and the one file that moved it**

```
EXECUTOR PRODUCT:  new 31   modified 47   total 78
OWNER-APPROVED:    new 30   modified 47   total 77
DELTA:             +1
```

The one file is `journal/20260827-043340__handoff__saubakirov.md` — the actual-clock handoff
event that review revision 2 item 6 **required**. Review revision 3 said not to return for a
budget ruling *"unless the count or scope moves again"*. It moved, by one, because a review
asked for a file, and it is raised here rather than absorbed.

Two further journal events in the range were written by the reviewer (`via: codex`) and the
coordinator during revision 3; both land in `5872d2f` under a coordinator attribution and
are not executor product.

## Verdict

**Evidence verdict: 56/59 VERIFIED, 1 DEFERRED, 0 BLOCKED, 2 N/A.**

- **DEFERRED (1)** — E23, non-specialist readability. Blocker named: no such participant
  exists in a transport-independent fixture; the observation is TFW-61's under S43.
- **N/A (2)** — E39, the equal-depth clause deleted by R3; E49, F5 transferred to TFW-61.

**What this evidence does not support**, stated so nobody has to infer it:

1. Concurrency was shown between two threads and two processes on **one machine**.
   Cross-machine and cross-provider behaviour is neither tested nor claimed.
2. Determinism holds **given identical inputs**. `tasks/TFW-36__content_marketing_blog_series/`
   carries a `.gitignore` containing `*`, so a fresh clone sees a different input set than a
   working tree. Its state file is force-added so all eleven ship, but the folder's other
   contents remain invisible to Git. Pre-existing; recorded as TD-183.
3. Second-resolution stamps are **accurate where Git recorded them** and **declared** where
   the legacy source held only a day. A migrated `created` of `20260819-000000` means "this
   day, time unknown" — it is not second-accurate history, and must not be read as such.

## Attachments

| File | Description |
|------|-------------|
| `measurement_log.txt` | **Every figure in this pass, measured once at `afd24f5`** — the pinned snapshot, the identity gate, the census, naming, control characters, migration and staging |
| `census.md` | The corrective-pass baseline, the budget position, and the destroyed-trace root cause |
| `corrective_plan.md` | The plan against TS §6, with each of the 15 findings and its disposition |
| `migration_accounting.md` | 61 rows against 53 directories, every identifier named, `Unaccounted: 0` |
| `fixture_transcript.txt` | 43 checks across AC-1, 2, 3, 4, 5, 9 and 12, all passing |
| `ceiling_measurement.txt` | The two populations behind the 120-code-point ceiling and the three entries it refuses |

> The fixture harness that produced `fixture_transcript.txt` does **not** ship. AC-9 limits
> release code to index generation and migration accounting. Where a rule is enforced by
> shipped code the harness calls that code rather than reimplementing it — the review's F4
> finding was precisely that a rule living only in a harness is not a shipped rule.

---

*EV — TFW-60 / Phase A: Task State & Coordination | 2026-08-26*
