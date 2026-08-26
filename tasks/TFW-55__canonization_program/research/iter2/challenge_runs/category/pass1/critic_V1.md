---
family: category
pass: 1
opaque_label: V1
task: /root/cat_p1_v1
model: gpt-5.6-sol
reasoning: low
fork_turns: none
status: completed-before-family-invalidation
---

## Exact full prompt

```text
You are an independent model-based bounded critic. Work only from the supplied frozen packet. You have no project history and must not infer founder intent or a preferred label. Do not use outside knowledge. Return only the requested JSON object.

For every case, return case_id, classification as TFW|NOT_TFW|INSUFFICIENT, one-sentence reason tied to the packet boundary, and when_apply. Then return definition, exclusions, primary_category_claim, and any internal ambiguity. Do not judge whether the category is philosophically true.

{"type":"object","additionalProperties":false,"required":["variant_label","cases","definition","exclusions","primary_category_claim","ambiguities","required_source_ids"],"properties":{"variant_label":{"type":"string"},"cases":{"type":"array","minItems":7,"maxItems":7,"items":{"type":"object","additionalProperties":false,"required":["case_id","classification","reason","when_apply"],"properties":{"case_id":{"type":"string"},"classification":{"enum":["TFW","NOT_TFW","INSUFFICIENT"]},"reason":{"type":"string"},"when_apply":{"type":"string"}}}},"definition":{"type":"string"},"exclusions":{"type":"array","items":{"type":"string"}},"primary_category_claim":{"type":"string"},"ambiguities":{"type":"array","items":{"type":"string"}},"required_source_ids":{"type":"array","items":{"type":"string"}}}}

VARIANT V1

Primary claim: this is a methodology for traceable AI-delegated work. A methodology is an organized transferable system of stable behaviours for bounding delegated cognition and preserving continuity across projects. Required boundary: F1 human purpose/authority; F2 bounded AI delegation; F3 selected durable material trace and result/current state; F4 authoritative result plus explicit continuation. Assurance scales separately with risk. The methodology excludes raw transcript-only archives, provenance without purpose/continuation, governance registers without work continuity, and ordinary project frameworks that do not require this full composition.

[{"id":"N1","text":"A repository has ADRs, Git history, and documentation CI. AI work happens in chat; no acceptance owner, durable result state, or continuation is recorded."},{"id":"N2","text":"A research assignment states purpose and human acceptance, bounds an AI analyst role, records material sources and rejected interpretations, preserves the verified result and current state, and names the next action using ordinary filenames."},{"id":"N3","text":"A complete provenance graph identifies entities, activities, agents, derivations, and timestamps but omits purpose, acceptance/stop responsibility, result selection, and continuation."},{"id":"N4","text":"An AI risk register defines roles, monitoring, and deactivation, but no selected task, result, decision, or continuation trace exists."},{"id":"N5","text":"A team uses every Scrum element. Material AI-delegated decisions and continuation state disappear when chat closes."},{"id":"N6","text":"A simple low-risk policy memo has one obvious source and no material alternative. A human states purpose and acceptance, bounds the AI role, and a durable note records the source, result, current closed state, and no-next-action status."},{"id":"N7","text":"A raw chat transcript is archived with timestamps but no selected decisions, authority declaration, authoritative result, or continuation summary."}]
```

## Exact raw output

```json
{
  "variant_label": "V1",
  "cases": [
    {
      "case_id": "N1",
      "classification": "NOT_TFW",
      "reason": "The repository has durable technical records but lacks F1 acceptance authority, F3 durable result/current state, and F4 explicit continuation.",
      "when_apply": "Classify as TFW only when the AI-delegated work also records human purpose and acceptance authority, selected material trace, authoritative result/current state, and continuation."
    },
    {
      "case_id": "N2",
      "classification": "TFW",
      "reason": "The assignment explicitly satisfies F1 through F4, and the use of ordinary filenames does not violate any stated boundary.",
      "when_apply": "Apply when those purpose, authority, bounded delegation, selected trace, authoritative state, and continuation records are durable."
    },
    {
      "case_id": "N3",
      "classification": "NOT_TFW",
      "reason": "The provenance graph supplies trace data but omits F1 purpose and authority, F3 result selection, and F4 continuation.",
      "when_apply": "Classify as TFW only if the provenance system is composed with explicit human purpose and authority, an authoritative selected result/current state, and continuation."
    },
    {
      "case_id": "N4",
      "classification": "NOT_TFW",
      "reason": "The risk register provides governance controls but no task-level F3 result/current state or F4 continuation trace.",
      "when_apply": "Classify as TFW only when governance is joined to a selected AI-delegated task satisfying the complete F1-F4 composition."
    },
    {
      "case_id": "N5",
      "classification": "NOT_TFW",
      "reason": "Complete Scrum usage does not meet the required composition because material AI decisions and continuation state are not durable after chat closes.",
      "when_apply": "Classify as TFW only when the project framework additionally requires and preserves all F1-F4 elements for the delegated work."
    },
    {
      "case_id": "N6",
      "classification": "TFW",
      "reason": "The low-risk memo satisfies F1 through F4, with a closed state and explicit no-next-action status constituting continuation.",
      "when_apply": "Apply at assurance proportional to the low risk; the absence of material alternatives does not require invented rejection traces."
    },
    {
      "case_id": "N7",
      "classification": "NOT_TFW",
      "reason": "A raw timestamped transcript lacks selected material trace, F1 authority, F3 authoritative result, and F4 continuation summary.",
      "when_apply": "Classify as TFW only after selected durable records establish the complete F1-F4 composition rather than relying on the transcript alone."
    }
  ],
  "definition": "TFW is an organized, transferable system of stable behaviours for traceable AI-delegated work that requires human purpose and authority, bounded AI delegation, selected durable material trace plus result/current state, and an authoritative result with explicit continuation.",
  "exclusions": [
    "Raw transcript-only archives",
    "Provenance records without purpose and continuation",
    "Governance registers without work continuity",
    "Ordinary project frameworks that do not require the full F1-F4 composition"
  ],
  "primary_category_claim": "TFW is a methodology for traceable AI-delegated work, with assurance scaled separately according to risk.",
  "ambiguities": [
    "The packet does not define a precise threshold for what makes a trace material or sufficiently selected.",
    "The packet does not specify the minimum durable form or storage medium for authoritative records.",
    "The packet does not fully define how much detail explicit continuation requires beyond examples such as a next action or no-next-action status.",
    "The packet states that assurance scales with risk but does not provide risk tiers or corresponding assurance measures."
  ],
  "required_source_ids": [
    "F1",
    "F2",
    "F3",
    "F4"
  ]
}
```
