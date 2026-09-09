# Evidence index — TFW_20260907-133942_PTTC / Phase B

Candidate `edf6d8261b12451c3ceb3cb5a9a6244bc3b47d1c`; Baseline `982a41841bea4cff2e253a98d6e0db008a7f7194`. Actual same-Executor source is on `codex/pttc-phase-b-exec`; native holder identities and exact producer commits are retained in the linked records. [RF](../RF__phase-b__finite_closure_and_recovery.md) and [EV](EV__phase-b__finite_closure_and_recovery.md) own claims and their limits.

## Reading order

1. Approved [TS](../TS__phase-b__finite_closure_and_recovery.md), [ONB](../ONB__phase-b__finite_closure_and_recovery.md), then real RF/EV. Formal Reviewer forms its own real phase judgment.
2. `accounting-*`, `candidate-commit.json`, `candidate-source-audit.json` and `phase-b-final-source-audit.json` establish immutable membership, chronology, source equality and original seals.
3. Command families01–05 each contain actual receipt/argv, pre-run source SHA256 manifest, stdout/stderr and observer events. Families04/05 also retain actual MkDocs streams. Original failures remain alongside the final successful source epoch.
4. Raw native input ZIP/manifest, both separately sealed initial responses, Coordinator actions and final independent Reviewer follow-up distinguish the six actual cases and epochs. Read their stated limits before interpreting snapshots.
5. `phase-b-command-ledger.json` carries the full prospective/measured envelope and pending final root command. Source and snapshot audits are not independent semantic verdicts.

## Immutable native sources

| Role/source | Producer / meaning |
|---|---|
| Raw input package | `76567803ff865bce74da34d664121809d31ec807`; ZIP SHA256 b9b4a2612a03d6f2056b6f75ed9f0bd623db196ca9241cf5139db7f2d892234f |
| Coordinator initial | `68950f8d8062dea0e5db38369e2a1dee8cdbf532`; SHA2565ca956882b5856ff436cfbb187e5dcb0f9bcb0d37b127b2819f11e394babf759 |
| Reviewer initial | `8c45f518e22d650464d8530cdcceb31cf2075e35`; SHA256801fbf198a192d26d390997ba6faaac2e7a942bc7679343d8c87a97e738363a0 |
| Profile correction | `e47a8921c69e7b20c03e0f6e10860f19733cd445`; explicit two-file synthetic completion after both seals |
| B1 action | `f22a659b28e26963955fe23fa1c7c7c0b92218e3`;141→142file working snapshots |
| B2 preparation | `24e27d4e67f414fffed0cd249b9c67044fd8ee13`; clean/damaged checks and 140-file damaged snapshot |
| B2 corrected RF return | `25c89cb65a140f1d83e734246fc2c91d7fc38772`; one corrected check and 146-file return snapshot |
| B2 final close | `8bfaebe2d185c1af39c7118fc7230e030df2ce34`; 148-file closed snapshot after separate actual approval/KNW |
| B5 setup | `015c7d4b4b8f2aad6be9ba8d8c9f03006ffdfe26`; 141-file synthetic epoch with exact unrelated NOTE |
| B5 final close | `4e04e2c04444a2ac0342a721e626ba56c254d488`; 142-file closed snapshot |
| Final native Reviewer | `13c8322c2321c4db11a68434ec2de02f27294ba6`; SHA256 0b460a49135e895bb59f54cd9f5a8e80b6ee7f12c75973e78af3d4b2d1aed5d6; bounded native completion, not formal real B APPROVE |

Both initial Markdown byte streams equal their immutable Git objects and remain unchanged; no extra response archive was needed. B3/B4/B6 paired ZIPs are copies of original raw input, explicitly not live captures or extra behavioral evidence. Final source audit verifies packaging equality only; the Reviewer did not inspect those reused pairs.

## Byte identity and reproduction

Git `core.autocrlf=input` can normalize text CRLF to LF. The table distinguishes raw working SHA256 from Git content identity; a raw-text SHA mismatch after checkout is not silently claimed as equality. `phase-b-original-captures.zip` preserves 47 original command/JSON/helper/NUL captures with RAW-MANIFEST and exact raw stream bytes; its SHA256 is 049de4cbb2aa14f53ada9c99e4caf9fa1b9880079d1501f4a29c497ee735e6ec. Native receipts additionally encode original stream and before/after bytes as base64. Binary ZIP/NUL bytes are retained unchanged. Use the raw archive for original bytes and the actual producer Git blob for normalized repository text.

