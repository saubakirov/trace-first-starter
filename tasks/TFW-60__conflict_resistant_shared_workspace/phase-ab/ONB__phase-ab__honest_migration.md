# ONB — TFW-60 / Phase AB: Honest Migration

> **Date**: 2026-08-29
> **Author**: Codex (Executor), `on_behalf_of: saubakirov`, `via: codex`
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-60](../HL-TFW-60__conflict_resistant_shared_workspace.md)
> **Phase HL**: [HL Phase AB](HL__phase-ab__honest_migration.md)
> **TS**: [TS Phase AB](TS__phase-ab__honest_migration.md)
> **Origin read**: [third field report](../FIELD-REPORT__TFW-60__third_external_update.md), all seven defect groups and §7
> **Predecessor read**: [Phase AA RF](../phase-aa/RF__phase-aa__portable_delivery.md) and [REVIEW revision 3](../phase-aa/REVIEW__phase-aa__portable_delivery__rev3.md)
> **Measured at**: source commit `f239644`, 2026-08-29. The working tree contains unrelated TFW-55 research changes; they are excluded from this phase and from every commit.

---

## 1. Understanding

Phase AB must make migration claims mechanically true. The identifier layer recognizes exactly three
whole-string forms, refuses everything else as malformed, and preserves every previously recognized
identifier. `migrate_board.py` must classify every board row and directory exactly once, stop before any
write when two rows resolve to one identifier or a computed invariant fails, and preserve identifier
characters while removing Markdown presentation. The same grammar must be issued by planning, carried by
configuration and templates, resolved by the documentation compiler, and described consistently by the
release surface. Existing task directories, state schemas, journal schemas, lifecycle values and index
format remain unchanged.

The concrete `HD-30b` collapse has been traced. It does **not** occur in `gen_index.parse_identifier()`:
`migrate_board.parse_board()` uses the unanchored search `re.search(r"[A-Z][A-Z0-9]*-\d+", cells[0])`.
That search extracts `HD-30` from the prefix of `HD-30b` before the shared parser sees the value. The
manifest then loses row identity inside a dictionary keyed by the shortened identifier and prints an
accounting guarantee that was never evaluated.

The implementation cannot start against the present TS. Its affected-file boundary omits ten files that
would continue issuing, documenting or resolving the retired current grammar, and AC-8 assigns release
artifacts and a tag to the Executor despite the Role Lock assigning those acts to `/tfw-release`. The
literal tag-order failure condition is also impossible for a normal tag that points to the release commit.
These are scope and authority defects, so the Executor must report them here and stop.

## 2. Entry Points

### Measured code path and baseline

| Path / corpus | Observation |
|---|---|
| `.tfw/scripts/gen_index.py` | `CLOCK_ID` and `LEGACY_ID` are anchored; `parse_identifier()` currently recognizes the two existing forms whole. `sort_key()` and unresolved diagnostics know only those forms |
| `.tfw/scripts/migrate_board.py` | `parse_board():130` performs the prefix search that collapses `HD-30b`; `_plain()` removes `_`; reconciliation is keyed by normalized identifier; the manifest prints an uncomputed guarantee; `written` derives identifiers with `split("__")[0]` |
| `.tfw/scripts/test_gen_index.py` · `test_migrate_board.py` | Three repository-state tests coexist with framework tests. They can be separated by the existing `repository` test-name convention without adding a test-configuration file |
| `docs/scripts/gen_docs.py` · `test_gen_docs.py` | The reference resolver accepts only `{task_prefix}-N`; a new task's `RF {ID}`, `HL-{ID}` and phase references will remain plain text unless this group joins scope |
| Targeted baseline | `python -m pytest .tfw/scripts/test_gen_index.py .tfw/scripts/test_migrate_board.py docs/scripts/test_gen_docs.py -q` → **224 passed, 1 skipped** in 8.34 s |
| `.tfw/workflows/update.md` | **1,380 words** before edit; AC-6 requires fewer than 1,200 after adding three rules |

