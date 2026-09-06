# REVIEW rev3 — TFW_20260902-111644_CRATM / Phase D: Team mode and Role Assignment

> **Date**: 2026-09-06
> **Author**: Codex (same independent Reviewer; acting as `saubakirov`)
> **Verdict**: 🔄 REVISE
> **RF**: [RF Phase D](RF__phase-d__team_mode_and_role_assignment.md), Round-3 dispatch tip `56128d282dd19ecb0aaaab6027a87d82911b845d`
> **TS**: [TS Phase D revision 3](TS__phase-d__team_mode_and_role_assignment__rev3.md), approved at `b755de9128f2b0442615a4ca8b787761f937bbcd`
> **Candidate**: `2363c3d315a855fc0bd6c6dbf683e16bfbaf1726`
> **Prior REVIEW**: [revision 2](REVIEW__phase-d__team_mode_and_role_assignment__rev2.md)
> **Stage files**: `review/rev3/map.md`, `review/rev3/verify.md`, `review/rev3/judge.md`

---

## 1. Map

Round 3 correctly separates one selected LEAD principal from distinct, directly addressable working
units; only the exact selected root Coordinator qualifies for the handle-bearing Plan/Resume title.
The 21 VALUE + 2 ASSURANCE Candidate also preserves the supplied/additional admission distinction,
copy parity, historical epochs and human-rooted operational chain.

The required collision composition is incomplete. Canon defines the new rendered title as
`LEAD_BASE`, but its inherited collision rule still applies only to `duplicate(BASE)`. The new
source-derived navigation oracle has no collision inputs, cases or mutants, so its green results
cannot establish AC-7's required collision/no-key behavior for the handle-bearing root title.
Separately, the Phase-D continuation assurance admits the new REVIEW sibling but rejects the three
workflow-required `review/rev3/` stage traces, so the prescribed review record makes that guard fail.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|---|---|---|
| V1 | Approval, Candidate and post-Candidate lineage | VERIFIED | Approval `b755de…` precedes Candidate `2363c3d…`; Candidate parent `6a5ee86…`; EV/RF/state/dispatch follow as TRACE only. |
| V2 | Complete Candidate surface | VERIFIED | Candidate modifies exactly 21 approved VALUE + 2 ASSURANCE paths; all 23 current blobs equal Candidate. |
| V-accounting | Independent value-bearing replay | VERIFIED | Baseline `8e68ab37d300122ff110500ad58f354f76b6210f`; Candidate `2363c3d315a855fc0bd6c6dbf683e16bfbaf1726`; exact literal membership 21; 459 additions + 462 deletions = 921 touched text LOC; binary N/A; actual is 11 below approved 21/932 and retains historical 16/640. |
| V3 | WIP and approval-epoch boundary | VERIFIED within recorded pre-act boundary | Receipt records identical before/after digest `ff36d393785fd6450ac0717603e47ad668e695026ed818454992dc4262be1719`, 20 unique paths, cached/untracked 0/0; five incoming TRACE paths have zero overlap. Six later-edited pre-Candidate blobs are no longer reconstructible; this limit is stated in the raw verification. |
| V4 | A5 attention measurements | VERIFIED | Direct measurer replay: active corpus 33,676/33,749 and central range 160/260, both below; all route caps cross; every workflow-local net is negative; no cap ratchet. |
| V5 | AT, authority, unit, admission and consumer behavior | VERIFIED | 14 mode cases, 75 Phase-D mutants, exact five-canon/ten-copy parity, managed-block parity, combined supplied/additional admission, direct root/child and replacement behavior. |
| V6 | Root/child navigation | VERIFIED for modeled cases | 16 cases and 14 mutants establish root qualification, Plan↔Resume continuity, child/invalid-source ordinary cues and altered-readback reporting. |
| V7 | Rendered LEAD collision and no-key behavior | FAILED | `.tfw/conventions.md:378` defines `LEAD_BASE`; line 398 says `duplicate(BASE)`. Stable-key duplicate expects `LEAD · cratm-main · CRATM · D · @ab` but no canonical `LEAD_BASE` suffix branch exists; without a key the fail-soft entry is ambiguous/absent. |
| V8 | Navigation assurance sufficiency | FAILED | `LeadNavigationCase`/resolver has no existing-title or stable-key input, the 16 cases contain no collision fixture, and the 14 mutants contain no collision/no-key target. Old collision tests exercise ordinary `BASE`. |
| V9 | Historical A–C/revision epochs | VERIFIED | Direct approval→Candidate byte checks and targeted integration protect phases A–C, master/phase HL, original/rev2/rev3 TS, original/rev2 REVIEW/stages, release/config/glossary/knowledge; Phase E absent. |
| V10 | Full verification and build at dispatch/pre-review tip | VERIFIED there | Targeted integration 11 passed/106 deselected; full suite 667 passed/1 skipped in 434.28s; strict MkDocs exact command exit 0; `git diff --check` exit 0. |
| V11 | Strict-build warning boundary | VERIFIED exactly | 24/24 pre-Candidate/Candidate tracked-Markdown token occurrence pairs independently match; this is not treated as full-log equivalence. |
| V12 | Knowledge citations | VERIFIED | 38 master-HL + 11 Phase-HL + 31 ONB rows = 80/80 source/item/semantic matches; 28 explicit local links resolve with zero missing paths; no current KNOWLEDGE contradiction beyond the AC-7 composition identified below. |
| V13 | Post-review continuation boundary | FAILED | The focused Phase-D continuation test fails after the required review commit: `_phase_d_allowed_continuation()` admits the REVIEW rev3 sibling but rejects `review/rev3/{map,verify,judge}.md`; 1 failed/116 deselected. |

