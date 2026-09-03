---
description: TFW Knowledge — consolidate fact candidates into verified project knowledge
---

# TFW Knowledge — Knowledge Consolidation Workflow

> **Role:** Coordinator
> **Output:** Updated `knowledge/` topic files, `KNOWLEDGE.md` §4 (index), `knowledge_state.yaml`
> **Trigger:** Manual (`/tfw-knowledge`) or gate in plan.md Step 2
> **Duration:** 5-20 minutes

> **🔒 ROLE LOCK: COORDINATOR**
> Permitted: reading all project artifacts, writing to KNOWLEDGE.md, `knowledge/` topic files, `.tfw/knowledge_state.yaml`.
> Forbidden: writing code, modifying RF/REVIEW/RES/HL/TS files (except adding `fact-candidates: processed` marker).

## Read Contract

Root instructions are already active. Read this workflow completely, then read the following
in order; shared ranges are addressed by unique heading.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | invoking task/phase `status.md` and `journal/`, when invoked from a task | current state before global material | task-local |
| 2 | `.tfw/project_config.yaml` → `tfw.knowledge` and `.tfw/knowledge_state.yaml` | limits, gate mode, processed digest state | project config/state |
| 3 | `.tfw/conventions.md` headings `Fact Categories` and `Knowledge Infrastructure` | category and file ownership | shared rule |
| 4 | `KNOWLEDGE.md` heading `Project Facts`, every current `knowledge/*.md`, and `.tfw/templates/knowledge/topic.md` | existing facts, counts, and output form | project knowledge/template |
| 5 | selected knowledge headings from only the pending task IDs reported in Phase 1 | batch inputs | task artifacts |
| 6 | user-approved facts from the current conversation | human-only input | user |

Full `conventions.md`, full `glossary.md`, `KNOWLEDGE.md` §§1–3, already-processed task
bodies, and derived indexes are not inputs. Missing or duplicate addressed headings are a
hard stop under `conventions.md` → `Context Selection`.

## Phase 1: Orient

1. Run `python .tfw/scripts/gen_index.py --knowledge-pending --format json`. This checker is
   read-only and hashes every resolvable current or legacy task by full identity.
2. If it exits nonzero, or `problems`/`removed_task_ids` is non-empty, **STOP**. Do not perform
   gate arithmetic or change knowledge/state over unresolved, ambiguous, malformed, or removed
   input.
3. If `migration_required` is true, the batch is every resolved task. Do not use the legacy
   sequence, date, or `last_consolidation_task` to skip any task. Otherwise the batch is the
   distinct `pending_task_ids`; zero is a no-op.
4. List topic-file fact counts and category coverage from the Read Contract, then present the
   orientation and the exact batch IDs.

## Phase 2: Gather

> **⚠️ Knowledge ≠ technical documentation.**
> Knowledge is what would be UNKNOWN without the human saying it: vision, priorities, emotions,
> business context, architectural philosophy, process corrections.
> Technical implementation details (tools config, API constraints, build errors) belong in tfw-docs.
>
> **YES**: "primary output = knowledge graph, not docs site", "close as MVP, don't stretch phases"
> **NO**: "MkDocs docs_dir cannot be project root", "use directory URLs not .md"

1. Scan only the batch tasks for headings named `Fact Candidates`, `Strategic Insights`,
   `Strategic Session Insights`, or `Execution Session Insights` in HL, RF, REVIEW, and RES
   artifacts, including their revisions, iterations, and phases. A task with none remains in
   the batch and will receive its explicit empty digest.
2. Review conversation history for the current session — extract facts from user messages not captured in artifacts
3. Check category coverage. Do not force a fact into an existing category; propose a topic
   file from the template when its approved category has none.
4. Present gathered candidates to user:

```
Found {N} candidates from {M} artifacts:
| # | Candidate | Category | Source | Confidence |
|---|-----------|----------|--------|------------|
```

> **Priority**: §11/§7 insights are pre-filtered strategic signals → higher value than standard FC. Standard FC mix strategic + technical; apply Human-Only Test more strictly.

🛑 **WAIT 1** — user reviews candidates and supplies any human-only facts.

## Phase 3: Consolidate

For each candidate:

1. **Human-Only Test** — would this fact be unknown without the human saying it?
   If an agent can discover it by reading code, running commands, or checking docs → **reject**
2. **Deduplicate** — check if fact already exists in topic files → skip
3. **Contradiction check** — if contradicts existing fact → flag, ask user
   - DO NOT auto-resolve contradictions — present both, user decides
4. **Verification**:
   - ≥2 independent sources → ✅ verified
   - 1 source → present to user for confirmation or skip
5. Prepare, but do not write, the exact topic-file changes and source markers. A processed
   source marker is `> fact-candidates: processed YYYY-MM-DD`; no other source content changes.
6. Derive proposed statistics from the current fact inventory plus the explicit batch
   disposition ledger. Never blind-increment a stored total.
7. Present promoted, merged, rejected, deferred, unchanged, marker, index, and statistics
   changes as the final write plan.

🛑 **WAIT 2** — user approves the exact changes before any source effect or state write.

## Phase 4: Update

1. Review existing facts for staleness; flag them and never auto-delete.
2. Apply only the approved topic-file and source-marker effects, then update `KNOWLEDGE.md`
   `Project Facts`. Do not write §§1–3.
3. Re-run the pending checker after all approved effects. The resolved task-ID set must match
   the approved batch universe; otherwise **STOP** and reconcile the newly changed input.
4. Build the final `processed_task_digests` map from the post-marker
   `current_task_digests`: update exactly the approved batch, retain unchanged prior entries,
   and, on migration, require every current task ID. Validate every digest as 64 lowercase hex.
5. Write `.tfw/knowledge_state.yaml` **state last**, after source markers, topic facts, index,
   post-marker recomputation, and validation all succeed. Keep `last_consolidation_date` as
   audit metadata and the approved derived statistics. After successful migration remove both
   `last_consolidation_seq` and `last_consolidation_task`; before success leave the old live
   state byte-for-byte unchanged.
6. Present the committed batch IDs, post-marker digests, dispositions, statistics, and any
   staleness warnings. If interrupted before state, retry the same batch and deduplicate it
   against current topic facts; the effect must converge without a duplicate fact or increment.

## Behavior Rules

- **DO NOT invent facts** — only consolidate from artifacts and conversation
- **DO NOT auto-resolve contradictions** — ask user
- **DO NOT delete facts** without user confirmation
- **DO NOT modify RF/REVIEW/RES/HL content** — only add the approved processed marker
- **DO NOT default all facts to existing categories** — use the addressed category table
- **DO NOT write state before approved source effects and post-marker digest recomputation**
