# REVIEW — TFW-56: Remove the Review Mode Axis

> **Date**: 2026-08-13
> **Author**: Reviewer (Claude Code)
> **Verdict**: ✅ APPROVE
> **RF**: [RF TFW-56](RF__TFW-56__review_mode_removal.md)
> **TS**: [TS TFW-56](TS__TFW-56__review_mode_removal.md)
> **HL**: [HL-TFW-56](HL-TFW-56__review_mode_removal.md) — 🔒 FROZEN, re-frozen after A1-A5, A7
> **EV**: [EV TFW-56](evidence/EV__TFW-56__review_mode_removal.md) — 16 items, all verified by the reviewer
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> This file is a synthesis of stage findings. Reference stage files for raw evidence.

---

## 1. Map

The `code / docs / spec` review-mode **selection** is gone in every place it lived: the
`.tfw/workflows/review/` folder and its three mode files, the `review.md` mode step and its 🛑 WAIT
gate, the `tfw.review.default_mode` key in two config files, four template fields, one propagation
row and six adapter copies. The checks the selection was gating were promoted into the universal
Judge checklist, which moves from 7 rows to 10 — seven of the eight gated rows promoted, one dropped
as a proven duplicate, none silently lost. `review.md`'s steps renumber 0-7 contiguously, so Step 0
is Session Naming for the first time and TD-106 closes by deletion rather than annotation.

Two design calls beyond the TS carry the result. **U2 was split into two separately quotable
clauses** — (a) mapping integrity, (b) design soundness — so TFW-53 Phase C can replace clause (a)
without silently evicting the promoted S3; a single fused sentence would have taken it out
invisibly. **The three orphaned verify actions were migrated, not declined**, which AC-4 also
permitted, on the ground that they are the Verify-stage half of the same 16.1% convergence that
Judge row 8 is the Judge-stage half of.

Scope: 20 modified + 3 deleted framework/root files + 1 new evidence artifact, net LOC −39. One
anomaly is self-reported and real: the three deletions were swept into a concurrent session's commit.

## 2. Verify

**Ratio: ⌈24 × 0.42⌉ = 10 required. Opened 24 of 24 — 100%**, escalated on discrepancy V-D1.
Raw log: `review/verify.md`.

| # | What was checked | Result | Evidence |
|---|-----------------|--------|----------|
| 1 | The mode folder and its three files | ✅ | `ls` fails; absent from `HEAD`; content recovered from `6c3c506` for the coverage audit |
| 2 | `review.md` steps 0-7 contiguous, Step 0 = Session Naming, no mode step or WAIT | ✅ | Headings re-counted; only surviving "mode" is the Role Lock phrase at L7 |
| 3 | Every `review.md` step reference repo-wide | ✅ | Swept `.tfw/`, adapters, `docs/`, `knowledge/`, root — **all resolve, none stale**. DoF-3 clear |
| 4 | `judge.md` — ten rows, no `Mode:`, rates carried, explicit-N/A structural | ✅ | Baseline had 7 rows + `Mode:` + Mode-Specific section; shipped file has 10 rows, `grep -c "Mode"` → 0, three N/A enforcement sites |
| 5 | `verify.md` Claim & Source Checks | ✅ | All three orphaned actions present as unconditional, with table and Checkpoint item |
| 6 | `REVIEW.md` §3 against `judge.md` | ✅ | 10/10, same order. Baseline had **6** rows — the pre-existing 0.8.8 gap is repaired as AC-5 requires |
| 7 | Both config files | ✅ | `default_mode` absent from both `tfw.review` blocks; `min_verify_ratio: 0.42` with its comment byte-identical and its `# ← FRAMEWORK` annotation intact |
| 8 | `config.md` propagation | ✅ | One `review` row; its `Step 2: Verify` pointer opened and confirmed |
| 9 | `conventions.md` §14, `glossary.md` | ✅ | Anti-pattern present and permits retention on consequence if the reason is written into the row; Reviewer heading disambiguated; Principles Check pointer corrected to Step 3 |
| 10 | Six adapter and entry-point copies | ✅ | Five `diff` runs re-run independently — **all empty**; sixth read in full, WAIT-gate line replaced with the four gates that remain |
| 11 | `VERSION`, CHANGELOG, TECH_DEBT, README | ✅ | `1.1.0`; `### Removed` names `tfw.review.default_mode` with upgrade instructions; TD-106 closed with the reason; Task Board current |
| 12 | **Coverage audit against the deleted files** | ✅ | Counted independently from `6c3c506`: **8** checklist rows, **10** verify entries → **8** distinct actions. Both RF tables match exactly, including a fourth `docs` action neither HL nor TS enumerated and the executor accounted for anyway |
| 13 | **The grep gate, re-run** | ✅ | Zero matches, exit 1. The executor's finding holds: `review/{code` matched nothing at baseline either — a quarter of the acceptance test could never fail |
| 14 | **Build gate, re-run** | ✅ | `python -m pytest docs/scripts/ -q` → **68 passed** |
| 15 | S1-vs-U7 dry-run, traced to source | ✅ | All three findings verbatim in TFW-53/A's own EV file (L71, L185, L129); both attachments resolve. Rows 7 and 8 produced different answers from different reasoning |
| 16 | History and attribution | ✅ | `68a8be8` touches no `tasks/` path but TFW-56's own three artifacts; `git show --stat fbdf443` confirms the leak exactly as described |
| 17 | HL §7.2 knowledge citations | ✅ | 26 citations, 8 sampled, **0 hallucinations** |

