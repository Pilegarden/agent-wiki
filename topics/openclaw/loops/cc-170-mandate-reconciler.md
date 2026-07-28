# cc-170-mandate-reconciler

**Topic:** openclaw  
**Agent:** openclaw-system-agent  
**Purpose:** Reconcile `topics/openclaw/README.md` and `topics/openclaw/.system/queue.md` against CC 170 mandate doc changes.  
**Schedule:** daily `0 9 * * *`  
**Deliver:** local  
**Mode:** cron  
**Profile:** dev

## Reads
- `topics/openclaw/README.md`
- `topics/openclaw/.system/queue.md`
- `/home/hermes/.hermes/wiki/topics/openclaw/skills/cc-170-system-mandate-review.md` if present

## Writes
- `topics/openclaw/.system/injections.md` short `UNREAD` block
- `topics/openclaw/loops/cc-170-mandate-reconciler.status` machine-readable status

## Behavior
1. Load the README, queue, and optional CC 170 review skill.
2. Identify mandate-side deltas that are missing or stale in the topics doc/queue.
3. Append only new actionable items to `injections.md` under a compact `UNREAD` block; do not restate existing content.
4. Write `.status` as `OK` when deltas are empty, or `DELTA <count>` plus the check date when there are discrepancies.
## Notes

- **Job ID**: `f9aefeca065b`
- **Created**: 2026-07-23 by loops-factory
- **Next run**: 2026-07-24 09:00 CEST
- Keep the loop doc concise and executable.
