# Gather — Service-account capability is not desktop or billing proof

> **Mindset:** Explorer; separate the documented boundaries before selecting a route.
> **Mode:** focused, one pass.
> **Parent:** [HL](../../HL-TFW_20260928-201325_SHI.md), frozen authority `f0a8aebbb11686f16081f29b86b96a9d8aa172cf`.
> **Goal:** Bound H1/H2/H4 by official surface, identity, eligibility and cost evidence.
> **Producer / Coordinator:** `codex:thread:local:01a0e909-5023-7ca0-b006-72b639f258c8` → `codex:thread:local:01a0e88a-41cb-75b0-b36f-0e8491af8dc2`.
> **Activation:** iteration-3 dispatch `6396796284138b9f976246db4054c6c24dbdf32e`; Coordinator accepted Briefing `45187c847b7b6fe3f7fa98ba5fe13975836ed84f` and authorized Gather.
> **Evidence date:** official pages fetched 2026-09-28; no actual workspace, credential or host was accessed in this stage.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| Provider identity | Dedicated non-human ChatGPT service account | Named member's Codex personal access token | Platform API project identity/key | Person's interactive ChatGPT login |
| Runtime surface | Trusted `codex exec` automation | Local app-server client/stdio | Remote app-server WebSocket/terminal UI | Desktop through an ordinary supported sign-in |
| Payment evidence | Actual eligible pay-as-you-go workspace/contract | Standard per-user subscription | Actual API usage agreement | Public catalogue only, actual entitlement unknown |
| Human-launch evidence | Explicit declaration with weak assurance | Verified authorized front-end action source | Token creator/operator metadata only | Unknown launcher |

Alternatives are not recommendations and do not imply every cross-combination is supported.

## Findings

### G1 — There is a distinct documented non-human route

