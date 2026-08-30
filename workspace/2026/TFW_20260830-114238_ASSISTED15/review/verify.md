# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF product paths claimed: 35
> Minimum files to verify: ceil(35 × 0.42) = 15
> Actual verification: 35/35 product paths and 47/47 evidence attachments; all high-risk requirements were independently rerun.

## Verification Log

The initial scope was already high-risk enough for complete verification. The first hostile discrepancy then made the workflow's 100% escalation mandatory. Every current product file was opened as UTF-8 and hashed; every retired path was compared with its baseline blob and confirmed absent.

| # | Product path | RF claim checked | Actual | Match |
|---|---|---|---|---|
| 1 | editions/02-assisted/.agents/skills/tfw-handoff/SKILL.md | Complete bounded Executor contract | Role lock, preflight, partial-history and Coordinator-only reporting are present | ✅ |
| 2 | editions/02-assisted/.agents/skills/tfw-handoff/agents/openai.yaml | Complete metadata pair | Valid metadata points to handoff and stable task path | ✅ |
| 3 | editions/02-assisted/.agents/skills/tfw-identity/SKILL.md | Working identity service contract | The documented create-profile command uses --corporate-role, which the shipped parser rejects; see D7 | ❌ |
| 4 | editions/02-assisted/.agents/skills/tfw-identity/agents/openai.yaml | Complete metadata pair | Valid metadata and fail-closed prompt | ✅ |
| 5 | editions/02-assisted/.agents/skills/tfw-identity/scripts/tfw_identity.py | Full operational-local-v1, ACL and component-chain defense | Positive matrix passes, but a newly created tfw-assisted namespace is not pinned and no ACL/private-permission evidence is checked; see D4 | ❌ |
| 6 | editions/02-assisted/.agents/skills/tfw-plan/SKILL.md | Coordinator/manual/autonomous lifecycle | Stable task path, one Executor/Reviewer, same-role reuse, exact-target and human acceptance rules are present | ✅ |
| 7 | editions/02-assisted/.agents/skills/tfw-plan/agents/openai.yaml | Complete metadata pair | Valid metadata | ✅ |
| 8 | editions/02-assisted/.agents/skills/tfw-review/SKILL.md | Independent full review | Full-contract re-review and no-fix role lock are present | ✅ |
| 9 | editions/02-assisted/.agents/skills/tfw-review/agents/openai.yaml | Complete metadata pair | Valid metadata | ✅ |
| 10 | editions/02-assisted/.agents/skills/tfw-update/SKILL.md | Protected bidirectional update contract | Contract is complete in prose, but the implementation does not carry the release manifest and reverse safety is not enforced; see D2 and D5 | ⚠️ partial |
| 11 | editions/02-assisted/.agents/skills/tfw-update/agents/openai.yaml | Complete metadata pair | Valid metadata | ✅ |
| 12 | editions/02-assisted/.codex/hooks.json | Exact stock hook retired | Absent; baseline SHA-256 044013a5…50434ce matches policy | ✅ |
| 13 | editions/02-assisted/.codex/hooks/tfw-hook.ps1 | Exact stock hook retired | Absent; baseline SHA-256 85191702…29361c7 matches policy | ✅ |
| 14 | editions/02-assisted/.codex/hooks/tfw-hook.sh | Exact stock hook retired | Absent; baseline SHA-256 18039f16…f5fca9a1a matches policy | ✅ |
| 15 | editions/02-assisted/AGENTS.md | Neutral 1.5 contract, no hook claims | Manual lifecycle, identity split, preservation and honest capability limits are present | ✅ |
| 16 | editions/02-assisted/CHANGELOG.md | Public-only 1.5/1.0 history | 1.5 is explicitly Unreleased; only public 1.0 baseline is claimed; no SemVer/tag/downstream history claim | ✅ |
| 17 | editions/02-assisted/MIGRATION.md | State-preserving migration | Manual and 1.0→1.5 paths, exact hook retirement, protected state and post-checks are present | ✅ |
| 18 | editions/02-assisted/PROJECT.md | Visibly uninitialized project | No project_id, person, organization or project default | ✅ |
| 19 | editions/02-assisted/README.md | Standalone manual Assisted 1.5 | Lifecycle, uninitialized start, templates, update path and limits are readable and mutually consistent | ✅ |
| 20 | editions/02-assisted/VERSION | Exact version authority | Exact bytes are 1.5 LF | ✅ |
| 21 | editions/02-assisted/knowledge/INDEX.md | Empty neutral knowledge navigation | Contains only generic empty-state rules and no organization knowledge | ✅ |
| 22 | editions/02-assisted/people/README.md | Empty neutral people navigation | Contains identity/role separation and no shipped profile | ✅ |
| 23 | editions/02-assisted/шаблоны/assets/tfw-mark.svg | Neutral restricted mark | Shape-only SVG; no text, metadata, events or external references | ✅ |
| 24 | editions/02-assisted/шаблоны/build_a4.py | Offline bounded builder | Stock/custom build and attacks pass; defaults resolve under the template root | ✅ |
| 25 | editions/02-assisted/шаблоны/overlay/theme.css | Six-property overlay | Exactly one root block and six allowed generic properties | ✅ |
| 26 | editions/02-assisted/шаблоны/theme.css | Six-property stock theme | Exactly one root block and six allowed generic properties | ✅ |
| 27 | editions/02-assisted/шаблоны/документ_A4.md | Complete worked A4 example | Complete Russian example with long tokens, code, lists and tables | ✅ |
| 28 | editions/02-assisted/шаблоны/заметка.md | Complete worked note | Complete generic note; status is a standalone bold paragraph immediately after a list, a minor Markdown polish issue only | ⚠️ minor |
| 29 | editions/02-assisted/шаблоны/план_работы.md | Complete worked plan | Complete result, scope, acceptance, risks and rollback example | ✅ |
| 30 | editions/02-assisted/шаблоны/презентация.html | Complete offline presentation | Five readable local slides, no external resource | ✅ |
| 31 | editions/ASSISTED_MAINTENANCE.md | Truthful maintenance authority | Source/target preservation guidance is clear, but “reverse never changes public core” and release-manifest continuity are not enforced by the shipped CLI; see D2 and D5 | ❌ |
| 32 | editions/README.md | Correct edition selection/capability boundary | Assisted 1.5 manual baseline and asymmetric maintenance are documented | ✅ |
| 33 | editions/maintenance/assisted_maintenance.py | Closed release/update/identity-adjacent V1–V12 entry point | Stock tests pass, but hostile cases disprove manifest completeness, forward completeness, operation-dir confinement, reverse validation/confinement and V11 coverage; see D1–D6 | ❌ |
| 34 | editions/maintenance/maintenance-policy.json | Closed deterministic policy | Canonical, 31 current entries classify uniquely, prior edge and three retirement hashes validate | ✅ |
| 35 | editions/maintenance/release-manifest.json | Complete current release boundary | Current stored 31 entries exactly equal independently regenerated entries and include policy, but this authority is omitted by forward and verify-release does not enforce completeness after tampering; see D1–D2 | ⚠️ partial |

