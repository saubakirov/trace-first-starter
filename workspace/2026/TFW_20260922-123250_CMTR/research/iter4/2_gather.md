# Gather — "What do we NOT know?"
> **Mindset:** Explorer. Map evidence layers and alternatives before narrowing; treat every inherited confidence as a question.
> **Test:** "Can each claim be assigned to an observed layer, provider surface, exact source, and comparison class?"
> **Parent:** [HL-TFW_20260922-123250_CMTR](../../HL-TFW_20260922-123250_CMTR.md)
> **Goal:** Before every separate TFW role launch, choose the least-resource model and reasoning depth that still clears the quality floor for the exact work, using only choices actually observable on that platform.
> **Producer unit:** `codex:thread:local:01a0c8bf-5bbb-75f1-ac97-b8e640b531ae`
> **Parent Coordinator:** `codex:thread:local:01a0c400-3e48-7422-bb86-3b34fe177aa5`
> **Briefing authority:** corrected `research/iter4/1_briefing.md` at source commit `cd7f4b817b26f7890cc17b997deccb30b7a96354`, landed at `9348a6938901fb75a3c1a59c32aa74846349dfe8`
> **Gather gate:** `journal/20260922-160545__gate_answer__3f7a.md` at Coordinator commit `2e43e5045704c2af945c95540604d55136f78391`
> **Observation date:** 2026-09-22

## Dimensions

Each row is an independent degree of freedom. Alternatives are evidence states or candidate choices, not recommendations.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| D1 — Quality-floor input | uncertainty / novelty | dependency breadth | oracle strength | consequence / reversibility |
| D2 — Selection candidate | actual Astra + high (iteration 3) | actual Sol + high (iteration 4) | counterfactual Sol + medium | counterfactual Terra/Luna pair |
| D3 — Evidence layer | requested arguments | resolved / effective settings | addressed delivery | result and material rework |
| D4 — Comparison class | same-work controlled trial | different-work contrast | within-launch counterfactual rationale | provider-doc capability comparison |
| D5 — Availability source | current task-tool roster | installed CLI roster/help | account/UI selector | general provider documentation |
| D6 — Addressable-unit proof | ready task/session ID | exact addressed send | bounded wait/readback | title/status readback |
| D7 — Prospective outcome | accepted without material rework | accepted after bounded rework | unresolved or escalated | completed but not fit for purpose |
| D8 — Economy measure | published per-token price | observed token/usage record | elapsed time / quota draw | completed-task cost including rework |

## Findings

### G1 — The two Codex launches establish different evidence, not an equivalent-work comparison

| Field | Iteration 3 | Iteration 4 | Evidenced conclusion |
|---|---|---|---|
| Exact work | Derive the rule and inspect three provider families end to end | Independently attack one completed RES against four bounded falsification questions | Different work; no model-quality or effort-quality comparison is valid between outcomes |
| Requested pair | `gpt-6-astra` + `high` | `gpt-5.6-sol` + `high` | Exact creation arguments are durable |
| Provision / delivery | Temporary client ID → ready task `01a0c89b…`; title/read/wait evidence; addressed activation | Temporary client ID → ready task `01a0c8bf…`; title write; addressed activation | Both are separate, directly addressable Codex tasks |
| Resolved / effective pair | Not exposed | Not exposed | Neither launch proves which backend model/effort actually ran |
| Outcome | Completed iteration-3 RES; stage gates accepted; source-scope correction recorded | Briefing first returned for two evidence-boundary corrections, then accepted | Outcomes are observable but task-different; acceptance does not prove the requested pair caused quality |
| Material rework | Ultra claim narrowed from a broad cross-surface implication | H3/H4 statuses corrected; equivalent-work and counterfactual limits added | Rework type is observable; model/effort causation is not |

Sources: iteration-3 dispatch `20260922-151933__dispatch__4b9e.md` at `f1ab1a03a2038d5b2887e4158c6c78fef58949e0`; supplemental dispatch at `dcc38f964e419eab1b389f31ae3d06dde6973fbd`; iteration-4 dispatch `20260922-155350__dispatch__9e2f.md` at `46aacbd96c0f360f0aa2736c12623153be57070d`; iteration-3 `RES.md` at Coordinator commit `46aacbd96c0f360f0aa2736c12623153be57070d`; iteration-4 gate answers at `e5c5fe50cb8f52dc2cbf51b340ecefb6c5408b54` and `2e43e5045704c2af945c95540604d55136f78391`.

### G2 — The iteration-4 rationale discriminates Astra from Sol, but not high from medium

The iteration-4 dispatch makes one real distinction: a bounded attack of an existing RES with an explicit HL oracle does not need iteration 3's end-to-end Astra launch. That supports the model downgrade from Astra to Sol as a rationale, while leaving effective execution and comparative quality unproved.

