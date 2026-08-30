# Verify — "Is it true?" (revision 3)
> **Mindset:** Auditor. Re-run the complete corrected contract, not only the latest diff.
> **Test:** "Would the terminal product and current evidence still prove the frozen TS if the RF and both earlier reviews disappeared?"
> Baseline: `f3eb986`; frozen HL: `ee09a8a`; terminal implementation/evidence: `afef18a`, `640fad5`, `1aa6e97`.

Actual verification coverage is **35/35 product paths (100%)** and **47/47 evidence attachments (100%)**. All attachments exist and are readable; 39 fully support their bounded claims, while eight are partial because their terminal pass conclusions are contradicted by the current Windows rerun and/or current Git tag state. No attachment is missing.

## Verification boundary

- The first-pass and revision-2 review traces were read as historical evidence and left unchanged. This pass writes only under `review/rev3/`.
- Product evaluation uses the frozen 35-path `editions/` boundary. Current root, TFW-55 and TFW-60 work is concurrent external state and was neither modified nor staged.
- `H:\...\innoforce_starter_v1.5` was accessed only through file enumeration, size and SHA-256 reads. No command used it as source code, renderer input, operation directory or update target.
- A long full maintenance/identity rerun was stopped after preserving a diagnostic stack because the same Windows failure was already independently reproducible with bounded probes. Remaining checks were isolated and bounded rather than repeating a known hang.
- Reviewer probes are retained at `review/rev3/d9_probe.py`, `d10_probe.py` and `v_probes.py`; they import the shipped implementation but write only to OS temporary directories.

## Product verification — 35/35

