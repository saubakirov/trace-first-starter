# REVIEW — TFW-60 / Phase AA: Portable Delivery

> **Date**: 2026-08-28
> **Author**: Claude Code (Reviewer), `actor: saubakirov`, `via: claude`
> **Verdict**: 🔄 **REVISE** — narrow, one round, three items
> **RF**: [RF Phase AA](RF__phase-aa__portable_delivery.md)
> **TS**: [TS Phase AA](TS__phase-aa__portable_delivery.md) at revision 3
> **EV**: [EV Phase AA](evidence/EV__phase-aa__portable_delivery.md)
> **Contract baseline**: master HL at `2123de1` (after amendment A4)
> **Reviewed at**: `440d6fd`. The RF declares its pin at `1079020`; the two later commits touched
> only the RF, the EV and one evidence artifact, and changed no code.
> **Stage files**: [`review/map.md`](review/map.md) · [`review/verify.md`](review/verify.md) · [`review/judge.md`](review/judge.md)

---

## 1. Map

Phase AA moves the four migration/index scripts from `docs/scripts/` into `.tfw/scripts/` with
`git mv`, replaces `parents[2]` depth arithmetic with a marker search, and writes
`.tfw/migrations/2.0.0.md` — the single created file — as a procedure for a project that is not
this repository. Around that move, ten field-report findings close: the board's location and
heading become inputs on the same code path that makes a committed revision the default source;
a directory whose name the identifier grammar rejects is reported as unresolved instead of being
called a backlog idea; the carrier validator names the key it rejected; `update.md` gains the
pristine-tag diff, the `task_containers` decision and a `team/` creation step; three adapter
sources stop routing `/tfw-research` at a file that has never existed.

Under owner revision R3 the phase **subtracts**: two proposed files are withdrawn before
creation, three templates leave the flat namespace for directories mirroring their output, and
`--check` / `--validate` / `--doctor` collapse into one flag with three subjects — deleting the
five-line config comment that existed only because the names had failed.

The phase's declared outcome is reported **unmet on its acceptance half** and handed to the
owner. That is compliance, not shortfall: TS §5 splits AC-13 into a development fixture the
executor closes and acceptance evidence only an operator who is not the author can produce, and
TS §7 makes any other answer a rejection.

## 2. Verify

Ratio 0.42 over 33 claimed files required 14. **A discrepancy escalated verification to 100%** —
all 33 opened or diffed, and the full 49-path change set reconciled against `census.md`.

| # | What was checked | Result | Evidence |
|---|-----------------|--------|----------|
| 1 | Full suite re-run | ✅ **253 passed, 1 skipped**, 254 collected — matches the RF exactly, against the ONB's recorded 220 baseline. Net **+33** | `pytest .tfw/scripts/` → 158+1 in 12 s; `pytest docs/scripts/` → 95 in 249 s |
| 2 | All three `--check` subjects | ✅ exit **0** each — 53 tasks validate; project consistent; index current. Every output names what it did **not** check | commands re-run here |
| 3 | `mkdocs build` | ✅ exit **0**, built in 230.8 s — the gate for `gen_docs.py`'s cross-directory import | verify.md command 13 |
| 4 | AC-1 gate grep | ✅ **11 hits outside `tasks/`, identical to `ac1_gate.txt` line for line**, including `KNOWLEDGE.md:22` named in the AC's own gate text so the RF could not report around it | verify.md command 8 |
| 5 | Root resolution | ✅ marker search, `.upstream` skipped, **refuses rather than guessing**. `parents[2]` survives only in a docstring and two test constants | `gen_index.py:75–100` |
| 6 | Depth defect actually observed | ✅ at three real placements inside a fixture project; `parents[2]` would have been wrong in two, once resolving **outside the project entirely** | `fixture_run.txt`, `fixture_report.md` § F1 |
| 7 | Parser untouched (AC-3) | ✅ **independently re-diffed**: `parse_board` 42 → 47 lines whole-function, exactly two code lines differ — the signature gaining the parameter and the locator using it. Every row-reading line byte-identical | verify.md command 12 |
| 8 | Moves are moves | ✅ `git diff --name-status` records `R063/R069/R075/R065/R100/R100`; `git log --follow` returns 9 / 6 / 3 / 3 / 5. History follows every relocation | verify.md command 11 |
| 9 | Adapter copies | ✅ **22 workflow copies + 11 Codex skills, all byte-identical**; 4 broken `/tfw-research` routes fixed across all three sources; one remaining `research.md` string in the tree is the CHANGELOG describing the fix | verify.md V10, V15 |
| 10 | Never-modify classes | ✅ no file under `tasks/` outside this phase's own artifacts is in the change set; `KNOWLEDGE.md` untouched; 11 provenance comments byte-unchanged | verify.md V16 |
| 11 | `update.md` ceiling | ✅ **1165 words** against 1200, reached by deleting duplication rather than cutting required content | `wc -w` |
| 12 | Evidence artifacts | ✅ **60 items, 60 artifacts resolve, 0 missing.** 1 correctly DEFERRED with a named blocker and named closing artifact; 1 correctly N/A (`git tag -l` confirms no tag was cut) | verify.md Evidence Verification |
| 13 | Knowledge citations | ✅ **33 of 33** (HL §7.2 ×29 + ONB §7 N1–N4) resolve, exist, match meaning and are relevant. **0 hallucinated, 0 irrelevant.** Two application notes are artifacts of the ONB predating TS R3, not defects | verify.md Knowledge Citations |
| 14 | **Discrepancies** | ⚠️ **six**, one Medium and five Low — §4 below | verify.md D1–D6 |

