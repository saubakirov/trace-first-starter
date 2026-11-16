"""Shared, read-only continuous GOAL grammar for state checks and economics."""
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

CONTRACT = "continuous-v1"
PREFIX = "<!-- tfw-goal-event "
PREPARING = {"TODO", "HL_DRAFT", "RES", "BLOCKED", "REJECTED"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, name, minimum=0):
    require(type(value) is int or isinstance(value, str) and
            re.fullmatch(r"0|[1-9][0-9]*", value), name + " must be an integer")
    number = int(value)
    require(number >= minimum, name + " is below its minimum")
    return number


def control_scalar(value):
    if value.startswith('"'):
        parsed = json.loads(value)
        require(isinstance(parsed, str), "control scalar must be text")
        return parsed
    if value.startswith("'"):
        require(re.fullmatch(r"'(?:[^']|'')*'", value), "invalid quoted scalar")
        return value[1:-1].replace("''", "'")
    require(not value.startswith(("&", "*", "|", ">", "[", "{")) and ": " not in value,
            "unsupported control scalar; quote a one-line value")
    return value


def control_fields(path):
    content = Path(path).read_text(encoding="utf-8")
    envelope = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.S)
    require(envelope, "control needs front matter: " + Path(path).name)
    fields, list_key = {}, None
    lines = iter(envelope[1].splitlines())
    pending = next(lines, None)
    while pending is not None:
        line, pending = pending, next(lines, None)
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        item = re.fullmatch(r"\s*-\s+(.+)", line)
        if item:
            require(list_key is not None, "unexpected control list")
            fields[list_key].append(control_scalar(item[1]))
            continue
        entry = re.fullmatch(r"([a-z_]+):(?:\s+(.*))?", line)
        require(entry and entry[1] not in fields, "unsupported or duplicate control field")
        key, value = entry.groups()
        if key in ("summary", "via", "actor") and value is not None:
            continuation = []
            while pending is not None and (not pending.strip() or pending.startswith(" ")):
                continuation.append(pending)
                pending = next(lines, None)
            if re.fullmatch(r"[|>][-+]?", value):
                nonblank = [s for s in continuation if s.strip()]
                require(nonblank, "empty control prose block")
                indent = min(len(s) - len(s.lstrip(" ")) for s in nonblank)
                prose = [s[indent:] if s.strip() else "" for s in continuation]
                fields[key] = ("\n" if value[0] == "|" else " ").join(prose)
                list_key = None
                continue
            value = " ".join([value, *(s.strip() for s in continuation if s.strip())])
        list_key = key if value is None else None
        fields[key] = [] if value is None else control_scalar(value)
    return fields


def validate_envelope(state):
    require(state.get("coordination_mode") == "goal" and
            state.get("goal_contract") == CONTRACT, "unknown continuous GOAL contract")
    require("goal_attempt" not in state, "continuous GOAL cannot carry goal_attempt")
    step = integer(state.get("goal_step"), "goal_step")
    require(state.get("lifecycle") not in ("TS_DRAFT", "PHASES"),
            "GOAL uses one task HL, never TS or phase dispatch")
    filename = "HL-" + str(state.get("id")) + ".md"
    require(state.get("authority") == filename, "GOAL authority must name its task HL")
    ref = state.get("goal_ref")
    require(ref is None and step == 0 and state.get("lifecycle") in PREPARING or
            isinstance(ref, str) and re.fullmatch(re.escape(filename) + r" @ [0-9a-f]{40}", ref),
            "continuous execution requires the task's immutable goal_ref")
    return step


def hl_limits(content, state):
    owner, task = re.escape(str(state.get("owner"))), re.escape(str(state.get("id")))
    require(re.match(r"^# HL\s+—\s+" + task + r"(?::|\s*$)", content, re.M),
            "goal_ref names another task's HL")
    require(len(re.findall(r"^> \*\*Contract\*\*:", content, re.M)) == 1 and
            re.search(r"^> \*\*Contract\*\*: 🔒 FROZEN — approved by " + owner +
                      r" \d{4}-\d{2}-\d{2}\s*$", content, re.M),
            "goal_ref needs its owner-frozen HL")
    names = ("Goal attempt limit", "Execution step limit", "Review maximum interval")
    values = {}
    for name in names:
        prefix = r"^> \*\*" + re.escape(name) + r"\*\*:"
        declarations = re.findall(prefix + r".*$", content, re.M)
        numbers = re.findall(prefix + r" ([1-9][0-9]*)\s*$", content, re.M)
        require(not declarations or len(declarations) == len(numbers) == 1,
                "HL needs one positive " + name)
        if numbers:
            values[name] = int(numbers[0])
    if state.get("goal_contract") == CONTRACT:
        require(set(values) == set(names[1:]), "continuous HL needs step/interval, no attempt limit")
        return dict(step_limit=values[names[1]], review_interval=values[names[2]])
    require("goal_contract" not in state and "goal_step" not in state and
            set(values) == {names[0]}, "historical HL needs only its attempt limit")
    return dict(attempt_limit=values[names[0]])


