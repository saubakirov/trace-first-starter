# EV ? TFW_20260902-111644_CRATM / Phase C: Authority routing
> **Date**: 2026-09-06
> **Author**: Executor (Codex, acting as saubakirov)
> **Task**: TFW_20260902-111644_CRATM
> **TS**: [TS Phase C](../TS__phase-c__authority_routing.md)
> **Approval / planning**: 1f1173d968e9b74a5e06e3e2070ae604c2844ca5 / 95eb2ab510ed8d89205ed5fe498ccb061c112888
> **Baseline / Candidate**: fb08c120a91aca4c9ceaea859d46dd49c032afd0 / b2a963670e2587cffa6a61d8851f37065f03cda9

## Environment

| Field | Value |
|---|---|
| OS | Windows-11-10.0.26200-SP0 |
| Runtime | 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] |
| Database | N/A |
| Target | clean detached local Git worktree |
| Pipeline | configured pytest and real MkDocs fixture |

R0/R1 source evidence makes no authentication, provider, or production-runtime claim.

## Evidence

| # | AC | Verified | Result | Artifact |
|---|---|---|---|---|
| E1 | AC-1 | owner/root/prefix/CL/refusals | VERIFIED | validator and 38 payloads |
| E2 | AC-2 | proposer/nearest/grant/fallback/signer | VERIFIED | 38 parity; 10 mutants |
| E3 | AC-3 | human exceptions and Role Locks | VERIFIED | source/payloads |
| E4 | AC-4 | consumers/copies/census | VERIFIED | census/parity/tests |
| E5 | AC-5 | scope/invariants/words/caps/build | VERIFIED | counts/suite |
| E6 | AC-6 | ancestry/bootstrap/Candidate/membership | VERIFIED | lineage |
| E-accounting | AC-6 | approval; selector/action/class/reason; valid Phase C attribution; 12 files; 89 + 90 = 179 actual against immutable 12 / 320; binary N/A; below prompts; NUL-safe | VERIFIED | accounting JSON |

Actual underspend is not a rebaseline.

## Complete executable authority validator

Complete resolver, full payload factory, independent oracle, and mutants plus source-tree helpers.

Exact extraction/run command:

```powershell
@'
from pathlib import Path
p=Path('workspace/2026/TFW_20260902-111644_CRATM/phase-c/evidence/EV__phase-c__authority_routing.md')
t=p.read_text(encoding='utf-8')
m='```python authority-validator\n'
program=t.split(m,1)[1].split('\n```',1)[0]
exec(compile(program,'<EV authority-validator>','exec'),{})
'@ | python -
```
```python authority-validator
from __future__ import annotations
import json
from dataclasses import dataclass,field
from pathlib import Path
class SourceContractError(RuntimeError):pass
@dataclass(frozen=True)
class SourceTree:
 root:Path
 overlays:dict[str,str]=field(default_factory=dict)
 @classmethod
 def from_path(cls,root):
  root=Path(root).resolve()
  if not root.is_dir():raise FileNotFoundError(root)
  return cls(root)
 def read(self,path):
  path=path.replace("\\","/")
  if path in self.overlays:return self.overlays[path]
  target=self.root/path
  if not target.is_file():raise SourceContractError(path)
  return target.read_text(encoding="utf-8")
 def with_text(self,path,text):return SourceTree(self.root,{**self.overlays,path.replace("\\","/"):text})
def resolve_heading(text,heading):
 lines=text.splitlines();matches=[]
 for i,line in enumerate(lines):
  x=line.lstrip()
  if x.startswith("#"):
   n=len(x)-len(x.lstrip("#"));title=x[n:].strip()
   if title==heading or title.startswith(heading+" "):matches.append((i,n))
 if len(matches)!=1:raise SourceContractError(heading)
 start,level=matches[0];end=len(lines)
 for i in range(start+1,len(lines)):
  x=lines[i].lstrip()
  if x.startswith("#") and len(x)-len(x.lstrip("#"))<=level:end=i;break
 return "\n".join(lines[start:end])

# CRATM Phase C: the source contract is projected into executable, in-memory authority fixtures.
# Expected outcomes below are independent literals; neither fixture execution nor mutation output
# reads the expected oracle.
@dataclass(frozen=True)
class AuthorityDecision:
    case: str
    decision: str
    ruler: str | None
    refusal_reason: str | None
    proposer: str
    path: tuple[str, ...]
    signer: str | None


def _authority_rule(text: str, number: int) -> str:
    section = resolve_heading(text, "HL Contract")
    prefix = f"{number}. **"
    line = next((line for line in section.splitlines() if line.startswith(prefix)), None)
    if line is None:
        raise SourceContractError(f"HL Contract rule {number} does not resolve")
    return line


def authority_contract(tree: SourceTree) -> dict[str, bool]:
    conventions = tree.read(".tfw/conventions.md")
    rule8 = _authority_rule(conventions, 8)
    rule9 = _authority_rule(conventions, 9)
    rule10 = _authority_rule(conventions, 10)
    review = tree.read(".tfw/workflows/review.md")
    return {
        "owner_from_status": "`status.md.owner` must be a declared human" in rule8,
        "separate_root_authorization": "separate governing record authorizes the root Coordinator" in rule8,
        "coordinator_only": "Only a Coordinator" in rule8,
        "child_only": "new child" in rule8,
        "preserve_proposer": "Preserve the originating proposer through transcription and sessions" in rule8,
        "skip_false": "skip `false` grants" in rule8,
        "stable_handle_equality": "same handle" in rule8,
        "nearest": "nearest remaining immutable `true` principal" in rule8,
        "owner_fallback": "otherwise the owner" in rule8,
        "accountability_forbidden": "`accountable_to`" in rule8 and "never supplies root" in rule8,
        "owner_explicit": "real explicit decision" in rule9,
        "restrict_on_filing": "applies on filing" in rule10,
        "purpose_owner": "both route to the **owner**, never the executor" in review,
        "reviewer_stops": "stops\nwithout resolving authority" in review,
    }


def _authority_nodes(**updates: dict[str, object]) -> dict[str, dict[str, object]]:
    nodes = {
        "root": {"handle": "ruler-root", "type": "agent", "workflow_role": "Coordinator",
                 "grant": True, "grant_changed": False, "accountable_to": "owner-human"},
        "mid": {"handle": "ruler-mid", "type": "agent", "workflow_role": "Coordinator",
                "grant": True, "grant_changed": False, "accountable_to": "owner-human"},
        "worker": {"handle": "probe-worker", "type": "agent", "workflow_role": "Researcher",
                   "grant": False, "grant_changed": False, "accountable_to": "owner-human"},
        "executor": {"handle": "exec-worker", "type": "agent", "workflow_role": "Executor",
                     "grant": False, "grant_changed": False, "accountable_to": "owner-human"},
    }
    for node_id, replacement in updates.items():
        nodes[node_id] = replacement
    return nodes


def _authority_edge(writer: str, destination: str) -> dict[str, str]:
    return {"writer": writer, "destination": destination,
            "scope_ref": "phase/status.md", "role_ref": "authority/delegation-record"}


def _authority_payload(name: str, **updates: object) -> dict[str, object]:
    payload: dict[str, object] = {
        "name": name,
        "status_owner": {"handle": "owner-human", "type": "human"},
        "root_authorizations": [{"owner": "owner-human", "coordinator": "root",
                                 "scope_ref": "phase/status.md",
                                 "authority_ref": "authority/delegation-record"}],
        "nodes": _authority_nodes(),
        "edges": [_authority_edge("root", "mid"), _authority_edge("mid", "worker")],
        "claim_delegated": True,
        "route_kind": "amendment",
        "amendment_type": "EXTEND",
        "proposer_node": "worker",
        "originating_proposer": "probe-worker",
        "transcriber_node": "mid",
        "reserved": False,
        "grant_change_for": None,
        "owner_initiated": False,
        "explicit_owner_decision": False,
        "signer": "ruler-mid",
        "spoof_provenance": {"accountable_to": None, "binding": None, "title": None,
                             "provider": None, "on_behalf_of": None},
    }
    payload.update(updates)
    return payload


