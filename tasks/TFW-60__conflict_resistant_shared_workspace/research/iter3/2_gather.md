# Gather — "What do we NOT know?"

> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-60](../../HL-TFW-60__conflict_resistant_shared_workspace.md)
> Goal: several humans and agents advance different tasks in one synchronized folder without editing
> the same project-root registries first.
> Loops run: 3 of 3 (deep)

---

## Dimensions

Iterations 1-2 already decomposed carrier, journal grammar, ownership, edition split, sync guarantees and
Git topology. These seven are the decision factors those passes did **not** have, because the mechanisms
they govern entered after iteration 2 closed. No alternative below is marked recommended.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| **D-I Mutation enforcement** | Deterministic engine owns every control/journal write | Thin executable validator, advisory; the agent writes | Strict skill contract only; no executable component | Structural filesystem gate — atomic path creation, name gate, one-writer role split |
| **D-II Event identifier grammar** | Monotonic per-task counter (`TFW-60-E0007`) | UTC timestamp (`20260826-162000`) | Content digest | No explicit identifier — position in the file *is* the identity |
| **D-III Journal carrier** | One appended file per numbered segment (JSONL) | One file per event in `journal/` | A bounded section inside the task's own control file | No journal — role artifacts and commits are the record |
| **D-IV Cross-file duplication** | Snapshot stores `last_event_id` + `journal_head` | Snapshot stores nothing derivable from the journal | One file carries snapshot and history together | — |
| **D-V Participant resolution** | Shared mutable registry / `CURRENT_USER` | Shared profiles + machine-local binding + generated `device_instance_id` | Shared profiles + machine-local binding, no device ID | Shared profiles + one explicit question, no persistent binding |
| **D-VI Machine-local footprint** | Full TFW home: `device.yaml`, `profiles/<p>/preferences.md`, `projects/<id>/{binding,git}.yaml` | One per-project machine-local file (bound profile + private preferences + Git paths) | Git paths only | Nothing outside the project folder |
| **D-VII Git topology** | `.git` inside the synchronized root | G-B: worktree synchronized, Git dir + index pinned outside | G-A: every participant pins their own external Git dir/index | No Git in the synchronized tree; the landing owner keeps a separate clone |

---

## Findings

### G1 — The zero-occurrence claim is confirmed by measurement

`grep -ri` across all ten iteration-1 and iteration-2 files (2 443 lines):

| Term | Hits | Term | Hits |
|---|---:|---|---:|
| `tfw-status` | 0 | `people/` | 0 |
| `state engine` | 0 | `device_instance` / `device instance` | 0 / 0 |
| `deterministic engine` | 0 | `TFW home` | 0 |
| `state-transition engine` | 0 | `LOCALAPPDATA` / `XDG_CONFIG` | 0 / 0 |
| `engine` | 0 | `binding.yaml` / `profile_id` | 0 / 0 |
| `machine-local` | **5** | `executable` | **4** |

Both non-zero terms were read in place. All five `machine-local` hits and all four `executable` hits
concern **Git directory/index placement or an executable Git preflight probe** — `iter1/2_gather.md:147`,
`iter1/3_extract.md:210`, `iter1/4_challenge.md:22`, `iter1/4_challenge.md:190`, `iter1/RES.md:79`,
`iter2/2_gather.md:233`. None concerns a state engine, a mutation interface or an identity subsystem.

**RR.** The master HL §10 table is accurate. Both mechanisms are genuinely unexamined.

### G2 — The field starter: a shipped Assisted v1.4 in a live Google Drive mount

`H:\My Drive\Innoforce AI-First Knowledge\innoforce_starter_v1.4`, inspected read-only.

**Provider runtime, directly observed (PR — the first PR-class evidence any iteration has had):**

- Two Google Drive for desktop virtual drives are mounted on this machine: `G:` (`c0rp.aubakirov@gmail.com`)
  and `H:` (`saubakirov@innoforce.kz`). Two `GoogleDriveFS.exe` processes are running, versions
  **129.0.1.0** and **130.0.2.0**. The starter sits on the streamed virtual drive `H:`, not on a local
  mirror directory.
- The tree contains **18 directories and exactly 18 `desktop.ini` files** — coverage is 100 %, verified
  by testing every directory for the file and finding zero misses. They appear in dot-directories too:
  `.agents/desktop.ini`, `.agents/skills/desktop.ini`, `.agents/skills/tfw-plan/agents/desktop.ini`,
  `.codex/hooks/desktop.ini`. The parent folder `Innoforce AI-First Knowledge/` has one as well.
