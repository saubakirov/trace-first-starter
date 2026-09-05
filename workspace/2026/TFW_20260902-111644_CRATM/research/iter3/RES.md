# RES — TFW_20260902-111644_CRATM: Provider-homogeneous execution profiles (Iteration 3)

> **Date**: 2026-09-05
> **Author**: Researcher (Codex), on behalf of saubakirov
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW_20260902-111644_CRATM](../../HL-TFW_20260902-111644_CRATM.md)
> **Mode**: Pipeline · focused
> **Iteration**: 3 of 2 (min) / 5 (max) — normal sequential semantics
> **Assigned hypotheses**: H10, H11, H12

---

## Research Context

Iteration 3 tests the provider split opened by the owner's Helpdesk field run: whether the first
release has one universal topology or honest provider-homogeneous profiles. It compares Helpdesk's
Claude session/relay trace with RCFR and VBSA's Codex task/worktree traces through one observable
contract: visible identity, provisioning, direct addressability, role separation, worktree isolation,
durable legal artifacts, and owner turns after autonomy. Current provider documentation is used only
for supported capability; it never fills a missing field run. No mixed team or Claude peer was
launched, and Helpdesk is not represented as a native Claude agent-team end-to-end test.

## Briefing

See [1_briefing.md](1_briefing.md). This sequential iteration begins from iteration 2 decisions D1,
D3, D4 and D10 and its four open threads. The evidence chain is [Gather](2_gather.md) →
[Extract](3_extract.md) → [Challenge](4_challenge.md). Main Coordinator approved each stage at its
STOP. One source correction was made transparently in Gather when the current Claude documentation
served a newer feature/version description than the initial indexed page.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | **A long-lived TFW role passes an eight-gate observable contract, not a provider label.** The gates are identity, provisioning, direct address, Role Lock, worktree isolation, durable trace, artifact boundary, and walk-away outcome | Helpdesk had provider sessions and successful artifacts but failed role visibility/routing and introduced a drifting roster. RCFR/VBSA had distinct tasks/worktrees and direct routing. A feature name alone predicts neither result. Gather G1–G8; Extract E2 |
| D2 | **A nested subagent behind a relay is a helper, never the long-lived role holder** | Helpdesk's `reviewer`, `executor`, and `researcher` were invisible cross-session; messages and replies resolved to their parent sessions. Codex subagents likewise return to the parent. A bounded helper is legal only while the parent keeps the workflow role. Gather G2; Challenge incompatible pairs |
| D3 | **Codex managed tasks are the first-release profile candidate, with G1–G7 field-supported and G8 not controlled** | RCFR and VBSA repeatedly expose user-visible role task ids, direct sends/waits, same-role reuse through revisions, separate managed worktrees, and legal coordinator/executor/reviewer artifacts. Neither trace declared a pre-run owner-turn measurement, and VBSA stopped on a real lifecycle ambiguity. This is capability evidence, not a reliability rate or completed walk-away experiment. Gather G4–G6; Challenge C1 |
| D4 | **“Claude-only” is at least three profiles, not one:** native agent team, owner-opened peer sessions, and headless resumable sessions. Coordinator-created background peers and a two-level hybrid are additional current-document candidates | The three required families have different evidence: agent teams are documentation-only for TFW and lack automatic teammate worktrees; peers have Helpdesk/iteration-2 field identity but not a roster-free whole chain; `-p` has measured creation/explicit resume but only a one-word workflow proxy. Current docs add background sessions and cross-session messaging, neither field-tested on this installed build. Extract E1–E4 |
| D5 | **H11's owner-preprovisioning premise is not universal and the broader Claude feasibility claim remains open** | Current [agent-team documentation](https://code.claude.com/docs/en/agent-teams) lets an interactive lead spawn teammates; current [cross-session messaging](https://code.claude.com/docs/en/cross-session-messaging) lets sufficiently new independent sessions discover/message peers. The measured workstation is Claude Code `2.1.109`, below the documented current Windows cross-session floor, and no candidate has carried a native whole TFW unit. Gather G3; Extract E3; Challenge C2 |
| D6 | **Version, OS and surface are dispatch-time diagnostic evidence, never participant identity or a profile registry** | A version string can remain unchanged while flags, org policy or inbound controls disable delivery; Helpdesk also reports a surface not reconstructable from today's version floor. The frozen contract keeps principal, role, reports-to edge, autonomy boundary and semantic channel. Existing dispatch/journal evidence records actual tool presence, nonce delivery, permission result and worktree identity. No version field, live roster, pid, lock or copied provider runtime state is added. Challenge C3 |
| D7 | **A Claude-native whole-TFW trial is mandatory before a Claude profile is specified or executed, and its gate belongs at the future Phase D Claude-profile boundary—not at Phase A** | Phase A's frozen outcome is git worktree isolation and commit attribution; iterations 1–3 already supplied its evidence and a Claude session topology cannot change that outcome. Phase D introduces team mode/Role Assignment and is where a provider profile would be promised. The eight-step acceptance gate below must pass there first. Main Coordinator direction; Extract E6; Challenge C2/C5 |
| D8 | **Mixed long-lived roles are excluded from the first release under the current no-runtime contract and measured routes; mixed bounded helpers remain legal** | Both measured crossings start fresh runs, not the other provider's existing role. Claude channels and Codex app-server/SDK show a bridge is technically plausible, so permanent impossibility is false; they also require a plugin/MCP server/client, credentials, liveness and security—the runtime scope the frozen task excludes. Challenge C4/C6 |
| D9 | **Provider runtime state may assist execution but never becomes TFW task authority** | Claude team config is generated and removed on exit; its task list follows provider retention. Helpdesk's copied live roster drifted in one day. Status, immutable journal, dispatch evidence and role artifacts remain the only durable project trace. Gather G2/G3; Challenge C2/C3 |
| D10 | **Owner interaction is measured by cause after a declared boundary, not inferred from topology** | Contract returns for reserved claims, self-ruling, Purpose Check contradiction, REJECT, unavailable participant, budget excess or nonterminating chain are honest stops. Permission clicks, peer creation after autonomy, relay forwarding, roster repair and “keep going” are profile failures for the run. Challenge C5 |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Which Claude family should run the first native acceptance unit: isolated teammates, owner-opened peers, background peers, headless sessions, or the two-level hybrid? | Open; Phase D gate | Do not choose from documentation. Run exactly one family through the common acceptance gate, then compare another only if the first fails or the alternative has independent value |
| Q2 | Can an agent-team teammate enter and remain in a distinct worktree while preserving direct team addressability and Role Lock? | Open; native test required | Current docs explicitly say teammates are not automatically worktree-isolated. No field trace closes the manual composition |
| Q3 | Can Claude channels and Codex app-server address the actual existing user-visible role tasks bidirectionally without a custom bridge/runtime? | Deferred outside first release | Current docs show bridge ingredients, not a direct cross-provider peer route. Research only in a separately scoped task if mixed execution gains independent value |
| Q4 | What is the controlled Codex G8 reliability rate? | Open; non-blocking for present planning | RCFR/VBSA support G1–G7. A later run must predeclare the boundary and count every owner turn, silent task, duplicate fork and replacement |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H10 | A Codex-only team can use independently addressable user-visible tasks/threads for every long-lived TFW role, while subagents remain bounded stage helpers rather than role holders | 🟡 field-supported, not yet synthesized | 🟡 **field-supported for G1–G7; G8 not controlled** | RCFR/VBSA task ids, direct coordinator routing, separate CWD/worktrees and role artifacts; selection bias and owner-turn counter-evidence in Challenge C1 |
| H11 | A Claude-only team can satisfy the provider-neutral contract if the owner provisions peers before autonomy and the coordinator uses native discovery/messaging without relays or a roster | 🟠 needs a real TFW trial | 🟠 **single-premise form split; broader feasibility open** | Owner provisioning is one C6 alternative, not universal after documented agent teams/background sessions. C5/C6/C7/C8/C9 each retain a different missing TFW gate; no Claude-native whole unit exists |
| H12 | Mixed-provider execution cannot satisfy walk-away with current session controls and should be outside the first release | 🟡 strong negative evidence | ✅ **supported as a first-release restriction, not permanent impossibility** | Measured fresh crossings lack an existing-session peer route. Channels/app-server are out-of-scope bridge ingredients, defining reversal evidence rather than a current profile |

