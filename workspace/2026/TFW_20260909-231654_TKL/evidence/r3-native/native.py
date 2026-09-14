"""Single pinned R3 native attempt. Finite evidence driver; no receiver runtime installation."""
import ast
import datetime as dt
import hashlib
import html
import json
import os
from pathlib import Path, PurePosixPath
import re
import runpy
import secrets
import subprocess
import sys
import tarfile
import traceback
import zipfile

HERE = Path(__file__).resolve().parent
TASK = HERE.parent.parent
SOURCE = TASK.parents[2]
RECEIVER = Path("C:/Users/c0rpa/AppData/Local/Temp/TFW_TKL_NATIVE_01a09a0c/self-adoption-r3")
BASELINE = "ec91c56007c20cda79f740fec15c85e4af74d17c"
CANDIDATE = "a99ba6cd756a7db444f217aef4e5a0eb83faee51"
PIN = "22c75aae5ce1a0a6aed5a7b867277a304dd3ee6e"
DEADLINE = dt.datetime.fromisoformat("2026-09-13T22:43:37+00:00")
OBSERVER = TASK / "evidence/r3-preflight/observer.py"
assert hashlib.sha256(OBSERVER.read_bytes()).hexdigest() == "515fa7513171ba663f784982df23a994e3052370081381022cdf808fd0e5dd48"
observe = runpy.run_path(str(OBSERVER))["observe_bytes"]
GIT = ["git", "-c", "core.longpaths=true", "-c", "core.autocrlf=false"]
STEP = sys.argv[1] if len(sys.argv) > 1 else ""
DETAIL = {"step": STEP, "started_at": dt.datetime.now(dt.timezone.utc).isoformat(), "argv": sys.argv, "subprocesses": [], "writes": []}

def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def read(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))

