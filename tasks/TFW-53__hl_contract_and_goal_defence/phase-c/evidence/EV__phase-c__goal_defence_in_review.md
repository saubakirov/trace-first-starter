# EV — TFW-53 / Phase C: Goal Defence in Review

> **Date**: 2026-08-13
> **Author**: Executor (Claude Code)
> **Task**: TFW-53
> **TS**: [TS Phase C](../TS__phase-c__goal_defence_in_review.md)

---

## Environment

| Field | Value |
|-------|-------|
| OS | Windows 11 Pro 10.0.26200 |
| Language / Runtime | Python 3.x — `pytest`, `mkdocs` (the docs pipeline is the only consumer of every file this phase changes: Source Manifest rows 4, 5, 12, 13, 14) |
| Deploy target | local docs build, `docs/mkdocs.yml` |
| CI / Pipeline | local; `.github/workflows/docs.yml` consumes the same build |
| Repository state | branch `master`, HEAD `2370082` at collection time. **A concurrent TFW-55 session held `README.md` and `tasks/TFW-55*` throughout** — every command below was scoped to this phase's paths |
| Reference sets used | HL-TFW-53 at frozen baseline `e8ee76e`; replay corpus recovered with `git show 721ca15:<path>` and `git show 9e19a4f:<path>` |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Row 2 clause (a) is the Purpose Check; the mapping-integrity check is gone from **both** live sites; the checklist is still ten rows; clause (b) survives with its 4.5% rate and separate answer | local repo | **VERIFIED** | `grep -rc "mapping integrity" .tfw/templates/review/judge.md .tfw/workflows/review.md` → `judge.md:0`, `review.md:0`. `grep -c "^| [0-9]" .tfw/templates/review/judge.md` → `10`. Before/after of the row quoted in RF §1. **Divergence, disclosed:** clause (b) is not byte-identical — *"against those principles"* → *"against HL §7 principles"*, three words, because the antecedent *"those"* pointed at the deleted clause (a). RF §2 decision 2 |
| E2 | AC-2 | All five properties present as failing conditions, not advice: fused citation-and-harm, excess-and-adjacency, deferral confession, override clause, materiality bar. The row was filled once against RF TFW-53/B, and the failing variant (bare citation, no harm) shown being rejected by the row's own wording | local repo | **VERIFIED** | [`purpose_check_replay.md`](purpose_check_replay.md) §5 — passing and failing forms side by side |
| E3 | AC-3 | Reference set stated (master HL at its committed frozen baseline + Project North Star); TS and Phase HL named invalid with their one-line reasons; fallback chain stated; baseline recovery **points at** `conventions.md` §3 rule 15 and does not restate the command | local repo | **VERIFIED**, with one pre-existing divergence named | Block read in `judge.md`. Gate command: `grep -rn "git log --format" .tfw/ --include="*.md"` → **two** hits: `conventions.md:77` (rule 15, the owner) and **`templates/HL.md:10`** — a pre-existing copy of the recovery form inside the contract header block, which **AC-7's gate forbids this phase to modify**. Nothing new was created by this phase; the fourth instance of amendment A13's pattern. RF §6 obs. 1 |
| E4 | AC-4 | Line 28 names the frozen baseline; the Step 3 paragraph is replaced, not deleted; Reviewer Identity names goals, values and north star with block authority; `not fit for purpose` routes to the owner; verdict vocabulary unchanged | local repo | **VERIFIED** | `grep -n "frozen baseline\|not fit for purpose" .tfw/workflows/review.md` → lines 28, 87, 102. Verdict set at line 100 still reads `APPROVE / REVISE / REJECT`; no fourth token anywhere in the file |
| E5 | AC-5 | `review.md` word count before and after with the same command, plus the ledger | local repo | **VERIFIED** — reported, not resolved | `wc -w`: **1,065 → 1,176**, under F2's 1,200 hard threshold with 24 words of headroom; **not** in the 700–900 working range. Ledger in §Exhibit A below. **No word was removed to pay for an addition** — the ledger's removal column is empty by construction |
| E6 | AC-6 | PV Index gains priority 0; priority 1 relabelled; priorities 1-7 keep their content; admission criteria, single-locus rule, multi-location rule and the same-file rule are in `conventions.md`; "Who scans PV" still resolves | local repo | **VERIFIED** | `glossary.md` PV Index read in full: rows 2-7 byte-identical, row 1's *content* unchanged and only its label moved, row 0 added. `conventions.md` §3 → **Project North Star**, seven numbered rules |
| E7 | AC-7 | `templates/HL.md` gains the north-star field **below** the contract block; the field takes a list; the fallback is stated; explicit `N/A` grammar present | local repo | **VERIFIED** | `git diff .tfw/templates/HL.md` → a single additive hunk at line 15+, entirely after the contract block's own instruction line. Zero deletions |
| E8 | AC-8 | `REVIEW.md` §3 row 2 realigned to `judge.md`; the `not fit for purpose` finding surfaced in §4 Verdict with citation and harm; still ten rows; no new section | local repo | **VERIFIED** | `grep -n "^| [0-9]" .tfw/templates/REVIEW.md` → rows 1-10, row 2 = *"Purpose Check — is this what we set out to do? + design soundness"*. The finding block sits inside the existing `### If REJECT` subsection — no heading added (F22) |
| E9 | AC-9 | `P{N}` corrected to HL §7; `PP{N}` and `NS{N}` declared; nothing else in the file touched | local repo | **VERIFIED** | `grep -n "P{N}\`\|NS{N}\|PP{N}" .tfw/compilable_contract.md` → lines 59, 60, 61 in the §2 pattern table. `git diff --numstat` → `3 1` — one row rewritten, two added, no other line in the file changed. `PP{N}` is **declared and unused here**: this repository has no `KNOWLEDGE.md` §0 (D37 removed it) and none was invented |
| E10 | AC-10 | Two review-side anti-patterns in §14; the north-star definition in §3; additions only; no other phase's entries touched | local repo | **VERIFIED** | `git diff --numstat .tfw/conventions.md` → **`27 0`** — twenty-seven insertions, **zero deletions**. `git diff .tfw/conventions.md \| grep -c "^-[^-]"` → `0` |
| E11 | AC-11 | The Purpose Check as shipped, replayed against 6 rejected-corpus REVIEWs and 3 sound ones, each with its citation-and-harm field filled | local repo, git history at `721ca15` / `9e19a4f` | **VERIFIED** _(re-scored on the second pass)_ | [`purpose_check_replay.md`](purpose_check_replay.md) — **4 of 6 non-approve on the rejected corpus** (all four `not fit for purpose`), **0 of 3 on the sound corpus**. AC-11's `≥1` condition holds. Discrimination in both directions: 48/B is a sound phase inside a rejected task, 49/A is aligned with a contract that was itself wrong for the product, and TFW-42/A produced a near-miss the materiality bar stopped. **Was 5 of 6 on the first pass** — row 49/A ruled a contract defect on a quotation of §1 that ended early; corrected per REVIEW Phase C D1 and AC-13, with the cause named in the replay's §0 |
| E12 | AC-12 | The third outcome exists, is distinct from pass and fail, and routes to the owner as a contract defect; `review.md` carries one routing clause | local repo | **VERIFIED** — the gate, which is textual | `judge.md` → Purpose Check outcome table, row 3, plus the bar stated below it. Status vocabulary deliberately unchanged (`✅/❌/⚪`) — the third outcome is a **finding**, not a fourth symbol, so no new token enters the checklist or the verdict set. `review.md`:102 routes it to the owner |
| E14 | AC-12 | The third outcome **exercised against a real internally-inconsistent contract** — what the TS's Evidence field expected AC-11 to supply | git history at `9e19a4f`, `721ca15` | **DEFERRED** | **Blocker named: no such case exists in the nine-review corpus.** The one candidate, TFW-49/A, was withdrawn on the second pass — §1 asks for readability *and* structural validation in one sentence, so DoD-3 discharges it rather than contradicting it. TFW-49's contract was internally **coherent** and wrong for the product, which is the purpose question, not this one. `judge.md` states the absence plainly rather than shipping a weak example (AC-14); HL §9's risk row now reads `Unmeasured`. Same shape as Phase B's DEFERRED on the unexercised rejected-amendment path: the branch is specified and readable, and no available history exercises it |
| E13 | build gate | Tests and site build after all seven file changes | local | **VERIFIED** | `python -m pytest docs/scripts/ -q` → **68 passed** in 42.31s. `python -m mkdocs build -f docs/mkdocs.yml` → **built in 30.74s**. **0** warnings name any of the seven changed files as source; **0** name this phase's artifacts. Repo-wide 455 warnings is the pre-existing baseline, grown from Phase B's 401 by concurrent sessions — 16 of the new ones are sourced to `tasks/TFW-55*`, which this phase did not touch |

