# Give feedback on TFW

Use the conversation where you encountered the problem. Your agent can inspect the installed TFW rule and the local evidence while both are still available.

> Примени tfw-feedback к последнему сбою учёта.

In English, try “Use tfw-feedback to investigate the last accounting failure.” For a feature question, say what decision you need to make.

After installing or updating to a revision that includes Feedback, Codex, Antigravity and Claude Code have a workspace skill named `tfw-feedback` for their selected adapter. You can also say “Read `.tfw/extensions/feedback/SKILL.md` and apply it to this incident.” This file route also works in Cursor. An older installation without the file needs an update to a revision containing it. [Read the skill](.tfw/extensions/feedback/SKILL.md)

## What comes back

The agent returns a title and a short issue body in the chat. It can inspect existing evidence and asks you before a new paid run. Here is an illustrative issue showing how far a saved refusal alone can take you.

> **Show which IDE version the accounting reader received and which it supports**
>
> **Impact** — A coordinator needs usage for a delegated task. The collection stopped, and the contributor had to open the reader's source to learn which version it expected.
>
> **Cause** — With the same saved input, the reader reports an unsupported version for 2.7.0. With its recognized version label, 2.17.0, it reaches the storage-layout check. The version guard's error omits both labels. Compatibility with real 2.7.0 calls is still open.
>
> **Proposed change** — Include the supplied and supported IDE versions in the error from `antigravity_snapshot`. To decide whether to extend the reader itself, compare one saved parent/child pair with the native model and usage, including whether the parent's counters include the child.
>
> **Check** — With a 2.7.0 input, collection still refuses, names both versions, and produces no token figure. A contributor can explain the missing measurement directly from that error.

Read and edit the complete draft. Remove anything that identifies your organization, project or users. Open **Issues** in the TFW repository named by `tfw.upstream` in your project's `.tfw/project_config.yaml`. Add the finding to a matching issue or create one for a distinct problem. Paste the title and body. You can also ask an agent with GitHub access to publish the reviewed text there. For an existing PR, add the relevant finding to its discussion. A suggested correction and a way to verify it are enough to start.
