# RF — TFW-46 / Phase B: Workflows + Integration

> **Date**: 2026-07-07
> **Author**: Executor (Antigravity, Claude Opus 4.6)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-46](../HL-TFW-46__evidence_layer.md)
> **TS**: [TS Phase B](TS__phase-b__workflow_integration.md)
> **ONB**: [ONB Phase B](ONB__phase-b__workflow_integration.md)

---

## 1. What Was Done

Evidence Layer Phase B: integrated Evidence concept into TFW's three lifecycle workflows. Added Step 11 (Collect evidence) to handoff.md between build gate and Pre-RF Gate, extended review.md Trust Protocol with evidence-specific entries, added evidence reminder to plan.md Step 7 for coordinators, and fixed TD-1 stale reference in RF.md template.

### Modified Files

| # | File | Change |
|---|------|--------|
| 1 | [handoff.md](../../.tfw/workflows/handoff.md) | New Step 11 (Collect evidence) with proportionality clause, DEFERRED/BLOCKED guidance, proactive tooling note. Old Steps 11-12 renumbered to 12-13. Step 13 mandatory sections now includes §5 Evidence. `Never omit §5.` added |
| 2 | [review.md](../../.tfw/workflows/review.md) | Trust Protocol: 2 new entries — "Evidence: VERIFIED" (Verify level) and "Evidence: N/A" (Challenge level). Step 3 Verify: evidence audit reference pointing to verify.md |
| 3 | [plan.md](../../.tfw/workflows/plan.md) | Step 7 sub-step 3: Evidence fields reminder for coordinators. References TS template grammar. Proportionality note |
| 4 | [RF.md](../../.tfw/templates/RF.md) | Line 68: `§5 Observations` → `§6 Observations` (TD-1 fix from Phase A REVIEW) |
| 5 | [README.md](../../README.md) | Task Board: TFW-46 status updated, Phase B TS/ONB links added |

## 2. Key Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| K1 | Step 11 stays domain-agnostic — lists environment types (deployed service, browser, rendered document, running query, opened file) without naming specific tools | Per TS DoF-1 and HL P4. Tool names would restrict Evidence to code-only workflows |
| K2 | `Never omit §5.` as a separate sentence before `Never omit §7-9.` | Two distinct constraints: §5 = evidence completeness, §7-9 = knowledge sections. Merging into `§5, §7-9` would conflate unrelated concerns |
| K3 | plan.md evidence reminder as sub-step 3 (after budget check) | Coordinator is already in "writing AC items" cognitive mode at this point. Same pattern as Step 4a's PV scan reminder — pointer, not duplication |
| K4 | Trust Protocol evidence entries placed between "DoD met" and "No diagrams needed" | Follows semantic grouping: verification-type entries (Tests, Files, DoD, Evidence) grouped before challenge-type entries (Diagrams, FC). Evidence entries naturally extend the "verify claims" cluster |

## 3. Acceptance Criteria

- [x] **AC-1: Evidence Collection step in handoff.md** — Step 11 exists between build gate (Step 10) and Pre-RF Gate (Step 12). Proportionality clause present ("If NO TS AC items have Evidence fields — skip this step entirely"). DEFERRED/BLOCKED guidance present. Proactive tooling note present. No specific tool names. Steps 11→12, 12→13 renumbered. Step 12 (Pre-RF Gate) unchanged. Step 13 mandatory sections includes §5 Evidence. `Never omit §5. Never omit §7-9.`
- [x] **AC-2: Trust Protocol extended in review.md** — 2 new entries: "Evidence: VERIFIED" (Verify level, check artifact exists), "Evidence: N/A or no evidence" (Challenge level, check TS had Evidence fields). Existing entries unchanged. RF §5 referenced correctly.
- [x] **AC-3: Evidence reminder in plan.md** — Step 7, sub-step 3. 3 lines: consider Evidence fields, write `Evidence:` field, proportionality note. References TS template grammar. No duplication.
- [x] **AC-4: Review.md Step 3 evidence reference** — 1 line added: "Check evidence: verify.md includes an Evidence Verification section — audit evidence artifacts against RF §5 claims."
- [x] **AC-5: Fix TD-1 from Phase A** — RF.md line 68: `§5 Observations` → `§6 Observations`.

## 4. Verification

- Lint (`echo "configure your lint command"`): N/A (markdown-only changes)
- Tests (`echo "configure your test command"`): N/A (no executable tests for .tfw)
- Verify (`echo "configure your verify command"`): N/A (no verify command configured)

**Manual verification performed:**
1. handoff.md: Step numbering verified (7, 8, 9, 10, 11, 12, 13). Step 11 is between Step 10 (build gate) and Step 12 (Pre-RF Gate). §5 Evidence in mandatory sections list.
2. review.md: Trust Protocol now has 9 entries (was 7). Two new evidence entries correctly placed. Step 3 has evidence audit reference.
3. plan.md: Sub-step 3 exists after budget check (sub-step 2), before small/large task branching.
4. RF.md: Line 68 now reads `§6 Observations` (was `§5 Observations`).

## 5. Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Step 11 present in handoff.md with all required elements | Local file | VERIFIED | handoff.md lines 85-90 |
| E2 | AC-1 | Step renumbering 11→12, 12→13 correct | Local file | VERIFIED | handoff.md lines 94, 96 |
| E3 | AC-1 | §5 Evidence in mandatory sections + Never omit §5 | Local file | VERIFIED | handoff.md lines 101, 106 |
| E4 | AC-2 | 2 new Trust Protocol entries present with correct trust levels | Local file | VERIFIED | review.md lines 45-46 |
| E5 | AC-3 | Evidence reminder in plan.md Step 7 sub-step 3 | Local file | VERIFIED | plan.md lines 125-127 |
| E6 | AC-4 | Step 3 evidence reference present | Local file | VERIFIED | review.md line 77 |
| E7 | AC-5 | TD-1 stale ref fixed | Local file | VERIFIED | RF.md line 68 |

Evidence verdict: 7/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `plan.md` | 130 | numbering | Small task sub-steps use `3a, 4a, 5a` while new evidence step is `3`. When coordinator executes, the numbering might cause brief confusion (budget=2, evidence=3, then 3a for TS writing). Pre-existing pattern — not introduced by this change |
| 2 | `glossary.md` | 48 | stale-ref | `RF §7 "Strategic Insights (Execution)"` should be `RF §8` after Phase A renumbering. Already noted in Phase A RF obs #2 and routed to Phase C |

## 7. Fact Candidates

No fact candidates.

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

No diagrams.

---

*RF — TFW-46 / Phase B: Workflows + Integration | 2026-07-07*
