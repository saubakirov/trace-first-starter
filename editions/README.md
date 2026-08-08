# TFW Editions

TFW Editions are different amounts of discipline for different kinds of work. They are not levels of personal maturity. The same person may use Light for a one-off analysis, Assisted for a recurring process, and Full for a long or high-risk project.

Each edition directory is a starter root. Copy the **contents** of the chosen directory into the root of your project. Do not use `editions/01-light/` as a nested working directory.

## Choose by the work

| Edition | Use it when | What it provides | Availability |
|---|---|---|---|
| **Light** | The work is one-off, educational, or exploratory; one person is responsible; the cost of a missed manual update is acceptable | Four short files for the goal, task list, task trace, and durable project memory | Available now in [`01-light/`](01-light/) |
| **Assisted** | Work repeats, two or three participants need separate ownership, or missed trace/status updates have become a recurring problem | The Light discipline plus Codex-supported structure and quiet checks | Available now in [`02-assisted/`](02-assisted/) |
| **Full** | The project is long-running, cross-functional, regulated, or expensive to get wrong; research, evidence, review, and knowledge gates are needed | The complete HL → RES → TS → ONB → RF → REVIEW lifecycle | Available as the repository's existing [`.tfw/`](../.tfw/) core |

Choose the smallest edition that matches the work. Move upward when the current edition's manual limits become observable, not because a title or technical background says you should.

## How the line evolved

Full TFW established the complete trace-first lifecycle. TFW-51 then tested a four-file Russian starter in a live seminar: people unfamiliar with the method could begin real non-code work immediately. That field result became Light.

Light deliberately leaves routine visible. The agent must create and maintain each task trace, update task status, and transfer durable knowledge by hand. These limits teach the method and are acceptable for compact work. Assisted addresses those observed omissions with status folders and Codex lifecycle checks while keeping its limits visible.

There is no `03-team/` directory. Organization by multiple agent roles is a separate future concern, not an edition delivered by TFW-52.

## Moving between editions

- **Start Light:** copy the contents of [`01-light/`](01-light/) into a clean project root and follow its README.
- **Light → Assisted:** use [`02-assisted/MIGRATION.md`](02-assisted/MIGRATION.md); preserve the Light goal, tasks, traces, results, and memory before activating the new contract.
- **Any edition → Full:** adopt the complete `.tfw/` lifecycle when the work needs formal planning, research, evidence, independent review, or knowledge consolidation.

Every edition keeps the same forward contract: understand the user's goal, plan backwards from a useful result, preserve the task trace, separate durable knowledge from temporary context, and leave enough context for the next person or AI to continue.
