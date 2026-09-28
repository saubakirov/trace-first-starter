# Gather — Shared host: permission, declarations and isolation

> **Mindset:** Explorer; map independent factors before choosing a configuration.
> **Mode:** focused, one OODA pass.
> **Parent:** [approved HL](../../HL-TFW_20260928-201325_SHI.md), frozen at `f0a8aebbb11686f16081f29b86b96a9d8aa172cf`.
> **Goal:** Establish the decision factors for a permitted shared-host arrangement with separately reconstructable human declarations, projects and authority.
> **Producer:** Researcher `codex:thread:local:01a0e909-5023-7ca0-b006-72b639f258c8`.
> **Recipient/parent:** Coordinator `codex:thread:local:01a0e88a-41cb-75b0-b36f-0e8491af8dc2`.
> **Activation:** dispatch `793d1ac`; exact Coordinator continuation accepted Briefing `9191e8b` and authorized Gather only; native-gates, baseline selection, no peer dialogue.

## Dimensions

Alternatives are a search space, not recommendations or assertions that each is permitted.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| D1: entitlement and billing | One personal account used by several people | Separate personal accounts/subscriptions | One organizational arrangement with distinct end-user accounts/seats | Usage-billed API organization/application |
| D2: host entry and execution boundary | Shared desktop and shared OS user | Separate sessions under one OS user | Separate OS users and private project/app state | Per-project containers/VMs with separately scoped access |
| D3: launch declaration carrier | Existing journal event body linked to governing artifacts | Existing role/launch artifact section referenced by journal | New task-local launch record | No declaration; initiator explicitly unknown |
| D4: stable host mapping | Machine-local host description referenced by observations | Task-local observation in existing artifact/event | Project-local host record | Unnamed observed host attributes only |
| D5: initiating-device evidence | Explicit human declaration, weak assurance | Observed connection metadata, limited assurance | Verified device identity from a separately authorized system | Unknown |

D1/D2 cannot substitute for D3–D5. A personal account reused on one computer remains multi-person account use. Several worktrees do not create distinct provider accounts or OS access boundaries.

## Findings

### G1 — Official terms reject the shared personal-account interpretation

