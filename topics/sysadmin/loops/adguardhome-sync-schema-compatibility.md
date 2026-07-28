# adguardhome-sync-schema-compatibility

- topic: `sysadmin`
- queue ref: `topics/sysadmin/.system/queue.md` `adguardhome-sync schema compatibility`
- status: **draft/awaiting approval** — manual schema review required
- mode: manual
- deliver: local

## Scope

Dry-run `adguardhome-sync` fails on both nodes due to outdated schema. Review config schema for v0.9.2 compatibility and test `.200` → `.201` sync.

## Steps

1. Capture current `/opt/adguard/conf/AdGuardHome.yaml` plus `adguardhome-sync` config.
2. Check feed schema version and adapter keys against v0.9.2 changelog.
3. Update config to compatible schema (or pin compatible version).
4. Dry-run sync `.200` → `.201` and inspect diff.
5. Run live sync on approval and verify `.201` accepts new config.
6. Restart `.201` AdGuard and confirm healthy.

## Safety

Review schema changes before applying. Maintain backup of original config on both nodes.

## Loop Registry

- registry: `topics/_global/loop-registry.md`
