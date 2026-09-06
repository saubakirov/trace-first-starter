# RES — TFW_20260902-222456_RTBO: Tooling boundary and diagnostic materiality

> **Date**: 2026-09-06
> **Author**: Codex (Researcher)
> **Status**: 🔬 RES — Iteration 1 complete
> **Parent HL**: [HL-TFW_20260902-222456_RTBO](../../HL-TFW_20260902-222456_RTBO.md)
> **Mode**: Pipeline

---

## Research Context

This iteration investigated whether the current index/status module belongs in Full, only in the
upstream maintainer repository, or across a split boundary. It mapped actual consumers and runtime
dependencies, separated public task navigation from citation reachability, and tested whether the
known 123-character event can become quiet without weakening material state and trace findings. The
investigation was necessary because `gen_index.py` is not merely an index generator: moving or
deleting it affects ordinary workflows, migration, documentation, and repository diagnostics.

## Briefing

See [iteration 1 briefing](1_briefing.md). The owner authorized an autonomous complete research run,
refuted H1 as a sufficient value case for shipping a collector, and required unknown answers to be
recorded rather than invented.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Treat the current `gen_index.py` location and module boundary as accidental, not architectural. | It combines six independent products and is imported by Knowledge Gate, migration, and documentation consumers; a flat delete or move breaks all three. |
| D2 | Carry the corrected C4*+C8* boundary into iteration 2 as the leading design, not yet the final placement decision. | It matches the owner's product boundary: Full owns the canonical method and tool-independent outcomes; the upstream repository owns doctor/collector/docs code. It remains conditional on a complete no-helper Knowledge Gate and migration proof. |
| D3 | Classify journal-summary brevity as advice, never validity. Preserve the one-line prompt and normally-120 guidance; remove length from failures and exit status. | The actual 123-character event has no other defect when length is relaxed, while independent event/status defects still fire. No consumer renders the summary. |
| D4 | Separate diagnostics into structural/trace integrity, project consistency, advisory authoring, and historical compatibility classes. | One binary bucket made a harmless prose overrun indistinguishable from corrupted identity. Current checks are also fragmented, so a renamed `--check tasks` would overclaim coverage. |
| D5 | Preserve task-page compilation and citation resolution independently of global task navigation. | The corpus has 1,307 task Markdown files and at least 43 non-task files with task/artifact references. MkDocs renders pages omitted from navigation; reachability does not require a top-level task library. |
| D6 | Do not claim value for a public current-status page from this iteration. | CI can generate a list without committing it, but no usage or decision evidence shows that public prominence helps. A CI-only artifact remains a reversible survivor. |
| D7 | Keep Assisted unchanged and code-free. | It currently contains no index/helper/PyYAML surface and explicitly prohibits hidden runtime dependencies; no investigated need crosses that edition boundary. |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Can Full execute the exact selected-section Knowledge Gate without a shipped Python/PyYAML dependency and without recurring false pending results? | open — iteration 2 | The current mandatory command is too complex to remove by prose assertion alone; a complete procedure and conformance corpus must be tested. |
| Q2 | How does a pre-2.0 receiver obtain exact board migration without turning the migration program into permanent active runtime? | open — iteration 2 | A versioned explicitly invoked tool is the leading shape; no-Python behavior and delivery location remain unproved. |
| Q3 | Which historical current-grammar events may safely receive today's strict semantic checks? | open — iteration 2 | Current read validation is tolerant and pre-write validation has no production caller; applying today's rules retroactively can manufacture immutable defects. |
| Q4 | Should a current-status list be a public page, a CI artifact, or absent? | open — evidence/owner choice | Build-only generation is feasible; user value is unmeasured. |
| Q5 | Are the other prose bounds in `status.md` material assertions or authoring advice after the index is retired? | open — iteration 2 | They are repairable unlike journal history, but their former display rationale weakens when the committed index leaves. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | At scale, one canonical read-only collector prevents material omissions and identity mistakes that ad-hoc agent enumeration cannot prevent cheaply. | refuted by owner | ⚪ not retested | The owner stated that a capable agent will create a fit-for-environment script; scale alone does not justify shipped runtime. |
| H2 | Full can include an optional status collector without making Python or PyYAML a practical prerequisite when all workflows have a complete no-helper path. | needs-research | 🟡 conditionally supported, not selected | The condition is technically coherent, but current plan/knowledge/init/update have no no-helper path, `yaml` imports before CLI parsing, and no value case offsets shipping cost. Gather G2; Extract E1; Challenge C1–C2. |
| H3 | CI-generated current status helps orientation, broad primary task navigation distracts, and citation-reachable traces are sufficient. | needs-research | 🟡 partly supported | CI-only generation and hidden citation targets are supported. Broad prominence has no evidence; the value of a public current list is also unmeasured. Gather G4; Extract E4; Challenge C4. |
| H4 | Material integrity checks can be separated from advisory wording so the 123 event becomes quiet without hiding structural defects. | needs-research | 🟢 central claim supported; doctor coverage incomplete | Relaxing only length clears the real event while synthetic attribution, refs, transition-shape, illegal-transition, lifecycle, authority, and identity defects remain. Current report surfaces still omit or fragment some of these. Gather G3/G5; Challenge C3. |

