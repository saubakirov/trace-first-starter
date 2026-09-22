# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42 (from `project_config.yaml`)
> RF files claimed: 10
> Files to verify: ⌈10 × 0.42⌉ = 5 (minimum); actual: 10/10 (100%)

## Verification Log

### V1: `.tfw/migrations/3.5.0.md`
- **RF claim:** Created with route table (§1), workflow retirement procedure (§2), `.agent/` classification algorithm (§3), and verification checklist (§4).
- **Actual:** File exists (101 lines). Contains § 1 "Pin the target and follow the complete route" with route table from 3.4.1 through 1.x. § 2 "Retire `.agents/workflows/`" with step-by-step install/remove. § 3 "Classify and retire `.agent/`" with content-type classification table. § 4 "Verify and complete the update" with 5-point verification checklist. Follows `3.4.0.md`/`3.4.1.md` structural precedents.
- **Match:** ✅

### V2: `KNOWLEDGE.md` (L31)
- **RF claim:** Adapters row updated: 11→10 routes, `.agent/workflows/`→`.agents/skills/`, `.agent` "fully retired".
- **Actual:** L31 reads: "One tooling manifest defines four vendor roots and 10 routes. [...] Antigravity and Codex share the `.agents/skills/` surface; singular `.agent` is fully retired". `git grep ".agent/workflows/" -- KNOWLEDGE.md` returns exit 1 (zero matches).
- **Match:** ✅

### V3: `.tfw/glossary.md` (L377-379)
- **RF claim:** Tool Adapter definition updated: `.agents/workflows/tfw-{command}.md` → `.agents/skills/tfw-{command}/SKILL.md`.
- **Actual:** L379 reads: "Antigravity uses `.agents/rules/tfw.md` for its persistent rule and `.agents/skills/tfw-{command}/SKILL.md` for commands."
- **Match:** ✅

### V4: `README.md` (L192)
- **RF claim:** Antigravity entry point updated: `.agent/rules/tfw.md` → `.agents/rules/tfw.md` plus `.agents/skills/tfw-*/SKILL.md`.
- **Actual:** L192 reads: `| Antigravity | .tfw/adapters/antigravity/ | .agents/rules/tfw.md plus .agents/skills/tfw-*/SKILL.md |`
- **Match:** ✅

### V5: `README.ru.md` (L190)
- **RF claim:** Same Antigravity entry point update (Russian localization).
- **Actual:** L190 reads: `| Antigravity | .tfw/adapters/antigravity/ | .agents/rules/tfw.md и .agents/skills/tfw-*/SKILL.md |`
- **Match:** ✅

### V6: `README.kk.md` (L191)
- **RF claim:** Same Antigravity entry point update (Kazakh localization).
- **Actual:** L191 reads: `| Antigravity | .tfw/adapters/antigravity/ | .agents/rules/tfw.md және .agents/skills/tfw-*/SKILL.md |`
- **Match:** ✅

### V7: `.tfw/CHANGELOG.md` (L8-40)
- **RF claim:** Added `## [3.5.0] — 2026-09-22` with AGSK codename, Changed/Removed/Compatibility subsections.
- **Actual:** L8 `## [3.5.0] — 2026-09-22`, L10 "AGSK — Antigravity Skill Migration & Legacy .agent Retirement", L14 `### Changed` (6 items), L27 `### Removed` (2 items), L33 `### Compatibility and updating` with link to `migrations/3.5.0.md`. Follows Keep a Changelog format.
- **Match:** ✅

### V8: `.agents/rules/tfw.md` (L35-43)
- **RF claim:** Added `### Coordination Messaging` section with `send_message` instructions for all TFW roles.
- **Actual:** L35-43 contain the section with UUID extraction instructions, Researcher/Executor/Reviewer reporting requirements, and cross-session support statement. Matches TS §6 point 3 prescribed content verbatim.
- **Match:** ✅

### V9: `.tfw/adapters/antigravity/tfw-rules.md.template`
- **RF claim:** Synchronized with `.agents/rules/tfw.md` (byte-identical).
- **Actual:** `git diff --no-index .tfw/adapters/antigravity/tfw-rules.md.template .agents/rules/tfw.md` → exit 0, zero output. Byte-identical confirmed.
- **Match:** ✅

