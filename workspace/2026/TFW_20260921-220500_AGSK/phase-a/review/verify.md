# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 15
> Files to verify: ⌈15 × 0.42⌉ = 7

## Verification Log

### V1: `.agent/rules/agents.md` (DELETE)
- **RF claim:** Deleted.
- **Actual:** `Test-Path .agent` → `False`. Directory and file absent from filesystem.
- **Match:** ✅

### V2: `.agents/workflows/tfw-plan.md` (DELETE, representative of 10)
- **RF claim:** All 10 workflow files deleted.
- **Actual:** `Test-Path .agents/workflows` → `False`. Directory absent. `git show 68dd9ce --stat` confirms all 10 files removed in Candidate commit.
- **Match:** ✅

### V3: `.agents/rules/tfw.md` (MODIFY)
- **RF claim:** Modified to reference `skills` instead of `workflows`.
- **Actual:** Line 8 now reads: `For /tfw-*, invoke the matching repository-local skill. The canonical workflow's Read Contract selects all further inputs.` — replaces the old `open .agents/workflows/tfw-<command>.md` instruction. No other references to `.agents/workflows/` present. 40 lines, 2225 bytes.
- **Match:** ✅

### V4: `.tfw/adapters/antigravity/tfw-rules.md.template` (MODIFY)
- **RF claim:** Synced with `.agents/rules/tfw.md`.
- **Actual:** `git diff --no-index .tfw/adapters/antigravity/tfw-rules.md.template .agents/rules/tfw.md` → exit code 0, zero output. Files are byte-identical. 40 lines, 2225 bytes each.
- **Match:** ✅

### V5: `.tfw/adapters/manifest.yaml` (MODIFY)
- **RF claim:** Retargeted `antigravity` commands to `.agents/skills`.
- **Actual:** Lines 79–82: `source: .tfw/adapters/codex/skills/tfw-{command}/SKILL.md`, `target: .agents/skills/tfw-{command}/SKILL.md`, `strategy: copy`. Persistent section still correctly points `tfw-rules.md.template` → `.agents/rules/tfw.md`. YAML is syntactically valid (parseable without error).
- **Match:** ✅

### V6: `.tfw/adapters/antigravity/README.md` (MODIFY)
- **RF claim:** Updated adapter docs to remove `.agent/` references.
- **Actual:** 18 lines. References `.agents/rules/` and `.agents/skills/`. No mention of `.agent/` (singular) or `workflows`. Step 2 of "Install or Repair" says "Copy every manifest command skill to `.agents/skills/tfw-{command}/SKILL.md`." Step 3 says "Preserve foreign neighbors and customized/unowned content." — the old legacy-preservation instructions (`.agent/rules`, `.agent/workflows`) removed.
- **Match:** ✅

### V7: Candidate commit membership
- **RF claim:** 15 VALUE files, 11 deletions + 4 modifications.
- **Actual:** `git show --stat 68dd9ce` → exactly 15 files changed: 8 insertions, 1241 deletions. 11 deletions (`.agent/rules/agents.md` + 10 workflows), 4 modifications (`.agents/rules/tfw.md`, `tfw-rules.md.template`, `manifest.yaml`, `README.md`). Zero non-VALUE files in Candidate. Zero trace files mixed in.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `Test-Path .agent; Test-Path .agents/workflows` | `False`, `False` |
| 2 | `git diff --no-index .tfw/adapters/antigravity/tfw-rules.md.template .agents/rules/tfw.md` | Exit 0, zero output (byte-equal) |
| 3 | `python -m pytest tools/tests/ docs/scripts/ -q` | 14 passed in 3.86s, exit code 0 |
| 4 | `git show --stat 68dd9ce` | 15 files changed, 8 insertions(+), 1241 deletions(-) |
| 5 | `git show --stat a26322e` | 4 files changed (RF, EV, journal, status) — trace-only |
| 6 | `git diff --stat e3f19b9 68dd9ce -- .agent/ .agents/ .tfw/adapters/` | 15 files, 8(+)/1241(-) |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | "Baseline: `e3f19b984fc1ba894a91cc6f832b59f2efc308ad`" | RF §1, EV E-accounting | `git log` confirms this is the `tfw: complete FRATS` commit, the immediate predecessor of the ONB commit | ✅ |
| C2 | "Candidate: `68dd9ce413dde6ecea5c54575a8b658380cd8df9`" | RF §1, EV E-accounting | `git show 68dd9ce` confirms "Implementation Candidate" commit with exactly 15 VALUE files, before EV/RF/trace writes | ✅ |
| C3 | "14 passed in 9.11s" | RF §4, EV E6 | Independent rerun: 14 passed in 3.86s, exit 0. Count matches; timing variation is expected | ✅ |

