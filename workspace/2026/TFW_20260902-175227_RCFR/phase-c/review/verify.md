# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 47
> Files to verify: ⌈47 × 0.42⌉ = 20

The first discrepancy escalated verification to 100%. All 47 files named by candidate
`1429fe70cd77f0a9b0ff24c17b15bfe7bcc6ec86` were opened directly or covered by an exact
byte/content check, and all six evidence artifacts were replayed or inspected.

## Verification Log

### V1: seven canonical secondary workflows
- **RF claim:** Each secondary path preserves its baseline algorithm, gates, effects, and role boundary through a workflow-owned Read Contract.
- **Actual:** The seven workflows own ordered reads and the thin skills route to them. Two current role declarations conflict with their new locks: Docs says `Coordinator / Reviewer` but locks `COORDINATOR`; Release says `Coordinator / Maintainer` but locks `COORDINATOR`.
- **Match:** ❌

### V2: fourteen Codex secondary skill files
- **RF claim:** Each source skill equals its installed copy and remains a thin role-aware router.
- **Actual:** All seven `.tfw/adapters/codex/skills/.../SKILL.md` files are byte-equal to their seven `.agents/skills/.../SKILL.md` copies and route into the canonical workflow. Their declared roles also expose the Docs/Release disagreement with the workflow locks.
- **Match:** ⚠️ partial

### V3: twelve changed tracked workflow copies
- **RF claim:** Changed Claude and Antigravity workflow copies equal their canonical workflows.
- **Actual:** Every changed `.claude/commands/tfw-*.md` and `.agent/workflows/tfw-*.md` copy is byte-equal to its canonical source. The unchanged Knowledge copies are also equal.
- **Match:** ✅

### V4: `.tfw/templates/status.md`, `.tfw/templates/journal/event.md`, `.tfw/scripts/gen_index.py`
- **RF claim:** Every immutable current-event bound is mechanically enforced before installation.
- **Actual:** Closed keys, required fields, vocabulary, declared human, token/stamp matching, transition pairs, and several summary/ref bounds are enforced. Direct calls to `validate_new_event` nevertheless accepted an impossible calendar timestamp, absolute and parent-traversing refs, and a numeric summary. These are all outside the template's declared bounds.
- **Match:** ❌

### V5: `.tfw/conventions.md`, `.tfw/glossary.md`, `.tfw/adapters/manifest.yaml`
- **RF claim:** Shared authority, lifecycle vocabulary, and the exact 4×11 adapter topology remain coherent.
- **Actual:** The manifest has exactly 11 expected routes and four adapters; status vocabulary and transition ownership remain single-sourced. The retained role headings conflict with two workflow locks, so the active instruction graph is not fully coherent.
- **Match:** ⚠️ partial

### V6: `docs/scripts/test_gen_index.py`
- **RF claim:** Tests exercise strict current-event validation and lifecycle/refusal semantics.
- **Actual:** The tests cover the named examples used by the RF, but do not exercise semantic ISO validity, ref relativity, or summary type. The production validator accepts all three omitted malformed forms.
- **Match:** ❌

### V7: `docs/scripts/test_runtime_context.py`
- **RF claim:** Phase C semantic records are produced independently from baseline/candidate sources before comparison with expected records, and expected records cannot feed production.
- **Actual:** `PHASE_C_SEMANTIC_SPECS` stores `PHASE_C_EXPECTED_RECORDS[...]` directly as each production projection (lines 406–509). `execute_phase_c_semantic` checks anchors plus one clause and returns that stored projection for all six fields (lines 514–527). The anti-feed test mutates the expected dictionary only after the spec captured the same tuple (lines 1594–1603), so it cannot expose the feed. The Phase C stale scan likewise searches only five literal clauses and does not compare active role declarations.
- **Match:** ❌

### V8: `docs/scripts/test_integration.py`
- **RF claim:** Four clean receivers install 11 commands, rerun idempotently, repair secondary drift, and preserve unrelated content.
- **Actual:** The configured tests pass. A separate temporary-receiver replay mutated `resume` for all four adapters; each repaired it, kept an unrelated file byte-identical, and retained 11 command routes.
- **Match:** ✅

