# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20261004-174815_LPF](../../HL-TFW_20261004-174815_LPF.md)
> Goal: A TFW project holds only the result and the selected trace: working material lives outside the project under the task ID and is gone when the task closes, and a comment carries value or is absent.
> Producer unit: `claude-code:agent:local_a7cf0ab7-482d-403e-b738-504d82bba898/lpf-researcher` (native agent `a2f09276b39617fd0`); mode focused, one pass.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1 Working-material root (H1) | `~/.tfw/work/<ID>/` on every OS | `~/.tfw/work/<ID>/` on POSIX, `%LOCALAPPDATA%\tfw\work\<ID>\` on Windows | system temporary directory `<temp>/tfw/work/<ID>/` | ignored folder inside the project (HL fallback) |
| D2 How a sandboxed role reaches the root (H1) | nothing needed: root is inside the default writable set | one-time per-tool setting (writable root, additional directory, allow rule) | per-action human approval | role runs without a sandbox |
| D3 Removal and survival (H1, C1) | removed only at Closing step 6 | Closing step 6, earlier OS cleanup tolerated | removed after the Reviewer's verdict | removed at each role's return |
| D4 What a verdict may rest on for an observation that cannot be repeated (H2, C3) | only the Reviewer's own repetition | the EV row's captured observation with method and commit as attestation | the Executor's working material while it still exists | items the TS names as retained |
| D5 Status of docstrings (H5) | a comment like any other: value or absent | always allowed | allowed only when a program reads it | allowed when a program reads it or it documents a public interface |
| D6 Reviewer's check against comment correspondence (H5) | listed command over the Candidate diff plus judgement of each added line | full read of every changed file | linter configuration in the receiver | no check, rule text only |
| D7 Disposition of "historical" prose in `.tfw/` (H7) | keep as rule | clean in this task | hand to the agreed separate task | remove duplicates only |

## Findings

### G1: H1 trial protocol and proof of mode

One fixed probe per surface, run from a throwaway git workspace outside the repository: create a
folder, write a file with a fresh nonce, read it back, delete file and folder — at four locations:
the workspace (control), `~/.tfw/work/<ID>/probe`, `%LOCALAPPDATA%\tfw\work\<ID>\probe`,
`%TEMP%\tfw\work\<ID>\probe`. Outcomes were read from each tool's own event stream (exit codes,
exception names, denial records), not from the model's summary. Classes, fixed before the trials:
(a) no stricter than the control in the same mode; (b) needs an approval or escalation the control
did not need; (c) refused with no approval path.

| Surface on this Windows 11 machine | Mode run | What proves the mode |
|---|---|---|
| Codex CLI 0.152.1, `codex exec`, no sandbox flag | read-only (exec default) | `--ignore-user-config --ignore-rules --ephemeral`; every write, control included, failed with PowerShell `MethodInvocationNotSupportedInConstrainedLanguage` |
| Codex CLI 0.152.1, `codex exec --sandbox workspace-write` — **counts** | workspace-write, native Windows sandbox `unelevated` (as configured on this machine) | the flag; control succeeded inside the sandbox; outside writes failed with `UnauthorizedAccessException` |
| Antigravity CLI `agy` 1.2.12, no mode flag | `request-review` | `permission_mode` in the stream's init event |
| Claude Code CLI 2.1.283 | not run | `claude auth status` → `loggedIn: false`; the probe returned "OAuth session expired". Signing in is not mine to do |
| This session's shell (bypassPermissions) | non-counting baseline | the session's own mode |

An early pair of Codex runs was discarded: its probe used `Remove-Item -Recurse -Force`, which
Codex rejected as "blocked by policy" in every location, the control included, so it measured the
command, not the location. The counting probe uses plain .NET create/write/read/delete calls.

### G2: H1 results

| Surface | Workspace (control) | `~/.tfw/work/<ID>` | `%LOCALAPPDATA%\tfw\work\<ID>` | `%TEMP%\tfw\work\<ID>` |
|---|---|---|---|---|
| Codex `exec --sandbox workspace-write` | ok | **(b)** denied by the sandbox; interactive on-request asks to escalate | **(b)** same | **(a)** ok |
| Codex, `%TEMP%` pointed at a new owner-only folder | ok | — | — | **(a)** ok; Codex added a Modify entry for its sandbox identity to that folder at run time |
| Antigravity, file tools (`write_to_file`, `view_file`) | ok | **(b)** "write_file" permission needed; headless auto-denied | **(b)** same | **(a)** ok, also with `%TEMP%` pointed outside the workspace tree |
| Antigravity, terminal tool | needs approval (control too) | same as control | same | same |
| Baseline, this session (bypass) | ok | ok | ok | ok |

Reading: in the default modes observed here, the system temporary directory behaves like the
workspace for Codex and Antigravity; both TFW machine-local roots need an approval the workspace
does not. The temp result is deliberate, not an accident of this machine's permissive `%TEMP%`
folder: it held when `%TEMP%` pointed at an owner-only folder outside the workspace tree.

The owner's own configuration on this machine runs without a sandbox: Codex `sandbox_mode =
"danger-full-access"` with `approval_policy = "never"`; Claude Code `permissions.defaultMode =
bypassPermissions`. In the owner's actual use every probed location is writable; the default-mode
results above describe ordinary users and receivers.

### G3: H1 documented defaults of the surfaces people use

- **Codex** (OpenAI, `learn.chatgpt.com/docs/agent-approvals-security`, accessed 2026-10-04): for
  the desktop app, CLI and IDE extension, "Version-controlled folders: `Auto` (workspace write +
  on-request approvals)"; non-version-controlled folders `read-only`. "The workspace includes the
  current directory and temporary directories like `/tmp`." "Codex requires approval to edit
  outside the workspace or to access network." For non-interactive runs it advises
  `codex exec --sandbox workspace-write`. Windows (`docs/windows/windows-sandbox`): agent mode "uses
  a Windows sandbox to block filesystem writes outside the working folder"; `elevated` is the
  preferred mode, `unelevated` the fallback; both the desktop app and the CLI use the native Windows
  sandbox. Writable roots extend through `writable_roots` / `--add-dir`.
- **Claude Code** (`code.claude.com/docs/en/permission-modes`, `/permissions`, `/desktop`,
  `/sandboxing`): "With Claude Code v2.1.283 or later, auto mode is the built-in starting permission
  mode for interactive terminal and VS Code sessions"; `claude -p` and the Agent SDK start in
  `default` (Manual). The Desktop Code tab offers a mode selector, reads the same settings files and
  states no separate built-in starting mode. In auto mode "file edits in your working directory are
  auto-approved"; everything else, including writes outside it, goes to a background classifier.
  `acceptEdits` auto-approves edits and `mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, `sed` only "for
  paths in the working directory or `additionalDirectories`"; Manual asks for every write. Sandbox:
  "runs on macOS, Linux, and WSL2. On native Windows, Claude Code runs commands unsandboxed"; "off
  by default"; when on, writes reach "the working directory, a per-user temp directory, and
  directories you've added", and Claude Code sets `$TMPDIR` to that per-user directory, so
  "sandboxed and unsandboxed commands resolve `$TMPDIR` to different directories".
