# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: spec
> Min verify ratio: 0.42
> RF files claimed in target diff: 11
> Files to verify: ceil(11 × 0.42) = 5; explicit Coordinator scope and a link-audit
> precision note triggered 100% verification (11/11 target paths, including 8/8
> framework consumers).

## Verification Log

### V1: `.tfw/conventions.md`
- **RF claim:** Owns the Requirement Claim → observation → Proof Record → RF Executor
  Attestation → independent REVIEW chain, Evidence-status consequences, Value Debt,
  deviation handling, and scope-attention response.
- **Actual:** The source contains the complete chain, the seven-field Proof Record
  schema, Local/Seam/Live triggers, complete Value Debt, row-scoped four-status
  consequences, material-deviation rules, and all five scope-response choices. Phase
  B purpose/learning contracts remain present; H4 remains an explicit non-claim.
- **Match:** ✅

### V2: `.tfw/glossary.md`
- **RF claim:** Concisely defines/narrows Requirement Claim, Proof Record, Local/Seam/
  Live Proof, Value Debt, Executor Attestation, Material Deviation, Verification,
  Evidence, status vocabulary, and Scope Budget while linking to owners.
- **Actual:** Definitions are concise, mutually non-collapsing, domain-neutral, and
  linked to conventions/templates. `N/A` cannot waive Local/triggered Seam Proof and
  Scope Budget explicitly cannot command automatic split/fail.
- **Match:** ✅

### V3: `.tfw/workflows/plan.md`
- **RF claim:** Adds purpose/insight disposition, a point-of-use Requirement Claim
  gate, conditional Gate/Evidence intent, and value/cohesion-led scope responses.
- **Actual:** Steps 1–8 retain the Phase B purpose/PV/Strategic Insight flow. Pre-TS
  Steps 1–5 require intent, boundary, precision, Local plus triggered Seam/Live Proof,
  justified `N/A`, and simplify/remove/coherent-split/override/return scope choices.
- **Match:** ✅

### V4: `.tfw/templates/TS.md`
- **RF claim:** Carries the compact Requirement Claim within the existing AC surface.
- **Actual:** §5 relates intent/authority, observable claim, boundary, precision, proof
  intent, Gate, and Evidence. Compact/grouped fields and justified `N/A` remain valid;
  code tests/builds are conditional examples, not universal gates.
- **Match:** ✅

### V5: `.tfw/templates/ONB.md`
- **RF claim:** Adds a pre-action specification-to-reality check without a parallel
  specification artifact.
- **Actual:** The existing Understanding, Entry Points, Questions, Risks, and
  Inconsistencies surfaces now compare identifiers, cited sources, required checks,
  live outcome/proof feasibility, and product cohesion. Acceptance-critical mismatch
  is a blocking question and STOP; adaptable substitution requires RF disclosure.
- **Match:** ✅

### V6: `.tfw/workflows/handoff.md`
- **RF claim:** Simplifies execution around claim-applicable gates while preserving the
  complete Executor role/approval/deviation/output/Pre-RF/STOP contract.
- **Actual:** The local role lock and forbidden writes precede action; ordered context
  load remains complete; ONB must be committed/pushed and explicitly approved;
  execution preserves complete output and applicable checks; deviations and proof are
  typed; current RF/EV templates are opened before attestation; Executor STOP remains
  local and explicit.
- **Match:** ✅

### V7: `.tfw/templates/RF.md`
- **RF claim:** Makes RF an accountable Executor Attestation tied to `PR-*`,
  limitations/debt/deviations, reproducible verification, and a concise EV pointer.
- **Actual:** Header and §§2–5 implement that boundary. A checked result cannot coexist
  with unresolved blocking proof; local support may coexist only with an explicit
  Seam/Live non-claim/debt; §§6–9 remain mandatory and Phase B-compatible.
- **Match:** ✅

### V8: `.tfw/templates/evidence/EV.md`
- **RF claim:** Uses the existing EV artifact to index stable Proof Records, retain
  Evidence rows/statuses, and record complete Value Debt.
- **Actual:** The PR schema resolves claim, boundary/class, method, result,
  artifact/provenance, material actor/time, and debt. All four status conditions and
  failure consequences are explicit; complete debt names claim, proof, owner, event,
  route, impact/non-claim, and closure condition. No new proof artifact is introduced.
- **Match:** ✅

### V9: lifecycle traces and exact target diff
- **RF claim:** Target `6816acd` changes the eight approved framework consumers, adds
  Phase C EV/RF, and changes only the TFW-48 README row; protected sources and exact
  values stay unchanged.
- **Actual:** `git diff --name-only 00cf52a..6816acd` contains exactly those 11 paths.
  Framework scope is 8/8 with zero extras; protected diff is empty; README has one row
  delta; config and template retain `14/8/1200/12`.
