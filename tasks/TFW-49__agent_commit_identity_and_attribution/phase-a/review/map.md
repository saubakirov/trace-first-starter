# Map — "What was done?"
> **Mindset:** Experienced newcomer. Understand before judging.
> **Test:** "Can I explain what was done without relying on the RF?"
> RF: [RF Phase A](../RF__phase-a__canonical_contract_and_validator.md)
> TS: [TS Phase A](../TS__phase-a__canonical_contract_and_validator.md)
> Mode: code

## Understanding

Phase A introduces a prospective C1-R commit-identity contract through exactly six
framework consumers: a versioned JSON schema, project activation state, a
standard-library Python formatter/parser/message validator/range auditor, its tests,
and canonical conventions/glossary documentation. The schema owns accepted values,
patterns, forms, templates, trailers, and the truth boundary. Project state separately
owns policy, contract version, the full last-pre-policy anchor, and explicit false
hook/authentication claims.

The executable validates ordinary C1-R subjects, guarded `task:none`, complete
content-origin records, optional metadata, co-author coexistence, same-context Git
reserved forms, secret-safe diagnostics, and the exact exclusive `anchor..target`
commit graph. Phase A deliberately does not implement commit routing, permanent
hooks, Git configuration, workflow/adapter consumers, authentication, Proof Records,
or acceptance authority.

The corrective result at `b4c0a06dc9fbc104c5b8997865b6df3211bd5c0c` closes the
prior REVIEW findings by validating every downstream-consumed owner field, separating
public context-required parsing from the range audit's private structural path, adding
the corresponding negative coverage, and correcting the MkDocs warning attribution.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — schema is the sole accepted-value/pattern owner and all consumed owner fields fail closed | RF AC-1 / PR-1 claims exhaustive field and semantic validation with field-specific diagnostics and fixture-driven consumption | Yes; truth checked in Verify |
| AC-2 — separate state owns `agent-managed`, version relation, full anchor, and false hook/auth claims | RF AC-2 / PR-2 states the exact values and fail-closed state validation | Yes; truth checked in Verify |
| AC-3 — exact C1-R format, parser, normalization, and independent search keys | RF AC-3 / PR-3 claims the complete registry/work-class matrix and unsafe-input rejection | Yes; truth checked in Verify |
| AC-4 — reserved forms require exact expected context | RF AC-4 / PR-4 claims absent `E_EXPECTED_CONTEXT`, stale `E_CONTEXT_MISMATCH`, and a private range-only structural path | Yes; truth checked in Verify |
| AC-5 — operator meaning, guarded `task:none`, full origins, metadata, and co-authorship remain distinct | RF AC-5 / PR-5 claims the same boundary | Yes; truth checked in Verify |
| AC-6 — stable actionable diagnostics disclose no arbitrary local or sensitive content | RF AC-6 / PR-1/PR-4/PR-6 claims field-specific failures, synthetic correction, and non-disclosure | Yes; truth checked in Verify |
| AC-7 — exact exclusive anchored DAG audit is complete and fail closed | RF AC-7 / PR-2/PR-7 claims anchor exclusion and all required topology/error cases | Yes; truth checked in Verify |
| AC-8 — provenance/non-authentication/authority boundaries are explicit | RF AC-8 / PR-8 claims the six non-claims, bypasses, and Phase B/C boundaries | Yes; truth checked in Verify |
| AC-9 — examples and owner links consume the schema and render | RF AC-9 / PR-1/PR-9 claims executable examples, no prose registry, rendered anchors, owner links, and readable layout | Yes; truth checked in Verify |
| AC-10 — exact six-consumer scope and reproducible quality | RF AC-10 / PR-7/PR-9/PR-10 claims 136 contract tests, 68 docs tests, identical MkDocs results, exact range, and protected state | Yes; truth checked in Verify |

## Deviations and Attention Signals

The RF declares no requirement or scope deviation. The original implementation was
1,307 framework lines. The corrective tree is 1,708 lines: 857 executable, 609 tests,
160 JSON, and 82 documentation additions. The 401-line increase is confined to the
same conventions/parser/test proof surface and directly implements prior D1/D2. The
final result is 508 lines over the configured 1,200 LOC attention signal, but the
signal remains descriptive rather than an automatic failure gate; Verify and Judge
must assess cohesion and phase boundaries independently.

The user later established a separate publication boundary: completion and a local
C1-R review commit do not authorize remote push. This does not change Phase A product
scope or verdict criteria, but it governs the review trace lifecycle and is challenged
as a Human-Only Fact Candidate in Judge/REVIEW.

## Checkpoint

**Self-check:**
- [x] RF §§1–9 read completely
- [x] TS Acceptance Criteria, Definition of Failure, and Evidence fields mapped
- [x] Phase HL Principles and Definition of Failure mapped
- [x] ONB scope, blockers, citations, and commit baseline understood
- [x] Prior REVISE D1–D3 and corrective claims isolated without limiting review to the patch

Stage complete: YES
