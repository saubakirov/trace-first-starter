# HL — TFW-55 / Phase A: Project North Star Essay

> **Date**: 2026-08-26
> **Author**: Coordinator
> **Status**: ✅ APPROVED — owner-approved derivation 2026-08-26; master contract remains frozen at `a60bc6d`
> **Parent HL**: [HL-TFW-55](../HL-TFW-55__canonization_program.md)
> **Master freeze**: `a60bc6d` — `[codex/TFW-55/freeze/coordinator] re-freeze owner-approved canon architecture`
> **Research**: [Iteration 1](../research/iter1/RES.md) · [Iteration 2](../research/iter2/RES.md)
> **Authority**: derivation-only; the master HL owns Vision, Target State, Phases, DoD, DoF, and Principles

---

## Context

Phase A rewrites one production file: `.tfw/README.md`. It becomes the English **Project North Star** and shortest complete explanation of TFW's stable meaning. It does not rewrite the operational specification, the root landing pages, or the working Body of Knowledge.

The owner has selected this architecture after research:

```text
Philosophy of Trace
        ↓ grounds
TFW methodology
        ↓ is realized by
workflows and implementations
        ↓ one self-applying reference example
this repository
```

`Methodology` is an owner positioning decision, not a category or novelty established by Iteration 2. The public explanation must therefore earn the word through a clear function, minimum composition, exclusions, and observable consequences.

## Source Authority for Phase A

| Source | Phase A role | Not allowed |
|---|---|---|
| `Книга TFW/мини-эссе 0.8/` — nine essays | Primary author voice, problem-led order, metaphors, and conceptual language | Copying the series wholesale or preserving an overclaim because it reads well |
| `Книга TFW/body of knowledge/00. Архитектура TFW.md` | Owner-approved architecture and working definition | Treating the external Obsidian file as repository authority after the rewrite |
| `Книга TFW/body of knowledge/version 0.1.md` | Completeness, contradiction, hypothesis, and risk checklist | Calling the draft BoK canonical, hiding its open status, or expanding Phase A into a BoK |
| TFW-55 Iteration 1 and 2 RES | Evidence limits, competing explanations, F1–F4/R1 completeness checks | Exposing research labels as the essay's teaching structure or claiming human-learning evidence |
| Current `.tfw/README.md` and repository corpus | Material to retain, qualify, subtract, and link | Treating every historical/current mechanism as timeless meaning |

## The Result the Owner Will Review

### Definition contract — semantic preview, not mandatory final prose

> **TFW is a methodology for joint work between people and AI, grounded in the Philosophy of Trace. It applies when a person delegates part of intellectual work to agents: the person retains purpose, authority, judgment, acceptance, accountability, and the responsibility to stop; agents perform bounded work; selected durable traces preserve enough material context, decisions, result/current state, and continuation for the work to be inspected and resumed.**

The essay should reach this answer through the reader's problem, not open with a compressed definition dump. It must not begin with HL/TS/RF names, installation, or the Full lifecycle.

### Problem-led narrative map

F1–F4 and R1 remain internal completeness tests. Public prose uses ordinary terms such as Goal, Value, Question, Task, Context, Boundaries, Trace, authority, result/current state, and continuation.

| Order | Reader's question | Required answer | Source emphasis | Target words |
|---:|---|---|---|---:|
| 1 | Why does ordinary AI work disappear? | Much intellectual work becomes invisible; an agent can produce an output without preserving why it exists or how to continue | Mini-essays 01–02 | 150–190 |
| 2 | Why is chat not enough? | Model memory and chat history are useful raw material, not selected organizational memory or authority | Mini-essay 03 | 120–160 |
| 3 | What is a Trace? | A selected, durable, inspectable material record that makes purpose, decisions, state, and continuation visible; not transcript, private reasoning, or automatic truth | Mini-essay 04 + RES | 190–240 |
| 4 | What makes work continuable? | Goal and Value orient; Questions expose uncertainty; Tasks bound work; Context and Boundaries prevent drift; result/current state and next step or close preserve continuity | Mini-essays 05–06 | 230–280 |
| 5 | What remains human when agents do the work? | Purpose, legitimate authority, judgment, acceptance, accountability, and stop decisions remain explicit; agents receive bounded work | Mini-essays 02, 05 + RES | 170–210 |
| 6 | How can work “remember itself”? | Durable artifacts answer six operational questions and allow another human or agent to continue; this is neither consciousness nor independent authority | Mini-essay 07 + master §3 | 150–190 |
| 7 | What exactly is TFW? | Philosophy of Trace → TFW methodology → realizations/workflows; repository = self-applying reference implementation | Mini-essay 08 + architecture note | 190–240 |
| 8 | Why are Light, Assisted, and Full different? | They are proportional realizations; each adds coordination/assurance when risk requires it, and one observed teaching route—not the definition or a universal maturity law | Mini-essay 08 + RES | 110–150 |
| 9 | What is stable, what is not, and where next? | `NS1` purpose, `NS2` principles, `NS3` non-goals; North Star/spec/corpus/future-BoK authority; links to use and audit | Architecture note + master A2/A4 | 250–320 |
| | **Essay ceiling** | Coherent English essay readable in one sitting | | **≤ 2,000** |

