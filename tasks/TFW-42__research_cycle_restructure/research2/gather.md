# Gather — "What do we NOT know?" (Iteration 2)
> Parent: [HL-TFW-42](../../HL-TFW-42__research_cycle_restructure.md)
> Goal: Map agent capabilities for research subtasks and formalize how TFW guides coordinators in agent selection.

## Dimensions

| Dimension | Alt A | Alt B | Alt C |
|-----------|-------|-------|-------|
| D1: Guidance specificity | Generic archetypes (Web Researcher / Code Auditor / Infra Operator) | Tool-specific recommendations (Claude Code for X, Codex for Y) | Capability-based (needs web search? → tool with web search) |
| D2: Guidance location | Comment in iterations.yaml template | Table in conventions.md (reference) | Prompt in plan.md Step 6b (workflow) |
| D3: Decision model | Human decides, no recommendation | Human decides, framework provides decision table | Framework suggests based on focus keywords |

## Findings

### G1: AI coding tool capability matrix (external research, 4 web searches)

Built from external research on 5 major tool categories:

| Capability | Antigravity | Claude Code | Codex CLI | Cursor | Aider |
|-----------|-------------|-------------|-----------|--------|-------|
| **Web search** | ✅ Native (Google) | ✅ Native WebSearch/WebFetch + MCP | ❌ Sandboxed (no internet) | ⚠️ Limited (doc lookup) | ❌ None |
| **MCP integration** | ✅ Full (Google Sheets, ClickHouse, etc.) | ✅ Full (extensible) | ❌ None | ⚠️ Partial | ❌ None |
| **Context window** | ~1M tokens (Gemini) | 200K standard, ~1M preview | ~128K (o3/o4-mini) | Varies by model | Varies |
| **File traversal** | ✅ Project-wide | ✅ Project-wide | ✅ Sandboxed clone | ✅ IDE-native | ✅ Git-aware |
| **Shell commands** | ✅ Via run_command | ✅ Native terminal | ✅ Sandboxed | ⚠️ Integrated terminal | ✅ Native |
| **Browser automation** | ✅ Built-in | ❌ Via MCP only | ❌ None | ❌ None | ❌ None |
| **Multi-file editing** | ✅ Structured tools | ✅ Native | ✅ Native | ✅ Composer mode | ✅ Native |
| **Image generation** | ✅ Built-in | ❌ None | ❌ None | ❌ None | ❌ None |
| **Parallel agents** | ✅ Agent Manager | ❌ Sequential | ✅ Background tasks | ❌ Sequential | ❌ Sequential |
| **Async (fire-and-forget)** | ❌ Interactive | ❌ Interactive | ✅ Cloud sandbox, PR output | ❌ Interactive | ❌ Interactive |

### G2: Research subtask type mapping

What kinds of work happen within TFW research iterations? Mapped from AFD-2 + TFW-42 iter 1:

| Research subtask | Description | Key capability needed |
|-----------------|-------------|----------------------|
| **Web research** | Searching external sources, documentation, best practices | Web search, large context for synthesis |
| **Code audit** | Analyzing existing codebase structure, dependencies, patterns | File traversal, shell commands, fast navigation |
| **Architecture synthesis** | Designing systems from gathered findings | Large context window, multi-source integration |
| **Infra reconnaissance** | Querying live servers, databases, APIs | MCP integration, shell access, interactive sessions |
| **Competitive analysis** | Comparing external tools, frameworks, approaches | Web search, structured comparison |
| **Data analysis** | Querying databases, analyzing datasets | MCP (ClickHouse, PostgreSQL), data tools |
| **Document review** | Reading and synthesizing existing project artifacts | File traversal, large context |
| **Prototype validation** | Building small proofs-of-concept | Shell commands, file editing, test execution |

### G3: Subtask-to-tool mapping (combining G1 + G2)

