# Challenge — What do we not expect?

> **Mindset:** Critic. Attack the leading dated-folder choice and retain strong exceptions.
> **Parent:** [HL-TFW_20260923-223151_PTW](../../HL-TFW_20260923-223151_PTW.md)
> **Goal:** Identify a defensible default and its failure conditions across code and non-code work.
> **Producer / route:** `codex:thread:local:01a0d505-d0b4-76f2-ad95-58f1bf9cfe2e` → Coordinator `codex:thread:local:01a0cf4d-9254-7633-9ba9-393b0eb8e802`; dispatch `journal/20260925-010738__dispatch__ef88.md`, frozen HL `515b837`.

## Consistency Check

All 15 pairs of Gather's six dimensions were checked. Pairs D1–D2, D1–D3, D1–D4, D1–D5, D1–D6, D2–D3, D2–D4, D2–D5, D2–D6, D3–D4, D3–D5, D3–D6, D4–D5, D4–D6 and D5–D6 generally coexist **only if** the result remains reachable and the package/local form boundary is explicit. The following pair values fail under the *current* project contract or the option's own definition:

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible here |
|---|---|---|---|---|
| D1 Trace location | Existing commit/PR/document **only** | D2 Record boundary | New separate `task.md` or triad | A new task file negates the no-new-file candidate; it may be a good design, but is a different configuration. |
| D1 Trace location | Existing non-code document only | D2 Record boundary | Git commit trailers or Git note | A document without a Git commit cannot carry metadata attached to that commit. |
| D3 Distribution boundary | Current Full manifest command | D6 Local form evolution | Daily receiver treated as unrelated project content | Current init/update validates exact ten commands; adding an eleventh while claiming the unchanged contract is contradictory. |
| D4 Name and identity | `tfw-task` as a new Full-like role route | D3 Distribution boundary | Current fixed Full manifest without canonical change | HL §7.2 records `/tfw-task` retirement; reviving it by name or adapter copy alone would repeat the orphan command/Role Lock defect. |

**Surviving configurations** from Extract, including constrained survivors:

| Config | D1 location | D2 record | D3 package | D4 name/ID | D5 discovery | D6 evolution | Notes |
|---|---|---|---|---|---|---|---|
| C1 | Dated folder | One file | Optional package | Daily/timestamp | Search/links | New records | Survives as greenfield default candidate; no measured cost proof. |
| C2 | Dated folder | Triad | Project copy | Daily/timestamp | Search/links | Local pin | Observed SenseLab practice; local contract. |
| C3 | Object | Document section | Bundled | Task/object | Object links | Local pin | Survives only with stable object/access and explicit history/current distinction. |
| C4 | Commit | Structured message | Bundled | Quick/SHA | Git search | Inline | Strong conditional code-only no-folder candidate. |
| C5 | PR/issue | Host description | Project copy | Task/host ID | Host search | Host template | Survives locally if access/export are governed. |
| C6 | Git note | One note | Optional package | Daily/SHA | Note ref | New notes | Mechanically possible; reachability/distribution weak. |
| C7 | Dated folder | One file | Full manifest | Daily/timestamp | Subject folders | Upstream receiver | Requires a deliberate new canonical Full command/update contract first; not available as a drop-in. |
| C8 | Object | Task record + source | Optional package | Daily/object ID | Object links | Local pin | Survives when object scope is stable and project elects local form. |
| C9 | Dated folder | One file | Bundled | Daily/timestamp | Generated view | New records | Survives only if a measured retrieval failure justifies a read-only view. |
| C10 | Existing document | Embedded section | Optional package | Daily/document ID | Exact links | Inline | Strong conditional non-code no-folder candidate. |

**Unexpected survivors:** C4 and C10 show that a new folder is not logically required for every bounded Task. C6 survives the storage check but may lose the portability/retrieval check; it remains visible rather than being dismissed by unfamiliarity.

## Findings

### C1 — Letter and design: the dated folder earns history, but can bury the current source

**Observed:** SenseLab's `daily/2026/20260908-executive-pilot/task.md` separates accepted letter text, event description and Word attachment; it preserves three brief revisions, six source messages, owner-reported WhatsApp/email transmission and the limit that the agent did not send or verify delivery. Moving all of that into the current letter would blur the version the recipient should read and the historical decision record. The sticker pack Task similarly holds revision history while `docs/design/stickers/README.md` carries the current shared catalogue.

