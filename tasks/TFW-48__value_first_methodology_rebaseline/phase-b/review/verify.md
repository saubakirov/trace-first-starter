# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: spec
> Min verify ratio: 0.42
> RF framework files claimed: 12
> Initial files to verify: ⌈12 × 0.42⌉ = 6
> Actual files verified: 12/12 — discrepancies triggered mandatory 100% escalation

## Verification Log

### V1: `.tfw/conventions.md`
- **RF claim:** Defines the Phase B consumer map, purpose-led planning, Comparative
  Decision Procedure, H4 non-claim, qualitative research closure, Learning Receipts,
  and the twelve-object numeric disposition ledger.
- **Actual:** The new owned sections and all twelve ledger rows exist, and the ledger
  correctly classifies `max_iterations`. However, the existing `iterations.yaml`
  example still describes `min_iterations: 2` as coming from configuration/override
  and `max_iterations: 5` as a **soft ceiling**. The latter directly conflicts with
  the new ledger's statement that `max_iterations` loses ceiling/closure authority.
- **Match:** ⚠️ partial

### V2: `.tfw/glossary.md`
- **RF claim:** Provides one concise definition for Comparative Decision Procedure and
  one for Research Intensity, with references to the operational owner.
- **Actual:** Both new definitions and owner links exist. The same glossary still says:
  a Research Pass requires at least one pass and recommends at most three; research has
  a configurable minimum of two iterations; `min_iterations` is a hard floor that
  blocks TS; every Dimension has at least three Alternatives; and a Dimension with at
  least three Alternatives is required for Configuration Space. It also describes the
  three stages as a flexible-order checklist. These are active public definitions that
  compete with the new procedure, fit, numeric-authority, and closure contracts.
- **Match:** ❌

### V3: `.tfw/workflows/plan.md`
- **RF claim:** Starts planning from product purpose and uncertainty, traces human
  insight dispositions, gates comparative-procedure fit, and uses qualitative
  iteration triggers.
- **Actual:** Purpose, Project Values, decision-changing uncertainty, insight
  implication/disposition, Pre-TS coverage, FIT/MISMATCH, and named iteration triggers
  are present. MISMATCH returns the unresolved information need to Coordinator/user
  and does not select a substitute method.
- **Match:** ✅

### V4: `.tfw/workflows/research/base.md`
- **RF claim:** Operates the same bounded procedure for focused/deep intensity, keeps
  the complete filesystem-traced iteration floor, and closes by evidence/decision
  claims rather than activity counts.
- **Actual:** The workflow requires Briefing → Gather → Extract → Challenge → RES when
  the procedure fits, routes mismatch to Coordinator/user, distinguishes qualitative
  intensity, records coverage/exclusions/counter-evidence/decision effect/unresolved
  gaps, and permits an unresolved outcome.
- **Match:** ✅

### V5: `.tfw/workflows/research/focused.md`
- **RF claim:** Defines focused intensity qualitatively without count-based completion.
- **Actual:** Focused intensity narrows the decision, evidence families, countercheck,
  and residual uncertainty while retaining the same stages and closure authority. No
  fixed loops, decisions, turns, hypotheses, sources, or files are completion gates.
- **Match:** ✅

### V6: `.tfw/workflows/research/deep.md`
- **RF claim:** Defines deep intensity through evidence diversity, counter-evidence,
  edge/failure cases, and explicit unresolved uncertainty.
- **Actual:** All listed qualitative obligations are present, the same procedure and
  authority are retained, and no fixed activity count proves completion.
- **Match:** ✅

### V7: `.tfw/templates/HL.md`
- **RF claim:** Extends Strategic Insights with planning implication and TS
  disposition/destination without adding a new capture surface.
- **Actual:** The existing Strategic Insights section carries the insight, implication,
  source, and TS disposition/destination. Guidance lists AC, scope, guidance, DoF,
  decision/research direction, explicit non-use, and downstream destinations.
- **Match:** ✅

### V8: `.tfw/templates/RES.md`
- **RF claim:** Synthesizes selected stage receipts and human insights, preserves
  `## Fact Candidates`, and records source, destination/backlink, and responsible actor
  while keeping Phase D promotion ownership transitional.
- **Actual:** The canonical heading remains; Fact Candidate eligibility is limited to
  qualifying promote/merge/derive signals; required relations and actor are explicit;
  reject/local/defer remain in resolvable existing traces; strategic insights and HL
  update recommendations remain distinct.
