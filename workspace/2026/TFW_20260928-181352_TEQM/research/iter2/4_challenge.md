# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260928-181352_TEQM](../../HL-TFW_20260928-181352_TEQM.md)
> Goal: Identify what this exact Claude Code session exposes about its own tokens/time/money and how `economics.md` could collect it.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D2 | Live context-window occupancy gauge (C1) | HL Artifact contract | "cumulative lifetime token consumption" | The gauge is explicitly compactable (`autoCompactsAtPercent: 97`); a compaction event shrinks `tokensUsed` while real, billed cumulative consumption keeps growing. Treating C1's number as a lifetime total after any compaction silently undercounts — the exact anti-pattern iter1 flagged for Codex's cumulative-vs-step counters (iter1 D4), now confirmed on the Claude Desktop surface too. |
| D3 | Quota percentage (C1) | HL Money contract | "observed provider charges... or a dated tariff-based estimate" | A percentage of a rolling 5-hour/weekly window is neither an observed charge nor a price-based estimate. Converting it to dollars needs the plan's total price and the pool's absolute token/request size, and neither is exposed by `get_usage`. `extraUsage.enabled: false` additionally means this account has no metered overage figure to fall back on. |
| D4 | Per-child `get_usage` (C5) | Collection timing | "poll after the child's work is done" | The tool's own contract states context is `"unavailable"` for an idle, starting or archived session. A Coordinator that waits to poll children until convenient can lose the numeric snapshot entirely; collection must happen *during* the child's own run, matching the HL Artifact contract's "collection happens during work," not as an afterthought. |

**Surviving configurations** (from Extract's Configuration Space, after removing incompatible pairs):

| Config | D1 | D2 | D3 | Notes |
|--------|----|----|----|-------|
| C1' | This session's `get_usage`/`get_session` | Point-in-time context-window occupancy + identity | Quota % only, labeled explicitly as non-monetary | Usable as a *coverage/identity* source, not a cost source |
| C4' | Two same-session samples, timestamped, taken *before any compaction* | A short-interval Δ-occupancy, valid only within one uncompacted window | Still non-monetary | Usable as a cheap, bounded stage-level proxy; must record whether a compaction occurred between samples, or the delta is void |
| C5' | `list_sessions(linked:true)` + per-child `get_usage` taken *while each child is still running*, ideally at the child's own close | Sibling identity/model, each child self-reports before archiving | Shared account quota only | The only surviving child-coverage design: each role captures and writes its own snapshot before ending, not a later external pull |

**Unexpected survivors:**
- C4' survives despite looking, at Briefing time, like a strictly weaker duplicate of C1 — it is actually the only configuration on this surface that produces a *rate* (tokens per unit wall-clock, within a bounded window), which is closer to the HL's "execution interval" concept than either raw sample alone, provided the compaction caveat is recorded alongside it.
- C5' survives in a self-reporting form nobody in the Briefing proposed as the primary design — the Briefing's Q3 asked whether *this surface* could tell a *future collector* about child coverage; the answer that survives scrutiny is architectural (self-report at each role's own close) rather than mechanical (a central poll), and it matches the existing task-local-truth principle (HL §7 Principle 5) rather than requiring a new one.

## Findings

### C1: The two-sample delta is genuine but narrow

The two live samples in Gather (G1) showed `tokensUsed` moving from 134,884 to 147,756 (+12,872) across roughly 153 seconds of real tool activity, with `percentUsed` moving 13%→15%, well below the 97% auto-compact threshold — so this particular delta is not compaction-corrupted. But a full task/role lifetime for a non-trivial TFW iteration very plausibly crosses a compaction boundary at least once (this task's own iter1 alone ran five stages across one long-lived producer). A collector relying on C4' must therefore record the compaction watermark (`autoCompactsAtPercent`, and ideally whether it fired) alongside every delta, or explicitly bound its claim to "no compaction observed in this window" the way this Challenge does here.

### C2: The quota percentage cannot be back-converted into tokens or dollars

Nothing in `get_usage`'s output states the absolute size of the "5-hour" or "weekly" pool in tokens or requests, and nothing states this account's subscription price. A search for the Team-plan's exact pool size and price (queried in Gather, `G2`/`G3`) returned only third-party explainer estimates for Pro/Max tiers, not an authoritative figure for this account's actual Team-plan window — reusing those unverified third-party numbers to impute a dollar cost for this task would manufacture evidence the HL explicitly forbids (DoF-1: "reconstructed from text length or guessed counters and presented as observed consumption"). The honest position is: on this exact surface, under this exact plan, task-level money remains **unknown**, not merely "unlabeled" — there is no calculable estimate to label, unlike iter1's Claude CLI row, which at least had a `costBasis: list` figure to label as an estimate.

### C3: Child coverage is inferred from the tool's own documented contract, not from a live join

This iteration did not spawn a child TFW role (no `Agent` call), so C5' is a design recommendation grounded in the tool's own written behavior ("an idle, starting or archived session reports it unavailable"), not an executed observation. It is reported as such — a documented mechanism, distinct from an observed one — consistent with the Trust Protocol's requirement to verify technical approaches rather than assume them, and with iter1's own observed/documented distinction for AGY and Codex.

### C4: This session's identity is more stable than iter1's CLI sessions, which helps task/role binding

Both `get_usage`/`get_session` samples returned the same `sessionId` across the whole multi-stage pass (Briefing through this Challenge), unlike iter1's Claude Code CLI, where each separate invocation minted its own ephemeral `session_id`. One stable Desktop session ID naturally spanning one Researcher's whole iteration is a *better* fit for TFW's one-role-one-unit binding than stitching together multiple CLI session IDs after the fact — a genuine advantage of this surface over the CLI one, even though its token/money detail is coarser.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C1'/C4'/C5' survive as the only defensible configurations for this surface; each has a named, recorded limitation. | Whether a future economics.md pilot accepts "money: unknown" for this exact surface, or requires pairing it with the CLI/OTel route (iter1) whenever a dollar figure matters — an implementation/TS decision, not this iteration's to make. |
| The context-window-size discrepancy (Gather G3, 1,000,000 vs commonly documented 200K/500K) remains unresolved by external sources; it does not block this iteration's conclusions since no dollar or token-count claim depends on the window's absolute size. | Confirming the actual contextWindow basis for `claude-sonnet-5` on a Team plan, if a later iteration needs it. |

**Sufficiency:**
- [x] External source used? (carried forward: OTel monitoring doc, usage-limit search/GitHub issues)
- [x] Briefing gap closed? (Guiding Questions 1–3 all answered, with explicit confidence labels)
- [x] Pairwise incompatibility checked? Surviving configurations listed?

Stage complete: YES
→ User decision: none required — iteration mandate authorizes continuous execution; proceeding to Synthesis.
