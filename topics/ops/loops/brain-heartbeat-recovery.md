# brain-heartbeat-recovery

- topic: `ops`
- agent: `ops` (system-level)
- status: **active**
- cron job: `b2d9c7c4e555`
- schedule: every 120m
- deliver: `local`
- profile: `dev`

## Scope

Read-level gbrain health snapshot. Uses `curl http://127.0.0.1:12787/health` to probe the local gbrain HTTP daemon. No admin-scoped tools, no repo mutation, no config changes.

## State

- last_status: ok
- last_error: none
- last_run: 2026-07-28 15:02 CEST

## Recovery Note

Prior phantom misclassification corrected by live-evidence override on 2026-07-25: job `b2d9c7c4e555` is active in `~/.hermes/profiles/dev/cron/jobs.json` and last ran 2026-07-25 04:19 CEST; loop doc and registry restored to active state.

## Output

Compact Telegram summary:
- `[GBRAIN OK]` when `/health` returns `{"status":"ok"}`
- 2–4 line failure blurb when unreachable, malformed, or non-ok status

## Loop Registry

- registry: `topics/_global/loop-registry.md`
- rows: `brain-heartbeat-recovery`
