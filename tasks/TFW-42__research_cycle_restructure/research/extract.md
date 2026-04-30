# Extract — "What do we NOT see?"
> Parent: [HL-TFW-42](../../HL-TFW-42__research_cycle_restructure.md)
> Goal: Determine how TFW should present multi-agent research orchestration to users via iterations.yaml.

## Configuration Space

Reduced from 64 theoretical to 12 meaningful configurations by eliminating obviously contradictory combinations (e.g., "no agent field" + "active suggestion to assign agents").

| Config | D1: Agent specification | D2: Iteration dependency | D3: Framework guidance |
|--------|------------------------|-------------------------|----------------------|
| C1 | Free-text name | Linear chain | Document-only |
| C2 | Free-text name | Linear chain | Prompt-in-template |
| C3 | Free-text name | Linear chain | Active suggestion |
| C4 | Free-text name | DAG | Active suggestion |
| C5 | Structured profile | Linear chain | Active suggestion |
| C6 | Structured profile | DAG | Active suggestion |
| C7 | Enum from registry | Linear chain | Active suggestion |
| C8 | Enum from registry | DAG | Active suggestion |
| C9 | No agent field | Implicit (sequential) | Document-only |
| C10 | Free-text name | None (sequential by number) | Prompt-in-template |
| C11 | Free-text name | Implicit | Prompt-in-template |
| C12 | No agent field | None (sequential) | Document-only |

## Findings

### E1: Mapping AFD-2 empirical patterns to configurations

AFD-2 actually used: free-text agent names, implicit sequential dependencies (each iteration read predecessor RES), and no framework guidance (coordinator chose agents intuitively).

This maps to **C11** (Free-text name + Implicit dependency + Prompt-in-template). However, AFD-2 was a pioneer — it had no template guidance because the feature didn't exist yet. The question is what the framework SHOULD provide, not what AFD-2 used.

**Actual AFD-2 dependency patterns:**
- iter 1→2: Agent switch (Antigravity→Codex). Codex needed iter 1's architecture analysis to know what to audit.
- iter 2→3: Same agent continuation (Codex→Codex). Deeper dive into same domain.
- iter 3→4: Agent switch (Codex→Antigravity). Code audit findings fed architecture synthesis.
- iter 4→5: Agent switch (Antigravity→Claude Code). Architecture design needed infra validation.
- iter 5→6: Agent switch (Claude Code→Antigravity). Infra facts fed domain modeling.
- iter 6→7→8: Same agent continuation (Antigravity×3). Progressive synthesis.

**Observation:** Dependencies were ALWAYS linear (each iteration depended on predecessor). No DAG patterns observed. Even when agent switches happened, the dependency was "read previous RES" — not "read specific iterations."

### E2: Configuration complexity vs TFW philosophy analysis

TFW principle F4 (structural enforcement): the structure should make the right thing easy and the wrong thing hard.

