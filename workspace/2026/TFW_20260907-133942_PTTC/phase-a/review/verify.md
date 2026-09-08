# Verify — Independent Phase A audit

Min verify ratio: `tfw.review.min_verify_ratio = 0.42`. RF names 4 VALUE files and 9 unique Executor TRACE files (ONB, RF, EV, ledger, variants, archive, state and two events); the complete implementation/RF package is 13 paths. Minimum is ceil(13 × 0.42) = 6. All four VALUE files and all nine TRACE files were inspected; supplied authority/intake journals were also read. No sampled exclusion is used.

## Verification Log

### V1 — Source/output split and retained protection

Independent AST inspection starts from Baseline `099d37d21ddfada2ca72c576055f0a26029c7205`, not the Executor inventory. It finds 156 baseline function bodies, 149 effective names and seven shadowed definitions at exactly the TS ranges. Candidate has 150 functions/helpers: 15 output tests plus the original build fixture, and 90 pure tests plus helpers. All 16 output functions, including fixture decorator/body, are unchanged. Of 145 surviving effective baseline names, 142 have unchanged ASTs, including decorators; the only changed bodies are the board guard and the two disclosed knowledge predicates. Every shared global value is unchanged. The three added globals are the real K2 Candidate/approval/capture anchors.

The two removed effective aliases call the two retained substantive predicates named by AC-2. The two removed helpers have no remaining name loads; their consumers were shadowed bodies. No additional active protection was silently deleted. Pure imports are hashlib/re/shutil/subprocess/sys/Path/pytest/yaml; local imports are yaml and source-reader tfw_state. Module-level work is literal/regex/path construction, with no generator/build-backed import. Inspection of function/helper dependencies, output-related literals and actual process records identifies source/Git/temp inputs rather than generated-site reads. Historical assurance path literals remain historical selectors.

The board guard changes only its self-excluded filename to `Path(__file__).name`; it still scans the docs Python population, exempts the migration parser, and now also scans the former integration file. No blanket generator exclusion is added. Candidate `test_runtime_context.py` changes exactly R10/R14 to the new module; container behavior, historical URLs and the output-backed landing predicate remain unchanged. `gen_docs.py`, `tfw_state.py`, `tools/tests/`, product knowledge, both project configurations and protected history are outside the VALUE diff.

Primary independent receipt: [source/evidence audit](evidence/independent-source-evidence-audit.json), [name-status](evidence/review-accounting-name-status.nul), [numstat](evidence/review-accounting-numstat.nul).

### V2 — Knowledge protection and exact semantic judgment (E3/E4)

The new helper checks selected row cardinality, B–E-or-later phase lineage, required source paths at immutable historical epochs, and actual required result/approval commits. The historical regression compares whole rows only at the finite pre/post-K2 inputs. Current prose is not compared with historical whole rows; executable protection and semantic judgment have separate stated jobs. The structural adverse group retains missing/duplicate decisions/artifacts, phase mismatch, fabricated Candidate, wrong approval and wrong TS source. Those controls are included in the independent six-selection run.

This judgment concerns the exact archive inputs, not AC4's hypothetical rationale-only case:

| Input / SHA-256 | Independent semantic decision and real grounds |
|---|---|
| `knowledge-wording.md` / `15be6f4f984118c4ce3d6280ba1c2df95dda7415ef45cc8b94bab9eae3ec652c` | ACCEPT as a bounded faithful explanation. D82 retains ordinary-Full/no-runtime/cache/prose-bound and upstream-tooling boundaries, direct hidden landings, and Assisted/history protection. The unchanged cited RTBO REVIEW describes these same changes; omitted implementation metrics are not normative changes. D83 retains the post-freeze owner choice, stable principal/distinct units, protected mandate, per-unit activation and exact root navigation; actual A7 plus rev3 §§2/3/AC-7 support it. D84 retains optional resolved durable-principal attribution, omission when unresolved and no identity/title-derived authority; the actual Phase E cumulative RF §§1–3 and final REVIEW rev2 V-sweep attest the exact canonical sentence, which was independently read in the current workflow. This rewrite does not create approval or permission, and unchanged cited sources remain authoritative. |
| `knowledge-approved-successor-synthetic.md` / `024b0c2aa0f8fc4d49a60b9f416e0797fb1928090bc635007874906a91cd6c7c` | ACCEPT only as the labeled illustration of an existing owner act. Initial TS at `b755de9128f2b0442615a4ca8b787761f937bbcd` AC-1/2 required the old pre-freeze role-table model. A7 at `2386bfb0994f6e0a1aed7b734e345cdb2a540ae1`, master §12 row A7, explicitly supersedes it with one selected principal and distinct units. Recorded REVIEW rev2 at `18d54060da8796ddca7d648365cbfeb18f60690b` §8 preserves old history and routes the A7 correction to the revised TS. Rev3 at `73d711808a6b6fe1b1e15589e7c3c9d479a9e8a5` §§2/3 and AC-7 carries that model and the exact root-title refinement. All four attached source files byte-match `git show` at those real refs. D999 is explicitly a synthetic unrelated row, not a live decision or new owner approval. |
| `knowledge-authority-distortion-for-independent-review.md` / `fe8a4f10c67796dbbaf04609fd66a3e4e606468df10a83e721056d9667e47a06` | REJECT the input: it changes writer into a working unit whose title grants amendment authority. That contradicts D84's durable acting-principal subject, actual Phase E optional-writer decision, and A7/rev3's separation of principal, unit, title and grant. It also contradicts its own following sentence. This is material authority distortion even though row identity and links remain structurally valid. The structural helper is not claimed to reject arbitrary meaning; this independent semantic decision provides the required consequence. |

These decisions establish no universal meaning validator or G8 reliability. Live KNOWLEDGE.md was not changed.

### V3 — Guidance and native decisions

Candidate README blob equals the independently read AC4 guide `2fdf930de8d974d47961b7fbd0708afe51520dd5`. All six change/risk categories name existing selections, with generated-output and broad-risk triggers. Collection/full-suite gates match project configuration; guidance cannot waive authority or budget. E-S fixture reuse is distinct from a changed source corpus; changed knowledge requires current structural/semantic evidence; an altered oracle invalidates its affected pass. The exact native v1 response was formed before unblinding and remains unchanged. The attached decisions preserve the Reviewer's conditional-output challenge and different selection breadth. No repeated case batch or provider trial occurred.

### V4 — Raw evidence, Candidate crossing and accounting

The archive has 109 members and the declared SHA-256 `fd878b9b5e136f349afdc56f83a209154a520732ba79c53d722b54fcd68cab0d`. Its internal index covers every other member; every length/hash matches. This establishes integrity, not the truth of its prose: actual raw stdout, process events, source manifests, variants and normal/adverse HTML were also inspected.

All 1,984 files in the contemporaneous full-run input manifest hash to the actual Candidate Git blobs; all four pretest VALUE blob identities match. Candidate is the linear child of `62cb3f58a56c2dc8e69fd5f67366264f10725c6d`, precedes RF/EV, and has no later VALUE change. Actual raw root Git commands use immutable inputs except HEAD/MERGE_HEAD/merge enumeration. The inspected predicate asserts literal HEAD only with MERGE_HEAD present; both crossing sides have no MERGE_HEAD. The merge graph is identical, preserving selected historical Phase E merge `b977b89be0c759297dd5653040564f0169ba3e56` and its parents. Thus the new Candidate SHA does not invalidate those results. Later reporting/review traces are outside that manifest and receive no blanket full-suite PASS.

The control pair uses 1,968 identical Baseline non-VALUE files (independently checked against Git), exact Candidate overlays, unchanged scanner test/helper/constants/fixtures and the same recorded interpreter/package/environment tuple. Raw wall times are 148.5193369 and 0.9893969 seconds: 147.5299400 seconds lower, MkDocs 1→0. The initial baseline has no pre-run whole-source manifest; its contemporaneous detached identity plus retained root and subsequent clean tracked/composition audit are the available provenance. Together with the exact unchanged controlled fixture subject, these support this limited local comparison. Pytest 9 is outside the project range; the pair is not supported-environment acceptance. Ordinary acceptance uses pytest 8.4.2. No universal speedup, labor or monetary claim is accepted.

Raw collection reports 549 tests; full run reports 548 passed and the existing board-accounting skip. Eight raw pytest receipts sum to 1,006.1777711 seconds and three MkDocs starts; builds are not added twice. The original absent failure is retained (121 pass/3 fail), with exact two-selector correction and the three dependent tests rerun. The stale pure family passes all 124; the 1,778-file stale preservation receipt supports no output mutation. The ordinary adverse run starts with valid stale output, performs a successful fresh build and fails the unchanged frontmatter-leak assertion for exactly one of 1,726 pages. Independent inspection finds no leak in the normal HTML and the real header-as-body leak in the adverse HTML; the variation touches only disposable `add_frontmatter` input and the restored hash matches the untouched generator.