## Discrepancies Found

No discrepancies.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | `evidence/EV__phase-a__adapter_migration_and_cleanup.md` | ✅ exists | ✅ — 7 evidence rows, all VERIFIED, arithmetic matches git diff output |

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | HL §7.2 #1 | P0: `README.md` § How It Works | ✅ line 135 | ✅ — 5-row principle table | ✅ — "Inspectable project context" supports clean directory organization | ✅ — removing legacy directories makes project structure inspectable |
| 2 | HL §7.2 #2 | P1: `.tfw/conventions.md` Role Lock Protocol | ✅ conventions.md exists | ✅ — heading present | ✅ — Role Lock governs Coordinator/Executor/Reviewer separation | ✅ — Executor strictly followed TS directives |
| 3 | HL §7.2 #3 | P2: `.tfw/compilable_contract.md` §2 Reference Format | ✅ file exists | ✅ — §2 heading present | ✅ — exact-path references and cross-reference validity | ✅ — paths in artifacts are exact, no broken links within Phase A scope |
| 4 | HL §7.2 #4 | P3: `KNOWLEDGE.md` Row "Adapters" | ✅ line 31 | ✅ — row says "Antigravity authority is plural `.agents`; singular `.agent` is compatibility only" | ✅ — confirms `.agents` as authoritative root | ✅ — Phase A eliminates `.agent/` per this knowledge |
| 5 | HL §7.2 #5 | P5: `.tfw/adapters/manifest.yaml` Секции adapters | ✅ lines 74–82 | ✅ — four adapter sections present | ✅ — defines copy strategy and source/target | ✅ — manifest updated to skills target |

Total: 5, resolved: 5, semantically verified: 5, irrelevant: 0, hallucinated: 0

## Checkpoint

**Self-check:**
- [x] Opened ≥ 7 files and recorded findings? (7 verifications + 3 claim checks)
- [x] Independently established evidence applicability and ran necessary affected checks, or named the exact unresolved claim? (Ran tests, filesystem checks, git diffs independently)
- [x] Claim & Source Checks filled — 2-3 key claims spot-checked, every citation traced to a real artifact, data claims checked against a primary source (or explicit N/A with a reason)? (3 claims, all traced)
- [x] Each RF §3 (AC) checkmark verified against actual file? (AC-1 through AC-6 verified)
- [x] KNOWLEDGE.md checked — contradictions with changes documented? (KNOWLEDGE.md line 31 still references `.agent/workflows/` — update deferred to Phase B per TS §2 Out of Scope)
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist, meanings match, applications are relevant)?
  - Total: 5, resolved: 5, semantically verified: 5, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified (files exist, claims match)?
  - Total evidence items: 1 (EV file with 7 rows), verified: 1, missing: 0

Stage complete: YES

### Selected knowledge evidence

ONB §7 knowledge citations mirror HL §7.2 entries 1–5 with the same priority assignments. The Executor read and applied them per ONB §7 table (all marked "Applied"). No new citations were introduced in the ONB that were not already in the HL. The EV artifact is produced by the same Executor unit (`5a66cfd3-f075-45ad-9816-9d1aabf35468`) that produced the ONB and RF. Evidence applicability is independently confirmed by the Reviewer's own filesystem checks, git diffs, and test runs above — not inherited from the Executor's declarations.