| Config | Complexity | Aligns with TFW? | Risk |
|--------|-----------|-------------------|------|
| C1 | Low | ✅ Simple, optional | Agent field unused by most projects |
| C2 | Low | ✅ Template nudges without forcing | Best balance — guidance without overhead |
| C3 | Medium | ⚠️ Active suggestion may feel prescriptive | Coordinator prompted even when single-agent |
| C4 | Medium-High | ❌ DAG adds complexity for unproven pattern | No empirical evidence for DAG dependencies |
| C5 | High | ❌ Structured profiles = agent definition (not TFW's job) | Over-engineering: TFW doesn't own agent capabilities |
| C6 | Very High | ❌ Structured + DAG = framework bloat | Maximum complexity, minimum proven value |
| C7 | Medium | ❌ Registry requires maintenance, fails on new agents | Brittle: new agents require framework update |
| C8 | High | ❌ Registry + DAG = maximum coupling | Both dimensions are over-engineered |
| C9 | Minimal | ✅ Status quo (works for single-agent) | Misses multi-agent entirely |
| C10 | Low | ✅ Simple, explicit sequential | `depends_on` adds no value over sequential numbering |
| C11 | Low | ✅ Template guides, implicit deps | Clean but no `depends_on` for future flexibility |
| C12 | Minimal | ✅ Pure simplicity | Same as C9 — ignores the feature request |

### E3: Cross-framework comparison — what level of specification works

| Framework | Agent spec complexity | Works for them? | Why |
|-----------|----------------------|-----------------|-----|
| CrewAI | High (role + goal + backstory + delegation flag) | Yes | They need agent DEFINITION — agents are LLM instances |
| AutoGen | Medium (name + description) | Yes | Description drives automated selection |
| LangGraph | N/A (code, not config) | Yes | Agents = functions, no config needed |
| MetaGPT | Medium (role → LLM mapping) | Yes | Different models per role |
| **TFW** | **Low (name only)** | **Yes** | **Agents = external tools, not LLM instances. No definition needed** |

**Key finding:** TFW's minimal specification is correct BECAUSE TFW agents are external tools (IDE-level systems), not LLM instances. The coordinator already knows which tool to use — the framework just needs to record the choice for traceability.

### E4: The "brief" field analysis — redundancy with "focus"

HL-TFW-42 proposes both `focus` and `brief` fields in iterations.yaml:
- `focus`: research direction (exists today)
- `brief`: iteration briefing text (proposed new)

**Analysis:** These overlap. The `focus` field already serves as a brief. In AFD-2, the `focus` field contained multi-line descriptions that functioned as briefs. Adding a separate `brief` field creates redundancy.

**Options:**
1. Keep both — `focus` = one-line summary, `brief` = detailed briefing
2. Drop `brief` — `focus` already serves this purpose (YAML multiline support)
3. Rename `focus` → `brief` — better naming, single field

Option 2 is cleanest: `focus` already uses YAML `>` for multiline content (seen in TFW-42's own iterations.yaml). No new field needed.

### E5: The "sources" field analysis — value vs overhead

HL-TFW-42 proposes `sources: [external, afd-2_experience, tool_documentation]`.

**Analysis:** This field records expected research sources. In practice:
- The briefing.md already captures research plan (sources are implicit in the plan)
- The gather.md findings section records actual sources used
- Adding `sources` to iterations.yaml duplicates information that lives in stage files

**However:** `sources` in iterations.yaml serves a DIFFERENT purpose — it's a planning hint, not a record. It tells the researcher WHAT KINDS of sources to prioritize before they start. This is useful for multi-agent handoff: "this iteration needs external web research" vs "this iteration needs code-level analysis."

**Decision: keep `sources` as optional field.** It adds value for multi-agent cases (signals research approach) without creating mandatory overhead.

### E6: The "notes" field analysis

HL-TFW-42 proposes `notes` field. This is a free-text catch-all.

**Analysis:** Catch-all fields tend to accumulate noise. Better to have specific optional fields (`agent`, `sources`, `depends_on`) that each serve a clear purpose. A generic `notes` field doesn't pass the "Would the next agent decide differently?" test.

**Decision: drop `notes` field.** If coordinator has something to say, `focus` already supports multiline text.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| 12 configurations mapped, clear complexity gradient visible | None |
| AFD-2 dependencies are purely linear — no DAG evidence | None |
| TFW's agent spec should be minimal (name only) — validated against 4 frameworks | None |
| `brief` and `notes` fields are redundant — `focus` already serves both purposes | None |
| `sources` field has unique value for multi-agent handoff | None |

**Sufficiency:**
- [x] External source used? (Cross-framework comparison table)
- [x] Briefing gap closed? (H1 evidence: iterations.yaml agent field + optional enrichment = sufficient)
- [x] Configuration Space built from Gather dimensions? (12 configs from 3 dimensions)

**Deep mode criteria:**
- [x] Hypothesis tested? (H1 tested via configuration analysis — C2 emerges as likely winner)
- [x] Counter-evidence sought? (E4: brief field redundancy, E5: sources redundancy analysis, E6: notes field noise risk)

**Metacognitive check:** NEW discovery — `brief` and `notes` fields are redundant with existing `focus` field. This simplifies the proposed schema from 5 new fields to 3 (`agent`, `sources`, `depends_on`). Also confirmed that iteration dependencies are purely linear in practice — DAG is over-engineering.

Stage complete: YES
→ User decision: proceed (autonomous mode)
