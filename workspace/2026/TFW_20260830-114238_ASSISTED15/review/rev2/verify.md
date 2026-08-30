# Verify — “Are the corrected claims true?” (revision 2)
> **Mindset:** Auditor. This is a full rerun, not a delta review.
> **Test:** “If RF and the first review disappeared, would the current product and evidence prove the frozen contract?”
> Minimum product ratio: 0.42; required minimum: `ceil(35 × 0.42) = 15`.
> Actual product verification: **35/35 paths (100%)**.
> Actual evidence verification: **47/47 attachments inspected (100%); 39 fully support their bounded claims, 8 partial/overclaiming, 0 missing**.

## Verification boundary

- Contract baseline: `ee09a8a5bf...`; product comparison baseline: `f3eb986`.
- Corrected terminal package: `b37f7a3`, `964abd2`, `85d4e76`; current `HEAD` is `85d4e76d7b3ae0f9f7e439b329250527d8bc3f71`.
- The first-pass `review/{map,verify,judge}.md` and formal REVISE remain unchanged. This pass writes only under `review/rev2/`.
- Literal `f3eb986..HEAD` includes 60 paths outside `editions/` and this task workspace from concurrent TFW-60/root work. An independent task-attributed audit enumerated all 17 Assisted commits and found **0 forbidden-path hits**. The literal and attributed audits are both retained; concurrent changes are not reclassified as Assisted work.
- `editions/` remains exactly 35 product paths: 25 added, 7 modified, 3 deleted; 2,871 additions + 778 removals = 3,649 changed lines, below the 4,800 ceiling. `git diff --check f3eb986 -- editions` passes.
- Reviewer diagnostic commands briefly created an ignored Python cache and rewrote two evidence summaries through `verify_task.py`; the cache was removed and both tracked evidence files were restored byte-exactly to `HEAD` before continuing. No product, RF, EV, HL, TS, ONB, status or journal artifact was changed.

## Product verification — 35/35