def save(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

def bound():
    assert dt.datetime.now(dt.timezone.utc) < DEADLINE, "native deadline"
    assert not (HERE / "STOP.json").exists(), "attempt already stopped"

def call(argv, cwd=SOURCE, label=None):
    bound()
    label = label or f"{STEP}-{len(DETAIL['subprocesses']) + 1}"
    out, err = HERE / f"{label}.stdout.raw", HERE / f"{label}.stderr.raw"
    record = {"argv": list(map(str, argv)), "cwd": str(cwd), "start": now(), "stdout": out.name, "stderr": err.name}
    DETAIL["subprocesses"].append(record)
    env = os.environ.copy()
    env.update(PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1", DISABLE_MKDOCS_2_WARNING="true")
    remaining = (DEADLINE - dt.datetime.now(dt.timezone.utc)).total_seconds()
    with out.open("wb") as stdout, err.open("wb") as stderr:
        result = subprocess.run(list(map(str, argv)), cwd=cwd, env=env, stdout=stdout, stderr=stderr, timeout=max(1, remaining - 90))
    record.update(end=now(), exit=result.returncode)
    assert result.returncode == 0, f"subprocess failed: {label}, exit {result.returncode}"
    return out.read_bytes()

def git(*args, cwd=SOURCE):
    return call([*GIT, *args], cwd)

def safe(name):
    p = PurePosixPath(name)
    return bool(name) and not p.is_absolute() and ".." not in p.parts and "\\" not in name and ":" not in name

def guard():
    bound()
    for path, identity in read("03-current-pins.json").items():
        assert observe((SOURCE / path).read_bytes()) == identity, f"source/authority drift: {path}"
    # Historical rows remain bound to immutable content-addressed objects and the pinned schema.
    assert git("rev-parse", "HEAD").decode().strip() == PIN
    schema = json.loads((TASK / "evidence/r3-preflight/03-source-authority-target.json").read_text(encoding="utf-8"))
    return schema

def files():
    assert RECEIVER.exists() and RECEIVER.is_dir() and not RECEIVER.is_symlink(), "receiver root type/existence"
    assert RECEIVER.resolve() == RECEIVER, "receiver root resolves elsewhere"
    found = []
    for current, dirs, names in os.walk(RECEIVER, topdown=True, followlinks=False):
        directory = Path(current)
        if directory == RECEIVER:
            dirs[:] = [x for x in dirs if x != ".git"]
        for name in dirs + names:
            q = directory / name
            rel = q.relative_to(RECEIVER).as_posix()
            assert safe(rel) and q.resolve().is_relative_to(RECEIVER), f"unsafe physical path: {rel}"
            assert not q.is_symlink() and not (getattr(q.lstat(), "st_file_attributes", 0) & 0x400), f"reparse path: {rel}"
        for name in names:
            q = directory / name
            assert q.is_file(), str(q)
            found.append(q)
    assert found, "empty receiver is not success"
    return sorted(found)

def physical():
    return {p.relative_to(RECEIVER).as_posix(): observe(p.read_bytes()) for p in files()}

def stable():
    guard()
    actual = physical()
    expected = read("expected-current.json")
    assert set(actual) == set(expected), "unexpected physical membership"
    assert actual == expected, "unexpected physical bytes"
    return actual

def set_expected(value=None):
    save("expected-current.json", value if value is not None else physical())

def write_receiver(rel, data, purpose):
    bound()
    assert safe(rel), rel
    path = RECEIVER / rel
    assert path.resolve().is_relative_to(RECEIVER), rel
    before = observe(path.read_bytes()) if path.exists() else None
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    after = observe(path.read_bytes())
    assert after == observe(data), rel
    DETAIL["writes"].append({"path": rel, "purpose": purpose, "before": before, "after": after, "at": now()})

def zip_tree(path, mapping):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED, compresslevel=1) as z:
        for rel in sorted(mapping):
            z.write(RECEIVER / rel, rel)

def git_metadata(name):
    with zipfile.ZipFile(HERE / name, "w", zipfile.ZIP_DEFLATED, compresslevel=1) as z:
        for q in sorted((RECEIVER / ".git").rglob("*")):
            if q.is_file():
                z.write(q, q.relative_to(RECEIVER).as_posix())

def prepare():
    guard()
    assert not RECEIVER.exists() and not RECEIVER.is_symlink(), "root exists; refusing reuse"
    common = git("rev-parse", "--git-common-dir").decode().strip()
    common = (SOURCE / common).resolve()
    git("clone", "--no-checkout", "--shared", str(common), str(RECEIVER))
    git("checkout", "--detach", BASELINE, cwd=RECEIVER)
    checkout = physical()
    save("06-checkout-map.json", checkout)
    expected = read("03-positive-map.json")
    extras = set(checkout) - set(expected)
    assert extras <= {".tfw/templates/knowledge_state.yaml"}, sorted(extras)
    for rel in extras:
        target = (RECEIVER / rel).resolve()
        assert target.is_relative_to(RECEIVER) and target.is_file()
        before = observe(target.read_bytes())
        target.unlink()
        DETAIL["writes"].append({"path": rel, "purpose": "faithful positive-epoch fixture; positive file absent", "before": before, "after": None, "at": now()})
    archive = TASK / "evidence/r2-native/06-partial-physical.zip"
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == "7ac460d99dbf9c39ca51d969ae03292d6652d2b6584c227fe2e8d45d795b2f42"
    with zipfile.ZipFile(archive) as z:
        names = [x.filename for x in z.infolist() if not x.is_dir()]
        assert len(names) == len(set(names)) == 2317 and set(names) == set(expected)
        for name in sorted(names):
            assert safe(name)
            data = z.read(name)
            assert observe(data) == expected[name], name
            write_receiver(name, data, "hydrate sealed positive-epoch fixture")
    actual = physical()
    assert len(actual) == 2317 and actual == expected
    save("06-positive-physical-map.json", actual)
    set_expected(actual)
    git_metadata("06-git-metadata.zip")
    DETAIL["result"] = {"repository_files": 2317, "exact_positive_map": True, "new_target_effects": 0}

def stage():
    schema = guard()
    stable()
    archive = HERE / "07-candidate.tar"
    git("archive", "--format=tar", f"--output={archive}", CANDIDATE)
    staging = RECEIVER / ".tfw/.upstream"
    assert not staging.exists(), "staging must be absent in prepared positive repository"
    staged = {}
    with tarfile.open(archive, "r:") as tar:
        for item in tar.getmembers():
            if item.isdir():
                continue
            assert item.isfile() and safe(item.name), item.name
            data = tar.extractfile(item).read()
            rel = ".tfw/.upstream/" + item.name
            write_receiver(rel, data, "exact Candidate source staging, not installed product")
            staged[item.name] = observe(data)
    assert staged
    for row in schema["sources"]:
        if row["commit"] == CANDIDATE:
            assert staged[row["path"]]["sha256"] == row["sha256"], row["path"]
    import yaml
    cfg = yaml.safe_load((RECEIVER / ".tfw/project_config.yaml").read_text(encoding="utf-8"))
    assert cfg["tfw"]["installed_from"] == schema["targets"][3]["old_installed_from"]
    assert (staging / ".tfw/VERSION").read_text(encoding="utf-8").strip() == "3.3.0"
    required = [".tfw/workflows/update.md", ".tfw/migrations/3.3.0.md", ".tfw/migrations/knowledge-lifecycle.md", ".tfw/adapters/manifest.yaml", ".tfw/templates/update_receipt.md", ".tfw/templates/briefing.md"]
    for rel in required:
        assert (staging / rel).read_bytes() == git("show", CANDIDATE + ":" + rel)
    changelog = (staging / ".tfw/CHANGELOG.md").read_text(encoding="utf-8")
    pos = changelog.find("3.3.0")
    assert pos >= 0
    save("07-source-routing.json", {"version": "3.3.0", "untagged": True, "configured_upstream": cfg["tfw"].get("upstream"), "installed_from_before": cfg["tfw"]["installed_from"], "required_source_paths": required, "changelog_equal_version_excerpt": changelog[max(0, pos - 100):pos + 7000], "configured_checks": cfg.get("build"), "source_files": staged, "current_receipts": [x for x in read("03-positive-map.json") if x.startswith(".tfw/update_receipts/")], "old_SLC_TKL_mechanics": "Accepted positive epoch and R1 evidence reused; no old migration replay"})
    set_expected()
    DETAIL["result"] = {"staging_files": len(staged), "staging": str(staging), "tag_claim": False}

def target_bytes(row):
    rel = row["path"]
    old = (RECEIVER / rel).read_bytes()
    if rel == ".tfw/project_config.yaml":
        before = row["old_installed_from"].encode()
        after = row["intended_installed_from"].encode()
        assert old.count(before) == 1
        intended = old.replace(before, after)
    else:
        intended = (RECEIVER / ".tfw/.upstream" / rel).read_bytes()
    assert observe(old) == row["verified_old_identity"], rel
    assert observe(intended) == row["verified_intended_identity"], rel
    return old, intended

def preserve():
    schema = guard()
    before = stable()
    intent = {"candidate": CANDIDATE, "pin": PIN, "receiver": str(RECEIVER), "source_authority_schema": "dd6dfe034ee4ab6a0c1d32300f81ce038ea7f381f6ec9e592c2cc1cb68655c8e", "targets": schema["targets"], "positive_map_sha256": hashlib.sha256((HERE / "03-positive-map.json").read_bytes()).hexdigest()}
    encoded = json.dumps(intent, sort_keys=True, ensure_ascii=False).encode("utf-8")
    address = hashlib.sha256(encoded).hexdigest()
    base = ".tfw/update_receipts/knowledge-lifecycle/" + address
    assert not (RECEIVER / base).exists()
    archive = HERE / "08-old-intended.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=1) as z:
        for row in schema["targets"]:
            old, intended = target_bytes(row)
            z.writestr("old/" + row["path"], old)
            z.writestr("intended/" + row["path"], intended)
        for rel in read("03-positive-map.json"):
            if rel == ".tfw/knowledge_state.yaml" or rel.startswith("knowledge/") or rel in ["README.md", ".tfw/README.md"]:
                z.writestr("preserved/" + rel, (RECEIVER / rel).read_bytes())
    write_receiver(base + "/intent.json", encoded, "immutable content-addressed intent")
    write_receiver(base + "/old-intended.zip", archive.read_bytes(), "complete old/intended and state/legacy bytes")
    write_receiver(base + "/positive-map.json", (HERE / "03-positive-map.json").read_bytes(), "complete old positive repository identity")
    save("08-preservation.json", {"address": address, "base": base, "intent": observe(encoded), "old_intended_zip": observe(archive.read_bytes()), "source_authority": read("03-current-pins.json"), "before_map_files": len(before), "knowledge_state": "present" if ".tfw/knowledge_state.yaml" in before else "explicitly absent", "purpose_operation": "README and current .tfw/README are unchanged in this affected R3 scope; original positive purpose designation and attachment retained"})
    set_expected()

def effect(index):
    schema = guard()
    before = stable()
    preserve_info = read("08-preservation.json")
    base = RECEIVER / preserve_info["base"]
    assert observe((base / "intent.json").read_bytes()) == preserve_info["intent"]
    assert observe((base / "old-intended.zip").read_bytes()) == preserve_info["old_intended_zip"]
    row = schema["targets"][index]
    old = (RECEIVER / row["path"]).read_bytes()
    assert observe(old) in [row["verified_old_identity"], row["verified_intended_identity"]]
    with zipfile.ZipFile(base / "old-intended.zip") as z:
        intended = z.read("intended/" + row["path"])
        assert observe(intended) == row["verified_intended_identity"]
    guard()
    assert observe((RECEIVER / row["path"]).read_bytes()) == before[row["path"]]
    if old != intended:
        write_receiver(row["path"], intended, "authorized current-description effect" if index < 3 else "single installed_from provenance scalar")
    after = physical()
    expected = dict(before)
    expected[row["path"]] = row["verified_intended_identity"]
    assert after == expected
    set_expected(after)
    DETAIL["result"] = {"path": row["path"], "identity": after[row["path"]], "unrelated_preserved": True, "physical_writes": int(old != intended)}

def module_ast(data):
    tree = ast.parse(data.decode("utf-8"))
    if tree.body and isinstance(tree.body[0], ast.Expr) and isinstance(tree.body[0].value, ast.Constant) and isinstance(tree.body[0].value.value, str):
        tree.body.pop(0)
    return ast.dump(tree, include_attributes=False)

def check():
    schema = guard()
    stable()
    for row in schema["targets"][:3]:
        assert observe((RECEIVER / row["path"]).read_bytes()) == row["verified_intended_identity"]
    assert observe((RECEIVER / ".tfw/project_config.yaml").read_bytes()) == schema["targets"][3]["verified_old_identity"]
    with zipfile.ZipFile(RECEIVER / read("08-preservation.json")["base"] / "old-intended.zip") as z:
        assert module_ast(z.read("old/tools/tfw_state.py")) == module_ast((RECEIVER / "tools/tfw_state.py").read_bytes())
    knowledge = (RECEIVER / "KNOWLEDGE.md").read_text(encoding="utf-8")
    row = next(line for line in knowledge.splitlines() if line.startswith("| Task Storage |"))
    assert "Knowledge Gate" not in row and "task_containers" in row
    conv = (RECEIVER / ".tfw/conventions.md").read_text(encoding="utf-8")
    a = conv.index("### Where tasks live")
    b = conv.find("\n### ", a + 1)
    section = conv[a:b if b >= 0 else len(conv)]
    assert "Knowledge Gate" not in section and "ordinary current-work selection" in section
    old = read("03-positive-map.json")
    actual = physical()
    protected = {k: v for k, v in old.items() if k not in {r["path"] for r in schema["targets"]}}
    assert all(actual[k] == v for k, v in protected.items())
    selected = [k for k in old if k.startswith((".agents/", ".claude/", ".agent/"))]
    assert all(actual[k] == old[k] for k in selected)
    # Read the previously used compatibility expectation as evidence; do not run or install a test oracle.
    test_path = SOURCE / "docs/scripts/test_integration.py"
    text = test_path.read_text(encoding="utf-8")
    tree = ast.parse(text)
    node = next((n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "test_tkl_five_reviewed_fragment_occurrences_reach_existing_exact_ids"), None)
    compatibility = ast.get_source_segment(text, node) if node is not None else "Exact named function absent; current two-page native observation uses its own bounded source/HTML checks."
    save("12-source-check.json", {"current_task_storage": row, "current_where_tasks_live": section, "non_docstring_AST_equal": True, "preserved_repository_paths": len(protected), "unchanged_selected_adapter_paths": selected, "compatibility_expectation_read": compatibility, "source_test_executed": False})
    DETAIL["result"] = {"checks": "three intended files, old config, AST and complete other positive repository identities", "compatibility_expectation_read": compatibility}

def build():
    stable()
    save("13-build-input-map.json", physical())
    site = RECEIVER / "site"
    assert not site.exists()
    call([sys.executable, "-m", "mkdocs", "build", "-f", "docs/mkdocs.yml", "--site-dir", str(site)], RECEIVER, "13-build")
    after = physical()
    before = read("expected-current.json")
    assert all(after[k] == v for k, v in before.items())
    added = {k: v for k, v in after.items() if k not in before}
    assert added and all(k.startswith("site/") or "__pycache__" in k for k in added)
    save("13-build-output-map.json", added)
    set_expected(after)
    DETAIL["result"] = {"site": str(site), "files": len(added), "existing_inputs_preserved": True, "builds": 1}

def text_only(value):
    return " ".join(html.unescape(re.sub(r"<[^>]*>", " ", value)).split())

def output():
    stable()
    site = RECEIVER / "site"
    k = site / "knowledge-index/index.html"
    c = site / "reference/conventions/index.html"
    kh, ch = k.read_text(encoding="utf-8"), c.read_text(encoding="utf-8")
    rows = re.findall(r"<tr\b[^>]*>.*?</tr>", kh, re.S)
    matching = [x for x in rows if "Task Storage" in text_only(x)]
    assert len(matching) == 1
    ktext = text_only(matching[0])
    assert "Knowledge Gate" not in ktext and "task_containers" in ktext
    heading = re.search(r'<h([1-6])\b[^>]*id="where-tasks-live"[^>]*>', ch)
    assert heading
    end = re.search(r"<h[1-" + heading.group(1) + r"]\b", ch[heading.end():])
    segment = ch[heading.start():heading.end() + end.start()] if end else ch[heading.start():]
    ctext = text_only(segment)
    assert "Knowledge Gate" not in ctext and "ordinary current-work selection" in ctext
    observation = {"opened": [k.relative_to(site).as_posix(), c.relative_to(site).as_posix()], "current_task_storage": ktext, "where_tasks_live": ctext, "source_epoch": "Prepared positive receiver plus three actual Candidate description effects", "module_docstring": "Source/AST only; not compiled by this docs pipeline", "cleanup": "Retain exact source staging and one-build site for independent inspection; no recursive delete"}
    # Additional exact fragment occurrences are supplied as finite source-grounded selection, never a test transplant.
    selections = HERE / "14-fragment-selection.json"
    if selections.exists():
        checks = []
        with zipfile.ZipFile(HERE / "14-opened-pages.zip", "w", zipfile.ZIP_DEFLATED) as z:
            pages = {k.relative_to(site).as_posix(), c.relative_to(site).as_posix()}
            for row in read("14-fragment-selection.json"):
                page = site / row["source"]
                destination = site / row["target"]
                source_html = page.read_text(encoding="utf-8")
                target_html = destination.read_text(encoding="utf-8")
                assert row["href"] in source_html, row
                assert ('id="' + row["id"] + '"') in target_html, row
                checks.append({**row, "source_identity": observe(page.read_bytes()), "target_identity": observe(destination.read_bytes()), "resolves": True})
                pages.update([row["source"], row["target"]])
            for name in sorted(pages):
                z.write(site / name, name)
        observation["fragment_checks"] = checks
    else:
        with zipfile.ZipFile(HERE / "14-opened-pages.zip", "w", zipfile.ZIP_DEFLATED) as z:
            z.write(k, k.relative_to(site).as_posix())
            z.write(c, c.relative_to(site).as_posix())
        observation["unchanged_fragment_evidence"] = "Prior accepted unchanged R1 destination mechanics reused under D86; only actual affected current pages observed in this step."
    save("14-output.json", observation)
    DETAIL["result"] = observation

def provenance():
    assert read("13-build.step.json")["exit"] == 0
    assert read("14-output.json")["cleanup"].startswith("Retain")
    effect(3)

def receipt():
    stable()
    schema = guard()
    for row in schema["targets"]:
        assert observe((RECEIVER / row["path"]).read_bytes()) == row["verified_intended_identity"]
    timestamp = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    attempt = "UPDATE__" + timestamp.strftime("%Y%m%d-%H%M%S") + "__" + secrets.token_hex(2)
    rel = ".tfw/update_receipts/" + attempt + ".md"
    assert not (RECEIVER / rel).exists()
    preservation = read("08-preservation.json")["base"]
    content = f"""---
kind: update_receipt
attempt_id: {attempt}
recorded_at: {timestamp.isoformat()}
writer: robert
---

# Update Receipt — {attempt}

## 1. Pinned source and receiver

Receiver: {RECEIVER}. Baseline Git checkout {BASELINE}, hydrated from the accepted positive R1 repository epoch, exactly 2317 files.
Source: configured upstream https://github.com/saubakirov/trace-first-starter, explicitly authorized untagged Candidate {CANDIDATE}, locally materialized with git archive.
Target workflow: .tfw/.upstream/.tfw/workflows/update.md at that Candidate. Version remains 3.3.0; no release tag is claimed.
Attempt began 2026-09-13T22:13:37Z; this record is sealed at {timestamp.isoformat()}.

## 2. Authority and semantic groups

robert, same Executor 01a09a0c-c9e2-7d01-af4e-64931af967ed, acts for saubakirov.
Sole Coordinator 01a09974-6716-7cc0-9916-fd6d04c91481 dispatched exact pin {PIN} under LEAD grant a54fa27cb9fd7aa78000e586fd3922b2c9e40cd4.
Governing task TFW_20260909-231654_TKL; unchanged approved TS and Candidate. The connected group is three current descriptions plus their new installed_from provenance. No material question remains for this bounded observed group.
Independent task acceptance remains the same Reviewer and Coordinator; this receipt grants none.

## 3. Decision and effects

Applied: .tfw/conventions.md current Where tasks live clauses (26), tools/tfw_state.py module description (55), KNOWLEDGE.md Task Storage row (57).
Applied after checks/output: one tfw.installed_from scalar in the customized 4420-byte .tfw/project_config.yaml (56/58), ending at {CANDIDATE}.
Complete actual old/intended files, state/legacy bytes and original map: {preservation}/old-intended.zip, intent.json and positive-map.json.
Preserved: all other positive repository files, project README/current purpose designation, knowledge/state/markers, histories, selected adapters, custom version/container/build/owner choices and prior receipts.
Purpose operation: preserve bytes; current .tfw/README.md is outside the changed R3 description group. Its original positive designation and source references remain unchanged.
Skipped: all unchanged payload/adapter/migration groups; D86 reuses accepted R1 selection/order/authority/algorithms/SLC/cuts/refusal. No upstream task/team/knowledge memory was installed as product.
Refused: none in this completed affected application. Earlier R2 STOP is retained externally, not retried or erased.

## 4. Verification

| Check | Result | Artifact |
|---|---|---|
| Source integrity and provenance | VERIFIED | Pinned current source/authority rows, Candidate staging map and four intended identities |
| Receiver state/config exclusions | VERIFIED | Complete positive and per-effect before/after maps; immutable preservation above |
| Connected-group consistency | VERIFIED | Three current descriptions, unchanged non-docstring AST, one config scalar after output |
| Adapter/runtime surface | VERIFIED | Every selected positive adapter path unchanged; accepted unchanged mechanics reused |
| Maintainer checks | N/A | Source/configured suite already independently accepted; this grant forbids replay |
| Receiver proof | VERIFIED for this bounded application | One actual MkDocs build/raw streams and opened affected HTML; exact intended config |

The unchanged completed repeat is the next separate observation; this receipt does not claim it happened before sealing.
This finite prepared receiver proves no arbitrary interruption, universal recovery, production deployment or human comprehension.

## 5. Cleanup, continuation, and final-message input

Cleanup disposition was observed before sealing: retain {RECEIVER}/.tfw/.upstream and {RECEIVER}/site for independent inspection; both have complete diagnostic maps. No destructive cleanup was needed.
Unresolved material items at sealing: unchanged repeat and independent AC7/AC11 sufficiency remain subsequent observations.
Next authoritative action: same Executor performs the one authorized zero-write repeat, seals evidence and returns to sole Coordinator, then the same independent Reviewer judges.
Final message delivery at receipt time: planned/not-yet-observed.
Final message inputs: the three observed description corrections, preserved custom/history bytes, provenance, actual output and explicit evidence limits.
Attachments: {preservation}; external task evidence/r3-native maps, raw command streams and opened pages.
"""
    write_receiver(rel, content.encode("utf-8"), "immutable template-complete attempt receipt after cleanup disposition")
    save("16-receipt.json", {"path": rel, "identity": observe(content.encode("utf-8")), "sealed_at": now(), "delivery_at_seal": "planned/not-yet-observed", "repeat_at_seal": "not yet observed"})
    # Outcome rendering is separate from and never rewrites the receipt or receiver.
    (HERE / "16-outcome.md").write_text(f"""# Результат обновления TKL

В изолированном receiver исправлены три текущих описания и обновлена ссылка installed_from на Candidate {CANDIDATE}.
Пользовательские настройки, история, состояние знаний и выбранные адаптеры сохранены. Одна сборка и фактически открытые страницы проверены.
Source staging и site оставлены для проверки. Неизменный повтор ещё предстоит; окончательная независимая оценка AC7/AC11 остаётся открытой.
Источник результата: {rel}. Доставка и понимание человеком не утверждаются.
""", encoding="utf-8", newline="\n")
    set_expected()
    DETAIL["result"] = read("16-receipt.json")

def repeat():
    before = stable()
    schema = guard()
    for row in schema["targets"]:
        assert observe((RECEIVER / row["path"]).read_bytes()) == row["verified_intended_identity"]
    rec = read("16-receipt.json")
    assert observe((RECEIVER / rec["path"]).read_bytes()) == rec["identity"]
    preservation = read("08-preservation.json")
    assert observe((RECEIVER / preservation["base"] / "old-intended.zip").read_bytes()) == preservation["old_intended_zip"]
    guard()
    after = physical()
    assert before == after
    assert not DETAIL["writes"]
    save("17-repeat-before.json", before)
    save("17-repeat-after.json", after)
    save("17-repeat-result.json", {"started_at": DETAIL["started_at"], "completed_at": now(), "result": "UNCHANGED", "files": len(after), "physical_receiver_writes": 0, "completed_repeat_count": 1, "new_receipt_or_build": False, "same_source_authority_intent_effect_provenance_receipt": True})
    DETAIL["result"] = read("17-repeat-result.json")

def seal():
    final = stable()
    assert read("17-repeat-result.json")["result"] == "UNCHANGED"
    save("18-final-map.json", final)
    zip_tree(HERE / "18-final-physical.zip", final)
    git_metadata("18-final-git-metadata.zip")
    source = {k: v for k, v in final.items() if k.startswith(".tfw/.upstream/")}
    derived = {k: v for k, v in final.items() if k.startswith("site/") or "__pycache__" in k}
    repository = {k: v for k, v in final.items() if k not in source and k not in derived}
    save("18-inventory.json", {"source_staging": source, "derived": derived, "repository_and_receipts": repository, "all_files": len(final), "git_metadata": "18-final-git-metadata.zip", "physical_archive": observe((HERE / "18-final-physical.zip").read_bytes())})
    save("18-native-result.json", {"outcome": "SUCCESS for the bounded affected-native application and one unchanged repeat", "candidate": CANDIDATE, "pin": PIN, "start": "2026-09-13T22:13:37Z", "deadline": DEADLINE.isoformat(), "sealed_at": now(), "new_target_effects": 4, "repeat": read("17-repeat-result.json"), "receiver": str(RECEIVER), "files": len(final), "source_staging_files": len(source), "derived_files": len(derived), "repository_receipt_files": len(repository), "no_old_receiver_access": True, "no_retry": True, "deductions_seconds": 0, "next": "Commit and return within the same native bound, then no further receiver actions."})
    DETAIL["result"] = read("18-native-result.json")

COMMANDS = {"prepare": prepare, "stage": stage, "preserve": preserve, "effect26": lambda: effect(0), "effect55": lambda: effect(1), "effect57": lambda: effect(2), "check": check, "build": build, "output": output, "provenance": provenance, "receipt": receipt, "repeat": repeat, "seal": seal}
LABELS = {"prepare": "06", "stage": "07", "preserve": "08", "effect26": "09", "effect55": "10", "effect57": "11", "check": "12", "build": "13", "output": "14", "provenance": "15", "receipt": "16", "repeat": "17", "seal": "18"}
try:
    bound()
    COMMANDS[STEP]()
    DETAIL.update(exit=0, completed_at=now())
except BaseException as exc:
    DETAIL.update(exit=1, completed_at=now(), error=type(exc).__name__, message=str(exc), traceback=traceback.format_exc())
    save("STOP.json", DETAIL)
finally:
    save(LABELS.get(STEP, "unknown") + "-" + STEP + ".step.json", DETAIL)
    print(json.dumps({k: v for k, v in DETAIL.items() if k not in ["writes", "subprocesses"]}, ensure_ascii=False))
if DETAIL["exit"]:
    sys.exit(1)

