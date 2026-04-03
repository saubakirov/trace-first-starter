# RES — TFW-18: Knowledge Consolidation

> **Date**: 2026-04-03
> **Author**: Coordinator (research mode)
> **Status**: 🔬 RES — In progress
> **Parent HL**: [HL-TFW-18](HL-TFW-18__knowledge_consolidation.md)
> **Mode**: Pipeline

---

## Research Context
TFW-18 introduces three new mechanisms: Fact Candidates in every artifact, Dream-like 4-phase consolidation in tfw-docs, and a Knowledge Gate with separate lifecycle. This research investigates how similar systems work externally, validates the fact category taxonomy, and challenges the consolidation design before TS.

## Briefing

### Research Plan
1. **Gather** — study how other knowledge management systems solve fact collection + consolidation (Claude Code dream, Obsidian daily notes, Zettelkasten, personal knowledge graphs). How do they handle verification, deduplication, pruning?
2. **Extract** — analyze our existing TFW artifacts (RF, REVIEW, RES files from real tasks) to find examples of facts that WERE lost. Quantify the problem: what kinds of facts disappeared?
3. **Challenge** — test the 4-phase Dream model against TFW's constraints. Is Orient→Gather→Consolidate→Prune the right decomposition? Does the knowledge_state.yaml approach actually work for enforcement?

### Scope Intent
- **In scope:** consolidation process design, fact categories, gate mechanism, template changes
- **Out of scope:** user_preferences.md design (simple, no research needed), adapter sync mechanics (known pattern from TFW-17)

### Guiding Questions
1. Чаще бизнес и образование → категории validated
2. Docker Swarm vs K8s, backend location, Innoforce vs Avtobys → environment + context facts
3. knowledge_state.yaml коммитится в git (командная работа)

→ User direction: received, proceed to Gather

## Decisions
| # | Decision | Rationale |
|---|----------|-----------|
| R1 | TFW Fact Candidates = Zettelkasten "fleeting notes" model, NOT MemGPT "archival storage" | TFW is file-based, not DB-based. Candidates in artifacts → consolidated into KNOWLEDGE.md = fleeting → permanent |
| R2 | LangMem's 3-type model (semantic/episodic/procedural) maps to TFW: semantic = Project Facts, procedural = conventions.md, episodic = RF/RES | No need for separate episodic storage — TFW already has it in task artifacts |
| R3 | Claude Code dream's "three-gate" trigger (24h + 5 sessions + lock) → TFW uses task count + yaml tracking | TFW has no sessions/time — tasks are the unit of work |
| R4 | Topic files in `knowledge/` folder (project root), NOT inline in KNOWLEDGE.md | Claude Code pattern. KNOWLEDGE.md = 124 lines already. §5 inline would exceed agent-friendly limits |
| R5 | `/tfw-knowledge` = separate workflow, NOT tfw-docs extension | Different trigger (periodic vs per-task), different duration (10-20 min vs 2 min), different scope (batch vs single) |
| R6 | Agents only write Fact Candidates. All tracking/stats/consolidation = tfw-knowledge job | Minimize agent burden. One duty per role |
| R7 | No `pending_candidates` in yaml — seq-based check sufficient | `current_seq - last_consolidation_seq >= interval` |
| R8 | All limits configurable in PROJECT_CONFIG.yaml | User preference. Defaults: 200/30/50/8 |
| R9 | Gate mode configurable: hard (default) / soft / off | User preference. tfw-config future task will auto-propagate |
| R10 | Quality filter: "Would the next agent decide differently?" | Prevents trivial facts. Embedded in template |
| R11 | Fact Candidates mandatory in ALL artifacts (RES, RF, REVIEW) | Extract showed RES richest source but RF/REVIEW also needed |
| R12 | `.user_preferences.md` = single file, project root, gitignored. Separate future task (tfw-user-tune) | Preferences are stable, not pipeline material. Out of TFW-18 scope |