The fetched [Service accounts](https://learn.chatgpt.com/docs/enterprise/service-accounts) page describes headless Codex automation using a dedicated workspace identity, available only on pay-as-you-go plans. Workspace owners/admins create accounts; people manage them while signed into their own accounts. Account permissions/plugins are assigned separately rather than inherited from the creator. Service tokens require CLI `0.142.0` or later; the documented headless path uses `CODEX_ACCESS_TOKEN`. On shared/temporary runners the page favors environment-provided credentials over a saved login.

Runs are attributed to the service account. Available governance data may identify token creation or settings changes, which is not a statement that it identifies the human who requested each run. This distinction leaves H2's declaration requirement intact. **Inference:** this is a meaningful H1/H4 alternative to personal-account sharing, not permission to relabel a shared personal login as a service account.

### G2 — Capability matrix: explicit support, derived fit and unknowns

Sources fetched: [Access tokens](https://learn.chatgpt.com/docs/enterprise/access-tokens), [Authentication](https://learn.chatgpt.com/docs/auth), [App server](https://learn.chatgpt.com/docs/app-server), plus G1. No documented command was executed.

| Surface / claim | Source-established status | Boundary |
|---|---|---|
| Service-account token → trusted `codex exec` | Explicit example in Service accounts; minimum CLI version stated | Installed Linux version, actual eligible account and successful operation remain unchecked. |
| Codex access token → trusted app-server automation | Access tokens explicitly documents credential use through the environment or stored CLI login | Applying this generic support to the dedicated identity is a combined-document inference, not a live service-account/app-server test. |
| Local app-server transport | App server lists `stdio` as default and describes its integration interface | Credential acceptance alone does not establish complete TFW role provisioning, addressing, readback or visible-unit behavior. |
| Remote CLI terminal UI → app-server | App server documents a remote terminal UI and WebSocket auth | The same page labels WebSocket experimental/unsupported and says it is not supported for production workloads. This materially qualifies a remote-control candidate. |
| Desktop service-account sign-in | Not established by these pages | Authentication documents desktop ChatGPT browser login and Platform API-key login, not a service-account-token sign-in procedure. Do not infer support merely because a rich client uses app-server internally. |
| Codex cloud or Workspace Agent trigger from a Codex token | No general equivalence | Authentication requires ChatGPT sign-in for cloud; Access tokens distinguishes Codex scope from Workspace Agents scope. Neither proves this service route supports the pilot's desired cloud features. |

The access-token guide specifically separates the credential used by app-server to call OpenAI from client-to-server transport authentication. A remote transport must not reuse the Codex credential as its bearer/capability token. Remote connection security and provider authentication remain separate from TFW authority. The WebSocket warning does not erase documented trusted local token use, but it prevents an unqualified production-remote recommendation.

### G3 — Eligibility and account management are separate from seats and local permissions

[Access tokens](https://learn.chatgpt.com/docs/enterprise/access-tokens) currently names Business and Enterprise workspaces. The broader [Authentication](https://learn.chatgpt.com/docs/auth) automation paragraph names Enterprise. Preserve this difference in specificity: the dedicated token page is the more explicit capability source, but neither proves eligibility for the actual workspace. Service accounts further restrict their own availability to pay-as-you-go plans.

[Roles and workspace permissions](https://learn.chatgpt.com/docs/enterprise/roles-and-workspace-permissions) separates membership/seats, administrative and feature roles, local runtime policy and connected-system access. Seats determine product surfaces; custom roles cannot expand seat/plan eligibility. The token guide also separates token-creation permission from local Codex access. Therefore a token control appearing in a UI, or an operator receiving a management role, is not evidence that every product surface is enabled.

For the later actual selection, retain distinct evidence for workspace/plan eligibility, account creation/operation authority, assigned service permissions, token scope/validity, required local Codex access and connected-system access. Do not request or copy secrets into TFW traces. Current eligibility remains **unknown**; no billing/authentication endpoint or token refresh was attempted.

### G4 — Official price information does not settle service-account cost

The fetched [Pricing](https://learn.chatgpt.com/docs/pricing) page lists standard Business at USD 20 per user/month billed annually with a two-user minimum, or USD 25 monthly. It also distinguishes flexible credit-based usage, notes that credit purchase prices/discounts depend on the plan/agreement, and separates API-key billing. These are public catalogue facts on 2026-09-28, **not a quote for the service-account route or this pilot**.

The inspected service-account page supplies the pay-as-you-go eligibility condition but no explicit service-account seat fee, minimum purchase, included allowance, operator-seat requirement or concrete bill for two humans/two projects. Targeted official-document searches did not resolve those service-specific commercial details. No conclusion that the account is free, replaces two paid seats, shares one flat subscription or saves money follows.

Missing comparison inputs: actual eligible agreement, required human/service seats and commitments, credit purchase price, chosen model/speed and expected input/cache/output/other chargeable usage, concurrent capacity/features, tax and administration. These are decision inputs, not owner questions in this iteration. Actual current Linux subscription/contract remains unknown; the earlier cached Pro label is irrelevant to proving this new route's availability.

### G5 — Consequences to carry into Extract, not implementation instructions

- H1's candidate set expands to a documented non-human workspace route; actual availability and economics remain open.
- H2 remains necessary: provider account, managing person, token creator, run launcher, TFW working unit and mandate are not one subject. A fresh declaration/source must not be inferred from the service identity.
- H4 now has a documented headless basis, a conditional app-server fit, an explicit remote-WebSocket limit and an unestablished desktop path. Compare the minimum trusted headless use with the desired human interaction before choosing a transport.
- E2's existing subject/source separation appears able to describe the provider identity without a new TFW principal/profile. Whether any semantic clarification or Phase B surface/economic decision is needed is Extract work. No renewed 37-path audit is justified by these pages alone.

## Checkpoint

| Found | Remaining |
|---|---|
| Dedicated non-human/PAYG capability is documented | Actual eligible workspace, permissions and contract |
| CLI, app-server, remote transport and desktop claims separated | Concrete route fit and native TFW unit/coordination behavior |
| Service attribution does not identify each human launcher | Exact declaration/evidence mapping in a candidate flow |
| Standard catalogue and credit principles known | Service-specific seats/charges and measured savings |

**Focused decision:** continue with the documented headless route as a distinct candidate; do not treat generic app-server authentication, desktop internals or standard Business pricing as proof of the missing surface/economic claims. One pass completed; three targeted official-document queries, five current documentation page fetches plus the already fetched service-account source. No broad role audit, live credential test or product workload.

**Knowledge handover:** framework/task authority and source epoch unchanged from Briefing. The findings above are technical documentation evidence, not human-only Fact Candidates. Exact recipient is the same Coordinator. Current eligibility, real trial and savings remain unavailable; stage completion closes the bounded documentation gathering, not those acceptance obligations.

- [x] External sources used and fetched, with date and scope stated.
- [x] Briefing Gather gap closed to supported distinctions or explicit unknowns.
- [x] Independent dimensions and at least three alternatives identified.

Stage complete: YES
Gate: WAIT — submit exact Gather path/SHA; recommend Extract.
