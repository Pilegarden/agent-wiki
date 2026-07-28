# vault-sync-push-trigger

- topic: `sysadmin`
- queue ref: `topics/sysadmin/.system/queue.md`
- status: active
- cron job: `337fb9ff9a8a`
- schedule: `*/15 * * * *`
- deliver: `local`
- profile: `dev`

## Scope

Lightweight vault push trigger. Script `vault-sync-trigger.sh` is present under `profiles/dev/scripts-local/` and cron state is healthy.

## State

- last_status: ok
- last_error: none
- last_run: 2026-07-28 15:15 CEST

## Notes

Cron state recovered to `ok`. Prior runtime-error (2026-07-25 06:00 CEST) was transient/no longer reflected by live cron store.

## Loop Registry

- registry: `topics/_global/loop-registry.md`
- rows: `vault-sync-push-trigger`
