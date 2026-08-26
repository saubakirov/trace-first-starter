# TFW55-I2-CATEGORY-EXEC-v3

Status: **PENDING NEW EXTRACT GATE — ZERO v3 RUNS**

This package replaces only the invalidated execution instrumentation for the category family. It does not modify the frozen v2 fixture, category semantics, opaque labels/order, answer key, rubric, critic/scorer schemas, replication rule, or evidence limits.

The invalidated v2 category traces remain audit-only at `research/iter2/challenge_runs/category/`. They are not pass 1, replication, comparison, or research evidence. v3 must restart all five category critics and all required scorers from the beginning.

## Why v3 exists

The fourth v2 category scorer received an abbreviated manually assembled prompt. v3 removes that discretionary assembly step:

1. `build_category_inputs.ps1 -Mode critic-packets` mechanically generates all five exact critic packet files from hash-guarded v2.
2. After each critic, its raw JSON is saved verbatim.
3. `build_category_inputs.ps1 -Mode scorer-input` performs mechanical checks and generates the complete exact scorer input from the preassembled packet, raw output, v2 neutral answer key, complete rubric, and exact scorer schema.
4. Before scorer spawn, the generated scorer-input SHA-256 is recorded.
5. The fresh scorer preserves the exact prompt it received; that prompt's SHA-256 must match before the next scorer starts. Any mismatch invalidates the whole family immediately.

Fresh isolation and settings remain `gpt-5.6-sol`, reasoning `low`, `fork_turns=none`, one critic or scorer per task. Mapping stays sealed through all required passes. The v2 full-family replication rule remains literal.

No v3 run is authorized until the coordinator closes the new Extract gate.
