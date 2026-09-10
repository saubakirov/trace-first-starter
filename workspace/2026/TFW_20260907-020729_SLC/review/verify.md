# Verify — SLC Phase A

RF: [actual return](../RF__TFW_20260907-020729_SLC.md). TS: [exact approved specification](../TS__TFW_20260907-020729_SLC.md). Authority and actual unit are resolved in [map](map.md).

Configured minimum: `tfw.review.min_verify_ratio = 0.42`; RF names 24 VALUE plus six ASSURANCE files, so the minimum is ceil(30 × 0.42) = 13. Actual verification is **30/30**, including all eight exact installed copies. The disclosed procedural deviations were examined at full coverage; none silently receives a clean procedural PASS. TRACE/evidence inventories were checked separately and do not alter the selector.

## Verification Log

| Ref | Actual files inspected | Claim and actual result |
|---|---|---|
| V1 | `.tfw/templates/project_config.yaml`, `.tfw/project_config.yaml`, `.tfw/quickstart.md`, `.tfw/workflows/init.md` | Clean acquisition excludes live upstream config/state/receipts/history; template uses workspace and no history key. Existing configured/history-only input routes before full discovery, while Full Setup preserves the selected paths. Native NF-1/2/4 cover the approved bounded effects; later full init is source-checked, not claimed native completion. |
| V2 | `tools/tfw_state.py`, `docs/scripts/gen_docs.py`, `.tfw/compilable_contract.md` | Existing active API and scalar choice remain. The optional reference union validates history, deduplicates resolved paths and feeds the actual collision-aware walker. Globs, source/output mapping, hidden landings and artifact/bare-ID resolution use it; ordinary discovery does not. Per-page lazy observation avoids a persistent stale cache. Inspected surrounding walker, mapping and resolver bodies, not just diff lines. |
| V3 | `.tfw/conventions.md`, `.tfw/workflows/resume.md`, `.tfw/workflows/knowledge.md` | Operations are explicitly separated. Historical guard precedes phase/current closing/repair. Knowledge returns incomplete migration to the authorized updater before ordinary arithmetic; its normal digest and state-last algorithm is unchanged. No new status vocabulary or current portfolio. |
| V4 | `.tfw/workflows/update.md`, `.tfw/migrations/3.3.0.md` | One guide owns seven cuts and six refusal classes; missing/colliding preservation are variants of one class. Prior authority, exact membership and old/intended fields precede writes; compatible readers precede narrowing, state precedes final config, later unaffected work survives. Equal-version entry resolves the guide before already-current; exact single/custom and keep-active choices survive. No wholesale rollback or prefix pruning. |
| V5 | `.tfw/knowledge_state.yaml`, `tasks/README.md` | Independently replayed Git before/after YAML: 53 exact historical pairs removed, 11 retained, all other values equal. All historical task files and KNOWLEDGE/topics are byte-identical. README changes only container explanation and historical chronology. No inferred DONE/REJECTED. |
| V6 | `.tfw/VERSION`, `.tfw/CHANGELOG.md` | Coherent prepared 3.3.0 with both configs; guide directly routes 3.2.0 and delegates earlier ordered routes to unchanged 3.2.0/predecessors. Required briefing/manifest/RELEASE inputs and all earlier guides are unchanged. This is prepared composition, not a tag or publication. |
| V7 | `.agents/workflows/tfw-{init,knowledge,resume,update}.md`, `.claude/commands/tfw-{init,knowledge,resume,update}.md` — eight literal files | Read canonical changes and compared every whole copy byte-for-byte. All eight equal their canonical source. Native NF-4 additionally verifies the distinct installed Codex thin skill surface and preserved foreign neighbors. |
| V8 | `tools/tests/test_tfw_state.py`, `docs/scripts/test_gen_docs.py`, `docs/scripts/test_integration.py` | Real active/reference readers, malformed history, whole-ID collision, mapping/resolver/landing functions and generated-output consumer tests. Existing legacy fixtures now state their deliberate tasks choice. Integration retains one shared real build and active-only current diagnostics. |
| V9 | `docs/scripts/test_update_experience.py`, `docs/scripts/test_runtime_context.py`, `docs/scripts/test_repository_contracts.py` | The recovery interpreter is explicitly a disposable model; seven prepared cuts and seven refusal parameters cover six classes. Custom choices, read edges, release/copy parity and historical/live PTTC epochs remain. No copied model is offered as native proof. |