## Commands Executed

| # | Command / check | Result |
|---|---|---|
| 1 | git diff --exit-code f3eb986 -- forbidden root/Full/Light paths | Exit 0; no forbidden baseline change |
| 2 | git diff name-status/numstat/check f3eb986 -- editions | 25 added, 7 modified, 3 deleted, 35 total; 2,452 added + 778 removed = 3,230; diff-check exit 0 |
| 3 | Independent product census and SHA-256 read | 32 current files opened as UTF-8; 3 deleted blobs matched exact stock hashes and are absent |
| 4 | Regenerate manifest in memory and compare with stored manifest | Current package: 31/31 entries exactly equal; manifest 32b6354f…e213686; policy 2caf8bba…d64b07 |
| 5 | assisted_maintenance.py verify-release --source-root editions | Exit 0, state verified |
| 6 | assisted_maintenance.py self-test --source-root editions | Exit 0, V1–V12 all true |
| 7 | tfw_identity.py self-test | Exit 0, reported V7/V8 true |
| 8 | build_a4.py --self-test | Exit 0, six checks true |
| 9 | gen_index.py --check project and --check tasks | Project consistent; 54 task states valid |
| 10 | Parse all evidence JSON/NDJSON/PDF/HTML/image attachments | 47 files found; 12 JSON and 2 NDJSON parse; 4 PDFs have expected hashes/pages; 20 visual files opened |
| 11 | Independent visual inspection with original-detail images | All 16 PDF page images and all 4 browser full captures opened; Cyrillic/Latin and core layout are readable; discrepancies in D8 |
| 12 | pdfinfo and pdftotext on all four PDFs | Page counts 3+3+5+5; custom A4 exposes browser header/footer and absolute file URL |
| 13 | Hostile manifest omission: remove README entry only, recanonicalize, run shipped verifier in temp | Stored entries 30, regenerated 31, omitted file exists, yet state verified; D1 reproduced |
| 14 | Hostile forward fixture followed by verify-release on resulting target | Forward status verified and VERSION=1.5, but release manifest absent and verification raises FileNotFoundError; D2 reproduced |
| 15 | Hostile operation-dir symlink into target | Text path outside but resolved path inside; target/operation was created before failure; D3 reproduced |
| 16 | Hostile reverse candidate under a public tree using a minimal fabricated report | Candidate accepted and public tree changed; D5 reproduced |
| 17 | Hostile identity namespace creation | locality returned proven, pin rows held only path/device/inode, tfw-assisted did not exist at probe and was still not pinned after creation; persistent registry was written; D4 reproduced |
| 18 | Identity documented-command/help comparison | Skill uses --corporate-role; parser requires --organization-role; D7 reproduced |
| 19 | Relative-link and public marker scan | 5/5 relative links resolve; no Innoforce/person/company/path/brand residue in shipped public payload; generic provider name Shared Drives is expected |
| 20 | Read-only H: inventory with Python code-point order | 29 files, digest 3a1885c6…dbee96b; matches retained pre/post evidence |
| 21 | Read-only H: inventory with PowerShell culture order | 29 files, digest 7e2248a7…4fadc3; matches retained pre/post evidence and explains aggregate-order difference |
| 22 | Git commit/remote/tag audit | Product/evidence commits are not contained in a remote-tracking ref or tag; branch is 144 commits ahead of origin/master; no publication evidence found |
| 23 | Live role-tree inspection | Exactly one phase Coordinator, the same completed Executor, and this one independent Reviewer; E4 live lineage is established |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|---|---|---|---|
| C1 | “Exactly 35 product paths / 3,230 changed lines; no forbidden baseline diff” | RF §4, EV E1 | Primary Git diff from f3eb986 | ✅ |
| C2 | “The complete 29-row field inventory is stable under both documented orders” | RF §§2,4; EV E12 | Current read-only H: inventories plus source-immutability.json pre/post values | ✅ — both current digests match; the different aggregate hashes are fully explained by sort order |
| C3 | “Actual clean P2 reaches 1.5 and both directions are complete” | RF §§3–5; EV E12 | Primary forward journal/terminal plus independent hostile target/reverse fixtures | ❌ — VERSION reaches 1.5, but the target lacks release-manifest.json; reverse accepts a fabricated report and may write under public core |

