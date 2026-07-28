# trading-watcher

- topic: `trading`
- agent: `trading-watcher` (profile at `~/.hermes/profiles/trading-watcher/`)
- status: **resolved/phantom** — superseded by `trading-infra-watcher` cron `b5aa5e1f418c`
- cadence: none
- deliver: none
- type: agent summary with no standalone deployed Hermes cron

## Scope

Portfolio health check cycle per trigger. Agent uses `/srv/trading/portfolio.json` + Avanza MCP live prices (`get_stock_quote` or `search_instruments`) and reports:

1. **Layer allocation drift** — L0–L4 allocations against targets (±5% tolerance)
2. **Data freshness** — NAV dates, snapshot timestamps (>24h flagged stale)
3. **Hard-stop breach** — `/srv/trading/kill_exit.json` active breaches
4. **Signal watchlist anomalies** — `/srv/trading/watchlist_signals.json` new/unresolved
5. **Rebalance calendar** — upcoming/past-due events

## Phantom Status

Claimed Job ID `5a1d4ea6796d` is absent from all Hermes profile cron stores. Previous loop-factory annotations incorrectly cited an active dev cron; live audit on 2026-07-27 04:51 CEST confirms the ID is not present anywhere.

Per loops-factory policy, this loop is not recreated without an explicit `[LOOPS]` queue item or user direction.
