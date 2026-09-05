# RES — TFW_20260905-124029_RTPSN: Session naming ergonomics (Iteration 2)

> **Date**: 2026-09-05
> **Author**: Codex (Researcher) · on behalf of `saubakirov`
> **Status**: 🔬 RES — Iteration 2 complete; overall research sufficient for planning
> **Parent HL**: [HL-TFW_20260905-124029_RTPSN](../../HL-TFW_20260905-124029_RTPSN.md)
> **Mode**: Pipeline · `focused` · one iteration explicitly mandated

---

## Research Context

Iteration 2 tested H1–H2: whether task-bound TFW sessions should use short
workflow-function cues and whether a compact positional title can remain
unambiguous, searchable, traceable and portable. The study combined all 11
canonical workflows, the available task-ID corpus, a 30-title current-app
sidebar snapshot, exact character counts, current desktop capabilities,
official Codex rename documentation, W3C label guidance and Unicode standards.
It preserved Iteration 1's current thin-proxy baseline and did not create,
fork, rename or behaviorally exercise another session.

## Briefing

[`1_briefing.md`](1_briefing.md) bounded the run to H1–H2 and required one exact
grammar plus deterministic resolution and fail-soft rules. Raw evidence is in
[`2_gather.md`](2_gather.md), the configuration model in
[`3_extract.md`](3_extract.md), and adversarial tests in
[`4_challenge.md`](4_challenge.md).

Primary external sources:

