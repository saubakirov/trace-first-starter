# Gather — What do we not know?

> **Mindset:** Explorer. Map independent choices and their evidence before narrowing.
> **Parent:** [HL-TFW_20260922-192606_PCUX](../../HL-TFW_20260922-192606_PCUX.md)
> **Goal:** Preserve strategic Coordinator planning while enabling command-only launches, live mandates, truthful provider routes, and complete documented closure.
> **Producer / route:** `codex:thread:local:01a0cb19-cbf2-7603-8775-c776f52660d4` → `codex:thread:local:01a0c980-4552-7ed3-b2aa-3c5cc46bc7bc`.
> **Source epoch:** repository at approved HL freeze `5259851e6f07206a07d022db11ef1cbc91dca775` plus the Researcher checkpoint `a62bf2d`; external documentation opened 2026-09-23. External pages describe their named products and versions, not an observed PCUX field trial.

## Dimensions

Alternatives here describe the design space. The approved HL already rules out some of them; Extract will test compatibility and name those exclusions explicitly.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| D1 — authorization at first command | Resolve the existing frozen mandate from task files and record dispatch when address is known | Require a prewritten addressed dispatch before the child starts | Add a launch token or registry that the child redeems | Make every child owner-direct |
| D2 — first reliable child address | Creation receipt | First routed status/gate return | One transport-only readiness exchange where a provider needs it | Preassigned dormant role pool |
| D3 — live operating selection | Current status fields plus a referenced immutable owner decision | New status selection field(s) plus a journal decision event | Edit/re-freeze HL for each switch | Keep selection only in conversation |
| D4 — complete role topology | Separate visible role tasks/chats | Separate named role subagents with their own return and continuation | One session changes role sequentially | Mixed visible and compact roles at distinct gates |
| D5 — shared repository write control | Separate worktree per mutator | One local workspace, one active mutation owner, fixed review candidate | Shared workspace with concurrent writes | External lock/service |
| D6 — close evidence and disposal | Existing RF/REVIEW/close trace plus exact task-owned dispositions | New task-local resource register | Provider cleanup metadata alone | Owner manually inventories all resources at the end |

## Findings

### G1 — Current state, authority, event and launch carriers

`status.md` is the only live state and route authority. Its closed schema has five coordination fields: `coordinator_route`, `owner_gateway`, `dialogue`, `activation`, and `coordination_authority`. `tools/tfw_state.py` accepts `gateway:{address}` with `tfw-gates-only`; it requires a gateway only in the other direction, when dialogue is `iterative`. The same validator admits only `owner-only` or `delegated:{ref}` activation. It has no current launch/reporting selection, effective checkpoint, or citation to a separate owner mode decision. Its event kind vocabulary includes `dispatch` and `gate_answer`, but no mode-decision kind. Sources: `.tfw/conventions.md` → `Task control files`, `Task Statuses`, `Workflow activation and routing`; `.tfw/templates/status.md`; `.tfw/templates/journal/event.md`; `tools/tfw_state.py` `COORDINATION_KEYS`, validation and `EVENT_KINDS`.

The current activation prose requires an actual Coordinator dispatch citing the mandate and says dispatch preserves the child's native address. `plan.md` also says dispatch records the destination and address after approval. This conflicts with the approved HL's valid command-first route when the parent learns the address only from a creation receipt or later gate. The current `Session identity` and Plan Step 5 also couple a gateway title or iterative permission to dialogue, though the status parser already accepts gates-only gateway state. These are source conflicts for H5/H6, not evidence that an unaddressed child has been authenticated. Sources: `.tfw/conventions.md` → `Session identity`, `Workflow activation and routing`, `Launch selection`; `.tfw/workflows/plan.md` Steps 5 and 7 and dispatch paragraph; HL §§3.4, 4.1.

The current Codex task exposes separate visible task creation, exact task-addressed send, wait/readback and title write/readback mechanisms. This Researcher received a command-only delegated task, changed its title with an exact returned title, sent a Briefing gate to the recorded Coordinator, and received that Coordinator's addressed acceptance. That is a bounded live observation of this route; it is not a P3/P4 complete role chain or proof for another provider. Official OpenAI documentation distinguishes a skill's reusable instructions from live MCP data/actions, matching the repository's command/authority separation. [OpenAI Docs — Skills](https://developers.openai.com/plugins/concepts/skills).

### G2 — Role identity, compact mechanisms and provider limits

Current TFW requires distinct directly addressable units, exact role commands, durable artifacts and returns, and an independent Reviewer. The existing `handoff.md` and `review.md` require matching spine/dispatch, same-unit continuation, producer provenance, Candidate and evidence checks, and return to `coordinator_route`. A subagent mechanism alone proves none of these TFW effects. Sources: `.tfw/conventions.md` → `Workflow activation and routing`, `Role Lock Protocol`; `.tfw/workflows/handoff.md` → `Identity, activation, and returned work`, Steps 1–3; `.tfw/workflows/review.md` → `Identity, activation, and trust`; HL §§3.5, 5–6.