| # | Product path | Independent result |
|---|---|---|
| 1 | `editions/02-assisted/.agents/skills/tfw-handoff/SKILL.md` | Complete bounded Executor/partial-history/Coordinator-reporting contract; matches frozen lifecycle. |
| 2 | `editions/02-assisted/.agents/skills/tfw-handoff/agents/openai.yaml` | Valid complete metadata pair. |
| 3 | `editions/02-assisted/.agents/skills/tfw-identity/SKILL.md` | Documented `--organization-role` command now executes, but the promised per-operation locality defense is not fully implemented before the first registry read; see D10. |
| 4 | `editions/02-assisted/.agents/skills/tfw-identity/agents/openai.yaml` | Valid fail-closed metadata. |
| 5 | `editions/02-assisted/.agents/skills/tfw-identity/scripts/tfw_identity.py` | Stock 23-check matrix passes and corrected full-chain/ACL fixtures pass; independent call-order instrumentation exposes D10. |
| 6 | `editions/02-assisted/.agents/skills/tfw-plan/SKILL.md` | One-Coordinator/one-Executor/one-Reviewer, same-role reuse, manual fallback and acceptance boundary present. |
| 7 | `editions/02-assisted/.agents/skills/tfw-plan/agents/openai.yaml` | Valid metadata. |
| 8 | `editions/02-assisted/.agents/skills/tfw-review/SKILL.md` | Full-contract repeat review and Reviewer no-fix role lock present. |
| 9 | `editions/02-assisted/.agents/skills/tfw-review/agents/openai.yaml` | Valid metadata. |
| 10 | `editions/02-assisted/.agents/skills/tfw-update/SKILL.md` | Manifest/provenance/confinement corrections are documented; its project-lock guarantee is not met across distinct operations; see D9. |
| 11 | `editions/02-assisted/.agents/skills/tfw-update/agents/openai.yaml` | Valid metadata. |
| 12 | `editions/02-assisted/.codex/hooks.json` | Deleted; exact accepted stock hook only. |
| 13 | `editions/02-assisted/.codex/hooks/tfw-hook.ps1` | Deleted; exact accepted stock hook only. |
| 14 | `editions/02-assisted/.codex/hooks/tfw-hook.sh` | Deleted; exact accepted stock hook only. |
| 15 | `editions/02-assisted/AGENTS.md` | Neutral Russian-authoritative Assisted 1.5, manual baseline and truthful capability limits. |
| 16 | `editions/02-assisted/CHANGELOG.md` | Useful public changelog: `1.5 — Unreleased` plus public `1.0` baseline only; no false tag/release history. |
| 17 | `editions/02-assisted/MIGRATION.md` | Complete protected-state/manual migration and exact hook retirement guidance. |
| 18 | `editions/02-assisted/PROJECT.md` | Visibly uninitialized; no plausible organization/project/person defaults. |
| 19 | `editions/02-assisted/README.md` | Standalone lifecycle, initialization, templates, identity and maintenance entry points are readable and mutually consistent. |
| 20 | `editions/02-assisted/VERSION` | Exact bytes `1.5\n`. |
| 21 | `editions/02-assisted/knowledge/INDEX.md` | Neutral empty knowledge navigation; no Innoforce knowledge. |
| 22 | `editions/02-assisted/people/README.md` | Neutral empty people navigation and identity/role distinction. |
| 23 | `editions/02-assisted/шаблоны/assets/tfw-mark.svg` | Shape-only SVG; no text, metadata, event, URL, script or private marker. |
| 24 | `editions/02-assisted/шаблоны/build_a4.py` | Stock/custom and six hostile checks pass twice; offline bounded builder. |
| 25 | `editions/02-assisted/шаблоны/overlay/theme.css` | One `:root`, six declared generic properties. |
| 26 | `editions/02-assisted/шаблоны/theme.css` | One `:root`, six declared generic properties. |
| 27 | `editions/02-assisted/шаблоны/документ_A4.md` | Complete useful Russian example with long heading/token, code, lists and wide/tall tables. |
| 28 | `editions/02-assisted/шаблоны/заметка.md` | Complete generic note; only non-blocking Markdown spacing polish remains. |
| 29 | `editions/02-assisted/шаблоны/план_работы.md` | Complete result/scope/acceptance/risk/rollback example. |
| 30 | `editions/02-assisted/шаблоны/презентация.html` | Five readable local Russian slides, no external dependency. |
| 31 | `editions/ASSISTED_MAINTENANCE.md` | Direction/manifest/reverse guidance is clear, but the asserted cross-operation project lock is ineffective; see D9. |
| 32 | `editions/README.md` | Edition selection and Assisted 1.5 capability boundary are accurate. |
| 33 | `editions/maintenance/assisted_maintenance.py` | Corrected D1–D6 behaviors pass; a new hostile concurrent-operation fixture disproves the project-lock claim; see D9. |
| 34 | `editions/maintenance/maintenance-policy.json` | Canonical, deterministic and uniquely classifying; exact three retirement hashes and manifest authority hold. |
| 35 | `editions/maintenance/release-manifest.json` | Stored 31 payload entries exactly equal independent regeneration; repeated public hashes stable. |

## Commands and independent reruns

