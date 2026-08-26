# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF production files claimed: 12
> Files to verify: 12 — 100% by the Phase A.2 review contract and mandatory discrepancy escalation

## Verification Log

### V1: `.tfw/README.md`
- **RF claim:** The existing problem-led North Star integrates the approved 8 + 4 meanings without filler, deterministic overclaims, or exceeding 4,200 words.
- **Actual:** The clean file is a coherent 1,857-word / 128-line essay; the independently reconstructed owner-integrated image is 1,864 words / 132 lines. Candor, Structural Enforcement, Naming Creates Behavior, Portability, bounded Trace continuity, four Success Criteria, human acceptance, and one-owner-per-truth semantics are present. Prohibited claims occur only inside explicit negations/non-goals.
- **Match:** ✅

### V2: `.tfw/glossary.md`
- **RF claim:** PV priorities 0 and 1 point to current clauses and define a full semantic scan.
- **Actual:** Priority 0 points to the root purpose surface plus `NS1`–`NS3`; priority 1 points to Methodology values and Success Criteria. Priorities 0–4 full / 5–7 by relevance and resolution/item/meaning/relevance checks are explicit.
- **Match:** ✅

### V3: `.tfw/conventions.md`
- **RF claim:** Knowledge Citations require real-item and semantic-relevance verification, with distinct priority 0/1 meanings.
- **Actual:** The normative citation table requires exact item, concrete application, semantic integrity, and separate purpose versus methodology-value claims even when one file holds both.
- **Match:** ✅

### V4: `.tfw/templates/HL.md`
- **RF claim:** Stale examples are replaced and planning must scan priorities 0–4 in full / 5–7 by relevance.
- **Actual:** Current North Star anchors replace the deleted section; the template requires distinct P0/P1 items, exact clauses, concrete applications, and relevance rather than a file-only citation.
- **Match:** ✅

### V5: `.tfw/workflows/plan.md`
- **RF claim:** `/tfw-plan` has a mandatory semantic Project Values path.
- **Actual:** Step 3 requires the complete priority 0–4 scan, relevant 5–7 scan, distinct P0/P1 meanings, exact item/application, and reasoned N/A only after scanning.
- **Match:** ✅

### V6: `.tfw/workflows/review.md`
- **RF claim:** `/tfw-review` verifies semantic match and relevance and escalates any resolving-but-wrong citation to 100%.
- **Actual:** Verify requires the full PV scan, item/meaning/application checks, distinct P0/P1 handling, and 100% verification after any discrepancy.
- **Match:** ✅

### V7: `.tfw/templates/review/verify.md`
- **RF claim:** The checkpoint records semantic citation outcomes.
- **Actual:** The template records resolution, item existence, meaning, relevance, and total/resolved/semantically verified/irrelevant/hallucinated counts.
- **Match:** ✅

### V8: `.claude/commands/tfw-plan.md`
- **RF claim:** Exact full copy of canonical plan workflow.
- **Actual:** Byte-identical to `.tfw/workflows/plan.md`; SHA-256 `03943bdc67a0e4a196e316304094419a3165f4e815407cad7ed82c3e427519c4`.
- **Match:** ✅

### V9: `.agent/workflows/tfw-plan.md`
- **RF claim:** Exact full copy of canonical plan workflow.
- **Actual:** Byte-identical to `.tfw/workflows/plan.md`; same SHA-256.
- **Match:** ✅

### V10: `.claude/commands/tfw-review.md`
- **RF claim:** Exact full copy of canonical review workflow.
- **Actual:** Byte-identical to `.tfw/workflows/review.md`; SHA-256 `b0d56ed3a8506e195f07582d9e73497a36447d6c7ed19e32b604300217dff181`.
- **Match:** ✅

### V11: `.agent/workflows/tfw-review.md`
- **RF claim:** Exact full copy of canonical review workflow.
- **Actual:** Byte-identical to `.tfw/workflows/review.md`; same SHA-256.
- **Match:** ✅

### V12: `tasks/TFW-60__conflict_resistant_shared_workspace/HL-TFW-60__conflict_resistant_shared_workspace.md`
- **RF claim:** Only the current header and free §7.2 changed; frozen/history and the live parallel Phase A file remained untouched.
- **Actual:** The committed diff has exactly two hunks: the Project North Star header field and five §7.2 rows. The remainder is byte-identical; the external Phase A file remains SHA-256 `767924202e4a75a9790d94628ddcd2b394c18fd70e6ef6fba0c087c643f7e382`.
- **Match:** ✅

