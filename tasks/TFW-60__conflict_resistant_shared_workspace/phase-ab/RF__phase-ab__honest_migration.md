# RF — TFW-60 / Phase AB: Honest Migration

> **Date**: 2026-08-29
> **Author**: saubakirov
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-60](../HL-TFW-60__conflict_resistant_shared_workspace.md)
> **TS**: [TS Phase AB](TS__phase-ab__honest_migration.md)

---

## 1. What Was Done

### New Files

| File | Description |
|------|-------------|
| `journal/20260829-165540__transition__d26e.md` | Durable Executor transition from approved onboarding into RF execution |
| `evidence/parser_and_prose_before_after.txt` | Pre-change cause and post-change HELPDESK_SHAPE classification/prose output |
| `evidence/runtime_guarantees.txt` | Passing arithmetic plus a deliberately failed invariant naming `TFW-9` |
| `evidence/current_id_end_to_end.txt` | Disposable Git-backed `ABT` task and its rendered index row |
| `evidence/four_corpora_compatibility.txt` | Identifier-by-identifier comparison at four pinned commits |
| `evidence/verification_gates.txt` | Configured gates, split test runs, tag refusal, adapter hashes, scope measurement and seven dispositions |
| `evidence/EV__phase-ab__honest_migration.md` | Acceptance evidence register and verdict |

### Modified Files

| File | Changes |
|------|---------|
| `.tfw/scripts/gen_index.py` | Added the current grammar, whole-input dispatch, directory collision refusal, truthful malformed reporting, ReaderError key recovery, free-form `via` validation and retired-key checks |
| `.tfw/scripts/migrate_board.py` | Replaced prefix extraction with shared whole parsing; added duplicate refusal, exact partitions, computed pre-write guarantees, faithful prose normalization and manifest disclosure |
| `.tfw/scripts/test_gen_index.py`, `.tfw/scripts/test_migrate_board.py` | Added current/dirty/legacy, malformed, collision, guarantee, prose, `via`, ReaderError and retired-key regressions, including the committed HELPDESK_SHAPE fixture |
| `.tfw/conventions.md`, `.tfw/glossary.md`, `.tfw/project_config.yaml` | Made `PREFIX_stamp_ABBR` the issued grammar, preserved both historical forms, defined collision refusal and declared `via` free-form |
| `.tfw/workflows/plan.md`, `.tfw/workflows/init.md` | Require owner abbreviation approval before creation, one real clock read, exact-path refusal and session naming with the full new ID |
| `.tfw/workflows/update.md` | Reduced to 852 words; added source/tag pins and recheck, installed-baseline provenance handling, reachable retired-term checks and installed-adapter-only sync |
| `.tfw/migrations/2.0.0.md` | Named all three grammars, removed the staging claim, made malformed inputs non-actionable and documented split test commands |
| `.tfw/templates/project_config.yaml`, `.tfw/templates/HL.md`, `.tfw/templates/status.md` | Updated issuance examples, added the HL abbreviation field and preserved project-owned scope budgets |
| `.tfw/compilable_contract.md`, `docs/scripts/gen_docs.py`, `docs/scripts/test_gen_docs.py` | Extended artifact, phase, HL and bare-task references across all three grammars with underscore-safe boundaries and exact normalized directory matching |
| `.claude/commands/tfw-{plan,update,init}.md`, `.agent/workflows/tfw-{plan,update,init}.md` | Re-synced six approved byte-identical workflow copies |
| `status.md` | Recorded the phase's RF lifecycle and completion timestamp |

## 2. Key Decisions

1. One shared dispatcher classifies an entire candidate as `current`, `clock`, `legacy`, or malformed. Board-specific prefix extraction was the mechanism that shortened `HD-30b` to `HD-30`; removing it fixes the cause rather than widening the legacy grammar.
2. Migration guarantees are executable partitions, not prose assertions. The same function gates planning and manifest rendering before any output path is opened, and its arithmetic is printed verbatim in the manifest.
3. New identifiers use `PREFIX_YYYYMMDD-HHMMSS_ABBR`. The owner approves `ABBR` in the planning exchange; on collision the workflow asks for a different abbreviation and neither recomputes the stamp nor invents a suffix.
4. Historical paths are immutable compatibility inputs. Legacy and `2.0.0-dirty` identifiers remain supported forever; validation stops on normalized duplicates instead of choosing a path silently.
5. `via` is descriptive provenance, not authentication. It is absent for a hand edit or a non-empty free-form provider/tool string; no provider registry is invented. This resolves TD-197's decision in favor of the approved free-form option.
6. Release mutation remains atomic and Coordinator-owned. VERSION, CHANGELOG and tag work is deliberately deferred to `/tfw-release` after review, as approved in ONB answer 2 and TS revision 2.

### What an existing `2.0.0-dirty` project must know