| # | Product path | Independent result |
|---:|---|---|
| 1 | `editions/02-assisted/.agents/skills/tfw-handoff/SKILL.md` | Complete Executor contract; role lock, baseline, evidence, partial history and Coordinator-only return are explicit. |
| 2 | `editions/02-assisted/.agents/skills/tfw-handoff/agents/openai.yaml` | Valid bounded metadata for the handoff role. |
| 3 | `editions/02-assisted/.agents/skills/tfw-identity/SKILL.md` | Correct first-access and live-lock claims are documented, but the actual successful Windows persistent path does not terminate; see D11. |
| 4 | `editions/02-assisted/.agents/skills/tfw-identity/agents/openai.yaml` | Valid internal-role metadata with implicit invocation disabled. |
| 5 | `editions/02-assisted/.agents/skills/tfw-identity/scripts/tfw_identity.py` | D10 call ordering and substitution rejection pass independent instrumentation; real `validated_registry_lock` stalls during post-lock ACL proof, so V7/V8 cannot complete; see D11. |
| 6 | `editions/02-assisted/.agents/skills/tfw-plan/SKILL.md` | Complete Gate 0, manual/autonomous, same-role reuse, knowledge and human-acceptance contract. |
| 7 | `editions/02-assisted/.agents/skills/tfw-plan/agents/openai.yaml` | Valid bounded planner metadata. |
| 8 | `editions/02-assisted/.agents/skills/tfw-review/SKILL.md` | Complete independent full-review and full-rerun contract. |
| 9 | `editions/02-assisted/.agents/skills/tfw-review/agents/openai.yaml` | Valid bounded reviewer metadata. |
| 10 | `editions/02-assisted/.agents/skills/tfw-update/SKILL.md` | Stable target-keyed locking and first-mutation order are correctly specified, but the actual Windows lock holder cannot reach ready state; see D11. |
| 11 | `editions/02-assisted/.agents/skills/tfw-update/agents/openai.yaml` | Valid bounded update metadata. |
| 12 | `editions/02-assisted/.codex/hooks.json` | Absent; baseline retirement hash matches policy exactly. |
| 13 | `editions/02-assisted/.codex/hooks/tfw-hook.ps1` | Absent; baseline retirement hash matches policy exactly. |
| 14 | `editions/02-assisted/.codex/hooks/tfw-hook.sh` | Absent; baseline retirement hash matches policy exactly. |
| 15 | `editions/02-assisted/AGENTS.md` | Standalone Russian-authoritative service contract; manual lifecycle, role separation, identity, knowledge, update and honesty boundaries agree. |
| 16 | `editions/02-assisted/CHANGELOG.md` | Public-only `1.5 - Unreleased` plus truthful public 1.0 baseline; no invented SemVer/date/downstream history. |
| 17 | `editions/02-assisted/MIGRATION.md` | Protected-state and exact stock-hook retirement guidance agrees with policy and product. |
| 18 | `editions/02-assisted/PROJECT.md` | Uninitialized, no project UUID, human, organization or hidden runtime state. |
| 19 | `editions/02-assisted/README.md` | Complete onboarding, manual/autonomous lifecycle, identity, templates and protected update guidance; five local links resolve. |
| 20 | `editions/02-assisted/VERSION` | Exact bytes `1.5\n`. |
| 21 | `editions/02-assisted/knowledge/INDEX.md` | Empty neutral navigation with explicit promote/retain/reject decision. |
| 22 | `editions/02-assisted/people/README.md` | Complete surname/collision/profile/automation semantics without shipped participant state. |
| 23 | `editions/02-assisted/шаблоны/assets/tfw-mark.svg` | Neutral shape-only SVG; no text, metadata, event, script, URL or private marker. |
| 24 | `editions/02-assisted/шаблоны/build_a4.py` | AST-valid; TI1 validator and isolated self-test pass; external/escaping/theme/SVG attacks reject. |
| 25 | `editions/02-assisted/шаблоны/overlay/theme.css` | Six-property closed overlay example, no active/external content. |
| 26 | `editions/02-assisted/шаблоны/theme.css` | Six-property closed stock theme, no active/external content. |
| 27 | `editions/02-assisted/шаблоны/документ_A4.md` | Complete worked neutral A4 example with long token, code, lists and wide/tall tables. |
| 28 | `editions/02-assisted/шаблоны/заметка.md` | Complete worked neutral decision note, not an empty placeholder. |
| 29 | `editions/02-assisted/шаблоны/план_работы.md` | Complete result/acceptance/risk/rollback work plan. |
| 30 | `editions/02-assisted/шаблоны/презентация.html` | Complete five-slide offline Russian presentation with readable stock layout. |
| 31 | `editions/ASSISTED_MAINTENANCE.md` | Clear asymmetric authority, stable-lock, P6, partial/recovery and no-publication contract; actual Windows lock behavior contradicts its successful-operation claim; see D11. |
| 32 | `editions/README.md` | Edition selection, Assisted 1.5 lifecycle and asymmetric maintenance guidance agree with the package. |
| 33 | `editions/maintenance/assisted_maintenance.py` | Manifest, policy, reverse, link, role and stable-key logic pass isolated checks; actual Windows `ProjectLock` cannot complete post-lock ACL revalidation; see D11. |
| 34 | `editions/maintenance/maintenance-policy.json` | Canonical policy hash `2caf8bba…d64b07`; three retirement hashes equal baseline bytes and all three paths are absent. |
| 35 | `editions/maintenance/release-manifest.json` | Canonical self-excluded manifest hash `f09603aa…c66ea`; `verify-release` regenerates the exact 31-record payload. |

The Git delta is exactly 25 added, seven modified and three deleted product paths. Numstat is 3,257 additions + 778 removals = **4,035 changed lines**, below the 4,800 frozen ceiling. All three Python products parse through `ast`; `git diff --check f3eb986 -- editions` is clean.

## Commands and independent reruns

