# Task: Maintain and Evolve the Canonical Trace-First Framework

## Objective
Provide a portable, domain-agnostic workflow that converts any AI chat into a structured project with a repeatable loop: **Context → Analysis → Action**, capturing short Summaries in `STEPS.md`. The framework must work for writing (reports, contracts), analytics, research, code, and full product deliveries.

## In-Scope
- Clear rituals and artifacts (`README.md`, `AGENTS.md`, `STEPS.md`, `TASK.md`, optional `digest.txt`)
- Universal operating modes for both text and code (Discuss/Scope, Plan, Produce, Edit/Refactor, Test/Review, Publish/Deploy)
- Language auto-detection; **Don’t be sycophantic**; **No placeholders**
- Exact Summary format appended to every agent reply
- Security posture: local execution, no plain-text secrets, env-vars with documentation

## Out-of-Scope (for this repo)
- Storing real secrets or proprietary data
- Domain-specific examples larger than needed for illustration (keep root canonical and compact)

## Definition of Done (DoD)
- The root contains: `README.md`, `AGENTS.md`, `TASK.md`, `STEPS.md`, `KICKOFF_midchat.txt`, `KICKOFF_newchat.txt`
- Reading `README.md` alone is sufficient for a human/agent to start and succeed
- `AGENTS.md` enforces: language auto-detect, **no sycophancy**, **no placeholders**, Summary discipline
- `STEPS.md` contains at least one valid Summary entry; the format is consistently followed
- Kickoff prompts include the canonical repository link and a non-browsing fallback
- Any change that affects ritual/format includes a short rationale and updates this `TASK.md` (changelog note)

## Governance & Evolution
- Propose improvements via PRs or inline diffs in agent replies
- Keep the root flat and canonical; prefer updating this README over adding folders
- Versioning (lightweight): semantic-ish tags (e.g., `v1.0`, `v1.1`) when rituals or formats change

## Risks & Mitigations
- **Risk**: loss of context if Summaries aren’t maintained → **Mitigation**: Summary is mandatory at the end of every agent reply
- **Risk**: verbosity and token costs → **Mitigation**: flat root, minimal necessary text, explicit reading order
- **Risk**: drift between docs and practice → **Mitigation**: “Self-evolution” rule and PR/patch habit

## Initial Milestones
1) v1.0 — Canonical root published; kickoff prompts point to the canonical repo
2) v1.1 — Add concise examples for text deliverables (report/contract skeleton) and code deliverables (script + tests), kept inside README
3) v1.2 — Add optional review checklists (docs/code) while keeping root flat
