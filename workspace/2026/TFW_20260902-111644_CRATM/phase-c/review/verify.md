# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: `0.42`
> RF files claimed: `14` Candidate files (`12` VALUE + `2` ASSURANCE)
> Files to verify: `ceil(14 × 0.42) = 6`; one discrepancy escalated the review to `14/14`.

## Verification Log

### V1: `.tfw/conventions.md`
- **RF claim:** Sole human-rooted authority resolver, compatible Rung 3, preserved exceptions, and complete Phase C prohibitions.
- **Actual:** Rule 8 contains the resolver and the named exceptions. Rung 3 consumes it. However, rule 8 does not state the guarantee it replaced, while live anti-patterns at lines 1057 and 1059 still use owner-signing language. EV classifies those sites as `live; narrowed`, not as one of AC-4's four permitted classifications.
- **Match:** ❌

### V2: `.tfw/workflows/plan.md`
- **RF claim:** Preserves proposer, invokes rule 8, validates authority/signature, and stops only on unresolved amendment authority.
- **Actual:** Iteration routing preserves proposer and cites rule 8. Step 6d nevertheless unconditionally asks for `separate root authorization` and a `child-only chain`, then stops on missing facts; it has no ordinary-CL/no-delegation branch even though rule 8 routes that case directly to the owner.
- **Match:** ❌

### V3: `.tfw/workflows/review.md`
- **RF claim:** Uses shared Rung-3 authority and retains Purpose, contract-defect, and REJECT owner routes.
- **Actual:** The Rung-3 route cites rule 8, preserves proposer, and stops the Reviewer; Purpose/contract-defect and REJECT remain human-owner routes.
- **Match:** ✅

### V4: `.tfw/workflows/handoff.md`
- **RF claim:** Requires a valid terminal rule-8 verdict and keeps resolution outside Executor authority.
- **Actual:** Rung 3 accepts only after rule 8 resolves a terminal verdict and explicitly refuses Executor resolution.
- **Match:** ✅

### V5: `.tfw/templates/HL.md`
- **RF claim:** §12 records origin, ruler/signature, direct-owner act, reserved/self-grant returns, and RESTRICT.
- **Actual:** The template records originating proposer, resolved ruler, signer, owner-only exceptions, and filing-only RESTRICT as claimed.
- **Match:** ✅

### V6: `.tfw/templates/RES.md`
- **RF claim:** Research remains non-ruling; Coordinator transcribes preserved origin and routes under rule 8.
- **Actual:** The template separates refinements from amendment proposals, preserves origin, and requires a rule-8 resolved-ruler verdict.
- **Match:** ✅

### V7: `.agent/workflows/tfw-plan.md`
- **RF claim:** Byte-identical accepted Plan receiver.
- **Actual:** SHA-256 `a73290e9504ee95e267758064fdfafd5a68b263a29ef67503935a374fbcd48d2`, equal to canonical Plan. It faithfully copies V2's defect.
- **Match:** ⚠️ partial

### V8: `.agent/workflows/tfw-review.md`
- **RF claim:** Byte-identical accepted Review receiver.
- **Actual:** SHA-256 `0082008bd307635a7d6632d078ddc7753d1881c7782a69a51b489c8b2fae58ce`, equal to canonical Review.
- **Match:** ✅

### V9: `.agent/workflows/tfw-handoff.md`
- **RF claim:** Byte-identical accepted Handoff receiver.
- **Actual:** SHA-256 `5c1faf2f0b61935a1273071ea5d7e8f49cacedb98580a2f67c071fdab2cd676d`, equal to canonical Handoff.
- **Match:** ✅

### V10: `.claude/commands/tfw-plan.md`
- **RF claim:** Byte-identical accepted Plan receiver.
- **Actual:** Same canonical Plan SHA-256 and bytes. It faithfully copies V2's defect.
- **Match:** ⚠️ partial

