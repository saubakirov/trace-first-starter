# Challenge — Where the smallest arrangement fails

> **Mindset:** Critic; every elimination needs a reason, every survivor retains its evidence limits.
> **Parent:** [approved HL](../../HL-TFW_20260928-201325_SHI.md), frozen `f0a8aebbb11686f16081f29b86b96a9d8aa172cf`.
> **Goal:** Falsify configurations that conflate permission, launch attribution or project isolation before proposing a minimum viable contract.
> **Producer:** `codex:thread:local:01a0e909-5023-7ca0-b006-72b639f258c8`.
> **Parent/recipient:** `codex:thread:local:01a0e88a-41cb-75b0-b36f-0e8491af8dc2`.
> **Activation:** dispatch `793d1ac`; Coordinator accepted Extract `fd625b2` and authorized Challenge. Native-gates, baseline selection, focused mode, one OODA pass.

## Consistency Check

This is a source-based design challenge, not an executed pilot, access test or independent REVIEW. D1–D5 and C0–C7 refer to [Gather](2_gather.md) and [Extract](3_extract.md).

| Dimension pair | Challenge result |
|---|---|
| D1 entitlement × D2 host/session | An allowed organization arrangement can use a shared host; a shared host cannot cure the personal-account prohibition. Separate seats require separately used accounts even if the OS setup is shared. |
| D1 × D3 declaration carrier | A truthful launch record cannot authorize prohibited provider use. The record must not equate declared human and authenticated provider account. |
| D1 × D4 host mapping | No entitlement follows from a named computer, regardless of where its mapping is stored. |
| D1 × D5 client device | Multiple-device allowance for one individual cannot become several-person account permission. |
| D2 × D3 | A durable per-launch record can coexist with shared or separate sessions, but no declaration repairs shared writable state or credentials. |
| D2 × D4 | An observed session's host can be recorded locally in the task; moving execution requires a new observation, not mutation of the old mapping. |
| D2 × D5 | Session, IP and OS login can supply limited observations; none establishes a person's identity or a verified personal device by itself. |
| D3 × D4 | One event/artifact can preserve both launch and host facts with different sources. A machine-only mapping cannot replace durable task evidence. |
| D3 × D5 | An unknown client device is compatible with an explicit weak-assurance launcher; a missing launcher is not evidence of two declared initiators. |
| D4 × D5 | Execution host and initiating device may differ; collapsing them into one device field loses the approved scenario. |

**Incompatible combinations or claims under the current contract:**

| Dimension A | Alternative | Dimension B | Alternative / claim | Why incompatible |
|---|---|---|---|---|
| D1 | Shared personal/end-user OpenAI account | D2 | Any shared host arrangement claimed permissible | Inspected public terms prohibit multi-person account use; transport is immaterial. |
| D2 | Separate sessions under one unrestricted UID | D3 | Any carrier claimed to prove project access isolation | The carrier records provenance but cannot remove that UID's shared filesystem/app access; DoF 3 remains unaddressed. |
| D3 | No declaration | D5 | Connection/device observation used as inferred person | Violates DoD 1/4 and DoF 1; technical source is not a human declaration. |
| D4 | Machine-local mapping only | D3 | Durable return omits observed host/ref | A recipient without the machine cannot reconstruct the execution host; DoD 1/5 not met. |
| D4 | Unnamed attributes only | D5 | Named initiating device | Client evidence does not supply the selected stable execution-host label. |

**Surviving configurations:** conditional research survivors, not selected or accepted implementations.

| Config | D1 | D2 | D3 | D4 / D5 | Disposition and conditions |
|---|---|---|---|---|---|
| C2 | Organizational distinct users/seats | Separate OS users and project-scoped access | Existing event body where kind/owner fit | Task-local host observation / unknown client permitted | Survives subject to actual entitlement, economic decision, complete launch coverage and real isolation proof. |
| C3 | Organizational distinct users/seats | Separate OS users and project-scoped access | Existing role section + immutable journal/artifact reference | Task-local host observation / declared client | Survives without treating declared device as verified; continuation references must resolve exact epochs. |
| C1/C7 | Separate personal subscriptions | Separate users or bounded VM/container | Existing event body where applicable | Task-local or locally sourced durable observation | Technical fallback only. Multiple subscriptions do not establish the one-subscription target; needs owner decision before selection. |
| C6 | Usage-billed API organization/application | Separate users/project-scoped access | Existing role section + refs | Task-local observation / unknown client | Architectural fallback only; economic model and product/role capabilities require explicit assessment and owner decision. |
| C5 | Organizational distinct users/seats | Bounded VM/container | New launch record | New host record / verified device | Technically possible but not a minimum: no demonstrated gap justifies all added carriers/identity controls. Defer unless C2/C3 fail a concrete case. |