- [OpenAI — ChatGPT & Codex changelog](https://learn.chatgpt.com/docs/changelog)
- [W3C — Clear Visible Labels](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p06-clear-labels/)
- [W3C — Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html)
- [W3C — Consistent Identification](https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification)
- [W3C — Headings and Labels](https://www.w3.org/WAI/WCAG21/Understanding/headings-and-labels)
- [Unicode — Normalization Forms](https://www.unicode.org/reports/tr15/)
- [Unicode — Emoji](https://www.unicode.org/reports/tr51/tr51-7.html)

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Select the base grammar `{WORK} · {TASK}[ · {PHASE}]` | It directly instantiates frozen HL §3, uses one space around U+00B7, keeps a stable leftmost function cue and reduces the real 49-character full form to 16 characters for `PLAN · CRATM · A` (G3, C2–C4) |
| D2 | Use uppercase workflow-function vocabulary: `PLAN`, `RESEARCH`, `EXEC`, `REVIEW`, `RESUME`, `DOCS`, `INIT`; use `LEAD` only for an already authoritative lead binding | Functions distinguish the actual workflow better than the shared formal roles; exact skill names add syntax; `LEAD` labels but cannot create hierarchy (E3–E4, C1) |
| D3 | Resolve `{TASK}` from canonical state: unique approved modern abbreviation, else full canonical ID; preserve legacy `TFW-##` | The current 10-ID corpus has 10 unique abbreviations and full IDs average 24.8 characters; full-ID fallback deterministically resolves future abbreviation collisions (G1, E2, C6) |
| D4 | Render `{PHASE}` as the bare canonical phase ID and omit the entire segment when phase is absent or ambiguous | The fixed third position makes `A` or `A3-Q-R` interpretable without `Phase`/`Ph.`; omission is truthful, while a guessed phase is not. Research iteration is not a phase unless task state says so (C3) |
| D5 | Rename at the first checkpoint where every included slot is authoritative and before substantive workflow work | This yields explicit placements for new/existing plan, research, handoff, review, resume, single-task docs and full init; early handoff/review rename currently trusts request text before state (G5, E2, C5) |
| D6 | Do not apply task-oriented rename to project-wide workflows or multi-task modes | `/tfw-knowledge`, `/tfw-release`, `/tfw-update`, `/tfw-config`, docs batch and init attach/repair do not resolve one task; inventing one would create false navigation metadata (G5, C5) |
| D7 | Separate task-abbreviation collision from exact rendered-title collision | Full task ID solves only the first. Exact collision first uses an existing authoritative phase/`LEAD`; an opaque host-key suffix is proposed separately because it extends frozen grammar, and absent approval/capability the collision is reported once without invented ordinal (E5, C6) |
| D8 | Keep middle dot canonical; propose ASCII pipe only as verified host transport fallback | U+00B7 remained unchanged under NFC/NFD/NFKC/NFKD and is punctuation, not emoji. Cross-host rendering/search is unmeasured, so a host that fails readback may need ` | `; hyphen and emoji have stronger ambiguity/presentation costs (G6, C4) |
| D9 | Mark H1 and H2 partially supported, not proven as comparative human-performance claims | Structure, uniqueness, length and workflow coverage support a concrete selection; no controlled timing/error, pixel truncation or host-search experiment proves “faster”, “more accurately” or universally “better” (C1–C2, C7) |
| D10 | Recommend overall research as sufficient for `/tfw-plan` | Two required iterations are complete; naming and entry architecture now have implementable defaults and explicit acceptance gaps. Remaining new/resumed, readback and cross-host checks are implementation/review evidence, not a reason to invent a third discovery iteration (D1–D9; Iteration 1 D5–D8) |

### Exact grammar and vocabulary

```text
BASE := WORK " · " TASK [ " · " PHASE ]

WORK := PLAN | RESEARCH | EXEC | REVIEW | RESUME | DOCS | INIT | LEAD
TASK := unique-approved-abbreviation | full-canonical-task-id | legacy-TFW-##
PHASE := bare-canonical-phase-id
```

Rules:

- `WORK`, abbreviation and canonical phase spelling preserve their authoritative
  values except that the fixed work vocabulary is uppercase.
- `LEAD` is allowed only when CRATM or governing delegation/state already binds
  that session as lead/main coordination; title remains navigation metadata.
- `PHASE` is optional by evidence, not by preference. No `Phase`, `Ph.`, `I2`,
  placeholder or guessed token is inserted.
- Examples: `PLAN · CRATM · A`, `RESEARCH · RTPSN`,
  `EXEC · CRATM · A`, `REVIEW · TFW-37 · A`, `RESUME · CRATM`,
  `LEAD · CRATM`.

### Workflow placement matrix

| Workflow | Title shape | Exact placement |
|----------|-------------|-----------------|
| `/tfw-plan`, new task | `PLAN · TASK[ · PHASE]` | immediately after approved canonical task ID is created; before HL/research/planning work |
| `/tfw-plan`, existing task | `PLAN · TASK[ · PHASE]` | after Read Contract resolves task/phase; before knowledge/reasoning action |
| `/tfw-research` | `RESEARCH · TASK[ · PHASE]` | after task and iteration context are resolved; before Briefing/stage work; iteration does not fill phase |
| `/tfw-handoff` | `EXEC · TASK[ · PHASE]` | after Read Contract Item 1 resolves task/phase; before ONB |
| `/tfw-review` | `REVIEW · TASK[ · PHASE]` | after Read Contract Item 1 resolves task/phase; before Map |
| `/tfw-resume` | `RESUME · TASK[ · PHASE]` | after one task is selected; include phase only when state makes it unique; otherwise omit |
| `/tfw-docs` | `DOCS · TASK[ · PHASE]` | after Select/Triage resolves one task in auto/manual mode; skip in batch |
| `/tfw-init` | `INIT · TASK` | full-init only, immediately after init-task ID creation; skip attach/repair |
| `/tfw-knowledge`, `/tfw-release`, `/tfw-update`, `/tfw-config` | none | project-wide: no task-oriented rename rule |

### Fallback order

1. If modern abbreviation is not unique across accessible task roots, render the
   full canonical ID for the conflicting task.
2. If phase is absent or ambiguous, omit the phase segment.
3. If hierarchy is not explicitly authoritative, never render `LEAD`.
4. If BASE collides, first add only an already authoritative semantic
   discriminator. The ` · @<short-stable-key>` transport suffix remains A1 and
   cannot be used before owner approval.
5. If U+00B7 is not preserved by rename/readback, ` | ` remains A2 and cannot
   replace the frozen separator before owner approval.
6. If rename/readback/stable-key capability is absent, report that limitation or
   unresolved collision once, then continue the substantive workflow. Never
   invent an ordinal or claim success without readback evidence.

### Rejected alternatives

| Alternative | Why rejected |
|-------------|--------------|
| Formal role: `Coordinator`, `Executor`, `Reviewer` | Conflates distinct workflows; four identical `Coordinator | INF-12` titles are visible in the current sample |
| Exact skill: `tfw-plan` | Longer than `PLAN`, leaks command spelling, and adds no workflow distinction |
| Task-first: `CRATM · PLAN · A` | Same length but moves the cue that resolves current role/function ambiguity away from the stable prefix |
| Marked phase: `Phase A` / `Ph.A` | Six-character cost or a second abbreviation vocabulary; fixed third slot makes the bare canonical ID sufficient |
| ASCII hyphen | Visually collides with hyphens inside `TFW-37` and complex phase/task IDs |
| Emoji prefix | Presentation varies by environment, can consume extra UTF-16 units, and is not a self-sufficient human-language label |
| Invented `#2` collision ordinal | Has no canonical source and can drift after archive/reorder |
| Rename before Read Contract | Requires trusting request wording before authoritative task/phase state is loaded |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | What exact title grammar should Phase B implement? | ✅ closed | D1–D4: `{WORK} · {TASK}[ · {PHASE}]`, functional work vocabulary, unique approved abbreviation/full-ID fallback and bare authoritative phase |
| Q2 | Where should each workflow rename? | ✅ closed | D5–D6 and the placement matrix cover all 11 canonical workflows and conditional modes |
| Q3 | Is H1's faster/more-accurate human recognition demonstrated? | 🟡 open acceptance evidence | No controlled user timing/error study was performed; the selected vocabulary is supported structurally, not by a measured human effect |
| Q4 | Is middle-dot rendering/search proven on every host? | 🟡 open per-host evidence | No. Normalization is stable and current desktop rename capability exists, but cross-host indexing, pixel truncation and readback require adapter-specific checks |
| Q5 | May an exact semantic collision receive ` · @<short-stable-key>`? | 🟠 owner verdict required | A1 proposes the exceptional navigation-only suffix because three semantic slots cannot distinguish otherwise identical sessions |
| Q6 | May an affected host substitute ASCII ` | `? | 🟠 owner verdict required | A2 proposes the transport-only fallback after failed middle-dot readback; canonical output otherwise remains U+00B7 |
| Q7 | Is there visible evidence for both new and resumed titles in the chosen grammar? | 🟡 implementation/review evidence | Not in this iteration: the mandate forbade creating/forking another session. Phase B acceptance must exercise and read back one of each on a supported host |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | A short workflow-function vocabulary such as `PLAN`, `RESEARCH`, `EXEC`, `REVIEW`, and a distinct lead cue is recognized faster and more accurately than formal role names or exact skill names without implying false authority | needs-research | 🟡 **partially supported; vocabulary selected** | Function tokens uniquely map task-bound workflows, reduce length, and avoid role conflation; `LEAD` is constrained to existing authority. Human recognition speed/error was not measured (G2–G3, E3–E4, C1–C2) |
| H2 | A compact positional grammar can use the approved task abbreviation and a short or bare phase cue while deterministic collision and fallback rules preserve recognition, searchability, rendering, and traceability better than full IDs or longer forms | needs-research | 🟡 **partially supported; grammar selected conditionally** | The selected 16-character example is 67.3% shorter than the 49-character full form; current abbreviations are 10/10 unique; bare phase, full-ID collision fallback and all-workflow placement are deterministic. Cross-host search/rendering and human recognition remain acceptance evidence (G1–G7, E1–E6, C2–C7) |

## HL Update Recommendations

> The researcher classifies. The researcher never applies.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 | Record the 30-title sidebar observation, 13–59 length range, mean 29.6, mixed title styles and four identical `Coordinator | INF-12`; distinguish observation from unmeasured truncation/search behaviour | G2 |
| R2 | §7.2 | Select `{WORK} · {TASK}[ · {PHASE}]`; define work vocabulary, source-of-truth rules, bare/omitted phase, `LEAD` authority constraint, all-workflow classification and placement matrix | D1–D6, C1–C5 |
| R3 | §8 | Add corpus/length baseline: 10/10 unique modern abbreviations, 3–10 abbreviation length, 23–30 full-ID length (mean 24.8), 53 legacy tasks, and 49→16 characters (67.3%) for the representative full-to-compact comparison | G1–G3 |
| R4 | §9 | Separate abbreviation collision, exact semantic collision and host capability failure; require no-guessing, readback-aware, report-once behaviour and implementation evidence for new/resumed tasks | E1–E2, E5, C6–C7 |
| R5 | §10 H1 | Mark partially supported: select functional vocabulary but state that comparative human speed/accuracy remains unmeasured | D2, D9, C1–C2 |
| R6 | §10 H2 | Mark partially supported: select compact positional grammar and deterministic base fallbacks, while retaining cross-host rendering/search and human recognition as acceptance gaps | D1–D4, D7–D9 |
| R7 | §11 | Record the semantic-title/host-transport separation and the rule that title metadata neither proves command entry nor grants Role Lock/hierarchy authority | E1, E4, Iteration 1 D8 |

### Amendment Proposals — frozen sections, owner verdict required

| # | § | Type | Proposed change | Evidence | Cost | Alternatives considered |
|---|---|------|-----------------|----------|------|------------------------|
| A1 | §3 | `EXTEND` | Permit exceptional collision render `{BASE} · @<short-stable-key>` only after an exact BASE collision remains following authoritative phase/`LEAD` resolution, only when host exposes a stable key; suffix is navigation-only and grants no authority | Current sidebar has four identical formal-role/task titles; full task ID cannot distinguish sessions of the same work/task/phase (G2, E5, C6) | Adds a fourth visible transport segment, opaque text and host dependency; needs deterministic shortest-unique-prefix/readback tests | First use existing phase/`LEAD`; full ID solves only abbreviation collisions; invented ordinal drifts; report-only is the mandatory fallback when no key or no approval |
| A2 | §3 | `EXTEND` | Permit transport separator ` | ` only when rename/readback on a specific host fails to preserve canonical ` · `; semantic slots and spacing stay unchanged | U+00B7 normalization is stable, but other-host rendering/search is unobserved; current corpus proves pipe is accepted locally (G2, C4) | Creates two visible render forms and may split literal search habits; requires per-host evidence and report-once logging | Keep middle dot and report failure; hyphen conflicts with ID punctuation; emoji presentation is variable |

## Fact Candidates

> fact-candidates: processed 2026-09-05

**No fact candidates.** User messages supplied scope, prohibitions and the
coordinator mandate; all substantive project claims were discoverable from the
repository, app state or cited external sources.

## Strategic Insights (Research)

**No strategic insights.** No new human domain briefing occurred during this
iteration; the strategic constraints were already captured in the HL and
coordinator mandate.

## Findings Map

```text
selected canonical workflow
          |
          v
 task-bound in this mode? ---- no ----> no task-oriented rename
          |
         yes
          v
 resolve exactly one task from state
          |
          +-- modern abbreviation unique? -- no --> full canonical ID
          |                 |
          |                yes
          |                 v
          |          approved abbreviation
          v
 authoritative phase? ---- no ----> omit third segment
          |
         yes
          v
 render bare phase ID
          |
          v
 BASE = WORK · TASK [· PHASE]
          |
          +-- exact collision? -- yes --> existing semantic discriminator
          |                                  |
          |                         still collision / none
          |                                  v
          |                    A1 stable-key suffix if approved,
          |                    else report once without guessing
          v
 rename supported? ---------- no ----> report once; continue workflow
          |
         yes
          v
 rename + readback when available
          |
          +-- middle dot not preserved --> A2 pipe fallback if approved
          v
 title is navigation metadata; workflow/Role Lock remains authority
```

## Iteration Status

- **Iteration:** 2 of 2 (min) / 5 (max), per `research/iterations.yaml`
- **Hypotheses tested:** H1 (partially supported; function vocabulary selected, human effect unmeasured); H2 (partially supported; grammar selected, cross-host/human effect unmeasured)
- **Hypotheses deferred:** None
- **Gaps discovered:** controlled human timing/error comparison absent; pixel-level truncation and literal-search indexing unavailable; no live evidence for hosts beyond current desktop and documented modern Codex CLI; no proposed-grammar new/resumed pair because new sessions were forbidden; exact collision host-key suffix and ASCII separator fallback need owner verdicts
- **Superseded decisions:** None; Iteration 2 preserves Iteration 1 D5–D8 and adds a naming layer after authoritative workflow/task resolution

`research/iterations.yaml` intentionally remains unchanged with Iteration 2
marked pending; the Coordinator owns status updates and HL recommendation handling.

### Open Threads (for next iteration)

No research iteration is recommended. The following items move to planning,
owner decision and implementation/review evidence rather than another discovery
loop:

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | A1 exact-collision suffix | Base grammar cannot distinguish two genuinely identical semantic sessions | Owner verdict in `/tfw-plan`; if accepted, specify stable-key source, shortest unique prefix and readback test |
| 2 | A2 ASCII separator fallback | Provider-neutral semantics cannot guarantee every host preserves/indexes U+00B7 | Owner verdict in `/tfw-plan`; activate only from host-specific failed readback evidence |
| 3 | New/resumed acceptance evidence | Frozen DoD B7 requires at least one visible example of each on a supported host | TS acceptance cases plus implementation/review screenshots or readback evidence |
| 4 | Human and UI performance limits | H1/H2's comparative words remain stronger than current evidence | Optional later product study: blinded titles, fixed task set, time/error rate, sidebar width/truncation and literal search; not required to select the implementation default |
| 5 | Controlled entry-architecture adherence | Iteration 1 H4 did not establish behavioural superiority | Separate future approved eval only if the owner wants to revisit the current thin-proxy baseline |

### Recommendation

- [x] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations, obtain owner verdicts for A1–A2, and write/revise TS
- [ ] MORE NEEDED
- [ ] BLOCKED

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 2 selects the exact base grammar `{WORK} · {TASK}[ · {PHASE}]` with
short functional work cues, authoritative unique abbreviation/full-ID fallback,
bare known phase and no guessed segment. It supplies exact placement for all 11
workflows, separates semantic resolution from host transport, preserves the
Iteration 1 thin-proxy baseline, and isolates two frozen-claim extensions as
owner-gated amendments. The real corpus supports compactness and current
uniqueness, while W3C, Unicode and official Codex sources support consistent
text labels, normalization stability and rename capability. **Self-critique:**
the study did not measure human timing/errors, pixel truncation, literal search,
other-host rendering, or a new/resumed pair in the selected grammar. Those limits
prevent a fully confirmed comparative H1/H2 verdict, but they do not prevent a
falsifiable TS and implementation: the remaining claims are explicit acceptance
tests rather than unresolved design choices. Overall research is therefore
sufficient to return to `/tfw-plan`.

---

*RES — TFW_20260905-124029_RTPSN: Session naming ergonomics (Iteration 2) | 2026-09-05*
