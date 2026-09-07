# Verify - "Are the claims true?"

The approved 47 literal VALUE paths were replayed exactly. The latest executor package was checked for accounting, RF/EV alignment, live trace state, field-carrier metadata, source citations and the AC-4 temporal contract. No new field, native or full-suite run was started by this review.

## Verification Log

### V1: Candidate and value-bearing accounting

- RF/EV claim: baseline `8fd8e40b734e9c439bb84721ef8bee441b9fcdd7`, field Candidate `d6d26003972f7b18fe10d492960d0cbac9f0a3e8`, prior product Candidate `64a963517eca0b0a37aca9f73801eb7fd4366a28`; 35 logical rows / 47 literal paths; 38 Git records; `+1344/-894=2238`; binary `0`.
- Actual latest correction: the read-only baseline-to-`b801daeab171270153c49f542550b1accabc19cb` replay reports 35 logical rows / 47 literal paths / 38 records; `+1382/-894=2276`; binary `0`; protected diff empty; only `docs/scripts/test_update_experience.py` is outside VALUE. This is a post-field source correction; no receiver was rerun.
- Match: VERIFIED for the replayed latest source correction, but RF/EV still declare the prior `64a963...` Candidate and its old arithmetic; this is finding F-006.

### V2: Candidate timing and provenance

- RF claim: the field campaign stayed on `d6d260...`; the prior product Candidate was `64a963...` and the latest post-field source correction is `b801dae...`.
- Actual: `b801dae...` is a source-only correction after the field campaign; its receipt-order changes affect selected VALUE paths and its test change is outside VALUE. The field aggregate and SOURCE-ADMISSION still pin `d6d260...`; no receiver was rerun after either product correction.
- Match: VERIFIED for timing/isolation; RF/EV Candidate projection requires correction (F-006).

### V3: Source-derived causal assertions

- RF claim: the final local assurance has 13 targeted tests, including causal counterexamples for stale provenance and owner-language loss.
- Actual: `python -m pytest docs/scripts/test_update_experience.py -q` independently returned `13 passed in 0.32s`. The provenance test requires the complete normative untagged-Candidate rule inside `## 0. Pin the Payload`, checks actual `tfw.installed_from` SHA provenance, rejects invented `v{VERSION}`, and rejects a stale-rule mutant even when the Candidate SHA is appended elsewhere. The owner-language test compares baseline, field Candidate and final source text.
- Match: VERIFIED.

### V4: Native campaign and field evidence

- RF claim: six frozen rows were consumed exactly once; four stopped before updater behavior; two Claude rows changed receivers; no native PASS is claimed.
- Actual: SOURCE-ADMISSION, FIELD-MANIFEST, the aggregate ledger and all six reports contain distinct native identities, prompt hash, slot order, exits, timeout flags, receiver summaries and safe final/action records. Three Codex rows stopped on `bwrap`; AFD Claude stopped on auth-layout mismatch; helpdesk/Atamat Claude report receiver changes. The current aggregate F-004 table preserves read-only source/receiver/session/config/adapter/purpose/receipt facts for those two rows, including the Atamat provenance deviation. The detailed read-only semantic disposition is recorded in V4a below: selected payload/managed-block/receipt/message facts are verified or have observed deviations, while exact changed prose semantics, one build-block comparison and owner comprehension remain unknown. No new native/full run was started in this review.
- Match: VERIFIED as bounded, nonterminal evidence.

### V4a: F-004 independent semantic disposition from existing read-only evidence

Inputs were the exact safe `REPORT.md`/`OBSERVATIONS.md` pairs, the aggregate F-004 carrier, the pinned Candidate source, the two receiver-volume comparisons already available to the review, and the exact safe native final messages. No receiver volume was rewritten, no provider was launched, and no owner choice was requested.

