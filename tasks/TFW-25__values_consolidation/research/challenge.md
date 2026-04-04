# Challenge — "What do we NOT expect?"
> Parent: [HL-TFW-25](../HL-TFW-25__values_consolidation.md)
> Goal: Stress-test the three most aggressive proposals from Extract.

## Findings

### C1: Dropping "Determinism and Safety" from README Values

**Proposal:** Remove because it's "fully covered by conventions §12."

**Challenge:** External research says safety exists at BOTH levels — as a *principle* ("why we care") and as *rules* ("how we enforce it"). Microsoft, Google, NIST all include safety in their top-level values AND in implementation specs. Dropping it from values while keeping it only in conventions means TFW would have enforcement without stated belief.

**Counter-argument for dropping:** The current "Determinism and Safety" section in README lists 5 bullet points — and all 5 are implementation rules ("don't fabricate data", "use environment variables", "never claim something was run"). Not one bullet states a *belief*. It reads like conventions §12 copy-pasted into the README.

**Resolution:** Don't drop the *concept* — drop the current *implementation*. Rewrite as a genuine value statement:

> **Honesty Over Convincingness** — AI agents that sound confident while being wrong are more dangerous than agents that refuse to answer. TFW agents must never fabricate data, claim untested results, or simulate external systems. When context is insufficient, the correct behavior is to ask, not guess.

This captures the *belief* (honesty > convincingness) while the *rules* stay in conventions §12. The rename also follows D28 (Naming Creates Behavior) — "honesty" triggers different agent behavior than "determinism."

**Verdict:** RENAME + REWRITE, not remove. **Values count stays at 7** (or becomes 8 with the rename).

### C2: Is 3-tier the right taxonomy, or would 2-tier be simpler?

**Proposal (HL):** 3-(layered hierarchy: README Values / KNOWLEDGE §0 Principles / conventions Rules.

**Challenge:** 2-tier (Values + Rules, no middle layer) would be simpler — fewer places to maintain, less confusion about where something belongs.

**Counter-argument:** The middle tier (KNOWLEDGE §0) serves a role the other two can't:
- README Values = public-facing philosophy (stable, rarely changes)
- conventions.md Rules = enforceable standards (changes with implementation)
- KNOWLEDGE §0 = *battle-tested design decisions* that are too specific for public philosophy but too strategic for rule lists

Example: P5 "Meta-project awareness" — this is a unique design principle for this specific project (TFW describes itself using itself). It's not a universal value for the README, and it's not an enforceable rule. It belongs in a middle tier.

**Also:** 7 items stay in §0 after pruning. That's a manageable middle tier — compact enough to scan in one read. If it were 2-3 items, merge up; if 15+, too bloated. 7 is the right size.

**Verdict:** 3-tier is correct. The middle tier earns its existence.

### C3: Could pruning 12 knowledge/ facts cause information loss?

Testing each candidate against: "Would the next agent decide differently not knowing this?"

**Convention facts proposed for pruning:**
| Fact | Info loss risk | Verdict |
|------|---------------|---------|
| F4 (checkpoint fields in templates) | Zero — templates are the source | ✅ Safe to prune |
| F5 (ref-inside-step pattern) | Low — plan.md demonstrates it. BUT this is the *named pattern* that explains WHY refs work. D28 applies: naming > explanation | ⚠️ **KEEP** — the name "ref-inside-step" has value beyond the code |
| F6 (Config Sync Registry scope) | Low — workflow explains it | ✅ Safe to prune |
| F8 (§3.1 domain-agnostic) | Zero — template shows it | ✅ Safe to prune |
| F9 (filesystem state machine) | Zero — P14 + code cover it. philosophy/F4 also covers it | ✅ Safe to prune |
| F10 (RES = synthesis) | Zero — template structure shows it | ✅ Safe to prune |
| F12 (stage template structure) | Zero — templates exist | ✅ Safe to prune |

**Revised convention pruning: 6 facts (not 7)** — keep F5 (ref-inside-step is a named pattern per D28).

**Process facts proposed for pruning:**
| Fact | Info loss risk | Verdict |
|------|---------------|---------|
| F2 (knowledge ≠ docs) | Low — two separate workflows. But philosophy/F2 covers the distinction better | ✅ Safe to prune (philosophy/F2 = authoritative version) |
| F3 (scan conversation for FCs) | Zero — template instruction | ✅ Safe to prune |
| F8 (crash → gate skipping) | Low — process/F10 (resume protocol) documents the fix. Problem statement without fix = noise | ✅ Safe to prune |
| F9 (4 roles) | Zero — conventions §15 | ✅ Safe to prune |
| F10 (resume protocol) | Zero — base.md Step 0 | ✅ Safe to prune |

**Process pruning: 5 facts — all confirmed safe.**

**Final pruning count: 11 facts (was 12, kept convention/F5)**
- convention: 12 → 6 facts
- process: 10 → 5 facts
- philosophy: 4 → 4 facts (user: keep all)
- constraint: 3 → 3 facts (all strategic)
- **Total: 29 → 18 facts**

## Checkpoint

| Found | Remaining |
|-------|-----------|
| "Determinism/Safety" → RENAME to "Honesty Over Convincingness", not remove | None |
| 3-tier taxonomy validated — middle tier earns its existence | None |
| Pruning adjusted: 11 facts (not 12) — kept convention/F5 | None |
| Values count = 8 (not 7) with the rename | Within HL cap |

**Sufficiency:**
- [x] External source used? (safety-as-value research)
- [x] Briefing gap closed? (all three stress tests resolved)

Stage complete: YES
→ User decision: ___
