# Extract — What do we not see?

> **Mindset:** Analyst. Make combinations and their dependency conditions visible before ranking.
> **Parent:** [HL-TFW_20260923-223151_PTW](../../HL-TFW_20260923-223151_PTW.md)
> **Goal:** Map coherent name, Trace location/form and distribution combinations for bounded one-worker work.
> **Producer / route:** `codex:thread:local:01a0d505-d0b4-76f2-ad95-58f1bf9cfe2e` → Coordinator `codex:thread:local:01a0cf4d-9254-7633-9ba9-393b0eb8e802`; dispatch `journal/20260925-010738__dispatch__ef88.md`, frozen HL `515b837`.

## Configuration Space

Gather's six dimensions have many theoretical combinations. These ten coherent configurations span each location and packaging boundary, including combinations absent from the Briefing. Codes `D1`–`D6` refer to exact Gather dimension names; an option appearing here is not an endorsement.

| Config | D1 Trace location | D2 Record boundary | D3 Distribution boundary | D4 Name and identity | D5 Relation/discovery | D6 Local form evolution |
|---|---|---|---|---|---|---|
| C1 | Dated `daily/YYYY/id/` | One `task.md` | Optional package with owned template | `tfw-daily-task`, timestamp/slug | Bounded search + exact links | Package version for new records |
| C2 | Dated `daily/YYYY/id/` | SenseLab triad | Project-local skill copy | `tfw-daily-task`, timestamp/slug | Bounded search + exact links | Project pins local form |
| C3 | Beside current object | Small decision section in current product document | Skill-bundled resource | `tfw-task`, object-scoped heading | Object navigation + exact links | Project pins local form |
| C4 | Existing commit | Structured commit message/body and trailers | Skill-bundled resource | `tfw-quick-task`, commit SHA | Commit/object search | Per-record inline form |
| C5 | Existing PR/issue | PR/issue description with selected Trace | Project-local skill copy | `tfw-task`, PR/issue ID | Host search + exact links | Host template changes only new records |
| C6 | Git note attached to commit | One structured note | Optional package with owned template | `tfw-daily-task`, commit SHA | Note ref search | Package version for new notes |
| C7 | Dated `daily/YYYY/id/` | One `task.md` | Full manifest command | `tfw-daily-task`, timestamp/slug | Subject folders | Upstream updates receiver |
| C8 | Beside current object | Task-local record + current product source | Optional package with owned template | `tfw-daily-task`, object-scoped ID | Object navigation + exact links | Project pins local form |
| C9 | Dated `daily/YYYY/id/` | One `task.md` | Skill-bundled template copied on entry | `tfw-daily-task`, timestamp/slug | Generated read-only view | Package version for new records |
| C10 | Existing non-code deliverable document | Small source/result/check/next section within it | Optional package with owned template | `tfw-daily-task`, document ID | Exact document links | Per-record inline form |

## Findings

### E1 — Trace completeness is a property of content plus reachability

