# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF implementation/evidence files claimed: 41
> Initial minimum: ⌈41 × 0.42⌉ = 18
> Actual verification: 41/41 scoped implementation/evidence files plus all 8 governing/lifecycle trace files. The first discrepancy escalated the sample to 100%.

## Verification Log

### V1: active roots and persistent carriers — 4/4
- **Files:** `AGENTS.md`, `CLAUDE.md`, `.agent/rules/agents.md`, `.agent/rules/tfw.md`.
- **RF claim:** The universal foundation preload was replaced by compact command routing.
- **Actual:** The managed blocks are compact, but `AGENTS.md:6-10` and `.agent/rules/agents.md:6-10` still order full `conventions.md`, full `glossary.md`, and full `KNOWLEDGE.md` at every new session. The candidate test inspects only the marker-bounded block and ignores these active instructions outside it.
- **Match:** ❌ — D1.

### V2: shared authority and knowledge state — 4/4
- **Files:** `.tfw/conventions.md`, `.tfw/glossary.md`, `.tfw/knowledge_state.yaml`, `.tfw/templates/knowledge_state.yaml`.
- **RF claim:** Shared authority is compact and singular; the live and template states use full task digests.
- **Actual:** The digest map and template schema are present and replay cleanly. The runtime adapter authority is not singular: `.tfw/conventions.md:655` still names Antigravity's obsolete singular `.agent/rules`, while the glossary delegates runtime behavior to that section and the manifest/adapter documentation name plural `.agents/rules` and `.agents/workflows`.
- **Match:** ⚠️ partial — digest state holds; adapter authority conflicts (D3).

### V3: canonical workflows — 5/5
- **Files:** `.tfw/workflows/plan.md`, `.tfw/workflows/knowledge.md`, `.tfw/workflows/init.md`, `.tfw/workflows/update.md`, `.tfw/workflows/config.md`.
- **RF claim:** Plan and knowledge own selective read contracts and digest reconciliation; init/update/config consume one manifest.
- **Actual:** The five canonical workflows contain those mechanisms and reference the one tooling manifest. The plan/knowledge contracts cannot override the earlier active root preload, so the end-to-end AC-1/AC-6 result does not hold.
- **Match:** ⚠️ partial — workflow-local changes hold; D1 prevents the claimed topology.

### V4: derived workflow copies — 10/10
- **Files:** the five changed `.claude/commands/tfw-{plan,knowledge,init,update,config}.md` copies and the five `.agent/workflows/tfw-{plan,knowledge,init,update,config}.md` copies.
- **RF claim:** All ten revision-2 derived copies match their canonical workflows.
- **Actual:** Ten SHA-256 pair comparisons report zero mismatches.
- **Match:** ✅.

### V5: adapter mapping, documentation, and templates — 9/9
- **Files:** `.tfw/adapters/manifest.yaml`; `.tfw/adapters/README.md`; the Antigravity README/template; the Claude Code README/template; the Codex README/template; the Cursor template.
- **RF claim:** One four-vendor, eleven-command map drives clean receivers and the persistent templates have no common preload.
- **Actual:** The manifest contains four adapters and eleven role-bearing commands; all four empty-receiver cases pass and the four templates are compact. The plural Antigravity target they consistently declare conflicts with the active runtime authority in `conventions.md` (D3).
- **Match:** ⚠️ partial.

### V6: implementation and test scripts — 4/4
- **Files:** `.tfw/scripts/gen_index.py`, `.tfw/scripts/test_gen_index.py`, `docs/scripts/test_integration.py`, `docs/scripts/test_runtime_context.py`.
- **RF claim:** K0-K9 and adapter checks are executable; semantic records and read topology are independently verified.
- **Actual:** The digest and receiver tests exercise their implementations and pass. The semantic suite does not execute baseline or candidate sources: `semantic_record()` returns the same `OUTCOMES` tuple for both profiles, mutants replace `gate` after construction, and the omitted-edge test removes a string from its own in-memory tuple. The read audit uses a hand-authored `CANDIDATE_EDGES` list rather than resolving the active root. With `PROJECT_ROOT` replaced by a nonexistent path, all 19 paired records and all six mutant-family comparisons still report success. The G4 test likewise checks only that twelve hard-coded rows have three non-empty strings.
- **Match:** ❌ — D1 and D2.

