# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260902-111644_CRATM](../../HL-TFW_20260902-111644_CRATM.md)
> Goal: a project declares who its participants are, a coordinator runs the task with a team of them in isolated trees under a contract it cannot move.

> Every number below was produced by a command run in this session on 2026-09-02/03 against
> `d:\projects\research\steps-framework` at `cdbc493`. Nothing here is quoted from an earlier task.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| **D1: how a Claude participant is reached** | peer interactive session, addressed by name | headless session: `claude -p` + captured `session_id` + `--resume` | in-process subagent | no delegation — the coordinator does it in sequence |
| **D2: how a Codex participant is reached** | interactive thread chain (the owner's current practice) | `codex exec` + `resume <SESSION_ID>` | `codex mcp-server` attached to the caller as an MCP server | file drop: a prompt written into the tree, picked up by a session the human opens |
| **D3: how the delegate's result returns** | text on stdout, read by the caller | `--output-last-message <FILE>` / `--output-format json` — a file the caller parses | a repository artifact (ONB, RF, REVIEW) the caller reads | a journal event only, detail in the artifact it references |
| **D4: what carries the writer's identity** | a new closed-schema key `writer` in the event | reuse the existing free-form `via` | a second principal key alongside `on_behalf_of` | the filename token (the pre-`2.0.0-dirty.3` design) | 
| **D5: how worktrees are occupied** | one per principal | one per phase | vendor-created, vendor-named (what Codex does today) | one shared tree, no isolation |

Five independent factors: who is reachable, by what call, how the answer comes back, where the name is
written, and where the work happens. D4 is independent of D1–D3 — the writer field is needed whether the
delegate is a peer, a headless run or a subagent, because what it records is the *write*, not the call.

## Findings

### G1: Eight peer Claude sessions, six of them three days old, and one answered a delegation

`ListAgents` from this session, twice, twenty minutes apart, returned the same eight peers:

```
kaznpu-ai-lab-8a       3d      innoforce-ai-first-bd  3d
kaznpu-ai-lab-a5       3d      helpdesk-2c            3d
kz-it-telegram-list-14 3d      innoforce-ai-first-25  3d
steps-framework-ea     1d      steps-framework-66     1h
```

Three sessions of one tool are open in **this** project at once (`-ea`, `-66`, and this one) — the canon's
rule that two sessions of one tool are two writers is not a thought experiment here, it is the
inventory. Two probes were sent, each asking for one line and no work:

| Target | Age | Project | Result |
|---|---|---|---|
| `helpdesk-2c` | 3 days | a **different** project | Answered in under a minute, with substantive state: *"d:\projects\research\helpdesk — last work: TFW update 2.0.0-dirty.4 → 2.0.0-dirty.5 (uncommitted) + field reports into TFW-60; currently idle."* |
| `steps-framework-66` | 1 hour | this project | Delivered (`success: true`, msg id recorded). **No reply had arrived** by the time this stage closed |

So: a three-day-old session in another project accepted a delegation-shaped message and returned
project state; a one-hour-old session in this project did not answer within the window. Delivery is
confirmed for both — the channel enqueues and drains at the receiver's next tool round — so
non-response is the receiver's state, not a lost message. **`knowledge/constraint.md` F11 is false as
written**: peers are not a Codex-only capability. What F11 got right is that this says nothing about
reliability.

### G2: Addressable and creatable are two different capabilities

Nothing in this session can *create* a peer. Peers are interactive sessions a human opened; the tools
available create either an in-process subagent (dies with the turn) or a headless run. Measured: the
two headless sessions this iteration created do **not** appear in `ListAgents`. The honest three-way split:

| Shape | Created on demand? | Survives the caller? | Addressable by name later? |
|---|---|---|---|
| peer interactive session | **no** — a human opens it | yes | yes, by its listed name |
| headless `claude -p` session | **yes** | yes — transcript on disk | by `session_id`, not by name |
| in-process subagent | yes | no | no |

### G3: The reverse crossing works first try; the forward crossing needed three things said in words

**Codex → Claude.** `claude` is on `PATH` (`/c/Users/c0rpa/.local/bin/claude`, 2.1.109). One call:

```
claude -p "Reply with exactly one word: PONG" --model haiku --output-format json
→ exit 0 · 5.7 s wall (1.6 s model) · result "PONG" · session_id 41bd5295-…
  usage: 10 input · 50 output · 33,644 cache read · $0.0040364
claude -p --resume 41bd5295-… "What single word did you just say?"
→ exit 0 · 5 s · result "PONG" · same session_id · $0.0036819
```

The thread survived the process boundary and answered from its own history. Vendor documentation
confirms the mechanism and adds one fact worth having: a `-p` run is saved as a resumable session
unless `--no-session-persistence` is passed, and *"Claude Code finds the session by its ID in any
project on this machine"* — which is exactly the cross-project reach G1 measured on the peer channel.

**Claude → Codex.** `codex` is **not** on `PATH`; it exists only as `%APPDATA%\npm\codex.cmd`
(codex-cli 0.120.0). Four failures before any work happened, in this order:

| # | What was run | What happened |
|---|---|---|
| 1 | `codex exec -s read-only "…"` | `Error loading config.toml: unknown variant 'default', expected 'fast' or 'flex'` in `service_tier`. The owner's live config is unreadable to the installed CLI |
| 2 | `… -c service_tier="flex"` | API `400 Unsupported service_tier: flex`. The CLI accepts two values and the API accepts neither of the two |
| 3 | `… -c service_tier="fast"` | API `400 The 'gpt-5.6-sol' model requires a newer version of Codex` — the config's model is newer than the binary |
| 4 | any of the above under a captured stdin | `Reading additional input from stdin...` — the run blocks until stdin closes |

Plus a permanent non-fatal pair on every run: `codex_models_manager::cache: failed to load models
cache: unknown variant 'max'` and `failed to refresh available models`. What finally ran:

```
codex exec -s read-only -c service_tier="fast" -m gpt-5.4 -c model_reasoning_effort="low" \
  "Reply with exactly one word: PONG" </dev/null
→ exit 0 · 16 s · prints "PONG" · "tokens used 43,466"
```

So H5's forward direction is real — stdout, not an exit code — and it is reachable only by overriding
the owner's own configuration in three places. The cost asymmetry for one identical word:

| Direction | Wall | Billed | Per-call floor |
|---|---|---|---|
| Codex → Claude (`claude -p`, haiku) | 5.7 s | $0.0040 | 33,644 cached + 60 fresh tokens |
| Claude → Codex (`codex exec`, gpt-5.4 low) | 16 s | not reported by the CLI | **43,466 tokens** |

### G4: `resume --last` from a foreign caller attached to the owner's own thread

The natural two-stage form — dispatch, then follow up — was measured and it landed in the wrong place:

```
codex exec … resume --last "What single word did you just say?"
→ exit 0 · session id 01a06376-e119…  (started 23:52:10, transcript 2.8 MB, "tokens used 264,806")
  answer: "Контекст"
```

This session's three `exec` sessions started at 23:57:05, 23:57:27 and 23:57:47. `--last` chose none of
them: it chose a session opened five minutes *earlier* — the owner's own interactive Codex thread — and
answered out of that thread's context, in that thread's language. The rollout file's mtime moved to
23:59:18, so **the turn is now permanently recorded in a session this iteration was never delegated**.
The vendor documentation states the cause plainly: sessions created by `codex exec` are excluded from
`--last` unless `--include-non-interactive` is passed, and that flag does **not** exist in this build's
`codex exec resume --help`. The only safe form on this machine is `resume <SESSION_ID>` with the id
captured from the first run's own output.

Two further mechanics from the same help output: `-o, --output-last-message <FILE>` hands the
delegate's final message to the caller as a file, and `codex mcp-server` (stdio) exists in this build —
Codex can be attached to a Claude session as an MCP server rather than shelled out to.

### G5: Two vendors in one tree, and what a finished Codex run leaves behind

```
$ git worktree list
D:/projects/research/steps-framework                  cdbc493 [master]
C:/Users/c0rpa/.codex/worktrees/ac4b/steps-framework  4d885b4 (detached HEAD)
```

`~/.codex/worktrees/` holds **15** entries: 12 named by a four-hex token, and **3 named readably** —
`kz-intake-phase-a`, `kz-intake-phase-a-review`, `kz-intake-phase-a-smoke`. A readable, task-shaped
worktree name is therefore not something the protocol has to win from the vendor; it is already
achievable, and the vendor's default is what produced the opaque ones. Six of the token directories
contain an **empty** `steps-framework/` shell — 4.0 K, no `.git` file, no contents — while
`.git/worktrees/` holds exactly one admin entry. So a finished run's disposition is measured: the
contents and the registration are removed, and an empty directory is left. Litter, not a dangling tree.

Meanwhile, both research iterations of this task are running **in this same working tree** right now:
iteration 1 (Codex) wrote `research/iter1/1_briefing.md` at 00:03 and `2_gather.md` at 00:05 while this
file was being written into `research/iter2/`. Two vendors, one index, no collision so far — because
each writes only inside its own subfolder and neither has staged anything.

### G6: The journal corpus, counted

126 events across `tasks/` and `workspace/`:

| Composition | Count |
|---|---|
| `on_behalf_of` + `via`, no `actor` | 98 |
| both `actor` and `on_behalf_of` | 22 |
| `actor` only (pre-rule, two-part filenames) | 6 |
| neither | **0** |

`actor` values: `saubakirov` 25, **`claude-code` 2, `codex` 1** — three legacy events already name a
tool where a person was meant, which is the failure the field was retired for, preserved in place.

`via` values: `claude-code` 62, `codex` 33, `claude` 26 — and the spelling changed mid-corpus:
`claude` appears 26 Aug–29 Aug, `claude-code` from 29 Aug onward. **One tool, two spellings, no rule
broken**, because the field is declared free-form. Anyone counting writers by `via` gets two
populations for one participant.

### G7: The validator decides H9, and today it refuses the writer field

`.tfw/scripts/gen_index.py` declares `EVENT_KEYS = {time, kind, actor, on_behalf_of, via, from, to,
refs, summary}` and reports an unknown key as a **problem**. Probes against the live
`validate_event`, with the real `team/` profiles loaded:

| # | Event | Result |
|---|---|---|
| 1 | baseline new event | `[]` — clean |
| 2 | baseline **+ `writer: codex-lead`** | **`['unknown keys: writer']`** |
| 3 | `on_behalf_of: codex-lead` | `["on_behalf_of 'codex-lead' is not a declared team/ participant (saubakirov)"]` |
| 4 | real legacy shape `20260826-201231__transition.md` with `actor` only | `[]` — tolerated exactly as documented |
| 5 | **new** event carrying `actor: claude-code` | **`[]`** — accepted |

Row 2: the writer field is not markup. Until `EVENT_KEYS` gains it, **every new event carrying it
fails validation**. Row 3: the human-only rule for `on_behalf_of` is enforced in code, so a principal
cannot be smuggled through the existing field — the writer key is the only door. Row 5: the template's
*"do not add the field to a new event"* has no enforcement site, so a new event may reintroduce `actor`
today and pass. Live check for reference: `gen_index.py --check tasks` → **1 problem across 61 tasks**
(a 123-code-point summary in `TFW_20260902-112841_RDP`), so the corpus is otherwise clean and a new
failure introduced by Phase B would be visible immediately.

By contrast, `team_profiles()` parses a profile's front matter with `yaml.safe_load` and validates
**nothing**: no key set, no required keys, no unknown-key check. The three carriers the HL treats
alike are not alike:

| Carrier | Key set | Cost of one new field |
|---|---|---|
| `status.md` | closed — unknown key is an error | edit the validator |
| journal event | closed — unknown key is an error | **edit the validator** |
| `team/{handle}.md` | **open — nothing is checked** | none |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| 8 peers, one 3-day-old cross-project peer answered a delegation; F11 is false as written | whether an unanswered peer is busy or unreachable — not separable from outside |
| Peers can be addressed but not created; headless sessions can be created and resumed by id | nothing outstanding for this iteration's scope |
| Both crossing directions verified with real runs; the forward one needs three overrides and costs 43,466 tokens a call | whether a current Codex build removes the three overrides — cannot be tested without upgrading the owner's machine |
| `resume --last` attaches to the owner's interactive thread and leaves a turn in it | — |
| 15 worktree dirs, 3 already readably named, 6 empty shells left behind, 1 live Codex tree at detached HEAD | merge cost — H3, iteration 1's assignment, deliberately untested here |
| 126 events, 0 without an accountable party, 3 legacy events naming a tool, `via` spelled two ways | — |
| `writer` fails the shipped validator; `team/` profiles are validated by nothing | whether `gen_index.py` counts as "nothing executable" under DoD 16 — a contract question, raised in Challenge |

**Sufficiency:**
- [x] External source used? — Claude Code headless/sessions documentation; OpenAI Codex non-interactive documentation, which supplied the cause of G4
- [x] Briefing gap closed? — H4, H5 and H9 each have measurements; the three shared hypotheses carry data for Challenge
- [x] Dimensions identified? — five, each with ≥3 alternatives

Stage complete: YES
→ User decision: gates waived by the owner for this iteration ("no questions to me"); advancing to Extract

---

## Addendum — 2026-09-03, `codex-cli 0.152.1`

> Appended after the stage closed, when the owner upgraded the Codex CLI. Nothing above is edited;
> this block records what changed and what was over-claimed. Q1 of the RES asked exactly this.

`codex-cli 0.120.0` → **0.152.1**. Re-run in `d:\projects\research\steps-framework`, same prompt:

```
codex exec -s read-only "Reply with exactly one word: PONG"      ← no overrides, no redirect
→ exit 0 · 10 s · model gpt-5.6-sol, reasoning effort xhigh (the owner's own config)
  "PONG" · tokens used 5,030 · 368 bytes of output
codex exec -s read-only resume 01a063b7-a108-… "What single word did you just say?"
→ exit 0 · 9 s · "PONG", answered from the thread's own history · tokens used 18,623
```

| Measure | 0.120.0 | 0.152.1 |
|---|---|---|
| Config overrides needed to run at all | **3** (`service_tier`, `-m`, effort) | **0** |
| Owner's `config.toml` | refused (`unknown variant 'default'`) | loads |
| Model | had to be forced to `gpt-5.4` | `gpt-5.6-sol` at xhigh — the owner's own |
| `codex_models_manager` decode errors | on every run | none |
| Output volume for one word | 307,553 bytes (the server's model catalogue) | 368 bytes |
| Cold call, one word | 16 s · 43,466 tokens | **10 s · 5,030 tokens** |
| Follow-up by explicit `SESSION_ID` | not reachable | ✅ 9 s · 18,623 tokens |
| `--include-non-interactive` on `exec resume` | absent | **still absent** |

**One claim above is corrected, not updated.** G3's failure row 4 reads *"the run blocks until stdin
closes"*. That was an over-claim: what was observed was the informational line `Reading additional
input from stdin...`, never a hang. Re-tested on 0.152.1 with no redirect and a 45-second cap: exit 0
in 8 s. `</dev/null` is a tidiness measure, not a requirement.

**Two findings survive the upgrade unchanged.** `codex` is still not on `PATH` — only
`%APPDATA%\npm\codex.cmd` — so a foreign caller still needs the absolute path. And
`--include-non-interactive` is still missing, so there is no reason to believe `--last` has stopped
preferring interactive sessions. **It was deliberately not re-tested**: the only way to test it is to
write into a session nobody delegated, and doing that once (G4) was already one trace-integrity
incident too many. The safe form is unchanged and now measured working: capture the session id from
the first run, follow up with `resume <SESSION_ID>`.

Note the cost shape: a follow-up (18,623) costs more than a cold call (5,030), because resuming
replays the thread. Chaining is not free even when the door is cheap.