### Grammar carriers found outside TS §4

| Omitted path | Why it must change if AC-3 remains in this phase |
|---|---|
| `.tfw/templates/project_config.yaml` | New projects copy it during init; it still sets `id_format: "{YYYYMMDD}-{HHMMSS}__{slug}"` and calls `task_prefix` legacy-only |
| `.tfw/templates/HL.md` | The canonical HL header has no abbreviation field, although AC-3 requires the approved abbreviation in that header |
| `.tfw/templates/status.md` | Its `id` and `authority` examples still issue the dirty-era identifier |
| `.tfw/glossary.md` | `Task Naming` declares the dirty-era form current and only one legacy form |
| `.tfw/workflows/init.md` | The first task is explicitly created as `YYYYMMDD-HHMMSS__tfw_init`; changing only `plan.md` leaves init issuing the old grammar |
| `.tfw/compilable_contract.md` | It says `task_prefix` recognizes legacy identifiers only and defines reference patterns only for `PREFIX-N` |
| `docs/scripts/gen_docs.py` | Its artifact, phase, HL and bare-task regexes accept only `task_prefix-N`; the new ID cannot participate in D43's reference cascade |
| `docs/scripts/test_gen_docs.py` | The omitted compiler behavior needs regression coverage |
| `.claude/commands/tfw-init.md` · `.agent/workflows/tfw-init.md` | Byte-identical copies of the newly affected canonical init workflow |

`KNOWLEDGE.md` D68 and §3 Legacy also declare `YYYYMMDD-HHMMSS__slug` current and describe only a
dual-grammar reader. They must become a post-review `/tfw-docs` input, not an Executor edit: D37 and the
Role Lock reserve `KNOWLEDGE.md` for that workflow.

### Census before any implementation edit

| Measure | Present TS | Complete AC-3 surface | Limit |
|---|---:|---:|---:|
| Physically modified implementation/release paths | 15 | **25** | 30 |
| Budget-counted modified paths | 11 | **19** | 30 |
| New implementation files | 0 | **0** | 15 |
| Planned implementation LOC | not yet measured | below 3,000, to be measured after the TS boundary is approved | 3,000 |

The six byte-identical Claude Code/Antigravity copies of `plan.md`, `update.md` and the newly implicated
`init.md` are excluded from the budget under S32 but included in the physical-path count. Codex skills are
thin routers to canonical workflows under D54; their bytes contain no grammar and require verification,
not modification. ONB, RF and evidence files are work artifacts excluded under S46.

### Four pinned corpora available for AC-1

| Corpus | Pinned commit | Live worktree | Execution rule |
|---|---|---|---|
| steps-framework | `f239644` | unrelated TFW-55 changes | read the commit, never the dirty files |
| KZ-IT-telegram-list | `97dd429` | two unrelated local paths changed/untracked | read the commit at `D:/projects/KZ-IT-telegram-list` |
| innoforce-ai-first | `58329e7` | clean at a later commit | read the pinned update commit at `D:/projects/research/innoforce-ai-first` |
| helpdesk | `aec5f2d` | active HD-31 work is dirty | read the committed update at `D:/projects/research/helpdesk`; never write the consumer |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|---|---|
| 1 | **May the coordinator revise TS §4 so the complete grammar surface is in scope?** Ten required paths are absent: `.tfw/templates/{project_config.yaml,HL.md,status.md}`, `.tfw/glossary.md`, `.tfw/workflows/init.md`, `.tfw/compilable_contract.md`, `docs/scripts/{gen_docs.py,test_gen_docs.py}`, and the two full init adapter copies. **Option (a), recommended:** add them; the physical count becomes 25 and the budget count 19, both within limits. **Option (b):** narrow AC-3 to the parser and `plan.md`; init, new-project configuration, templates and compiled references then knowingly contradict the new current grammar. **Option (c):** remove AC-3 from Phase AB and plan the grammar as another phase; this contradicts amendment A5's owner ruling unless the frozen contract is amended again | **(a) — add all ten. Approved.** You did exactly what TS §4 asked: it says the estimate is *"the coordinator's and is not authority"* and that the executor measures before editing. The mechanism worked; my scoping was short by ten paths.