## Open Questions
| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Should consolidation auto-increment pending_candidates? | ✅ Resolved | No — seq-based check sufficient (R7) |
| Q2 | KNOWLEDGE.md §5 size limit — how many? | ✅ Resolved | Configurable. Default: 200 lines total, 30 lines §5 index (R8) |

---

## Stage: Gather — "What do we NOT know?"

### External findings

**Claude Code Dream (3-gate + 4-phase):**
- Trigger: 24h elapsed + 5 sessions + lock acquisition. Manual via `/dream`
- 4 phases: Orient (read MEMORY.md) → Gather Signal (session transcripts → extract) → Consolidate (merge, resolve contradictions, absolute dates) → Prune (≤200 lines, remove stale)
- Read-only access to project. Writes only to `memory/` directory
- `MEMORY.md` = index file (≤200 lines). Topic files = detail (`patterns.md`, `debugging.md`)
- Key insight: **prunes aggressively**. Memory is not a log — it's a working set

**Zettelkasten (fleeting → literature → permanent):**
- Fleeting notes = raw capture, no long-term value (= our Fact Candidates)
- Literature notes = extracted from sources (= our RES findings)
- Permanent notes = verified, in your own words, linked, atomic (= our KNOWLEDGE.md facts)
- KEY: verification = "can you explain it in your own words?" + "does it connect to existing notes?"
- "Permanent" ≠ "final" — permanent notes are living documents, regularly edited

**LangMem (semantic/episodic/procedural):**
- 3 memory types: Semantic (facts, preferences), Episodic (past experiences), Procedural (rules/behaviors)
- TFW mapping: Semantic = KNOWLEDGE.md §5, Episodic = RF/RES artifacts, Procedural = conventions.md
- Key insight: **hot-path + background manager**. Hot-path = agent writes facts during work. Background = manager consolidates later
- This is EXACTLY our model: agents write Fact Candidates (hot-path) → tfw-docs consolidates (background)

**MemGPT (hierarchical paging):**
- Main Context (RAM) ↔ External Context (disk). Agent autonomously pages data in/out
- Recall Storage (conversation history) + Archival Storage (persistent facts)
- Not applicable: requires DB-backed storage, too heavy for TFW's file-based model

### Checkpoint: Gather
| Found | Remaining |
|-------|-----------|
| Claude Code dream: 3-gate trigger, 200-line limit, topic files, aggressive pruning | — |
| Zettelkasten: fleeting→permanent pipeline maps perfectly to Candidates→Facts | — |
| LangMem: hot-path + background consolidation = our model exactly | — |
| MemGPT: not applicable (DB-based, wrong paradigm for TFW) | — |
| All 3 applicable systems share: **size limits** + **contradiction resolution** + **regular pruning** | — |

**Agent assessment:** Gather is sufficient. Three external models validated — TFW-18 design aligns strongly with Zettelkasten (fleeting→permanent) and LangMem (hot-path + background). One design gap found: HL doesn't mention topic files (Claude Code uses them to offload detail from the main index).
**Depth check:** 4 web searches (Claude Code dream, AI memory patterns, Zettelkasten, MemGPT/LangMem). External-heavy stage.
**Recommendation:** Close Gather. Move to Extract.
**Stage Handoff:** For Extract I plan to: analyze real TFW task artifacts to find lost facts, check if current categories match the types of facts that get lost, and look for implicit knowledge patterns in our artifacts.
→ User decision: Closed. Proceed to Extract.

## Stage: Extract — "What do we NOT see?"

Analyzed 21 RF files and 4 RES files from TFW task history.

### Findings

**E1: Facts ARE being lost.** RES-12 Decision R3 ("conventions.md = canonical definition, PROJECT_CONFIG = operational override") = convention fact. Not in KNOWLEDGE.md. Future agent won't know this distinction unless they read RES-12.

**E2: User preferences embedded in RF.** RF-11A Key Decision #1: "English throughout — matching user preference." This is a user preference baked into a task decision. No central record.

**E3: Observations ≠ Facts confirmed.** All 21 RFs contain Observations — exclusively tech debt (desync, naming, missing tests). Zero project facts. The Observations pipeline works (RF → REVIEW → TECH_DEBT.md). Facts pipeline doesn't exist.

