# Gather — "Which execution topologies actually expose the role holder?"
> **Mindset:** Explorer. Map observed behaviour, documented capability, and inference separately.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260902-111644_CRATM](../../HL-TFW_20260902-111644_CRATM.md)
> Goal: Re-charter full TFW agent-team delegation with project-scoped roles and task-local coordination while preserving the frozen no-runtime, no-live-roster boundary.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D _(if any)_ |
|-----------|-------|-------|-------|-----------------|
| D1. Long-lived role identity | User-visible provider task/session | Agent-team teammate | Nested subagent | One session changes roles |
| D2. Provisioning | Coordinator creates a task/teammate | Owner opens every peer before autonomy | Coordinator launches a resumable headless run | Parent session spawns a hidden child |
| D3. Discovery and addressability | Direct task/thread id | Provider-native team list and teammate name | Explicit returned session id | Parent relay plus free-text handle |
| D4. Role separation | Dedicated task/session per TFW role | Dedicated teammate per TFW role | Independent process per role | Shared session with sequential role switches |
| D5. Workspace isolation | Managed worktree per role task | Permanent worktree with multiple chats | Manually assigned worktree per role | Shared checkout with file partitioning |
| D6. Durable coordination trace | Frozen status/journal and role artifacts | Provider-generated team/task state outside project | New live project roster | Transcript only |
| D7. Artifact legality | Existing TFW artifacts only | Ephemeral provider runtime state only | New committed session registry | Agent-definition file used as a role holder |
| D8. Owner intervention after autonomy | Contract-declared infrastructure exception only | Owner provisions peers before the boundary | Owner relays messages during execution | Owner approves each workflow gate |

## Findings

### G1. Evidence ledger and classification

The sources answer different questions and are not interchangeable:

| Evidence class | Sources | What it can establish | What it cannot establish |
|----------------|---------|-----------------------|--------------------------|
| **Field-observed** | Helpdesk `SESSIONS.md` and its TFW artifacts; RCFR/VBSA task metadata, journals, commits and worktrees | What a named run actually exposed, routed, wrote, isolated, or returned to the owner | Unused provider capabilities or a native run that did not occur |
| **Provider-documented** | Current OpenAI and Anthropic product documentation | Supported topology, creation, messaging, persistence and isolation semantics | That those mechanics carried a complete TFW unit under CRATM's frozen constraints |
| **Inferred** | Comparisons made from the two classes above | Candidate profile viability, failure modes, and the test envelope still needed | Independent proof; every inference must remain traceable to observations or documentation |

Local field set:

- Helpdesk: `D:\projects\research\helpdesk\workspace\2026\HD_20260903-160919_BIAI\SESSIONS.md`, plus its Phase A dispatch, ONB, RF and final REVIEW.
- RCFR: [root status](../../../TFW_20260902-175227_RCFR/status.md), phase journals/artifacts, git history, and the archived user-visible coordinator tasks.
- VBSA: [root status](../../../TFW_20260904-113200_VBSA/status.md), phase journals/artifacts, git history, and active/archived user-visible coordinator, executor and reviewer tasks.

The provider-document set was refreshed on 2026-09-05. Documentation statements below are labelled as documentation, not promoted into field observations.

### G2. Helpdesk is a successful TFW trace with a failed autonomy topology

**Field-observed:**

- `SESSIONS.md` explicitly describes itself as a live session roster. It says the role map is otherwise lost and must be updated when composition changes, even though it also says task state remains authoritative elsewhere.
- Three intended long-lived role holders (`reviewer`, `executor`, `researcher`) were nested subagents behind the `helpdesk-14`, `helpdesk-af`, and `helpdesk-58` parent sessions. They did not appear as independently addressable cross-session peers; messages landed at their parents, which acted as relays.
- A request to create a coordinator was initially interpreted as creating `.claude/agents/tfw-phase-coordinator.md`. The owner corrected that interpretation and the file was deleted. An agent-definition file therefore did not establish a live role holder.
- The phase coordinator was constrained from creating agents and could not manage the research role directly. Sender recognition also failed behind relays because the child saw the relay parent as the sender.
- The roster drifted: it lagged a phase transfer, named `helpdesk-d2` as the current reviewer, and the final review was later authored by Reviewer `helpdesk-9f`. An executor had to ask the owner/chain who the active coordinator was.
- Existing TFW artifacts remained viable. The executor produced ONB/RF, and a separate reviewer produced an APPROVE review after sabotage in an isolated git worktree. The root reached its post-review knowledge state.
- The run nevertheless required owner corrections, peer-session opening, relay routing, and roster repair. Those are observations about this Helpdesk run; they are not evidence that a Claude-native agent team cannot do better.

**Inferred:** copying this topology into CRATM would fail the observable peer boundary and frozen DoF 3/7. The hidden child is not the addressable role holder, and `SESSIONS.md` would be a second live state authority/new task artifact. Helpdesk must therefore remain a field counterexample, not be renamed a Claude-native end-to-end acceptance run.