**Discrepancies:** one Low (V-D1, §4 below). Two non-defects recorded so the review does not read as
having missed them: `conventions.md:466` left by decision (V-D2), and the `Review Mode` file count
drifting 41 → 43 because this task's own RF and EV contain the string (V-D3).

## 3. Judge

> Ten rows, matching `review/judge.md` one-for-one and in the same order.
> `⚪ N/A` is permitted on any row and requires a stated reason — a skipped row is never a bare ✅.
> **This is the first review filled under the checklist this task ships.**

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ✅ | Twelve TS ACs and fifteen HL DoD items each cross-checked against a file, not a claim |
| 2 | Philosophy aligned — mapping integrity + design soundness | ✅ | **(a)** all eight TS §3 principle mappings resolve to ACs that were met. **(b)** the U2 clause split and the migrate-not-decline call both protect the *next* task rather than simplify this one |
| 3 | Tech debt documented | ✅ | Eight observations with file, line, type and consequence; two of them self-incriminating |
| 4 | Style & standards | ✅ | Naming, RF §1-§9 complete, EV template followed, commit subject grammar correct, CRLF discipline held |
| 5 | Observations collected | ✅ | Six real, two knowledge-layer corrections. No filler |
| 6 | RF completeness (§7-9 present) | ✅ | Five fact candidates with sources, three insights each carrying an Implication, three diagrams that carry the argument rather than decorate it |
| 7 | Evidence completeness — does it exist? | ✅ | 16 rows, 4-status vocabulary only, every VERIFIED row carrying a command with output or a named-file reading; all seven N/A quote TS §5 verbatim |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | **One finding (Low).** RF §3 AC-8 presents the gate as `grep -rn "review mode" .tfw/` → 0 matches; run as written it returns two hits in the new CHANGELOG entry. The `--exclude=CHANGELOG.md` flag is present in EV §E6 and was dropped in the summary. AC-8's actual criterion — *every remaining hit means the same thing* — holds. Plus one partial: the `git log -p` lockstep behind the `tfw.version` bump was not re-run end to end |
| 9 | Backward compatibility | ✅ | Inert key with named upgrade instructions; every step-number anchor swept and resolving; 43 existing REVIEW files untouched; docs pipeline green after three pages disappear; no TFW-53 frozen DoD made unlandable |
| 10 | Safety | ⚪ N/A | No secrets, credentials or executable paths. The one irreversible operation is a fully recoverable `git rm`. **Reason it is not a bare ✅:** trace safety is not clean — a concurrent session's broad `git add` captured this task's staged deletions, so a destructive operation landed under the wrong task's name. Triaged as TD-144, not scored against this RF, which disclosed it |