## Verdict

Evidence verdict: **13/14 VERIFIED, 1 DEFERRED, 0 BLOCKED, 0 N/A**

> **Second pass, 2026-08-13.** REVIEW Phase C ruled 🔄 REVISE on evidence sufficiency: E11's replay row
> 49/A rested on a quotation of §1 that ended one clause early. Verified against `9e19a4f` before being
> accepted, corrected in the replay with its cause named, and propagated to E11, E12 and the new E14. The
> shipped mechanism is unchanged; the corpus was not re-run. AC-11 recounts to 4 of 6 and still passes.

Three rows carry a disclosed divergence rather than a clean pass, and none is softened:

- **E1** — clause (b) is not byte-identical. Three words changed, for a stated structural reason. A
  reviewer running AC-1's `diff` gate will see it, so it is named here first.
- **E3** — the gate's literal form (*no second copy of the recovery command in `.tfw/`*) does **not** hold,
  because `templates/HL.md`:10 carries one and AC-7's gate forbids this phase to touch it. The AC's four
  substantive bullets all hold; the gate has a pre-existing counterexample this phase may not clear.
- **E14** — `DEFERRED`, with the blocker named: the corpus contains no genuinely self-contradictory
  contract, so the third outcome ships specified, readable and unexercised. Recorded as a status rather
  than as a sentence in a paragraph, because that is the difference between a gap a reviewer can audit and
  one they have to notice.

