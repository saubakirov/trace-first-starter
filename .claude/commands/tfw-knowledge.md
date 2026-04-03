---
description: TFW Knowledge — consolidate fact candidates into verified project knowledge
---

# TFW Knowledge — Knowledge Consolidation Workflow

> **Role:** Coordinator
> **Output:** Updated `KNOWLEDGE.md` §5, topic files in `knowledge/`, updated `knowledge_state.yaml`
> **Trigger:** Manual (`/tfw-knowledge`) or gate in plan.md Phase 0
> **Duration:** 5-20 minutes

> **🔒 ROLE LOCK: COORDINATOR**
> Permitted: reading all project artifacts, writing to KNOWLEDGE.md, `knowledge/` topic files, `.tfw/knowledge_state.yaml`.
> Forbidden: writing code, modifying RF/REVIEW/RES/HL/TS files (except adding `fact-candidates: processed` marker).

## Prerequisites

1. Read `.tfw/knowledge_state.yaml` — current state, last consolidation seq
2. Read `KNOWLEDGE.md` — current knowledge index
3. Read all topic files in `knowledge/` — current verified facts
4. Read `.tfw/PROJECT_CONFIG.yaml` → `tfw.knowledge` section for limits

## Phase 1: Orient

- Understand current knowledge state: how many facts, which categories exist, when was last consolidation
- Note `last_consolidation_seq` and compute task range to scan
- List topic files and their fact counts
- Present orientation summary to user

## Phase 2: Gather

> **⚠️ Conversation history is the primary source of strategic knowledge.**
> The human's messages contain domain insights, stakeholder priorities, business context,
> and concerns that artifacts miss. Look for decisions, emotions, and data shared during work.
> Technical implementation details belong in tfw-docs — here we capture what informs decisions.

- Scan all RF, REVIEW, and RES files for tasks since `last_consolidation_seq`
- **Review conversation history** for the current session — extract facts from user messages that weren't captured in artifact Fact Candidates
- Collect Fact Candidates from each artifact's Fact Candidates section
- If no candidates found in any artifact or conversation — note in stats, inform user, skip to Phase 4
- Present gathered candidates to user:

```
Found {N} candidates from {M} artifacts:
| # | Candidate | Category | Source | Confidence |
|---|-----------|----------|--------|------------|
```

🛑 **WAIT** — user reviews candidates before consolidation

## Phase 3: Consolidate

For each candidate:

1. **Human-Only Test** — would this fact be unknown without the human saying it?
   If an agent can discover it by reading code, running commands, or checking docs → **reject**
2. **Deduplicate** — check if fact already exists in topic files → skip
3. **Contradiction check** — if fact contradicts an existing fact → flag, ask user
   - DO NOT auto-resolve contradictions — present both facts, user decides
4. **Verification**:
   - If ≥2 independent sources → mark as ✅ verified, add to topic file
   - If 1 source → present to user for confirmation or skip
5. **Write to topic file** — add fact to appropriate `knowledge/{category}.md`
   - Create new topic file from `.tfw/templates/TOPIC_FILE.md` if category doesn't exist
   - Check `max_facts_per_topic` limit — if exceeded, ask user which facts to prune
   - Check `max_topic_files` limit — if exceeded, ask user to merge categories
6. **Mark processed** — add marker to source artifact:
   ```
   > fact-candidates: processed YYYY-MM-DD
   ```

Present consolidation results to user before finalizing.

🛑 **WAIT** — user approves changes before writing

## Phase 4: Prune

- Review existing facts for staleness (source > 20 tasks ago or source artifact deleted)
- Flag stale facts for user review — DO NOT auto-delete
- Check limit compliance:
  - `max_facts_per_topic` per topic file
  - `max_topic_files` total
  - `max_index_facts_lines` for KNOWLEDGE.md §5
- Update `KNOWLEDGE.md` §5 compact index:
  - Category counts + links to topic files
  - Respect `max_index_lines` for total KNOWLEDGE.md size
- Update `.tfw/knowledge_state.yaml`:
  - `last_consolidation_seq` → current task seq
  - `last_consolidation_date` → today
  - Stats: total_facts, verified, unverified, rejected, candidates_processed, sources_scanned
- Present summary to user

## Behavior Rules

- **DO NOT invent facts** — only consolidate from artifacts
- **DO NOT auto-resolve contradictions** — ask user
- **DO NOT exceed topic file limits** without user approval
- **DO NOT delete facts** without user confirmation
- **DO NOT modify RF/REVIEW/RES content** — only add the `fact-candidates: processed` marker

## Anti-patterns

- Agent invents facts not found in any artifact
- Agent auto-resolves contradictions without asking user
- Agent skips Orient and jumps to Gather
- Agent writes facts without user approval
- Agent exceeds configured limits without asking
- Agent modifies artifact content beyond the processed marker

## Limits

> Configured in `.tfw/PROJECT_CONFIG.yaml` (`tfw.knowledge`).
> Values below are defaults. Override in PROJECT_CONFIG for your project.

| Parameter | Default | Config key |
|-----------|---------|------------|
| Consolidation interval | 5 tasks | `interval` |
| Gate mode | hard | `gate_mode` |
| Max facts per topic | 50 | `max_facts_per_topic` |
| Max topic files | 8 | `max_topic_files` |