## 4. Verdict

**✅ APPROVE**

The work does what the frozen contract says, and the verification is reproducible rather than
asserted. Every claim I re-ran came back matching: the grep gate (zero, exit 1), the build gate (68
passed), the five parity diffs (all empty), the eight-row and eight-action coverage audit rebuilt
independently from the deleted files at `6c3c506`, and all three dry-run findings traced verbatim
into TFW-53/A's own evidence file. Nothing in the diff touches anything TS §2 puts out of scope.

Three things raise this above a compliant deletion.

1. **The coverage accounting is load-bearing and it survives an independent rebuild.** This task's
   real risk was losing the strongest check while looking like simplification — HL Risk 7 names it,
   and the first version of the contract would have dropped roughly two thirds of the 16.1% signal.
   I counted the eight rows and the eight distinct verify actions from the deleted files myself and
   opened each stated destination. The tables match exactly, including one `docs` action that neither
   HL nor TS enumerated and the executor homed anyway because DoF-1 covers every action, not only the
   three that were named.
2. **The U2 clause split is the right call and it was not asked for.** TS §6 said *sharpen, do not
   restructure*. A fused sentence would have satisfied that instruction and let TFW-53 Phase C evict
   the promoted S3 without either task's DoD noticing. Two separately quotable clauses cost nothing
   now and keep Phase C landable. The one residual line Phase C's TS needs is named in RF obs. 2 and
   carried into tech debt as TD-145.
3. **The executor reported two findings against itself.** The mandated acceptance grep contained a
   dead alternative — `review/{code` never matched anything, at baseline or after — which is
   literally the anti-pattern this task adds to `conventions.md` §14. It ran the command as written
   rather than quietly fixing the AC, recorded the exit status, and put a wider sweep beside it as
   separate evidence. Same with the commit leak: correct outcome, wrong attribution, disclosed in
   three places and left unrepaired because rewriting another session's commit is not an executor's
   call. That is the judgement the framework wants.

**The one finding, and why it does not change the verdict.** RF §3 AC-8 states its gate as
`grep -rn "review mode" .tfw/` → 0 matches. Run exactly as written it returns two hits, both in the
1.1.0 changelog entry describing the removal. The EV file records the correct command with
`--exclude=CHANGELOG.md`, so the work was done properly and the RF dropped the flag when summarising.
TS AC-8's gate is not "zero matches" — it is *every remaining hit means the same thing*, and both
hits mean the removed axis, in the one file DoD-15 forbids rewriting. No DoF item is triggered: DoF-9
concerns the AC-12 grep, which **is** recorded with its output and its exit status. This is a
one-line reporting inaccuracy in a summary, against a claim that verifies. Carried as TD-146, Low,
following the TD-137 precedent for RF-internal wording errors with no artifact impact.

**HL §8 directives discharged.** Two items were explicitly deferred *to TECH_DEBT at review time*:
the `min_verify_ratio`-lost-on-upgrade defect (RES FC5) and the general `update.md` removed-key rule
that amendment A5 was narrowed away from. Both are registered below as TD-147 and TD-148.

### If REVISE — items to fix:
Not applicable.

### If REJECT — fundamental issues:
Not applicable.

## 5. Tech Debt Collected

