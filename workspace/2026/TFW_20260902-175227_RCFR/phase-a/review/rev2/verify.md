# Verify — Review Revision 2: “Are the claims true?”
> **Mindset:** Auditor. The RF is a declaration, not a fact.
> **Test:** “If I removed the RF, would the evidence alone prove the work was done?”
> **Min verify ratio:** 0.42 default
> **RF files claimed:** 57 cumulative paths (41 implementation/test/evidence + 16 governing/lifecycle traces)
> **Minimum:** 24 paths; **actual:** 57/57 cumulative paths accounted for, all 23 return-round paths opened, and the discrepancy escalated verification to 100%

## Verification Log

### V1: candidate identity, lineage, and scope — 57/57
- **RF claim:** The returned candidate has 3,224 additions plus 1,239 deletions, 4,463 changed LOC across 57 paths, within the 4,600 round ceiling and 5,000 hard ceiling.
- **Actual:** Exact candidate `ade6d415fc02a8f888494f036ba8a495d4cf32b7` and reviewer `HEAD` `4e9a7f56287cbbadf631580b11cecb3ceae135f2` resolve to the same tree `ab29276c630a172da169e3985cc9df8af0f84bb3`. Independent `git diff --numstat 2728dae…ade6d41` gives 57 paths, 3,224 additions, 1,239 deletions, and 4,463 changed LOC. The repair range contains only R1–R3 implementation inputs and authorized cumulative traces/evidence; no frozen HL, Phase A HL, Phase B/C, sixth evidence file, or 42nd implementation/test/evidence path changed.
- **Match:** ✅

### V2: R1 active bootstrap and read audit
- **RF claim:** Active roots no longer preload the three common libraries, and the actual root → skill → workflow → addressed-range graph reduces `/tfw-plan` by 45.4% and `/tfw-knowledge` by 47.4%.
- **Actual:** Both `AGENTS.md` and `.agent/rules/agents.md` delegate input selection to the selected workflow and contain no full-library preload in the active context section. The audit resolves the command route, selected skill, canonical workflow, read-contract headings, transitive reads, and repeated reads from both source trees. Independent replay gives plan 64,229 → 35,068 words (45.4%) and knowledge 78,587 → 41,347 words (47.4%), each above 30%.
- **Match:** ✅

### V3: R2 semantic records and source mutations
- **RF claim:** Nineteen baseline/candidate records are derived from real source trees for `{decision, refusal, artifact effects, citations, gate}`, and six family mutants prove candidate sensitivity.
- **Actual:** `SourceTree` now rejects absent roots and reads both the baseline commit and current tree. Each scenario also checks one real heading/needle, and each P/R/E/V/C/A mutant removes that needle and is rejected. However, `OUTCOMES` at `docs/scripts/test_runtime_context.py:64` still stores every six-field behavior record; `_scenario()` copies that tuple into `Scenario.outcome`, and `execute_scenario()` at line 101 returns `SemanticRecord(*scenario.outcome, …)` after only a presence check. A minimal source containing only the P1 heading and one anchor still emits the full decision/refusal/citation/gate record even though those values are absent; replacing the in-memory `Scenario.outcome` makes both unchanged baseline and candidate sources emit the replacement record. The source is therefore a gate, not the oracle that derives the behavior output.
- **Match:** ❌ — D1

### V4: R2 graph/address failures and R03–R14 ledger
- **RF claim:** An omitted command route, missing/duplicate addressed heading, and all 12 deletion-ledger rows resolve against real files/headings and fail independently when damaged.
- **Actual:** The route omission removes the actual `/tfw-plan` row from an `AGENTS.md` overlay; heading mutants alter the addressed `Task control files` heading; the resolver refuses zero and duplicate matches. R03–R14 are parsed from the research recommendation table and each authority, condition/action, test, and history target resolves against the current source tree.
- **Match:** ✅

### V5: R3 Antigravity authority and clean receiver
- **RF claim:** Conventions, glossary, manifest, and installed receiver use plural `.agents/*`; changing any one surface back to singular fails.
- **Actual:** The `Tool Adapter Pattern` and glossary `Tool Adapter` sections name `.agents/rules/tfw.md` and `.agents/workflows/tfw-{command}.md`; the manifest targets the same paths; an empty receiver contains exactly that persistent rule plus eleven commands. The four cross-surface singular mutations are rejected, and the four-vendor receiver suite passes.
- **Match:** ✅

### V6: digest transaction and prior accepted surfaces
- **RF claim:** State-last reconciliation ends with no pending/removed/problem IDs and no migration; the previously accepted digest, copy-equality, exact-command, template, and receiver guarantees remain green.
- **Actual:** Pre-review `--knowledge-pending --format json` reports 61 current tasks, `pending_task_ids=[]`, `removed_task_ids=[]`, `problems=[]`, and `migration_required=false`. The 155 resolver tests pass. Integration tests cover canonical/copy equality, the exact four-by-eleven manifest, templates, generated docs, and empty receivers without regression.
- **Match:** ✅