- **Antigravity** (`antigravity.google/docs/permissions/`): the Default preset runs commands "inside
  an isolated Terminal sandbox, which by default has access only to your workspace and system temp
  directories"; files outside the workspace default to Ask; allow rules take the form
  `write_file(/path)`.
- **Cursor** (`cursor.com/docs/agent/security/run-modes`; not installed here): default run mode
  Auto-review; the terminal sandbox (macOS and Linux only) gives read/write inside the workspace and
  "/tmp and platform temp directories are writable unless disabled"; External-File Protection
  "prevents the agent from automatically creating, modifying or deleting files outside the
  workspace"; extra writable paths go in `sandbox.json`.

Limitations: the Codex desktop app cannot be driven headless and was not trialled — the vendor
document says it shares the native sandbox with the CLI. Codex's preferred `elevated` Windows
sandbox was not trialled: its setup creates sandbox users and changes firewall and local policy,
which is a system security change outside this role. macOS and Linux rest on documentation.

### G4: H1 lifetime and identity of the temporary directory

- Linux: `systemd-tmpfiles` cleans `/tmp` after 10 days and `/var/tmp` after 30; where `/tmp` is a
  tmpfs (Debian's current default) it is empty after every reboot (Debian manpages, debian-devel
  2024). macOS: files in `/tmp` unaccessed for 3 days are deleted by the daily periodic job.
  Windows: Storage Sense is off by default but may switch itself on at low disk space and delete
  temporary files (Microsoft Learn, Storage Sense).
