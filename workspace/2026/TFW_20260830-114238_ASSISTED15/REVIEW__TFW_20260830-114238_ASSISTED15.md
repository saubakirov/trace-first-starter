# REVIEW — TFW_20260830-114238_ASSISTED15 / Single Phase: Neutral Assisted 1.5 Product and Maintenance Bridge

> **Date**: 2026-08-30
> **Author**: saubakirov via Codex Reviewer
> **Verdict**: 🔄 REVISE
> **RF**: [RF — TFW_20260830-114238_ASSISTED15](RF__TFW_20260830-114238_ASSISTED15.md)
> **TS**: [TS — TFW_20260830-114238_ASSISTED15](TS__TFW_20260830-114238_ASSISTED15.md)
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> This file synthesizes the independent review. The stage files remain the raw evidence.

---

## 1. Map

The result reconstructs Assisted as a standalone, Russian-authoritative 1.5 edition within an exact 35-product-path delta. It combines five lifecycle roles, fail-closed local identity, neutral reusable templates, public-only release history, and an asymmetric maintenance bridge: verified public stock may move forward while downstream discoveries return only as privacy-safe review candidates. The real Innoforce tree remains read-only P6 evidence rather than public payload.

The governing design assigns separate authorities to the release manifest, maintenance policy, private operation report, and public candidate. It preserves manual lifecycle as the normative baseline, exact hook retirement, protected downstream state, and explicit human acceptance after independent review.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|-----------------|--------|----------|
| 1 | Product boundary and exact baseline diff | ✅ | 35/35 paths opened: 25 added, seven modified, three deleted; 3,230 changed lines; no forbidden diff from `f3eb986`; budgets hold. |
| 2 | Current release authority and stock positive commands | ⚠️ | Current 31-entry manifest and policy hashes regenerate exactly; shipped release, V1–V12, identity, template and task checks pass. Hostile checks expose D1–D7, so the green signals establish less than RF/EV claim. |
| 3 | All evidence and rendered artifacts | ❌ | 47/47 attachments exist and were inspected; 28 fully match their bounded claims, 19 are partial or contradicted. All 16 page images and four browser full captures were visually checked; D8 records the render/path/format defects. |
| 4 | Neutrality and privacy | ⚠️ | The shipped product is semantically neutral: no Innoforce facts, people, brand, private history, unique source path or organization knowledge; SVG/CSS restrictions hold. Reverse-flow enforcement and rendered path hygiene fail under D5/D8. |
| 5 | EV E4 deferred role lineage | ⚠️ | Live lineage is exactly one Phase Coordinator → same Executor → one independent Reviewer, with Coordinator-only reporting. The claimed V11 complete/partial/lost-handle/no-interrupt/overlap/full-review scenario matrix is not established; D6. |
| 6 | EV E12 source, directions and publication | ⚠️ | H: P6 source immutability and the two canonical sort digests are independently confirmed; no product/evidence commit is in a remote-tracking ref or tag and no publication was performed. Both maintenance directions are not accepted because of D2/D5. |
| 7 | Knowledge and claim sources | ✅ | 20/20 HL/ONB citations resolve, exist, match their meaning and are relevant. D59 exposes claim-boundary contradictions in RF/EV, not a frozen-contract defect. |

Raw verification log: [review/verify.md](review/verify.md). Verification was complete; no required file, attachment, source or tool remained unavailable.

### Findings and required evidence

