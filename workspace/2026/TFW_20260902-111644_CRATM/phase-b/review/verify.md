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

## Round 2 — Verification Update

> Returned Executor TRACE tip: `c4ebd9077295b031460426dc2c71819409d494d6`
> Coordinator ruling: `3bc14ef3980a24ceae3b679db02deb15dc4f9225`
> Returned files after ruling: 7 TRACE paths
> Minimum at 0.42: ⌈7 × 0.42⌉ = 3; inspected: 7/7 plus the ruled live REVIEW

### R2-V1: Preserved validator and full fixtures

- **RF claim:** EV Round 2 contains one complete executable program with the 17 full documented YAML
  payloads and expected outcomes; its fresh run returns 17/17 and exit 0.
- **Actual:** The unique `ROUND2_VALIDATOR_START/END` fence was extracted exactly and piped to
  Python. AST inspection found 17 literal, non-empty YAML payload strings in the expected order:
  11 profile, 4 event, and 2 binding cases. Every payload parses to a complete mapping. The run
  printed 17 PASS rows plus `RESULT 17/17 passed` and exited 0. Program SHA-256 is
  `1c375695ac39e429f262f3e70cadd0aedbd98ac21b996554e918d745b30fbfb2`.
- **Match:** ✅

### R2-V2: Recorded output and external-state boundary

- **RF claim:** The actual and recorded observation have 21 lines with delta 0; both documented real
  binding paths remain absent.
- **Actual:** The program's 18 stdout lines plus independently observed `validator_exit=0`,
  `windows_binding_exists=False`, and `posix_binding_exists=False` match the EV's 21-line block in
  order with `Compare-Object` delta 0. Both
  `C:\Users\c0rpa\AppData\Local\tfw\bindings.yaml` and
  `C:\Users\c0rpa\.tfw\bindings.yaml` are absent after replay. No fixture file was created.
- **Match:** ✅

### R2-V3: Preservation and execution honesty

- **RF claim:** Round 2 appends current evidence without rewriting or retrospectively attributing the
  unpreserved pre-Candidate validator bytes or staging transcript.
- **Actual:** Ruling→tip numstat is additive for ONB `70/0`, RF `29/0`, and EV `367/0`; the original
  records remain byte content within their cumulative files. ONB, RF, EV, and the ruling each state
  that the program is reconstructed current evidence and that historical validator/staging bytes are
  unavailable. Search finds no manufactured status/cached-name/`commit --only` transcript; the four
  returned commits themselves have exact, uncontaminated TRACE memberships and task/phase/role
  subjects.
- **Match:** ✅ — the first-round limitation remains explicit and is not claimed closed.

### R2-V4: Candidate, governing artifacts, and returned boundary

- **RF claim:** Candidate is unchanged/reachable, there is no later VALUE, and HL/TS/live REVIEW are
  unchanged after the Coordinator ruling.
- **Actual:** Approval→Candidate→first REVIEW→ruling→tip ancestry all exit 0; the ruling's exact parent
  is first REVIEW commit `e1e8816ffa187f90f5524b9585a2564e37cf3f00`. Candidate→tip diff and
  history over the four literal VALUE paths are empty. Baseline→Candidate still yields four `M`
  records and `143 + 72 = 215` touched text LOC. At ruling and tip, blob IDs are identical for Master
  HL `39975c4…`, Phase HL `f89ecd4…`, governing TS `e353f01…`, and live first REVIEW `f8b50ca…`;
  the TS blob also equals the approval blob. Returned changes are exactly ONB, RF, EV, phase status,
  and three journal events.
- **Match:** ✅

### R2-V5: Coordinator rulings and lifecycle trace

- **RF claim:** The same Executor followed the one accepted rung-1 bound; all four first-round
  disposition proposals are terminally ruled.
- **Actual:** Live REVIEW records item 1 as accepted rung 1, item 2 as `not material — owed but
  forbidden to pay retrospectively`, and items 3–4 as `promoted — TFW_20260902-111644_CRATM`.
  Item 1's observable evidence condition now holds. The promoted task directory, `status.md`, and
  proposal exist; proposal §6 item 9 plus frozen Phase E deliverable 6/DoD 17 own the citation-debt
  sweep. Phase B trace records `RF → ONB → RF` with the same human principal/tool identity, and status
  is currently `RF`.
- **Match:** ✅

### Round 2 Commands Executed

