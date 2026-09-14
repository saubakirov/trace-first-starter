# R3 observer checkpoint launch and scope

From the f3f3 repository root, the actual tested launch is:

```powershell
& 'E:/TEMP/pttc-phase-a-b9b5/venv/Scripts/python.exe' 'workspace/2026/TFW_20260909-231654_TKL/evidence/r3-preflight/observer.py' preflight
```

This command was executed once in operation 3. Do not rerun it after its hard deadline.
The observer SHA-256 is `515fa7513171ba663f784982df23a994e3052370081381022cdf808fd0e5dd48`.
For a later authorized native operation, the same file exposes `file` and `tree` with required
`--root` and `--output` arguments. Output must be outside the observed subject. Its single
`observe_bytes` function supplies the same byte/hash/Git/bare-EOL interpretation for every mode.
Future tree enumeration and native application have not run or been verified by this preflight.
A native pin must impose actual existence, cardinality, source/authority and complete-preservation
guards; it cannot infer those from the preflight result.

The full finite proposal is `03-observation-schema.json`; exact identities and target derivations
are `03-source-authority-target.json`. The first proposed native invocation reads its own actual
clock only after a separate immutable Coordinator pin. No receiver path has been opened here.
Old R2 clock/grants/results remain exhausted/history, and the new grant is conditional.
