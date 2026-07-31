# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Mode: code
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | `verify.md` Acceptance matrices: TS AC 7/7, HL DoD 10/10, DoF 11/11 absent |
| 2 | Philosophy aligned | ✅ | P1–P10 each has an observable implementation/proof relation; one owner/router, explicit authority, action locality, truthful replay, separate publication, thin adapters, and Phase C boundary all hold |
| 3 | Tech debt documented | ✅ | RF §6 reports no observation; independent 100% scope/test/render audit found no qualifying new debt. TD-125/TD-126 are unchanged and not duplicated |
| 4 | Style & standards | ✅ | Standard-library production code, frozen data records, explicit type hints, stable error codes, schema-owned validation, safe top-level exception boundary, clean patch, 2/2 compile |
| 5 | Observations collected | ✅ | RF §6 was challenged; unchanged warning debt is accurately attributed to TD-125 and no new product defect was found |
| 6 | RF completeness (§7–9) | ✅ | §7 explicitly reports no Fact Candidates, §8 contains the disclosed scope-attention insight, §9 contains an accurate owner/router/publication diagram |
| 7 | Evidence completeness | ✅ | All seven TS Evidence fields have EV rows; all seven N/A reasons are claim-based and independently justified; PR-B1–PR-B8 resolve |

## Mode-Specific Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 7 | Code quality | ✅ | Router owns only workflow/operation policy, imports Phase A truth owners, performs no Git/config/network action, and compiles cleanly |
| 8 | Test coverage | ✅ | 285 combined contract tests, 68 docs tests, 149 router cases, and 92% branch-aware router coverage; independent operation/security probes agree |
| 9 | Security | ✅ | Explicit context, guarded `task:none`, exact equality, current-operator replay, no external/global hook access, safe diagnostics, false publication/authentication flags |
| 10 | Breaking changes | ✅ | Phase A owners/config/legacy paths unchanged; installed workflow copies are restored to canonical parity; root adapter instructions outside approved blocks are preserved; Cursor remains absent |

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|----------------|----------|----------------|
| 1 | D54 — thin adapter surfaces and behavioral parity | Four templates declare only surface; installed consumers delegate semantics to canonical workflow/router | No |
| 2 | D55 — rule locality and complete authority at the consequence boundary | Router cues exist only at the three current action surfaces and include the complete authority/non-publication consequence | No |
| 3 | D57 — Proof/Verification/Evidence/RF/REVIEW are distinct | Router and RF explicitly deny authentication, Proof, Evidence, attestation, or review authority | No |
| 4 | D58 — Phase B routing/consumption; Phase C hooks/config/migration/cross-agent proof | Phase A owners are unchanged; Phase B implements router/consumers only; Phase C remains absent/open | No |
| 5 | process F26 — push is a separate human boundary | Handoff/docs/release and every returned plan preserve local-only completion; remote ref remains unchanged | No |

## Fact Candidate Challenge

RF §7's “No Fact Candidates” is supported. The only human-only publication signal is
already consolidated as process F26. RF §8 S1 is an execution judgment about a
measured task-local scope boundary, not a new human-only project fact. The review
conversation introduced no new Human-Only candidate.

## Judgment

The Phase B result is sufficient for approval. The executable boundary is independently
reproduced, the complete physical consumer set matches the authorized scope, every
claim and negative boundary is traceable, and the only non-reproduced detail is the
exact browser layout-width observation. That limitation does not undermine the
rendered-content seam because both builds, warning sets, required headings, anchors,
and 251 local links across the three target pages were independently verified.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Checked RF §7–9 for presence AND quality (not just existence)?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"?
- [x] Fact Candidates from RF reviewed — any that need challenge?

Stage complete: YES
