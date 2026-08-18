# POSTMORTEM — TFW-48: Value-First Methodology Rebaseline

> **Status**: ❌ REJECTED — closed unsuccessfully, terminal, the trace is kept
> **Rejected**: 2026-08-04 · **Status assigned**: 2026-08-18 (TFW-53 Phase E)
> **Last live board status**: `🟡 TS (D)` at `5b17786:README.md`:294 — the task was mid-flight when the
> restore removed it, not rejected. The terminal status rests on the owner's verdict in `bc6779e` and
> was **assigned by this phase**, not restored.
>
> This file is a signpost into git history, not a restored artifact. All 75 TFW-48/49 artifacts remain
> in git history and are read with `git show`, never re-added to the working tree.

---

## What the task attempted

TFW was to be re-derived from its north star rather than incrementally patched: philosophy, terminology,
artifacts, workflows, gates, knowledge loop, evidence model, limits and adapters rebuilt as one coherent
methodology, smaller where precision could replace prose and stronger where a structural gate protects
meaning. Approved 2026-07-28, research update approved 2026-07-29. It reached Phase D of four before it
was stopped.

Full HL: `git show 721ca15:tasks/TFW-48__value_first_methodology_rebaseline/HL-TFW-48__value_first_methodology_rebaseline.md`

## The owner's verdict

From the restore commit `bc6779e`, verbatim:

> TFW-48 and TFW-49 remain in Git history as rejected experiments in delegating methodology redesign
> and execution to Codex without sufficient human supervision. They are historical context only and are
> not current methodology authority.

The same commit records how it was carried out: *"Executed by Codex under explicit user instruction.
This commit restores content without rewriting history and grants no publication authority."*

TFW-48 has no verdict of its own — this ruling names both tasks jointly. That is why the board row says
the status was assigned rather than restored.

## The failure mechanism

Stated as a mechanism, because the mechanism is what transfers:

**Blanket delegation granted at approval time → research produces a scope-expanding signal → the same
coordinator amends the approved HL to absorb it → phase TSs derive from the amended HL → reviewers
verify RF against those TSs → nothing in the chain ever compares the result to what the owner
approved.**

Every step is individually defensible. Nothing in the framework, as it then stood, compared the finished
work against the approved contract, so the drift was never detectable from inside the process. Seven
REVIEW verdicts were issued across TFW-48 and TFW-49, six of them `✅ APPROVE`, on work the owner then
rejected wholesale.

This is the failure [TFW-53](../TFW-53__hl_contract_and_goal_defence/HL-TFW-53__hl_contract_and_goal_defence.md)
was written to answer: an approved HL becomes a frozen contract, changes to it go through a logged
amendment with an explicit owner verdict, and the reviewer gains a Purpose Check whose reference is the
committed contract baseline — never the TS, which is downstream of any drift.

## Recovering the full artifacts

| What | Reference | How |
|------|-----------|-----|
| All 75 TFW-48/49 artifacts | `721ca15` | `git show 721ca15:<path>` · list with `git ls-tree -r --name-only 721ca15 -- tasks/` |
| The removal | `bc6779e` | Blob-for-blob restore to the v0.9.0 tree — 149 files changed, 27,103 deletions |
| The pre-restore board rows | `5b17786:README.md`:294–295 | `git show 5b17786:README.md \| sed -n '294,296p'` |

## What replaced it

**Nothing replaced it. No successor task has been chartered.**

---

*POSTMORTEM — TFW-48 | written 2026-08-18 by TFW-53 Phase E*
