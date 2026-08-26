# Category family — invalidated instrumentation trace

Status: **INVALIDATED BEFORE PASS-1 SCORING COMPLETION — NO COMPARATIVE EVIDENCE**

## Failure

The critic pass completed for all five opaque variants in frozen order. Separate scoring completed for `Q7`, `M2`, and `R5`. While issuing the `K8` scorer, the orchestrator supplied an abbreviated `PACKET`, shortened `RUBRIC`, and loosened `OUTPUT_SCHEMA` instead of the exact frozen scorer input required by `TFW55-I2-EXTRACT-v2`.

This is an execution-protocol/design defect, not a malformed model output and not a replication trigger. Under the frozen `no_adaptation` rule:

- the whole category family is invalid;
- the `K8` score must not be used;
- the otherwise valid `Q7/M2/R5` scores must not be compared;
- `V1` received no scorer because execution stopped immediately after detecting the defect;
- pass 2 is prohibited as a repair, and no mapping was revealed;
- no later families were started.

## Frozen-order ledger

| Opaque label | Critic | Scorer | Status |
|---|---:|---:|---|
| `Q7` | completed | completed | preserved, unusable because family invalid |
| `M2` | completed | completed | preserved, unusable because family invalid |
| `R5` | completed | completed | preserved, unusable because family invalid |
| `K8` | completed | completed with wrong scorer input | invalidating event; raw trace preserved |
| `V1` | completed | not started | stopped by freeze rule |

## Mapping seal

The opaque-to-configuration mapping was **not revealed to any critic or scorer and is not interpreted here**. The existing mapping remains only inside the already-frozen v2 instrument. No category conclusion, C1/C3/C4/C9/C10 disposition, or H2 inference is drawn from these runs.

## Required next gate

Return the category family to Extract for a newly frozen execution package that makes exact scorer-input assembly mechanically reproducible. Challenge remains stopped before ablation. The preserved traces are instrumentation/audit evidence only, never research evidence.
