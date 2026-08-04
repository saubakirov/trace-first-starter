# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Mode: spec
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | Verify V2-V7 establishes AC-1 through AC-6; the independent Reviewer trace and final 16-subject audit close the Executor-deferred part of AC-6 |
| 2 | Philosophy aligned | ✅ | One Markdown owner, precise names, no runtime, no duplicated grammar, no cadence, and explicit publication authority align with all seven HL §7 principles; see Principles Check below |
| 3 | Tech debt documented | ✅ | RF §6 records two pre-existing role-label inconsistencies; both were verified and triaged below rather than silently ignored |
| 4 | Style & standards | ✅ | Six-path total scope, two-file correction, English artifact structure/content, one normative sentence/example, no placeholders, and passing `git diff --check` satisfy conventions |
| 5 | Observations collected | ✅ | RF observations are accurate naming drift, but neither creates a subject/push conflict because conventions §15 owns the role value; quality filter does not promote them as TFW-50 debt |
| 6 | RF completeness (§7-9) | ✅ | RF §7 contains two human-sourced correction facts; §8 contains three bounded execution insights; §9 diagrams the single-owner/four-role/no-cadence relationship |
| 7 | Evidence completeness | ✅ | TS AC-1 through AC-5 prescribe N/A repository-source evidence and EV records N/A; AC-6 EV correctly deferred Reviewer-owned proof at Executor handoff, then Verify V6/V7 resolves it without altering Executor evidence |

## Mode-Specific Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 8 | Analytical quality | ✅ | The full trace preserves the original plan and implementation, exposes the handoff-centered gap, inventories all role/consumer classes, retains Extract's rejected cadence proposal as evidence, and uses Challenge to derive C7 before revising HL/TS/ONB; Verify V1/V5/V6 confirms implementation follows that conclusion |
| 9 | Source attribution | ✅ | Verify V8 confirms all 22 HL/ONB citation rows and the official Git primary-source claims about title/subject, author/committer metadata, and authentication; hallucinations: 0 |

## Principles Check

| HL §7 principle | TS mapping | Verified AC result | Principle violation? |
|-----------------|------------|--------------------|----------------------|
| P1 Outcome over mechanism | AC-1, AC-6 | One searchable subject contract; 16/16 readable current-task subjects; no runtime | No |
| P2 Naming creates behavior | AC-1, AC-2 | Exact grammar and five precisely derived terms | No |
| P3 Single source of truth | AC-1, AC-4 | One normative owner; glossary/reference and conflict-specific instantiations only | No |
| P4 Declared context, not identity proof | AC-2, AC-5 | Subject trace is separated from Git author/committer metadata and authentication; no unmarked-human inference | No |
| P5 Human publication authority | AC-4, AC-6 | Handoff and release require explicit push approval; remote remains baseline | No |
| P6 Proportional completeness | AC-3, AC-5 | Four roles covered through universal ownership without 20-copy/cadence expansion | No |
| P7 Transparent boundaries | AC-4, AC-5, AC-6 | Six paths, four protected blobs, exact exclusions, confounders, tests, cleanup, and no-publication state are explicit | No |

## Definition of Failure Check

| TS §7 failure condition | Triggered? | Evidence |
|-------------------------|------------|----------|
| Implementation outside six-path allowlist | No | Verify V4: unexpected 0, missing 0 |
| New framework/runtime/config/state file or phase | No | Verify V4 and full range path inventory |
| Full rule duplicated outside conventions | No | Verify V2/V5: one grammar occurrence in non-task corpus |
| New commit cadence/checkpoint policy | No | Verify V5 and added-line inspection |
| Handoff Evidence drift changed | No | Verify V3: full preserve blobs equal `389168a` |
| Authentication/human-detection claim | No | Verify V2/V8 |
| Extra fields, fixed limits, matrices, or trailers | No | Verify V2/V4 |
| Handoff/release automatic push | No | Verify V3/V5 |
| Remote action, history rewrite, or hook restoration | No | Verify V1/V4/V7 |
| Failed tests/checks or generated debris | No | Verify V7: 55 unit + 13 integration passed; generated roots removed |

## Observations Triage

| RF observation | Verified? | Quality-filter decision | Rationale |
|----------------|-----------|-------------------------|-----------|
| `docs.md` role header says `Coordinator / Reviewer` | ✅ | Do not promote | It is pre-existing, outside TFW-50, and produces no current subject error: conventions §15 is the normative owner and actual docs subjects use `coordinator` |
| `release.md` role header says `Coordinator / Maintainer` | ✅ | Do not promote | It is pre-existing, outside TFW-50, and produces no current subject error: conventions §15 and active `RELEASE.md` both use `coordinator` |

No project-level TECH_DEBT entry is warranted by the review quality bar. If role-label normalization is later desired for consistency, it requires a separately approved cleanup rather than expansion of TFW-50.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|----------------|----------|----------------|
| 1 | D15 / convention F5: canonical workflow ownership and thin adapters | One normative conventions owner; only conflicting handoff copies changed | No |
| 2 | D23 / philosophy F22: compress instructions and avoid template/prompt bloat | One sentence, one example, concise glossary; rejected 20-copy expansion | No |
| 3 | D24: enforcement-critical values inline | All five subject components and publication boundary are inline in the sole rule | No |
| 4 | D28 / process F3-F4: precise naming plus actionable steps | Exact field names and point-of-use conflict fixes | No |
| 5 | process F6/F22: resist scope explosion and generic overhead | Challenge removed unsupported cadence and broad adapter churn | No |

## Fact Candidate Challenge

RF §7's two candidates are genuine human-supplied corrections and pass the Human-Only Test. They remain candidates for later `/tfw-knowledge`; this review neither promotes them nor duplicates them.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Checked RF §7-9 for presence AND quality (not just existence)?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"?
- [x] Fact Candidates from RF reviewed — any that need challenge?

Stage complete: YES