`support-accounting.ps1` carries the original approved 25-literal-path PowerShell array and unchanged NUL-safe argv. `support-capture.py` and `support-pttc_b_observer.py` document sender capture only. The receiver's check is the plain PowerShell file in its preserved snapshots; no sender history/runtime is imposed on receiver operation. Do not rerun old failed commands to reconstruct already captured evidence.

The inventory below excludes this self-referencing index. Its Git IDs are computed for the exact current file contents under repository filters and become reachable with the return commit. Later formal review/capture/landing records may append new evidence; they cannot relabel an old failure or retrospective state.

## Complete attachment inventory

| Attachment | Raw working SHA256 | Git content identity |
|---|---|---|
| [01-pure.events.jsonl](01-pure.events.jsonl) | `b865d04a1044504b78ca9fcb27fe89dad08e76a538c9c8e4a185d1392120917b` | `7982518761ae1e3d96721ef8007ad2baa8b29679` |
| [01-pure.receipt.json](01-pure.receipt.json) | `729b877d724f3275fcf4030ccaced62403c944ecc4b7a14414b3509532af0551` | `82282dbed569dfb5b818ca3a37252da1ebc70c8f` |
| [01-pure.sources.json](01-pure.sources.json) | `ae0dffa434463f168fe0f83fd2450730d4ca8c091bb2581f3391bc54ad768295` | `89203f51efc0348e8e6846557fc7c26b6c899b9f` |
| [01-pure.stderr.txt](01-pure.stderr.txt) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` |
| [01-pure.stdout.txt](01-pure.stdout.txt) | `58a043ee3dbfead65336dee53b15a710b57d4e4c9f1eb657c7c8fee56512f1ea` | `2fd9d954efc35461742553b42ad5ed230209e880` |
| [02-correction.events.jsonl](02-correction.events.jsonl) | `668cf93045de2fb2c78fd2203b111f96334bdf50e7f5aeb0e5dad4b9d694ea15` | `eedad359027705759a2173a2064aa968ba1dfc4b` |
| [02-correction.receipt.json](02-correction.receipt.json) | `29125a1bff6522aab15e913c5ee9cf3c48e9c3edc6c80b0b7e686dc293099f80` | `f65044cf1d1ea3ffb30f878cd873a3884e845148` |
| [02-correction.sources.json](02-correction.sources.json) | `c45e61661911fd36dd6415b28a55e80e78912256369bc207d66caf3fac9008e2` | `b9d2fa6dd10dbe5cd6938ea118607c225401f0c9` |
| [02-correction.stderr.txt](02-correction.stderr.txt) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` |
| [02-correction.stdout.txt](02-correction.stdout.txt) | `d08bbbcc6c0ee87c722a9715545a9335b163cca86b37c9dd6879268b6e613712` | `33305d375656316bbba8ea2bd280ee039d167e57` |
| [03-collection.events.jsonl](03-collection.events.jsonl) | `54031bc811063ea7867969df8c51b47b107380d5ed3733442016a67642bc6d20` | `02e87a855583aa6de7ef4d1f98fa21ff8b64d833` |
| [03-collection.receipt.json](03-collection.receipt.json) | `9454c57bc0166f0ba1c35dff2280ff18907a0a9012f303c280407a902ec5ca05` | `6fb2474bd8801f549192a510dc88a31810869a68` |
| [03-collection.sources.json](03-collection.sources.json) | `c45e61661911fd36dd6415b28a55e80e78912256369bc207d66caf3fac9008e2` | `b9d2fa6dd10dbe5cd6938ea118607c225401f0c9` |
| [03-collection.stderr.txt](03-collection.stderr.txt) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` |
| [03-collection.stdout.txt](03-collection.stdout.txt) | `3cf09d70079f2c0a35a362a7057d8c6a71f8113357f9fbb3d071882031af9992` | `f8b96318bdd02a94178da3d349f4b3d96cd99d1b` |
| [04-full.events.jsonl](04-full.events.jsonl) | `563b8bcf75c3a727cce68359b46cb7400044eb049e8a71b1fd0f3b689a15b939` | `02f21a30e4b46f09fe3b120b5b32a7fccfcd6103` |
| [04-full.mkdocs-50824.stderr.txt](04-full.mkdocs-50824.stderr.txt) | `599216b9978f29204b3b09815dc828e4fd1115ce53a3614e2724f7a10536ecd0` | `bd0b87ce3187966aaf2f07bb716c23a7a0034a72` |
| [04-full.mkdocs-50824.stdout.txt](04-full.mkdocs-50824.stdout.txt) | `9f38572273b18f71e8b2be78d42b542a5ffdcec73ffea6ba156a6c17753f539e` | `a8e240a4d9496163c99c99d5c1f99fdfa2ec00a3` |
| [04-full.receipt.json](04-full.receipt.json) | `aa22865be9ffb64c5cef7654e0ef94b5a2ef687dcacd1b05533769165269a873` | `4c0aef580ea2856a0703639c3051ca8101b556bc` |
| [04-full.sources.json](04-full.sources.json) | `c45e61661911fd36dd6415b28a55e80e78912256369bc207d66caf3fac9008e2` | `b9d2fa6dd10dbe5cd6938ea118607c225401f0c9` |
| [04-full.stderr.txt](04-full.stderr.txt) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` |
| [04-full.stdout.txt](04-full.stdout.txt) | `e4b2296c1e0309e9ef2f3c10f7cb9f159f9081402f7b52c94b62dbe669e4e004` | `15594381440b603dcef68cf82dc325190dd4210c` |
| [05-full-corrected.events.jsonl](05-full-corrected.events.jsonl) | `9f43349b6275a8c257ec19ff04dae8aa4cdd4c9f01cede3c9150a8922a63cdd5` | `9edd09060d96dbb397a8f6eba7cb60189098ce21` |
| [05-full-corrected.mkdocs-42772.stderr.txt](05-full-corrected.mkdocs-42772.stderr.txt) | `1c5f549e1417a8c1081a8ff808dc58ef95519699647e3eefa1ff2babe9fbf3b4` | `13f1682c7a4099efdcbcd9d349cf9a4c7f1828d1` |
| [05-full-corrected.mkdocs-42772.stdout.txt](05-full-corrected.mkdocs-42772.stdout.txt) | `9f38572273b18f71e8b2be78d42b542a5ffdcec73ffea6ba156a6c17753f539e` | `a8e240a4d9496163c99c99d5c1f99fdfa2ec00a3` |
| [05-full-corrected.receipt.json](05-full-corrected.receipt.json) | `3241b075c9c47e272dd7b7c346b5afe56c859e5a8c94d8b8f838d40280adfef1` | `860b288eeca02161147a217cc538e93998066e5a` |
| [05-full-corrected.sources.json](05-full-corrected.sources.json) | `45ae56d07d05ce96bcbf3cf22b4e07f8f46efca05e8fb4f54333296fcf4c8138` | `104f811c3371e566e9b0d5c2b6d205d06e14f5b2` |
| [05-full-corrected.stderr.txt](05-full-corrected.stderr.txt) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` |
| [05-full-corrected.stdout.txt](05-full-corrected.stdout.txt) | `40106831a0ef2178bd737544c74f0d86a18bee743543b42a611dbbd0bba1ce80` | `8c59d19e76a958dfbd82ec43842dffe02ae67213` |
| [EV__phase-b__finite_closure_and_recovery.md](EV__phase-b__finite_closure_and_recovery.md) | `e96873007de0a81ac9cfd109bf6ad54eabf8890ac4dbc3279c03d7b0c79e3878` | `035fc1353355c570b7284d9f0e1aa930e34c5dc2` |
| [accounting-inputs.json](accounting-inputs.json) | `93966c8667a2b62a665f6bdbe103ade2320b179ad177c930d45ca7cea3cff256` | `404f0e569c6889fdbc2ccf93a06e7f7644be8acd` |
| [accounting-name-status.nul](accounting-name-status.nul) | `aa9a27dd17710903a192a71b31103d9a1fb80ae908bbb1df5ca21e48ed09af2c` | `e1c6d887a7d9dbaca570f99c3205241de40aab87` |
| [accounting-numstat.nul](accounting-numstat.nul) | `ed9e41c898530cb543b47b2e28726b65d196c9ba702985c16eedf2808226ddb6` | `7087363e63d009bf7f278835934d9d1e2cb2d686` |
| [accounting-result.json](accounting-result.json) | `0ca68fdc4fd6ce3cf5a2c617d9c58bd92d2ac985c61eb16f1afee894c424aeb6` | `33e1b67c20c3548246b2c4c9aef3d8d203739519` |
| [candidate-commit.json](candidate-commit.json) | `9cbe3738ed925aa138a602c382275a91a5629e953b6d50a90eadc203e67864c9` | `fba8236c50aba042f1b9203727066b93c468ca24` |
| [candidate-source-audit.json](candidate-source-audit.json) | `cca9040312f74a569acb8955c275f873de9ed48da639339a7ba3ffdff35a3dad` | `f0e3816ef9e4d8f03a2c83bf0d08bae45595137a` |
| [control-merge-after-candidate.json](control-merge-after-candidate.json) | `289c5a6d3da19b9736cad74710b9282bdb418e760ee322365bfcefae1b868cda` | `874b93e5c2b9470346800fce7aeff1d77333ac60` |
| [native-B1-after.zip](native-B1-after.zip) | `858bae58c42e55061e6a200c10b2e879961a57ac62a1dd2374495f685d4472a0` | `6dbb75f8420347e4993b74b16477c1275a81fc5b` |
| [native-B1-before.zip](native-B1-before.zip) | `da8fa2daf1a55a3a5c64997a7a1bad272367c55fbab2979e0d4985796c025af7` | `2ccf11e75ce8204c83681325af394fc3071e4325` |
| [native-B2-after.zip](native-B2-after.zip) | `444fe9ac471ae9602426b2883efe0d5fe7ea86ad8fa38d9fc431b23cd065fa79` | `1ce6df1983686b418a23c3989a94ba1f810e58b0` |
| [native-B2-before.zip](native-B2-before.zip) | `3d9624cc487afa8c7171bc5a89c636d2b42685c66fa53ad1162aff019b9750be` | `42c2df1701fdc7585411e50cccde03c593c81d39` |
| [native-B2-corrected-return.zip](native-B2-corrected-return.zip) | `2e689beb375c20166dbe881372fba67bc2edac6c0a4235b0cc947d13c4903ae6` | `9baaa5209985ff9c4c2ad2db8d281e4de74c9354` |
| [native-B2-correction.json](native-B2-correction.json) | `1e5a430eba656bd9e0e1c85c0a3ff93c7ed59d1adea5176e8822eaf917952a32` | `c1cc09f440a12bf1280edd30a87bbc59b69d5106` |
| [native-B2-preparation.json](native-B2-preparation.json) | `aa07be0f4fc69818ca223ad67628fe11b6ed408f7993b4a290a499d00923405e` | `ee443e80b63920c88b7eb802567453a58748291d` |
| [native-B3-after.zip](native-B3-after.zip) | `b9b4a2612a03d6f2056b6f75ed9f0bd623db196ca9241cf5139db7f2d892234f` | `cb025b2001e28cf4fffdbd194a9ece1f14e2499e` |
| [native-B3-before.zip](native-B3-before.zip) | `b9b4a2612a03d6f2056b6f75ed9f0bd623db196ca9241cf5139db7f2d892234f` | `cb025b2001e28cf4fffdbd194a9ece1f14e2499e` |
| [native-B4-after.zip](native-B4-after.zip) | `b9b4a2612a03d6f2056b6f75ed9f0bd623db196ca9241cf5139db7f2d892234f` | `cb025b2001e28cf4fffdbd194a9ece1f14e2499e` |
| [native-B4-before.zip](native-B4-before.zip) | `b9b4a2612a03d6f2056b6f75ed9f0bd623db196ca9241cf5139db7f2d892234f` | `cb025b2001e28cf4fffdbd194a9ece1f14e2499e` |
| [native-B5-after.zip](native-B5-after.zip) | `4b88d26905015599adb47595c98eb82e8908c720294c5ef905a893052aabe982` | `45e41f6df2214c5161a51c5413d65e984beccc1e` |
| [native-B5-before.zip](native-B5-before.zip) | `ca8c2d59e66f238afcf511068b081c862180d6dd7fe59567dfd4061c1c06a7e4` | `7e2eac7cc21b66371bf24de429964a8d10183a0a` |
| [native-B5-setup.json](native-B5-setup.json) | `9e053a553ffeae60c2e0356648528bfab8cf11cb1cb5b78aa23c8d6c205558ae` | `5dc5109900110fb8807c0b7a20ab8497a88dbb54` |
| [native-B6-after.zip](native-B6-after.zip) | `b9b4a2612a03d6f2056b6f75ed9f0bd623db196ca9241cf5139db7f2d892234f` | `cb025b2001e28cf4fffdbd194a9ece1f14e2499e` |
| [native-B6-before.zip](native-B6-before.zip) | `b9b4a2612a03d6f2056b6f75ed9f0bd623db196ca9241cf5139db7f2d892234f` | `cb025b2001e28cf4fffdbd194a9ece1f14e2499e` |
| [native-coordinator-actions.md](native-coordinator-actions.md) | `5245e1fd8991bd2c48d3a0ddd08b3a8df4ae0bfa95b3e6782cb0d6916878d6a7` | `41d3f321753c29a91b1f3b1a3c13b175a4dcad88` |
| [native-coordinator-initial.md](native-coordinator-initial.md) | `5ca956882b5856ff436cfbb187e5dcb0f9bcb0d37b127b2819f11e394babf759` | `0fa27c9b4e23bf219b3f11aedd66dd07b750d286` |
| [native-profile-preparation-correction.json](native-profile-preparation-correction.json) | `9e3eb197fa6e80f5f74dba2a2101aeef12366e51290e7880595bfd53c905ea7b` | `4563ec9d8dc8268b666b55bd10029624e50436c6` |
| [native-reviewer-followup.md](native-reviewer-followup.md) | `0b460a49135e895bb59f54cd9f5a8e80b6ee7f12c75973e78af3d4b2d1aed5d6` | `b87f6490a9d27f58ec4ba46d5d65e2ca38f9afd5` |
| [native-reviewer-initial.md](native-reviewer-initial.md) | `801fbf198a192d26d390997ba6faaac2e7a942bc7679343d8c87a97e738363a0` | `bb2450afb8d363b67296098bc91053ebf7a82320` |
| [phase-b-command-ledger.json](phase-b-command-ledger.json) | `055b18be93053aba2cacef137d74bf1bb1313d562b557b5cd669eb3cab0e0b2a` | `786883a22ac164822a2b90a587717f1d8d411be0` |
| [phase-b-failed-source.zip](phase-b-failed-source.zip) | `f9da62a8d36f148c019b1379a6df7aa869fa292defe5162e1f24b37c0078ae73` | `859ca046e5f7c2ea8724f04179e96565fe1fe7e0` |
| [phase-b-final-source-audit.json](phase-b-final-source-audit.json) | `f5717eb5129cbef5a75ab884ff204fa56dfa92e1ac871cf810fdeabeaa342418` | `e2f483ba0f6c545b4d516c68daa0ee76032c5791` |
| [phase-b-installation.json](phase-b-installation.json) | `24477b48b6ea643e653cde25490e52243cf58f47117e8c08103826898bb6e90e` | `6d4cd98adc1e87e848a04d3e8ee2e4d687babc30` |
| [phase-b-native-inputs.json](phase-b-native-inputs.json) | `9c75c703449306a665ba93afdcd4f42f09940c46e366f0e2a25fe16806f6d668` | `358cd42ff0d49f35d384da7ff7df2c6370febeb6` |
| [phase-b-native-inputs.zip](phase-b-native-inputs.zip) | `b9b4a2612a03d6f2056b6f75ed9f0bd623db196ca9241cf5139db7f2d892234f` | `cb025b2001e28cf4fffdbd194a9ece1f14e2499e` |
| [phase-b-original-captures.zip](phase-b-original-captures.zip) | `049de4cbb2aa14f53ada9c99e4caf9fa1b9880079d1501f4a29c497ee735e6ec` | `d8ddf21bc2f21df939dd00f8e946aec158773930` |
| [phase-b-readiness.json](phase-b-readiness.json) | `017983f8b18945578330cbd284c3ace5baee59ef8c2dd67a4ecaafcaac84142d` | `8060390bb02512a340e80093376186383392a9e1` |
| [rf-return-validation.json](rf-return-validation.json) | `8c60d7cdcc81196a545d6eca8181a0e2e2d46eb3473b7b179e7855ee47652a89` | `80637153524468e9716c9e53ccff1ed1c32e45eb` |
| [rf-staging.json](rf-staging.json) | `2239b56f0d73a4d076b492e5d92483a7417e897b0b1fcc72664cafea694517c2` | `9adac074d1942b81b64d9bc34c3e96cd06613146` |
| [support-accounting.ps1](support-accounting.ps1) | `6e204cd7086913f7c45bda04b34ce86bc42e3b92b9e3d12d9af27e2e7f44c133` | `7f173ee7069990e1a129fac469946056171ae109` |
| [support-capture.py](support-capture.py) | `261c8912fc9a941913d5f856ef889d85862d7a9a7dac534009f2683a58421b5a` | `3601202bfb952a12e0c5cb68b91f182af2919c95` |
| [support-pttc_b_observer.py](support-pttc_b_observer.py) | `84e16d2c715b7fa4f631883b81996b3b3e0a312882db71a90e94e0c683aaa6a4` | `58705bbc141f3b608afd1c2de7ae5c023224ccc7` |
| [trace-package-staging.json](trace-package-staging.json) | `897402e76af676780faa7dea54f77ad7bb9eea8d295e0263306f03b217316cf6` | `3b3e23d48fe3afe0493580c6b7865014bd93213a` |