**What could not be verified here:** AC-13 half two, by construction. Acceptance evidence
requires a real external project updated by an operator who is not the author, and no artifact
in this repository can substitute for it. The executor did not claim otherwise.

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | **14 of 15 AC halves met and independently re-verified.** AC-13 half two reported ❌ UNMET and routed to the owner — what TS §5 and §7 require of the executor |
| 2 | Purpose Check + design soundness | **(a) ✅ · (b) ✅** | **(a)** Serves DoD 19 at baseline `2123de1` — *"An external project completes the update … **from the payload alone** … every instruction the release gives names something the receiving project actually has"* — and NS1, *"another authorized person or agent can … continue without rebuilding the original conversation."* **Harm at stake:** without this phase a receiving project is told to run `docs/scripts/migrate_board.py`, a file `/tfw-update` never copies, so continuation means reconstructing the framework's tooling by hand — measured, not predicted, by the first external update. Excess: none (AC-12 is owner-admitted and bounded; the phase is net subtractive). Deferral confession: none (RF §6 items 3, 5, 7 name other homes and ship nothing there). **(b)** HL §7 principle 5 is structurally enforced, not asserted — `test_no_check_subject_writes_anything` byte-compares the whole tree across all three subjects. Principles 4 and 9 hold and were verified |
| 3 | Tech debt documented | ✅ | RF §6: seven observations, each naming file, type and why it was not fixed. None is filler |
| 4 | Style & standards | ⚠️ | Naming, word ceiling and commit attribution all honoured. **Against that, `.tfw/templates/status.md` ships a self-contradiction and a miscount** — §4 items 1 and 2 |
| 5 | Observations collected | ✅ | Quality filter applied; six of seven promoted, one reclassified as a recorded decision |
| 6 | RF completeness (§7-9) | ✅ | §7 seven fact candidates with named human/coordinator sources; §8 three execution-derived insights; §9 three diagrams carrying information the prose does not |
| 7 | Evidence completeness | ✅ | 60 of 60 artifacts exist; every TS Evidence field covered; all statuses valid |
| 8 | Evidence sufficiency | ⚠️ | The strong parts are strong and I re-derived rather than read them — test counts, gate grep, parser diff, depth placements all reproduce. **Four claims are looser than their evidence** (§4 item 3), in a phase whose own DoF names *"a check reported as passing that never ran"* in four forms |
| 9 | Backward compatibility | ✅ | The one deliberate break (`build.verify: --validate → --check tasks`) is taken knowingly with its blast radius stated and named in the CHANGELOG as one of exactly two commands that change. `iter_task_dirs`' return type deliberately unchanged because three callers read it. `mkdocs build` exit 0 proves the import path. Copies verified identical |
| 10 | Safety | ✅ | No secrets or network surface. The destructive surface is bounded in the right direction: migration opens no existing path and never renames; `--check` writes nothing (whole-tree byte comparison); root resolution refuses rather than guessing. The one live-system risk — writing into the owner's real external project — was avoided and recorded read-only (E48). No push, no tag |