### V9: six Phase C evidence artifacts
- **RF claim:** The artifacts prove AC-1…AC-8 and support an 8/8 VERIFIED verdict.
- **Actual:** All files resolve. Runtime counts, adapter results, suite results, scope, and exclusions reproduce. The AC-3, AC-4, and AC-6 evidence repeats conclusions from incomplete or circular checks and therefore does not support its VERIFIED status.
- **Match:** ❌

### V10: candidate scope and exclusions
- **RF claim:** 41 implementation/test files, 4,109 changed LOC, zero new runtime files, and no forbidden task/prior-phase/release/version change.
- **Actual:** Against approved TS baseline `cf36dd6bd94bb7448f7355a18bbd258ff508640a`, the implementation/test set is 41 existing files with 1,874 insertions and 2,235 deletions (4,109 changed LOC). Candidate adds only six required evidence files. No `tasks/`, prior phase, master HL, README/edition, changelog, release, or version file changed; `git diff --check` is clean.
- **Match:** ✅

### V11: primary routes and exact word-count ledger
- **RF claim:** Every changed path and corpus clears 30%, while the five primary paths do not regress.
- **Actual:** Exact `\S+` replay matches the recorded transcript: Plan 24,730→24,638; focused Research 6,103→6,103; deep Research 6,168→6,168; Handoff 6,366→6,274; Review 25,182→25,090. Secondary/lifecycle reductions range from 30.1% to 96.6%; trajectory is 310,485→112,210 (63.9%) and unique active `.tfw` corpus is 66,436→32,092 (51.7%).
- **Match:** ✅

### V12: contract, citations, and historical rulings
- **RF claim:** Freeze, authority, thresholds, exclusions, and the ruled RDP diagnostic remain intact.
- **Actual:** Candidate does not modify the frozen master/phase contracts or earlier phases. All cited knowledge items resolve and match their asserted use. `--check tasks` still reports only the previously ruled immutable RDP `123>120` summary plus 17 informational legacy phase directories.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | PASS — 491 passed, 1 skipped in 312.88s. |
| 2 | `python -m pytest .tfw/scripts/ docs/scripts/ --collect-only -q` | PASS — 492 collected. |
| 3 | `python .tfw/scripts/gen_index.py --check project` | PASS — exit 0; release 2.1.0 consistent. |
| 4 | `python .tfw/scripts/gen_index.py --check tasks` | Expected diagnostic — exit 1; only the ruled RDP 123-code-point summary; 17 legacy phase directories informational. |
| 5 | `python docs/scripts/test_runtime_context.py --audit --baseline-ref cf36dd6bd94bb7448f7355a18bbd258ff508640a` | PASS — 569 output lines exactly match `runtime-context-whole-system.txt`. |
| 6 | `python docs/scripts/test_runtime_context.py --semantic-json --semantic-mutants --phase-c-semantic-json --phase-c-mutants --revise-routes` | Mechanical replay PASS — 3,698 output lines exactly match the semantic transcript; inspection found the Phase C oracle circularity described above. |
| 7 | Direct `validate_new_event` adverse-fixture calls | FAIL — impossible time, absolute/parent refs, and numeric summary each returned no problem. |
| 8 | Canonical/copy and source/installed byte comparisons | PASS — all expected pairs equal. |
| 9 | Independent four-adapter temporary-receiver replay with `resume` drift | PASS — all repaired, unrelated content preserved, 11 routes retained. |
| 10 | `git diff --check cf36dd6bd94bb7448f7355a18bbd258ff508640a 1429fe70cd77f0a9b0ff24c17b15bfe7bcc6ec86` and explicit scope counts | PASS — clean diff; 41 existing implementation/test files and 4,109 changed LOC. |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | “every immutable current-event bound [is] refused before installation” | RF §3 AC-3; EV E3 | `.tfw/templates/journal/event.md` and live `validate_new_event` calls | ❌ — four declared bounds are not fully enforced. |
| C2 | “expected data cannot feed production” | RF §3 AC-6; EV E6 | `docs/scripts/test_runtime_context.py:406-527,1594-1603` | ❌ — expected tuples are embedded in the production specs. |
| C3 | “zero unexplained ... competing current instructions” | RF §3 AC-4; EV E4 | all current secondary workflows/skills plus `_phase_c_stale_instruction_errors` | ❌ — Docs and Release carry contradictory role declarations that the literal-clause scan cannot see. |

