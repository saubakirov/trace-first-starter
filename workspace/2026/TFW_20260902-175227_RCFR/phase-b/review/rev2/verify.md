# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 12 revision-2 implementation/test files
> Files to verify: ⌈12 × 0.42⌉ = 6; actual verification: 12/12

## Verification Log

### V1: `.tfw/conventions.md`
- **RF claim:** one source-derived table is the sole rung-1/rung-2/rung-3/mixed REVISE authority.
- **Actual:** the uniquely addressed `The 🔄 REVISE route` table contains all four requested cases
  and all five requested outputs: recipient, ruling site, governing artifact, lifecycle effect, and
  hard stop. `Task Statuses`, `Role Lock Protocol`, and `Hard Stop Rule` delegate to that mapping.
- **Match:** ✅

### V2: `.tfw/workflows/plan.md`
- **RF claim:** the Coordinator rules once and applies the shared route without a universal TS revision.
- **Actual:** Step 8 reads the shared route, separates rung 1, rung 2/mixed, and rung 3, preserves
  Coordinator authority, and stops before execution. No forbidden universal-route phrase remains.
- **Match:** ✅

### V3: `.tfw/workflows/handoff.md`
- **RF claim:** the Executor accepts only a route-authorized rung-specific bound.
- **Actual:** the return entry gate requires `RF` plus a ruled live REVIEW for rung 1,
  `TS_DRAFT` plus the highest approved TS revision for rung 2/mixed, and an owner verdict before
  rung-3 dispatch; onboarding moves the authorized prior state to `ONB` only after acceptance.
- **Match:** ✅

### V4: `.tfw/workflows/review.md`
- **RF claim:** the Reviewer proposes and stops while the Coordinator owns the later ruling.
- **Actual:** Steps 5–6 forbid Reviewer rulings, make REVISE lifecycle-neutral, and route proposals
  to the Coordinator through the shared table; APPROVE and REJECT retain their separate routes.
- **Match:** ✅

### V5: six tracked workflow copies
- **RF claim:** canonical Plan, Handoff, and Review remain byte-equal to Claude and legacy
  Antigravity copies.
- **Actual:** SHA-256 comparisons are equal for each canonical file and both destinations; all nine
  consumers are free of the four enumerated universal-route contradictions.
- **Match:** ✅

### V6: `docs/scripts/test_runtime_context.py`
- **RF claim:** both Researcher graphs contain four stage templates, six P/R/E/V/C/A mutants change
  a produced record before independent rejection, and exact route/mutant cases are source-derived.
- **Actual:** `RESEARCH_STAGE_TEMPLATES` enumerates Briefing/Gather/Extract/Challenge and
  `_add_primary_supplements()` adds the same sequence in both modes. `semantic_mutant_result()`
  derives the mutated source record before consulting `EXPECTED_RECORDS`; the CLI independently
  produced six changed named fields. `resolve_revise_routes()` parses the conventions table, and
  four cell mutants alter lifecycle, recipient, artifact, or hard-stop output before rejection.
- **Match:** ✅

### V7: `docs/scripts/test_integration.py`
- **RF claim:** route consumers/copies share one authority, contradiction detection fires, and
  clean-receiver behavior remains intact.
- **Actual:** the added tests resolve the shared route, byte-compare both copies, reject an injected
  universal TS-revision clause, and run with the pre-existing four-vendor install/idempotence/repair
  receiver suite. Independent execution passed all targeted and full gates.
- **Match:** ✅

### V8: exact scope, budget, parity, and exclusions
- **RF claim:** revision 2 uses 12/12 files and 551 LOC; cumulative Phase B uses 24/24 distinct files
  and 1,556/3,500 LOC; named exclusions are unchanged.
- **Actual:** `999d987..8b16c0b` is exactly the twelve TS §3 paths and 442 additions + 109 deletions
  = 551. `80382fb..8b16c0b`, excluding phase traces, contains exactly 24 distinct
  implementation/test paths. The RF's 1,556 is conservative cumulative round churn
  (`1,005 + 551`); the coalesced baseline-to-current diff is 1,554. Both are below 3,500.
  `tasks/`, RDP, TFW-36, knowledge/config/template/manifest/skill paths, master/phase HL, and TS
  revision 1 are byte-unchanged from `272a7cf`; the live first REVIEW is unchanged by the Executor
  from the Coordinator return baseline `e091ef1`. Candidate ancestor `8b16c0b` and RF-named
  `8066284` have the identical tree.
