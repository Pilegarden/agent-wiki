# trading-infra-watcher

- topic: `trading`
- agent: `trading-infra-watcher`
- status: **active** — recovered by loops-factory phantom recovery on 2026-07-26
- cron job: `b5aa5e1f418c`
- cadence: Mon–Fri 09:00, 14:00
- deliver: `telegram:-1004376316450:8`
- model pin: `stepfun/step-3.7-flash:free`
- profile: `dev` (cron runs from dev profile store)

## Cron Details

- **Claimed Job ID**: `b5aa5e1f418c`
- **Schedule**: `0 9,14 * * 1-5`
- **Deliver**: `telegram:-1004376316450:8`
- **Created**: prior to 2026-07-10 (pre-existed loops-factory audit); **recovered**: 2026-07-26 by loops-factory
- **Script**: `/home/hermes/.hermes/scripts/trading-infra-watcher.sh` (`755`)

## State

- last_status: ok
- last_error: none
- last_run: 2026-07-28 14:00 CEST
- failure_count: 0
- max_retries: 3
- pause_on_fail: false
Compact Telegram summary:
- RED: blocked artifact, missing path, JSON parse failure
- YELLOW: sloppy free space, stale deploy marker
- GREEN: one-line OK when all checks pass

## Failure Mode

Profile config issue: user reported YAML parse error on `/home/hermes/.hermes/profiles/trading-infra-watcher/config.yaml`; Hermes falls back to default config. Cron itself remains bound despite fallback. Missing or invalid Telegram delivery path suppresses outbound summaries until restored.
