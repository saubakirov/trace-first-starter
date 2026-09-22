# Gather — What establishes a usable launch choice?

> **Mindset:** Explorer; focused mode, one OODA pass.
> Parent: [CMTR HL](../../HL-TFW_20260922-123250_CMTR.md)
> Goal: Choose a sufficient model and reasoning effort for each actual launch, then economize within that quality floor.
> Producer: `codex:thread:local:01a0c89b-3d1e-7bd1-b8ab-a6376a7607d1`
> Parent / sole material return route: `codex:thread:local:01a0c400-3e48-7422-bb86-3b34fe177aa5`
> Authority: re-frozen HL `addb2e707dd9f271b7bf1287617a8b93b8d72cb0`; A2 `2c72ec8c6b0b21269caf95b707d26c631be5df52`; dispatch `f1ab1a03a2038d5b2887e4158c6c78fef58949e0`; origin `none`.
> Continuation: [Briefing answer](../../journal/20260922-152623__gate_answer__6af2.md) at `c3daca5182df3d4121582183cfb0dd38cb9ea433` inspected through `git show`; permits only Gather. Governing status remains Phase B `RES`, iteration 3 `in_progress`, assigned to this unit.
> Observation date: 2026-09-22, Windows / PowerShell. Repository base `839dfb07b90673c630b947de46a1598d21e63a36`; Briefing `d4d52c793df05295706161eb89765df69d8d8d18`.

## Dimensions

These are independent inputs or choices, not scored tiers. Alternatives remain open until Challenge.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| Uncertainty / novelty | Known transformation and examples | Missing facts retrievable from authoritative sources | Conflicting interpretations requiring judgment | Novel behavior without a reliable precedent |
| Dependency breadth | Local invariant | Several coupled artifacts | Multiple systems or providers | Long context with distant constraints |
| Verification strength | Deterministic check covers the consequence | Tests cover only some failure modes | Independent human/role judgment | No effective oracle currently available |
| Error cost / reversibility | Cheap isolated correction | Expensive rework across artifacts | Broad downstream reliance | Irreversible effect or purpose/authority error |
| Model capability constraint | Bounded transformation | Sustained synthesis and tool use | Adversarial judgment | Required modality/context/tool unavailable |
| Effort choice on a feasible model | Lowest exposed setting | Greater supported depth | Highest supported single-unit depth | Fixed/unexposed; no separate control |
| Availability evidence | Current host-native inventory | Current selector in the target session | Documentation/help only | No observable source |
| Enforcement and return | Native parameterized task plus exact return | Owner-operated visible session | CLI contract requiring a native pilot | No authorized usable route |

## Findings

### G1 — Evidence levels attach to claims, not provider brands

- **Verified:** a bounded observation reproduced here, such as a roster command returning values, or an installed help surface exposing a flag. A verified declaration is still only a declaration of runtime behavior.
- **Unverified:** documented/declared behavior has not been exercised on the target host/account; a plausible launch remains a candidate contract.
- **Unavailable:** the necessary observation/control is absent from this unit's accessible, authorized surface. It does not mean the provider cannot support it elsewhere.

This distinction applies `KNOWLEDGE.md` D59/D78, not an invented confidence percentage. Selection sufficiency, actual effective settings and causal savings need different evidence. A completed document cannot establish any of them by itself.

### G2 — Codex desktop: an exposed launch contract and a real addressed unit

**Verified native declaration:** this task exposes `mcp__codex_app__create_thread` with separate `model` and `thinking` arguments. The current calling-host roster in that tool's schema is:

| Model identifier, recorded as a dated observation only | Declared supported thinking values |
|---|---|
| `gpt-6-astra` | `low`, `medium`, `high`, `xhigh`, `max`, `ultra` |
| `gpt-5.6-sol` | `low`, `medium`, `high`, `xhigh`, `max`, `ultra` |
| `gpt-5.6-terra` | `low`, `medium`, `high`, `xhigh`, `max`, `ultra` |
| `gpt-5.6-luna` | `low`, `medium`, `high`, `xhigh`, `max` |
| `gpt-5.5` | `low`, `medium`, `high`, `xhigh` |

The tool declares account-default inheritance when parameters are omitted and validates destination-host combinations. Repository work uses a project and a separate worktree; queued creation returns a `clientThreadId`, which is not a usable `threadId`. `send_message_to_thread` addresses a task and can override model/thinking on a follow-up. Those declarations do not prove this unit's active model or authorize changing it. No selection mutation or new task was invoked during Gather.

