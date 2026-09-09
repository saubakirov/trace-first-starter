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

### Canonical Knowledge Gate algorithm

This addressed algorithm is the complete ordinary Full route. Implement it with semantic YAML
support already available to the acting agent; do not require, import, or invoke a repository
helper, Python, or PyYAML. A disposable independent implementation is acceptable only when it
produces these exact semantic results. Regex-only YAML interpretation is prohibited.

1. Semantically parse `.tfw/project_config.yaml`. Require `tfw.knowledge` to be a mapping,
   `gate_mode` to be exactly `off`, `soft`, or `hard`, `interval` to be a positive integer,
   and `tfw.task_containers` to be an ordered non-empty list of repository-relative directory
   paths. A missing, unreadable, duplicate, or wrong-shaped value is indeterminate: **STOP**.
2. In each configured container, inspect direct child directories plus direct children of a
   four-digit year directory. Recognize only these whole directory-name grammars: current
   `PREFIX_YYYYMMDD-HHMMSS_ABBR` where prefix and abbreviation are uppercase alphanumeric;
   dirty-era `YYYYMMDD-HHMMSS__slug`, whose whole name is its ID; and legacy
   `PREFIX-N[__slug]`, normalized only to `PREFIX-N`. A bare timestamp is not an ID. Sort
   legacy numerically first, dirty-era by stamp+slug second, and current by stamp+prefix+abbr
   third. Report every other candidate directory. If two paths normalize to one ID, report
   both; do not choose either.
3. For every recognized task, recursively select only Markdown artifacts whose basename
   starts `HL-` or `HL__`, `RF__`, `REVIEW__`, or `RES__`. Sort by repository-relative POSIX
   path. Files with other basenames do not supply Knowledge Gate sections.
4. Read each selected file as UTF-8 and normalize CRLF or CR to LF. Outside fenced code blocks
   (` ``` ` or `~~~`), select Markdown headings level 1–6 whose title, after removing an
   optional leading section number and optional trailing `🟢 FREE`, is exactly `Fact Candidates`,
   `Strategic Insights`, `Strategic Session Insights`, or `Execution Session Insights`, or
   begins that exact name followed by ` (`. The body is every byte after that heading through
   the line before the next heading of equal or higher rank. Preserve nested headings and the
   body's final LF. Never interpret heading-like text inside a fence.
5. For each task, order selected sections by repository path then occurrence. For every
   `(path, heading, body)` tuple, feed UTF-8 `path`, one NUL byte, UTF-8 canonical heading,
   one NUL byte, then UTF-8 LF-normalized body into one SHA-256 stream. A task with no selected
   sections feeds exactly two NUL bytes. The lowercase 64-hex result is that task's current
   digest.
6. Semantically parse `.tfw/knowledge_state.yaml` and require a `knowledge` mapping. If the
   file/mapping is missing or unreadable, **STOP**. If `processed_task_digests` is absent, this
   is an explicit migration state; otherwise require a mapping from whole normalized task IDs
   to lowercase 64-hex digests. Invalid keys or values are indeterminate.
7. `removed_task_ids` is the sorted set of processed IDs absent from current discovery.
   `pending_task_ids` is the sorted set of current IDs whose digest differs from the processed
   value. Any unreadable selected input, unmatched path, collision, digest-state error,
   or removed ID makes the input indeterminate: report every problem, perform no threshold
   arithmetic, and change no knowledge or state.
8. With determinate input, an absent digest map makes the batch every current task; otherwise
   the batch is the distinct pending IDs. In `off` mode, report `skip`. In `soft` mode, report
   the batch count over the interval and continue. In `hard` mode, count below the interval
   means continue; count at or above it means **STOP** and route to `/tfw-knowledge`.

After applying the algorithm, list topic-file fact counts and category coverage from the Read
Contract, then present the exact batch IDs. A zero batch is an explicit no-op. Do not use legacy
sequence, date, `last_consolidation_task`, a generated index, or an optional diagnostic report
as authority.

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
3. Re-run the canonical Knowledge Gate algorithm after all approved effects. The resolved task-ID set must match
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
   Return the actual changed outputs and their effects on accepted claims, with the selected
   Applied/N/A marker, to the existing Coordinator for `conventions.md` → `Closing and record
   recovery`. Changed final claims need that route's affected checks and independent judgment;
   this return grants no acceptance, extra capture cycle or broader processed batch.

## Behavior Rules

- **DO NOT invent facts** — only consolidate from artifacts and conversation
- **DO NOT auto-resolve contradictions** — ask user
- **DO NOT delete facts** without user confirmation
- **DO NOT modify RF/REVIEW/RES/HL content** — only add the approved processed marker
- **DO NOT default all facts to existing categories** — use the addressed category table
- **DO NOT write state before approved source effects and post-marker digest recomputation**