### Project North Star contract

The essay contains three visible, citable anchors:

| ID | Content | Minimum test |
|---|---|---|
| `NS1 — Purpose` | Why TFW exists and what value it protects when intellectual work is delegated | A coordinator can reject work that does not preserve purpose, human authority, inspectability, or continuation |
| `NS2 — Principles` | A small stable set grounded in the Philosophy of Trace | Each principle changes an observable work choice; no slogan-only list |
| `NS3 — Non-goals` | What TFW must not become | Explicitly rejects: prompt/chat archive; deterministic generator; replacement for judgment; maximum-documentation bureaucracy; vendor-bound tool; untested capability claim |

Phase B will point to these same IDs from all three root READMEs. It must not invent a second North Star.

### Authority visible in the essay

```text
"Why does TFW exist; what must remain stable?" → Project North Star (.tfw/README + root pointer)
"What concepts and open questions need depth?" → future approved, versioned BoK (separate task)
"How does this implementation work today?"    → conventions · glossary · workflows · Editions
"Why did it become this?"                     → tasks · verified knowledge · Git history
```

The working Obsidian BoK remains source material. Phase A may explain the future authority slot in one concise sentence, but it must not create, publish, link as canonical, or pre-design the BoK.

### Values inherited from the master contract

| Value carried into the essay | Observable consequence in the text |
|---|---|
| Questions before premature answers | Open uncertainty is visible before a task is treated as solved |
| Human purpose remains human | No sentence gives an agent legitimate authority or accountability |
| Bounded delegation | Agent work has purpose/context, boundaries, and acceptance authority |
| Trace, not transcript | Selected material continuity is preserved; hidden reasoning is never required |
| Continuation over isolated output | A result identifies authority, current state, and next step or explicit close |
| Proportional assurance | Evidence, review, and verified knowledge scale with risk; Full artifacts are not universal minima |
| Self-application without mysticism | The repository can explain its change history; “self-aware” means inspectable capability only |
| Subtraction before addition | North Star content is funded inside the unchanged 2,000-word ceiling |

## Deliverables

1. Rewrite `.tfw/README.md` under the problem-led narrative and unchanged 2,000-word ceiling.
2. State one functional definition and the approved Philosophy of Trace → TFW methodology → realizations architecture.
3. Define selected Trace, continuability, human/agent boundaries, operational self-awareness, and proportional assurance in domain-independent language.
4. Designate `NS1` Purpose, `NS2` Principles, and `NS3` Non-goals as the `.tfw/README.md` half of the Project North Star.
5. State North Star / future approved BoK / living specification / corpus authority without creating a new surface.
6. Remove or qualify deterministic, code-centric, self-maintaining, same-artifact, provenance-only, absolute memory-ownership, and unbounded agent claims.
7. Preserve source and subtraction decisions in the normal Phase A evidence/RF trace, not in a public claims register.

## Explicitly Not in Phase A

- root `README.md`, `README.ru.md`, and `README.kk.md` — Phase B after Phase A REVIEW;
- the BoK — a separate next task after Phase A REVIEW;
- changes to workflows, templates, artifact contracts, Editions, adapters, configuration, or runtime behavior;
- a methodical guide, book, course, deck, university package, commercial offer, or brand redesign;
- proof of learning efficacy, terminology reception, adoption, market demand, or category novelty.

## Phase-Local Risks

| Risk | Control in TS |
|---|---|
| The essay becomes a summary of nine source essays | One narrative, ≤2,000 words, one job per section; source wording is material rather than structure to preserve verbatim |
| `methodology` is presented as research-proven elevation | Function/composition/exclusions lead; category and component novelty are not research claims |
| The North Star becomes slogans or a new registry | Three citable sections live inside the essay and have observable reject/accept tests |
| The draft BoK silently becomes authority | It is a checklist only; future approval requires a separate task after Phase A REVIEW |
| Founder language overclaims reproducibility, expertise, observability, or memory ownership | Required claim-disposition ledger narrows each claim before publication |
| Full mechanics creep into the opening | Artifact inventories and lifecycle explanation are excluded; living specification owns detail |
| Editions become pedagogical doctrine | Describe one observed problem-led route and proportional implementations; preserve evidence limits |

---

*HL — TFW-55 / Phase A: Project North Star Essay | 2026-08-26*