Current Claude Code documentation says custom subagents can load skills and invoke unlisted available skills if their tool set permits it; a general-purpose or custom subagent can be resumed by ID/name with preserved history, while built-in Explore/Plan are one-shot. It also describes `SendMessage` for resumed subagents and, on versions/surfaces that enable it, other sessions. These are documented possibilities, not proof that the owner's Claude Desktop surface gives each role an exact TFW command, direct return, browser tool, independent review and end-to-end continuation. [Claude Code — Create custom subagents](https://code.claude.com/docs/en/sub-agents), [Claude Code — Extend Claude Code](https://code.claude.com/docs/en/features-overview).

The approved HL §2 selects the owner's 2026-09-23 Claude Desktop report at SHA-256 `66bea5b7b4271f27189264f471dbe0cbc68f239a0ad2be9e2f361d9df583b1d6` (15,403 bytes). For that setup it reports that a click-created full chat needs a nonempty initial prompt; local launch uses the shared checkout; full-chat creation needs the owner click; a named subagent can be launched natively; and archive leaves a worktree/branch restoration dependency. It does **not** establish a complete TFW trial. The current on-disk file is a later 19,211-byte SHA-256 `14e9af73a3115e48ae49864a3b2c95ec24b6e2ccfe720d9e23ce6612fea6c5c7` epoch with a browser addendum; the Coordinator says the owner has not declared it ready. This stage uses only the bounded selected observations in HL §2 and leaves browser-dependent eligibility unresolved.

Official Antigravity documentation distinguishes IDE Agent conversations, CLI subagents and their control panel. It describes multiple IDE conversations and a separate CLI subagent mechanism with IDs, tool/skill configuration and optional shared workspace. This supports a mechanism-level compact possibility, but neither its CLI docs nor the owner report proves that the owner's active IDE exposes autonomous full-chat creation or a complete TFW role cycle. The owner's current full-chat creation route therefore remains a dated manual-surface report pending actual local inspection. [Antigravity IDE — Agent](https://www.antigravity.google/docs/agent), [Antigravity — Custom subagents](https://www.antigravity.google/docs/subagents/).

### G3 — Shared writes, stable review, knowledge effects and resource close

Current `.tfw/conventions.md` requires a separate worktree for a delegated mutating run, but also says a worktree is not a lock and one mutation owner controls each tree. The approved HL selects one Claude local workspace with serialized writes; this requires a focused exception to the blanket worktree sentence and a stable Candidate boundary before an independent Reviewer reads it. `handoff.md` already fixes the first tested implementation descendant as Candidate, requires exact-path commits, and returns that SHA with evidence. `review.md` independently verifies the returned result. Sources: `.tfw/conventions.md` → `Worktrees for concurrent mutation`, `Landing a deliverable across sessions`; `.tfw/workflows/handoff.md` Steps 1–3; `.tfw/workflows/review.md` → `Finding contract and judgment order`; HL §§3.5, 3.7.

Current close requires material handover, docs/knowledge Applied or reasoned N/A, an independent check of changed final claims, actual landing where selected, then terminal status/event. `docs.md` and `knowledge.md` already own distinct technical and human knowledge effects. The current close route does not explicitly require a task changelog entry, exact resource dispositions, or parent-after-return archival. The approved HL §3.7 adds these obligations without authorizing release or broad deletion. Git's own worktree documentation says normal removal requires a clean linked tree, cannot remove the main tree, and a locked tree resists removal; this supports exact ownership and preservation checks before any task-local disposal. [Git — git-worktree](https://git-scm.com/docs/git-worktree). Sources: `.tfw/conventions.md` → `Closing and record recovery`; `.tfw/workflows/docs.md` Steps 1–3; `.tfw/workflows/knowledge.md` Steps 1–3; HL §3.7.

## Checkpoint

| Found | Remaining for Extract/Challenge |
|---|---|
| Six independent dimensions expose the concrete source seams for H1/H2/H5–H9. | Test the smallest status/event/reader design against the frozen command-only and mode-switch claims. |
| Claude and Antigravity document subagent mechanisms; the selected Desktop report narrows full-chat launch and shared checkout. | Determine exact compact eligibility and fallback without promoting mechanism documentation to a complete TFW trial; browser addendum remains pending owner selection. |
| Current Candidate, review and knowledge routes offer reusable close anchors. | Specify write serialization, fixed-candidate review, changelog ownership and exact resource/restore dispositions. |

**Sufficiency:**

- [x] External source used: opened official OpenAI, Anthropic, Google and Git documentation on 2026-09-23.
- [x] Briefing gap closed for this stage: dimensions and current-source conflicts are mapped; no solution is selected yet.
- [x] Dimensions identified: D1–D6, with at least three alternatives each.

**Stage decision:** carry D1–D6 into Extract under `focused`; keep browser-dependent compact eligibility explicitly open until the owner completes and selects the addendum or a native field check is available.

## Material handover at this checkpoint

Producer is the named Researcher unit above. Inspected scope is the selected current TFW carriers/readers and opened primary product/Git documentation, plus the original Claude report's bounded HL §2 observations. Material: the present schema and workflow text conflict at command-first address timing, gateway/dialogue coupling and live-mode carrier; existing Candidate/review/close machinery can be tested for reuse. Uncertainty: external product docs are mechanism evidence only; the later Claude browser addendum is unselected; no complete compact TFW role trial is observed. Continuation: the same unit maps configurations in Extract after the Coordinator returns this Gather gate.

---
Stage complete: YES
→ User decision: no new owner decision at Gather; Coordinator may narrow the next stage if a material source conflict is identified.
