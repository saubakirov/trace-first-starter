# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW-46](../../HL-TFW-46__evidence_layer.md)
> Goal: Close the gap between "RF says done" and "actually works for the user" by adding an Evidence layer to TFW.

## Research Plan

**Gather:**
- External: research how "evidence of completion" is framed across disciplines — DevOps (deployment evidence), QA (acceptance testing vs unit testing), regulatory/audit (audit trail, chain of evidence), scientific publishing (reproducibility), legal (chain of custody). Focus on terminology and the cognitive/behavioral framing each term produces.
- External: survey AI agent frameworks (Devin, SWE-bench, AutoCodeRover, OpenHands, etc.) — do any distinguish "tests pass" from "actually works"? What terms do they use?
- Internal: scan an existing project's `testing/` system — STATUS.md, evidence folders, PASS/FAIL/XFAIL/XPASS vocabulary, anti-self-deception mechanisms. Extract the mature pattern.
- Internal: scan backend project tasks/, a multi-service project's RF, TFW-36 blog phases — extract implicit evidence patterns. Where did things break at the mocked→real transition?
- Candidate dimensions: Terminology (term choice), Domain Pattern (what "real" means per domain), Evidence Lifecycle (who designs / who collects / who audits)

**Extract:**
- Build a domain catalog: for each project type (code, docs, analytics, HR/tenders, design), what constitutes "real evidence"? What tools exist?
- Build a terminology comparison matrix: each candidate term × connotations × industry usage × agent behavior it would trigger (per D28 Naming-as-Prompting)
- Cross-reference domain patterns with terminology — does one term cover all domains?

**Challenge:**
- Stress-test the winning terminology against edge cases: trivial tasks (typo fix), non-code tasks (blog post, tender document), offline tasks (print to PDF)
- Counter-evidence: are there domains where the synthetic/real distinction doesn't apply? Where evidence would be pure bureaucracy?
- Attack H6/H7 directly: does the chosen term produce different agent behavior than alternatives?

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | Evidence can be domain-agnostic with a fixed status vocabulary (VERIFIED/DEFERRED/BLOCKED/N/A) but domain-specific evidence types | open |
| H3 | Existing user projects already contain implicit evidence patterns that can be extracted and generalized | open |
| H6 | There exists a single term (Evidence/Proof/Attestation/Verification/Acceptance) that produces correct agent behavior across all TFW roles | open |
| H7 | The term choice affects agent behavior more than the section instructions (per D28 Naming-as-Prompting) | open |

> **Iter1 focus:** H3, H6, H7 per iterations.yaml. H1 touched via domain catalog but primary testing deferred to iter2.

## Scope Intent
- **In scope:** Terminology decision (which word + why), domain evidence patterns (what "real" means across real-world projects), external precedent (how other frameworks/disciplines handle this), an existing project's testing/ deep scan
- **Out of scope:** Template section numbering, workflow integration points (Phase B), tooling/MCP patterns (H4 — iter2), section merge decision (H5 — iter2), adapter updates

## Guiding Questions
1. The HL proposes "Evidence" as the term — but is this actually the best word? Per D28, naming creates behavior. What behavior does "Evidence" trigger vs "Proof" vs "Attestation" vs "Acceptance Test"?
2. In non-code projects (backend API, blog, HR/tenders), what does the executor actually do (or fail to do) at end-of-task? Are there real examples of "RF said done but wasn't"?
3. The testing project's testing/ has STATUS.md, XFAIL/XPASS, evidence folders — which elements are project-specific and which generalize to any TFW project?

## User Direction

**Q1 (terminology):** User says "Evidence" feels right — it emerged organically during work. No strong alternative preference. Per Trust Protocol: domain input → trust as-is, but term choice is a technical approach → verify externally.

**Q2 (non-code evidence):** Concrete examples of end-of-task failures in document/spreadsheet projects:
- Document rendering: elements shift, stretch, layout breaks
- Encoding issues: characters display incorrectly
- Excel: cells too small, content hidden/truncated, columns need resizing
- Color scheme: wrong colors, poor contrast, text unreadable behind colors
- General: visual appearance differs from intent — things "look wrong" but pass any automated check

**Implication:** For docs/spreadsheets, "evidence" = visual confirmation that the output looks correct to a human. No automated test catches "color scheme doesn't match" or "cell too narrow." This is exactly the synthetic/real gap the HL describes.

**Q3 (testing project priorities):** No specific priorities. Scan broadly.

---
Stage complete: YES