### V11: `.claude/commands/tfw-review.md`
- **RF claim:** Byte-identical accepted Review receiver.
- **Actual:** Same canonical Review SHA-256 and bytes.
- **Match:** ✅

### V12: `.claude/commands/tfw-handoff.md`
- **RF claim:** Byte-identical accepted Handoff receiver.
- **Actual:** Same canonical Handoff SHA-256 and bytes.
- **Match:** ✅

### V13: `docs/scripts/test_runtime_context.py`
- **RF claim:** Source-derived full authority payloads, resolver projections, independent expected outcomes, and output-changing mutants.
- **Actual:** The module defines 38 payloads and ten mutants; targeted tests pass. Its `ordinary_cl` case reaches the helper's early `if not claim_delegated: return owner` branch and therefore does not exercise the actual Plan 6d consumer text that omits this branch.
- **Match:** ⚠️ partial

### V14: `docs/scripts/test_integration.py`
- **RF claim:** Consumer/copy coherence plus independent detection of a surviving universal owner-only route.
- **Actual:** Copy parity and injected Handoff mutant checks pass. `_cratm_authority_consumer_errors()` is a required-substring check and the owner-only contradiction detector covers Plan/Handoff/Review, not the live conventions §14 anti-patterns or the ordinary-CL Plan branch.
- **Match:** ⚠️ partial

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `git rev-parse --verify <each ref>^{commit}` + `git merge-base --is-ancestor` for approval/Baseline/Candidate/EV/RF/state chain | PASS; every ref is a commit and every declared ancestry edge exits 0. |
| 2 | NUL-safe `git diff --name-status --find-renames=50% -z` and `--numstat ... -z` over the literal 12-path VALUE selector | PASS; 12 `M` records, 89 additions, 90 deletions, 179 touched text LOC. |
| 3 | `git show --name-status b2a963...` | PASS; Candidate contains exactly 12 VALUE + 2 ASSURANCE files and subject `[codex/TFW_20260902-111644_CRATM/phase-c/executor] implement authority routing`. |
| 4 | `git diff` / `git log` from Candidate through `f36c426...` over the 12 VALUE paths | PASS; no later VALUE change/history. |
| 5 | Six canonical/copy SHA-256 and byte comparisons | PASS; all six pairs equal. |
| 6 | In-memory rule-8/Plan-6d branch probe | `RULE8_DIRECT_ORDINARY_CL=True`; `PLAN6D_HAS_ORDINARY_CL_BRANCH=False`; Plan lists separate-root + child-only facts and stops when missing. |
| 7 | Baseline/current rule-8 comparison | Baseline says only an explicit owner verdict rules; current 1,320-character rule has no `formerly`/`previously`/`replaced`/owner-only statement. |
| 8 | Live `owner|ruler|verdict` census over current contract/workflows/templates plus EV classification replay | Two §14 sites remain current and are classified `live; narrowed`, outside AC-4's allowed classification set. |
| 9 | Seven targeted Phase C authority/integration tests | PASS — `7 passed in 154.45s`. |
| 10 | `python -m pytest .tfw/scripts/ docs/scripts/ --collect-only -qq` | PASS — `192 + 65 + 31 + 74 + 97 + 177 = 636` collected. |
| 11 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | PASS — `635 passed, 1 skipped in 358.87s`. |
| 12 | `python -m mkdocs build --config-file docs/mkdocs.yml -q` | PASS, exit 0; inherited unresolved-reference warnings do not name Phase C. |
| 13 | `python .tfw/scripts/gen_index.py --check project` | PASS — framework 2.1.0, one participant, project consistent. |
| 14 | `git diff --check <Baseline> <Candidate> -- <exact 14 paths>` | PASS; no output. |
| 15 | Execute the EV's extracted 503-line program and compare stdout to recorded fenced JSON | PASS for 3,788-line content after removing the terminal newline; actual stdout SHA-256 is `260d571f...`, while claimed `1a0445cb...` is the fenced content without that newline. |
| 16 | Search RF/EV for cached-name/status/`git commit --only` transcript | `NO_CONTEMPORANEOUS_STAGING_TRANSCRIPT_IN_RF_OR_EV`; ONB contains only the prospective intention. |
| 17 | Inspect `.tfw/README.md` explicit anchors and HL C1/C2 fragments | PASS — the source declares `<a id="ns1"></a>` and `<a id="methodology-values"></a>`; both fragments resolve. |
| 18 | Broad `python -m pytest -q` from repository root | Collection stops on duplicate `docs/scripts` / generated `site/scripts` module basenames; not the configured suite and not attributed to Candidate. |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | “every live owner-only occurrence is classified” | RF §3 AC-4 / EV census | Current `.tfw/conventions.md` lines 1057, 1059 and EV's classification table | ❌ — both are current; `live; narrowed` is not an allowed AC-4 class. |
| C2 | “ordinary CL compatibility” | RF §3 AC-1 | Rule 8, Plan 6d, runtime-context helper | ❌ — the source resolver has the route, but Plan 6d omits it and the test helper bypasses Plan. |
| C3 | “rule 8 states the current guarantee and the one it replaced” | Frozen master DoD 10 / Phase C deliverable 3 | Baseline rule 8 and Candidate rule 8 | ❌ — the prior owner-only guarantee is absent from Candidate rule 8. |
| C4 | `12` VALUE files and `89 + 90 = 179` | RF §1 / EV E-accounting | NUL-safe Git diff at immutable Baseline/Candidate | ✅ |
| C5 | `635 passed, 1 skipped`; 636 collected | RF §4 / EV E5 | Independently repeated configured pytest commands | ✅ |
| C6 | 503-line program reproduces recorded 3,788-line output “byte-for-byte” with SHA `1a0445...` | RF §4 / EV raw validator | Direct extraction/execution and SHA-256 | ❌ — content matches only after stripping stdout's final LF; raw stdout SHA is `260d571f...`. |
| C7 | Exact-path staging remains visible | RF AC-6 claim / TS AC-6 and Technical Guidance | Candidate membership/subject plus RF/EV search | ❌ — exact commit membership and role attribution are visible, but no contemporaneous full-status, cached-name, pathspec, or `commit --only` transcript exists. |