- The temp path is not one place for every tool: Claude Code's sandbox rewrites `$TMPDIR`; macOS
  gives each user a private `$TMPDIR` while `/tmp` is shared; Codex and Antigravity keep the
  inherited variable. On Windows all three probed tools used the same `%TEMP%`.
- Tools already treat temp as their own scratch space: Claude Code keeps this session's scratchpad
  under the system temp directory; `agy` wrote a Node compile cache into whatever `%TEMP%` it was
  given.

### G5: H1 existing TFW roots

`conventions.md` places `bindings.yaml` and `worktrees/` under `~/.tfw/` on POSIX and
`%LOCALAPPDATA%\tfw\` on Windows; the economics quote cache uses `~/.tfw/rates` on every OS
(`project_config.yaml`, `economics/README.md`, `tfw_economics.py` `Path.home()`). On this machine
both roots exist: `%LOCALAPPDATA%\tfw\` (bindings, worktrees, credentials — not opened) and
`~/.tfw/` (rates). A worktree under the TFW root is itself the Codex workspace when a role works in
it, so worktrees need no extra grant; a separate working folder would.

### G6: H2 census of this repository's reviews

Corpus: 343 review documents in `tasks/` and `workspace/` (148 `REVIEW*.md`, 195 `review/*.md`).
26 distinct documents cite a non-EV file under `evidence/` by path (121 citations: JSON 69, TXT 38,
XZ 7, JSONL 3, PNG 2, HTML 2; a 27th hit is a copy of one REVIEW inside another task's evidence); 12
mention screenshots, logs or images; 158 use repetition wording (reproduced, replayed, reran,
recomputed).

| How the cited raw file was used | Cases |
|---|---|
| Audited as an object; the claim established by the Reviewer's own repetition | RTBO E1–E9; RWNR V9–V11; TFW-60/AB E1, E2, E4–E8; SLC accounting and final output (own MkDocs build, 369 links); RCFR (defect found by reading the code and the Reviewer's own diagnostic run); ATC rev2 (own build); TLD C7 (built files checked, screenshot only corroborating) |
| Claim established only through the Executor's raw data | RTPSN V6–V8: live model trial records, 7 attempts, 702,852 tokens, nondeterministic — the Reviewer recomputed the summary from them; FA15ES V8/E12/E13: the Executor's PNG renders opened, not re-rendered, although re-rendering was possible; TKL O1: a 600-second bound read from timestamps in a raw seal file |
| Defect found only in a raw file | TKL O1: a step finished about 40 seconds late, ruled not material |
| Defect in the evidence itself, visible because it was committed | RWNR V7 (receipt without hashes or inputs; the semantic false greens were found independently); TFW-60/AB E3 (a rule transcribed, not an observed refusal); ASSISTED15 E20/E21 (captures carry a local file URL; PNG files with JPEG bytes); TKL O3 (whitespace in committed raw custody evidence) |

`knowledge/process.md` F32: three review returns in one task came from figures typed from memory;
the Reviewer caught each by re-running the command ("the command returns 16"). Its stated fix is
to re-take counts with one command before the RF "and put the raw output in the evidence file" —
the HL already maps this to the observed output carried inline in the EV row.

### G7: H2 external anchor

PCAOB AS 1105.08: "evidence obtained directly by the auditor is more reliable than evidence
obtained indirectly"; AS 1105 names reperformance — the auditor's independent execution of a
procedure — as its own evidence form (`pcaobus.org`, AS 1105). It supports C3 for repeatable
checks and gives no answer for an observation that cannot be repeated.

### G8: H5 who reads docstrings and comments in the receivers' stacks

| Stack | Program that reads it | What it reads |
|---|---|---|
| Python | `argparse` with `description=__doc__` (common idiom) | module docstring becomes `--help` text |
| Python | Typer (`typer.tiangolo.com`, Command Help) | function docstring is the command help |
| Python | FastAPI (`fastapi.tiangolo.com`, Path Operation Configuration) | endpoint docstring becomes the OpenAPI description, Markdown included, cut at `\f` |
| Python | FastMCP (`gofastmcp.com/servers/tools`) | docstring becomes the tool description and parameter descriptions sent to the model |
| Python | `doctest` (`docs.python.org`) | runs the `>>>` examples inside docstrings as tests |
| Python | PEP 263; ruff/flake8; coverage.py | `# -*- coding: … -*-` on line 1–2; `# noqa[: code]`; `# pragma: no cover` |
| JS/TS | TypeScript (`typescriptlang.org`, JS projects) | JSDoc types in `.js` under `checkJs` or `// @ts-check`; `// @ts-ignore`, `// @ts-expect-error`, `/// <reference …/>` |
| JS/TS | ESLint | `/* eslint-disable */`, `// eslint-disable-next-line` |
| YAML | yaml-language-server; yamllint | `# yaml-language-server: $schema=…`; `# yamllint disable-line rule:…` |
| Markdown | markdownlint (README); TFW install/update | `<!-- markdownlint-disable -->` family; `<!-- TFW:CODEX:START -->`/`END` and the Claude pair |
| Any | `help()`, pydoc, IDE hovers | render docstrings for a human reader; no program decision |

