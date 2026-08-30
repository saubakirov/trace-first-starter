# REVIEW — TFW_20260830-114238_ASSISTED15 / Repeat Review 3: Neutral Assisted 1.5 Product and Maintenance Bridge

> **Date**: 2026-08-30
> **Author**: saubakirov via Codex Reviewer
> **Verdict**: 🔄 REVISE
> **RF**: [RF — TFW_20260830-114238_ASSISTED15](RF__TFW_20260830-114238_ASSISTED15.md)
> **TS**: [TS — TFW_20260830-114238_ASSISTED15](TS__TFW_20260830-114238_ASSISTED15.md)
> **Historical reviews**: [First-pass REVISE](REVIEW__TFW_20260830-114238_ASSISTED15.md); [Repeat Review 2 REVISE](REVIEW__TFW_20260830-114238_ASSISTED15__rev2.md)
> **Stage files**: `review/rev3/map.md`, `review/rev3/verify.md`, `review/rev3/judge.md`
> This is a full repeat review after terminal corrections `afef18a`, `640fad5`, `1aa6e97`. Both earlier review histories remain unchanged.

---

## 1. Map

The terminal result remains a Russian-authoritative, standalone Assisted 1.5 confined to the frozen 35-product-path `editions/` boundary. It combines five manual lifecycle roles, local identity, neutral offline templates, public-only release history and an asymmetric maintenance bridge: verified public stock may move forward under a closed baseline, while downstream learning returns only as a privacy-safe candidate requiring independent review. The real P6 Innoforce tree remains read-only evidence, never public payload.

The same Executor corrected the prior D9/D10 findings without adding a product path. This same independent Reviewer repeated Map, Verify and Judge over all current product paths, attachments, citations and actual runtime behavior rather than reviewing only the correction diff.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|---|---|---|
| 1 | Frozen boundary, product inventory and commit attribution | ✅ | 35/35 product paths: 25 added, 7 modified, 3 retired; 4,035 changed lines. All 21 Assisted task commits have zero forbidden-path hits. Concurrent root/TFW-55/TFW-60 state is separately identified and untouched. |
| 2 | Complete evidence and citation census | ⚠️ | 47/47 attachments inspected = 100%; 39 fully support bounded claims, eight are partial and none is missing. All cited authorities and 23 checked semantic anchors resolve. |
| 3 | D1–D8 and D10 reopening | ✅ | Manifest/policy authority, hostile path/privacy cases, seven role scenarios, documented identity command, neutral renders and D10 first-access/substitution ordering pass independent isolated checks. Substituted registry reads/accesses/writes are zero. |
| 4 | D9 real two-process lock and successful Windows runtime | ❌ | D11: the first maintenance holder never emits readiness within 15 seconds and the identity command also stalls. Bounded stacks terminate in Windows ACL/private-permission proof after the byte/project lock is acquired. Required loser/different-target contention cannot begin. |
| 5 | Rendered result and semantic neutrality/privacy | ✅ | All 20 PNGs were opened and all four PDFs parsed/read. Cyrillic pages are readable, links resolve, SVG/CSS are neutral, and the product carries no Innoforce fact, person, brand, corporate path, logo or private history. |
| 6 | Both maintenance directions and H: immutability | ⚠️ | Reverse confinement/privacy and 29-row H: pre/post equality under both digest orders hold; H: remained read-only. Forward product semantics are present, but current successful forward execution is blocked by D11. |
| 7 | E4 lineage and E12 publication scope | ⚠️ | E4 is accepted from the actual one-Coordinator → same-Executor → same-Reviewer lineage and deterministic seven-scenario table. No Assisted task push/tag/remote publication occurred and no remote ref contains the terminal product. D12 records that unrelated local tag `v2.0.0-dirty.5` now contains Assisted ancestors, making the stronger retained “no tag contains” sentence stale without violating task-scoped AC-12. |

Raw verification: [review/rev3/verify.md](review/rev3/verify.md).

### Repeat-review findings

| ID | Severity | Exact finding | Required acceptance evidence |
|---|---|---|---|
| D11 | Critical | On Windows, successful identity and maintenance lock entry do not terminate: stack traces reach `private_permissions`/`_windows_acl` after a live byte/project lock is held. The first D9 holder cannot emit readiness, so real same-target contention, loser zero-write behavior, different-target independence and a complete V1–V12 run are not reproducible. | Correct the lock/ACL interaction inside existing product paths. Expensive `icacls`/ACL work must occur outside a held live byte/project lock, or use another demonstrably safe bounded order; subprocesses require an explicit timeout and fail-closed result; nested/conflicting lock/ACL calls are prohibited. Retain fresh successful identity and maintenance full runs plus independent bounded D9 and D10 probes. |
| D12 | High, evidence integrity | The retained “no tag contains” statement was true at capture but is now false: unrelated release tag `v2.0.0-dirty.5` contains the Assisted ancestor commits. The tag target is an external release commit, no remote ref contains the Assisted terminal product, and the 21 task-attributed commits contain no publication action. This is not an AC-12 violation by the Assisted task. | Do not delete or rewrite the unrelated tag. Refresh RF, EV, attestation and derived audit evidence to state the current facts: external local tag containment, zero Assisted task push/tag operations, and no remote containment/publication. Remove the stronger global-isolation claim. |

