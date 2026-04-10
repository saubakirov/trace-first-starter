# Gather — Iteration 2: "What do we NOT know?"
> Parent: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> Predecessor: [RES1](../RES__TFW-32__methodology_and_positioning.md)
> Goal: Address naming precision, visualization sections, business processes, multi-iteration enforcement.

## Findings

### G1: Naming precision — "Strategic Insight" vs "Knowledge Candidate"

**External research confirms:** Category names act as **cognitive frames** for LLMs. Specific names trigger specific model behavior, generic names trigger generic behavior.

| Category Label | LLM Behavior Pattern |
|---------------|---------------------|
| "Knowledge" | Lists facts. Focuses on breadth and coverage. Retrieval mode |
| "Strategic Insight" | Prioritizes trends, causality, risks, recommendations. Synthesis mode |
| "Fact Candidate" | Captures observations. Lists what was noticed. Reporting mode |

**Key finding:** "Knowledge" = declarative/information-oriented (WHAT is the information). "Strategic Insight" = analytical/synthesis-oriented (WHAT DOES the information MEAN for our goals). These trigger fundamentally different cognitive modes in LLMs.

**Critical problem with RES1 D2 ("Doc Candidates + Knowledge Candidates"):**
- "Knowledge Candidate" is too broad — agent behavior = dump everything that could be knowledge (generic coverage mode)
- "Doc Candidate" is similarly vague — what kind of documentation?
- RES1 chose names based on WORKFLOW ROUTING (which workflow processes this) rather than CAPTURE BEHAVIOR (what kind of thing to look for)

**D28 analysis (Naming Creates Behavior):**

| Name | What it tells the agent to LOOK FOR | Precision |
|------|-------------------------------------|-----------|
| "Fact Candidates" (current) | Observations, patterns, anything noteworthy | Medium — too broad |
| "Doc Candidates" (RES1) | Things about documentation? about the project? | Low — unclear target |
| "Knowledge Candidates" (RES1) | Anything that could be knowledge | Very Low — maximally vague |
| "Strategic Insights" (current HL §11) | Business context, stakeholder priorities, domain knowledge, decisions, motives | High — specific target |
| "Observations" (RF §5, already exists) | Technical patterns, tech debt, code quality issues | High — specific target |

**I notice:** TFW already HAS the precise names. They're just in different sections:
- RF §5 **Observations** = operational/technical findings (agent-observed, internal)
- HL §11 **Strategic Session Insights** = domain/stakeholder knowledge (human-sourced, external)
- RF §6 / RES §FC **Fact Candidates** = catch-all for everything else

The problem isn't naming §11 — it's that §6 "Fact Candidates" is the vague one. "Strategic Insights" is already precise.

### G2: Visualization/Diagrams — where they live in other frameworks

**arc42 model (12-section architecture documentation):**

| Diagram Type | arc42 Section | TFW Equivalent |
|-------------|---------------|----------------|
| System Context | §3 Context & Scope | **HL §3.1** (vision-level) |
| Container/Component | §5 Building Block View | **RF** (detailed result) |
| Runtime/Dynamic | §6 Runtime View | **RF** (sequence diagrams, API flows) |
| Deployment | §7 Deployment View | **RF** (infrastructure result) |

**Pattern observed:** arc42 has diagrams in EVERY section, not one central place. But each diagram has a CLEAR PURPOSE at that level:
- Vision/Context diagrams → planning artifacts (HL equivalent)
- Detail/Runtime diagrams → result artifacts (RF equivalent)
- Architecture Decision diagrams → ADR section (KNOWLEDGE equivalent)

**C4 model hierarchy:** Context → Containers → Components → Code. Each level has its own diagram. Maps to TFW: HL = Context level, RF = Container/Component level.

**Key insight from external research:** "Pragmatism — only document what is necessary. Only add diagrams when they provide more value than text."

