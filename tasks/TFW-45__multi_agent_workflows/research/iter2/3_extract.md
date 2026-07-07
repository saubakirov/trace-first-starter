# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-45](../../HL-TFW-45__multi_agent_workflows.md)
> Goal: Map the design space for swarm execution model and surface hidden combinations.

## Configuration Space

Cross-referencing D2 (mode model) × D4 (backward compatibility) — the two highest-impact design axes. D1 (injection level) and D3 (info passing) are resolved: system prompt for injection, full stage files for passing.

| Config | D2: Mode model | D4: Backward compat | Swarm × focused/deep interaction | Implementation complexity | Notes |
|--------|---------------|---------------------|--------------------------------|--------------------------|-------|
| S1 | Third mode (`swarm.md`) | Hard — C9 preserved | Swarm replaces focused/deep selection | Low | **Simplest but incorrect.** Swarm is not about investigation depth. A swarm agent STILL needs to know: focused or deep? |
| S2 | Orthogonal axis: `execution_model: single \| multi` in config | Hard — single is default | `execution_model × mode` = 4 combos. Config selects both independently | Medium | **Correct modeling.** Two independent axes. Default: `single + focused`. Opt-in: `multi + deep` |
| S3 | Orthogonal axis with auto-detection | Soft — auto-detect platform capability | If platform has `define_subagent` → multi, else → single. Mode still separate | Medium | **Smart default.** No user choice for execution model — platform decides. User still picks mode |
| S4 | Multi-agent by default, no fallback | Break allowed | All stages spawn sub-agents. Single-agent platforms can't run it | Low | **Aggressive.** User said "willing to break." But H1 unvalidated — breaking compat on unproven hypothesis is reckless |
| S5 | Orthogonal axis + workflow-level override | Hard — single default, per-workflow override | `research.execution_model: multi` in project_config.yaml. Review can stay single | Medium | **Granular.** Research can be multi while review stays single until Phase B |
| S6 | No config — workflow command decides | Soft | `/tfw-research --swarm` flag or separate `/tfw-research-swarm` command | Low | **User's option (a).** Separate commands. No config change needed. Clean separation |

## Findings

### E1: S1 is structurally wrong — swarm ≠ mode

S1 (third mode) conflates two independent axes:
- `focused/deep` = investigation DEPTH (how many OODA loops, require counter-evidence?)
- `single/multi` = execution MODEL (one agent or many?)

A swarm Gather agent still needs to know: run 1 OODA loop (focused) or up to 3 (deep)? If `swarm.md` replaces `focused.md`/`deep.md`, this information is lost. You'd need `swarm-focused.md` and `swarm-deep.md` — which proves they're independent axes.

**S1 eliminated.**

### E2: S4 is premature — breaking compat on unproven H1

User said "willing to break backward compatibility IF genuinely better." But H1 is unvalidated. Making multi-agent default before empirical proof = building on assumption. Industry pattern: "start single-agent, opt-in to multi when proven."

Also: Codex and Claude Code users who DON'T have reliable sub-agent spawn would be locked out.

**S4 eliminated.**

### E3: S3 (auto-detection) — hidden smart combination

Nobody proposed auto-detection in the Briefing or HL. The insight: TFW already knows what platform it's running on (via adapter layer). If the adapter reports `has_subagent_spawn: true`, the workflow automatically uses multi-agent execution. Users on platforms without spawn get single-agent transparently.

**Problem:** This removes user choice. Maybe user WANTS single-agent on a platform that supports multi. Maybe for a quick check (focused mode), spawning 4 agents is overkill.

**Refinement → S3':** Auto-detection sets the DEFAULT, user can override. `execution_model: auto | single | multi` in project_config.yaml. `auto` checks platform capability.

### E4: S6 (command-level) vs S2/S5 (config-level)

User suggested "separate commands." Let me compare:

| Aspect | S6 (command-level) | S2/S5 (config-level) |
|--------|-------------------|---------------------|
| User experience | `/tfw-research --swarm` or `/tfw-research-swarm` | Set once in config, all research runs multi |
| Per-run flexibility | ✅ Every run chooses | ❌ Need to change config |
| Config complexity | Zero | One new key in project_config.yaml |
| Discoverability | User must know the flag exists | Config documents the option |
| Workflow file changes | Workflow checks flag | Workflow reads config |

**S6 is cleaner for experimentation** (user can try swarm once without committing). **S5 is cleaner for production** (set and forget).

**Hidden combination S7:** Both. Config sets default, command flag overrides. `execution_model: auto` in config. `/tfw-research --single` overrides to force single-agent. Or `/tfw-research --multi` forces multi even when config says single.

### E5: What swarm.md actually contains — content sketch

Given that swarm is an execution model (not a mode), what does the protocol file contain?

```
# Swarm Execution Protocol

## When to use
- Platform supports sub-agent spawn (auto-detected or configured)
- Mode: any (focused or deep — orthogonal)

## Stage Agent Composition
For each stage (Gather, Extract, Challenge):
1. System prompt = Mindset block (from stage template) + TFW context loading instruction
2. Input = predecessor stage files (full, not summarized)
3. Output = completed stage file
4. Tools = read-only by default, write for stage file only

## System Prompt Template
> You are {role_noun}. {mindset_test}.
> First action: read `AGENTS.md`, then `.tfw/conventions.md`.
> Your task: {stage_description}.
> Input files: {list of predecessor files to read}.
> Output: write {stage_file_name} in {directory}.
> Mode: {focused|deep} — {mode_parameters}.

## Information Flow
Briefing → [coordinator writes]
Gather → [sub-agent: Explorer]
  receives: 1_briefing.md
  produces: 2_gather.md
Extract → [sub-agent: Analyst]
  receives: 1_briefing.md + 2_gather.md
  produces: 3_extract.md
Challenge → [sub-agent: Critic]
  receives: 1_briefing.md + 2_gather.md + 3_extract.md
  produces: 4_challenge.md
RES → [coordinator writes — synthesizes all stage files]
```

**Key design decision:** Coordinator (parent agent) writes Briefing and RES. Sub-agents write Gather/Extract/Challenge. This is because:
- Briefing requires USER INTERACTION (guiding questions → user answers). Sub-agent can't interact with user
- RES requires SYNTHESIS across all stages. Coordinator sees all output
- Gather/Extract/Challenge are the COGNITIVE WORK stages where fresh Mindset matters

### E6: Briefing stage — special treatment needed

Briefing has a fundamental difference from Gather/Extract/Challenge:
- It requires USER INPUT (guiding questions → wait → record answers)
- Sub-agents in Antigravity communicate via `send_message`, not direct user chat
- The coordinator IS already the Strategist (planning the investigation)

**Conclusion:** Briefing should NOT be spawned as a sub-agent. The coordinator (parent agent) writes the Briefing directly, as it does today. Only Gather/Extract/Challenge get spawned.

This also means: only 3 sub-agents per research iteration, not 4. Simpler.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| S1 eliminated (swarm ≠ mode) | |
| S4 eliminated (premature compat break) | |
| S3' (auto-detect + user override) = smart default | Whether auto-detect is implementable per adapter |
| S7 (config default + command override) = best combo | Exact config key name and values |
| Swarm protocol content sketched | Template wording for system_prompt |
| Briefing stays with coordinator, only 3 stages spawn | |
| Swarm × mode is independent (2 axes confirmed) | |

**Sufficiency:**
- [x] External source used? (Building on 5 web searches from Gather)
- [x] Briefing gap closed? (Design space mapped, H8 resolved)
- [x] Configuration Space built from Gather dimensions? (7 configs, 2 eliminated, 1 hidden combo)
- [x] Hypothesis tested? (H8 resolved: swarm = execution model, orthogonal to mode)
- [x] Counter-evidence sought? (S4 premature, S3 removes user choice → S3' fixes)
- [x] Metacognitive check: S7 (config + command override) and S3' (auto-detect with override) = combinations nobody proposed ✅

Stage complete: YES
→ User decision: ___
