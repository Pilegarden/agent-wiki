# keepalived-vip-failover-test

- topic: `sysadmin`
- queue ref: `topics/sysadmin/.system/queue.md` `keepalived VIP failover test`
- status: **draft/awaiting approval** — manual test required
- mode: manual
- deliver: local

## Scope

Test VIP `192.168.10.249` failover. VIP currently on `.200` MASTER. Simulate `.200` failure and confirm `.201` takes VIP.

## Steps

1. Verify VIP is on `.200` (`ip a show` / `keepalived` state).
2. Stop keepalived on `.200` or take interface down.
3. Observe VIP migration status on `.201` (`ip a`, `tcpdump`).
4. Restore `.200` and confirm VIP returns.
5. Log latency of failover.

## Safety

Ensure at least one MASTER remains. Coordinate with any active AdGuard traffic. Restore quickly.

## Loop Registry

- registry: `topics/_global/loop-registry.md`
