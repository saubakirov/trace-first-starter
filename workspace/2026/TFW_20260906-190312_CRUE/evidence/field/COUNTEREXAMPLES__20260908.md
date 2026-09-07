# Bounded source-derived counterexamples — 2026-09-08

These are synthetic/source checks only. They do not exercise a provider, updater, receiver, or owner.

## Provenance counterexample

Synthetic state: `tfw.version=3.0.0`, `tfw.installed_from=...@v2.0.0`, applied source SHA
`d6d26003972f7b18fe10d492960d0cbac9f0a3e8`, and no `v3.0.0` tag. The settled source rule rejects
silently retaining the old installed provenance after applying the new payload and also rejects
inventing `...@v3.0.0`; it requires the configured upstream plus the verified Candidate SHA and an
explicit untagged-Candidate label.

## Owner-language counterexample

The baseline briefing template contains the owner-language instruction “what it lets them do, not what
the procedure calls it”. Candidate d6 lacks that instruction. The final Candidate restores the
instruction in the briefing template and Step 8 while retaining outcome-led, evidence-bounded wording.
This is a source regression check, not proof of native briefing quality or comprehension.

The bounded assertion was run after the final Candidate was committed:

```powershell
$base = git show 8fd8e40b734e9c439bb84721ef8bee441b9fcdd7:.tfw/templates/briefing.md
$field = git show d6d26003972f7b18fe10d492960d0cbac9f0a3e8:.tfw/templates/briefing.md
$final = Get-Content .tfw/templates/briefing.md -Raw
$workflow = Get-Content .tfw/workflows/update.md -Raw
$baseHas = [bool]($base -match 'what it lets them do')
$fieldHas = [bool]($field -match 'what it lets them do')
$finalHas = [bool]($final -match 'what the change lets them do')
$workflowHas = [bool]($workflow -match 'verified full Candidate SHA')
if ((-not $baseHas) -or $fieldHas -or (-not $finalHas) -or (-not $workflowHas)) { throw 'counterexample failed' }
'PASS: old-tag/new-payload provenance and owner-language loss/restoration are source-derived only'
```

Observed output:

```text
PASS: old-tag/new-payload provenance and owner-language loss/restoration are source-derived only
```
