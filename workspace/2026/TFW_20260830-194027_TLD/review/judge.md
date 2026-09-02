# Judge — "Is the quality sufficient?"

> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | All eleven ACs verified against artefacts, not declarations — verify.md V1–V25 and the map.md TS↔RF table. AC-1 `diff` empty and `md5` reproduced (V1) · AC-2 census re-run, 33 hits, per-line classification accurate (V6) · AC-3 search run verbatim, **243** (V3) · AC-4 the three outcomes present in all three canonical sites (V2, V4, V5) · AC-5 scan re-run, only prohibitions remain (V7) · AC-6 suite green, 220 built pages resolve, snapshot page exists (V15, V16, commands 1/9/10) · AC-7 all eight points read against the written step (V17) · AC-8 all six points, plus the safety heading confirmed in the named project (V17, C9) · AC-9 net −1, config diff is one value, `.tfw/scripts/` untouched (V23) · AC-10 33 copies byte-identical, both marker blocks, `VERSION` 2.1.0 (V20–V23) · AC-11 all three commands re-run clean (commands 1–3). HL DoD 1–13 each map onto one of these; DoD 9 was dropped by amendment A1 and DoD 13 replaced it. **AC-3's canonical text is met — the defect in row 9 is in delivery, not in the AC** |
| 2 | **(a) Purpose Check** — is this what we set out to do? · **(b) Design soundness** | ✅ / ✅ | **(a)** See *Purpose Check* below — aligned. **(b)** Sound against all seven HL §7 principles, and soundness here is mostly *restraint*. P1 (subtraction is the deliverable): net −1, verified as a census, not asserted. P2: one write, and the heading that carries the search key was deliberately **not** renamed (RF §2 decision 5) — renaming it would have emptied the replacement across the whole corpus with every test still green. P3: three outcomes and no fourth, with `pending` correctly typed as a waiting state rather than smuggled in as a fourth. P4: the channel is closed, not filtered harder — the design answers `constraint.md` F3's four-month-old finding by removing the section rather than strengthening the filter that had already failed. P5: the seal is a `git mv`, so byte-identity is a fact the log shows rather than a claim a header makes. P6: migration step 6 contains no command at all — *"Move it however your project moves files."* P7: one release, every consumer, including the **adapter template** nobody had listed. The one design element I would have pushed back on — a new checklist row, a new file, a config key — is absent in every case |
| 3 | **Debt disposed** | ✅ | Nine rows in REVIEW §5, every one disposed. **1** `pending — owner` (RF O1, the Windows frontmatter leak — the identifier grammar in `conventions.md` §229–246 requires the owner to approve title **and** abbreviation *before a directory is created*, so a task directory cannot exist yet; title and ABBR are proposed in §5 and the row converts to `promoted` on approval, keeping the task open, which it is). **8** `not material`, each carrying its ruling and its reason on its face — none is a bare label. **0** `→ backlog`, **0** *"someone should open a task"*, **0** undisposed. What each disposition names: row 1 names an owner decision that is being asked for now, not a queue; rows 2–9 name nothing because `not material` is a ruling, not a pointer, and each states why. Six of the nine were the executor's own Observations; three are this review's findings (verify.md D2, D3, and the O2 word-count measurement) |
| 4 | Style & standards | ✅ | Reference format per `compilable_contract.md` §2 throughout; content language `en` as configured; identifier and journal grammars correct (V25); templates followed section-for-section. Naming: `DEBT-SNAPSHOT.md` copies `BOARD-SNAPSHOT.md` exactly, including its no-manifest-row shape — the `conventions.md` §10.4 uppercase question is raised honestly as O4 rather than papered over. **One measured breach**, and it is the rule that is out of date rather than the file: `review.md` is 1 708 words against §11's ≤1 200 — but so are `init.md` (2 032), `plan.md` (1 702) and `handoff.md` (1 452). Four of ten workflows breach a rule nothing enforces. The executor recorded it in the CHANGELOG's *Known open* and refused to cut the disposition gate to fit a word count, which is the right call: §5 row 2 rules it not material and says why |
| 5 | Observations collected | ✅ | Seven, and the quality filter holds — not one is filler. O1 is a real rendering defect on every task-glob page, visible in the task's own screenshot. O5 is the sharpest: it names a wording gap **in the mechanism this task just shipped**, found by the executor walking their own gate, and it cost me nothing to resolve because it was written down. O7 restates a repeatedly-evidenced gap (`TD-110`) and correctly declines to fix it with a new script. O3, O4 and O6 are inherited or deliberate and are labelled as such. No observation is used to smuggle in unrequested work |
| 6 | RF completeness (§7-9) | ✅ | §7 six Fact Candidates, all High, each traced to a dated coordinator ruling rather than to the executor's own opinion — the Human-Only Test holds for all six. §8 four Strategic Insights, each with an explicit **Implication** line; S2 and S3 are genuinely load-bearing (see row 9's counterfactual and RF §2 decision 5). §9 three ASCII diagrams — before/after of where debt is written, the `TD-N` resolution path, and the source→copy map with the un-listed template row called out. Quality, not just presence |
| 7 | Evidence completeness — does the evidence **exist**? | ✅ | Twelve items for eleven ACs plus DoF 3. Every TS Evidence field is covered. Three named artefacts all exist and were opened: `disposition_walk.md` (7 140 B), `dry_run_receiving_projects.md` (9 177 B), `td_citation_resolves_to_snapshot.png` (66 827 B). Statuses are valid, and **all four N/A are the status the TS itself assigns** — checked against the TS text, not taken on the executor's word (verify.md Evidence Verification). The Trust Protocol's *challenge the N/A* row was applied and the N/As survive it |
| 8 | Evidence sufficiency — does the evidence **establish the claim**? | ✅ | The green signals are load-bearing rather than decorative. `diff`-empty plus a reproduced `md5` at a **named revision** establishes AC-1 far better than a header assertion would. The search returning 243 establishes AC-3's live half — a search that returned nothing would have replaced a registry with a dead end, and the TS says so. `disposition_walk.md` establishes AC-4 *against* the executor's interest: six of ten came out `not material`, and that number is stated first and argued in both directions rather than buried. **What it does not establish, and does not claim to:** one walk is not a firing rate, and the RF says so in those words. **One evidential gap, immaterial:** the screenshot has no address bar, so on its own it does not prove the click landed on the snapshot — the inline transcript names the URL and title, and I confirmed independently that `site/tasks/DEBT-SNAPSHOT/index.html` exists, that `site/reference/tech-debt` does not, and that 220 built pages link to the former |
| 9 | Backward compatibility | ❌ | **`$0` in `review.md`'s new search block collides with the Claude Code slash-command argument placeholder.** The downstream consumer is `/tfw-review` itself. Invoked as `/tfw-review <path>`, the harness substitutes both `$0` occurrences with the argument before the text reaches the agent, and the search arrives unrunnable; invoked bare, `$0` resolves empty and the awk program is a syntax error. **Reproduced first-hand in this session** — verify.md D1 quotes what actually arrived. New in this task: no workflow at `c153895` carried a numeric `$N`, and the pre-existing snippets in `config.md` and `update.md` use named variables the mechanism does not touch. The Codex path is unaffected (its skill is a pointer to the source file); `.agent/workflows/tfw-review.md` carries the same string and was not tested. **Counterfactual, and it is the point:** RF §2 decision 5 and §8 S3 both argue that when discovery replaces maintenance the discovery key becomes an interface. The same reasoning, applied one layer down to the *transport*, catches this. The canonical file is right and `cmp` fidelity is perfect — the release simply ships its headline mechanism broken to the tool it is read in |
| 10 | Safety | ✅ | One irreversible act — removing a project-root artifact — and it is handled correctly at every step: performed as `git mv` so history survives (`R098` in the diff), byte-identity proven twice against a fixed cited revision, rollback stated in the migration text, and the guide's *If it goes wrong* corrected so it no longer claims blanket additivity. No secrets, credentials or destructive commands anywhere. DoF 3 independently confirmed: all three sibling registries present with months-old mtimes and no snapshot created in any of them (verify.md C8). The safety carve-out itself is conservative in the right direction — it asks a human and does nothing on silence |

