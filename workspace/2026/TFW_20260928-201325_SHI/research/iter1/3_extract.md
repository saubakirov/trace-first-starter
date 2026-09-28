# Extract — Configuration space and minimum carriers

> **Mindset:** Analyst; expose combinations before choosing a survivor.
> **Parent:** [approved HL](../../HL-TFW_20260928-201325_SHI.md) at `f0a8aebbb11686f16081f29b86b96a9d8aa172cf`.
> **Goal:** Compare how a shared host can preserve permitted access, declared launch provenance and independently recoverable projects.
> **Producer:** `codex:thread:local:01a0e909-5023-7ca0-b006-72b639f258c8`.
> **Parent/recipient:** `codex:thread:local:01a0e88a-41cb-75b0-b36f-0e8491af8dc2`.
> **Activation:** dispatch `793d1ac`, unchanged native-gates/baseline routing; exact Coordinator continuation accepted Gather `cd5dda3` and authorized Extract. Focused, one OODA pass; no implementation authority.

## Configuration Space

Use [Gather](2_gather.md) D1–D5 alternatives unchanged. The initial Cartesian space has 4 choices in each of 5 dimensions. D1-A is retained as the owner's rejected personal-account baseline for comparison, but its public OpenAI prohibition is already established, not reopened as a deployment option. The following factored representation covers every other combination without listing 768 almost-identical rows. `A–D` means each of the four Gather alternatives independently; it does not mean they are interchangeable or accepted.

| Config family | D1: entitlement and billing | D2: host entry and execution boundary | D3: launch declaration carrier | D4: stable host mapping | D5: initiating-device evidence |
|---|---|---|---|---|---|
| F1 | B: separate personal accounts/subscriptions | A–D | A–D | A–D | A–D |
| F2 | C: organizational arrangement with distinct accounts/seats | A–D | A–D | A–D | A–D |
| F3 | D: usage-billed API organization/application | A–D | A–D | A–D | A–D |

The space includes technically possible but acceptance-incomplete combinations. For example, no declaration (D3-D) honestly records unknown but cannot demonstrate the required two declared initiators. Unnamed host attributes (D4-D) cannot alone satisfy the selected stable host-name claim. These remain controls for Challenge rather than silent exclusions.

Representative combinations expose materially different dependencies; this table ranks none:

| Config | D1: entitlement and billing | D2: host entry and execution boundary | D3: launch declaration carrier | D4: stable host mapping | D5: initiating-device evidence |
|---|---|---|---|---|---|
| C0 baseline | Shared personal account | Shared desktop/OS user | No declaration | Unnamed attributes | Unknown |
| C1 | Separate personal subscriptions | Separate OS users | Existing event body | Task-local observation | Unknown |
| C2 | Organizational distinct users/seats | Separate OS users | Existing event body | Task-local observation | Unknown |
| C3 | Organizational distinct users/seats | Separate OS users | Existing role artifact section + journal ref | Task-local observation | Explicit declaration |
| C4 | Organizational distinct users/seats | Separate sessions/same OS user | Existing event body | Machine-local host description | Connection metadata |
| C5 | Organizational distinct users/seats | Per-project VM/container access | New task-local launch record | Project-local host record | Separately verified device |
| C6 | Usage-billed API organization/application | Separate OS users/project access | Existing artifact section + journal ref | Task-local observation | Unknown |
| C7 | Separate personal subscriptions | Per-project VM/container access | Existing event body | Machine-local host description | Explicit declaration |

**Combination revealed beyond Briefing:** C3 couples one organizational arrangement with independently named users and a task-local host observation plus a declaration in an existing role artifact. Centralized billing does not require a central TFW host registry; explicit client-device uncertainty can coexist with useful human launch declarations. This is a candidate architecture, not a purchased or proven setup.

## Findings

### E1 — One bill, one account and one execution host are different economic choices

