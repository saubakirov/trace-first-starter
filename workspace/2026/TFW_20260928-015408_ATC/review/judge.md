# Judge — TFW_20260928-015408_ATC

> Verify: [verify.md](verify.md). Judgment applies to Candidate `7dfed8bf5350e10f889f66c606a672a52e88f9a3` under approved TS `772d5773ba92e5534579cfd0e9152619a4261554`.

## Status and Materiality

The rendered HL coordination-selection table is a material VALUE defect, F1. It is a one-row structural error in a shipped authority template, not a request for a new role, test, or policy. The other bounded claims hold for the local environment and named revisions; unobserved provider wake remains an explicit limit.

## 1. VALUE

| Subject | Status | Evidence / finding IDs |
|---|---|---|
| Purpose and approved value | ❌ | F1; Purpose Check below. Most A plus B/V behavior serves the purpose, but the owner-facing mandate template does not render its authority columns. |
| Domain behavior and acceptance criteria | ❌ | V1–V5: AC-1/TS §4's HL selection template is not usable as the intended table; AC-2/3/4/5/7 otherwise hold at their stated scope. AC-6 presentation remains a Coordinator act after REVIEW. |
| Architecture and HL principles | ✅ | V1–V4: one direct task Coordinator, bounded phase Coordinators, safe successor, historical compatibility and scoped roles. F1 is a local template defect, not a rejected architecture. |
| Safety and security | ✅ | V1/V2/V4: no new host/MCP mechanism or external action; invalid routes refuse; old carrier retained. No deployed security claim exceeds local evidence. |
| Human acceptance authority and reserved effects | ❌ | V5/F1: the coordination-selection template loses the tabular link among scope, upward route, reservations and immutable epoch in its rendered form. Actual ATC owner approvals and dispatches remain valid (V4). |

### Purpose Check

The master HL at frozen A1 says the selected arrangement must be “made usable in the shipped workflow and receiving-project entry points” (§3.7) and that another unit should recover “intent, authority, state and next action from lawful durable inputs” (§3.5). Project NS1 requires another authorized person or agent to “inspect its material grounds and current result” and see “where authority remains.” The Candidate advances these goals through explicit task/phase routes, but F1 makes the shipped HL selection table render as a paragraph, obscuring which reservation and epoch bound which role and route. This creates a concrete risk of misreading an owner mandate in a future receiving HL.

Excess/adjacency: no unapproved role, host mechanism or runtime was added (V1/V4). Deferral: live wake and Coordinator's pre-merge presentation are explicitly left to their actual observation/authority gates, not claimed complete (V3). Materiality: the malformed authority table affects human-readable bounded delegation and portability, not merely word choice. The approved vision is coherent and the repair is within the existing TS; this is not a contract defect or whole-result purpose rejection.

## 2. ASSURANCE

| Subject | Status | Evidence / finding IDs |
|---|---|---|
| Evidence exists | ✅ | RF §5, EV, accounting JSON, receiving probe, immutable Git blobs (V2–V4). |
| Evidence applies to accepted subject, Candidate, environment, oracle and dependencies | ✅ | V2–V4; exact candidate and baseline verified, current source/installed copies checked. File-backed receiver is explicitly bounded. |
| Evidence is sufficient for each material claim and risk | ❌ | V5/F1 independently disproves the HL-template presentation claim. Remaining material claims have sufficient local proof; no live wake or universal receiver claim is accepted. |
| Permanent guards demonstrate relevant counterfactual detection | ⚪ N/A | No new permanent guard was admitted. Existing 14-test pass is a positive regression control; temporary invalid-route probes have relevant negative inputs (Verify Guard table). |

## 3. TRACE

| Subject | Status | Evidence / finding IDs |
|---|---|---|
| Governing authority and independent role lineage | ✅ | V1/V4: HL A1, approved TS, Executor and Reviewer exact dispatches, distinct units and Coordinator route. |
| Accepted-result identity and immutable accounting | ✅ | V4: fixed Candidate, exact 23-path selector, 313/223 numeric LOC, 46 blob token replay and digest. |
| Reproducibility and citation integrity needed for material claims | ✅ | Verify source/citation tables; relevant PV links resolve. Build warnings and live-provider limits are disclosed. |
| Authorized continuation, item routes and dispositions | ✅ | F1 has same-Executor correction via Coordinator, unchanged TS/rung 1, new VALUE Candidate and affected recheck. Coordinator owes owner-facing comparison after independent review. |
| Record-only observations | ✅ | `KNOWLEDGE.md` §1 still describes the previous Gateway topology; it is a pending Coordinator docs/knowledge alignment, not a reason to move this implementation Candidate by itself. |