| TS clause / required effect | Inspected artifact or action | Result | Consequence for delivered source |
|---|---|---|---|
| AC-3 bullets 1-3: install `.tfw/README.md`, preserve designated legacy content, and record purpose evidence | 63 selected Candidate payload files were byte-exact in both read-only receiver comparisons. Helpdesk's selected preservation selector was empty; its old `.tfw/README.md` was identified as methodology-only TFW Philosophy/NS1-3, not a project-purpose designation. Atamat's old body was also full TFW Philosophy/NS1-3 with no Atamat business-purpose paragraph; its exact legacy README attachment has SHA `107c011228ffc9f6396f626ba9ade63bf476cd3992e2deca1aa7a9b0aa792f2a`. A Project North Star keyword alone was not treated as purpose evidence. | VERIFIED for selected payload/preservation handling and for not inventing a purpose designation. Exact semantic classification of other changed README bytes remains UNKNOWN. | The delivered source may retain the bounded purpose claim; it cannot claim universal purpose preservation or owner-authorized purpose selection. |
| AC-5 bullets 1-3: declared adapter surfaces, foreign-neighbor preservation, and separate capability claims | Helpdesk comparison: 11/11 Claude commands, plural Antigravity surface, legacy surface and Codex skills; `CLAUDE.md` and `AGENTS.md` managed blocks exact. Atamat comparison: its existing singular Antigravity/Claude selection is preserved; no before/after Codex managed block or skills were selected. The plural-root divergence is observed separately; managed `CLAUDE.md` block exact and outside text unchanged. | Helpdesk VERIFIED for the inspected surfaces. Atamat is VERIFIED for the installed/selected surfaces, with plural-root divergence retained as a bounded deviation; absent unselected Codex is not an automatic failure. | Keep AC-5 receiver-specific and scoped to installed/owner-selected adapters. Do not promote a universal adapter claim or convert unselected Codex absence into field failure. |
| AC-3/AC-5 configuration-preservation bullets: retain project settings and separate configured checks from framework values | Nested `build.*` blocks were extracted before/after from both read-only receivers. The exact Helpdesk `lint=make lint` and `test=make test-unit` values are equal; Atamat is byte-equal after EOL normalization. The strict known-safe-set guard passed, and the unified diff has no added/deleted substantive non-comment lines, only comment/blank changes. Neither native report shows a successful project check: Helpdesk lacks `ruff`/`pytest`; Atamat reports placeholders and a removed `build.verify` target. | VERIFIED for literal configuration preservation in both receivers. Check execution/success remains UNKNOWN and the reports' BLOCKED/placeholder statements are honest. | Do not promote project-check PASS or runtime build behavior. Retain the stated blocked/owner-next-action limitations. |
| AC-4 bullet 3 and AC-6 bullets 1-3: receipt before final rendering and outcome-led final message | Helpdesk UPDATE/BRIEFING receipt paths and hashes are reconciled; Atamat UPDATE receipt and legacy-readme attachment are reconciled. The exact safe final messages lead with outcome, list observed actions and limits, avoid owner-comprehension claims, and provide next actions. | VERIFIED for receipt existence/identity and message structure. Delivery/read/comprehension is UNKNOWN because no owner response exists. | The messages can be evaluated as bounded artifacts; they cannot establish human benefit, adoption or comprehension. |
| AC-9 bullets 1 and 3-5: eight dimensions, one bounded owner request, correction package and nonterminal limits | P: selected preservation facts verified, broader diff claims remain reported. M: source d6 and versions reconciled; Atamat `installed_from` deviation observed. C: blocked checks are disclosed rather than called PASS. A: Helpdesk reports end-to-end and Atamat reports partial completion, consistent with metadata and limitations. B: useful-now sections are present, but their semantic value is not independently measurable. L/N: explicit limitations and next actions are present. Q/owner decision sufficiency remains UNKNOWN. | Mixed: VERIFIED bounded facts, two observed deviations/unknowns, and no unsupported positive claim. | AC-8/AC-9 remain nonterminal only for the named unknowns; no second campaign is needed or authorized to fill them. |

This is a concrete disposition of F-004, not a provider rerun: the unresolved items are exact semantic meaning of changed prose, Atamat's absent declared surfaces, project-check success and owner comprehension.

### V5: AC-9 aggregate and causal package

- RF claim: the canonical field carrier maps the complete aggregate, all six reports, eight dimensions, three-report 2.2.0 baseline and one correction package.
- Actual: `evidence/FIELD-ANALYSIS.md` links the aggregate; the aggregate has six rows by eight dimensions and the exact three qualitative historical reports; `CAUSAL-AUDIT__20260908.md` covers provenance, plural/singular adapter targets and technical-vs-owner briefing; `COUNTEREXAMPLES__20260908.md` and the test supplement preserve non-native limits. Final evidence-only correction `714aadf...` states that the AC-9 aggregate/correction package is present, that only Atamat has the intentionally unadvanced `installed_from` deviation, and that no separate Atamat briefing filename is required. Codex stops are exactly three.
- Match: VERIFIED for package existence; AC-9 outcome remains nonterminal because comprehension is absent and semantic effects are not independently established.

