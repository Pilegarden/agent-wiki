# adguard-yaml-fix

- topic: `sysadmin`
- queue ref: `topics/sysadmin/.system/queue.md` `.200 AdGuard YAML fix`
- status: **draft/awaiting approval** — manual schema fix required
- mode: manual
- deliver: local

## Scope

Fix `!!seq into string` at line 20 of `/opt/adguard/conf/AdGuardHome.yaml` so the AdGuard Home service reaches `active` and `/control/status` returns 200.

## Steps

1. Inspect `/opt/adguard/conf/AdGuardHome.yaml` line 20 context.
2. Correct YAML schema (convert scalar string to sequence/object as expected by AdGuardHome v0.9.2).
3. Validate with `adguardhome-sync` dry-run if applicable.
4. Restart AdGuard Home and confirm `systemctl status` shows `active` and `/control/status` returns HTTP 200.
5. Record outcome in loop doc.

## Safety

Read-only until step 2. Confirm backup exists before editing. Revert on parse failure.

## Loop Registry

- registry: `topics/_global/loop-registry.md`
