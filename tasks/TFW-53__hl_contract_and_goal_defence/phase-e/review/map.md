# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF__phase-e__rejected_trace_restoration.md](../RF__phase-e__rejected_trace_restoration.md)
> TS: [TS__phase-e__rejected_trace_restoration.md](../TS__phase-e__rejected_trace_restoration.md)
> ONB: [ONB__phase-e__rejected_trace_restoration.md](../ONB__phase-e__rejected_trace_restoration.md)
> Contract baseline: `11cd340` (recovered by `conventions.md` §3 rule 15)

## Understanding

TFW's status set could say a task succeeded, was in flight, or was waiting — and nothing at all could say
a task had failed. Closing a failed task meant lying with `✅ DONE`, misusing `❌ BLOCKED` (which means
waiting), or deleting the folder. This project did the third thing: restore commit `bc6779e` took the
tracked tree back to the v0.9.0 blob-for-blob and `README.md` reverted to a state that had never contained
the TFW-48 and TFW-49 rows. Nobody decided to erase the failure status; the restore method erased it.

Phase E ships three things and then uses them once. **The state:** `❌ REJECTED` as a terminal task status
in five carriers — `conventions.md` §5 (diagram *and* table), `project_config.yaml`, its template twin,
`glossary.md` `## Status Flow`, and the README legend. **The rule:** `conventions.md` §13 gains a third
sentence making the erasure a violation — reverting a *result* never reverts its *trace*. **The warning:**
one `conventions.md` §14 anti-pattern for the whole-tree restore, written from the mechanism and naming no
task and no repository. Then the application: two post-mortem files (544 and 727 words) and two restored
board rows, with TFW-48's status marked **assigned now** and TFW-49's a byte-identical **restoration**.

Three decisions shape the result. The status is drawn as a **side node reachable from any status**, not as
a branch under the review verdict `❌ REJECT` — TFW-48 was rejected out of `🟡 TS_DRAFT` without ever
reaching a review, which settles it by counterexample. The `REJECTED` collision is **three-way**, not
two-way (task status · review verdict `❌ REJECT` · HL §12 amendment verdict `❌ REJECTED`), and it is
closed at both ends without editing `templates/HL.md`, which is Phase A's file. And the TFW-49 owner
verdict is quoted **whole**, not elided, because the middle of the block is where the owner listed what was
actually rejected.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — `❌ REJECTED` in all five carriers, terminal, side node, BLOCKED boundary stated, count sentence updated, three-way collision stated at both ends, nothing else in the vocabulary changed | RF §3 AC-1, seven boxes checked; the seven sites quoted in RF §1 | ✅ |
| AC-2 — §13 trace rule and §14 anti-pattern, both added not rewritten, general (no task ID, no repository) | RF §3 AC-2, four boxes checked; both passages quoted | ✅ |
| AC-3 — two rows between TFW-47 and TFW-50, TFW-48 assigned / TFW-49 restored, one-line description cells | RF §3 AC-3, three boxes checked plus one ⚠️ — the rows were in the working tree, not in the phase commit | ⚠️ flagged by the executor; resolved since (see Deviations) |
| AC-4 — five sections in fixed order, verdict verbatim and whole, mechanism as mechanism, resolving git references, what replaced it, one page, identical section order | RF §3 AC-4, seven boxes checked | ✅ |
| AC-5 — one file per folder, nothing from `721ca15` back in the tree, count stated | RF §3 AC-5, three boxes checked | ✅ |
| AC-6 — one `### Added` block under `[Unreleased]`, `[1.2.0]` / `VERSION` / `tfw.version` untouched, recorded as a coordinator scope extension | RF §3 AC-6, four boxes checked | ✅ |
| Frozen DoD-34 / DoD-35 / DoD-36 (baseline `11cd340`) | Covered by AC-1 / AC-2 / AC-3+AC-4 respectively | ✅ |

## Deviations from TS

1. **AC-6 is itself an addition to the TS**, made by the coordinator at the ONB gate (ONB R3) and recorded
   in the TS header and in AC-6's own last bullet as a coordinator scope extension with a stated limit —
   one block under `[Unreleased]`, nothing else in the file. Authorised and bounded, not silent drift.

2. **AC-1 was corrected from four carriers to five** during the ONB, on the ground that the prose said four
   while the enumeration and the gate said five. Frozen DoD-34 names four; all four are inside the five.
   Shipping `templates/project_config.yaml` as well is strictly more complete than the frozen clause, not
   different from it — no amendment required, and the TS says so on the page.

3. **The TS gate predicted seven `REJECTED` hits; the EV reports ten; the actual count is twelve.** The
   executor reconciled seven against ten in the EV file. The reconciliation is itself short by two — see
   verify.md D1. The two missing hits are the phase's own board rows.

4. **`README.md` was left unstaged by design** (TS §9, ONB Q2 answer (b)) because a concurrent TFW-55
   session held it. It has since been committed — by `8d9432b`, whose subject is
   `[claude-code/TFW-58/proposal/coordinator] propose the revise protocol`. The board rows are now in
   history, so AC-3's ⚠️ resolves; the commit subject naming a different task is a trace-attribution
   wrinkle recorded in judge.md, not an executor defect.

5. **The §5 diagram's pre-existing loose `❌ BLOCKED` edge was deliberately not repaired** — TS §7 makes
   repairing it a failure condition, because deciding what transitions into `BLOCKED` is a decision, not a
   tidy-up. RF §6 observation 1 records it instead.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy? *(baseline `11cd340`: P17 "a failed trace is the most valuable trace"; P3 structural enforcement; P9 naming creates behavior; P8 tool-agnostic; §7.1 gives Phase E `conventions.md` §5 + §13 and one §14 entry, and restricts it to visibility only)*
- [x] Read ONB — were blocking questions resolved? *(three blockers: Q1 the three-way collision, Q2 the held `README.md`, Q3 the diagram shape. All answered by the coordinator, all six recommendations approved, R3 promoted to AC-6, and the owner ruled on the vocabulary itself)*

Stage complete: YES