| # | Command | Result |
|---|---|---|
| R2-1 | Extract unique EV validator fence and pipe the exact body to `python -` | PASS — 17 PASS rows, `RESULT 17/17 passed`, exit 0 |
| R2-2 | AST/PyYAML inspection of all literal fixture tuples | PASS — 17/17 full non-empty YAML mappings; expected name/order/outcome list matches the 17-row Round 1 matrix |
| R2-3 | Compare program output plus exit/path facts with the recorded output block | PASS — actual 21 lines, recorded 21 lines, delta 0 |
| R2-4 | `git merge-base --is-ancestor` across approval→Candidate→REVIEW→ruling→tip | PASS — all exit 0; ruling parent is exact first REVIEW |
| R2-5 | Candidate→tip diff and log over four literal VALUE paths | PASS — empty diff; zero later VALUE commits |
| R2-6 | Approved NUL-safe Baseline→Candidate name-status/numstat replay | PASS — four `M` files; 143 additions, 72 deletions, 215 touched LOC; no binary row |
| R2-7 | Blob comparison at ruling→tip for Master HL, Phase HL, TS, and live REVIEW | PASS — all four pairs identical; approval/ruling TS blob also identical |
| R2-8 | `git diff --check <ruling> <tip>` | PASS — exit 0 |
| R2-9 | `python .tfw/scripts/gen_index.py --check project` | PASS — project consistent with declared release |
| R2-10 | Real Windows/POSIX binding existence checks | PASS — both absent |

### Round 2 Claim & Source Checks

| # | Claim / citation checked | Where it appears | Primary source | Holds? |
|---|---|---|---|---|
| R2-C1 | Complete replayable evidence closes AC-1/AC-2/AC-4 | RF Round 2; EV E-fixtures-R2 | Exact fenced Python program, 17 full literal YAML payloads, independent output and exit status | ✅ |
| R2-C2 | Candidate and VALUE accounting remain immutable | RF §1/Round 2; EV Round 2 | Primary Git ancestry, NUL-safe diff output, Candidate commit tree, Candidate→tip path history | ✅ |
| R2-C3 | Every first-round proposal was ruled at an existing legal target | Live REVIEW Coordinator rulings | Ruling commit `3bc14ef…`; master task status/proposal; frozen Phase E deliverable 6 and DoD 17 | ✅ |

### Round 2 Discrepancies

No new discrepancy. The preserved program itself emits 18 lines; the 21-line evidence block also
contains three separately observed shell facts (exit and two path checks). Reviewer verification
keeps those sources distinct and reproduces the combined block exactly. The unpreserved historical
validator bytes and pre-commit transcript remain unavailable by the accepted item-2 disposition;
Round 2 neither claims nor manufactures them.

### Round 2 Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|---|---|---|
| E-fixtures-R2 | EV Round 2 / AC-1, AC-2, AC-4 | ✅ | ✅ exact program extracted; 17 complete fixtures; 17/17; exit 0; 21/21 combined evidence lines; binding paths absent |
| E1/E2/E4 | Cumulative first-round rows plus E-fixtures-R2 | ✅ | ✅ current behavior and replayability established; historical limitation preserved |
| E3/E5/E-accounting | Unchanged cumulative rows | ✅ | ✅ first-round verification remains applicable; Candidate→tip VALUE and protected-artifact checks confirm no invalidating change |

Current cumulative evidence total: 7 rows; fully verified: 7; missing: 0; deferred: 0; blocked: 0.

### Round 2 Knowledge Citations

The same Reviewer's first-round 90-row audit remains current. Every P0–P4 and relevant P5–P7 source
blob is identical at first REVIEW `e1e8816…` and returned tip `c4ebd90…`; ONB only appends §8 and
does not alter its 45-row citation table. Therefore the prior totals remain exact: 88/90 source chains
resolve, 88/90 semantic identifications are exact, 0 are irrelevant, and 2 rows share the one known
B9 bad anchor. The two stale master ordinals and B9 anchor are not hidden: Coordinator terminally
promoted them to the existing master task's Phase E sweep. No new knowledge citation was introduced.

### Round 2 Checkpoint

- [x] Opened all 7 returned TRACE paths plus the ruled live REVIEW?
- [x] Executed the exact preserved validator and inspected all 17 complete payloads?
- [x] Verified recorded output, exit status, external-state boundary, and current evidence sufficiency?
- [x] Replayed immutable Candidate/accounting and proved no later VALUE?
- [x] Verified first-round limitation and item-2 non-fabrication rather than reconstructing history?
- [x] Verified all four Coordinator rulings and their existing targets?
- [x] Confirmed P0–P7 source blobs/citation table unchanged and carried forward the exact audit result?

Round 2 stage complete: YES