Every link in the RF and EV index resolves to a real task-local artifact. Numeric claims were checked
against Git trees and fresh command output rather than copied from RF prose.

## Discrepancies Found

1. **AC-6 / Rung 1:** the Phase C semantic oracle is self-fed. Expected tuples initialize the
   values returned as “produced”, and the purported anti-feed mutation occurs after that capture.
   The output-changing mutants change a predeclared tuple selected by one prose clause; they do not
   independently derive the six semantic fields from source.
2. **AC-3 / Rung 1:** `validate_new_event` does not enforce all template-declared pre-write bounds.
   It accepts `2026-99-99T99:99:99+99:99`, `C:/outside.txt`, `../outside.md`, and numeric `summary: 7`
   when the remaining record is valid.
3. **AC-2 and AC-4 / Rung 1:** active Docs and Release role declarations compete with their locks,
   and the stale/duplicate census cannot detect such conflicts because it searches only five fixed
   strings instead of enumerating and reconciling the active instruction graph.

Because discrepancies exist, the verification sample was escalated from 20 to all 47 candidate
files.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | `runtime-context-whole-system.txt` | ✅ | ✅ — graph rows, primary anchors, and omission/address/preload mutants reproduce. |
| E2 | `semantic-and-lifecycle-whole-system.txt` | ✅ | ⚠️ — route anchors replay, but role-boundary equivalence is contradicted by current Docs/Release declarations. |
| E3 | `verification-whole-system.txt` | ✅ | ❌ — its selected fixtures pass, but the live validator accepts other forms explicitly forbidden by the declared schema. |
| E4 | `stale-duplicate-ledger.txt` | ✅ | ❌ — census is not exhaustive and omits two current role conflicts. |
| E5 | `clean-receiver-secondary-routes.txt` | ✅ | ✅ — independently replayed for all four adapters, including Resume drift. |
| E6 | `semantic-and-lifecycle-whole-system.txt` | ✅ | ❌ — Phase C expected records feed production; the transcript proves the harness output, not source-independent semantics. |
| E7 | `runtime-context-whole-system.txt` | ✅ | ✅ — every total and threshold independently recomputed. |
| E8 | `verification-whole-system.txt` | ✅ | ✅ — suite, collection, project/task checks, diff, scope, and exclusions independently reproduced. |

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | Master HL §7.2 K1 | P0 — `.tfw/README.md` NS1 | ✅ | ✅ | ✅ — purpose, inspectability, authority, continuation | ✅ — reduction must preserve purposeful continuation. |
| 2 | Master HL §7.2 K2 | P0 — `.tfw/README.md` NS3 | ✅ | ✅ | ✅ — bureaucracy is a non-goal | ✅ — forbids a generated runtime layer. |
| 3 | Master HL §7.2 K3 | P1 — Methodology values | ✅ | ✅ | ✅ — structural enforcement, naming, portability | ✅ — constrains compact routes. |
| 4 | Master HL §7.2 K4 | P2 — philosophy F22, F40, F43, F45 | ✅ | ✅ | ✅ — minimal templates, terms, architecture, subtraction | ✅ — directly informs compaction. |
| 5 | Master HL §7.2 K5 | P3 — D23, D25, D61 | ✅ | ✅ | ✅ — progressive disclosure and deletion precedents | ✅ — direct architecture precedent. |
| 6 | Master HL §7.2 K6 | P3 — D63, D68, D72 | ✅ | ✅ | ✅ — freeze, local authority, citation bar | ✅ — protected semantics. |
| 7 | Master HL §7.2 K7 | P4 — Conventions Design Rules / Anti-patterns | ✅ | ✅ | ✅ — algorithmic refs, locks, structural gates | ✅ — implementation constraints. |
| 8 | Master HL §7.2 K8 | P5 — convention F4, F8, F14 | ✅ | ✅ | ✅ — references, single owners, template scope | ✅ — carrier design. |
| 9 | Master HL §7.2 K9 | P6 — process F3, F4, F22, F30 | ✅ | ✅ | ✅ — precise algorithms and enforcement sites | ✅ — verification design. |
| 10 | Master HL §7.2 K10 | P7 scan | ✅ | ✅ | ✅ — no additional applicable fact | ✅ — task is methodology-runtime work. |
| 11 | Phase HL Knowledge Basis | P0 — NS1, NS3, root `How It Works` | ✅ | ✅ | ✅ — continuation and task-local truth | ✅ — whole-system reduction. |
| 12 | Phase HL Knowledge Basis | P1 — Methodology values / Success Criteria | ✅ | ✅ | ✅ — observable, portable, resumable behavior | ✅ — proof quality. |
| 13 | Phase HL Knowledge Basis | P2 — philosophy F22, F40, F43, F45 | ✅ | ✅ | ✅ | ✅ — compaction method. |
| 14 | Phase HL Knowledge Basis | P3 — D23, D25, D61, D68, D72, D73, D74 | ✅ | ✅ | ✅ — ownership, proof, primary paths | ✅ — phase inheritance. |
| 15 | Phase HL Knowledge Basis | P4 — HL, Design Rules, Anti-patterns | ✅ | ✅ | ✅ — derivation, refs, locks, traces | ✅ — scope and authority. |
| 16 | Phase HL Knowledge Basis | P5 — convention F4, F8, F14 | ✅ | ✅ | ✅ | ✅ — carrier ownership. |
| 17 | Phase HL Knowledge Basis | P6 — process F3, F4, F22, F30, F32, F35, F37–F40, F43 | ✅ | ✅ | ✅ — measured revisions, external verification, pre-write bounds | ✅ — evidence and lifecycle proof. |
| 18 | Phase HL Knowledge Basis | P7 topic scan | ✅ | ✅ | ✅ — no additional applicable constraint | ✅ — bound already complete. |
| 19 | ONB §7 #1 | P0 — K1 / NS1 | ✅ | ✅ | ✅ | ✅ — inspectable continuation. |
| 20 | ONB §7 #2 | P0 — K2 / NS3 | ✅ | ✅ | ✅ | ✅ — no new layer. |
| 21 | ONB §7 #3 | P1 — K3 / Methodology values | ✅ | ✅ | ✅ | ✅ — structural and portable gates. |
| 22 | ONB §7 #4 | P2 — K4 / philosophy F22, F40, F43, F45 | ✅ | ✅ | ✅ | ✅ — subtraction and architecture. |
| 23 | ONB §7 #5 | P3 — K5 / D23, D25, D61 | ✅ | ✅ | ✅ | ✅ — established precedents. |
| 24 | ONB §7 #6 | P3 — K6 / D63, D68, D72 | ✅ | ✅ | ✅ | ✅ — frozen claims and finite REVISE authority. |
| 25 | ONB §7 #7 | P4 — K7 / Design Rules and Anti-patterns | ✅ | ✅ | ✅ | ✅ — no lock, trace, or evidence violation admitted. |
| 26 | ONB §7 #8 | P5 — K8 / convention F4, F8, F14 | ✅ | ✅ | ✅ | ✅ — one owner per rule. |
| 27 | ONB §7 #9 | P6 — K9 / process F3, F4, F22, F30 | ✅ | ✅ | ✅ | ✅ — every rule needs an enforcement site. |
| 28 | ONB §7 #10 | P7 — K10 scan | ✅ | ✅ | ✅ | ✅ — no new domain constraint. |
| 29 | ONB §7 #11 | P7 — stakeholder F13 | ✅ | ✅ | ✅ — Resume repair, not deletion | ✅ — command remains present. |
| 30 | ONB §7 #12 | P7 — risk F1 | ✅ | ✅ | ✅ — explicit-path commits | ✅ — Reviewer commit discipline. |
| 31 | ONB §7 #13 | P3 — D73, D74 | ✅ | ✅ | ✅ — workflow ownership, oracle, routes | ✅ — inherited Phase A/B result. |
| 32 | ONB §7 #14 | P6 — process F32, F35, F37–F40, F43 | ✅ | ✅ | ✅ — final evidence, clean receivers, pre-write bounds | ✅ — direct Phase C proof obligations. |

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings?
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Claim & Source Checks filled — 2-3 key claims spot-checked, every citation traced to a real artifact, data claims checked against a primary source (or explicit N/A with a reason)?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist, meanings match, applications are relevant)?
  - Total: 32, resolved: 32, semantically verified: 32, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified (files exist, claims match)?
  - Total evidence items: 8, verified: 5, missing: 0; 3 present artifacts do not substantiate their VERIFIED claim

Stage complete: YES
