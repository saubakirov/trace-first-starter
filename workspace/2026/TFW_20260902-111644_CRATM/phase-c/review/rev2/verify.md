# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed for Return Round 1: 6
> Files to verify: ⌈6 × 0.42⌉ = 3; verified: 6/6

## Verification Log

### V1: `.tfw/conventions.md`
- **RF claim:** rule 8 states the old and new guarantees; the two live §14 owner-signing readers are narrowed to valid rule-8 verdicts; named human exceptions survive.
- **Actual:** rule 8 says `Old: “only the owner rules.” New ordinary delegation: nearest eligible non-proposer, else governing owner.` It retains ordinary CL → owner, delegated nearest-eligible/fallback, owner-reserved and self-grant routes. §14 lines 1057 and 1059 now require the valid rule-8 verdict. Rules 9 and 10 retain the real-human owner-initiated and `RESTRICT`-on-filing exceptions.
- **Match:** ✅

### V2: `.tfw/workflows/plan.md`
- **RF claim:** §6d handles ordinary CL before delegated-prefix validation and keeps all downstream amendment outcomes.
- **Actual:** the first branch is `No delegation claimed`, requires only human status owner and signer, and routes directly to owner. The second branch requires all seven delegated facts and stops on gaps. Approved/rejected/`RESTRICT` outcomes remain present.
- **Match:** ✅

### V3: `.agent/workflows/tfw-plan.md`
- **RF claim:** accepted Plan copy is synchronized.
- **Actual:** byte-identical to canonical Plan; SHA-256 `3d7439e86191d4ad6a9b0417ba07aa7aca3f560a5e83c6a35f98d7400d987352`.
- **Match:** ✅

### V4: `.claude/commands/tfw-plan.md`
- **RF claim:** accepted Plan copy is synchronized.
- **Actual:** byte-identical to canonical Plan; SHA-256 `3d7439e86191d4ad6a9b0417ba07aa7aca3f560a5e83c6a35f98d7400d987352`.
- **Match:** ✅

### V5: `docs/scripts/test_integration.py`
- **RF claim:** current-source census rejects competing universal owner readers while preserving allowed human exceptions and all six workflow copies.
- **Actual:** the detector scans all six live consumers, exempts only a named `RESTRICT` no-owner-verdict line, rejects an injected owner-only §14 mutant, and the two direct integration checks pass.
- **Match:** ✅

