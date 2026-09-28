# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260928-181352_TEQM](../../HL-TFW_20260928-181352_TEQM.md)
> Goal: Identify what this exact Claude Code session exposes about its own tokens/time/money and how `economics.md` could collect it.

## Configuration Space

| Config | D1: Numeric source | D2: What the number represents | D3: Money meaning |
|--------|--------------------|-------------------------------|--------------------|
| C1 | This session's `get_usage`/`get_session` | Live context-window occupancy gauge | Quota %, no dollar figure |
| C2 | Claude Code CLI JSON (iter1) | Per-invocation cumulative total | `total_cost_usd` @ `costBasis: list` |
| C3 | Claude Code OTel (documented, not locally observed) | Per-request counter, exported continuously | `claude_code.cost.usage` in USD |
| C4 | This session's `get_usage`, sampled twice (delta) | A derived interval proxy: Δcontext-occupancy over Δwall-clock | Still quota %, not dollars — delta does not create a price |
| C5 | `list_sessions(linked:true)` + per-child `get_usage` | Sibling identity/model only, unless the child is queried live | Same account-level quota, shared across parent and children |

C4 is the combination nobody proposed in the Briefing: nothing in the Briefing anticipated that *sampling the same live gauge twice* would itself be a distinct, weaker configuration (an interval proxy) rather than a stronger one — see Challenge.

## Findings

### E1: HL need → mechanism map, this surface only

| HL need | Available on this exact session? | Mechanism | Confidence |
|---|---|---|---|
| Session/model identity | Yes | `get_session`: `sessionId`, `model`, `effort`, `permissionMode`, `title`, `createdAt` | Observed |
| Task/role binding | Partial | The session's own `sessionId` is stable for this whole iteration's multi-stage work (one Researcher = one session), but nothing ties it to the TFW task ID or role name except this RES's own header | Observed + inferred |
| Input/output/cache/thinking token counters | No | Not present in `get_usage`; only an undifferentiated context-occupancy total split by *content type* (Messages/System tools/MCP tools/…), not by *token direction* | Observed |
| Execution time interval | No exact counter | `createdAt`/`lastActivityAt` give wall-clock bounds only; no per-turn or per-role `duration_ms` comparable to iter1's CLI `duration_ms: 2810` | Observed |
| Money/cost basis | No dollar figure | Only quota percentage against a fixed rolling window (5-hour, weekly, weekly-per-model); `extraUsage.enabled: false` for this account | Observed |
| Child/parallel role coverage | Schema-documented, not exercised | `list_sessions(linked:true)` + per-child `get_usage`, but only while each child is running | Documented, unverified |

### E2: Where this iteration's evidence sits relative to iter1's three-platform matrix

Iter1 left the "Claude Desktop" row as: *"documented conditional route / numeric unverified... Desktop: numeric access on all three surfaces [unverified]"*, filled only by an adjacent Claude Code CLI (Git Bash) observation. This iteration fills that Desktop row directly — but the surface actually being measured is one specific Desktop mode: an in-app Claude Code agent session with MCP session-management tools loaded (the "Code tab" described in this session's own system context), not the Chat or Cowork modes iter1's Gather also named. The finding does not generalize to those other modes, which expose no comparable tool in this session.

The resulting picture is not "Desktop has no numeric access" (iter1's provisional read) but "Desktop's Code-tab agent surface has a *different*, coarser numeric access than the CLI: context-occupancy + account quota, not token-direction + cost." This is a refinement of iter1's H1 row, not a reversal of it.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Every HL numeric need maps to either "observed, coarse" or "not present" on this surface; none map to "observed, matches HL's needed granularity." | Whether the OTel-documented richer schema (C3) can ever be attached to *this* Desktop surface, or is CLI-only by construction — this iteration's evidence cannot settle that; it is a product-design question, not one this session can probe further. |
| C4 (the sampled delta) is a real, cheap technique available to any economics.md collector on this surface. | Whether C4's delta is trustworthy — tested in Challenge. |

**Sufficiency:**
- [x] External source used? (carried forward from Gather; no new fetch needed for this stage's synthesis)
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?

Stage complete: YES
→ User decision: none required — iteration mandate authorizes continuous execution.
