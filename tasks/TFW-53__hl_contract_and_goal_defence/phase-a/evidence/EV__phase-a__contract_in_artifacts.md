# EV — TFW-53 / Phase A: Contract in Artifacts

> **Date**: 2026-08-13
> **Author**: Executor (Claude Code)
> **Task**: TFW-53
> **TS**: [TS Phase A](../TS__phase-a__contract_in_artifacts.md)

---

## Environment

| Field | Value |
|-------|-------|
| OS | Windows 11 Pro 10.0.26200 |
| Language / Runtime | Python 3.13.5 |
| Shells | PowerShell 5.1.26100.8655 · Git Bash (MSYS2), git 2.42.0.windows.1 |
| Build | `python -m pytest docs/scripts/` · `python -m mkdocs build --config-file docs/mkdocs.yml` (mkdocs 1.6.1) |
| CI / Pipeline | `.github/workflows/docs.yml` — same two steps, run locally here |

> `project_config.yaml` `build.lint/test/verify` are unconfigured starter placeholders
> (`echo "configure your … command"`). The docs pipeline is the only build that consumes the files
> this phase changes — `conventions.md` and `.tfw/templates/**` are Source Manifest rows 4 and 13.
> Substitution approved in ONB Recommendation 6.

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Header contract field, three-state section marking, §12 pointer, inline heading markers | — | N/A | TS Evidence field: `N/A — template content; correctness is established by reading, and there is no runtime behaviour to observe.` Gate result in RF §3 |
| E2 | AC-2 | Shipped §12 column grammar diffed against the **live** rows of HL-TFW-53 §12 | Git Bash, `awk` field extraction over the real artifact | **VERIFIED** | See §E2 below. 12 live rows (TS said nine — written before A9–A12 existed). Column set matches 10/10. One gap found and closed: verdict `🚫 WITHDRAWN` |
| E3 | AC-3 | Two-class split; `Coordinator applies these` removed | — | N/A | TS Evidence field: `N/A — template content.` Gate `grep -n "Coordinator applies these" .tfw/templates/RES.md` → 0 matches, recorded in RF §3 |
| E4 | AC-4 | HL Contract definition in `conventions.md` §3 | — | N/A | TS Evidence field: `N/A — convention text.` |
| E5 | AC-5 | Verdict as a distinct recorded act; remark ≠ approval; owner-initiated change is an amendment | — | N/A | TS Evidence field: `N/A — convention text.` |
| E6 | AC-6 | Documented recovery command run on live history under **both** shells | PowerShell 5.1 **and** Git Bash | **VERIFIED** | [`baseline_recovery.txt`](baseline_recovery.txt) — shipped slash-free form returns 5 freeze commits in both shells; the rejected `/freeze/` form returns 0 rows in Git Bash |
| E7 | AC-7 | Delegated mandate is a ceiling | — | N/A | TS Evidence field: `N/A — convention text.` |
| E8 | AC-8 | Five discriminating RES iter1 rows classified from the shipped rule text alone | Reading, against `research/iter1/RES.md` | **VERIFIED** | [`classification_exercise.md`](classification_exercise.md) — 5/5 agreement, **with the circularity limit stated first**; produced one rule change (tripwire timing) |
| E9 | AC-9 | The shipped Phase HL rule applied to the historical artifact that motivated it | Git Bash, `git show 721ca15:…` | **VERIFIED** | See §E9 below. All four prohibited section classes present in `TFW-48/phase-a/HL__phase-a__method_kernel.md` |
| E10 | AC-10 | REJECT branch (a) redefined; verdict vocabulary unchanged | — | N/A | TS Evidence field: `N/A — convention text.` |
| E11 | AC-11 | Shipped §3.1 rule applied to HL-TFW-53's own §3.1 | Reading, against the HL at `ffe6c6a` | **VERIFIED** | See §E11 below. Passes 4/4 |
| E12 | AC-12 | Seven anti-patterns appended, none removed | — | N/A | TS Evidence field: `N/A — convention text.` Reproducible count in RF §4 |
| E13 | AC-13 | Anchored recovery form run in both shells; superseded form run alongside for contrast; plus a probe of what `^` actually anchors to | PowerShell 5.1 **and** Git Bash | **VERIFIED** | [`baseline_recovery.txt`](baseline_recovery.txt) §§6–10 — appended under a dated second-pass heading, first pass intact. 5 commits in each shell, `f379c5e` absent; superseded form returns 6 in each. See §E13 below |
| E14 | AC-14 | RF §1 internal consistency after the corrective passes | Reading against a diffstat | N/A | TS Evidence field: `N/A — RF-internal accuracy, verifiable by reading against a diffstat.` Gate command and figures in RF §4 |
| E15 | AC-15 | Rule 15 word counts before and after compression, **plus** AC-13's two-shell gate re-run to prove the compression did not weaken the rule | Python word count over the parsed rule block; both shells for the re-run | **VERIFIED** | [`baseline_recovery.txt`](baseline_recovery.txt) §§11–12 + final counts. 162 → 57 words; block 958 → 853; command behaviour identical. See §E15 below |