## Claude-native Acceptance Gate

This gate applies **before Phase D specifies or dispatches a Claude profile**. It is not a Phase A
prerequisite and does not block planning the already-researched isolation/attribution outcome.

1. **Behavioral preflight in existing evidence:** capture actual CLI/surface, OS/version for diagnosis,
   required tool/flag presence, worktree base, permission mode and inbound decision. Store no live
   registry or “current version” profile field.
2. **Frozen unit:** choose one small approved phase with Phase Coordinator, Executor and Reviewer,
   existing ONB/RF/REVIEW outputs, explicit `Autonomous from`, and no known amendment.
3. **Provisioning identity:** record how every long-lived role was created. Team trial proves teammate,
   not subagent; peer trial proves independent session, not parent relay; headless trial captures the
   explicit session id and forbids `--last`.
4. **Direct route:** coordinator lists or explicitly identifies the exact target, sends a nonce-bearing
   bounded assignment, and receives a direct reply. Duplicate/ambiguous names, parent relays or owner
   forwarding fail; no roster is introduced.
5. **Isolation:** before mutation, record absolute worktree and git common directory for each role;
   worktree paths differ, and only the allowed mutation owner dirties each. Shared-checkout file
   partitioning fails.
6. **Role/artifact cycle:** Phase Coordinator writes neither ONB/RF nor REVIEW; Executor writes ONB/RF;
   Reviewer independently reads the fixed result and writes REVIEW. Force one rejection/correction and
   reuse the same role identities without switching roles.