**(b) is the option I want to name as unacceptable rather than merely reject.** It would ship a framework where `init.md` creates a project's *first* task in the old grammar and `plan.md` creates its second in the new one. A new project would meet the contradiction on day one — and a framework contradicting itself about its own identifier is the exact class Phase AB exists to end. Choosing it would be committing this phase's subject inside this phase.

`gen_docs.py` is in scope for a functional reason, not tidiness: its resolver accepts only `PREFIX-N`, so a new-grammar task cannot participate in D43's citation cascade at all. `KNOWLEDGE.md` D68 stays out — D37 reserves it for `/tfw-docs`; record both stale statements in RF Observations.

Physical 25, budget 19, both inside `30 / 15`. **The limits do not move**: no overrun is authorized for this phase, and a further group returns to me before you act on it. |
| 2 | **Who performs AC-8, and what does “before the tag exists” mean?** `conventions.md` §15 assigns `VERSION` and `CHANGELOG.md` to `/tfw-release`, and `release.md` assigns tags to the Coordinator/Maintainer; the Executor is permitted ONB, RF and code. In addition, a tag that points to the release commit cannot pre-exist the commit whose files name that version. **Option (a), recommended:** revise AC-8 so the Executor prepares code and an RF, then `/tfw-release` after review writes `VERSION`/`CHANGELOG`, creates and verifies `v2.0.0-dirty.4`, and publishes no fetch instruction before the tag exists; narrow DoF 7 to that observable publication boundary. **Option (b):** add an explicit owner-approved Role Lock exception allowing this Executor to write the two release files and create an unreviewed tag, while also defining a realizable order. **Option (c):** tag the current `.3` commit before implementation and later move the tag; this makes the tag false and mutable and is not recommended | **(a) — follow §15, and it corrects Phase AA rather than diverging from it.**

You are right and I checked: `conventions.md`:675 assigns `release.md` to the Coordinator with *"version bump → CHANGELOG → tag"* — all three. In Phase AA I ruled that the executor writes `VERSION` and `CHANGELOG`, keeping only the tag back. That ruling was wrong against §15, and rule 17 is why: a delegated mandate *"does not create what an agent may do."* Propagating my own error into a second phase to look consistent is not a reason.

So: you deliver code, tests, fixtures and the RF. `/tfw-release` after review performs the version bump, the CHANGELOG entry and the tag as one act — which is also the only order in which they can be true at the same time.

**Inconsistency 9 is my error and DoF 7 is rewritten.** A tag can only point at an object that exists, so *"named anywhere before the tag exists"* forbids the only realizable sequence. What I meant is the failure the third report actually hit: its operator read `VERSION` = `.3` and a CHANGELOG saying *"tagged locally"* while `git tag` disagreed. The prohibition belongs at the **publication boundary** — no instruction telling anyone to fetch, clone or archive a reference that does not exist — not on files naming their own version. |
| 3 | **What counts as AC-3's end-to-end created task and abbreviation exchange?** A permanent real task would create state and traces outside Phase AB, while a silent derived abbreviation violates AC-3. **Option (a), recommended:** the owner approves `ABT` here for a disposable Git-backed fixture; this ONB answer is the durable exchange, the fixture runs the real planning creation path in a temporary directory, and evidence records its path/index before the directory is discarded. **Option (b):** name and authorize a permanent real task, including its title, goal and abbreviation; that is a separate project mutation and must be put explicitly in scope. **Option (c):** use only a unit test with a hard-coded abbreviation; cheaper, but it does not satisfy the specified human-approval gate | **(a) — approved, and `ABT` is approved as the abbreviation.** This exchange is the durable record AC-3 asks for.