A docstring that a program reads is output text: its reader is whoever reads that output (a CLI
user, an API client, a model choosing a tool), so being program-read does not exempt it from the
value test.

### G9: H5 this repository's own code

Five scripts pass the module docstring to `argparse.ArgumentParser(description=__doc__)`:
`.tfw/economics/tfw_economics.py:1702` (shipped to receivers), `tools/tfw_doctor.py:277`,
`tools/check_git_blob_sizes.py:177`, `tools/migrations/2.0.0/migrate_board.py:1104`,
`docs/scripts/command_entry_eval.py:1135`. Deleting those docstrings changes `--help` — the H5 false
case "the Executor of this very task needs a docstring to satisfy a tool" holds for them. Other
program-read lines: shebangs in `tfw_economics.py` and `check_git_blob_sizes.py`; `# noqa: E402` in
`docs/scripts/test_gen_docs.py:11`; no PEP 263 line, no doctest. Program-read docstrings still
carry narrative: `migrate_board.py`'s 31-line module docstring explains why the board was retired.

### G10: H7 census in `.tfw/`

Listed pattern, case-insensitive:
`\b(historical(ly)?|legacy|retired|remains? readable|readable at (its|their) original|never issued?|old receivers?|older receivers?)\b`.
Scope: tracked `.tfw/` files except `CHANGELOG.md` and `migrations/` (history by purpose, 266
lines) and `update_receipts/` (frozen before-copies, 30 lines).

- 169 matching lines in 42 files, against 65,713 words of live `.tfw/` Markdown.
- Largest: `conventions.md` 41, `workflows/knowledge.md` 11, `workflows/init.md` 10,
  `glossary.md` 10, `workflows/update.md` 7, `workflows/docs.md` 6, `workflows/config.md` 6,
  `templates/KNOWLEDGE.md` 6, `economics/README.md` 6, `compilable_contract.md` 6,
  `templates/status.md` 5; 31 files hold 1–4.
