# Knowledge: Process

> Topic file for `process` facts. Updated by `/tfw-knowledge`.
> See KNOWLEDGE.md §5 for the index.

| # | Fact | Verified | Source(s) | Added |
|---|------|----------|-----------|-------|
| F1 | TFW = teamwork. The framework's purpose is to enable collaboration between multiple agents and humans | ⚠️ 1 source | Chat TFW-18 (user) | 2026-04-03 |
| F2 | `/tfw-knowledge` = separate explicit workflow, not part of tfw-docs. tfw-docs = quick per-task pass, knowledge = product and team knowledge requiring structure, metrics, rigor | ⚠️ 1 source | Chat TFW-18 (user) | 2026-04-03 |
| F3 | Agents MUST scan conversation history before writing Fact Candidates — knowledge comes from the human, from their decisions, messages, and interactions with the world. Chat = primary source of knowledge | ⚠️ 1 source | Chat TFW-18 (user) | 2026-04-03 |
| F4 | The best fact candidates come from user emotions and frustration in chat, not from structured artifact sections. When the user is angry, excited, or sharing insights during research — that's the primary signal for strategic knowledge | ⚠️ 1 source | REVIEW-18B FC#2, chat TFW-18B | 2026-04-03 |
| F5 | Naming creates behavior in AI agents more effectively than explanation. Right terminology triggers right associations. «Маленький промпт + точные термины > длинный промпт с объяснениями». Claude «dreaming» = 1 word replacing paragraphs. TFW adopted: OODA, Sufficiency Verdict, Trust Protocol, Progressive Disclosure | ✅ verified | RES TFW-22 FC#2, REVIEW TFW-22 FC#2 | 2026-04-04 |
| F6 | AI agents follow numbered steps + gates perfectly but lose focus in prose workflows. Workflow = algorithm (steps + gates + refs), not info dump. Observed: executor doesn't deviate from TS steps. Confirmed across TFW-22 and prior tasks | ✅ verified | RES TFW-22 FC#3, REVIEW TFW-22 FC#3 | 2026-04-04 |
| F7 | AI should write findings to file FIRST, then summary to chat. Protects against session interruption/death. Adds ~10-15% tokens, not 100% | ✅ verified | RES TFW-22 FC#5, REVIEW TFW-22 FC#6 | 2026-04-04 |
| F8 | When AI crashes mid-workflow and user presses "continue", all 🛑 WAIT gates are lost. 6/6 gates violated in TFW-23 research. Crash recovery not built into TFW — need mechanism to re-read workflow + determine current gate. Gate skipping → feature loss → user trust erosion | ✅ verified | RF-A TFW-23 FC#3, RF-B TFW-23 FC#1, REVIEW TFW-23 FC#1 | 2026-04-04 |
| F9 | TFW has 4 roles: Coordinator, Researcher, Executor, Reviewer. Researcher extracted from Coordinator following TFW-8 pattern (Reviewer extraction). Trigger: TFW-23 crash caused 6/6 gates violated — one role + two functions = role confusion. After crash, "Coordinator" skipped stages and wrote HL/TS directly | ✅ verified | RF-A TFW-24 FC#1, REVIEW TFW-24 FC#1 | 2026-04-04 |
| F10 | Resume Protocol (base.md Step 0): check filesystem state → resume from first missing file. Resolves F8 crash problem. No chat history dependency — any agent in any chat can pick up research | ✅ verified | RF-A TFW-24 FC#4, REVIEW TFW-24 FC#1 | 2026-04-04 |