The owner delegated these answers to me. I am exercising that for `ABT` because the choice has no consequence — a disposable directory, discarded after evidence is captured. **An abbreviation for a real task is never mine and never derived**; it comes from the owner in the planning exchange, which is the whole point of the criterion.

(c) fails because the human gate is exactly what is under test; a hard-coded constant proves the parser, not the protocol. (b) mutates the project to test it.

Evidence records the created path, the index rendering the full title, and the exchange that approved the token — this ONB. |

The `/tfw-handoff` invocation authorizes this onboarding pass. It does not silently approve the scope and
release-boundary changes above. After they are resolved, the coordinator must revise the TS, mark it
approved as Phase AA's TS was, and return the corrected phase to `/tfw-handoff`.

## 3a. Coordinator rulings on §4, §5 and §6

**Recommendations — all six approved.** Two are rulings, not agreements:

- **Rec 2, `via` free-form — accepted as the TD-197 decision.** Your reason is better than mine: no canonical
  provider registry exists, so validating it would confuse declaration with authentication and recreate the
  boundary D59 draws. State it as non-empty provider text at the point `via` is defined, and TD-197 closes.
- **Rec 4, `-k "not repository"` — accepted.** It satisfies AC-5 with the naming convention already in the
  files and adds no configuration. Note in the RF that the framework command and the corpus command are both
  named in the migration guide, since AC-5's last bullet is what a receiving project is *told* to run.

**Risks — acknowledged. Risk 6 is a hole in my spec and is now closed:**

- **Risk 6 — collision on the new grammar.** AC-3 did not say what happens when the same second and the same
  approved abbreviation meet. It says so now, and silent suffixing is forbidden because it would invent the
  fourth grammar DoF already refuses. Two rules, both reusing mechanisms this phase already builds:
  **at creation**, if the whole identifier already exists, refuse and ask for a different abbreviation —
  the timestamp is read from the clock and is never re-composed to dodge a collision;
  **at validation**, two directories resolving to one identifier is the same hard stop AC-1 defines for two
  board rows. Offline peers cannot see each other, so the second rule is the one that actually fires.
- **Risk 1 — directory-side collisions.** Same treatment: `TFW-1__a` and `TFW-1__b` are a hard stop, not a
  silent dictionary overwrite. AC-1's rule is about identifiers, not about which side they came from.
- **Risk 3 — "before any write" includes the manifest.** Correct, and stricter than I wrote. Opening the
  manifest is a write. Every invariant and duplicate gate runs before it is created.
- **Risks 2, 4, 5, 7, 8 approved as you state them.** Risk 5 is a second reason `gen_docs.py` belongs in
  scope: `\b` treats `_` as a word character, so the resolver's boundary strategy cannot take the new
  pattern unchanged.

**Inconsistencies — you are right on all nine. Four are mine:**

- **#1 — the mechanism is traced, and my guess was wrong in the useful direction.** The collapse is the
  unanchored `re.search()` in `parse_board()`, *before* `LEGACY_ID` is consulted — so `LEGACY_ID` never had
  the chance to refuse `HD-30b`, exactly as I suspected but could not locate. Put this in the RF: the defect
  was an unanchored search reaching an identifier before the anchored grammar did.
- **#4, #5, #6** — `init.md`, the templates and the compiled references are Q1, now in scope.
- **#7 — Codex skills: verify, never rewrite.** You are right and the owner's 2026-08-28 ruling does not
  contradict you. That ruling says each adapter's files are byte-identical copies **of their own source**,
  placed where the tool expects them. A Codex skill is a byte-identical copy of a thin router under D54;
  copying a workflow body into it would break the adapter architecture, not honour the ruling. Verify
  identity, change nothing. My TS §4 line was wrong.
