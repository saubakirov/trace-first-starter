# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 12
> Files to verify: ⌈12 × 0.42⌉ = 6; escalated on discrepancy to 12/12 (100%)

## Verification Log

### V1: `.tfw/workflows/plan.md`
- **RF claim:** canonical Plan is a 1,199-word pure returning-work inspector/router with total routing, identity re-resolution, no lifecycle effects, and exact Coordinator control.
- **Actual:** the Candidate blob has 1,199 strict UTF-8 Unicode `\S+` words and contains the intended pre-route, lifecycle table, identity boundary, no-mutation declaration, and fixed Coordinator-control address before Step 2. Its shipped text is consistent with the TS, but the assurance does not semantically bind several rows or effect prohibitions to the model it reports.
- **Match:** ⚠️ partial

### V2: `.agents/workflows/tfw-plan.md`
- **RF claim:** exact Antigravity full-copy receiver.
- **Actual:** SHA-256 `47c79864b215c176e170da39e2b26067ecb04d60c894440c992e47b7e12b5749`, byte-identical to canonical Plan at Candidate.
- **Match:** ✅

### V3: `.claude/commands/tfw-plan.md`
- **RF claim:** exact Claude full-copy receiver.
- **Actual:** SHA-256 `47c79864b215c176e170da39e2b26067ecb04d60c894440c992e47b7e12b5749`, byte-identical to canonical Plan at Candidate.
- **Match:** ✅

### V4: `docs/scripts/test_runtime_context.py`
- **RF claim:** source-derived exact 28-case route model, ten identity cases, no-mutation checks, and semantic mutants.
- **Actual:** 28 route cases and ten identity labels exist and the suite passes, but `resolve_rwnr_route()` consumes a hard-coded case object rather than the temporary repository created by `_rwnr_materialize_case()`. The snapshot therefore surrounds a function that cannot access or mutate that repository. The contract checker searches for a small token set and the model returns hard-coded expected routes. Three independent semantic mutations—`RES` routed to Handoff, a same-principal child changed from `PLAN` to `LEAD`, and an inserted instruction to write `status.md`—all returned `contract_errors=[]` while the model continued returning the original correct outputs. Identity inputs/readback/mutation are likewise fixed strings rather than authoritative state/journal/dispatch observations.
- **Match:** ❌

### V5: `docs/scripts/test_repository_contracts.py`
- **RF claim:** Candidate accounting, receiver migration, history preservation, parity/scope, and unchanged-Resume assurance.
- **Actual:** accounting, parity, history and exact Candidate-scope checks reproduce. The receiver model applies one adapter at a time and classifies config separately; it has no all-subject connected-group preflight. With Antigravity old-exact and Claude foreign, Antigravity is modified before Claude refuses, so the combined group is not unchanged. The Phase A receiver test therefore does not prove the AC-5 all-preflight condition.
- **Match:** ❌

### V6: `ONB__phase-a__continuation_responsibilities.md`
- **RF claim:** no blocking questions; exact authority, scope and citation application established before execution.
- **Actual:** the owner-approved TS, `3/900` denominator, Executor unit/address/parent, exact dispatch, C1 fallback, and all 33 inherited citation applications are recorded. No unresolved ONB blocker is visible.
- **Match:** ✅

### V7: `evidence/phase-a-routing.json`
- **RF claim:** 28 exact routes/no-mutation scenarios, ten identity cases, and seven rejecting semantic mutant families.
- **Actual:** it contains 28 scenario rows, ten identity rows and seven mutant rows, all bound to Candidate. The records are outputs from the hard-coded model above; `mutation` is the literal string `none`, not a before/after hash, and rows do not carry the required source state/lineage inputs or repository snapshot identities. The receipt does not expose the three false-green mutations found independently.
- **Match:** ❌

