# round2.md — raw output behind EV rows E12–E18

> **Date**: 2026-09-02 · **Author**: Claude Code (Executor), on behalf of `saubakirov`
> Every block below is pasted from a command run in this session, from the project root, in Git Bash.
> Nothing is retyped from memory.

---

## §1 — AC-13: the order is the coordinator's artifact, and Step 6 no longer writes a bound

The order's own commits, subject-filtered on this task's `ts` scope:

```
4d1ac8b 16:56:31 [claude-code/TFW_20260902-112841_RDP/onb/coordinator] answer Q5-Q9; five corrections to the order
a356f63 16:36:22 [claude-code/TFW_20260902-112841_RDP/ts/coordinator] TS revision 2, rewritten without the count
f1f102b 16:16:02 [claude-code/TFW_20260902-112841_RDP/ts/coordinator] clean the template dirt out of revision 2
1a5d282 16:08:20 [claude-code/TFW_20260902-112841_RDP/ts/coordinator] TS revision 2: the round is the coordinator's artifact
7bfc5b1 15:59:06 [claude-code/TFW_20260902-112841_RDP/ts/coordinator] TS revision 2: the lifecycle must tell the truth
cc66aa9 14:26:26 [claude-code/TFW_20260902-112841_RDP/onb/coordinator] answer onboarding; four of the fixes are mine
```

Every occurrence of the word `bound` left in `review.md` — one, and it is the prohibition:

```
155:4. If 🔄 REVISE: the items stay **proposals** and the work returns to the **coordinator**, who orders the round in a TS revision (§15). No bound, no dispatch
```

The nine basis cells, read out of the order's §5a — the column that is the citation bar's enforcement
site. An empty cell here would mean the item does not belong in the table:

```
item  1  basis: **HL DoF 5**, frozen: *"the reviewer retains disposition authority anywhere in the canon"* is a failure 
item  2  basis: TS AC-5, AC-10 
item  3  basis: **HL §7.1** — every claim about the corpus carries its measurement 
item  4  basis: TS AC-10 
item  5  basis: TS AC-10. A release whose trace does not resolve its own citations 
item  6  basis: **HL §12 A14**, frozen. *The entry itself exists — round 1 added it (commit `2cddc89`); what it says is wro
item  7  basis: TS AC-12 and AC-14; `status.md` asserted `RF` while items were owed 
item  8  basis: **HL §12 A14** and **§4 deliverable 8**, frozen and unfinished: it named the RF and the REVIEW and skipped t
item  9  basis: **HL §12 A13**, frozen and `RESTRICT`, so it applies on filing 
```

The approval clause in the order's header:

```
5:> **Status**: 🟡 TS_DRAFT — `✅ APPROVED — saubakirov, 2026-09-02, by dispatch`. The owner invoked
21:> **Basis**: HL §12 **A13** and **A14**, both `✅ APPROVED — saubakirov, 2026-09-02`
```

---

## §2 — AC-14: the chain walked on this round

| Step | Role | File read | File written | Had to infer or ask? |
|---|---|---|---|---|
| 1 | Reviewer | `RF__…md`, `TS__…md`, stage files | `REVIEW__…md` §4 — 🔄 REVISE, items as proposals | no |
| 2 | Coordinator | `REVIEW__…md` | `TS__…__rev2.md`; `PROPOSAL__…RTMW.md`; `status.md` → `TS_DRAFT` | no |
| 3 | Executor | `TS__…__rev2.md` — the order found in §5a | `ONB__…md` §8; `status.md` → `ONB` | **no detector, nothing hidden** |
| 4 | Coordinator | `ONB__…md` §8 | `ONB__…md` §8.2a, in the template's own designated answer cells; five corrections to `TS__…__rev2.md` | no |
| 5 | Executor | `TS__…__rev2.md` as amended | canon edits; `RF__…md` §…2; this file | no |
| 6 | Reviewer of round 2 | `RF__…md` §…2 against `TS__…__rev2.md` | `REVIEW__…__rev2.md` | **not yet run — the reviewer's act** |

**Could a reader who was not in the conversation follow it?** Yes for steps 1–5, and the test is that
this table cites only files. The one thing a fresh reader would *not* get from the artifacts is why the
coordinator answered in the executor's file — and the amended AC-14 now states that as the designated-cell
rule, so the artifacts answer it too. Step 6 is unverifiable from here by construction.

The journal, which is the same chain seen from the outside:

```
20260902-154517__handoff__c058.md
20260902-154941__handoff__8af1.md
20260902-155307__transition__d670.md
20260902-155905__transition__3292.md
20260902-160819__handoff__aab3.md
20260902-165919__transition__ce94.md
```

```
---
time: 2026-09-02T16:59:19+05:00
kind: transition
on_behalf_of: saubakirov
via: claude-code
from: TS_DRAFT
to: ONB
refs:
  - ONB__TFW_20260902-112841_RDP.md
  - TS__TFW_20260902-112841_RDP__rev2.md
summary: "round 2 taken: the order was found in the TS, the ONB is answered, nine items stand"
---
```

---

## §3 — AC-15: the grammar's first instance is this directory

