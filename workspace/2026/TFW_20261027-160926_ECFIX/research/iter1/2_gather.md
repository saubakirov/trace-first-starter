# Gather — Source discovery, identity and coverage boundaries

> **Mindset:** Explorer. Separate observable facts from assumed compatibility.
> Parent: [HL](../../HL-TFW_20261027-160926_ECFIX.md)
> Goal: Explain actual Claude Code and Antigravity Daily/Full consumption through discoverable, correctly attributed native sources.
> Producer: `codex:thread:local:01a17d31-497c-7c02-9dfe-33555f8a0314`
> Parent Coordinator: `codex:thread:local:01a17d02-d786-7583-ba4f-abb00d60f5e5`
> Authority: frozen HL at `91eeb269e9db44356cb356187363a1f3689e3c06`; unchanged delegated/native-gates/tfw-gates-only spine.
> Continuation: `journal/20261027-165412__gate_answer__dbaf.md @ 66f79e9da5c7565cbe528ae1f6650916bf8b07fe` accepts Briefing and authorizes Gather only.
> Originating proposer: `none`. Observation date: 2026-10-27, timezone `+05:00`.

## Dimensions

No alternative is selected by this stage.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| D1: Surface and format support | Exact observed surface/version recipe | Structurally checked compatible version family | Distinct reader per native surface | Diagnosed unsupported surface |
| D2: Exact own-source binding | Native identity/transcript metadata | Runtime identity plus verified deterministic location | Explicit designated-source receipt | Attributable binding gap |
| D3: Invocation and inherited-work membership | Disjoint response/source identities | Parent-inclusive source with declared children | Proven fork/task boundary and inherited exclusion | Ambiguous attribution refused |
| D4: Numeric coverage | Complete selected bound | Last-good partial measurement plus later failure | Valid native counters through another checked extraction | No numerical measurement available |
| D5: Entry discoverability | Common README owns all recipes | Common contract routes to provider-owned recipe | Runtime-provided locator plus thin shipped guidance | Explicit unsupported-entry diagnosis |

## Findings

### G1 — Version axes must remain separate

Actual read-only commands `claude --version`, `agy --version`, `antigravity --version` returned Claude Code `2.1.289`, CLI `1.2.16`, and VS Code base `1.107.0` / commit `15487b3041e65228cae24980a3f796c905ef582c`. The installed IDE's `resources/app/product.json`, resolved relative to its executable, separately reports `ideVersion: 1.23.2`. These are not interchangeable with the collector's literal accepted label `Antigravity-IDE-2.17.0`. Executable presence is not a completed native IDE probe.

The current `antigravity chat --help` exposes an IDE chat action with ask/edit/agent modes. `agy --help` separately exposes headless JSON, exact `--conversation`, a print timeout and plan/sandbox controls. No IDE model generation was attempted in Gather. The designated CLI experiment below does not prove IDE support.

### G2 — Current routes reach shared guidance; native discovery remains unproven

At source commit `66f79e9da5c7565cbe528ae1f6650916bf8b07fe`, Daily's canonical skill explicitly reads `.tfw/economics/README.md` at start/resume; Plan, Handoff, Review and Research also name it. The Claude and Antigravity Daily entries are thin routers to the canonical Daily skill. Claude's installed `.claude/commands/tfw-economics.md` matches the canonical workflow byte-for-byte: SHA-256 `657b3835ab87e4849d2fd03f662f144c81e344d2f0f48e66565f152c3543b4d6`. Antigravity's economics skill routes to that workflow.

The common README already describes Claude child filenames and composite source IDs, but gives no actionable Antigravity store locator. Neither inspected provider adapter README owns a numeric-source discovery procedure. These are static source facts, not evidence that a fresh native agent follows the chain. No receiver installation defect has yet been reproduced.

### G3 — Claude fresh-session experiment stopped at authentication

