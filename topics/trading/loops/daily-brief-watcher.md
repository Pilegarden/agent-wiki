# daily-brief-watcher

- topic: `trading`
- queue ref: `topics/trading/.system/queue.md` `[LOOPS] daily-brief-watcher`
- status: **active** — recovered 2026-07-22 by loops-factory
- cadence: Mon–Fri 06:30
- deliver: `local`
- model pin: not required (script-only loop)

## Scope

Lightweight guard around the daily brief artifact needed by Market Daily Snapshot.
Verifies `/home/hermes/.hermes/profiles/dev/market/daily-brief.md` exists and is non-empty before the daily market pipeline runs.

## Cron Details

```bash
hermes cron create \
  --name "daily-brief-watcher" \
  --repeat 999 \
  --deliver "local" \
  --workdir "/home/hermes" \
  --script "daily-brief-watcher.sh" \
  "30 6 * * 1-5" \
  "Run daily-brief-watcher and report status"
```

- **Claimed Job ID**: `cfa9d1137d7f`
- **Script**: `/home/hermes/.hermes/scripts/daily-brief-watcher.sh` (`755`)
- **Created**: 2026-07-15 by loops-factory; **recovered**: 2026-07-22 by loops-factory

## Recovery

- Recovered 2026-07-22 with Job ID `cfa9d1137d7f`.

## State

- last_status: ok
- last_error: none
- last_run: 2026-07-28 06:33 CEST

## Output

Stdout status line:
- 🟢 brief present
- 🔴 brief missing / empty

## Failure Mode

- Missing brief file → 🔴 local notification; cron continues
- Malformed/non-empty brief has no content validation beyond size 0

## Recover

Regenerate brief or reorder cron dependencies before Market Daily Snapshot if this job reports missing.