### V8: `evidence/phase-a-receiver-migration.json`
- **RF claim:** all five outcome classes, connected-group refusal, four-adapter ten-command convergence, and empty second runs.
- **Actual:** all five labels and four adapter-local first/second runs are present; absent Cursor, foreign Claude, unmarked root and config classifications are represented. `foreign_claude.group_unchanged=true` covers only that isolated receiver after other adapter trials, not the connected retirement group required by AC-5; a cross-adapter foreign case changes the group before refusal.
- **Match:** ❌

### V9: `evidence/phase-a-history.json`
- **RF claim:** exact 179-entry task manifest and three ordered raw-line aggregate subsequences.
- **Actual:** independent Git-object regeneration yields 205 selected paths = 23 live + 179 task + 3 aggregate, digest `ed52c4c26845e90c14a569f867ec2200b18da44374f7df2fd897bf7fb58bef96`, unchanged task tree entries, and valid subsequences for the three named baseline blobs.
- **Match:** ✅

### V10: `evidence/phase-a-accounting.json`
- **RF claim:** immutable Baseline/Candidate accounting, `3/747`, Plan/C 1,199, parity, no other instruction source, and no trigger.
- **Actual:** independent Git-object and strict-UTF-8 recomputation reproduces Baseline blobs `81f7d78…`/`31f3159…`, `2,021 + 716 = 2,737`, three rows of `85 + 164`, total `255 + 492 = 747`, Plan/C 1,199, exact copy parity, and no other changed surviving instruction source after generated-copy exclusion.
- **Match:** ✅

### V11: `evidence/phase-a-tests.txt`
- **RF claim:** raw targeted/configured test, scope, parity, accounting and unchanged-Resume output.
- **Actual:** the recorded commands/results are internally consistent: 355 targeted passes, 625 collected, 624 passes plus one platform skip, exact five Candidate paths, `3/747`, parity, and empty Candidate Resume-path diff. The exact 355-test Candidate rerun independently passes in 280.84s. A green run is insufficient for AC-2–AC-5 because the relevant assertions admit the false-green cases above.
- **Match:** ⚠️ partial

### V12: `evidence/EV__phase-a__continuation_responsibilities.md`
- **RF claim:** seven VERIFIED rows, one per AC plus accounting, all resolving to adequate evidence.
- **Actual:** the file has the required seven rows and Candidate identity. E-accounting, E1 arithmetic/scope, and the history portion of E5 reproduce; E2–E4 and the connected-group portion of E5 overstate the assurance, so E6's all-green conclusion is not supportable.
- **Match:** ❌

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | Candidate/RF/dispatch ancestry, commit/path history, and worktree inventory | Baseline → proposal → approval producer → Candidate → RF → Reviewer dispatch is ordered; Candidate is the only implementation-path commit and remains reachable in the Executor worktree. |
| 2 | Independent strict-UTF-8/Git-object accounting and split-history script | Reproduced `3/747`, Plan/C 1,199, three-copy SHA parity, 179-task digest, and all three aggregate subsequences. |
| 3 | `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_repository_contracts.py -q` in a clean detached worktree at Candidate | 355 passed in 280.84s. The worktree was removed after the run. |
| 4 | Executor-task inspection of pre-Candidate status, cached names and commit invocation | Full status contained only the five approved paths; cached names matched; commit used `git commit --only --` with all five literal pathspecs. |
| 5 | Three independent Plan-source mutations against `rwnr_route_contract_errors`, `resolve_rwnr_route`, and `resolve_rwnr_identity` | Wrong `RES` owner, child-claims-LEAD, and write-smuggling each produced `contract_errors=[]`; model outputs remained the original expected values. |
| 6 | Cross-adapter receiver case: apply Antigravity old-exact, then encounter foreign Claude | Antigravity returned APPLIED, Claude REFUSED, and the whole connected group changed (`whole_connected_group_unchanged=False`). |
| 7 | Citation resolution scan for master HL §7.2 and ONB §7 | 33/33 master links resolve; ONB's 33 numbered references map one-to-one to those master rows. |
| 8 | JSON parse and runtime-reader reference scan | All four JSON receipts parse and bind Candidate/producer; no runtime or test source reads the evidence artifacts. |