| Check | Result |
|---|---|
| Fresh `verify-release --source-root editions` | Exit 0; manifest `f09603aa…c66ea`, policy `2caf8bba…d64b07`. |
| Fresh template `--self-test` | Exit 0; stock theme/mark, standalone output, escape, theme and SVG attacks all pass. |
| Fresh full maintenance self-test | Did not complete. It was bounded after the independent D9/D11 reproduction established the same lock/ACL path. |
| Fresh identity self-test | Did not complete after more than four minutes. A 15-second `faulthandler` capture shows the main thread in `windows_acl` → `private_permissions(lock)` → `validated_registry_lock`; diagnostic process then terminated without repository writes. |
| Independent D9 real-process probe | Failed: the first real process did not reach `LOCKED` within 15 seconds. Its 10-second stack is `_windows_acl` → `private_permissions` → `ProjectLock.__enter__` after the byte lock has been acquired. No operation directory or target/source write occurred. |
| Independent D10 order/substitution probe | Exit 0 under a Reviewer-only surrogate lock primitive: `reprobe → lock access → reprobe → registry read → reprobe`; namespace substitution before the first access produced 0 registry/lock metadata accesses, 0 registry reads, unchanged substituted bytes and no runtime files. This closes the logical D10 ordering defect but does not make the real live-lock path terminate. |
| Independent D1/D3/D5/D6/D7 probe | Exit 0: omitted real payload rejects; real junction operation parent rejects with target and operation absent; fake/public-root reverse rejects at zero writes; secret-different reverse candidates are byte-identical; exactly seven role cases pass with zero duplicates; documented `--organization-role` creates `ivanov`. |
| Project/task schema | Both exit 0; project declares `2.0.0-dirty.5`, 54 tasks validate, only pre-existing informational phase-state notes. |
| Hook retirement | Three current paths absent and all three policy SHA-256 values equal `f3eb986` bytes. |
| Markdown links | Five local product links checked; zero broken. |
| PDF/image validation | Four PDFs parse as 3 + 3 + 5 + 5 pages with expected A4/16:9 sizes, Cyrillic text, no local URL/header/footer; all 20 PNG signatures valid. |
| Visual inspection | All 16 page images and four single-shot full captures opened again; no clipping, seam, unreadable glyph/token/table, branding, path leak or external asset dependency. |
| Product semantic/privacy scan | Only generic provider term `Shared Drives` appears in the functional provider deny-list. No Innoforce fact, person, brand, logo, path, project history or private payload is present. |
| H: before/after | Both reads: 29 files, culture digest `7e2248a7…4fadc3`, code-point digest `3a1885c6…dbee96b`; values equal retained pre/post evidence. |

## Original findings D1–D10 reopened

| Finding | Revision-3 result |
|---|---|
| D1 — manifest completeness | Closed: exact regeneration passes and independently omitted real payload rejects. |
| D2 — forward manifest continuity | Static implementation and retained historical records are coherent, but a current forward run cannot pass the live-lock entry point because of D11. Terminal closure is therefore not independently reproducible. |
| D3 — operation ancestry | Closed: independent real Windows junction parent rejects before operation-directory or target writes. |
| D4 — identity chain/ACL | Full-chain/namespace logic remains present and substitution rejects, but a successful Windows persistent operation stalls during post-lock ACL proof. D11 prevents terminal closure. |
| D5 — reverse provenance/confinement | Closed: independent fake provenance and candidate-under-public cases reject at zero writes; two valid secret-different operations create byte-identical generic candidates. |
| D6 — role matrix | Closed: exactly seven deterministic cases, expected equals observed, duplicates zero. |
| D7 — documented flag | Closed: clean copied starter accepts `--organization-role` and creates `ivanov`. |
| D8 — rendered evidence | Closed: all 20 images visually opened again; four PDFs parse and text remains readable/neutral/offline. |
| D9 — same-target serialization | Stable target-key derivation and pre-operation ordering are present statically, but the first actual lock-holder cannot reach ready state. The required real two-process contention result is not currently reproducible because of D11. |
| D10 — first-access order | The specific ordering/substitution defect is closed by independent instrumentation: re-probe precedes lock/registry access and substituted state gets zero access/write. The actual successful locked-read path remains blocked by D11. |

## V1–V12 terminal matrix

| Gate | Current independent status |
|---|---|
| V1 | Satisfied: exact payload regeneration and hostile omitted payload. |
| V2 | Satisfied: manifest/policy authority and hashes agree. |
| V3 | Not satisfied: junction/drift preconditions hold, but real stable-lock contention cannot start because the holder stalls. |
| V4 | Not independently satisfiable: partial/recovery path requires the stalled forward lock. Retained historical records are internally consistent. |
| V5 | Not independently satisfiable: protected-byte fixture requires the stalled forward lock; retained before/after JSON is byte-identical. |
| V6 | Satisfied: reverse privacy/provenance/confinement independently passes. |
| V7 | Partially satisfied: profile semantics and documented create command pass, but the full identity matrix cannot terminate. |
| V8 | Not satisfied: D10 order/substitution passes, but the supported Windows live-lock/ACL operation does not complete. |
| V9 | Satisfied: template attacks, actual PDFs and all visual artifacts pass. |
| V10 | Satisfied: product agreement and semantic neutrality/privacy pass. |
| V11 | Not satisfied: a complete current V1–V12/identity repetition is non-terminating. |
| V12 | Not satisfied: reverse and P6 immutability pass, but forward depends on V3/V11 and current tag state contradicts the terminal attestation. |