```
HL-TFW_20260902-112841_RDP.md
ONB__TFW_20260902-112841_RDP.md
REVIEW__TFW_20260902-112841_RDP.md
RF__TFW_20260902-112841_RDP.md
TS__TFW_20260902-112841_RDP.md
TS__TFW_20260902-112841_RDP__rev2.md
evidence
journal
research
review
status.md
```

Revision 1 unsuffixed and never renamed, revision 2 the sibling that governs; one RF and one ONB, each
appended rather than duplicated. The four new rows in `conventions.md` §4:

```
392:| Single-phase TS revision | `TS__{ID}__rev{N}.md` | `TS__TFW_20260829-172110_ABT__rev2.md` |
393:| Single-phase REVIEW revision | `REVIEW__{ID}__rev{N}.md` | `REVIEW__TFW_20260829-172110_ABT__rev2.md` |
394:| Phase TS revision | `TS__phase-{x}__{title}__rev{N}.md` | `TS__phase-a__conventions__rev2.md` |
395:| Phase REVIEW revision | `REVIEW__phase-{x}__{title}__rev{N}.md` | `REVIEW__phase-a__conventions__rev2.md` |
411:**`__rev{N}` is the one suffix the grammar admits, and it is an ordinal.** It names a **revision round** —
```

---

## §4 — AC-16: the count, counted before and after

At `1f5f578`, the commit that shipped it — tracked files, excluding the trace under `workspace/` and
`tasks/`:

```
.agent/workflows/tfw-handoff.md:1
.agent/workflows/tfw-review.md:1
.claude/commands/tfw-handoff.md:1
.claude/commands/tfw-review.md:1
.tfw/CHANGELOG.md:2
.tfw/conventions.md:1
.tfw/glossary.md:1
.tfw/project_config.yaml:1
.tfw/templates/project_config.yaml:1
.tfw/workflows/handoff.md:1
.tfw/workflows/review.md:1
KNOWLEDGE.md:2
TOTAL: 14 hits in 12 files
```

At `HEAD` — the gate's own command, as corrected by the ONB so that the gitignored `site/` build is out
of scope by construction rather than by an exclusion someone must remember:

```
$ git grep -n "max_revision_cycles" -- . | grep -v "^workspace/\|^tasks/"
(no output — 0 hits in 0 files)
```

The plain sweep beside it, for the belt: every remaining hit is in the gitignored documentation build.

```
site
```

Word budget — every figure re-run in this session, `1f5f578^` being the state before round 1:

```
site                            1f5f578^   round1      now  ceiling
review.md Steps 4-6                  483      480      477      483
review.md Anti-patterns              163      160      160      163
review.md whole file                1706     1702     1699        -
handoff.md whole file               1452     1749     1730     1200
plan.md whole file                  1702     1702     1847     1200
conventions.md 5                     952     1433     1673        -
conventions.md 4 naming              291      291      668        -
```

Both config files re-parsed after the key was removed, and the `ONB` entry re-read:

```
.tfw/project_config.yaml
  tfw.review = {'min_verify_ratio': 0.42}
  ONB        = Onboarding report written; the executor is working toward the RF, re-entry after a 🔄 REVISE included
.tfw/templates/project_config.yaml
  tfw.review = {'min_verify_ratio': 0.42}
  ONB        = Onboarding report written; the executor is working toward the RF, re-entry after a 🔄 REVISE included
```

All 22 adapter copies against their 11 sources:

```
OK    .claude/commands/tfw-config.md
OK    .agent/workflows/tfw-config.md
OK    .claude/commands/tfw-docs.md
OK    .agent/workflows/tfw-docs.md
OK    .claude/commands/tfw-handoff.md
OK    .agent/workflows/tfw-handoff.md
OK    .claude/commands/tfw-init.md
OK    .agent/workflows/tfw-init.md
OK    .claude/commands/tfw-knowledge.md
OK    .agent/workflows/tfw-knowledge.md
OK    .claude/commands/tfw-plan.md
OK    .agent/workflows/tfw-plan.md
OK    .claude/commands/tfw-release.md
OK    .agent/workflows/tfw-release.md
OK    .claude/commands/tfw-resume.md
OK    .agent/workflows/tfw-resume.md
OK    .claude/commands/tfw-review.md
OK    .agent/workflows/tfw-review.md
OK    .claude/commands/tfw-update.md
OK    .agent/workflows/tfw-update.md
OK    .claude/commands/tfw-research.md
OK    .agent/workflows/tfw-research.md
drift=0
```

The index gate, unchanged script:

```
17 phase directories under 6 task(s) carry no state file; informational lines above, exit code unaffected
59 tasks validate against the closed schema
not checked: index freshness -- this gate deliberately does not answer it (--check index), project consistency (--check project)
```

---

## §5 — item 7 (AC-12): the lifecycle told the truth

`(develop)` in §5, and the verdict list:

```
(develop) occurrences in section 5: 0
667:- 🔄 **REVISE** — specific issues → 🟡 TS_DRAFT while the coordinator writes the round's order, then
668-  🟠 ONB when the executor takes it. Each item is routed by **rung** (below)
```

This task's own state, now:

