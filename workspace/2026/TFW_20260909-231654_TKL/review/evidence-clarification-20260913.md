# Reviewer check receipt — 2026-09-13

## Scope and provenance

This is a record-only seal of checks already executed in Reviewer task
`01a09aaf-9af3-7d13-8ef8-59d3bc84d5e7`. It does not start a review round and did not execute a
test, build, native trial or product/helper mutation. The source verdict epoch remains
`de2abc53da88da3e990d83c3ec4efd0859da46ff`; its review input is
`3b1c1237eef44c0fd7283831d12888d927765c21`, Candidate is
`27cdb701b91c5b45b9f54b3e98c9ad67635b3e30`, and Baseline is
`ec91c56007c20cda79f740fec15c85e4af74d17c`.

The original Reviewer turn is Codex turn `01a09b96-46f0-7133-b87b-e5018412e1ee`, with the
available system clock envelope `2026-09-13T16:25:12Z` through `2026-09-13T17:11:55Z`
(`2,803,699 ms`). The command-event schema retained durations but no per-command start/finish
timestamps. No narrower wall-clock values are reconstructed. The current record observation was
made at `2026-09-13T17:16:37.6158073Z`; lifecycle was `RF`, HEAD was `de2abc...`, and the working
tree was clean. `review/map.md` was not edited; its SHA-256 at that observation was
`26fbe654fafaf3014eaa44441c2c65f648d1cc928e9f8d026efbd579540c41ee`.

## Fresh affected pytest slice already run

Origin event: `exec-25dc6fa1-f52b-45e5-938c-d1f9a6f96ef7`. The event records the exact outer
executable and command below, cwd
`C:\Users\c0rpa\.codex\worktrees\19a7\steps-framework`, status `completed`, exit code `0`, and
duration `191,089 ms`.

```text
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -Command 'python -m pytest tools/tests/test_tfw_state.py tools/tests/test_tfw_doctor.py docs/scripts/test_repository_contracts.py docs/scripts/test_runtime_context.py docs/scripts/test_update_experience.py docs/scripts/test_gen_docs.py docs/scripts/test_integration.py -q -k "tkl or knowledge_pending or nested_record or no_normative_file_states_a_retired_rule or no_adapter_file_states_a_retired_rule or installed_adapter_copies_match_their_sources"'
```

Expanded inner argv was:

```text
python
-m
pytest
tools/tests/test_tfw_state.py
tools/tests/test_tfw_doctor.py
docs/scripts/test_repository_contracts.py
docs/scripts/test_runtime_context.py
docs/scripts/test_update_experience.py
docs/scripts/test_gen_docs.py
docs/scripts/test_integration.py
-q
-k
tkl or knowledge_pending or nested_record or no_normative_file_states_a_retired_rule or no_adapter_file_states_a_retired_rule or installed_adapter_copies_match_their_sources
```

The event preserved the inner executable token `python`, not the resolved process path. A read-only
same-session observation at `2026-09-13T17:16:37.6158073Z` resolved that token to
`D:\python\Python313\python.exe` (file version `3.13.5`, 105,816 bytes, file mtime
`2025-06-11T13:10:24Z`). This is a post-run resolver observation, not a fabricated
contemporaneous executable receipt.

The seven exact test homes are the seven path arguments above. Static inspection identifies the
selected names in them as the `tkl_*` cases plus
`test_knowledge_pending_reports_changed_removed_and_migration`,
`test_installed_adapter_copies_match_their_sources`,
`test_no_normative_file_states_a_retired_rule`, and
`test_no_adapter_file_states_a_retired_rule`; parametrization accounts for the executed-case count.

The command event retained one combined PTY output, not separately located stdout/stderr files. The
complete accessible output is sealed below exactly as UTF-8 with CRLF line endings: 129 bytes,
SHA-256 `cecd50770152f96174e92da0e62a1aeca3ffe3652f7bc75a4009cdc55dc787b8`.

```text
...................................................                      [100%]
51 passed, 489 deselected in 189.47s (0:03:09)
```

Tracked source for the check was review input `3b1c123...`; the 65 VALUE+ASSURANCE paths inspected
by Reviewer were Git-equal to Candidate. The command wrapper did not contemporaneously seal a full
working-tree status, so this receipt does not claim more. The already-created untracked Reviewer
stage directory was outside product/assurance scope.

## Current isolated documentation build already run

Origin event: `exec-b55abe88-cf7c-4bef-84b0-0811e3e9e718`. It records the same outer PowerShell
executable/cwd, status `completed`, exit code `0`, and duration `149,250 ms`. The actual inner build
argv was:

```text
python
-m
mkdocs
build
--config-file
docs/mkdocs.yml
--site-dir
C:\Users\c0rpa\AppData\Local\Temp\tfw-review-01a09aaf-current-site
```