def authority_fixture_payloads() -> dict[str, dict[str, object]]:
    no_true = _authority_nodes()
    no_true["root"] = {**no_true["root"], "grant": False}
    no_true["mid"] = {**no_true["mid"], "grant": False}
    false_then_true = _authority_nodes()
    false_then_true["mid"] = {**false_then_true["mid"], "grant": False}
    same_handle = _authority_nodes()
    same_handle["fresh"] = {"handle": "probe-worker", "type": "agent",
                            "workflow_role": "Coordinator", "grant": True,
                            "grant_changed": False, "accountable_to": "owner-human"}
    same_handle["top"] = {"handle": "ruler-top", "type": "agent",
                          "workflow_role": "Coordinator", "grant": True,
                          "grant_changed": False, "accountable_to": "owner-human"}
    orphan_nodes = _authority_nodes()
    orphan_nodes["orphan"] = {**orphan_nodes["root"], "handle": "orphan-ruler"}
    second_root_nodes = _authority_nodes()
    second_root_nodes["root2"] = {**second_root_nodes["root"], "handle": "ruler-second"}
    unknown_grant = _authority_nodes()
    unknown_grant["mid"] = {**unknown_grant["mid"], "grant": None}
    duplicate_grant = _authority_nodes()
    duplicate_grant["mid"] = {**duplicate_grant["mid"], "grant": [True, False]}
    changed_grant = _authority_nodes()
    changed_grant["mid"] = {**changed_grant["mid"], "grant_changed": True}
    foreign_accountability = _authority_nodes()
    foreign_accountability["worker"] = {**foreign_accountability["worker"],
                                        "accountable_to": "other-human"}
    cases = {
        "ordinary_cl": _authority_payload(
            "ordinary_cl", claim_delegated=False, root_authorizations=[], edges=[], signer="owner-human"),
        "root_child": _authority_payload(
            "root_child", edges=[_authority_edge("root", "worker")], signer="ruler-root"),
        "two_level_nearest": _authority_payload("two_level_nearest"),
        "false_then_higher_true": _authority_payload(
            "false_then_higher_true", nodes=false_then_true, signer="ruler-root"),
        "no_true_owner": _authority_payload("no_true_owner", nodes=no_true, signer="owner-human"),
        "proposer_nearest_true": _authority_payload(
            "proposer_nearest_true", proposer_node="mid", originating_proposer="ruler-mid",
            transcriber_node="root", signer="ruler-root"),
        "same_principal_fresh_session": _authority_payload(
            "same_principal_fresh_session", nodes=same_handle,
            root_authorizations=[{"owner": "owner-human", "coordinator": "top",
                                  "scope_ref": "phase/status.md",
                                  "authority_ref": "authority/delegation-record"}],
            edges=[_authority_edge("top", "fresh"), _authority_edge("fresh", "worker")],
            signer="ruler-top"),
        "coordinator_transcribes_child": _authority_payload("coordinator_transcribes_child"),
        "executor_source": _authority_payload(
            "executor_source", edges=[_authority_edge("root", "executor"),
                                       _authority_edge("executor", "worker")], signer="ruler-root"),
        "backward_ancestor": _authority_payload(
            "backward_ancestor", edges=[_authority_edge("root", "mid"),
                                        _authority_edge("mid", "root")]),
        "repeated_child": _authority_payload(
            "repeated_child", edges=[_authority_edge("root", "worker"),
                                     _authority_edge("root", "worker")], signer="ruler-root"),
        "competing_parent": _authority_payload(
            "competing_parent", edges=[_authority_edge("root", "mid"),
                                       _authority_edge("root", "worker"),
                                       _authority_edge("mid", "worker")]),
        "missing_parent": _authority_payload(
            "missing_parent", nodes=orphan_nodes, edges=[_authority_edge("orphan", "worker")]),
        "unknown_writer": _authority_payload(
            "unknown_writer", edges=[_authority_edge("missing", "worker")]),
        "unknown_destination": _authority_payload(
            "unknown_destination", edges=[_authority_edge("root", "missing")]),
        "unassigned_owner": _authority_payload(
            "unassigned_owner", status_owner={"handle": "unassigned", "type": "unassigned"}),
        "nonhuman_owner": _authority_payload(
            "nonhuman_owner", status_owner={"handle": "owner-agent", "type": "agent"}),
        "accountable_without_root": _authority_payload(
            "accountable_without_root", root_authorizations=[], signer="ruler-mid"),
        "binding_as_provenance": _authority_payload(
            "binding_as_provenance", root_authorizations=[],
            spoof_provenance={"accountable_to": None, "binding": "ruler-root", "title": None,
                              "provider": None, "on_behalf_of": None}),
        "title_as_provenance": _authority_payload(
            "title_as_provenance", root_authorizations=[],
            spoof_provenance={"accountable_to": None, "binding": None, "title": "Coordinator",
                              "provider": None, "on_behalf_of": None}),
        "provider_as_provenance": _authority_payload(
            "provider_as_provenance", root_authorizations=[],
            spoof_provenance={"accountable_to": None, "binding": None, "title": None,
                              "provider": "codex", "on_behalf_of": None}),
        "accountability_as_provenance": _authority_payload(
            "accountability_as_provenance", root_authorizations=[], nodes=foreign_accountability,
            spoof_provenance={"accountable_to": "owner-human", "binding": None, "title": None,
                              "provider": None, "on_behalf_of": None}),
        "unknown_grant": _authority_payload("unknown_grant", nodes=unknown_grant),
        "duplicate_grant": _authority_payload("duplicate_grant", nodes=duplicate_grant),
        "changed_grant": _authority_payload("changed_grant", nodes=changed_grant),
        "mismatched_signer": _authority_payload("mismatched_signer", signer="ruler-root"),
        "two_roots": _authority_payload(
            "two_roots", nodes=second_root_nodes,
            root_authorizations=[{"owner": "owner-human", "coordinator": "root",
                                  "scope_ref": "phase/status.md",
                                  "authority_ref": "authority/delegation-record"},
                                 {"owner": "owner-human", "coordinator": "root2",
                                  "scope_ref": "phase/status.md",
                                  "authority_ref": "authority/delegation-record"}]),
        "owner_reserved": _authority_payload("owner_reserved", reserved=True, signer="owner-human"),
        "agent_self_grant": _authority_payload(
            "agent_self_grant", grant_change_for="probe-worker", signer="owner-human"),
        "restrict": _authority_payload(
            "restrict", claim_delegated=False, root_authorizations=[], edges=[],
            amendment_type="RESTRICT", signer=None),
        "owner_initiated": _authority_payload(
            "owner_initiated", claim_delegated=False, root_authorizations=[], edges=[],
            proposer_node=None, originating_proposer="owner-human", transcriber_node=None,
            owner_initiated=True, explicit_owner_decision=True, signer="owner-human"),
        "false_owner_initiated": _authority_payload(
            "false_owner_initiated", owner_initiated=True, explicit_owner_decision=False,
            signer="owner-human",
            spoof_provenance={"accountable_to": "owner-human", "binding": "owner-human",
                              "title": "Owner", "provider": None,
                              "on_behalf_of": "owner-human"}),
        "purpose_not_fit": _authority_payload(
            "purpose_not_fit", claim_delegated=False, root_authorizations=[], edges=[],
            route_kind="purpose_not_fit", signer="owner-human"),
        "contract_defect": _authority_payload(
            "contract_defect", claim_delegated=False, root_authorizations=[], edges=[],
            route_kind="contract_defect", signer="owner-human"),
        "review_reject": _authority_payload(
            "review_reject", claim_delegated=False, root_authorizations=[], edges=[],
            route_kind="review_reject", signer="owner-human"),
        "budget_return": _authority_payload(
            "budget_return", claim_delegated=False, root_authorizations=[], edges=[],
            route_kind="budget", signer="owner-human"),
        "unavailable_participant": _authority_payload(
            "unavailable_participant", claim_delegated=False, root_authorizations=[], edges=[],
            route_kind="unavailable", signer="owner-human"),
        "fallback_probe": _authority_payload(
            "fallback_probe", nodes=foreign_accountability | {
                "root": {**foreign_accountability["root"], "grant": False},
                "mid": {**foreign_accountability["mid"], "grant": False}}, signer="owner-human"),
    }
    return cases


def _authority_refusal(payload: dict[str, object], reason: str,
                       proposer: str | None = None) -> AuthorityDecision:
    return AuthorityDecision(str(payload["name"]), "REFUSE", None, reason,
                             proposer or str(payload["originating_proposer"]), (),
                             str(payload["signer"]) if payload["signer"] is not None else None)


def _authority_route(payload: dict[str, object], ruler: str, proposer: str,
                     path: tuple[str, ...], decision: str = "ROUTE") -> AuthorityDecision:
    signer = str(payload["signer"]) if payload["signer"] is not None else None
    if signer != ruler:
        return _authority_refusal(payload, "mismatched-verdict-signer", proposer)
    return AuthorityDecision(str(payload["name"]), decision, ruler, None, proposer, path, signer)


def resolve_amendment_authority(tree: SourceTree, payload: dict[str, object]) -> AuthorityDecision:
    contract = authority_contract(tree)
    nodes = payload["nodes"]
    assert isinstance(nodes, dict)
    status_owner = payload["status_owner"]
    assert isinstance(status_owner, dict)
    owner = str(status_owner.get("handle"))
    if not contract["owner_from_status"]:
        proposer_node = payload.get("proposer_node")
        owner = str(nodes.get(proposer_node, {}).get("accountable_to", owner))
    if status_owner.get("type") != "human" or owner == "unassigned":
        return _authority_refusal(payload, "governing-owner-is-not-a-declared-human")

    proposer = str(payload["originating_proposer"])
    if not contract["preserve_proposer"] and payload.get("transcriber_node") in nodes:
        proposer = str(nodes[str(payload["transcriber_node"])]["handle"])

    kind = str(payload["route_kind"])
    if kind in {"purpose_not_fit", "contract_defect", "review_reject"}:
        if contract["purpose_owner"]:
            return _authority_route(payload, owner, proposer, (owner,), "HUMAN")
        return _authority_route(payload, "ruler-mid", proposer, ("ruler-mid",))
    if kind in {"budget", "unavailable"}:
        return _authority_route(payload, owner, proposer, (owner,), "HUMAN")
    if payload["amendment_type"] == "RESTRICT" and contract["restrict_on_filing"]:
        return AuthorityDecision(str(payload["name"]), "APPLY_ON_FILING", None, None,
                                 proposer, (), None)
    if payload["owner_initiated"]:
        explicit = bool(payload["explicit_owner_decision"])
        if not contract["owner_explicit"]:
            explicit = payload["spoof_provenance"].get("on_behalf_of") == owner
            if explicit:
                proposer = owner
        if explicit and proposer == owner:
            return _authority_route(payload, owner, proposer, (owner,), "DIRECT_OWNER_ACT")
    if not payload["claim_delegated"]:
        return _authority_route(payload, owner, proposer, (owner,))

    authorizations = payload["root_authorizations"]
    assert isinstance(authorizations, list)
    if not authorizations and not contract["accountability_forbidden"]:
        roots = [node_id for node_id, node in nodes.items()
                 if node.get("workflow_role") == "Coordinator"
                 and node.get("accountable_to") == owner]
        if roots:
            authorizations = [{"owner": owner, "coordinator": roots[0],
                               "scope_ref": "derived-accountability",
                               "authority_ref": "derived-accountability"}]
    if contract["separate_root_authorization"] and len(authorizations) != 1:
        return _authority_refusal(payload, "missing-or-competing-root-authorization", proposer)
    if len(authorizations) != 1:
        return _authority_refusal(payload, "unresolved-root", proposer)
    authorization = authorizations[0]
    root = str(authorization.get("coordinator"))
    if authorization.get("owner") != owner or root not in nodes:
        return _authority_refusal(payload, "invalid-root-authorization", proposer)
    if not authorization.get("scope_ref") or not authorization.get("authority_ref"):
        return _authority_refusal(payload, "missing-root-provenance", proposer)
    if nodes[root].get("workflow_role") != "Coordinator":
        return _authority_refusal(payload, "root-is-not-coordinator", proposer)

    reached, parents = {root}, {}
    for edge in payload["edges"]:
        writer, destination = str(edge.get("writer")), str(edge.get("destination"))
        if writer not in nodes:
            return _authority_refusal(payload, "unknown-writer", proposer)
        if destination not in nodes:
            return _authority_refusal(payload, "unknown-destination", proposer)
        if writer not in reached:
            return _authority_refusal(payload, "missing-parent-prefix", proposer)
        if contract["coordinator_only"] and nodes[writer].get("workflow_role") != "Coordinator":
            return _authority_refusal(payload, "edge-source-is-not-coordinator", proposer)
        if not edge.get("scope_ref") or not edge.get("role_ref"):
            return _authority_refusal(payload, "missing-edge-provenance", proposer)
        if destination in reached and contract["child_only"]:
            cursor = writer
            ancestors = {writer}
            while cursor in parents:
                cursor = parents[cursor]
                ancestors.add(cursor)
            if destination in ancestors:
                reason = "backward-ancestor-edge"
            elif destination in parents and parents[destination] != writer:
                reason = "competing-parent"
            else:
                reason = "repeated-child"
            return _authority_refusal(payload, reason, proposer)
        parents[destination] = writer
        reached.add(destination)

    proposer_node = payload.get("proposer_node")
    if proposer_node not in reached:
        return _authority_refusal(payload, "proposer-outside-resolved-prefix", proposer)
    if payload["reserved"] or payload["grant_change_for"] == proposer:
        return _authority_route(payload, owner, proposer, (str(proposer_node), owner), "HUMAN")

    path_nodes, cursor = [], str(proposer_node)
    while cursor in parents:
        cursor = parents[cursor]
        path_nodes.append(cursor)
    if cursor != root:
        return _authority_refusal(payload, "prefix-does-not-terminate-at-root", proposer)
    eligible = []
    for node_id in path_nodes:
        node = nodes[node_id]
        grant = node.get("grant")
        if not isinstance(grant, bool) or node.get("grant_changed"):
            return _authority_refusal(payload, "unknown-duplicate-or-changed-grant", proposer)
        same_principal = (str(node.get("handle")) == proposer if contract["stable_handle_equality"]
                          else node_id == payload.get("proposer_node"))
        granted = grant if contract["skip_false"] else not grant
        if granted and not same_principal:
            eligible.append(str(node.get("handle")))
    if eligible:
        ruler = eligible[0] if contract["nearest"] else eligible[-1]
    elif contract["owner_fallback"]:
        ruler = owner
    else:
        ruler = str(nodes[str(proposer_node)].get("accountable_to"))
    return _authority_route(payload, ruler, proposer,
                            tuple(str(nodes[node]["handle"]) for node in path_nodes) + (owner,))