All HL/ONB citations trace to real local primary artifacts. No external quantitative claim is needed to decide this implementation: the decisive claims are source code, Git state, filesystem manifests, PDF bytes and the pinned field inventory, all directly reachable.

## Discrepancies Found

### D1 — Critical — verify-release does not enforce manifest completeness

- **Requirement:** TS AC-2 requires the stored manifest to bind every payload file except itself; AC-11 requires hostile history/path/schema coverage.
- **Location:** editions/maintenance/assisted_maintenance.py lines 242–253 generate a complete manifest, but lines 756–763 only validate entries already present and never compare them with manifest_for_source.
- **Reproduction:** in a temporary package, delete only the 02-assisted/README.md entry from the manifest and recanonicalize it. The file remains present; stored count is 30, regeneration count is 31, yet verify-release returns state=verified.
- **Harm:** a release may silently omit a payload file from the integrity boundary while the official verifier declares it verified. V1/V2 and EV E2/E11 are therefore not sufficient.
- **Correction request:** make release verification regenerate the full allowed payload set and require canonical entry equality; add omitted payload, omitted policy, unexpected payload, self-entry and non-regular hostile fixtures to the shipped matrix.

### D2 — Critical — forward reaches VERSION 1.5 without carrying the release manifest

- **Requirement:** TS AC-2 makes release-manifest.json a source of truth; AC-12 requires the P2 target to reach a maintainable 1.5 with before/after manifests.
- **Location:** editions/maintenance/assisted_maintenance.py lines 369–399 plan only manifest records; lines 420–430 stage only those records; the manifest intentionally excludes itself at lines 242–253 and is never added separately to the forward plan.
- **Evidence:** retained forward-journal.ndjson has 34 path events and includes policy/VERSION but not maintenance/release-manifest.json. Independent fixture: forward status=verified, VERSION=1.5, release manifest absent, post-forward verify-release=FileNotFoundError.
- **Harm:** the target cannot validate or serve as the trusted source for the next update. EV E12’s “reaches 1.5” is materially incomplete.
- **Correction request:** carry the verified manifest as a separately classified release-authority write, include it in staging/baseline/postconditions, and require verify-release to pass on the resulting target.

