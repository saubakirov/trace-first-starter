# HL — TFW-55 / Phase A.2: North Star Values and Consumer Integrity

> **Date**: 2026-08-26
> **Author**: Coordinator
> **Status**: ✅ HL_APPROVED — Amendment A7 and this derivation approved by the owner 2026-08-26
> **Parent HL**: [HL-TFW-55](../HL-TFW-55__canonization_program.md)
> **Pre-A7 master baseline**: `e3e7b33` — latest reachable TFW-55 freeze commit before this correction
> **Approved amendment**: A7 (`EXTEND`) — approved and applied 2026-08-26; recover the new baseline through the master HL `freeze` commit filter
> **Prior Phase A**: [RF](RF__phase-a__canonical_foundation_essay.md) · [REVIEW](REVIEW__phase-a__canonical_foundation_essay.md) — `✅ APPROVE` remains unchanged
> **Authority**: derivation-only; the master HL owns Vision, Target State, Phases, DoD, DoF, and Principles
> **Execution gate**: passed by explicit owner approval; `/tfw-handoff` may start only from the new narrow re-freeze commit

---

## Corrective Context

The current `.tfw/README.md` is a good problem-led Project North Star. Phase A rewrote that one production file under a TS that explicitly excluded glossary, workflows, and templates. Its Reviewer then found two stale consumers—PV priority 1 in `.tfw/glossary.md` and the Project North Star example in `.tfw/templates/HL.md`—but treated them as non-blocking because the file pointers still resolved.

That scope and acceptance boundary was materially incomplete. PV priority 1 is not optional documentation: every Coordinator must scan it during `/tfw-plan`, and every Reviewer must verify the resulting citations. A pointer to a real file but a deleted section is a false input. The current TFW-60 master HL demonstrates the propagation: its header and §7.2 cite `The Thesis`, `Values and Principles`, and `Success Criteria`, none of which exists in the current essay.

Corrective Phase A.2 repairs this omission without rewriting the good essay, revoking the old verdict, or pretending the failure never passed review.

```text
                 CORRECTIVE PHASE A.2

 TFW-25 values + TFW-32 success outcomes
                     │
                     ▼
        explicit disposition, no silent loss
                     │
                     ▼
 .tfw/README.md stays a coherent North Star essay (≤4,200 words; no filler)
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
 current PV consumers       current task consumer
 glossary / HL template     TFW-60 header + §7.2
 plan / review / verify
          └──────────┬──────────┘
                     ▼
  links resolve AND claimed meaning is actually present
```

## Verified Planning Snapshot

| Item | Snapshot at planning | Consequence |
|---|---|---|
| Repository HEAD | `9bf1f57480221005e45579dcea15478f9b3d3af1` (detached worktree) | No planning or later execution step may assume a clean branch or exclusive checkout |
| Pre-A7 TFW-55 contract baseline | `e3e7b33` — `[codex/TFW-55/freeze/coordinator] supersede Phase B doorway contract` | The approved A7 is applied at a new narrow re-freeze baseline before handoff |
| `.tfw/README.md` tracked baseline | blob `71a4d725cff7d0d7508403589195e9f87a0fc49a` | Prior reviewed essay remains the semantic baseline |
| `.tfw/README.md` working snapshot | SHA-256 `876e6dca71e4d3ebbc3c13aebf758bd6d02a17a90a05c09cd16cbe5b1ebdd21b`; 1,555 whitespace-delimited words | Includes an owner/parallel four-line brand image insertion; preserve and integrate it, do not claim or remove it |
| North Star ceiling | 4,200 descriptive whitespace-delimited words | 2,645 words of measured headroom from the planning snapshot; this is safety margin, not a target or permission for filler; if quality still does not fit, stop for a new owner amendment instead of cutting meaning |
| Other pre-existing dirty state | modified `README.md` (TFW-60 Phase A row), modified TFW-55 `research/iterations.yaml`; untracked TFW-54 HL, TFW-55 iter2/tmp corpus, and TFW-60 `phase-a/` | Treat all as foreign/shared state; only exact in-scope hunks may be touched or staged |
| TFW-60 Phase A draft | untracked `phase-a/HL__phase-a__task_state_and_coordination.md`, blob hash `146828bfe6caa7b2c56b5813dcf26df78377fe2f` at planning | Phase A.2 may correct only the tracked TFW-60 master header and free §7.2; it must not edit, overwrite, add, or stage the parallel phase draft |
| Knowledge Gate | current sequence 60 − consolidation 58 = 2; hard interval 5 | Passed; no new consolidation or research is required for planning |

The Executor must capture the complete baseline again at handoff. This table is provenance, not permission to overwrite changes made after planning.

