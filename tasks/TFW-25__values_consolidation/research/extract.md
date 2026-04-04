# Extract — "What do we NOT see?"
> Parent: [HL-TFW-25](../HL-TFW-25__values_consolidation.md)
> Goal: Exact audit — which P# items move, which knowledge/ facts are prunable, which README values stay/change.

## Findings

### E1: P1-P14 classification with action

Cross-referencing every P# against the Values/Principles/Rules taxonomy and checking if the content is already expressed elsewhere:

| P# | Content (short) | Tier | Already in... | Action |
|----|----------------|------|---------------|--------|
| P1 | Traces over code | **Value** | README §Values ("Traces Over Code") | STAY in §0. Already in README — no change needed |
| P2 | Index, don't duplicate | **Value** | README §Values ("Single Source of Truth") | STAY in §0. Subsumed by SSOT in README |
| P3 | Philosophy stays rich — narrative > DRY | **Value** | Implicit in README narrative format | STAY in §0. Unique nuance — worth keeping |
| P4 | Glossary = dictionary, conventions = rules | **Rule** | Self-evident from conventions.md §1 + glossary format | REMOVE from §0. Obvious from file structure |
| P5 | Meta-project awareness | **Principle** | Unique — not stated elsewhere | KEEP in §0 (compress to 1-liner). Relevant for meta-project only |
| P6 | Lightweight docs | **Rule** | Implicit in tfw-docs workflow (5-item checklist) | REMOVE from §0. Workflow IS the implementation |
| P7 | Self-review ≠ review — separate roles | **Value** | README §Roles (4 roles). conventions §15 (Role Lock) | STAY in §0. Core belief about quality |
| P8 | RESEARCH ≠ passive checklist | **Value/Principle** | research/base.md Mindset + Rules | COMPRESS in §0. Long description → 1-liner. Enforcement lives in workflow |
| P9 | Coordinator Mindset: quality > speed | **Value** | README §Values ("Completeness Over Speed" — partial). plan.md Mindset section | MERGE into README "Completeness Over Speed" or keep as §0 1-liner |
| P10 | Token density ≤1200 words | **Rule** | constraint/F2. base.md limits table. PROJECT_CONFIG | MOVE to conventions or REMOVE from §0. Pure engineering constraint |
| P11 | Enforcement values MUST be inline | **Rule** | D24 (Config Sync Registry). convention/F5 | MOVE to conventions or REMOVE from §0. Engineering pattern |
| P12 | DNA / Library split | **Rule** | D25. Convention/F5 (ref-inside-step) | MOVE to conventions or REMOVE from §0 |
| P13 | Progressive Disclosure | **Principle** | D25 (modular architecture). Implicit in research/{base,focused,deep}.md | REMOVE from §0. The architecture IS the principle |
| P14 | Filesystem = state machine | **Value** | philosophy/F4. conventions §4. research/ subfolder | PROMOTE to README as "Structural Enforcement". Remove from §0 after promotion |

**Summary:**
- **STAY in §0 (compact):** P1, P2, P3, P5, P7, P8, P9 (7 items)
- **REMOVE from §0:** P4, P6, P10, P11, P12, P13 (6 items)
- **PROMOTE to README:** P14 (1 item → "Structural Enforcement")

### E2: knowledge/ facts self-evidence audit

Checking each fact: "Is this now obvious from the code it describes?"

#### convention.md (12 facts)

