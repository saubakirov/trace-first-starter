# Map — “What was done?”

> **Reviewer:** robert, Reviewer task `01a09aaf-9af3-7d13-8ef8-59d3bc84d5e7`, for saubakirov
> **Direct parent:** Coordinator `01a09974-6716-7cc0-9916-fd6d04c91481`
> **Selected LEAD:** `01a08161-79d3-7472-a01e-8cdc957ee951`
> **R1 review input:** `c02cd3ca1af5d33eea37479ad514d0541e5daafe`
> **Exact R1 return:** `92a78deee082521b1056ef38aa14d51d36a3b649`
> **Candidate:** `65c3c94b2347c69f6d21ac2e2664a39ef46b3ae2`
> **Baseline:** `ec91c56007c20cda79f740fec15c85e4af74d17c`
> **Prior verdict:** `de2abc53b873483fdd8deca7ca99ea8883461ff5`, clarified by `a644c996e67bd01f677709140f51563bd17f5334`
> **RF:** [RF__TFW_20260909-231654_TKL.md](../../RF__TFW_20260909-231654_TKL.md)
> **TS:** [TS__TFW_20260909-231654_TKL.md](../../TS__TFW_20260909-231654_TKL.md), approved and current blob `f69fd4099a21a07ae2d17e6b5108b04ac94f107e`

## Understanding

R1 keeps the accepted R0 scope and adds two bounded corrections. Candidate `65c3c94b...` restores five historical compiled fragment destinations through the generator, contract/adapters and integration tests (AC-8); the same Executor then performs the single Coordinator-authorized established-receiver replay from the corrected Candidate into the pinned Baseline, preserving old/intended bytes before each write, installing readers before authority retirement, opening compiled output, exercising one unchanged repeat and one changed-authority refusal, and sealing the actual receiver effects (AC-7).

The final R1 return appends the new evidence and cumulative ONB/RF/EV reports without moving Candidate. AC-1–6 and AC-9/10 are inherited only within the prior REVIEW's stated bounds; AC-11 is open until this Reviewer independently accepts the corrected AC-7/8 evidence, exact accounting and the applicability/rendering of changed final reports.

## TS ↔ RF Alignment

| TS requirement | R1 RF claim | Aligned? |
|---|---|---|
| AC-1 — complete, proportionate producing-role handovers | Inherited from R0; no R1 change to the accepted handover finding. | ✅ Addressed; inherited within R0 bounds |
| AC-2 — distinguish missing, justified-none, unavailable, retain-only and owed publication | Inherited from R0; R1 does not reclassify prior outcomes. | ✅ Addressed; inherited within R0 bounds |
| AC-3 — qualification preserves meaning, identity and authority | Inherited from R0; corrected replay consumes the existing scoped record without broadening it. | ✅ Addressed; inherited within R0 bounds |
| AC-4 — honest replay, concurrent publication and contradiction | Inherited from R0; the R1 unchanged repeat and authority-drift refusal add adoption-local evidence only. | ✅ Addressed; inherited within R0 bounds |
| AC-5 — stable ordinary-file entry and currentness decision | Inherited subject to checking the current `KNOWLEDGE.md` architecture-map wording against the shipped current-use entry and retained SLC source. | ✅ Addressed; observation requires materiality check |
| AC-6 — finite PTTC close and accepted-effect recovery | Inherited from R0; R1 preserves the approved recovery semantics. | ✅ Addressed; inherited within R0 bounds |
| AC-7 — clean init and bounded adoption | R1 claims one actual established-receiver replay with 57 before-image paths, 58 immediate write pairs, 55 reader-first changes, a prepared cut/continuation, six opened HTML pages, an unchanged repeat, a changed-authority refusal and sealed effects. | ✅ Addressed; correction requires independent verification |
| AC-8 — source and compiled legacy/current destinations | R1 Candidate adds five historical fragment aliases; 89 generator/resolver, 47 contract/adapter and 18 integration tests pass, followed by the 641-test configured collection, one production build and five browser observations. | ✅ Addressed; correction and final-report rendering require independent verification |
| AC-9 — consumer routes agree and bookkeeping stops | Inherited from R0; R1 claims no new live global bookkeeping or router divergence. | ✅ Addressed; inherited within R0 bounds |
| AC-10 — bounded fresh mixed-current consumer | Inherited from R0; no replacement consumer attempt is claimed. | ✅ Addressed; inherited within R0 bounds |
| AC-11 — reviewability and exact evidence | R1 claims complete sealed custody, exact report prefixes, 17 final report/control paths and unchanged TS/approval authority; acceptance remains blocked on this verdict. | ✅ Addressed; final acceptance open |
| Dedicated accounting row | Candidate is claimed to change all and only 58 VALUE paths: 53 MODIFY, four CREATE, one DELETE; `+1230/-999 = 2229`, below the unchanged approved thresholds `116` paths and `5148` changed lines. | ✅ Addressed; exact rerun required |

## Changed-file and evidence map

- Product/ASSURANCE Candidate delta: seven files in commit `65c3c94b...` — two workflow copies, the compilable contract, generator code and two test files — completing AC-8 without changing the 58-path VALUE selector.
- R1 AC-8 evidence: `evidence/r1-ac8/` records pre/post input seals, the three affected test slices, configured collection, production build, navigation receipts, exact accounting and the checkpoint seal.
- R1 AC-7 evidence: `evidence/r1-ac7/` records source revalidation, fixed clock, SLC prerequisite, preservation, all 58 immediate before/after pairs, reader-only cut, continuation, build/opened output, repeat/refusal and raw/Git seals.
- Exact raw replay commit: `6b0d5c748d51c55c7c22147799cdb70131c22049`; final R1 report/control commit: `92a78deee082521b1056ef38aa14d51d36a3b649`.
- Coordinator admission/recovery receipts are TRACE-only. Their custody explanation is review context, not a substitute for the Executor's sealed evidence or a new acceptance claim.