| Check | Result |
|---|---|
| `verify-release --source-root editions`, twice | Exit 0 both times; manifest `3697803d…4156624b`, policy `2caf8bba…3d64b07`, byte-stable. |
| Fresh full maintenance `self-test` | Exit 0; V1–V12 report true; omitted payload/policy, unexpected/self/nonregular, operation link, reverse fake/public-root, next-source and seven role cases all report true. |
| Fresh identity `self-test` | Exit 0; V7/V8 and all 23 declared checks true, including actual private ACL, full namespace pin, junction/substitution/root-swap/live-lock cases. |
| A4 builder self-test, twice | Exit 0 twice; all six static/stock/custom/attack checks true. |
| Task evidence runner | Exit 0 and reproduced the retained public hash, but its execution writes evidence summaries; those diagnostic writes were restored. Its matrix omission is recorded under D9/D10 rather than treated as proof. |
| `.tfw/scripts/gen_index.py --check tasks` / `--check project` | Exit 0 / exit 0. `--check index` reports stale shared `workspace/00-INDEX.md`; this is concurrent shared aggregate state outside the frozen product boundary and was not edited by the Reviewer. |
| Manifest regeneration after cache cleanup | 31/31 exact entries; stored/generated equality restored; no `__pycache__` remains. |
| D1 hostile omitted real payload | Rejected with `release manifest paths differ from regenerated allowed payload`. |
| D2 forward manifest continuity | `verified=true`, manifest carried byte-exact, resulting target verifies and is accepted as next source. |
| D3 real Windows junction parent | Rejected with `operation directory parent ancestry contains a link or reparse point`; zero target product write. |
| D5 reverse hostile provenance/confinement | Incomplete fake terminal and candidate under public root both reject at zero writes. |
| D6 role matrix | Exactly seven deterministic cases: complete, partial, lost-handle, no-interrupt, overlap, manual-fallback, full-re-review; all expected/observed records equal and duplicates=0. |
| D7 clean documented identity command | `create-profile --organization-role ...` exits 0 and creates the expected Latin handle in a clean copy. |
| D8 render validation | Four PDFs parse as 3+3+5+5 pages; PDF text has no local URL; all 20 replacements have true PNG signatures and retained hashes. |
| D9 independent held-lock fixture | `lock_paths_equal=false`; a second operation with the same target but another operation directory returns `second_status=verified` while the first alleged project lock remains held. |
| D10 call-order instrumentation | `call_order=read_registry->reprobe`; therefore registry access occurs before the first operation-time revalidation. |
| Relative link audit | HL: 16 links, 0 missing; ONB: 2 links, 0 missing. All ten PV sources and twenty HL/ONB citation applications were read semantically. |
| Privacy/neutrality scan and manual read | No field organization, private payload/history/path/brand/person projected into product. Hits are only the deliberately split forbidden scanner strings and generic provider label `Shared Drives`; SVG/CSS remain neutral. |
| H: post-review read-only inventory | Actual source `H:\Shared drives\IT\Innoforce AI-First Knowledge\innoforce_starter_v1.5`: 29 files; PowerShell culture digest `7e2248a7…4fadc3`, Python code-point digest `3a1885c6…dbee96b`; both equal retained pre/post. |
| Live role tree | Exactly one Phase Coordinator, the same completed Executor, and this same independent Reviewer; no duplicate task role session. |
| Git publication audit | `85d4e76` is in no remote-tracking branch and no tag; no Assisted correction commit is published. No push/tag command was run by this Reviewer. |

## Closure of original D1–D8

| Historical finding | Full-rerun result |
|---|---|
| D1 manifest completeness | Closed: exact regenerated payload equality and all five hostile manifest cases reject. |
| D2 forward manifest | Closed: separately journaled/carried byte-exact; target and next-source verification pass. |
| D3 operation link | Closed: actual Windows junction ancestry rejects before target product write. |
| D4 identity chain/ACL | Closed for the corrected tested cases: full created namespace chain and private owner/ACL are proven; permissive ACL/substitution/junction/root swap reject. D10 is a distinct first-read ordering defect. |
| D5 reverse provenance/confinement | Closed: canonical neighboring terminal/journal and exact outside candidate root required; fabricated/public-root cases reject. |
| D6 role matrix | Closed: deterministic seven-scenario record exists and passes; live lineage separately verified. |
| D7 documented identity flag | Closed: one flag name throughout and clean documented execution succeeds. |
| D8 rendered evidence | Closed: all 20 actual PNGs visually opened; no header/footer/local URL, byte mismatch, seam, clipping or unreadable glyph/table/token found. |

## New discrepancies

### D9 — Critical — “project lock” is unique per operation, not shared per target

