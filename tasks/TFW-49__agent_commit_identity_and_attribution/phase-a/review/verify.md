# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: code
> Min verify ratio: 0.42
> RF files claimed: 8
> Files to verify: ⌈8 × 0.42⌉ = 4
> Actual coverage: 8/8 claimed paths, the RF itself, all 10 AC, and all 10 EV rows

## Verification Log

### V1: `.tfw/commit_identity.schema.json`
- **RF claim:** Sole operational owner for accepted C1-R data, including grammar,
  forms, trailers, example inputs, and the truth boundary.
- **Actual:** The production record contains the claimed values and patterns and the
  executable consumes registry/pattern fixture mutations. However, schema validation
  accepts a record with `truth_boundary` removed and accepts
  `grammar.identity_template: "not-an-identity"`.
- **Match:** ❌ partial — production content is correct, but the declared schema-shape
  gate does not validate all consumed semantic-owner fields.

### V2: `.tfw/commit_identity_state.json`
- **RF claim:** Separate `agent-managed` state with contract `1.0.0`, the full
  exclusive activation anchor, and false hook/authentication claims.
- **Actual:** Exact values are present; current validation and ancestry checks pass;
  state contains no copied universal registry.
- **Match:** ✅

### V3: `.tfw/scripts/commit_identity.py`
- **RF claim:** Standard-library formatter/parser/message validator/context comparator
  and fail-closed exact range auditor.
- **Actual:** Runtime imports are standard-library only. Formatting, parsing,
  normalization, trailers, guarded `task:none`, diagnostics, and the Git DAG audit
  behave as claimed except that a reserved form without supplied expected context is
  accepted by the public `validate-subject` command.
- **Match:** ❌ partial — stale supplied context fails, but absent context succeeds
  contrary to TS AC-4 and RF/EV PR-4.

### V4: `.tfw/scripts/test_commit_identity.py`
- **RF claim:** Forty-six tests cover contract mutation, diagnostics, staged paths,
  trailers, and temporary Git topology.
- **Actual:** All 46 tests pass and cover the named Git/state/parser scenarios. The
  suite explicitly exercises reserved structural parsing but has no assertion that
  public validation rejects absent expected context, and its schema-shape fixtures do
  not reject a missing truth boundary or semantically invalid identity template.
- **Match:** ❌ partial — passing tests do not cover the two acceptance-critical gaps.

### V5: `.tfw/conventions.md` and `.tfw/glossary.md`
- **RF claim:** Canonical human contract and concise glossary references with operator,
  origin, range, bypass, non-authentication, and Phase B/C boundaries.
- **Actual:** Required headings, semantics, C2-R rejection, owner links, six non-claims,
  bypasses, and phase boundaries are present. Generated anchors resolve, the rendered
  conventions table has six rows including its header, and neither inspected page
  overflows horizontally.
- **Match:** ✅

### V6: `phase-a/evidence/EV__phase-a__canonical_contract_and_validator.md`
- **RF claim:** Ten Proof Records and ten Evidence rows cover all AC, with 8 N/A and
  2 VERIFIED dispositions.
- **Actual:** All rows and referenced artifacts exist. The N/A dispositions are
  appropriate for deterministic Local/Seam claims under the Trust Protocol, and the
  two rendered/current-repository observations were independently reproduced.
  PR-1 and PR-4 nevertheless overstate the behavior described in V1 and V3.
- **Match:** ❌ partial

### V7: `README.md`
- **RF claim:** Lifecycle trace advanced to RF with ONB/RF links.
- **Actual:** The TFW-49 row is at `🟢 RF (A)` and both links resolve.
- **Match:** ✅

### V8: exact implementation range and protected state
- **RF claim:** Only six approved framework consumers plus EV/RF/README traces changed;
  no hooks, config, workflows, adapters, knowledge, or history were modified.
- **Actual:** `7740d83e..b83d8ee3` contains exactly the six approved framework paths
  plus EV/RF/README. The implementation commit has the ONB baseline as its direct
  parent. `.tfw/hooks` has no tracked paths, repository-local `core.hooksPath` remains
  unset, and no protected implementation path changed.
- **Match:** ✅

## Commands Executed

