# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW-47](../../HL-TFW-47__codex_adapter_shortcut_skills.md)
> Goal: Every completed task produces a mandatory `evidence/` folder with a structured EV template file.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1: Sections structure | env header + table + verdict | D2: Freeform narrative | no table | Sections structure requires a table; freeform eliminates it |
| D3: Template tiers | minimal/full selection | D3: Row-level N/A | per-row status | Tiers add selection overhead that N/A rows already solve — redundant, not incompatible but wasteful |
| D4: Freeform env block | unstructured text | D1: Full report | per-AC sections | Full report demands structured environment for reproducibility; freeform undermines it |

**Surviving configurations:**

| Config | D1: Structure | D2: AC coupling | D3: Proportionality | D4: Environment | Notes |
|--------|--------------|----------------|--------------------|--------------------|-------|
| C1 | Sections (env + table + verdict) | Per-AC rows | Row-level N/A | OS + tools + timestamp | Minimal environment, proven table |
| C2 | Sections (env + table + verdict) | Per-AC rows | Row-level N/A | + DB/runtime + deploy target | Richer environment, AFD-36 proof |
| C7 | Sections (env + table + verdict) | Per-AC rows | Min bar = env + 1 row | + DB/runtime + deploy target | Simplest proportionality |

**Unexpected survivors:**
- **C7** survived despite being the simplest — no "required vs optional" distinction means zero decision points for the agent. The minimum bar (environment + 1 verification row) is the proportionality mechanism itself: trivial tasks fill 1 row, complex tasks fill N rows. N/A status handles ACs that can't be verified yet.

## Findings

### C1: Stress-test against HD-13 (trivial frontend refactor)

**Task:** Remove client-side filtering, switch to server-side API params. No deploy.
**RF §4 Verification:** `npm run build`: ✅ 0 errors, 111 modules. Manual verification awaits deploy.
**What EV would look like:**

```markdown
## Environment
- OS: Windows
- Node: (version)
- Date: 2026-04-17
- Deploy target: beta (not deployed)

## Evidence Table
| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1..AC-11 | `npm run build` — 0 errors, 111 modules, 313ms | Local dev | VERIFIED | — |
| E2 | AC-1..AC-8 | Manual browser testing of filter behavior | Beta | DEFERRED | Not deployed yet |

Evidence verdict: 1/2 VERIFIED, 1 DEFERRED
```

**Verdict:** Template works. 2 rows, ~15 lines total. Proportional. Not overhead. Even this trivial case benefits from explicit DEFERRED status — it makes "awaits deploy" visible and trackable.

### C2: Stress-test against HD-30/A (complex backend + migration)

**Task:** 11 ACs, MCP postgres validation, EXPLAIN plans, migration roundtrip, 355 tests.
**RF §4:** 60+ lines of inline evidence (SQL outputs, EXPLAIN plans, test counts).
**What EV would look like:**

```markdown
## Environment
- OS: Windows
- PostgreSQL: 16.11 (localhost:5433/helpdesk)
- Python: 3.11.5 (.venv)
- Date: 2026-05-15
- Deploy target: beta (not deployed in Phase A)

## Evidence Table
| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Repeated query params parsed as list; legacy single-value compat | Integration test | VERIFIED | test_filters_smoke.py |
| E2 | AC-2 | IN-clause WHERE blocks + empty-list guard | 5 unit tests | VERIFIED | test_ticket_repo_filters.py |
| E3 | AC-3 | Migration 026: 13→16 indexes, roundtrip clean | MCP postgres | VERIFIED | evidence/migration_roundtrip.txt |
| E4 | AC-4 | CREATE STATISTICS: 0→2 pg_statistic_ext entries | MCP postgres | VERIFIED | — |
| E5 | AC-5 | EXPLAIN ANALYZE plans: no Seq Scan >50% at scale | Integration test | VERIFIED | evidence/explain_plans.txt |
| E6 | AC-6 | Distinct endpoints: correct JSON, RLS, Redis cache | 8 unit tests | VERIFIED | test_references_distinct.py |
| E7 | AC-7 | Export cache canonical hash stability | 9 unit tests | VERIFIED | test_export_cache_canonical.py |
| E8 | AC-8 | Normalize idempotent, 12 confusables | 20 unit tests | VERIFIED | test_text_normalize.py |
| E9 | AC-9 | Write-side hook on create, whitelisted keys | Unit + integration | VERIFIED | — |
| E10 | AC-10 | pg_trigger audit check: empty result | MCP postgres | VERIFIED | — |
| E11 | AC-11 | Integration: RLS, homoglyph, distinct, EXPLAIN | Testcontainers PG | VERIFIED | test_filters_smoke.py |

Evidence verdict: 11/11 VERIFIED, 0 DEFERRED
```

