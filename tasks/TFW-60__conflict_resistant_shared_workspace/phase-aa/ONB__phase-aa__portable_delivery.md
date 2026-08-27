# ONB — TFW-60 / Phase AA: Portable Delivery

> **Date**: 2026-08-27
> **Author**: Claude Code (Executor), `actor: saubakirov`, `via: claude`
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-60](../HL-TFW-60__conflict_resistant_shared_workspace.md)
> **Phase HL**: [HL Phase AA](HL__phase-aa__portable_delivery.md)
> **TS**: [TS Phase AA](TS__phase-aa__portable_delivery.md)
> **Origin read**: [FIELD-REPORT](../FIELD-REPORT__TFW-60__first_external_update.md) F1–F10 and §6
> **Predecessor RF read**: [Phase A RF](../phase-a/RF__phase-a__task_state_and_coordination.md)
> **Measured at**: working tree `866c38d`, 2026-08-27. Two files are dirty from unrelated tasks
> (TFW-55 `research/iterations.yaml`, TFW-54 `HL-TFW-54__…`) — see Risk 6.

---

## 1. Understanding

Phase A shipped a task model that works in this repository and cannot be handed to another one.
Four things the release requires are outside the payload `/tfw-update` copies: `gen_index.py`,
`migrate_board.py`, a `team/` explanation, and a migration guide that never existed. The first
external consumer completed its update anyway — by hand-carrying files and reconstructing an
order the release states once, in a code fence, inside a CHANGELOG.

Phase AA closes that gap and nothing else. The model is untouched: no carrier schema, no event
grammar, no lifecycle value, no identifier rule. The work is a `git mv` and everything that names
its result, a migration guide written for a project that is not this one, five defects the external
run found in the two scripts, a post-update self-check that reports and exits, one adapter route
that has been broken for two releases, one out-of-theme session-naming fix, and a `2.0.0-dirty.2`
release surface that describes what shipped.

The phase passes or fails on one thing: **at least one project other than this one completes the
update with zero hand-carried files and zero edits inside `.tfw/`.** Every Phase A review round ran
here, which is why none of this was found. Question 1 is therefore the question that decides whether
this phase can be executed at all.

## 2. Entry Points

### The move and its dependents

| Path | Why it matters |
|---|---|
| [gen_index.py](../../../docs/scripts/gen_index.py) | 41,732 B. `--root` default `parents[2]` at L871. `TASK_DIR` L52, `LEGACY_ID` L49, `parse_identifier` L92, `iter_task_dirs` L146, `read_status` L186 (F5 message at L203), `collect` L640 (F4 drop at L171–172), `Backlog` render L812 |
| [migrate_board.py](../../../docs/scripts/migrate_board.py) | 29,714 B. `BOARD_HEADING` L49 (F3), `read_board` L546 (F8), `parents[2]` L605, empty-board refusal L637, `"backlog idea, never started"` L444 (F4), `sys.path.insert(parent)` L37 |
| [test_gen_index.py](../../../docs/scripts/test_gen_index.py) · [test_migrate_board.py](../../../docs/scripts/test_migrate_board.py) | 131 passed, 1 skipped — matches the field report exactly |
| [gen_docs.py](../../../docs/scripts/gen_docs.py) | `import gen_index` at L18 — a bare same-directory import. Root derivation at L190 |
| [test_integration.py](../../../docs/scripts/test_integration.py) | L174 globs `docs/scripts/*.py`; L309 lists shipped-text roots including `docs/scripts` |
| [docs/mkdocs.yml](../../../docs/mkdocs.yml) | `gen-files` runs `scripts/gen_docs.py` relative to `docs/`. Unaffected by the move; the import at L18 is not |

### Normative references and the release surface

`.tfw/conventions.md:332` · `.tfw/glossary.md:309` · `.tfw/project_config.yaml:132,133,139` ·
`.tfw/workflows/init.md:69,233` · `README.md:257` · `.tfw/CHANGELOG.md:75,79,91,120,131,132` ·
`KNOWLEDGE.md:22` (see Q5) · `workspace/00-INDEX.md:4,14,123` (generated).

### The eleven provenance comments — confirmed

`git grep -l "Written by docs/scripts/migrate_board.py"` returns 13 files: `migrate_board.py`
itself, the Phase AA TS, and **exactly eleven `status.md` files**. The TS's count is correct and
their bytes stay.

### Baseline measurements taken before any edit

