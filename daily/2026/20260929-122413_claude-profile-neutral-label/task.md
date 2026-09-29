# Daily Task — 20260929-122413_claude-profile-neutral-label: Neutral source label in the Claude Code Coordinator profile

## 1. Source and attribution

- Human requester and acceptance authority: the project owner (`owner:saubakirov` in task records)
  in this Claude Code desktop chat; the app account is the owner's. No delegated Full-role authority
  is inferred.
- Request source: the first message of this chat. The app shows this session as started from parent
  session `local_e765482b-dbca-4147-92e0-68203ede7668`; who composed the message there is not
  observed. After an interruption, the human in this chat wrote “continue”.
- Worker: Claude Code desktop session `claude-code:session:local_42b07c8b-8152-45df-aea6-486d58b83e7f`
  (model `claude-opus-5-5`), worktree `hungry-moser-da2ce2`, branch `claude/hungry-moser-da2ce2`.
- Observed before the first product write: `2026-09-29T12:24:13+05:00`.
- Selected request excerpts (owner, this chat): “replace the private name in the current file with a
  neutral label (for example "the owner's dated Claude Desktop report") without changing meaning,
  capability claims or dates. Keep the change minimal.”; “Do not edit frozen historical records”;
  “Do not rewrite git history.”; “commit only your own files with an explicit path list”;
  “Ask the owner before pushing.”
- Related: `daily/2026/20260929-104929_claude-subagent-economics/task.md` (on local `master` at
  `0cd723a2`, not yet on this branch) found the same name in this profile, lines 8 and 33, and left
  it outside that Daily. This record acts on that finding.
- Follow-up excerpts (owner, this chat, 2026-09-29, after commit `8d7ee923`): «про pcux тоже недо
  убрать не понимаю зачкм лно там для кого в чем ценность? докажи покажи» and «что еще странного
  попало в конвенции ридми и т.д.?»
- Close excerpt (owner, this chat, 2026-09-29, after commit `4e3e2e6e`): «просто слей в мастер и
  закрывай задачу». The owner also asked what the 2026-09-23 date is for; answered in chat: it
  marks when the observations were made, so a reader knows they may be out of date.

## 2. Goal, Value and Boundaries

Goal: the shipped `.tfw/adapters/claude-code/coordinator.md` no longer names the owner's private
project; both mentions become a neutral label.

Value: every receiver that installs or updates TFW, and every reader of this public repository, gets
the Claude Code profile without the owner's private project name, while agents read the same dated
evidence limits as before.

Boundaries: change only the two affected phrases in that file, without reflowing lines, plus this
record; update any copy that must stay byte-identical. Frozen history stays untouched: `workspace/`,
`tasks/`, `.tfw/update_receipts/`, released `.tfw/CHANGELOG.md` sections, Git history and tags.
Meaning, capability claims and dates are preserved. Commit only these paths with
`git commit --only`. Push, merge into `master`, release and tags are reserved to the owner.

Completion oracle: the guard's own name list and matching (whole word, case-insensitive) finds no hit
in the file; the diff changes exactly two lines and only the name phrase in each, so dates and
capability statements are otherwise byte-identical; the local pre-commit guard reports no leak for
the committed paths; no other copy requires parity.

Revision — 2026-09-29: the owner's follow-up widens the change to the PCUX pointer in line 33 of
the same profile. The second question asks for a read-only inventory and authorizes no other change.

## 3. Context before action

- Rules inspected: `CLAUDE.md`, `AGENTS.md`, the owner's private preferences (not copied), the Daily
  entry, the canonical `.tfw/extensions/daily-task/SKILL.md` and its template, `.tfw/README.md`
  NS1–NS3, `RELEASE.md`, `.tfw/adapters/README.md`, `.tfw/adapters/manifest.yaml`,
  `.tfw/workflows/update.md` Step 4, and the local guard `.git/hooks/pre-commit` (outside the
  repository; its name list stays outside the repository).
- Current object at HEAD `01515878dbcafa9fd3e7182c83ddda1245e5ff53` (= `origin/master`):
  `.tfw/adapters/claude-code/coordinator.md`, blob `0917e9da36bdf9f896223a3e3ea2c35f85dd2040`,
  SHA-256 `fa0d7cb74960aa8e0dee27dafc345c56ea39f443aa67aa3bfabe8cfffe335b70`. The guard's list
  matches the private name twice: lines 8 and 33.