**Verdict:** Table works at 11 rows. EXPLAIN plans go into `evidence/explain_plans.txt` as a binary/text artifact rather than bloating the table. The `Artifact` column handles this naturally.

### C3: Stress-test against TFW-46/A (methodology task, no code runtime)

**Task:** Update conventions.md, glossary.md, templates. No build, no deploy, no runtime.
**What was actually verified:** File existence, word counts, section structure.
**What EV would look like:**

```markdown
## Environment
- OS: Windows
- Editor: Claude Code / Antigravity
- Date: 2026-07-10
- Deploy target: N/A (documentation)

## Evidence Table
| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | conventions.md §3 updated with evidence sections | File diff | VERIFIED | — |
| E2 | AC-2 | conventions.md §12 extended with 2 entries | File diff | VERIFIED | — |
| E3 | AC-3 | conventions.md §14 has 5 evidence anti-patterns | File diff | VERIFIED | — |
| E4 | AC-4 | TS template has Evidence field in §5 AC items | File inspection | VERIFIED | — |
| E5 | AC-5 | RF template §5 Evidence section present with table | File inspection | VERIFIED | — |

Evidence verdict: 5/5 VERIFIED, 0 DEFERRED
```

**Verdict:** Even methodology tasks produce meaningful evidence rows. "File diff" and "File inspection" are legitimate environments for documentation tasks. The template doesn't force runtime environment metadata that doesn't exist.

### C4: C1 vs C2 vs C7 — what actually differentiates them?

| Aspect | C1 | C2 | C7 |
|--------|----|----|-----|
| Environment depth | Minimal (OS + tools) | Rich (+ DB, deploy target) | Rich (same as C2) |
| Proportionality | Row-level N/A | Row-level N/A | Min bar (env + 1 row) |
| Difference from C2 | Less env info | Reference config | Simpler proportionality |

**Key realization:** C1 and C7 are C2 variants, not independent configurations.
- C1 = C2 with less environment info → just make environment fields optional beyond OS/date/tools
- C7 = C2 with "min bar" language → the min bar IS the N/A mechanism (1 row where everything is N/A = degenerate case of the same table)

**C2 absorbs C1 and C7.** The template has rich environment fields but marks them "(if applicable)." The minimum bar is not a separate mechanism — it's a natural consequence of "fill the table, use N/A where not applicable."

### C5: Attack — "Does per-AC coupling fail when ACs are fine-grained?"

AFD-36 had 5 ACs → 7 evidence rows (some ACs got multiple verification angles). HD-30 had 11 ACs → 11 rows. What if a task has 20 ACs?

**Answer:** TS §5 already caps ACs at a reasonable number (typically 5-15 per phase). And per-AC rows don't mean one-row-per-AC-exclusively — multiple ACs can share a row (AC column: "AC-3, AC-5, AC-8"). The table scales linearly with verification acts, not with AC count.

### C6: Attack — "Is the environment header redundant with the Environment column in each row?"

AFD-36 put environment info per-row. The proposed template adds a header block. Is this redundant?

**Answer:** No. The header captures **common denominator** (OS, date, tools). Rows capture **per-verification specifics** (which DB instance, which deploy target). This is the ISO 29119 pattern: test execution log has a header environment + per-test observations.

Example: Header says "PostgreSQL 16.11, localhost:5433". Row E3 says "MCP postgres query against same instance." No repetition.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C2 absorbs C1 and C7 — single surviving configuration | — |
| Template tested against 3 task types: trivial (2 rows), complex (11 rows), methodology (5 rows) | — |
| Environment header + per-row environment = complementary, not redundant | — |
| Per-AC coupling scales; comma-separated ACs handle shared verifications | — |
| Minimum bar = natural consequence of N/A, not separate mechanism | — |

**Sufficiency:**
- [x] External source used? (ISO 29119 environment header pattern)
- [x] Briefing gap closed? (All dimensions resolved to single surviving config)
- [x] Pairwise incompatibility checked? Surviving configurations listed? (C2 = sole survivor)

Stage complete: YES
→ User decision: proceed to RES