C0 fails permission and provenance. C4 as written fails to establish project/credential isolation; adding actual enforcement could produce a new bounded candidate, but merely changing its session title or `CODEX_HOME` would not prove an OS access boundary.

**Unexpected survivor:** C2 with an explicitly unknown initiating device can still satisfy the frozen contract, which permits unknown client evidence. Strong device attestation is not a prerequisite for honest self-declared human provenance. C3 survives the no-transition continuation edge better than an event-only design, without requiring a new universal event kind.

## Findings

### CH1 — Minimal provenance needs relationships, not more identity objects

[W3C PROV-DM](https://www.w3.org/TR/2013/REC-prov-dm-20130430/), Recommendation 2013-04-30, §§2.1 and 5.3, fetched 2026-09-28, distinguishes entities, activities, attribution and association/delegation. It supports separating who authored an artifact from who participated in a later activity. **Inference for SHI:** one role/launch record with explicit source relationships can preserve these distinctions without one new participant object per run. TFW's existing mandate rules still govern authority; this is not adoption of PROV syntax, ontology, a new runtime or a claim that a provenance statement authenticates its subject.

| Counterexample | Required honest behavior | Carrier consequence |
|---|---|---|
| Anna authors HL; Bek launches it | Preserve Anna as author, Bek as declared launcher, actual owner and immutable mandate independently | Existing HL + one launch declaration/source link; do not rewrite the author or owner. |
| Bek clicks launch before the new task directory exists | At creation, preserve the actual observed declaration and known time; if only capture time is known, say so | The initial created event or initial owning artifact can hold it. No pre-task global registry is logically required. |
| Coordinator launches a Researcher later without human input | Immediate source is that Coordinator; original human launch is inherited lineage, not a fresh assertion that Bek launched the child | Link child dispatch to parent source and human declaration; retain current exact units. |
| Same unit resumes on a new machine | Re-observe host, record changed context and link the earlier launch; do not invent a new human | Append a permitted continuation section or actual existing event, with immutable source epoch. |
| Another human uses a disconnected XRDP session | Earlier declaration cannot describe the new launch automatically | Require a fresh material-launch declaration, or record initiator unknown and stop any dependent identity/authority claim. |
| A declared name conflicts with the governing owner/mandate | A weak declaration is provenance, never grant or owner substitution | Return unresolved authority through the existing Coordinator route. |
| Client IP changes or shared NAT is present | Preserve IP only as observed connection metadata, if relevant; personal device remains unknown without other evidence | Avoid a mandatory device ID and avoid reverse inference. |
| A task record is copied into another project | The old source remains a source; task, unit, host and mandate must be resolved for the new act | No reuse of a copied record as new launch evidence. |
| Host label is reused for a replacement computer | A stable label alone cannot establish continuity of physical machine | New dated mapping and source; preserve old facts. Global UUID or hardware fingerprint is not automatically required. |
| Personal-machine historical binding has no launcher/host | Keep the old attribution readable as it was | No retrospective launch claim, data backfill or per-run principal profile. |
| No valid journal kind fits a no-transition continuation | Do not invent `launch` or fake a transition merely to log context | Existing role-owned artifact section can carry the material observation; its immutable version must remain referenceable. |
| New launcher falsely declares another name | Mark self-declaration's weak assurance; do not claim detection or verified human identity | This limit is accepted by HL; stronger authentication would be a separate design/cost decision. |

The event-only candidate therefore cannot claim universal sufficiency yet. A small shared semantic contract with existing role-artifact fallback survives these cases conceptually. Iteration 2 should perform a precise carrier/path mapping and subtraction review before selection; no template has been changed here.

### CH2 — Isolation must survive the actual access graph

[Docker Engine security](https://docs.docker.com/engine/security/), daemon attack surface and Linux capabilities sections, fetched 2026-09-28, warns that daemon control and host mounts can enable host filesystem modification; default capabilities/mounts do not guarantee complete isolation. This defeats the blanket claim that putting each project in a container proves DoD 4. Rootless/bounded deployments are possible alternatives, not installed/verified facts.

Gather observed a privileged-capable SSH user and two ordinary home permission sets. No cross-user access was attempted and no project ACL/mount map was obtained. Accordingly:

- Distinct OS users are a useful starting boundary, not complete evidence for all project or provider credentials.
- Separate Git worktrees prevent selected file/index collisions, but shared refs/config and same-user filesystem access remain outside that guarantee.
- A project runtime with access to both projects, an unrestricted Docker socket or broad credentials can defeat the intended separation even when result files have correct names.
- The later authorized trial should exercise two disposable project fixtures under the selected real access controls, demonstrate separate result/launch reconstruction and bounded cross-project access, then return real evidence. No permanent test suite, host setup or trial is authorized or performed by this stage.

The trial's threat model must state trusted host administration. If the owner instead requires protection against the host administrator, the shared-host design needs a different decision; the present research does not promise it.

### CH3 — The financial claim remains unproved even after technical success

The common host can be technically usable while the intended subscription arrangement is prohibited or more expensive. The observed cached `pro` label is not a fresh paid entitlement. Existing two OS sessions do not imply two distinct provider identities, and no subscription or second user's account was inspected. Business per-user pricing is a genuine alternative to investigate, not proof of a cheaper equivalent to the requested Pro workload. API billing changes cost and capability assumptions.

No claim of savings follows from the GPU/RAM inventory, parallel app processes or a standard plan label. The necessary later comparison is a permitted actual arrangement at the required features/usage, including seat count, allowances, incremental usage costs and administration. Until then H1 remains open outside the rejected shared-personal-account interpretation. A fallback must return to the Coordinator/owner; no research recommendation silently amends the frozen economic goal.

## Checkpoint

| Found | Remaining |
|---|---|
| All ten dimension pairs checked; C0 fails and C4's asserted isolation fails | No installed survivor or live trial proven |
| C2/C3 survive conditionally; unknown client device is contract-compatible | Actual entitlement/economic choice and exact carrier coverage |
| Event-only recording has a no-transition/Role Lock edge; role artifact fallback avoids inventing events | Iteration-2 minimal file/template map, immutable reference rules and subtraction result |
| Container/worktree/OS labels cannot stand in for actual access controls | Phase-B permitted two-person/two-project trial under a later execution mandate |

**OODA:** observe external provenance and container-security counter-evidence plus prior exact host findings → orient against frozen DoD/DoF and all dimension pairs → decide that conditional C2/C3 merit further research while shared-account and shared-UID proof claims fail → act by returning bounded survivors and unresolved decisions for synthesis.

**Sufficiency:**
- [x] External source used: W3C PROV-DM and official Docker security documentation.
- [x] Briefing Challenge gap closed through explicit counterexamples and failure conditions; no unperformed test is reported as a result.
- [x] Pairwise consistency checked and survivors/failed claims listed.

**Knowledge handover:** producer/recipient and authority above; all local rules retain baseline `7edb91d`, prior stage commits `9191e8b`, `cd5dda3`, `fd625b2`, host observation time 2026-09-28T17:28:04Z. Material finding: minimum provenance appears achievable with existing carriers plus precise relationships, but permission and runtime isolation require separate proof. No registry or device attestation is justified by these edge cases. Current knowledge-use/handover rules were reread; no new contrary local record was applied. Actual account entitlement, economic choice and live acceptance remain the Coordinator/owner's open dependencies.

Stage complete: YES
→ Coordinator decision requested: close Challenge and authorize RES synthesis for iteration 1. Recommend next iteration focus on actual-plan decision input and exact minimal carrier/file coverage. WAIT; no RES written before this gate.