def _events(task, state):
    owners = (("journal/*.md", {"activation", "review_start"}),
              ("ONB__*.md", {"start", "check"}), ("evidence/EV*.md", {"start", "check"}),
              ("RF__*.md", {"rf"}), ("REVIEW__*.md", {"review"}))
    for pattern, kinds in owners:
        for path in sorted(task.glob(pattern)):
            for line in path.read_text(encoding="utf-8").splitlines():
                if not line.startswith(PREFIX):
                    continue
                require(line.endswith(" -->"), "malformed GOAL marker in " + path.name)
                event = json.loads(line[len(PREFIX):-4])
                require(isinstance(event, dict) and event.get("kind") in kinds,
                        "wrong GOAL event owner in " + path.name)
                if pattern.startswith("journal"):
                    carrier = control_fields(path)
                    name = re.fullmatch(r"(\d{8}-\d{6})__(\w+)__[a-f0-9]{4}\.md", path.name)
                    clock = datetime.fromisoformat(carrier.get("time", ""))
                    require(name and clock.utcoffset() is not None and
                            clock.strftime("%Y%m%d-%H%M%S") == name[1] and
                            name[2] == carrier.get("kind") and
                            carrier.get("on_behalf_of") == state.get("owner"),
                            "GOAL journal clock/kind/owner disagrees")
                    expected = {"activation": {"handoff", "gate_answer"}, "review_start": {"dispatch"}}
                    require(carrier.get("kind") in expected[event["kind"]] and
                            "goal_attempt" not in carrier, "wrong continuous journal carrier")
                    refs = carrier.get("refs")
                    require(isinstance(refs, list) and state["authority"] in refs,
                            "GOAL journal needs its authority ref")
                    for target in refs:
                        resolved = (task / target).resolve()
                        require(not Path(target).is_absolute() and
                                resolved.is_relative_to(task.resolve()) and resolved.is_file(),
                                "GOAL journal has missing or escaping reference")
                yield event