| # | Command / method | Result |
|---|------------------|--------|
| 1 | `python -m pytest .tfw/scripts/test_commit_identity.py -q` | `46 passed in 11.89s` |
| 2 | `python -m compileall -q .tfw/scripts/commit_identity.py`; `validate-state`; `describe` | Compilation passed; state/description were valid and machine-readable |
| 3 | `python .tfw/scripts/commit_identity.py audit-range --repo .` at `b83d8ee3` | Exact exclusive range valid; four descendants; `actor_authentication:false` |
| 4 | `python -m pytest docs/scripts/test_gen_docs.py docs/scripts/test_integration.py -q` in an isolated final-commit worktree | `68 passed in 29.22s` |
| 5 | Identical `python -m mkdocs build --config-file docs/mkdocs.yml` in isolated `7740d83e` and `b83d8ee3` worktrees | Both exit 0; both have 283 warning lines and 131 normalized distinct warnings; set delta is 0 added / 0 removed |
| 6 | In-app browser inspection of generated conventions/glossary anchors | Both anchors, three owner links per section, required content, and `1265/1265` no-overflow layout reproduced |
| 7 | `git diff --name-status`, `--numstat`, `--check`, parent/range/config/hook scans | Exact six framework consumers; 1,307 cohesive framework lines; protected state unchanged; diff check passed |
| 8 | Malformed-schema library probe | Missing `truth_boundary` and invalid `identity_template` both accepted by schema/state validation; invalid template fails only later as `E_SUBJECT_FORMAT` |
| 9 | Public reserved-form CLI probe | No expected context: exit 0 and `{"form":"fixup","status":"valid"}`; stale context: exit 2 with `E_CONTEXT_MISMATCH` |
| 10 | Phase/Master citation target and ONB mirror scan | 22/22 targets resolve; ONB records all 22 |

## Discrepancies Found

1. **D1 — incomplete schema-shape enforcement.** `validate_schema` accepts a contract
   with the schema-owned `truth_boundary` removed and accepts an unusable
   `identity_template`. This contradicts the Phase HL's in-scope schema validation,
   AC-1/PR-1's valid versioned semantic-owner claim, and AC-6's field-specific
   failure-before-fabrication boundary. The malformed template is rejected only later
   as `E_SUBJECT_FORMAT`, while missing truth data reaches a later generic operation
   failure.
2. **D2 — missing expected context is accepted for reserved forms.** The public CLI
   accepts `fixup! [codex/TFW-49/phase-a/reviewer] target` with no expected fields.
   TS AC-4 says reserved forms validate only with supplied exact four-field context;
   RF §2/§3 and EV PR-4 explicitly say absence fails. Stale supplied context correctly
   fails. The structural-only path used by range audit can remain separate, but the
   public contextual validation claim is false.
3. **D3 — RF V3 warning measurements are not reproducible.** With exact detached
   baseline/final inputs and the same MkDocs command, both commits produce 283 warning
   lines and 131 normalized distinct warnings, with a zero-set delta. RF V3 reports
   `284/283`, `132/136`, and `11 added / 7 removed`. The stronger product conclusion
   is favorable—no warning changed—but the attested measurements and attribution must
   be corrected.

Any discrepancy requires 100% escalation; all claimed paths, AC, Principles, Proof
Records, Evidence rows, and protected boundaries were therefore checked.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|-----------------|------------------|----------------|
| E1 / PR-1 | ✅ | ❌ partial — production ownership is real, schema-shape completeness is overstated |
| E2 / PR-2 | ✅ | ✅ — state/version/anchor and N/A disposition reproduced |
| E3 / PR-3 | ✅ | ✅ — deterministic C1-R behavior reproduced |
| E4 / PR-4 | ✅ | ❌ — absent expected context succeeds |
| E5 / PR-5 | ✅ | ✅ — `task:none`, origins, metadata, and co-author separation reproduced |
| E6 / PR-6 | ✅ | ❌ partial — normal diagnostics are safe, but malformed owner semantics are not rejected at the schema field boundary |
| E7 / PR-7 | ✅ | ✅ — exact DAG/range edge matrix and current audit pass |
| E8 / PR-8 | ✅ | ✅ — six-consumer non-claim scan passes |
| E9 / PR-9 | ✅ | ✅ — rendered anchor/link/layout observation independently reproduced |
| E10 / PR-10 | ✅ | ✅ — exact scope, current repository, absent permanent hooks, and rendered sub-boundary reproduced |

Evidence status audit: 8 N/A dispositions are justified for deterministic Local/Seam
claims; E9/E10 are proportionate VERIFIED observations. Status labels do not cure the
false PR-1/PR-4 statements or RF V3 measurements.

## Knowledge Citations Verified

| # | Artifact | Citation set | Link resolves? | Item exists? |
|---|----------|--------------|----------------|--------------|
| 1 | Phase HL §7.1 | Master HL, RES D1–D9, D28/D54/D55/D57, two philosophy headings, Role Lock, Challenge C1–C8 | ✅ 10/10 | ✅ 10/10 |
| 2 | Master HL §7.2 | Six philosophy headings, D28/D54/D55/D57, Role Lock, Session Naming | ✅ 12/12 | ✅ 12/12 |
| 3 | ONB §7 | Mirrors both citation sets and records their application | ✅ 22/22 | ✅ 22/22 |

No citation hallucination or contradiction with D28, D54, D55, or D57 was found.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈8 × 0.42⌉ files and recorded findings?
- [x] Ran at least 1 build/test command?
- [x] Each RF §3 AC checkmark verified against actual files?
- [x] KNOWLEDGE.md and all applicable Project Value sources checked?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total Phase/Master citations: 22, verified: 22, hallucinations: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 10, verified without discrepancy: 7, partial/false: 3, missing: 0

Stage complete: YES