[OpenAI Terms of Use](https://openai.com/policies/terms-of-use/), effective 2026-01-01, Registration and access, prohibit sharing credentials or making an individual's account available to another person. The [Account Sharing Policy](https://help.openai.com/en/articles/10471989-openai-account-sharing-policy) distinguishes an individual's use on multiple devices from multiple people using one account. Both pages were fetched 2026-09-28. No exception for a common physical computer was established.

[OpenAI Services Agreement](https://openai.com/policies/services-agreement/), effective 2026-01-01, §§3.1–3.2 also prohibit shared individual login credentials and restrict an End User Account to one End User. Section 2.2 permits API integration into customer applications for end users, subject to that agreement. This is a different access/billing architecture, not evidence that sharing a Pro account is allowed.

**Bounded conclusion:** D1-A conflicts with the inspected public OpenAI terms. A shared organizational bill with distinct users is a different candidate; no actual organizational purchase, custom contract or paid entitlement was observed. These findings do not prove that every provider forbids every shared subscription arrangement. The actual contractual/customer context and any custom terms remain unverified. H1 is contradicted for the shared personal OpenAI account interpretation and remains open for a permitted arrangement actually available to the pilot.

### G2 — Real host has separate XRDP users; its entitlement evidence is only cached

Read-only SSH used the owner's named endpoint and existing `mikrotik_rsa` key, `BatchMode=yes` and `StrictHostKeyChecking=yes`. Selected observations below were captured at **2026-09-28T17:28:04Z**; no installation, account change, new desktop session, provider request, purchase or host configuration was performed. Routine SSH connection/session records may be produced by the server.

| Observation | Selected result | What it establishes / does not establish |
|---|---|---|
| OS/host | `serv-X870-AORUS-ELITE-WIFI7`; Ubuntu 24.04.4 LTS | Matches the earlier HL observation; `saubakirov-home-linux-01` remains the owner's selected TFW label, not an OS rename or authenticated device identity. |
| XRDP | service active; `xrdp 0.9.24-4`, `xorgxrdp 1:0.9.19-1` | Installed active remote desktop infrastructure, not a successful TFW pilot. |
| Sessions | `c2`: OS user `saubakirov`; `c3`: OS user `university`; both `Service=xrdp-sesman`, `Type=x11`, `State=active`, `Remote=no` | Two distinct active XRDP-managed OS sessions coexist. OS usernames are not declared human identities; `Remote=no` from this API does not identify the initiating device or prove a local physical launch. |
| Processes | ChatGPT and Codex process names under both OS users | Two app process contexts exist; their projects, contents, provider accounts and human operators were not inspected or inferred. |
| Home access metadata | `/home/saubakirov` mode `0750`, UID/GID `1002/1002`; `/home/university` mode `0750`, UID/GID `1008/1009`; observed ACLs only owner/group/other, no named-user entries | There is a basic per-user filesystem boundary. All project ACLs, group membership of other users, mounts and privileged paths were not audited. |
| Own app/config directories | `/home/saubakirov/.codex` and `.tfw` mode `0700`, UID/GID `1002/1002` | Protects against other ordinary UIDs under these observed permissions; does not isolate two processes acting as the same UID or a privileged administrator. |
| Own login capabilities | SSH user belongs to `sudo`, `docker`, `kvm`, `family` and its primary group | The observed launcher is privileged-capable; a private home alone cannot establish isolation against administrators. No privilege escalation was attempted. |
| Cached entitlement label | Own `.codex/auth.json` exists; allowlisted `chatgpt_plan_type` claims from cached ID/access token payloads both read `pro` | A cached Pro label, not cryptographically verified entitlement, fresh billing evidence, a contract, or proof of the current app's selected account. Other claims and token strings were not printed or retained. No other user's credential store was opened. |

**Reproduction boundary:** `hostname`, `/etc/os-release`, `id`, `systemctl is-active xrdp`, `loginctl show-session c2/c3 -p Name -p Type -p Service -p Remote -p State`, `dpkg-query`, `stat`/`getfacl`, and process **names/users only** provide the non-secret observations. Credential inspection used in-memory JSON/JWT parsing in Python and emitted only recognized plan enum values; never run `cat auth.json`, print token payloads, or copy credentials into research evidence. A fresh account/workspace plan view or owner-supplied billing/contract fact is still needed through the Coordinator before actual-plan acceptance.

### G3 — The installed XRDP default can reuse an OS user's session

Observed `/etc/xrdp/sesman.ini`: `Policy=Default`, `MaxSessions=50`, `KillDisconnected=false`, `DisconnectedTimeLimit=0`, `RestrictOutboundClipboard=none`.

The installed package's `sesman.ini(5)` and [upstream v0.9.24 manual](https://raw.githubusercontent.com/neutrinolabs/xrdp/v0.9.24/docs/man/sesman.ini.5.in), fetched 2026-09-28, define Default allocation by user and bit depth. Other policies additionally distinguish display size, IP address or connection. Thus reconnecting with a shared OS login is not a reliable new-person/new-launch boundary. IP or connection separation would still not authenticate a person or name their device.

The configured maximum is a limit, not demonstrated capacity. The current observations prove coexistence of two OS sessions only; they do not prove 50 usable AI sessions. Reconnect behavior and later project separation must be exercised only in the authorized trial. A durable declaration can be designed independently of transport, but no such launch was performed here.

### G4 — Existing TFW carriers already separate some subjects; the launch facts are missing

Sources at checkout baseline `7edb91d6557242191fbe69fb132f35a487f31e3a`: `.tfw/conventions.md` headings Task control files, Declared participants and principals, Which handle a machine acts as, Worktrees for concurrent mutation and Exact-path staging; `.tfw/templates/bindings.yaml`, `.tfw/templates/team/profile.md`, `.tfw/templates/journal/event.md`; `tools/tfw_state.py` status/event key validation.

- `team/` profiles and optional `writer` provide declared principal attribution, not authentication. `on_behalf_of` names the accountable human; `via` names the tool. None currently means the person who initiated a particular launch.
- A machine binding maps one project root to one principal. Its contract explicitly excludes host/device keys and provider data. Reusing that mapping as a per-launch human identity would misrepresent the shared-user case.
- The journal already supports immutable event bodies and artifact references; dispatch bodies preserve exact units and mandate scope. This creates a plausible existing location for additional launch facts without immediately adding a registry.
- Status/event frontmatter uses closed key sets, confirmed by `tfw_state.py`. Arbitrarily adding `host` or `initiator` frontmatter would require a deliberate schema change; an existing event body is a materially different alternative.
- No `launch` event kind exists. A design must distinguish initial owner launch, role dispatch and continuation; it cannot assume every launch is already a valid `dispatch`, or invent a new kind during research.

**Decision carried forward:** compare reuse of existing semantic sections before proposing any new host registry, per-run profile or schema extension. No file/field choice is approved at Gather.

### G5 — Worktree separation and access isolation are distinct

Current TFW requires a separate worktree for a mutating delegated run unless the selected route explicitly serializes one shared checkout, plus one mutation owner and exact-path commits. It explicitly says a worktree is not a lock.

[Git worktree documentation](https://git-scm.com/docs/git-worktree), REFS/CONFIGURATION FILE/DETAILS, fetched 2026-09-28, confirms linked worktrees retain shared refs and normally shared repository configuration while having per-worktree state. **Inference:** this prevents some file/index collisions; it is not a confidentiality or credential boundary between processes with the same OS access. Separate projects and separate roles within one project are different layers to verify. No remote project content or unrelated task history was inspected.

## Checkpoint

| Found | Remaining |
|---|---|
| Public OpenAI terms reject multi-person sharing of one personal/end-user account. | Actual fresh entitlement and contractual context; available compliant economic arrangement. |
| Two distinct XRDP-managed OS sessions and private home metadata observed. | Real people, project roots/access, credential separation, durable unit addresses and end-to-end two-project trial. |
| Default XRDP allocation depends on OS user/bit depth; OS metadata does not establish initiating device. | Actual reconnect/launch declaration behavior; device evidence may remain unknown. |
| Existing journal/artifact bodies can be compared against new carriers; closed schemas and bindings impose real change costs. | Exact minimum carrier and preservation rules, to compare in Extract and challenge later. |

**OODA:** Observe official sources, current carriers and read-only host metadata → orient against H1–H3 → decide that a common account, separate sessions, declarations and permissions cannot be collapsed into one claim → act by handing these dimensions and unresolved acceptance conditions to Extract.

**Sufficiency:**
- [x] External source used: current official OpenAI terms/authentication, version-matched XRDP source and Git documentation.
- [x] Briefing's Gather gap closed: decision dimensions and source-backed limits mapped; acceptance-critical unknowns are named rather than claimed resolved.
- [x] At least three independent dimensions and at least three alternatives per dimension identified.

**Knowledge handover:** producer and exact recipient above; inspected scope/version and observation time stated per finding. Material return: one shared Pro account is not a permitted multi-person OpenAI configuration under inspected public terms; separate OS sessions already exist but do not establish human identity or project isolation; existing TFW carrier reuse deserves comparison. Uncertainty: actual paid state/custom terms and the real pilot remain open. Historical risk F1 is applied as collision evidence; current canonical worktree/staging rules, not F1's old missing-rule claim, govern. No new conflicting relation since the Briefing's scoped ATC/PCUX lookup was encountered in selected inputs.

Stage complete: YES
→ Coordinator decision requested: close Gather and authorize Extract using these conditions. No new owner answer is needed to compare conditional configurations; the exact paid-plan/contract fact remains a named dependency for H1 acceptance. WAIT; no Extract work started.