## Verdict

Evidence verdict: **7/15 VERIFIED, 0 DEFERRED, 0 BLOCKED, 8 N/A**

The 8 N/A are the TS's own `Evidence:` fields, quoted verbatim in the table — not executor
judgement. The 7 VERIFIED are the five ACs TS §6 named as observable against a live artifact or live
history, plus AC-13 and AC-15, both added in review passes and both verified on the same live history.

---

## E2 — §12 column grammar against the live corpus (AC-2)

**Shipped grammar** (`.tfw/templates/HL.md` §12):

```
| # | Date | § | Type | Proposer | Proposed change | Evidence | Cost | Alternatives considered | Verdict |
```

**Live corpus** — HL-TFW-53 §12 header row, byte-for-byte identical. **12 rows** (A1–A12), not the
nine the TS names; A9–A12 were filed after the TS was written.

| Field | Can the shipped grammar hold every live value? | Notes |
|-------|-----------------------------------------------|-------|
| `#` | ✅ | `A1`–`A12` |
| `Date` | ✅ | 2026-08-08 / 2026-08-10 |
| `§` | ✅ | Live values are section *and* sub-target (`§5 DoD-2`, `§4 Phases A/B/D + §5 DoD`). Free text, holds |
| `Type` | ✅ | 11 × `EXTEND`, 1 × `SUPERSEDE`. **`RESTRICT` is not exercised by this corpus** — no historical proposal narrowed the contract. Untested against live data, recorded as a coverage gap |
| `Proposer` | ✅ | Four distinct values, all covered by the template's placeholder: `Research (iter1)`, `Research (iter2)`, `Owner`, `Executor (Phase A ONB Q2)`, `Coordinator (from Phase A ONB Risk 1)` |
| `Proposed change` · `Evidence` · `Cost` · `Alternatives considered` | ✅ | All 12 rows populate all four |
| `Verdict` | ⚠️ → ✅ | **Gap found.** 10 × `✅ APPROVED — owner, {date}`, 1 × `✅ APPROVED … (proposer and ruler are the same party; recorded per A4)`, and **A11 = `🚫 WITHDRAWN by the coordinator, 2026-08-10`** — a value the draft vocabulary did not enumerate |

**Gap and resolution.** A withdrawn proposal has no home in a four-value vocabulary. Deleting the
row breaks append-only; marking it `❌ REJECTED` credits the owner with a decision they never made.
`🚫 WITHDRAWN — {proposer}, YYYY-MM-DD` was added to the shipped vocabulary, constrained to
retraction *by the proposer* and *only before a ruling*. This is precisely what AC-2's Evidence
clause was written to surface — a real artifact with real rows exposing a field the grammar could
not hold.

**Result: the amended template can carry HL-TFW-53's own §12 unchanged.**

## E9 — The Phase HL rule against the artifact that motivated it (AC-9)

Command: `git show 721ca15:tasks/TFW-48__value_first_methodology_rebaseline/phase-a/HL__phase-a__method_kernel.md`

Shipped rule under test (`conventions.md` §3 → HL Contract, rules 20–21):

> 20. **A Phase HL is derivation-only.** It may restate master content and add execution context —
>     files, sequencing, phase-local risks.
> 21. **A Phase HL may not carry its own §1, §5, §6 or §7.** … A Phase HL that authors them is a
>     second, unapproved contract.

| What the historical file carries | Line | Prohibited by |
|---|------|---------------|
| `## 1. Vision` — its own vision narrative | 11 | Rule 21 (§1) |
| `## 5. Definition of Done (DoD)` — **10** items | 116 | Rule 21 (§5) |
| `## 6. Definition of Failure (DoF)` — **9** items | 129 | Rule 21 (§6) |
| `## 7. Principles` — **10** numbered principles, of which master P7, P10 and P12 do not survive | 143 | Rule 21 (§7) |
| `## 7.1 Quality Contract` — its own quality contract | 156 | Rule 21 (§7 subsection, frozen with §7) |
| Header: `**Status**: ✅ HL — Approved scope derived from master HL` | 5 | Rule 3 by implication — a self-declared approval on an artifact no owner ruled on |