```
---
id: TFW_20260902-112841_RDP
title: "Review Decision Protocol"
goal: "a review orders work and defers work, and neither has a stated basis, a named decider, or a rule that ends the loop"
value: "every finding a review produces becomes a decision by rule: one criterion from NS1, one named decider, one termination"
lifecycle: ONB
owner: saubakirov
authority: HL-TFW_20260902-112841_RDP.md
created: 20260902-112841
updated: 20260902-165919
---
```

`templates/status.md`'s enumeration — read, and unchanged, because no status was added or renamed:

```
80:lifecycle takes one of the ids in project_config.yaml `tfw.statuses`:
81-TODO · HL_DRAFT · RES · PHASES · TS_DRAFT · ONB · RF · REV · KNW · DONE · BLOCKED · REJECTED
82-
```

---

## §6 — items 1–5: what was verified rather than redone

```
fa17b41 17:14:52 [claude-code/TFW_20260902-112841_RDP/rf/executor] round 2 items 6-9: the round is an artifact, the count is gone
fb1fb36 16:58:37 [claude-code/TFW_20260902-112841_RDP/rf/executor] round 2 items 1, 2, 4, 5: commit the orphaned round-1 fixes
5c74762 16:38:47 [claude-code/TFW_20260902-153617_RTMW/config/coordinator] give the receiver a migration it can follow
1de76bc 16:07:01 [claude-code/TFW_20260902-153617_RTMW/config/coordinator] retire /tfw-task; drop the by-name exception
1f5f578 15:01:03 [claude-code/TFW_20260902-112841_RDP/rf/executor] ship the review decision protocol
9ea9a4f 11:16:51 [claude-code/TFW_20260830-194027_TLD/review/coordinator] close the task; correct the release claim
168e119 10:59:33 [claude-code/TFW_20260830-194027_TLD/task/executor] revision 2: frontmatter, three causes removed not escaped
dc09eec 10:22:04 [claude-code/TFW_20260830-194027_TLD/task/executor] revision 1: the debt search survives its adapter
dfba46f 07:35:34 [claude-code/TFW_20260830-194027_TLD/task/executor] retire the debt registry; disposition before closing
5a72b2b 19:19:03 [claude-code/project/release/coordinator] release v2.0.0
a6302ae 18:56:49 [claude-code/TFW-60/phase-ac/coordinator] consolidate knowledge: 9 facts at seq 60, close phase AC
cab7243 18:35:38 [claude-code/project/release/coordinator] release v2.0.0-dirty.5
```

Item 3, the entry as it now stands — one of the two removals is a verbatim duplicate and the other is not,
which is what the item ordered and what `1de76bc` delivered:

```
353:  `conventions.md` §14. The second is a **verbatim** duplicate of `§14:902`. The first is not:
354-  `§14:901` reads ``- Executor writes REVIEW file → **Role Lock violation**`` and carries no
355-  ``(start `/tfw-review` instead)``, so that clause is now in neither list. What it told the executor
356-  is stated once, in §15's Hard Stop Rule: a finished executor is instructed to start `/tfw-review`.
357-
```

---

## §7 — the build gate: one test red, deliberately

```
1 failed, 321 passed, 1 skipped in 149.41s (0:02:29)

```

The detector, and the complete list of what it reports — all twelve are the one form AC-15 requires, so
nothing unintended hides behind the count:

```
938:DOUBLED_SLUG = re.compile(r"\{ID\}__")
offenders: 12
  .agent/workflows/tfw-handoff.md:30: `TS__{ID}__rev{N}.md`
  .agent/workflows/tfw-handoff.md:55: `TS__{ID}__rev{N}.md`
  .agent/workflows/tfw-plan.md:197: `TS__{ID}__rev{N}.md`
  .claude/commands/tfw-handoff.md:30: `TS__{ID}__rev{N}.md`
  .claude/commands/tfw-handoff.md:55: `TS__{ID}__rev{N}.md`
  .claude/commands/tfw-plan.md:197: `TS__{ID}__rev{N}.md`
  .tfw/conventions.md:392: `TS__{ID}__rev{N}.md`
  .tfw/conventions.md:393: `REVIEW__{ID}__rev{N}.md`
  .tfw/glossary.md:153: `TS__{ID}__rev{N}.md`
  .tfw/workflows/handoff.md:30: `TS__{ID}__rev{N}.md`
  .tfw/workflows/handoff.md:55: `TS__{ID}__rev{N}.md`
  .tfw/workflows/plan.md:197: `TS__{ID}__rev{N}.md`
```

The file never reaches a receiving project — `update.md` Step 5 copies `.tfw/` and nothing else:

```
src=.tfw/.upstream/.tfw
find "$src" -type f | while read -r f; do rel=${f#"$src"/}
  case "$rel" in project_config.yaml|knowledge_state.yaml) echo "skipped: .tfw/$rel (project-owned)" ;;
  *) mkdir -p ".tfw/$(dirname "$rel")" && cp "$f" ".tfw/$rel" ;; esac; done
```

---

*round2.md — TFW_20260902-112841_RDP: Review Decision Protocol | 2026-09-02*