The complete Baseline→Candidate inventory also contains Coordinator-owned planning/control changes, Executor ONB/controls, self-host preservation and check attachments. Their semantic roles are TRACE; no hidden necessary VALUE path, rename, binary VALUE file, unrelated product edit or protected selector change was found. Candidate→actual RF→prepared review merge contains only this task's TRACE paths.

## Commands Executed and evidence applicability

| Check | Independent result |
|---|---|
| Execute the PowerShell block read from the TS at approval `40b2dd5666cf608a9f1282567550de6a6b62fadd`, with exact Candidate and fresh `review/accounting` directory | The saved Executor script is text-identical to the approved block. Both new NUL-delimited outputs are byte-identical to Executor attachments. |
| Parse complete native Git name-status/numstat records | **24 logical files, 424 additions, 167 deletions, 591 touched text LOC, zero binary/non-text N/A, zero renames**. Raw [names](accounting/slc-05c6fcdfe6a1c1b4e9615f0390d094ee1b1fb5e8-name-status.z), [numstat](accounting/slc-05c6fcdfe6a1c1b4e9615f0390d094ee1b1fb5e8-numstat.z). |
| Git object/ancestry, complete inventory and native Executor tool history | Exact TS blob unchanged; approval/C1/Candidate/root dispatch reachable. First product commit is Candidate. C1 was ruled at 22:18:12; actual first product patch is 22:20:27. Native pre-commit status/cached-set checks, literal path arrays and commit `--only --` were observed for product and return commits. The default 47f4a5 merge subject remains the disclosed deviation. |
| Compare all 121 inputs in `08-full.receipt.json` to current files and all 30 VALUE/ASSURANCE files to Candidate Git blobs | **121/121 and 30/30 equal**, no mismatch. Read the capture helper: it calls actual `pytest.main`, observes `subprocess.run` without replacing results and records the real MkDocs subprocess. |
| Read successful full check and actual retained HTML | Original **581 passed, 1 skipped**, exit 0; nested MkDocs exit 0, 113.64 seconds. Four HTML hashes still match; all **198** recorded relative landing links exist (11 + 151 + 1 + 35). No corpus-wide clean-link claim. |
| Self-host Git/YAML/membership replay | **53 historical IDs, 42 stateless, 53 removed pairs, 11 unaffected pairs**. Whole historical trees, knowledge and all unrelated state values equal. Before-image content address matches its directory; both decoded originals equal Baseline Git bytes; guide hash and approval refs match. |
| Native archive/source/snapshot/receiver read-only checks | Results below. Fresh `git archive Candidate .tfw` equals the clean native source archive SHA256 `0d2c52981cd4b027ad6ae4b2b874d44b2f26335c821cd05262b2aacbbf957e58`. |
| Native before/final YAML and protected-file comparisons | Each of eleven cases has the expected active/history fields. Only NF-6 and NF-9 remove the exact SLCFX-1 pair; all other state values survive. NF-8 preserves later `c*64`, NF-10 preserves conflicting `d*64`. Original purpose/profile/task bytes remain. All six repeat and two historical-read manifest pairs are identical before append-only repeat receipts. |
| Artifact reference checks | RF 19, ONB 20 and EV 53 local Markdown targets all resolve. PV row/target checks below. |

Accounting source is immutable Baseline `affd9033abf94e9b9a9e27114f3bfbb16066438a` and Candidate `05c6fcdfe6a1c1b4e9615f0390d094ee1b1fb5e8` / tree `c1c9f62fc31634f11227a7b9c4789d5c8f118f92`. Immutable owner plan is **24/+393−163=556**, not 591 or the prospective ~700 forecast. Actual growth is 35 LOC; 24/591 is below both owner boundaries 48/1112 and soft triggers 50/5000. C1 `cc94d1241c3b31c33adbe6920121e537e4c25718` is prospective necessary growth in the same 24 paths, with unchanged invariants. No trigger requires decomposition and no deferred authority is used. Raw names SHA256 `1b9edafa090f7265e4461fbba7ae23367f17ad54156e1c1a6c426b3a5568bfc7`; numstat SHA256 `05092624169c98caa4758c5d86311c497615dd351874b0162b40613c4dde2e6b`.

