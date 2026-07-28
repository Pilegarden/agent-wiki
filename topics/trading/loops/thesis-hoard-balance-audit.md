# thesis-hoard-balance-audit

- topic: `trading`
- queue ref: `topics/trading/.system/queue.md`
- status: **active**
- cron job: `1a61890a11d1`
- schedule: `0 9 * * 1`
- deliver: `origin`
- profile: `dev`

## Scope

Weekly thesis-hoard balance audit. Executes the thesis-hoard balance audit script and surfaces threshold breaches. Green runs post a one-line summary; red runs list each failing threshold with current vs target values.

## State

- last_status: ok
- last_error: none
- last_run: 2026-07-27 09:02 CEST

## Notes

Live cron present in dev profile store since 2026-07-17. No pending approval items.

## Loop Registry

- registry: `topics/_global/loop-registry.md`
- rows: `thesis-hoard-balance-audit`
