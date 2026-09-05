# ONB — TFW_20260902-111644_CRATM / Phase A: Isolation and attribution for concurrent work

> **Date**: 2026-09-05
> **Author**: Codex (Executor)
> **Status**: 🟠 ONB — No blocking questions; autonomous grant applies
> **Parent HL**: [HL-TFW_20260902-111644_CRATM](../HL-TFW_20260902-111644_CRATM.md)
> **TS**: [TS Phase A](TS__phase-a__isolation_and_attribution.md)

---

## 1. Understanding

Phase A adds a prose-only, provider-independent protocol for isolated mutation-bearing runs, exact-path staging, and producer-attributed cross-session landing. The implementation is confined to the seven literal VALUE paths approved in the TS: three canonical Markdown files and four tracked workflow copies. It must preserve selective loading, Candidate-before-EV/RF ordering, exact Candidate reachability, and the immutable 7-file/160-LOC planning denominator while adding no runtime, transport policy, identity semantics, manifest change, test, or later-phase behavior.

## 2. Entry Points

- `.tfw/conventions.md` → `Commit Attribution` and `Anti-patterns (prohibited)`: canonical protocol, staging, landing, and measured failures.
- `.tfw/workflows/handoff.md` → commit and Candidate checkpoints: Executor-side exact-path enforcement without changing ONB→implementation/test→Candidate→EV/RF order.
- `.tfw/workflows/review.md` → Verify/Decide checkpoints: independent path-set, staging, landing, and Candidate checks without changing Purpose Check or accounting replay.
- `.agent/workflows/tfw-{handoff,review}.md` and `.claude/commands/tfw-{handoff,review}.md`: the four exact tracked copies named by the TS.
- `workspace/2026/TFW_20260902-111644_CRATM/phase-a/`: governing status/journal, approved TS, this ONB, later EV/RF, and lifecycle trace.
- Execution boundary: detached worktree `C:/Users/c0rpa/.codex/worktrees/75c7/steps-framework`, Git dir `D:/projects/research/steps-framework/.git/worktrees/steps-framework1`, common dir `D:/projects/research/steps-framework/.git`, starting at approval commit `29a5c8a98af52493d142c9872ca97a22a5db4eda`.

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|---|---|
| — | No blocking questions. | The approved autonomous execution grant satisfies the ONB gate. |

## 4. Recommendations (suggestions, not blocking)

1. Keep the workflow additions at the existing commit/Candidate and independent Verify checkpoints. A reference to `conventions.md` alone is too weak under selective reads, while duplicating the protocol body would deepen the documented attention debt.
2. Treat the TS's seven literal VALUE paths as the implementation and accounting authority. The current adapter manifest names `.agents/workflows/…`, but the approved selector and repository's tracked copies name `.agent/workflows/…`; changing or expanding that topology is explicitly outside Phase A.
3. Record actual cross-session landing as post-review work for the Phase Coordinator. During Executor evidence, verify the producer-shaped Candidate subject, changed-path history, and Candidate reachability; classify the not-yet-performed coordinator landing observation honestly rather than inventing it.
4. Keep every commit exact-path: inspect full status and cached names, stage only the named TRACE or VALUE set, and use `git commit --only -- <paths>` so a staged sibling cannot ride along.

## 5. Risks Found (edge cases, potential issues not in TS)

1. Workflow-copy multiplication makes small canonical additions count three times in Baseline→Candidate LOC. The canonical role edges must remain short enough that actual touched LOC stays below the owner-escalation ceiling and is measured before Candidate creation.
2. The protocol requires review before landing, while the Executor must finish EV/RF before review and is forbidden to perform coordinator landing. Landing-specific real-environment evidence is therefore temporally deferred; Candidate reachability and producer attribution are independently testable now.
3. This app-managed worktree is detached. The Candidate must be recorded by full SHA and remain reachable until the Coordinator lands and verifies it; equivalent bytes under a replacement SHA are not evidence.
4. A separate index prevents sibling-worktree staging, but it does not prevent broad staging of unrelated files inside this worktree. Exact paths remain mandatory from ONB onward.

## 6. Inconsistencies with Code (spec vs reality)