Under D86 no new full suite/build/native cycle was necessary: the actual tested product/test/config inputs, retained outputs, oracles and same-host assumptions remain applicable. The new RF/EV/review/closure prose was absent from that build and is explicitly excluded from its output acceptance. Later material closure or release-output changes still require the affected check and this same independent Reviewer. Historical failed 02-source, failed 03-collection and interrupted 06-full remain non-PASS epochs. A Reviewer diagnostic initially used Windows' default text decoder and failed before native comparison; rerunning read-only with Python UTF-8 completed the comparisons above. It did not change receiver files or evidence.

## Claim & Source Checks

| Ref | Primary source checked | Conclusion |
|---|---|---|
| C1 | Git Baseline/Candidate blobs plus preserved exact config/state originals and historical directory IDs | The 53/11 claim is established independently, without trusting the RF or pruning an ID prefix. |
| C2 | Actual same-source compiler HTML and its real relative targets | The four required output examples are observable and retain their exact hashes/links. Original suite/build source hashes remain applicable; historical diagnostics are not suppressed. |
| C3 | Original Coordinator prepared/observed snapshots, content-addressed before-images and corrected sealed attempts | Migration/repeat/refusal claims match actual state changes. Source, authority, prepared input, operation and outcome are distinct. NF-3 original dirty-source attempt cannot support clean-entry PASS. |
| C4 | Native Executor task tool calls and Git path history | Candidate is the first tested product commit, before EV/RF; C1 precedes product patches. Exact-path staging and sole producer are recoverable. `47f4a5`'s default subject is not concealed by later attribution. |

Native and Executor task addresses are evidence of separate acting units, not authentication or provider reliability. Local native Executor trajectory inspected at `C:/Users/c0rpa/.codex/sessions/2026/09/09/rollout-2026-09-09T14-34-41-01a08585-01f5-7101-b4a7-5155aaead0da.jsonl`, specifically actual tool calls at 17:20:27, 18:00:52–18:01:42, 18:04:16 and 19:25:06–19:25:33 UTC; no reasoning trace is required or reproduced.

## Independent native integrity audit

Recomputed from archive members, original E:/TEMP files, every snapshot tree and current receiver, without receiver writes. Historical NF-3 alias compared against both retained copies.

```json
{
  "files": 9394,
  "directories": 4397,
  "bytes": 84881882,
  "snapshots": 54,
  "receivers": 11,
  "snapshot_receiver_comparisons": 8865,
  "mismatches": 0,
  "archive_sha256": "2b96acbdd5fd814477bd330c8642a1908af1d07a5beb01854bb30b441aa513a5",
  "manifest_sha256": "7a7bf1b4d988857878d52b1ceb064ffd507f57c282de5c0ce271d434bddeeec5"
}
```

## Evidence Verification

| EV row | Actual evidence and result | Applicability limit |
|---|---|---|
| E1 / AC-1 | NF-1 acquired 71 clean framework files and created real WDP status/event in workspace; independent prepared NF-2 created FTP/HL_DRAFT with four new files | NF-1 profile/directory ordering deviated; neither case claims complete research/init |
| E2 / AC-2 | Corrected NF-3 3.2.0 input→Candidate keeps tasks and all state; repeat unchanged. NF-4 history-only repair installs eleven selected Codex skills and one managed block, preserves foreign content | Custom combinations are real deterministic consumer tests, not universal native evidence |
| E3 / AC-3 | NF-5 absent/empty, NF-6 history and NF-7 observed grouped question before scripted keep-active reply; repeat retains decisions | Qualified NF-5 preparation and early preservation retain their actual provenance; synthetic reply is not a new human decision |
| E4 / AC-4 | Actual compiler/output checks plus NF-4/NF-6 zero-write historical-read snapshots | Missing historical state remains absent; no continuation/full-corpus-link certification |
| E5 / AC-5 | Seven model cuts/six refusal classes remain models. Native NF-6 observes state before config; NF-8/9 recover expected prepared cuts; NF-10 preserves its conflicting digest and refuses | Prepared cuts are not crashes. NF-10 adds 74 diagnostic staging files before refusal, so the whole attempt is not zero-write or completed update |
| E6 / AC-6 | Independent exact self-host reconciliation and before-image/Git verification, V5/C1 | No external receiver repository was mutated |
| E7 / AC-7 | Complete 30-file shipped/test inventory, explicit clean acquisition and final receiver manifests | Python is upstream assurance/diagnostic tooling, not a shipped Full prerequisite; packaging is finite evidence |
| E8 / AC-8 | Actual 3.3.0 composition and unchanged predecessor inputs; NF-6 upgrade and NF-9 equal-version recovery/repeat | Final release checks/tag/publication remain separate actual effects |
| E9 / AC-9 | PTTC closing/control/session ranges and handoff/review/docs are unchanged; changed guards and current/historical test epochs inspected | PTTC native evidence is dependency evidence only |
| E-accounting / AC-10 | Independently replayed exact 24/591 accounting with immutable 24/556 denominator and prospective C1 | No late VALUE, missing authority or alternative selector |
| E10 / AC-10 | Actual RF, EV, Candidate and this independent review exist at their respective stages | Canonical proposals, real docs/knowledge effects, final affected judgment, selected landing and closure remain subsequent Coordinator work; no native family is deferred |