**Result: the shipped rule classifies the artifact as a violation on four independent counts**, which
is the outcome the rule was written to produce. §14 also carries the matching anti-pattern.

What the rule would still permit in that file: §2, §3, §4, §7.2, §8, §9, §10, §11 — restatement and
execution context. The prohibition is targeted, not a ban on the artifact class.

## E11 — The shipped §3.1 rule against HL-TFW-53's own §3.1 (AC-11)

Subject: HL-TFW-53 §3.1, as it stands at `ffe6c6a`.

| Shipped property | Present? | Where |
|------------------|----------|-------|
| 1. Written backwards from the finished state | ✅ | Opens *"Rendering of §3–§5 as already approved"*; carries *"The life of a task after this ships"* and *"What you actually see, six months in"* |
| 2. Rendered visually — mandatory, not a format choice | ✅ | File/folder tree of every change, an ASCII phase-dependency flow, an end-to-end lifecycle flow, a before/after pair for a research iteration, and a sample rendered §12 log |
| 3. The value is shown, not only the artifact | ✅ | The per-phase table's second column is *"What it buys — stated as what stops happening"*; plus *"0 new artifacts in a project's root — a project adopting this pays nothing on upgrade day"* |
| 4. Complete enough to hold at once | ✅ | Every entry in the change tree carries its phase label `[A]`–`[E]`, and the per-phase table gives one line per phase |

**Result: 4/4 — pass.**

Recorded honestly: it passes *now*. It did not pass before 2026-08-10 — HL §11 S34 records that this
five-phase HL had no complete change map until the owner asked for one, and A9 is what put it there.
The rule this phase ships would have failed the HL that commissioned it, on property 4, for two days.
That is the argument for the rule, not against it.

**Not tested:** the earlier *budget and cut-order* property is absent from both the rule and this
check — removed from the contract by amendment A12 (2026-08-10) and deliberately not implemented.

## E13 — The anchored recovery form on live history (AC-13)

Added to the TS after the second review pass. R3's observation: the first-pass form was unanchored,
`--grep` searches the whole commit message, and `f379c5e` matched because its body quotes the broken
pattern it was fixing. Six returned where five are real.

| Form | Git Bash | PowerShell 5.1 | `f379c5e` present? |
|------|----------|----------------|--------------------|
| **Shipped** `git log -E --grep="^\[[^]]*/TFW-53/freeze/"` | 5 | 5 | **no** |
| Superseded `git log --grep="TFW-53/freeze"` | 6 | 6 | yes |
| Rejected (first pass) `git log --grep="/TFW-53/freeze/"` | **0** | 5 | — |

Three properties, all measured rather than assumed:

1. **Anchoring is what removes the pollution.** `f379c5e` is a corrective commit, not a freeze
   commit; it was being handed to a reader as a baseline candidate.
2. **The absent leading slash is what keeps it runnable.** The rejected first-pass form returns zero
   rows under Git Bash — MSYS rewrites a leading `/` as a filesystem path. Both properties are
   required; each alone fails a different way.
3. **`^` anchors to the start of any line, not to the subject.** Probe: `git log -E --grep="^TD-137"`
   returns `267bd06`, where `TD-137` occurs only as the first token of a *body* line. So the anchor
   removes mid-line mentions — the failure actually observed — but would not remove a body line
   beginning with a conforming prefix. Rule 15 ships this as a stated limit with the instruction
   that follows from it, rather than implying a selectivity it does not have.

Full transcripts: [`baseline_recovery.txt`](baseline_recovery.txt) §§6–10. The first pass (§§1–5) is
appended to, never overwritten — per the TS, it is the record of the first failure this rule survived.

> **Superseded within the same pass.** AC-15's revision (TD-143) replaced the anchored `--grep` form
> below with a subject-only one. The table and the three properties stand as the record of what was
> tested and why the anchored form was not enough — see §E15, which supersedes this exhibit's
> conclusion while confirming its measurements.

## E15 — A subject-only recovery form, with the negative test AC-15 requires (AC-15)

AC-15's Evidence field is explicit that a word count alone is not sufficient: *"a compression that
kept the weaker mechanism would pass the word count and fail the negative test; both are required."*
Both were run, and the negative test is what changed the deliverable.

**Measurement 1 — the negative test, on a constructed fixture.** AC-15 instructs: *"must not return
a commit whose body quotes a conforming prefix — construct that commit locally to prove it if none
exists."* Built as an empty commit `0d5b6f0` on a throwaway branch `tmp/ac15-negative-test`, subject
deliberately **not** a freeze subject, body containing the line
`[claude-code/TFW-53/freeze/coordinator] re-freeze after something`. Branch deleted after the run;
master untouched.