- Terms: historical 84, legacy 70, retired 15, "remains readable" 14, "never issue(d)" 6. The HL's
  phrase family proper (historical with readable or never issue on one line): 7 lines.
- "Legacy" is partly a defined term (for example legacy D/topic rows in `KNOWLEDGE.md`), not prose
  about the past.
- Classification criteria, fixed now and applied in Extract. Protective rule: tells an agent what
  to do or not do with an old artifact or receiver (read, refuse, preserve, never rewrite); removing
  it changes behaviour. Duplicate rule: operative but restating a rule stated elsewhere. Chatter: no
  operative effect — history, rationale, notes to future agents. Anchor: ISO/IEC Directives Part 2,
  notes "shall not contain requirements … Notes should be written as a statement of fact"
  (`iso.org/sites/directives/current/part2`). The census exceeds the planned 150-line sample
  threshold only slightly; Extract classifies all 169 lines instead of a sample.

### G11: Queries and files

Web (27; soft limit 5, exceeded with the Coordinator's leave): H1 — Codex sandbox search; OpenAI
security, sandboxing, agent-approvals-security, windows (404), windows-sandbox and config-basic
pages (two redirects); Codex Windows sandbox search ×2; Claude Code permissions, permission-modes,
desktop and sandboxing pages; Cursor search and run-modes page; Antigravity search and permissions
page; OS temp-cleanup search. H2 — PCAOB AS 1105 search. H5 — FastAPI/FastMCP/Typer search;
TypeScript/ESLint search; YAML/markdownlint search; markdownlint README; doctest/PEP 263/coverage/
ruff search. H7 — ISO/IEC Directives Part 2 search.

Project files opened beyond grep counts: H2 — RWNR `phase-a/review/verify.md`, RTPSN
`phase-a/review/verify.md`, SLC `REVIEW__…SLC.md` (one section), `knowledge/process.md` F32; context
lines from the other 22 cited reviews. H5 — the five scripts above (docstrings via `ast`). H1 —
`conventions.md`, `project_config.yaml`, `economics/README.md` by grep. Outside the repository, H1:
the owner's Codex and Claude Code settings, sandbox and permission keys only.

Trial side effects: no file remains in any probed location; Codex left Modify entries for its
sandbox identities on the temp folders it used, which is its normal operation; Antigravity recorded
six headless conversations in its local history; Codex ran with `--ephemeral`. The throwaway
workspaces and raw outputs are deleted after this record.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| H1: in default modes the system temp directory is writable like the workspace for Codex (Windows trial; POSIX docs), Antigravity (Windows trial; docs) and Cursor (docs); both TFW roots need an approval in Codex and Antigravity | Claude Code live trial blocked: CLI not signed in. Codex app and `elevated` sandbox documented only |
| H1: temp lives days, not weeks (macOS 3 days unaccessed, Linux 10 days or reboot); `$TMPDIR` differs between tools | Weigh against C3 and Closing step 6 in Extract |
| H2: 26 of 343 reviews cite raw executor files; most with own repetition; three claims rested on raw data (live model trials, renders, a timing); one non-material defect found only in raw data | Decide in Extract what an EV row must carry for an observation that cannot be repeated |
| H5: docstrings are program-read in argparse, Typer, FastAPI, FastMCP, doctest; five scripts here, one shipped | Exception wording and the Reviewer's listed command (Extract) |
| H7: 169 lines in 42 live files; seven in the HL's phrase family proper | Classify all 169 (Extract) |

**Sufficiency:**
- [x] External source used? 27 web queries and fetches
- [ ] Briefing gap closed? — all except the Claude Code trial
- [x] Dimensions identified? seven

Knowledge handover: material as above; inspected scope in G11; uncertainty — Claude Code
default-mode behaviour unobserved, Codex app and `elevated` sandbox documented only, POSIX
documented only; no knowledge publication. Continuation: on the Coordinator's answer, Extract.

Stage complete: YES
→ User decision: Coordinator's ruling (addressed message, 2026-10-04): Gather closed; go to Extract.
1. Claude Code trial: path (a). Signing in is the owner's action and the Coordinator asks the owner
   separately; Extract does not wait. If the sign-in appears before synthesis, the trial is added
   here as a separate dated section without rewriting what is recorded; if not, RES records that
   the DoD 9 trial for Claude Code awaits the owner's sign-in and that the current basis for Claude
   Code is vendor documentation. The trial is not counted as done and removing the criterion is not
   proposed (the owner decides at the TS stop).
2. Auto-mode rule accepted: a classifier pass is outcome (a), marked "automatic check,
   nondeterministic"; a classifier block is outcome (b). Record the Claude Code version and the
   exact mode string.
3. Extract inputs: the three H2 cases where a verdict rested on executor data and the outcome of the
   169 H7 lines feed the decisions on C1, C3 and C5; for each tool where a location gave outcome (b),
   name the setting that removes it.

## Addendum 2026-10-04 23:01 +05:00 — Claude Code trials after the owner's sign-in

Added on the Coordinator's instruction after the owner ran `claude auth login`; the sections above
are unchanged. Same four locations, same oracle, the auto-mode rule from the ruling above.

- **Surface:** Claude Code console CLI **2.1.289** (it updated itself from 2.1.283 since G1), signed
  in with a claude.ai account; this session's own engine is 2.1.286. Headless `claude -p` from a
  throwaway git workspace outside the repository.
- **Isolation:** `--setting-sources project` (the owner's user settings — `bypassPermissions`,
  allow-lists, additional directories — not loaded; the workspace has no project settings),
  `--strict-mcp-config`, `--safe-mode`, `--no-session-persistence`, and this session's `CLAUDE*`
  environment variables removed. `--permission-prompts none`: a prompt nobody can answer is denied,
  which is the Q1 rule.
- **Proof of mode:** `permissionMode` in each run's init event. A run with no mode flag reported
  `default`: headless `-p` starts in Manual. Per the vendor page, interactive terminal and VS Code
  sessions start in `auto` from 2.1.283.
- **Channels:** file tools (Write, then Read) and shell (one Bash block per location:
  `mkdir`, write, `cat`, `rm`, `rmdir`). Model reported: `claude-fable-5-1` in both trials.

| Mode string | Channel | Workspace (control) | `~/.tfw/work/<ID>` | `%LOCALAPPDATA%\tfw\work\<ID>` | `%TEMP%\tfw\work\<ID>` |
|---|---|---|---|---|---|
| `auto` | Write, Read | ok | ok | ok | ok |
| `auto` | Bash | ok | ok | ok | ok |
| `default` (Manual) | Write | denied: needs approval | denied | denied | denied |
| `default` (Manual) | Read | allowed without approval | denied: needs approval | denied | denied |
| `default` (Manual) | Bash | denied: needs approval | denied | denied | denied |

- **`auto`:** zero denials in 12 steps. Outcome **(a), automatic check, nondeterministic**, at all
  three outside locations. Per the vendor page, Write outside the working directory and
  non-read-only Bash both go to the background classifier. The stream does not record which
  approval path passed each call.
- **`default` (Manual):** every write needs a human, the workspace included, so the location changes
  nothing for writes. Reading back outside the working directory needs an approval the control did
  not need: outcome **(b)** at all three outside locations. No unattended role can write anywhere in
  this mode.
- **Temporary directory vs TFW root:** for Claude Code on Windows they behave the same in both
  modes. There is no sandbox on native Windows, and the permission layer treats both as outside the
  working directory.
- **Slip, corrected:** in the first Manual run, three Write steps failed with "File has not been
  read yet", because the auto trial's files were still in place (my cleanup was late). The
  leftovers were removed and the Manual trial was repeated with a new nonce; the table shows the
  repeat. The first run's other nine steps agree with it; its Read in the workspace ran without
  approval.
- **Side effects:** no files remain in any location; no Claude Code session was saved.