All **11/11 EV rows exist**. Ten establish their bounded completed claims; E10 accurately describes the required subsequent independent review/closing stage. Source observations support only their actual inputs/output/oracles/environment. Original attempts and transport aliases remain inspectable; archive integrity alone is not substituted for semantic review.

## Knowledge Citations Verified

Independent P0/P1 reads of designated README sections were separate semantic checks. P2 philosophy was read in full (F1–F47), P3 Architecture Map/Decisions in full (D1–D86), P4 HL/HL Contract, Design Rules and Anti-patterns in full; cited Where tasks live/Discovery/Closing were additionally read. Relevant P5–P7 items were selected below. Historical D47/D68/D70 blanket wording is qualified by current source/3.3.0 successors and D85/D86, not silently promoted over current authority.

| HL / ONB row | Priority and exact item | Resolution, existence, meaning and relevance |
|---|---|---|
| 1 / 1 | P0 NS1 | Pass: purposeful, inspectable human-governed continuity requires original history and explicit authority |
| 2 / 2 | P0 NS2 principle 2; NS3 non-goals | Pass: simplest complete form, no documentation bureaucracy or invented archive mechanism |
| 3 / 3 | P1 Structural Enforcement; Success Criteria 1/4 | Pass independently of P0: reader behavior, native observation and resumable usable result support the claimed practice |
| 4 / 4 | P2 F22/F23/F43/F45 | Pass: clean template instantiation, state contamination, necessary architectural job and subtraction |
| 5 / 5 | P3 D47/D68/D69 | Pass: state separation, task-local truth/stable paths and whole-ID semantics; historical single-setting wording is the explicit migration subject |
| 6 / 6 | P3 D73/D82/D85 | Pass: exact digest selection, no Full runtime and existing pinned update/preservation/receipt route |
| 7 / 7 | P4 HL Contract, Design Rules, Anti-patterns | Pass: exact approval/role boundaries and point-of-use rules; historical prose ceiling is superseded by D82 |
| 8 / 8 | P4 Where tasks live, Discovery | Pass: operation-specific participation preserves paths and does not infer state |
| 9 / 9 | P5 convention F19/F23 | Pass: consistent lower-case YAML keys, English semantic artifacts and Russian communication |
| 10 / 10 | P6 process F6/F22 | Pass: bounded one-phase scope and no tautological additional mechanism |
| 11 / 11 | P7 stakeholder F6 | Pass: interruption frequency never supplies authority; settled cases need no repeated question |
| 12 / 12 | P3 D86 and Closing and record recovery | Pass: actual Coordinator effects/landing precede DONE; applicable evidence survives unchanged inputs |
| additional Coordinator prose / 13 | P3 D76/D77 | Pass: fixed accounting and prospective growth, isolated units, exact commits and reachable Candidate |

Totals: **25 citation rows** (12 HL + 13 ONB), all 25 semantically verified; **33 linked targets** (20 HL + 13 ONB) resolve, zero missing, invented or irrelevant items. ONB row 13 explicitly extends the already-cited Architecture Decisions source. No citation discrepancy was found. Knowledge capture must record the accepted active/history successor at the later docs gate; that future effect is not pre-certified.

## Discrepancies and observation assessment

RF O1–O6 are real preserved procedural/evidence limitations. Their consequences and proposed canonical dispositions belong once in REVIEW §5. No current Candidate breach of an approved AC or frozen HL claim was found. The first NF-3 entry remains invalid; the corrected real upgrade/repeat pays the missing clean-entry evidence without relabeling history. NF-5/6 earlier preservation remains earlier provenance, with exact input/source revalidation before affected application.

