# EV — TFW-55 / Phase A.2: North Star Values and Consumer Integrity

> **Date**: 2026-08-26
> **Author**: Codex Executor
> **Environment**: Windows 11, PowerShell, Git, local filesystem
> **TS**: [Phase A.2 TS](../TS__phase-a2__north_star_values_and_consumer_integrity.md)
> **ONB**: [Phase A.2 ONB](../ONB__phase-a2__north_star_values_and_consumer_integrity.md)
> **Verification state**: exact pre-RF pass complete; formal review and post-review closure deferred by role lock

---

## 1. Evidence Verdict

The acceptance checks for AC-1 through AC-9 pass on the Executor state. Their TS evidence
classification is `N/A` because the relevant documents, hashes, diffs, and synthetic local checks are
directly inspectable. AC-10 is `DEFERRED`: a separate Reviewer and the post-APPROVE Coordinator stage
cannot exist during this handoff.

| AC | Acceptance result | Evidence status | Reproducible basis |
|---|---|---|---|
| AC-1 | PASS | N/A | ONB baseline plus final read-only Coordinator recapture and disposable integration test |
| AC-2 | PASS | N/A | 12-row ledger below; cardinality and enum checks |
| AC-3 | PASS | N/A | Heading order, before/final word and line counts, no-filler and brand-block checks |
| AC-4 | PASS | N/A | Required-clause and prohibited-claim scans plus sentence-level source comparison |
| AC-5 | PASS | N/A | Active/history census, anchor checks, TFW-60 exclusion comparison, semantic map |
| AC-6 | PASS | N/A | Plan source inspection, P0/P1 fixture, exact copy hashes |
| AC-7 | PASS | N/A | Review source/template inspection, positive/negative fixtures, exact copy hashes |
| AC-8 | PASS | N/A | Historical zero-diff and corrective-provenance checks |
| AC-9 | PASS | N/A | Exact-final link, scope, UTF-8, whitespace, copy, count, and manifest bundle |
| AC-10 | Executor portion PASS; closure pending | DEFERRED | Separate `/tfw-review`, bounded return loop, and post-APPROVE `/tfw-docs` remain future locked stages |

**Evidence verdict:** 0/10 VERIFIED, 1 DEFERRED, 0 BLOCKED, 9 N/A.

## 2. Approved 8 + 4 Disposition Ledger

Exactly 12 rows are present. Each uses one approved enum and points to current canonical meaning.