- **Match:** ✅

### V9: `.tfw/templates/research/1_briefing.md`
- **RF claim:** Captures decision, alternatives/configuration question, approach-changing
  result, FIT/MISMATCH, and a compact Learning Receipt without arbitrary plan/question
  counts.
- **Actual:** All fields are present. MISMATCH records the unresolved need and stops for
  Coordinator/user authority. `## Learning Receipt` and explicit
  `No selected signal` are present.
- **Match:** ✅

### V10: `.tfw/templates/research/2_gather.md`
- **RF claim:** Uses material alternatives and coverage rather than fixed
  dimension/alternative counts and adds a Learning Receipt.
- **Actual:** Coverage, exclusions, alternatives, evidence effect, and insufficiency are
  qualitative. The Learning Receipt includes typed dispositions and explicit
  `No selected signal`.
- **Match:** ✅

### V11: `.tfw/templates/research/3_extract.md`
- **RF claim:** Preserves cross-stage configuration structure without a configuration
  quota and adds a Learning Receipt.
- **Actual:** Extract depends on Gather, records decision-relevant configurations and
  gaps without a sampling count, and includes the same explicit receipt/no-signal
  contract.
- **Match:** ✅

### V12: `.tfw/templates/research/4_challenge.md`
- **RF claim:** Preserves counter-evidence/pairwise challenge without count completion
  and adds a Learning Receipt that can reopen a decision.
- **Actual:** Challenge consumes prior stage traces, records counter-evidence, failure
  cases, decision effect, unresolved gaps, and reopen/change outcomes. The receipt and
  explicit no-signal path are present without a count gate.
- **Match:** ✅

## Acceptance-Criteria Verification

| AC | Result | Independent finding |
|----|--------|---------------------|
| AC-1 | ❌ | New owners/gates exist and runtime research codes are absent, but the glossary still publishes competing Pass, Iteration, `min_iterations`, Stage, Dimension, and Alternative rules. |
| AC-2 | ✅ | Purpose-led planning, four disposition examples, Pre-TS coverage, Project Values cascade, and TFW-44 supersession through existing surfaces are present. |
| AC-3 | ❌ | The new FIT/MISMATCH contract is correct, but legacy glossary text still presents RESEARCH as the generic research definition, treats stages as flexible order, and adapts Extract/Challenge around a three-dimension threshold. The procedure is therefore not consistently bounded across affected consumers. |
| AC-4 | ✅ | Focused/deep are qualitative intensity controls, preserve one procedure, retain transitional names/keys, and do not use counts as completion proof. |
| AC-5 | ❌ | The new twelve-row ledger and full iteration floor exist, but the glossary still gives counts hard-floor/recommended-maximum/required-configuration authority and conventions still labels `max_iterations` a soft ceiling. |
| AC-6 | ✅ | All four stage templates contain proportionate typed Learning Receipts and explicit `No selected signal`; counter-evidence can reopen a decision. |
| AC-7 | ✅ | RES preserves the canonical Fact Candidates surface, required relations/actor, distinct insight/decision routing, no new framework file, and the Phase D transitional ownership boundary. |
| AC-8 | ✅ | H4 remains unresolved, T0-only, and non-architectural. No selector, catalog, registry, runtime strategy choice, strategy extension, or prohibited comparison was introduced. |
| AC-9 | ❌ | Links, anchors, tests, scope, config, and rendered layout pass, but obsolete activity-count completion statements remain in affected files and RF descriptive word counts are inaccurate. Cross-consumer semantic consistency is not achieved. |

**Result:** 5/9 AC pass; AC-1, AC-3, AC-5, and AC-9 fail.

## Commands Executed