### D3 — High — operation-dir confinement is bypassed through a directory link

- **Requirement:** TS AC-3 and DoF require operation/staging outside source and target and zero unauthorized writes.
- **Location:** editions/maintenance/assisted_maintenance.py lines 443–465 use operation.absolute() and a textual commonpath test instead of a resolved/pinned component chain, then create the directory before the target baseline.
- **Reproduction:** an external symlink to the target with operation below the link is textually outside but resolves inside. The shipped function created target/operation before failing with PermissionError.
- **Harm:** operation state can be written inside the protected target and outside the classified plan; on another filesystem it may proceed farther before the unexplained-change check.
- **Correction request:** resolve and pin every existing component, reject symlink/junction/reparse ancestry and prove the to-be-created parent outside both roots before creation; add an actual Windows link/junction fixture.

### D4 — Critical — operational-local-v1 proves locality without ACL evidence or the full created chain

- **Requirement:** TS AC-7/AC-8 require private permissions, ACL/probe evidence and the full ancestor/component chain to remain pinned at every operation.
- **Location:** tfw_identity.py lines 274–299 record only normalized path, device and inode for the existing parent; lines 302–310 recheck only those rows. Lines 428–451 create tfw-assisted and then continue using the old pin. No ACL/owner/private-permission check exists.
- **Reproduction:** with an existing local ancestor and absent tfw-assisted namespace, locality returns proven; the namespace is absent from the pin, update_registry creates it and writes bindings.json. Pin row width is only three fields.
- **Harm:** the newly created component may be replaced by a junction/reparse point between creation and lock/temp writes, and broad permissions can still be labelled proven. EV E8’s “full component pin” claim is false.
- **Correction request:** after creation, open/lstat and pin the namespace and full chain before lock/temp creation; require platform-appropriate private ACL/owner evidence or return unknown; add namespace-substitution and permissive-ACL zero-write fixtures.

### D5 — High — reverse candidate neither validates a terminal report nor prevents public-core mutation

- **Requirement:** TS AC-6 requires a validated append-only terminal report and candidate-only reverse flow with no public-core mutation before review.
- **Location:** assisted_maintenance.py lines 534–557 accept any dict with matching schema/status, allow extra/missing terminal fields, read noncanonical JSON, and accept any new candidate_dir without source/public/target confinement.
- **Reproduction:** a fabricated minimal report was accepted; setting candidate_dir below a temporary public tree created maintenance-candidate/public-candidate.json and changed that public tree.
- **Harm:** the command’s own “never mutates public core” guarantee depends on caller discipline and a candidate can be minted without a valid operation record.
- **Correction request:** validate the closed canonical terminal schema and regular-file provenance, and require an exact approved candidate root proven outside public/source/target roots; retain privacy noninterference tests and add these hostile cases.

### D6 — High — V11 is a token-presence scan, not the claimed role scenario matrix

- **Requirement:** TS AC-4/AC-11 require complete, partial, lost-handle, no-interrupt, overlap, manual fallback and full-re-review scenarios.
- **Location:** assisted_maintenance.py lines 695–715 declares V11 true when five files are longer than 300 characters and selected Russian substrings appear.
- **Evidence:** EV E4 says shipped V11 “covers” the scenarios, but no executable/tabletop scenario artifact exists. The actual live lineage does pass: one Coordinator → same Executor → one independent Reviewer, child reporting through the Coordinator only.
- **Harm:** wording can satisfy the release gate while capability/handle/interruption behavior is untested.
- **Correction request:** separate contract lint from scenario verification; add a deterministic state-table/tabletop fixture with recorded inputs/outputs for every required failure mode. Preserve the established live lineage for correction and full re-review.

### D7 — High — the shipped identity command is not executable as documented