- Content is UTF-16LE:
  `[.ShellClassInfo] / ConfirmFileOp=0 / IconResource=C:\Program Files\Google\Drive File Stream\130.0.2.0\GoogleDriveFS.exe,27`.
  **The client version is embedded in the file body.** A client upgrade therefore rewrites one file in
  *every directory of the tree*.

This is the PR-class observation iteration 2 recorded as *not observed* (`iter2/RES.md` evidence
boundary). It is narrow: it establishes provider-written artifacts and mount topology. It does **not**
establish offline fork, reconnect, conflict-copy naming or two-device reconciliation — the folder holds
no active task and no second device is observable from here.

**No `.git` anywhere.** `find . -name ".git*"` returns nothing, in this and in all three earlier starter
versions. Four TFW skills operate in the folder with no repository present.

### G3 — What the field starter uses instead of every mechanism the Phase A draft adds

Read from `AGENTS.md` (20 993 B), `README.md`, `people/README.md` and the four `SKILL.md` files.

| Phase A draft mechanism | Field starter equivalent | Carrier |
|---|---|---|
| Monotonic ID allocated by an engine | `ID = YYYYMMDD-HHMMSS__slug`. *"При коллизии не переиспользуй и не перезаписывай путь: возьми новый фактический timestamp."* | none — the clock |
| Atomic allocation / duplicate prevention | *"Атомарно создай только отсутствующую папку `work/<ID>/`"* (`tfw-plan` SKILL §2.3) | the filesystem's own create-if-absent |
| `status.yaml` strict nine-field YAML | one line in `work/<ID>/TRACE.md`: `Статус: new\|doing\|review\|done\|blocked` | ordinary Markdown |
| `journal/` segmented JSONL + chain digests | `## Ход работы` section inside the same `TRACE.md` | ordinary Markdown |
| `last_event_id` / `journal_head` reconciliation | nothing to reconcile — no duplicated fact exists | — |
| `tasks/INDEX.md` derived portfolio view | none, and explicitly prohibited: *"Не создавай общий task board, общий счётчик или `CURRENT_USER`."* | `work/` directory listing |
| Root Task Board | none | — |
| `state_owner` / `owner_epoch` | *"Одна задача и её изменяемый trace имеют одного владельца записи и одного активного писателя этапа"*; `handoff` and `review` are forbidden to run at the same time and must send an exception report at any sign of parallel writing | role discipline |
| Agent-only `tfw-status` mutation interface | the lifecycle skill itself writes the field; `FAIL` changes *only* `Статус: review → doing` | skill contract |
| Identity subsystem (`people/` + TFW home + `device_instance_id`) | one profile → silent; several → private-device binding; otherwise **one** question. Separate `automation:<name>`. *"общего файла текущего пользователя в проекте нет"* | `people/<handle>.md` + an unspecified private-device store |
| Stable paths through terminal states | *"Смена статуса никогда не перемещает task folder: одна задача всегда живёт на `work/<ID>/`"* | convention |
| Deterministic hashing | the reviewer skill instructs the agent: *"до и после записи вердикта зафиксируй SHA-256 результата"* | whatever hash tool the environment has |
| `active_task` required | *"`active_task=none` допустим"* — reading and ordinary conversation create nothing | explicit non-requirement |

`шаблоны/build_a4.py` (165 lines) is a **document builder**: it converts one Markdown file to a
print-styled A4 HTML page using an inline CSS block and `io, re, sys, html`. It has no knowledge of
tasks, status, journals or identity. It is neither a state engine nor evidence against one.

### G4 — The identification Gate: structural enforcement with zero code

`AGENTS.md` line ~68 and every `SKILL.md` §1. Before substantive work each Codex task must be renamed
to exactly `plan | <ID>`, `handoff | <ID>` or `review | <ID>`; the agent must verify the rename succeeded;
*"Если точное имя нельзя установить и проверить, этап блокируется."* Markdown, a handle, a cycle number,
a different case or a different separator are all forbidden.

What this buys with no executable component:

- The session's identity is the task identity, so a second concurrent writer on the same task is visible
  in the environment's own task list rather than discovered from file contents.