### V6: `docs/scripts/test_runtime_context.py`
- **RF claim:** the real Plan consumer executes ordinary, delegated-nearest, missing-root and output-changing mutant cases without moving fixed caps.
- **Actual:** the parser reads the actual §6d bullet order. Direct execution produced ordinary CL `ROUTE → owner-human`, delegated `ROUTE → ruler-mid`, missing root `REFUSE`, and a Plan-source mutant that changes ordinary CL to `REFUSE` and is independently rejected. Both protected cap spans are byte-identical to the ruling tip.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `git switch --detach 10e6b0...`; object, ancestry and status checks | Returned tip resolved; prior REVIEW tip is an ancestor; initial reviewer tree was clean and detached. |
| 2 | `git diff f904e3a... 989240a... --` six exact return paths | Exactly 6 modified files; `184 insertions, 14 deletions`; source changes are the ruled conventions/Plan corrections plus assurance. |
| 3 | Independent NUL-safe `--name-status -z` / `--numstat -z`, Baseline → replacement Candidate, exact 12-path selector | Exactly 12 `M` VALUE records; 94 additions + 92 deletions = 186 touched LOC; no binary row. |
| 4 | Candidate membership, subject, parent and `merge-base --is-ancestor` replay | Candidate has exactly the six returned paths, parent `f904e3a...`, correct Executor subject; all exact lineage edges pass. |
| 5 | `git diff 989240a... 10e6b0a... --` exact 12 VALUE + 2 ASSURANCE paths | Empty: zero post-Candidate VALUE/ASSURANCE mutation. |
| 6 | Extract and execute complete `authority-validator-return-1`; hash actual stdout and recorded fence | 38 fixtures, 38 parity decisions, 10 authority mutants, 3 Plan cases, 1 Plan mutant; stdout 108192 / `71f852a...`; fence 108191 / `44e2878...`; `fence + LF == stdout`. |
| 7 | Direct actual-Plan consumer call with independent expected tuple checks | Ordinary CL → owner; delegated nearest → `ruler-mid`; missing root refuses; source mutant changes output and is rejected. |
| 8 | `pytest test_runtime_context.py -q -k "cratm_phase_c or ..."` | 8 passed, 171 deselected. |
| 9 | `pytest test_integration.py -q -k "cratm_phase_c"` | 2 passed, 95 deselected. |
| 10 | `pytest .tfw/scripts/ docs/scripts/ --collect-only -qq` | 638 collected (192 + 65 + 31 + 74 + 97 + 179). |
| 11 | `pytest .tfw/scripts/ docs/scripts/ -q` | 637 passed, 1 skipped in 336.71s. |
| 12 | `python .tfw/scripts/gen_index.py --check project` | Project consistent with framework 2.1.0. |
| 13 | Direct route/corpus projection and protected-cap span comparison | Active corpus 33310 ≤ 33749; every route and local cap passes; both cap spans unchanged since ruling. |
| 14 | `git diff --check` | No output; exit 0. |
| 15 | `python .tfw/scripts/gen_index.py --check tasks` after Reviewer state write | Report-only known lag reproduced: the older reader rejects current optional `writer` fields and the historical RDP event remains 123/120. The new event itself follows the current template (closed keys, valid `RF → KNW`, 73/120 summary); no Candidate, return-bound or state-schema breach was found. |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | Replacement Candidate was committed by one exact six-path command with clean post-status | EV §8.2; RF §§10.1–10.3 | Commit `989240a...`, parent `f904e3a...`, commit membership, subject and later path history | ✅ — transcript, object and graph agree; the earlier Candidate was not reconstructed. |
| C2 | Exact stdout and fenced representations differ by one terminal LF | EV §8.3; RF §10.2.5 | Fresh execution of the complete inline validator and fresh byte hashes | ✅ — 108192/`71f852...` and 108191/`44e2878...`; equality holds after LF. |
| C3 | Fixed cap/corpus and compatibility evidence remain valid | EV §8.5; RF §10.5 | Current source projection, ruling-tip AST span comparison, 638-item collection and full suite | ✅ — 33310 ≤ 33749, protected spans unchanged, 637 pass + 1 skip. |

All links and artifact citations in the cumulative RF, ONB and EV resolve. The replacement Candidate,
ruling, approval, Baseline, historical REVIEW and returned state tip are commit objects in one verified
ancestry chain. The cumulative EV's Return Round 1 section is readable and extractable; its seven
`VERIFIED` rows are Executor claims, each independently supported by the checks above.

Verification limit: repository-wide task checking is not green because of the explicitly known
RDP/current-`writer` reader lag. This is outside the returned VALUE/ASSURANCE Candidate and was
reported, not repaired. The project-structure check, targeted consumers and full configured suite
remain green.

## Discrepancies Found

No discrepancies.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | EV §8.1 R1-E1 — Plan ordinary-CL branch | ✅ | ✅ — actual consumer and direct call route to owner before delegated validation. |
| E2 | EV §8.1 R1-E2 — authority fixtures/mutants | ✅ | ✅ — fresh complete validator reports 38/38 decisions and 10/10 mutants. |
| E3 | EV §8.1 R1-E3 — human exceptions/current census | ✅ | ✅ — zero universal readers; rule 9, rule 10, reserved/self-grant and purpose routes remain. |
| E4 | EV §8.1 R1-E4 — copies and Plan mutant | ✅ | ✅ — six copy relations pass and the actual-source mutant changes output. |
| E5 | EV §8.1 R1-E5 — caps, corpus and suite | ✅ | ✅ — fixed caps, 33310/33749 corpus, 638 collection and 637/1 suite reproduced. |
| E6 | EV §8.1 R1-E6 — Candidate capture and no later VALUE | ✅ | ✅ — exact six-member commit and empty post-Candidate 12+2 diff. |
| E7 | EV §8.1 R1-E-accounting — immutable accounting | ✅ | ✅ — exact 12 VALUE, 94 + 92 = 186, approval/Baseline/ruling/Candidate and authority unchanged. |

Evidence totals: 7 items, 7 independently verified, 0 missing, 0 mismatched.

## Knowledge Citations Verified