The prior configured collection/full-suite evidence remains applicable: it was run in the same Windows/Python environment with HEAD fixed at the immutable Candidate before its commit, and no later VALUE or ASSURANCE change exists. A second full run would not close the assurance-oracle gaps found above.

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | `3 VALUE files`, `255 + 492 = 747`, Plan/C `1,199` | RF §1 accounting; RF §§3–4 | Baseline/Candidate Git objects, literal selector, strict UTF-8 counter | ✅ |
| C2 | 28 exact source-derived routes and repository no-mutation proof | RF §§1, 3–4; EV E2 | Candidate Plan plus `test_runtime_context.py` and routing receipt | ❌ — cases and outputs are hard-coded separately; temporary repositories are not evaluator inputs. |
| C3 | identity re-resolution/readback and inference rejection are proved | RF §3; EV E3 | Candidate Plan, identity model and routing receipt | ❌ — state/lineage/dispatch and before/after hashes are not exercised; child-LEAD mutation false-greens. |
| C4 | receiver migration refuses the entire connected group before writes | RF §§1, 3; EV E5 | `test_repository_contracts.py` and receiver receipt | ❌ — only adapter-local refusal is modeled; a foreign later adapter follows an earlier write. |
| C5 | owner approval predates Candidate and fixes `3/900` | RF §1 accounting | proposal `413945ca…`, approval producer `7f4e942f…`, dispatch f58c, Candidate ancestry | ✅ |

## Discrepancies Found

1. **AC-2 / AC-4 — the route and no-mutation assurance is not source-semantic and admits effectful false greens.** The test model receives hard-coded cases, not the temporary task/phase carriers, and its source gate checks selected tokens rather than each required route/effect. The three independent mutations above remain accepted while the model reports the original route/title/no-write outcome. This also trips TS §7's failure condition that wording tests must change observable route/mutation results.
2. **AC-3 — identity assurance does not exercise authoritative continuation inputs or required stop-case hashes.** The ten cases are mode strings with literal result/title/readback/mutation values; there are no task/phase state, ordered journal, mandate root/current-unit, parent/channel or dispatch inputs, and no before/after repository hashes for the invalid-AT stops. Required inference, child-inheritance, skipped re-resolution and missing-readback mutants are not independently rejected.
3. **AC-5 — receiver assurance is not an all-subject connected-group preflight.** Adapter runs and config classification are separate; a foreign Claude receiver can be discovered only after Antigravity has already changed. The evidence's isolated `group_unchanged` flag therefore cannot support the approved connected-group claim.
4. **AC-6 / EV — evidence statuses overclaim the failed AC-2–AC-5 gates.** The routing receipt omits required state/lineage inputs and mutation hashes, and the EV marks the affected claims VERIFIED despite the false-green and partial-group evidence above.