- **Requirement:** TS AC-4/AC-7/AC-10 require complete mutually consistent skills and referenced commands.
- **Location:** tfw-identity/SKILL.md line 27 documents --corporate-role; tfw_identity.py line 610 requires --organization-role.
- **Reproduction:** create-profile --help exposes only --organization-role; the documented flag is rejected by argparse.
- **Harm:** a fresh Assisted user following the internal gate cannot create a profile with the published command.
- **Correction request:** use one flag name in skill, parser, people terminology and tests; execute the documented command from a clean copy.

### D8 — Medium — rendered evidence contradicts its own polish/path and format claims

- **Requirement:** TS AC-9/AC-10 require polished offline stock/custom outputs and no private/location path in generated output.
- **Evidence:** a4-custom.pdf and pages 1–2 visibly contain browser date/title headers and the absolute file:///D:/projects/.../a4-custom.html footer. All four browser-*-full.png files begin with JPEG JFIF bytes, not PNG bytes; the full captures also contain stitch overlap/duplication. render-summary.json nevertheless records the visual package without these exceptions.
- **Harm:** the custom A4 artifact is not a clean deliverable and leaks a local filesystem path; mislabeled/stitched browser evidence is not a faithful PNG capture.
- **Correction request:** rerender with browser headers/footers disabled, emit files whose extension matches their bytes, visually inspect every replacement page/full capture, and update the summary honestly.

No frozen-HL amendment is indicated. Every discrepancy is repairable within the approved 35 product paths and task-local evidence scope; fixes should return to the same Executor, followed by a complete re-review in this Reviewer session.

## Evidence Verification

All 47 attachments exist. JSON/NDJSON parses, PDF hashes/page counts and visual bytes were checked independently. Status below means whether the artifact supports the RF/EV claim made from it, not merely whether the file opens.