Designated experiment identity: `8de76803-77af-4da7-a4c3-9d2b49019a20`. Launch: `claude -p --session-id 8de76803-77af-4da7-a4c3-9d2b49019a20 --output-format json --effort medium --max-budget-usd 2 --permission-mode dontAsk --tools Read,Glob,Grep,Bash --allowedTools Read,Glob,Grep,Bash --strict-mcp-config` with an empty MCP config. The prompt requested at most six read-only calls, normal TFW instruction discovery, exact own-source identity/path evidence, no delegation, no writes and no unrelated conversations or credentials. It supplied no source location or answer. The configured model was not overridden.

Native result: process exit `1`, `is_error: true`, `terminal_reason: api_error`, result `Failed to authenticate: OAuth session expired and could not be refreshed`. The same envelope had `subtype: success`, API duration `0`, empty `modelUsage`, zero token fields and zero spawned agents. No successful model inference or instruction-discovery behavior is evidenced. Authentication was not changed or retried.

Exact assigned-ID filename lookup found the experiment's journal `8de76803-77af-4da7-a4c3-9d2b49019a20.jsonl` beneath the runtime Claude config root's `projects/` directory, inside the directory encoding this experiment's absolute worktree path. Its 18 lines name only that session. Numeric-only inspection found one assistant record: model `<synthetic>`, `isApiErrorMessage: true`, all input/output/cache fields zero. SHA-256: `be531475691132f9dc78c749c2d7640571b9b5eeadba9863e47977fd64119222`.

Direct invocation of the unchanged `claude_rows` on these actual bytes returned one usage row for `<synthetic>` with total zero. This is a verified reader-level acceptance of an error marker; full CLI validation/reporting has not yet been exercised. It is not evidence of a successful zero-cost task. The experiment has an explicit non-success disposition; auth restoration is required for ordinary/child/fork native behavior tests.

### G4 — Antigravity CLI incurred measurable work without answering

Launch: `agy --print` with the same bounded discovery question adapted to Antigravity, `--output-format json --mode plan --sandbox --effort medium --print-timeout 120s`, and a task-temporary `--log-file`. No model override, permission bypass or persistent settings change was used.

The native result assigned conversation `e9cd3d63-d046-4a0b-910a-dda96009db04`, exited `0`, and reported `status: SUCCESS` but an empty response and `denied_actions: [{action: command, display_name: RunCommand}]`. Stderr explicitly explained that a command requiring interactive permission was denied in headless mode. This was not a completed discovery answer. The result's observed cumulative counters were input `23,805`, cache read `0`, output `522`, thinking `419`, total `24,327`; reported invocation duration was `11.8062474` seconds, not native generation time.

The experiment's own runtime log named language-server version `1.2.16` and app-data root `.gemini/antigravity-cli` under the runtime Windows user profile. An exact UUID filename lookup beneath that root resolved `conversations/e9cd3d63-d046-4a0b-910a-dda96009db04.db`. No other conversation contents were inspected. SQLite read-only connection plus in-memory backup found `gen_metadata` columns `[idx, data, size]`, one row at index `0`. Selecting only the existing decoder's numeric fields yielded model `gemini-3.8-flash-n`, fresh `23,805`, cached `0`, candidate output `522`, thinking `419`, content `103`. The numeric result agrees with the native envelope and `522 = 419 + 103`. Physical DB SHA-256 at observation: `e084d6ced9f506f2db4ad56a774a1a28075ee0d49f973c17c4da36568c5624c9`; this physical hash is distinct from the collector's ordered numeric-row hash.

The unmodified `antigravity_rows` called with the truthful label `Antigravity-CLI-1.2.16` refused: `unsupported Antigravity private source version`. No run relabelled CLI bytes as IDE 2.17.0. Thus one observed CLI numeric row matches the old mapping, but a general compatible-family claim, IDE support, timestamp mapping and child/inherited semantics are unproved. The workload's 24,327 observed tokens remain part of experiment membership even though the requested answer was absent.

### G5 — Public sources offer precise binding mechanisms and permission caveats