| ID | Severity | Exact finding | Required correction and acceptance evidence |
|---|---|---|---|
| D1 | Critical | `editions/maintenance/assisted_maintenance.py:242` generates completeness, but `:756` validates only listed entries. Removing one payload entry and recanonicalizing still returns `state=verified`. | Require exact equality with regenerated allowed payload; add omitted payload/policy, unexpected payload, self-entry and non-regular hostile fixtures. |
| D2 | Critical | `assisted_maintenance.py:369`, `:420` and `:443` plan/stage manifest records but never the self-excluded `release-manifest.json`. A forward target reaches VERSION 1.5 without a manifest and fails `verify-release`. | Carry the manifest as a separately classified release authority through stage, baseline and postconditions; prove the forward target passes `verify-release` and can serve as the next source. |
| D3 | High | `assisted_maintenance.py:443` uses `absolute()` plus textual `commonpath`, then creates operation state before the target baseline. An outside symlink resolving inside target created `target/operation`. | Resolve and pin all existing components, reject link/junction/reparse ancestry, prove the to-be-created parent outside source/target, and retain an actual Windows hostile fixture. |
| D4 | Critical | `editions/02-assisted/.agents/skills/tfw-identity/scripts/tfw_identity.py:274` pins three fields for existing parents; `:428` creates `tfw-assisted` but never pins that component or checks ACL/owner/private permissions before lock/temp writes. | Pin/open/lstat the full created chain after namespace creation; require platform ACL/owner proof or return unknown; add namespace-substitution and permissive-ACL zero-write fixtures. |
| D5 | High | `assisted_maintenance.py:534` accepts a fabricated minimal report and any candidate directory; a candidate under a temporary public tree mutated that tree. | Validate a closed canonical terminal schema and regular-file provenance; require one approved candidate root proven outside public/source/target; add fake-report and public-root hostile fixtures. |
| D6 | High | `assisted_maintenance.py:695` calls V11 complete from file length and Russian token presence; no deterministic role failure-mode matrix exists. | Separate contract lint from a recorded state/tabletop matrix for complete, partial, lost-handle, no-interrupt, overlap, manual fallback and full re-review. Preserve the established live role lineage. |
| D7 | High | `tfw-identity/SKILL.md:27` documents `--corporate-role`; `tfw_identity.py:610` accepts only `--organization-role`. | Align skill/parser/people terminology and execute the documented command from a clean edition copy. |
| D8 | Medium | `a4-custom.pdf` and page images expose a local `file:///D:/projects/...` footer; all four `browser-*-full.png` files have JPEG JFIF bytes and stitch overlaps. | Rerender without browser headers/footers, make extension and bytes agree, visually inspect every replacement, and update `render-summary.json` honestly. |

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ❌ | AC-1 and AC-5 hold; D1–D8 leave AC-2/3/4/6/7/8/9/10/11/12 materially unmet. |
| 2 | Purpose Check + design soundness | ❌ | Purpose is aligned with HL §1 at Contract Baseline `ee09a8a` and the Project North Star; the neutral bridge prevents users being stranded on 1.0 or coupled to private practice. Design soundness fails because D1–D5 do not structurally enforce the frozen authority/safety model. No amendment is needed. |
| 3 | Tech debt documented | ✅ | RF §6 says “No observations”; all reviewer findings are in-scope corrections, not deferred debt. |
| 4 | Style & standards | ❌ | D7 breaks the documented CLI; D8 mislabels visual bytes and leaks a local path in output. |
| 5 | Observations collected | ✅ | RF reports none; independent defects are correctly kept in current scope. |
| 6 | RF completeness (§7–9 present) | ✅ | Two valid Fact Candidates, two useful Strategic Insights and one authority-flow diagram are present. |
| 7 | Evidence completeness — does it exist? | ✅ | 47/47 attachments exist; every TS evidence category is represented. |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | 19/47 attachments are partial or contradicted; positive tests do not establish the hostile and visual claims disproved by D1–D8. |
| 9 | Backward compatibility | ❌ | D2 leaves upgraded 1.0 consumers without the next-update authority; D7 breaks the documented identity consumer path. |
| 10 | Safety | ❌ | H: immutability, no secrets and no publication hold, but D3–D5 permit writes across protected path/locality boundaries. |

## 4. Verdict

**🔄 REVISE**

The implementation is fit for the approved purpose and remains within the frozen product boundary, so rejection or a frozen-HL amendment would be disproportionate. It is not acceptance-ready: three Critical, four High and one Medium findings show that release completeness, forward continuity, path confinement, operational locality, reverse provenance/confinement, role-scenario evidence, the documented identity command and render evidence do not yet satisfy the TS.

The same Executor must make a bounded correction inside the existing approved product/evidence scope. The same Reviewer must then repeat a complete review; prior green positive tests may not substitute for the hostile cases.

### Items to fix

1. **Release authority — D1/D2.** Enforce regenerated manifest equality, carry the manifest through forward update, and prove the target is a valid next release source.
2. **Path and reverse confinement — D3/D5.** Pin resolved components outside protected roots; require a closed terminal report and one approved outside candidate root; retain hostile fixtures.
3. **Identity locality and command — D4/D7.** Pin the created namespace/full chain, establish private ACL/owner state or fail closed, align the flag, and execute the documented command.
4. **Role evidence — D6.** Replace token-presence coverage with the deterministic scenario record required by AC-4/AC-11 while preserving the current one-Coordinator/same-Executor/one-Reviewer lineage.
5. **Render evidence — D8.** Regenerate clean PDFs/PNG captures, inspect every changed page/full capture, update the evidence summary, and rerun the full evidence set honestly.

Correction boundaries: no new product path is authorized, no HL/TS amendment is needed, H: remains strictly read-only, and no push, tag or publication is permitted.

## 5. Tech Debt Collected

No tech-debt item is collected. D1–D8 are present-scope acceptance defects and must not be deferred.

## 6. Traces Updated

- [x] Task `status.md` remains at lifecycle `RF` for correction; this review adds an RF→RF transition journal event.
- [x] HL status is unchanged because the single phase has not completed.
- [x] Task `status.md` `updated` reflects the review clock; no counter was incremented.
- [x] Other project files were checked; unrelated `.gitignore`, TFW-55 and TFW-60 state was not staged or modified by this review.
- [x] tfw-docs: N/A at REVISE; no approved product result exists to document.
- [x] tfw-knowledge: Deferred until APPROVE; RF §7 candidates remain candidates rather than verified knowledge.

## 7. Fact Candidates

No new reviewer-observed human-only Fact Candidate was introduced. The two human-sourced candidates in RF §7 remain relevant and unchallenged; consolidation is deferred until the implementation is approved.

---

*REVIEW — TFW_20260830-114238_ASSISTED15 / Single Phase: Neutral Assisted 1.5 Product and Maintenance Bridge | 2026-08-30*