## Discrepancies

### D11 — Critical — Windows live-lock revalidation is non-terminating

- **Requirement:** TS AC-3 requires a real live project lock before operation/staging/baseline/mutation; AC-7/AC-8 require a usable proven persistent identity path with private permissions, live lock and post-read validation; AC-11 requires reproducible V1–V12. A fail-closed error is acceptable, but an ordinary successful-path operation must terminate and the real D9 contention fixture must run.
- **Maintenance location:** `editions/maintenance/assisted_maintenance.py` lines 596–623. After `msvcrt.locking(...LK_NBLCK...)`, `ProjectLock.__enter__` launches path-based PowerShell ACL probes (`_windows_acl`, lines 165–193) while the live byte lock is held. The independent holder never emits its ready record; the stack is `_windows_acl:179 → private_permissions:199 → ProjectLock.__enter__:617`.
- **Identity location:** `editions/02-assisted/.agents/skills/tfw-identity/scripts/tfw_identity.py` lines 472–541. `validated_registry_lock` enters `live_lock`, then runs `private_permissions(lock)` while the live byte lock is held. The stack is `windows_acl:306 → private_permissions:318 → validated_registry_lock:539`.
- **Observed harm:** normal Windows forward updates cannot reach the operation directory, same-target loser or different-target proof; normal persistent identity status/update and both shipped self-tests can stall indefinitely. Retained `V3/V7/V8/V11/V12=true` is not a reproducible terminal claim. The repository and targets remain unchanged in the bounded failures, but availability and the advertised update/identity behavior are broken.
- **Required correction:** make Windows ACL/owner verification and live-lock acquisition mutually safe without weakening the race boundary. Do not launch a path-based ACL subprocess that can block while the byte lock is held. Establish private ACL before any lock-file content access, preserve full-chain/owner/ACL revalidation, and use a non-inheriting/share-safe handle or handle-based security query for any post-acquire identity proof. Add bounded actual-Windows tests proving (1) the holder reaches ready state promptly, same-target loser blocks before operation-directory and target writes, and a different target completes; (2) identity set/status completes promptly with every registry read under the validated live lock; and (3) substitution/permissive lock or namespace cases remain zero-read/zero-write. Then repeat the full matrix twice.

### D12 — High, external current-state blocker — terminal no-tag attestation is stale

- **Requirement:** TS AC-12 line 209 and Definition of Failure line 248 require no tag/publication in this task; RF lines 42/76, EV E1/E12 and `boundary-and-source-attestation.md` additionally claim no tag contains the Assisted product commits.
- **Observed current state:** local tag `v2.0.0-dirty.5` now targets `cab7243` (`[claude-code/project/release/coordinator] release v2.0.0-dirty.5`, 2026-08-30 18:35:38 +05:00). Both `afef18a` and terminal `1aa6e97` are ancestors. No remote-tracking ref contains them.
- **Attribution:** the retained `640fad5` log truthfully recorded an empty tag containment set at capture time. The later tag belongs to concurrent external release work, not any of the 21 Assisted task commits or Reviewer probes. It was not modified here.
- **Observed harm:** current RF/EV/publication evidence is no longer literally true, so E12 cannot close from the terminal package. The Coordinator must resolve the external tag state/authority and require a fresh truthful final audit; the Assisted Executor must not silently delete or rewrite an unrelated tag.

Neither discrepancy requires an amendment to the frozen HL. D11 is repairable inside existing approved product paths; D12 is external state/attestation coordination, not a product-scope expansion.

## Evidence attachment verification — 47/47

“Partial” means the file exists and records a real bounded run, but its terminal completeness/pass claim is no longer supported by the independent current-state verification.

