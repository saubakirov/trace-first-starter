---
time: 2026-09-03T00:00:00+05:00
kind: amendment_escalated
on_behalf_of: saubakirov
via: claude-code
refs:
  - HL-TFW_20260902-111644_CRATM.md
  - research/iter1/RES.md
  - research/iter2/RES.md
  - research/iterations.yaml
summary: "three proposals filed from iter2 and all three rejected the same day; contract unmoved"
---

Both research iterations complete. Iteration 1 (Codex measuring Codex) filed no amendment
proposals. Iteration 2 (Claude measuring its own side and the crossings) filed three, all against
the validator `.tfw/scripts/gen_index.py` or the contract clauses that mention editing it.

All three were ruled `❌ REJECTED` on 2026-09-03. A1 and A2 rest on a carrier the owner is retiring,
which removes the code-versus-markup tension between DoD 5 and DoD 16 outright. A3 fails on a
stronger ground the owner named: Phase B does not add a field beside `actor`, it revives `actor`, so
enforcing a prohibition that this task's own next phase deletes is scaffolding. The coordinator had
carried that proposal forward and was designing an enforcement site for it.

**No re-freeze.** A rejected amendment leaves the original contract in force, so the baseline did not
move and this commit deliberately does not carry the reserved `freeze` scope word. The recovery form
must return exactly one commit for this task until a frozen claim actually changes.

Applied in the same pass: twenty-one refinements to the free sections, from both iterations. The
load-bearing ones correct the coordinator rather than confirm it — a peer Claude session cannot be
created from inside a session, so the delegate a Role Assignment can name is a headless resumable
session that the HL never listed; both vendor crossings work but neither can address the other's
existing session, making a dispatch send-and-wait with follow-up by id; a fourth trace-integrity
corruption was measured through the vendor's session store, which no worktree isolates; and H8 has
no control case in AFD at all — 138 arcs, 7 multi-round, the reviewer unchanged in every one, against
the coordinator's figure of 13.