Any discrepancy requires 100% verification; all 12 RF-claimed files were checked.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | `evidence/EV__phase-a__continuation_responsibilities.md` | ✅ | ❌ — structure and identities resolve, but E2–E6 contain unsupported VERIFIED conclusions. |
| E2 | `evidence/phase-a-routing.json` | ✅ | ❌ — counts match, but source/state inputs and mutation hashes are absent and semantic false greens are hidden. |
| E3 | `evidence/phase-a-receiver-migration.json` | ✅ | ❌ — proves adapter-local behavior, not connected-group all-preflight refusal. |
| E4 | `evidence/phase-a-history.json` | ✅ | ✅ — independently reproduced. |
| E5 | `evidence/phase-a-accounting.json` | ✅ | ✅ — independently reproduced. |
| E6 | `evidence/phase-a-tests.txt` | ✅ | ⚠️ partial — recorded commands/results and rerun hold, but passing assertions do not prove the missing semantics. |

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | HL §7.2 #1–14; ONB §7 #1–14 | P0 — root `How It Works`; `.tfw/README.md` NS1, NS2.1–2.7, NS3, Where truth belongs | ✅ | ✅ | ✅ — continuity, purpose, subtraction, questions, selected trace, authority, proportional assurance and non-goals are stated as cited | ✅ — each constrains the router, history, authority or evidence boundary claimed. |
| 2 | HL §7.2 #15–21; ONB §7 #15–21 | P1 — Methodology values and Success Criteria 1, 2, 4 | ✅ | ✅ | ✅ — Candor, Structural Enforcement, Naming, Portability and the named outcomes match | ✅ — directly governs adversarial evidence, canonical copies, exact naming and resumability. |
| 3 | HL §7.2 #22–23; ONB §7 #22–23 | P2 — `knowledge/philosophy.md` F3 and F45 | ✅ | ✅ | ✅ — critical opposition/proof and proof-gated subtraction are accurately represented | ✅ |
| 4 | HL §7.2 #24–26; ONB §7 #24–26 | P3 — `KNOWLEDGE.md` D15, D31, D68 | ✅ | ✅ | ✅ — thin adapters, filesystem continuation and task-local live state match the applications | ✅ |
| 5 | HL §7.2 #27–29, #33; ONB §7 same | P4 — HL Contract rules 3/8/12, Design Rules, Anti-patterns, Session identity/AT | ✅ | ✅ | ✅ — amendment, 1,200-word, Role Lock/history/routing and identity clauses exist and match | ✅ |
| 6 | HL §7.2 #30–31; ONB §7 #30–31 | P6 — `knowledge/process.md` F37 and F39 | ✅ | ✅ | ✅ — immutable-method measurement and grep-derived delivery set are stated as cited | ✅ |
| 7 | HL §7.2 #32; ONB §7 #32 | P7 — `knowledge/stakeholder.md` F13 | ✅ | ✅ | ✅ — owner regards Resume as obsolete while deletion remains separate/proof-gated | ✅ |

P5 relevance scan found F1/F5 on canonical adapter copies, but the stronger P3 D15 and current manifest/parity evidence already govern the same application; no contradiction or missing decision constraint results. P7 F16 independently supports the session-title navigation boundary. Total citation instances: 66; resolved: 66; semantically verified: 66; irrelevant: 0; hallucinated: 0.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈12 × 0.42⌉ files and recorded findings? (12/12 after mandatory escalation)
- [x] Independently established evidence applicability and ran necessary affected checks, or named the exact unresolved claim?
- [x] Claim & Source Checks filled — key claims checked, every citation traced, and numeric claims checked against primary Git objects?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — no contradiction with the product change; assurance defects are recorded above?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: 66, resolved: 66, semantically verified: 66, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 6, verified: 2, partial: 1, mismatched: 3, missing: 0

Stage complete: YES

---

## Revision Round 1 — Bounded Affected-Result Re-verification

### Scope and lineage

- Review scope is limited to the four accepted rung-1 assurance corrections in REVIEW §4.1; Map, Judge, Purpose, approved HL/TS, VALUE, citations, and the unaffected history/parity result were not restarted.
- Replacement immutable Candidate: `ddb6fc4a1ab528525abd1020ee2fb562d4e10f65`.
- Corrected cumulative TRACE base: `495de8ceda0532f4a9fdf2cf4002dcc84b652791`, whose first parent is the replacement Candidate.
- Prior independent REVIEW producer: `99685b70c18bc19fcda7c7543d2d0545acc2912b`; Coordinator ruling producer: `d68e797c60811c4566be68397dc83da9d4f5089c`.
- Candidate changes exactly the two ruled ASSURANCE paths: `docs/scripts/test_runtime_context.py` and `docs/scripts/test_repository_contracts.py`. Candidate-to-TRACE changes contain no assurance path.