| Candidate | Returns | Fixture `0d5b6f0` | Verdict |
|-----------|---------|-------------------|---------|
| `git log --grep="TFW-53/freeze"` (first form) | 6 | included | ❌ |
| `git log -E --grep="^\[[^]]*/TFW-53/freeze/"` (AC-13's form) | 6 | **included** | ❌ |
| `git log -P --grep="\A\[[^]]*/TFW-53/freeze/"` (PCRE `\A`) | 6 | **included** | ❌ |
| **`git log --format="%h %s"` filtered on `^\S+ \[[^]]*/TFW-53/freeze/`** | **5** | **excluded** | ✅ **shipped** |

**The finding that decided it: no `--grep` form can be subject-only.** Git matches a commit message
line by line, so `^` under `-E` and `\A` under `-P` both anchor to a *line* start — never to the
subject. Independently probed with `git log -P --grep="\ATD-137"`, which returns `267bd06`, a commit
where `TD-137` occurs only as the first token of a body line. AC-15's premise — that a form filtering
on `%s` is subject-scoped and `--grep` is not — is correct, and it is correct for a stronger reason
than the AC states: not that `--grep` is *unanchored*, but that it is *unanchorable* to the subject.
This is why the anchored form and its "Known limit" bullet were deleted rather than shortened.

**Measurement 2 — size.** Word counts by parsing the rule block between the `15.` and `16.` markers,
and the `#### HL Contract` block between its heading and the next `###`:

| | Before | After | Delta |
|---|--------|-------|-------|
| Rule 15 | **162** | **56** | −106 (ceiling: 60) |
| `#### HL Contract` block | 958 | 852 | −106 |
| Other 20 rules in the block | — | — | **0** — every per-rule count verified identical |

The block delta equals the rule delta exactly: nothing was smuggled elsewhere and no rule grew to
absorb what rule 15 lost. Context for the target: the block median is 37 words, and rule 15 at 162
was longer than rules 17–21 combined.

**Measurement 3 — the shipped form on live history, both shells.**

| | Git Bash | PowerShell 5.1 | `f379c5e` | fixture |
|---|----------|----------------|-----------|---------|
| Shipped subject-only form (§§13, 14) | **5** | **5** | absent | excluded |

The git half of the command is identical in both; only the text filter differs, which is why rule 15
names the pattern and not the filter. The no-leading-slash constraint still applies to the pattern
and is stated.

**Third edit, same pass — no platform names in the shipped core.** On the owner's challenge
(*"is it ok that there is something about windows in conventions?"*), the compressed rule's
*"because Git Bash on Windows rewrites one as a path"* became *"because some shells rewrite a leading
slash as a path"*. `conventions.md` is copied into every project and HL §7.1 bars environment-specific
text there. Verified across all three shipped files:
`grep -niE "windows|macos|linux|git bash|msys|powershell"` → **0 matches**. The platform, the shell
and the measured counts survive in RF §7 FC1 as an *environment* fact, which is where per-project
detail belongs. Three word-count readings appear in the transcript — 55, 57 and the final 56 — because the rule was
edited three times in one pass: compressed, de-platformed on the owner's challenge, then rewritten
subject-only. Each reading was correct when taken; 56 / 852 / −106 is the shipped state.

**What was removed and where it went.** Three behaviours, all measured, none discarded:

| Behaviour | Was in | Now in |
|-----------|--------|--------|
| A leading `/` is rewritten as a path by some shells; 0 rows vs 5 | rule 15, one paragraph | RF §7 **FC1** → `knowledge/environment.md` |
| `--grep` matches whole messages; unanchored returns 6 where 5 are real | rule 15, one paragraph | RF §7 **FC4** |
| `^` and `\A` anchor to any line start, so `--grep` is unanchorable to the subject | rule 15, "Known limit" | RF §7 **FC5** |

The "Known limit" is gone from `conventions.md` in the strong sense AC-15 asked for: the shipped
mechanism does not have that limit, so there is nothing left to document. What survives in knowledge
is why three other candidates were rejected.

`conventions.md` ships no pointer to them yet — `knowledge/environment.md` does not carry them until
`/tfw-knowledge` runs, and a citation that resolves to a file without the content is the S32 defect
this project has already documented once.

---

*EV — TFW-53 / Phase A: Contract in Artifacts | 2026-08-13 · third pass 2026-08-13*
