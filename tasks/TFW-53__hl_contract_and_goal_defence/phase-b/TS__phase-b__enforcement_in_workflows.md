# TS — TFW-53 / Phase B: Enforcement in Workflows

> **Date**: 2026-08-13
> **Author**: Coordinator (Claude Code)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-53](../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN
> **Baseline**: `git log --format="%h %s"` filtered on `^\S+ \[[^]]*/TFW-53/freeze/`

---

## 1. Objective

Phase A defined the contract. Nothing enforces it yet, and the framework now contradicts itself: `conventions.md` says a frozen section may not be edited, while `plan.md` Step 6c still instructs the coordinator to *"Update HL with research findings"* — the exact line that produced the TFW-49 drift. Two rules in one framework requiring opposite things is worse than either alone. This phase replaces that instruction with classification, gives the amendment verdict both its paths, and makes the researcher propose instead of prescribe.

## 2. Scope

**In:** `.tfw/workflows/plan.md` — Step 4 approval, Step 6c rewrite, verdict handling, re-freeze. `.tfw/workflows/research/base.md` — Step 6 classification.

**Out:** `conventions.md` and the templates (Phase A, shipped — read them, do not edit them). Review (Phase C). Glossary, adapters, version (Phase D). Rejected-task traces (Phase E). Any TD item not listed in §6.

## 3. Principles Check

| # | Principle (HL §7) | Enforced by | Gate |
|---|------------------|-------------|------|
| P2 | Classify, never edit | AC-2 | Step 6c classifies; the "update HL" instruction is gone, not qualified |
| P3 | Structural enforcement over guidelines | AC-1, AC-3 | Approval and re-freeze are recorded acts with artifacts, not advice |
| P4 | Batch, don't interrupt | AC-2 | One escalation per iteration, not one per finding |
| P5 | Evidence, cost, alternative | AC-2 | The escalation message carries all three or it is not an escalation |
| P6 | Narrow D19, don't revoke it | AC-4 | The researcher still feeds the HL; only the frozen channel turns from write to propose |
| P7 | Token density | AC-6 | `plan.md` leaves this phase **shorter** than it entered |
| P8 | Tool-agnostic by behaviour | AC-5 | No platform, shell or vendor named in either workflow |
| P11 | A remark is not a verdict | AC-3 | Both verdict paths are explicit acts |
| P12 | A frozen baseline must be diffable | AC-3 | Re-freeze commit after every approved amendment |
| P1, P9, P10, P13–P17 | — | N/A | Task-level, or owned by Phases A, C, E |

## 4. Affected Files

| File | Action | Words now |
|------|--------|----------:|
| `.tfw/workflows/plan.md` | MODIFY | 1,206 |
| `.tfw/workflows/research/base.md` | MODIFY | 869 |

**Budget:** 0 new, 2 modified. Limits: 14 files, 8 new, 1,200 LOC, 12 modified — all far clear. The binding constraint here is not file count, it is AC-6.

## 5. Acceptance Criteria

### AC-1: Approval is recorded, not implied
`plan.md` Step 4's approval gate writes the contract state into the HL instead of leaving approval implicit (D20's "implicit approval = transition to next status" is the root cause Phase A closed in the artifact; this closes it in the workflow).

- [ ] On approval, Step 4 sets the HL header `Contract` field to the frozen value with the owner and date
- [ ] Step 4 requires the freeze commit **before** the first research iteration, using the recovery-form grammar from `conventions.md` rule 14
- [ ] The step references `conventions.md` §3 for the rules rather than restating them

Gate: read Step 4; confirm the three items. Then confirm no rule text was copied from `conventions.md` — a reference, not a duplicate.
Evidence: `N/A — workflow text.`

### AC-2: Step 6c classifies instead of updating [depends: AC-1]
The core of this phase. Today Step 6c line 106 reads *"Update HL with research findings (present diff to user)"* and line 117 repeats it for the end of research.

- [ ] Both instructions are **replaced, not annotated**. Neither "update HL" survives with a qualifier attached
- [ ] The replacement: read the RES recommendation classes, apply refinements to free sections, write amendment proposals into HL §12 as `PROPOSED`, leave frozen sections untouched
- [ ] Escalation is **one batched message per iteration** carrying evidence, cost and a considered alternative — the three fields §12 already requires
- [ ] The step states that the coordinator may not apply a proposal it filed itself

Gate: `grep -n "[Uu]pdate HL" .tfw/workflows/plan.md` returns nothing. Read the replacement and confirm the four items.
Evidence: Replay one real iteration against the shipped step — take the recommendation rows from `research/iter2/RES.md` and route each using only the shipped text. Record which land as refinements, which as proposals, and any row the step cannot route. A step that cannot route the research this task actually produced is not finished.

### AC-3: Both verdict paths exist, and an approved amendment re-freezes [depends: AC-2]

- [ ] **Approved:** apply to the frozen section, then a re-freeze commit at the new baseline
- [ ] **Rejected:** the row keeps its verdict and stays; the original contract continues to hold; work resumes without further ceremony
- [ ] A restrictive change applies on filing per `conventions.md` rule 10 — the workflow points at the rule rather than restating its classification test
- [ ] The re-freeze instruction names the reserved scope word, not a specific command line

