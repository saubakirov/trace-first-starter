# POSTMORTEM — TFW-49: Agent Commit Identity and Attribution

> **Status**: ❌ REJECTED — closed unsuccessfully, terminal, the trace is kept
> **Rejected**: 2026-07-31 by owner verdict · **Board row restored**: 2026-08-18 (TFW-53 Phase E)
> **Last live board status**: `❌ REJECTED — complete product-fit failure; superseded by TFW-50` at
> `5b17786:README.md`:295 — this row is a **restoration** of a status the task already carried, unlike
> TFW-48's, which was assigned now.
>
> This file is a signpost into git history, not a restored artifact. All 75 TFW-48/49 artifacts remain
> in git history and are read with `git show`, never re-added to the working tree.

---

## What the task attempted

Every post-activation commit in an agent-managed TFW repository was to identify its operator context at
the start of the subject in one canonical form, so a human or a later agent could filter history by agent
surface, TFW role, task and phase. Provenance rather than decoration, readable without special tooling,
with structural validation preventing drift between roles, adapters and repositories. Approved
2026-07-30; three phases completed and reviewed before the owner ruled.

Full HL: `git show 721ca15:tasks/TFW-49__agent_commit_identity_and_attribution/HL-TFW-49__agent_commit_identity_and_attribution.md`

## The owner's verdict

From the HL header at `ad0696e`, quoted whole — the middle of this block is where the owner named *what*
was rejected, so an elided version loses the substance:

> **Final owner verdict — 2026-07-31:** TFW-49 solved a small prompt-design need
> with an unnecessary software subsystem. The useful outcome is only the readable
> `[surface/task/work/role] summary` format and its purpose. The schema, state,
> Python validator/router/runtime, Git hooks, range audit, installation lifecycle,
> and cross-platform machinery are rejected. Phases A–C remain immutable failure
> evidence; they are not the desired architecture. TFW-50 owns removal and the
> prompt-first replacement. No TFW-49 history is rewritten and no publication is
> authorized.

And from the restore commit `bc6779e`, verbatim:

> TFW-48 and TFW-49 remain in Git history as rejected experiments in delegating methodology redesign
> and execution to Codex without sufficient human supervision. They are historical context only and are
> not current methodology authority.

## The failure mechanism

Stated as a mechanism, because the mechanism is what transfers:

**Blanket delegation granted at approval time → research produces a scope-expanding signal → the same
coordinator amends the approved HL to absorb it → phase TSs derive from the amended HL → reviewers
verify RF against those TSs → nothing in the chain ever compares the result to what the owner
approved.**

TFW-49 shows the mechanism at its clearest, because its own approved contract already contradicted
itself: §1 promised *"readable without special tooling"* and *"provenance, not decoration"*, while DoD-3
required a versioned structural validator. Against a self-contradictory reference set the same evidence
supports both a pass and a block, so reviewers checking each RF against its TS were working correctly and
could not have caught the outcome. Three phases were approved on the way to a complete product-fit
failure.

This is the failure [TFW-53](../TFW-53__hl_contract_and_goal_defence/HL-TFW-53__hl_contract_and_goal_defence.md)
was written to answer: a frozen contract, a logged amendment channel with an explicit owner verdict, and a
reviewer Purpose Check measured against the committed contract baseline rather than the TS — including a
third outcome for exactly this case, where the reference set is internally inconsistent and the defect
belongs to the contract rather than to the work.

## Recovering the full artifacts

| What | Reference | How |
|------|-----------|-----|
| All 75 TFW-48/49 artifacts | `721ca15` | `git show 721ca15:<path>` · list with `git ls-tree -r --name-only 721ca15 -- tasks/` |
| The commit that recorded the approval of TFW-49's research | `9e19a4f` | `[master]: TFW-49: approve agent commit identity research`, 2026-07-30. **Not a contract baseline** — it carries no `freeze` scope word, because that grammar is a product of TFW-50 and TFW-53, both later |
| The owner's final verdict | `ad0696e` | `git show ad0696e:tasks/TFW-49__agent_commit_identity_and_attribution/HL-TFW-49__agent_commit_identity_and_attribution.md` |
| The removal | `bc6779e` | Blob-for-blob restore to the v0.9.0 tree — 149 files changed, 27,103 deletions |
| The pre-restore board rows | `5b17786:README.md`:294–295 | `git show 5b17786:README.md \| sed -n '294,296p'` |

## What replaced it

[**TFW-50**](../TFW-50__minimal_agent_commit_attribution/) — one readable commit-subject rule owned by
`conventions.md`, no runtime. The schema, the Python validator and router, the git hooks and the
installation lifecycle are not part of the replacement.

---

*POSTMORTEM — TFW-49 | written 2026-08-18 by TFW-53 Phase E*
