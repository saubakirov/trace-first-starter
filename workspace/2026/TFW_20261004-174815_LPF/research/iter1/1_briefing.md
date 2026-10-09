# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW_20261004-174815_LPF](../../HL-TFW_20261004-174815_LPF.md)
> Goal: A TFW project holds only the result and the selected trace: working material lives outside the project under the task ID and is gone when the task closes, and a comment carries value or is absent.
> Producer unit: `claude-code:agent:local_a7cf0ab7-482d-403e-b738-504d82bba898/lpf-researcher` = native agent `a2f09276b39617fd0` in Claude Code session `bd8d3d9f-d605-429a-a889-2c6d2bd03aa5` (binding accepted by the Coordinator at the mode gate)
> Parent Coordinator: `claude-code:session:local_a7cf0ab7-482d-403e-b738-504d82bba898`
> Activation / dispatch source: delegated; command-first `/tfw-research TFW_20261004-174815_LPF`; `journal/20261004-193543__dispatch__71eb.md @ 72b88163`
> Coordination authority: `HL-TFW_20261004-174815_LPF.md @ efc915a9fa3e4366a3567be800d028ee011c916f`, §4.1
> Originating proposer: `none`

Iteration 1 of `research/iterations.yaml` (first pending entry; no `iter1/` existed at resolution).
Mode: focused. Session title `RESEARCH · LPF` is unavailable for an in-session agent. Model
claude-opus-5-5 as dispatched; the process environment carries `CLAUDE_EFFORT=max` as the requested
setting; the effective reasoning level is unknown.

**Economics source binding** (`.tfw/economics/README.md`, Claude Code JSONL recipe): provider
`claude-code`; source ID `bd8d3d9f-d605-429a-a889-2c6d2bd03aa5/a2f09276b39617fd0`; file
`<session>/subagents/agent-a2f09276b39617fd0.jsonl` in Claude Code's projects folder (found by a
one-off marker; only the matching file name was returned); source version 2.1.286; range start at
line 1, the activation message, 2026-10-04T14:36:27.882Z (19:36:27 +05:00); timezone +05:00; task
`TFW_20261004-174815_LPF`, no phase; owner `saubakirov`; role `researcher`. The finite end and
cutoff are set at the RES return.

## Research Plan

### Gather — observe, count, collect sources