| # | Evidence attachment | Exists? | Matches claim? |
|---|---|---|---|
| E1 | assisted15-fixture-results.json | ✅ | ⚠️ Partial — recorded outputs reproduce, but V8/V11/V12 conclusions omit D2/D4/D6 |
| E2 | assisted15-verification.log | ✅ | ⚠️ Partial — commands really pass; “FINAL=PASS” is disproved by hostile checks |
| E3 | boundary-and-source-attestation.md | ✅ | ✅ Boundary and retained dual-order source digests match |
| E4 | boundary-summary.json | ✅ | ⚠️ Boundary fields hold; fixture_all_v1_v12 reports command booleans, not complete coverage |
| E5 | EV__TFW_20260830-114238_ASSISTED15.md | ✅ | ❌ E2/E4/E8/E9/E10/E11/E12 contain material overclaims; E4 live lineage itself is now established |
| E6 | identity-windows.json | ✅ | ⚠️ Actual positive/project/lock/junction cases hold; it does not prove ACL or the newly created namespace chain |
| E7 | maintenance/forward-journal.ndjson | ✅ | ⚠️ Parses 35 rows and proves the operation, but also proves the manifest path was omitted |
| E8 | maintenance/forward-terminal.json | ✅ | ⚠️ Create-once verified record exists, but verified does not mean maintainable 1.5 without the manifest |
| E9 | maintenance/partial-journal.ndjson | ✅ | ✅ Two canonical events; injected first-write failure represented |
| E10 | maintenance/partial-terminal.json | ✅ | ✅ Immutable create-once partial status |
| E11 | maintenance/protected-after.json | ✅ | ✅ Eight protected entries equal before state |
| E12 | maintenance/protected-before.json | ✅ | ✅ Eight protected entries and hashes resolve |
| E13 | maintenance/public-candidate-a.json | ✅ | ⚠️ Closed public projection bytes are privacy-safe; private report validity/confinement is unproved |
| E14 | maintenance/public-candidate-b.json | ✅ | ⚠️ Byte-identical to candidate A; same reverse safety gap |
| E15 | maintenance/recovery-terminal.json | ✅ | ✅ Separate linked verified recovery record |
| E16 | run_evidence.py | ✅ | ⚠️ Reproducible generator, but its V12 check stops at VERSION/hooks and its role/locality conclusions inherit gaps |
| E17 | source-immutability.json | ✅ | ✅ Current independent 29-row digests match both retained pre/post values |
| E18 | templates/a4-custom.html | ✅ | ✅ Standalone Russian HTML, no external resources |
| E19 | templates/a4-custom.pdf | ✅ | ❌ Correct hash/pages but contains local browser header/footer and absolute file URL |
| E20 | templates/a4-custom-page-1.png | ✅ | ❌ Readable but visibly contains local file URL/header/footer |
| E21 | templates/a4-custom-page-2.png | ✅ | ❌ Readable but visibly contains local file URL/header/footer |
| E22 | templates/a4-custom-page-3.png | ✅ | ✅ Readable final table/page |
| E23 | templates/a4-stock.html | ✅ | ✅ Standalone Russian HTML, no external resources |
| E24 | templates/a4-stock.pdf | ✅ | ✅ Three valid readable pages |
| E25 | templates/a4-stock-page-1.png | ✅ | ✅ Readable, no clipping |
| E26 | templates/a4-stock-page-2.png | ✅ | ✅ Readable, no clipping |
| E27 | templates/a4-stock-page-3.png | ✅ | ✅ Readable final table/page |
| E28 | templates/browser-a4-custom-full.png | ✅ | ⚠️ Opens visually, but bytes are JPEG and capture has stitch overlap |
| E29 | templates/browser-a4-stock-full.png | ✅ | ⚠️ Opens visually, but bytes are JPEG and capture has stitch overlap |
| E30 | templates/browser-presentation-custom-full.png | ✅ | ⚠️ Opens visually, but bytes are JPEG and capture duplicates content at stitch seams |
| E31 | templates/browser-presentation-stock-full.png | ✅ | ⚠️ Opens visually, but bytes are JPEG and capture duplicates content at stitch seams |
| E32 | templates/presentation-custom.html | ✅ | ✅ Five local Russian slides, no external resources |
| E33 | templates/presentation-custom.pdf | ✅ | ✅ Five valid readable pages |
| E34 | templates/presentation-custom-page-1.png | ✅ | ✅ Readable, no clipping |
| E35 | templates/presentation-custom-page-2.png | ✅ | ✅ Readable, no clipping |
| E36 | templates/presentation-custom-page-3.png | ✅ | ✅ Long token and glyphs readable |
| E37 | templates/presentation-custom-page-4.png | ✅ | ✅ Table readable |
| E38 | templates/presentation-custom-page-5.png | ✅ | ✅ Lists readable |
| E39 | templates/presentation-stock.html | ✅ | ✅ Five local Russian slides, no external resources |
| E40 | templates/presentation-stock.pdf | ✅ | ✅ Five valid readable pages |
| E41 | templates/presentation-stock-page-1.png | ✅ | ✅ Readable, no clipping |
| E42 | templates/presentation-stock-page-2.png | ✅ | ✅ Readable, no clipping |
| E43 | templates/presentation-stock-page-3.png | ✅ | ✅ Long token and glyphs readable |
| E44 | templates/presentation-stock-page-4.png | ✅ | ✅ Table readable |
| E45 | templates/presentation-stock-page-5.png | ✅ | ✅ Lists readable |
| E46 | templates/render-summary.json | ✅ | ⚠️ Hashes/pages/DOM counts hold; visual verdict omits the custom header/path and browser format/stitch defects |
| E47 | verify_task.py | ✅ | ⚠️ Read-only boundary check reproduces counts, but trusts the shipped fixture result for complete V1–V12 coverage |

Evidence totals: 47/47 exist; 28 fully match their bounded claim; 19 are partial or contradicted; 0 missing.

## Knowledge Citations Verified