**Current TFW state:**
- HL §3.1 "Result Visualization" — EXISTS but is too narrow. Instructions say "show the outcome" (only one purpose)
- RF — NO visualization section. All diagrams are ad-hoc, embedded wherever
- RES — NO visualization section
- TS — NO visualization section (but TS shouldn't need one — it references HL §3.1)

### G3: Business processes — how to represent value delivery flows

**BPMN + Value Stream Mapping in agile:**
- **Two levels** confirmed by external research:
  - High-level: Value Stream Map = flow from request → delivery of value (who, what, when). Used in PLANNING
  - Detail-level: BPMN process diagram = exact steps, decisions, API calls, DB operations. Used in RESULT documentation
- "Keep documentation Just Enough and Iterative" — start with high-level in planning, add detail in execution
- "Focus on handoff points (seams)" — where work moves between teams/systems
- "Living artifacts" — diagrams update as process evolves

**User input analysis (from briefing + HL S15):**
1. "Бизнес процесс — как некий флоу от юзера и до получения ценности или результата"
2. "ИИ рисует аски арт или диаграмму последовательностей — там видно процесс, и понимает ли ИИ где его конец, где достигается ценность"
3. "Нам надо завести раздел со схемами — для дизайна/вижна, для бизнес процессов, для диаграмм"
4. "Везде должно быть одна общая глава с одним четким названием, которая на стадии знаний будет куда-то собираться"

**I notice a tension:** User wants ONE chapter name across all artifacts, but the PURPOSE of diagrams differs by artifact:
- HL: "what it SHOULD look like" (vision)
- RF: "what it ACTUALLY looks like" (result)
- RES: "what we DISCOVERED" (findings visualization)

The content differs. But the CONSOLIDATION target is the same: during 📚 KNW, all diagrams from all artifacts should be collectable into one place in knowledge.

### G4: Multi-iteration research — structural enforcement design

**External research confirms:**
- "Checkpoint-Resume Pattern" = define critical moments, save state, resume from last known good state
- "CLAUDE.md Pattern" = structured config/log file read at session start
- The key is **externalized workspace memory** — files that both agents and humans can inspect/edit
- "Aggressive Summarization" — store summaries, not raw history

**VLM-3 actual experience (4 iterations):**
- User ran 4 separate research sessions
- Each produced findings that changed assumptions from previous sessions  
- No control file existed — user mentally tracked what was covered
- This worked because user was actively involved, but would FAIL for delegated teams

**THIS session (iteration 2) — what actually happened:**
1. User read RES1, identified gaps and new insights
2. User came to new agent with: list of gaps, reference to RES1, explicit "create research2"
3. I (researcher) had to re-read: HL, RES1, all 4 stage files from research/, conventions, templates
4. Total context loading: ~8 files, ~60K characters
5. What was MISSING that would have helped: a structured summary of "what was covered, what was NOT covered, what changed during RES1"

**What the researcher SHOULD output at the end (structural enforcement):**

```
## Iteration Status
- Iteration: 1 of {min}
- Hypotheses tested: H1, H2, H3, H5, H8
- Hypotheses remaining: H6 (deferred), H7 (designed not tested)
- New hypotheses generated: none
- Gaps discovered: [list]
- Recommendation: Run iteration 2 focusing on [gaps + new hypotheses]
→ Launch next `/tfw-research` in a separate agent. Pass this file as context.
```

**Coordinator gate in plan.md:**
- After RES: coordinator checks iterations.yaml
- If `current_iteration < min_iterations` → MUST launch next research
- If `current_iteration >= min_iterations` → coordinator CAN proceed to TS, OR launch more
- Coordinator CANNOT skip to TS while iterations remain

## Checkpoint

| Found | Remaining |
|-------|-----------|
| "Strategic Insight" is ALREADY the precise name — D28 validates it | Design: what to do with §6 "Fact Candidates" vagueness |
| arc42/C4 confirm: diagrams at EVERY level, not one place | Design: exact section name, format, consolidation path |
| BPM confirms two levels: vision (HL) + detail (RF) | Design: section template for each artifact |
| Multi-iteration: structural enforcement needed, checkpoint-resume pattern | Design: exact format of iterations.yaml + researcher exit message |
| "Knowledge Candidate" triggers generic retrieval mode in LLMs | → Keep "Strategic Insight", don't rename to "Knowledge" |

**Sufficiency:**
- [x] External source used? (AI naming research, arc42, C4, BPMN, VSM, checkpoint-resume patterns)
- [x] Briefing gap closed? (all 4 hypotheses investigated)

**Deep mode criteria:**
- [x] Hypothesis tested? H5b (naming: "Strategic" > "Knowledge" — confirmed), H6 (visualization: arc42 model gives concrete placement), H6b (business processes: two-level pattern), H7b revised (structural enforcement with checkpoint-resume)
- [x] Counter-evidence sought? For H5b: sought reasons why "Knowledge Candidate" could work (it doesn't — triggers wrong LLM behavior). For H6: sought argument that ONE central section is enough (arc42 says no — each level needs its own).

**Metacognitive check:** I discovered something NEW — the existing TFW naming is ALREADY right. §5 Observations = operational (precise), §11 Strategic Insights = domain (precise), §6 Fact Candidates = the vague one that needs fixing. RES1 went wrong by trying to rename the precise names (Strategic → Knowledge) instead of fixing the vague one (Fact Candidates).

Stage complete: YES
→ User decision: ___
