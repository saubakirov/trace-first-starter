# Assisted 1.5 amended boundary and source attestation

- Product authority: amended HL `37b61d4`, approved TS `f4c676c`.
- Product checkpoint: `e27024bb782e7d95e1ef82c9ff7a80c51e411cf0`.
- Baseline census: 33 paths = 23 new / 7 modified / 3 deleted; 1838 changed LOC.
- Product executables: `editions/02-assisted/шаблоны/build_a4.py`; the sole file is the artifact builder. Removed identity and maintenance executables are absent.
- Static release authority: 29 rows; two regenerations and recorded rows are equal.
- Field source: 29 read-only rows; canonical pre/post `3a1885c65b13388a51ddaa5b1454122876d4f17d268bc49f0f94f6bb2dbee96b`; PowerShell/Python per-file row sets equal. Historical culture-sort aggregate `7e2248a7f7e77161644d8394b1557c731e0b5b31d7713843de30655b6e4fadc3` is retained as a different ordering convention, not source drift.
- External local tags are recorded per object and per contained task commit in `boundary-summary.json`: refs/tags/v2.0.0=5a72b2bd420922d640d4c7f7ed0bf4507e9285af contains_product=False; refs/tags/v2.0.0-dirty.5=cab7243737c68528d0a520d2d01e935ca585b022 contains_product=False. They are concurrent external state and stayed unchanged during this run. This task performed zero tag or push acts and did not rewrite either tag.
- Remote-tracking refs containing amended product checkpoint at capture: none.
- Every post-baseline commit whose subject names `TFW_20260830-114238_ASSISTED15` was audited: 27 commits, zero forbidden path hits = True. Owner-authorized config commit `f3eb986` is the explicit census baseline, not an Assisted product change. Concurrent dirty TFW-55/config state is external and was not staged.
- Earlier runtime/ACL/locking/terminal evidence is superseded by amendment A1 and is not counted for amended acceptance.