| Measurement | Value |
|---|---|
| `pytest docs/scripts/ -q` | **220 passed, 1 skipped**, 305 s |
| `pytest test_gen_index.py test_migrate_board.py -q` | **131 passed, 1 skipped**, 4.9 s |
| `update.md` | 835 words (design ceiling 1200) |
| `init.md` · `plan.md` | 1,821 · 1,501 words — both already over the ceiling |
| Adapter copies vs sources | all 22 byte-identical. Nothing is out of sync going in |
| CI | `.github/workflows/docs.yml` runs `mkdocs build` only. **No CI change needed** — no pipeline runs pytest |

### The AC-13 fixture, located

`D:\projects\KZ-IT-telegram-list` is reachable, clean, at `2.0.0-dirty`. Its pre-update commit
`c919640` (parent of `97dd429`) is a complete external fixture at TFW **1.3.0**:

- board at `tasks/README.md` under `## Board`, with a separate `## Backlog` — exactly F3;
- four task directories, mixed grammar: `TFW-01_…`, `TFW-02_…` (single `_`), `TFW-3__…`,
  `TFW-4__…` — exactly F4;
- `task_containers: [tasks]`, one container — not this repository's two;
- **no TFW version tags at all** (`git tag -l` → `data-2026-08-27` only), which relocates AC-10 —
  see Recommendation 8.

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | **AC-13 — which project is the external fixture, and may I create it?** The only external consumer has *already* migrated, so a `2.0.0-dirty → 2.0.0-dirty.2` update there exercises payload delivery but can never exercise AC-2's guide (it does not cross a major), AC-3's board locator, AC-4's classification or AC-8's revision default. Options: **(a)** clone `KZ-IT-telegram-list` at `c919640` into the scratch directory and run the full 1.3.0 → 2.0.0-dirty.2 update there — real corpus, real board location, real mixed grammar, reproducible, and not this repository; **(b)** name another real pre-2.0.0 project; **(c)** run against the live consumer only and mark the migration half of AC-13 DEFERRED. (a) needs your authorization because it writes outside this repository. My recommendation is **(a) plus a second, lighter run against the live consumer** — (a) covers migration, the live run covers the payload path a real operator will actually take | **(a), with a distinction the TS failed to make.** Clone to scratch and build against it. **Never touch the live consumer** — it is the owner's project, and a second agent writing into it is the F14 / TD-144 defect this whole task exists to end. The distinction: a **development fixture** is not **acceptance evidence**. You need the first to build AC-2, AC-3, AC-4 and AC-8 at all; the owner's real runs are the second. AC-13 as written conflates them and is being amended. Your clone at `c919640` closes the fixture half. The evidence half is closed by the owner updating two real projects, and you report it **unmet** and hand it back. If your RF ever says the external check passed on your own clone, that is the fifth form of the DoF pattern and review must reject it. |
| 2 | **Where does the AC-13 field report live?** Its predecessor sits at task root as `FIELD-REPORT__TFW-60__first_external_update.md`. Options: a second root-level `FIELD-REPORT__TFW-60__second_external_update.md`; or `phase-aa/evidence/` as an evidence attachment indexed in the EV file. The first matches precedent and is visible to Phases B and C; the second keeps phase evidence in one place. Which? | **Both, split by what they are.** Your clone run is evidence: `phase-aa/evidence/`, indexed in the EV file. The owner's real external run is advisory input the whole task reads, so it goes to task root as `FIELD-REPORT__TFW-60__second_external_update.md`, matching its predecessor and visible to Phases B and C. You author the first and not the second. |
| 3 | **AC-14 — may the executor create the `v2.0.0-dirty.2` tag?** §15 Role Lock assigns `VERSION` and `CHANGELOG.md` to `release.md` / Coordinator; this TS assigns them to me under "Release surface", which I read as authorized. The **tag** is different, and AC-13 needs a source the fixture can be pointed at. Options: **(a)** I write VERSION + CHANGELOG, commit, create the local annotated tag, run AC-13 against it — the fixture then exercises the real "clone a tag" path; **(b)** I write VERSION + CHANGELOG and commit, AC-13 runs against that **commit SHA**, and `/tfw-release` cuts the tag after approval — no executor tag, at the cost of AC-13 not testing the tag path. No push either way, per Commit Attribution | **(b).** `conventions.md` §15 assigns `release.md` to the coordinator and a tag is a release act; more to the point, a tag on unreviewed work asserts releasability, which is the reviewer's finding to make, not yours. You write `VERSION` and `CHANGELOG.md` — the TS authorizes those and I confirm it — commit, and point the fixture at that **commit SHA**. On the cost you name: `git clone` plus `git checkout <sha>` exercises the same mechanics as a tag; a tag adds a name, not a path. And the real tag path does get tested — I cut `v2.0.0-dirty.2` after review, and the owner's two updates run against it. The people who matter test it, just not inside your pass. |
| 4 | **AC-11 census growth — two adapter source files the TS does not name.** `/tfw-research` routes to the non-existent `.tfw/workflows/research.md` in **three** adapter sources, not one: `claude-code/CLAUDE.md.template:31` (named in TS §4), `claude-code/README.md:43`, `antigravity/README.md:22,64`. AC-11 says *"every path in every adapter source resolves; a test fails if one does not"*, so a test satisfying AC-11 fails on all three. Approve adding both files to Modify, or bound AC-11 to the template and let the test allow the two READMEs (in which case AC-11's own gate cannot be written as stated)? | **Add both to Modify.** You are right that bounding AC-11 to the template makes its own gate unwritable, and an AC whose gate cannot be written is not an AC. `claude-code/README.md` and `antigravity/README.md` join the census; Modify moves to roughly 25 against a limit of 30. This is the return-to-coordinator rule working as intended — a group appeared, you raised it before acting, nothing was absorbed silently. |
| 5 | **`KNOWLEDGE.md:22` is a normative reference to `docs/scripts/gen_index.py`.** AC-1 requires every normative reference to name the payload path, and its gate says the grep *"returns only historical trace artifacts and the eleven provenance comments"* — `KNOWLEDGE.md` is neither. TS §9 says `KNOWLEDGE.md` is untouched. Options: **(a)** I change that one path (contradicts §9 as written); **(b)** `/tfw-docs` changes it after approval, and AC-1's gate is amended now to name `KNOWLEDGE.md` as a known exception so the RF does not report a green gate that is red; **(c)** amend AC-1's gate to exclude it permanently. Silence is the one option I will not take: an unexplained grep hit is the shape of DoF's *"a check reported as passing that never ran"* | **(b).** `KNOWLEDGE.md` belongs to `/tfw-docs` under the D37 ownership split and you do not write it. AC-1's gate is amended now to name it as a known exception, and the reference is added to the RF §6 observations so `/tfw-docs` closes it after approval. Your closing line is the right instinct and I am recording it as the reason: an unexplained grep hit is exactly the shape of a check reported as passing that never ran. |
| 6 | **AC-9 — where does the self-check live?** Field-report rec 9 proposed `gen_index.py --doctor`. AC-9 says only *"one command"*. Options: **(a)** a `--doctor` flag on `gen_index.py` — no new file, and it inherits the report-and-exit character `--validate` already has, but it puts payload/`team/`/config checking inside the index generator; **(b)** a new `.tfw/scripts/doctor.py` plus `test_doctor.py` — Create goes 7 → 9 (limit 15), a cleaner separation, and one more file for a receiving project to know about. My recommendation is **(a)**: AC-9's *"it is named in the migration guide as the last step"* is easier to satisfy with a command the project already runs | **(a) — `--doctor` on `gen_index.py`.** Your reasoning holds, and there is a second reason: the file already carries `--validate`, which validates task state rather than the index, so it is not a pure generator today and `--doctor` does not make it one. Fewer commands for a receiving project to learn wins. Non-negotiable rider from your own inconsistency 6: the output must state that it does **not** answer index freshness, or the next operator reads one flag's silence as the other's answer.<br><br>**⚠ SUPERSEDED at TS R3 — do not implement this answer.** The owner challenged the phase's additions and this one did not survive. Your inconsistency 6 described the trap and I accepted the trap instead of removing it: `project_config.yaml` already needs five lines of comment to keep `--check` and `--validate` apart, and I approved a third synonym. **When prose is required to distinguish your own names, the names are wrong.** The three collapse into `--check index` / `--check tasks` / `--check project`, and the comment is deleted rather than rewritten. TS §5 AC-9 carries it. |
| 7 | **AC-4 — confirm "reported", not "matched".** AC-4 allows the single-underscore legacy form to be *"either matched or reported"*. Matching it means editing `LEGACY_ID`/`parse_identifier`, which is an **identifier rule**, and TS §7 DoF forbids *"any edit to … the identifier rules"*. So only *reported* is available. Confirm, because if you meant *matched*, this is a materially larger and DoF-conflicting change | **Confirmed — reported, never matched.** You read DoF correctly; widening `LEGACY_ID` is an identifier rule change and is forbidden here. One addition, so the consequence is not left as a dead end: the migration guide tells the operator that a directory reported as unresolved may be **renamed by hand** to the recognized grammar if they want it picked up. That keeps it a human act with a trace, and it is the same shape as the `UNDECLARED` ruling — the tool never normalizes, an accountable person may resolve. |
| 8 | **AC-8 — what happens when there is no committed board to read?** Defaulting `read_board()` to a committed revision needs a defined behaviour when the project is not a Git repository, or `README.md` (or `--board`) does not exist at `HEAD`. Options: **(a)** refuse, naming the working-tree opt-in — consistent with the empty-board refusal, and it never silently reads a stale or a live file; **(b)** fall back to the working tree with a printed notice — friendlier, and it reintroduces exactly the silent live read AC-8 exists to remove. My recommendation is **(a)**, with the printed revision that AC-8's third bullet already requires | **(a) — refuse, naming the working-tree opt-in.** Consistent with the empty-board refusal you are preserving, and (b) reintroduces the silent live read that AC-8 exists to remove. A printed notice is the thing nobody reads. The refusal names the opt-in flag and prints the revision it tried, per AC-8's third bullet. |

> **⚠ Two coordinator answers below were superseded on 2026-08-27 by TS revision 3** — Q6 and
> inconsistency #1. The originals stay visible and are marked in place; a superseded instruction is
> corrected by appending, never by overwriting, which is the rule the journal and §12 already follow.
> **The TS is the authority. Where this file and the TS disagree, the TS is right.**

## 3a. Coordinator rulings on §4, §5 and §6

Answered here rather than left silent, because several are decisions and not suggestions.

**Recommendations — all eight approved.** Two are more than approvals:

- **Rec 2 is a finding, not a tidy-up.** `build.*` sits under *"Project sections (preserve)"* in
  `update.md`, so a receiving project keeps a `build.verify` naming a path that no longer exists. That is
  a second instance of F1's own class, arriving through the update path this phase is fixing. The
  migration guide must name `build.*` as something the operator edits by hand. Had you not raised it, it
  would have shipped again.
- **Rec 8 is a correctness catch.** The consumer has no TFW tags at all; the pristine-tag diff ran against
  the **source** tree. `update.md` must say whose tag, or an operator looks for a tag their project never
  had and concludes the technique does not apply.

**Risks — acknowledged, and Risk 4 changes how AC-1 is verified.**

- **Risk 4 is the sharpest thing in this onboarding.** `parents[2]` resolving correctly by coincidence at
  `.tfw/scripts/` means a source-only move passes every test here while leaving F1's aggravating detail
  fully intact — and AC-1's stated gate does not catch it, because the default is relative to the script
  file rather than the cwd. Your fixture — the tools copied to a different depth inside a project — is
  the observable test, and AC-1's gate is amended to require it.
- **Risk 5, census.** Your enumeration is authoritative; TS §4's `Modify — 26` was my estimate and the
  table under-listed. The RF carries the counted number, not mine. With Q4's two additions and
  `KNOWLEDGE.md` excluded by Q5, expect roughly 25 against a limit of 30.
- **Risk 6, dirty tree.** Your stance is correct and is now a rule for this phase: pin a commit that
  excludes the other tasks' artifacts and say so in the EV file. Do not commit another task's work to make
  your own measurement clean.
- **Risks 1, 3 and 7 approved as you propose** — one code path for AC-3 and AC-8, a skipped `.upstream`
  segment with the resolved root printed every run, and `workspace/00-INDEX.md` regenerated and counted as
  derived output rather than a modified file.

**Inconsistencies — you are right on all six. Two are my errors:**

- **#1 — `team_README.md` violates `conventions.md` §10.4.** Use `team_readme.md`. My TS was wrong; the
  TS is corrected rather than left for you to deviate from.
  > **⚠ SUPERSEDED at TS R3 — the file is withdrawn, not renamed.** Renaming was the small answer to a
  > correct catch. The owner asked the larger question and it does not survive: `templates/research/`,
  > `templates/evidence/` and `templates/review/` had already settled that a template producing into a
  > directory *lives* in a directory — so the right name was `templates/team/README.md`, and the right
  > answer was that no such template is needed at all. AC-7 creates `team/` together with its first
  > profile, so an unexplained directory never appears, and the content duplicated `conventions.md` at
  > three separate points. **Create nothing here.** Three existing templates also move into that shape:
  > `team_profile` → `team/profile`, `journal_event` → `journal/event`, `topic_file` → `knowledge/topic`.
- **#2 — the HL diagram is loose**, the TS is right. `team_profile.md` already exists. A Phase HL is
  derivation-only and carries no contract, so nothing is amended; recorded so the reviewer does not read
  the diagram as a second requirement.
- **#4 and #5** — naming the offending key means deriving it from the raw front-matter at the marked line,
  and the template's example is invalid on `goal`, `value` and `authority` as well as `title`. Both are
  in scope; AC-5 means all of them.
- **#3 and #6** acknowledged as you state them.
  > **#6 updated at TS R3.** You were right that the trap exists; naming it was not enough. The flags
  > merge, so there is no `--doctor` silence for an operator to misread and no comment to maintain.

## 4. Recommendations (suggestions, not blocking)

1. **Keep `update.md` under the 1200-word ceiling by routing, not by prose.** It is at 835 words and
   AC-2, AC-6, AC-7, AC-9 and AC-10 all add to it. Written out in full that is roughly +400–600 words
   and the file lands at 1250–1450, over the §11 design rule. I intend to put the *decision* and the
   *route* in `update.md` (one or two lines each) and the reasoning, the ordering constraint and the
   worked commands in `.tfw/migrations/2.0.0.md`. This also serves AC-2's *"the ordering constraint
   appears where a reader is about to violate it"*. If you want the detail inline instead, say so —
   it is a convention overrun and it should be your call, not mine.

2. **`build.lint` and `build.test` run `pytest docs/scripts/ -q`** (`project_config.yaml:132–133`).
   After the move that command no longer runs the two suites this release cares about. I will point
   them at both directories. **The delivery consequence is bigger than the edit:** `update.md` lists
   `build.*` under *"Project sections (preserve)"*, so a receiving project keeps its own stale
   command and its `build.verify` keeps naming `docs/scripts/gen_index.py`. The migration guide must
   name `build.*` as something the operator updates by hand. This is a second instance of F1's class
   and it would otherwise ship again.

3. **`test_no_board_shaped_regex_survives_in_the_generators` (test_integration.py:174) globs
   `docs/scripts/*.py`.** After the move `gen_index.py` leaves that directory and the test's coverage
   silently shrinks while it keeps passing — the exact shape of DoF's *"a check reported as passing
   that never ran"*. I will make it scan both directories and assert that it found the files it
   expects to find, so an empty glob fails instead of passing.

4. **Add a sibling `iter_unmatched_task_dirs()` rather than change `iter_task_dirs()`'s signature.**
   F4's mechanism is `gen_index.py:171–172`: a directory `parse_identifier` rejects is `continue`d,
   so it never reaches `unresolved` — that is *why* the consumer saw 2 directories where 4 exist.
   `iter_task_dirs` is called by `gen_docs.py:348`, `migrate_board.py` and the tests; returning a
   tuple would break all three. An additive sibling keeps the working callers working.

5. **AC-11's path checker needs a declared allowlist.** A naive resolver over adapter copies reports
   16 failures that are all correct paths: `~/.tfw/bindings.yaml` is per-machine and deliberately
   outside the tree, and `.tfw/.upstream/.tfw/CHANGELOG.md` is created at runtime by `update.md`
   Step 0. The allowlist must be short, named and commented, or the test gets disabled the first
   time it cries wolf.

6. **`gen_docs.py:18` is a bare `import gen_index`** that works only because the two files share a
   directory. After the move it needs an explicit `sys.path` insert of `<root>/.tfw/scripts`,
   bootstrapped from `gen_docs.py`'s own root derivation at L190. `mkdocs` runs it through the
   `gen-files` plugin with `docs/` as the config root, so this path must be absolute, not relative
   to the cwd. `mkdocs build` is a gate for exactly this reason.

7. **`.tfw/scripts/README.md` should state the root-resolution rule, not just the commands.** AC-1's
   *"the tools work wherever a project places them"* is only true to a project that knows it is true.
   One sentence — *the tools find the project root by walking upward for `.tfw/`, so you may put them
   anywhere* — is what converts the code change into a delivered capability.

8. **AC-10's "pristine previous tag" lives in the source, not the receiver.** The consumer has no TFW
   version tags at all; the field report's `git show v1.3.0:.tfw/<f>` ran against the **source**
   tree, which does have `v1.3.0` and `v2.0.0-dirty`. `update.md` must say whose tag, or an operator
   will look for a tag their own project never had and conclude the technique does not apply to them.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **AC-3 and AC-8 interact and the TS treats them separately.** Once `--board` can name a path *and*
   the default input is a committed revision, the board must be read as `git show REV:<board-path>`.
   Reading `--board` from the working tree while claiming a revision would produce a run whose log
   names a revision it did not read — a false provenance statement, which is worse than either
   defect alone. I will implement them as one code path.

2. **AC-2's routing cannot fire on the live consumer.** *"Route to the guide when the update crosses a
   major"* — `2.0.0-dirty → 2.0.0-dirty.2` does not cross a major. So a run against the already
   migrated consumer exercises the payload and skips the guide entirely. This is the mechanical reason
   Question 1 needs a pre-2.0.0 fixture, not a preference for thoroughness.

3. **The marker search can resolve the wrong root.** Walking upward for `.tfw/` finds
   `.tfw/.upstream/` as a project root for any tool run from inside the staging directory that
   `update.md` Step 0 creates. Arguably correct, and it means an operator can silently generate an
   index for the upstream clone instead of their own project. I intend to skip a candidate whose path
   contains a `.upstream` segment and to print the resolved root on every run, so a wrong answer is
   visible rather than inferred.

4. **`parents[2]` coincidentally still resolves correctly at `.tfw/scripts/`.** From
   `.tfw/scripts/gen_index.py`, `parents[2]` *is* the project root — so a source-only move would pass
   every test in this repository while leaving F1's aggravating detail fully intact. AC-1's stated
   gate (*"run both tools from a checkout placed at a different depth"*) does not catch it either,
   because the default is relative to the **script file**, not the cwd. The observable test is a copy
   of the tools at a *different depth inside* a project — e.g. `tools/tfw/gen_index.py` — and that is
   the fixture I will use.

5. **Census reconciliation.** TS §4 declares **Modify — 26**; the paths its table actually lists
   count to **23** by my enumeration (4 normative + update + plan + status template + adapter
   template + 3 tooling + 3 release + 9 adapter copies). My census adds 2 (Question 4) and possibly
   `KNOWLEDGE.md` (Question 5), reaching 25–26. Nothing crosses a limit (30 modified, 15 new). I am
   raising it rather than resolving it because DoF requires it and because the RF's accounting has to
   match a number the TS can be diffed against.

6. **The working tree is dirty with two unrelated artifacts** — TFW-55's `research/iterations.yaml`
   and an untracked TFW-54 HL. TS §6 requires evidence measured at a pinned commit. Either those land
   under their own task first, or my pinned commit deliberately excludes them and the EV file says so.
   I will not commit another task's artifacts to make my own measurement clean.

7. **`workspace/00-INDEX.md` will change without being in the census.** It is generated and carries
   three references to `docs/scripts/gen_index.py` (L4, L14, L123). Regenerating it is correct and
   costs nothing; leaving it stale leaves three wrong paths in a file the README routes readers to. I
   will regenerate it and count it as a derived output, not a modified file — flagging the choice
   because a reviewer will otherwise find an uncounted diff.

## 6. Inconsistencies with Code (spec vs reality)

1. **`.tfw/templates/team_README.md` violates conventions §10.4.** TS §4 Create names that filename;
   §10.4 says *"Markdown templates in `.tfw/templates/` also follow `lower_snake_case`"* and reserves
   uppercase for project-root documents and `.tfw/` framework docs — a template is neither.
   `team_readme.md` complies; every existing sibling (`team_profile.md`, `topic_file.md`,
   `journal_event.md`) does too. I will use `team_readme.md` unless you say otherwise, and record the
   deviation from the TS in the RF.

2. **HL and TS name different new files for AC-7.** The Phase HL's AFTER diagram says
   `templates/team_profile.md + a step that creates the acting profile`; `team_profile.md` **already
   exists** and needs no creation. The TS's Create list says `team_README.md`, which is the `team/`
   directory README. Reading both with the field report's rec 7 (*"a `README` template inside
   `.tfw/`"*), the TS is right and the HL diagram is loose. Recording it so the reviewer does not read
   the HL as a second requirement.

3. **F4 is one classification, not two.** AC-4 requires *"the manifest and the index agree"*, which
   reads as two fixes. They already share a source: `migrate_board.reconcile()` assigns
   `"board-only, backlog"` (L381) and the reason string `"backlog idea, never started"` (L444), and
   `gen_index.collect()` renders `Backlog` from that same snapshot class (L704). Fixing the
   classification fixes both consumers. Good news, recorded so the RF's two ticks are not read as two
   independent verifications of one change.

4. **F5's "name the offending key" is not available from the exception.** The message comes from
   `read_status` (L203) and `read_phase_status` (L308) as `exc.__class__.__name__`.
   `yaml.MarkedYAMLError` carries `problem_mark`/`context_mark` — a **line and column**, not a key. So
   naming the key requires deriving it from the raw front-matter text at that line. Feasible and
   worth it, and materially more than a message change. AC-5's gate (*"feed five files whose titles
   contain a colon-space; each error names its key"*) is what I will build against.

5. **The `status.md` template's example is invalid under its own advice in more than one line.** F5
   names `title: short task name`. `goal:`, `value:` and `authority:` model the same unquoted form,
   and `goal: why this task exists, one line` is exactly the shape that breaks — a plain scalar with
   punctuation. AC-5's *"the template's example quotes its values"* is therefore all of them, not one.

6. **`--validate` and `--doctor` have no overlap problem, but `--check` does.** `project_config.yaml`
   carries a deliberate comment explaining why `build.verify` is `--validate` and **not** `--check`
   (`--check` asks whether the shared index is current, which would make every task-local transition
   fail a gate). If AC-9 becomes `--doctor` (Question 6a), its output must state that it does not
   check index freshness, or the next operator will read one flag's silence as the other's answer.
   AC-9's *"its output names what it did not check"* covers this; naming the specific trap here so it
   is not left to judgement.

## 7. Knowledge Citations

> Coordinator's citations: master HL §7.2, 29 items. All 29 read. Phase AA is a **delivery** phase, so
> a large share are correctly N/A — they governed Phase A's design of the model, and this phase
> changes no part of the model. Each N/A states why rather than deferring to the group.

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | PV 0 — `README.md` opening · § How It Works | ✅ | **Applied** | *Bounded resumability* is what AC-2's guide and AC-9's self-check deliver to a project that has no session history here. `README.md:257` is also a census hit |
| 2 | PV 0 — `.tfw/README.md` NS1, NS2 (principles 3, 5) | ✅ | **Applied** | *Authorized continuation* is exactly what a receiving project cannot do today: it is told to run a file it does not have. AC-1 is this clause made true off-site |
| 3 | PV 1 — Structural Enforcement | ✅ | **Applied** | Drives Recommendation 3 and Risk 4. A gate whose glob has moved out from under it, or a depth check `parents[2]` still satisfies by accident, is prose wearing a test's clothes |
| 4 | PV 1 — one authoritative owner per truth type | ✅ | **Applied** | The load-bearing constraint on AC-9: the self-check reports and exits. The moment it writes it becomes a second authority over task state |
| 5 | PV 1 — Portability · Success Criteria | ✅ | **Applied** | The whole phase. *Provider-independent durable context* is not portable if the payload cannot carry its own tooling. No package manager, no installer — ordinary files, per HL's exclusions |
| 6 | PV 2 — `philosophy.md` F4 (structural gates beat state tables) | ✅ | **Applied** | AC-11's path test and AC-9's self-check are structural. The field report's own finding was that the best available signal was two framework tests a consumer was never told to run |
| 7 | PV 2 — F11 (TFW Markdown *is* the knowledge graph; avoid extra entities) | ✅ | **Applied** | Argues for Question 6 option (a): a flag on a tool the project already runs, over a fourth script it must learn about. Also argues against a `migrations/` index file — one guide per major, routed to, no registry |
| 8 | PV 2 — F27 (observable file-by-file progress is stakeholder value) | ✅ | **Applied** | Shapes AC-9's output: per-check lines a person can act on, plus an explicit list of what it did not check |
| 9 | PV 2 — F34 (a vague request must lead through discovery to a usable result) | ✅ | **Applied** | Question 1 is this clause. *"An external project"* is not usable until a specific fixture exists and is authorized |
| 10 | PV 2 — F38 (coordinator attention is finite) | ✅ | **Applied** | Why the eight questions are batched into one file with options and a recommendation each, rather than arriving as eight turns |
| 11 | PV 3 — `KNOWLEDGE.md` D31, D50 (filesystem state and locality) | ✅ | **Applied** | Phase A's foundation, unchanged here. Cited because Question 5 concerns `KNOWLEDGE.md:22`, which is where D31/D50's mechanism is indexed — including the path this phase moves |
| 12 | PV 3 — D37 (exclusive knowledge write territories) | ✅ | **N/A** | Phase C's concern. Nothing here writes `knowledge/` or touches `/tfw-docs` versus `/tfw-knowledge` ownership. It is *why* Question 5 offers option (b) rather than assuming I may edit `KNOWLEDGE.md` |
| 13 | PV 3 — D43 (knowledge citation cascade) | ✅ | **Applied** | This section is the cascade's executor link. Recorded per row, with N/A justified per row |
| 14 | PV 3 — D55, D59 (commit attribution; capability claims keep boundaries apart) | ✅ | **Applied** | Commits use `[claude-code/TFW-60/phase-aa/executor]`; no push without approval. D59 is Question 3: writing `VERSION` is authorized by the TS, cutting a tag is a release capability and I am not assuming it |
| 15 | PV 3 — D65 (reverting a result never reverts its trace) | ✅ | **Applied** | The 82 never-modify artifacts and the eleven provenance comments. Rewriting a comment about a past act at a path that was correct then would make the record say something that did not happen |
| 16 | PV 4 — `conventions.md` §§3–5 | ✅ | **Applied** | §4's identifier rules are what collapse AC-4 to *reported* (Question 7). §10.4's naming rule is Inconsistency 1. §11's word ceiling is Recommendation 1 |
| 17 | PV 4 — §13, §14 (trace discipline; whole-tree restore failure) | ✅ | **Applied** | The move is `git mv`, not copy-and-delete — a script whose history stops at Phase AA loses four rounds of reasoning. No trace deletion anywhere in this phase |
| 18 | PV 5 — `convention.md` F22 (root board update is a process artifact) | ✅ | **N/A** | Settled by Phase A: the live board is retired and its bytes are in `BOARD-SNAPSHOT.md`. Phase AA only makes the board's *location* an input for projects that still have one (AC-3) |
| 19 | PV 6 — `process.md` F7, F30 (cross-session context is lost; capture without enforcement changes nothing) | ✅ | **Applied** | F30 is the field report's own thesis restated: *"the file copying took minutes; the rest of the session was reconstructing what to do and in what order."* AC-2 is the enforcement half — a guide routed to from the step that needs it, not prose in a CHANGELOG |
| 20 | PV 7 — `risk.md` F1 (two sessions share one Git index; verbal warning 0/1) | ✅ | **Applied** | Directly operational: the AC-13 fixture is a **separate clone** with its own index (Question 1a), never a second working tree over this one |
| 21 | PV 7 — `constraint.md` F1, F3 (shared personal state is unsafe; templates generate filler) | ✅ | **Applied** | F1 bounds AC-7: `team_readme.md` explains the directory and the binding's location outside the tree, and ships **no** participant. F3 is why `.tfw/scripts/README.md` gets Recommendation 7's one load-bearing sentence instead of a generated wall |
| 22 | RES 1 — YAML 1.2.2 | ✅ | **Applied** | AC-5's root cause is a spec fact: a colon followed by a space ends a plain scalar. Both the quoted example and the key-naming validator derive from it |
| 23 | RES 1 — RFC 8259 | ✅ | **N/A** | JSONL was not the chosen journal carrier; Phase AA changes no carrier |
| 24 | RES 1 — Git · git-rev-parse · git-add | ✅ | **Applied** | AC-8's committed-revision default is `git show REV:<path>`; Question 8 is precisely the *"is this even a repository"* preflight this citation warns about |
| 25 | RES 1 — Google Drive troubleshooting | ✅ | **N/A** | Transport mode is TFW-61. AC-8's quiescence rule is prose in the guide, not a sync assumption |
| 26 | RES 1 — OneDrive sync troubleshooting | ✅ | **N/A** | Same boundary as 25 |
| 27 | RES 1 — Dropbox conflicted copies | ✅ | **N/A** | Same boundary as 25 |
| 28 | RES 1 — gsd-pi · BMAD · Hermes · Spec Kit · OpenSpec | ✅ | **Applied, as counter-evidence** | Every one of them ships its tooling *inside* the artifact it distributes. That comparison is the strongest available argument for `.tfw/scripts/` over the sync-table alternative rec 1 offered as a fallback |
| 29 | RES 2 — git-interpret-trailers · git-log · git-merge-base | ✅ | **N/A** | Phase A's L3 landing-completion derivation. Untouched here |

### New items the coordinator did not cite

| # | Source | Item | Why it belongs |
|---|---|---|---|
| N1 | `.tfw/conventions.md` §10.4 | YAML and Markdown template naming is `lower_snake_case`; uppercase is reserved for project-root and `.tfw/` framework docs | Decides Inconsistency 1. The TS's `team_README.md` does not comply and no §7.2 row covers naming |
| N2 | `.tfw/conventions.md` §11 Design Rules | Workflow instructions ≤ 1200 words; enforcement-critical values inline | Governs Recommendation 1 — five ACs land in one 835-word file. Not in §7.2, and it is the binding constraint on how AC-2, AC-6, AC-7, AC-9 and AC-10 are written |
| N3 | `.tfw/conventions.md` §10.3 File Classification | `build.*` and `task_containers` are **project** sections that an update preserves | Recommendation 2's delivery consequence: a preserved section keeps a stale path forever, so the guide must name it by hand. This is F1's class recurring in the config, and no §7.2 row reaches it |
| N4 | `.tfw/templates/journal_event.md` | Closed `kind` vocabulary; the timestamp is read from the clock | The F9 ruling's basis — the vocabulary stays closed and the canon states some artifacts have no event. Cited because AC-14's fourth bullet asks me to write that rule into the canon |

---

*ONB — TFW-60 / Phase AA: Portable Delivery | 2026-08-27*