## Disposition Contract

Every row below must appear in the final EV/RF ledger with one of exactly three dispositions: `EXPLICIT RESTORE`, `SEMANTIC MERGE`, or `INTENTIONAL RETIRE`. A merge names the surviving clause and why it is equivalent. A retirement names the contradiction or obsolete assumption. Absence is never a disposition.

### TFW-25 values

| Approved value | Planned disposition | Canonical requirement and reason |
|---|---|---|
| Traces Over Code | `SEMANTIC MERGE`; retire the literal slogan | Preserve selected durable Trace, continuity, and rationale in `NS2`; do not restore disposable-code, software-only, or deterministic-regeneration claims |
| Candor Over Flattery | `EXPLICIT RESTORE` | Name it in the North Star and connect it to evidence-backed disagreement, surfaced risk, and refusal to flatter |
| Completeness Over Speed | `SEMANTIC MERGE` | Map it to complete, usable, bounded results and explicit close/continuation; do not make speed or artifact volume the success metric |
| Honesty Over Convincingness | `SEMANTIC MERGE` | Map it to visible uncertainty, no fabricated evidence, and bounded capability claims; retain the behavior without inflating the principle list mechanically |
| Structural Enforcement | `EXPLICIT RESTORE` | Name it as a current normative methodology value: important gates live in structure and observable state, not exhortation alone |
| Naming Creates Behavior | `EXPLICIT RESTORE` | Name it and state that precise terms shape agent behavior and must map to the intended cognitive role |
| Single Source of Truth | `SEMANTIC MERGE` | Map it to `Where truth belongs`: one authoritative owner per truth type, not one monolithic file or duplicated authority |
| Portability | `EXPLICIT RESTORE` | Name ordinary durable files and provider independence without claiming every realization is Markdown-only |

### TFW-32 team-centric Success Criteria

| Approved outcome | Planned disposition | Canonical requirement and reason |
|---|---|---|
| Any team member can resume from any checkpoint | `EXPLICIT RESTORE` | Add a visible Success Criteria location; qualify the actor as authorized and avoid “no context lost” absolutism |
| Every decision is traceable | `SEMANTIC MERGE` | Require material decisions, alternatives, evidence, and disposition to be traceable; “every” is too absolute for selected Trace |
| Knowledge compounds over time | `EXPLICIT RESTORE` | State that reviewed and verified knowledge can compound; do not claim automatic or lossless compounding |
| The output requires no manual editing | `INTENTIONAL RETIRE` | This conflicts with explicit human judgment/acceptance and implies deterministic prompt regeneration. Replace the success test with a complete, usable, inspectable result that needs no placeholders or reconstruction but still requires authorized acceptance |

No concrete contradiction was found for Candor, Naming, Portability, or Structural Enforcement. They therefore receive explicit canonical places. The owner approved retirement of the fourth Success Criterion and semantic retirement of the literal `Traces Over Code` slogan; execution may not silently choose a different disposition.

## Active Consumer Boundary

| Class | Files | Phase A.2 treatment |
|---|---|---|
| Canonical North Star | `.tfw/README.md` | Bounded editorial integration only; preserve essay shape, current claims, brand insertion, and ≤4,200-word ceiling; do not expand toward the ceiling |
| Current normative PV contract | `.tfw/glossary.md`, `.tfw/conventions.md` | Point priority 0/1 to real current clauses and define semantic-relevance verification, not file existence alone |
| Current planning carriers | `.tfw/templates/HL.md`, `.tfw/workflows/plan.md` | Use real North Star anchors; make priorities 0–4 a full scan and require distinct semantic citation even when priorities 0/1 share a file |
| Current review carriers | `.tfw/workflows/review.md`, `.tfw/templates/review/verify.md` | Require a full PV scan and verify that priority 0/1 citations resolve to the claimed clause and apply to the task |
| Installed full-copy adapters | `.claude/commands/tfw-plan.md`, `.agent/workflows/tfw-plan.md`, `.claude/commands/tfw-review.md`, `.agent/workflows/tfw-review.md` | Exact copies of their canonical workflows after the source edits; drift check is mandatory |
| Current downstream task | `tasks/TFW-60__conflict_resistant_shared_workspace/HL-TFW-60__conflict_resistant_shared_workspace.md` | Correct only the Project North Star header and free §7.2 citations to current anchors/meaning; frozen claims and parallel Phase A draft stay untouched |
| Current knowledge/debt indexes | `KNOWLEDGE.md` D44/current TFW-55 entry; `TECH_DEBT.md` TD-166 | Correct or close only after formal REVIEW APPROVE through the appropriate Reviewer/`/tfw-docs` stage; not Executor production scope |
| Immutable history | TFW-25, TFW-32, TFW-55 Phase A/B/B.2 artifacts, old REVIEW and stage files, `.tfw/CHANGELOG.md`, Git history | Read and cite; never rewrite merely because a string search finds an obsolete heading or claim |

