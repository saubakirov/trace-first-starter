# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW-52](../../HL-TFW-52__tfw_light_v1.md)
> Goal: Define a coherent TFW edition spine in which Light and Assisted remain useful products, teach the evolution of the method, and migrate additively toward Team and Full.

## Research Plan

### Gather
- Reconstruct early TFW history from Git and compare its smallest working concepts with the current `.tfw/` canon and the field-tested TFW-51 prototype.
- Decompose the decision into independent factors: semantic invariants, edition selection criteria, source topology, migration contract, and pedagogical sequencing.
- Read HL INNO-6/8/12/13 as required educational evidence and map their claims to H7–H8 without assuming transferability.
- Use external sources to test progressive scaffolding, authentic-task learning, product-line/source-layout patterns, and migration continuity; actively collect evidence against the proposed ladder.

### Extract
- Build a configuration space that crosses source topology, semantic core, selection model, migration strategy, and learning sequence.
- Derive a minimal invariant set and a Light → Assisted → Team → Full artifact-migration table from repository evidence rather than the current HL proposal alone.
- Compare configurations against typical non-code work in several departments and identify combinations not proposed in the HL.
- Re-check the emerging synthesis against external primary sources and seek counterexamples where staged editions create confusion, duplication, or lock-in.

### Challenge
- Attack surviving configurations with wrong-root use, live-project migration, terminology drift, edition mis-selection, independent updates, and novice/advanced mixed-audience scenarios.
- Seek counter-evidence in early TFW reversals, current anti-patterns, TFW-51 limitations, and INNO evidence that does not generalize.
- Use external primary research to challenge instructional fading, transfer, and cognitive-load assumptions; reject configurations that depend on unsupported pedagogy.
- Decide the status of H5–H8 and produce bounded recommendations for the coordinator, leaving Assisted enforcement and Team mechanics to later iterations.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H5 | A source layout under `editions/01-light/`, `02-assisted/`, then `03-team/` is clearer and safer than root `.tfw-light/` / `.tfw-assisted/` folders when each edition is copied into the runtime root. | open |
| H6 | One semantic core — goal → Working Backwards task → trace → knowledge — permits mechanical edition upgrades without loss or manual reconstruction of accumulated project state. | open |
| H7 | Edition choice by work complexity, number of roles, cost of error, and knowledge lifetime is clearer across departments than labels such as beginner/advanced. | open |
| H8 | The sequence do → notice a limit → receive a mechanism → repeat and compare traces teaches TFW evolution better than a lecture that describes all four editions in order. | open |

## Scope Intent
- **In scope:** iteration 1 product spine; early Git history; current framework; TFW-51 field prototype; HL INNO-6/8/12/13; H5–H8; edition topology; semantic invariants; department-neutral selection criteria; additive migration; pedagogical sequence; external evidence and counter-evidence at every stage.
- **Out of scope:** implementation; edits outside this iteration folder; Assisted hook/runtime contracts (H1–H4); Drive or scheduler mechanics; Team session/thread mechanics (H9); changes to HL, README, `iterations.yaml`, TS, or product files; commits.

## Guiding Questions
1. Which concepts are genuinely invariant from the earliest useful TFW through TFW-51 and the current canon, and which are later mechanisms that belong only to higher editions?
2. Which combination of source topology, edition-selection criteria, and migration mapping minimizes ambiguity while preserving independent usability and compatibility?
3. What repository, field, educational, and external evidence would falsify H5–H8 rather than merely confirm the approved HL?

## User Direction
- Run TFW-52 iteration 1 in `deep` mode and test H5–H8.
- Required local evidence: early TFW Git history, current `.tfw/`, TFW-51, and HL INNO-6/8/12/13 in `D:\projects\research\innoforce-ai-first`.
- Perform external research and seek counter-evidence at briefing, gather, extract, and challenge.
- At every gate, report `[CHECKPOINT: briefing|gather|extract|challenge]`, findings, only blocking questions (maximum three), and a recommended next action; do not ask the user directly.
- Apply working defaults for non-blocking uncertainty. Write only within this iteration folder. Do not commit.

## Briefing Evidence Check

### Required-source inventory

- **Early TFW history is available:** the repository starts at `45fd1b0` (2025-09-08) and exposes pre-v3 artifacts through the v2 transition (`d297fec`) and v3 migration (`85e4217`). Gather will sample artifacts at semantic transitions rather than treating commit subjects as evidence.
- **Current canon is available:** `.tfw/` contains the active conventions, workflows, templates, glossary, configuration, and accumulated decisions loaded for this iteration.
- **Field prototype is available:** TFW-51 contains its approved HL plus the four-file starter (`README.md`, `AGENTS.md`, `TASKS.md`, `memory/PROJECT.md`).
- **Educational HLs are available:** HL INNO-6, INNO-8, INNO-12, and INNO-13 resolve in `D:\projects\research\innoforce-ai-first\tasks\...` and will be read in Gather.

### External framing and counter-evidence

1. Git's official submodule documentation establishes a real counter-alternative to H5: separate repositories can be mounted under one superproject while retaining independent history and versioning. Therefore, `editions/` must win on TFW-specific coupling, copy/install UX, and migration evidence; it cannot be accepted merely because one repository looks simpler. Source: <https://git-scm.com/docs/gitsubmodules>.
2. Google's published monorepo case identifies a common source of truth as a benefit but explicitly presents the model as a trade-off supported by specialized tooling. This supports comparing coupled evolution in one repository, not blindly generalizing a monorepo recommendation to tiny starter editions. Source: <https://research.google/pubs/why-google-stores-billions-of-lines-of-code-in-a-single-repository/>.
3. Kapur's randomized studies found that problem solving before instruction can improve conceptual understanding and transfer when it is followed by instruction and consolidation. This is preliminary support for H8's experience-first sequence, but only as a deliberately designed two-phase cycle. Source: <https://doi.org/10.1111/cogs.12107>.
4. Kirschner, Sweller, and Clark synthesize counter-evidence that minimally guided instruction is inefficient for novices. This prevents H8 from being interpreted as "let novices discover TFW alone"; Gather must locate the guidance, bounded task, feedback, and consolidation supplied by each edition. Source: <https://doi.org/10.1207/s15326985ep4102_1>.

### Briefing decisions

- **BF-D1:** Treat H5 as a topology trade-off with three live families — same-repository edition directories, root hidden sibling frameworks, and independently versioned repositories — and require TFW-specific evidence for elimination.
- **BF-D2:** Test H8 as **bounded experience followed by explicit naming, comparison, and consolidation**, not as unguided discovery. Evidence for either pure lecture or pure discovery will count as counter-evidence to the HL's simplified wording.

### Preliminary hypothesis test

- **H8 — still open, boundary refined.** External evidence supports problem-before-instruction under designed conditions and also warns against minimal guidance for novices. The iteration must test whether TFW-51/INNO materials provide enough structure and consolidation for the sequence to be educationally credible.

### Metacognitive check

The new result is not confirmation of the HL: both H5 and H8 now have explicit live counter-models. Source topology cannot be inferred from generic monorepo preference, and experience-first pedagogy is only defensible if guidance and consolidation are visible in the actual materials.

---
Stage complete: YES