The exact wrapper also checked these generated routes after the build:

```text
knowledge/records/TKL-20260913-01/index.html
knowledge-index/index.html
knowledge/process/index.html
tasks/TFW-22__coordinator_research_enrichment/RES__TFW-22__coordinator_research_enrichment/index.html
tasks/2026/TFW_20260909-231654_TKL/journal/20260913-141400__handoff__8c2a/index.html
tasks/2026/TFW_20260909-231654_TKL/HL-TFW_20260909-231654_TKL/index.html
```

All six existed. The wrapper also returned
`RECORD_LINK_D37=True RECORD_LINK_D82=True RECORD_LINK_OWNER=True`, and MkDocs reported
`Documentation built in 148.28 seconds`. The command's combined output was not file-captured and
the Codex event archive marks it `truncated: true`, `originalChars: 1042074`; therefore no false
raw-stream location or hash is asserted. The retained site directory is the result oracle for the
five targeted failures. Relevant page identities are:

| Generated page | Bytes | SHA-256 | mtime UTC |
|---|---:|---|---|
| `tasks/2026/TFW_20260909-231654_TKL/HL-TFW_20260909-231654_TKL/index.html` | 118510 | `abe5752e55c23ced56cd57fa34decd269cd38e9ee812f1a049aebd54838b51ea` | `2026-09-13T17:03:26.7689102Z` |
| `tasks/2026/TFW_20260909-231654_TKL/ONB__TFW_20260909-231654_TKL/index.html` | 97637 | `938e5543ab097ff5e10e3a8dd4d7df161c67562f02c6f0c1139ef7ef74071368` | `2026-09-13T17:03:26.7849815Z` |
| `tasks/2026/TFW_20260907-020729_SLC/RF__TFW_20260907-020729_SLC/index.html` | 88552 | `c636634f11f814d93e72976fa669b317445a37f4710e666d6882568d7848f540` | `2026-09-13T17:03:25.5064706Z` |
| `tasks/2026/TFW_20260907-020729_SLC/REVIEW__TFW_20260907-020729_SLC/index.html` | 110794 | `dbe812b0d7630d08ea54f6f8b6ffbbaa1c751f0a6f8c598818681f81438f8472` | `2026-09-13T17:03:25.4920806Z` |
| `reference/workflows/knowledge/index.html` | 55004 | `78fe70c862d87632fe78ddbb4b2df9cb466df9b8ea58a6a13580b958bff34ec8` | `2026-09-13T17:03:17.4516196Z` |

Five concrete occurrences were checked against those exact HTML bytes:

| # | Source occurrence and generated fragment | Target/checked HTML IDs | Result |
|---:|---|---|---|
| 1 | `HL-TFW_20260909-231654_TKL.md:31` → `reference/workflows/knowledge/#canonical-knowledge-gate-algorithm` | target page contains no `id="canonical-knowledge-gate-algorithm"` and no gate/canonical ID was inferred as a replacement | broken |
| 2 | `HL-TFW_20260909-231654_TKL.md:190` → SLC RF `#11-correction-round-c2--exact-link-preservation` | requested ID absent; generated ID is `11-correction-round-c2-exact-link-preservation` | broken |
| 3 | `HL-TFW_20260909-231654_TKL.md:190` → SLC REVIEW `#c2-bounded-acceptance--2026-09-10` | requested ID absent; generated ID is `c2-bounded-acceptance-2026-09-10` | broken |
| 4 | `ONB__TFW_20260909-231654_TKL.md:81` → SLC RF `#11-correction-round-c2--exact-link-preservation` | requested ID absent; generated ID is `11-correction-round-c2-exact-link-preservation` | broken |
| 5 | `ONB__TFW_20260909-231654_TKL.md:81` → SLC REVIEW `#independent-c2-return-and-closure-boundary--2026-09-10` | requested ID absent; generated ID is `independent-c2-return-and-closure-boundary-2026-09-10` | broken |

## Run-13 source-before mismatch accounting

Run 13 used source commit `9543ad3b9504a691c457dc721e606cc1017e483d`; its receipt clocks are
`2026-09-13T11:03:37.090124Z` through `2026-09-13T11:12:14.816977Z`. Raw map
`evidence/checks/13-full/source-before.json` is 9,958 bytes with SHA-256
`df9e78d4f54468f585115deef4bfe7657fef476862722331ead477f8d8d31633`; raw archive
`source-before.zip` is 458,407 bytes with SHA-256
`5cbd7d3711603c42c4ab05fac704c7724504e3cddf94291fb1d230f0efa63643`.
The JSON has 69 entries; the archive has 68 and omits only
`.tfw/templates/knowledge_state.yaml`, whose JSON entry is explicitly `{"absent":true}`. Each of the
18 rows below exists in the archive and its raw
bytes reproduce the JSON identity.

