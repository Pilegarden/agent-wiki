# orm-mandate-reconciler

**Topic:** system/orm  
**Agent:** orm-governance-agent  
**Purpose:** Reconcile `topics/system/orm/README.md` and `topics/system/orm/.system/queue.md` against ISO 27001 doc changes and mandate diffs.  
**Schedule:** daily `0 9 * * *`  
**Deliver:** local  
**Mode:** cron  
**Profile:** dev

## Reads
- `topics/system/orm/README.md`
- `topics/system/orm/.system/queue.md`
- `topics/system/orm/skills/system-mandate-diff.md` if present
- `topics/system/orm/skills/system-orm-governance-review.md` if present

## Writes
- `topics/system/orm/.system/injections.md` short `UNREAD` block
- `topics/system/orm/loops/orm-mandate-reconciler.status` machine-readable status

## Behavior
1. Confirm queue `[LOOPS]` item `orm-mandate-reconciler` is the active reconciliation target.
2. Load `system-mandate-diff` skill. Identify current and prior ISO 27001 mandate revision snapshots.
3. Run mandate diff. If exit code is `1`, preserve line in `injections.md` and mark status `breaking`.
4. Load `system-orm-governance-review` skill. Surface added/removed/modified controls, owner gaps, evidence gaps, and modified objectives.
5. Append only new actionable items to `injections.md`.
6. Write `.status` with `state`, `timestamp`, `drift_file`, `anomalies`, `queue_item`.

- **Job ID**: `97aff819f7ca`
- **Created**: 2026-07-23 by loops-factory
Top-level keys in `orm-mandate-reconciler.status`:

| Key | Type | Notes |
|---|---|---|
| `state` | string | `ok`, `breaking`, `noop`, `error` |
| `timestamp` | string | ISO 8601 UTC |
| `drift_file` | string | Empty if no diff run |
| `anomalies` | integer | Governance review anomalies found |
| `queue_item` | string | Matches `.system/queue.md` LOOPS entry |
