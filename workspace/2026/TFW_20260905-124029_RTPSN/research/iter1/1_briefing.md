# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW_20260905-124029_RTPSN](../../HL-TFW_20260905-124029_RTPSN.md)
> Goal: Make task-bound TFW sessions enter the intended canonical role workflow reliably before receiving a concise, evidence-selected identity.

## Research Plan

### Gather
- Census the 11 manifest command routes and all four adapter definitions, recording manifest declaration, source, tracked receiver, local installation, and live-host evidence separately.
- Reconstruct current and pre-RCFR entry texts and the two observed `/tfw-plan` incidents without treating temporal order as causality.
- Count actually read entry and canonical-workflow words and estimate tokens for full-copy, current-proxy, strengthened-proxy, and direct-entry candidates, including double reads.
- Decompose evidence into invocation, canonical load, algorithm/path coverage, post-load adherence, and any fifth cause supported by traces.

### Extract
- Build a configuration space across entry form, authority location, runtime read path, observability, and adapter distribution model.
- Cross-reference each candidate with adherence evidence, runtime context, parity/drift surface, maintenance burden, and portability.
- Separate static source/parity evidence from behavioural evidence and explicit host/runtime limits.

### Challenge
- Test the strongest candidates against both known incidents and representative Coordinator, Researcher, Executor, and Reviewer routes.
- Try to falsify the alleged RCFR regression by comparing pre/post wording and by locating unchanged, uncovered, or later-ignored instructions.
- Eliminate configurations that create a second algorithm, conceal duplicate reads, rely on an uninstalled route, or claim behaviour that cannot be observed.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H3 | Recent deviations reflect a measurable command-entry regression introduced by changed entry cues; alternatives are non-invocation, non-load, uncovered path, post-load noncompliance, or another evidenced cause. Current evidence weighs against pure non-loading in the two incidents. | needs-research |
| H4 | One of byte-identical full copies, current thin proxies, strengthened minimal proxies, or a direct single-authority entry yields materially better cross-role adherence and total value once runtime context, drift, maintenance, portability, and observability are counted. | needs-research |

## Scope Intent
- **In scope:** Iteration 1 only; H3–H4; all 11 commands; four manifest adapters; declared/installed/live topology; current and pre-RCFR entry wording; known incidents; viable entry architectures; word and estimated-token counts; adherence, drift, maintenance, portability, and observability evidence.
- **Out of scope:** Session-title grammar and ergonomics (H1–H2); Iteration 2; TS, implementation, adapter repair, HL edits, ONB, RF, REVIEW, merge, push, CRATM role/orchestration changes, or claims about unobserved hosts.

## Guiding Questions
1. Which causal class best explains each known failure, and what evidence distinguishes invocation, load, coverage, and later compliance?
2. Which entry architecture provides the best measured assurance per actually read context while preserving one canonical algorithm and one Role Lock?
3. Where do the 11-command/four-adapter declared, installed, tracked, and live surfaces disagree, and which claims remain untestable?

## User Direction
- The Coordinator delegated one Researcher session and explicitly limited this run to Iteration 1, H3–H4.
- Use the repository-local `/tfw-research` workflow in Researcher Role Lock, create every stage trace and `research/iter1/RES.md`, then stop before Iteration 2.
- Do not create another session, fork, subagent, TS, code, ONB, RF, REVIEW, merge, or push. Report verdicts, evidence, gaps, recommendation, and local commit hash.
- Default `focused` mode is accepted as the concrete mode because the question and required evidence surfaces are bounded; no blocking user question remains.

---
Stage complete: YES