RF's explicit `No diagrams` was challenged: frozen HL §3.1/3.2 already visualizes the operation split, and the shipped guide's disposition/cut tables plus observed intermediate snapshots explain every changed state edge. No missing decision, transition or acceptance claim requires another RF diagram. This is a finding of no additional visual debt, not exemption from the inspection.

## Checkpoint

- [x] All 30 product/test files inspected; eight copies checked as whole bytes; full TRACE inventory classified.
- [x] Evidence applicability independently established; affected native/config/output/identity checks completed without gratuitous full suite repetition.
- [x] Primary counts, key claims, artifact refs and evidence transport independently checked.
- [x] Every RF AC assertion evaluated; later real closure is explicitly limited.
- [x] P0–P4 independently scanned and P5–P7 selected; all HL/ONB citations verified semantically.
- [x] All 11 EV rows examined; no missing native family, six repeats and two historical reads verified.
- [x] KNOWLEDGE contradictions/successor obligations identified above; RF empty Fact Candidates challenged against actual human input, which repeats already-recorded authority and goals.

Stage complete: YES.

## Bounded final-output verification — 2026-09-10T09:16:18+05:00

This is the existing independent Reviewer's D86 continuation, not a restart of the original Verify stage. Governing dispatch/input tree: `470e7b56d9303a8c7374ae55d180968fd417aba4`, nonce `slc-output-materiality`; actual observed build input: **`3366ae87da0e73f4cf54a4c109ff0479e3bd33c7`**. Same actual unit, parent, authority and role as Map/REVIEW. No authored file changed during the initial assessment. The following record is authorized by the root's direct request to persist its cited input before remedy.

### Actual evidence identity

Evidence producer is native Coordinator `01a08584-8bcf-7481-97a0-bd27d04dbb55`, principal robert. Immutable first-epoch commit **`fdd5879021a1807e72069b97270c000eeb6fc06a`**, transport-only commit **`d7aad979e61c68e31081402e693d62ef95fa1413`**. Within those objects, the owning directory is `workspace/2026/TFW_20260907-020729_SLC/evidence/final-release/`; read `COORDINATOR-FINAL-RELEASE.md`, `opened-output.json`, `opened-html.tar.xz`, `transport.json`, and `raw-capture.tar.xz`. The original physical evidence was also read at `C:/Users/c0rpa/.codex/worktrees/4907/steps-framework/` under the same task path. These are exact Git-object/source locators, not a claim that this review commit imports the sibling evidence files.

- Independently verified the opened-HTML archive SHA256 **`fe093dfe34403a43aa344b7bf3d912636cb0def1f7d01f56e3caeedf1296bef1`** and all **12** member hashes against the recorded outputs. Parsed actual archived anchors with the standard-library HTML parser; all **121** recorded negative href observations occur in those actual files. This count includes old KNOWLEDGE/legacy diagnostics and does not classify them all as new defects.
- Independently verified raw-capture SHA256 **`82da2e8059cec8418fbea0bc3b7765ce9c168df1bdafbb3584873d1befdc1d77`**, all **20** original member hashes/sizes and the corresponding fdd5879 Git blobs. Exactly **12** differ only through CRLF→LF normalization. Original output JSON SHA256 is `cefb62e0d0b241b517f501ca960b7ebbe9be485ace4263450b4a8c1fb94514d1`; its normalized Git blob SHA256 is `a358c5f7fede96c6f78e3451d754587b818bd54915d6cbf3d48f189f3fbe1b34`. Neither identity substitutes for the other.
- Original retained full stdout confirms **581 passed, 1 skipped in 577.30 s**; receipt exit is **0**, capture duration **577.887212 s**. Coordinator reports the actual single nested MkDocs build at **127.75 s / exit 0** and 2,209 unchanged tracked inputs. This continuation does not repeat that full input census or the suite; a successful build does not prove the failing links below.

### O7: current compiled parent-HL navigation

All paths in the following table are relative to the archived `site/tasks/2026/TFW_20260907-020729_SLC/`. Each row was independently located in the actual HTML. The output JSON reports a missing target for its nested HL href.

