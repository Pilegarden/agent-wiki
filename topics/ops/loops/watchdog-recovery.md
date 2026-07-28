# ops/watchdog-recovery

## Status
**Resolved 2026-07-13**

## Finding
Systemd services `adguard-watchdog.service` and `hermes-dashboard-watchdog.service`
in `/etc/systemd/system` (static) were failing with:
```
can't open file '/home/hermes/.hermes/scripts/check-uptime.py': [Errno 2] No such file or directory
can't open file '/home/hermes/.hermes/scripts/watchdog-hermes-dashboard.py': [Errno 2] No such file or directory
```
Both had corresponding timers that fired every 2 minutes and accumulated 4h+ of failed runs.

## Action taken
1. `sudo systemctl disable --now` both services and timers.
2. Removed unit files from `/etc/systemd/system` (and checked user scope was absent).
3. `systemctl daemon-reload`.

## outcome
No failing watchdog services remain. Timer noise cleared. Journal noise stopped.

## Recovery playbook
- Re-monitor: if watchdogs are needed again, restore scripts under `/home/hermes/.hermes/scripts/` with correct implementations and re-enable.
- Future ops loops should verify `ExecStart` paths exist before enabling timers.