## 3. Judge

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD met? (all TS acceptance criteria) | ❌ | D11 leaves AC-3/7/8/11 and dependent AC-12 incomplete. D12 does not violate task-scoped AC-12, but its stale evidence sentence must be corrected before acceptance. |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ❌ | Purpose is aligned with frozen HL §1 at `ee09a8a` and NS1: the neutral product prevents users remaining on 1.0 or inheriting private company practice. Design soundness fails because D11 makes a required Windows structural gate non-terminating. No contract defect or amendment exists. |
| 3 | Tech debt documented | ✅ | RF §6 reports no observations; D11/D12 are current-scope corrections, not deferred debt. |
| 4 | Style & standards | ✅ | Exact boundary, naming, Russian readability, template usefulness, no placeholders and semantic neutrality hold. |
| 5 | Observations collected | ✅ | RF reports none; both review findings remain in acceptance scope. |
| 6 | RF completeness (§7–9 present) | ✅ | Two valid human-sourced Fact Candidates, two useful strategic insights and the asymmetric authority-flow diagram are present. |
| 7 | Evidence completeness — does it exist? | ✅ | 47/47 attachments exist and every TS evidence class is represented. |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | Eight attachments are partial: actual successful Windows lock behavior contradicts their green conclusions, and one no-containing-tag sentence is stale. |
| 9 | Backward compatibility | ✅ | Existing 1.0 state, templates, identifiers and protected content remain preserved; D11 fails a new 1.5 mechanism rather than proving an existing-interface regression. |
| 10 | Safety | ❌ | Privacy, reverse confinement, H: immutability and task-scoped no-publication hold, but D11 can hold a live lock while an unbounded ACL subprocess path fails to complete. |

Full ruling: [review/rev3/judge.md](review/rev3/judge.md).

## 4. Verdict

**🔄 REVISE**

The result is fit for the approved purpose, stays inside the frozen product boundary, and preserves closure of D1–D8 plus the logical D10 first-access correction. It is not acceptance-ready because D11 makes the real Windows lock/ACL path non-terminating, preventing the defining identity and safe-maintenance operations from completing and preventing the required D9/V1–V12 evidence from being reproduced. D12 is a separate task-local evidence-integrity correction: the task did not push, create a tag or publish remotely, but an unrelated later release tag now contains its ancestor commits and the retained stronger sentence must no longer be presented as current fact.

No HL/TS amendment is needed. The same Executor must make only the bounded corrections below, and this same Reviewer must perform another complete re-review afterward. No new product path, publication, push or tag is authorized.

### Items to fix

1. **D11 — bounded, non-conflicting Windows lock/ACL path.** Within existing product paths, remove the non-termination while preserving full-chain owner/ACL validation and D10 first-access ordering. Move expensive `icacls`/ACL subprocess work outside any held live byte/project lock, or use another proven safe order; define explicit subprocess timeout/fail-closed behavior; remove any nested/conflicting lock/ACL call. Retain fresh successful identity and maintenance full runs with bounded timeouts. Retain a real two-process same-target D9 test proving one stable target key, loser blocked before operation-directory creation with zero target/product writes, and independent different-target progress. Recheck D10 order and substitution-before-first-read after the repair.
2. **D12 — truthful task-scoped publication evidence.** Do not delete, move or rewrite unrelated tag `v2.0.0-dirty.5`. Refresh RF/EV/attestation and generated audit evidence so they explicitly distinguish: the external local tag now contains Assisted ancestors because of a concurrent release; no Assisted task commit or operation created a tag or pushed; no remote-tracking ref contains the terminal product and no Assisted remote publication occurred. Remove the stale stronger claim that no local tag contains the product commits.

Correction constraints: H: remains strictly read-only; product changes remain under the existing approved `editions/` paths; RF/evidence changes remain task-local; root guides, `.tfw`, `KNOWLEDGE.md`, `TECH_DEBT.md`, Light and unrelated work stay untouched; no push, tag or publication.

## 5. Tech Debt Collected

No tech-debt item is collected. D11/D12 are current-scope acceptance corrections and cannot be deferred.

## 6. Traces Updated

- [x] Task `status.md` remains lifecycle `RF` for correction and receives a new RF→RF transition event for this repeat verdict.
- [x] First-pass and revision-2 REVIEW/stage traces remain unchanged; revision 3 uses distinct artifacts.
- [x] HL/TS/ONB/RF/EV and implementation remain unchanged by the Reviewer.
- [x] Unrelated `.gitignore`, `.tfw`, root knowledge and TFW-55/TFW-60 state remain unstaged and unmodified by this review.
- [x] tfw-docs: N/A on REVISE; the frozen product boundary forbids root `KNOWLEDGE.md`, `TECH_DEBT.md`, `.tfw` and root-guide changes.
- [x] tfw-knowledge: N/A on REVISE; RF candidates remain candidates and scope-drift consolidation is prohibited.

## 7. Fact Candidates

No new reviewer-observed human-only Fact Candidate was introduced. The two user-sourced RF §7 candidates remain relevant and unchallenged; consolidation waits for eventual approval.

---

*REVIEW — TFW_20260830-114238_ASSISTED15 / Repeat Review 3: Neutral Assisted 1.5 Product and Maintenance Bridge | 2026-08-30*
