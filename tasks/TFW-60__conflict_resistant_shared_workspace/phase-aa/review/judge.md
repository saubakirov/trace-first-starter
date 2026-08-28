# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | verify.md V1–V16 and the 15-row TS↔RF table in [map.md](map.md). **14 of 15 AC halves met and independently re-verified**; AC-13 half two is reported ❌ UNMET by the executor and routed to the owner, which is what TS §5 and §7 require of it — *"the executor can close only the first"*, and an RF claiming otherwise *"must be rejected"*. Reporting it unmet is compliance, not a shortfall in the work. Suite re-run here: **253 passed, 1 skipped** against a 220 baseline; all three `--check` subjects exit 0; `mkdocs build` exit 0 in 230.8 s |
| 2 | **(a) Purpose Check** · **(b) Design soundness** | **(a) ✅** · **(b) ✅** | **(a)** Serves master HL §1 baseline *"A TFW workspace lets several humans and agents work on different tasks at the same time"* as realized through DoD 19 — *"An external project completes the update to a released version **from the payload alone** — no file hand-carried from this repository, no edit inside `.tfw/`, and every instruction the release gives names something the receiving project actually has"* — and north star **NS1**, *"another authorized person or agent can … continue without rebuilding the original conversation"*, with the Portability value *"no vendor may become the sole home of project memory."* **Concrete harm at stake:** without this phase a receiving project is instructed by `conventions.md` and the CHANGELOG to run `docs/scripts/migrate_board.py`, a file `/tfw-update` never copies — so continuation requires reconstructing the framework's own tooling by hand, which is the exact failure NS1 names and which the first real external update measured (*"the file copying took minutes; the rest of the session was reconstructing what to do and in what order"*). Three tests, all answered *no*: **excess** — the one out-of-theme rider, AC-12's session naming, is owner-admitted and bounded in TS §6, and the phase's net movement is subtractive (1 created against 2 withdrawn and 3 removed from the flat namespace); **deferral confession** — RF §6 items 3, 5 and 7 name other homes and correctly ship nothing there; **materiality** — no material harm to the value. **(b)** Answered separately: HL §7 principle 5 (*local truth, derived views*) is what makes `--check` report-and-exit, and it is structurally enforced, not asserted — `test_no_check_subject_writes_anything` byte-compares the whole tree across all three subjects. Principle 4 (*stable paths*) holds: AC-4 reports an unmatched directory and never moves or renames it. Principle 9 (*no trace deletion*) holds: 82 historical artifacts and 11 provenance comments verified byte-unchanged (verify.md V16), and every relocation is a `git mv` recorded as `R0xx` |
| 3 | Tech debt documented | ✅ | RF §6 carries seven observations, each naming a file, a type and why it was **not** fixed. Two are decisions the TS explicitly asked to be recorded as decisions (`BOARD-SNAPSHOT.md`'s name; the `phases/` check). Triaged below |
| 4 | Style & standards | ⚠️ **see finding** | `conventions.md` §10.4 naming honoured — `team_README.md` was caught at ONB and the file was then withdrawn entirely. `update.md` at 1165 words is under the §11 ceiling of 1200 and was brought there by deleting duplication, not required content. Commit subjects follow §15: `[claude-code/TFW-60/phase-aa/executor]`, verified in `git log`. **Against that: `.tfw/templates/status.md` ships a self-contradiction and a miscount** — verify.md **D1** and **D2** |
| 5 | Observations collected | ✅ | Quality filter applied below. Six of seven survive; one is downgraded to a recorded decision rather than debt. None is filler — every item names the concrete cost of leaving it |
| 6 | RF completeness (§7-9) | ✅ | §7 seven fact candidates, each with a named human or coordinator source and a confidence — not template filler; #1, #2 and #7 are the owner's own R3 reasoning, #6 is a machine-environment fact no test here could produce. §8 three strategic insights, all execution-derived. §9 three diagrams, and they carry information the prose does not: the payload boundary before/after, the flag collapse, and the board's path to task-local state including the four reconciliation classes |
| 7 | Evidence completeness — does the evidence **exist**? | ✅ | 60 items, **60 artifacts resolve**, 0 missing. Every TS Evidence field is covered. Statuses valid: 58 VERIFIED, 1 DEFERRED with a named blocker and a named closing artifact, 1 N/A with a cited ruling. Eight attachment files all present and all non-trivial |
| 8 | Evidence sufficiency — does the evidence **establish the claim**? | ⚠️ **mostly, with four named gaps** | The strong parts are genuinely strong and I re-derived them rather than reading them: the test counts reproduce exactly (158+95 = 253/1); the AC-1 gate grep reproduces line for line; `parse_board`'s untouchedness holds under an independent diff; the depth defect is observed at three real placements where `parents[2]` would have been wrong twice, once **outside the project entirely**. RF §4's *"checks that failed first, then passed"* table is the right instinct and is the antidote to the DoF pattern it names. **The four gaps:** **D5** — E47's bare *"0 framework files edited inside `.tfw/`"* is contradicted by its own transcript's `1` and reconciled only in a sibling file; **D4** — the `git log --follow` counts are the values at `80c2ed5`, one commit before the declared pin, and TS §6 makes pinning a rule; **D6** — E60's *"as a class"* describes a line-scanning heuristic that a message assembled into a variable escapes; **C2** — `ac3_parser_untouched.txt`'s displayed diff omits the signature line that carries the new parameter. None of the four makes a claim false. All four make a claim looser than its evidence, in a phase whose own DoF names *"a check reported as passing that never ran"* in four forms |
| 9 | Backward compatibility | ✅ | The one deliberate break is `build.verify: --validate → --check tasks`, taken knowingly: AC-9 states the blast radius (this repository and one consumer, both already being touched), states that `2.0.0` is unreleased, and states that the cost grows permanently after. The CHANGELOG's § "Migration from `2.0.0-dirty`" names it as one of exactly two commands that change. Downstream consumers checked: `gen_docs.py`'s `import gen_index` is rebootstrapped and `mkdocs build` exits 0; `iter_task_dirs`'s return type is deliberately **not** changed (D2) precisely because three callers read it; all 22 workflow copies and 11 Codex skills verified byte-identical to their sources; `docs/mkdocs.yml` needed no change and the build proves it. The 11 generated `status.md` provenance comments are left naming the old path on purpose, and the guide tells a receiving project why |
| 10 | Safety | ✅ | No secrets, credentials or network calls introduced. The destructive-operation surface is the point of the phase and it is bounded in the right direction: `migrate_board.py` *"opens no path that already exists, and never renames or moves anything"*, the empty-board refusal is preserved, `--check` writes nothing (asserted by a whole-tree byte comparison), and `find_project_root` **refuses rather than guessing** — *"guessing a root means writing files into a directory nobody chose."* The one live-system risk this phase could have created was writing into the owner's real external project; E48 records that it was read-only and every fixture command ran under the scratch path. No push occurred; no tag was cut |

## Purpose Check — row 2 clause (a)

**Answered above in row 2(a), against the master HL at baseline `2123de1` plus the north star.
Not against the TS, and not against the Phase HL.**

Outcome: **Aligned ✅.** The clause is DoD 19 as frozen by amendment A4, read together with
NS1 and the Portability value; the harm is a receiving project unable to continue without
reconstructing tooling the payload never carried, which the first external update measured
rather than predicted.

**Reference set consistency:** checked, and coherent. The baseline's Phase AA block, DoD 19,
DoF 10 (*"a phase is called releasable while … migration guidance still describe[s] the prior
ownership model"*) and NS1 all pull the same direction. No two clauses require opposite
things. No contract defect.

**A note the outcome does not change.** The phase's declared outcome — *a project other than
this one completes the update from the payload alone* — is **not yet demonstrated**, because
the only run was the author's own clone. That is not a purpose failure: purpose asks whether
this is what we set out to do, and it is exactly that. It is a completeness question, and the
contract answers it deliberately by splitting AC-13 in two and assigning the second half to
the owner. Phase AA is correct work whose final proof is not the executor's to produce.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | **D37** — `/tfw-docs` owns `KNOWLEDGE.md` §1–§3; `/tfw-knowledge` owns `knowledge/*` | RF §6 obs 1: `KNOWLEDGE.md:22` still names `docs/scripts/gen_index.py`; the executor did not write it | **No — the opposite.** D37 is why the executor stopped, and AC-1's gate text was amended at ONB Q5 to name the hit so the RF could not report a green gate over a red one. This is the ownership split working |
| 2 | **D65** — reverting a result never reverts its trace | 82 historical artifacts, 11 provenance comments, `KNOWLEDGE.md`'s two historical rename rows: all left byte-unchanged | No. Verified in verify.md V16 |
| 3 | **D55** — minimal commit attribution | Commits carry `[claude-code/TFW-60/phase-aa/executor]` | No. Verified in `git log` |
| 4 | **D59** — capability claims keep boundaries apart | The `v2.0.0-dirty.2` tag was **not** cut; the fixture was pointed at a commit SHA | No. `git tag -l` confirms |
| 5 | **D31, D50** — filesystem state and locality | `--check` reports and exits; nothing this phase ships writes task state | No |

**One item goes stale as a result of this phase and is correctly left to its owner:**
`KNOWLEDGE.md:22`'s architecture-table path. It is the single open thread and it has a named
owner, a named workflow and a declared reason.

## Findings

### F1 — the payload contradicts itself on the rule this phase wrote · **Medium** · verify.md D1

`.tfw/templates/status.md:92`:

> Normalizing such a value to a declared one is prohibited.

That is, verbatim, the sentence commit `f14f744` **rewrote** in `glossary.md` — the old text
was *"**Normalizing such a value to a declared one is prohibited**"* — and replaced in
`conventions.md` §5 with a two-act table: *migration never normalizes, an accountable owner
may resolve through a recorded `transition` event carrying `from: UNDECLARED`.*

The executor recognised that exact wording as the defect, fixed two copies, and left the
third. TS §5 AC-14's fourth bullet states the harm in advance: *"currently the prohibition
reads as absolute and projects will either strand tasks or resolve them without a trace."*
That harm now ships — in the canonical carrier template, which is the file a person
hand-authoring `status.md` actually opens, in a phase whose entire subject is that a
receiving project has only the payload and the payload must not mislead it.

This is not a wording objection. Two shipped normative files give a reader opposite
instructions about the same act, and the reader most likely to hit it is the one the phase
was written for. `.tfw/CHANGELOG.md` announces the corrected rule under **Canon**, so the
release states one thing and the template it ships states another. The fix is one sentence in
a file this phase already modified.

Secondary, same file, line 78: *"the four keys that are never prose — id, lifecycle, owner,
authority, created, updated"* lists **six** keys (verify.md D2). Cosmetic on its own; it sits
in the paragraph AC-5 wrote specifically so a person gets the carrier right by hand.

### F2 — four claims looser than their evidence · **Low** · verify.md D4, D5, D6, C2

Each is small; the class matters because TS §7 makes it a named failure mode.

- **D5** — E47 reports *"0 framework files edited inside `.tfw/`"*; `fixture_run.txt` prints
  `framework files edited inside .tfw/: 1`. The reconciliation is real, correct and one file
  away in `fixture_report.md` (a `__pycache__` `.pyc`, and it produced a genuine finding that
  the guide now carries). The EV **row** carries the bare number.
- **D4** — RF and EV both declare *"Pinned at `1079020`"*; RF §1's `git log --follow` counts
  are the values at `80c2ed5` (9 and 6 at the pin, not 8 and 5). TS §6: *"Evidence is measured
  at a pinned commit and never against `HEAD`."*
- **D6** — *"Runtime output is ASCII **as a class**"* describes a line scanner that toggles on
  `print(` / `SystemExit(` and resets on a line ending in `)`. It caught five real occurrences
  and is worth keeping; it does not enforce the class.
- **C2** — `ac3_parser_untouched.txt` reports *"changed code lines: 2 (one replacement)"* and
  shows only the locator. The signature line also changed, to carry the new parameter. I
  re-diffed the function independently and the substance holds: every row-reading line is
  byte-identical.

### F3 — the RF's Modified count is not the count of its own rows · **Low** · verify.md D3

RF §1 heads its table **"Modified — 25"**, the figure `census.md` reaches by classifying the
four scripts as *moves*. The RF's table then lists those same four scripts as Modified rows,
plus two the census does not count. Distinct paths in the table: roughly 31.

No budget limit is crossed under the census's declared method, and the census was raised to
the coordinator **before acting**, which is the return-to-coordinator rule working exactly as
designed. But the TS's own basis for the classification did not survive execution: it
predicted the scripts would *"relocate rather than get rewritten … cost a move and their path
constants"*, and `gen_index.py` changed **507** lines and `migrate_board.py` **246**. That is a
coordinator estimate the work invalidated, not an executor error — recorded here so the next
phase's budget table does not inherit the same premise.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Every `⚪ N/A` carries a stated reason — no row skipped as a bare ✅? — no row was answered `⚪ N/A`; rows 9 and 10 are answered on substance, not waived
- [x] Row 2(a): answered against the contract baseline (`2123de1`) and the north star — never the TS or a Phase HL — with a quoted clause **and** a named harm in one field?
- [x] Rows 7 and 8 answered separately, with different reasoning? — 7 asks whether 60 artifacts exist (they do, all of them); 8 asks whether they prove what they are offered to prove, and names four places where they prove slightly less
- [x] Referenced verify.md findings in DoD assessment? — row 1 cites V1–V16 and the re-run commands
- [x] Checked RF §7-9 for presence AND quality (not just existence)? — row 6 assesses each section's content, not its heading
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"? — five items checked, no contradictions; one item goes stale and is correctly routed
- [x] Fact Candidates from RF reviewed — any that need challenge? — seven reviewed. **None challenged.** #5 and #6 are checkable and check out (the fixture corpus, and the cp1252 console that produced the blocker in `fixture_run.txt`). #1, #2 and #7 are the owner's own words at TS R3 and are the most valuable of the set

Stage complete: YES
