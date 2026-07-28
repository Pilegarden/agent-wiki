# cron-dependency-monitor

- topic: `sysadmin`
- queue ref: `topics/sysadmin/.system/queue.md`
- status: active
- cron job: `7d390796d546`
- schedule: `0 8 * * *`
- deliver: `local`
- profile: `dev`

## Scope

Cron dependency monitor. Script `cron-monitor-wrapper.sh` is present under `profiles/dev/scripts-local/` and cron state is healthy.

## State

- last_status: ok
- last_error: none
- last_run: 2026-07-28 08:00 CEST (live)

## Notes

Previous runtime-error caused by missing `cron-monitor-wrapper.sh`. Script is now restored; no pending approval items.

## Loop Registry

- registry: `topics/_global/loop-registry.md`
- rows: `cron-dependency-monitor`