- **#8, #9** — Q2.

**TD-199 closes.** `f239644` gave the R4 pass the RF it shipped without — revision 3, §11. The waiver
recorded at Phase AA's closure stands as history; the gap it named is gone.

## 4. Recommendations (suggestions, not blocking)

1. **One parser, named results.** Keep all three anchored forms in `gen_index.py` and have migration and
   documentation consumers call the dispatcher. Do not let each consumer grow a fourth extraction regex.
2. **Choose free-form `via`.** State that `via` is a non-empty provider/tool string, not a closed
   vocabulary. No canonical provider registry exists; validation would confuse declaration with
   authentication and recreate the D59 boundary. Record this as the TD-197 decision in RF.
3. **Make the helpdesk fixture committed test data in code.** A named fixture constant in
   `test_migrate_board.py` is committed, reviewable and needs no new file. Capture the failing baseline
   before editing and the passing result after editing as separate evidence attachments.
4. **Separate framework and corpus tests with the existing names.** Use `-k "not repository"` for the
   framework command and `-k repository` for corpus checks. This meets AC-5 without introducing an
   unlisted `pytest.ini`/`conftest.py` group.
5. **Run all corpus comparisons from pinned commits and write only into temporary roots.** The three
   external live worktrees contain owner work. Their paths are evidence sources, not implementation
   targets.
6. **Leave D68 to `/tfw-docs`.** Record both stale statements in RF Observations so the knowledge owner
   can supersede them after review without breaking D37.

## 5. Risks Found (edge cases, potential issues not in TS)

1. Two legacy directories such as `TFW-1__a` and `TFW-1__b` normalize to the same identifier. The current
   directory dictionary silently overwrites one even if board rows are unique. Exact accounting should
   reject directory-side collisions too, or explicitly prove why they cannot enter the corpus.
2. `written = path.parent.name.split("__")[0]` loses part of dirty-era identifiers and cannot represent the
   new grammar. A post-write check based on it can pass or fail for the wrong entity unless it uses the
   same dispatcher.
3. A validation performed after `--manifest OUT` is opened already violates “before any write,” even if
   no `status.md` is written. Every invariant and duplicate gate must run before manifest creation.
4. Markdown link labels, strike-through rows and plain-text IDs enter `parse_board()` through different
   presentation shapes. The parser must retain the original row text for diagnostics while classifying a
   normalized candidate exactly once.
5. The new identifier contains underscores, while Python regex `\b` treats underscore as a word
   character. The documentation resolver's current word-boundary strategy cannot simply substitute the
   new pattern; tests need adjacent punctuation, section suffixes and phase suffixes.
6. The new form has no slug/full title in its path. Same-second tasks with the same approved abbreviation
   collide. The existing bounded retry is no longer sufficient if the identifier must keep the original
   timestamp. The corrected TS should either define refusal on collision or define how a new owner-approved
   abbreviation is obtained; silent suffixing would create a fourth grammar.
7. A local release tag on unreviewed work asserts a release outcome before REVIEW. Even an explicit
   Executor exception should not erase that sequencing risk.
8. The source and two consumer worktrees are dirty. Tests against live `HEAD` would be irreproducible and
   could accidentally include unrelated work; pinned commits avoid both failures.

## 6. Inconsistencies with Code (spec vs reality)

1. TS says the `HD-30b` mechanism was untraced; the collapse is now traced to the unanchored
   `re.search()` in `migrate_board.parse_board()`, before `LEGACY_ID` is consulted.
2. TS requires every guarantee to be computed. The manifest currently prints “Every row and every
   directory is accounted for exactly once” as prose and derives `unaccounted` from resolution strings,
   not from an independently checked partition.
3. TS requires identifier characters preserved. `_plain()` removes every underscore as if it were
   Markdown markup, including the underscores in `normalize_text()` and the new identifier grammar.
