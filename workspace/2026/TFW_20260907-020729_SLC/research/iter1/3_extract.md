# Extract — What do we NOT see?
> **Mindset:** Analyst. Make the configuration space explicit before selecting it.
> **Test:** Reveal combinations omitted from the initial workspace-versus-tasks framing.
> Parent: [HL SLC](../../HL-TFW_20260907-020729_SLC.md)
> Goal: One workspace default with compatible historical access.

## Configuration Space

Codes and dimension meanings come from [Gather](2_gather.md). All 27 combinations are representable; their contract compatibility is evaluated in Challenge.

| Config | Representation | Digest treatment | Recovery |
|---|---|---|---|
| C1 | A | A | A |
| C2 | A | A | B |
| C3 | A | A | C |
| C4 | A | B | A |
| C5 | A | B | B |
| C6 | A | B | C |
| C7 | A | C | A |
| C8 | A | C | B |
| C9 | A | C | C |
| C10 | B | A | A |
| C11 | B | A | B |
| C12 | B | A | C |
| C13 | B | B | A |
| C14 | B | B | B |
| C15 | B | B | C |
| C16 | B | C | A |
| C17 | B | C | B |
| C18 | B | C | C |
| C19 | C | A | A |
| C20 | C | A | B |
| C21 | C | A | C |
| C22 | C | B | A |
| C23 | C | B | B |
| C24 | C | B | C |
| C25 | C | C | A |
| C26 | C | C | B |
| C27 | C | C | C |

## Findings

### E1: The jobs can be separated without moving a source
Representation A admits `task_containers: [workspace]` and optional `historical_containers: [tasks]`; creation and current discovery use the former, while exact historical resolution and docs use the ordered union. Representation B embeds these roles in each entry. Representation C needs subtraction for current discovery while retaining a mixed aggregate. In each case the historical reader can keep the existing ID grammar and output mapping. [W3C's URI design note](https://www.w3.org/Provider/Style/URI) supports separating persistent public addresses from reorganized storage; this is external rationale, not evidence that the current compiler already understands history.

### E2: Recovery is independent of the final schema
A plain historical list does not require a second digest map. Conversely, an elaborate schema does not solve interrupted state writes. C1 (plain list, one-time exact digest reconciliation, existing update recovery) and C7 (plain list, separate historical digest map, existing recovery) illustrate this independent choice. C7 was not proposed in the Briefing and remains visible for challenge, rather than being eliminated by omission.

### E3: A two-file change has observable intermediate states
Let U be the initial active container set, H the verified historical task-ID set, P the prior digest map, and A the remaining active IDs. Target config excludes H's container; target map is P with only keys in H removed. Updating config before state makes P minus A nonempty. Updating state before config can make H temporarily pending. Neither order alone proves all operations see a finished migration. Recovery must preserve authority, exact membership, prior values and current project work; it must not rely on a success receipt that has not yet been sealed.

### E4: A narrow exception is different from overwriting knowledge state
The target update guide could authorize only the verified historical keys in `processed_task_digests`; unrelated digests, stats, dates and knowledge content remain project state. Removing a container is not knowledge consolidation and cannot mark a previously unprocessed task as processed. Empty/missing digest maps need no invented retired entries. A stale remembered ID outside H remains a real problem. This can be expressed without redesigning the unrelated gate threshold.

## Checkpoint

| Found | Remaining |
|---|---|
| Complete 27-row space; reader-role separation; distinct digest and write-order choices | Reject incompatible alternatives using the receiver and interrupted-state probes; choose a defensible recovery scope |

**Sufficiency:** external source used: YES; Briefing gap closed for Extract: YES; complete configuration space built: YES.

Stage complete: YES
Decision: close Extract and proceed to Challenge within the owner's research authorization. No schema or product change has been applied.