**Purpose Check outcome: Aligned ✅.** Reference set checked for internal consistency: the
baseline's Phase AA block, DoD 19, DoF 10 and NS1 all pull the same direction. **No contract
defect.**

## 4. Verdict

**🔄 REVISE** — narrow, one round.

The work is correct, and I want to say that before the finding: fourteen acceptance criteria
hold under independent re-derivation, not under re-reading. The test counts reproduce exactly.
The AC-1 gate grep reproduces line for line. The parser's untouchedness survives a diff I ran
myself. The depth defect is observed at three real placements where `parents[2]` would have been
wrong twice — once resolving outside the project entirely — which is the observation TS §5 said
this repository could never produce. And AC-13 half two is reported unmet, which was the one
answer that took discipline rather than effort.

**What holds it back is that the payload now contradicts itself on the rule this phase wrote.**

`.tfw/templates/status.md:92` still reads *"Normalizing such a value to a declared one is
prohibited."* That is verbatim the sentence commit `f14f744` **rewrote** in `glossary.md` and
replaced in `conventions.md` §5 with the two-act rule: migration never normalizes, an accountable
owner may resolve through a recorded `transition` event. The executor identified that exact
wording as the defect, corrected two copies, and left the third — in the canonical carrier
template, which is the file a person hand-authoring `status.md` actually opens, in the phase
whose entire subject is that a receiving project has only the payload and the payload must not
mislead it. `.tfw/CHANGELOG.md` announces the corrected rule under **Canon**, so the release as
it stands states one thing and the template it ships states another.

TS §5 AC-14's fourth bullet named the harm in advance: *"the prohibition reads as absolute and
projects will either strand tasks or resolve them without a trace."* That harm ships. This is not
a wording objection — two shipped normative files give a reader opposite instructions about the
same act, and the reader most likely to hit it is the one this phase was written for.

Why this is a REVISE and not debt: the coordinator's next act is cutting `v2.0.0-dirty.2`
(E53), and the act after that is the external update that closes AC-13 half two. Approving now
tags a release whose payload contradicts its own release note, and then runs the acceptance test
against it. The fix is one sentence in a file already in this phase's change set.

Nothing here is grounds for ❌ REJECT: purpose is aligned, the contract is coherent, the design
is sound, and no frozen section is in question.

### Items to fix

| # | Where | What | Why |
|---|-------|------|-----|
| **1** | `.tfw/templates/status.md:92` | Bring the `UNDECLARED` sentence into line with `conventions.md` §5 — migration never normalizes, an accountable owner may resolve through a recorded `transition` event carrying `from: UNDECLARED`. Cite §5 rather than restating the table; the profile template's own R3 treatment is the model | Closes AC-14's fourth bullet in the payload rather than in two of its three copies. verify.md **D1** |
| **2** | `.tfw/templates/status.md:78` | *"the four keys that are never prose — id, lifecycle, owner, authority, created, updated"* lists **six**. Correct the count | Same paragraph AC-5 wrote so a person gets the carrier right by hand. verify.md **D2** |
| **3** | RF §1, §4 · EV E47, E60 | Four claims looser than their evidence, corrected in place, no re-run required: **(a)** E47's *"0 framework files edited inside `.tfw/`"* carries its `__pycache__` caveat **at the row**, not only in `fixture_report.md`; **(b)** RF §1's `git log --follow` counts are re-measured at the declared pin `1079020` (**9** and **6**) or the pin is stated as `80c2ed5` for that measurement; **(c)** E60 / RF §4's *"as a class"* is stated as what `test_every_runtime_message_is_ascii` actually enforces — a line-scanning check over `print(` / `SystemExit(` sites, which caught five real occurrences and does not reach a message assembled into a variable; **(d)** `ac3_parser_untouched.txt` notes the signature line alongside the locator | TS §6 makes pinning a rule and TS §7 names *"a check reported as passing that never ran"* in four forms. Each is small; the class is the one this phase legislates against. verify.md **D4, D5, D6, C2** |