> **Source format**: Use reference patterns (compilable_contract.md §2).

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| TD-144 | RF TFW-56 obs. #1 | **High** | `.tfw/conventions.md` §4 | Two agent sessions shared one working tree and index; a broad `git add`/`commit -a` in the TFW-53/B session captured TFW-56's staged mode-file deletions into `fbdf443`. Verified in `git show --stat fbdf443`. Outcome correct, attribution wrong — recovering *"when did TFW-56 delete the mode files"* from TFW-56's commits returns nothing. TFW has no convention requiring explicit-path staging. In a framework whose thesis is that traces are the product, a silent trace transfer is the highest-consequence item here | → backlog, **priority**: add a staging rule to conventions §4 Commit Attribution |
| TD-145 | RF TFW-56 obs. #2 | Med | `.tfw/templates/review/judge.md` row 2 | TFW-53 Phase C's frozen DoD-20 replaces the *mapping integrity* check in Judge row 2, and its context block names that row as the target. The promoted S3 *design soundness* (4.5%, six hard ❌) now lives in clause (b). Clause (b) was deliberately written as separable so Phase C **can** replace clause (a) and leave it — but nothing in either task's frozen DoD requires it to | → **Phase C TS**: one line preserving clause (b) |
| TD-146 | REVIEW TFW-56 finding, judge row 8 | Low | `tasks/TFW-56__review_mode_removal/RF__TFW-56__review_mode_removal.md` §3 AC-8 | The AC-8 summary states `grep -rn "review mode" .tfw/` → 0 matches; run as written it returns two hits in the new CHANGELOG entry. The EV file carries the correct `--exclude=CHANGELOG.md` form. RF-internal, no artifact impact — AC-8 passes on its own criterion (*every hit means the same thing*) | → backlog (correct the line at `/tfw-docs`, TD-137 precedent) |
| TD-147 | HL TFW-56 §8, RES iter1 FC5 — **deferred to review time by the HL** | Med | `.tfw/workflows/update.md`, `.tfw/project_config.yaml` | `min_verify_ratio` sits inside a `tfw.review` block that `update.md` marks *framework → update*, so any project that tuned 0.42 loses its value on upgrade. Pre-existing, explicitly **not** caused by this task — AC-6 proves it was not made worse | → backlog |
| TD-148 | HL TFW-56 §8 / A5 narrowing — **deferred to review time by the owner's ruling** | Med | `.tfw/workflows/update.md` Step 3 | `update.md` triages at **file** granularity and has no rule for removed config **keys**, so a removed key falls through its 🟢/🟡/🔴 categorisation and is silently orphaned in existing projects. A5 was approved narrowed to the CHANGELOG clause only; the general framework rule was deferred to its own item | → own task |
| TD-149 | RF TFW-56 obs. #5 | Med | `RELEASE.md` §3 | The MAJOR row's *"required file removed"* clause classified this task as MAJOR while the owner ruled it MINOR on observable impact. As written, deleting any unused framework file forces a major version — which penalises deletion in a framework whose whole method is deletion. The written rule and the applied standard have now visibly diverged once | → backlog |
| TD-150 | RF TFW-56 obs. #7 | Med | `.tfw/workflows/config.md` L101-112 | The Adapter Sync block lists four `cp` commands to `.agent/workflows/` only — it omits `.claude/commands/` entirely and omits `review.md` from both. The workflow that exists to prevent adapter drift documents half the adapters; all copies have stayed identical by discipline, not by procedure | → backlog |
| TD-151 | RF TFW-56 obs. #6 | Low | `.tfw/conventions.md` L466 | §11 Design Rules: *"Mode files loaded at Step 2, not at start"*. Phrasing inherited from D42; still true of research (`research/base.md` Step 2), so editing it was correctly declined as out of scope. A reader who knows the D42 lineage reads it as a dangling reference | → backlog |
| TD-152 | RF TFW-56 obs. #8 | Low | `.tfw/templates/review/judge.md` rows 9-10 | S2 (8.5%) and S4 (4.0%) sit at positions 9 and 10. HL §7.2 #25 records that LLM judges are order-sensitive and that tail positions are the weakest. The order is HL §3.1's frozen after-diagram and was implemented as specified; the chosen mitigation is the structural explicit-N/A grammar, not reordering | ⬜ Monitor — re-measure once the ten-row checklist has a corpus |

**Not promoted to TECH_DEBT — routed to the knowledge layer instead:**

| Source | Item | Route |
|--------|------|-------|
| RF obs. #3 | `knowledge/process.md` F19 — both halves now historical: the step is deleted and Step 0 is Session Naming | `/tfw-knowledge` |
| RF obs. #4 | `KNOWLEDGE.md` L74 (D42 revoked, row does not say so) and L173 (Legacy row still describes mode files) | `/tfw-docs` |

## 6. Traces Updated

