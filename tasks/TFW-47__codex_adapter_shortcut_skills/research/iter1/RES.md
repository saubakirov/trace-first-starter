# RES — TFW-47: Evidence Template Design (Iteration 1)

> **Date**: 2026-07-17
> **Author**: Researcher (Antigravity)
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW-47](../HL-TFW-47__codex_adapter_shortcut_skills.md)
> **Mode**: Pipeline

---

## Research Context

TFW-46 (D52) introduced evidence as a concept — three-role pipeline, 4-status vocabulary, §5 in RF template. But D16 made `evidence/` folder optional ("only for binary artifacts"). Result: 0/38 tasks created the folder. This iteration researches the evidence template file design — naming, internal structure, proportionality across task types, and alignment with TFW values — so that Phase A can implement it with confidence.

## Briefing

Reference: [1_briefing.md](1_briefing.md). User direction: EV abbreviation accepted, per-AC vs freeform needed research, minimum evidence bar needed empirical research from helpdesk/afd/tfw projects.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | **File name: `EV__{PREFIX}-{N}__{title}.md`** (2-letter abbreviation). Multi-phase: `EV__phase-{x}__{title}.md` | Fits the dominant TFW naming pattern (HL, TS, RF = 2 chars). Unambiguous. Per D28 (naming-as-prompting), short precise name creates correct agent behavior. User confirmed. |
| D2 | **Template structure: Environment header + per-AC evidence table + verdict line** | AFD-36/A empirically proved this structure works (7 rows, 6 VERIFIED, 1 DEFERRED). ISO 29119 validates the pattern (execution log = environment + per-test observations + summary). Environment header captures common denominator; row-level Environment column captures per-verification specifics. |
| D3 | **AC coupling: per-AC rows, comma-separated AC references for shared verifications** | Per-AC is more traceable — reviewer can check every AC has coverage. When one verification covers multiple ACs (e.g., "deployed to beta — AC-3, AC-5 verified"), the AC column accepts "AC-3, AC-5". This is what AFD-36 already did organically. |
| D4 | **Proportionality: no template tiers, no section optionality — row-level N/A + natural minimum bar** | Template tiers create decision fatigue (which tier? → agents always pick minimal). Section optionality creates "is this required?" confusion. Single template where you fill what you verified and N/A what you didn't. Minimum bar = environment header + ≥1 evidence row. Trivial task: 1-2 rows. Complex task: 10+ rows. The table length IS the proportionality. |
| D5 | **Environment header fields: Date, Author, OS, Language/Runtime (if applicable), Database (if applicable), Deploy target, CI/Pipeline (if applicable)** | Rich but with "(if applicable)" for non-universal fields. TFW methodology tasks don't have DB or CI. Frontend tasks don't have DB. The header self-documents what's relevant. ISO 29119: "test environment details" is mandatory but tailorable. |
| D6 | **Evidence table columns: `# | AC | What was verified | Environment | Result | Artifact`** — identical to RF §5 | Reuses the proven D52 table structure. No new column design needed. The value of EV over inline RF §5 is: (a) physical file existence, (b) environment header, (c) attachments index, (d) reviewer can audit without parsing RF. |
| D7 | **Attachments section: optional, only when binary artifacts exist in `evidence/`** | Screenshots, API responses, EXPLAIN plans, test output logs go into `evidence/` as files. The EV template lists them with descriptions. If no binary artifacts — section is empty/omitted. This is the legitimate use for D16's original "only for binary" intent — now the template file is always present, binary attachments are the optional part. |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| OQ1 | Should RF §5 be removed/simplified after EV file exists? | Open | RF §5 currently duplicates what EV captures. Options: (a) keep both (redundancy for quick RF scanning), (b) RF §5 becomes a one-line pointer to EV, (c) remove RF §5 entirely. Coordinator decision — not a research question. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | A single structured evidence template file per task (not per-AC) is sufficient for traceability | open | ✅ confirmed | Stress-tested against 3 task types (2-row trivial, 11-row complex, 5-row methodology). Per-AC table rows within a single file provide full traceability without per-AC file proliferation. |
| H2 | The evidence template should include environment metadata (OS, tool versions, timestamps) for reproducibility | open | ✅ confirmed | ISO 29119 mandates test environment details. AFD-36/A's per-row environment info is useful but insufficient alone — a header block captures the common denominator. Fields marked "(if applicable)" handle diversity. |

## HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| R1 | HL §3.1: Replace `EV__TFW-50__feature_x.md` placeholder with confirmed naming pattern and known structure (environment header + per-AC table + verdict + optional attachments) | D1, D2, D6, D7 |
| R2 | HL Phase A deliverable 1: Template structure is now defined — "Create `.tfw/templates/evidence/EV.md`" with the structure from D2/D5/D6/D7 | All decisions |
| R3 | HL §10 H1/H2: Mark as confirmed with evidence references | Hypothesis table |
| R4 | HL Phase A: Add consideration for RF §5 relationship (OQ1) — coordinator should decide during TS writing | OQ1 |

## Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | process | User's most active projects (helpdesk, afd, tfw) — user explicitly named these as the empirical base for design decisions. "afd" = `ai-first-devices` at `D:\projects\research\ai-first-devices` | User, briefing session 2026-07-17 | ★★★ |
| FC2 | environment | AFD-36/A (Codex executor) is the first and only RF to properly fill §5 Evidence with per-AC table, status vocabulary, and verdict line. All other RFs across all projects (helpdesk 30+ RFs, tfw 38 tasks) have no §5 Evidence section | Empirical scan, Gather stage | ★★★ |

> fact-candidates: processed 2026-07-30

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | process | User wants to "open a task folder and see `evidence/` with real verification results — not read the RF and take it on faith" (HL §1 quote). The physical folder is the psychological contract: filesystem presence = done, absence = not done. This is the same principle as D31 (file existence = stage completion) applied to evidence | User, HL §1 quote + D31 pattern | ★★★ |

## Findings Map

```
                    RESEARCH QUESTION
                    "What should EV look like?"
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
         NAMING         STRUCTURE    PROPORTIONALITY
         EV (2-char)    3 sections   No tiers
         D28 proven     │             N/A rows
                        │             min bar = env + 1
              ┌─────────┼─────────┐
              ▼         ▼         ▼
         ENV HEADER   TABLE     VERDICT
         OS, date,    per-AC    N/M VERIFIED
         tools,       rows      X DEFERRED
         DB (opt),    Result:   Y BLOCKED
         deploy (opt) VERIFIED/
                      DEFERRED/
                      BLOCKED/
                      N/A
                        │
                        ▼
                   ATTACHMENTS
                   (optional section)
                   binary files in evidence/

    EMPIRICAL VALIDATION
    ┌──────────────┬──────────────┬──────────────┐
    │ HD-13        │ HD-30/A      │ AFD-36/A     │
    │ trivial      │ complex      │ complex+deploy│
    │ 2 rows       │ 11 rows      │ 7 rows       │
    │ 1 DEFERRED   │ 11 VERIFIED  │ 6V + 1D      │
    └──────────────┴──────────────┴──────────────┘
```

## Iteration Status

> **Mandatory block.**

- **Iteration:** 1 of 2 (min) / 4 (max)
- **Hypotheses tested:** H1 (✅ confirmed), H2 (✅ confirmed)
- **Hypotheses deferred:** None
- **Gaps discovered:** OQ1 (RF §5 relationship with EV file — coordinator decision)
- **Superseded decisions:** None

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | RF §5 ↔ EV file redundancy | If both exist, agents will fill one sloppily | Coordinator decides in TS (not research scope) |

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to update HL and write TS
- [ ] **MORE NEEDED**
- [ ] **BLOCKED**

Iteration 1 covered all evidence template design questions. Iteration 2 (Codex adapter mechanics) is a separate topic per `iterations.yaml`.

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Research surveyed 3 real TFW-adopting projects (helpdesk, afd, tfw), examined RF evidence patterns empirically, and cross-referenced with ISO 29119 test execution log standards. The evidence template design converged to a single surviving configuration: `EV__{PREFIX}-{N}__{title}.md` with environment header, per-AC evidence table (reusing RF §5 columns), verdict line, and optional attachments index. All 4 dimensions (structure depth, AC coupling, proportionality, environment metadata) resolved through dimensional analysis without remaining ambiguity. AFD-36/A served as the empirical proof-of-concept — the only RF across all projects that filled §5 Evidence properly. The key insight: proportionality is not a template design feature but a natural consequence of table length (trivial = 2 rows, complex = 11 rows). Both HL hypotheses confirmed.

---

*RES — TFW-47: Evidence Template Design (Iteration 1) | 2026-07-17*
