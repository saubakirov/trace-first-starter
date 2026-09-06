# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42 from `.tfw/project_config.yaml` `tfw.review.min_verify_ratio`
> RF files claimed: 6 (2 new + 4 modified)
> Files to verify: ⌈6 × 0.42⌉ = 3; citation and evidence discrepancies escalated verification to 6/6

## Verification Log

### V1: `.tfw/conventions.md`
- **RF claim:** Adds the shared principal/profile/event/binding contract in §4 without changing
  Phase A or D79 behavior.
- **Actual:** Defines stable project-local human/agent principals; optional descriptive roles;
  direct human accountability; an exact Boolean two-level grant; optional non-authoritative
  mentality; optional current `writer`; strict separation from accountability, tool, token, and
  legacy `actor`; and one-job external binding resolution. Independent section hashes prove the
  D79 Session identity and Phase A commit/worktree/staging/landing ranges are byte-identical at
  Baseline and Candidate.
- **Match:** ✅

### V2: `.tfw/templates/team/profile.md`
- **RF claim:** Documents compatible human/agent schema, direct accountability, stable grant,
  mentality, and opposite-grant examples.
- **Actual:** The original four-key human remains complete. The field table and examples require an
  agent's direct human `accountable_to`, lexical YAML Boolean `may_rule_amendments`, immutable
  grant-bearing handle, optional descriptive roles, and optional non-authoritative mentality.
  Independent fixture replay produced 11/11 expected profile outcomes.
- **Match:** ✅

### V3: `.tfw/templates/journal/event.md`
- **RF claim:** Adds optional `writer` while preserving human accountability, free-form tool text,
  opaque token uniqueness, and legacy `actor` composition.
- **Actual:** `writer` is optional and must name a declared human or valid agent principal;
  `on_behalf_of`, `via`, token, and `actor` are explicitly orthogonal. Independent event fixtures
  produced 4/4 expected outcomes. The 28 Baseline journal blobs containing `actor:` all exist at
  Candidate and have identical blob IDs.
- **Match:** ✅

### V4: `.tfw/templates/bindings.yaml`
- **RF claim:** Allows the external one-job binding to select a valid human or agent principal and
  grants nothing.
- **Actual:** The template retains one top-level `bindings` map, external locations, one mapping per
  project, and one-profile silent resolution. It excludes authority, mentality, fallback, default,
  liveness, device, and provider data. Independent binding fixtures produced 2/2 expected outcomes;
  neither documented real binding path exists on this machine.
- **Match:** ✅

### V5: `ONB__phase-b__named_principals.md`
- **RF claim:** Records onboarding, coverage, constraints, risks, and pre-implementation decisions.
- **Actual:** The ONB resolves the approved Baseline/selector and blocking questions, names the four
  VALUE owners and protected subjects, identifies the report-only mismatch, and records the master
  ordinal drift. Its §7 checks all 45 governing knowledge citations. It does not preserve the actual
  `$validator` definition later used for fixture evidence.
- **Match:** ⚠️ partial — comprehension is complete; later command provenance is absent.

### V6: `evidence/EV__phase-b__named_principals.md`
- **RF claim:** Supplies six VERIFIED evidence rows, exact fixtures/results, compatibility/corpus
  checks, configured gates, and immutable accounting replay.
- **Actual:** Git lineage, selector, arithmetic, word counts, protected hashes, legacy corpus,
  report-only diagnostic, and configured checks independently reproduce. The 17 fixture payloads
  and outcomes are present and an independent validator reproduced 17/17. However, the EV records
  only `$validator | python -`; it omits the `$validator` program and therefore does not capture the
  “exact parser command” required by AC-1, AC-2, and AC-4 evidence clauses. It also contains no
  complete pre-commit status, cached-name list, or `git commit --only -- <paths>` record; only the
  resulting exact commit membership is independently provable.
