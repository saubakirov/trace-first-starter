# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | [verify.md](verify.md) discrepancy 1: AC-1, AC-2 and AC-4–AC-6 reproduce, but AC-3's Gate/Evidence contract requires an actual reviewed crossing landing and exact Candidate reachability before cleanup. EV E3b is still `DEFERRED`, while RF §3 marks AC-3 complete. |
| 2 | Two clauses, both answered. (a) Purpose Check; (b) Design soundness | ✅ | **(a)** Against contract-baseline Master HL blob `90f2f9d…` at freeze `11888e…` plus live NS1: *“another authorized person or agent can … inspect its material grounds and current result, see where authority remains, and continue”* is served by isolated indexes and producer-attributed path history; without them, foreign staging or a landing under the wrong task hides ownership and makes safe continuation materially unreliable. There is no excess, different-home confession, or internal reference-set conflict. **(b)** The design is sound against frozen HL §7: Git owns the mechanism, TFW owns the protocol; isolation is not a lock; exact staging is structural enforcement; short role edges preserve selective reads. The missing landing is incomplete execution, not a design defect. |
| 3 | Debt disposed | ✅ | The four §5 rows to be synthesized have admissible, concrete proposals: the AC-3 return targets the existing Phase A directory; the manifest item targets the existing master task and its Phase E obligation; the stale ordinals and immutable RDP event state why they are owed-but-forbidden or not owed here. Each remains `pending — coordinator`, which is legal and keeps the task open until the Coordinator rules once. No bare priority or nonexistent “backlog” target is used. |
| 4 | Style & standards | ✅ | All seven VALUE paths stay inside the literal selector; unique headings, Markdown structure, named prohibitions, exact-path commands, Candidate ordering, and tracked-copy parity hold. `git diff --check` passes. The two stale citation ordinals are pre-existing Master-HL §7.2 observations and are separately recorded, not hidden. |
| 5 | Observations collected | ✅ | RF §6 contains three real, source-backed issues: manifest topology mismatch, two stale NS2 ordinals, and an immutable other-task summary exceeding the census ceiling. Review triage names the inspectability/continuation consequence or its material absence for each. |
| 6 | RF completeness (§7–9) | ✅ | RF §7 explicitly says no Fact Candidates; §8 explicitly says no Strategic Insights; §9 contains a coherent lifecycle diagram whose REVIEW -> landing -> reachability -> cleanup order is consistent with the governing contract. |
| 7 | Evidence completeness — does the evidence exist? | ✅ | EV exists and supplies one row for every TS evidence obligation, including the dedicated immutable accounting row. All seven statuses use the permitted vocabulary; 6 are VERIFIED and E3b is explicitly DEFERRED with owner, dependency, and timing named. |
| 8 | Evidence sufficiency — does the evidence establish the claim? | ❌ | The green signals establish implementation text, exact staging, parity, word necessity, tests, and accounting. They do not establish AC-3 completion: E3b explicitly says the actual post-review landing did not occur. Historical `87c26bb…` has no REVIEW in its tree and is not current-lineage evidence. |
| 9 | Backward compatibility | ✅ | Handoff and Review still expose their prior ordered checkpoints, Candidate/accounting/Purpose semantics remain, canonical copy groups are byte-identical, headings are unique, the structural check passes, and independent runtime-context/full suites pass 2/2 and 306/306. No interface, template section, anchor, or downstream process was removed. |
| 10 | Safety | ✅ | No secret, credential, runtime, hook, daemon, destructive command, or behavior-selecting config was added. Reviewer verification did not remove a worktree or rewrite user files; the canonical protocol explicitly withholds cleanup until reviewed landing and exact Candidate reachability are proved. |

Rows 7 and 8 deliberately differ: the evidence set is complete and candid, but one candid `DEFERRED` row cannot prove the RF's completed AC-3 claim.

## Purpose Check — row 2 clause (a)

Contract baseline recovery selected freeze `11888e547b0b37dc09469aee8fe2fd897d797906`; the Master HL blob there is `90f2f9d9fd85e079fd3d5c88d0644079ed3edd32`, identical to review-ready HEAD. The Project North Star was reread independently from `.tfw/README.md` NS1–NS3.

**Aligned:** *“another authorized person or agent can … inspect its material grounds and current result, see where authority remains, and continue”* is served by preventing shared-index contamination and making a crossed deliverable recoverable under its producer; the concrete harm avoided is an apparently valid history whose staged content or task attribution belongs to a different session, making later authority and continuation materially unreliable.

- **Excess and adjacency:** no. The seven files implement only frozen Master-HL Phase A deliverables 1–5 and add no runtime, transport, branch policy, provider canon, or new artifact class.
- **Deferral confession:** no off-purpose work shipped. E3b confesses an unfinished required landing step, not a different home for implemented VALUE.
- **Materiality:** the purpose value is material because the frozen Vision and NS1 expressly require inspectable authority and continuation; this is not a wording objection.
- **Reference consistency:** no conflict. The baseline requires isolated worktrees and attributable crossings; NS1–NS3 require purposeful, provider-independent continuity. Satisfying either does not violate the other.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D55 — commit subject is searchable declared task context | Landing rule and Candidate subject preserve producer task/phase attribution | No. |
| 2 | D59 — recoverability is not locking; a separate session is not an independent person | Canon expressly says worktree isolation is neither lock nor merge strategy and makes no independence claim | No. |
| 3 | D68 — task-local state and opaque event token | Phase state/journal remain task-local; no actor identity is placed in the token | No. |
| 4 | D73 — workflow-owned ordered reads and one adapter topology | Short checkpoint edges preserve ordered reads and literal tracked copies are synchronized | No implementation contradiction. The pre-existing manifest singular/plural mismatch is correctly reported for later disposition. |
| 5 | D74/D75 — selective role paths preserve semantics with bounded context | No universal preamble was restored; targeted and full runtime-context suites pass | No. |

RF contains no Fact Candidates to challenge.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just a symbol)?
- [x] Every `⚪ N/A` carries a stated reason? No N/A row is used.
- [x] Row 2(a) answered against contract-baseline Master HL and Project North Star, never TS/Phase HL, with one quoted clause and a named material harm?
- [x] Rows 7 and 8 answered separately with different reasoning?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Row 3 prepares every §5 row for one Coordinator ruling, with existing targets and named consequences/absences?
- [x] Checked RF §§7–9 for presence and quality?
- [x] KNOWLEDGE.md cross-referenced and contradictions documented?
- [x] Fact Candidates from RF reviewed? RF has none.

Stage complete: YES