| # | Attachment | Result |
|---:|---|---|
| 1 | `assisted15-fixture-results.json` | Partial — structurally valid and internally coherent; current D11 contradicts V3/V7/V8/V11/V12 completeness. |
| 2 | `assisted15-verification.log` | Partial — resolvable historical run; current lock path does not reproduce and the no-tag tail is stale. |
| 3 | `boundary-and-source-attestation.md` | Partial — boundary/H/privacy facts hold; live-lock success and no-tag statements do not hold currently. |
| 4 | `boundary-summary.json` | Partial — 35/4,035 census and hashes hold; `fixture_all_v1_v12` is not a current terminal conclusion. |
| 5 | `EV__TFW_20260830-114238_ASSISTED15.md` | Partial — E1–E12 table overclaims the current lock/publication state. |
| 6 | `identity-windows.json` | Partial — retained values are valid JSON but current successful-path Windows matrix does not terminate. |
| 7 | `maintenance/forward-journal.ndjson` | Full historical operation record; 35 classified events parse. |
| 8 | `maintenance/forward-terminal.json` | Full historical terminal record; matches journal operation and 32 mutations. |
| 9 | `maintenance/partial-journal.ndjson` | Full historical create-once partial record. |
| 10 | `maintenance/partial-terminal.json` | Full historical partial terminal matching one mutation. |
| 11 | `maintenance/protected-after.json` | Full; byte-identical to protected-before. |
| 12 | `maintenance/protected-before.json` | Full; eight protected classes represented. |
| 13 | `maintenance/public-candidate-a.json` | Full generic projection. |
| 14 | `maintenance/public-candidate-b.json` | Full and byte-identical to A despite different private operation. |
| 15 | `maintenance/recovery-terminal.json` | Full historical terminal linked to the partial operation. |
| 16 | `run_evidence.py` | Partial — read-only H logic and fixtures are inspectable, but current execution reaches D11. |
| 17 | `source-immutability.json` | Full; both 29-row digest orders reproduced before/after. |
| 18 | `templates/a4-custom.html` | Full; UTF-8, Russian, standalone, no external resource element. |
| 19 | `templates/a4-custom.pdf` | Full; 3-page A4 PDF, readable text, no local URL/header/footer. |
| 20 | `templates/a4-custom-page-1.png` | Full; visually inspected. |
| 21 | `templates/a4-custom-page-2.png` | Full; visually inspected. |
| 22 | `templates/a4-custom-page-3.png` | Full; visually inspected. |
| 23 | `templates/a4-stock.html` | Full; UTF-8, Russian, standalone, no external resource element. |
| 24 | `templates/a4-stock.pdf` | Full; 3-page A4 PDF, readable text, no local URL/header/footer. |
| 25 | `templates/a4-stock-page-1.png` | Full; visually inspected. |
| 26 | `templates/a4-stock-page-2.png` | Full; visually inspected. |
| 27 | `templates/a4-stock-page-3.png` | Full; visually inspected. |
| 28 | `templates/browser-a4-custom-full.png` | Full; single-shot full capture, no seam/clipping. |
| 29 | `templates/browser-a4-stock-full.png` | Full; single-shot full capture, no seam/clipping. |
| 30 | `templates/browser-presentation-custom-full.png` | Full; five complete slides, no seam/clipping. |
| 31 | `templates/browser-presentation-stock-full.png` | Full; five complete slides, no seam/clipping. |
| 32 | `templates/presentation-custom.html` | Full; five Russian slides and no external resource element. |
| 33 | `templates/presentation-custom.pdf` | Full; 5-page 16:9 PDF, readable text, no local URL/header/footer. |
| 34 | `templates/presentation-custom-page-1.png` | Full; visually inspected. |
| 35 | `templates/presentation-custom-page-2.png` | Full; visually inspected. |
| 36 | `templates/presentation-custom-page-3.png` | Full; visually inspected. |
| 37 | `templates/presentation-custom-page-4.png` | Full; visually inspected. |
| 38 | `templates/presentation-custom-page-5.png` | Full; visually inspected. |
| 39 | `templates/presentation-stock.html` | Full; five Russian slides and no external resource element. |
| 40 | `templates/presentation-stock.pdf` | Full; 5-page 16:9 PDF, readable text, no local URL/header/footer. |
| 41 | `templates/presentation-stock-page-1.png` | Full; visually inspected. |
| 42 | `templates/presentation-stock-page-2.png` | Full; visually inspected. |
| 43 | `templates/presentation-stock-page-3.png` | Full; visually inspected. |
| 44 | `templates/presentation-stock-page-4.png` | Full; visually inspected. |
| 45 | `templates/presentation-stock-page-5.png` | Full; visually inspected. |
| 46 | `templates/render-summary.json` | Full; hashes, page counts, signatures and visual statements agree with direct inspection. |
| 47 | `verify_task.py` | Partial — its static checks are inspectable, but the full current run invokes the non-terminating maintenance/identity path and its publication audit is stale. |

