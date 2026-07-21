# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-47](../../HL-TFW-47__codex_adapter_shortcut_skills.md)
> Goal: Every completed task produces a mandatory `evidence/` folder with a structured EV template file.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: Template structure depth | Flat table (AC-aligned rows only) | Sections: environment + table + verdict | Full report (environment + per-AC sections + verdict + attachments index) | Minimal header + freeform |
| D2: AC coupling | Per-AC rows (one E-row per acceptance criterion) | Per-verification-act rows (one row per thing observed, may combine ACs) | Freeform narrative (no table) | |
| D3: Proportionality mechanism | Section-level optionality (required header, optional detailed sections) | Row-level N/A status (every AC gets a row, trivial ones = N/A with reason) | Template tiers (minimal vs full, selected by task complexity) | Single template, minimum bar = environment + 1 verification |
| D4: Environment metadata depth | OS + tool versions + timestamp only | + database/runtime versions + deploy target | + network/infra context + CI pipeline ID | Freeform "Environment" text block |

## Findings

### G1: Empirical evidence patterns across 3 projects (helpdesk, afd, tfw)

**AFD-36/A** (complex, multi-service, beta deploy) — the only RF with a real `§5. Evidence` section:
- 7 evidence entries (E1–E7), per-AC, structured table with columns: `# | AC | What was verified | Environment | Result | Artifact`
- 6 VERIFIED, 1 DEFERRED — uses the D52 status vocabulary correctly
- Environment column varies per row: "JVM unit + PostgreSQL 16 Testcontainer + beta PostgreSQL", "H2 PostgreSQL-mode unit + beta PostgreSQL"
- Artifact column references test files + live query results + pipeline IDs
- Verdict line: "Evidence verdict: 6/7 VERIFIED, 1 DEFERRED, 0 BLOCKED, 0 N/A"
- **Key observation:** This RF was written by Codex executor — the first to actually fill §5 Evidence. The section already has the structure the EV template needs.

**HD-30/A** (complex, backend filters + migration) — no §5 Evidence section at all:
- Written pre-D52 (2026-05-15, before evidence layer shipped)
- §4 Verification contains rich inline evidence: SQL EXPLAIN plans (40+ lines), MCP postgres query results, migration roundtrip logs, test counts
- Evidence is there but unstructured — scattered across §4 Verification
- Environment info embedded in prose: "local PG 16.11 via MCP", "localhost:5433/helpdesk"

**HD-13** (simple, frontend-only refactor) — no §5 Evidence:
- §4 Verification = 2 lines: build command result + "manual verification awaits deploy"
- Zero real-environment evidence — purely synthetic (build passed)
- This is the "trivial task" case: what would go in `evidence/`?

**TFW tasks** (methodology-only, no code execution):
- 0/38 tasks have `evidence/` folder
- §4 Verification typically = "file count matches", "word count reduced by X%"
- Evidence is inherently different: file existence, diff stats, grep counts

### G2: ISO 29119 test execution log structure (external)

ISO/IEC/IEEE 29119-3 defines a Test Execution Log with:
- **Log identifier** — unique ID
- **Environment details** — hardware, software, configuration
- **Test procedure references** — links to test cases
- **Execution metadata** — date, tester, status per test
- **Actual results** — what was observed
- **Incident references** — links to bug reports
- **Environmental observations** — environment-related issues

Key principles from external research:
1. **Centralize evidence** — don't scatter across Slack/email/local drives
2. **Maintain traceability** — every test traces to a requirement
3. **Distinguish product defects from environment issues**
4. **Consistent formatting** — standardized templates
5. **Tailorable** — ISO 29119 explicitly supports lightweight tailoring for Agile

### G3: Existing TFW naming patterns

| Artifact | Abbreviation | File pattern | Length |
|----------|-------------|-------------|--------|
| High Level | HL | `HL-{PREFIX}-{N}__{title}.md` | 2 chars |
| Task Spec | TS | `TS__{PREFIX}-{N}__{title}.md` | 2 chars |
| Result File | RF | `RF__{PREFIX}-{N}__{title}.md` | 2 chars |
| Research | RES | `RES__{PREFIX}-{N}__{title}.md` | 3 chars |
| Onboarding | ONB | `ONB__{PREFIX}-{N}__{title}.md` | 3 chars |
| Review | REVIEW | `REVIEW__{PREFIX}-{N}__{title}.md` | 6 chars |
| **Evidence** | **EV** | `EV__{PREFIX}-{N}__{title}.md` | **2 chars** |

Pattern: 2-3 letter abbreviations dominate (5/6). REVIEW is the outlier. `EV` fits perfectly — short, unambiguous, follows the naming-as-prompting principle (D28).

### G4: RF §5 Evidence table already has the right columns

The current RF template `§5. Evidence` (from D52) has:
```
| # | AC | What was verified | Environment | Result | Artifact |
```

AFD-36/A proves this table works in practice. The EV template can reuse this exact structure — it's not a new invention, it's an extraction from RF into its own file.

**What EV adds over inline RF §5:**
1. Environment metadata header (once per task, not per-row)
2. Attachments index (binary artifacts get listed)
3. Physical file existence = auditable by reviewer
4. Separation of concerns: RF = what was done, EV = proof it works

### G5: Minimum evidence bar — empirical analysis

| Task type | Example | What was actually verified | Minimum viable evidence |
|-----------|---------|---------------------------|-------------------------|
| Complex backend + deploy | AFD-36/A | 7 per-AC verifications, beta deploy, PromQL queries | Full table, all ACs, real environment |
| Complex backend, pre-deploy | HD-30/A | EXPLAIN plans, migration roundtrip, 355 tests, MCP queries | Table + inline artifacts |
| Simple frontend refactor | HD-13 | `npm run build` passed | Environment + "build clean" = 1 row |
| TFW methodology (no code) | TFW-46/A | File count, diff stats, word count | Environment + "files created as specified" |

**Observation:** Even the simplest task has *something* to evidence — at minimum, the build/lint command and its output. The proportionality isn't "skip evidence" but "fewer rows in the table."

## Checkpoint

| Found | Remaining |
|-------|-----------|
| 4 dimensions identified with 3-4 alternatives each | — |
| AFD-36/A = working proof of RF §5 table structure | — |
| 0/38 TFW tasks created `evidence/` | — |
| ISO 29119 validates environment + traceability + centralization | — |
| EV naming fits TFW patterns (2-char, unambiguous) | — |
| Minimum bar = environment header + ≥1 verification row | — |

**Sufficiency:**
- [x] External source used? (ISO 29119 test execution log)
- [x] Briefing gap closed? (All 3 guiding questions addressed: naming=EV, per-AC=yes with N/A, minimum bar=environment+1 row)
- [x] Dimensions identified? (4 independent dimensions: structure depth, AC coupling, proportionality, environment depth)

Stage complete: YES
→ User decision: ___
