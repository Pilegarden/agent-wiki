# sysadmin/adguard-dashboard-watchdog

## Status
**Resolved 2026-07-13**

## Finding
System-wide services for adguard and dashboard watchdogs were failing because
the referenced Python scripts did not exist. This matched earlier deferred
ticket about absent-script failure.

## Action taken
Monitoring units removed because monitoring intent is no longer maintained.
If monitoring is required again, restore scripts + re-enable units.

## Planned projects
Create lightweight watchdog implementations under `/home/hermes/.hermes/scripts/`
only if ops decides monitoring is still required.
Dependency: ops/watchdog-recovery decision.