The same native `create_thread` declaration available to this task permits both `gpt-5.6-sol` + `high` and `gpt-5.6-sol` + `medium`. Holding model, tools, context capacity, role boundary, and task constant makes Sol + medium the cleanest cheaper plausible counterfactual. The dispatch cites “strong independent judgment” for `high`, but records no threshold or predicted failure that distinguishes `high` from `medium`. Sol + medium therefore remains neither sufficient nor insufficient: it is untested, and the rationale is presently under-discriminating at the effort boundary.

The current task-tool roster also exposes Terra and Luna alternatives. OpenAI's current API catalog describes Astra, Sol, Terra, and Luna with descending list prices—Astra `$10/$50`, Sol `$4/$20`, Terra `$2/$12`, and Luna `$0.20/$1.20` per input/output million tokens—and common tool categories. Those API prices establish plausible per-token economy, not Codex Desktop quota cost, completed-task cost, model availability after task creation, or quality sufficiency. The Codex task schema is the launch authority for this surface; the API catalog is only external cost/capability context.

[OpenAI model catalog](https://developers.openai.com/api/docs/models) · [OpenAI model-selection guide](https://developers.openai.com/api/docs/guides/model-selection)

The model-selection guide requires an explicit accuracy target and comparison against a smaller candidate while maintaining that target. CMTR has an approved goal and acceptance clauses, but no equivalent-work output from Sol + medium (or Terra/Luna) and no launch-specific measurable acceptance oracle yet. The honest Gather conclusion is provisional selection, not optimum or demonstrated minimum.

### G3 — Requested, resolved, delivered, outcome, and rework are five non-substitutable claims

| Claim | What would prove it | Present Codex evidence | Present status |
|---|---|---|---|
| Requested | Exact arguments supplied to task creation | Both dispatch traces record `model` and `thinking` | observed |
| Resolved / effective | Native response or run metadata naming applied model and effort after policy/fallback | `create_thread` return and subsequent task tools expose no such fields | unavailable |
| Delivered | Ready address plus exact task-addressed activation and bounded readback | Ready task IDs, title/read/wait evidence, addressed activation | observed |
| Outcome | Returned artifact evaluated against its own exact work | Iteration-3 RES and accepted iteration-4 Briefing | observed, different work |
| Rework | Durable returned correction tied to the artifact defect | Iteration-3 Ultra narrowing; iteration-4 two-item Briefing correction | observed, cause unassigned |

No arrow between these rows is automatic. Requested arguments do not prove effective settings; delivery does not prove quality; acceptance does not prove minimum cost; rework does not identify model or effort as the cause. This applies project knowledge D59 (availability ≠ tested) and D78 (non-substitutable evidence rungs; no causal overclaim), plus North Star NS2/NS3: preserve material grounds and reject untested capability claims.

### G4 — Antigravity CLI has a strong candidate contract; IDE and complete TFW launch readiness do not inherit it

Read-only native observations on this host:

- `agy --version` returns `1.2.8`; iteration 3 recorded `1.2.7`, demonstrating that even same-day exact versions are not durable core policy.
- `agy models` fetched a live CLI roster including Gemini Flash low/medium/high variants, Gemini Pro variants, Claude Sonnet/Opus thinking variants, and GPT-OSS 120B medium.
- `agy --help` exposes `--model`, `--effort low|medium|high`, `--conversation`, `--continue`, `--input-format`, and `--output-format`.

Google's native headless documentation adds two useful boundaries: an unknown `--model` fails non-zero instead of silently falling back, and stream/json results carry a `conversation_id`, status, cumulative usage, and turn results. The initialization record includes `model` only when the caller explicitly set it. These mechanics can support a future CLI pilot and return contract, but no inference run, complete TFW role chain, owner-visible IDE selector, IDE account roster, or IDE addressed return was exercised here. CLI evidence cannot prove IDE behavior.

[Google Antigravity headless-mode documentation](https://antigravity.google/docs/cli/headless/)

### G5 — Claude Code documents readback paths and also documents substitution/clamping risks

Read-only native observations on this host:

- `claude --version` returns `2.1.278 (Claude Code)`.
- `claude --help` exposes session-scoped `--model`, `--effort low|medium|high|xhigh|max`, `--session-id`, `--resume`, `--bg`, `attach`, `logs`, and background-session management.

Anthropic's current Claude Code model configuration says `/model` and `--model` select a model, `/status` and the status line expose the current model, and the session header shows current effort. It also documents why launch flags alone are not proof: organization allowlists can substitute or reject a model; in JSON/stream output the actual model must be read from `modelUsage`; organization/model limits can clamp effort, silently in JSON/stream or background cases. Therefore iteration 3's Claude controls are documented candidate mechanics, not a verified current account roster or working TFW role chain. Claude Desktop remains a separate surface; installed Claude Code evidence does not establish its selector, availability, addressability, or return contract.

[Claude Code model configuration](https://code.claude.com/docs/en/model-config)

### G6 — Phase C needs outcome predicates that can fail, not a success-shaped trace

The evidence inventory exposes four prospective falsification families for later stages to test:

| Candidate predicate | Observation that would contradict it |
|---|---|
| The rationale selects the least-resource sufficient pair | An adjacent lower-resource pair passes the same predeclared work oracle with no greater material rework, while the rationale supplied no boundary excluding it |
| Dispatch reliably applies the selection | Native result/readback names a different effective model/effort, or the surface can silently substitute/clamp without a checked result field |
| Accepted outcome supports the selected pair | Acceptance depends on task-different evidence, post hoc criteria, or corrections material to the claimed quality floor |
| A provider binding is ready for a claimed TFW mode | The claimed surface lacks a current roster, separate visible unit, exact addressed return, or effective-setting readback required by that mode |

A completed artifact alone contradicts none of these failure cases. Conversely, bounded rework alone does not falsify the pair until the defect is traced to a predeclared quality requirement and competing explanations—context, instruction, source availability, tool route, or oracle weakness—are separated.

### G7 — Relevant project knowledge narrows the use of these observations

- `KNOWLEDGE.md` D59 forbids equating availability with testing; D78 forbids replacing one evidence rung with another. They require the five-layer separation in G3.
- `knowledge/process.md` F31 says stronger checking cannot repair a wrong reference point; iteration 3 and iteration 4 therefore cannot become a model comparison merely because both artifacts are reviewed. F37 requires method and revision for measurements; provider/version/cost claims are dated and scoped here. F49 keeps the cheaper pair as a research hypothesis rather than a premature owner choice.
- `knowledge/environment.md` F5 is human-grounded evidence that role/platform strengths differ, but frozen HL §3 forbids selecting from a role label; it may influence a risk hypothesis, never determine the launch pair.
- `knowledge/constraint.md` F11 requires installed-surface proof and says provider capability supplies neither identity nor authority. That supports the CLI/IDE/Desktop boundaries above.
- `.tfw/README.md` NS1–NS3 require inspectable grounds, proportional assurance, provider portability, and no untested capability claims. A policy that records only a fluent reason or successful artifact would fail those principles.

No incoming successor/correction/equivalence/conflict record was found for the exact cited knowledge identities in the current record space; their stated scopes remain applicable.

## OODA — Focused pass

- **Observe:** Durable Codex dispatch/gate records, current native task-tool schema, installed Antigravity/Claude read-only roster/help surfaces, official provider documentation, and scoped project knowledge were inspected.
- **Orient:** Evidence was separated by provider surface, claim layer, and comparison class. The strongest new gap is not model availability but the missing threshold between Sol `high` and Sol `medium` for the exact iteration-4 task.
- **Decide:** Subsequent stages may test rationale discrimination and define a prospective equivalent-work oracle. They may not infer effective settings, claim the cheaper pair sufficient, or compare iteration-3 and iteration-4 outcomes causally.
- **Act:** Carry D1–D8 and the five-layer evidence matrix into Extract; carry G6's candidate falsifiers into Challenge.

## Checkpoint

| Found | Remaining |
|---|---|
| The actual launches prove requested pair and delivery, not effective settings or minimum sufficiency | Native effective-setting evidence for either Codex launch remains unavailable |
| Sol + medium is the cleanest lower-effort counterfactual on the same current Codex surface | No separately authorized equivalent-work trial or predeclared acceptance oracle exists |
| Antigravity CLI 1.2.8 exposes roster, controls, conversation IDs, status, and usage; unknown model names fail loudly | No CLI TFW pilot, IDE selector/account evidence, or IDE role-chain return |
| Claude Code 2.1.278 exposes launch/session controls and documents model/effort readback | No live account picker/result, no effective-setting observation, no complete chain; Desktop remains untested |
| Four prospective falsification families are observable in principle | Exact Phase C acceptance thresholds and controlled trial design remain for Extract/Challenge and Coordinator decision |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed for Gather: sources, evidence layers, candidate alternatives, and unknowns are bounded?
- [x] Dimensions identified?

**Gather decision:** Preserve Sol + medium as a counterfactual only; carry requested/resolved/delivery/outcome/rework as separate fields; treat every provider claim as surface-specific.

Stage complete: YES
→ User decision: pending Coordinator gate — close Gather or request one bounded correction