| # | Command/check | Result |
|---|---------------|--------|
| 1 | `git diff --name-status 8758529 4466109` and `git diff --stat 8758529 4466109` | Exactly twelve approved `.tfw` framework consumers plus lifecycle `README.md`; no added framework file; 13 files, 497 insertions, 160 deletions. |
| 2 | `git diff 4466109 d2f1466` | Only final `README.md`, RF, and EV trace changes. |
| 3 | `git diff --check 8758529 4466109` | PASS. |
| 4 | Diffs for `.tfw/project_config.yaml` and `.tfw/templates/project_config.yaml` | Empty; no config/template/exact-value change. |
| 5 | Targeted `rg` scans over all twelve consumers | Found the legacy count/closure conflicts recorded in Discrepancies D1–D2; found no runtime `K3`, `M5`, `R9`, `V1`, selector/catalog/runtime-strategy architecture, or H4 benefit claim. |
| 6 | Structural counts | 12/12 ledger rows including `max_iterations`; 4/4 stage templates contain `## Learning Receipt`; 4/4 contain explicit `No selected signal`; `## Fact Candidates` preserved. |
| 7 | Independent whitespace word count at `4466109` | Actual total 17,115, not RF 17,120. Four consumer after-counts and total differ; all baseline counts and line counts reproduce. |
| 8 | `python -m pytest docs/scripts/test_gen_docs.py docs/scripts/test_integration.py` | PASS — 68 tests in 32.59s. |
| 9 | Fresh `python -m mkdocs build --config-file docs/mkdocs.yml --site-dir <temporary-dir>` | Completed in 28.10s; known non-strict warning baseline remains covered by TD-125. |
| 10 | In-app browser audit of conventions, glossary, plan, base/focused/deep, HL/RES, and four stage-template pages | Pages loaded, expected headings/anchors were reachable, owner-link navigation worked, and no page-level horizontal overflow was observed. Rendered glossary also exposes the stale semantic definitions from D1. |
| 11 | HL §7.2 and ONB §7 citation resolution | 13/13 HL rows and 14/14 ONB rows resolve to existing files/items; 27/27 total, 0 hallucinations. |

### RF Descriptive Measurement Reproduction

| Consumer | RF words after | Actual words after | Difference |
|----------|---------------:|-------------------:|-----------:|
| `.tfw/glossary.md` | 3,479 | 3,478 | -1 |
| `.tfw/workflows/plan.md` | 1,488 | 1,487 | -1 |
| `.tfw/templates/HL.md` | 1,166 | 1,164 | -2 |
| `.tfw/templates/RES.md` | 764 | 763 | -1 |
| **Total (12 consumers)** | **17,120** | **17,115** | **-5** |

The other eight after-word counts, every before-word count, every line count, the
twelve-consumer count, and the zero-new-framework-file count reproduce.

## Discrepancies Found

1. **D1 — material competing glossary contracts.** `.tfw/glossary.md` retains a
   minimum pass, recommended maximum passes, a default minimum iteration count, a hard
   `min_iterations` TS gate, mandatory three-alternative dimensions, and a
   three-dimension branch. It also describes research stages as flexible order. These
   are active consumer instructions, not historical ledger entries, and contradict the
   new bounded procedure and count-retirement authority.
2. **D2 — material stale ceiling contract.** `.tfw/conventions.md` still labels
   `max_iterations: 5` as a soft ceiling in its `iterations.yaml` example, while the
   Phase B ledger says the same object loses ceiling and closure authority.
3. **D3 — RF measurement inaccuracy.** Four after-word counts are high by a combined
   five words. This is descriptive rather than independently acceptance-critical, but
   AC-9 explicitly requires honest reporting.
4. **D4 — EV E9 overclaims rendered consistency.** The rendered pages are structurally
   readable and navigable, but the rendered glossary visibly contains D1. Therefore
   E9's semantic cross-consumer PASS cannot support AC-9 as written.

The first discrepancy triggered 100% verification of all twelve framework consumers.

## Evidence Verification

The eight N/A dispositions match the corresponding TS Evidence fields; N/A means that
no live external-outcome artifact is required, not that source verification may be
skipped. Each was therefore challenged against the affected consumers under the Trust
Protocol.