| Research subtask | Best-fit tools | Why |
|-----------------|---------------|-----|
| Web research | Antigravity, Claude Code | Both have native web search. Antigravity has larger context for synthesis |
| Code audit | Codex CLI, Claude Code, Cursor | Fast file traversal + shell. Codex excels at autonomous code analysis |
| Architecture synthesis | Antigravity, Claude Code | Large context needed. Antigravity edge: ~1M tokens |
| Infra reconnaissance | Claude Code, Antigravity | MCP integration for live server access. Claude Code = terminal-native |
| Competitive analysis | Antigravity, Claude Code | Web search + structured output |
| Data analysis | Antigravity, Claude Code | MCP servers (ClickHouse, PostgreSQL). Antigravity has Google Sheets MCP |
| Document review | Any tool | All can read files. Context window matters for large doc sets |
| Prototype validation | Codex CLI, Claude Code, Cursor | Shell commands + test execution. Codex = async background |

**Key observation:** No tool is universally best. The choice depends on the iteration's PRIMARY subtask type. Most iterations involve 2-3 subtask types — the coordinator picks based on the dominant one.

### G4: Where should guidance live? Analysis of TFW locations

| Location | Pros | Cons | Maintenance burden |
|----------|------|------|-------------------|
| **Comment in iterations.yaml template** | Visible at decision point. No extra file to read. | Limited space. Can't include full table. | Low — update template only |
| **Table in conventions.md** | Authoritative reference. Full detail. | Not visible at decision point. Coordinator must remember to check. | Medium — update when tools evolve |
| **Prompt in plan.md Step 6b** | Active guidance. Forces coordinator to consider. | Adds workflow weight. May feel prescriptive. | Medium — update workflow |
| **Separate reference doc** | Full space for detailed guidance. | New file to maintain. Low discoverability. | High — easily forgotten |

### G5: Tool-agnostic vs tool-specific guidance tension

**TFW's core principle:** tool-agnostic (`.tfw/` works with any AI tool). Naming specific tools (Claude Code, Codex CLI) would:
- Break tool-agnosticism
- Become stale as tools evolve (new tools appear, old tools gain capabilities)
- Bind TFW to a specific ecosystem

**Counter-argument:** Generic archetypes ("Web Researcher") are too vague. Coordinators need concrete examples to act.

**Resolution pattern found:** Use a two-tier approach:
1. **Conventions** define CAPABILITY CATEGORIES (tool-agnostic): "web search", "code audit", "MCP integration"
2. **Project-level config or KNOWLEDGE.md** maps capabilities to SPECIFIC TOOLS (project-specific): "Antigravity = web search + MCP + large context"

This mirrors how TFW handles other tool-specific data (e.g., `project_config.yaml` has build commands, not tool names in conventions).

### G6: Counter-evidence — does agent guidance add value? (deep mode)

**Scenario: experienced coordinator.** Already knows which tool to use. Guidance = noise.
- AFD-2 coordinator chose agents intuitively based on experience. No guidance framework needed.
- Counter: guidance helps NEW coordinators or multi-person teams where not everyone knows all tools.

**Scenario: single-tool user.** Has only Claude Code. Guidance about tool selection = irrelevant.
- This is the MAJORITY case for most TFW users.
- Counter: guidance still serves as inspiration ("maybe I should try another tool for this iteration").

**Verdict:** Guidance should be LIGHT and OPTIONAL. A brief comment in the template + a reference to a capability table. Never prescriptive, never required.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| 5-tool capability matrix with 10 capabilities each | None |
| 8 research subtask types mapped to best-fit tools | None |
| 4 guidance locations analyzed with pros/cons | None |
| Tool-agnostic resolution: capability categories + project-level mapping | None |

**Sufficiency:**
- [x] External source used? (4 web searches on tool capabilities)
- [x] Briefing gap closed? (capability mapping + formalization location answered)
- [x] Dimensions identified? (3 dimensions × 3 alternatives)

**Deep mode criteria:**
- [x] Hypothesis tested? (H1 extended: agent field works, guidance formalization explored)
- [x] Counter-evidence sought? (G6: experienced coordinator, single-tool user)

**Metacognitive check:** NEW discovery — the two-tier resolution (capability categories in conventions vs specific tools in project config). This preserves TFW's tool-agnosticism while giving concrete guidance. Also discovered that research subtask types map cleanly to tool capabilities, making the guidance table actionable.

Stage complete: YES
→ User decision: proceed (autonomous mode)