## Deviations from TS and bounded limitations

1. The original self-adoption Q3 omission remains historical and unaltered. R1 is the sole prospectively authorized replacement replay; it does not rewrite the first attempt.
2. The R1 AC-8 affected slices and build precede the later final ONB/RF/EV append. Applicability to the unchanged Candidate may be inherited, but the changed final reports need a fresh bounded rendering check in Verify.
3. No new configured full test execution is claimed. The prior configured run remains reusable only for unchanged coverage; R1 supplies current affected slices plus collection as authorized.
4. Two browser-observer errors and one transport parse error are retained with successful filesystem/HTML and raw-custody evidence. Their materiality remains for Verify/Judge.
5. Coordinator recovery proves the admitted branch and hashes, but cannot explain why the earlier local directory disappeared. This is a disclosed custody limitation, not product evidence.
6. The current `KNOWLEDGE.md` Architecture Map still uses “Knowledge Gate” wording in the Task Storage row. Verify must determine whether the current-use entry, scoped successor record and retained SLC source make that wording historical context or a materially false current routing assertion.

No R1 work is mapped as an undisclosed VALUE expansion, a second native attempt, or a replacement for the preserved R0 epoch.

## Checkpoint

**Self-check:**

- [x] Read the cumulative RF §§1–5 completely, including the R1 correction and material handover.
- [x] Read all eleven unchanged TS ACs and mapped R1 plus inherited claims to RF §3.
- [x] Read frozen HL §7 and can state its continuity, responsibility, preservation, source, minimal-completeness, bounded-access and finite-assurance philosophy.
- [x] Read the cumulative ONB; R1 authority, sequencing and terminal Coordinator rulings are explicit.

Stage complete: YES

## R2 continuation map — 2026-09-14

> **R2 review input:** `1409cbdcb8046bcc0a7c0efa727536e5ad6d3e62`
> **Exact R2 return:** `b91ec17f16a1a5ef13171b53a404670c5b9745b2`
> **Tested Candidate / checkpoint:** `a99ba6cd756a7db444f217aef4e5a0eb83faee51` / `793cd97f71f484fcbe7c2e01dcfe7503148b402d`
> **Stopped native raw:** `1a0a37c443fe0d762a1396f1354d93ac08391637`

R2 implements the single ruled current-description correction in three existing VALUE paths and one existing ASSURANCE path. It removes the three active-gate claims from the current Task Storage row, `Where tasks live` contract and maintained state-reader docstring, while a scoped source guard keeps explicit retirement and historical D82/D87 occurrences valid. The exact Candidate delta is VALUE `+5/-6` plus ASSURANCE `+58/-0`; executable state-reader AST, migration/update algorithms, selected path set, authority/order and historical sources are unchanged.

The affected-native continuation required by this Reviewer's `93b8becd...` clarification did not complete. Its sole authorized attempt stopped during preparation operation 3, before new source staging, preservation, writes 26/55/57, config provenance 56/58, native build or unchanged repeat. Later equality of the 2,317 prepared positive-repository files diagnoses the observer's total-LF versus bare-LF mismatch but does not turn the stopped case into an observed Candidate effect.

| TS requirement | R2 RF claim | Mapped status before Verify |
|---|---|---|
| AC-5 | The stable entry and current location contract no longer activate the retired global gate; history and scoped current-use routing remain. | Addressed by source change/guard; independently verify semantics and output. |
| AC-7 | Prior R1 mechanics remain applicable under D86, but new Candidate source/intended/actual/provenance effects and unchanged repeat are unobserved. | Explicitly BLOCKED; inspect the stop and applicability boundary. |
| AC-8 | One Candidate-epoch build and eight inspected HTML pages cover changed current prose and the five preserved compatibility fragments; no new native output is claimed. | Addressed at source epoch; later reports require affected rendering judgment. |
| AC-9 | The three contradictory current descriptions are corrected; 25 affected checks cover current/historical separation and unchanged active/reference/custom/collision cases. | Addressed by source evidence; independently verify the selected claims and guard. |
| AC-11 | Same 58 literal VALUE paths, 53M/4A/1D and `+1235/-1005 = 2240`; complete return reports missing affected native evidence honestly. | Accounting and inspectability addressed; dependent completion remains open. |

R2 changes no AC-1–4/6/10 subject. Their R1 acceptance is eligible for D86 reuse only within its recorded limits. O1–O3, original Q3, four init limitations, prior clocks/failures and the R1 positive/refusal epochs remain preserved.

**Prior-verdict header clarification.** The original header above contains the non-object SHA `de2abc53b873483fdd8deca7ca99ea8883461ff5`. The actual preserved R0 verdict commit is `de2abc53da88da3e990d83c3ec4efd0859da46ff`; this current clarification does not rewrite the historical field or create product/native work.

**R2 checkpoint:** cumulative RF §§1–5 including R2, all TS ACs, frozen HL §7 and ONB §§15–17 were read. Authority, exact returns and stopped state are explicit; no blocking onboarding question was left unresolved. Stage complete: **YES**.