**Attack:** A new worker looking only in `daily/` could miss a later edit to the current letter or sticker catalogue; a year folder can be hard to browse, and a slug can become stale after the deliverable changes. The dated-folder option passes only when the internal context gate starts at the *current object* and uses the old Task as cited history, with a bounded search and exact relation when material. If a letter itself is a stable internal artifact containing a short source/result/check/next section and the project already organizes access around it, C10 can eliminate the folder. The actual SenseLab letter is a counterexample to claiming C10 always suffices: accepted content, multiple formats and reported delivery history would make an embedded section intrusive or fragile. C10 remains a conditional no-folder exception, not observed as the current field implementation.

### C2 — Patch: a commit can carry selected Trace, but the observed one does not

**Observed:** Commit `6c3ac7745a2bc6588414c6711297d07243a2522f` changed 18/14 lines in the PTW HL to clarify the Daily-owned template boundary. Its commit message says only `Clarify Daily-owned trace template boundary`; it does not itself state the human source, Goal/Value, verification or next authority. The HL and task history supply those elsewhere. Thus this *actual* patch does not prove a bare commit is a complete Daily Trace.

**Counterexample construction, not field proof:** For a genuinely tiny code correction already committed under a project that retains reachable Git history, a commit body could name the requester/source link, Goal and Value, boundary, reason, changed object, test result and explicit close or next step; [Git's trailer format](https://git-scm.com/docs/git-interpret-trailers) supports searchable structured fields. If a second worker can reconstruct the bounded request and acceptance state from `git log -- <object>` and the commit, C4 defeats the universal H12 claim with zero new Task folder. Its cost rises or validity fails when the work is non-code, uncommitted, squashed or rewritten without preserving the Trace. [Git's rebase documentation](https://git-scm.com/docs/git-rebase) confirms rebase replays and can combine commits, changing history; a SHA permalink only anchors the original reachable object. A commit author also does not establish the human requester: that attribution must be explicit.

### C3 — Package and template: path isolation is insufficient

**Observed:** The proposed `.tfw/extensions/daily-task/templates/task.md` does not currently exist. The manifest has exactly ten Full role commands and `update.md` verifies those target copies while preserving unrelated receiver content. SenseLab's project-local skill has one stated source and a Claude entry, but its own closure does not claim a live independent provider trial.

**Attack:** C1 loses its promised update safety if an update omits the extension entirely, copies an old provider entry, or overwrites a project-changed template. Moving the file from `.tfw/extensions/` to a skill bundle alone does not resolve versioning or local overrides. A credible optional package needs a pinned canonical source, exact receiver map/check, and an owner-visible rule for customized forms. C7's shortcut through the Full manifest raises the fixed-command parity and semantic Role Lock cost; no observed benefit offsets that yet. The template should affect new records only unless the owner separately authorizes migration.

### C4 — Name, scale and the false low-risk cue

`daily` is established in SenseLab and explicitly outside Full there; `quick` would more strongly cue insufficient assurance, and `tfw-task` has a retired-command history. This supports retaining the known invocation provisionally, while explaining in the skill that “daily” is a *route for a bounded request*, not a cadence or risk classification. A timestamp must include a collision suffix and stable full ID; the slug is for orientation, never a mutable taxonomy or authority. A real multi-worker retrieval failure should trigger a generated, read-only view test before any maintained journal. No archive-size measurement here justifies subject folders or a view.

### C5 — Git notes and host records: portability stress

[Git notes](https://git-scm.com/docs/git-notes) live in separate refs, and their display/rewrite/merge behavior is separately configured. A second worker who fetches ordinary branches may not have the notes ref; requiring that ref adds a hidden dependency for the default Trace. [GitHub's repository access guidance](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-an-issues-only-repository) shows that private cross-repository issue references can reveal limited detail to a reader without access. C5 therefore needs an authorized reader and ordinary-file/equivalent continuation route; a host URL alone does not prove portability. Both can be useful project-selected forms but do not beat C1 as an unconditioned cross-project default.

## Checkpoint

| Found | Remaining |
|---|---|
| C1 survives as a provisional cross-project default; C4 and C10 are credible no-folder exceptions with explicit prerequisites. | A clean receiver/update trial and matched continuation/cost measurement are absent. |
| Actual letter, design and patch cases show where current object, history and human source separate. | Test a real no-folder Task before claiming H12 has been empirically falsified. |
| `.tfw/extensions/` path alone does not prove opt-in update safety; C7 requires canonical change. | Coordinator must decide whether §3 needs a narrow amendment or can be implemented under its existing “proposed default” wording. |

**Sufficiency:**
- [x] External source used: official Git rebase, trailers and notes documentation plus GitHub access guidance.
- [x] Briefing gap closed: strongest named default attacked with letter/design, patch, package and lookup failures.
- [x] All 15 dimension pairs checked; surviving and unexpected configurations listed.

Stage complete: YES
→ Coordinator decision: Challenge checkpoint pending; propose synthesis with explicit uncertainty, two-class HL recommendations and decision matrix.
