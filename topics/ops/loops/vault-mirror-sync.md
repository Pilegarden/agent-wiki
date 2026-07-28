# vault-mirror-sync recovery

- topic: `ops`
- queue ref: `topics/ops/.system/queue.md` `[LOOPS] vault-mirror-sync recovery`
- status: stale/phantom — Hermes cron absent despite earlier doc notes
- Claimed Job ID `87e93b77a514` is absent from all Hermes profile cron stores.
- Loop doc remains for history; current scheduler state provides no active cron with this ID.
- Per loops-factory policy, this loop is not recreated without an explicit `[LOOPS]` queue item or user direction.

## Phantom Status

- Claimed Job ID `87e93b77a514` is absent from all Hermes profile cron stores.
- **Phantom-loop audit** (2026-07-23 18:38 CEST): claimed Job ID absent from all profile `cron/jobs.json` files. Status: `phantom`.
- Per loops-factory policy, this loop is not recreated without an explicit `[LOOPS]` queue item or user direction.
- **Phantom-loop audit** (2026-07-27 04:51 CEST): claimed Job ID absent from all profile `cron/jobs.json` files. Status: `phantom`.
- **Phantom audit timestamp**: 2026-07-27 04:51 CEST
- **Live registry note**: `vault-mirror-sync` remains absent from all `~/.hermes/profiles/*/cron/jobs.json` stores; registry kept stale/phantom.
- **Last loops-factory tick**: 2026-07-27 04:51 CEST