- History: the name entered this file on 2026-09-23 in PCUX commits `1893cd27` and `5ee5f190`; ATC
  `7dfed8bf` rewrote the file and kept both mentions. Tags `v3.6.0`, `v3.6.1`, `v3.7.0` and
  `v3.7.1` carry two mentions each; `v3.5.2` and earlier carry none. History and tags stay as they are.
- Governing source: PCUX HL §2 titles this source “Owner-Supplied Claude Desktop Field Report —
  2026-09-23”, and the profile itself calls such a source an “owner report”. The neutral label
  follows both.
- Copies and parity: searches of tracked files and the worktree for the profile's distinctive
  sentences find only this file. `CLAUDE.md`, `.tfw/adapters/claude-code/CLAUDE.md.template` and
  `.tfw/adapters/README.md` hold only the path pointer. The manifest maps the ten commands, not
  Coordinator profiles; profiles are `.tfw/` payload files that init and update deliver as they are.
  Byte parity binds command receivers and Codex skills, not this file. No tracked file records its
  hash; the docs generator does not publish `.tfw/adapters/`; no test pins its text.
- Mutation owner: ATC is DONE; PCUX is KNW and this is not its closure work. Active LFD
  (`TFW_20260929-003444_LFD`, TS_DRAFT on local `master` at `bd575c43`) does not list this file in
  its TS rev2 change table and has not changed it; SHI and TEQM (HL_DRAFT) do not mention it. No
  formal task owns this change.
- Prior-work lookup: `daily/2026/` on this branch and on local `master`, `KNOWLEDGE.md` and
  `knowledge/`, searched for this path, “private name”, “neutral label” and the guard. One match:
  the Related record above.
- Out of scope, not changed: the same name also appears in the released `[2.0.0]` section of
  `.tfw/CHANGELOG.md` (lines 1478–1479, frozen; the docs site republishes the changelog) and in
  `knowledge/environment.md` fact F6 (current knowledge, governed by the knowledge route).
- Changelog: `[Unreleased]` is empty; a two-phrase wording fix without behavior change is not a
  notable change for receivers, so no entry is added.
- North Star fit: NS1, the profile keeps its purpose, authority limits and a traceable source (PCUX
  HL §2) while no longer publishing a private name; NS2.2, the smallest complete change; NS2.5, push,
  merge and release stay with the owner; NS2.7, checks match the risk: the guard's own matching and
  a diff review.
- Consequential question: none open; the owner supplied the label and the boundaries.
- Planned replacement (`<name>` stands for the private name):
  - line 8: `the dated <name> report below` → `the owner's dated Claude Desktop report below`;
  - line 33: `The owner-supplied Claude Desktop <name> report` → `The owner-supplied Claude Desktop report`.

## 4. Result, decisions and check

Pre-action checkpoint: no product change is applied yet and no check result is claimed.

Completion addition — 2026-09-29:

- Result in `.tfw/adapters/claude-code/coordinator.md`: line 8 now reads “the owner's dated Claude
  Desktop report below is context, not today's capability receipt.”; line 33 begins “The
  owner-supplied Claude Desktop report selected in PCUX HL §2 is dated 2026-09-23 and scoped to that
  setup.” No other byte changed.
- Decision, line 8: the owner's example label. Its “Claude Desktop report” repeats the label of
  line 33, which holds the date. The 2026-09-27 note further down is also an owner report about
  Claude Desktop; the sentence's claim (context, not today's capability receipt) holds for both, so
  the wider reading changes no rule.
- Decision, line 33: only the name is dropped; “owner-supplied Claude Desktop report” was already
  neutral. Lines are not reflowed: line 8 grows from 91 to 105 characters, and its paragraph already
  has a 110-character line.
- No other copy and no changelog entry changed, for the reasons in §3.
- Checks:
  - the guard's name list with its matching: 0 hits in the profile (2 before) and 0 in this record;
  - `git diff --numstat`: `2 2`; word diff: line 8 adds `owner's` and replaces the name with
    `Claude Desktop`, line 33 removes the name; the date and every capability statement are
    unchanged;
  - LF line endings and the final newline preserved; `git diff --check` clean;
  - new blob `05616b2412b779029bd41d9ec54ae5fb682da95b`, SHA-256
    `1113d4b6bc886941d94b21dd955fd3ad3a3d439a1264fc9c2592a8d9c68e6d7d`;
  - the local pre-commit guard, run on exactly these two staged paths before the commit: no
    blocking finding and no leak warning.