## Purpose Check — row 2 clause (a)

**Reference set:** master HL at contract baseline `c153895`, recovered per `conventions.md` §3 rule 15, plus
the Project North Star (`README.md` opening and § How It Works · `NS1` · `NS2` · `NS3`). Not the TS.

**Status: ✅ Aligned.**

**The clause served, quoted:** HL §1 Vision — *"A review records the debt it found in its own task and
writes nothing else… There is no project registry to append to, to prune, or to feel guilty about"* — and
`NS3 — Non-goals`, which forbids TFW becoming *"a maximum-documentation bureaucracy… that measures success
by artifact count."* **The concrete harm at stake, avoided:** an obligatory write into a shared list that
23 of 25 measured projects never read, growing 3.5× faster than anyone closed it, whose only unique column
was a disposition the REVIEW can carry itself — every review paying a second write for a file that
consumed nothing. That harm is removed, and removed by subtraction: maintained root artifacts fall 8 → 7
with nothing created in exchange.

Three tests, each answered:

1. **Excess and adjacency — no.** Nothing was delivered that the clause does not ask for. The three
   candidates I looked for are all absent: no new file, template, script, check or configuration key
   (DoF 5, verified in the diff); no per-task debt artifact (DoF 1, the design the HL exists to reject);
   no rescue of rows from the registry (DoF 2 / amendment A1, and the ONB's self-reported structural read
   was ruled and bounded by the coordinator before execution). The one out-of-TS file — `test_integration.py`
   — is a consumer of the retired path that AC-6 required to pass, not an adjacency.