- **Requirement:** TS AC-3 line 99 requires a project lock immediately before mutation; AC-11 lines 193–200 require complete race/conflicting-writer coverage; frozen HL DoF 7 forbids silently merging a conflicting writer.
- **Location:** `editions/maintenance/assisted_maintenance.py:644-647`. The target-derived key is stable, but `lock_path = operation / f"project-{lock_key}.lock"`. `execute_forward` creates each operation directory independently at lines 615–627, so two operations for one target lock two different files.
- **Independent reproduction:** hold `ProjectLock(<held-operation>/project-<same-target>.lock)`, then call `execute_forward` for the same target with `<second-operation>`. Output: `lock_paths_equal=false`, `second_status=verified`, `second_completed_while_first_lock_held=true`.
- **Impact:** the OS lock provides no mutual exclusion between normal distinct operations. Two maintenance writers can both pass the claimed project-lock gate; baseline/per-path checks may detect some races but cannot replace the explicitly required lock or guarantee conflict prevention.
- **Correction request:** locate the lock in a stable, private and pinned lock root keyed by the canonical pinned target identity and independent of the unique operation directory; acquire it before the complete target baseline/staging/mutation sequence. Add a real two-operation/two-process fixture proving distinct operation directories contend and the loser performs zero product writes. Preserve operation journals as create-once per-operation records.

### D10 — High — identity registry is read before operation-time locality revalidation

- **Requirement:** TS AC-8 lines 155–165 permits persistent binding only when the full locality/ACL/component evidence is revalidated at every operation, including substitution defense; AC-7 requires unsafe state to avoid persistent identity access/state.
- **Location:** `editions/02-assisted/.agents/skills/tfw-identity/scripts/tfw_identity.py:495-500` calls `read_registry(store)` before `reprobe(decision)` in `update_registry`. The command path also performs a redundant `read_registry` at lines 761–764 before its first re-probe.
- **Independent reproduction:** replace `read_registry` and `reprobe` with order-recording probes and stop at the first re-probe. Actual output is `call_order=read_registry->reprobe`, `read_before_first_reprobe=true`.
- **Impact:** after locality is initially proven, an ancestor/namespace substitution may redirect the first existence/file/read access before the saved chain is checked. Later re-probes protect the write path, but they do not satisfy “revalidated at every operation” before the first registry access and do not close the bounded privacy/race claim.
- **Correction request:** re-probe the complete pinned chain and re-check private ACL/owner evidence before any registry or lock `exists`, type check or byte read; remove the redundant pre-read in the command dispatcher and perform all binding reads under the validated lock where applicable. Add a fixture that substitutes the namespace after `locality()` but before the first read and asserts both zero read of the substituted registry and zero persistent write.

No frozen-HL amendment is indicated: both defects are repairable inside the existing five affected product paths and task-local evidence boundary.

## Evidence attachment verification — 47/47

“Full” means the attachment accurately supports its bounded claim. “Partial” includes an accurate recorded run whose completeness conclusion is disproved by D9/D10.

