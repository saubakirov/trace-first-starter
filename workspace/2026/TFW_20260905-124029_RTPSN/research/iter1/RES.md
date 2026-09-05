# RES — TFW_20260905-124029_RTPSN: Command-entry reliability and causal diagnosis (Iteration 1)

> **Date**: 2026-09-05
> **Author**: Codex (Researcher) · on behalf of `saubakirov`
> **Status**: 🔬 RES — Iteration 1 complete; more research required
> **Parent HL**: [HL-TFW_20260905-124029_RTPSN](../../HL-TFW_20260905-124029_RTPSN.md)
> **Mode**: Pipeline · `focused` · one iteration explicitly mandated

---

## Research Context

Iteration 1 tested H3–H4: whether the two known `/tfw-plan` deviations constitute a
measurable regression caused by RCFR entry-cue changes, and whether byte-identical full
copies, current thin proxies, strengthened minimal proxies, or direct single-authority
entry have a demonstrated cross-role reliability advantage after runtime context, drift,
maintenance, portability, and observability are counted. Evidence combines the source
session trace, Git history, all 11 command routes, all four manifest adapters, receiver
hashes and live-host state, targeted integration tests, exact word counts, transparent token
estimates, and official OpenAI documentation. No new behavioural session was created.

## Briefing

[`1_briefing.md`](1_briefing.md) bounded this run to Iteration 1 and three questions: causal
classification, evidence per entry architecture, and declared/installed/live topology.
Evidence is recorded in [`2_gather.md`](2_gather.md), the configuration space in
[`3_extract.md`](3_extract.md), and counter-evidence in [`4_challenge.md`](4_challenge.md).

Primary external sources:

- [OpenAI — Build skills](https://developers.openai.com/codex/skills)
- [OpenAI — Model guidance](https://developers.openai.com/api/docs/guides/latest-model)
- [OpenAI — model migration/eval guidance](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.2)
- [OpenAI — GPT-5.5 guidance](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.5)

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Diagnose CRATM as an algorithm/path-coverage gap, not an entry failure | The skill and complete `plan.md` reads completed; the existing-task route skipped the create-only rename branch (G1, C1) |
| D2 | Diagnose RTPSN as post-load noncompliance | The current skill and complete workflow read completed before the assistant elevated an unresearched title candidate, then acknowledged the violation (G1, C1) |
| D3 | Refute H3 as stated | The 154→141-word RCFR diff preserved the Role Lock, complete-read requirement, gates, and stop; `n=2` incidents have different downstream causes and no controlled pre/post measurement exists (G2, C1) |
| D4 | Treat receiver/authority skew as a fifth infrastructure failure class | The manifest-authoritative plural `.agents/workflows` is absent while singular `.agent/workflows` compatibility copies exist and match canonical files; this is evidenced risk but not the cause of either incident (G4, C2) |
| D5 | Keep current thin proxy + canonical workflow as the operational baseline | It is live, schema-valid, and separates skill selection from canonical load in traces. Its `/tfw-plan` overhead is 141 words (~188 estimated tokens), with no evidence that another architecture buys behavioural adherence (G3, C4) |
| D6 | Do not deploy byte-identical full copies as a universal cure | They do not repair the observed mechanisms, multiply algorithm-bearing receivers, and the current canonical `plan.md` lacks the `name` metadata required for an exact Codex `SKILL.md` (G6, E4–E5, C3–C4) |
| D7 | Keep the 151-word strengthened proxy and schema-valid direct entry as controlled experiment arms only | The former adds 10 words (~14 estimated tokens) and a sharper pre-action boundary; the latter removes proxy overhead and textual drift, but neither has comparative cross-role evidence (G7, E3–E6, C4–C6) |
| D8 | Require an evidence ladder for future reliability claims | Source presence, receiver parity, invocation, canonical load, later conformance, and controlled comparative effect are distinct levels; current tests reach structural parity and incidents reach load plus failed conformance, not comparative effect (E1, C4) |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Did RCFR introduce a measurable command-entry regression? | ✅ closed for current evidence | No. H3 is refuted as stated: neither known incident is an observed invocation/non-load failure, and there is no controlled pre/post effect estimate. A smaller cue effect in other runs remains possible but unmeasured (D1–D3) |
| Q2 | Which entry architecture has materially better cross-role adherence? | 🟡 open | None is demonstrated. Current thin proxy is the least-regret operational baseline; strengthened and direct variants require controlled repeated trials (D5–D8) |
| Q3 | What do full copies, proxies, and direct entry cost at `/tfw-plan` runtime? | ✅ closed for checked-out text | Full/direct: 2,150 words (~2,867 tokens); current: 2,291 (~3,055); strengthened specimen: 2,301 (~3,068); pre-RCFR: 2,304 (~3,072). Estimates use `ceil(words × 4/3)` (G3, E3) |
| Q4 | Are all four adapters installed and live? | ✅ closed for this checkout/host | No. Codex is declared, installed, exact, and live; Claude receivers are present/exact but not live-observed; Cursor and declared plural Antigravity receivers are absent; singular Antigravity compatibility copies are present/exact but undeclared and not live (G4) |
| Q5 | Why do plural manifest authority and singular tracked Antigravity compatibility files coexist? | 🟡 open | Tests enforce plural authority and reproduce it in a clean receiver, but repository history/policy explaining the retained singular surface was not established in this iteration (G4, C2) |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | A short workflow-function vocabulary is recognized faster and more accurately than formal role or skill names without implying false authority | needs-research | ⚪ **deferred to Iteration 2** | Naming ergonomics were explicitly out of scope |
| H2 | A compact positional title grammar with deterministic collision/fallback rules outperforms full IDs or longer forms | needs-research | ⚪ **deferred to Iteration 2** | Naming, rendering, search, collision, and host rename capability were explicitly out of scope |
| H3 | Recent deviations reflect a measurable command-entry regression introduced by changed entry cues; alternatives include non-invocation, non-load, uncovered path, post-load noncompliance, or another cause | needs-research | 🔴 **refuted as stated** | Both incidents read proxy and canonical workflow. CRATM is uncovered-path; RTPSN is post-load noncompliance. RCFR removed 13 proxy words but retained the relevant entry obligations. No comparative rate exists (G1–G2, C1) |
| H4 | One candidate entry architecture yields materially better cross-role adherence and total value after full cost comparison | needs-research | 🟡 **inconclusive on adherence; baseline recommendation available** | Cost/topology are measured, but behavioural evidence covers two Coordinator failures and one non-independent Researcher run only. Current proxy has the best demonstrated operational fit, not demonstrated behavioural superiority (G3–G7, E1–E6, C3–C6) |

## HL Update Recommendations

> The researcher classifies. The researcher never applies.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 | Replace the provisional “proxy thinning caused the deviations” interpretation with the traced split: CRATM uncovered existing-task path; RTPSN post-load noncompliance; both completed the current skill and canonical workflow reads | G1, C1 |
| R2 | §2 | Record the 11-command/four-adapter state separately as declared, present/exact, clean-install reproducible, and live; explicitly distinguish plural `.agents/workflows` authority from singular `.agent/workflows` compatibility files | G3–G5, C2 |
| R3 | §7.2 | Preserve current thin Codex proxies as the operational baseline; keep strengthened minimal proxy and schema-valid direct entry as later experimental alternatives, not selected implementation | D5–D7, C4–C7 |
| R4 | §8 | Add the measured context baseline and formula: current `/tfw-plan` 2,291 words/~3,055 estimated tokens including both reads; full/direct 2,150/~2,867; strengthened specimen 2,301/~3,068; estimates are not runtime billing telemetry | G3, E3 |
| R5 | §9 | Split reliability risk into non-invocation, proxy non-load, canonical non-load, uncovered algorithm path, post-load noncompliance, and receiver/authority skew; require evidence at the exact failed boundary | G1, E1–E2, C2 |
| R6 | §9 | Add full-copy drift/schema risk and direct-entry portability risk; retain exact parity and clean-receiver tests but state that they do not test model adherence | G4–G6, E4–E6, C4 |
| R7 | §10 H3 | Mark refuted as stated; retain cue effects only as an unmeasured alternative for future controlled study, not as the diagnosis of the two incidents | D3, C1 |
| R8 | §10 H4 | Mark material cross-role adherence unresolved; record current thin proxy as provisional least-regret baseline and the concrete future eval threshold from C6 before any architecture migration | D5–D8, C4–C6 |
| R9 | §11 | Add the six-level evidence ladder and the implication that entry reliability, workflow path coverage, and later instruction following require separate metrics and repair surfaces | E1–E2, C3 |

### Amendment Proposals — frozen sections, owner verdict required

**No amendment proposals.** The findings refine evidence, risks, architecture alternatives,
and hypothesis status without invalidating a frozen declarative claim at HL granularity.

## Fact Candidates

> fact-candidates: processed 2026-09-05

**No fact candidates.** The user supplied scope, terminal conditions, and known evidence
targets; every substantive project claim in this iteration was independently discoverable
from repository files, Git history, tests, or the source session trace.

## Strategic Insights (Research)

**No strategic insights.** No new human domain briefing occurred; the owner's research
constraints and cost concerns were already recorded in the HL and Briefing.

## Findings Map

```text
literal command / natural-language match
                 |
                 v
       [R2 command/skill invoked?] -------- no ------> non-invocation
                 |
                yes
                 v
          [proxy loaded?] ----------------- no ------> proxy non-load
                 |
                yes
                 v
     [R3 canonical workflow loaded?] ------ no ------> canonical non-load
                 |
                yes
                 v
      [applicable branch specified?] ------ no ------> uncovered path (CRATM)
                 |
                yes
                 v
       [R4 later action conforms?] -------- no ------> post-load noncompliance (RTPSN)
                 |
                yes
                 v
              expected result

parallel distribution chain:
manifest authority -> generated receiver -> present/exact -> live host
                              |
                              +---- mismatch ----> receiver/authority skew

Only repeated controlled comparisons reach R5 and can rank behavioural adherence.
```

## Iteration Status

- **Iteration:** 1 of 2 (min) / 5 (max), per `research/iterations.yaml`
- **Hypotheses tested:** H3 (refuted as stated); H4 (cross-role adherence inconclusive; current thin proxy recommended as operational baseline)
- **Hypotheses deferred:** H1 and H2 (planned naming-ergonomics Iteration 2; explicitly outside this run)
- **Gaps discovered:** no controlled architecture trial; no independent Executor/Reviewer or other-command behaviour sample; no live Claude/Cursor/Antigravity observation; declared plural Antigravity receiver absent from checkout; current word-based token estimate lacks runtime telemetry; H4's material adherence effect remains unknown
- **Superseded decisions:** None

`research/iterations.yaml` intentionally remains unchanged with Iteration 1 marked pending;
the Coordinator owns status update and creation of Iteration 2.

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|----------------|-----------------|
| 1 | H1–H2 naming ergonomics | The task's minimum two-iteration gate and frozen plan require a separate naming study | Coordinator adds Iteration 2, then a Researcher tests work cue, task cue, phase grammar, collisions, rendering, search, and host rename capability without assuming an architecture migration |
| 2 | Controlled entry-architecture adherence eval | H4 cannot support “materially better” without R5 evidence | Later approved study: current vs 151-word strengthened vs schema-valid direct; pinned model/effort, representative role/path fixtures, repeated trials, per-boundary graders, token/latency telemetry, and the C6 materiality thresholds |
| 3 | Antigravity plural/singular authority history and live installation | Receiver skew can masquerade as an available command | Trace why singular compatibility files remain, verify intended migration policy, and test the manifest-declared plural receiver on an actual host before making liveness claims |

### Recommendation

- [ ] SUFFICIENT
- [x] **MORE NEEDED** — Iteration 1 is sufficient for its H3–H4 scope and unblocks the Coordinator's iteration decision, but overall research still requires the separately planned H1–H2 naming iteration; H4 behavioural superiority remains explicitly unproven
- [ ] BLOCKED

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 1 found no evidence that RCFR's 154→141-word proxy change caused the two known
deviations: both sessions loaded the proxy and all of `plan.md`, after which CRATM encountered
an uncovered workflow path and RTPSN failed to follow a loaded gate. Full copies, stronger
proxies, and direct entry therefore do not pass the incident-substitution test as cures.
The current thin proxy remains the least-regret baseline at 141 words/~188 estimated tokens
of `/tfw-plan` overhead because it is live, schema-valid, and diagnostically observable;
this is not a claim of superior cross-role adherence. The analysis also exposed plural vs
singular Antigravity receiver skew and defined a six-level evidence ladder plus a falsifiable
future eval. **Self-critique:** behavioural evidence is `n=2` Coordinator failures plus one
non-independent Researcher run, other hosts were not live-tested, and token counts are word
proxies rather than telemetry. The RES consequently recommends no entry-architecture
migration and preserves H4's behavioural claim as unresolved.

---

*RES — TFW_20260905-124029_RTPSN: Command-entry reliability and causal diagnosis (Iteration 1) | 2026-09-05*
