# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: spec
> Min verify ratio: 0.42
> RF files claimed: 7
> Files to verify: ⌈7 × 0.42⌉ = 3; escalated to 7/7 after a descriptive-count discrepancy

## Verification Log

### V1: `README.md`
- **RF claim:** The public promise and “How It Works” were reconciled with the value-first Method Kernel, and the TFW-48 Task Board row was advanced to RF.
- **Actual:** The opening names purpose, values, evidence, reality, independent review, and durable learning; “How It Works” contains seven protected-outcome rows and links to the Method Kernel plus owned values/success criteria; the TFW-48 row is `🟢 RF (A)` with the RF link.
- **Match:** ✅

### V2: `.tfw/README.md`
- **RF claim:** The philosophy now makes the five obligations, proportionality, evidence precedence, independent judgment, learning, and six success criteria explicit.
- **Actual:** “How TFW Works” contains exactly five obligation rows, explains obligation/claim-level proportionality and the comparative scope of staged research, and links conventions/glossary owners. Values preserve candor, completeness, honesty, structural enforcement, naming, semantic ownership, and portability. “Success Criteria” contains six outcome criteria.
- **Match:** ✅

### V3: `.tfw/conventions.md`
- **RF claim:** The file owns the operational Method Kernel, object composition, Rule Deployment, claim-typed proof, learning/extension lifecycles, Numeric Control taxonomy, and eight-object transitional ledger.
- **Actual:** §1.1 contains exactly five kernel obligations; the composition includes Rule Records, per-claim Proof Records, event-triggered Learning Transactions, zero-or-more Registered Extensions, and applicable Numeric Controls. The four Rule Deployment cases, four proof obligations, three receipt dispositions, six extension fields, seven numeric types, and eight ledger objects all exist. The transition statement explicitly defers consumer changes. `project_config.yaml` is unchanged.
- **Match:** ✅

### V4: `.tfw/glossary.md`
- **RF claim:** All 15 Phase A terms are defined once, domain-neutrally, with links to operational owners; Evidence vocabulary is aligned with EV/RF.
- **Actual:** Each required `###` heading occurs exactly once (15/15). The generated glossary exposes all terms and 17 operational links targeting eight conventions anchors; all eight target anchors exist. Evidence, Evidence Collection, Evidence Audit, and status vocabulary point to EV-file use without collapsing Evidence into Proof Record.
- **Match:** ✅

### V5: `ONB__phase-a__method_kernel.md`
- **RF claim:** The ONB records onboarding, citation audit, risks, and the approval gate.
- **Actual:** All mandatory ONB sections are present; no blocking questions remained; §7 records 12 citation groups and their use. The note that TS was still draft records onboarding-time state; the current TS header subsequently records approval.
- **Match:** ✅

### V6: `evidence/EV__phase-a__method_kernel.md`
- **RF claim:** The structured evidence file covers all nine ACs with 2 VERIFIED, 7 N/A, and no DEFERRED/BLOCKED items.
- **Actual:** The file has the required environment, nine per-AC rows, artifacts, and verdict. E2 and E9 are independently reproducible: the generated landing, philosophy, conventions, and glossary pages load; the promise, five-obligation table, six success criteria, 15 glossary terms, and eight operational anchors are present and navigable. Each N/A row matches the TS, which reserves runtime consumer evidence for later phases.
- **Match:** ✅

