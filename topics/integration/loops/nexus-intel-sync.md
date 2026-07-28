# nexus-intel-sync

**Topic:** integration
**Agent:** nexus-integration
**Job ID:** `da64be0fe62c`
**Purpose:** Verify intel platform connectivity/auth-rotation and surface a findings-only summary.
**Schedule:** daily `0 8 * * *`
**Deliver:** local
**Mode:** cron
**Profile:** nexus-integration

## Reads
- `topics/integration/README.md`
- `topics/_global/agents/nexus-integration.md`

## Writes
- `topics/integration/.system/injections.md` short `UNREAD` block
- `topics/integration/loops/nexus-intel-sync.status` machine-readable status

## Behavior
1. Load the agent definition and configured intel endpoints.
2. Verify reachability and auth-token freshness.
3. Append only new findings to `injections.md` under a compact `UNREAD` block; do not restate existing content.
4. Write `.status` as `OK` when all green, or `ANOMALY <count>` plus the check date when there are discrepancies.
## State

- status: **live/runtime-error** — profile `nexus-integration` is stopped; cron `da64be0fe62c` exists in nexus-integration profile cron store but has never executed. Created 2026-07-24, next_run was 2026-07-25 08:00 CEST; `last_run_at` is null.
- last_status: none
- last_error: none
- last_run: never
- failure_count: 0

## Recovery Note

Live cron exists in `~/.hermes/profiles/nexus-integration/cron/jobs.json` but the owning profile is `stopped`, so the job has not started. Root cause is profile activation, not job absence. Not phantom.