def continuous_progress(task, state, limits=None):
    """Check recorded progress; can_start requires ONB but never supplies role authority."""
    task = Path(task)
    completed = validate_envelope(state)
    require(state.get("id") == task.name, "continuous GOAL task/root mismatch")
    tables = {key: {} for key in ("activation", "start", "check", "rf", "review_start", "review")}
    base = {"review", "purpose", "step", "candidate", "goal_ref"}
    for event in _events(task, state):
        kind = event["kind"]
        keys = {"activation": {"goal_ref", "step_limit", "review_interval"},
                "start": {"step", "goal_ref"}, "check": {"step", "outcome"},
                "rf": base, "review_start": base, "review": base | {"verdict", "reviewer"}}[kind]
        require(set(event) == keys | {"kind"}, "unexpected continuous " + kind + " fields")
        if "goal_ref" in event:
            require(isinstance(event["goal_ref"], str) and re.fullmatch(
                re.escape(state["authority"]) + r" @ [0-9a-f]{40}", event["goal_ref"]),
                "event needs the task's immutable HL epoch")
        if kind == "activation":
            require(type(event["step_limit"]) is int and type(event["review_interval"]) is int,
                    "activation limits must be numeric")
            integer(event["step_limit"], "step limit", 1)
            integer(event["review_interval"], "review interval", 1)
            key = event["goal_ref"]
        elif kind in ("start", "check"):
            key = integer(event["step"], "step", 1)
            require(type(event["step"]) is int, "marker step must be numeric")
            if kind == "check":
                require(event["outcome"] in ("pass", "fail", "blocked"), "invalid step outcome")
        else:
            key = integer(event["review"], "review ID", 1)
            require(type(event["review"]) is int and type(event["step"]) is int,
                    "marker review and step must be numeric")
            integer(event["step"], "review step")
            require(event["purpose"] in ("interim", "final") and
                    isinstance(event["candidate"], str) and
                    re.fullmatch(r"[0-9a-f]{40}", event["candidate"]), "invalid review purpose/Candidate")
            if kind == "review":
                allowed = {"interim": {"CONTINUE", "REVISE", "REJECT"},
                           "final": {"APPROVE", "REVISE", "REJECT"}}
                require(event["verdict"] in allowed[event["purpose"]], "verdict contradicts review purpose")
                require(isinstance(event["reviewer"], str) and event["reviewer"].strip() and
                        event["reviewer"] != state.get("coordinator_route"),
                        "review needs its independent producer")
        table = tables[kind]
        require(key not in table or table[key] == event, "conflicting " + kind + " event " + str(key))
        table[key] = event

    epochs, starts, checks = (tables[k] for k in ("activation", "start", "check"))
    presentations, launches, reviews = (tables[k] for k in ("rf", "review_start", "review"))
    require(sorted(starts) == list(range(1, len(starts) + 1)), "step starts must be consecutive")
    require(sorted(checks) == list(range(1, len(checks) + 1)) and set(checks) <= set(starts),
            "step results need consecutive started steps")
    require(completed == len(checks), "goal_step disagrees with completed evidence; recover before advancing")
    require(len(starts) - completed in (0, 1), "resolve the pending step before starting another")
    active = epochs.get(state.get("goal_ref"))
    require(active or not starts and not presentations and state.get("lifecycle") in PREPARING,
            "continuous execution needs its bound activation")
    if active and limits is not None:
        require(all(active[k] == limits[k] for k in ("step_limit", "review_interval")),
                "activation limits disagree with frozen HL")
    require(sorted(presentations) == list(range(1, len(presentations) + 1)),
            "review presentations must have consecutive IDs")
    require(sorted(launches) == list(range(1, len(launches) + 1)) and
            set(launches) <= set(presentations) and set(reviews) <= set(launches),
            "review needs its presented and launched ID")
    producers, last_step = set(), 0
    for n, presented in sorted(presentations.items()):
        require(last_step <= presented["step"] <= completed and presented["goal_ref"] in epochs,
                "presentation has an unproved step/epoch or reversed order")
        last_step = presented["step"]
        for collection in (launches, reviews):
            if n in collection:
                require(all(collection[n][k] == presented[k] for k in base),
                        "review launch/return differs from presented Candidate, purpose, step or epoch")
        if n in reviews:
            producer = reviews[n]["reviewer"]
            require(producer not in producers, "every review launch needs a fresh independent context")
            producers.add(producer)
        require(n == len(presentations) or n in reviews, "resolve pending review before another presentation")
    for n, start in sorted(starts.items()):
        bound = epochs.get(start["goal_ref"])
        require(bound is not None and n <= bound["step_limit"], "step exceeds its activated HL limit")
        prior = [r for r in reviews.values() if r["step"] < n]
        last = max(prior, key=lambda r: r["review"], default=None)
        require(not last or last["verdict"] != "REJECT" or last["goal_ref"] != start["goal_ref"],
                "REJECT needs an owner-ruled epoch before more execution")
        last_valid = max((r["step"] for r in prior if r["verdict"] != "REJECT"), default=0)
        require(n <= last_valid + bound["review_interval"], "review interval exceeded before step " + str(n))
        require(not any(p["step"] < n and i not in reviews for i, p in presentations.items()),
                "resolve pending review before execution")
    pending = completed + 1 if len(starts) > completed else None
    pending_reviews = sorted(set(presentations) - set(reviews))
    current = max(reviews.values(), key=lambda r: r["review"], default=None)
    last_review = max((r["step"] for r in reviews.values() if r["verdict"] != "REJECT"), default=0)
    due = min(active["step_limit"], last_review + active["review_interval"]) if active else None
    if state.get("lifecycle") in ("RF", "REV", "KNW", "DONE"):
        require(not pending and presentations and last_step == completed,
                "presentation lifecycle needs completed current work")
    if state.get("lifecycle") in ("KNW", "DONE"):
        require(not pending_reviews and current and current["purpose"] == "final" and
                current["verdict"] == "APPROVE" and
                current["step"] == completed and current["goal_ref"] == state.get("goal_ref"),
                "closing needs current final APPROVE of step/HL and no pending review")
    return dict(contract=CONTRACT, started_steps=len(starts), completed_steps=completed,
                failed_steps=sum(x["outcome"] == "fail" for x in checks.values()),
                pending_step=pending, step_limit=active["step_limit"] if active else None,
                review_interval=active["review_interval"] if active else None,
                last_review_step=last_review, next_review_due=due,
                presentations=len(presentations), review_starts=len(launches),
                review_launches=[launches[n] for n in sorted(launches)],
                reviews=[reviews[n] for n in sorted(reviews)],
                pending_reviews=pending_reviews,
                can_start=bool(state.get("lifecycle") == "ONB" and active and not pending and
                               not pending_reviews and
                               completed < due and
                               (not current or current["verdict"] != "REJECT" or
                                current["goal_ref"] != state.get("goal_ref")))), checks