7. **Owner-turn outcome:** after the declared boundary, count every owner message. Only a frozen
   exhaustive return trigger may be nonzero. Permission approval, peer creation, relay, roster repair,
   manual wake or “keep going” fails the profile for this run.
8. **Terminal reconstruction:** the unit reaches its approved terminal state, and status, immutable
   journal, dispatch and role artifacts reconstruct provisioning, routing, correction, verdict and
   owner-turn count without provider transcript/runtime state.

All eight must pass in one native run. Separate provider demos do not compose into acceptance.

## HL Update Recommendations

> **The researcher classifies. The researcher never applies.** Every recommendation names the HL
> section it targets and lands in one of the two tables below. Editing the HL is not a researcher
> output — see conventions.md §15 Role Lock.
>
> - **Refinements** target the free sections (§2, §7.2, §8, §9, §10, §11). The coordinator applies
>   them directly, no ceremony.
> - **Amendment Proposals** target the frozen sections (§1, §3, §4, §5, §6, §7). The coordinator
>   may **not** apply them. They are transcribed into HL §12 Amendment Log with verdict `PROPOSED`
>   and wait for an owner ruling. Nothing in a frozen section moves before that ruling exists.
>
> Which class a finding belongs to is decided by the granularity rule in conventions.md §3 —
> the frozen unit is the declarative claim, not the section text.
>
> If a class is empty, say so: **No refinements.** / **No amendment proposals.**

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 | Replace the universal reading of “a Claude peer cannot be created” with dated field evidence plus the current split: iteration 2 measured owner-opened peers and `-p` continuity; current docs add lead-created teammates, background sessions, cross-session messaging and per-session worktrees; installed `2.1.109` does not prove the newer Windows route | D4–D6; Gather G3; Extract E3 |
| R2 | §2 | Add the one-contract field comparison: Helpdesk completed legal TFW artifacts but used hidden relay subagents, owner correction and a drifting roster; RCFR/VBSA repeatedly used distinct user-visible Codex role tasks, direct routing and separate worktrees, while still lacking a controlled G8 experiment | D1–D3; Gather G2/G4/G5 |
| R3 | §8 | Add `Claude-native profile acceptance` as a Phase D-specific dependency: all eight gate steps above pass before a Claude profile is specified/executed. State explicitly that it is **not** a Phase A dependency; Phase A's isolation/attribution planning may proceed under its existing VBSA landing gate | D7; Extract E6; Challenge C2/C5 |
| R4 | §9 | Revise R11/R14/R15/R17/R20–R23 as one coherent profile risk set: semantic channel tested at dispatch; actual behavior before version; nested child/definition never a role; route-specific provisioning instead of universal owner pre-opening; no live roster; mixed first-release boundary; G8 owner-turn causes counted. Keep versions out of Role Assignment/profile | D2, D4–D10; Challenge C3–C5 |
| R5 | §10 | Replace H10–H12 statuses with the table above; close “one Claude topology” into C5/C6/C7/C8/C9; retain exact reversal evidence; record channels/app-server as why H12 is scoped to first release rather than eternity | Hypothesis table; Challenge C4/C6 |
| R6 | §10 | Replace the “Claude trial before Phase D TS” open thread that named only headless `-p` with the common eight-step native gate and three mandatory distinct families. No current iteration 4 is required merely to plan Phase A | D4/D7; Claude-native Acceptance Gate |
| R7 | §11 | Add the planning insight that availability, addressability, isolation, durable trace and G8 are independent controls; provider documentation can open a candidate but only one field run can close its profile. Add that owner turns are classified by cause, so a contract stop is not a routing defect and a permission/relay turn is not erased by eventual APPROVE | D1/D10; Challenge C1/C5 |

