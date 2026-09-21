# Judge — formal review round 2

> **Mindset:** Judge. Evidence from Verify → rule on quality.
> **Test:** Would I stake my reputation on this passing production review?
> **Verify findings:** [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---:|---|---|---|
| 1 | DoD met? | ❌ | Candidate implementation, accounting, configured checks, parity, receiver safety and D75 route hold, but `verify.md` discrepancy 1 shows that the required rung-2 positive/material-negative replay cannot be reconstructed from the evidence. Master DoD 10's behavior-justified subtraction and DoD 15's complete accepted return lineage are therefore not fully established. |
| 2 | Two clauses: **(a) Purpose Check**; **(b) Design soundness** | ✅ | **(a) Aligned.** Baseline HL §1 requires artifacts to be “smaller, mutually consistent and behaviorally complete”; North Star NS1 requires an authorized participant to “inspect its material grounds and current result” and continue without rebuilding the conversation. The concrete harm is a compressed authority/coordination rule whose material negative behavior cannot be inspected, causing a later role to trust an unsupported `PASS` or reconstruct the oracle. The Candidate addresses the intended consistency/reader-cost problem and adds no adjacent work; the finding is incomplete proof, not a different purpose. **(b) Sound.** Canonical ownership, exact projections, provider-local capability limits and transcript isolation are coherent with HL §7; no implementation design defect was found. |
| 3 | Debt disposed / honest pending ruling | ✅ | One REVIEW §5 proposal is prepared as `pending — coordinator`, which legally keeps Phase B open. It routes an evidence-only AC-3/AC-10/AC-12 repair to the existing `phase-b/` lineage and names the consequence: without an exact harness the claimed replay is not independently inspectable. The Reviewer does not rule or repair it. D75 remains the already-required post-APPROVE Docs effect; receiver changes remain not owed under TS §2 and DoF 7/12. |
| 4 | Style & standards | ❌ | Candidate naming, headings, exact-path isolation, Markdown, word ceilings, links and copy parity hold. The required evidence standard does not: `rung2-semantic-replay.txt` labels its output exact while omitting the command and predicates that produced it, contrary to reproducible, file-first trace practice and the AC-3 traceability gate. |
| 5 | Observations collected | ✅ | RF §6 correctly carries only the pre-existing D75 route and excludes receiver work. Verify adds one concrete, source-backed evidence finding rather than a generic backlog item. |
| 6 | RF completeness (§7–9) | ✅ | Final Return Round 2 includes §7 Fact Candidates, §8 Strategic Insights and §9 Diagrams. Each explicitly says none and gives a bounded reason compatible with this implementation/evidence return. |
| 7 | Evidence completeness — does it exist? | ✅ | Every TS evidence artifact and EV row exists, including the new rung-2 replay file; E9 candidly remains downstream. This is only an existence judgment. |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | Strong green signals establish exact accounting, all ten word ceilings, 20/20 projections, three persistent-target matches, 14 tests, 54 dry-run schedules, 84 links, metric pairs and the receiver epoch. They do not establish that the 32 rung-2 `PASS` labels were produced by Candidate-derived predicates or material-negative mutations: the executed command/harness is absent. E3-R2, and the scenario portions of E10-R2/E12-R2, are therefore only partial. |
| 9 | Backward compatibility | ✅ | Historical artifact forms remain readable, no history or receiver tree is rewritten, true task phases/cognitive stages/config modes remain named correctly, all generated/managed copies match sources, and the configured suite passes. No existing consumer or active anchor was found broken. |
| 10 | Safety | ✅ | No secret, credential, destructive action, receiver mutation, history rewrite, runtime service, release, push or publication occurred. The Reviewer used an isolated detached Candidate worktree and exact-path commits; unrelated user paths remain unstaged. |

Rows 7 and 8 deliberately differ: the required evidence file exists, but its claimed execution is not
independently reconstructable from the durable record.

## Purpose Check — row 2 clause (a)

**Reference set:** master HL at A4 contract baseline
`35fba767abd768413237bf6416102e189f1d91e6`, plus root `README.md` and `.tfw/README.md` NS1–NS3,
Methodology Values and Success Criteria. The downstream TS and derivation-only Phase HL were not used
as purpose authority.

**Outcome: Aligned (✅).** The clause served is HL §1's requirement that canonical artifacts be
“smaller, mutually consistent and behaviorally complete,” under NS1's requirement that another
authorized participant can inspect material grounds, current result and authority and continue
without rebuilding the original conversation. The concrete harm is a shorter coordination corpus
that appears proven but leaves a future Reviewer unable to reconstruct which Candidate conditions
made owner-direct, invalid-continuation or transcript-inspection scenarios pass or refuse. Phase B
targets exactly that harm; the missing harness is incomplete proof inside the intended work, not a
different purpose.

- **Excess and adjacency:** no. Candidate stays within the approved 47 VALUE paths; no receiver
  mutation, new runtime, registry, workflow, command, permanent test, release or publication exists.
- **Deferral confession:** no. D75's later `/tfw-docs` effect is an explicitly sequenced closing
  effect. The replay repair belongs to the current evidence contract rather than a different home.
- **Materiality:** yes for acceptance quality. AC-3 exists to prevent semantic subtraction from being
  accepted on assertion; output names without executable predicates cannot demonstrate the material
  negative cases. This is not a wording objection.
- **Reference consistency:** no contract defect. The North Star's Selected Trace and Structural
  Enforcement values are compatible with the frozen HL's compression goal: preserve a compact,
  executable evidence trace instead of adding product runtime or transcript capture.

No `not fit for purpose` or contract-defect owner route is found.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---:|---|---|---|
| 1 | D75 — trajectory `310,485→112,536 (−63.8%)` | Terminal RCFR evidence and fresh replay resolve `310,485→112,206 (−63.9%)`; RF supplies the exact later `/tfw-docs` replacement | **Yes in current knowledge, correctly disclosed by RF.** It remains pending until an APPROVE verdict permits the authorized Docs effect and bounded follow-up. |
| 2 | D73–D74 — selective context, canonical ownership and source-derived semantics | Phase B consolidates shared rules and retains role-local actions | No implementation contradiction. The missing rung-2 harness prevents acceptance of the proof record, not the underlying knowledge items. |
| 3 | D85 — receiver-safe update evidence | Receiver replay is epoch-bound and read-only | No. Helpdesk's later clean HEAD is a later epoch and is not merged into the recorded observation. |
| 4 | D86 — finite Coordinator closure | AC-9 leaves review, Docs/follow-up and terminal close downstream | No. The deferral is explicit; this REVISE keeps the phase open. |

RF §7 contains no Fact Candidate to challenge.

## Checkpoint

**Self-check:**

- [x] Every checklist item has evidence.
- [x] No `⚪ N/A` row is used.
- [x] Row 2(a) is answered against the contract baseline and North Star, with a quoted clause and named harm.
- [x] Rows 7 and 8 are answered separately with different reasoning.
- [x] `verify.md` discrepancy 1 is cited in the DoD assessment.
- [x] Row 3 prepares the single §5 item for Coordinator ruling with an existing target and named consequence.
- [x] RF §§7–9 were checked for presence and quality.
- [x] `KNOWLEDGE.md` was cross-referenced and contradictions documented.
- [x] RF Fact Candidates were reviewed (explicitly none).

Stage complete: **YES**