## Commands Executed

| # | Command / independent check | Result |
|---|---|---|
| 1 | Exact entry gate: `rev-parse`, porcelain-v2, cached and unstaged diffs | Entry HEAD `6816c6e4a080a90f456769b8309746b82646ef9c`; index/worktree clean; freeze is an ancestor; no merge commit |
| 2 | Disposition parser plus source-to-target comparison | 12 unique rows = 8 TFW-25 + 4 TFW-32; 6 restore / 5 merge / 1 retire; all targets and bounded reasons semantically hold |
| 3 | Independent word/line/hash count on clean and owner-integrated North Star | 1,857 / 128 / `7cbcf1de…`; integrated 1,864 / 132; both ≤ 4,200; owner image preserved exactly |
| 4 | Required/prohibited-clause scans and sentence-level source audit | All restored meanings present; deterministic, disposable-output, lossless-context, automatic-truth, transcript, and independent-authority claims remain bounded negations/non-goals |
| 5 | Exact copy comparisons and repository adapter map | Plan and review triples byte-identical; 11 canonical mappings / 33 files / 0 failures |
| 6 | Positive P0/P1 and negative stale-heading fixtures | P0 and P1: resolution/item/meaning/relevance all true and distinct; old `Values and Principles`: file resolves but item/meaning/relevance all false → discrepancy |
| 7 | New/retargeted local Markdown path and anchor resolver | 34 occurrences checked / 0 failures |
| 8 | Active-consumer stale-string scan | 0 occurrences across all 12 current production consumers |
| 9 | Repository boundary census on clean Executor tree | 46 paths = 44 task traces + 1 changelog + 1 current KNOWLEDGE; 0 active consumers |
| 10 | Same census on disposable owner-integrated result | 47 paths = 45 task traces + 1 changelog + 1 current KNOWLEDGE; 0 active consumers |
| 11 | Same census on untouched live owner tree before integration | 49 paths, but they include stale active `.tfw/glossary.md` and `.tfw/templates/HL.md`; this is not the final image |
| 12 | TFW-60 diff and allowed-region exclusion | Exactly two permitted hunks; no frozen/history diff; parallel Phase A owner file unchanged |
| 13 | Historical preservation diffs | Original Phase A TS/RF/REVIEW/judge, TFW-25, and TFW-32 sources unchanged; original `✅ APPROVE` unchanged |
| 14 | Production changed-path set | Exactly the 12 planned current consumers; no missing or extra production path |
| 15 | Strict UTF-8, mojibake signatures, `git diff --check` | 0 invalid files; 0 mojibake signatures; diff check PASS |
| 16 | Read-only owner manifests plus disposable full-chain integration | Start manifest: 3 tracked / 93 untracked, tracked SHA `bf47bfc4…`, untracked SHA `715cae60…`; patch check/apply PASS; owner image, TFW-60 row/phase work, research state, and all foreign files preserved |
| 17 | Session/return trace | Executor commits are role-tagged separately; Phase A.2 had no REVIEW/stage files at RF tip; formal return counter was 0 before this verdict; the stopped setup task is not counted |

No product build runner applies to these Markdown contracts. The checks above exercise the document, copy, link, encoding, history, and dirty-state contracts directly.

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|---|---|---|---|
| C1 | All 8 TFW-25 values and 4 TFW-32 outcomes have explicit, non-weaker dispositions | EV §2; RF §§3–4 | TFW-25 TS/RF, TFW-32 Phase D source wording, current `.tfw/README.md` clauses | ✅ — 12/12 source items, enums, targets, and reasons hold; the two approved retirements have bounded replacements |
| C2 | North Star is 1,857 clean words and 1,864 after the owner image is integrated | RF §4; EV §§3–4 | Direct UTF-8 counts of the committed file and disposable owner-integrated image | ✅ — independently reproduced; both are far below 4,200 |
| C3 | Foreign owner state survives one application of the Executor chain | RF §4; EV §4 | Read-only manifests from `C:\Users\c0rpa\.codex\worktrees\3936\steps-framework` and disposable apply | ✅ — owner image, root foreign row, TFW-60 phase work, research state, 3 tracked hunks, and 93 untracked files preserved |
| C4 | Repository boundary census has 49 correctly classified final paths | EV §§5, 8 | Clean tip, live owner tree, and disposable owner-integrated tree | ❌ — final images have 46 clean / 47 integrated paths; 49 is the pre-integration live owner count and includes two stale active consumers |