**E4: RES files are the richest source.** RES-12 has 7 Challenge findings (implicit convention facts). RES-14 has interaction model decisions. RES findings are recorded as Decisions, but not in a reusable format (no Category, no Confidence).

**E5: KNOWLEDGE.md at 124 lines.** Adding §5 with 30+ inline facts would push to 180+ lines. Topic files justified from day one.

### Checkpoint: Extract
| Found | Remaining |
|-------|-----------|
| Facts lost between tasks (E1) — quantified with real examples | — |
| User preferences scattered in RF decisions (E2) | — |
| Observations pipeline works, Facts pipeline missing (E3) | — |
| RES = richest fact source, RF/REVIEW secondary (E4) | — |
| KNOWLEDGE.md at 124 lines — topic files needed immediately (E5) | — |

**Agent assessment:** Extract confirmed the problem with concrete examples. The gap is real and quantifiable.
**Depth check:** Scanned 21 RF files, 4 RES files, KNOWLEDGE.md structure. 1 external search (topic file scalability).
**Recommendation:** Close Extract. Move to Challenge.
→ User decision: Closed. Proceed to Challenge.

## Stage: Challenge — "What do we NOT expect?"

### C1: Limits — KNOWLEDGE.md vs topic files

Claude Code's 200-line limit exists because MEMORY.md is auto-injected at session start. TFW's KNOWLEDGE.md is loaded in Prerequisites — same constraint.

**Design: KNOWLEDGE.md §5 = compact index, topic files = detail.**

```
KNOWLEDGE.md §5:
| Category | Count | Topic File |
|----------|-------|------------|
| environment | 7 | [→](knowledge/environment.md) |
| stakeholder | 4 | [→](knowledge/stakeholders.md) |
```

**Defaults (configurable in PROJECT_CONFIG.yaml):**

| Parameter | Default | Config key |
|-----------|---------|------------|
| KNOWLEDGE.md max lines | 200 | `tfw.knowledge.max_index_lines` |
| §5 index max lines | 30 | `tfw.knowledge.max_index_facts_lines` |
| Topic file max facts | 50 | `tfw.knowledge.max_facts_per_topic` |
| Topic files max count | 8 (soft) | `tfw.knowledge.max_topic_files` |

→ User decision: Accepted. Configurable, defaults as proposed.

### C2: Quality gate — "Would the next agent decide differently?"

Filter embedded in Fact Candidates template:
- Good: "CI runs on self-hosted runner — affects timeout config"
- Bad: "project uses git", "code is in Python"
- Rule: **Record only if the next agent would make a different decision knowing this fact.**

→ User decision: Accepted.

### C3: Gate enforcement mode

**Default: hard with escape hatch** (configurable).
- `tfw.knowledge.gate_mode: hard` — skip requires justification, recorded in task board
- `tfw.knowledge.gate_mode: soft` — reminder only
- `tfw.knowledge.gate_mode: off` — no gate

Future TODO: `tfw-config` workflow to propagate yaml config changes to workflows.

→ User decision: Accepted. Configurable, default = hard.

### Checkpoint: Challenge
| Found | Remaining |
|-------|-----------|
| C1: Limits design — index + topic files, configurable defaults | — |
| C2: Quality gate — "different decision" filter | — |
| C3: Gate mode — hard/soft/off, configurable | — |

**Agent assessment:** All challenges resolved. No showstoppers. Design is sound with configurable parameters.
**Depth check:** 2 web searches (KB size limits, Claude memory structure). Applied findings to TFW context.
**Recommendation:** Close Challenge. Proceed to Final Checkpoint.
→ User decision: Closed.

---

## Final Checkpoint

| Stage | Status | Key Findings |
|-------|--------|-------------|
| Gather | ✅ | Zettelkasten (fleeting→permanent) = our model. LangMem (hot-path + background) = our model. Claude Code topic files = design gap in HL. 3-gate trigger → seq-based tracking |
| Extract | ✅ | 21 RFs analyzed — zero project facts recorded. RES richest source. KNOWLEDGE.md at 124 lines — topic files needed from start |
| Challenge | ✅ | Limits configurable (200/30/50/8 defaults). Quality filter: "different decision" rule. Gate: hard/soft/off configurable. Future TODOs: tfw-config, tfw-user-tune |

