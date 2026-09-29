# Daily Task — 20260929-130629_single-phase-agent-mode: Single-phase agent mode for Claude Code and Antigravity

## 1. Source and attribution

- Human requester and acceptance authority: the project owner (`owner:saubakirov` in task records)
  in this Claude Code desktop chat; no delegated Full-role authority is inferred.
- Worker: Claude Code desktop session `claude-code:session:local_42b07c8b-8152-45df-aea6-486d58b83e7f`
  (model `claude-opus-5-5`), worktree `hungry-moser-da2ce2`, branch `claude/hungry-moser-da2ce2`.
- Observed before the first product write: `2026-09-29T13:06:29+05:00`.
- Owner's request (this chat), in answer to the proposal to delete the Claude profile's dated
  section with its three references: «да, удаляй и сливай в мастер. а работа однофазным агентом
  должна быть легальным выбором для для клод или антигравити если задача реально небольшая, мы уже
  раза 3 ьак делали работает отлично. это там тоже запрещено? когда будешь делать правки я хочу
  видеть где что куда посему уенно цель точно точечно»
- Related: `daily/2026/20260929-122413_claude-profile-neutral-label/task.md` (closed; found the
  section's contradiction afterwards in chat); `workspace/2026/TFW_20260929-003444_LFD/`
  HL §4.1 records the owner's choice of in-session agents on 2026-09-29, and its ONB notes that the
  Claude profile forbids them.

## 2. Goal, Value and Boundaries

Goal: (1) the Claude Code profile no longer carries its “Dated source and current check” section,
whose second paragraph argues for a mode the profile forbids and whose first repeats rules stated
elsewhere; (2) the Claude Code and Antigravity profiles offer a single-phase agent mode as a legal
owner choice for a really small one-phase task.

Value: the profile an agent reads at every new task stops contradicting itself, and the owner's
working practice (about three runs with good results, by the owner's account) becomes a bounded,
legal option with its safeguards instead of a per-task exception.

Boundaries: change only `.tfw/adapters/claude-code/coordinator.md`,
`.tfw/adapters/antigravity/coordinator.md`, one `[Unreleased]` entry in `.tfw/CHANGELOG.md`, and this
record. The Codex profile and the Codex template's own ban stay as they are (not requested). The
shared rules stay as they are: they do not tie roles to full chats. The Antigravity dated section and
its PCUX sentence (inventory items of the related record) stay. Merge into local `master` is
authorized; push is not.

Completion oracle: for a really small one-phase task neither profile forbids the mode, and outside
it every prohibition stays; the deletion matches the text shown to the owner; the profiles have no
copies; the local guard is clean; the configured tests pass.

## 3. Context before action

- Base: `master` at `b2638056aeea9daa34726062952965766f57ada9` (this branch fast-forwarded to it).
  Inputs, blob and SHA-256: Claude profile `fec79d213c3f230f2418778df774c0cef52a8d4f`
  `41ecb0034f94f59af7ed1ae18735f17c7f08cdd66f7441c65a124eaf034c8914`; Antigravity profile
  `dcc2c7ccdc41cdcdc961cfdc3c67951c853414b8`
  `b27f023cbb1627618aeaec842c5046c0e233866bc67c099064ea77716486263f`; changelog
  `ee565068a41ea2559b4b49fcd80db3e6c316cd85`
  `b54e6c1b245fb673744fbd9c4d2b2fe5a584e371b682ee772d8ace9b19e5656c`.
- Where the mode is forbidden today: Claude profile lines 9 (only the full-chat route is offered),
  17 (“No subagent substitutes …”), 47–48 (“still need distinct full role chats”) and 52
  (“Historical subagent reports … not admission …”); Antigravity profile lines 8–10 (only the
  full-chat route), 16 (“A hidden subagent is not a TFW role unit.”) and 40 (“still need distinct
  full role chats” and “Earlier subagent observations … prove no complete run.”).
- Where it is not forbidden: `.tfw/conventions.md` “New-task startup card” asks for distinct roles and
  a separate choice of who starts agents, not full chats; its working unit is directly addressable by
  its parent. `CLAUDE.md`, `.agents/rules/tfw.md`, the workflows and the glossary have no such ban.
  Only `.tfw/adapters/codex/AGENTS.md.template` bans subagents, for Codex.
- History: `v3.6.0` and `v3.6.1` allowed separate subagents for a small one-phase task in both
  profiles (Claude “Conditional compact route”). PCUX `46f37928` turned it into an offered
  “Single-phase subagent mode” and added the 2026-09-27 paragraph as its support; ATC `7dfed8bf`
  removed the mode before `v3.7.0` and added the bans, leaving that paragraph and the cut Antigravity
  sentence “… prove no complete run.” behind.
- Mutation owner: none for these files. Active LFD commits to `master` but its TS rev2 change table
  names neither profile nor the changelog; SHI and TEQM do not touch them.
- Prior-work lookup: the Related records above; no other Daily or knowledge record on this mode.
- North Star fit: NS2.2, the removed section is repetition plus a contradiction; NS2.5, the mode is
  the owner's explicit choice, bounded to one small phase; NS2.7, the safeguards of 3.6.1 return with
  it (own workflow per role, fixed Candidate, a new Reviewer, exit to full chats).
- Consequential question: none open. The owner set the goal; the wording is this worker's and is
  shown to the owner with each change.

## 4. Result, decisions and check

Pre-action checkpoint: no product change is applied yet and no check result is claimed.

## 5. Next or close

Next: apply the deletion, then the mode, then the changelog entry; check; merge into local `master`;
show the owner every change with its place, reason and purpose.