- Do not rename `YYYYMMDD-HHMMSS__slug` directories. Every consumer continues to read them; only newly created tasks use `PREFIX_stamp_ABBR`.
- Planning now asks the owner to approve an uppercase alphanumeric abbreviation before creation. Merge the framework `id_format`, current prefix semantics and retired-key removals while preserving project-owned `task_containers`, `build.*` and `scope_budgets`.
- Re-run migration from a committed board. Run `-k "not repository"` during migration and `-k repository` after the board is removed and the derived index exists.
- A malformed board identifier or directory is reported without state or inferred reason. Duplicate normalized rows or directories stop before the manifest is written.
- Update from a pinned source commit whose target tag exists. Use `installed_from` to distinguish provenance drift from customization and repeat the source/tag checks after payload writes.
- Run `python .tfw/scripts/gen_index.py --check project`; remove `initial_seq`, `id_max_retries`, and `review.default_mode` when reported.
- The eventual `2.0.0` version marker, CHANGELOG entry and verified tag are produced together by `/tfw-release` after an approving review.

## 3. Acceptance Criteria

- [x] **AC-1:** exact three-form parsing, visible malformed inputs, duplicate row/directory refusal and four pinned-corpus compatibility are verified.
- [x] **AC-2:** every row, parsed directory and malformed directory participates in a computed exact-once guarantee; deliberate imbalance stops and names `TFW-9`.
- [x] **AC-3:** canon, configuration, planning/init workflows, templates and documentation resolver issue and resolve the approved current grammar; the disposable `ABT` task rendered its full title in the index.
- [x] **AC-4:** Markdown presentation is removed while `normalize_text()` and `working_days` remain intact.
- [x] **AC-5:** framework and repository-state test groups are independently runnable and documented in migration order.
- [x] **AC-6:** source/tag quiescence, provenance drift, reachable retired-vocabulary checking and the 1200-word ceiling are satisfied.
- [x] **AC-7:** canon and validator agree on optional, non-empty, free-form `via`; TD-197's implementation decision is closed in this RF.
- [x] **AC-8 executor:** all seven third-report §7 items are fixed or filed with exact scope reasons, and dirty-era consumer instructions are recorded above.
- [ ] **AC-8 release:** DEFERRED by approved role sequencing — `/tfw-release` performs VERSION, CHANGELOG and verified tag together after review.

## 4. Verification

- Lint (`python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only`): **PASS — 284 collected**.
- Tests (`python -m pytest .tfw/scripts/ docs/scripts/ -q`): **PASS — 283 passed, 1 skipped**.
- Verify (`python .tfw/scripts/gen_index.py --check tasks`): **PASS — 53 task states valid**.
- Project check (`python .tfw/scripts/gen_index.py --check project`): **PASS — consistent with declared `2.0.0-dirty.3` payload**.
- Migration-only selection: **PASS — 281 passed, 3 deselected**.
- Repository-state selection: **PASS — 2 passed, 1 skipped, 281 deselected**.
- Adapter parity: **PASS — three canonical workflow triplets and 11 Codex skill source/copy pairs byte-identical**.
- Scope: **PASS — 23 physical implementation paths, 17 counted, 0 new implementation files, 1029 counted-line churn**.

## 5. Evidence

> **Cognitive mode:** Observational verification — evidence lives in the EV file, not inline.

See [EV file](evidence/EV__phase-ab__honest_migration.md) for full evidence details.

Evidence verdict: **8/9 VERIFIED, 1 DEFERRED, 0 BLOCKED, 0 N/A**.

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| O1 | `KNOWLEDGE.md` | 102, 162 | naming | D68 and §3 Legacy still call dirty-clock task IDs current (and D68 still calls the event suffix an actor). D37 reserves this index for `/tfw-docs`; update it after review from this RF |
| O2 | `.tfw/templates/team/profile.md` | 12-14, 27-33 | style | The template says profiles cover humans and agents, then says `team/` holds people and agent profiles are unusable. This third-report item was outside the approved Phase AB surface and is filed for a scoped follow-up |
| O3 | `.tfw/adapters/antigravity/tfw-rules.md.template`, `.agent/rules/tfw.md` | 5-7, 5-8 | duplication | Adapter source requires `{version}` substitution while the rendered rule correctly reads `.tfw/VERSION`. Both paths were outside the approved surface; align source/rendering in a scoped adapter update |
| O4 | `.tfw/templates/journal/event.md` | 49, 70 | naming | The event template still describes `via` as a provider family. The canonical convention and validator now deliberately accept free-form provider/tool text; update this omitted carrier in a scoped follow-up |

## 7. Fact Candidates

No fact candidates. The execution introduced no new human-only project facts beyond the approved ONB decisions already preserved in the task trace.

## 8. Strategic Insights (Execution)

No strategic insights. No new domain correction or strategic context was supplied during execution.

## 9. Diagrams

```text
board rows + task directories
             |
             v
 whole-candidate dispatcher
 current | dirty-clock | legacy | malformed
             |
             v
 duplicate normalized-ID gate --------> REFUSE before any output
             |
             v
 exact reconciliation partitions
 rows: matched / board-only / unresolved / malformed
 dirs: matched / directory-only / row-named malformed / orphan malformed
             |
             v
 computed exact-once guarantees --------> REFUSE with guarantee + identifiers
             |
             v
 manifest (arithmetic + checked/not-checked disclosure)
             |
        --apply only
             v
 new status.md files + BOARD-SNAPSHOT.md
```

---

*RF — TFW-60 / Phase AB: Honest Migration | 2026-08-29*