### V7: evidence artifacts — 5/5
- **Files:** `evidence/EV__phase-a__common_authority_and_context_topology.md`, `runtime-context-before-after.txt`, `semantic-fixtures.txt`, `knowledge-gate-replay.txt`, `clean-receiver-adapters.txt`.
- **RF claim:** Six acceptance criteria are verified by contemporaneous raw evidence.
- **Actual:** All files exist. E3 and E4 reproduce. E1, E2, E5, and E6 rely on the incomplete topology/self-validating suite and therefore do not establish their stated claims.
- **Match:** ❌ — evidence exists but is insufficient.

### V8: governing and lifecycle traces — 8/8
- **Files:** governing TS revision 2, ONB, RF, four phase journal events, and phase `status.md`.
- **RF claim:** The revision-2 scope and lifecycle lineage are complete and within budget.
- **Actual:** The 36 implementation/test files plus 5 evidence files match the approved 41-path scope; the eight additional paths are governing/lifecycle traces. Candidate changed LOC is 3,644 against the 4,600 ceiling. The phase was at `RF` before this review.
- **Match:** ✅.

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | candidate SHA/ref and clean-tree guard | `HEAD` and `refs/heads/codex/tfw-20260902-175227-rcfr-phase-a` both resolve to `e0aca06b0045c92c277d5a23cc85cd476d88345d`; candidate tree was clean before review writes |
| 2 | `python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only` | 405 collected |
| 3 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | 404 passed, 1 skipped in 169.43s; final rerun after REVIEW/status/journal writes: 404 passed, 1 skipped in 145.82s |
| 4 | `python -m pytest .tfw/scripts/test_gen_index.py -q` | 155 passed in 2.86s |
| 5 | `python -m pytest docs/scripts/test_runtime_context.py -q` | 64 passed in 0.18s; D2 explains why the semantic successes are not probative |
| 6 | `python -m pytest docs/scripts/test_integration.py -q` | 47 passed in 185.77s |
| 7 | `python docs/scripts/test_runtime_context.py --audit` | reproduced the RF totals: plan 32,917→8,028 and knowledge 31,779→2,052 |
| 8 | independent active-root transitive recount with the same `\S+` method | mandatory full common reads add 25,549 words: plan 32,917→33,577 (**-2.0%**, a regression); knowledge 31,779→27,601 (**13.1%** reduction) |
| 9 | semantic source-independence probe with `PROJECT_ROOT` set to a nonexistent directory | `nonexistent_root_pairs=True cases=19 mutants=True` — the claimed oracle succeeds without candidate or baseline sources |
| 10 | ten canonical/derived SHA-256 comparisons | `derived_copy_pairs=10 mismatches=0` |
| 11 | `python .tfw/scripts/gen_index.py --knowledge-pending --format json` | exit 0; 61 current, 0 pending, 0 removed, 0 problems, no migration |
| 12 | `python .tfw/scripts/gen_index.py --check project` | PASS; the command explicitly does not inspect artifact content or adapter-copy equality |
| 13 | `python .tfw/scripts/gen_index.py --check tasks` | exit 1; one pre-existing RDP journal summary is 123 code points against the 120 ceiling; 17 stateless historical phase directories are informational |
| 14 | `git diff --check` | PASS |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | “Both owned paths exceed the 30% reduction threshold” | RF §3 AC-6 and §4 | active `AGENTS.md`, workflow read contracts, baseline `2728dae`, raw audit | ❌ — actual instructed exposure is -2.0% for plan and 13.1% for knowledge |
| C2 | “Independent semantic oracle” and “every deliberate mutant fails” | RF §1, §3 AC-5, EV E5 | `docs/scripts/test_runtime_context.py:43-113,326-330` | ❌ — expected outputs are shared constants and the tests succeed with no source tree |
| C3 | “Exact vendor discovery paths” | RF §1 and AC-4 | manifest/adapter docs plus `.tfw/glossary.md:308-310` and `.tfw/conventions.md:650-656` | ❌ — plural metadata/documentation conflicts with singular runtime authority |

Every RF/EV artifact citation resolves to a real file. Every HL §7.2 and ONB §7 citation also resolves; their semantic verification is recorded below. Resolution does not cure C1-C3 because the cited evidence does not establish those claims.

## Discrepancies Found

1. **D1 — AC-1 and AC-6 fail.** Active root instructions still impose the universal full-library preload. The candidate test and audit deliberately look only at the managed block/static edge list, so their reported 75.6%/93.5% reductions omit mandatory transitive reads. The corrected results are -2.0% and 13.1%, both below the 30% threshold.
2. **D2 — AC-5 fails and AC-2's G4 gate is not established.** The semantic records, mutants, omitted-edge check, and deletion-ledger check validate hard-coded declarations rather than baseline/candidate behavior or real authority/history resolution.
3. **D3 — AC-2/AC-4 authority is inconsistent.** The manifest and adapter documentation declare plural `.agents/*` as Antigravity's vendor path, while the runtime authority still declares singular `.agent/rules`.
4. **D4 — surviving RF observation.** The pre-existing RDP journal summary is 123 code points and keeps `--check tasks` red. Repair is outside this phase and would rewrite an immutable unrelated event.

