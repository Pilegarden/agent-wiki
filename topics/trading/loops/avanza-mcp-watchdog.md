# avanza-mcp-watchdog

- topic: `trading`
- queue ref: `topics/trading/.system/queue.md` `[LOOPS] avanza-mcp-watchdog`
- status: **stale/phantom** — claimed cron job ID `55c3a863d778` absent from all Hermes profile cron stores; prior recovery claim was incorrect
- cron job: none
- schedule: `0 * * * 1-5`
- deliver: `telegram:-1004376316450:8`
- profile: `dev`

## Scope

Hourly Avanza MCP hard-stop watchdog. Verifies `avanza_quote_helper.py` can fetch a quote for instrument `804998` and reports OK or FAIL.

## State

- status: stale/phantom
- last_status: none
- last_error: none
- failure_count: 0
- max_retries: 3
- pause_on_fail: false

## Phantom Status

- Job ID `55c3a863d778` absent from all Hermes profile cron stores as of 2026-07-27 09:58 CEST.
- Prior loops-factory tick (2026-07-27 09:01 CEST) incorrectly marked this loop as active/recovered; false recovery claim corrected.
- No open `[LOOPS]` queue item and no user direction to redeploy; cron NOT recreated per phantom-loop policy.
- Loop remains marked stale/phantom until explicit approval to redeploy.

## Loop Registry

- registry: `topics/_global/loop-registry.md`
- rows: `avanza-mcp-watchdog`
