# Judge rev3 — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD / all TS AC | ❌ | Rev2 AC-1–AC-5 and rev3 AC-6 hold, but AC-7 checkbox 4 does not: `duplicate(BASE)` neither includes nor unambiguously covers the rendered `LEAD_BASE`; Verify V13–V14. |
| 2 | Purpose and design | (a) ✅ (b) ❌ | **(a)** Purpose is aligned: the result serves the frozen Vision's owner-inspectable delegated chain and NS1 continuity, with no adjacent Phase-E/runtime/release work. **(b)** Design is unsound at the collision boundary: the new title form bypasses the existing uniqueness/fail-soft contract. |
| 3 | Debt disposed by consequence | ✅ | The original REVIEW's two rows retain their Coordinator-ratified `not material — owed and forbidden to pay` dispositions and cited barring clauses. This acceptance failure is a revision proposal, not debt. |
| 4 | Style and standards | ❌ | The canonical grammar explicitly distinguishes `BASE` from `LEAD_BASE` but scopes the next normative collision clause only to the former. That is an observable contract omission, not a wording preference. |
| 5 | Observations collected | ✅ | RF preserves its earlier observations and explicit empty §7–§9 outcomes. The newly confirmed material defect is recorded as a verdict finding rather than deferred as an observation. |
| 6 | RF §7–§9 complete | ✅ | Fact Candidates, Strategic Insights and Diagrams are present and explicitly empty; no new human-sourced fact or explanatory diagram is needed for this source-level defect. |
| 7 | Evidence exists | ✅ | Cumulative EV and all seven Round-3 attachments exist; accounting, WIP, A5, scenarios, mutants, tests and strict-build token counts are inspectable. |
| 8 | Evidence is sufficient | ❌ | Green navigation evidence has no collision inputs, branch, case or mutant. It cannot establish AC-7's retained collision/no-key behavior even though all modeled cases pass. |
| 9 | Backward compatibility | ❌ | Ordinary `BASE` collision behavior remains, but the newly rendered root form does not inherit it. Concurrent selected-root titles can collide without the existing stable-key suffix/fail-soft safeguard AC-7 promised to preserve. |
| 10 | Safety | ✅ | Review changed only Reviewer-owned rev3 trace files. No secret, destructive action, implementation, lifecycle mutation, dispatch, release, tag, push, or external write was performed. |

## Purpose Check — row 2 clause (a)

**Aligned:** the frozen Vision says, “The owner can leave routine coordination to the LEAD and return
to an inspectable finished result; ultimate authority and accountability remain with the human who
initiated the mandate.” North Star NS1 requires “purposeful, human-governed continuity.” The concrete
harm at stake is an owner opening or continuing the wrong root because two selected-root tasks render
the same visible title; that obscures navigation and continuation even though it grants no authority.

The result stays within the approved Phase-D outcome and does not ship work assigned to Phase E,
RTBO integration, runtime/index repair, release or knowledge promotion. The contract baseline and
Project North Star are internally consistent. The failure is a design/implementation omission inside
the approved TS, not a purpose failure or frozen-contract defect.

## Design Analysis — row 2 clause (b)

The new root predicate and handle source are otherwise coherent: one exact selected root qualifies,
children retain ordinary cues, and navigation grants nothing. The design breaks at composition with
D79's inherited title transport. `LEAD_BASE` is a separate rendered form, but collision still names
only `BASE`; no source rule tells a duplicate root title to suffix, and no modeled input could expose
the omission. The fail-soft no-key rule is therefore unreachable or ambiguous for precisely the new
title whose collision behavior AC-7 says remains.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---|---|---|
| 1 | D79 — only a BASE collision adds the stable-key prefix; exact readback otherwise reports once and continues | Round 3 says inherited collision/readback behavior remains for the new LEAD title | **Yes within the implementation:** D79's literal `BASE` subject was retained while Phase D introduced separate `LEAD_BASE`; AC-7 required the composition to be completed. |
| 2 | D80–D82 — principal, rooted delegation and AT activation are distinct | RF principal/unit/root behavior | No; these contracts are implemented and independently exercised. |

## Finding and Correction Classification

| Finding | Material consequence | Failed approved criterion | Rung |
|---|---|---|---|
| Collision and no-key behavior do not apply unambiguously to rendered `LEAD_BASE`, and assurance never exercises that boundary | Duplicate selected-root tasks can render indistinguishable titles or skip the required fail-soft report, defeating the navigation guarantee the owner uses to choose the correct root | TS rev3 AC-7 checkbox 4; AC-7 Gate and Evidence clauses | **Rung 1 — correction inside the approved TS** |

The approved TS already specifies the desired behavior, selected VALUE/ASSURANCE surface and evidence
method. No HL amendment or TS revision is required.

## Proposed Rung-1 Correction Bound

1. In `.tfw/conventions.md` `Session identity`, make the collision subject explicitly cover the
   actually rendered title forms, including both `BASE` and `LEAD_BASE`, while preserving the shortest-
   unique leading stable-key prefix, exact-readback-only success, report-once reasons and continue-
   unclaimed failure behavior.
2. In `docs/scripts/test_runtime_context.py`, extend the source-derived `LeadNavigationCase`/resolver
   with existing-title and stable-key inputs. Exercise a duplicated qualified root title with keys
   `ab7`/`ac9` expecting `· @ab`, the same duplicate with no stable key expecting report-once/no-key
   and unclaimed continuation, and altered readback of the suffixed title.
3. Add output-changing independent mutants that remove `LEAD_BASE` from the collision subject and
   bypass the no-key branch. Each must change the rendered/report projection before rejection. Keep
   the existing ordinary-`BASE`, root/child, continuity, stale/forwarded and readback cases green.
4. Preserve the approved 21 VALUE selector, two ASSURANCE paths, principal/unit/mandate separation,
   admission distinction, Role Locks, direct routes, copy/managed-block parity, historical A–C and
   prior review epochs, strict-build evidence boundary, and both existing debt dispositions. Change no
   profile, runtime/index, Phase E, RTBO, release, tag, push or saved-master integration surface.
5. Because item 1 is later VALUE and item 2 is later ASSURANCE, create a replacement tested Candidate,
   recompute AC-6 from the immutable Baseline/approval epoch, and append cumulative ONB/EV/RF round
   content before returning to this same independent Reviewer task.

This is one proposal, not an acceptance ruling or implementation order. It returns directly to the
Phase-D Coordinator under the existing approved TS.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence?
- [x] Every N/A carries a reason? — none used.
- [x] Row 2(a) uses the contract baseline and North Star, not the TS/Phase HL, with clause and harm?
- [x] Rows 7 and 8 are answered separately?
- [x] Verify V13–V14 are cited in the DoD assessment?
- [x] Existing debt rows retain Coordinator rulings and consequences?
- [x] RF §7–§9 and current `KNOWLEDGE.md` were checked?
- [x] Fact Candidates reviewed? — none.

Stage complete: YES