Official [Claude hooks reference](https://code.claude.com/docs/en/hooks#common-input-fields), checked 2026-10-27, documents native session identity and transcript location, with asynchronous-write lag. Its [SubagentStop section](https://code.claude.com/docs/en/hooks#subagentstop) distinguishes parent transcript location from the child's own transcript and identity. These are candidate binding grounds to verify on the installed version, not a requirement to add permanent hooks. [Subagent documentation](https://code.claude.com/docs/en/sub-agents) describes separate request usage and child transcript persistence.

Official [Antigravity headless documentation](https://antigravity.google/docs/cli/headless/), checked 2026-10-27, documents JSON conversation identity and cumulative usage, and explains soft-denied tools with zero process exit. This supports treating permissions, response outcome and consumption as distinct. It does not document the private SQLite schema or establish compatibility with the existing IDE reader. Public references contain newer surface examples and cannot replace installed observations.

### G6 — Current mixed-history check is a concrete candidate mechanism

Static inspection of `claude_rows` shows `seen_sessions` is populated before the `args.start` check, and the final check requires exactly the chosen session ID. Earlier response IDs also guard against splitting one response across the selected boundary. Relaxing the former without preserving the latter could hide ambiguity. The observed code supports the reported mechanism as a candidate, but auth failure prevented a new native fork reproduction. H2 and H3 remain open; synthetic fixtures cannot fulfill those native proof requirements.

## OODA and knowledge handover

**Observe:** current entry/reader files, installed executable metadata, two explicitly designated native experiment results, exact experiment numeric sources and official docs. **Orient:** separate format/version, availability, binding, permission outcome and numeric measurement. **Decide:** five dimensions remain necessary; close Gather with a concrete authentication dependency and unproved IDE/native-lineage scope. **Act:** return the evidence and stage questions to the same Coordinator; do not implement a reader or change provider permissions.

Material insights are G1–G6, produced by this Researcher at the stated source/observation epoch. Applicable knowledge remains the Briefing's scoped TEQM/current README, evidence-level boundaries and GSC research-dialogue exception; no new qualified knowledge publication is claimed. The own Researcher rollout binding was rechecked: same exact ID/version, start `0`, observed physical prefix `234` lines on resume; final RES capture remains owed. The current title remains `RESEARCH · ECFIX`.

Temporary stdout/log receipts were hashed before cleanup: Claude result `bc30bc7776fa18dc0812d074467ffc57f1c536dea82e0bf84f7fb381b9bce2ad`; AG result `6a4bc3f8d1f7c32115cba6966ca30fa21dccdcfee977321ff15c41ea0ce371e7`; own AG log `a94f0d91af2cff28e14f1821fa9a2c462538938bc2ffd993968461bfd983d7f0`. Their material fields are preserved above, not raw conversations. Original provider-created source files remain unchanged locally for exact-source follow-up; hashes are provenance, not a claim of portable receipt of raw bytes.

## Checkpoint

| Found | Remaining |
|---|---|
| Static Daily/Full route to common guidance; matching Claude economics copy | Fresh native behavior through each entry and isolated receiver |
| Exact designated Claude source with an auth-error synthetic zero row | Authenticated ordinary/child/fork probes and full collector disposition |
| Exact CLI DB with a cross-checked numeric row; truthful-version refusal | Current IDE source and wider decoder/lineage validation |
| Soft-denied AG command still incurs measured consumption | A successful bounded native discovery answer within applicable permissions |

**Sufficiency:**
- [x] External source used.
- [x] Briefing gap closed at Gather level: dimensions and actual environment limits established; no successful fresh-discovery claim.
- [x] Five independent dimensions identified with at least three alternatives each.

**Questions for the Coordinator:**
1. Route the expired Claude OAuth dependency to the owner for normal native authentication; retain successful Claude ordinary/child/fork evidence as acceptance-critical until restored?
2. Proceed to Extract on available evidence and a separate IDE probe, keeping CLI compatibility an observation rather than silently expanding supported scope?
3. Keep the AG command denial as a measured unsuccessful invocation and test a narrower permitted read-only discovery path before considering any permission change?

Stage complete: YES
Recommendation: close Gather; await the Coordinator's explicit Extract decision under research Step 5.