## Discrepancies Found

### D1 — blocking evidence discrepancy: the EV records a non-final census as the final result

EV §§5 and 8 claim `49 Markdown paths` classified as 46 task traces, one changelog, one current KNOWLEDGE path, and one active North Star bounded negation. Independent reproduction gives:

- clean Executor tip: **46** = 44 task traces + CHANGELOG + KNOWLEDGE;
- expected owner-integrated result: **47** = 45 task traces + CHANGELOG + KNOWLEDGE;
- untouched live owner tree: **49**, but that count includes the still-pre-integration stale active consumers `.tfw/glossary.md` and `.tfw/templates/HL.md`.

There is no matching active North Star occurrence in either final image. The twelve active consumers themselves are clean, so AC-5's delivered behavior holds, but AC-9's exact-final EV reproducibility requirement does not. EV and RF must be corrected from a retaken final clean/integrated census, without changing implementation.

### D2 — blocking citation discrepancy: master HL §7.2 row 6 resolves but is partly irrelevant

Master HL §7.2 row 6 cites `knowledge/convention.md F7, F9, F17–F19` for a claim that includes “use newcomer-readable terms.” F7 supports a compact value set, F9 a brand anchor, and F19 naming consistency. F17 is blog tone and F18 is a specific Russian Post 24 structural example; neither supports newcomer-readable terminology or Phase A.2 application. The ONB correctly labels the same bundle `Applied / partly N/A`, but the HL row itself overstates the citation.

This is exactly the resolving-but-wrong case the new gate is meant to detect, so verification was escalated to 100%. It is an upstream free-section trace defect, not an implementation defect and not something the Reviewer may repair. The Coordinator/owner must correct the master HL §7.2 citation/application before the formal return is re-reviewed.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|---|---|---|
| E1 | `phase-a/evidence/EV__phase-a2__north_star_values_and_consumer_integrity.md` | ✅ | ❌ partial — disposition, count, link, copy, encoding, scope, history, and integration claims reproduce, but the exact-final repository census does not |

TS evidence classifications remain correctly represented as 9 N/A and 1 DEFERRED at Executor handoff. The single EV artifact is real but is not fully verified because of D1.

## Knowledge Citations Verified