## Exhibit A — `review.md` word ledger (AC-5)

`wc -w` counts blockquote `>` markers as words; the marker column separates that artifact from real text.

| # | Site | Before | After | Δ | Of which `>` markers | What changed |
|---|------|-------:|------:|--:|---:|--------------|
| 1 | Line 28 — context loading | 13 | 31 | **+18** | 0 | *"Master HL for the task"* → *"Master HL at its frozen baseline"*, plus the reference-set naming and the rule-15 pointer. **Required by AC-4 and load-bearing:** without it the reference-set rule has nothing to bind to |
| 2 | Reviewer Identity | 23 | 57 | **+34** | +2 | Third defended object added — goals, values, north star — with block authority. `not rubber stamp` restored (D46 recorded it; only the first half ever shipped) |
| 3 | Step 3 — the `HL §7 Principles check` paragraph | 46 | 57 | **+11** | 0 | **Replaced in place**, per ONB Q1 → (a). Predicted budget-neutral; came in +11 because the replacement must name *two* invalid references and the fused field |
| 4 | Step 4 — Routing | 0 | 48 | **+48** | 0 | New: `not fit for purpose` → owner; contract defect → owner; vocabulary unchanged. Covers AC-4 and AC-12 in one block |
| | **Total** | **1,065** | **1,176** | **+111** | | Against the TS §6 ledger's ≈ +104 estimate |

**Removals to buy headroom: none.** Sites 1-3 are in-place replacements mandated by an AC; site 4 is new
text. Nothing pre-existing was deleted, so AC-5's pairing requirement — every removed word matched to the
text it restated — has an empty set to satisfy and the DoF-2 trap (manufacturing duplication to pay for an
addition) was never approached. The first draft landed at **1,192**; the 16 words between that and 1,176
were cut from **this phase's own new text** in sites 2 and 4, not from anything the file already had.

**Reported, not resolved (AC-5 bullet 3):** 1,176 meets the ≤1,200 hard threshold and misses the 700-900
working range. Reaching 700-900 needs ~280 more words removed, and every remaining block in `review.md` is
the sole statement of its mechanism. Same posture and same reason as Phase B at 1,195.

## Attachments

| File | Description |
|------|-------------|
| [`purpose_check_replay.md`](purpose_check_replay.md) | AC-11 — nine replayed reviews, per-row citation-and-harm, outcomes, the three recorded divergences, the reconciliation with `~4 in 149`, and AC-2's dry-run |

---

*EV — TFW-53 / Phase C: Goal Defence in Review | 2026-08-13*