- **Match:** ✅

## Acceptance Criteria Verification

| AC | Independent result | Evidence |
|----|--------------------|----------|
| AC-1 | ✅ | 8/8 consumer source audit; single conventions owner; concise glossary; no ninth consumer/new proof artifact; RF ownership matrix matches actual roles |
| AC-2 | ✅ | Plan/TS carry intent, claim, boundary, precision, proof and Evidence intent; document/source/software/stakeholder/operation cases derive the correct boundary |
| AC-3 | ✅ | TS/ONB/handoff distinguish binding precision from guidance; six RF reality cases correctly return STOP, deviation, `N/A`, debt, or block |
| AC-4 | ✅ | Conventions/glossary/plan/TS consistently make the four exact values transitional attention signals; six scope cases preserve cohesion; config values unchanged |
| AC-5 | ✅ | Handoff source plus rendered ONB/handoff pages preserve role lock, context, approval, applicable checks, complete output, deviations, Pre-RF, and STOP across six domains |
| AC-6 | ✅ | EV schema and PR-1…PR-10 are stable/resolvable; six proof cases preserve Local plus triggered Seam/Live/debt and reject presence/checkmark implication |
| AC-7 | ✅ | Four statuses remain observation-row scoped; six status cases correctly accept four valid dispositions and reject missing provenance/unjustified `N/A` |
| AC-8 | ✅ | RF template and filled RF relate every AC to `PR-*`, limitations and actual checks while preserving independent REVIEW authority and concise EV pointer |
| AC-9 | ✅ | Six production counter-cases trace to Iteration 1 Gather; six cross-domain cases use the same universal claim grammar without uniform volume or code-default gates |
| AC-10 | ✅ | Exact scope/protected/config/diff checks pass; 68 tests pass; non-strict build passes; strict delta is zero; 8×2 render checks and 11 anchors pass |

## RF and EV Claim Audit

- **PR-1…PR-10:** 10/10 records resolve to the claimed AC, an actual source/method,
  actual result, provenance/reference, actor/date, and explicit `None` debt. The record
  index does not use Evidence status as claim closure.
- **Production/cross-domain matrices:** 6/6 + 6/6 rows contain a claim boundary,
  triggered proof, honest attestation/non-claim, and authority outcome. The historical
  cases match the cited Gather records.
- **Precision/proof/status/scope matrices:** 6/6 + 6/6 + 6/6 + 6/6 branches are
  semantically correct. An equivalent 21-assertion scan across all eight consumers
  passes 21/21.
- **Measurements:** Reproduced exactly from `00cf52a` and the final tree: lines
  1,864→2,182; `\S+` tokens 15,207→18,472; branch cues 142→153; framework diff
  510 insertions + 192 deletions = 702. All eight per-file rows match RF.
- **Strict attribution:** Detached `00cf52a` worktree and final tree received identical
  29-file ignored TFW-36 inputs and the same environment/command. Both exit 1 with 264
  normalized warning records / 121 unique; duplicate-preserving delta is added 0,
  removed 0. TD-125 is unchanged and not attributable to Phase C.
- **Links/anchors:** All 11 named rendered owner/template anchors resolve. Every
  Phase C-added owner link resolves. The RF's aggregate `76/76 concrete source links`
  label is reproducible only when pre-existing template link placeholders are treated
  as valid template contracts rather than literal current-tree files; seven
  `path-to-*`/instantiated-EV placeholders are intentionally unresolved before
  template instantiation. This is a precision note, not an AC-10 failure: none was
  introduced by Phase C and all changed operational owner links resolve.
- **Rendered QA:** Conventions, glossary, plan, TS, ONB, handoff, RF, and EV pages were
  opened at 1265×720 and 753×720. Table counts reproduce 31/2/0/5/3/0/10/5; 0/16
  pages have body overflow; every wide table is inside a MkDocs scroll wrapper; 0
  broken same-page fragments were observed.

## Commands Executed

| # | Command / method | Result |
|---|------------------|--------|
| 1 | `python -m pytest docs/scripts/test_gen_docs.py docs/scripts/test_integration.py -q` | ✅ 68 passed in 58.69s |
| 2 | `python -m mkdocs build --config-file docs/mkdocs.yml` | ✅ exit 0; built in 42.05s |
| 3 | Identical `python -m mkdocs build --strict --config-file docs/mkdocs.yml` in detached baseline/final trees | ✅ both exit 1; 264/121 each; added 0, removed 0 |
| 4 | `git diff --check 00cf52a..6816acd` | ✅ PASS |
| 5 | Exact/protected/config/README diff audits | ✅ 8 framework + EV/RF + one Board row; protected count 0; values unchanged |
| 6 | PowerShell line/`\S+`/branch-cue reproduction | ✅ all totals and 8/8 rows match RF |
| 7 | 21-assertion semantic and targeted negative scans | ✅ 21/21; no active auto-split, proof-from-presence, Evidence=Proof, or code-universal contract |
| 8 | In-app browser DOM/layout and anchor audit | ✅ 8 desktop + 8 responsive pages; 11/11 anchors; no body overflow |

