# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260902-111644_CRATM](../../HL-TFW_20260902-111644_CRATM.md)
> Goal: a project declares who its participants are, a coordinator runs the task with a team of them in isolated trees under a contract it cannot move.

## Configuration Space

Five dimensions with four alternatives each is 1,024 rows, so the template's reduction applies: C1 is
the configuration the HL's §3.1 already draws, and every further row differs from it in at least one
column. Nothing is evaluated here — eliminations are Challenge's work.

| Config | D1 Claude reached by | D2 Codex reached by | D3 result returns as | D4 writer carried by | D5 worktree |
|---|---|---|---|---|---|
| **C1** *(the HL as drawn)* | peer session by name | interactive thread chain | repository artifact | new `writer` key | one per principal |
| C2 | headless `-p` + `--resume` id | interactive thread chain | repository artifact | new `writer` key | one per principal |
| C3 | headless `-p` + `--resume` id | `exec` + `resume <ID>` | repository artifact | new `writer` key | one per principal |
| C4 | headless `-p` + `--resume` id | `exec` + `resume <ID>` | `--output-last-message` file | new `writer` key | one per phase |
| C5 | peer session by name | `codex mcp-server` over stdio | text on stdout | new `writer` key | one per principal |
| C6 | subagent | `exec` + `resume <ID>` | repository artifact | new `writer` key | one per phase |
| C7 | peer session by name | interactive thread chain | repository artifact | reuse free-form `via` | one per principal |
| C8 | peer session by name | interactive thread chain | repository artifact | second principal key | one per principal |
| C9 | no delegation (sequenced) | interactive thread chain | repository artifact | new `writer` key | one per phase |
| C10 | peer session by name | file drop | repository artifact | new `writer` key | vendor-created |
| C11 | headless `-p` + `--resume` id | `exec` + `resume --last` | text on stdout | new `writer` key | one shared tree |
| C12 | peer session by name | interactive thread chain | journal event only | new `writer` key | one per principal |

## Findings

### E1: The three carriers the HL treats as markup are two closed schemas and one open one

§3.1's file map lists three templates under Phase B — `team/profile.md`, `journal/event.md`,
`bindings.yaml` — and no code. The measurement in G7 splits them:

```
  team/{handle}.md   ── parsed by yaml.safe_load, no key set, no required keys ──► a new field is free
  journal event      ── EVENT_KEYS is closed; unknown key = problem            ──► a new field is a CODE CHANGE
  bindings.yaml      ── lives outside the tree, read by no shipped script      ──► a new field is free
```

So H7's migration question and H9's migration question have **opposite answers**, for the same reason
in reverse: `organization_role` and `project_role` cost nothing because nothing validates a profile,
and `writer` costs an edit to `.tfw/scripts/gen_index.py` because the event schema is closed on
purpose. Two consequences the HL does not currently carry:

1. **§3.1's change map is incomplete.** `gen_index.py` is not in it, and Phase B cannot deliver DoD 5
   (*"`type: agent` is consumed by something… named as a writer"*) without touching it.
2. **DoD 16 reads against DoD 5 for the executor who has to do it.** *"Nothing executable is added: no
   script, no hook, no daemon, no lock, no config key that selects behaviour"* forbids *adding*;
   extending the key set of a validator that already ships is not adding, and an executor should not
   have to infer that from the word "added" at the moment they are about to break the gate.

The same probe found the mirror-image gap: a **new** event carrying `actor:` validates clean, so the
template's prohibition has prose but no enforcement site — the thing §7.1 forbids in its own words.

### E2: MCP is the combination nobody proposed, and it is the same shape as the git decision

D2 Alt C was not in the HL's blind-spot list, and it changes what "a TFW-side mechanism" means. The
installed Codex build carries `codex mcp-server` (stdio); Claude Code is an MCP client and this session
has one server connected already (`playwright`, health-checked ✓). External reading confirms this is
not a local curiosity: MCP is the cross-vendor standard both tools implement in both directions over
JSON-RPC 2.0/stdio, with ACP (IDE integration) and A2A (agent-to-agent orchestration) as the two
neighbouring protocols for the same plumbing.

The structural point is §7 P8 applied to a second substrate:

| | mechanism owned by | protocol owned by | TFW writes |
|---|---|---|---|
| isolation | git (`git worktree`) | TFW | where a tree lives, who deletes it |
| **the crossing** | **the vendors' MCP/stdio** | **TFW, if it chooses to** | **what a dispatch must contain** |

This is not a proposal to adopt MCP — declaring a transport is TFW-61's subject and DoF 11 forbids
taking it here. It is the observation that the HL's "without a TFW-side mechanism" in H5 has three
answers, not one, and the cheapest of them (shell out and read stdout) is the one this iteration
measured working.

### E3: Only one return path survives the caller's death

Cross-referencing D3 against the failure modes measured in Gather:

| Return path | Survives caller exit | Readable by a third party | Auditable six months later | Cost |
|---|---|---|---|---|
| text on stdout | no | no | no | free |
| `--output-last-message` / `--output-format json` file | yes, until deleted | yes, if the path is declared | weakly — an untracked file | free |
| **repository artifact (ONB/RF/REVIEW)** | **yes** | **yes** | **yes — it is the trace** | the artifact's own cost |
| journal event only | yes | yes | **no** — the canon forbids an event carrying the detail | free |

C12 is therefore already excluded by the canon rather than by judgement: an event that carried the
delegate's result would be the journal becoming the next unbounded shared file. The HL's choice —
`dispatch` plus the role artifacts — is the only row that is both durable and permitted. What Gather
adds is that the vendors supply the *file* variant natively (`-o`, `--output-format json`), so the
handoff from a machine-readable result to a repository artifact needs no mechanism either.

### E4: A session id is not a principal, and `via` has already failed the identity job once

Three identity-shaped values were measured in this session, and they are not interchangeable:

```
  session id 41bd5295-…      unique, machine-generated, resumable, meaningless to a reader
  via: claude-code           free-form, spelled two ways for one tool inside one corpus
  team/ handle               declared, human, checked in code against the profile's type
```

The corpus proves the middle row cannot be promoted: `via` drifted from `claude` to `claude-code` on
2026-08-29 with no rule broken, because free-form is what it was declared to be. A writer field that is
also free-form inherits that drift on day one; a writer field that must resolve to a `team/` handle
demands a profile — which is the exact pressure that produced a profile per agent session in two
external projects. **H9's real content is not "can a field be added" but "what is the field checked
against"**, and the corpus contains both failures already: three legacy events name a tool in `actor`,
and `on_behalf_of` is checked in code and refuses `codex-lead` today.

### E5: The per-call floor makes a chatty protocol unaffordable, independently of auditability

One word cost 43,466 tokens through `codex exec` and ~33.7 K cached tokens through `claude -p`. A
delegation protocol with a per-call floor of tens of thousands of tokens is priced like a process
start, not like a function call. Two consequences that fall out of arithmetic rather than principle:

| Delegation shape | Calls per phase | Token floor per phase |
|---|---|---|
| whole workflow ("run `/tfw-handoff` for phase A") | ~1 | ~40 K |
| per-stage ("gather", then "extract", then "challenge") | ~4 | ~170 K |
| per-question chat between coordinator and delegate | 10–30 | 0.4 M – 1.3 M |

S2 records the owner pricing drift as *«сожрано куча токенов»*. The floor says the same thing about
granularity: whole-workflow delegation is the cheap shape whether or not it is the auditable one.
Whether narrower handoffs stay *permitted* is H6 and belongs to iteration 1; this is the price tag,
not the ruling.

### E6: The two role dimensions already exist, in the other edition, with their absence semantics written

`editions/02-assisted/team/README.md` declares each human profile as exactly five fields, two of which
are **`Роль в компании`** (organization) and **`Роль в проекте`** (project), and states the rule the HL
asks Phase B to invent: *"Корпоративная и проектная роли не объединяются: они могут совпадать,
различаться или быть неприменимы. `не указана` означает нехватку подтверждённых данных, а не
отсутствие роли."* Two dimensions, three absence values (`не применимо` / `не указана` / a value),
field-tested.

The same file also carries a design Full has not considered, and it is the closest thing to a
counter-proposal in the project: Assisted's third participant type is **`automation`**, not `agent`
(`team/automation-<slug>.md`, `Идентификатор: automation:<slug>`), and *"автономная task-роль
handoff/review обычно вообще не требует отдельного профиля: она наследует владельца из trace"* — an
autonomous role usually needs no profile at all, inheriting the owner from the trace.

S4 rules that a shared noun does not make two schemas one, and Assisted is out of scope by §3. Both
still hold with this on the table. What changes is that Phase B is no longer inventing two role
dimensions — it is choosing whether to match a sibling edition's wording or to diverge from it
knowingly, and the same question applies to `agent` versus `automation`.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| The three Phase B carriers are two closed schemas and one open one; `writer` is a code change and §3.1 does not say so | whether the owner reads a validator edit as "adding something executable" — a contract question for Challenge |
| MCP is a third, vendor-neutral answer to H5 that the HL never listed; same shape as the git decision | nothing here decides it — TFW-61 owns transport |
| Only the repository-artifact return path is durable and permitted; the vendors supply the file variant natively | — |
| A session id, a `via` string and a `team/` handle are three different things; `via` already drifted | what the writer field is *checked against* — the open question H9 actually turns on |
| Per-call floor is ~40 K tokens; chatty delegation is priced out before auditability is argued | — |
| Assisted already ships both role dimensions and their absence semantics, plus `automation` instead of `agent` | whether Full matches the wording or diverges — a Phase B decision, not a research one |

**Sufficiency:**
- [x] External source used? — MCP/ACP/A2A interoperability reading; both CLIs' own `--help` output as primary evidence
- [x] Briefing gap closed? — every dimension from Gather is cross-referenced; the writer question is now sharper than the HL states it
- [x] Configuration Space built from Gather dimensions? — twelve rows under the documented reduction rule

Stage complete: YES
→ User decision: gates waived by the owner for this iteration; advancing to Challenge