All 12 JSON, two NDJSON, four HTML, four PDF, 20 PNG, two Python, two Markdown and one log attachment validate their expected encoding/magic/parse shape. Evidence ratio is exactly **47/47 inspected = 100%**, above the configured 42% minimum.

## Citations and source authority

- All ten frozen HL knowledge citations K1–K10 resolve at Contract Baseline `ee09a8a`. Their 23 named fact/section anchors (`How It Works`, NS1/NS3, F4/F5/F8/F10/F20/F27–F34, D57–D60, conventions §§3/11/14) are present.
- Both RES iterations and their official-primary-source matrices remain resolvable; the terminal implementation does not require a new research or HL amendment.
- Current dirty root knowledge/framework files were not treated as Assisted implementation authority. Frozen citations were read from `ee09a8a` where concurrent edits could change current text.

## Deferred evidence decisions

- **Semantic neutrality/privacy — accepted.** Manual reading of all 35 product paths, direct marker scans, SVG/CSS inspection and all 20 rendered images show no Innoforce fact, person, brand, logo, corporate path, project history or private payload. The generic `Shared Drives` provider label is a platform-deny term, not field projection.
- **E4 live lineage — accepted.** The live agent tree contains exactly one Phase Coordinator, the same Executor used through both corrections, and this one independent Reviewer reused for three full passes; reports flowed through the Coordinator. The seven-scenario table is complete and deterministic.
- **P6 H: source immutability — accepted.** Both Reviewer before/after inventories are 29 rows and equal the retained culture/code-point digests. The two aggregate hashes differ only because the same rows are serialized in different Unicode sort orders.
- **Reverse direction — accepted.** Independent hostile and privacy probes show closed provenance, exact outside-root confinement, zero public mutation and secret-independent candidate bytes.
- **Forward direction / E12 — not accepted.** D11 prevents current maintainable forward execution and V3/V11 closure. D12 also makes the terminal no-tag attestation stale. E12 remains deferred/blocked at Verify.

## Dual audit and publication state

- The task-attributed history is exactly **21 commits** from `ee09a8a` through `1aa6e97`; every commit path is under `editions/` or `workspace/2026/TFW_20260830-114238_ASSISTED15/`, with zero forbidden hits.
- The literal repository-wide `f3eb986..HEAD` difference contains concurrent `.tfw`, root guides/knowledge, adapters, docs and TFW-60 work. Those paths are external and were not staged or modified by this Reviewer.
- No remote-tracking ref contains the terminal product. Local tag `v2.0.0-dirty.5` does contain it, as recorded in D12.

## Purpose risk checkpoint

The neutral standalone product shape, templates, lifecycle, privacy boundary and asymmetric maintenance design still match the North Star. The terminal result is not currently useful as a complete Assisted 1.5 release because its two defining persistent operations—safe forward update and proven local identity—can stall on the supported Windows platform, and the current publication attestation is false after concurrent tag creation. These are implementation/state defects, not reasons to weaken the frozen purpose or broaden the product boundary.

## Checkpoint

**Self-check:**
- [x] Re-read and inspect all 35 product paths, not only `afef18a`.
- [x] Inspect all 47 evidence attachments and every current citation/authority surface.
- [x] Independently test D9 real-process readiness and D10 first-access/substitution ordering with bounded probes.
- [x] Reopen D1–D8 and V1–V12 proportionally without repeating a known indefinite full run.
- [x] Inspect all 20 rendered page/full-capture images and parse all four PDFs.
- [x] Recompute H: before/after rows and both digest orders read-only.
- [x] Audit all 21 task commits, literal global differences, remote refs and tags.
- [x] Decide E4, semantic neutrality/privacy, reverse direction and P6 immutability independently.
- [x] Record exact discrepancies, severity, reproduction, impact and bounded remediation without changing implementation.

Stage complete: YES
