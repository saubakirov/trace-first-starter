# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | AC-1 and AC-5 hold, but the complete TS DoD does not: AC-2/AC-11 fail under D1; AC-2/AC-12 under D2; AC-3 under D3; AC-7/AC-8 under D4; AC-6/AC-12 under D5; AC-4/AC-11 under D6; AC-4/AC-7/AC-10 under D7; and AC-9/AC-10 evidence quality under D8. See `verify.md` §§ Discrepancies Found and Deferred Evidence Decisions. |
| 2 | Two clauses, both answered. **(a) Purpose Check** — is this what we set out to do? **(b) Design soundness** | ❌ | **(a) ✅ Aligned.** Contract Baseline `ee09a8a`, HL §1: “A user can copy one standalone starter, initialize it naturally, work through result-first planning, execution, independent review, human acceptance, and reusable templates, while maintainers can move universal improvements between the public core and an Innoforce overlay without blind mirroring.” The material harm at stake is leaving general users on a frozen 1.0 starter or coupling them to private company practice; the neutral 1.5 result directly addresses it, adds no excluded adjacent product, and has no deferral confession or North-Star conflict. **(b) ❌ Unsound as shipped.** D1–D5 leave release authority, both update directions, path confinement, and identity locality dependent on incomplete checks or caller discipline, contrary to HL §7 principles 3–5 and 9 and North Star Structural Enforcement. These are repairable work defects, not a contract defect. |
| 3 | Tech debt documented | ✅ | RF §6 explicitly says “No observations.” D1–D8 are current-scope acceptance defects that must be corrected now, not deferred debt; no backlog item is being used to conceal an unmet criterion. |
| 4 | Style & standards | ❌ | D7 makes the documented identity command non-executable because the skill and parser use different flag names. D8 labels JPEG bytes as `.png` and publishes a rendered custom A4 artifact with a local path footer. These violate mutual-consistency, truthful-artifact and usable-output standards. |
| 5 | Observations collected | ✅ | RF §6 explicitly reports no out-of-scope observations. Independent review found eight in-scope defects and keeps them in the correction package rather than misclassifying them as observations. |
| 6 | RF completeness (§7–9) | ✅ | RF §7 contains two relevant, human-sourced Fact Candidates; §8 contains two useful execution insights; §9 provides a direction/authority diagram. Both Fact Candidates pass the Human-Only Test and need no challenge, though consolidation waits for approval. |
| 7 | Evidence completeness — does the evidence exist? | ✅ | All 47 declared attachments exist and every TS evidence category is represented. JSON/NDJSON, PDF, page-image, browser-capture, source-inventory and executable artifacts were all reachable; none is missing. |
| 8 | Evidence sufficiency — does the evidence establish the claim? | ❌ | The shipped positive commands are genuinely green, but hostile checks disprove material conclusions: 28/47 attachments fully support their bounded claims while 19 are partial or contradicted. D1–D8 show that V1/V2/V8/V11/V12, E2/E4/E8/E9/E10/E11/E12 and render claims do not establish the full DoD. |
| 9 | Backward compatibility | ❌ | A 1.0 downstream consumer can be reported at VERSION 1.5 without `release-manifest.json` (D2), so it cannot verify or become the trusted input to the next update. A fresh identity consumer following the shipped skill receives an argparse error (D7). These are existing documented workflows, not hypothetical new interfaces. |
| 10 | Safety | ❌ | H: source immutability, public semantic neutrality, secret-difference privacy projection and no publication all hold. They do not cure D3 (operation state written through a link inside the protected target), D4 (writes under an unpinned/new or overly permissive identity namespace), or D5 (reverse candidate may mutate public core after accepting a fabricated report). |

Rows 7 and 8 deliberately differ: the evidence set is complete, but a complete set of artifacts is not sufficient when the tests prove a weaker property than the claim.

## Purpose Check — row 2 clause (a)

The result is aligned with the Project North Star and the master HL at Contract Baseline `ee09a8a`. It preserves purpose, inspectability, human acceptance, provider-independent files, and a continuable public/downstream boundary. There is no excess beyond `editions/`, no work that the baseline assigns elsewhere, and no internal inconsistency between the baseline and North Star. The verdict is therefore not `not fit for purpose` and no owner-routed contract amendment is needed.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D59 — availability must remain distinct from tested capability, and separate sessions are not automatically independent people | RF/EV label V11 role scenarios and E8 locality/full-chain behavior verified from token/positive checks; E12 labels both update directions demonstrated | Yes. D6 proves V11 is contract-token lint rather than the stated scenario matrix; D4 disproves the full created-component/ACL locality claim; D2/D5 disprove complete bidirectional maintenance. The actual one-Coordinator → same-Executor → one-Reviewer lineage itself is independently established. |
| 2 | D57/D58 — visible editions topology and honest manual Assisted capability | RF says the package remains standalone under `editions/`, removes hooks, and treats manual order as normative | No. The topology, hook retirement and manual-capability boundary were independently confirmed. |

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Every ⚪ N/A carries a stated reason — no row is N/A in this review.
- [x] Row 2(a) is answered against Contract Baseline `ee09a8a` and the Project North Star, with a quoted clause and named harm.
- [x] Rows 7 and 8 are answered separately, with different reasoning.
- [x] DoD assessment references `verify.md` D1–D8.
- [x] RF §7–9 were checked for presence and quality.
- [x] KNOWLEDGE.md was cross-referenced and the material D59 contradiction is documented.
- [x] RF Fact Candidates were reviewed and need no challenge.

Stage complete: YES