PV priorities 0–4 were scanned in full; priorities 5–7 were scanned for every cited relevant item.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | HL §7.2 C1 | P0 — NS1 Purpose + NS3 Non-goals | ✅ | ✅ | ✅ — continuity, human control, no replacement runtime | ✅ — authority remains human-rooted and provider-neutral. |
| 2 | HL §7.2 C2 | P1 — Methodology values + Success Criteria | ✅ | ✅ | ✅ — structural enforcement, visible trace, usable result | ✅ — refusal and signed-ruler behavior is executable and tested. |
| 3 | HL §7.2 C3 | P2 — `philosophy.md` F37 | ✅ | ✅ | ✅ — mandate is a ceiling, never new permission | ✅ — self-grant/self-ruling route to owner. |
| 4 | HL §7.2 C4 | P3 — D59, D63, D73–D77, D79–D80 | ✅ | ✅ | ✅ — boundaries, contract, context, VALUE, worktrees, session/principal identity | ✅ — prior contracts and exact Candidate boundaries remain intact. |
| 5 | HL §7.2 C5 | P4 — HL Contract / REVISE route / Role Lock / anti-patterns | ✅ | ✅ | ✅ — canonical authority and enforcement sites | ✅ — one rule-8 resolver is consumed at actual boundaries. |
| 6 | HL §7.2 C6 | P5 — `convention.md` F5 | ✅ | ✅ | ✅ — canonical workflow owns copies | ✅ — all six accepted copy relations are byte-identical. |
| 7 | HL §7.2 C7 | P6 — `process.md` F30/F36/F38/F46 | ✅ | ✅ | ✅ — enforcement site, complete release, pre-act bound, sequencing | ✅ — return ships source, copies, tests and trace together. |
| 8 | HL §7.2 C8 | P7 — `constraint.md` F2/F12/F14 | ✅ | ✅ | ✅ — attention, file-owned obligations, separate review act | ✅ — fixed caps hold and Reviewer remains independent. |
| 9 | HL §7.2 C9 | P7 — `risk.md` F1 | ✅ | ✅ | ✅ — broad staging demonstrated unsafe | ✅ — captured `commit --only` uses six full paths. |
| 10 | HL §7.2 C10 | P7 — `stakeholder.md` F6 | ✅ | ✅ | ✅ — avoid both constant interruption and drift | ✅ — ordinary owner fallback and bounded delegation coexist. |
| 11 | ONB §7 #1 | C1 — NS1 Purpose + NS3 Non-goals | ✅ | ✅ | ✅ | ✅ — implementation follows the cited application. |
| 12 | ONB §7 #2 | C2 — Methodology values + Success Criteria | ✅ | ✅ | ✅ | ✅ — behavior is observable in source-derived tests. |
| 13 | ONB §7 #3 | C3 — `philosophy.md` F37 | ✅ | ✅ | ✅ | ✅ — grant remains a ceiling. |
| 14 | ONB §7 #4 | C4 — D59/D63/D73–D77/D79–D80 | ✅ | ✅ | ✅ | ✅ — no prior contract is regressed. |
| 15 | ONB §7 #5 | C5 — convention authority ranges | ✅ | ✅ | ✅ | ✅ — edits land only at the canonical and live reader sites. |
| 16 | ONB §7 #6 | C6 — `convention.md` F5 | ✅ | ✅ | ✅ | ✅ — tracked Plan copies are synchronized. |
| 17 | ONB §7 #7 | C7 — `process.md` F30/F36/F38/F46 | ✅ | ✅ | ✅ | ✅ — complete consumer/evidence delivery and sequencing hold. |
| 18 | ONB §7 #8 | C8 — `constraint.md` F2/F12/F14 | ✅ | ✅ | ✅ | ✅ — repository-owned obligations and review boundary hold. |
| 19 | ONB §7 #9 | C9 — `risk.md` F1 | ✅ | ✅ | ✅ | ✅ — exact-path Candidate capture is present. |
| 20 | ONB §7 #10 | C10 — `stakeholder.md` F6 | ✅ | ✅ | ✅ | ✅ — routine delegation does not erase human exceptions. |

Citation totals: 20, resolved 20, semantically verified 20, irrelevant 0, hallucinated 0.
`KNOWLEDGE.md` §1, including D73–D80, contains no contradiction with the returned changes.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈6 × 0.42⌉ files and recorded findings? 6/6.
- [x] Ran at least 1 build/test command? Targeted, integration, collection, full suite and project checks ran.
- [x] Claim & Source Checks filled with primary commit/source/runtime evidence?
- [x] Each RF §3/§10.4 AC checkmark verified against actual files?
- [x] KNOWLEDGE.md checked; no contradiction found?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: 20, resolved: 20, semantically verified: 20, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 7, verified: 7, missing: 0

Stage complete: YES