The approved NUL-safe four-path commands reproduce the raw accounting byte-for-byte: `+2922 -2937 = 5859`, four logical text files, no rename, binary metric inapplicable. The immutable denominator remains 4/6400; neither 8-file nor 12,800-LOC owner multiplier is reached. The 5,000 soft trigger was already ruled by owner receipt before work. Candidate six-path commit contains four VALUE paths and authorized phase state/event only. Other Baseline-to-Candidate changes are prior task/root control intake, not hidden product scope.

Native [Executor commit receipts](evidence/executor-commit-native-receipts.json) independently confirm exact paths, pre-commit status/cached inspection and `git commit --only`, including Candidate command `exec-519a3025-24f4-4319-a830-d04ff23be93e` and RF commit `exec-1fa9f6b3-6587-4b7d-bcaa-2c60381a3958`. Imported allocation receipt retains its source identity. No selected uncommitted sibling dependency or landing/cleanup is claimed.

## Commands Executed

| Observation | Result |
|---|---|
| Read-only Git/source/AST/ZIP/manifest/primary-source inspections; literal approved NUL accounting | Identities, arithmetic, unchanged bodies, evidence integrity and boundaries independently reproduced; raw receipts linked above |
| One pytest 8.4.2 process selecting board guard, controlled scanner negative, historical Phase D knowledge, historical/current Phase E knowledge, knowledge structural damages and live R10/R14 ledger | **6 passed in 13.31 s**, measured process wall **14.2099964 s**, exit 0, 0 MkDocs, six collected, site absent before/after. Exact argv/input identities and raw reports: [start](evidence/review-targeted.start.json), [receipt](evidence/review-targeted.receipt.json), [stdout](evidence/review-targeted.pytest.txt), [events](evidence/review-targeted.events.jsonl). No further pytest/build allocation remains here. |

The observer is byte-identical to the inspected raw attachment and records successful child starts/test reports; it supplies no assertions or selection. Reviewer command accounting separately records measured command time and a five-second wrapper/preparation upper bound around the targeted process, without counting polling fragments twice. Coordinator dispatch 3deb replaces the old 0.154197-second line with 60 seconds; starting common amount is 1,599.239969 seconds.

## Claim & Source Checks

| Claim | Primary verification | Holds? |
|---|---|---|
| Moved tests preserve effective protection | Independent all-body AST/global comparison plus meaningful retained negative run | Yes |
| Legitimate successor does not fabricate authority | Exact initial TS, A7 act, ruled return and final TS byte-equal to Git; semantic comparison above | Yes, finite labeled case |
| Savings and adverse result are real observations | Original process receipts, unchanged subject/composition, successful build then existing assertion failure and different HTML | Yes, stated local/environment limits |
| Candidate/accounting apply to tested result | Actual 1,984 Git blobs, pretest identities, Git predicate semantics and NUL bytes | Yes; root landing remains future |

## Discrepancies Found

No material discrepancy or unreported VALUE change found. RF's prior common-budget figure is superseded transparently by later dispatch 3deb. The failed pure run, pytest-9 comparison limitation, conditional historical skip and missing baseline pre-run corpus manifest are disclosed evidence qualifications, not hidden passes. Architecture is adequately explained by the existing phase/master flow and README's explicit two-module boundary; another diagram is not necessary to understand this change.

### Project-wide debt discovery

[Discovery receipt](evidence/debt-discovery.json) searches both configured containers, `workspace` and `tasks`: 118 REVIEW files, 357 table rows and four rows naming the changed surface. TD-193 was explicitly closed in TFW-60/AA REVIEW rev3; the moved payload-path predicate and all three adverse forms remain intact. RDP REVIEW rev2 row 1 and rev3 row 5 have actual Coordinator `paid` rulings; the current strict ordinal-ending regex and its third adverse assertion preserve those repairs. None is reopened.

TD-189 retains a historical `Backlog — monitor` entry. Its old ~250-second full-suite observation is not a current benchmark or an approved instruction to exclude output checks. The current result removes unrelated MkDocs setup from pure selections and explicitly retains the configured full gate. No additional material failure is established by this legacy generic monitoring entry. REVIEW §5 preserves it as a pending Coordinator proposal to retire that further obligation by a consequence ruling; the Reviewer does not invent a terminal disposition or rewrite the retired debt snapshot. This administrative ruling blocks DONE until resolved, not the Candidate verdict.

