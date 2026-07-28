# trading/x-twitter-heartbeat

- topic: `trading`
- queue ref: `topics/trading/.system/queue.md` `[LOOPS] x-twitter-heartbeat`
- status: **removed** — cron job `e0260ed247a1` deliberately removed by user [Stop] 2026-07-27 16:06 CEST
|- cron job: ~~`e0260ed247a1`~~ (removed; no longer present in any Hermes profile cron store)
- cadence: Mon–Fri 10:00, 16:00
- deliver: `telegram:-1004376316450:8`
- profile: `dev`

## Scope

Periodic X/Twitter research digest. Fetches recent bookmarks, classifies against thesis taxonomy, reports new signals. Lightweight — no hoard writes, no unbookmarking, no brain-logging.

## Removal Note

Cron `e0260ed247a1` removed by user [Stop] 2026-07-27 16:06 CEST. Residual script `/home/hermes/.hermes/profiles/dev/scripts-local/x-twitter-heartbeat.sh` retained for investigation; investigation superseded.

## Loop Registry

- registry: `topics/_global/loop-registry.md`