### Amendment Proposals — frozen sections, owner verdict required

> Same column grammar as HL §12, minus the three fields a researcher cannot fill: the coordinator
> adds `Date` and `Proposer` on transcription, and `Verdict` opens as `PROPOSED`. The `#` column
> exists in both — number rows `A1`, `A2` … locally here; the coordinator re-assigns them into the
> HL's continuing sequence, because §12 is append-only and never renumbers.
> A row without evidence, cost and a considered alternative is not a proposal.

| # | § | Type | Proposed change | Evidence | Cost | Alternatives considered |
|---|---|------|-----------------|----------|------|------------------------|
| A1 | §3 Target State; cascade to §4 Phase D | `RESTRICT` | For the first release, every **long-lived** Role Assignment execution chain uses one provider-homogeneous profile with a field-proven native route. Mixed-provider fresh runs may be bounded helpers whose result returns to the role holder, but may not occupy long-lived role rows. A Claude profile is admitted only after the Phase D acceptance gate; Codex profile work may proceed at its current evidence level | Iteration 2 measured only fresh crossings; Helpdesk shows the relay/owner consequence of an unaddressable role; iteration 3 found no in-scope existing-session crossing. Claude channels and Codex app-server/SDK make a bridge plausible only by adding the runtime/transport/security surface frozen out by §3 | The first release cannot use a mixed Codex/Claude long-lived role chain (including the illustrative mixed reviewer row) and exposes provider-specific profile text. Claude support waits for a native trial; expanding later needs new evidence and an owner ruling | Keep one universal mixed-capable mode — rejected because its existing-session route is absent and returns the owner/relay to routing. Declare mixing impossible forever — rejected because channels/app-server are credible bridge ingredients. Build the bridge now — rejected because it adds a runtime, credentials, liveness and security design outside this task |

## Fact Candidates

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.
>
> **Scope:** Agent-observed project patterns discovered during research.
> Record facts about THIS project — not findings about alternatives,
> not implementation details (those belong in tfw-docs).
>
> **Human-Only Test**: would this fact be unknown without the human saying it?
> If an agent can discover it by reading code or running commands — it's not a fact candidate.
> These are NOT verified facts. They become facts after `/tfw-knowledge` consolidation.
>
> **Before writing:** review the conversation history. The human's messages are the primary source.

No fact candidates. Every new fact in this iteration was agent-observable from task artifacts,
provider documentation or executable output; the owner-approved directions are already captured in
the master HL and are not duplicated as unverified project knowledge.

> **Source format**: Use reference patterns (e.g., `HL-TFW-19`, `D24`). See compilable_contract.md §2.

## Strategic Insights (Research)

> **Cognitive mode:** Deep analytical synthesis. Capture human-sourced domain knowledge
> observed during research briefings, then ADD implications — what does this insight
> mean for the project's direction?
>
> **Human-Only Test:** Would this insight be unknown without the user saying it?
> If an agent can discover it by reading code — it's NOT a strategic insight, it's a Fact Candidate.
>
> **When to fill:** Only when the human provides domain knowledge, corrections, or strategic
> context in research briefings. If no human interaction occurred — write "No strategic insights."
>
> **Categories:** conventions.md §10.1.

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | stakeholder | The owner is comfortable delegating the complete chain when every long-lived participant is Codex and cites RCFR/VBSA as the working form. **Implication:** Codex is the first profile candidate, but comfort and field traces do not authorize a G8 reliability claim | User, 2026-09-05, master HL S22 and approved iteration 3 | ★★★ |
| SS2 | process | The owner does not want a mixed-provider autonomous team in the first release and required Helpdesk evidence not to be renamed a Claude-native test. **Implication:** profile boundaries and evidence labels are product scope, not implementation notes; changing the frozen universal-looking target requires A1 rather than a silent refinement | User, 2026-09-05, master HL S23–S24 and iteration 3 direction | ★★★ |

## Findings Map

