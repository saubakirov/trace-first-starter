# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. The evidence from Verify is evaluated separately from the frozen purpose.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | Verify's AC summary finds AC-1 and AC-6 unmet: three mandatory Researcher stage-template reads are absent from the claimed complete graph, and the family mutants reject before producing changed semantic output. This also fails frozen master-HL DoD 3, Principle 9, and Quality Contract 1 because the before/after method omits candidate mandatory reads, even though corrected reductions still clear 30%. |
| 2 | Two clauses, both answered. (a) Purpose Check; (b) Design soundness | ❌ | **(a) ✅ Aligned:** frozen master HL §1 at `f88bffe02eb3fc8c202e483d43ce95d1014422f6` says, “Every TFW role enters each lifecycle checkpoint with the smallest sufficient, role-specific context,” and North Star NS1 requires an authorized successor to “inspect its material grounds and current result” and continue without reconstructing the conversation; the concrete harm at stake is permanent context tax displacing attention while incomplete proof could hide a lost mandatory input. The result introduces no adjacent or deferred feature and the intended harm is material. **(b) ❌ Design soundness:** the compressed role algorithms themselves preserve the cited principles, but the acceptance design is not sound because its graph model suppresses three required reads and five family mutant checks do not reach the produced-output boundary they purport to protect. |
| 3 | Debt disposed | ✅ | RF observation 1 is the same immutable RDP `123>120` diagnostic already ruled in Phase A REVIEW §5: `not material — owed and forbidden to pay — coordinator, 2026-09-03`. The named consequence remains a red `--check tasks` signal that may normalize as noise; payment remains barred by journal immutability and Phase B TS §2/AC-6. No new §5 item is needed or pending. |
| 4 | Style & standards | ✅ | The 23-file implementation surface follows canonical naming, adapter ownership, addressed reads, role locks, and diff hygiene; reviewer trace paths also follow the stage layout. The two findings concern proof correctness, not prose styling. |
| 5 | Observations collected | ✅ | RF §6 records the only reproducible out-of-scope diagnostic. The two material verification defects are verdict findings rather than out-of-scope observations and are carried into REVIEW §4. |
| 6 | RF completeness (§7–9) | ✅ | RF §7, §8, and §9 are all present. “No fact candidates” and “No strategic insights” do not conceal a contradiction or human-only claim; the diagram accurately shows root → skill → workflow → task/shared/template routing and tooling-only copy ownership. |
| 7 | Evidence completeness — does the evidence exist? | ✅ | EV enumerates E1–E6 with allowed statuses and all four attached transcripts exist. Every TS Evidence field has a corresponding claimed environment/action/observable-success entry. This row concerns presence, not probative force. |
| 8 | Evidence sufficiency — does the evidence establish the claim? | ❌ | Green signals establish exact baseline counts, test execution, copy parity, clean receivers, budgets, exclusions, and the 30% floor. They do not establish complete candidate Researcher graphs or one output-changing mutant per P/R/E/V/C/A family; see verify discrepancies 1–2 and evidence table E1–E5. |
| 9 | Backward compatibility | ✅ | Existing consumers are canonical workflows, installed/generated adapters, task artifacts, and clean receivers. Ordinary semantic records match baseline, all copies are byte-equal, receivers expose 11/11 commands, reinstall/idempotence/preservation tests pass, and no changed consumer interface or anchor was found. |
| 10 | Safety | ✅ | Diff and evidence contain no secrets or credentials, add no network or destructive operation, and do not modify immutable history. The known RDP event remains untouched. |

Rows 7 and 8 intentionally differ: the evidence package is complete as a set of artifacts, but two of its acceptance claims are not established by what those artifacts test.

## Purpose Check — row 2 clause (a)

Reference recovery used `conventions.md` §3 rule 15 and the attributed freeze commit `f88bffe02eb3fc8c202e483d43ce95d1014422f6`. The entire master HL at that commit was reread independently of Verify, followed by the root README opening and “How It Works” and `.tfw/README.md` NS1–NS3.

**Outcome: aligned.** “Every TFW role enters each lifecycle checkpoint with the smallest sufficient, role-specific context” serves NS1's inspectable, continuable work: it prevents repeated framework text from exhausting attention while the requirement to retain purpose, grounds, authority, and routes prevents a shorter path from becoming uninspectable. There is no excess/adjacent deliverable, no deferral confession, and the saved attention plus protection against omitted guarantees is material rather than a wording preference.

This purpose result does not override the work defects: the delivered architecture points at the approved value, but its acceptance proof cannot yet justify closing the phase.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D73 — workflow-selected context, source-derived P/R/E/V/C/A records, single manifest | Phase B extends the selective paths and asserts independent family mutants | No contradiction. D73 records the approved Phase A foundation and one output-changing source substitution; it does not assert that Phase B's new per-family requirement is already satisfied. The Phase B failure is an unverified extension, not a conflict with current knowledge. |

RF §7 contains no Fact Candidates. That is acceptable for this revision: no Human-Only claim requires challenge, and durable Phase B knowledge must not be promoted before an approved review.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence?
- [x] Every `⚪ N/A` carries a stated reason? No N/A status was used.
- [x] Row 2(a) answered against the master-HL contract baseline and North Star, never the TS or Phase HL, with a quoted clause and named harm?
- [x] Rows 7 and 8 answered separately with different reasoning?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Row 3 disposes the sole observation through the existing Coordinator ruling, names its persistent consequence, and cites the barring clauses?
- [x] RF §7–9 checked for presence and quality?
- [x] KNOWLEDGE.md cross-referenced and contradiction result documented?
- [x] RF Fact Candidates reviewed; none require challenge?

Stage complete: YES