## 4. Finding Rulings

| ID | Class | Subject / affected claim or authority | Fact + oracle | Harm and material consequence | Owner / completion | Route / rung | Candidate effect | Disposition |
|---|---|---|---|---|---|---|---|---|
| F1 | VALUE | `.tfw/templates/HL.md` authority-selection table; TS §4, AC-1, frozen HL §3.7 and NS1 | 11 header/data cells, 10 separator cells; Python Markdown and generated MkDocs HTML render a paragraph (V5) | New HLs copied from this template lose the readable association among role, upward route, reservations and epoch, weakening owner review and lawful receiver reconstruction | Same Executor; render an 11-column table and show affected source/docs checks, exact accounting and a new fixed Candidate | Coordinator rules ordinary rung 1 under unchanged TS, returns same Executor | moves when VALUE template is corrected | pending |

## 5. Aggregate Verdict

**Verdict:** 🔄 REVISE

**Reason:** F1 is a material, correctable VALUE failure of a shipped owner-authority template. V1–V4 establish the other bounded implementation, evidence and trace claims, so the next act is the narrow rung-1 correction and independent affected recheck of the new Candidate. This verdict does not authorize merge, final owner acceptance or provider wake claims.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | Accepted claim | Contradiction / effect |
|---|---|---|---|
| 1 | `KNOWLEDGE.md` §1, “Coordinator UX & Current Selection” still describes a separate GATEWAY as the current full-session topology | Approved A1/TS makes task Coordinator direct for one phase and phase Coordinators bounded for long work | The old architecture-map row is stale at the new Candidate epoch. Coordinator's later docs/knowledge alignment must scope it truthfully; no VALUE Candidate restart or owner ruling is inferred from this reference row. D83 and PCUX records remain historical at their source epochs. |

## Checkpoint

**Self-check:**
- [x] Judged VALUE, then ASSURANCE, then TRACE and all mandatory floors.
- [x] Supported each status with Verify evidence and explained N/A.
- [x] Tested Purpose against frozen master HL and Project North Star, with concrete harm.
- [x] Separated evidence existence, applicability and sufficiency.
- [x] Gave F1 the full item contract, rung and Candidate effect.
- [x] Kept later docs and owner effects with their actual Coordinator/owner.
- [x] Derived one verdict from material consequence, not count or checklist volume.

Stage complete: YES

## Round 2 — bounded affected judgment, 2026-09-28

**VALUE.** The replacement Candidate repairs F1 within the existing approved TS. The generated owner-authority selection is now a real 11-column table, allowing the scope, upward route, reservations and epoch to be inspected as linked columns. This serves the frozen master HL §3.7 requirement for a usable shipped workflow/entry and Project NS1's inspectable human-governed continuity. The A/B/V architecture, historical compatibility, human reservations and safety boundaries are unchanged. F1 is paid for the local shipped result; live external receiving-agent activation and idle-parent wake remain unobserved, exactly as before.

**ASSURANCE.** The rendered HTML and independent rebuild establish the affected presentation claim at replacement Candidate `bddccf8e1287e30db2ca4bf43ad0bcf68d0d0f65`. The full Baseline→replacement VALUE accounting, digest and tokenizer rows independently match. Existing route, parser and receiver-parity evidence remains applicable because its subject paths and dependencies did not change. EV E2.1's optional fragment SHA-256 is wrong; direct committed-file and rebuilt-content equality establish the relevant claim without that number. The correct hashes are recorded in Verify as a non-material TRACE observation.

**TRACE.** The same Executor accepted the Coordinator's rung-1 ruling at `c944f6b`, produced one VALUE correction and a new fixed Candidate, then returned cumulative RF/EV at `a40e02c`. Current status is valid `RF`; the approved TS/denominator and Coordinator route are unchanged. The new live REVIEW sibling may record APPROVE and the authorized `RF → KNW` transition. The Coordinator still owes the owner-facing pre-merge comparison, docs/knowledge alignment, final owner acceptance and any later effects. No new material item remains; the digest observation is disposed in the current review record with Candidate unchanged.

**Round 2 aggregate verdict:** ✅ APPROVE for the replacement Candidate and affected result. F1 is paid. This Reviewer returns to the same Coordinator for the canonical closing route and remains available for changed final claims; it does not capture knowledge or declare DONE.
