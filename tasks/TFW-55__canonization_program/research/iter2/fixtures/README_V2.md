# TFW-55 Iteration 2 — Extract fixture v2

Status: **FROZEN FOR COORDINATOR REVIEW — NO CRITIC OR SCORER RUNS EXECUTED**

Normative design: `frozen_design.v2.json`

SHA-256: `d7fdb413af669abdf92cb3c055f7a966db3d4daec58d2ac15c36e679805f0f7a`

v2 supersedes the rejected-before-run v1. Its controls are:

- all eight external sources used by Gather/Extract are versioned in the registry; the Iteration-1 RES is a ninth internal baseline entry;
- six family-specific critic JSON schemas and six family-specific scorer JSON schemas are frozen;
- D9 is a surface-partitioned **mandatory agent-route** test. Each blind packet receives only its required route, contains P1–P6 exactly once, and has a mechanically verified load of 2493 UTF-8 bytes, 246 whitespace words, and two delivered surfaces. Human-side D9 is not tested;
- exposition is explicitly a **linear-ordering proxy**. It cannot select D7/D8 or trigger A3;
- the first full family pass is an adversarial probe. A material score/ambiguity/malformed difference forces one full-family replication with identical model/reasoning controls; selective reruns and third passes are forbidden;
- every critic output is evaluated in a separate isolated opaque scoring task. The scorer receives the opaque packet/output and relevant neutral answer key, but no internal mapping, frozen-HL preference, founder intent, or other variant;
- mapping is revealed only after every required critic and scorer pass for the family is complete;
- programmatic checks cover JSON/schema validity, labels, IDs/counts/enums, actual bytes/words/source units, D9 proposition coverage, exposition block coverage, and runtime input tokens when available.

No Challenge run is authorized until the coordinator closes the revised Extract gate. Any post-run change to packet, prompt, answer key, schema, rubric, label, order, scoring, or replication rule invalidates the full family and requires returning to Extract.
