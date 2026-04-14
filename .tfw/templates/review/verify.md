# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: {code / docs / spec}
> Min verify ratio: {from PROJECT_CONFIG.yaml, default 0.42}
> RF files claimed: {N}
> Files to verify: ⌈N × ratio⌉ = {M}

## Verification Log

### {V1: file path}
- **RF claim:** {what RF says about this file}
- **Actual:** {what the file actually contains}
- **Match:** ✅ / ❌ / ⚠️ partial

### {V2: file path}
...

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | {build/test/lint command} | {output summary} |

> If no commands could be run: state why. "No test runner" is valid.

## Discrepancies Found

{List. If none: "No discrepancies."}

> On ANY discrepancy: escalate to 100% verification (check all files).

## Checkpoint

**Self-check:**
- [ ] Opened ≥ ⌈N × ratio⌉ files and recorded findings?
- [ ] Ran at least 1 build/test command (or documented why not)?
- [ ] Each RF §3 (AC) checkmark verified against actual file?
- [ ] KNOWLEDGE.md checked — do changes contradict known decisions?
  - If yes: list contradictions
  - If no applicable items: "No KNOWLEDGE.md contradictions."

Stage complete: YES / NO