`EOL` values are `CRLF/LF/CR` terminator counts. `Candidate` is Git blob SHA-1 and blob bytes.
`Working` is raw filesystem SHA-256 and bytes at the record observation. For all 18 rows, replacing
CRLF with LF makes the complete texts byte-identical; the common normalized prefix is the entire
file, the Git-filtered working blob equals Candidate, and the only observed difference is the EOL
observer representation. No semantic change is inferred from the raw/Git hash difference.

| Path | Source-before raw: bytes; SHA-256; EOL | Candidate: blob; bytes | Working raw: bytes; SHA-256; EOL |
|---|---|---|---|
| `.tfw/conventions.md` | 100306; `97cb69402892b42fc3f05646586d57d0f962d8f3b0a94ac285865b6fc96636ea`; 1436/0/0 | `ab5504f898e972fc02d3827665070cbede9cf60c`; 98870 | 98870; `fb05c43570cf65b512e620c97633d0115daa8b733e9649e4a3c426e566b8cf21`; 0/1436/0 |
| `.tfw/workflows/review.md` | 16727; `c9c63ad961e70e66a3a480dc646586e0f27fa2bf61fc76b20689f876bef6e492`; 248/0/0 | `a389ae6f619d28d5a2a18745fd2eb73531208f5d`; 16479 | 16479; `6ba0bd35cece81760270e23de42cf14c030ac9450e6eac12c15123527a4ca2f6`; 0/248/0 |
| `.tfw/workflows/docs.md` | 4992; `3863e69a77371a084156dd295e38dd0b3f9788f4ddd632961e99808da464e176`; 75/0/0 | `26b80dbb58c2f1406afef90ea5639f9dced246b7`; 4917 | 4917; `46fb7316afdb4c8ceb7e7c5986332781f44d678fbd224baa4846a4e38c133271`; 0/75/0 |
| `.tfw/workflows/knowledge.md` | 7106; `1701035491afd0eb2558f9c0d818b5295bee247eb9443d1f394fc00ec09f0520`; 101/0/0 | `48b6a1547ddd4cee3291240b10939375bd16763e`; 7005 | 7005; `8fc4ebd2a220155967a460465ac1a49f80273562bd6e0a9d5db09c3d2757d61c`; 0/101/0 |
| `.agents/workflows/tfw-review.md` | 16727; `c9c63ad961e70e66a3a480dc646586e0f27fa2bf61fc76b20689f876bef6e492`; 248/0/0 | `a389ae6f619d28d5a2a18745fd2eb73531208f5d`; 16479 | 16479; `6ba0bd35cece81760270e23de42cf14c030ac9450e6eac12c15123527a4ca2f6`; 0/248/0 |
| `.claude/commands/tfw-review.md` | 16727; `c9c63ad961e70e66a3a480dc646586e0f27fa2bf61fc76b20689f876bef6e492`; 248/0/0 | `a389ae6f619d28d5a2a18745fd2eb73531208f5d`; 16479 | 16479; `6ba0bd35cece81760270e23de42cf14c030ac9450e6eac12c15123527a4ca2f6`; 0/248/0 |
| `.agents/workflows/tfw-docs.md` | 4992; `3863e69a77371a084156dd295e38dd0b3f9788f4ddd632961e99808da464e176`; 75/0/0 | `26b80dbb58c2f1406afef90ea5639f9dced246b7`; 4917 | 4917; `46fb7316afdb4c8ceb7e7c5986332781f44d678fbd224baa4846a4e38c133271`; 0/75/0 |
| `.claude/commands/tfw-docs.md` | 4992; `3863e69a77371a084156dd295e38dd0b3f9788f4ddd632961e99808da464e176`; 75/0/0 | `26b80dbb58c2f1406afef90ea5639f9dced246b7`; 4917 | 4917; `46fb7316afdb4c8ceb7e7c5986332781f44d678fbd224baa4846a4e38c133271`; 0/75/0 |
| `.agents/workflows/tfw-knowledge.md` | 7106; `1701035491afd0eb2558f9c0d818b5295bee247eb9443d1f394fc00ec09f0520`; 101/0/0 | `48b6a1547ddd4cee3291240b10939375bd16763e`; 7005 | 7005; `8fc4ebd2a220155967a460465ac1a49f80273562bd6e0a9d5db09c3d2757d61c`; 0/101/0 |
| `.claude/commands/tfw-knowledge.md` | 7106; `1701035491afd0eb2558f9c0d818b5295bee247eb9443d1f394fc00ec09f0520`; 101/0/0 | `48b6a1547ddd4cee3291240b10939375bd16763e`; 7005 | 7005; `8fc4ebd2a220155967a460465ac1a49f80273562bd6e0a9d5db09c3d2757d61c`; 0/101/0 |
| `knowledge/records/TKL-20260913-01.md` | 3802; `affb020c75e91b5e1d90b06cb94ff4d838d09a4bc6239fc6d6681ba833ee27c7`; 38/0/0 | `c22dbcc910ccddf8c3a96c012cfa3bb3f4f257a8`; 3764 | 3764; `d13918a5d99569332a971d35dd56461565d27533463b20e4336cd3db2f20b7b0`; 0/38/0 |
| `tools/tests/test_tfw_state.py` | 15168; `3037ff3a31823374b2f34b883e8d3c0a5cc6267301005b092051080350a12e2d`; 362/0/0 | `c2beb0f1ac4468c0ca23d470d174a8ece241cc0b`; 14806 | 14806; `0ce88f3e7fa56ee2f328d93712298617d947f858cfeb45eaf3f4d93dd9072fac`; 0/362/0 |
| `tools/tests/test_tfw_doctor.py` | 7144; `0f4692285a1e2144e505d77ea24e726bd8e28ec704babb9cde3120f09d581104`; 187/0/0 | `7337605de47c47f51c7b29403c224d75d99be28c`; 6957 | 6957; `d9c2d0e0610ee5d0792391a8f8c6963695fa6c9c7cd71dabebc97ee904af6276`; 0/187/0 |
| `docs/scripts/test_repository_contracts.py` | 158854; `eb3b8c82a80e27df9a11bfd37214216b1add5573fef3aff5d02ad708eec73aa6`; 2963/0/0 | `39cc634adc264701063d22fe9ef4d09e21d9abfe`; 155891 | 155891; `d38b87acf020ffebaf5d0f5a06df4df026208c4080f7cd514e4c8782f74caabf`; 0/2963/0 |
| `docs/scripts/test_runtime_context.py` | 349128; `037444a785d6876f174679173414a4b7cd0ca2855c73eecc9d3861f71ea988b3`; 5993/0/0 | `8ed34b4b08d2cd15e4655dc1be99f861cba80729`; 343135 | 343135; `b79fa316708373cd9654d0018874f813adc35ce3ba349c7506c032fb3b9454de`; 0/5993/0 |
| `docs/scripts/test_update_experience.py` | 44600; `5ddb7e4ac43ed3511cf6f0d62c2be48364b3382f8a9af584c911faf45b1d14e8`; 824/0/0 | `1fe7e94ce132e2283316112291daae0c752d7363`; 43776 | 43776; `3dca74177301669346dedee52f792c5ab255bf0b3d4daf28270747e55ca3846d`; 0/824/0 |
| `docs/scripts/test_gen_docs.py` | 32959; `4351fa5a404173715199475464fa3c55245f3eaeb4e00de1c0f2f95ab9751d69`; 767/0/0 | `887c5c7cd3276dbe89ea21e6943db08f0c2b2c46`; 32192 | 32192; `43a52b5d9d1174b9f42dedb5296b7771a5a1c0a342d6524976d3d4ba6a5dcdcd`; 0/767/0 |
| `docs/scripts/test_integration.py` | 15224; `fd16bff8a8e0180412ed2b6f2cbfee3fbfe4ba8f3756336b33552d2f3b72579b`; 326/0/0 | `38bbf627814e981c4f5e850b41ba6b3e30d667bb`; 14898 | 14898; `2fac080974b063ab7a2cfdfd5b1d76ef24c00b173f2814a3eb9fc6e2a8659055`; 0/326/0 |

Coverage is bounded as follows. The seven test files are the seven exact pytest homes. The selected
adapter-copy and retired-rule cases cover the canonical `review`/`docs`/`knowledge` contracts and
their six installed copies. The selected TKL/state/doctor/runtime/generator/integration cases cover
the record's source/authority behavior, adoption/repeat/refusal behavior, and generated navigation.
The isolated MkDocs build consumes the current canonical documentation and record and exposes the
compiled link result. These checks cover the text semantics of the 18 dependencies at Candidate;
they do not convert the CRLF-versus-LF raw observer difference into a semantic claim or prove raw-EOL
preservation as a separate requirement.

## Lineage boundary

This receipt supports the already-issued result only: AC-7 is a cited correction, AC-8 is a cited
correction, and AC-11 depends on both. REVIEW §5 contains exactly three proposals, O1–O3. A future
AC-7 self-replay would be a separate native attempt beyond expired `0173`/`e5a1` bounds and requires
LEAD routing with its own receiver/source/cost clock before execution; the Reviewer recommendation
does not extend that bound.