### V7: `RF__phase-a__method_kernel.md`
- **RF claim:** The RF completely reports files, decisions, nine ACs, verification/evidence, observations, Fact Candidates, Strategic Insights, and Diagrams.
- **Actual:** All required sections are present and the substantive AC/test/link claims reproduce. One descriptive measurement is off by one: the executor-delivered `d749364:README.md` count is 2968 whitespace-delimited words, not 2969; the other seven line/word values reproduce exactly.
- **Match:** ⚠️ partial — one non-normative descriptive count corrected by this review

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest docs/scripts/test_gen_docs.py docs/scripts/test_integration.py` | ✅ 68 passed in 57.93s |
| 2 | `git diff --check d749364^ d749364` | ✅ PASS |
| 3 | `git diff --quiet d749364^ d749364 -- .tfw/project_config.yaml` | ✅ No config diff |
| 4 | `git diff --name-status/--numstat d749364^ d749364` | ✅ Four canonical files modified; RF and EV added; no out-of-scope implementation file in the Phase A result commit |
| 5 | `rg` research-code and prohibited locality/strategy scan over the four canonical files | ✅ No K3/M5/R9/V1 runtime term; no Pattern A/B, global light/heavy, always-inline/reference, or strategy-selector/catalog claim |
| 6 | PowerShell glossary-heading, numeric-ledger, deliverable-existence, and citation-path checks | ✅ 15/15 term headings once; 8/8 ledger objects; 7/7 deliverable paths; all Phase HL and ONB relative citation paths resolve |
| 7 | Independent line/word recount from `d749364^` and the delivered files | ⚠️ Seven values match RF; `README.md` after-count is 2968 rather than 2969 |
| 8 | `python -m mkdocs build --strict --config-file docs/mkdocs.yml` | ⚠️ Non-zero with 94 warnings, reproducing RF §4/§6; warnings include the existing resolver backlog and already-created TFW-48 planning/onboarding trace links |
| 9 | Rendered browser inspection of `/`, `/concepts/philosophy/`, `/reference/conventions/`, and `/reference/glossary/` | ✅ Changed promise/contract/term content is readable and navigable; 5 kernel rows, 15 terms, and 8/8 anchors observed |

## Discrepancies Found

1. **RF descriptive count:** RF §4 reports 2969 words for executor-delivered `d749364:README.md`; two independent whitespace-based recounts produce 2968. This does not change any acceptance result or threshold and is explicitly non-normative, but the RF claim is not exact.
2. **Pre-existing rendered asset debt:** the generated philosophy page renders its body and changed links correctly, but the unchanged `../docs/brand/philosophy.png` hero reference is broken because the generated `site/` tree does not contain the asset. This was not introduced by Phase A and does not contradict E2/E9's scoped text/link claims, but it is a real documentation defect to backlog.

The first discrepancy triggered 100% file verification. No further RF/implementation discrepancy was found.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | `evidence/EV__phase-a__method_kernel.md` | ✅ | ✅ — required structure and 9 AC dispositions present |
| E2 | `site/index.html`; `site/concepts/philosophy/index.html` | ✅ | ✅ — promise hierarchy, value/success sections, and changed links are readable and navigable |
| E3 | `.tfw/conventions.md` Method Kernel source gate | ✅ | ✅ — contract exists; runtime evidence is correctly N/A for Phase A |
| E4 | `.tfw/glossary.md`; generated conventions page | ✅ | ✅ — 15 headings once; 8/8 unique operational anchors resolve |
| E5 | Rule Deployment contract and RF scenario table | ✅ | ✅ — four required consequence/locality cases present |
| E6 | Proof contract and RF examples | ✅ | ✅ — Local/Seam/Live/Value Debt mapping is additive and packaging-independent |
| E7 | Learning/extension contract and RF matrix | ✅ | ✅ — both independence directions and observable registration are present |
| E8 | Numeric lifecycle, ledger, and config diff | ✅ | ✅ — seven types, eight objects, transition warning, no config change |
| E9 | Four generated pages plus pytest inline output | ✅ | ✅ — pages load, changed content/anchors resolve, 68 tests independently pass |

Evidence items audited: 9; VERIFIED dispositions substantiated: 2/2; N/A dispositions justified: 7/7; missing: 0.

## Knowledge Citations Verified

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | Phase HL §7.2 #1–3 | Root README; `.tfw/README.md` values and success criteria | ✅ | ✅ |
| 2 | Phase HL §7.2 #4 | `knowledge/philosophy.md` F3, F4, F11, F13, F17, F18, F20, F24–F26 | ✅ | ✅ |
| 3 | Phase HL §7.2 #5–7 | KNOWLEDGE D23–D29, D37, D43–D45, D49–D54 | ✅ | ✅ |
| 4 | Phase HL §7.2 #8 | `knowledge/convention.md` F4, F8, F13, F19 | ✅ | ✅ |
| 5 | Phase HL §7.2 #9 | `knowledge/process.md` F3–F7, F13–F16, F22–F25 | ✅ | ✅ |
| 6 | Phase HL §7.2 #10–11 | TFW-48 Iteration 1 D1–D10 and Iteration 2 D11–D20 | ✅ | ✅ |
| 7 | ONB §7 #1–12 | Cascaded Phase/Master HL sources plus `knowledge/philosophy.md` F21–F22 | ✅ | ✅ |

Citation rows: Phase HL 11 + ONB 12 = 23; verified: 23; hallucinations: 0. The complete Project Values index was scanned; no delivered Phase A contract contradicts current README values, KNOWLEDGE decisions, conventions, or topic facts.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈7 × 0.42⌉ files and recorded findings?
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citations: 23, verified: 23, hallucinations: 0
- [x] Evidence artifacts from RF §5 verified (files exist, claims match)?
  - Total evidence items: 9, verified dispositions: 9, missing: 0

Stage complete: YES
