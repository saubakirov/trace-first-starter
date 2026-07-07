# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW-45](../../HL-TFW-45__multi_agent_workflows.md)
> Goal: Stress-test surviving configurations and expose failure modes in the swarm execution model.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D2: Orthogonal axis | execution_model config | D4: Break allowed | No fallback | If execution_model exists in config, it implies single IS an option. "No fallback" contradicts having a config switch |
| D2: Third mode (S1) | swarm.md replaces focused/deep | D2: Orthogonal axis | swarm × mode | Cannot be both a mode replacement AND orthogonal to modes. Mutually exclusive designs |
| D3: Predecessor RES only | Minimal transfer | Stage dependencies | Extract needs Gather Dimensions | Extract can't build Configuration Space without Gather's Dimensions table. RES-only transfer = insufficient |

**Surviving configurations:**

| Config | Mode model | Backward compat | Interaction | Notes |
|--------|-----------|-----------------|-------------|-------|
| S2 ✅ | Orthogonal: `execution_model: single\|multi` | Hard — single default | Config-level | Clean but rigid — can't try swarm once without config change |
| S3' ✅ | Orthogonal + auto-detect | Soft — platform decides default | Config with smart default | Auto sets default, user overrides |
| S5 ✅ | Orthogonal + per-workflow override | Hard — single default per workflow | Config with workflow granularity | Research=multi, Review=single until Phase B |
| S6 ✅ | Command-level | Soft — user chooses per run | Flag or separate command | Clean for experimentation |
| S7 ✅ | Config default + command override | Both | Config + flag | Most flexible but most complex |

## Findings

### C1: Attack on H1 — "What if system-prompt persona is ALSO simulation?"

**Attack:** H1 claims fresh agent with Mindset-as-system-prompt produces "more genuine" output. But what does "genuine" mean? The model is ALWAYS simulating — whether the role is in system prompt or conversation. There's no "real" Explorer inside the model. System prompt just makes the simulation MORE PERSISTENT, not more real.

**Defense:** The claim isn't about "genuine identity" — it's about **eliminating anchoring bias**. Even if both are simulation, the fresh agent doesn't carry cognitive baggage from Gather when doing Extract. The value is in ISOLATION, not in "authenticity." The system-prompt placement ensures the persona can't be overridden by conversation drift.

**Counter-counter:** What if the Analyst agent, receiving Gather's file as input, anchors to the Gather findings ANYWAY — just via the file instead of via conversation history? The anchoring source changes (file vs memory) but the anchoring itself remains.

**Resolution:** The file-based anchoring is WEAKER than conversation-based anchoring:
1. File = structured output (Dimensions table, Findings) — easier to read critically than raw conversation
2. Conversation = includes the REASONING PATH (why Gatherer chose X over Y) — this creates stronger anchoring because the agent "lived through" the reasoning
3. File = finite, bounded input. Conversation = grows unboundedly, with middle information lost ("Lost in the Middle")

**Verdict:** H1 is structurally justified. Fresh agent + file input ≠ single agent + conversation history. The anchoring is weaker, even if not eliminated. **This is sufficient for a design decision, with empirical validation planned.**

### C2: Attack on "Briefing stays with coordinator"

**Attack:** If the whole point of swarm is fresh Mindset per stage, why does Briefing get special treatment? The Strategist Mindset is just as important as Explorer/Analyst/Critic.

**Defense (structural):** Briefing has a UNIQUE constraint — it requires user interaction:
1. Strategist proposes guiding questions
2. 🛑 STOP — wait for user
3. User answers are recorded in Briefing file

Sub-agents in Antigravity communicate via `send_message`, not direct user chat. The coordinator IS the user-facing agent. Spawning a Briefing sub-agent would require the coordinator to relay user messages back and forth — adding complexity for no cognitive benefit (the coordinator isn't "contaminated" yet, it's the start of research).

**Counter:** In Claude Code Agent Teams, agents CAN interact with users. Platform-specific behavior.

**Resolution:** For TFW-45 (first implementation), Briefing stays with coordinator. This is the simpler, safer design. If empirical testing shows Briefing benefits from isolation, it can be moved to a sub-agent in a future task. The protocol allows this — `swarm.md` can define Briefing as coordinator-owned or spawned.

**Verdict:** Briefing with coordinator is correct for now. Not a permanent constraint.

### C3: Attack on S3' (auto-detection) — "How does adapter report capability?"

**Attack:** S3' assumes the adapter can report `has_subagent_spawn: true`. But how? Current adapter structure is just `.agent/rules/` and `.agent/workflows/`. There's no capability reporting mechanism.

**Defense:** The research workflow ITSELF can detect capability:
- Antigravity: check if `define_subagent` tool exists (the workflow can reference tool availability)
- Claude Code: check if `.claude/agents/` directory exists
- Codex: check if `.codex/agents/` directory exists