**Observed behavior:** the Coordinator's exact activation reached this Researcher; this unit sent addressed returns, and received exact continuations. `set_thread_title` returned this unit's ID and `RESEARCH · CMTR · B`; a separate `read_thread` of **this unit only** returned the same title. Coordinator monitoring used bounded cursor-based `wait_threads`, never its transcript. The dispatch at `f1ab1a0` records requested `gpt-6-astra` + `high`; its creation arguments and effective backend model/effort were not observed here. The return establishes delivery, not minimum sufficient cost or comparative quality.

**External contract check:** [Codex App Server, model/list](https://learn.chatgpt.com/docs/app-server#list-models-modellist) documents model-specific effort metadata and pagination. That endpoint is a possible native inventory source when actually exposed; this unit used the current task-tool schema, not a fabricated endpoint call. [OpenAI model guidance](https://learn.chatgpt.com/docs/models) distinguishes client/account availability and effort; it also describes `ultra` as subagent orchestration. Thus the spelling of an effort enum alone does not establish compatibility with CMTR's single addressable role boundary. No `ultra` launch was tested.

Local CLI check: `codex --version` returned `codex-cli 0.152.1`; `codex --help` exposes `--model`, config overrides and `app-server`. This is a second installed surface, not proof that CLI defaults equal desktop-task defaults.

### G3 — Antigravity CLI: live roster, with effort encoded in some model IDs

**Verified observations:** `Get-Command agy` resolves `C:\Users\c0rpa\AppData\Local\agy\bin\agy.exe`; `agy --version` returned `1.2.7`. `agy --help` exposes `--model`, `--effort (low|medium|high)`, `--conversation`, `--print`, and stream-JSON input/output. `agy models --help` describes a model listing. `agy models` exited 0 after “Fetching available models...” and returned:

```text
gemini-3.8-flash-high     Gemini 3.8 Flash (High)
gemini-3.8-flash-medium   Gemini 3.8 Flash (Medium)
gemini-3.8-flash-low      Gemini 3.8 Flash (Low)
gemini-3.7-flash-high     Gemini 3.7 Flash (High)
gemini-3.7-flash-medium   Gemini 3.7 Flash (Medium)
gemini-3.7-flash-low      Gemini 3.7 Flash (Low)
gemini-3.6-flash-high     Gemini 3.6 Flash (High)
gemini-3.6-flash-medium   Gemini 3.6 Flash (Medium)
gemini-3.6-flash-low      Gemini 3.6 Flash (Low)
gemini-3.1-pro-high       Gemini 3.1 Pro (High)
gemini-3.1-pro-low        Gemini 3.1 Pro (Low)
claude-sonnet-4-6         Claude Sonnet 4.6 (Thinking)
claude-opus-4-6-thinking  Claude Opus 4.6 (Thinking)
gpt-oss-120b-medium       GPT-OSS 120B (Medium)
```

This is the CLI inventory at observation time. It does not establish remaining quota, successful inference, or every model × effort combination. In particular the output contains no `gemini-3.1-pro-medium`, and the Claude entries expose no selectable effort variants in this listing. Separate **decisions** for capability and effort do not require independent wire fields: a provider may encode the pair in one slug.

**Documented, unexercised:** [headless mode](https://antigravity.google/docs/cli/headless/) describes `--model`, `--effort`, resumable `conversation_id`, stream results and exact-ID continuation. [CLI changelog](https://www.antigravity.google/changelog) records alias/effort-variant resolution in `cli.log`; that can support a later selected-session readback. No headless prompt, conversation creation, conversation resume or log inspection was performed here. An actual long-lived, owner-visible TFW role chain is therefore **unverified**, not proved by the roster or JSON protocol.

### G4 — Antigravity IDE is a different binding

`antigravity --version` returned `1.107.0`, build `15487b3041e65228cae24980a3f796c905ef582c`, `x64`. The installed `antigravity chat --help` exposes `--mode` values `ask`, `edit`, `agent`, `--new-window`, `--reuse-window`, files and profile. It exposes **no model or reasoning flag**. Execution mode is not reasoning effort. No window was opened.

[Official model documentation](https://antigravity.google/docs/models) describes a selector under the conversation prompt and plan-dependent availability; choices persist between messages. [Google's CLI announcement](https://antigravity.google/blog/introducing-google-antigravity-cli) separately describes CLI and Antigravity 2.0, including importing CLI conversations. Neither proves that this installed IDE shares the CLI roster or can natively create/address a TFW role from this Codex task.

**Current boundary:** the IDE's live selector and effective setting are unavailable to this unit; owner-assisted selector operation is documented, not locally piloted. An exact IDE model recommendation must wait for its own current selector. The CLI inventory must not silently substitute for it.

### G5 — Claude Code: current installed controls, account roster still unobserved

`Get-Command claude` resolves `C:\Users\c0rpa\.local\bin\claude.exe`; `claude --version` returned `2.1.278 (Claude Code)`. Read-only help returned:

| Installed surface | Declared control |
|---|---|
| `claude --help` | `--model`, `--effort (low, medium, high, xhigh, max)`, `--session-id`, `--resume`, `--name`, `--worktree` |
| `claude --help` | `--bg` prints a session ID; `attach`, `logs`, `stop`, `agents` address background sessions; a running-session resume may create a copy |
| `claude agents --help` | `--json` for an active-session listing; model/effort defaults for dispatch from the agent view |

No model-inference command, session listing, existing-session content or credentials were read. Native Claude task tools are not exposed in this Codex tool inventory. `claude models` was not invented or attempted. The account-specific selectable model list and effective model/effort are **unavailable from the observations collected here**.

[Claude model configuration](https://code.claude.com/docs/en/model-config) documents `/model`, model aliases, `--model`, model-specific effort limits, `/effort`, header readback and `/status`. Unsupported effort may resolve downward; aliases and organization caps matter. A help enum is consequently not a per-model availability matrix. The same document distinguishes adaptive effort from fixed thinking budgets; the historical `--max-thinking-tokens` claim is not present in installed help. [Agent view](https://code.claude.com/docs/en/agent-view) supplies a candidate visible-session route, but no native Claude-only TFW chain was exercised. Claude Desktop is a further distinct surface and remains uninspected.

### G6 — What the sources do and do not establish for the rule

The frozen HL supplies four quality factors; the native findings add feasibility constraints: model-specific efforts, required context/tools, destination host and role topology. Public [OpenAI guidance](https://learn.chatgpt.com/docs/models#pick-a-reasoning-effort) and [Anthropic's model/effort discussion](https://claude.com/blog/claude-model-and-effort-level-in-claude-code) describe quality/resource tradeoffs; they do not prove a universal threshold for this project. No measured cost frontier or cross-provider equivalence of `high` was found or tested here.

The actual CMTR dispatch shows a concrete requested pair and rationale (disputed architecture, multiple providers, weak oracle). Its product outcome is still in progress. The prior iterations' 95% coverage, 75% savings and causal overthinking assertions remain unsupported; no corresponding measurements are inherited.

**Gather decision:** preserve provider-surface-specific evidence and separate requested, resolved and observed outcome claims. Carry exact effort semantics, lack of a cost ordering and model-specific capability constraints into Extract. No candidate rule or model has yet won the comparison.

## Checkpoint

| Found | Remaining |
|---|---|
| Current Codex task-tool roster and explicit model/thinking fields; real vertical delivery and own-title readback | Creation-argument/effective-setting readback and final independently assessed outcome |
| Antigravity CLI live roster; effort variants and native help | Actual resolved settings, quota and owner-visible role-chain pilot |
| Installed Antigravity IDE chat contract | Its live selector, account roster and exact addressed return route |
| Installed Claude Code parameter/session contract | Current account picker, per-model caps, effective settings and role-chain pilot |
| Distinct quality, feasibility and economy questions | Extract configurations; Challenge counterexamples; independent iteration 4 |

**OODA:** observed installed help, live CLI inventory, current task tools and primary documentation; oriented against A2 and predecessor overclaims; decided to separate capability declarations from exercised behavior; recorded this bounded stage and returned it.

**Sufficiency:**
- [x] External source used: linked provider-owned pages opened on 2026-09-22; four search queries in this stage plus direct page opens. The guessed `/cli/commands/model/` URL failed and supplies no evidence.
- [x] Briefing Gather gap closed: each target surface has an evidence source or an explicit missing observation; unavailable runtime proofs remain visible.
- [x] Dimensions identified without recommending alternatives.

## Material handover at this checkpoint

- **Producer / epoch:** this Researcher, native observations and external documents dated 2026-09-22; authority and repository epochs in the header.
- **Inspected scope:** selected routing/answer, Gather template, native tool declarations, version/help/roster commands above, provider-owned documentation and the previously selected knowledge. No new knowledge-record relation changed the Briefing disposition.
- **Materiality:** CLI and IDE bindings differ; model and effort are logically separate but may share one provider slug; launch parameters do not by themselves prove applied settings or sufficient quality.
- **Uncertainty / owner:** effective settings and native long-lived chain proofs remain with Coordinator-controlled later launches. This unit has no authority to fill the gap by spawning helpers or switching provider.
- **Continuation:** recommend close Gather and authorize Extract in the same unit. Coordinator must decide against this artifact before any Extract work.

---
Stage complete: YES
→ Coordinator decision: pending; stop at Gather checkpoint.