## HL Update Recommendations

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 | Replace the single "script responsibilities" description with the six-product responsibility graph and record that four ordinary workflows currently make the helper operationally mandatory. | Gather G1–G2 |
| R2 | §8 | Mark documentation trace compilation as independently preservable; mark the no-helper Knowledge Gate and versioned board-migration route as unresolved dependencies for iteration 2. | Extract E2/E4; Challenge C1/C4 |
| R3 | §9 | Add the risks of a prompt-only Knowledge Gate drifting from exact digest behavior, retroactive validation manufacturing immutable defects, and bare no-HL task links resolving to folders without index pages. | Challenge C1/C3/C4 |
| R4 | §10 | Set H2 to conditionally supported but not selected, H3 to partly supported, and H4 to supported for summary separation with doctor coverage still open. Route the four iteration-2 proof obligations from Iteration Status. | Challenge C5 |
| R5 | §7.2 | Add the YAML carrier-complexity, build-only page, hidden-navigation, optional-dependency, and assertion-versus-annotation sources as research evidence where the coordinator finds them material. | Gather G2/G4; Extract E3/E4; Challenge C2–C4 |

### Amendment Proposals — frozen sections, owner verdict required

No amendment proposals. The leading design and every unresolved alternative remain inside the
frozen no-runtime, no-cache, non-gating, Assisted-clean, citation-reachable boundary.

## Fact Candidates

No fact candidates. Agent-observed dependency and behavior findings belong to this RES, and the
owner's maintainer-versus-receiver distinction and H1 judgment are already recorded in HL §10–11.

## Strategic Insights (Research)

No new strategic insights. This researcher received no new human direction beyond the governing HL
and the already-recorded autonomous-run instruction.

## Findings Map

```text
CURRENT MONOLITH (.tfw/scripts/gen_index.py)
│
├─ committed index writer + freshness check ──────> retire
├─ status/journal report ─────────────────> upstream doctor candidate
├─ exact identity/state reader ──┬──> docs compiler
│                                  ├──> pre-2.0 migration
│                                  └──> Knowledge Gate
├─ project consistency check ────────────> upstream QA candidate
└─ 120-character assertion ──────────────> prompt advice only

LEADING BOUNDARY TO PROVE

Full payload                          Upstream repository / CI
┌─ canonical file/data contract          ┌─ maintainer doctor + status collector
├─ environment-chosen operations         ├─ declared Python/PyYAML environment
├─ complete Knowledge Gate outcome <----┼─ shared conformance cases
└─ no mandatory helper                  └─ docs compiler

Versioned pre-2.0 migration tool ──> explicit compatibility path, not active lifecycle

Documentation build
task pages ──> compiled, hidden from global nav ──> cited traces remain reachable
status list ──> CI-only by default pending evidence ──> no committed cache
```

## Iteration Status

- **Iteration:** 1 of 2 (min) / 5 (max)
- **Hypotheses tested:** H2 (conditionally supported, not selected), H3 (partly supported), H4 (central separation supported; doctor scope incomplete)
- **Hypotheses deferred:** H1 (already refuted by owner and intentionally not retested); final placement judgment for H2, public-list value for H3, and complete diagnostic surface for H4 await the explicit iteration-2 proofs below
- **Gaps discovered:** no-helper Knowledge Gate; versioned migration without permanent runtime; event-era diagnostic compatibility; hidden/bare-link reachability; materiality of other prose bounds; public status-list value
- **Superseded decisions:** None

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | Exact no-helper Knowledge Gate | Removing the shipped module today hard-stops plan and knowledge; a vague manual fallback would weaken D73. | Specify and exercise an environment-neutral procedure against the current digest map, malformed path, collision, fenced heading, changed section, removed task, and empty-section cases. |
| 2 | Versioned pre-2.0 migration | `migrate_board.py` imports nine names from the monolith and exact accounting protects real historical corpora. | Compare in-payload versioned tool, separately obtained migration bundle, and agent-synthesized implementation under Python/PyYAML absence; preserve explicit failure behavior. |
| 3 | Doctor contract and compatibility epochs | Current checks mix advice with integrity, omit some desired diagnostics, and cannot safely apply every new rule to immutable history. | Define audiences, classes, exit semantics, current-versus-legacy applicability, and conformance cases; include the real 123 event and synthetic structural defects. |
| 4 | Documentation reachability and status-list value | Navigation can be removed safely only if cited targets and no-HL identifiers remain reachable; a public status page has no evidence yet. | Build a temporary navigation-hidden projection, test representative links including no-HL tasks, and compare public page versus CI-only artifact without committing generated output. |
| 5 | Remaining prose bounds | Title/goal/value/outcome limits may become the next 123-style noise after the index is removed. | Trace each bound to a material consumer and compliance time; retain as assertion only with an evidenced consequence. |

### Recommendation

- [ ] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [x] **MORE NEEDED** — run mandatory iteration 2 on the five open threads above, prioritizing the no-helper Knowledge Gate and migration boundary; do not repeat the responsibility inventory
- [ ] **BLOCKED** — no blocker

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 1 established that the user's two pains are real but the apparent single script is a false
unit of change. The 120-character rule can be removed from validity cleanly and independently;
compiled trace pages can remain reachable without a top-level task library or committed portfolio;
and Assisted is already correctly isolated. The leading direction is a Full method that works with
environment-chosen tools plus an upstream-only doctor/collector/docs implementation, with one-time
migration isolated by version. The result is not yet sufficient for TS: exact Knowledge Gate
behavior, migration delivery, event-era diagnostics, and hidden-link behavior require one focused
adversarial iteration. The iteration's limitation is lack of readership analytics for the public
status page, so it recommends no public prominence by default rather than pretending that value was
measured.

Research iteration 1 complete. Continue with `/tfw-plan` to review iterations and decide next step.

---

*RES — TFW_20260902-222456_RTBO: Tooling boundary and diagnostic materiality | 2026-09-06*
