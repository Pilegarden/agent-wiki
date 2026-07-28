---
name: cc-170-system-mandate-review
description: Reviews a target system's configuration, documentation, and operational evidence against the CC 170 system mandate to identify alignment gaps, conformance status, and remediation priorities. Designed for both tick-triggered automated reviews and ad-hoc human spot-checks.
tags:
  - compliance
  - cc-170
  - openclaw
  - governance
  - system-controls
  - audit
wiki_path: topics/openclaw/skills/cc-170-system-mandate-review.md
factory: skills-factory
created: 2026-07-23
---

# CC 170 System Mandate Review

Evaluate whether a target system's current state — configuration, documentation, and operational evidence — aligns with the CC 170 mandate requirements.

## Traits & Normative Definitions

This skill assumes that OpenCLAW traits and normative definitions are sourced from `SOUL.md` at review time. Do not hard-code or duplicate those definitions in this skill; inject them from the active personality context to remain consistent across OpenCLAW governance operations.

## Usage

### Tick-Triggered Review (Automated)

Used by scheduled or event-driven crawls to produce a standardized conformance snapshot.

**Input**
- Target system identifier or root path
- CC 170 mandate document path or reference
- `SOUL.md` trait context for the current evaluation cycle

**Process**
1. Ingest the CC 170 mandate and extract control clusters.
2. For each control, determine what system evidence satisfies it (config artifact, documented procedure, runtime telemetry, runbook).
3. Collect the evidence from the target system.
4. Map evidence to controls; record conformance status: `PASS`, `FAIL`, or `EVIDENCE MISSING`.
5. Aggregate into a conformity summary with a gap register.

### Human Spot-Check (Ad-Hoc)

Used when an operator wants a quick but structured alignment read without a full automated run.

**Process**
1. Select the specific control subset or risk domain to review.
2. Run a targeted evidence pull against that subset.
3. Present results as a sign-off checklist with explicit PASS/FAIL/UNKNOWN per control and a confidence statement.

## Output Schema

```yaml
review:
  target: ""
  mandate_version: ""
  conducted_at: ""
  mode: ["tick" | "spot-check"]
  traits_source: "SOUL.md"
  controls_total: 0
  controls_pass: 0
  controls_fail: 0
  controls_evidence_missing: 0
  gap_register:
    - control_id: ""
      status: "FAIL | EVIDENCE MISSING"
      rationale: ""
      recommended_remediation: ""
  evidence_map:
    - control_id: ""
      evidence_path: ""
      evidence_type: ["config" | "documentation" | "operational"]
      conformance_note: ""
  conformance_summary: ""
```

## Controlling Norms

- `SOUL.md` is the source of truth for OpenCLAW traits and normative language. Do not override or localize definitions.
- CC 170 mandate is the grading rubric; the target system's lived state is the object of evaluation.
- Both tick and spot-check modes must produce machine-parseable output so results can be ingested by dashboards or reports.
- A `FAIL` requires a rational evidence statement; a `PASS` requires a verifiable reference to the evidence artifact.

## Full Reference

Load the canonical Hermes skill via `skill_view(name='cc-170-system-mandate-review')`.
