# Judge — “Is the quality sufficient?”
> **Mindset:** Judge. Verify established the facts; this stage rules on acceptance quality.
> **Verify findings:** [verify.md](verify.md)
> **Purpose references:** master HL contract baseline `74e63242a1a713c8a2c4490edda24f84bfc68153`, plus `README.md § How It Works` and `.tfw/README.md § NS1–NS3`.

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | Verify V4, V5, V7, V8 and V12 disprove AC-2 through AC-6's assurance claims: route/no-write and identity semantics admit false greens; connected-group receiver preflight is absent; EV overstates those results. Accounting, parity, history and unchanged Resume do hold, but frozen DoD 15 and 17 and the TS require the missing independent proof. |
| 2 | Purpose Check and design soundness | ❌ | **(a) Aligned:** the result serves frozen HL §1's clause that there be “one clear public entry” only when “every behavior that protected continuation has an explicit, tested survivor route”; the material harm at stake is deleting Resume in Phase B while phase choice, historical read safety, identity/authority, or recovery routing is not actually protected. There is no excess, confessed deferral, or material purpose drift: the Candidate changes only the intended Plan entry and assurance, leaves lifecycle effects with their owners, and does not retire Resume. **(b) Design soundness fails:** the assurance design uses a hard-coded oracle disconnected from its temporary repository and adapter-local writes without a whole-group preflight, contrary to HL §7 principles 1, 3 and 4 and North Star `Structural Enforcement`; passing results therefore cannot reveal precisely the semantic and partial-mutation failures they are meant to prevent. |
| 3 | Debt disposed | ⚪ N/A | RF §6 contains no observation and this review found no separate out-of-scope debt row. The four defects are acceptance findings within the approved Phase A TS, not debt to defer; therefore REVIEW §5 has no item requiring a coordinator disposition or a destination trace. |
| 4 | Style & standards | ✅ | Plan is within the 1,200-word rule, keeps the canonical workflow authoritative, uses exact lifecycle names, preserves Role Locks in its text, and both full-copy receivers are byte-identical. The defects are executable-assurance defects, not naming or prose-style defects. |
| 5 | Observations collected | ✅ | RF explicitly reports no out-of-scope observations. Independent inspection of implementation, evidence, history and the Executor task found no separate quality issue that belongs outside this phase; review findings remain in the verdict rather than being mislabeled as observations. |
| 6 | RF completeness (§7–9) | ✅ | RF §§7, 8 and 9 are present and explicitly say there are no fact candidates, strategic insights or diagrams. That is substantively appropriate: the review defects are phase-local implementation/evidence findings, not durable human-domain facts or a new strategic decision. |
| 7 | Evidence completeness — does the evidence exist? | ✅ | EV plus routing, receiver, history, accounting and raw-test artifacts all exist, parse, identify the immutable Candidate, and collectively provide a row for every AC and accounting obligation. This answers existence only; it does not validate their conclusions. |
| 8 | Evidence sufficiency — does the evidence establish the claim? | ❌ | The green targeted/full-suite signals establish that the assertions execute, while independent mutations show they do not establish AC-2/AC-4 route semantics or no-write behavior; identity rows lack authoritative carrier/lineage/dispatch inputs and before/after hashes; and a cross-adapter case disproves AC-5 whole-group refusal. Verify discrepancies 1–4 and V4–V8 give the exact counterevidence. |
| 9 | Backward compatibility | ✅ | Existing consumers retain the canonical Plan path and two exact full-copy adapters; the configured suite passes, Plan's planning/handoff routes remain present, Resume is byte-unchanged, and no live command or receiver is removed in Phase A. The finding blocks Phase B safety assurance but does not show an existing interface or anchor broken by this Candidate. |
| 10 | Safety | ✅ | The Candidate contains workflow text and tests only, performs no receiver retirement or historical rewrite, introduces no secret/credential handling, and leaves Resume intact. Partial connected-group mutation is a demonstrated defect in the proposed assurance model, captured under rows 1, 2 and 8; it is not an irreversible operation performed by this Phase A Candidate. |

Rows 7 and 8 intentionally differ: the complete evidence package exists, but material parts do not prove the claims assigned to them.

## Purpose Check Detail

The contract baseline was recovered from the approved A1 re-freeze commit `74e63242a1a713c8a2c4490edda24f84bfc68153`, not from the downstream TS or Phase HL. Its frozen §1, §3–§7 and current Project North Star are coherent: subtraction is allowed only after inspected, bounded, scenario-backed continuation survives. The Candidate is directed at that exact purpose and does not ship work assigned elsewhere. The acceptance block is therefore not `not fit for purpose` and not a contract defect; it is insufficient design assurance inside an otherwise fit-for-purpose phase result.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|----------------|----------|----------------|
| 1 | D15 — thin adapters and one canonical workflow source | Plan behavior is canonical and both receivers are exact copies. | No; independent hashes confirm it. |
| 2 | D31 — filesystem state machine and research-local continuation | Plan routes RES to `/tfw-research` without taking the effect. | No contradiction in the shipped workflow text; the test oracle's disconnect means the claim is not adequately proved. |
| 3 | D68 — task-local live state and on-demand discovery | Existing-task routing reads task/phase carriers rather than a global projection. | No contradiction in the intended workflow; Verify records that the assurance model does not consume those carriers. |

No RF fact candidate requires challenge because RF §7 contains none.

## Checkpoint

**Self-check:**
- [x] Every checklist item has specific evidence.
- [x] The sole `⚪ N/A` states why no debt row exists.
- [x] Purpose was checked against the master contract baseline and Project North Star, not the TS or Phase HL, with a quoted clause and material harm.
- [x] Evidence existence and evidence sufficiency were judged separately.
- [x] Verify findings are referenced in the DoD assessment.
- [x] REVIEW §5 will contain no deferred debt because every failure is an in-scope correction proposal.
- [x] RF §§7–9 were checked for both presence and quality.
- [x] Applicable KNOWLEDGE.md items were cross-referenced; no product contradiction was found.

Stage complete: YES