### V6: Live control state

- RF claim: the final RF/EV package is the current release/evidence handoff.
- Actual: the latest `status.md` records `CONSUMED=6`, prior product Candidate `64a963...`, semantic effects unverified, owner comprehension missing, and nonterminal AC-6/AC-8/AC-9/AC-10 dispositions. The latest journal labels its old zero-slot material as a pre-admission snapshot and appends the current projection correction. Field state matches the manifest, SOURCE-ADMISSION and aggregate, but the latest `b801dae...` product correction is not yet projected.
- Match: VERIFIED for field state; Candidate projection remains finding F-006.

### V7: RF/EV disposition consistency

- RF claim: AC-6 is blocked/deferred while comprehension is unobserved, and the RF evidence verdict is `9/13 VERIFIED, 2 DEFERRED, 2 BLOCKED`.
- Actual: EV E6 is BLOCKED and carries the same `9/13 VERIFIED, 2 DEFERRED, 2 BLOCKED` disposition. RF and EV preserve the same nonterminal state; neither claims native PASS or owner comprehension.
- Match: VERIFIED; former finding F-001 is resolved.

### V8: Copy/parity and source checks

- RF claim: source and installed-copy parity are verified, while live Antigravity/native updater behavior is not claimed.
- Actual: the Candidate diff contains the approved source and selected copies only; EV/causal audit state the exact 11-command copy census and the Atamat divergence. The committed full-suite receipt reports `540 passed, 1 skipped`; the independent targeted update module passed. A targeted integration parity selection was attempted but produced no output for several minutes and was interrupted; no result from that attempt is promoted.
- Match: VERIFIED for the committed bounded claim; the targeted integration check is inconclusive and is not promoted as evidence.

### V-citations: historical research objects

- Claim: the iter2 research files cite the retired `.tfw/scripts/test_gen_index.py` helper.
- Actual: two direct current-checkout links still name a path that is intentionally absent. `evidence/FIELD-ANALYSIS.md` now qualifies both references as historical-object citations and gives the exact replay `git show 8e68ab37d300122ff110500ad58f354f76b6210f:.tfw/scripts/test_gen_index.py`. The current package does not represent the retired helper as a live runtime dependency.
- Match: VERIFIED as an explicit historical-object exception; former finding F-003 is resolved/qualified.

### V9: AC-4 receipt temporal contract

- TS requirement: AC-4 section 189 requires the immutable receipt after current observations and cleanup resolution/disclosure, before rendering the final user message; the receipt is not a claim that a person read or understood the message.
- Actual latest source: `.tfw/workflows/update.md` section 5 now says Step 7 resolves cleanup/disclosure and seals the receipt before Step 8; the receipt records `planned/not-yet-observed` delivery state and is not rewritten after rendering. Section 7 makes this the sole cleanup/receipt point; section 8 renders from the sealed receipt. The template carries the same planned delivery state.
- Match: VERIFIED against frozen AC-4; former finding F-005 is resolved by `b801dae...`.

### V10: latest Candidate projection

- The latest source correction is `b801daeab171270153c49f542550b1accabc19cb`, but the governing RF/EV/field carriers still name `64a963517eca0b0a37aca9f73801eb7fd4366a28` and retain its `1344/894` accounting. The source correction is reachable and the field Candidate remains unchanged, but the handoff projection is not yet coherent.
- Match: INVALID - finding F-006. Reviewer cannot rewrite RF/EV/status under Role Lock.

## Commands Executed

| # | Command | Result |
|---:|---|---|
| 1 | `git diff --name-status --find-renames=50% -z 8fd8e40... 64a9635... -- <47 selector paths>` | 38 records; expected membership and rename identities |
| 2 | `git diff --numstat --find-renames=50% -z 8fd8e40... 64a9635... -- <47 selector paths>` | `1344/894`, no binary row |
| 3 | `python -m pytest docs/scripts/test_update_experience.py -q` | `13 passed in 0.32s` |
| 4 | `git diff --check 8fd8e40... 64a9635... -- <47 selector paths>` | PASS |
| 5 | Markdown-link existence scan over task-local artifacts | 187 syntactic links found; two historical research links are current-checkout-absent and explicitly qualified as historical-object citations |
| 6 | `python -m pytest docs/scripts/test_integration.py -q -k "every_path_an_installed_adapter_copy_names_resolves or phase_e_integrated_workflows_have_exact_copy_parity"` | Interrupted after several minutes with no output; inconclusive, not promoted |
| 7 | Read-only baseline-to-`b801dae...` selector replay supplied with the latest correction | 47 literal / 38 records / 35 logical; `1382/894=2276`; binary 0; protected diff empty |