- **H1 trials.** From a throwaway git workspace outside the repository, run one fixed
  write → read → delete probe against four locations: the workspace (control), `~/.tfw/work/<ID>/`,
  `%LOCALAPPDATA%\tfw\work\<ID>\` and `<system temp>/tfw/work/<ID>/`. Surfaces: Codex CLI 0.152.1 in
  its default mode with no sandbox-removing flag; a separate headless Claude Code 2.1.286 process
  with `--permission-mode default`, excluding the owner's allow-lists where the CLI can; Antigravity
  only if its `agy` command runs an agent non-interactively without a new sign-in. Outcomes come
  from the tools' own event streams (exit codes, permission denials), not from the model's summary.
  Mode proof is the tool's printed or initial configuration plus the owner's sandbox keys (those
  keys only). This session's shell runs with bypassPermissions and is recorded only as a
  non-counting baseline that separates OS permissions from sandbox limits.
- **H1 sources.** Vendor documentation of sandbox and file-access scopes for Codex (Windows sandbox,
  writable roots, temp handling), Claude Code (permission modes, macOS/Linux sandbox, Windows),
  Antigravity and Cursor (outside-workspace access, terminal sandbox). OS rules for the lifetime of
  temporary files (Windows Storage Sense, macOS `$TMPDIR`, Linux tmpfiles/tmpfs) and for
  machine-local data (Windows Known Folders, XDG). TFW's own definitions of the `bindings`,
  `worktrees` and `rates` roots, by grep and addressed heading.
- **H2 corpus.** Enumerate every `REVIEW*.md` and `review/*.md` in `workspace/` and `tasks/`; locate
  each citation of a non-EV file under `evidence/` (logs, JSON, images, archives) and read only the
  hits in context. External anchor: audit-evidence standards on reperformance versus inspection of
  another party's records.
- **H5 inventory.** From language and vendor documentation, list which tools read docstrings, doc
  comments and comment directives in common stacks (Python, JS/TS, Go, Rust, Java/C#, PHP, Ruby,
  shell, YAML/TOML/Dockerfile). In this repository's deliverable-6 code, find docstrings a program
  reads (`__doc__`, doctest, CLI help).
- **H7 count.** Fix one listed pattern for the "historical / legacy / remains readable / never
  issue" family and count matching lines per file in `.tfw/`. External anchor: normative versus
  informative text (RFC 2119/8174, ISO/IEC Directives Part 2).

Candidate decision dimensions — H1: writability in default mode, survival until Closing step 6,
reference form, consistency with existing roots, path length and sync exposure, reach of every role
and of Closing. H2: claim type, method of establishment, verdict dependence. H5: reader (human,
tool, directive), checkability by a listed command, loophole channel. H7: operative effect,
uniqueness, addressee.

### Extract — map configurations

- H1: matrix surface × location × outcome class (Q1) with lifetime and reference form → one
  recommended root per OS family and its fallback.
- H2: per-review table of raw-file dependence; whether any verdict rested only on executor bytes.
- H5: classify comment forms (value for the reader / program-read / correspondence); draft the
  exception list; design the Reviewer's listed-command check over the Candidate diff for comments,
  docstrings, identifiers and commit bodies.
- H7: classify every hit (a stated stratified sample if the census exceeds ~150 lines) as protective
  rule, duplicate rule or chatter, with the criteria written before classification; shares per file.

### Challenge — test survivors

- H1: common non-default settings that break the root (Codex read-only or `exec` defaults, Claude
  Code sandbox on macOS/Linux, Cursor sandboxed terminal), temp cleanup before close, Windows path
  length, a task whose Executor and Reviewer use different tools.
- H2: what makes a registry row insufficient — unrepeatable live observations; the typed-from-memory
  figures behind `knowledge/process.md` F32.
- H5: whether the rule is enforceable without code; whether the Executor of this very task must keep
  a docstring for a tool.
- H7: whether "mostly rule" survives a stricter classifier; what is trivially removable now versus
  owned by the agreed separate task.
- Subtraction only where iteration-1 evidence shows something removable; the full subtraction
  challenge belongs to iteration 2.

Budget: Gather will exceed the soft limits (about 12–15 web queries; more than 15 project files,
because H2 covers every review). Each query and opened file is listed in the stage file with the
hypothesis it serves.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | Codex, Claude Code and Antigravity with ordinary sandbox settings can create, read and delete files under TFW's machine-local root (`~/.tfw/`, `%LOCALAPPDATA%\tfw\`) on Windows and POSIX; the system temporary directory is the fallback. False case: a sandbox confines writes to the project tree. | open |
| H2 | Reviewers establish claims by repeating the command or opening the live result, not by reading the executor's raw files. False case: a past REVIEW found a defect only in a raw log. | open |
| H5 | The comment rule holds against its loopholes: explanations do not migrate into docstrings, identifiers or commit messages, and a Reviewer can check this without code. False case: the Executor of this task needs a docstring to satisfy a tool, or the check is impractical. | open |
| H7 | The "historical … remains readable, never issued" prose in `.tfw/` is mostly rule protecting old receivers; chatter is small. False case: a large share is notes between agents. | open |

H3, H4 and H6 belong to iteration 2.

## Scope Intent
- **In scope:** H1 trials on this Windows machine for every surface I can launch in its default
  mode, documentation for the other surfaces and for macOS/Linux, and a root recommendation; H2 over
  this repository's reviews; H5 consumer inventory, exception list, a no-code Reviewer check and this
  repository's own code as the false-case test; H7 count and classification in `.tfw/`.
- **Out of scope:** H3, H4, H6 and the full subtraction challenge (iteration 2); rule wording, TS
  and HL edits (Coordinator); receivers' content; cloud agent surfaces; trials on macOS/Linux (no
  machine); any change to code, comments or `.tfw/` prose; cleaning the legacy prose (the agreed
  separate task).

## Guiding Questions
1. **H1 oracle, fixed before the trials.** Per surface × location I record one class: (a) no
   stricter than the in-workspace control in the same mode; (b) stricter — needs an approval or
   escalation the control did not need; (c) refused with no approval path. I propose that only (a)
   qualifies a location, because TFW roles run without a human at each step and a prompt nobody
   answers is a block; (b) is reported as a DoF 2 risk together with the setting that would remove
   it. If `codex exec` with no flags starts read-only, so that even the control fails, I add one run
   with `--sandbox workspace-write` (the mode Codex edits in, sandbox kept), label both and count the
   latter. Confirm or set another rule.
2. **Surfaces the owner actually uses (DoF 2).** Launchable here: Claude Code CLI 2.1.286 (the
   engine of the Desktop Code tab), Codex CLI 0.152.1, Antigravity with an `agy` command; no Cursor.
   Does the owner use Codex through another surface (desktop app, IDE extension) or any macOS/Linux
   machine, which would add a required case?
3. **Receivers' stacks (H5).** If the receivers' main languages and frameworks are known, name them
   in one line; otherwise the inventory stays generic and no receiver project is scanned.

## User Direction

Coordinator's ruling at the mode gate (addressed message, 2026-10-04):

- Mode **focused**. The address binding above is accepted; it and the economics source binding are
  recorded here and in RES, with no separate journal event. The missing title is accepted.
  `CLAUDE_EFFORT=max` is the requested environment; the effective reasoning level is unknown.
- The web-query limit (5 per stage) is soft: it may be exceeded when every query is named in the
  stage file with the hypothesis it serves. The limit of 3 questions per turn stays hard.
- H1 validity: a trial counts only in the permission and sandbox mode the tool applies by default
  for an ordinary user. This Claude Code session runs with bypassPermissions, so a trial from inside
  it is not an observation under ordinary settings. Every trial records the tool, its mode and what
  proves that mode. Codex runs in its default mode, without flags that remove the sandbox.
- Everything the trials create (files, command output) is this task's working material: it stays
  outside the repository and is deleted once the observation is recorded in the stage file. Only
  stage files and RES enter the repository. The `credentials` folder is not opened.

Coordinator's answer to this Briefing (addressed message, 2026-10-04): the plan is accepted as
written; exceeding the soft limits with every query and file named is allowed.

1. Q1 accepted: only outcome (a), in the tool's default mode, qualifies a location; (b) is reported
   as a DoF 2 risk with the setting that removes it. Added: for each tool, quote the vendor document
   that names the default mode of the surface people use (for Codex the interactive `codex` and the
   app, not only `codex exec`). If `codex exec` starts read-only, the labelled second run with
   `--sandbox workspace-write` counts.
2. The owner's surfaces, from this repository's files: Codex through the Codex desktop app
   (`codex:thread:local:…` routes; app worktrees in `git worktree list`) and the CLI; Claude Code
   through the Code tab of Claude Desktop; Antigravity installed, with an adapter; Cursor has an
   adapter but is not installed here. This machine is Windows 11; nothing is known about other OS.
   POSIX rests on documentation, no live trial; DoD 1 must still name both OS families. The Codex
   app cannot be driven headless: rely on documentation for whether its sandbox matches the CLI and
   mark that as a limitation.
3. Receivers' stacks (field reports and size-only observations): mainly Python (FastAPI services,
   scripts), some JavaScript/TypeScript for the web, some Markdown-only projects without code; YAML
   configuration everywhere. Receiver projects are not scanned; the H5 inventory follows these
   stacks.

## Sources and knowledge handover

Inspected at this checkpoint: `status.md`; journal events created, transition and dispatch; the HL
at `efc915a9` (unchanged at `72b88163`); `research/iterations.yaml`; `tfw.research` in
`.tfw/project_config.yaml`; `conventions.md` headings `HL (High Level)`, `Session identity`,
`Commit Attribution`, `Fact Categories`, `Anti-patterns (prohibited)`, `Context Selection`,
`Workflow activation and routing`, `Knowledge handover`, `Current knowledge use`;
`.tfw/economics/README.md` source recipes and producer return; `research/base.md`, `focused.md`;
this template.

Feasibility observations, no trial yet: Codex CLI 0.152.1 and Claude Code CLI 2.1.286 are
launchable; Antigravity is installed with an `agy` command whose non-interactive use is unknown; no
Cursor is installed. Both TFW roots already exist on this machine: `%LOCALAPPDATA%\tfw\` holds
`bindings.yaml`, `worktrees` and `credentials` (not opened); `~/.tfw/` holds `rates`.

Knowledge inputs for the stages: the HL §7.2 citations as given (P0–P6); for H2
`knowledge/process.md` F32 and KNOWLEDGE D52/D53; for H1 the conventions headings that define the
existing roots. No knowledge publication is made.

Material handover: no finding yet; H1, H2, H5 and H7 remain open. Continuation: on a valid answer
to this Briefing, copy `2_gather.md` and run Gather.

---
Stage complete: YES

**Gate status: answered — plan accepted; Gather started.**