4. TS §4 lists `plan.md` as the issuing workflow. `init.md` independently issues the first task and still
   hard-codes the old form.
5. TS requires the HL header to record the abbreviation, but the canonical `HL.md` template has no field
   for it; the `status.md` and project-config templates also teach the old form.
6. TS requires one current grammar across the framework, but `glossary.md`, `compilable_contract.md`,
   `gen_docs.py` and D68 still define the dirty-era grammar as current. D68 cannot be changed by this role.
7. TS lists `tfw-plan`/`tfw-update` under `.agents/skills/` as adapter copies. Codex skills are deliberate
   thin routers under D54 and contain no workflow body; copying canonical Markdown into them would violate
   the adapter architecture. They should be verified byte-identical to their adapter sources and otherwise
   remain unchanged.
8. TS assigns `VERSION`, `CHANGELOG.md` and a tag to the phase Executor. The Role Lock assigns the first
   two and the tag to the release Coordinator/Maintainer.
9. TS DoF forbids naming `.4` anywhere before its tag exists. A normal annotated or lightweight tag can
   point only to an existing Git object, so release files in the target commit necessarily exist before
   the tag reference does.

## 7. Knowledge Citations

> Master HL §7.2 contains 29 citations. All 29 source items were read. Items governing Phase A's carrier
> or future transport are marked N/A rather than imported into this phase.

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|---|---|---|---|
| 1 | PV 0 — `README.md` opening and § How It Works | ✅ | **Applied** | Honest whole parsing and computed claims preserve a checkpoint another participant can inspect without reconstructing the tool's hidden guess |
| 2 | PV 0 — `.tfw/README.md` NS1 and NS2 | ✅ | **Applied** | The phase protects purposeful, inspectable continuation; refusing malformed input is selected Trace, not fabricated continuity |
| 3 | PV 1 — Structural Enforcement | ✅ | **Applied** | Duplicate and invariant failures must be executable pre-write gates, not reassuring manifest prose |
| 4 | PV 1 — one authoritative owner per truth type | ✅ | **Applied** | Migration reports and exits; it does not become a second authority over existing task state. D37 also keeps `KNOWLEDGE.md` outside this role |
| 5 | PV 1 — Portability and Success Criteria | ✅ | **Applied** | Grammar carriers and reference compilation must agree in a receiving project, not only in this repository |
| 6 | PV 2 — `philosophy.md` F4 | ✅ | **Applied** | Computed partitions, hard stops and end-to-end creation are structural gates |
| 7 | PV 2 — F11 | ✅ | **Applied** | One shared identifier dispatcher avoids parallel parser entities and a fourth grammar |
| 8 | PV 2 — F27 | ✅ | **Applied** | The manifest names each arithmetic invariant and its operands so progress and failure are inspectable |
| 9 | PV 2 — F34 | ✅ | **Applied** | The vague “create a task end to end” gate is converted into Question 3 with concrete fixture choices |
| 10 | PV 2 — F38 | ✅ | **Applied** | Three blocking decisions are batched in one onboarding gate; none is discovered piecemeal during execution |
| 11 | PV 3 — D31 and D50 | ✅ | **Applied** | Task-local state remains authoritative and no existing path moves; only identifier recognition changes |
| 12 | PV 3 — D37 | ✅ | **Applied** | `KNOWLEDGE.md` is reported for `/tfw-docs`, not edited by the Executor |
| 13 | PV 3 — D43 | ✅ | **Applied** | Finding the legacy-only compiler regex expands the required scope: new identifiers must remain resolvable in the citation cascade |
| 14 | PV 3 — D55 and D59 | ✅ | **Applied** | The ONB commit uses declared attribution; Recommendation 2 keeps `via` declaration separate from authentication |
| 15 | PV 3 — D65 | ✅ | **Applied** | No existing task directory or trace is renamed, moved or rewritten during parser migration |
| 16 | PV 4 — `conventions.md` §§3–5 | ✅ | **Applied** | Phase authority, three existing/current grammar carriers, task locality and role boundaries define the stop |
| 17 | PV 4 — `conventions.md` §§13–14 | ✅ | **Applied** | Malformed and duplicate inputs remain visible; no trace or unmatched row is silently dropped |
| 18 | PV 5 — `convention.md` F22 | ✅ | **Applied** | The retired board is migration input/process history, not new product authority |
| 19 | PV 6 — `process.md` F7 and F30 | ✅ | **Applied** | Update rules and manifest arithmetic must be durable and enforceable, not reconstructed from a session |
| 20 | PV 7 — `risk.md` F1 | ✅ | **Applied** | External corpora are read at pinned commits and never staged or modified from this shared worktree |
| 21 | PV 7 — `constraint.md` F1 and F3 | ✅ | **Applied** | No personal state enters the tree; template changes are limited to fields required by the new grammar |
| 22 | RES 1 — [YAML 1.2.2](https://yaml.org/spec/1.2.2/) | ✅ | **N/A** | Phase AB changes identifier values, not the closed `status.md` mapping schema or YAML parser |
| 23 | RES 1 — [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259) | ✅ | **N/A** | JSONL was not selected and no journal carrier changes here |
| 24 | RES 1 — [Git](https://git-scm.com/docs/git), [git-rev-parse](https://git-scm.com/docs/git-rev-parse), [git-add](https://git-scm.com/docs/git-add) | ✅ | **Applied** | Pinned commit objects isolate dirty corpora; Git object/ref ordering exposes the literal AC-8 contradiction |
| 25 | RES 1 — [Google Drive troubleshooting](https://support.google.com/drive/answer/2565956?hl=en) | ✅ | **N/A** | Transport mode is TFW-61; this phase makes no synchronization guarantee |
| 26 | RES 1 — [OneDrive sync troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/sharepoint/sync/troubleshoot-sync-issues) | ✅ | **N/A** | Same boundary as item 25 |
| 27 | RES 1 — [Dropbox conflicted copies](https://help.dropbox.com/organize/conflicted-copy) | ✅ | **N/A** | Same boundary as item 25 |
| 28 | RES 1 — [gsd-pi](https://github.com/open-gsd/gsd-pi), [BMAD](https://github.com/bmad-code-org/BMAD-METHOD), [Hermes](https://github.com/NousResearch/hermes-agent), [Spec Kit](https://github.com/github/spec-kit), [OpenSpec](https://github.com/Fission-AI/OpenSpec) | ✅ | **N/A** | Phase AB repairs the selected local file contract; it does not import another system's coordination or storage mechanism |
| 29 | RES 2 — [git-interpret-trailers](https://git-scm.com/docs/git-interpret-trailers), [git-log](https://git-scm.com/docs/git-log), [git-merge-base](https://git-scm.com/docs/git-merge-base) | ✅ | **Applied in part** | Reachable pinned commits support reproducible corpus evidence; Phase A's landing-completion derivation itself is unchanged |

### New items the coordinator did not cite

| # | Source | Item | Why it belongs |
|---|---|---|---|
| N1 | `.tfw/conventions.md` §15 · `.tfw/workflows/release.md` | Release artifacts and tags belong to the Coordinator/Maintainer, not the Executor | This directly conflicts with AC-8 and determines Question 2 |
| N2 | `.tfw/glossary.md` `Task Naming` · `.tfw/compilable_contract.md` §2 | Both are live framework authorities/consumers for identifiers and both still declare only the old current grammar | These omissions determine Question 1 and the true affected-file census |
| N3 | `.tfw/conventions.md` §10.3 | Framework templates and compilation contract are upstream-owned release payload; project config is a framework/project merge | Explains why changing only the live project config does not deliver AC-3 to a new or updated project |

---

*ONB — TFW-60 / Phase AB: Honest Migration | 2026-08-29*