### V7: cumulative traces and evidence
- **RF claim:** ONB/RF/EV and four raw evidence files append rather than erase earlier results; phase state is `RF`; the unrelated RDP event remains unchanged and reported.
- **Actual:** Revision-3 sections are additive in cumulative ONB, RF, EV, and raw evidence. Phase journal records `TS_DRAFT → ONB → RF`; status authority is TS revision 3. Round-1 stage blobs remain unchanged. The prior REVIEW was changed only by Coordinator commit `640e702` to record its required one-act disposition ruling before ordering rev3; no Executor commit touched it. The RDP event remains immutable and `--check tasks` still reports its 123-code-point summary against the 120 ceiling.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | candidate/tree identity and clean-tree guard | `ade6d41^{tree}` = `HEAD^{tree}` = `ab29276…`; clean before review writes |
| 2 | `git diff --numstat 2728dae…ade6d41` | 57 files; 3,224 additions + 1,239 deletions = **4,463/4,600 LOC** |
| 3 | `python docs/scripts/test_runtime_context.py --audit` | plan 64,229 → 35,068 (**45.4%**); knowledge 78,587 → 41,347 (**47.4%**) |
| 4 | `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q` | 118 passed in 284.02s |
| 5 | `python -m pytest .tfw/scripts/test_gen_index.py -q` | 155 passed in 1.60s |
| 6 | `python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only` | 412 collected |
| 7 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | 411 passed, 1 skipped in 272.52s |
| 8 | `python .tfw/scripts/gen_index.py --check project` | PASS |
| 9 | `python .tfw/scripts/gen_index.py --check tasks` | Exit 1 only for the pre-existing immutable RDP summary: 123 code points vs 120; six historical task groups remain informational |
| 10 | `python .tfw/scripts/gen_index.py --knowledge-pending --format json` | 61 current; zero pending, removed, or problems; migration false |
| 11 | `git diff --check 2728dae…ade6d41` | PASS |
| 12 | independent minimal-source and outcome-substitution probe | P1 full record survives a source containing only one required anchor; changing only `Scenario.outcome` changes both baseline and candidate records — D1 reproduced |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | “actual active root → skill → workflow → addressed-range graph” and both reductions exceed 30% | RF §10 R1 and EV round-1 return | active roots, selected skills, canonical workflows, read contracts, raw audit | ✅ — independent totals match |
| C2 | “source-derived 19-case semantic records” | RF §10 R2; EV AC-5 return; semantic raw evidence | `docs/scripts/test_runtime_context.py:64-101` and adverse probe | ❌ — source controls only anchor presence; all behavior fields come from `OUTCOMES` |
| C3 | “plural Antigravity authority across all runtime surfaces” | RF §10 R3; EV AC-4 return | conventions, glossary, manifest, clean receiver, cross-surface mutations | ✅ |
| C4 | “4,463/4,600 cumulative changed LOC” | RF §10 scope; EV round return | primary `git diff --numstat 2728dae…ade6d41` | ✅ — 3,224 + 1,239 = 4,463 |

Every RF/EV artifact citation resolves. All 13 master-HL §7.2 and ONB §7 knowledge applications were semantically verified in review revision 1; revision 3 adds no new application and does not change their source items or asserted meanings.

## Discrepancies Found

1. **D1 — TS revision 3 R2 and AC-5 remain unmet.** Real roots, needles, and mutants are now exercised, but the actual `{decision, refusal, artifact effects, citations, gate}` outputs are still fixed in `OUTCOMES` and shared by baseline and candidate. The passing suite proves anchor survival, not behavioral equivalence derived independently from each source tree. This is the exact core of REVIEW revision 1 D2 that R2 ordered to replace.

Any discrepancy requires 100% verification; V1–V7 account for all 57 cumulative candidate paths and all 23 return-round paths.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | EV AC-1; `runtime-context-before-after.txt`; runtime tests | ✅ | ✅ — active graph and reductions reproduce |
| E2 | EV AC-2; semantic/ledger evidence; runtime/integration tests | ✅ | ✅ — one-authority topology, G4 target resolution, and structural failures reproduce |
| E3 | EV AC-3; `knowledge-gate-replay.txt` | ✅ | ✅ — resolver and zero-pending replay reproduce |
| E4 | EV AC-4; `clean-receiver-adapters.txt` | ✅ | ✅ — exact paths, four vendors, eleven commands, and R3 mutations reproduce |
| E5 | EV AC-5; `semantic-fixtures.txt` | ✅ | ❌ — D1: source access and anchor mutation do not derive the six behavior fields |
| E6 | EV AC-6; full suite and scope evidence | ✅ | ✅ — thresholds, 4,463 LOC, and configured suite reproduce |

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1–13 | Master HL §7.2 K1–K10 and cumulative ONB §7 #1–#13 | P0 NS1/NS3; P1 Structural Enforcement/Naming/Portability; P2 F22/F40/F43/F45; P3 D23/D25/D54/D61/D63/D68/D69/D72; P4 conventions §§11/14; P5 F4/F8/F14; P6 F3/F4/F22/F30; P7 relevance scan; router entries | ✅ 13/13 | ✅ 13/13 | ✅ 13/13 — unchanged from revision-1 full verification | ✅ 13/13 — no new revision-3 application |

`KNOWLEDGE.md` remains stale in its Architecture Map `Adapters` row: it names singular `.agent/workflows` and says `config.md` owns the full map. That contradicts the accepted manifest/plural topology, but §§1–3 are post-approval `/tfw-docs` territory and this REVISE round cannot update them.

## Checkpoint

**Self-check:**
- [x] Accounted for 57/57 cumulative paths and opened all 23 return-round paths?
- [x] Ran targeted and full configured suites plus independent adverse probes?
- [x] Claim & Source Checks filled; candidate identity, numerical claims, citations, and primary sources verified?
- [x] Each RF §3/§10 acceptance claim checked against actual files and behavior?
- [x] `KNOWLEDGE.md` contradiction documented without editing it?
- [x] All 13 knowledge applications remain resolved, semantically verified, relevant, and non-hallucinated?
  - Total: 13, resolved: 13, semantically verified: 13, irrelevant: 0, hallucinated: 0
- [x] All six evidence items checked separately for existence and sufficiency?
  - Total: 6, verified: 5, insufficient: 1, missing: 0

Stage complete: YES