## Discrepancies Found

1. **AC-4 / frozen master DoD 9–11:** two current §14 owner-only enforcement sentences survive under the non-contract classification `live; narrowed`; rule 8 does not textually redefine `owner verdict` as a generic ruler-signed channel.
2. **Frozen master Phase C deliverable 3 / DoD 10:** Candidate rule 8 states the new route but omits the prior “only owner rules” guarantee, so the intended weakening is not legible in the canonical rule itself.
3. **AC-1 and AC-4:** Plan 6d makes delegated-chain facts unconditional and lacks the required ordinary-CL/no-delegation direct-owner branch. Existing assurance passes because its helper short-circuits before consuming Plan 6d.
4. **AC-6 / HC-C1 / Technical Guidance:** Candidate membership and role attribution are reconstructible, but the required contemporaneous full-status, cached-name, exact pathspec, and `git commit --only` evidence is absent from RF/EV.
5. **Evidence accuracy:** the validator payload is reproducible, but “byte-for-byte output” and its SHA refer to fenced content without stdout's terminal LF, not the raw program output.
Any one discrepancy triggered 100% verification; all 14 Candidate files were inspected.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | `evidence/EV__phase-c__authority_routing.md` | ✅ | ❌ — payload content, tests, accounting, lineage, counts, and copy parity reproduce; AC-1/AC-4/AC-6 conclusions and the raw-output hash wording do not fully match the underlying sources. |

## Knowledge Citations Verified