Priorities 0–4 were read in full; priorities 5–7 were scanned by relevance. Each of the 17 master-HL rows and its 17 ONB confirmations was checked independently. For owner-foreign RES Iteration 2, resolution is against the authoritative read-only owner state that the integration contract preserves.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|---|---|---|---|---|---|
| 1 | HL §7.2 #1 | P0: root `README.md` at `b924926` — project-guide surfaces | ✅ | ✅ | ✅ | ✅ |
| 2 | HL §7.2 #2 | P0/P1: current `.tfw/README.md` essay baseline | ✅ | ✅ | ✅ | ✅ |
| 3 | HL §7.2 #3 | P3: `KNOWLEDGE.md` D2, D35, D40, D52–D60 | ✅ | ✅ | ✅ | ✅ |
| 4 | HL §7.2 #4 | P2: `knowledge/philosophy.md` F3, F6, F8, F10–F16, F21–F25, F32–F33 | ✅ | ✅ | ✅ | ✅ |
| 5 | HL §7.2 #5 | P4: `.tfw/conventions.md` §§3, 11, 14 | ✅ | ✅ | ✅ | ✅ |
| 6 | HL §7.2 #6 | P5: `knowledge/convention.md` F7, F9, F17–F19 | ✅ | ✅ | ❌ — F17/F18 do not support newcomer-readable terminology | ❌ — blog tone/history is irrelevant to the asserted A.2 application |
| 7 | HL §7.2 #7 | P6: `knowledge/process.md` F2, F11, F16, F22, F25, F27 | ✅ | ✅ | ✅ | ✅ |
| 8 | HL §7.2 #8 | P7: `knowledge/constraint.md` F2, F3, F6–F7 | ✅ | ✅ | ✅ | ✅ |
| 9 | HL §7.2 #9 | P7: `knowledge/domain.md` F1–F3 | ✅ | ✅ | ✅ | ✅ |
| 10 | HL §7.2 #10 | P7: `knowledge/stakeholder.md` F1, F4 | ✅ | ✅ | ✅ | ✅ |
| 11 | HL §7.2 #11 | Relevant task history: TFW-32 Phase D | ✅ | ✅ | ✅ | ✅ |
| 12 | HL §7.2 #12 | Relevant task history: TFW-51/52 proportional Editions | ✅ | ✅ | ✅ | ✅ |
| 13 | HL §7.2 #13 | Relevant research: TFW-55 RES Iteration 1 | ✅ | ✅ | ✅ | ✅ |
| 14 | HL §7.2 #14 | Relevant research: TFW-55 RES Iteration 2 | ✅ — authoritative owner state | ✅ | ✅ | ✅ |
| 15 | HL §7.2 #15 | Owner mini-essay 0.8 corpus | ✅ | ✅ — 9 files / 5,589 words | ✅ | ✅ |
| 16 | HL §7.2 #16 | Owner architecture note | ✅ | ✅ — 710 words | ✅ | ✅ |
| 17 | HL §7.2 #17 | Owner working BoK v0.1 | ✅ | ✅ — 6,675 words | ✅ | ✅ — explicitly non-canonical |
| 18 | ONB §7 #1 | P0: root practical-guide baseline | ✅ | ✅ | ✅ | ✅ |
| 19 | ONB §7 #2 | P0/P1: current North Star baseline | ✅ | ✅ | ✅ | ✅ |
| 20 | ONB §7 #3 | P3: `KNOWLEDGE.md` D2, D35, D40, D52–D60 | ✅ | ✅ | ✅ | ✅ |
| 21 | ONB §7 #4 | P2: philosophy facts | ✅ | ✅ | ✅ | ✅ |
| 22 | ONB §7 #5 | P4: conventions §§3, 11, 14 | ✅ | ✅ | ✅ | ✅ |
| 23 | ONB §7 #6 | P5: convention facts with F17/F18 explicitly marked partly N/A | ✅ | ✅ | ✅ — applied subset and N/A subset are distinguished | ✅ |
| 24 | ONB §7 #7 | P6: process facts | ✅ | ✅ | ✅ | ✅ |
| 25 | ONB §7 #8 | P7: constraint facts | ✅ | ✅ | ✅ | ✅ |
| 26 | ONB §7 #9 | P7: domain facts | ✅ | ✅ | ✅ | ✅ |
| 27 | ONB §7 #10 | P7: stakeholder facts | ✅ | ✅ | ✅ | ✅ |
| 28 | ONB §7 #11 | TFW-32 Phase D source | ✅ | ✅ | ✅ | ✅ |
| 29 | ONB §7 #12 | TFW-51/52 proportional Editions | ✅ | ✅ | ✅ | ✅ |
| 30 | ONB §7 #13 | RES Iteration 1 | ✅ | ✅ | ✅ | ✅ |
| 31 | ONB §7 #14 | RES Iteration 2 | ✅ — authoritative owner state | ✅ | ✅ | ✅ |
| 32 | ONB §7 #15 | Owner mini-essay corpus, N/A to reopened source selection | ✅ | ✅ | ✅ | ✅ — reasoned N/A |
| 33 | ONB §7 #16 | Owner architecture boundary | ✅ | ✅ | ✅ | ✅ |
| 34 | ONB §7 #17 | Owner working BoK, N/A to deliverables | ✅ | ✅ | ✅ | ✅ — reasoned N/A |

`KNOWLEDGE.md` D44 still describes the pre-A.2 PV index. That known contradiction is explicitly routed by the TS/RF to post-APPROVE `/tfw-docs`; it does not contradict the delivered current glossary/workflows, but it cannot be closed during this REVISE verdict. TD-166's implementation is present and verified in the template/workflow copies; registry closure remains pending a successful formal return.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈12 × 0.42⌉ files and recorded findings? — 12/12 production consumers plus all task/evidence traces
- [x] Ran at least 1 build/test command (or documented why not)? — direct contract checks listed above
- [x] Claim & Source Checks filled — key claims, every citation, and primary data independently checked?
- [x] Each RF §3 (AC) checkmark verified against actual file? — AC-1–AC-8 and role-separated AC-10 hold; AC-9 fails exact-final evidence reproducibility
- [x] KNOWLEDGE.md checked — D44 documented as the planned post-APPROVE correction?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: 34, resolved: 34, semantically verified: 33, irrelevant: 1, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 1, verified: 0, missing: 0, partial: 1

Stage complete: YES
