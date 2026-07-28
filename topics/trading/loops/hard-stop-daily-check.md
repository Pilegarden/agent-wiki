# hard-stop-daily-check

- topic: `trading`
- queue ref: `topics/trading/.system/queue.md`
- status: **active**
- cron job: `94c1991eff81`
- schedule: `0 18 * * 1-5`
- deliver: `origin`
- profile: `dev`

## Scope

Daily hard-stop breach check for portfolio positions. Reads `/srv/trading/portfolio.json` and checks all positions with `hard_stop_sek` or `hard_stop_eur` thresholds via the hard-stop-check skill workflow. Reports only if a breach or near-breach is found.

## State

## State

- last_status: ok
- last_error: none
- last_run: 2026-07-27 18:01 CEST

## Notes

Deployed cron. No pending approval items.

## Loop Registry

- registry: `topics/_global/loop-registry.md`
- rows: `hard-stop-daily-check`