Raw commands, per-claim results, evidence limits and the mandatory collision probe are recorded in
[verify.md](review/rev3/verify.md).

## 3. Judge

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD / all TS AC | ❌ | AC-1–AC-5 hold. AC-6's legal-continuation guard fails after prescribed review traces land; AC-7 checkbox 4 and its source-derived evidence gate fail because collision does not cover `LEAD_BASE`. |
| 2 | Purpose and design | (a) ✅ (b) ❌ | Purpose remains aligned with the frozen owner-inspectable LEAD outcome and NS1; design is unsound where the new rendered form bypasses the inherited uniqueness/fail-soft rule. |
| 3 | Debt disposed by consequence | ✅ | The two original rows retain terminal Coordinator rulings and barring clauses; this acceptance failure is not debt. |
| 4 | Style and standards | ❌ | A normative grammar names two title forms, then applies collision only to one; the omission changes observable behavior. |
| 5 | Observations collected | ✅ | Original observations remain; the new defect is recorded as a verdict finding. |
| 6 | RF §7–§9 complete | ✅ | All three sections are present and explicitly empty; no new fact candidate, insight or diagram is owed. |
| 7 | Evidence exists | ✅ | Cumulative EV and all seven Round-3 attachments exist and resolve. |
| 8 | Evidence is sufficient | ❌ | Green navigation records cannot prove a branch they never model, and the continuation assurance turns red at the committed-review boundary. |
| 9 | Backward compatibility | ❌ | Ordinary `BASE` retains collision handling, but the new handle-bearing root form does not inherit the existing safeguard AC-7 promised; landing required rev3 stage traces also makes the Phase-D boundary assurance fail. |
| 10 | Safety | ✅ | Reviewer changed trace artifacts only and performed no implementation, lifecycle, dispatch, release, push or destructive action. |

Purpose outcome: **Aligned**. Design outcome: **unsound inside the approved TS**. The material harm
is navigational, not an authority leak: duplicate selected-root titles can prevent the owner from
distinguishing which root to inspect or continue. The full Purpose Check, D79–D82 comparison and
correction classification are in [judge.md](review/rev3/judge.md).

## 4. Verdict

**🔄 REVISE**

Two material Rung-1 defects are confirmed. First, the selected root renders a separate handle-bearing
`LEAD_BASE`, but the canonical collision rule and new assurance still operate only on ordinary
`BASE`. Therefore duplicated qualified-root titles cannot deterministically receive the shortest-
unique stable-key suffix or the no-key fail-soft result required by the approved TS. Second, the
Phase-D continuation allowlist admits the new REVIEW sibling but rejects its three required rev3
stage traces, making the repository's focused boundary guard fail when the prescribed review record
is committed.

### If REVISE — proposals to coordinator