### Sufficiency Check
**Question:** Sufficient for HL finalization? Can we confidently define phases, approach, and dependencies?
**Self-check:**
- Are there unclosed Open Questions in RES? → Q1 resolved (compute at check, no pending_candidates). Q2 resolved (configurable limits).
- Did all stages produce substantive findings or were any perfunctory? → All 3 stages produced concrete findings with real examples.
- Did every stage include external research? → Gather: 4 web searches. Extract: 1 web search + 25 artifact scans. Challenge: 2 web searches.
- Is the solution proportionate to the problem scale? → Yes. Template additions (Phase A) are minimal. New workflow (Phase B) is bounded. Gate (Phase C) is configurable.
- Are phases, boundaries and dependencies clear enough to finalize HL? → Yes. Phase A (templates), Phase B (tfw-knowledge workflow + docs update), Phase C (gate + config).
**Agent assessment:** Sufficient. All major design decisions resolved. Three external models validated our approach. Two future TODOs identified (tfw-config, tfw-user-tune) but they don't block TFW-18.
→ User decision: ___

**Verdict:** Sufficient for HL finalization / Need another pass

## Closure

### Summary
Research validated TFW-18 design against three external knowledge management models (Zettelkasten, LangMem, Claude Code Dream). Key refinements: (1) topic files in `knowledge/` folder for scalability, (2) KNOWLEDGE.md §5 as compact index with configurable limits, (3) `/tfw-knowledge` as separate workflow (not tfw-docs extension), (4) all parameters configurable in PROJECT_CONFIG.yaml, (5) quality filter "Would the next agent decide differently?", (6) gate mode hard/soft/off.

### HL Update Recommendations
| # | What to update | Source |
|---|---------------|--------|
| 1 | Add `knowledge/` folder structure (index + topic files model) | Gather: Claude Code topic files pattern |
| 2 | Replace `📋 DOCS` references → `/tfw-knowledge` as separate workflow | Gather+Extract: separate lifecycle confirmed |
| 3 | Add configurable limits to PROJECT_CONFIG.yaml (knowledge section) | Challenge C1 |
| 4 | Add quality filter to Fact Candidates template | Challenge C2 |
| 5 | Make gate mode configurable (hard/soft/off) | Challenge C3 |
| 6 | Fact Candidates mandatory in ALL artifacts (RES, RF, REVIEW) | Extract E3-E4 |
| 7 | Add mindset reminders to handoff, research, review workflows | TFW-17 proven pattern |
| 8 | Add future TODOs: tfw-config, tfw-user-tune | Challenge C3, Gather discussion |
| 9 | Update Phase C scope: tfw-knowledge workflow + gate in plan.md | Full research |
| 10 | Remove pending_candidates from knowledge_state.yaml | Gather Q1 resolved |

### Next Step
Coordinator updates HL with research findings → user confirms → TS.
→ User decision: ___

## Conclusion

Research confirmed that TFW-18's design aligns with proven knowledge management patterns (Zettelkasten, LangMem, Claude Code Dream) while adapting them to TFW's file-based, role-locked, task-driven model. The most valuable finding was the **topic files pattern** (Claude Code) — without it, KNOWLEDGE.md would become unreadable within ~10 tasks. The second key finding was from artifact analysis: **21 RF files contain zero project facts** — the gap is real and measurable. The quality filter ("Would the next agent decide differently?") and configurable limits prevent the known failure mode of noise accumulation. Two future tasks emerged organically: `tfw-config` (yaml-to-workflow propagation) and `tfw-user-tune` (personal preferences pipeline).

Self-critique: Extract stage could have analyzed artifacts from other projects (family-budget, atamat) for cross-project validation. Stayed within TFW project only.

---

*RES — TFW-18: Knowledge Consolidation | 2026-04-03*