| # | RF/EV evidence ref | Artifact/status exists? | Matches claim? |
|---|--------------------|-------------------------|----------------|
| E1 | AC-1 static ownership/consumer mapping — N/A | ✅ | ❌ — static verification finds competing glossary contracts. |
| E2 | AC-2 planning contract/examples — N/A | ✅ | ✅ — planning fields, dispositions, examples, and gate are present. |
| E3 | AC-3 procedure applicability — N/A | ✅ | ❌ — new fit behavior is correct, but stale public RESEARCH/Stage/Dimension definitions make the boundary inconsistent. |
| E4 | AC-4 intensity behavior — N/A | ✅ | ✅ — focused/deep source behavior is qualitative and preserves the procedure. |
| E5 | AC-5 numeric/external outcome — N/A | ✅ | ❌ — no exact value changed, but static source review finds old hard-floor/ceiling/completion authority. |
| E6 | AC-6 receipt structure — N/A | ✅ | ✅ — all four templates and no-signal paths verified. |
| E7 | AC-7 downstream consolidation — N/A | ✅ | ✅ — Phase D remains the downstream owner and no capture surface/file was added. |
| E8 | AC-8 prohibited H4 execution — N/A | ✅ | ✅ — targeted and semantic scans confirm the non-claim. |
| E9 | AC-9 rendered documentation — VERIFIED | ✅ | ❌ — layout/navigation claims reproduce, but rendered semantic consistency does not because D1 remains visible. |

All 9/9 EV rows exist and use TS-valid disposition labels; 5/9 substantively support
their AC claims, 4/9 conflict with verified source/rendered content, and 0 are missing.

## Knowledge Citations Verified

| # | Artifact rows | Citation | Link resolves? | Item exists? |
|---|---------------|----------|----------------|--------------|
| 1 | HL #1 / ONB #1 | Phase A RF, decisions 1–7 | ✅ | ✅ |
| 2 | HL #2 / ONB #2 | Phase A REVIEW, APPROVE | ✅ | ✅ |
| 3 | HL #3 / ONB #3 | Iteration 2 RES, D15 and D18–D20 | ✅ | ✅ |
| 4 | HL #4 / ONB #4 | KNOWLEDGE D22 | ✅ | ✅ |
| 5 | HL #5 / ONB #5 | KNOWLEDGE D23 | ✅ | ✅ |
| 6 | HL #6 / ONB #6 | KNOWLEDGE D37 | ✅ | ✅ |
| 7 | HL #7 / ONB #7 | KNOWLEDGE D43 | ✅ | ✅ |
| 8 | HL #8 / ONB #8 | KNOWLEDGE D49 | ✅ | ✅ |
| 9 | HL #9 / ONB #9 | KNOWLEDGE D51 | ✅ | ✅ |
| 10 | HL #10 / ONB #10 | KNOWLEDGE D55 | ✅ | ✅ |
| 11 | HL #11 / ONB #11 | `knowledge/philosophy.md` F3, F4, F13, F18, F24–F26 | ✅ | ✅ |
| 12 | HL #12 / ONB #12 | `knowledge/process.md` F3–F7, F13–F16, F22–F25 | ✅ | ✅ |
| 13 | HL #13 / ONB #13 | TFW-44 HL §11 → TS gap | ✅ | ✅ |
| 14 | ONB #14 | `knowledge/philosophy.md` F21 | ✅ | ✅ |

Total citation rows: 27; verified: 27; hallucinations: 0.

## RF Observation, Fact-Candidate, and Conversation-History Challenge

RF §§6–8 were not accepted merely because they contain explicit "No..." text.
Coordinator/user history was reviewed for human-only facts, corrections, goals, and
execution-stage insights:

- the user's product/value-first, proxy-count, learning-routing, domain-neutrality,
  and H4 concerns are already recorded in the approved master/Phase B HL Strategic
  Insights and are not new execution discoveries;
- execution messages approved or restated scope, mismatch, closure, receipt, and H4
  boundaries without adding new human-only project facts;
- D1–D4 are reviewer-discoverable implementation/RF defects and therefore belong in
  verification and revision, not Fact Candidates;
- D1–D2 are in-scope defects, not out-of-scope technical-debt observations.

Accordingly, no new Fact Candidate or strategic insight is invented, and no new
TECH_DEBT entry is justified. The RF's empty Fact Candidate/Strategic Insight
dispositions withstand the human-only test; its lack of a defect report does not
withstand independent verification and is addressed by this review.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈12 × 0.42⌉ files and recorded findings?
- [x] Escalated to 12/12 files after discrepancies?
- [x] Ran at least 1 build/test command?
- [x] Each RF §3 AC checkmark verified against actual files?
- [x] KNOWLEDGE.md checked and relevant contradictions documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total citations: 27, verified: 27, hallucinations: 0
- [x] Evidence artifacts/statuses from RF §5 and EV verified?
  - Total evidence items: 9, substantively matched: 5, contradictory: 4, missing: 0

Stage complete: YES