### Ruling-item verification

| # | Accepted correction | Independent result | Evidence |
|---|---|---|---|
| R1-1 | Source- and carrier-bound routing/no-effect oracle | VERIFIED | Materialized task/phase carriers and Candidate Plan source are evaluator inputs. Wrong-RES routing, child-title and write-smuggling mutations changed observable projections and were rejected; repository hashes remained stable. The round receipt covers 28 cases and records inputs plus cryptographic pre/post identities. |
| R1-2 | Authoritative identity carriers and stop mutants | VERIFIED | Status, authority-selected principal/root, current unit/role/readback, ordered journal and dispatch are materialized and observed. All seven required mutant families changed the projection or stopped with `STOP_IDENTITY`, remained unclaimed, and preserved the repository hash; missing, ambiguous, stale, foreign and wrong-root cases did likewise. |
| R1-3 | All-subject connected receiver preflight | VERIFIED | Config and all four supported adapters are classified before any write. Clean owned/absent/target-current groups converge and repeat with no diff; a foreign config or later adapter refuses before mutation with equal whole-group pre/post hashes. Managed-block replacement preserves surrounding bytes. |
| R1-4 | Replacement Candidate, post-freeze suites and cumulative evidence | VERIFIED | Candidate precedes TRACE; targeted and configured suite executions occurred after the Candidate freeze; round receipts bind Candidate, prior Candidate, prior REVIEW producer, Coordinator ruling and `revision-1`; cumulative RF/EV append corrected claims without replacing the historical round. |

### Independent checks and applicability

| Check | Result |
|---|---|
| Targeted exact-Candidate rerun in a clean detached worktree: `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_repository_contracts.py -q` | 355 passed in 325.28s; detached worktree removed after the run. |
| Independent adversarial carrier/source exercise | Wrong RES, write-smuggling and child-LEAD mutants were rejected with changed projections and stable repository hashes; all seven identity mutant families and five invalid-authority cases stopped safely. |
| Independent connected-group exercise | Managed config/adapter content applied while preserving outer bytes; foreign config and foreign-later-adapter cases refused with the whole group byte-identical. |
| Executor post-freeze configured evidence | 625 collected; 624 passed and one documented platform skip. The commands ran after `ddb6fc4…` and before TRACE. Reviewer reused this full-suite evidence because Candidate, environment, command, inputs and oracle are unchanged; the full suite was not redundantly rerun by Reviewer. |
| VALUE/accounting replay | Still exactly 3 VALUE files and `255 + 492 = 747` touched text LOC; Plan/C remains 1,199; no unclassified instruction source. |
| Unaffected files | Prior Candidate → replacement Candidate is empty for canonical Plan, both Plan receiver copies, canonical Resume and both Resume receiver copies. All three Plan copies retain SHA-256 `47c79864b215c176e170da39e2b26067ecb04d60c894440c992e47b7e12b5749`. |
| History and citations | Existing independently reproduced 205-entry history result and 66/66 citation verification remain input-applicable; neither underlying artifact nor claim changed. |
| Evidence independence | Runtime and test source do not read committed RF/EV/receipt artifacts; JSON accounting/history values independently reproduce. |

### Bounded checkpoint

- [x] All four Coordinator-accepted defects retested against replacement Candidate.
- [x] Exact two-path ASSURANCE delta and Candidate-before-TRACE lineage verified.
- [x] Post-freeze targeted and configured suite evidence verified; applicability limit recorded.
- [x] Unchanged VALUE `3/747`, Plan/C `1,199`, Plan/receiver parity and Resume-empty-diff verified.
- [x] No new debt, observation, Fact Candidate, strategic insight, documentation capture or release effect identified.

Bounded affected-result conclusion: **APPROVE**. The corrected assurance closes the four ruled defects without changing purpose, authority, VALUE, Plan, Resume, Phase B or the prior unaffected review results.

Stage complete: YES — revision-round append
