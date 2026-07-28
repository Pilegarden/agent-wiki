---
name: system-orm-governance-review
description: "Audits ISO 27001 control text against a reusable task-structure checklist for system/orm governance reviews. Use when doing tick-triggered control coverage scans, human spot-checks, or diffing ISO revision snapshots against current ORM tasks."
tags:
  - governance
  - iso-27001
  - orm
  - compliance
  - audit
wiki_path: topics/system/orm/skills/system-orm-governance-review.md
factory: skills-factory
created: 2026-07-23
---

# System ORM Governance Review

Tagline: `extract → checklist → coverage`

Normative definitions (`control`, `objective`, `task`, `evidence`) live in SOUL.md.
This skill maps; it does not redefine the terms.

## Checklist Template

```markdown
# ISO 27001 Review Snapshot
_Reference: system/orm_
_Generated: <timestamp>_

| Control ID | Objective | Task Type | Owner | Cadence | Evidence Path | Status |
|---|---|---|---|---|---|---|
|             |            |           |       |         |               |        |
```

## Parse Rules

1. **Input scope.** Accept ISO 27001 control text as Markdown, PDF, or pasted excerpt.
   Drop annex-only content unless the user explicitly scopes the review to that annex.
2. **Extract control ID and objective.** One control ID per row; objective shortened to
   one sentence. If no ID is present, mark the row `UNMAPPED_SOURCE`.
3. **Sort.** Order rows by control ID within domain groups (A.5–A.18).

## Task-Type Definitions

- `implement` — configure, build, or deploy the control.
- `check` — collect evidence artifact this cycle.
- `verify` — prove the control operates correctly in this environment.
- `maintain` — recurring task; assign a `Cadence` and start date.
- `accept_exception` — approved risk acceptance; must include owner and expiry date.

## Status Ladder

`planned | in_flight | done | overdue | n/a`

## Coverage Rules

- Every control in scoped ISO text gets exactly one row.
- `Orphaned task` = a `system/orm` task that does not map to any control in this
  snapshot. Mark its control cell `UNMAPPED_SOURCE`.
- `Evidence gap` = Evidence Path is blank or does not point to an existing artifact.
  Mark `missing` in the Evidence column; append `/MISSING`.

## Diff Snapshot

Compare this snapshot to the most recent saved snapshot at system/orm:

- **Added controls** — rows in this run absent from last snapshot.
- **Removed controls** — rows in last snapshot absent from this run.
- **Owner gaps** — rows where Owner is blank.
- **Evidence gaps** — rows where Evidence contains `missing`.
- **Modified controls** — same Control ID, changed objective text or task type.

## Invocation

- **cron / tick.** Run `extract` → fill checklist → append
  `/system/orm/review-<YYYY-MM-DD>.md`. One append per tick; never overwrite.
- **human spot-check.** Open the latest snapshot, run the verify column only.
- **post-revision.** Diff current snapshot against prior snapshot; surface only delta
  rows; assign owners on anomalies.

## Verification

Exit only when all of the following hold:

- Every row contains a control ID or is marked `UNMAPPED_SOURCE`.
- Coverage run produces exactly one row per control in the input scope.
- Every evidence path is validated for existence or marked `missing`.
- Diff output reproduces when rerun against the same pair of snapshots.

## Full Reference

Load the canonical Hermes skill via `skill_view(name='system-orm-governance-review')`.