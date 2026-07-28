# adguard-home-sync

| Field | Value |
|---|---|
| Name | adguard-home-sync |
| Topic | dev |
| Schedule | every 30m |
| Agent | dev |
| Mode | watcher |

## Task
Verify `adguardhome-sync` can still reach `.251` after `.250` reports sync failure or `192.168.10.251:80` connect refused.

## Read
- `.250` `adguardhome-sync` cron failure state / exit code
- `.250` outbound network path to `.251:80`
- `.205` ARP cache for `.251`
- `.251` firewall / `iptables-nft`
- `.251` HTTP `control/status` response

## Write
- Outcome marker: Pass / Fail with exact failure mode
- Remediation notes for ARP mismatch, firewall, or service-down

## Failure contract
- `max_parallel`: 1
- `backoff`: 10m
- `max_retries`: 3
- `pause_on_fail`: false

## Success criteria
- Pass = sync from `.250` reaches `.251` and returns HTTP 200.
- Fail = exact failure mode (`ARP` mismatch / `firewall` block / `AdGuardHome` down), with remediation path.

## Cron Status
- Job ID: 6cf4ddcff112
- Schedule: */15 * * * * (every 15m)
- Name: adguard-home-sync-watchdog
- Status: active