AUTHORITY_EXPECTED = {
    "ordinary_cl": ("ROUTE", "owner-human", None),
    "root_child": ("ROUTE", "ruler-root", None),
    "two_level_nearest": ("ROUTE", "ruler-mid", None),
    "false_then_higher_true": ("ROUTE", "ruler-root", None),
    "no_true_owner": ("ROUTE", "owner-human", None),
    "proposer_nearest_true": ("ROUTE", "ruler-root", None),
    "same_principal_fresh_session": ("ROUTE", "ruler-top", None),
    "coordinator_transcribes_child": ("ROUTE", "ruler-mid", None),
    "executor_source": ("REFUSE", None, "edge-source-is-not-coordinator"),
    "backward_ancestor": ("REFUSE", None, "backward-ancestor-edge"),
    "repeated_child": ("REFUSE", None, "repeated-child"),
    "competing_parent": ("REFUSE", None, "competing-parent"),
    "missing_parent": ("REFUSE", None, "missing-parent-prefix"),
    "unknown_writer": ("REFUSE", None, "unknown-writer"),
    "unknown_destination": ("REFUSE", None, "unknown-destination"),
    "unassigned_owner": ("REFUSE", None, "governing-owner-is-not-a-declared-human"),
    "nonhuman_owner": ("REFUSE", None, "governing-owner-is-not-a-declared-human"),
    "accountable_without_root": ("REFUSE", None, "missing-or-competing-root-authorization"),
    "binding_as_provenance": ("REFUSE", None, "missing-or-competing-root-authorization"),
    "title_as_provenance": ("REFUSE", None, "missing-or-competing-root-authorization"),
    "provider_as_provenance": ("REFUSE", None, "missing-or-competing-root-authorization"),
    "accountability_as_provenance": ("REFUSE", None, "missing-or-competing-root-authorization"),
    "unknown_grant": ("REFUSE", None, "unknown-duplicate-or-changed-grant"),
    "duplicate_grant": ("REFUSE", None, "unknown-duplicate-or-changed-grant"),
    "changed_grant": ("REFUSE", None, "unknown-duplicate-or-changed-grant"),
    "mismatched_signer": ("REFUSE", None, "mismatched-verdict-signer"),
    "two_roots": ("REFUSE", None, "missing-or-competing-root-authorization"),
    "owner_reserved": ("HUMAN", "owner-human", None),
    "agent_self_grant": ("HUMAN", "owner-human", None),
    "restrict": ("APPLY_ON_FILING", None, None),
    "owner_initiated": ("DIRECT_OWNER_ACT", "owner-human", None),
    "false_owner_initiated": ("REFUSE", None, "mismatched-verdict-signer"),
    "purpose_not_fit": ("HUMAN", "owner-human", None),
    "contract_defect": ("HUMAN", "owner-human", None),
    "review_reject": ("HUMAN", "owner-human", None),
    "budget_return": ("HUMAN", "owner-human", None),
    "unavailable_participant": ("HUMAN", "owner-human", None),
    "fallback_probe": ("ROUTE", "owner-human", None),
}


def authority_fixture_results(tree: SourceTree) -> dict[str, AuthorityDecision]:
    return {name: resolve_amendment_authority(tree, payload)
            for name, payload in authority_fixture_payloads().items()}


def authority_mutant_results(tree: SourceTree) -> list[dict[str, object]]:
    mutations = (
        ("proposer-preservation", ".tfw/conventions.md",
         "Preserve the originating proposer through transcription and sessions",
         "Replace the originating proposer with the transcriber session", "two_level_nearest"),
        ("nearest-order", ".tfw/conventions.md", "nearest remaining immutable `true` principal",
         "highest remaining immutable `true` principal", "two_level_nearest"),
        ("grant-polarity", ".tfw/conventions.md", "skip `false` grants", "skip `true` grants",
         "false_then_higher_true"),
        ("stable-handle", ".tfw/conventions.md", "same handle", "same session",
         "same_principal_fresh_session"),
        ("status-owner-fallback", ".tfw/conventions.md", "otherwise the owner",
         "otherwise `accountable_to`", "fallback_probe"),
        ("accountability-provenance", ".tfw/conventions.md", "never supplies root",
         "may supply root", "accountable_without_root"),
        ("coordinator-only", ".tfw/conventions.md", "Only a Coordinator", "Any role",
         "executor_source"),
        ("owner-explicit-act", ".tfw/conventions.md", "real explicit decision",
         "`on_behalf_of` decision", "false_owner_initiated"),
        ("restrict-filing", ".tfw/conventions.md", "applies on filing", "waits for a ruler",
         "restrict"),
        ("purpose-owner", ".tfw/workflows/review.md",
         "both route to the **owner**, never the executor",
         "both route to the resolved ruler", "purpose_not_fit"),
    )
    results = []
    for family, path, old, new, case in mutations:
        source = tree.read(path)
        if old not in source:
            raise SourceContractError(f"{family}: mutation source does not resolve")
        normal = resolve_amendment_authority(tree, authority_fixture_payloads()[case])
        produced = resolve_amendment_authority(
            tree.with_text(path, source.replace(old, new, 1)), authority_fixture_payloads()[case])
        expected = AUTHORITY_EXPECTED[case]
        independent_rejects = (produced.decision, produced.ruler, produced.refusal_reason) != expected
        results.append({"family": family, "case": case, "normal": normal.__dict__,
                        "produced": produced.__dict__, "projection_changed": produced != normal,
                        "independent_expected_rejects": independent_rejects})
    return results