This is runtime detection, not config declaration. The workflow file says: "IF you have `define_subagent` available AND `execution_model != single`, spawn sub-agents."

**Problem:** This makes `swarm.md` platform-aware — it needs to know about `define_subagent`. But iter1 D3 said swarm.md should be platform-agnostic.

**Resolution:** The detection logic lives in the WORKFLOW (`research/base.md`), not in `swarm.md`. The workflow checks execution_model config + platform capability. `swarm.md` just describes the PROTOCOL (who gets what Mindset, what input, what output). The workflow translates protocol → platform spawn.

**Verdict:** S3' is viable. Detection in workflow, protocol in swarm.md. Clean separation.

### C4: Attack on orthogonality — "Does swarm × focused make sense?"

**Attack:** Swarm × focused = spawn 3 sub-agents that each run 1 OODA loop. That's expensive (3 agent spawns) for shallow investigation. Is it worth it?

**Defense:** The value of swarm isn't DEPTH — it's ISOLATION. Even with 1 OODA loop, the Analyst doesn't see the Explorer's reasoning path. For a focused-mode research (quick check, low uncertainty), this isolation might STILL produce better results than a single agent that carries Gather's context into Extract.

**Counter:** For focused mode, the conversation is SHORT (few turns). "Lost in the Middle" and attention dilution are minimal. The anchoring bias argument is weakest here.

**Resolution:** Swarm × focused is VALID but LOW VALUE. The config should allow it, but the recommendation should be: use swarm with deep mode where the benefit is clearest (longer conversations, more OODA loops, more anchoring risk).

**Verdict:** Not incompatible, just low-ROI. Keep as valid combination but document the recommendation.

### C5: Attack on surviving configs — "Too many options"

**Attack:** 5 surviving configurations (S2, S3', S5, S6, S7) is too many. The TS can't implement all 5. What's the recommended one?

**Defense (narrowing):**
- S2 is a subset of S7 (S7 = S2 + command override). **Subsume S2 into S7.**
- S5 is a subset of S7 (per-workflow override = just a config key). **Subsume S5 into S7.**
- S6 is a subset of S7 (command flag = one aspect of S7). **Subsume S6 into S7.**
- S3' is a refinement of S7 (auto-detect = a value for the config key). **Subsume S3' into S7.**

**All survivors converge to S7 with S3' as the smart default:**

```yaml
# project_config.yaml
tfw:
  research:
    execution_model: auto    # auto | single | multi
    default_mode: focused    # focused | deep
```

Where `auto` = detect platform capability → use multi if available, single if not.

Command override: `/tfw-research --single` or `/tfw-research --multi` overrides config for one run.

**Verdict:** S7+S3' is the recommended configuration. All other survivors are subsets of it.

### C6: Attack on "3 sub-agents only" — cost concern

**Attack:** Spawning 3 sub-agents per research iteration = 3× the token cost minimum (each sub-agent gets its own context window). In deep mode with multiple OODA loops, each agent may use significant tokens. For a team running multiple iterations, this adds up.

**Defense:** 
1. Current single-agent mode already uses a massive context window (the conversation grows across all stages)
2. Sub-agents start with SMALL context (system_prompt + stage files) and grow only as needed
3. The cost comparison is: 1 large context (single agent) vs 3 smaller contexts (sub-agents). Total tokens may be SIMILAR
4. If cost is a concern, `execution_model: single` is one config change away

**Verdict:** Cost is real but not blocking. Monitor in practice. Config provides escape hatch.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| H1 structurally justified (anchoring bias, file < conversation) | Empirical validation (helpdesk — separate task) |
| All 5 survivors converge to S7+S3' (config + auto-detect + command override) | Exact config syntax (TS scope) |
| Briefing stays with coordinator (structural + platform constraint) | Future: may revisit if evidence shows benefit |
| Swarm × focused = valid but low-ROI | Documentation of recommendation |
| Cost = real but not blocking, config escape hatch exists | Monitoring in practice |
| Detection logic in workflow, protocol in swarm.md | |

**Sufficiency (deep mode):**
- [x] External source used? (Building on Gather's evidence base)
- [x] Briefing gap closed? (All 3 hypotheses have verdicts)
- [x] Pairwise incompatibility checked? (3 pairs, 2 configs eliminated in Extract, all survivors converged)
- [x] Hypothesis tested? (H1: structurally justified. H8: resolved — orthogonal axis + S7+S3'. H9: fresh wins)
- [x] Counter-evidence sought? (6 attacks with defenses. File-based anchoring counter-argument addressed)
- [x] Metacognitive check: C5 convergence (all survivors → S7+S3') was unexpected — started with 5, ended with 1 recommended ✅

Stage complete: YES
→ User decision: ___
