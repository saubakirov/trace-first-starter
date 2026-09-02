#!/usr/bin/env python3
"""Reproduce the WCAG contrast checks for the rendered Assisted templates."""

from __future__ import annotations


RGB = tuple[int, int, int]


def color(value: str) -> RGB:
    return tuple(int(value[index : index + 2], 16) for index in (1, 3, 5))  # type: ignore[return-value]


def composite(foreground: RGB, alpha: float, background: RGB) -> RGB:
    return tuple(round(foreground[index] * alpha + background[index] * (1 - alpha)) for index in range(3))  # type: ignore[return-value]


def luminance(rgb: RGB) -> float:
    channels = []
    for raw in rgb:
        value = raw / 255
        channels.append(value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4)
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


def ratio(foreground: RGB, background: RGB) -> float:
    first, second = luminance(foreground), luminance(background)
    return (max(first, second) + 0.05) / (min(first, second) + 0.05)


WHITE = color("#FFFFFF")
A4_CASES = [
    ("A4 muted metadata", color("#52606D"), WHITE, 4.5),
    ("A4 blue heading", color("#334E68"), WHITE, 4.5),
    ("A4 primary heading", color("#243B53"), WHITE, 4.5),
    ("A4 body", color("#1F2933"), WHITE, 4.5),
    ("A4 body on quote", color("#1F2933"), composite(color("#D9E2EC"), 0.55, WHITE), 4.5),
    ("A4 body on light", color("#1F2933"), color("#F0F4F8"), 4.5),
    ("A4 table header", color("#111111"), color("#D9E2EC"), 4.5),
]

LIGHT_BOXES = [
    composite(color("#334E68"), 0.10, WHITE),
    composite(color("#27AE60"), 0.08, WHITE),
    composite(color("#D9E2EC"), 0.55, WHITE),
]
PRESENTATION_CASES = [
    ("Presentation muted", color("#555555"), WHITE, 4.5),
    ("Presentation heading", color("#243B53"), WHITE, 4.5),
    ("Presentation act-1 label", WHITE, color("#243B53"), 4.5),
    ("Presentation act-2 label", WHITE, color("#334E68"), 4.5),
    ("Presentation light-box heading", color("#243B53"), min(LIGHT_BOXES, key=lambda bg: ratio(color("#243B53"), bg)), 4.5),
    ("Presentation light-box body", color("#333333"), min(LIGHT_BOXES, key=lambda bg: ratio(color("#333333"), bg)), 4.5),
    ("Presentation table/quote", color("#111111"), color("#D9E2EC"), 4.5),
]

TITLE_STOPS = [color("#243B53"), color("#486581")]
PAUSE_STOPS = [color("#102A43"), color("#243B53"), color("#334E68")]


def worst_translucent_text(alpha: float, stops: list[RGB]) -> tuple[float, RGB, RGB]:
    cases = [(ratio(composite(WHITE, alpha, stop), stop), composite(WHITE, alpha, stop), stop) for stop in stops]
    return min(cases, key=lambda item: item[0])


def worst_tinted_box(foreground: RGB, tint: RGB, alpha: float) -> tuple[float, RGB, RGB]:
    cases = [(ratio(foreground, composite(tint, alpha, stop)), foreground, composite(tint, alpha, stop)) for stop in PAUSE_STOPS]
    return min(cases, key=lambda item: item[0])


def report(name: str, value: float, threshold: float) -> None:
    verdict = "PASS" if value >= threshold else "FAIL"
    print(f"{name}: {value:.2f}:1 (threshold {threshold:.1f}:1) {verdict}")
    if verdict != "PASS":
        raise SystemExit(1)


for case_name, foreground, background, threshold in A4_CASES + PRESENTATION_CASES:
    report(case_name, ratio(foreground, background), threshold)

report("Title-slide translucent ordinary text", worst_translucent_text(0.85, TITLE_STOPS)[0], 4.5)
report("Pause-slide translucent ordinary text", worst_translucent_text(0.78, PAUSE_STOPS)[0], 4.5)
report("Pause-slide white text on green tint", worst_tinted_box(WHITE, color("#27AE60"), 0.24)[0], 4.5)
report("Pause-slide white text on red tint", worst_tinted_box(WHITE, color("#E74C3C"), 0.24)[0], 4.5)
report("Pause-slide white code on neutral tint", worst_tinted_box(WHITE, WHITE, 0.14)[0], 4.5)
report("Pause-slide green large heading", worst_tinted_box(color("#7CE7A8"), color("#27AE60"), 0.24)[0], 3.0)
report("Pause-slide red large heading", worst_tinted_box(color("#FF9A8B"), color("#E74C3C"), 0.24)[0], 3.0)

light_index = ratio(color("#A8A8B4"), WHITE)
pause_index = worst_translucent_text(0.55, PAUSE_STOPS)[0]
print(f"Incidental slide index on light slide: {light_index:.2f}:1 (WCAG 1.4.3 incidental marker)")
print(f"Incidental slide index on pause slide: {pause_index:.2f}:1 (WCAG 1.4.3 incidental marker)")
print("CONTENT_CONTRAST=PASS")