| # | Fact (short) | Self-evident from... | Verdict |
|---|-------------|---------------------|---------|
| F1 | Adapter = byte-copy | Adapter files themselves | ⚠️ Keep — not obvious without trying |
| F2 | CRLF inconsistency | No rule exists → still relevant | Keep |
| F3 | TS descriptions can drift | General principle, not code-specific | Keep |
| F4 | Checkpoint fields in templates | templates/research/*.md | **PRUNE** — templates show this |
| F5 | Ref-inside-step pattern | plan.md, base.md demonstrate it | **PRUNE** — code IS the pattern |
| F6 | Config Sync Registry scope | config.md workflow explains it | **PRUNE** — workflow shows this |
| F7 | Adapter drift → copy-on-modify | Related to F1 | Keep (complements F1) |
| F8 | §3.1 domain-agnostic | templates/HL.md shows it | **PRUNE** — template IS the rule |
| F9 | Filesystem state machine | conventions §4, research/ subfolder | **PRUNE** — P14 + architecture show this |
| F10 | RES = synthesis | templates/RES.md structure | **PRUNE** — template IS the proof |
| F11 | HL Working Backwards | templates/HL.md §1 | Borderline — keep (template doesn't explain WHY) |
| F12 | Stage templates structure | templates/research/* | **PRUNE** — templates exist |

**Prunable convention facts: F4, F5, F6, F8, F9, F10, F12 = 7 facts**
Keep: F1, F2, F3, F7, F11 = 5 facts

#### process.md (10 facts)

| # | Fact (short) | Self-evident from... | Verdict |
|---|-------------|---------------------|---------|
| F1 | TFW = teamwork | README §Roles | Borderline — philosophical, keep |
| F2 | tfw-knowledge ≠ tfw-docs | Two separate workflows exist | **PRUNE** — file existence = documentation |
| F3 | Scan conversation for FCs | templates/RES.md, RF.md have the instruction | **PRUNE** — template says it |
| F4 | Best FCs from user emotions | Strategic insight — NOT in any code | Keep |
| F5 | Naming creates behavior | D28, philosophy — user confirmed = Value | Keep (might move to philosophy/) |
| F6 | Agents follow steps + gates | Process insight — not directly in code | Keep |
| F7 | Write to file first, then chat | Process insight — not enforced in code | Keep |
| F8 | Crash recovery / gate skipping | D31, process/F10 covers the fix | **PRUNE** — F10 (resume protocol) covers the problem + solution |
| F9 | 4 roles | conventions §15, glossary §Roles | **PRUNE** — obvious from code |
| F10 | Resume Protocol | base.md Step 0 | **PRUNE** — code IS the protocol |

**Prunable process facts: F2, F3, F8, F9, F10 = 5 facts**
Keep: F1, F4, F5, F6, F7 = 5 facts

#### philosophy.md (4 facts)

| # | Fact (short) | Self-evident? | Verdict |
|---|-------------|--------------|---------|
| F1 | Zettelkasten inspiration | Strategic origin story | Keep |
| F2 | tfw-docs vs tfw-knowledge = different systems | Overlaps with process/F2 | Keep (this is the authoritative version) |
| F3 | User wants critical opponent | Strategic — user preference | Keep |
| F4 | Structural enforcement > format enforcement | P14 + README value | Keep but compress (will be in README) |

**Prunable philosophy facts: 0** (user confirmed: philosophy = keep)

#### constraint.md (3 facts)

| # | Fact (short) | Self-evident? | Verdict |
|---|-------------|--------------|---------|
| F1 | User prefs not in shared files | Not in any code | Keep |
| F2 | Workflow degrades >1200 words | P10 + PROJECT_CONFIG | Borderline — keep (empirical finding) |
| F3 | Agents generate filler FCs | Process insight | Keep |

**Prunable constraint facts: 0**

### E3: README Values — proposed final list

Current (5 values): Candor, Completeness, Determinism/Safety, Portability, SSOT

Proposed (7 values):

| # | Value | Status | Source |
|---|-------|--------|--------|
| 1 | **Traces Over Code** | Exists (implied in thesis, not in §Values) | §Thesis |
| 2 | **Candor Over Flattery** | Exists — enrich with P9 coordinator mindset | §Values + P9 |
| 3 | **Completeness Over Speed** | Exists | §Values |
| 4 | **Structural Enforcement** | NEW — from P14, philosophy/F4 | P14 + TFW-24 |
| 5 | **Naming Creates Behavior** | NEW — from D28, process/F5, user belief | D28 + TFW-22 |
| 6 | **Single Source of Truth** | Exists | §Values |
| 7 | **Portability** | Exists | §Values |

**Dropped:** "Determinism and Safety" — fully covered by conventions §12. Not a belief, it's a rule set (don't fabricate, don't guess, use env vars). HL flagged this as merge candidate.

**Count: 7** — within the 4-8 range validated by external research.

### E4: KNOWLEDGE.md §3 Legacy pruning candidates

Current: 35 items (lines 115-148). Items where `Status = Removed/Replaced` AND the replacement is fully implemented:

Checking which items are now purely historical with no active reference value:

- Lines 115-121 (STEPS.md, TASK.md, Summary Discipline, AI_ENTRY_POINT, SUCCESS_CRITERIA, 00_meta/, Review in handoff) — all from TFW-2/4/8, pre-v3. No one references these anymore. **PRUNE all 7.**
- Lines 123-125 (inline scope budgets, version strings, hardcoded template lists) — TFW-12 era. Superseded mechanics. **PRUNE all 3.**
- Lines 127-128 (Complexity Check, status emoji rename) — TFW-14/15. Done. **PRUNE 2.**
- Lines 132-135 (Example Flow, good/bad research, inline checkpoint, duplicate anti-patterns) — TFW-21. All removed. **PRUNE 4.**
- Line 136 (Pattern B superseded) — D17→D24. Already in D24. **PRUNE 1.**
- Line 137 (Naming rules removed from plan.md) — TD-48 cleanup. **PRUNE 1.**

**Total prunable Legacy items: 18 out of 35** (~51%)
Keep: 17 recent items (TFW-22 through TFW-24)

### E5: KNOWLEDGE.md §4 Tech Stack

4 lines of content: Markdown+YAML, Git/GitHub, Claude/Cursor/Antigravity, MIT License. 
All trivially obvious from: repo files, `.tfw/adapters/`, LICENSE file, README.

**Verdict: REMOVE entire section.** (HL already proposed this.)

## Checkpoint

| Found | Remaining |
|-------|-----------|
| P1-P14 classified: 7 stay, 6 remove, 1 promote | None |
| 12 knowledge/ facts prunable (7 convention + 5 process) | Need to verify no cross-refs break |
| README Values: 7 items (drop Determinism/Safety, add 2 new) | None |
| Legacy: 18 items prunable | None |
| §4 Tech Stack: remove | None |

**Sufficiency:**
- [x] External source used? (taxonomy from Gather validates classification)
- [x] Briefing gap closed? (exact lists produced for all pruning targets)

Stage complete: YES
→ User decision: ___