| Case | HTML path | One-based line |
|---|---|---|
| RF | `RF__TFW_20260907-020729_SLC/index.html` | 2767 |
| REVIEW | `REVIEW__TFW_20260907-020729_SLC/index.html` | 2740 |
| Current status | `status/index.html` | 2618 |
| RF→KNW event | `journal/20260910-005516__transition__98d5/index.html` | 2624 |
| Final dispatch | `journal/20260910-010809__dispatch__34e7/index.html` | 2622 |
| Current TS | `TS__TFW_20260907-020729_SLC/index.html` | 3016 |

RF source line 6, REVIEW line 14 and TS line 6 have ordinary local parent-HL links. Status line 8 and the RF→KNW event line 14 carry the existing valid authority/ref. The RF output destination is literally:

```text
[HL-TFW_20260907-020729_SLC]([HL-TFW_20260907-020729_SLC](HL-[TFW_20260907-020729_SLC](HL-TFW_20260907-020729_SLC.md).md).md).md
```

The HL file and its compiled page exist. The task landing supplies working HL/RF/REVIEW/EV alternatives, and source authority/refs are valid; no authority loss is inferred. Nevertheless, this explicit compiled RF/REVIEW→HL transition is not usable.

**Predecessor comparison, read-only:** loaded the exact Baseline `affd9033abf94e9b9a9e27114f3bfbb16066438a` and Candidate `05c6fcdfe6a1c1b4e9615f0390d094ee1b1fb5e8` `gen_docs.py` definitions into memory, with only the existing test-style no-build `mkdocs_gen_files` import stub. Called each actual `resolve_references` on the same real current SLC root, explicit parent-HL link, supported plain `HL {ID}`, authority field, inline filename and bare ID. Explicit/plain HL and carrier forms nest under both versions; bare ID produces one clean link. No receiver fixture, generated page or source was written. The old resolver also retains its old workspace URL behavior; this diagnostic does not claim a full old-build reproduction or an introduced SLC regression.

Inspection explains the observation: sequential artifact, dash-HL and bare-ID substitutions can match tokens in the URL just created or in an existing destination. Changing the author to the supported plain HL form does not cure the failure. TS AC-4 requires actual artifact resolution and current-page URL/relative-link verification; AC-8/10 require this affected final acceptance. Frozen HL's original-path/documentation claim and the compilable contract's RF→HL example identify the concrete served route. Its inherited origin does not establish that result. Proposed remedy/completion and existing owner are stated once in REVIEW §4; this verification performs no fix.

### O8: raw evidence remains a repository output

For every selected missing raw target in SLC RF/EV/REVIEW, resolved the original source-relative path and compared its whole bytes to the actual `3366ae87` Git object: **12 RF + 50 EV + 4 REVIEW = 66**, all exist and equal. These are JSON, log/text, archive, script and raw accounting attachments. The predecessor and Candidate compilable manifests both declare Markdown-only inputs and neither includes raw-evidence publication. The existing link rewrite explicitly skips non-Markdown destinations. The selected legacy phase RF likewise has an unpublished `measurement_log.txt`.

This proves repository evidence linkage, not a functioning website download. A compiled-site-only reader cannot retrieve these raw files from the emitted relative hrefs. AC-10's real RF evidence is present and inspectable in the repository/portable package; no manifest or approved AC promises that this release will publish those attachments. Proposed **not material — not owed** is strictly for adding that publication/copy feature, with the site-only limitation retained. It neither waives O7 nor asserts all website links pass.

### Remaining output and execution boundaries

The two new KNOWLEDGE guide hrefs on `3366ae87` are actual negative docs-effect evidence. Root's `1938a7234ddef3a3f2a20603de03f5e041b3cf90` replaces them with code-form source paths; corrected generated output and any interruption/retry remain a later Coordinator epoch. No future output or remedy is pre-approved here. O7/O8 remain proposals to the root; first approval and O1–O6 rulings are preserved. Final acceptance is withheld for O7 until actual remedy and appropriate independent verification.

One initial evidence read emitted an oversized JSON response rather than the requested filter; all subsequent inspection selected metadata/negative links. An unavailable optional HTML parser import failed after the resolver diagnostic; the standard-library parser completed the HTML checks. A heading lookup containing a shell-mangled symbol failed without writes and was repeated with the unique unchanged heading text. None of these diagnostic failures changed evidence, source or receiver state, and none is presented as a passing check.