| # | Attachment | Result |
|---|---|---|
| 1 | `assisted15-fixture-results.json` | Partial — recorded outputs are reproducible, but V3/V8/V11 completeness omits D9/D10. |
| 2 | `assisted15-verification.log` | Partial — commands and hashes reproduce; terminal `PASS` overstates the frozen race matrix. |
| 3 | `boundary-and-source-attestation.md` | Partial — boundary/source/publication facts hold; “project lock pass” is disproved by D9. |
| 4 | `boundary-summary.json` | Partial — retained census/environment are accurate at capture; `fixture_all_v1_v12` is not complete against D9/D10 and current dual audit is 17 task commits. |
| 5 | `EV__TFW_20260830-114238_ASSISTED15.md` | Partial — E1/E2/E4–E7/E9/E10 facts hold, but E3/E8/E11 overclaim D9/D10; E12 dependency is not closed. |
| 6 | `identity-windows.json` | Partial — actual recorded ACL/junction/substitution/lock observations hold, but there is no pre-first-read revalidation fixture. |
| 7 | `maintenance/forward-journal.ndjson` | Full — canonical 35 planned path records including the separate manifest; actual operation trace. |
| 8 | `maintenance/forward-terminal.json` | Full — canonical create-once verified record for that bounded operation. |
| 9 | `maintenance/partial-journal.ndjson` | Full — started plus one path event for injected failure. |
| 10 | `maintenance/partial-terminal.json` | Full — canonical immutable partial terminal. |
| 11 | `maintenance/protected-after.json` | Full — eight protected entries byte-equal. |
| 12 | `maintenance/protected-before.json` | Full — eight protected entries and hashes resolve. |
| 13 | `maintenance/public-candidate-a.json` | Full — canonical privacy-safe candidate for a valid closed operation. |
| 14 | `maintenance/public-candidate-b.json` | Full — byte-identical projection/public ID from a distinct valid operation. |
| 15 | `maintenance/recovery-terminal.json` | Full — separate linked verified recovery record. |
| 16 | `run_evidence.py` | Partial — reproducible generator, but the race/locality matrix lacks D9/D10. |
| 17 | `source-immutability.json` | Full — both independent current 29-row digests match retained pre/post and the algorithm distinction is correct. |
| 18 | `templates/a4-custom.html` | Full — standalone Russian HTML, no external resources. |
| 19 | `templates/a4-custom.pdf` | Full — valid complete three-page header-free PDF and retained hash. |
| 20 | `templates/a4-custom-page-1.png` | Full — true PNG; visually readable. |
| 21 | `templates/a4-custom-page-2.png` | Full — true PNG; long token/table content readable. |
| 22 | `templates/a4-custom-page-3.png` | Full — true PNG; final table/footer clean. |
| 23 | `templates/a4-stock.html` | Full — standalone Russian HTML, no external resources. |
| 24 | `templates/a4-stock.pdf` | Full — valid complete three-page header-free PDF and retained hash. |
| 25 | `templates/a4-stock-page-1.png` | Full — true PNG; readable. |
| 26 | `templates/a4-stock-page-2.png` | Full — true PNG; readable. |
| 27 | `templates/a4-stock-page-3.png` | Full — true PNG; final table/footer clean. |
| 28 | `templates/browser-a4-custom-full.png` | Full — true single-shot PNG, no stitch overlap or local URL. |
| 29 | `templates/browser-a4-stock-full.png` | Full — true single-shot PNG, no stitch overlap. |
| 30 | `templates/browser-presentation-custom-full.png` | Full — true single-shot PNG covering all five slides without seam duplication. |
| 31 | `templates/browser-presentation-stock-full.png` | Full — true single-shot PNG covering all five slides without seam duplication. |
| 32 | `templates/presentation-custom.html` | Full — five local Russian slides; no external resources. |
| 33 | `templates/presentation-custom.pdf` | Full — valid complete five-page PDF and retained hash. |
| 34 | `templates/presentation-custom-page-1.png` | Full — true PNG; readable. |
| 35 | `templates/presentation-custom-page-2.png` | Full — true PNG; two-column content readable. |
| 36 | `templates/presentation-custom-page-3.png` | Full — true PNG; long token/glyphs readable. |
| 37 | `templates/presentation-custom-page-4.png` | Full — true PNG; table readable. |
| 38 | `templates/presentation-custom-page-5.png` | Full — true PNG; list readable. |
| 39 | `templates/presentation-stock.html` | Full — five local Russian slides; no external resources. |
| 40 | `templates/presentation-stock.pdf` | Full — valid complete five-page PDF and retained hash. |
| 41 | `templates/presentation-stock-page-1.png` | Full — true PNG; readable. |
| 42 | `templates/presentation-stock-page-2.png` | Full — true PNG; two-column content readable. |
| 43 | `templates/presentation-stock-page-3.png` | Full — true PNG; long token/glyphs readable. |
| 44 | `templates/presentation-stock-page-4.png` | Full — true PNG; table readable. |
| 45 | `templates/presentation-stock-page-5.png` | Full — true PNG; list readable. |
| 46 | `templates/render-summary.json` | Full — independent signature/hash/page/visual checks match all bounded fields. |
| 47 | `verify_task.py` | Partial — boundary/census checks are useful, but it trusts the incomplete shipped race/locality matrix and mutates retained summaries when run. |