## Evidence Verification

| EV item | Exists / independent disposition |
|---|---|
| E1 | Verified: source/output bodies and dependency inspection; absent correction composite, complete stale family, final source identities and independent targeted run |
| E2 | Verified: 156-body disposition, surviving effective targets, narrow guard and retained negative behavior |
| E3 | Verified: executable historical/current and structural positive/negative results; independent targeted rerun |
| E4 | Verified for these exact inputs by the source-grounded semantic judgments above |
| E5 | Verified: actual identical guide and independently formed native choices; no reliability overclaim |
| E6 | Verified as one limited local controlled comparison; unsupported pytest-9 environment is explicit |
| E7 | Verified: actual configured full/collection and genuine fresh-build frontmatter failure |
| E8 | Verified: exact tested bytes and relevant Git semantics across linear Candidate creation |
| E9 | Independent Candidate review completed here; root landing remains pending, not failed or retrospectively asserted |
| E-accounting | Verified: exact membership/numstat/authority/denominator and prospective trigger disposition |

Ten evidence rows inspected, nine complete for review scope and E9 split into completed review and future root landing; zero missing files. This does not rewrite the historical Executor EV statuses.

## Knowledge Citations Verified

Independent P0–P4 scan was completed before Judge; P5–P7 were selected for relevance. [Link inspection](evidence/citation-path-check.json) resolves all 17 explicit citation-section paths. The following 28 grouped citation applications cover every master HL §7.2, phase HL citation row and ONB §7 row; references using “same source” resolve to the stated source.

| Source/application groups | Exact cited items and semantic check | Result |
|---|---|---|
| Master/phase/ONB P0 (3) | NS1; NS2.2/4/5/7; NS3: subtract unrelated machinery while retaining authority, inspectability and protected consequence | Resolve/exist/match/relevant |
| Master/phase/ONB P1 (3) | Methodology values and Success Criteria 1–4: candid actual observations, observable structure, portability and acceptance readiness; distinct from P0 purpose | Resolve/exist/match/relevant |
| Master/phase/ONB P2 (3) | Philosophy F32/F36/F40–F43/F45: preserve purpose, materiality, architecture and useful explanation through subtraction | Resolve/exist/match/relevant |
| Master/phase/ONB P3 groups (5) | D37, D52–53, D59, D61, D63–64, D68, D71–77, D81–85 as selected in their rows: knowledge ownership, real evidence, independent purpose judgment, exact scope/history and receiver boundaries | Resolve/exist/match/relevant |
| Master/phase/ONB P4 (3) | HL Contract rules 3/6/8/13/17–21, Design Rules, Anti-patterns: invariant authority, lawful refinement/routing, exact scoped implementation and material review | Resolve/exist/match/relevant |
| Master/phase/ONB P5 (3) | Convention F21/F23: purpose/practice distinction and English semantic source; canonical artifact language independently agrees with project config | Resolve/exist/match/relevant |
| Master/phase/ONB P6 (3) | Process F39/F46–49/F51: real consumers, sequencing, bounded autonomy/research/spend and honest disposition | Resolve/exist/match/relevant |
| Master/phase/ONB P7 (3) | Constraint F3/F14/F16: no filler debt, separate acceptance act and upstream/receiver separation | Resolve/exist/match/relevant |
| Master/ONB technical research (2) | Main iter1 D1–7 and iter2 D1–9 / named R2 refinements; independent audit is separately pinned: historical/current distinction, structural split, finite verification and no empirical claim from research alone | Resolve/exist/match/relevant |

Total 28 applications: 28 resolved and semantically relevant, 0 irrelevant, 0 hallucinated. Existing knowledge is consistent with the change; no product knowledge was edited to satisfy an oracle.

## Checkpoint

- [x] All 13 changed package paths and additional authority inputs inspected; ratio exceeded.
- [x] One meaningful bounded test command completed with nonempty outcomes.
- [x] Key claims, actual sources, arithmetic and evidence provenance independently checked.
- [x] Every RF AC mark checked against implementation/raw evidence; E4 resolved independently.
- [x] KNOWLEDGE contradictions and all cited PV applications checked.
- [x] All ten EV references inspected; future landing distinguished from completed review.

Stage complete: YES.