tree=SourceTree.from_path(Path("."))
payloads=authority_fixture_payloads()
actual={k:v.__dict__ for k,v in authority_fixture_results(tree).items()}
expected={k:{"decision":v[0],"ruler":v[1],"refusal_reason":v[2]} for k,v in AUTHORITY_EXPECTED.items()}
mutants=authority_mutant_results(tree)
assert set(payloads)==set(expected)==set(actual)
assert all((v["decision"],v["ruler"],v["refusal_reason"])==AUTHORITY_EXPECTED[k] for k,v in actual.items())
assert all(v["projection_changed"] and v["independent_expected_rejects"] for v in mutants)
print(json.dumps({"candidate":"b2a963670e2587cffa6a61d8851f37065f03cda9","contract":authority_contract(tree),"payloads":payloads,"expected":expected,"actual":actual,"mutants":mutants},indent=2,sort_keys=True))
print(f"SUMMARY fixtures={len(payloads)} parity={len(actual)} mutants={len(mutants)} output_changing_rejected={sum(v['projection_changed'] and v['independent_expected_rejects'] for v in mutants)}")
```
### Raw validator output

Exit 0. Complete UTF-8 output SHA-256: 1a0445cb508a3634b462e083731e98eb661819c16980aa28ba2375268dda21f6

```json
{
  "actual": {
    "accountability_as_provenance": {
      "case": "accountability_as_provenance",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "missing-or-competing-root-authorization",
      "ruler": null,
      "signer": "ruler-mid"
    },
    "accountable_without_root": {
      "case": "accountable_without_root",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "missing-or-competing-root-authorization",
      "ruler": null,
      "signer": "ruler-mid"
    },
    "agent_self_grant": {
      "case": "agent_self_grant",
      "decision": "HUMAN",
      "path": [
        "worker",
        "owner-human"
      ],
      "proposer": "probe-worker",
      "refusal_reason": null,
      "ruler": "owner-human",
      "signer": "owner-human"
    },
    "backward_ancestor": {
      "case": "backward_ancestor",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "backward-ancestor-edge",
      "ruler": null,
      "signer": "ruler-mid"
    },
    "binding_as_provenance": {
      "case": "binding_as_provenance",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "missing-or-competing-root-authorization",
      "ruler": null,
      "signer": "ruler-mid"
    },
    "budget_return": {
      "case": "budget_return",
      "decision": "HUMAN",
      "path": [
        "owner-human"
      ],
      "proposer": "probe-worker",
      "refusal_reason": null,
      "ruler": "owner-human",
      "signer": "owner-human"
    },
    "changed_grant": {
      "case": "changed_grant",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "unknown-duplicate-or-changed-grant",
      "ruler": null,
      "signer": "ruler-mid"
    },
    "competing_parent": {
      "case": "competing_parent",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "competing-parent",
      "ruler": null,
      "signer": "ruler-mid"
    },
    "contract_defect": {
      "case": "contract_defect",
      "decision": "HUMAN",
      "path": [
        "owner-human"
      ],
      "proposer": "probe-worker",
      "refusal_reason": null,
      "ruler": "owner-human",
      "signer": "owner-human"
    },
    "coordinator_transcribes_child": {
      "case": "coordinator_transcribes_child",
      "decision": "ROUTE",
      "path": [
        "ruler-mid",
        "ruler-root",
        "owner-human"
      ],
      "proposer": "probe-worker",
      "refusal_reason": null,
      "ruler": "ruler-mid",
      "signer": "ruler-mid"
    },
    "duplicate_grant": {
      "case": "duplicate_grant",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "unknown-duplicate-or-changed-grant",
      "ruler": null,
      "signer": "ruler-mid"
    },
    "executor_source": {
      "case": "executor_source",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "edge-source-is-not-coordinator",
      "ruler": null,
      "signer": "ruler-root"
    },
    "fallback_probe": {
      "case": "fallback_probe",
      "decision": "ROUTE",
      "path": [
        "ruler-mid",
        "ruler-root",
        "owner-human"
      ],
      "proposer": "probe-worker",
      "refusal_reason": null,
      "ruler": "owner-human",
      "signer": "owner-human"
    },
    "false_owner_initiated": {
      "case": "false_owner_initiated",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "mismatched-verdict-signer",
      "ruler": null,
      "signer": "owner-human"
    },
    "false_then_higher_true": {
      "case": "false_then_higher_true",
      "decision": "ROUTE",
      "path": [
        "ruler-mid",
        "ruler-root",
        "owner-human"
      ],
      "proposer": "probe-worker",
      "refusal_reason": null,
      "ruler": "ruler-root",
      "signer": "ruler-root"
    },
    "mismatched_signer": {
      "case": "mismatched_signer",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "mismatched-verdict-signer",
      "ruler": null,
      "signer": "ruler-root"
    },
    "missing_parent": {
      "case": "missing_parent",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "missing-parent-prefix",
      "ruler": null,
      "signer": "ruler-mid"
    },
    "no_true_owner": {
      "case": "no_true_owner",
      "decision": "ROUTE",
      "path": [
        "ruler-mid",
        "ruler-root",
        "owner-human"
      ],
      "proposer": "probe-worker",
      "refusal_reason": null,
      "ruler": "owner-human",
      "signer": "owner-human"
    },
    "nonhuman_owner": {
      "case": "nonhuman_owner",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "governing-owner-is-not-a-declared-human",
      "ruler": null,
      "signer": "ruler-mid"
    },
    "ordinary_cl": {
      "case": "ordinary_cl",
      "decision": "ROUTE",
      "path": [
        "owner-human"
      ],
      "proposer": "probe-worker",
      "refusal_reason": null,
      "ruler": "owner-human",
      "signer": "owner-human"
    },
    "owner_initiated": {
      "case": "owner_initiated",
      "decision": "DIRECT_OWNER_ACT",
      "path": [
        "owner-human"
      ],
      "proposer": "owner-human",
      "refusal_reason": null,
      "ruler": "owner-human",
      "signer": "owner-human"
    },
    "owner_reserved": {
      "case": "owner_reserved",
      "decision": "HUMAN",
      "path": [
        "worker",
        "owner-human"
      ],
      "proposer": "probe-worker",
      "refusal_reason": null,
      "ruler": "owner-human",
      "signer": "owner-human"
    },
    "proposer_nearest_true": {
      "case": "proposer_nearest_true",
      "decision": "ROUTE",
      "path": [
        "ruler-root",
        "owner-human"
      ],
      "proposer": "ruler-mid",
      "refusal_reason": null,
      "ruler": "ruler-root",
      "signer": "ruler-root"
    },
    "provider_as_provenance": {
      "case": "provider_as_provenance",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "missing-or-competing-root-authorization",
      "ruler": null,
      "signer": "ruler-mid"
    },
    "purpose_not_fit": {
      "case": "purpose_not_fit",
      "decision": "HUMAN",
      "path": [
        "owner-human"
      ],
      "proposer": "probe-worker",
      "refusal_reason": null,
      "ruler": "owner-human",
      "signer": "owner-human"
    },
    "repeated_child": {
      "case": "repeated_child",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "repeated-child",
      "ruler": null,
      "signer": "ruler-root"
    },
    "restrict": {
      "case": "restrict",
      "decision": "APPLY_ON_FILING",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": null,
      "ruler": null,
      "signer": null
    },
    "review_reject": {
      "case": "review_reject",
      "decision": "HUMAN",
      "path": [
        "owner-human"
      ],
      "proposer": "probe-worker",
      "refusal_reason": null,
      "ruler": "owner-human",
      "signer": "owner-human"
    },
    "root_child": {
      "case": "root_child",
      "decision": "ROUTE",
      "path": [
        "ruler-root",
        "owner-human"
      ],
      "proposer": "probe-worker",
      "refusal_reason": null,
      "ruler": "ruler-root",
      "signer": "ruler-root"
    },
    "same_principal_fresh_session": {
      "case": "same_principal_fresh_session",
      "decision": "ROUTE",
      "path": [
        "probe-worker",
        "ruler-top",
        "owner-human"
      ],
      "proposer": "probe-worker",
      "refusal_reason": null,
      "ruler": "ruler-top",
      "signer": "ruler-top"
    },
    "title_as_provenance": {
      "case": "title_as_provenance",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "missing-or-competing-root-authorization",
      "ruler": null,
      "signer": "ruler-mid"
    },
    "two_level_nearest": {
      "case": "two_level_nearest",
      "decision": "ROUTE",
      "path": [
        "ruler-mid",
        "ruler-root",
        "owner-human"
      ],
      "proposer": "probe-worker",
      "refusal_reason": null,
      "ruler": "ruler-mid",
      "signer": "ruler-mid"
    },
    "two_roots": {
      "case": "two_roots",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "missing-or-competing-root-authorization",
      "ruler": null,
      "signer": "ruler-mid"
    },
    "unassigned_owner": {
      "case": "unassigned_owner",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "governing-owner-is-not-a-declared-human",
      "ruler": null,
      "signer": "ruler-mid"
    },
    "unavailable_participant": {
      "case": "unavailable_participant",
      "decision": "HUMAN",
      "path": [
        "owner-human"
      ],
      "proposer": "probe-worker",
      "refusal_reason": null,
      "ruler": "owner-human",
      "signer": "owner-human"
    },
    "unknown_destination": {
      "case": "unknown_destination",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "unknown-destination",
      "ruler": null,
      "signer": "ruler-mid"
    },
    "unknown_grant": {
      "case": "unknown_grant",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "unknown-duplicate-or-changed-grant",
      "ruler": null,
      "signer": "ruler-mid"
    },
    "unknown_writer": {
      "case": "unknown_writer",
      "decision": "REFUSE",
      "path": [],
      "proposer": "probe-worker",
      "refusal_reason": "unknown-writer",
      "ruler": null,
      "signer": "ruler-mid"
    }
  },
  "candidate": "b2a963670e2587cffa6a61d8851f37065f03cda9",
  "contract": {
    "accountability_forbidden": true,
    "child_only": true,
    "coordinator_only": true,
    "nearest": true,
    "owner_explicit": true,
    "owner_fallback": true,
    "owner_from_status": true,
    "preserve_proposer": true,
    "purpose_owner": true,
    "restrict_on_filing": true,
    "reviewer_stops": true,
    "separate_root_authorization": true,
    "skip_false": true,
    "stable_handle_equality": true
  },
  "expected": {
    "accountability_as_provenance": {
      "decision": "REFUSE",
      "refusal_reason": "missing-or-competing-root-authorization",
      "ruler": null
    },
    "accountable_without_root": {
      "decision": "REFUSE",
      "refusal_reason": "missing-or-competing-root-authorization",
      "ruler": null
    },
    "agent_self_grant": {
      "decision": "HUMAN",
      "refusal_reason": null,
      "ruler": "owner-human"
    },
    "backward_ancestor": {
      "decision": "REFUSE",
      "refusal_reason": "backward-ancestor-edge",
      "ruler": null
    },
    "binding_as_provenance": {
      "decision": "REFUSE",
      "refusal_reason": "missing-or-competing-root-authorization",
      "ruler": null
    },
    "budget_return": {
      "decision": "HUMAN",
      "refusal_reason": null,
      "ruler": "owner-human"
    },
    "changed_grant": {
      "decision": "REFUSE",
      "refusal_reason": "unknown-duplicate-or-changed-grant",
      "ruler": null
    },
    "competing_parent": {
      "decision": "REFUSE",
      "refusal_reason": "competing-parent",
      "ruler": null
    },
    "contract_defect": {
      "decision": "HUMAN",
      "refusal_reason": null,
      "ruler": "owner-human"
    },
    "coordinator_transcribes_child": {
      "decision": "ROUTE",
      "refusal_reason": null,
      "ruler": "ruler-mid"
    },
    "duplicate_grant": {
      "decision": "REFUSE",
      "refusal_reason": "unknown-duplicate-or-changed-grant",
      "ruler": null
    },
    "executor_source": {
      "decision": "REFUSE",
      "refusal_reason": "edge-source-is-not-coordinator",
      "ruler": null
    },
    "fallback_probe": {
      "decision": "ROUTE",
      "refusal_reason": null,
      "ruler": "owner-human"
    },
    "false_owner_initiated": {
      "decision": "REFUSE",
      "refusal_reason": "mismatched-verdict-signer",
      "ruler": null
    },
    "false_then_higher_true": {
      "decision": "ROUTE",
      "refusal_reason": null,
      "ruler": "ruler-root"
    },
    "mismatched_signer": {
      "decision": "REFUSE",
      "refusal_reason": "mismatched-verdict-signer",
      "ruler": null
    },
    "missing_parent": {
      "decision": "REFUSE",
      "refusal_reason": "missing-parent-prefix",
      "ruler": null
    },
    "no_true_owner": {
      "decision": "ROUTE",
      "refusal_reason": null,
      "ruler": "owner-human"
    },
    "nonhuman_owner": {
      "decision": "REFUSE",
      "refusal_reason": "governing-owner-is-not-a-declared-human",
      "ruler": null
    },
    "ordinary_cl": {
      "decision": "ROUTE",
      "refusal_reason": null,
      "ruler": "owner-human"
    },
    "owner_initiated": {
      "decision": "DIRECT_OWNER_ACT",
      "refusal_reason": null,
      "ruler": "owner-human"
    },
    "owner_reserved": {
      "decision": "HUMAN",
      "refusal_reason": null,
      "ruler": "owner-human"
    },
    "proposer_nearest_true": {
      "decision": "ROUTE",
      "refusal_reason": null,
      "ruler": "ruler-root"
    },
    "provider_as_provenance": {
      "decision": "REFUSE",
      "refusal_reason": "missing-or-competing-root-authorization",
      "ruler": null
    },
    "purpose_not_fit": {
      "decision": "HUMAN",
      "refusal_reason": null,
      "ruler": "owner-human"
    },
    "repeated_child": {
      "decision": "REFUSE",
      "refusal_reason": "repeated-child",
      "ruler": null
    },
    "restrict": {
      "decision": "APPLY_ON_FILING",
      "refusal_reason": null,
      "ruler": null
    },
    "review_reject": {
      "decision": "HUMAN",
      "refusal_reason": null,
      "ruler": "owner-human"
    },
    "root_child": {
      "decision": "ROUTE",
      "refusal_reason": null,
      "ruler": "ruler-root"
    },
    "same_principal_fresh_session": {
      "decision": "ROUTE",
      "refusal_reason": null,
      "ruler": "ruler-top"
    },
    "title_as_provenance": {
      "decision": "REFUSE",
      "refusal_reason": "missing-or-competing-root-authorization",
      "ruler": null
    },
    "two_level_nearest": {
      "decision": "ROUTE",
      "refusal_reason": null,
      "ruler": "ruler-mid"
    },
    "two_roots": {
      "decision": "REFUSE",
      "refusal_reason": "missing-or-competing-root-authorization",
      "ruler": null
    },
    "unassigned_owner": {
      "decision": "REFUSE",
      "refusal_reason": "governing-owner-is-not-a-declared-human",
      "ruler": null
    },
    "unavailable_participant": {
      "decision": "HUMAN",
      "refusal_reason": null,
      "ruler": "owner-human"
    },
    "unknown_destination": {
      "decision": "REFUSE",
      "refusal_reason": "unknown-destination",
      "ruler": null
    },
    "unknown_grant": {
      "decision": "REFUSE",
      "refusal_reason": "unknown-duplicate-or-changed-grant",
      "ruler": null
    },
    "unknown_writer": {
      "decision": "REFUSE",
      "refusal_reason": "unknown-writer",
      "ruler": null
    }
  },
  "mutants": [
    {
      "case": "two_level_nearest",
      "family": "proposer-preservation",
      "independent_expected_rejects": true,
      "normal": {
        "case": "two_level_nearest",
        "decision": "ROUTE",
        "path": [
          "ruler-mid",
          "ruler-root",
          "owner-human"
        ],
        "proposer": "probe-worker",
        "refusal_reason": null,
        "ruler": "ruler-mid",
        "signer": "ruler-mid"
      },
      "produced": {
        "case": "two_level_nearest",
        "decision": "REFUSE",
        "path": [],
        "proposer": "ruler-mid",
        "refusal_reason": "mismatched-verdict-signer",
        "ruler": null,
        "signer": "ruler-mid"
      },
      "projection_changed": true
    },
    {
      "case": "two_level_nearest",
      "family": "nearest-order",
      "independent_expected_rejects": true,
      "normal": {
        "case": "two_level_nearest",
        "decision": "ROUTE",
        "path": [
          "ruler-mid",
          "ruler-root",
          "owner-human"
        ],
        "proposer": "probe-worker",
        "refusal_reason": null,
        "ruler": "ruler-mid",
        "signer": "ruler-mid"
      },
      "produced": {
        "case": "two_level_nearest",
        "decision": "REFUSE",
        "path": [],
        "proposer": "probe-worker",
        "refusal_reason": "mismatched-verdict-signer",
        "ruler": null,
        "signer": "ruler-mid"
      },
      "projection_changed": true
    },
    {
      "case": "false_then_higher_true",
      "family": "grant-polarity",
      "independent_expected_rejects": true,
      "normal": {
        "case": "false_then_higher_true",
        "decision": "ROUTE",
        "path": [
          "ruler-mid",
          "ruler-root",
          "owner-human"
        ],
        "proposer": "probe-worker",
        "refusal_reason": null,
        "ruler": "ruler-root",
        "signer": "ruler-root"
      },
      "produced": {
        "case": "false_then_higher_true",
        "decision": "REFUSE",
        "path": [],
        "proposer": "probe-worker",
        "refusal_reason": "mismatched-verdict-signer",
        "ruler": null,
        "signer": "ruler-root"
      },
      "projection_changed": true
    },
    {
      "case": "same_principal_fresh_session",
      "family": "stable-handle",
      "independent_expected_rejects": true,
      "normal": {
        "case": "same_principal_fresh_session",
        "decision": "ROUTE",
        "path": [
          "probe-worker",
          "ruler-top",
          "owner-human"
        ],
        "proposer": "probe-worker",
        "refusal_reason": null,
        "ruler": "ruler-top",
        "signer": "ruler-top"
      },
      "produced": {
        "case": "same_principal_fresh_session",
        "decision": "REFUSE",
        "path": [],
        "proposer": "probe-worker",
        "refusal_reason": "mismatched-verdict-signer",
        "ruler": null,
        "signer": "ruler-top"
      },
      "projection_changed": true
    },
    {
      "case": "fallback_probe",
      "family": "status-owner-fallback",
      "independent_expected_rejects": true,
      "normal": {
        "case": "fallback_probe",
        "decision": "ROUTE",
        "path": [
          "ruler-mid",
          "ruler-root",
          "owner-human"
        ],
        "proposer": "probe-worker",
        "refusal_reason": null,
        "ruler": "owner-human",
        "signer": "owner-human"
      },
      "produced": {
        "case": "fallback_probe",
        "decision": "REFUSE",
        "path": [],
        "proposer": "probe-worker",
        "refusal_reason": "mismatched-verdict-signer",
        "ruler": null,
        "signer": "owner-human"
      },
      "projection_changed": true
    },
    {
      "case": "accountable_without_root",
      "family": "accountability-provenance",
      "independent_expected_rejects": true,
      "normal": {
        "case": "accountable_without_root",
        "decision": "REFUSE",
        "path": [],
        "proposer": "probe-worker",
        "refusal_reason": "missing-or-competing-root-authorization",
        "ruler": null,
        "signer": "ruler-mid"
      },
      "produced": {
        "case": "accountable_without_root",
        "decision": "ROUTE",
        "path": [
          "ruler-mid",
          "ruler-root",
          "owner-human"
        ],
        "proposer": "probe-worker",
        "refusal_reason": null,
        "ruler": "ruler-mid",
        "signer": "ruler-mid"
      },
      "projection_changed": true
    },
    {
      "case": "executor_source",
      "family": "coordinator-only",
      "independent_expected_rejects": true,
      "normal": {
        "case": "executor_source",
        "decision": "REFUSE",
        "path": [],
        "proposer": "probe-worker",
        "refusal_reason": "edge-source-is-not-coordinator",
        "ruler": null,
        "signer": "ruler-root"
      },
      "produced": {
        "case": "executor_source",
        "decision": "ROUTE",
        "path": [
          "exec-worker",
          "ruler-root",
          "owner-human"
        ],
        "proposer": "probe-worker",
        "refusal_reason": null,
        "ruler": "ruler-root",
        "signer": "ruler-root"
      },
      "projection_changed": true
    },
    {
      "case": "false_owner_initiated",
      "family": "owner-explicit-act",
      "independent_expected_rejects": true,
      "normal": {
        "case": "false_owner_initiated",
        "decision": "REFUSE",
        "path": [],
        "proposer": "probe-worker",
        "refusal_reason": "mismatched-verdict-signer",
        "ruler": null,
        "signer": "owner-human"
      },
      "produced": {
        "case": "false_owner_initiated",
        "decision": "DIRECT_OWNER_ACT",
        "path": [
          "owner-human"
        ],
        "proposer": "owner-human",
        "refusal_reason": null,
        "ruler": "owner-human",
        "signer": "owner-human"
      },
      "projection_changed": true
    },
    {
      "case": "restrict",
      "family": "restrict-filing",
      "independent_expected_rejects": true,
      "normal": {
        "case": "restrict",
        "decision": "APPLY_ON_FILING",
        "path": [],
        "proposer": "probe-worker",
        "refusal_reason": null,
        "ruler": null,
        "signer": null
      },
      "produced": {
        "case": "restrict",
        "decision": "REFUSE",
        "path": [],
        "proposer": "probe-worker",
        "refusal_reason": "mismatched-verdict-signer",
        "ruler": null,
        "signer": null
      },
      "projection_changed": true
    },
    {
      "case": "purpose_not_fit",
      "family": "purpose-owner",
      "independent_expected_rejects": true,
      "normal": {
        "case": "purpose_not_fit",
        "decision": "HUMAN",
        "path": [
          "owner-human"
        ],
        "proposer": "probe-worker",
        "refusal_reason": null,
        "ruler": "owner-human",
        "signer": "owner-human"
      },
      "produced": {
        "case": "purpose_not_fit",
        "decision": "REFUSE",
        "path": [],
        "proposer": "probe-worker",
        "refusal_reason": "mismatched-verdict-signer",
        "ruler": null,
        "signer": "owner-human"
      },
      "projection_changed": true
    }
  ],
  "payloads": {
    "accountability_as_provenance": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "accountability_as_provenance",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "other-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": "owner-human",
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "accountable_without_root": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "accountable_without_root",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "agent_self_grant": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": "probe-worker",
      "name": "agent_self_grant",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "owner-human",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "backward_ancestor": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "root",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "backward_ancestor",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "binding_as_provenance": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "binding_as_provenance",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": "ruler-root",
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "budget_return": {
      "amendment_type": "EXTEND",
      "claim_delegated": false,
      "edges": [],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "budget_return",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [],
      "route_kind": "budget",
      "signer": "owner-human",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "changed_grant": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "changed_grant",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": true,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "competing_parent": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "competing_parent",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "contract_defect": {
      "amendment_type": "EXTEND",
      "claim_delegated": false,
      "edges": [],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "contract_defect",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [],
      "route_kind": "contract_defect",
      "signer": "owner-human",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "coordinator_transcribes_child": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "coordinator_transcribes_child",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "duplicate_grant": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "duplicate_grant",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": [
            true,
            false
          ],
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "executor_source": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "executor",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "executor"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "executor_source",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-root",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "fallback_probe": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "fallback_probe",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "other-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "owner-human",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "false_owner_initiated": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "false_owner_initiated",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": true,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "owner-human",
      "spoof_provenance": {
        "accountable_to": "owner-human",
        "binding": "owner-human",
        "on_behalf_of": "owner-human",
        "provider": null,
        "title": "Owner"
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "false_then_higher_true": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "false_then_higher_true",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-root",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "mismatched_signer": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "mismatched_signer",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-root",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "missing_parent": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "orphan"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "missing_parent",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "orphan": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "orphan-ruler",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "no_true_owner": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "no_true_owner",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "owner-human",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "nonhuman_owner": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "nonhuman_owner",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-agent",
        "type": "agent"
      },
      "transcriber_node": "mid"
    },
    "ordinary_cl": {
      "amendment_type": "EXTEND",
      "claim_delegated": false,
      "edges": [],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "ordinary_cl",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [],
      "route_kind": "amendment",
      "signer": "owner-human",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "owner_initiated": {
      "amendment_type": "EXTEND",
      "claim_delegated": false,
      "edges": [],
      "explicit_owner_decision": true,
      "grant_change_for": null,
      "name": "owner_initiated",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "owner-human",
      "owner_initiated": true,
      "proposer_node": null,
      "reserved": false,
      "root_authorizations": [],
      "route_kind": "amendment",
      "signer": "owner-human",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": null
    },
    "owner_reserved": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "owner_reserved",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": true,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "owner-human",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "proposer_nearest_true": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "proposer_nearest_true",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "ruler-mid",
      "owner_initiated": false,
      "proposer_node": "mid",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-root",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "root"
    },
    "provider_as_provenance": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "provider_as_provenance",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": "codex",
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "purpose_not_fit": {
      "amendment_type": "EXTEND",
      "claim_delegated": false,
      "edges": [],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "purpose_not_fit",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [],
      "route_kind": "purpose_not_fit",
      "signer": "owner-human",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "repeated_child": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "repeated_child",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-root",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "restrict": {
      "amendment_type": "RESTRICT",
      "claim_delegated": false,
      "edges": [],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "restrict",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [],
      "route_kind": "amendment",
      "signer": null,
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "review_reject": {
      "amendment_type": "EXTEND",
      "claim_delegated": false,
      "edges": [],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "review_reject",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [],
      "route_kind": "review_reject",
      "signer": "owner-human",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "root_child": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "root_child",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-root",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "same_principal_fresh_session": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "fresh",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "top"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "fresh"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "same_principal_fresh_session",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "fresh": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "top": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-top",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "top",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-top",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "title_as_provenance": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "title_as_provenance",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": "Coordinator"
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "two_level_nearest": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "two_level_nearest",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "two_roots": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "two_roots",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root2": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-second",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        },
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root2",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "unassigned_owner": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "unassigned_owner",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "unassigned",
        "type": "unassigned"
      },
      "transcriber_node": "mid"
    },
    "unavailable_participant": {
      "amendment_type": "EXTEND",
      "claim_delegated": false,
      "edges": [],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "unavailable_participant",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [],
      "route_kind": "unavailable",
      "signer": "owner-human",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "unknown_destination": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "missing",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "unknown_destination",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "unknown_grant": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "mid",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "root"
        },
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "mid"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "unknown_grant",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": null,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    },
    "unknown_writer": {
      "amendment_type": "EXTEND",
      "claim_delegated": true,
      "edges": [
        {
          "destination": "worker",
          "role_ref": "authority/delegation-record",
          "scope_ref": "phase/status.md",
          "writer": "missing"
        }
      ],
      "explicit_owner_decision": false,
      "grant_change_for": null,
      "name": "unknown_writer",
      "nodes": {
        "executor": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "exec-worker",
          "type": "agent",
          "workflow_role": "Executor"
        },
        "mid": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-mid",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "root": {
          "accountable_to": "owner-human",
          "grant": true,
          "grant_changed": false,
          "handle": "ruler-root",
          "type": "agent",
          "workflow_role": "Coordinator"
        },
        "worker": {
          "accountable_to": "owner-human",
          "grant": false,
          "grant_changed": false,
          "handle": "probe-worker",
          "type": "agent",
          "workflow_role": "Researcher"
        }
      },
      "originating_proposer": "probe-worker",
      "owner_initiated": false,
      "proposer_node": "worker",
      "reserved": false,
      "root_authorizations": [
        {
          "authority_ref": "authority/delegation-record",
          "coordinator": "root",
          "owner": "owner-human",
          "scope_ref": "phase/status.md"
        }
      ],
      "route_kind": "amendment",
      "signer": "ruler-mid",
      "spoof_provenance": {
        "accountable_to": null,
        "binding": null,
        "on_behalf_of": null,
        "provider": null,
        "title": null
      },
      "status_owner": {
        "handle": "owner-human",
        "type": "human"
      },
      "transcriber_node": "mid"
    }
  }
}
SUMMARY fixtures=38 parity=38 mutants=10 output_changing_rejected=10
```
## Source records and live owner-only census

```text
rg -n `status.md.owner` must be a declared human|separate governing record authorizes the root Coordinator|nearest remaining immutable `true` principal|`HL Contract` rule 8|Owner-reserved|preserving origin|resolved-ruler verdict required|route to the \*\*owner\*\*, never the executor|Anyone edits a frozen HL section without a ?12 row carrying a logged owner verdict .tfw/conventions.md .tfw/workflows/plan.md .tfw/workflows/review.md .tfw/workflows/handoff.md .tfw/templates/HL.md .tfw/templates/RES.md
```

Exit 0; raw:

```text
.tfw/templates/RES.md:35:> (§1, §3–§7). The Coordinator transcribes the latter into §12 as `PROPOSED`, preserving origin, then
.tfw/templates/RES.md:36:> routes by `conventions.md` → `HL Contract` rule 8. Frozen claims wait for a valid terminal verdict.
.tfw/templates/RES.md:46:### Amendment Proposals — frozen sections, resolved-ruler verdict required
.tfw/workflows/plan.md:180:4. **Route once per iteration** — preserve each proposer; submit the evidenced/costed batch under `HL Contract` rule 8
.tfw/templates/HL.md:240:> transcription and later sessions. Resolve and sign under `conventions.md` → `HL Contract` rule 8;
.tfw/templates/HL.md:244:> **Owner-initiated** uses rule 9 only for the real human owner's explicit act on that row. Owner-reserved
.tfw/workflows/handoff.md:68:3. **Rung 3:** accept only after `HL Contract` rule 8 resolves a valid terminal verdict leaving an
.tfw/workflows/review.md:144:pass; both route to the **owner**, never the executor (`judge.md` row 2a). Rung 3 follows `The 🔄
.tfw/workflows/review.md:145:REVISE route` and `HL Contract` rule 8; the Reviewer preserves the proposer, proposes, and stops
.tfw/conventions.md:72:8. **A verdict is a distinct, resolved act.** Chat or workflow input is evidence, never a verdict. The governing task/phase `status.md.owner` must be a declared human and supplies the root/fallback ruler; a separate governing record authorizes the root Coordinator. Ordinary CL without delegated claim routes to that owner. For claimed delegation, a task/phase-local `dispatch` edge is its `writer` → destination plus governing scope/role references. Only a Coordinator on one unambiguous human-rooted prefix may add a new child. Before work refuse an Executor source, unknown/repeated/competing node or parent, ancestor/task-Coordinator target, missing root authorization, or non-human/unresolved termination. Preserve the originating proposer through transcription and sessions. For ordinary `EXTEND`/`SUPERSEDE`, walk upward from the proposer: skip `false` grants and the same handle; choose the nearest remaining immutable `true` principal, otherwise the owner. Before the signed terminal verdict validate chain, proposer, grant, reservation and signer; gaps or contradictions stay `PROPOSED` and block. Profile role, `accountable_to`, binding, title, provider, `writer`, or `on_behalf_of` never supplies root, path, proposer or grant. Owner-reserved claims and an agent's own grant/handle change route to the owner.
```

Broad Baseline census:

```text
git grep -n -i -E owner|ruler|verdict fb08c120a91aca4c9ceaea859d46dd49c032afd0 -- .tfw/conventions.md .tfw/workflows/plan.md .tfw/workflows/review.md .tfw/workflows/handoff.md .tfw/templates/HL.md .tfw/templates/RES.md
```

Exit 0; raw:

```text
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:59:| HL section | State after owner approval |
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:65:1. **The contract state is artifact state.** The HL header carries a `Contract` field with two values: `📝 DRAFT — not yet approved` and `🔒 FROZEN — approved by {owner} YYYY-MM-DD`. Task status tracks the pipeline; the `Contract` field tracks the artifact. They are not interchangeable.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:66:2. **Free sections stay free.** Research and the coordinator update §2, §7.2, §8, §9, §10 and §11 directly, with no proposal and no verdict. Risk registers, hypothesis statuses and dependency statuses are required to move.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:67:3. **A frozen section may not be edited.** The only channel is §12 Amendment Log: propose, wait for the owner's verdict, then apply. This holds for every role, including the coordinator that authored the HL.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:72:8. **A verdict is a distinct recorded act.** Input given inside a research thread, a review or a chat is evidence for a proposal, never approval of one. A proposal is ruled only by an explicit owner verdict written onto its §12 row.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:73:9. **An owner-initiated change to a frozen section is an amendment too** — logged in §12 with the owner as `Proposer` and the verdict on the same row. The log's value is the record, not the gate: a §12 that omits the owner's own changes cannot answer the question it exists to answer.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:74:10. **A restrictive change applies on filing.** Narrowing — adding a DoF item, tightening scope, dropping a deliverable — is logged with `Type` = `RESTRICT` and verdict `✅ APPLIED — no owner verdict required`. Restrictive-free is prohibited: the classifier benefits from the label, so the log costs nothing and removes the incentive.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:75:11. **`Type` states relation to the baseline, never disposition.** `EXTEND` adds and the original stays in force; `SUPERSEDE` replaces; `RESTRICT` narrows. Disposition belongs in `Verdict`.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:144:Formal coordinator report after reviewing RF: checklist, verdict, and a disposition on every debt item it captured.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:192:> The EV file captures environment metadata, per-AC verification results, and a verdict summary.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:199:| EV file | `evidence/EV__{...}.md` | Observational / Verification | Environment header, per-AC evidence table, verdict, attachments |
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:200:| RF | §5 Evidence (pointer) | Summary / Reference | One-line pointer to EV file + verdict summary |
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:247:the owner approves both before a directory is created; the HL header carries them side by side
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:250:code a person cannot read back — and never created without the owner's approval. A title is
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:254:owner-approved abbreviation. It never recomputes the timestamp, adds a suffix or silently
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:408:| **REVIEW** | **sibling** | Exactly one verdict is live, and the highest ordinal is it |
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:470:Every AI-authored commit MUST use `[agent/task/scope/role] summary`: set `agent` to the lowercase AI product name from explicit context, `task` to the canonical TFW task ID (`project` only when none exists), `scope` to the established lowercase work-slice slug or a lowercase hyphenated form of its explicit label, and `role` to the lowercase canonical TFW workflow owner from §15/Role Lock; keep `summary` short and imperative, commit locally, and push only after explicit user approval.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:489:not define a merge strategy; one mutation owner controls each worktree.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:638:| ❌ REJECTED | Task closed unsuccessfully and permanently. Distinct from ❌ BLOCKED, which is waiting and resumes when the dependency clears. Terminal: no status follows it, and the task folder and its board row are never deleted. This is a task status — not the review verdict ❌ REJECT, and not the HL §12 amendment verdict ❌ REJECTED; neither of those is terminal |
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:643:**`UNDECLARED`: migration never normalizes; an accountable owner may resolve.**
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:648:| The task's owner setting the correct value and recording a `transition` event with `from: UNDECLARED` | **Yes.** The accountable decision and its trace are explicit |
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:666:Review verdicts:
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:669:  once, then follows **The 🔄 REVISE route** below. The verdict alone never moves lifecycle
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:679:verdict artifact; recording a Coordinator ruling there is acceptance control, not a new
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:686:| Rung 3 | a frozen HL claim | Coordinator, then owner through the amendment channel | HL §12 proposal plus `amendment_escalated` event and owner verdict | none until the owner verdict leaves an executable bound | unchanged; Executor is not dispatchable | Reviewer → Coordinator → owner; **STOP until owner verdict** |
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:689:A REVISE item names the failed TS acceptance criterion or frozen HL claim, its owner, and an
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:693:dispatch until the owner verdict leaves an executable bound. The Executor appends ONB, RF, and EV
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:695:with the remainder disposed, or transition to `BLOCKED` and return to the task owner because no
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:696:basis can be stated. An `unassigned` owner is a hard stop. A fresh role holder resolves lineage
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:763:| Owner escalation multiplier | 2 | `owner_escalation_multiplier` | Delegated boundary against each immutable planned measure |
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:766:verdict, and pre-work ref. Compare forecasts/Candidate with the immutable owner plan; no ruling ratchets it.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:767:Owner rules before work at/above multiplier or from planned zero. Below it, Coordinator may add only a
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:768:necessary constituent while Goal, Value, outputs, AC, DoF, phase/ownership, architecture/target,
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:809:| [review.md](workflows/review.md) | Reviewer | Read RF → checklist → verdict → debt disposed → traces |
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:941:| Category | Files | Init | Update | Owner |
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:1057:- Anyone edits a frozen HL section without a §12 row carrying a logged owner verdict — the silent contract edit the amendment channel exists to replace
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:1059:- Coordinator applies an amendment before its verdict — the proposal and the change become the same act, and the owner rules on something already done
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:1061:- Any role treats a remark inside a research thread, a review or a chat as an amendment verdict — a comment is input, a verdict is a distinct recorded act
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/conventions.md:1141:When a Reviewer reaches a verdict, the correct action is to **name the next act** — a decision with
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/HL.md:5:> **Title**: {Title — the full title the owner approved}
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/HL.md:9:> **Frozen**: §1 · §3 · §4 · §5 · §6 · §7 — locked on owner approval
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/HL.md:14:> **Contract field** — one line, two states. Until the owner approves:
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/HL.md:16:> `🔒 FROZEN — approved by {owner} YYYY-MM-DD` and commits the file before research starts.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/HL.md:17:> A frozen section may not be edited afterwards: propose in §12, wait for the verdict.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/HL.md:47:> §3.1 is a gate, not an illustration: the owner's checkpoint **before** the spend of tokens and
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/HL.md:233:> A frozen section may not be edited before its row carries a verdict. Rows are never deleted,
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/HL.md:239:> **A remark inside a research thread is input, never a verdict.** Only an explicit owner ruling,
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/HL.md:240:> recorded on the row, changes a proposal's status. An **owner-initiated** change to a frozen
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/HL.md:241:> section is an amendment too: same row, `Proposer` = owner, verdict on the same line.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/HL.md:247:>   change applies **on filing** and is logged with the verdict `✅ APPLIED — no owner verdict
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/HL.md:250:> **`Verdict` values:** `PROPOSED` (awaiting a ruling) · `✅ APPROVED — {ruler}, YYYY-MM-DD` ·
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/HL.md:251:> `❌ REJECTED — {ruler}, YYYY-MM-DD` · `✅ APPLIED — no owner verdict required` (`RESTRICT` only) ·
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/HL.md:254:> credit the owner with a decision they never made).
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/HL.md:263:| # | Date | § | Type | Proposer | Proposed change | Evidence | Cost | Alternatives considered | Verdict |
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/HL.md:265:| A1 | YYYY-MM-DD | §{n} | `EXTEND` / `SUPERSEDE` / `RESTRICT` | {owner / coordinator / research iterN / executor} | {what changes} | {where the finding comes from} | {what it costs to accept} | {what else was weighed and why it lost} | `PROPOSED` |
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/RES.md:40:>   may **not** apply them. They are transcribed into HL §12 Amendment Log with verdict `PROPOSED`
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/RES.md:41:>   and wait for an owner ruling. Nothing in a frozen section moves before that ruling exists.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/RES.md:54:### Amendment Proposals — frozen sections, owner verdict required
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/templates/RES.md:57:> adds `Date` and `Proposer` on transcription, and `Verdict` opens as `PROPOSED`. The `#` column
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/handoff.md:68:3. **Rung 3:** do not accept a handoff until the owner verdict leaves an executable bound. A pending
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/handoff.md:79:revision, or a rung-3 round without an owner verdict is not executable. Record the missing authority
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/handoff.md:119:prompts and require their recorded terminal disposition, not a quality veto. The owner-approved VALUE
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/handoff.md:121:forecast at or above `owner_escalation_multiplier`, or growth from an applicable planned zero. The
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/handoff.md:148:    explain every non-VERIFIED row, summarize the verdict counts, and index any attachments.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/handoff.md:156:    - RF §5 says `See [EV file](...) for evidence details.` plus verdict summary.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/handoff.md:163:    including §5 as an EV pointer plus verdict summary and §7–§9 with explicit `No …` when empty.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/plan.md:72:   owner approves both in this exchange, before any task directory is created. Never invent a
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/plan.md:93:   if dir exists: STOP; ask the owner to approve a different abbreviation
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/plan.md:136:1. Set the HL header `Contract` field to `🔒 FROZEN — approved by {owner} YYYY-MM-DD`
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/plan.md:179:   - frozen claim → transcribe into HL §12 with verdict `PROPOSED`; the section itself stays untouched
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/plan.md:180:4. **Escalate once per iteration** — send all evidenced/costed alternatives together; only the owner rules them
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/plan.md:193:### 6d. Amendment verdicts — whenever one arrives, in research, ONB, review or execution
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/plan.md:195:- **✅ Approved** → apply frozen change, record §12 verdict, then commit the new `freeze` baseline
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/plan.md:196:- **❌ Rejected** → the row keeps its verdict and stays; the original contract holds; resume work
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/plan.md:197:- **`RESTRICT`** → applies on filing, no verdict required (`conventions.md` §3 rule 10)
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/plan.md:216:6b. Get owner approval of the TS and immutable VALUE denominator. Suggest `/tfw-handoff`; repeat per phase.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/plan.md:225:   claim, owner, and observable completion condition; an empty basis fails the citation bar.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/plan.md:229:   For rung 3, file the HL §12 proposal and `amendment_escalated` event, then wait for the owner; do
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/plan.md:230:   not dispatch an Executor until the verdict leaves an executable bound.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/plan.md:232:   `/tfw-handoff`." Rung 3: name the amendment and say "STOP until owner verdict." Never execute the
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:9:> **Output:** REVIEW file with verdict + a disposition on every debt item it captured
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:14:> Never modify implementation; fundamental defects go in REVIEW with verdict ❌ REJECT.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:27:| 5 | Decide | stage files; `.tfw/conventions.md` headings `Task control files`, `Session identity`, `Artifact file naming`, `Task Statuses`, `The 🔄 REVISE route`, `Safety and Execution Honesty`, `Trace Discipline`, and `Role Lock Protocol`; `.tfw/templates/REVIEW.md` | identity, verdict, disposition, routing, trace | stage/shared rule/template |
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:104:immutable owner-approved denominator. The Reviewer may not ratchet the plan, construct a different selector,
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:105:supply missing Coordinator/Owner authority after work, or invent a competing total. Missing, mutable,
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:138:> **Mindset:** Decision-maker. Synthesize stages into a binding verdict with cited proof.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:141:Write `REVIEW__*.md` from its template: synthesize §1–§3; §4 gives the evidenced APPROVE/REVISE/REJECT verdict.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:144:passing, and both route to the **owner**, never the executor (`judge.md` row 2a).
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:147:acceptance criterion, or a frozen HL claim; the rest is disposed of in §5. Cite nothing and the verdict is
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:148:✅ APPROVE, the remainder disposed. Neither cite nor approve and the work returns to the task's `owner`
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:152:membership, arithmetic, timing, or authority disagreement, and route it through the existing verdict rules.
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:174:## Step 6: Record verdict, then route proposals
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:180:After verdict:
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:181:1. **Set the task's own state only when the verdict authorizes it** — APPROVE enters `KNW`; REJECT
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:182:   follows its selected owner route; REVISE alone does not move lifecycle. Every actual transition
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:185:2. **Check §5** — every item carries one of the three dispositions. An undisposed item blocks `DONE`, not the verdict
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:192:After ✅ APPROVE verdict:
fb08c120a91aca4c9ceaea859d46dd49c032afd0:.tfw/workflows/review.md:200:**Hard stop:** after the verdict and its authorized trace/KNW routing are recorded, stop. Never
```

| Site | Old | Classification | Basis |
|---|---|---|---|
| conventions rule 3 | wait for owner | replaced route | rule-8 verdict |
| conventions rule 8 | owner only | replaced route | sole human-root resolver |
| conventions rules 9-10 | owner act / no verdict | preserved exceptions | real owner and RESTRICT |
| REVISE Rung 3 | to owner | replaced route | rule-8 ruler |
| section 14 silent edit | logged owner verdict | live; narrowed | row gate; rule 8 signer |
| section 14 early apply | owner after act | live; narrowed | pre-verdict ban |
| HL header/section 12 | owner ruling | replaced route | origin/ruler/signature |
| HL owner/RESTRICT/WITHDRAWN | owner acts | preserved exceptions | human-only cases |
| RES recommendations | owner ruling | replaced route | rule-8 verdict |
| Handoff Rung 3 | owner bound | replaced route | rule-8 verdict |
| Plan iteration/6d/REVISE | wait owner | replaced route | validate authority |
| Review Purpose/defect/REJECT | owner route | preserved exceptions | AC-3 routes |
| identifier/freeze/TS/budget | owner approval | unrelated | not amendment |
| CHANGELOG/KNOWLEDGE/traces | historical | historical | not live |

The section 14 sentence is live, not history. It competes only if treated as a second signer
algorithm. Canonical rule 8 narrows it to the owner-rooted section 12 channel and alone chooses the
ruler; HL verdict forms name that ruler. Its legacy owner wording is disclosed for Reviewer.
## Copy parity and assurance

| Canonical | Copy | Canonical SHA-256 | Copy SHA-256 | Equal |
|---|---|---|---|---|
| .tfw/workflows/plan.md | .agent/workflows/tfw-plan.md | a73290e9504ee95e267758064fdfafd5a68b263a29ef67503935a374fbcd48d2 | a73290e9504ee95e267758064fdfafd5a68b263a29ef67503935a374fbcd48d2 | yes |
| .tfw/workflows/plan.md | .claude/commands/tfw-plan.md | a73290e9504ee95e267758064fdfafd5a68b263a29ef67503935a374fbcd48d2 | a73290e9504ee95e267758064fdfafd5a68b263a29ef67503935a374fbcd48d2 | yes |
| .tfw/workflows/review.md | .agent/workflows/tfw-review.md | 0082008bd307635a7d6632d078ddc7753d1881c7782a69a51b489c8b2fae58ce | 0082008bd307635a7d6632d078ddc7753d1881c7782a69a51b489c8b2fae58ce | yes |
| .tfw/workflows/review.md | .claude/commands/tfw-review.md | 0082008bd307635a7d6632d078ddc7753d1881c7782a69a51b489c8b2fae58ce | 0082008bd307635a7d6632d078ddc7753d1881c7782a69a51b489c8b2fae58ce | yes |
| .tfw/workflows/handoff.md | .agent/workflows/tfw-handoff.md | 5c1faf2f0b61935a1273071ea5d7e8f49cacedb98580a2f67c071fdab2cd676d | 5c1faf2f0b61935a1273071ea5d7e8f49cacedb98580a2f67c071fdab2cd676d | yes |
| .tfw/workflows/handoff.md | .claude/commands/tfw-handoff.md | 5c1faf2f0b61935a1273071ea5d7e8f49cacedb98580a2f67c071fdab2cd676d | 5c1faf2f0b61935a1273071ea5d7e8f49cacedb98580a2f67c071fdab2cd676d | yes |

```text
python -m pytest docs/scripts/test_runtime_context.py -q -k "cratm_phase_c or test_phase_c_every_changed_path_and_active_corpus_clear_thirty_percent or test_rtpsn_phase_b_context_routes_corpus_and_local_caps_do_not_grow"
34 passed, 143 deselected in 33.90s; exit 0
python -m pytest docs/scripts/test_runtime_context.py -q -k "cratm_phase_c"
13 passed, 164 deselected; exit 0
python -m pytest docs/scripts/test_integration.py -q -k "cratm_phase_c or revision_2_revise"
4 passed, 93 deselected in 133.72s; exit 0
```

The integration mutant injects STOP until owner verdict and is independently rejected.
## Attention, compatibility, tests, and build

```powershell
@'
import importlib.util,json,pathlib,sys
p=pathlib.Path('docs/scripts/test_runtime_context.py').resolve();s=importlib.util.spec_from_file_location('ctx',p);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
t=m.SourceTree.from_git(pathlib.Path('.').resolve(),'b2a963670e2587cffa6a61d8851f37065f03cda9');print(json.dumps(m.session_identity_context_payload(t),indent=2,sort_keys=True))
'@ | python -
```

Exit 0; raw:

```json
{
  "active_corpus": {
    "baseline": 33749,
    "candidate": 33288,
    "ceiling": 33749
  },
  "baseline": "83b31ff8d6cdb879fdf4f20578fa688b48863f8a",
  "central_range": {
    "cap": 260,
    "passes": true,
    "words": 33
  },
  "claim_level": "R0/R1 structural and synthetic semantic evidence only",
  "routes": {
    "/tfw-docs": {
      "baseline": 15278,
      "candidate": 15264,
      "ceiling": 15278,
      "passes": true
    },
    "/tfw-handoff": {
      "baseline": 6366,
      "candidate": 6339,
      "ceiling": 6366,
      "passes": true
    },
    "/tfw-handoff:revise": {
      "baseline": 6366,
      "candidate": 6339,
      "ceiling": 6366,
      "passes": true
    },
    "/tfw-init": {
      "baseline": 4529,
      "candidate": 4513,
      "ceiling": 4529,
      "passes": true
    },
    "/tfw-plan": {
      "baseline": 24725,
      "candidate": 24678,
      "ceiling": 24725,
      "passes": true
    },
    "/tfw-research:deep": {
      "baseline": 6167,
      "candidate": 6156,
      "ceiling": 6167,
      "passes": true
    },
    "/tfw-research:focused": {
      "baseline": 6102,
      "candidate": 6091,
      "ceiling": 6102,
      "passes": true
    },
    "/tfw-resume": {
      "baseline": 3264,
      "candidate": 3194,
      "ceiling": 3264,
      "passes": true
    },
    "/tfw-review": {
      "baseline": 24954,
      "candidate": 24920,
      "ceiling": 24954,
      "passes": true
    }
  },
  "workflow_local": {
    ".tfw/workflows/docs.md": {
      "cap": 45,
      "net_words": -36,
      "passes": true
    },
    ".tfw/workflows/handoff.md": {
      "cap": 45,
      "net_words": -97,
      "passes": true
    },
    ".tfw/workflows/init.md": {
      "cap": 45,
      "net_words": -54,
      "passes": true
    },
    ".tfw/workflows/plan.md": {
      "cap": 45,
      "net_words": -103,
      "passes": true
    },
    ".tfw/workflows/research/base.md": {
      "cap": 45,
      "net_words": -83,
      "passes": true
    },
    ".tfw/workflows/resume.md": {
      "cap": 45,
      "net_words": -101,
      "passes": true
    },
    ".tfw/workflows/review.md": {
      "cap": 45,
      "net_words": -82,
      "passes": true
    }
  }
}
```

| Canonical | Baseline words | Candidate words | Net |
|---|---:|---:|---:|
| .tfw/conventions.md | 10854 | 11009 | +155 |
| .tfw/workflows/plan.md | 2057 | 2047 | -10 |
| .tfw/workflows/review.md | 2084 | 2105 | +21 |
| .tfw/workflows/handoff.md | 1987 | 1991 | +4 |
| .tfw/templates/HL.md | 1994 | 2002 | +8 |
| .tfw/templates/RES.md | 925 | 807 | -118 |

RES is below about 1,200. Protected spans equal approval ref 1f1173d968e9b74a5e06e3e2070ae604c2844ca5.

| Span | Baseline SHA-256 | Candidate SHA-256 | Equal |
|---|---|---|---|
| PHASE_C_PRIMARY_ENTRY_WORDS | 5e5bc216b0520e0843b56214f5f0973abdc9a3632a21213fa14b064bb5c6e81d | 5e5bc216b0520e0843b56214f5f0973abdc9a3632a21213fa14b064bb5c6e81d | yes |
| SESSION_ROUTE_CEILINGS | 87a076a1e9fb2849ffae9f27734208ee933cd865649e053795d3cd3a8c34ba4d | 87a076a1e9fb2849ffae9f27734208ee933cd865649e053795d3cd3a8c34ba4d | yes |
| test_phase_c_every_changed_path_and_active_corpus_clear_thirty_percent | 58633a1093493d7b11394aebb1e38184e89814ef3c163baa1fc45580985abb8d | 58633a1093493d7b11394aebb1e38184e89814ef3c163baa1fc45580985abb8d | yes |
| test_vbsa_plan_loads_three_unique_canonical_sections_with_d75_intact | ccc50c1dff23242d86e9faca61bf065e07546f87600f02892aefb704eb12802c | ccc50c1dff23242d86e9faca61bf065e07546f87600f02892aefb704eb12802c | yes |

```python
SESSION_ROUTE_CEILINGS = {
    "/tfw-plan": 24_725,
    "/tfw-research:focused": 6_102,
    "/tfw-research:deep": 6_167,
    "/tfw-handoff": 6_366,
    "/tfw-handoff:revise": 6_366,
    "/tfw-review": 24_954,
    "/tfw-resume": 3_264,
    "/tfw-docs": 15_278,
    "/tfw-init": 4_529,
}
```

Rejected short forms: convention-only loses consumers; unsynchronized copies contradict; old test
text preserves a false oracle. No A5 or cap edit.

```text
python -m pytest .tfw/scripts/ docs/scripts/ --collect-only -qq
192 + 65 + 31 + 74 + 97 + 177 = 636 collected; exit 0
python -m pytest .tfw/scripts/ docs/scripts/ -q
635 passed, 1 skipped in 360.27s (0:06:00); exit 0
python .tfw/scripts/gen_index.py --check project
framework 2.1.0; 1 participant; project consistent; exit 0
git diff --check fb08c120a91aca4c9ceaea859d46dd49c032afd0 b2a963670e2587cffa6a61d8851f37065f03cda9 -- [exact 14 paths]
no output; exit 0
```

Integration autouse runs python -m mkdocs build --config-file docs/mkdocs.yml before 97 tests and
fails on nonzero; full-suite success therefore includes the real Candidate build.
## Immutable accounting and lineage

```powershell
$valuePaths = @(
  '.tfw/conventions.md',
  '.tfw/workflows/plan.md',
  '.tfw/workflows/review.md',
  '.tfw/workflows/handoff.md',
  '.tfw/templates/HL.md',
  '.tfw/templates/RES.md',
  '.agent/workflows/tfw-plan.md',
  '.agent/workflows/tfw-review.md',
  '.agent/workflows/tfw-handoff.md',
  '.claude/commands/tfw-plan.md',
  '.claude/commands/tfw-review.md',
  '.claude/commands/tfw-handoff.md'
)
$baselineSha = 'fb08c120a91aca4c9ceaea859d46dd49c032afd0'
$candidateSha = 'b2a963670e2587cffa6a61d8851f37065f03cda9'
git diff --name-status --find-renames=50% -z $baselineSha $candidateSha -- $valuePaths
git diff --numstat --find-renames=50% -z $baselineSha $candidateSha -- $valuePaths
```

NUL bytes escaped and decoded without line splitting:

```json
{
  "actual_additions": 89,
  "actual_deletions": 90,
  "actual_touched_loc": 179,
  "approval_ref": "1f1173d968e9b74a5e06e3e2070ae604c2844ca5",
  "approved_denominator": {
    "additions": 200,
    "deletions": 120,
    "files": 12,
    "immutable": true,
    "touched_loc": 320
  },
  "authority_timing": "approval predates handoff",
  "baseline": "fb08c120a91aca4c9ceaea859d46dd49c032afd0",
  "binary_non_text": "N/A; numeric numstat",
  "candidate": "b2a963670e2587cffa6a61d8851f37065f03cda9",
  "logical_value_files": 12,
  "name_status_argv": [
    "git",
    "diff",
    "--name-status",
    "--find-renames=50%",
    "-z",
    "fb08c120a91aca4c9ceaea859d46dd49c032afd0",
    "b2a963670e2587cffa6a61d8851f37065f03cda9",
    "--",
    ".tfw/conventions.md",
    ".tfw/workflows/plan.md",
    ".tfw/workflows/review.md",
    ".tfw/workflows/handoff.md",
    ".tfw/templates/HL.md",
    ".tfw/templates/RES.md",
    ".agent/workflows/tfw-plan.md",
    ".agent/workflows/tfw-review.md",
    ".agent/workflows/tfw-handoff.md",
    ".claude/commands/tfw-plan.md",
    ".claude/commands/tfw-review.md",
    ".claude/commands/tfw-handoff.md"
  ],
  "name_status_exit": 0,
  "name_status_raw_nul_escaped": "M\\0.agent/workflows/tfw-handoff.md\\0M\\0.agent/workflows/tfw-plan.md\\0M\\0.agent/workflows/tfw-review.md\\0M\\0.claude/commands/tfw-handoff.md\\0M\\0.claude/commands/tfw-plan.md\\0M\\0.claude/commands/tfw-review.md\\0M\\0.tfw/conventions.md\\0M\\0.tfw/templates/HL.md\\0M\\0.tfw/templates/RES.md\\0M\\0.tfw/workflows/handoff.md\\0M\\0.tfw/workflows/plan.md\\0M\\0.tfw/workflows/review.md\\0",
  "name_status_records": [
    {
      "action": "M",
      "path": ".agent/workflows/tfw-handoff.md"
    },
    {
      "action": "M",
      "path": ".agent/workflows/tfw-plan.md"
    },
    {
      "action": "M",
      "path": ".agent/workflows/tfw-review.md"
    },
    {
      "action": "M",
      "path": ".claude/commands/tfw-handoff.md"
    },
    {
      "action": "M",
      "path": ".claude/commands/tfw-plan.md"
    },
    {
      "action": "M",
      "path": ".claude/commands/tfw-review.md"
    },
    {
      "action": "M",
      "path": ".tfw/conventions.md"
    },
    {
      "action": "M",
      "path": ".tfw/templates/HL.md"
    },
    {
      "action": "M",
      "path": ".tfw/templates/RES.md"
    },
    {
      "action": "M",
      "path": ".tfw/workflows/handoff.md"
    },
    {
      "action": "M",
      "path": ".tfw/workflows/plan.md"
    },
    {
      "action": "M",
      "path": ".tfw/workflows/review.md"
    }
  ],
  "numstat_argv": [
    "git",
    "diff",
    "--numstat",
    "--find-renames=50%",
    "-z",
    "fb08c120a91aca4c9ceaea859d46dd49c032afd0",
    "b2a963670e2587cffa6a61d8851f37065f03cda9",
    "--",
    ".tfw/conventions.md",
    ".tfw/workflows/plan.md",
    ".tfw/workflows/review.md",
    ".tfw/workflows/handoff.md",
    ".tfw/templates/HL.md",
    ".tfw/templates/RES.md",
    ".agent/workflows/tfw-plan.md",
    ".agent/workflows/tfw-review.md",
    ".agent/workflows/tfw-handoff.md",
    ".claude/commands/tfw-plan.md",
    ".claude/commands/tfw-review.md",
    ".claude/commands/tfw-handoff.md"
  ],
  "numstat_exit": 0,
  "numstat_raw_nul_escaped": "3\t3\t.agent/workflows/tfw-handoff.md\\013\t14\t.agent/workflows/tfw-plan.md\\04\t2\t.agent/workflows/tfw-review.md\\03\t3\t.claude/commands/tfw-handoff.md\\013\t14\t.claude/commands/tfw-plan.md\\04\t2\t.claude/commands/tfw-review.md\\010\t7\t.tfw/conventions.md\\09\t6\t.tfw/templates/HL.md\\010\t20\t.tfw/templates/RES.md\\03\t3\t.tfw/workflows/handoff.md\\013\t14\t.tfw/workflows/plan.md\\04\t2\t.tfw/workflows/review.md\\0",
  "numstat_records": [
    {
      "additions": 3,
      "deletions": 3,
      "path": ".agent/workflows/tfw-handoff.md",
      "touched_loc": 6
    },
    {
      "additions": 13,
      "deletions": 14,
      "path": ".agent/workflows/tfw-plan.md",
      "touched_loc": 27
    },
    {
      "additions": 4,
      "deletions": 2,
      "path": ".agent/workflows/tfw-review.md",
      "touched_loc": 6
    },
    {
      "additions": 3,
      "deletions": 3,
      "path": ".claude/commands/tfw-handoff.md",
      "touched_loc": 6
    },
    {
      "additions": 13,
      "deletions": 14,
      "path": ".claude/commands/tfw-plan.md",
      "touched_loc": 27
    },
    {
      "additions": 4,
      "deletions": 2,
      "path": ".claude/commands/tfw-review.md",
      "touched_loc": 6
    },
    {
      "additions": 10,
      "deletions": 7,
      "path": ".tfw/conventions.md",
      "touched_loc": 17
    },
    {
      "additions": 9,
      "deletions": 6,
      "path": ".tfw/templates/HL.md",
      "touched_loc": 15
    },
    {
      "additions": 10,
      "deletions": 20,
      "path": ".tfw/templates/RES.md",
      "touched_loc": 30
    },
    {
      "additions": 3,
      "deletions": 3,
      "path": ".tfw/workflows/handoff.md",
      "touched_loc": 6
    },
    {
      "additions": 13,
      "deletions": 14,
      "path": ".tfw/workflows/plan.md",
      "touched_loc": 27
    },
    {
      "additions": 4,
      "deletions": 2,
      "path": ".tfw/workflows/review.md",
      "touched_loc": 6
    }
  ],
  "phase_attribution": "all literal rows resolve to Phase C TS section 4; otherwise INVALID",
  "planning_content_ref": "95eb2ab510ed8d89205ed5fe498ccb061c112888",
  "trigger": {
    "actual": "12 files / 179 touched LOC",
    "configured": "50 files / 5000 touched LOC",
    "disposition": "one inseparable phase; below prompts"
  }
}
```

All rows are MODIFY/VALUE with TS reasons: contract, Plan, Review, Handoff, HL, RES, six receivers.
Two other Candidate paths are declared ASSURANCE; TRACE is excluded.

```json
{
  "ancestry": {
    "approval_to_candidate": {
      "ancestor": "1f1173d968e9b74a5e06e3e2070ae604c2844ca5",
      "descendant": "b2a963670e2587cffa6a61d8851f37065f03cda9",
      "exit": 0,
      "passes": true
    },
    "baseline_to_planning": {
      "ancestor": "fb08c120a91aca4c9ceaea859d46dd49c032afd0",
      "descendant": "95eb2ab510ed8d89205ed5fe498ccb061c112888",
      "exit": 0,
      "passes": true
    },
    "planning_to_approval": {
      "ancestor": "95eb2ab510ed8d89205ed5fe498ccb061c112888",
      "descendant": "1f1173d968e9b74a5e06e3e2070ae604c2844ca5",
      "exit": 0,
      "passes": true
    }
  },
  "candidate": "b2a963670e2587cffa6a61d8851f37065f03cda9",
  "candidate_to_capture_tip_value_diff": "",
  "capture_tip": "b2a963670e2587cffa6a61d8851f37065f03cda9",
  "membership": [
    ".agent/workflows/tfw-handoff.md",
    ".agent/workflows/tfw-plan.md",
    ".agent/workflows/tfw-review.md",
    ".claude/commands/tfw-handoff.md",
    ".claude/commands/tfw-plan.md",
    ".claude/commands/tfw-review.md",
    ".tfw/conventions.md",
    ".tfw/templates/HL.md",
    ".tfw/templates/RES.md",
    ".tfw/workflows/handoff.md",
    ".tfw/workflows/plan.md",
    ".tfw/workflows/review.md",
    "docs/scripts/test_integration.py",
    "docs/scripts/test_runtime_context.py"
  ],
  "membership_count": 14,
  "parent": "dc0a4388cdf2ccdb473b9450d1f18d648e96f610",
  "subject": "[codex/TFW_20260902-111644_CRATM/phase-c/executor] implement authority routing"
}
```

Bootstrap reported clean approval HEAD and planning parent before writes. Candidate is first after
the 635-pass run. At capture HEAD equals Candidate and later VALUE diff is empty. Reviewer reruns;
any later VALUE invalidates Candidate.
## Limitations and continuation

- R0/R1 does not authenticate actors or external systems.
- Section 14 wording is ambiguous alone; rule-8 narrowing is disclosed.
- Post-review tfw-docs is coordinator-only. Candidate is below Docs 15,278 and corpus 33,749;
  coordinator reruns before DONE.
- Executor does not pre-write REVIEW.

## Verdict

Evidence verdict: **7/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A** at Candidate boundary.

No attachments; full validator, expanded payloads, raw results, census, counts and lineage are inline.

---

*EV ? TFW_20260902-111644_CRATM / Phase C: Authority routing | 2026-09-06*