Evidence totals: **47 inspected; 39 full (82.98%); 8 partial/overclaiming (17.02%); 0 missing**.

## Knowledge citations — 20/20

The ten frozen sources were checked once at source and twice at their HL/ONB application. All 20 applications resolve, exist, preserve the source meaning and remain relevant.

| Citation pair | Source and semantic result |
|---|---|
| HL/ONB K1 | `README.md` How It Works — proportional discipline/continuity; valid. |
| HL/ONB K2 | `.tfw/README.md` NS1/NS3 — human-governed continuity and non-goals; valid. |
| HL/ONB K3 | `.tfw/README.md` methodology values/Success Criteria — structural, portable, resumable, acceptance-ready; valid. |
| HL/ONB K4 | `knowledge/philosophy.md` F32–F34 — preserve meaning and reach a usable result; valid. |
| HL/ONB K5 | `KNOWLEDGE.md` D57–D60 — topology and honest capability boundary; valid. D58’s older hook state is explicitly treated as superseded, not copied as a current claim. |
| HL/ONB K6 | `.tfw/conventions.md` §§3, 11, 14 — structural gates, evidence honesty and no scope drift; valid and directly material to D9/D10. |
| HL/ONB K7 | `knowledge/convention.md` F20 — uninitialized starter state is product behavior; valid. |
| HL/ONB K8 | `knowledge/constraint.md` F10 — edition independence; valid. |
| HL/ONB K9 | `knowledge/process.md` F27–F29 plus relevant F32 — routine discipline, real initialization, evidence/acceptance distinction and final recapture; valid. |
| HL/ONB K10 | `knowledge/stakeholder.md` F4–F5/F8 — low-friction, non-redundant onboarding and clean deterministic checks; valid. |

Totals: **20 resolved, 20 semantically verified, 0 irrelevant, 0 hallucinated**.

## Deferred evidence decisions

- **E4 — closed by this verification.** The live role tree is exactly one Phase Coordinator → the same completed Executor → this same independent Reviewer. Reports went to the Phase Coordinator, the first REVISE history is preserved, and the deterministic seven-scenario table passes.
- **Semantic neutrality/privacy — accepted.** Manual reading of all 35 product paths, private-marker scans, SVG/CSS inspection and all rendered outputs found no Innoforce knowledge, organization/person/brand/logo/private-history/path payload in the product. Generic provider terminology and scanner literals are functional, not field projection.
- **E12 field-source immutability — accepted.** The real 29-file H: source was read only; both current aggregate digests equal the retained pre/post values. The two hashes differ solely because PowerShell culture order and Python code-point order serialize the same rows differently.
- **E12 no publication — accepted.** No Assisted terminal commit is contained by a remote-tracking branch or tag; no push/tag/publication was run.
- **E12 both-direction mechanics — demonstrated, but E12 cannot close as a whole.** Forward reaches a verified maintainable 1.5 and reverse remains candidate-only with corrected provenance/confinement. However AC-12 depends on AC-3 and AC-11, and D9 leaves the required cross-operation project-lock/race property unsatisfied.

## Checkpoint

**Self-check:**
- [x] Full rerun, not delta-only: 35/35 product paths and 47/47 attachments.
- [x] Every original D1–D8 correction independently reopened and rerun.
- [x] Critical V1–V12, identity, template, boundary, manifest, maintenance and hostile checks rerun.
- [x] Every actual rendered image opened visually: 20/20.
- [x] Both H: digest algorithms rerun read-only after verification.
- [x] E4, E12, semantic neutrality/privacy and publication decided explicitly.
- [x] Twenty HL/ONB knowledge-citation applications revalidated.
- [x] Discrepancies have exact requirements, files/lines, reproductions, impact and bounded correction requests.
- [x] Unrelated `.gitignore`, TFW-55 and concurrent shared state were preserved.

Stage complete: **YES**

**WAIT — Verify is complete. Coordinator checkpoint is required before Purpose Check/Judge.**