PV priorities 0–4 were read in full; priorities 5–7 were read for every cited item and relevant neighboring facts. The frozen HL and ONB carry the same ten citations, so both occurrences were checked separately. Links resolve from each artifact.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant? |
|---|---|---|---|---|---|---|
| 1 | HL K1 | P0 README.md § How It Works — Proportional discipline across domains | ✅ | ✅ | ✅ | ✅ |
| 2 | HL K2 | P0 .tfw/README.md NS1 and NS3 | ✅ | ✅ | ✅ | ✅ |
| 3 | HL K3 | P1 Methodology values and Success Criteria | ✅ | ✅ | ✅ | ✅ |
| 4 | HL K4 | P2 knowledge/philosophy.md F32–F34 | ✅ | ✅ | ✅ | ✅ |
| 5 | HL K5 | P3 KNOWLEDGE.md D57–D60 | ✅ | ✅ | ✅ — topology, honest manual capability and explicit root handling are the stated application | ✅ |
| 6 | HL K6 | P4 conventions.md §§3, 11, 14 | ✅ | ✅ | ✅ | ✅ — structural enforcement directly exposes D1/D6 |
| 7 | HL K7 | P5 knowledge/convention.md F20 | ✅ | ✅ | ✅ | ✅ |
| 8 | HL K8 | P7 knowledge/constraint.md F10 | ✅ | ✅ | ✅ | ✅ |
| 9 | HL K9 | P6 knowledge/process.md F27–F29 | ✅ | ✅ | ✅ | ✅ |
| 10 | HL K10 | P7 knowledge/stakeholder.md F4–F5, F8 | ✅ | ✅ | ✅ | ✅ |
| 11 | ONB K1 | P0 README.md § How It Works — Proportional discipline across domains | ✅ via HL | ✅ | ✅ | ✅ |
| 12 | ONB K2 | P0 .tfw/README.md NS1 and NS3 | ✅ via HL | ✅ | ✅ | ✅ |
| 13 | ONB K3 | P1 Methodology values and Success Criteria | ✅ via HL | ✅ | ✅ | ✅ |
| 14 | ONB K4 | P2 knowledge/philosophy.md F32–F34 | ✅ via HL | ✅ | ✅ | ✅ |
| 15 | ONB K5 | P3 KNOWLEDGE.md D57–D60 | ✅ via HL | ✅ | ✅ | ✅ |
| 16 | ONB K6 | P4 conventions.md §§3, 11, 14 | ✅ via HL | ✅ | ✅ | ✅ |
| 17 | ONB K7 | P5 knowledge/convention.md F20 | ✅ via HL | ✅ | ✅ | ✅ |
| 18 | ONB K8 | P7 knowledge/constraint.md F10 | ✅ via HL | ✅ | ✅ | ✅ |
| 19 | ONB K9 | P6 knowledge/process.md F27–F29 | ✅ via HL | ✅ | ✅ | ✅ |
| 20 | ONB K10 | P7 knowledge/stakeholder.md F4–F5, F8 | ✅ via HL | ✅ | ✅ | ✅ |

Knowledge-citation totals: 20, resolved 20, semantically verified 20, irrelevant 0, hallucinated 0. No citation contradicts the frozen product objective. The discrepancies are implementation/evidence failures against those correctly cited values, not citation defects.

## Deferred Evidence Decisions

- **EV E4 live lineage:** accepted. The actual runtime tree shows one Phase Coordinator, the same completed Executor, and this independent Reviewer. No duplicate role session exists; reports route through the Coordinator. The separate V11 negative-scenario claim remains unverified under D6.
- **Semantic neutrality/privacy:** shipped product accepted. Full text/SVG/CSS scan plus manual reading found generic Russian templates and no Innoforce organization, person, brand, private history, unique path or copied knowledge. Reverse control and rendered-evidence path hygiene are not accepted under D5/D8.
- **EV E12 real-source P6:** accepted for read-only immutability. Both current read-only 29-file digests equal retained pre/post evidence; no review command wrote H:. The aggregate mismatch is exactly PowerShell culture sorting versus Python code-point sorting of the same row set.
- **EV E12 no publication:** accepted to the observable Git boundary. No product/evidence commit is in a local remote-tracking ref or tag; current branch remains ahead of origin/master. No push/tag/publication was performed by this Reviewer.
- **EV E12 both maintenance directions:** not accepted. Forward lacks the release manifest and reverse confinement/report validation fails under D2/D5.

## Checkpoint

**Self-check:**
- [x] Opened at least 15 files and recorded findings? 35/35 product paths plus 47/47 evidence attachments.
- [x] Ran at least one build/test command? Shipped commands, primary Git checks, render parsing, two field readers and hostile fixtures were run.
- [x] Claim & Source Checks filled with 2–3 high-impact claims and primary artifacts?
- [x] Each RF §3 AC checkmark verified against actual files?
- [x] KNOWLEDGE.md checked and contradictions documented? No knowledge contradiction; structural-enforcement facts support D1/D4/D6.
- [x] Knowledge citations from HL §7.2 and ONB §7 verified?
  - Total: 20, resolved: 20, semantically verified: 20, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total attachments: 47, fully matching: 28, partial/contradicted: 19, missing: 0
- [x] On discrepancy, escalated to 100% verification? Yes. The escalation materially changed the result by exposing D1–D8 despite all shipped positive commands passing.

Stage complete: YES