**Not an item to fix — recorded for the coordinator.** RF §1 heads its table *"Modified — 25"*,
the figure `census.md` reaches by classifying the four scripts as *moves*; the RF's table then
lists those same scripts as Modified rows. Distinct paths in the table: roughly 31. No budget
limit is crossed under the census's declared method, and the group was raised **before acting**,
which is the return-to-coordinator rule working. But the TS's basis for the classification did
not survive execution — it predicted the scripts would *"relocate rather than get rewritten …
cost a move and their path constants"*, and `gen_index.py` changed **507** lines,
`migrate_board.py` **246**. That is a coordinator estimate the work invalidated, not an executor
error. It belongs in the next phase's budget table, not in this round. verify.md **D3 / D3a**.

**On AC-13 half two.** It stays open and it is the owner's. The declared outcome of Phase AA is
*a project other than this one completes the update from the payload alone*, and the only run so
far was the author's own clone. The phase cannot be **closed** until a real external project is
updated by its own operator, filed at task root as
`FIELD-REPORT__TFW-60__second_external_update.md`. That is the contract's own design, not a gap
in the work — and it is why the revise round above is cheap to take now: the payload the owner
will run against should not contradict itself.

## 5. Tech Debt Collected

RF §6 carries seven observations. Quality filter applied — an item is promoted only if leaving
it causes a real problem. Six promoted, one reclassified.

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| TD-186 | RF TFW-60/AA §6 obs. 1 | Med | `KNOWLEDGE.md`:22 | The architecture table still names `docs/scripts/gen_index.py`. Correctly **not** written by the executor: `KNOWLEDGE.md` §1–§3 belongs to `/tfw-docs` under the D37 split, and AC-1's gate text names the hit explicitly so the RF could not report a green gate over a red one | → `/tfw-docs`, immediately after this phase is approved. Verified still open at review time |
| TD-187 | RF TFW-60/AA §6 obs. 3 | Med | `.tfw/workflows/init.md`, `.tfw/workflows/plan.md` | **1,897 and 1,598 words against the §11 design ceiling of 1,200.** Both were already over before this phase (1,821 · 1,501); it added 76 and 97. `update.md` was brought *under* the ceiling in this same phase by deleting duplication rather than cutting required content, so the technique is proven and available here — `init.md`'s tutorial asides and `plan.md`'s worked pseudocode are the named candidates | ⬜ Backlog — own task. Cutting a workflow is a change reviewers should see on its own, and it is out of this phase's scope |
| TD-188 | RF TFW-60/AA §6 obs. 5 | Med | `.tfw/scripts/gen_index.py` | `--check project` does not report a **retired framework file** still sitting in a receiving project's `.tfw/` — the fixture found `templates/topic_file.md` surviving the update, because copying a payload adds and overwrites but never removes. The migration guide now finds them by command, so the operator is not stranded | ⬜ Backlog. Correctly not added here: payload *completeness* and payload *minimality* are two claims, and the second needs a manifest of what the release ships, which does not exist |
| TD-189 | RF TFW-60/AA §6 obs. 6 | Low | `docs/scripts/test_integration.py` | The `docs/scripts/` suite takes ~250 s of the ~260 s total, almost all of it `mkdocs` builds inside tests; the payload suite alone is 12 s. **Confirmed by re-run here.** A receiving project runs only the payload suite so this never reaches them — but it makes this repository's own `build.test` slow enough to be skipped, which is how a gate stops being a gate | ⬜ Backlog — monitor. Candidate fix: mark the mkdocs-driven tests and let the default run exclude them |
| TD-190 | RF TFW-60/AA §6 obs. 7 | Low | `.tfw/CHANGELOG.md`:200–265 | The `2.0.0-dirty` entry's migration code fence still names `docs/scripts/`, correctly — it is a record of that tag — and the new entry says so and points at the guide. A reader who scrolls to the fence without reading the note above it can still copy a dead command. The structural fix is a per-release *superseded by* marker, which is a CHANGELOG-format change | ⬜ Backlog — → the task that revises `RELEASE.md`. Candidate: pairs with TD-179 and TD-180, which are already open against release procedure |
| TD-191 | REVIEW TFW-60/AA §2 · reviewer finding | Low | `.tfw/CHANGELOG.md`:101, TS TFW-60/AA §5 AC-11 | **`TD-11` names a debt row that does not exist.** The shipped release note says *"TD-11, unfixed across two releases"*, and the label originates in the field report. `TECH_DEBT.md` has no `TD-11`; the historical TD-11 (TFW-7) was a different defect — *"`.tfw/README.md` L280 says 3 canonical workflows"* — and was purged in the 2026-04-15 sweep. A reader following the release note's own citation finds nothing, or finds an unrelated row | ⬜ Backlog — either register the adapter-route defect under a fresh ID and correct the CHANGELOG reference, or drop the ID from the entry. Not urgent; it is a citation, not a rule |

