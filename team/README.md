# team/

One file per participant. Humans and agents alike — that is why this container is not
called `people/`.

A profile is **declared attribution**, not authentication. It records who a handle refers
to so that a task's owner and a journal event's actor mean something six months later. It
grants no permission and proves no identity.

## Files

| File | Participant | Type |
|---|---|---|
| [`saubakirov.md`](saubakirov.md) | Sanzhar Aubakirov | human |
| [`robert.md`](robert.md) | Robert | agent |

## Adding a participant

Copy [`.tfw/templates/team/profile.md`](../.tfw/templates/team/profile.md) to
`team/{handle}.md`, fill the applicable keys, and delete the guidance comment. A human needs
the four base keys. An agent also needs `accountable_to`, naming an existing human, and the
Boolean `may_rule_amendments`; `mentality` is optional descriptive guidance. The handle must
match the filename and use `[a-z0-9][a-z0-9-]*`.

An agent profile names a stable principal that answers directly to a human. A provider family —
`claude`, `codex`, `gemini` — is not an actor: two sessions of one tool must not acquire one
shared identity merely because they use the same provider. A profile alone neither activates AT
nor grants authority. After an approved HL is frozen and committed, the owner must explicitly
select the principal as LEAD and fix its bounded mandate; Coordinator, Researcher, Executor and
Reviewer remain distinct addressable working units and do not receive profiles of their own.

Which tool produced a record is still recorded — in the event's `via` field. What is gone is
the pretence that the tool was accountable.

## Who is acting in a session

One profile here — it is used, and nothing is asked.

Several profiles — the acting handle comes from a binding kept on the participant's own
machine, never in this tree: `~/.tfw/bindings.yaml` on POSIX,
`%LOCALAPPDATA%\tfw\bindings.yaml` on Windows, holding one mapping per project and nothing
else.

```yaml
bindings:
  /abs/path/to/project: saubakirov
```

No binding, a shared device, a copied binding, or a handle whose profile is gone: exactly
one short question before the first durable write. Once per session, not per turn.

Identity is never inferred from an OS username, a hostname, a folder name or an account
display string.

## What never goes here

Private preferences, device identifiers, machine-local paths, and any file naming the
current user. The binding lives outside the project on purpose: a project-local file can be
gitignored but not sync-ignored, so under file synchronization a per-user file reaches
everyone who shares the folder.