- **Match:** ✅

### V9: evidence and cumulative trace handling
- **RF claim:** exactly five evidence files are reused append-only; ONB/RF/EV preserve the rejected
  record and add a revision-2 account.
- **Actual:** the evidence directory contains exactly EV plus four raw `.txt` files. The result commit
  adds 36/15/238/104/56 lines respectively with zero deletions. The old evidence and rejected totals
  remain visible, and the revision-2 append supersedes them explicitly. ONB and RF likewise retain
  their original sections and add named revision-2 sections.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python docs/scripts/test_runtime_context.py --audit --baseline-ref 80382fb` plus independent TSV aggregation | ✅ Baselines `50,851/29,992/30,057/55,885/74,537`; candidates `25,085/6,103/6,168/6,366/25,537`; combined `241,322→69,259` = 71.3%; four stage edges in each Researcher mode. |
| 2 | `python docs/scripts/test_runtime_context.py --semantic-mutants` | ✅ Six complete produced records change the named P/R/E/V/C/A field and report `independent_expected_rejects: true`. |
| 3 | `python docs/scripts/test_runtime_context.py --revise-routes` | ✅ Exact rung 1, rung 2, rung 3, and mixed records recovered from source. |
| 4 | `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q` | ✅ 156 passed in 254.15s. |
| 5 | `python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only` | ✅ 450 tests collected in 0.17s. |
| 6 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | ✅ 449 passed, 1 skipped in 233.80s. |
| 7 | `python .tfw/scripts/gen_index.py --check project` | ✅ Exit 0; framework 2.1.0 and one participant are consistent. |
| 8 | `python .tfw/scripts/gen_index.py --check tasks` | ✅ Expected exit 1; exactly one problem across 61 tasks, the immutable RDP summary at 123 code points against 120. Six legacy notes are informational. |
| 9 | `git diff --check 999d987..8b16c0b` | ✅ No whitespace errors. |
| 10 | Git numstat/name-status, exclusion diffs, file counts, and SHA-256 parity checks | ✅ 12 files/551 round LOC; 24 cumulative files; all named implementation exclusions unchanged; exactly five evidence files; all four primary workflow and skill source/copy pairs byte-equal. |
| 11 | Exploratory `python -m pytest --collect-only -q` without the configured directory scope | N/A — as expected, repository `site/scripts` duplicates collide with `docs/scripts`; this was not a TS gate. The prescribed scoped collection in command 5 passes. |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | Corrected Researcher totals and combined reduction | RF rev2 §4; EV R2-E1/R2-E4 | Independent source-tree audit over immutable `80382fb` and current candidate | ✅ — exact totals and 71.3% reproduce. |
| C2 | Every semantic family changes produced output before independent rejection | RF rev2 §3; EV R2-E2 | `SEMANTIC_MUTATIONS`, `execute_scenario()`, independent `EXPECTED_RECORDS`, CLI output, and passing adverse tests | ✅ — P/R/E/V/C/A each changes its declared field after full record construction. |
| C3 | Exact route, scope, parity, receivers, and exclusions | RF rev2 §§3–4; EV R2-E3/R2-E4 | conventions table, three canonical consumers, six byte-copies, Git trees/diffs, and integration tests | ✅ — all route cases and contradiction mutants pass; 12/24 file ceilings and exclusions hold. The 1,556 figure is cumulative churn; coalesced net diff is 1,554. |

All artifact links in the RF, EV, governing TS, original REVIEW, and stage lineage resolve locally.

## Discrepancies Found

No revision-2 acceptance discrepancy. Two audit notes do not fail an AC:

1. The RF's 1,556 cumulative LOC is the sum of per-round churn, while a direct immutable-baseline
   diff reports 1,554 after overlapping edits coalesce; either accounting is safely below the
   TS's 3,500 ceiling and both expose the exact 24-file surface.
2. `KNOWLEDGE.md` D72 still states the now-overbroad universal “round is a TS revision” rule. TS
   revision 2 explicitly reserves that documentation reconciliation for post-APPROVE `/tfw-docs`;
   implementation authority is unambiguous in current conventions and workflows. Verification was
   nevertheless completed at 100% depth.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| R2-E1 | `evidence/EV__phase-b__primary_role_paths.md` + `runtime-context-primary-roles.txt` | ✅ | ✅ — four ordered stage edges in both modes, exact 6,103/6,168 totals, and omission failure independently reproduce. |
| R2-E2 | `semantic-primary-roles.txt` | ✅ | ✅ — append records all six changed named outputs, ordinary semantics, and expected-data isolation; independent CLI/tests match. |
| R2-E3 | `semantic-primary-roles.txt` + `clean-receiver-primary-routes.txt` | ✅ | ✅ — exact four route records, four output-changing contradictions, one shared authority, copy parity, and receiver regression are present and independently pass. |
| R2-E4 | `verification-primary-roles.txt` | ✅ | ✅ — 156/450/449+1, project/task checks, reductions, scope, exclusions, and parity match independent execution, subject to the documented 1,556 churn/1,554 coalesced-diff distinction. |

The evidence directory contains exactly five files; none was replaced or supplemented by a sixth.

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | Master HL §7.2 K1 | P0 · NS1 purpose/inspectability/authority/continuation | ✅ | ✅ | ✅ — reduction is subordinate to purposeful, human-governed continuity. | ✅ — gates and next-recipient semantics are the core risk. |
| 2 | Master HL §7.2 K2 | P0 · NS3 no maximum-documentation bureaucracy | ✅ | ✅ | ✅ — artifact count and prose volume are not success. | ✅ — supports subtraction of duplicate preload. |
| 3 | Master HL §7.2 K3 | P1 · Structural Enforcement; Naming Creates Behavior; Portability | ✅ | ✅ | ✅ — source-derived gates, precise rung names, and local copies instantiate the cited values. | ✅ |
| 4 | Master HL §7.2 K4 | P2 · philosophy F22/F40/F43/F45 | ✅ | ✅ | ✅ — template minimalism, terminology, architecture, and subtraction match the stated use. | ✅ |
| 5 | Master HL §7.2 K5 | P3 · D23/D25/D61 | ✅ | ✅ | ✅ — earlier template ownership, progressive disclosure, and deletion of a non-performing axis are accurately summarized. | ✅ |
| 6 | Master HL §7.2 K6 | P3 · D63/D68/D72 | ✅ | ✅ | ✅ — contract freeze, task-local authority, and citation-bar semantics are preserved; D72's route wording is the explicit post-approval docs delta. | ✅ |
| 7 | Master HL §7.2 K7 | P4 · Design Rules / Anti-patterns | ✅ | ✅ | ✅ — ref-inside-step, structural roles, and one authority constrain the repair. | ✅ — no new authority layer was created. |
| 8 | Master HL §7.2 K8 | P5 · convention F4/F8/F14 | ✅ | ✅ | ✅ — algorithmic references and single ownership match; templates were not expanded. | ✅ |
| 9 | Master HL §7.2 K9 | P6 · process F3/F4/F22/F30 | ✅ | ✅ | ✅ — named algorithmic gates and output-changing proof replace prose-only claims. | ✅ |
| 10 | Master HL §7.2 K10 | P7 relevance scan | N/A | ✅ | ✅ — remaining topic files were scanned. | ✅ — no additional domain/environment/risk constraint alters this bounded repair. |
| 11–20 | ONB §7 rows 1–10 | Inherited K1–K10 applications | ✅ | ✅ | ✅ — each accurately applies the corresponding master-HL item or records explicit N/A. | ✅ |
| 21–25 | ONB Revision 2 §7 R2-1–R2-5 | P0–P7 grouped applications | ✅ | ✅ | ✅ — each grouping names real inherited items and the concrete repair choice; R2-5 is explicit N/A after the relevance scan. | ✅ |

Independent P0–P4 reads covered the root README opening/`How It Works`, `.tfw/README.md` purpose,
principles, values, non-goals and success criteria, all of `knowledge/philosophy.md`, `KNOWLEDGE.md`
§1, and the three addressed conventions ranges. P5/P6 sources were read in full; all remaining P7
topic files were relevance-scanned.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈12 × 0.42⌉ files and recorded findings? — 12/12.
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Claim & Source Checks filled — 3 key claims checked, every citation traced, and numeric data independently recomputed?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — the anticipated D72 documentation delta is documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: 25, resolved: 25, semantically verified: 25, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 4, verified: 4, missing: 0; physical evidence files: exactly 5

Stage complete: YES