**Reclassified, not promoted:** RF §6 obs. 2 (`tasks/BOARD-SNAPSHOT.md`'s SCREAMING-KEBAB name)
and obs. 4 (`check_project`'s small duplication of the `build.*` path check, and `gen_docs.py`'s
ten-line bootstrap restatement of `find_project_root`). Obs. 2 is a **decision** TS §6 explicitly
asked to be recorded as one — Phase A's links resolve to that path and a rename days later would
break them — so it is a recorded ruling, not debt. Obs. 4 is honest duplication the executor
correctly identified as such: `gen_docs` needs the root in order to locate the module it would
import the function from, which is a bootstrap that cannot import its way out. Neither would
cause a real problem if left, which is the bar.

**Related open item confirmed still open:** TD-182 (the Assisted edition's folder-moving status
model) — deferred by owner decision and explicitly out of this phase's scope per TS §2.

## 6. Traces Updated

- [x] the phase's `status.md` — `lifecycle: RF` retained per the REVISE verdict (`conventions.md` §5: *"specific issues → back to execution, same task"*), with a `transition` event in the task's `journal/`
- [x] HL status — unchanged. Phase AA does not complete on this verdict
- [x] the phase's `status.md` — `updated` reflects this review; no counter incremented
- [x] Other project files — checked. `KNOWLEDGE.md:22` is stale by design and routed to `/tfw-docs` as TD-186; nothing else is stale as a result of this phase
- [ ] tfw-docs: **Deferred** — runs after ✅ APPROVE. TD-186 is its first item
- [ ] tfw-knowledge: **Deferred** — runs after ✅ APPROVE. RF §7 carries seven candidates and this REVIEW adds one

## 7. Fact Candidates

> fact-candidates: processed 2026-08-30

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | process | **A rule corrected in the canon is not corrected until every shipped copy of its old wording is found.** Phase AA rewrote the absolute `UNDECLARED` prohibition in `conventions.md` §5 and `glossary.md` and left the identical sentence standing in `.tfw/templates/status.md`. The two edited files are the ones a reviewer reads; the missed one is the one a receiving project reads. The mechanical form of the check is to grep the **old sentence**, not the concept, before declaring the rewrite complete | Reviewer, this review | High |

I record only one. RF §7's seven are strong and I challenged none of them; #5 (the reusable
`KZ-IT-telegram-list` fixture at `c919640`) and #6 (the owner's non-UTF-8 console) are both
checkable and both check out against `fixture_run.txt`. Adding paraphrases of them here would
make `/tfw-knowledge`'s job worse, not better.

---

*REVIEW — TFW-60 / Phase AA: Portable Delivery | 2026-08-28, reviewed at `440d6fd`*