- The gate fires **before** the agent reads the result or the sources, so an agent that cannot name itself
  cannot begin.
- It is enforced by an operation the agent must perform and verify, not by a rule it must remember.

This is the mechanism the repository's own PV 1 calls *Structural Enforcement*, realised with prose plus
one environment operation.

### G5 — Version archaeology: the same owner built this engine, shipped it, and withdrew it

The Drive folder holds four generations of the same starter side by side. `.codex/` contents:

| Version | `hooks.json` | `tfw-hook.ps1` | `tfw-hook.sh` |
|---|---|---|---|
| `innoforce_starter` (1.0) | ✅ | ✅ | ✅ |
| `innoforce_starter_v1.2` | ✅ | ✅ | ✅ |
| `innoforce_starter_v1.3` | ✅ | ✅ | ✅ |
| `innoforce_starter_v1.4` | **removed** | **removed** | **removed** |

`tfw-hook.ps1` is 361 lines, `tfw-hook.sh` is 377 — 738 lines of dual-implementation deterministic
local code. Read in full, it implements, in v1.3:

- `Find-AssistedRoot` — walks up looking for `PROJECT.md` with declared edition and version markers, and
  **fails closed** on zero or multiple matches (`"однозначный корень... не найден; запись отменена"`);
- `Get-StateDirectory` — a machine-local state home at `%LOCALAPPDATA%\TFW-Assisted\<first-8-bytes-of-SHA256(root)>`,
  falling back to the temp directory. *This is the Phase A draft's "standard machine-local TFW home",
  already built;*
- `Get-Actor` / `BindActor` — reads `people/*.md` profiles, returns the single profile silently, otherwise
  reads `actor.txt` from that machine-local home. *This is the draft's `binding.yaml`, already built;*
- `Get-TaskRecords` — parses `Владелец:` and `Статус:` out of every `work/<ID>/TRACE.md`; validates status
  against a closed allow-list `new|doing|review|done|blocked` and the task ID against a regex;
- `SessionStart` — emits a status census (`задачи new=…, doing=…, review=…`), resolves the actor, detects
  `active=ambiguous` when a participant has several `doing` tasks, and injects guidance into the session.
  *This is `tfw-status`'s read path, already built;*
- `RiskCheck` — a deterministic secret-pattern gate returning `hold`/`pass`;
- `Write-EventLog` — one timestamped event file per hook invocation in the machine-local home.
  *This is a journal, already built — machine-local rather than task-local;*
- `PreCompact` / `Stop` — idempotent checkpointing of the actor-scoped `doing` task and completion checks
  on required fields, allowed status, result existence and internal links.

The v1.4 `CHANGELOG.md` states why it was withdrawn, verbatim:

> **Почему hooks удалены** — Lifecycle hooks ранних выпусков были тестовыми. **На реальной большой папке
> `Stop` не укладывался в собственный timeout, а проверочный runner мог зависнуть без полного отчёта.**
> Это не доказанная защита, поэтому `.codex/hooks.json` и оба TFW adapter удалены из clean 1.4 до
> отдельной будущей задачи переработки; отсутствие startup summary теперь нормально.

`hooks.json` declares `"timeout": 10` for `SessionStart` and `PreCompact` and `"timeout": 30` for `Stop`.

**PR + RR.** A deterministic local component that had to traverse the task tree on a real large
synchronized folder exceeded a 30-second budget and could hang without returning. The replacement is the
prose in `AGENTS.md` §*Перед сокращением контекста и завершением* plus the four `SKILL.md` contracts, and
`README.md` now says the absence of a startup summary is normal.

**Scope of this evidence, stated honestly.** A session hook is not the same thing as an on-demand
mutation engine: the hook ran on every session event and had to scan the whole tree, while a mutation
engine touches one task folder. The failure does not transfer automatically. It *does* transfer to the
two responsibilities the Phase A draft gives the same engine that require full-tree traversal —
`tasks/INDEX.md` generation and migration accounting.

### G6 — The repository's own precedent: TFW-49

`tasks/TFW-49__agent_commit_identity_and_attribution/POSTMORTEM__TFW-49.md`, owner verdict quoted whole:

> TFW-49 solved a small prompt-design need with an unnecessary software subsystem. The useful outcome is
> only the readable `[surface/task/work/role] summary` format and its purpose. **The schema, state, Python
> validator/router/runtime, Git hooks, range audit, installation lifecycle, and cross-platform machinery
> are rejected.**