Any discrepancy requires 100% verification; V1-V8 record all 41 scoped files and all eight accompanying traces.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | EV AC-1; `runtime-context-before-after.txt`; `semantic-fixtures.txt` | ✅ | ❌ — D1: the audit omits active root reads |
| E2 | EV AC-2; `semantic-fixtures.txt`; runtime-context tests | ✅ | ❌ — D2/D3: the ledger is self-asserted and runtime adapter authority conflicts |
| E3 | EV AC-3; `knowledge-gate-replay.txt` | ✅ | ✅ — K0-K9, migration, state-last replay, and current zero-pending result reproduce |
| E4 | EV AC-4; `clean-receiver-adapters.txt`; integration tests | ✅ | ⚠️ partial — empty receivers and manifest structure pass, but D3 leaves runtime authority inconsistent |
| E5 | EV AC-5; `semantic-fixtures.txt` | ✅ | ❌ — D2: fixed outcomes are not an independent oracle |
| E6 | EV AC-6; `runtime-context-before-after.txt`; full gate | ✅ | ❌ — tests are green, but the corrected reductions miss the threshold |

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | HL §7.2 K1 / ONB §7 #1 | P0 — NS1 | ✅ | ✅ | ✅ — purpose, inspectability, authority, continuation | ✅ — prevents metric-only deletion |
| 2 | HL §7.2 K2 / ONB §7 #2 | P0 — NS3 | ✅ | ✅ | ✅ — bureaucracy is a non-goal | ✅ — applies to universal preload |
| 3 | HL §7.2 K3 / ONB §7 #3 | P1 — Structural Enforcement; Naming Creates Behavior; Portability | ✅ | ✅ | ✅ | ✅ — applies to gates, headings, and clean receivers |
| 4 | HL §7.2 K4 / ONB §7 #4 | P2 — philosophy F22, F40, F43, F45 | ✅ | ✅ | ✅ | ✅ — templates, precise terms, central authority, subtraction |
| 5 | HL §7.2 K5 / ONB §7 #5 | P3 — D23, D25, D61 | ✅ | ✅ | ✅ | ✅ — prior progressive-disclosure and review reductions |
| 6 | HL §7.2 K6 / ONB §7 #6 | P3 — D63, D68, D72 | ✅ | ✅ | ✅ | ✅ — frozen contract, local state, correction loop |
| 7 | HL §7.2 K7 / ONB §7 #7 | P4 — conventions §11 and §14 | ✅ | ✅ | ✅ | ✅ — references, role locks, structural enforcement |
| 8 | HL §7.2 K8 / ONB §7 #8 | P5 — convention F4, F8, F14 | ✅ | ✅ | ✅ | ✅ — algorithmic reads, one owner, no template duplication |
| 9 | HL §7.2 K9 / ONB §7 #9 | P6 — process F3, F4, F22, F30 | ✅ | ✅ | ✅ | ✅ — named algorithms and executable checks |
| 10 | HL §7.2 K10 / ONB §7 #10 | P7 — remaining topic files | ✅ | ✅ | ✅ — full relevance scan found no additional phase constraint | ✅ — N/A application is justified |
| 11 | ONB §7 #11 | New P3 — D54 | ✅ | ✅ | ✅ — exact eleven-command public set | ✅ — adapter baseline |
| 12 | ONB §7 #12 | New P3 — D69 | ✅ | ✅ | ✅ — full identifier parsing/refusal | ✅ — digest task enumeration |
| 13 | ONB §7 #13 | New P0 router entries — Evidence Collection, Execution Loop, Pre-RF Gate, Session Naming, Disposition | ✅ | ✅ | ✅ | ✅ — RDP semantic preservation targets |

## Checkpoint

**Self-check:**
- [x] Opened 41/41 scoped files (and all 8 governing/lifecycle traces) and recorded findings?
- [x] Ran build/test commands and independent adverse probes?
- [x] Claim & Source Checks filled; key claims checked against primary local sources and every citation traced?
- [x] Each RF §3 acceptance checkmark verified against actual files?
- [x] KNOWLEDGE.md checked; the stale adapter architecture row is documented for the eventual KNW step?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total application rows: 13, resolved: 13, semantically verified: 13, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 6, verified: 2, partial: 1, insufficient: 3, missing: 0

Stage complete: YES
