# Gather — What do we not know?

> **Mindset:** Explorer. Map the choices before ranking them.
> **Parent:** [HL-TFW_20260923-223151_PTW](../../HL-TFW_20260923-223151_PTW.md)
> **Goal:** Identify the smallest adequate, inspectable Trace architecture for bounded one-worker work without weakening its result or continuation.
> **Producer / route:** `codex:thread:local:01a0d505-d0b4-76f2-ad95-58f1bf9cfe2e` → Coordinator `codex:thread:local:01a0cf4d-9254-7633-9ba9-393b0eb8e802`; dispatch `journal/20260925-010738__dispatch__ef88.md`, frozen HL `515b837`.

## Dimensions

These are independent choices; none is selected at Gather. The assessment criteria across them are North Star/Goal/Value fit, human-source and worker attribution, result/check/continuation completeness, per-task reads and writes, later retrieval, update isolation and migration risk.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| D1 Trace location | Separate dated `daily/YYYY/id/` | Beside the current object/product | Existing commit/PR/document only | Git note attached to a commit |
| D2 Record boundary | One compact `task.md` | `task.md` + versioned `brief.md` + `messages.md` | Task-local record plus current product source | Existing document's small decision section |
| D3 Distribution boundary | Optional package with owned template | Skill-bundled resource and explicit copy | Full manifest command | Project-local skill copy with manual update |
| D4 Name and identity | `tfw-daily-task` + timestamp/slug | `tfw-task` + stable opaque ID | `tfw-quick-task` + timestamp/slug | Object-scoped name/path |
| D5 Relation/discovery | Bounded search + exact links | Subject folders | Maintained subject journal | Generated read-only view |
| D6 Local form evolution | New records use package version | Project pins or forks local template | Upstream overwrites receiver template | Per-record inline form with no shared template |

## Findings

### G1 — TFW purpose and current Full boundary

**Observed source:** `.tfw/README.md` NS1/NS2/NS3 requires human-governed, continuable, selected Trace in inspectable ordinary files and proportional assurance. The frozen HL §3 proposes one-shot Daily outside formal `workspace/`, preserving formal Full roles. `.tfw/conventions.md` lines under `Evidence subfolder` and `Trace Discipline` still say “Every task directory” and “Every task” without a formal-task qualifier; the adapter manifest and README declare exactly ten Full role commands. `init.md` and `update.md` install/repair that manifest's selected command set.

**Researcher inference:** A local `daily/` folder can coexist physically with `workspace/`, yet unqualified canonical wording creates a real interpretation gap. An optional Daily package is not automatically covered by Full's current copy/update contract. A new template path alone proves no isolation or update parity.

### G2 — Field forms and object truth

**Observed source:** At the SenseLab source path named in HL §2, `.agents/skills/tfw-daily-task/SKILL.md` requires a three-file split, immediate work after record creation, project-specific `team/` attribution and complete substantive-message capture. Its `daily/2026/DAILY_20260908-200855_tfw-daily-task/task.md` records versioned brief, message IDs, deliverables, verification and explicit limits on cross-provider testing. Its `brief.md` preserves three meaning changes with sources. `daily/2026/20260920-152000_umbrella-stickers-pack2/task.md` keeps task decisions and verification while `docs/design/stickers/README.md` carries the current shared product catalogue. The Task says rebuilt/check completed and explicitly does not claim human acceptance or Telegram publication.

**Researcher inference:** The triad has observed continuation value when the request changes meaning, but its complete-message rule and identity scheme are local. Product truth beside the object and task history in a dated folder are already complementary in this case. Counting one versus three Markdown files cannot establish context cost without measuring reads and changes.

### G3 — A non-code boundary case

**Observed source:** Helpdesk's local, untracked `daily/2026/20260922-181342_upm-interview-kit/task.md` records the human request, owner, separate output and mapping files, a link to the formal UPM HL, the explicit boundary that it does not move UPM lifecycle, and the next owner action of moving material to Google Docs and handing it to Nikolai. HL §2 records this as a working-tree observation, not a committed or reviewed source.

**Researcher inference:** A commit/PR-only Trace cannot serve this local non-code case as-is. A document section could hold the selected Trace if the document is stable, accessible to the next worker and can state the exact continuation authority; those conditions remain to test.

### G4 — Durable links and an additional Git location

**External primary sources:** [GitHub's permanent-link documentation](https://docs.github.com/en/repositories/working-with-files/using-files/getting-permanent-links-to-files) states that a branch URL changes with its head while a commit-ID URL identifies the exact file version. [Git's notes documentation](https://git-scm.com/docs/git-notes) describes notes as separate refs attached to objects without changing them and explains their separate display, rewrite and merge configuration.

**Researcher inference:** A commit SHA can anchor a code Trace precisely, but link stability does not ensure the Trace contains the human's Goal/Value, authority, check and next step. Git notes add a no-folder storage variant absent from HL §10; because the note lives in a distinct ref with separate handling, portability and discoverability need explicit proof before treating it as a Daily default.

### G5 — Unknowns that can change the architecture

The current sources do not measure mean read/write cost of the one-file versus triad forms, retrieval failure in a larger Daily archive, generic installation into a clean Codex/Claude receiver, or the effect of a later update on a project-local Daily template. The HL's cross-provider and future-team claims therefore remain hypotheses. A no-folder document example must distinguish a mutable current document from a historical request record, and a commit/PR example must survive non-code work without a vendor-only memory dependency.

## Checkpoint

| Found | Remaining |
|---|---|
| Six independent design dimensions and four Trace locations, including Git notes beyond HL's comparison set. | Extract configurations that preserve the full selected Trace in both code and non-code cases. |
| Field Daily triad and object-centred product source have distinct observed roles. | Test whether one-file default saves reads/writes without erasing meaning revisions or actual source. |
| Current Full manifest/update path covers ten role commands, not an optional Daily package. | Identify a feasible opt-in update boundary and local-override rule; do not claim install parity without a trial. |

**Sufficiency:**
- [x] External source used: official GitHub and Git documentation, bounded to reference durability and Git notes mechanics.
- [x] Briefing gap closed: locations, record forms, package boundaries, naming and relation choices exposed.
- [x] At least three independent dimensions identified.

Stage complete: YES
→ Coordinator decision: Gather checkpoint pending; propose Extract.