PV 0–4 were scanned in full. PV 5–7 were scanned in the cited/relevant files and items. Every cited link resolves, every cited item exists, and every meaning is relevant.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | HL §7.2 C1 | PV 0 — NS1 Purpose and NS3 Non-goals | ✅ — explicit `#ns1` anchor | ✅ | ✅ | ✅ |
| 2 | HL §7.2 C2 | PV 1 — Methodology values and Success Criteria | ✅ | ✅ | ✅ | ✅ |
| 3 | HL §7.2 C3 | PV 2 — `philosophy.md` F37 | ✅ | ✅ | ✅ | ✅ |
| 4 | HL §7.2 C4 | PV 3 — D59, D63, D73–D77, D79–D80 | ✅ | ✅ | ✅ | ✅ |
| 5 | HL §7.2 C5 | PV 4 — conventions named ranges | ✅ | ✅ | ✅ | ✅ |
| 6 | HL §7.2 C6 | PV 5 — `convention.md` F5 | ✅ | ✅ | ✅ | ✅ |
| 7 | HL §7.2 C7 | PV 6 — `process.md` F30, F36, F38, F46 | ✅ | ✅ | ✅ | ✅ |
| 8 | HL §7.2 C8 | PV 7 — `constraint.md` F2, F12, F14 | ✅ | ✅ | ✅ | ✅ |
| 9 | HL §7.2 C9 | PV 7 — `risk.md` F1 | ✅ | ✅ | ✅ | ✅ |
| 10 | HL §7.2 C10 | PV 7 — `stakeholder.md` F6 | ✅ | ✅ | ✅ | ✅ |
| 11 | ONB §7 row 1 | C1 — NS1 Purpose and NS3 Non-goals | ✅ — resolves through HL C1 | ✅ | ✅ | ✅ |
| 12 | ONB §7 row 2 | C2 — Methodology values and Success Criteria | ✅ | ✅ | ✅ | ✅ |
| 13 | ONB §7 row 3 | C3 — `philosophy.md` F37 | ✅ | ✅ | ✅ | ✅ |
| 14 | ONB §7 row 4 | C4 — D59, D63, D73–D77, D79–D80 | ✅ | ✅ | ✅ | ✅ |
| 15 | ONB §7 row 5 | C5 — conventions named ranges | ✅ | ✅ | ✅ | ✅ |
| 16 | ONB §7 row 6 | C6 — `convention.md` F5 | ✅ | ✅ | ✅ | ✅ |
| 17 | ONB §7 row 7 | C7 — `process.md` F30, F36, F38, F46 | ✅ | ✅ | ✅ | ✅ |
| 18 | ONB §7 row 8 | C8 — `constraint.md` F2, F12, F14 | ✅ | ✅ | ✅ | ✅ |
| 19 | ONB §7 row 9 | C9 — `risk.md` F1 | ✅ | ✅ | ✅ | ✅ |
| 20 | ONB §7 row 10 | C10 — `stakeholder.md` F6 | ✅ | ✅ | ✅ | ✅ |

## Checkpoint

**Self-check:**
- [x] Opened ≥ `ceil(14 × 0.42)` files and recorded findings? `14/14`.
- [x] Ran at least 1 build/test command? Configured full suite, targeted tests, MkDocs, structure, diff hygiene, and independent probes ran.
- [x] Claim & Source Checks filled — key claims, every citation, and primary Git/test sources checked?
- [x] Each RF §3 AC checkmark verified against actual files? AC-2 and AC-3 hold; AC-1, AC-4, AC-5 dependency, and AC-6 do not fully hold.
- [x] KNOWLEDGE.md checked — contradictions with changes documented? No D59/D63/D73–D80 regression found; the contradictions are with Phase C's own master/TS requirements.
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: `20`, resolved: `20`, semantically verified: `20`, irrelevant: `0`, hallucinated/unresolved: `0`.
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: `1`, fully verified: `0`, missing: `0`, partially matching: `1`.

Stage complete: YES