2. **Deferral confession — no.** Nothing in the RF or the TS names a different home for this work. The
   opposite: the executor closed two un-gated implications found by the dry run *in the prose* rather than
   reporting them onward, and the one thing genuinely left open — O2's word count — is recorded in the
   CHANGELOG's *Known open* under its own name rather than shipped as if solved.
3. **Materiality — the row 9 finding is material, and it is not a purpose failure.** `$0` breaks the
   delivery of the mechanism, not its design; the vision is served by the design and the fix is one line.
   A wording objection could not ground a block, and this is not one — but it belongs to backward
   compatibility, which is where it is recorded.

**Reference set internal consistency:** checked. Baseline HL §1/§3/§5/§6/§7 and the north star clauses are
mutually satisfiable — subtraction, structural enforcement and verbatim preservation all point the same
way here, and amendment A1 narrowed the contract without putting any clause in tension with another. **No
contract defect.**

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D53 — an *optional* evidence store used 0 of 38 times was made **mandatory** | An *obligatory* registry consumed 0 times is made **history** | **No.** Opposite remedies, one evidence discipline: measure consumption, then act on the measurement. The HL cites it as a mirror case and labels it as such |
| 2 | D37 — exclusive write territories between `/tfw-docs` and `/tfw-knowledge` | `docs.md` loses its debt row | **No.** The split is untouched; only a third territory that was never `/tfw-knowledge`'s is removed |
| 3 | D65 — reverting a result never reverts its trace; a record is never deleted | 121 rows preserved verbatim, 1 659 citations still resolving | **No.** Directly honoured, and strengthened by using a rename rather than a delete |
| 4 | §1 Architecture Map · §3 Legacy & Deprecation | Both updated by this task | **No.** Written by this task and verified in place (verify.md V24) — the map now carries a **Debt** component that says there is no registry, which is the honest shape |

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)? — all ten cite verify.md by finding number
- [x] Every `⚪ N/A` carries a stated reason — no row skipped as a bare ✅? — no row was N/A; all ten were answerable
- [x] Row 2(a): answered against the contract baseline and the north star — never the TS or a Phase HL — with a quoted clause **and** a named harm in one field? — yes, baseline `c153895` recovered by rule 15; the TS was deliberately not used
- [x] Rows 7 and 8 answered separately, with different reasoning? — 7 counts and locates the artefacts; 8 asks what the green signals establish, and names the one thing they do not
- [x] Referenced verify.md findings in DoD assessment? — row 1 cites V1–V25 and commands 1–10
- [x] Row 3: every §5 row disposed, and each disposition names something that exists today? — nine rows, eight `not material` with reasons, one `pending — owner` because the identifier grammar forbids creating the directory before the owner approves the title and abbreviation
- [x] Checked RF §7-9 for presence AND quality (not just existence)? — row 6
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"? — four items checked, none contradicts
- [x] Fact Candidates from RF reviewed — any that need challenge? — all six traced to dated coordinator rulings in the ONB and confirmed against it; none needs challenge. Candidate 3 (*no tool is bound to a TFW role*) was verified independently: the only tool names in the canon are a commit-attribution example and the Codex **adapter**

Stage complete: **YES**
