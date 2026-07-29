# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Mode: spec
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | Verify §Acceptance-Criteria Verification: 5/9 AC pass; AC-1, AC-3, AC-5, and AC-9 fail because active glossary/conventions contracts retain retired count and competing procedure semantics. |
| 2 | Philosophy aligned | ❌ | Principles P2, P4, P5, and P8 fail. The new contract is value-first, but the complete affected consumer set is not yet internally honest or precise. |
| 3 | Tech debt documented | ✅ | RF §6 names existing TD-125/126 and no new out-of-scope debt survives review. Verify D1–D4 are current in-scope defects and RF inaccuracies, so converting them into backlog debt would evade the approved TS. |
| 4 | Style & standards | ❌ | The same public glossary/conventions surfaces give incompatible authority to counts and stage order. That violates single-owner, precise-definition, and point-of-use consistency standards. |
| 5 | Observations collected | ✅ | RF's no-observation declaration was challenged against the diff and conversation history. No new out-of-scope observation qualifies; discovered problems are revision items, not observations. |
| 6 | RF completeness (§7–9) | ✅ | §§7–9 are present. The no-Fact-Candidate/no-execution-insight claims survive the human-only/history check, and the diagram accurately shows the intended new flow. |
| 7 | Evidence completeness | ❌ | All 9/9 EV rows exist and use TS-valid dispositions, but E1, E3, E5, and E9 do not substantively match the affected source/rendered content. |

## Mode-Specific Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 8 | Analytical quality | ❌ | The new ledger and procedures are methodologically coherent in isolation, but the delivered system simultaneously publishes legacy minimum/maximum/required-count rules. RF also misses those contradictions and overstates four word counts. |
| 9 | Source attribution | ✅ | All 27/27 HL/ONB citation rows resolve to real artifacts/items; commits `8758529`, `4466109`, and `d2f1466`, tests, source lines, and rendered pages are independently traceable. |

## Principles Check

The Coordinator request referred to "10/10 Principles", but the approved Phase B HL
contains twelve numbered principles. Canonical completeness governs, so all 12/12 were
judged rather than silently dropping two.

| # | Approved Phase B principle | Status | Evidence |
|---|----------------------------|--------|----------|
| P1 | Purpose Before Procedure | ✅ | Plan starts from product purpose, Project Values, uncertainty, and evidence need before the FIT/MISMATCH gate. |
| P2 | One Operational Method, Honest Scope | ❌ | New fit/mismatch behavior is bounded, but glossary `RESEARCH`, Stage, Dimension, and Alternative entries still publish generic/flexible/count-conditioned research behavior. |
| P3 | Intensity Is Not Method | ✅ | Focused/deep change breadth, counter-evidence, edge cases, and residual uncertainty while retaining one procedure. |
| P4 | Meaning Before Number | ❌ | Legacy Pass, `min_iterations`, dimension/alternative, and `max_iterations` ceiling statements still grant unsupported normativity. |
| P5 | Completion Is a Claim | ❌ | A hard minimum-iteration gate, recommended pass maximum, and soft iteration ceiling still compete with evidence/decision closure. |
| P6 | Learning Is Selected and Routed | ✅ | All four stage templates provide triggered, typed receipts plus intentional no-signal records. |
| P7 | Existing Surfaces Before New Sections | ✅ | HL, stage checkpoints, RES, open threads, and Fact Candidates are reused; no top-level capture section or framework file was added. |
| P8 | Precision Compresses Context | ❌ | New concise owner definitions do not compress reliably while stale public definitions retain contradictory operational rules. |
| P9 | Reality Can Overrule the Plan | ✅ | Counter-evidence, exclusions, changed decisions, reopen outcomes, and unresolved gaps are explicit. |
| P10 | Human Authority Remains Visible | ✅ | Mismatch, closure, additional-iteration triggers, unresolved outcomes, and RES return to Coordinator/user authority. |
| P11 | Domain-Agnostic by Design | ✅ | Product/content, operational, documentation, open exploration, and software examples do not default to code. |
| P12 | Method Claims Need Evidence | ✅ | H4 stays unresolved/T0-only; no selector, catalog, runtime choice, benefit claim, or prohibited comparison appears. |

**Principles result:** 8/12 pass; P2, P4, P5, and P8 fail.

## Definition-of-Failure Check

| TS Definition of Failure | Triggered? | Evidence |
|--------------------------|------------|----------|
| Any retired count is replaced by another unsupported number, hidden quota, or equivalent count language | **YES** | The affected glossary retains a minimum pass, recommended maximum passes, a hard `min_iterations` floor, and mandatory dimension/alternative counts; conventions retains `max_iterations` as a soft ceiling. |
| Config or config-template values change | No | Both diffs are empty. |
| `min_iterations` removal allows incomplete stage traces or bypasses Coordinator closure | No | Base preserves Briefing → Gather → Extract → Challenge → RES and Coordinator/user closure. |
| H4 architecture/benefit claim appears | No | H4/T0 boundary scans and semantic review pass. |
| New framework file/top-level capture section appears | No | Exactly twelve existing framework consumers changed; zero framework files added. |
| Later-phase consumers are modified or falsely declared implemented | No | Phase D/E/F boundaries remain explicit and later workflow consumers are untouched. |

One explicit Definition of Failure is enough to prevent APPROVE.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|----------------|----------|----------------|
| 1 | D23 — compress workflows through ownership and template references | RF claims one glossary definition/operational owner and compressed point-of-use gates | **Yes.** Legacy glossary entries continue to carry competing operational stage/count rules. |
| 2 | D49 — preserve natural research structure and TS requirements-first authority | RF claims natural Gather → Extract → Challenge dependency without numeric quotas | **Yes.** Glossary says stage order is flexible and binds configuration behavior to minimum dimensions/alternatives. |
| 3 | D55 — five protected obligations and typed objects govern Phase B | RF claims every hard-looking number has a lifecycle disposition and cannot silently decide closure | **Yes.** Legacy hard-floor/soft-ceiling/recommended-count text remains an active authority outside the ledger. |
| 4 | D37 — docs/knowledge write-boundary | RF claims Phase D remains the downstream promotion owner | No. RES and conventions preserve the transitional boundary; this review does not run `/tfw-docs` or `/tfw-knowledge`. |
| 5 | D43 — Project Values citation cascade | RF claims the existing cascade remains intact | No. Planning references the existing owners rather than duplicating them. |

## Fact-Candidate and Insight Challenge

No Fact Candidate is added. The human's value-first goals, concern about visible proxy
budgets, cross-domain requirement, learning-loop direction, and H4 skepticism are
already recorded in the approved master/Phase B planning traces. Coordinator execution
messages supplied approval and boundary restatement, not a new human-only fact. The
review findings are reproducible from repository source and commands, so they fail the
Human-Only Test and belong only in Verify/Verdict.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Checked RF §§7–9 for presence and quality?
- [x] KNOWLEDGE.md cross-referenced and contradictions documented?
- [x] Fact Candidates and conversation history challenged without inventing facts?
- [x] All 12 approved Phase B principles judged?
- [x] Definition of Failure checked?

Stage complete: YES