The earlier unscoped `git diff --check` also surfaced a blank-at-EOF in an unrelated historical feedback report outside the approved selector; it is not a changed Candidate/evidence path.

## Claim and Source Checks

| # | Claim / citation checked | Holds? |
|---:|---|---|
| C1 | `b801daeab171270153c49f542550b1accabc19cb` is the latest source correction; RF/EV still name prior `64a963...` | NOT COHERENT - F-006 |
| C2 | six slots, one start each, no retries | VERIFIED |
| C3 | AC-9 has all six by eight dimensions and three historical reports | VERIFIED as package shape |
| C4 | provenance correction rejects stale normative text and invented tag | VERIFIED |
| C5 | owner comprehension is observed | NOT CLAIMED; package explicitly records missing comprehension as a limitation |
| C6 | old research test citations resolve as current files | NOT CURRENT FILES; explicitly qualified and replayable as historical Git objects |

## Discrepancies Found

1. **F-004 - bounded semantic disposition remains nonterminal.** Read-only comparison verifies the selected 63-file payload, both receivers' literal build-configuration preservation, Helpdesk adapter/managed-block surfaces, Atamat Claude/legacy surfaces, Atamat README attachment, receipt identities and final-message structure. Atamat's existing singular Antigravity/Claude selection has no before/after Codex managed block/skills; AC-5 applies installed or owner-selected adapters, so this is not an automatic failure. The plural-root divergence, Atamat `installed_from` deviation, unavailable/placeholder project checks, unknown changed-prose semantics and missing owner comprehension remain bounded limits. These exact unknowns prevent AC-8/AC-9/AC-10 promotion; the missing comprehension is an explicit AC-9 limitation, not a new field gate or reason for another campaign.
2. **F-006 - latest Candidate is absent from the RF/EV projection.** The latest source correction is `b801dae...` with a changed selected VALUE accounting (`1382/894=2276`), while RF/EV and the field carrier still name prior Candidate `64a963...` and `1344/894=2238`. The field Candidate remains d6 and no field row was rerun, but the final handoff must distinguish the prior Candidate from the latest corrected source.

## Evidence Verification

| # | Evidence | Artifact exists? | Matches claim? |
|---:|---|---|---|
| E1 | `evidence/EV__TFW_20260906-190312_CRUE.md` | YES | PARTIAL; AC-6 state matches RF, but Candidate identity/accounting is prior to `b801dae...` |
| E2 | `evidence/FIELD-MANIFEST.md` | YES | YES; historical pre-freeze blocks are explicitly superseded |
| E3 | `evidence/SOURCE-ADMISSION.md` | YES | YES; exact d6 field Candidate and six admitted identities |
| E4 | `evidence/FIELD-ANALYSIS.md` | YES | YES; canonical carrier points to aggregate and historical-object replay |
| E5 | `evidence/field/AGGREGATE-FIELD-ANALYSIS.md` | YES | YES; six rows by eight dimensions and read-only F-004 facts |
| E6 | `evidence/field/CAUSAL-AUDIT__20260908.md` | YES | YES; source-to-result chains and native limits retained |
| E7 | `evidence/field/COUNTEREXAMPLES__20260908.md` | YES | YES; non-native causal/source checks and follow-up commit |
| E8 | six `evidence/field/<slot>/{REPORT,OBSERVATIONS}.md` pairs | YES | YES; identities, exits, hashes and secret-safe finals |
| E9 | `evidence/harness/PROJECT-CHECK-SET__20260908.md` and native harness records | YES | YES; controls and limits are recorded, not semantic success |

## Knowledge Citations Verified

The HL, ONB, conventions and KNOWLEDGE citations used by the package resolve and support the stated purpose, source/config/state separation, provenance, adapter boundaries, review authority and evidence limits. No field self-report is promoted as project knowledge, and no contradiction with `KNOWLEDGE.md` was found.

## Checkpoint

- [x] Full approved selector replayed; discrepancy escalation applied.
- [x] Targeted test command run; full-suite receipt independently inspected but not rerun per dispatch.
- [x] Key claims and primary artifacts checked; evidence paths tested.
- [x] RF AC dispositions compared against TS criteria.
- [x] KNOWLEDGE/PV sources and ONB citations checked.
- [x] Evidence artifact existence/content checked.

Stage complete: YES