1. **Apply and prove collision/readback/fail-soft behavior on the actually rendered handle-bearing
   LEAD title.** **Basis:** TS revision 3 AC-7 checkbox 4, plus its Gate and Evidence clauses.
   **Owner/rung:** Phase-D Coordinator, **Rung 1**, because the approved TS already specifies the
   desired behavior, selected VALUE/ASSURANCE paths and evidence method. **Observable completion
   condition:** canon unambiguously covers both `BASE` and `LEAD_BASE`; a duplicated root title with
   stable keys `ab7`/`ac9` renders `LEAD · cratm-main · CRATM · D · @ab` and succeeds only on exact
   readback; the same duplicate without a key reports once and continues unclaimed; altered readback
   reports once and continues unclaimed; source-derived cases and independent mutants expose each
   branch; all existing ordinary-title, root/child, continuity, admission, copy, history, full-suite
   and strict-build checks remain green.

2. **Admit the complete workflow-required rev3 review trace set at the continuation boundary.**
   **Basis:** TS revision 3 AC-6 checkboxes 2, 4 and 6. **Owner/rung:** Phase-D Coordinator,
   **Rung 1**, because this is a bounded assurance correction inside the approved continuation and
   evidence contract. **Observable completion condition:** at a committed post-review tip, the
   focused Phase-D boundary test admits exactly the rev3 REVIEW sibling and
   `review/rev3/{map,verify,judge}.md` as legal TRACE while still rejecting arbitrary product,
   assurance and unrelated trace paths.

**Proposed correction bound:** modify only `.tfw/conventions.md` and the necessary Phase-D assurance
inside `docs/scripts/test_runtime_context.py` and `docs/scripts/test_integration.py`, unless exact
evidence proves another already-approved 21-path/2-assurance member is mechanically necessary.
Preserve the approved selector, principal/unit/
mandate separation, root-only qualification, admission distinction, Role Locks, direct routes,
copy/managed-block parity, historical A–C/revision epochs, strict-build token/count evidence boundary,
and both existing debt dispositions. Do not change profiles, runtime/index behavior, Phase E, RTBO,
release/tag/push, saved-master integration or the TS/HL. Produce a replacement tested Candidate,
recompute AC-6 from the immutable Baseline/approval epoch, append cumulative ONB/EV/RF round content,
and return to this same independent Reviewer task.

These are two proposals, not a Coordinator ruling or implementation order. Phase lifecycle remains RF.

## 5. Tech Debt Collected and Disposed

The two original rows and their Coordinator rulings remain unchanged in substance. Neither is
reopened, and the new AC-7 failure is not classified as debt.

| # | Source | Severity | File | Description | Disposition |
|---|---|---|---|---|---|
| 1 | RF §6 observation 1 | Med | `.tfw/scripts/gen_index.py:746` | Current event reader omits template-valid `writer`. | **not material — owed and forbidden to pay (Coordinator ruling, 2026-09-06).** Approved Phase-D scope excludes the runtime/script repair and master A1/A2 rejected that carrier. |
| 2 | RF §6 observation 2 | Low | `workspace/2026/TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md:9` | Immutable historical summary exceeds today's 120-code-point limit. | **not material — owed and forbidden to pay (Coordinator ruling, 2026-09-06).** The TS excludes this repair and immutable history forbids payment here. |

## 6. Traces Updated

- [x] New Reviewer revision created as `REVIEW__phase-d__team_mode_and_role_assignment__rev3.md`; original/rev2 REVIEWs remain untouched.
- [x] New stage traces created only under `review/rev3/`; original/rev2 stage files remain untouched.
- [x] Phase lifecycle remains `RF`; no status or journal transition is made by a REVISE verdict.
- [x] Task lifecycle remains `PHASES`; master/phase HL and approved TS remain unchanged.
- [x] Candidate, approval epoch, post-Candidate TRACE, protected history and debt rulings remain intact.
- [x] tfw-docs: **Applied previously and preserved; not rerun for a REVISE proposal.**
- [x] tfw-knowledge: **N/A — no Fact Candidates.**

## 7. Fact Candidates

No fact candidates.

---

*REVIEW rev3 — TFW_20260902-111644_CRATM / Phase D: Team mode and Role Assignment | 2026-09-06*
