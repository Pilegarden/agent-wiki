---
name: system-mandate-diff
description: Diff mandate document versions for drift tracking and governance review. Compares two versions of an ISO 27001 mandate or similar governance document and identifies inserted/removed/modified controls, objective changes, scope drift, and normative definition shifts. Outputs machine-parseable JSONL for dashboard ingestion and reconciliation loops. Use for tick-triggered reviews and human spot-checks.
tags:
  - governance
  - iso-27001
  - orm
  - compliance
  - diff
wiki_path: topics/system/orm/skills/system-mandate-diff.md
factory: skills-factory
created: 2026-07-23
---

# system-mandate-diff

Diff mandate document versions for drift tracking against ISO 27001 or similar governance references.

## When to Use
- Comparing two revisions of a mandate document (e.g., ISO 27001 revision snapshots, policy versions, control register updates)
- Detecting control drift between archived and current mandate versions
- Feeding structured diff results into dashboards or reconciliation loops
- Spot-checking normative changes in scope, objectives, or control definitions

## Inputs
- Old version path: filesystem path or URL to prior mandate document
- New version path: filesystem path or URL to current mandate document
- Context (optional): `--scope <control-domain>` to limit comparison to a specific control domain or annex

## Behavior
1. Read both versions completely.
2. Identify and compare:
   - Controls: inserted, removed, renamed, modified
   - Objectives: changes to stated objectives, targets, or metrics
   - Scope: additions, removals, or boundary shifts
   - Normative definitions: changes to terms, roles, or compliance thresholds that normally live in `SOUL.md`
   - Metadata: version identifiers, dates, authorship, approval status
3. Classify each change by impact: `breaking` | `minor` | `documentation`
4. Emit a machine-parseable JSONL report to stdout.

## Output Format

Default output is JSONL (`application/x-ndjson`), one JSON object per line:

```json
{"change_type":"control","action":"modified","id":"A.5.1","domain":"Access Control","impact":"minor","old":"...","new":"..."}
{"change_type":"control","action":"removed","id":"A.8.15","domain":"Asset Management","impact":"breaking","old":"..."}
{"change_type":"objective","action":"modified","id":"O.3","domain":"","impact":"minor","old":"...","new":"..."}
{"change_type":"scope","action":"added","id":"","domain":"","impact":"breaking","old":"","new":"Cloud services in scope"}
{"change_type":"normative","action":"modified","id":"soul.risk-first","domain":"","impact":"breaking","old":"2% portfolio","new":"1.5% portfolio"}
{"change_type":"metadata","action":"modified","id":"version","domain":"","impact":"documentation","old":"2024-v1","new":"2025-v2"}
```

### Field Definitions
- `change_type`: `control` | `objective` | `scope` | `normative` | `metadata`
- `action`: `added` | `removed` | `modified` | `renamed`
- `id`: control ID, objective ID, or logical identifier; empty string when not applicable
- `domain`: control domain or annex; empty string when cross-cutting
- `impact`: `breaking` | `minor` | `documentation`
- `old`: prior value excerpt (max 300 chars)
- `new`: current value excerpt (max 300 chars)

## Human-Readable Summary
Append `--summary` to print a compact report after JSONL:

```text
DRIFT REPORT: 2024-v1 → 2025-v2
Controls: +1 added, -2 removed, +3 modified (1 breaking)
Objectives: 2 modified
Scope: 1 addition (breaking: Cloud services)
Normative: 1 modification to soul.risk-first (breaking)
Metadata: version updated
Recommended review: 5 items flagged
```

## Scope Filtering
Limit comparison to a specific control domain or annex:

```bash
system-mandate-diff old.md new.md --scope "Access Control"
system-mandate-diff old.md new.md --scope "A.5"
```

## Reconciliation Loop Integration
For cron-driven reconciliation:
- Emit JSONL to a file: `system-mandate-diff old.md new.md > changes.jsonl`
- Check for `"impact":"breaking"` lines before proceeding
- Exit codes: `0` = changes found (non-breaking), `1` = breaking changes detected, `2` = diff error

## Notes
- Normative definitions in `SOUL.md` are compared by ID reference, not inline. If SOUL.md is the current mandate version, pass the SOUL.md path as `--new`.
- For ISO 27001:2022, controls are mapped to Annex A. For ISO 27001:2013, controls use A.x numbering. The skill detects revision families automatically and normalizes control IDs when possible.
- If both documents share the same version identifier, emit a single `metadata` warning line and exit 0.

## Example Invocation

```bash
# Compare ISO 27001 snapshots
system-mandate-diff iso27001-2024.md iso27001-2025.md > drift.jsonl

# Filter for breaking changes only
system-mandate-diff iso27001-2024.md iso27001-2025.md | jq 'select(.impact == "breaking")'

# Spot-check summary
system-mandate-diff iso27001-2024.md iso27001-2025.md --summary
```

## Pitfalls
- Do not compare documents with different paragraph styles or heading depths without pre-normalization; line-based diffs produce noise.
- Normative changes in `SOUL.md` should reference the exact principle or rule ID, not prose excerpts, so reconciliation loops can key off stable identifiers.
- JSONL output must not contain trailing commas or embedded newlines; truncate `old`/`new` values to 300 chars.

## Full Reference

Load the canonical Hermes skill via `skill_view(name='system-mandate-diff')`.