- [x] README Task Board — status updated to 📚 KNW
- [x] HL status — single phase, task complete
- [ ] project_config.yaml — initial_seq: not applicable to this task
- [x] Other project files — TECH_DEBT.md appended with TD-144…TD-152
- [x] tfw-docs: **Applied** — §1 Architecture Decisions: **D61 added**, D42 struck through and marked revoked, D41 and D46 annotated so only their mode clauses die. §2 Key Artifacts: TFW-56 row added. §3 Legacy & Deprecation: new row for the deleted axis; the two stale rows describing "6 universal + 2-4 mode-specific" and "mode selection (code/docs/spec)" marked superseded. §1 Architecture Map needed no change — it never named the mode files
- [x] tfw-knowledge: **Applied — 18 candidates, 0 admitted, 1 existing fact corrected.** Owner ruling 2026-08-13: a fact qualifies only if it comes from the owner's head **and** is not already written anywhere in the repository. Every candidate failed the second half — the four philosophy items live in HL §11, HL §12 and D61; the release-standard item lives in ONB Q1 and TD-149; the blocking-question item was an agent's inference about the owner, not the owner's words; the shared-index item was found by an agent with `git` and belongs in a convention (TD-144), not in knowledge. `knowledge/process.md` F19 was corrected because it asserted a step that no longer exists. Fact counts unchanged at 105

> fact-candidates: processed 2026-08-13

> **Neither marker was pre-marked N/A.** This task revokes a recorded architecture decision (D42) and
> invalidates a knowledge fact (F19); closing without running both would have left the knowledge layer
> asserting a mechanism that no longer exists.

## 7. Fact Candidates

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | process | A checklist row can be validated at review time by filling it against an **archived** RF/EV/REVIEW triple before it ships. TFW-56 used TFW-53/A as the subject and made *"rows 7 and 8 produced different answers"* the pass condition of AC-2 rather than a caveat. The dry-run found three real issues that the archived review — scored under `spec` mode, both mode rows ✅ — did not surface | RF TFW-56 §2 decision 2, EV §E3; reproduced by the reviewer against the source EV file | High |
| 2 | process | A verdict-carrying claim can be true in the evidence file and overstated in the RF summary that cites it. Here the EV recorded `grep … --exclude=CHANGELOG.md` and the RF summary dropped the flag. The EV layer caught what the RF line did not — which is the argument for the two artifacts being separate | REVIEW TFW-56 judge row 8, verify.md V-D1 | High |
| 3 | constraint | A grep gate authored from memory rather than run once against the pre-change tree can ship an alternative that matches nothing and still read as a complete sweep. `review/{code` in TS AC-12 never matched — the real string was always `review/{mode}.md`. Confirmed by the reviewer at the `6c3c506` baseline | RF TFW-56 §7 FC4, EV §E7; reproduced | High |
| 4 | environment | Concurrent agent sessions in this project share one git working tree **and one index**. A broad `git add`/`commit -a` in either captures whatever the other has staged. Verified: `fbdf443` (TFW-53/B) carries TFW-56's three mode-file deletions. Mitigation that worked: stage by explicit path only | RF TFW-56 §7 FC1, EV §E9; reproduced in `git show --stat` | High |
| 5 | philosophy | The owner's applied release standard is **observable consumer impact**, not category of change: `1.1.0` was chosen over the `2.0.0` that `RELEASE.md` §3's *"required file removed"* clause prescribes, because nothing downstream breaks. The written rule has now visibly diverged from the applied one once | RF TFW-56 §8 S1, ONB Q1 (User, 2026-08-13) | High |
| 6 | philosophy | The HL amendment channel absorbed a **refuted premise** without the task dying: research inverted the empirical claim §3 rested on, seven amendments corrected the promotion set, and the frozen §3.1 diagram still told the executor exactly which ten rows in which order. First live case of TFW-53's contract mechanism doing what it was built for — a measurement arriving *after* the freeze produced an unambiguous instruction rather than a judgement call | RF TFW-56 §8 S3, HL §12 A1-A7 | High |

> **Source format**: Use reference patterns (e.g., `RF TFW-18`, `D24`). See compilable_contract.md §2.

---

*REVIEW — TFW-56: Remove the Review Mode Axis | 2026-08-13*