1. Phase HL and D73 call the workflow copies “manifest-declared,” and `.tfw/adapters/manifest.yaml` currently maps Antigravity commands to `.agents/workflows/tfw-{command}.md`; the approved TS, AC-4, Git index, and existing tracked copies instead use singular `.agent/workflows/tfw-{command}.md`. Phase A follows the literal approved selector and reports the topology mismatch without modifying the manifest or adding a VALUE path.
2. Master HL §7.2 rows 2 and 4 identify the quoted current NS2 clauses as principles 4 and 6. In the live `.tfw/README.md`, “Human authority, bounded delegation” is principle 5 and “Assurance proportional to risk” is principle 7. The links and quoted clauses resolve semantically, but the ordinal labels are stale and out of scope for Phase A.
3. TS AC-3 evidence requests a Phase A landing commit before worktree cleanup, while the canonical lifecycle requires review before landing and the Executor Role Lock forbids coordinator landing. Executor evidence will mark only that landing observation `DEFERRED` with the exact post-review dependency; it will not claim an action that has not occurred.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|---|---|---|---|
| 1 | Master 1 — PV0 `.tfw/README.md` NS1 | ✅ | Applied | Protocol and trace must preserve inspectability, authority, and continuation, especially exact Candidate reachability. |
| 2 | Master 2 — PV0 NS2, Human authority/bounded delegation | ✅ | Applied | HC-1, the fixed selector, denominator, stop conditions, and coordinator escalation implement the clause; the live ordinal is 5, not 4. |
| 3 | Master 3 — PV0 NS3 | ✅ | Applied | The deliverable stays prose over ordinary Git; no vendor-owned runtime or provider path becomes canon. |
| 4 | Master 4 — PV0 NS2, assurance proportional to risk | ✅ | Applied | Reuse role artifacts and one EV instead of adding a registry or parallel ledger; the live ordinal is 7, not 6. |
| 5 | Master 5 — PV1 Structural Enforcement | ✅ | Applied | Separate index plus exact-path commit gates replace an exhortation measured at 0/1. |
| 6 | Master 6 — PV1 Naming Creates Behavior | ✅ | Applied | Producer task/phase in the landing subject makes ownership recoverable from path history. |
| 7 | Master 7 — PV1 Portability | ✅ | Applied | POSIX and Windows TFW-owned locations are stated without adopting a provider path. |
| 8 | Master 8 — PV2 `knowledge/philosophy.md` F37 | ✅ | Applied | The mandate remains a ceiling; no new path, boundary, or budget authority is inferred. |
| 9 | Master 9 — PV2 `knowledge/philosophy.md` F38 | ✅ | Applied | Supports keeping Phase A cohesive and avoiding unrelated later-phase work. |
| 10 | Master 10 — PV3 D59 | ✅ | Applied | The protocol explicitly separates recoverability from locking and session separation from independent judgment. |
| 11 | Master 11 — PV3 D68 | ✅ | Applied | Paths remain stable; status is task-local; journal tokens provide uniqueness rather than identity. |
| 12 | Master 12 — PV3 D63 | ✅ | Applied | Frozen master/phase claims and the approved TS are read-only execution authority. |
| 13 | Master 13 — PV3 D64 | ✅ | N/A to implementation | Purpose adjudication belongs to the later independent Reviewer; implementation preserves the evidence needed for it. |
| 14 | Master 14 — PV3 D55 | ✅ | Applied | Commit subjects remain the searchable task/scope/role record and ground the landing rule. |
| 15 | Master 15 — PV3 D54 | ✅ | Applied | Canonical workflows and all four TS-named tracked copies must remain byte-identical. |
| 16 | Master 16 — PV3 D31 | ✅ | Applied | Existing file/state carriers are preserved; Phase A adds no runtime or new state carrier. |
| 17 | Master 17 — PV4 `conventions.md` rules 17–19 | ✅ | Applied | No self-widening or retrospective acceptance of scope/LOC growth. |
| 18 | Master 18 — PV4 `conventions.md` rules 20–21 | ✅ | Applied | Phase HL is derivation-only and is not edited by the Executor. |
| 19 | Master 19 — PV4 `conventions.md` §14 | ✅ | Applied | Three compact failure rows name the four measured occurrences without duplicating the rule body. |
| 20 | Master 20 — PV5 `knowledge/convention.md` F19 | ✅ | Applied | New headings and name grammar use one consistent casing/form per carrier. |
| 21 | Master 21 — PV6 `knowledge/process.md` F6 | ✅ | Applied | Frozen scope, Role Lock, and exact selectors prevent coordinator-style scope expansion. |
| 22 | Master 22 — PV6 `knowledge/process.md` F30 | ✅ | Applied | Each rule has a canonical definition plus the role checkpoint where it fires. |
| 23 | Master 23 — PV6 `knowledge/process.md` F7 | ✅ | Applied | Durable ONB, TS, EV, RF, status, and journal preserve context across sessions. |
| 24 | Master 24 — PV7 `knowledge/constraint.md` F11 | ✅ | N/A | The dated provider-capability claim is explicitly assigned to Phase E; Phase A adds no provider topology. |
| 25 | Master 25 — PV7 `knowledge/constraint.md` F12 | ✅ | Applied | Executor and Reviewer obligations are written in their workflow files, not left to tool memory. |
| 26 | Master 26 — PV7 `knowledge/constraint.md` F2 | ✅ | Applied | Existing over-limit workflows receive only the shortest materially necessary enforcement edges; exact counts go to EV. |
| 27 | Master 27 — PV7 `knowledge/risk.md` F1 | ✅ | Applied | Core basis for separate worktrees, full status inspection, exact paths, cached-set inspection, and foreign-hunk STOP. |
| 28 | Master 28 — PV7 `knowledge/stakeholder.md` F6 | ✅ | Applied | Autonomous grant removes routine owner gates without weakening the approved contract. |
| 29 | Master 29 — PV7 `knowledge/stakeholder.md` F7 | ✅ | Applied | Phase HL §3.1 was read as the rendered result before implementation effort. |
| 30 | Master 30 — PV7 `knowledge/stakeholder.md` F8 | ✅ | Applied | Parity and structural checks must finish silent/green rather than tolerate known failures. |
| 31 | Master 31 — PV7 `knowledge/environment.md` F3/F4 | ✅ | Applied | Landing remains subject-shaped and introduces neither a leading-slash filter nor message-wide `--grep`. |
| 32 | Master 32 — PV7 Assisted `team/README.md` | ✅ | N/A | Organization/project roles and Assisted automation semantics belong to Phase B, not Phase A. |
| 33 | Master 33 — PV3 D68, opaque event token | ✅ | Applied | Handoff and transition event filenames will use drawn opaque tokens; actor identity is not encoded in them. |
| 34 | Master 34 — PV3 D73 | ✅ | Applied | Preserve workflow-owned ordered reads and synchronize only the four literal tracked copies authorized by the TS; manifest mismatch is reported, not repaired. |
| 35 | Master 35 — PV3 D74/D75 | ✅ | Applied | Preserve selective role paths, unique headings, and existing Candidate/accounting order. |
| 36 | Master 36 — PV6 `knowledge/process.md` F39 | ✅ | Applied | Search confirmed defining/consuming/copy sites; the governing TS freezes the resulting seven-path delivery set. |
| 37 | Phase A1 — PV0 `.tfw/README.md` NS3 | ✅ | Applied | Prose protocol only; no script, hook, lock, daemon, or provider-owned canonical path. |
| 38 | Phase A2 — PV1 Structural Enforcement | ✅ | Applied | Worktree isolation is structural; staging rules cover legitimate shared-tree cases and local unrelated dirt. |
| 39 | Phase A3 — PV3 D55 | ✅ | Applied | Producer-attributed subject and `git log -- <path>` recoverability are the landing rule's mechanism. |
| 40 | Phase A4 — PV3 D59 | ✅ | Applied | Worktree isolation is expressly neither lock nor merge strategy. |
| 41 | Phase A5 — PV3 D68 | ✅ | Applied | An established worktree name is never rewritten; stable-path reasoning matches task directories. |
| 42 | Phase A6 — PV7 `knowledge/risk.md` F1 | ✅ | Applied | Exact staging and cached-name gates appear in both role surfaces and govern this phase's commits. |
| 43 | Phase A7 — PV7 `knowledge/environment.md` F3/F4 | ✅ | Applied | No shell-leading-slash or message-wide grep mechanism is introduced. |
| 44 | Phase A8 — PV6 `knowledge/process.md` F30 | ✅ | Applied | Canonical rules, workflow edges, and §14 failures each have distinct enforcement roles. |
| 45 | Phase A9 — PV7 `knowledge/constraint.md` F2 | ✅ | Applied | Baseline counts 9,791/2,013/2,102 were reproduced with `\S+`; final deltas and necessity will be recorded. |
| 46 | Phase A10 — PV3 D73 | ✅ | Applied | Ordered Read Contracts remain intact; adapter parity is tested against the TS's literal copy paths. |
| 47 | Phase A11 — PV3 D74/D75 | ✅ | Applied | No universal preamble or duplicated protocol body is added. |
| 48 | Phase A12 — PV4 `conventions.md` Design Rules | ✅ | Applied | Token density, inline enforcement, progressive disclosure, and adapter-safe command forms guide the edits. |
| 49 | Phase A13 — PV6 `knowledge/process.md` F39 | ✅ | Applied | Definition, consumers, copies, and verification sites were searched before the first implementation write. |

No new PV item is required. The manifest/singular-path and NS2-ordinal discrepancies are code/spec observations, not missing project knowledge.

---

*ONB — TFW_20260902-111644_CRATM / Phase A: Isolation and attribution for concurrent work | 2026-09-05*