**Source-backed observations:** The SenseLab sticker Task points to the current product catalogue and retains source-message IDs, changed briefs, verification and a precise non-publication claim. The Helpdesk interview kit Task separates the deliverable from UPM's formal state and names its owner handoff. [GitHub's commit permalink rule](https://docs.github.com/en/repositories/working-with-files/using-files/getting-permanent-links-to-files) makes an exact revision addressable. [Git's trailer syntax](https://git-scm.com/docs/git-interpret-trailers) makes short structured commit metadata parsable; it does not prescribe TFW fields or prove that future workers will find and read them. [GitHub issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms) support structured fields in a host-managed issue.

**Researcher inference:** C4 can preserve a tiny code repair's Goal, human source pointer, result, check and next action in a reachable commit body without a new folder if the source is already durable and allowed to be linked. C5 can do something similar where the project already governs work through issues/PRs, but a host record alone is a provider dependency unless an ordinary-file or export-equivalent is part of the project's current context. C10 could serve a stable non-code document only when the request/decision section is actually kept with the document, has appropriate access, and is not overwritten by later edits. The same fields in an inaccessible or transient surface do not pass NS1.

### E2 — The current candidate can lose on a measurable boundary

These are **challenge conditions**, not cost findings or a preferred ranking:

| Candidate | It can outperform a dated folder if… | It loses if… | Evidence needed |
|---|---|---|---|
| C3/C8 object-adjacent | repeated requests concern one stable object and the next worker starts from that object | ownership/access changes, one task crosses several objects, or history obscures current truth | resume a repeat request from object source and trace links; check authority and old/current separation |
| C4 commit body | tiny code change already has a durable commit and a complete, linked body readable during ordinary code review | work is uncommitted/non-code, commit is squashed/rebased without preserved link, or material source/check/next is omitted | compare a real small repair's commit against the selected-Trace checklist and a second-worker retrieval |
| C5 PR/issue | project already uses it as a durable work record and can expose the necessary selected Trace to authorized participants | host access, export and long-term portability fail; issue/PR is absent for local or confidential work | inspect a real host workflow and an ordinary-file-equivalent route |
| C10 document section | non-code deliverable itself stays authoritative and carries source, actual state and continuation | later edits erase historical decision or document is only a draft/output | resume from the document after a material revision |
| C2 triad | a request changes meaning several times or local attribution law requires complete messages | routine one-shot work repeatedly reads/writes three files with no decision benefit | compare actual read/write counts and missed decisions on matched tasks |

The matrix separates source facts from **estimated** cost. No measured per-task token/time or retrieval success rate exists yet; “outperform” names a falsifiable test, not an observed performance claim.

### E3 — Distribution has two different update boundaries

**Source-backed observations:** `.tfw/adapters/manifest.yaml` and `.tfw/adapters/README.md` declare ten Full role routes. `.tfw/workflows/init.md` installs their targets; `.tfw/workflows/update.md` repairs those same copies and preserves unrelated receiver content. The SenseLab skill already uses one `.agents/skills/` source and a Claude entry, but its records say independent multi-provider invocation was not verified.

**Researcher inference:** C7 changes the Full command contract and its receiver parity checks; it is not a free way to get updates. C1 and C9 need a separately explicit optional-package source/version/receiver map, plus a rule for what happens when the project has changed its local template. A skill-bundled template can avoid sharing Full's `.tfw/templates/`, but bundled resources may still be copied into provider-specific locations and drift unless one source and receiver verification are defined. C2 leaves proven SenseLab practice intact but project copies have no automatic generic update path.

### E4 — Name and relation effects remain open

The field `tfw-daily-task` name benefits from current use, while “daily” may imply cadence or low consequence. The neutral `tfw-task` candidate collides with the retired `/tfw-task` history named in HL §7.2; `quick` may similarly encourage underchecking. A timestamp/slug helps human navigation, but the slug is mutable semantic decoration: stable links need the immutable whole ID, and collision handling must not assume one writer or one time zone. Object-scoped IDs need a policy when the object is renamed or a task crosses objects. Subject folders and journals only help if retrieval improves enough to justify mutable categories and another maintained file; no observed failure yet establishes that threshold.

### E5 — Additional configuration missing from the initial HL comparison

C6, a Git note attached to a commit, is a genuine no-new-folder configuration. [Git's notes documentation](https://git-scm.com/docs/git-notes) confirms notes use separate refs and have their own display, rewrite and merge behavior. That mechanism could preserve metadata without editing a commit, but its separate-ref distribution and discovery requirements are precisely where a portable small-Task Trace may fail. C9 combines a dated independent Task with a generated *read-only* navigation view; it may address scale without a manually maintained journal if a real retrieval failure appears, but it adds build/discovery behavior not justified by current field evidence. Both warrant explicit challenge rather than silent omission.

## Checkpoint

| Found | Remaining |
|---|---|
| Ten coherent configurations across all six Gather dimensions; C6 and C9 expand the HL comparison. | Challenge survivors against NS1, one-shot cost, local update safety and cross-session retrieval. |
| Conditions where C1 loses to object/document/commit forms are explicit and testable. | Find a concrete no-folder counterexample; distinguish demonstration from measured routine performance. |
| Full command update and optional package update are separate contracts. | Determine whether a frozen HL change is necessary and price it with an alternative. |

**Sufficiency:**
- [x] External source used: official Git and GitHub documentation for commit metadata, permanent links, issue forms and Git notes.
- [x] Briefing gap closed: code and non-code no-folder paths, naming, lookup and package/update combinations mapped.
- [x] Configuration space built with Gather's six dimensions; no option selected at this stage.

Stage complete: YES
→ Coordinator decision: Extract checkpoint pending; propose Challenge.