Fresh external check on 2026-09-28: [official Codex pricing](https://learn.chatgpt.com/docs/pricing), Business section, describes per-user pricing and a 2+ user standard Business offer; its API section describes usage billing. The [workspace permissions documentation](https://learn.chatgpt.com/docs/enterprise/roles-and-workspace-permissions) separates seat eligibility, administrative roles, local runtime constraints and connected-system permissions. These pages establish product alternatives and control boundaries, not the pilot's purchase or entitlement. No price saving or feature parity is inferred.

| Configuration family | Relationship to the economic objective | Adoption/operating burden | Missing evidence |
|---|---|---|---|
| Shared personal Pro account | Contradicted by the inspected public terms; remote desktop does not change it | Low setup cannot cure the permission issue | No applicable exception observed |
| C1/C7 separate personal subscriptions | Shares compute; does not retain one-subscription saving | Separate accounts, sign-ins and costs; project/access setup | Exact entitlements, cost/usage baseline and owner decision on economic change |
| C2/C3/C4/C5 organizational arrangement | Can centralize billing while retaining individual end users; cannot promise one-seat economics | Seats and workspace administration plus host/access setup | Available plan/order, selected users/features and actual price/usage comparison |
| C6 API arrangement | Shared organizational spending can fund applications; consumption replaces the assumed subscription model | Credential scoping, budgets, integration and capability verification | Actual organization entitlement, permitted application design, projected cost and owner acceptance |

**Decision for the comparison:** do not substitute API billing or multiple subscriptions for the approved target silently. The Coordinator must resolve the intended economic meaning and any frozen-claim change. Further provider-market search is not needed to establish these OpenAI distinctions; another provider becomes relevant only as an actual available pilot candidate.

### E2 — Small carrier design can reuse material events and owning artifacts

Current templates inspected at `7edb91d6557242191fbe69fb132f35a487f31e3a`: journal event, HL, ONB, RF, RES and REVIEW; current activation/routing convention. Role artifacts already name producer unit, parent, activation source and coordination authority. Event bodies already name dispatch edges; no new global run registry is necessary merely to preserve those facts.

| Required fact | Existing semantic carrier | Smallest candidate addition / unresolved edge |
|---|---|---|
| HL author and accountable owner | HL author + task owner | Preserve both; do not replace author with later launcher. |
| Declared initiator and assurance | No dedicated current launch meaning in `writer`/`on_behalf_of` | One explicit declaration with source, time and self-declared assurance in the owning initial event or role artifact section. Never overload the accountable owner. |
| Stable execution host and observed attributes | Evidence/entry context in existing artifact/event | Owner-selected host label plus dated observation/source, or a reference to that record. An OS hostname/IP remains an attribute; label uniqueness is contextual, not globally certified. |
| Initiating device | Existing context can hold a fact or unknown | Carry source and confidence if available; otherwise explicit unknown. No mandatory device fingerprint service. |
| Exact unit, project/task and mandate | Existing producer/dispatch/status lineage | Reference the actual unit and immutable authority already required; retain the link from each material durable act to its launch context. |
| Continued autonomous child work | Dispatch and parent activation lineage | Preserve who declared the human launch upstream without falsely asserting that person directly launched each child. The parent unit remains the immediate dispatch source. |
| Changed launcher or execution host | Later immutable task event or role continuation section | New observation/launch context linked to the prior one; never rewrite history or inherit stale host/initiator by default. |

There is a boundary to solve in Challenge: a human may launch Plan before a task container exists. Initial creation can preserve that declaration when the container is created, but it cannot invent an earlier timestamp or evidence. Likewise, a no-transition continuation may fit an existing owning artifact better than inventing a journal kind. Separate new records remain an alternative only if existing semantic slots cannot preserve these cases clearly.

### E3 — Carrier alternatives have different costs even with identical facts

| Carrier choice | Benefit | Cost/dependency | What must be proved before choosing it |
|---|---|---|---|
| Existing event body | Immutable identity, time and task refs already exist | Semantic rules for initial launch versus dispatch/continuation; producer Role Locks | Every material path has a truthful permitted event kind and owning writer; otherwise use the artifact path. |
| Existing role artifact section referenced by event | Reuses current producer/mandate return; can cover roles that cannot write control files | Multiple templates need consistent semantics; amended role documents need immutable epoch references | Each act resolves exact context without copying a declaration as a new human act. |
| New task-local launch record | Uniform place independent of lifecycle events | New artifact, naming/ownership/read/return rules and extra references | A concrete reconstruction failure that neither existing carrier can resolve. |
| Machine-local host file | Avoids repeated host labeling across projects | Another install/discovery/migration dependency; unavailable when repository moves | Durable task evidence preserves the observed mapping even without access to that local file. |
| Project/global host registry | Central reference | Adds synchronization, namespace and currentness work across projects | Evidence of necessary cross-project lookup absent from the approved two-project scenario. |

**Subtraction candidates:** no per-run `team/` profiles; no device keys mixed into principal bindings; no duplicated unit/mandate registry; no all-click/token log; no mandatory fingerprint or identity provider. Removing these does not remove launch declarations, immutable source links or actual access checks.

### E4 — A stronger desktop boundary does not automatically isolate all projects

C4 still has a shared UID: separate visible sessions can read the same home/app credentials and do not establish per-project access separation. C1–C3 can separate people by OS account, but a person or agent with access to both projects may still cross project boundaries; the later pilot must verify scoped permissions and writable paths, not only home modes. C5/C7 add containers/VMs, but their value depends on actual mounts, credentials and privilege; the noun alone proves nothing. These are design inferences from Gather's observed access metadata and the product control boundaries, not penetration-test results.

For all candidates, separate project repositories/workspaces and each role's mutation worktree are necessary collision controls. Trusted host administrators remain able to affect the machine. A claim of protection against administrators would require a different boundary; it is neither specified nor proved here. The actual pilot should name the allowed operators, project access and administrative trust explicitly.

## Checkpoint

| Found | Remaining |
|---|---|
| Full factored D1–D5 space and eight concrete comparison cases | Challenge the minimum carriers and plausible access arrangements; no configuration selected yet |
| Central billing with separate users differs from sharing one seat/account | Actual available plan/order and owner's economic decision |
| Existing event/artifact paths can carry proposed launch facts | Initial task creation, continuations, moved host and changed initiator need falsification |
| Worktrees, OS identities, app state and project permissions are separate controls | Real later pilot evidence; no mutation or provider use performed |

**OODA:** observe current role carriers and official product/control distinctions → orient against all five Gather dimensions → decide to preserve a factored space and compare existing carriers before new artifacts → act by forwarding C1–C7 and the edge cases to Challenge.

**Sufficiency:**
- [x] External source used: current official pricing and workspace-permission pages; an initial guessed page returned 404 and was replaced by following the authentication page's actual official links.
- [x] Briefing gap closed for Extract: configurations, burden, carrier alternatives and decision-changing dependencies are explicit.
- [x] Configuration space derives from Gather dimensions without presenting conditional feasibility as observed acceptance.

**Knowledge handover:** producer/recipient and immutable epochs above; material result is the separation of organizational billing, individual entitlement, OS isolation and task-local declarations. Existing carriers can potentially cover the required provenance; a new registry has no demonstrated necessity. Uncertainty is preserved for actual plan/contract, starting before task creation, continuation semantics and runtime isolation. Current ATC authority and earlier scoped knowledge relation checks remain unchanged. No HL/TS/code/control file or host was modified.

Stage complete: YES
→ Coordinator decision requested: close Extract and authorize Challenge. No new owner answer is necessary for falsification; economic and live-trial acceptance remain unresolved. WAIT.