### V10: `.tfw/adapters/antigravity/README.md`
- **RF claim:** Added `## Coordination Messaging` section documenting cross-session addressed messaging.
- **Actual:** L19-33 contain "Coordination Messaging" section with role/reports table (Researcher, Executor, Reviewer), UUID extraction instructions, and cross-session platform support statement.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `git diff --numstat --find-renames=50% a26322e bde7334 -- $valuePaths` | 10 files: 174 adds, 5 deletes, 179 touched LOC. Exact match to RF claim. |
| 2 | `git diff --no-index .tfw/adapters/antigravity/tfw-rules.md.template .agents/rules/tfw.md` | Exit 0, zero output. Byte-identical. |
| 3 | `git grep ".agent/workflows/" -- KNOWLEDGE.md .tfw/glossary.md README.md README.ru.md README.kk.md` | Exit 1, zero matches. No stale workflow references. |
| 4 | `git grep ".agent/rules/tfw.md" -- README.md README.ru.md README.kk.md` | Exit 1, zero matches. No stale rule references. |
| 5 | `python -m pytest tools/tests/ docs/scripts/ -q` | 14 passed in 3.72s, exit code 0. |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|---|---|---|---|
| C1 | "Candidate `bde7334ff626e8c2c43f315717f90271182b4ab3`" | RF §1 accounting | `git log --oneline bde7334 -1` — exists as a valid commit in the repository | ✅ |
| C2 | "TS approval ref `637df43` (ONB commit containing approved TS)" | EV E-accounting | Journal entry `20260922-105700__transition__c218.md` confirms owner-direct TS approval via `/tfw-handoff`; the ONB was committed at that point | ✅ |
| C3 | "Baseline `a26322ea1551a376510d5403e0e7a2dfec5d4dcb`" | RF §1, TS §4 | TS §4 declares this as Phase A RF commit; Phase A was approved by REVIEW | ✅ |

## Discrepancies Found

No discrepancies.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|---|---|---|
| E1 | `evidence/EV__phase-b__migration_guide_and_documentation_sync.md` | ✅ | ✅ — 8 evidence rows (E1-E7 + E-accounting), all VERIFIED, matching RF §5 "8/8 VERIFIED" |
| E2 | `evidence/doc-sweep.txt` | ✅ | ✅ — 10 CLEAN lines for all VALUE paths, pattern `.agent/workflows/` and `.agent/rules/tfw.md`, zero matches |

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|---|---|---|---|---|---|
| 1 | HL §7.2 #1 | P0 — `README.md` § How It Works: "Inspectable project context" | ✅ | ✅ — L139 | ✅ — README adapter table update ensures consistent directory layout presentation | ✅ — directly relevant to AC-4 (adapter table updates reflect actual file structure) |
| 2 | HL §7.2 #2 | P1 — `.tfw/conventions.md` Role Lock Protocol | ✅ | ✅ — L1426 | ✅ — Executor role lock prohibits HL/TS/RES/REVIEW modifications | ✅ — Executor correctly restricted to implementation only |
| 3 | HL §7.2 #3 | P2 — `.tfw/compilable_contract.md` §2 Reference Format | ✅ | ✅ | ✅ — cross-references in migration guide follow compilable format (relative links to `3.4.0.md`, `3.4.1.md` etc.) | ✅ |
| 4 | HL §7.2 #4 | P3 — `KNOWLEDGE.md` Row "Adapters" | ✅ | ✅ — L31 | ✅ — directly targeted for AC-2 update | ✅ |
| 5 | HL §7.2 #5 | P5 — `.tfw/adapters/manifest.yaml` | ✅ | ✅ | ✅ — manifest paths verified as source of truth; manifest not modified (Phase A scope) | ✅ |

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings?
- [x] Independently established evidence applicability and ran necessary affected checks, or named the exact unresolved claim?
- [x] Claim & Source Checks filled — 2-3 key claims spot-checked, every citation traced to a real artifact, data claims checked against a primary source (or explicit N/A with a reason)?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist, meanings match, applications are relevant)?
  - Total: 5, resolved: 5, semantically verified: 5, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified (files exist, claims match)?
  - Total evidence items: 8, verified: 8, missing: 0

Stage complete: YES

### Selected knowledge evidence

ONB §7 cites the same 5 HL §7.2 references with matching applied/N/A assessments. The Executor unit (`ec458eac-9120-412b-ae03-78f365c5484d`) is distinct from the Coordinator (`8888199a-c102-44c8-b661-f9c6bef8d7a6`). Activation source is owner-direct (`/tfw-handoff`). Phase A predecessor (Candidate `68dd9ce`, approved via REVIEW at `phase-a/REVIEW__phase-a__adapter_migration_and_cleanup.md`) provides the verified baseline. No missing producers or unresolved attribution.