## Discrepancies Found

No acceptance-critical discrepancy.

One non-blocking evidence-label precision note is recorded above: `76/76 concrete
source links` conflates literal source links with pre-existing template-instantiation
placeholders. The changed link/anchor gate itself passes at 100%, so no TS Definition
of Failure condition is triggered and no implementation correction is required.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|-----------------|------------------|----------------|
| E1 / AC-1 | EV inline PR-1 and source graph | ✅ | ✅ `N/A` is claim-based; Local/Seam source proof exists |
| E2 / AC-2 | EV rendered observation; PR-2 | ✅ | ✅ `VERIFIED`; plan/TS pages and hierarchy reproduced |
| E3 / AC-3 | EV inline scenario result; PR-3 | ✅ | ✅ `N/A` is justified; no external/live execution is claimed |
| E4 / AC-4 | EV source/config result; PR-4 | ✅ | ✅ `N/A` is justified; exact values/source relation reproduced |
| E5 / AC-5 | EV rendered observation; PR-5 | ✅ | ✅ `VERIFIED`; role/approval/STOP and non-code flow reproduced |
| E6 / AC-6 | Filled EV + generated EV page; PR-6 | ✅ | ✅ `VERIFIED`; stable/grouped PR schema remains legible |
| E7 / AC-7 | Conventions/glossary/EV renders; PR-7 | ✅ | ✅ `VERIFIED`; four row-scoped consequences and overflow result reproduced |
| E8 / AC-8 | RF template render; PR-8 | ✅ | ✅ `VERIFIED`; attestation, limitation, verification and EV pointer visible |
| E9 / AC-9 | Historical corpus + 12 scenarios; PR-9 | ✅ | ✅ `N/A` is justified; no fresh production run is claimed |
| E10 / AC-10 | Eight-page rendered observation; PR-10 | ✅ | ✅ `VERIFIED`; 8/8 at both viewports and 11/11 anchors reproduced |

Evidence verdict independently confirmed: **6/10 VERIFIED, 0 DEFERRED, 0 BLOCKED,
4 N/A**. No Value Debt is triggered by the delivered Phase C documentation claims.

## Knowledge Citations Verified

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 / ONB §7 | Phase A RF, Key Decisions 2–7 | ✅ | ✅ |
| 2 | HL §7.2 / ONB §7 | Phase A REVIEW, APPROVE 9/9 | ✅ | ✅ |
| 3 | HL §7.2 / ONB §7 | Phase B RF, purpose/closure/numeric ledger | ✅ | ✅ |
| 4 | HL §7.2 / ONB §7 | Phase B REVIEW, APPROVE 9/9 and 12/12 | ✅ | ✅ |
| 5 | HL §7.2 / ONB §7 | Iteration 2 RES D14, D17–D19 | ✅ | ✅ |
| 6 | HL §7.2 / ONB §7 | Iteration 1 Gather HD-23/25/26/30; AFD-10/14/36 | ✅ | ✅ |
| 7 | HL §7.2 / ONB §7 | KNOWLEDGE D24 | ✅ | ✅ |
| 8 | HL §7.2 / ONB §7 | KNOWLEDGE D49 | ✅ | ✅ |
| 9 | HL §7.2 / ONB §7 | KNOWLEDGE D52–D53 | ✅ | ✅ |
| 10 | HL §7.2 / ONB §7 | KNOWLEDGE D55–D56 | ✅ | ✅ |
| 11 | HL §7.2 / ONB §7 | philosophy F20/F21/F24/F26 | ✅ | ✅ |
| 12 | HL §7.2 / ONB §7 | philosophy F28/F30/F31 | ✅ | ✅ |
| 13 | HL §7.2 / ONB §7 | constraint F7 | ✅ | ✅ |
| 14 | HL §7.2 / ONB §7 | stakeholder F3 | ✅ | ✅ |
| 15 | HL §7.2 / ONB §7 | process F4/F6/F16/F18/F23/F25 | ✅ | ✅ |
| 16 | HL §7.2 / ONB §7 | convention F4 | ✅ | ✅ |

ONB additions D31 and philosophy F22 also resolve and apply. No citation
hallucination or contradiction with KNOWLEDGE.md was found.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ceil(11 × 0.42) files and recorded findings? (11/11 target paths; 8/8 consumers)
- [x] Ran at least 1 build/test command?
- [x] Each RF §3 AC checkmark verified against actual files?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total coordinator citations: 16, verified: 16, hallucinations: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 10, verified/disposition-confirmed: 10, missing: 0

Stage complete: YES
