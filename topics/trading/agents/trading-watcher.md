# trading-watcher

- topic: `trading`
- agent: `trading-watcher`
- status: **resolved/superseded** — duplicate claim of trading-infra-watcher job `5a1d4ea6796d`; superseded by trading-infra-watcher loop. No standalone cron deployed for this agent.
- summary: Cron-based portfolio monitor for ISK/TJP. Single purpose: read `/srv/trading/portfolio.json`, validate layer allocations (L0–L4), data freshness, hard-stop triggers, signal watchlist anomalies, and rebalance calendar. Report findings — never modify.
- loop: resolved/phantom — duplicate claim of trading-infra-watcher job `5a1d4ea6796d`; superseded.
