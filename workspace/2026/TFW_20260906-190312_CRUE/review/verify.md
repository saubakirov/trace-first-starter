# Verify - "Are the claims true?"

The approved 47 literal VALUE paths were replayed exactly. The latest executor package was checked for accounting, RF/EV alignment, live trace state, field-carrier metadata, source citations and the AC-4 temporal contract. No new field, native or full-suite run was started by this review.

## Verification Log

### V1: Candidate and value-bearing accounting

- RF claim: baseline `8fd8e40b734e9c439bb84721ef8bee441b9fcdd7`, field Candidate `d6d26003972f7b18fe10d492960d0cbac9f0a3e8`, product Candidate `64a963517eca0b0a37aca9f73801eb7fd4366a28`; 35 logical rows / 47 literal paths; 38 Git records; `+1344/-894=2238`; binary `0`.
- Actual: replay with `git diff --name-status --find-renames=50% -z` and `--numstat -z` returned 47 literal selector members, 38 raw records, 35 logical rows, D3/R100x7/M22/R097x1/A4/R098x1, 1344 additions and 894 deletions, with no binary row. The exact final product SHA is 40 hexadecimal characters and resolves.
- Match: VERIFIED.

### V2: Candidate timing and provenance

- RF claim: the field campaign stayed on `d6d260...`; post-field VALUE corrections produced product Candidate `64a963...`; assurance/evidence commits are outside the 47-path VALUE selector.
- Actual: Candidate `64a963...` is descended from `4499e8c...` and changes only the four expected VALUE files in its own commit; assurance/evidence commits through final producer correction `714aadf...` have no selected VALUE changes after it. The field aggregate and SOURCE-ADMISSION pin `d6d260...`; no receiver was rerun after the post-field corrections.
- Match: VERIFIED.

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
| AC-3 bullets 1-3: install `.tfw/README.md`, preserve designated legacy content, and record purpose evidence | 63 selected Candidate payload files were byte-exact in both read-only receiver comparisons. Helpdesk's selected preservation selector was empty; its old `.tfw/README.md` was identified as methodology-only TFW Philosophy/NS1-3, not a project-purpose designation. Atamat's legacy README attachment was read and its SHA is `107c011228ffc9f6396f626ba9ade63bf476cd3992e2deca1aa7a9b0aa792f2a`. | VERIFIED for selected payload/preservation handling and for not inventing a Helpdesk purpose designation. Exact semantic purpose/authority classification remains UNKNOWN for changed README bytes. | The delivered source may retain the current bounded purpose claim; it cannot claim universal purpose preservation or owner-authorized purpose selection. |
| AC-5 bullets 1-3: declared adapter surfaces, foreign-neighbor preservation, and separate capability claims | Helpdesk comparison: 11/11 Claude commands, plural Antigravity surface, legacy surface and Codex skills; `CLAUDE.md` and `AGENTS.md` managed blocks exact. Atamat comparison: Claude and legacy surfaces exact; plural/Codex surfaces absent and no Codex marker present; managed `CLAUDE.md` block exact and outside text unchanged. | Helpdesk VERIFIED for the inspected surfaces. Atamat has an OBSERVED DEVIATION from the full declared topology; no general adapter PASS is justified. | Keep AC-5 receiver-specific: Helpdesk supports the inspected surface claim; Atamat remains limited to Claude/legacy preservation and requires an owner/source disposition for absent plural/Codex surfaces. |
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
- Actual: the latest `status.md` records `CONSUMED=6`, product Candidate `64a963...`, semantic effects unverified, owner comprehension missing, and nonterminal AC-6/AC-8/AC-9/AC-10 dispositions. The latest journal labels its old zero-slot material as a pre-admission snapshot and appends the current projection correction. This matches the current manifest, SOURCE-ADMISSION and aggregate state.
- Match: VERIFIED; former finding F-002 is resolved.

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
- Actual Candidate source: `.tfw/workflows/update.md` section 5 says not to seal before the final-message outcome and says to write at the end of Step 8; section 8 says to write the receipt last and requires recording whether the final message was delivered. The template repeats a `Final message delivered to the user` field. This places receipt creation after, or at least depends on, post-render delivery state, contrary to the frozen pre-render receipt gate.
- Match: INVALID - finding F-005. This is a real source/TS temporal collision, not a receipt evidence gap.

## Commands Executed

| # | Command | Result |
|---:|---|---|
| 1 | `git diff --name-status --find-renames=50% -z 8fd8e40... 64a9635... -- <47 selector paths>` | 38 records; expected membership and rename identities |
| 2 | `git diff --numstat --find-renames=50% -z 8fd8e40... 64a9635... -- <47 selector paths>` | `1344/894`, no binary row |
| 3 | `python -m pytest docs/scripts/test_update_experience.py -q` | `13 passed in 0.32s` |
| 4 | `git diff --check 8fd8e40... 64a9635... -- <47 selector paths>` | PASS |
| 5 | Markdown-link existence scan over task-local artifacts | 187 syntactic links found; two historical research links are current-checkout-absent and explicitly qualified as historical-object citations |
| 6 | `python -m pytest docs/scripts/test_integration.py -q -k "every_path_an_installed_adapter_copy_names_resolves or phase_e_integrated_workflows_have_exact_copy_parity"` | Interrupted after several minutes with no output; inconclusive, not promoted |

The earlier unscoped `git diff --check` also surfaced a blank-at-EOF in an unrelated historical feedback report outside the approved selector; it is not a changed Candidate/evidence path.

## Claim and Source Checks

| # | Claim / citation checked | Holds? |
|---:|---|---|
| C1 | `64a963517eca0b0a37aca9f73801eb7fd4366a28` is the final product Candidate | VERIFIED |
| C2 | six slots, one start each, no retries | VERIFIED |
| C3 | AC-9 has all six by eight dimensions and three historical reports | VERIFIED as package shape |
| C4 | provenance correction rejects stale normative text and invented tag | VERIFIED |
| C5 | owner comprehension is observed | NOT CLAIMED; package explicitly records missing comprehension as a limitation |
| C6 | old research test citations resolve as current files | NOT CURRENT FILES; explicitly qualified and replayable as historical Git objects |

## Discrepancies Found

1. **F-004 - bounded semantic disposition remains nonterminal.** Read-only comparison verifies the selected 63-file payload, both receivers' literal build-configuration preservation, Helpdesk adapter/managed-block surfaces, Atamat Claude/legacy surfaces, Atamat README attachment, receipt identities and final-message structure. It also records the Atamat absent plural/Codex surfaces, Atamat `installed_from` deviation, unavailable/placeholder project checks, unknown changed-prose semantics and missing owner comprehension. These exact unknowns prevent AC-8/AC-9/AC-10 promotion; the missing comprehension is an explicit AC-9 limitation, not a new field gate or reason for another campaign.
2. **F-005 - receipt timing contradicts TS AC-4.** Candidate `update.md` section 5/section 8 and `update_receipt.md` couple immutable receipt creation to the final-message delivery outcome and place it last, while frozen TS AC-4 requires the receipt before final-message rendering. Without correction, an interrupted run can lack the mandated recovery record before rendering, or an immutable receipt must be rewritten to capture delivery.

## Evidence Verification

| # | Evidence | Artifact exists? | Matches claim? |
|---:|---|---|---|
| E1 | `evidence/EV__TFW_20260906-190312_CRUE.md` | YES | YES; AC-6/count state now matches RF |
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