- Limits: the name stays in the file at tags `v3.6.0`–`v3.7.1`, in Git history, and in receivers
  until they update. The out-of-scope places named in §3 still contain it. These checks prove the
  source text only; the change asks nothing new of any host.

Revision — 2026-09-29 (owner's follow-up):

- Result: line 33 now begins “The owner-supplied Claude Desktop report is dated 2026-09-23 and
  scoped to that setup.”; only the words “selected in PCUX HL §2” are gone.
- Evidence shown to the owner: the Claude Code Coordinator reads this profile at every new task, in
  this repository and in every project that installs TFW, because it ships in `.tfw/`. The pointer
  names section 2 of `workspace/2026/TFW_20260922-192606_PCUX/HL-TFW_20260922-192606_PCUX.md`,
  outside `.tfw/`, so no receiver has it, and it gives no path. That section is a working record
  that opens with the report's machine-local location and the private project's path. The date,
  scope and limits a reader needs stay in the profile; maintainers find the source with `git log -S`
  on this file (`1893cd27`, `5ee5f190`).
- Open point put to the owner: in a receiving project “the owner” means that project's owner, so
  “the owner's” (line 8, the owner's example label), “owner-supplied” (line 33) and “the owner
  reported … in other projects” (line 35) attribute the upstream maintainer's reports to the wrong
  person. No wording is changed for this until the owner chooses.
- Checks: `git diff --numstat` against `8d7ee923`: `1 1`; the word diff removes only that phrase;
  no “PCUX” left in the file; LF endings kept; `git diff --check` clean; the local guard on the
  staged paths reports nothing. Blob `fec79d213c3f230f2418778df774c0cef52a8d4f`, SHA-256
  `41ecb0034f94f59af7ed1ae18735f17c7f08cdd66f7441c65a124eaf034c8914`.
- Read-only inventory reported in chat, nothing changed: shipped text that only makes sense inside
  this repository — `.tfw/adapters/codex/coordinator.md:70` (PCUX), `.tfw/adapters/antigravity/coordinator.md:32`
  (“The owner reported”) and `:42` (PCUX), `.tfw/workflows/review.md:151` (AGSK) and
  `.tfw/workflows/knowledge.md:116` (TKL and a Git object of this repository), each with its
  `.claude/commands/` byte copy, `.tfw/compilable_contract.md:134` (TKL, SLC), `README.md:269`
  (TFW-60). Checked and left as they are: illustrative examples in conventions and templates, task
  history in migration guides, `.tfw/knowledge_state.yaml` (never created by init, never overwritten
  by update, left out of LFD's archive). No machine-local path or personal e-mail in current shipped
  text, `KNOWLEDGE.md`, `knowledge/`, `docs/` outside `docs/feedback/`, `tools/` or `team/`.

## 5. Next or close

Prepared and checked; committed on branch `claude/hungry-moser-da2ce2` in the commit that carries
this record. Not pushed and not merged into `master`. Owner acceptance is not inferred.

Next authority: the owner accepts the wording and decides how to publish it. This branch is
`origin/master` plus this one commit, so it can be published alone. Pushing local `master` as it
stands would also publish its unpushed commits; the Related record reports that some of them carry
the private name.

Revision — 2026-09-29: the PCUX removal is a second commit on the same branch. The local pre-push
guard, run as a dry run, passes for this branch; at the time of the check it warned for 17 of the
166 unpushed non-merge commits on local `master` (10 with a private name, 9 with a machine-local
path). Waiting for the
owner: acceptance of the wording, the choice on “owner” attribution, which inventory items to fix
and under which route, and whether and how to push.

Close — 2026-09-29: the owner accepts the result as it stands and closes this Daily (excerpt in §1).
The proposals on “owner” attribution and the inventory are not taken up here; they stay recorded
above for a later decision. Landing, as instructed: this branch is merged into local `master`. The
merge commit is built outside the shared main checkout and brought in by fast-forward, because that
checkout's index holds another session's staged files and `git merge` needs an index that matches
HEAD. Nothing is pushed; pushing remains the owner's decision.