### G3. Current Claude documentation changes the H11 setup premise

> **Extract-stage source refresh, 2026-09-05:** the current documentation served after Gather is newer than the initially indexed page. The version and lifecycle details below supersede the initial `2.1.32+` note reported at the Gather STOP; this correction does not claim the currently installed binary implements the newer routes.

**Provider-documented:**

- [Agent teams](https://code.claude.com/docs/en/agent-teams) are an experimental Claude Code feature, disabled by default. The current page describes its baseline behaviour as of v2.1.178 and records later changes through at least v2.1.251. One interactive lead can spawn independent teammates; teammates have their own contexts, a shared task list, and direct teammate messaging. Non-interactive `-p` sessions cannot spawn teammates.
- The same page distinguishes teammates from subagents: subagents report only to the parent, while teammates can communicate directly. Teammate context does not inherit the lead conversation history; it receives project context plus its spawn prompt.
- Team configuration and task state are generated under `~/.claude/teams/{team-name}/` and `~/.claude/tasks/{team-name}/`. Team configuration is removed when the session ends; the local task list persists under normal retention. The documentation warns against preauthoring or editing this runtime state. There is no project-level equivalent.
- Documented limitations include one team per session, no nested teams, a fixed lead, possible lag in task status, slow shutdown, and no in-process teammate resumption.
- [Claude agents](https://code.claude.com/docs/en/agents) separately compares subagents, background agent sessions, agent teams, and worktrees. It says agent teams do **not** automatically isolate teammates in worktrees; file ownership/partitioning is the default collaboration mechanism.
- [Cross-session messaging](https://code.claude.com/docs/en/cross-session-messaging) is a separate, now-documented plane for sessions the user starts: Claude uses `ListAgents` and `SendMessage` to discover and directly message live local, background, remote, or web sessions. It requires v2.1.224+ on macOS/Linux/WSL and v2.1.234+ on native Windows, with later version floors for some providers and features. Delivery can be accepted, held for owner approval, or refused by per-session controls.
- [Claude worktrees](https://code.claude.com/docs/en/worktrees) can isolate separately launched sessions with `--worktree`; desktop sessions receive worktrees automatically, and a resumed session re-enters its bound worktree. This is documented for independent sessions and subagents, not automatic agent-team teammate isolation.
- [CLI usage](https://docs.anthropic.com/en/docs/claude-code/cli-usage) documents `claude -p` and explicit `--resume` mechanics, matching iteration 2's measured headless-session route but not turning that route into a team mailbox.

**Field-observed during the Extract refresh:** `claude --version` on this workstation returned `2.1.109`. That is below the documented native-Windows floor for current cross-session messaging; it does not prove which binary or feature flags the earlier Helpdesk sessions used.

**Inferred:** H11's current phrase “if the owner provisions peer sessions” is now version- and surface-bound, not a generally necessary Claude-only premise. The documented candidates are (a) a lead-created native agent team, (b) separately started peers using cross-session messaging and worktrees, and (c) explicit-id headless resumable sessions. Documentation does not close H11, and newer documentation does not make newer mechanics available in the measured `2.1.109` environment: no native Claude run has yet proved a complete TFW unit, per-role worktree isolation, legal artifacts, and zero owner routing after the autonomy boundary.

### G4. RCFR exposes a Codex-only chain as distinct tasks and worktrees

**Field-observed:**

- The app retains separate user-visible coordinator tasks for RCFR Phases A, B and C. The Phase C coordinator task (`01a06bad-…`) is associated with its own managed worktree (`…\worktrees\9e2b\steps-framework`) and directly messaged the Main Coordinator task (`01a0620a-…`).
- The same Phase C coordinator reused a distinct Reviewer task through correction rounds, waited on it directly, and reported the final verdict upward. No hidden parent relay or session roster appeared in the inspected route.
- Git history contains separate coordinator, executor and reviewer commits across phases, including the terminal Phase C coordinator closeout. Those commits prove artifact attribution and handoff order; the task metadata and distinct working directories, not the commit subjects alone, prove distinct task identity.
- The final task state is `DONE`; Phase C reported an independently approved candidate and a full suite of 520 passes with one skip.
- The owner had explicitly authorized finishing everything except push, and a self-hosting regression required a bounded correction. Thus RCFR is strong evidence for direct Codex task routing and role reuse, but it is not a controlled measurement of “no owner instruction after freeze.”

### G5. VBSA repeats the Codex chain and shows isolation under live correction

**Field-observed:**

- VBSA Phase A used distinct task ids for the Phase Coordinator (`01a06cdb-…`), Executor (`01a06d33-…`) and Reviewer (`01a06d61-…`). The coordinator sent each direct prompts and waited for its result; revisions reused the same long-lived role task.
- App metadata associates the Phase A coordinator and reviewer with different managed worktrees (`…\231d\…` and `…\4453\…`). Three current Phase B worktrees were observed at the same head; only one contained the untracked `phase-b/review/` change, while the other two were clean. This is direct isolation evidence, although the filesystem listing alone does not identify which role owns each anonymous worktree directory.
- Git history records distinct coordinator/executor/reviewer contributions for Phase A and coordinator/executor contributions for the active Phase B. Phase A reached an independent review approval.
- The Main Coordinator stopped at a knowledge/lifecycle boundary and asked the owner for a verdict before Phase B. This is an owner intervention in the observed run, even though the direct downward/upward routing itself worked without a relay or live roster.

**Inferred from G4–G5:** Codex has two repeat field traces for the structural core of H10: user-visible long-lived role tasks, direct coordinator routing, task reuse across revision, separate worktrees, and legal TFW artifact authorship. The evidence does not yet justify the stronger claim that either whole task was a controlled walk-away trial with zero post-freeze owner interaction.

### G6. OpenAI documentation is consistent with the observed Codex isolation model

**Provider-documented:**

- [Subagent workflows](https://learn.chatgpt.com/docs/agent-configuration/subagents) describe a parent spawning specialized subagents, collecting their results in one response, and surfacing subagent activity for inspection. That supports bounded helper use, but still describes a parent/child response topology rather than the independently addressable long-lived role tasks observed in RCFR/VBSA.
- [Git worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees) are documented as separate checkouts that allow independent chats in one project without overlapping working files. A managed worktree is normally associated with one chat; permanent worktrees may host multiple chats.
- [Environment modes](https://learn.chatgpt.com/docs/environments/modes) distinguishes local, worktree and cloud tasks and identifies worktree mode as the isolated local-change option.

The documentation corroborates the mechanics visible in the field traces, but RCFR/VBSA remain the stronger evidence that these mechanics were actually used for TFW role chains.

### G7. The mixed-provider route remains only a negative control

**Field-observed in iteration 2:** both provider directions could launch a fresh run and return text. Neither measured route addressed the other provider's already-running session/task. Claude follow-up required the explicit returned session id; an implicit “last session” route targeted unrelated owner state.

**Provider-documented context:** Claude's resumable CLI id, Claude agent-team mailbox, and Codex task/subagent planes are each provider-local mechanisms. The refreshed documentation found no common mailbox or direct existing-session identifier spanning those planes.

**Inferred:** a fresh cross-provider subprocess can be a bounded tool call, but it does not become a long-lived role peer. Without a direct existing-session route, continuing a mixed role requires a relay process or the owner to transport messages. This does not prove future impossibility; it identifies the exact missing capability for H12's first-release boundary.

### G8. Evidence still required from a later Claude-native run

No source inspected in this stage proves all of the following in one native Claude execution. This is the candidate acceptance envelope to refine after extraction and challenge:

1. One declared autonomy boundary, followed by zero owner routing except a predeclared infrastructure exception.
2. A Claude lead creates or provider-natively discovers every long-lived role holder; each role has an independently listable identity and is directly messageable without a parent relay.
3. Executor and Reviewer remain separate role holders through at least one RF/review cycle, including a correction round if the first review rejects.
4. Each concurrent writer uses a demonstrably separate git worktree; shared-checkout file partitioning does not silently substitute for the project's isolation requirement.
5. Only existing TFW status, journal and role artifacts are committed. Generated provider runtime state may remain outside the project, but no `SESSIONS.md`, new registry, or agent-definition role surrogate is added.
6. The bounded unit reaches its declared approved terminal state, and the durable trace is sufficient to reconstruct routing, artifacts, revisions, and owner interventions without using the chat transcript as task state.

Passing this envelope would be new field evidence for H11. Helpdesk does not pass it and must not be counted as the test.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Helpdesk precisely separates directly opened peer sessions from hidden relay subagents and shows live-roster drift | Determine whether any Helpdesk subchain nevertheless meets every observable criterion without owner/relay help |
| Current Claude agent teams let a lead spawn teammates, and current cross-session messaging lets sufficiently new sessions list/message separately started peers; owner-preprovisioning is not a universal premise | The installed Claude Code is `2.1.109`, below the documented Windows cross-session floor; no native Claude whole-TFW trial with explicit per-role worktree isolation has occurred |
| RCFR and VBSA provide repeated Codex task/worktree/role-artifact evidence | Quantify owner interventions and distinguish contract hard stops from routing failures |
| Mixed crossings launch fresh runs but do not address the other provider's existing role session | Challenge the negative finding against every documented direct-route alternative |
| Eight independent topology dimensions and their alternatives are enumerated | Extract pairwise profiles and exact acceptance/disconfirmation criteria |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified? _(skip if <3 independent factors — use comparison matrix in Findings instead)_

Stage complete: YES
→ Main Coordinator decision: pending at STOP