- **Match:** ⚠️ partial — outcomes hold, but two required provenance envelopes are incomplete.

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only` | PASS — 630 tests collected |
| 2 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | PASS — 629 passed, 1 skipped in 299.90 s |
| 3 | `python .tfw/scripts/gen_index.py --check project` | PASS — project consistent with declared release |
| 4 | `python -m mkdocs build --config-file docs/mkdocs.yml` | PASS — documentation built in 120.41 s; existing third-party/historical warnings remain |
| 5 | `git diff --check <Baseline> <Candidate> -- <four literal VALUE paths>` | PASS — exit 0 |
| 6 | Independent 17-case in-memory PyYAML contract validator | PASS — 17/17 expected accept/reject outcomes |
| 7 | `git diff --name-status --find-renames=50% -z <Baseline> <Candidate> -- <selector>` | PASS — four `M` records, exact literal membership |
| 8 | `git diff --numstat --find-renames=50% -z <Baseline> <Candidate> -- <selector>` | PASS — `41/13`, `18/16`, `14/11`, `70/32`; 143 + 72 = 215 touched text LOC; no binary row |
| 9 | `git merge-base --is-ancestor` for planning→approval→Candidate→TRACE tip | PASS — all exit 0 |
| 10 | `git log --reverse --name-status 1e2631b..bab2777` plus Candidate `diff-tree` | PASS — Candidate is the first VALUE commit, contains exactly four VALUE paths, and precedes EV/RF/RF-state TRACE |
| 11 | Candidate→TRACE-tip diff over the four VALUE paths | PASS — zero later VALUE paths |
| 12 | `Measure-Object -Word` on all four Baseline/Candidate blobs | PASS — `10547→10854`, `380→371`, `339→353`, `452→465` |
| 13 | SHA-256 of exact D79 and Phase A canonical ranges at both refs | PASS — `a7d9d69…cd06` and `ea39c941…cb80`, identical at both refs |
| 14 | Baseline `git grep -Il 'actor:' -- ':**/journal/*.md'` plus per-path Candidate blob comparison | PASS — 28 files, 0 missing, 0 mismatches |
| 15 | Blob-ID comparison for `gen_index.py`, `test_gen_index.py`, and `test_runtime_context.py` | PASS — all three match Baseline and the RF hashes |
| 16 | Governing-source search for `gen_index.py --check tasks`, `validate_event`, and `validate_new_event` | PASS — only two report-only config comments; no workflow, adapter, skill, or command receiver invocation |
| 17 | Baseline and Candidate archive replays of `gen_index.py --check tasks` | PASS — both exit 1 with the same sole RDP `123/120` warning, `63` tasks, and identical 17-stateless-phase information; temporary archives were removed |
| 18 | Existing profile/blob and real binding-path checks | PASS — unchanged four-key `saubakirov` profile; one profile; both external binding paths absent |
| 19 | Markdown-link and source-item audit for RF, EV, master/phase HL §7.2, and ONB §7 | PARTIAL — RF/EV links all resolve; master ordinals #2/#4 are stale; Phase B B9's source exists but its anchor is wrong |
| 20 | Added-line search for Phase C–E concepts and new-field consumer search | PASS — routing/team/provider terms occur only in explicit exclusions; no workflow/adapter/skill consumes the new profile fields |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | Four exact VALUE files and 215 touched LOC against an immutable 4-file/240-LOC denominator | RF §1; EV E-accounting | Primary Git name-status/numstat, approved TS at `1e2631b`, and commit ancestry | ✅ |
| C2 | 28 legacy `actor` blobs and reporter/test blobs are unchanged; report-only output has no delta | RF §4; EV E3/E5 | Primary Git blobs plus independent Baseline/Candidate archive runs | ✅ |
| C3 | Human/agent profile, event-writer, and binding contracts produce 17 expected outcomes | RF §4; EV E1–E4 | Candidate Markdown and independent in-memory PyYAML checker | ✅ behavior; ⚠️ Executor's exact validator program is not preserved |

All RF and EV Markdown citations resolve to real artifacts and anchors. All numeric claims above were
checked against Git or command output rather than another summary.

## Discrepancies Found

1. **Fixture-command provenance is incomplete.** EV says the exact shell form was captured, but the
   `$validator` definition is absent. `$validator | python -` cannot reproduce the reported run.
   This breaches the explicit Evidence clauses of TS AC-1, AC-2, and AC-4 even though an independent
   reconstruction confirms all 17 documented outcomes.
2. **Exact-path staging provenance is incomplete.** Candidate membership is exact and there is no
   contamination, but no durable complete pre-commit status, cached-name list, or
   `git commit --only -- <paths>` record exists for the Executor commits. The safe result is proven;
   the mandated commit procedure cannot be independently reconstructed.
3. **Two frozen-master citation ordinals are stale.** Master HL §7.2 #2 names Human authority as NS2
   principle 4, now principle 5; #4 names Assurance proportional to risk as principle 6, now 7. The
   quotations and applications remain semantically correct. This is the RF's disclosed observation.
4. **Phase HL citation B9 has a broken anchor.** It points to
   `#11-strategic-insights-planning`, while the real heading renders as
   `#11-strategic-insights-planning-free`. FA15ES S6 exists and supports the application, but the
   citation does not resolve.

The first discrepancy triggered and this log records 100% verification of all six claimed files.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|-----------------|------------------|----------------|
| E1 | EV E1 / AC-1 | ✅ | ⚠️ behavior and profile blob verified; required exact parser program absent |
| E2 | EV E2 / AC-2 | ✅ | ⚠️ semantics and outcomes verified independently; required exact parser program absent |
| E3 | EV E3 / AC-3 | ✅ | ✅ 28/28 legacy blobs, reporter/test blobs, consumer search, and diagnostic delta verified |
| E4 | EV E4 / AC-4 | ✅ | ⚠️ behavior and absent real bindings verified; required exact parser program absent |
| E5 | EV E5 / AC-5 | ✅ | ✅ boundaries, protected ranges, counts, and configured checks verified |
| E-accounting | EV E-accounting / AC-6 | ✅ | ✅ immutable lineage, membership, arithmetic, attribution, trigger, authority, and timing verified |