```text
ONE OBSERVABLE CONTRACT (G1 identity → G8 owner-turn outcome)
│
├─ Codex managed tasks
│  └─ RCFR + VBSA field traces ──► G1–G7 supported ──► first-release candidate
│                                  └─ G8 uncontrolled ──► later counted run, no reliability claim
│
├─ Claude-only
│  ├─ native team ───────────────► documented identity/message; worktree + hierarchy unproved
│  ├─ owner-opened peers ────────► field peer identity; whole no-roster chain unproved
│  ├─ headless resumable ────────► field create/resume; whole workflow + live peer unproved
│  └─ background/hybrid ─────────► documented composition only
│                                  └─► common eight-step Phase D gate before any Claude profile
│
└─ Mixed long-lived roles
   ├─ measured fresh crossings ──► no existing foreign-role route
   └─ channels + app-server ─────► bridge plausible, but adds forbidden runtime/security surface
                                      └─► exclude from first release; revisit in separate task

Across every branch:
stable principal/role/channel live in the frozen contract
actual version/OS/tools/nonce/worktree live in dispatch-time evidence
provider runtime state never becomes project task authority
```

## Iteration Status

> **Mandatory block.** Every RES must include this, even for single-iteration research.

- **Iteration:** 3 of 2 (min) / 5 (max), normal sequential semantics after the two parallel predecessors.
- **Hypotheses tested:** H10 (field-supported G1–G7; G8 not controlled), H11 (single-premise form split; broader Claude feasibility open), H12 (supported as current first-release restriction only).
- **Hypotheses deferred:** None. H11 was tested to an evidence-limited verdict; the missing native run is an explicit future Phase D gate, not an unstarted question and not a blocker to Phase A planning.
- **Gaps discovered:** no Claude-native whole-TFW run; no teammate-worktree composition proof; installed Claude build below the current documented Windows cross-session floor; no controlled Codex G8 denominator; no in-scope direct mixed existing-session route.
- **Superseded decisions:** D4/D5 supersede iteration 2 D1's universal inference that the only creatable durable Claude delegate is headless; its measured `-p` continuity remains valid for that build. D8 narrows any permanent reading of H12 because current channels/app-server make a future bridge plausible.

### Open Threads (for next iteration)

> If no open threads — write "No open threads."

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | Claude-native acceptance before the Phase D Claude profile | Without it, documentation would be promoted into an execution promise and Helpdesk would be misused as the missing run | At Phase D entry, choose one C5/C6/C7/C8/C9 family and execute the exact eight-step gate with Claude measuring its own side |
| 2 | Controlled Codex G8 reliability | C1 supports mechanics but has no predeclared owner-turn/fork failure denominator | During the next suitable Codex team run, declare the autonomy timestamp and count owner turns, duplicate/silent tasks and replacements; do not delay Phase A merely to manufacture a trial |
| 3 | Mixed bridge value and security | Channels/app-server could change the answer only by creating a new runtime/transport boundary | Open a separate task only if mixed long-lived roles have independent value; test actual desktop-task reachability, auth, approvals, identity, trace and liveness |

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to review all three iterations, apply free refinements, transcribe A1 as `PROPOSED`, and plan the already-researched Phase A outcome under its existing VBSA landing gate. This is sufficiency for **current planning**, not evidence that a Claude profile or Codex G8 reliability has passed.
- [ ] **MORE NEEDED** — no fourth iteration is needed before current planning. The Claude-native run remains mandatory at the future Phase D profile gate.
- [ ] **BLOCKED** — no current blocker.

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 3 turns one provider-neutral-looking promise into an evidence-labelled release boundary. The
Codex managed-task profile has repeated field support for identity, direct routing, role separation,
worktrees and legal artifacts, but no controlled walk-away result; Claude has three distinct required
families plus two newer documented compositions, none with a native whole-TFW pass; mixed long-lived
roles lack an in-scope existing-session route and therefore stay outside the first release unless A1
is rejected. The key missed-by-design finding is that current Claude channels and Codex app-server
make a future bridge plausible while simultaneously proving why the present no-runtime task cannot
smuggle one in. The main limitation is deliberate and material: this Codex iteration did not run
Claude, cannot identify the exact Helpdesk executable/flags, and sampled RCFR/VBSA retrospectively.
The result is sufficient to plan and to place the remaining tests at the correct future gates, not to
claim a Claude profile or G8 reliability that has not been observed.

---

*RES — TFW_20260902-111644_CRATM: Provider-homogeneous execution profiles (Iteration 3) | 2026-09-05*
