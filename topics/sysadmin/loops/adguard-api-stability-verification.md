# adguard-api-stability-verification

- topic: `sysadmin`
- queue ref: `topics/sysadmin/.system/queue.md` `.201 AdGuard API stability verification`
- status: **draft/awaiting approval** — manual verification required
- mode: manual
- deliver: local

## Scope

Confirm `/control/status` returns 200 consistently with configured credentials on both `.200` and `.201`. Verify VIP failover behavior.

## Steps

1. Authenticate to `.200` `/control/status` with configured credentials; expect HTTP 200.
2. Repeat on `.201`.
3. Simulate `.200` failure and verify VIP `192.168.10.249` migrates to `.201`.
4. Restore `.200` and confirm VIP returns.
5. Record any credential or VIP hiccup.

## Safety

Run from management host. Do not modify config. Abort if VIP failover leaves no MASTER.

## Loop Registry

- registry: `topics/_global/loop-registry.md`