| # | Source item | Disposition | Final canonical location | Semantic justification |
|---:|---|---|---|---|
| 1 | TFW-25 — Traces Over Code | `SEMANTIC MERGE` | [NS2 principle 3](../../../../.tfw/README.md#ns2), the Methodology-values synthesis, and NS3 | Selected durable Trace, material continuity, and rationale survive without weakening the invariant. The literal slogan is retired because disposable-code and identical-regeneration implications contradict selected Trace and the current non-goals. |
| 2 | TFW-25 — Candor Over Flattery | `EXPLICIT RESTORE` | [Methodology values](../../../../.tfw/README.md#methodology-values) | The named clause requires evidence-backed disagreement, surfaced risk and uncertainty, and refusal to substitute sycophantic agreement for judgment. |
| 3 | TFW-25 — Completeness Over Speed | `SEMANTIC MERGE` | NS2 principle 5, the Methodology-values synthesis, and [Success Criterion 4](../../../../.tfw/README.md#success-criteria) | Complete, usable, bounded work plus an explicit close or continuation preserves the behavior without making speed or artifact volume a success metric. |
| 4 | TFW-25 — Honesty Over Convincingness | `SEMANTIC MERGE` | [Methodology values](../../../../.tfw/README.md#methodology-values) and NS3 | Visible uncertainty, source boundaries, refusal to fabricate evidence, and bounded capability claims preserve the full honesty invariant without mechanically expanding the named-value list. |
| 5 | TFW-25 — Structural Enforcement | `EXPLICIT RESTORE` | [Methodology values](../../../../.tfw/README.md#methodology-values) | The named clause requires important gates in observable structure or state and distinguishes enforceable structure from prose exhortation. |
| 6 | TFW-25 — Naming Creates Behavior | `EXPLICIT RESTORE` | [Methodology values](../../../../.tfw/README.md#methodology-values) | Precise terms cue the intended cognitive role and action while the clause explicitly avoids claiming that names guarantee compliance. |
| 7 | TFW-25 — Single Source of Truth | `SEMANTIC MERGE` | [Where truth belongs](../../../../.tfw/README.md#where-truth-belongs) | One authoritative owner per truth type preserves the anti-duplication invariant more precisely than one monolithic file and is not weaker than the source value. |
| 8 | TFW-25 — Portability | `EXPLICIT RESTORE` | [Methodology values](../../../../.tfw/README.md#methodology-values) | Ordinary provider-independent files or equivalent inspectable forms protect durable context without claiming that every realization must be Markdown. |
| 9 | TFW-32 — Any team member can resume from any checkpoint | `EXPLICIT RESTORE` | [Success Criterion 1](../../../../.tfw/README.md#success-criteria) | An authorized participant can resume from a durable checkpoint. The actor and checkpoint are bounded, and the clause explicitly rejects a lossless-context promise. |
| 10 | TFW-32 — Every decision is traceable | `SEMANTIC MERGE` | [Success Criterion 2](../../../../.tfw/README.md#success-criteria) | Consequential choices, grounds, alternatives, and dispositions remain traceable; limiting the claim to material decisions avoids an every-message permanence requirement without weakening useful accountability. |
| 11 | TFW-32 — Knowledge compounds over time | `EXPLICIT RESTORE` | [Success Criterion 3](../../../../.tfw/README.md#success-criteria) | Reviewed and verified findings can improve later work; the clause does not promote raw notes automatically or claim lossless compounding. |
| 12 | TFW-32 — The output requires no manual editing | `INTENTIONAL RETIRE` | [Success Criterion 4](../../../../.tfw/README.md#success-criteria) | The absolute conflicts with human judgment and acceptance and implies deterministic reconstruction. Its bounded replacement requires a complete, usable, inspectable, placeholder-free result while retaining authorized human acceptance. |

Cardinality check: `8 TFW-25 + 4 TFW-32 = 12`; enum check: `6 EXPLICIT RESTORE + 5 SEMANTIC MERGE + 1 INTENTIONAL RETIRE = 12`; missing and duplicate source items: `0`.

## 3. North Star Integrity

| Measure | Freeze baseline | Clean Executor final | Expected Coordinator-integrated final |
|---|---:|---:|---:|
| Whitespace-delimited words | 1,548 | 1,857 | 1,864 |
| Lines | 105 | 128 | 132 |
| Word delta from corresponding baseline | — | +309 | +309 from the 1,555-word external baseline |
| Ceiling | 4,200 | PASS, 2,343 words below | PASS, 2,336 words below |

- Final clean SHA-256 for `.tfw/README.md`: `7cbcf1def560ea970ffa003afb9c089ae46a50c45382f04e85e7d6db0e56f875`.
- Heading order remains problem-led: disappearance → chat as raw material → Trace → continuability → human authority → self-describing work → TFW → proportional realizations → NS1 → NS2 → NS3 → Success Criteria → truth ownership.
- Exact legacy heading `Values and Principles`, exact legacy heading `The Thesis`, and the literal slogan `Traces Over Code` occur zero times in the active North Star.
- The approved bounded negations remain explicit: outputs are not disposable or identically regenerable, and resumption does not promise lossless context.
- The correction adds 309 words, not the available headroom; no BoK, implementation manual, artifact inventory, or competing authority surface was added.

## 4. Shared Dirty-State Preservation

The Coordinator worktree `C:\Users\c0rpa\.codex\worktrees\3936\steps-framework` was read only.
The pre-RF recapture matched the ONB baseline exactly.

| Component | ONB start | Pre-RF final | Result |
|---|---|---|---|
| Live HEAD | `f5994b401eca0583b1fed48e8d6a892cfbfcad77` | same | PASS |
| CRLF-normalized porcelain-v2 status SHA-256 | `cbebfd7e1b5859e327f1628c4549c221e7e50ba012f00fd031dca27d0276194e` | same | PASS |
| Tracked dirty / staged | 3 / 0 | 3 / 0 | PASS |
| Untracked count | 93 | 93 | PASS |
| Sorted `path<TAB>sha256<LF>` manifest SHA-256 | `715cae609d3d49f1a905220bd4f63ab33d038d22b3aa5df71cbc38a6ea76eec2` | same | PASS |

Tracked working-state comparison:

| Foreign/overlap path | HEAD blob | Working SHA-256 | Stable patch ID | Final relation |
|---|---|---|---|---|
| `.tfw/README.md` | `71a4d725cff7d0d7508403589195e9f87a0fc49a` | `876e6dca71e4d3ebbc3c13aebf758bd6d02a17a90a05c09cd16cbe5b1ebdd21b` | `9e458b945c8983731b8bc0ed5784edc459b2715a` | exact start match |
| `README.md` | `18b5f799d49aa68c686286de2f4d332a37e8e738` | `846af29f8c353b2cbdfbbf8c9b73989beb57c9aaa2bb91448f4bd7ad1c2a1614` | `676e2256863b13885983a873e948286bfd2a11e2` | exact start match |
| `tasks/TFW-55__canonization_program/research/iterations.yaml` | `23e3eed29a81870b32a1df6e43234480c6b5643f` | `0b0d55969bd42e78a0b77b5e04b05b008ee6914b1dd8435875088c0c8f7da7ca` | `239b53f04738971fb4e9e9abe166d04a6ce5639d` | exact start match |

The complete 93-path manifest is preserved in the [ONB](../ONB__phase-a2__north_star_values_and_consumer_integrity.md#complete-pre-existing-untracked-hash-manifest); aggregate equality proves no path or byte changed. The live TFW-60 Phase A draft remains `767924202e4a75a9790d94628ddcd2b394c18fd70e6ef6fba0c087c643f7e382`.

### Disposable integration proof

The owned production patch was generated from freeze to `d1c82fc`, overlaid onto a disposable
checkout containing the three live Coordinator tracked modifications, and applied with
`git apply --check --whitespace=error-all` followed by `git apply`.

| Preservation assertion | Result |
|---|---|
| Owned production patch SHA-256 | `5d9d735b16c46d8fe675a07f5c1f44ba3bb075e92a8613fad5fd27495e47d4bf` |
| Apply check and apply | PASS / PASS |
| Owner image block present and byte-identical | PASS; UTF-8 block SHA-256 `a52c82d1e76b7c91e5e70c6e2e3a4cfe9bbd87705eb04700e9b571cdf2c16334` |
| Owner image block contribution | 7 words and 4 lines; integrated total 1,864 words and 132 lines |
| Foreign TFW-60 Task Board row | byte-identical before/after integration |
| Owned TFW-55 Task Board row | changed by the owned patch only |
| Foreign research working file | byte-identical SHA-256 `0b0d55969bd42e78a0b77b5e04b05b008ee6914b1dd8435875088c0c8f7da7ca` |
| All 93 untracked files | absent from the patch and unchanged in the live aggregate manifest |

## 5. Consumer and History Boundary

| Check | Result |
|---|---|
| Active consumer scan for `Values and Principles`, `The Thesis`, `Traces Over Code`, `without manual editing`, and `every action` | 0 occurrences across the 12 current production consumers |
| Repository legacy/boundary census | 49 Markdown paths: 46 task traces (including the new corrective EV/RF), 1 changelog history, 1 current KNOWLEDGE path pending post-review correction, and 1 active North Star bounded negation; 0 unclassified active paths |
| TFW-60 master diff | exactly 2 hunks: current header and free §7.2 |
| TFW-60 content outside header and §7.2 | 660 lines before and after; byte-equivalent after allowed-region exclusion |
| TFW-60 base blob / clean final SHA-256 | `bcc5e66daee06f5bb883d4ed8a64ebbaad68e840` / `10a82f655efb5f4af3acc3af981addb5dffba346474b059665918e5b19f226ab` |
| TFW-60 parallel Phase A file | unchanged in the read-only external manifest |
| Original TFW-55 Phase A TS/RF/REVIEW/judge | zero diff |
| TFW-25 task and TFW-32 Phase D source/history | zero diff |

The prior Phase A REVIEW `APPROVE` therefore remains unchanged and valid for the scope it actually
reviewed. The corrective defect was an incomplete acceptance boundary: current framework consumers
were outside the original TS, and resolving file pointers were accepted without checking that the
cited section and claimed meaning still existed. The good problem-led essay was not treated as a
wholly failed result.

## 6. Semantic Consumer Fixtures

| Fixture | File resolves | Item exists | Meaning matches | Application relevant | Expected / actual |
|---|---:|---:|---:|---:|---|
| Positive P0 — `.tfw/README.md#ns2`, selected Trace and continuation | yes | yes | yes | yes | PASS / PASS |
| Positive P1 — `.tfw/README.md#methodology-values`, Structural Enforcement | yes | yes | yes | yes | PASS / PASS |
| Negative — resolving `.tfw/README.md` with deleted `Values and Principles` heading | yes | no | no | no | DISCREPANCY / DISCREPANCY |

Planning now requires priorities 0–4 in full, 5–7 by relevance, separate priority 0 and 1 semantic
items, exact clause/application citations, and reasoned N/A only after the scan. Review now checks
resolution, existence, meaning, and relevance and escalates a resolving-but-wrong item to 100%.
The verification checkpoint counts total, resolved, semantically verified, irrelevant, and
hallucinated citations.

## 7. Copy, Link, Encoding, and Scope Checks

| Check | Result |
|---|---|
| Plan canonical / Claude / Antigravity SHA-256 | all `03943bdc67a0e4a196e316304094419a3165f4e815407cad7ed82c3e427519c4` |
| Review canonical / Claude / Antigravity SHA-256 | all `b0d56ed3a8506e195f07582d9e73497a36447d6c7ed19e32b604300217dff181` |
| Repository full-copy drift census | 11 canonical mappings / 33 files / 0 failures |
| Exact-final new or retargeted local Markdown paths/anchors | 34 checked / 0 path or anchor failures |
| Strict UTF-8 decode | PASS for all modified text files |
| Mojibake scan | 0 replacement/encoding-corruption signatures |
| `git diff --check` | PASS |
| Production scope | exactly 12 planned current consumers, 1 ONB, and the normal TFW-55 Task Board transition |
| Historical/out-of-scope diff | 0 old Phase A, TFW-25, TFW-32, BoK, KNOWLEDGE, TECH_DEBT, changelog, brand, or parallel TFW-60 Phase A files |

## 8. Raw Verification Summary

Commands were run from the replacement worktree unless a `-C` Coordinator path is shown.

```text
git rev-parse HEAD (entry)                         f5994b401eca0583b1fed48e8d6a892cfbfcad77
git log --oneline f5994b4..d1c82fc                 0e7d2bb -> e975ae0 -> d1c82fc
git -C <Coordinator> rev-parse HEAD                f5994b401eca0583b1fed48e8d6a892cfbfcad77
git -C <Coordinator> status --porcelain=v2         96 lines; CRLF-normalized SHA cbebfd7e...
git -C <Coordinator> diff --name-only              3 paths; staged 0
git -C <Coordinator> ls-files --others             93 paths; manifest SHA 715cae60...
git diff --check                                   PASS
strict UTF-8 decode                                failures=0
semantic fixtures                                  failures=0
full-copy map                                      canonical=11, files=33, failures=0
new or retargeted local Markdown links             checked=34, failures=0
active stale-heading/slogan scan                   occurrences=0
repository boundary census                         49 classified paths, unclassified=0
TFW-60 exclusion comparison                        660/660 lines, identical=true
historical path diff                               empty
production changed-path census                     12 planned consumers
North Star count                                   1548 -> 1857 clean; 1864 integrated
disposable git apply --check / apply                PASS / PASS
```

## 9. Role-Separated Closure

The Executor created ONB, implementation, this EV, and RF only. No REVIEW, review stage file,
KNOWLEDGE/TECH_DEBT update, `/tfw-docs`, `/tfw-knowledge`, or BoK artifact was created or modified.
The required next workflow is a separate `/tfw-review`, whose Reviewer must independently rerun
AC-2, AC-5, AC-6, and AC-7. Only REVIEW `APPROVE` may permit the later Coordinator `/tfw-docs`
correction; the three-return ceiling and owner escalation rule remain in force.

---

*EV — TFW-55 / Phase A.2: North Star Values and Consumer Integrity | 2026-08-26*