Evidence row total: 6; fully verified: 3; partially verified: 3; missing: 0. The EV's aggregate
`6/6 VERIFIED` status overstates command replayability for E1/E2/E4.

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | Master HL §7.2 #1 | PV0 NS1 Purpose | ✅ | ✅ | ✅ | ✅ |
| 2 | Master HL §7.2 #2 | PV0 NS2 “Human authority, bounded delegation,” cited as principle 4 | ✅ | ✅ | ❌ — quoted item is current principle 5; principle 4 is Selected Trace | ✅ — quotation supports the application |
| 3 | Master HL §7.2 #3 | PV0 NS3 vendor/runtime non-goal | ✅ | ✅ | ✅ | ✅ |
| 4 | Master HL §7.2 #4 | PV0 NS2 “Assurance proportional to risk,” cited as principle 6 | ✅ | ✅ | ❌ — quoted item is current principle 7; principle 6 is Continuation | ✅ — quotation supports the application |
| 5 | Master HL §7.2 #5–#7 | PV1 Structural Enforcement, Naming Creates Behavior, Portability | ✅ | ✅ | ✅ — checked separately from PV0 in the same README | ✅ |
| 6 | Master HL §7.2 #8–#9 | PV2 philosophy F37/F38 | ✅ | ✅ | ✅ | ✅ |
| 7 | Master HL §7.2 #10–#16, #33–#35 | PV3 D31/D54/D55/D59/D63/D64/D68/D73–D75 | ✅ | ✅ | ✅ | ✅ |
| 8 | Master HL §7.2 #17–#19 | PV4 HL/delegation/phase rules and anti-patterns | ✅ | ✅ | ✅ | ✅ |
| 9 | Master HL §7.2 #20 | PV5 convention F19 | ✅ | ✅ | ✅ | ✅ |
| 10 | Master HL §7.2 #21–#23, #36 | PV6 process F6/F7/F30/F39 | ✅ | ✅ | ✅ | ✅ |
| 11 | Master HL §7.2 #24–#31 | PV7 constraint F2/F11/F12, risk F1, stakeholder F6–F8, environment F3/F4 | ✅ | ✅ | ✅ | ✅ |
| 12 | Master HL §7.2 #32 | PV7 Assisted `team/README.md` | file path exists | ✅ | ✅ | ✅ as field evidence, not Full-schema authority |
| 13 | Phase HL §7.2 B1 | PV0 NS2 principle 5 | ✅ | ✅ | ✅ | ✅ |
| 14 | Phase HL §7.2 B2 | PV1 Naming Creates Behavior; Portability | ✅ | ✅ | ✅ | ✅ |
| 15 | Phase HL §7.2 B3 | PV2 philosophy F37 | ✅ | ✅ | ✅ | ✅ |
| 16 | Phase HL §7.2 B4 | PV3 D59/D68/D76/D77/D79 | ✅ | ✅ | ✅ | ✅ |
| 17 | Phase HL §7.2 B5 | PV4 Task control files / machine handle resolution | ✅ | ✅ | ✅ | ✅ |
| 18 | Phase HL §7.2 B6 | PV5 convention F19 | ✅ | ✅ | ✅ | ✅ |
| 19 | Phase HL §7.2 B7 | PV6 process F30/F38/F39/F46 | ✅ | ✅ | ✅ | ✅ |
| 20 | Phase HL §7.2 B8 | PV7 constraint F12 | ✅ | ✅ | ✅ | ✅ |
| 21 | Phase HL §7.2 B9 | Task evidence FA15ES HL §11 S6 | ❌ — wrong anchor | ✅ | ✅ | ✅ |
| 22 | ONB §7 #1–#45 | Confirmation/application of all 36 master and 9 phase citations | 44/45 source chains; #45 inherits B9 | ✅ 45/45 | ✅ 45/45 — #2/#4 explicitly correct the stale ordinals | ✅ 45/45 |

All P0–P4 sources were scanned in full; P5–P7 sources named above were read by relevance. Across 90
citation/application rows (45 governing + 45 ONB), 88 source chains resolve, 88 governing semantic
identifications pass, 0 are irrelevant, and 2 rows expose the same hallucinated B9 anchor. The two
master ordinal mismatches are semantic discrepancies rather than unresolved links.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈6 × 0.42⌉ files and recorded findings? (6/6 after escalation)
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Claim & Source Checks filled — 2-3 key claims spot-checked, every citation traced to a real artifact, data claims checked against a primary source (or explicit N/A with a reason)?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist, meanings match, applications are relevant)?
  - Total: 90 rows, resolved: 88, semantically verified: 88 governing/application identifications, irrelevant: 0, hallucinated: 2 rows / 1 underlying anchor
- [x] Evidence artifacts from RF §5 verified (files exist, claims match)?
  - Total evidence items: 6, fully verified: 3, partial: 3, missing: 0

Stage complete: YES