The rule is behavioral: a current file that instructs a present or future workflow is an active consumer; a task trace records what was true or decided at that time and remains history unless it is itself the explicitly active task contract.

## Deliverables

1. Preserve the current North Star essay and integrate the approved value/Success-Criteria dispositions coherently within 4,200 descriptive whitespace-delimited words; use only the prose needed for meaning and do not treat the ceiling as a target.
2. Repair glossary, conventions, HL template, plan workflow, review workflow, and verify template so PV priorities 0/1 have current semantic targets and the Coordinator/Reviewer gates cannot pass on link existence alone.
3. Synchronize the four installed plan/review workflow copies and prove byte identity with canonical sources.
4. Correct the current TFW-60 master HL Project North Star header and free §7.2 citations without modifying frozen claims or parallel Phase A work.
5. Produce new Phase A.2 ONB, EV, and RF that preserve the exact starting snapshot, disposition ledger, active/history census, word/anchor/link checks, semantic fixtures, adapter drift checks, and old-APPROVE correction provenance.
6. Run a separate `/tfw-review` after execution. Use new stage files under `phase-a/review/phase-a2/`; allow at most three formal REVIEW returns before mandatory owner escalation.
7. Only after REVIEW APPROVE, run `/tfw-docs` as a separate Coordinator stage to correct current KNOWLEDGE wording and close or reclassify TD-166. Do not begin the BoK.

## Explicitly Not in Phase A.2

- a rollback to the old `.tfw/README.md`, a mechanical insertion of the old eight paragraphs, or a second values manual beside the essay;
- edits to the original Phase A RF, REVIEW, EV, review-stage files, TFW-25/TFW-32 history, or any old verdict;
- changes to the root README public guide, localizations, Editions, runtime, product code, docs site, brand assets, or TFW-60 frozen claims/Phase A draft;
- a BoK, guide, course, book, governance layer, claims registry, or new research iteration;
- accepting a word-count overrun, filler toward the ceiling, foreign dirty-state change, or broader scope through delegated authority;
- collapsing the required role sequence: `/tfw-docs` remains forbidden before REVIEW APPROVE, and the Executor may not write REVIEW.

## Research Decision

No new `/tfw-research` iteration is justified. The owner correction identifies the missing values and active consumers, TFW-25 and TFW-32 provide the approved source semantics, the current repository proves the broken references, and Phase A's own review stage records the mistaken acceptance boundary. The owner has now ruled on A7, both retirements, the full consumer-integrity scope, and the 4,200-word ceiling; no material empirical uncertainty remains.

## Approval and Review Control

The owner explicitly approved A7, this Phase HL, and the Phase A.2 TS together on 2026-08-26, including both retirements and the full consumer-integrity scope. The owner amended the ceiling to 4,200 descriptive whitespace-delimited words, explicitly as a maximum rather than a target. The Coordinator records that verdict, applies the frozen §4/§5/§6 extension, and creates a new narrow freeze commit before `/tfw-handoff`.

Execution and formal review use separate sessions. A `REVISE` returns to the same Phase A.2 execution chain. After three formal returns, work stops and the owner decides whether to narrow, amend, or reject; a fourth automatic cycle is prohibited.

## Phase-Local Risks

| Risk | Control in TS |
|---|---|
| Restoring values mechanically bloats or degrades the essay | Disposition ledger, coherent-essay test, 4,200-word maximum, explicit no-filler rule, and stop-for-amendment gate |
| A slogan restores code-centric or deterministic doctrine | Explicit semantic retirement of the literal `Traces Over Code` claim and prohibited-claim scan |
| A link resolves while pointing to the wrong meaning | Priority 0/1 semantic fixtures in plan and review ACs; mismatch is a discrepancy |
| Executor rewrites historical traces found by search | Active-consumer/history ledger and path-scope failure condition |
| Owner brand image or TFW-60 parallel work is lost | Full handoff baseline manifest, hunk-level integration, final foreign-state comparison, explicit-path staging |
| Workflow sources and installed copies drift | Source-first edits followed by byte-identity checks for all four copies |
| Success Criteria reproduce old absolutism | Four-row disposition contract and owner ruling on the manual-edit criterion |
| Corrective scope expands into BoK or docs work | Explicit exclusion; `/tfw-docs` only after REVIEW APPROVE; BoK remains forbidden |

---

*HL — TFW-55 / Phase A.2: North Star Values and Consumer Integrity | 2026-08-26*