Three phases were built and reviewed before the owner ruled. Removal was 149 files and 27 103 deletions.
The replacement, TFW-50 / D55, is **one Markdown rule in `conventions.md` and no runtime**.

`KNOWLEDGE.md` D24 states the same stance as a decision: *"No scripts — AI agent is the sync engine."*
`KNOWLEDGE.md` D58 already records the hook outcome from the repository side: *"tested Codex Desktop
builds do not durably dispatch them. The edition's proven mode is its documented manual order…
automatic enforcement is not claimed."*

TFW-54's own frozen DoD-14 — a different task, reached independently — reads: *"Nothing executable is
added: no script, no hook, no config key, no new artifact class"*, and its DoF-2 names *"anything
executable ships: a spawner, a hook, a script, a runtime. TFW-49's cause of death."*

**RR / PV.** Component-for-component, the Phase A draft proposes what TFW-49 was rejected for: two JSON
schemas, a validator/router/runtime, a checked Git helper, cross-platform machine-local machinery, and an
installation lifecycle (`/tfw-init` and `/tfw-config` "create or verify the device, binding and Git
attachment").

### G7 — Project North Star and PV, read for this question

- **NS2-6** — *"Assurance proportional to risk. Add evidence, review, and durable verified knowledge when
  their expected value exceeds their cost; **subtract ceremony that does not protect the purpose**."*
- **NS3** — TFW must not become *"a vendor-bound tool, runtime, model, interface, or memory feature"*, nor
  *"a deterministic generator that treats code or other outputs as disposable and promises identical
  reproduction"*. Read conservatively: "vendor-bound" plausibly qualifies the whole list, so this is
  suggestive rather than dispositive. NS2-6, D24, D55 and the TFW-49 verdict are not.
- **PV 2 `knowledge/philosophy.md` F11** (cited by the master HL itself, §7.2 row 7) — *TFW Markdown
  already is the knowledge graph; avoid extra entities.*
- **Master HL §7.1** — *"No new artifact is admitted without showing which existing responsibility it
  owns and which duplicate write it removes."*

### G8 — Git primary source on synchronized repositories

[Git FAQ](https://git-scm.com/docs/gitfaq), *"How do I sync a working tree across systems?"* — quoted
verbatim, because both halves matter:

> Git works best when you push or pull your work using the typical `git push` and `git fetch` commands and
> **isn't designed to share a working tree across systems**. This is potentially risky and in some cases
> can cause repository corruption or data loss.
>
> Usually, doing so will cause `git status` to need to **re-read every file in the working tree**.
> Additionally, Git's security model does not permit sharing a working tree across untrusted users, so it
> is **only safe to sync a working tree if it will only be used by a single user across all machines**.
>
> **It is important not to use a cloud syncing service to sync any portion of a Git repository**, since
> this can cause corruption, such as **missing objects, changed or added files, broken refs**, and a wide
> variety of other problems. These services tend to sync file by file on a continuous basis and don't
> understand the structure of a Git repository. This is especially bad if they sync the repository in the
> middle of it being updated…
>
> An example of the kind of corruption that can occur is conflicts over the state of refs, such that both
> sides end up with different commits on a branch that the other doesn't have. This can result in
> important objects becoming unreferenced and possibly pruned by `git gc`, causing data loss.

For the rsync escape hatch Git additionally requires that *"additional worktrees or a separate Git
directory… must be synced at the same time"* and that the repository is *"in a quiescent state for the
duration of the transfer"*.

**PS.** This is Git's own documentation, not a blog. Two consequences, one for each side of the argument:

1. *"Google Drive synchronizes `.git` and this breaks the repository"* is **documented, not folklore.**
   H7's opening charge fails against this source. `changed or added files` is exactly the class the
   `desktop.ini` observation in G2 falls into.
2. The same paragraph is **broader than the Phase A draft's conclusion.** Git says do not sync *any
   portion* of a repository and calls a shared working tree safe *only for a single user across all
   machines*. The draft's G-B baseline is a working tree in a **shared** Drive folder used by **several**
   participants. Moving `.git` out removes the object/ref corruption class; it does not make the
   configuration one Git documents as safe.

### G9 — Read-only census of what a synchronized `.git` would actually mean here

Measured on this repository, read-only (`find`, `du`, `ls`; no state-changing Git command was run):

| Quantity | Value |
|---|---:|
| Files under `.git/` | 5 444 |
| Directories under `.git/` | 1 163 |
| `.git/` size | 33 MB |
| Loose objects | 5 201 |
| `.git/index` | 112 846 B, single binary file, rewritten by most operations |
| Working-tree directories (excluding `.git`) | 1 189 |
| Tracked files | 801 |
| Present administrative state | `AUTO_MERGE`, `ORIG_HEAD`, `FETCH_HEAD`, `packed-refs`, `lost-found/` (147 files), `worktrees/` (2 linked worktrees) |
| `desktop.ini` in `.gitignore` | **absent** |
| Git version in use | 2.42.0.windows.1 |

Combining G2 and G9 as an **inference, not an observation**: a Drive client that writes `desktop.ini`
into 100 % of directories would add ≈1 163 files inside `.git` and ≈1 189 untracked files across the
worktree, and would rewrite all of them on every client version bump. Inside `.git/refs/heads/` such a
file is read as a ref; inside `.git/objects/xx/` it is counted as garbage. What confirms this: putting a
throwaway repository inside a Drive-synced folder and observing. That was not done — the mandate forbids
state-changing Git commands, so no repository could be created and committed into.

The `worktrees/` entry matters for the draft: a linked worktree keeps a **`.git` file** in its root. If
one of those worktrees lived in the sync root, the draft's rule *"no `.git` directory **or gitfile**"*
would be doing real work — that clause is well-aimed.

### G10 — H6 baseline measurement: the current write surface, exactly

Board and task census (measured today, `README.md`):

| Quantity | Value |
|---|---:|
| Task Board rows | 60 |
| Task directories under `tasks/` | 52 |
| Rows not in the canonical `[TFW-N](path)` link form | 9 |

Files carrying an explicit Task Board **write** instruction:

`.tfw/workflows/plan.md:52` · `.tfw/workflows/handoff.md:69,73` · `.tfw/workflows/review.md:116` ·
`.tfw/workflows/research/base.md:37` · `.tfw/workflows/init.md:102,170,202` ·
`.tfw/templates/REVIEW.md:69` · `.tfw/templates/RELEASE.md:54` · plus **read** sites in
`.tfw/workflows/release.md:16` and `resume.md`, and normative statements in `conventions.md:13,344,504`
and `glossary.md` (`Task Board`, `Coordinator … Manages Task Board`).

Files containing the string `Task Board` at all, outside `tasks/`: **48**.

**The adapter amplification factor, measured.** Frontmatter stripped, `md5sum` compared:

| Concept | Canonical | Installed copies |
|---|---|---|
| `plan` | `.tfw/workflows/plan.md` | `.claude/commands/tfw-plan.md` and `.agent/workflows/tfw-plan.md` — **identical bodies** (`15bffb6f…` ×3) |
| `handoff` | `.tfw/workflows/handoff.md` | same pattern (`0b9287b6…` ×3) |
| `review` | `.tfw/workflows/review.md` | same pattern (`afb13d58…` ×3) |
| `resume` | `.tfw/workflows/resume.md` | same pattern (`f38f5610…` ×3) |
| every Codex skill | `.tfw/adapters/codex/skills/<n>/SKILL.md` | `.agents/skills/<n>/SKILL.md` — **byte-identical for all 11** |

So one canonical workflow sentence costs **3 file writes**; one touched command concept costs **5**.
`docs/scripts/gen_docs.py` and `site/scripts/gen_docs.py` are also byte-identical duplicates, and the
board parser lives in both:

```python
# gen_docs.py:324  — Parse task board from README.md for statuses
r'\| \[?(?:TFW-\d+)\]?(?:\([^)]*\))?\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|'
```

It hardcodes the project's own task prefix and reads column 3 positionally — TD-81's implicit API,
duplicated across two trees.

Configured budgets (`.tfw/project_config.yaml`): `max_files_per_phase: 30`, `max_new_files: 15`,
`max_loc: 3000`, `max_modified_files: 30`.

### G11 — The repository's Assisted edition is four versions behind the field

`editions/02-assisted/PROJECT.md` declares `Версия редакции: 1.0`. It has 9 files, still ships
`.codex/hooks.json` + both hook adapters, and has **no** `.agents/skills/`, no `VERSION`, no
`CHANGELOG.md`. The shipped field artifact is v1.4 with four skills and no hooks, and its `tfw-hook.ps1`
differs from the in-repo copy.

Any Phase A that claims to ship an Assisted profile is therefore writing against a stale in-repo model.
The migration obligation *"a populated Assisted corpus must be included when available"* is also
currently unmeetable from this repository: all four field starters are unused templates with no `work/`
directory and no `people/<handle>.md` profiles.

### G12 — Provider exclusion semantics

Google's own documentation covers stream vs mirror selection
([stream & mirror](https://support.google.com/drive/answer/13401938?hl=en),
[Drive for desktop](https://support.google.com/drive/answer/10838124?hl=en)) and exposes selective sync at
folder level; community and vendor-adjacent sources agree that **nested subfolders inside a synced parent
cannot be excluded**. Nothing in Google's documentation gives a `.gitignore`-aware or dot-directory-aware
exclusion contract.

**PS + PR.** The draft's S25 conclusion — `.gitignore` cannot keep `.git` out of Drive, so a supported
root must not contain one — is sound and is now supported by direct observation that the client writes
into dot-directories (`.agents/`, `.codex/hooks/`) without hesitation.

---

## Checkpoint

| Found | Remaining |
|---|---|
| The zero-occurrence claim is measured and true; both mechanisms are unexamined (G1) | — |
| First PR-class evidence: Drive for desktop 129/130, streamed mount, `desktop.ini` in 18/18 directories including dot-directories, client version embedded in the body (G2) | Offline fork, reconnect, conflict-copy naming, two-device reconciliation — no active task, no second device observable |
| The shipped field product replaces every draft mechanism with prompt discipline, an atomic `mkdir`, a timestamp and a one-line status field; a shared board, a shared counter and `CURRENT_USER` are explicitly prohibited (G3) | Whether that holds under Full's same-task multi-role case, which Assisted forbids outright |
| The identification Gate enforces single-writer structurally with zero code (G4) | Whether a TFW adapter other than Codex can rename its own session |
| The same owner built the engine + machine-local home + binding + machine-local journal (738 LOC), shipped it in 1.0/1.2/1.3 and removed it in 1.4 because `Stop` blew its 30 s timeout on a real large folder and the runner could hang (G5) | A hook is not an on-demand engine; the failure transfers only to full-tree traversal responsibilities |
| TFW-49's owner verdict rejects exactly this component list; D24 says "no scripts — AI agent is the sync engine"; TFW-54 DoD-14 forbids anything executable (G6, G7) | — |
| Git's own FAQ documents the `.git`-in-cloud-sync corruption class — so it is **not** folklore — and in the same breath says a shared working tree is safe only for a single user, which the draft's G-B baseline is not (G8) | Empirical reproduction impossible under the no-Git-mutation constraint |
| A synchronized `.git` here would mean 5 444 files, 1 163 directories, 33 MB, and ≈1 163 injected `desktop.ini`; the worktree alone would gain ≈1 189 untracked ones and `.gitignore` does not list `desktop.ini` (G9) | Inference from a PR observation, not an observation of Git failing |
| Adapter amplification measured: 3 byte-identical copies per canonical workflow, 2 per Codex skill, 2 copies of the docs generator. 60 board rows, 52 task dirs, 48 files mentioning the board (G10) | — |
| The in-repo Assisted edition is v1.0 against a shipped v1.4; no populated Assisted corpus exists anywhere (G11) | — |

**Sufficiency:**
- [x] External source used? — Git FAQ (PS), Google Drive documentation (PS), live Drive mount (PR)
- [x] Briefing gap closed? — all three guiding questions have evidence to work on in Extract
- [x] Dimensions identified? — seven, each with ≥3 alternatives

**Metacognitive check.** Genuinely new, not confirmation: (a) the engine and the machine-local home were
*already built and withdrawn* by the same owner in the same environment — no iteration knew this; (b) the
`.git` claim the mandate suspected of being folklore is documented by Git itself, so that half of H7
inverts; (c) the budget overrun is driven by adapter duplication, which is independent of which
architecture is chosen. What I have not checked: whether any TFW adapter other than Codex can perform the
session-rename operation that G4's gate depends on.

Stage complete: YES
→ User decision: coordinator gate — proceed to Extract
