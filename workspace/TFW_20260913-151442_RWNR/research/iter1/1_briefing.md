# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW_20260913-151442_RWNR](../../HL-TFW_20260913-151442_RWNR.md)
> Goal: Determine whether `/tfw-resume` is a necessary public command and retire it only after every continuity guarantee has a proven surviving route.

## Research Plan

### Gather

- Inventory the canonical `/tfw-resume` algorithm as externally observable responsibilities, callers, receivers, accepted states, state transitions, safety stops, and failure exits.
- Trace each responsibility through `/tfw-plan`, lifecycle-specific workflows, conventions, status/journal rules, adapters, manifests, generated or managed receivers, installation/update logic, documentation, and scenario tests.
- Classify repository matches as live authority, thin adapter/receiver, test fixture, current documentation, or historical truth; verify the stated 2,685-word baseline from source.

### Extract

- Decompose every behavior by user job, canonical authority, responsible Role Lock, accepted input/state, output/route, mutation permission, and positive/negative evidence.
- Compare survivor configurations for known-task continuation, multi-phase choice, historical-only inspection, closing, and record recovery without creating a replacement command.
- Isolate responsibility gaps, duplicated semantics, generated-copy risks, clean-install/update implications, and the minimum retained instruction surface.

### Challenge

- Attempt to falsify H1–H4 with adversarial multi-phase, historical-only, closing/recovery, wrong-role, stale-receiver, clean-install, update, and historical-rewrite scenarios.
- Test whether the strongest retirement design preserves Role Locks, explicit routing, immutable history, and research-local continuation while staying below the 2,685-word retained-surface baseline.
- Record counterevidence, unresolved gaps, and the evidence required from iteration 2 before the owner can receive a defensible G1 recommendation.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | The returning-user job served by `/tfw-resume` is already covered by `/tfw-plan` plus lifecycle-specific commands, so a second public entry has no independent user value. | needs-research |
| H2 | Every unique resume protection can be assigned to an existing canonical route without widening the wrong Role Lock or creating a replacement public command. | needs-research |
| H3 | Canonical sources, skills, adapters, manifests, docs, tests, clean installs, and update receivers can remove resume consistently while historical traces remain untouched. | needs-research |
| H4 | The surviving design reduces the combined 2,685-word workflow surface and does not solve command count by making plan a larger monolith. | needs-research |

## Scope Intent

- **In scope:** Focused iteration 1 evidence for all observable resume responsibilities and live surfaces; canonical ownership and Role Lock mapping; lifecycle routing and safety stops; generated/managed adapter and manifest propagation; clean-install/update behavior; relevant command-entry and scenario tests; adversarial H1–H4 checks; historical-truth boundaries; exact word-count baseline and survivor accounting candidates.
- **Out of scope:** HL, TS, status, journal, or `iterations.yaml` mutation; iteration 2; implementation or command removal; TKL or project-knowledge mutation; review, release planning, tags, pushes, publishing, or any G1/G2 decision.

## Guiding Questions

1. Which `/tfw-resume` behaviors are genuine user-visible continuation contracts, and which are incidental command-local mechanics?
2. For each genuine contract, which existing canonical role and route can own it without widened authority, silent mutation, or a replacement public command?
3. Which live distribution, update, and scenario-test surfaces must agree before retirement can be considered safe while historical traces remain untouched?

## User Direction

- The owner-approved HL fixes the retirement question and requires focused research of at least two iterations before G1.
- The LEAD dispatched this unit for iteration 1 only and confirmed the dispatch at commit `a2363fd`; the Coordinator research-state producer is `859c4d0`, landed as `29a378d`, and the frozen HL baseline is `d375bf6`.
- Run focused mode, use primary repository evidence, test H1–H4 adversarially, preserve the 2,685-word baseline, commit only iteration-1 stage files and `RES.md`, and return gaps, open threads, recommendation, and G1 evidence directly to the LEAD.

## Agent Team Authority and Lineage

- **Selected LEAD layer:** principal `robert`; root unit `01a09a32-367e-7ea1-a405-9501d17ba270` (`LEAD · RWNR`); mandate authority is frozen HL §4.1 plus `journal/20260913-164128__dispatch__5774.md`; G1 and G2 remain owner-reserved.
- **Researcher layer:** principal attribution `robert`; actual unit `01a09a9e-6935-7f53-bba3-50b5b08b17da` (`RESEARCH · RWNR`); parent and direct return are the LEAD unit; bounded role/scope and autonomous point are the HL working-unit row plus `journal/20260913-165716__dispatch__ab3b.md`; governing lifecycle is `RES`, iteration 1 only.
- **Proposal origin:** `{robert, 01a09a32-367e-7ea1-a405-9501d17ba270}`. No relay, child amendment authority, TS authority, implementation authority, or release authority is claimed.

---
Stage complete: YES