Gate: read the verdict handling; confirm both paths and that neither is left to inference.
Evidence: Confirm against this task's own history — five freeze commits and twelve §12 rows across three amendment rounds. The shipped step must describe what actually happened here. Record any divergence: it is either a defect in the step or an undocumented practice worth naming.

### AC-4: The researcher classifies and never edits [depends: AC-2]
`research/base.md` Step 6 currently produces *"HL Update Recommendations (table)"* — one undifferentiated class.

- [ ] Step 6 requires the two classes Phase A shipped in `templates/RES.md`: `Refinements` and `Amendment Proposals`, each row naming its target HL section
- [ ] The Role Lock restatement is explicit: the researcher proposes; the researcher does not edit the HL
- [ ] D19 is visibly narrowed, not revoked — research still produces HL feedback every iteration

Gate: read Step 6 against `templates/RES.md`; the class names and the target-section column must match the template exactly. Divergent names would split the vocabulary Phase D then has to reconcile.
Evidence: `N/A — workflow text; correctness is agreement with a shipped template, verifiable by reading.`

### AC-5: Neither workflow names a platform, shell or vendor
Phase A removed `Windows` and `Git Bash` from `conventions.md` on the same reasoning: these files are copied into every project, so environment specifics belong in per-project knowledge.

- [ ] `grep -niE "windows|macos|linux|bash|msys|powershell|zsh"` over both files returns 0 matches
- [ ] Where a command form matters, the workflow points at `conventions.md` rule 15 rather than inlining a command

Gate: the grep above.
Evidence: `N/A — a grep is the whole check.`

### AC-6: `plan.md` leaves this phase shorter than it entered [depends: AC-2]
`plan.md` is **1,206 words** against F2's 1,200 hard degradation threshold and a 700–900 working range. It is already over. This phase adds four mechanisms to it.

- [ ] Final word count is **below 1,206** — not "within budget", *lower than the starting figure*
- [ ] The reduction comes from the Step 6c replacement removing more than it adds, not from compressing unrelated steps
- [ ] If the count cannot be met without losing a required mechanism, **stop and report** rather than trimming a mechanism to hit a number

Gate: word count before and after, both recorded with the command used.
Evidence: Record both counts and the per-step delta in the EV file. This is the one criterion most likely to fail honestly; a reported failure with the reason is a pass on the reporting, and a silent trim of a mechanism is a DoF hit.

### Evidence Artifacts

| File | Description |
|------|-------------|
| `phase-b/evidence/EV__phase-b__enforcement_in_workflows.md` | Environment header, per-AC table, verdict _(required)_ |
| `phase-b/evidence/routing_replay.md` | AC-2's replay of `research/iter2/RES.md` rows through the shipped step |

## 6. Technical Guidance

> Reference material. Deviate with justification in the RF.

- **Read Phase A's RF before starting** — not its TS. Its decisions 11–13 set precedent this phase inherits: a rule keeps the instruction and gives up the narrative; the "why" goes to knowledge; no platform in portable core.
- **The two lines to kill are `plan.md`:106 and :117.** They are the template-side twin's counterpart — `templates/RES.md:32` was removed in Phase A, and leaving these would reproduce the failure through the surviving channel.
- **Replacement, not accretion.** Phase A's rule 15 grew 30 → 162 words by annotating instead of replacing, and had to be rebuilt. Same trap, same file class.
- **`conventions.md` is the rulebook; `plan.md` is the algorithm.** Point at rules 1–21; do not restate them. Every sentence copied here is a sentence that will drift.
- **`research/base.md` has room** (869 words) — `plan.md` does not. If a mechanism can honestly live in either, put it in `research/base.md`.
- **This TS is deliberately short.** TD-142 measured Phase A's TS at 4,107 words against a 1,277 median across 64 tasks. Length there did not buy correctness — two blocking contradictions still surfaced at ONB. Ask at ONB; do not expect the TS to have anticipated everything.

## 7. Definition of Failure

- ❌ Either "update HL" instruction survives in any form, including qualified.
- ❌ A mechanism required by AC-1–AC-4 is trimmed or omitted to satisfy AC-6's word count.
- ❌ Rule text from `conventions.md` is copied into a workflow instead of referenced.
- ❌ Any file outside the two named in §4 is modified.
- ❌ A platform, shell or vendor is named in either workflow.
- ❌ The escalation is specified as per-finding rather than batched per iteration.

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| AC-6 is unachievable while adding four mechanisms | It is the likeliest honest failure. AC-6's third bullet makes reporting it the correct outcome; DoF makes trimming a mechanism the wrong one |
| The rewrite restates `conventions.md` and both drift | DoF-3; AC-1 and AC-3 gates both check for reference rather than duplication |
| Step renumbering breaks cross-references | `plan.md` steps are cited from adapters and from `resume.md`. Keep step numbers stable; replace content in place |
| The replay finds rows the step cannot route | That is the point of AC-2's evidence. A row that will not route is a finding, not a blocker — record it |

## 9. Cross-Phase Modifications

| File | Also modified in | Note |
|------|-----------------|------|
| `.tfw/workflows/plan.md` | Phase D | D re-syncs adapter copies of this file. Land the content here; D propagates it |
| `.tfw/workflows/review.md` | Phase C only | Not this phase. If a change seems to belong there, it is Phase C's |

---

*TS — TFW-53 / Phase B: Enforcement in Workflows | 2026-08-13*
